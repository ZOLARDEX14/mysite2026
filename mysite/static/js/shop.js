// Storefront Client Logic - TTT Shop
document.addEventListener('DOMContentLoaded', () => {
    // State variables
    let cart = JSON.parse(localStorage.getItem('ttt_shop_cart')) || {};

    // Elements
    const cartIconBtn = document.getElementById('cartIconBtn');
    const cartDrawerOverlay = document.getElementById('cartDrawerOverlay');
    const cartDrawer = document.getElementById('cartDrawer');
    const closeCartBtn = document.getElementById('closeCartBtn');
    const cartItemsContainer = document.getElementById('cartItemsContainer');
    const cartTotalPriceEl = document.getElementById('cartTotalPrice');
    const cartCountBadge = document.getElementById('cartCountBadge');
    
    const productModalOverlay = document.getElementById('productModalOverlay');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const modalProductImg = document.getElementById('modalProductImg');
    const modalProductTitle = document.getElementById('modalProductTitle');
    const modalRatingStars = document.getElementById('modalRatingStars');
    const modalSalesCount = document.getElementById('modalSalesCount');
    const modalCurrentPrice = document.getElementById('modalCurrentPrice');
    const modalOriginalPrice = document.getElementById('modalOriginalPrice');
    const modalProductDescription = document.getElementById('modalProductDescription');
    const modalStock = document.getElementById('modalStock');
    const modalLocation = document.getElementById('modalLocation');
    const modalQtyInput = document.getElementById('modalQtyInput');
    const qtyMinusBtn = document.getElementById('qtyMinus');
    const qtyPlusBtn = document.getElementById('qtyPlus');
    const btnAddCartSubmit = document.getElementById('btnAddCartSubmit');
    const btnBuyNowSubmit = document.getElementById('btnBuyNowSubmit');

    let currentModalProductId = null;

    // --- Search & Filters UI Helpers ---
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');

    if (searchForm) {
        searchForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const query = searchInput.value.trim();
            const params = new URLSearchParams(window.location.search);
            if (query) {
                params.set('q', query);
            } else {
                params.delete('q');
            }
            // Reset category when doing new search
            params.delete('category');
            window.location.search = params.toString();
        });
    }

    // --- Initial setup ---
    updateCartCount();

    // --- Cart Drawer Event Listeners ---
    cartIconBtn.addEventListener('click', () => {
        renderCartDrawer();
        cartDrawerOverlay.style.display = 'block';
        setTimeout(() => cartDrawer.classList.add('open'), 10);
    });

    const closeCartDrawer = () => {
        cartDrawer.classList.remove('open');
        setTimeout(() => {
            cartDrawerOverlay.style.display = 'none';
        }, 300);
    };

    closeCartBtn.addEventListener('click', closeCartDrawer);
    cartDrawerOverlay.addEventListener('click', closeCartDrawer);

    // --- Product Cards Click listeners ---
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('click', () => {
            const productId = card.getAttribute('data-id');
            openProductModal(productId);
        });
    });

    // --- Modal Event Listeners ---
    const closeProductModal = () => {
        productModalOverlay.style.display = 'none';
        currentModalProductId = null;
    };

    closeModalBtn.addEventListener('click', closeProductModal);
    productModalOverlay.addEventListener('click', (e) => {
        if (e.target === productModalOverlay) {
            closeProductModal();
        }
    });

    // Quantity Adjustment in Modal
    qtyMinusBtn.addEventListener('click', () => {
        let val = parseInt(modalQtyInput.value) || 1;
        if (val > 1) {
            modalQtyInput.value = val - 1;
        }
    });

    qtyPlusBtn.addEventListener('click', () => {
        let val = parseInt(modalQtyInput.value) || 1;
        let max = parseInt(modalStock.textContent) || 99;
        if (val < max) {
            modalQtyInput.value = val + 1;
        }
    });

    modalQtyInput.addEventListener('change', () => {
        let val = parseInt(modalQtyInput.value) || 1;
        let max = parseInt(modalStock.textContent) || 99;
        if (val < 1) modalQtyInput.value = 1;
        if (val > max) modalQtyInput.value = max;
    });

    // Add to Cart from Modal
    btnAddCartSubmit.addEventListener('click', () => {
        if (currentModalProductId) {
            const qty = parseInt(modalQtyInput.value) || 1;
            fetchProductDetailsAndAdd(currentModalProductId, qty, false);
            closeProductModal();
        }
    });

    // Buy Now from Modal
    btnBuyNowSubmit.addEventListener('click', () => {
        if (currentModalProductId) {
            const qty = parseInt(modalQtyInput.value) || 1;
            fetchProductDetailsAndAdd(currentModalProductId, qty, true);
        }
    });

    // --- Core E-Commerce Logic ---

    function openProductModal(productId) {
        // Reset quantity input
        modalQtyInput.value = 1;
        currentModalProductId = productId;

        // Fetch details from django API
        fetch(`/quiz/api/products/${productId}/`)
            .then(res => {
                if (!res.ok) throw new Error("Product fetch failed.");
                return res.json();
            })
            .then(data => {
                // Populate modal content
                modalProductImg.src = data.image_url || '/static/images/placeholder.png';
                modalProductTitle.textContent = data.name;
                modalSalesCount.textContent = data.sales_count;
                modalCurrentPrice.textContent = `฿${parseFloat(data.price).toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                
                if (data.original_price && data.original_price > data.price) {
                    modalOriginalPrice.textContent = `฿${parseFloat(data.original_price).toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                    modalOriginalPrice.style.display = 'inline';
                } else {
                    modalOriginalPrice.style.display = 'none';
                }

                modalProductDescription.textContent = data.description;
                modalStock.textContent = data.stock;
                modalLocation.textContent = data.location;

                // Ratings
                let ratingHtml = '';
                const rating = Math.round(data.rating);
                for (let i = 1; i <= 5; i++) {
                    if (i <= rating) {
                        ratingHtml += '★';
                    } else {
                        ratingHtml += '☆';
                    }
                }
                modalRatingStars.textContent = ratingHtml;

                // Display modal
                productModalOverlay.style.display = 'flex';
            })
            .catch(err => {
                console.error(err);
                alert("เกิดข้อผิดพลาดในการดึงข้อมูลสินค้า");
            });
    }

    function fetchProductDetailsAndAdd(productId, qty, redirectToCheckout = false) {
        fetch(`/quiz/api/products/${productId}/`)
            .then(res => res.json())
            .then(data => {
                addToCart(data, qty);
                if (redirectToCheckout) {
                    closeProductModal();
                    // Open cart drawer
                    cartIconBtn.click();
                } else {
                    alert(`เพิ่ม "${data.name}" จำนวน ${qty} ชิ้น เข้าตะกร้าแล้ว`);
                }
            })
            .catch(err => console.error(err));
    }

    function addToCart(product, qty) {
        const id = product.id;
        if (cart[id]) {
            cart[id].quantity += qty;
        } else {
            cart[id] = {
                id: product.id,
                name: product.name,
                price: product.price,
                image_url: product.image_url,
                quantity: qty,
                stock: product.stock
            };
        }
        
        // Ensure quantity doesn't exceed stock
        if (cart[id].quantity > product.stock) {
            cart[id].quantity = product.stock;
        }

        saveCart();
        updateCartCount();
    }

    function saveCart() {
        localStorage.setItem('ttt_shop_cart', JSON.stringify(cart));
    }

    function updateCartCount() {
        let totalCount = 0;
        for (let key in cart) {
            totalCount += cart[key].quantity;
        }
        cartCountBadge.textContent = totalCount;
    }

    function renderCartDrawer() {
        cartItemsContainer.innerHTML = '';
        let totalPrice = 0;
        let hasItems = false;

        for (let id in cart) {
            hasItems = true;
            const item = cart[id];
            const itemTotal = item.price * item.quantity;
            totalPrice += itemTotal;

            const cartItemEl = document.createElement('div');
            cartItemEl.className = 'cart-item';
            cartItemEl.innerHTML = `
                <img src="${item.image_url || '/static/images/placeholder.png'}" alt="${item.name}" class="cart-item-img">
                <div class="cart-item-info">
                    <h4 class="cart-item-title">${item.name}</h4>
                    <div class="cart-item-price">฿${parseFloat(item.price).toLocaleString(undefined, {minimumFractionDigits: 2})}</div>
                    <div class="quantity-control" style="margin-top: 6px; scale: 0.85; transform-origin: left center;">
                        <button class="quantity-btn dec-qty-btn" data-id="${item.id}">-</button>
                        <input type="text" class="quantity-input" value="${item.quantity}" readonly>
                        <button class="quantity-btn inc-qty-btn" data-id="${item.id}">+</button>
                    </div>
                </div>
                <div class="cart-item-actions">
                    <button class="btn-remove-item" data-id="${item.id}">ลบ</button>
                </div>
            `;
            cartItemsContainer.appendChild(cartItemEl);
        }

        if (!hasItems) {
            cartItemsContainer.innerHTML = '<div class="cart-empty-message">ไม่มีสินค้าในตะกร้าของคุณ</div>';
        }

        cartTotalPriceEl.textContent = `฿${totalPrice.toLocaleString(undefined, {minimumFractionDigits: 2})}`;

        // Bind events inside drawer
        bindDrawerEvents();
    }

    function bindDrawerEvents() {
        // Remove item buttons
        const removeBtns = cartItemsContainer.querySelectorAll('.btn-remove-item');
        removeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.getAttribute('data-id');
                delete cart[id];
                saveCart();
                updateCartCount();
                renderCartDrawer();
            });
        });

        // Decrease quantity buttons
        const decBtns = cartItemsContainer.querySelectorAll('.dec-qty-btn');
        decBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.getAttribute('data-id');
                if (cart[id] && cart[id].quantity > 1) {
                    cart[id].quantity--;
                    saveCart();
                    updateCartCount();
                    renderCartDrawer();
                }
            });
        });

        // Increase quantity buttons
        const incBtns = cartItemsContainer.querySelectorAll('.inc-qty-btn');
        incBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.getAttribute('data-id');
                if (cart[id] && cart[id].quantity < cart[id].stock) {
                    cart[id].quantity++;
                    saveCart();
                    updateCartCount();
                    renderCartDrawer();
                }
            });
        });
    }

    // Checkout Action
    const btnCheckout = document.getElementById('btnCheckout');
    if (btnCheckout) {
        btnCheckout.addEventListener('click', () => {
            let totalCount = 0;
            for (let key in cart) {
                totalCount += cart[key].quantity;
            }

            if (totalCount === 0) {
                alert("ไม่มีสินค้าในตะกร้าสำหรับสั่งซื้อ");
                return;
            }

            alert("ชำระเงินสำเร็จ! ขอบคุณที่อุดหนุน TTT Shop");
            cart = {};
            saveCart();
            updateCartCount();
            closeCartDrawer();
        });
    }
});
