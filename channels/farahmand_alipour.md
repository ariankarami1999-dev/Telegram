<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/NQvxoefCyNHsxAdMFoSUUiQn7dEeOULtu6x-5LPzHeJdXXyQZOgefg67Ms2O7RIY8CAwShz_XwFsHCKkJrAnComUeu6E4hGArWatRH6gkx-peJm1iCfldMTsfQ1xONhjhfj0XSe0OuTCwRlE4XuMblB_XxQBLJ0EQb_HcVCqJ0pzhbxe0gFtQg8F2ktWG1vPJdmRm71z_fCqY7bS-zRxQcJy4FDBjINU88YQhvyloydKF1ndIUN6SphBt0rSEkxIlRF-609khjJ00THT-X9eC-H4pUIH6k5K0_KBc9OPTtP5oIlDK2Rovcycf7IpvZF-VEng0oMzpfQYAf1_j6mZpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 00:18:01</div>
<hr>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnIbP8ejH5EkEjLaZbDouVOn5nxl2_FuX92tuIF9reaQvmv1YMg1xfE-RHaqyX_NRlOtjFPkCf7bMaOcLwMrb-a01cK4qkocgKADBrEWorHIZ9eIQu5yQte06lH1nPWM5607Wc0YRGnHVpvBI3cnN8PfaIML8bbEaIc_oYq1yM6Y7yNpfyLglPIZLPshw71K3hRe0aQrLHsiGpQ-eLvzftv_m8qt8QDBf7aFnRnddq7BN8i7TcRSxhOF7AZ_bTAYdW2esIjXcyugYTNFXERNyNovuTwnusGm5nquff3lg63blHgULwlG_8B3II98wBQnyUspQiA39qLrEsml8ib2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY99gAqmpfiE2H5fH1NbbcJdbCNKU1rLFCr6H-ZPrh-jxzqYliRgE_9fKPG3oPjiT1tUqu-sZ4yegwnJrr2FQCS2xG75FeV04OPOXvb0i0nP932ie1QqKYbDKygi_JNHPkVqncZoIp1Pp2yunnGYmjnSotn78rLxXn03YY4G3JJtYF_Yl1pG2vfr6KkuWpsfMc5SV6yRxXGFd-ZErHFnGPyTO4TxIxFJ_iPgJPq4MX6gwxgHr1Re6YmWMjEFswPjZW06wXgIdnItb_BpRVBz7EU-yxhs37xMI9jOcgzHm_TV4ucJbeALFQrhKE9SrLAlpi25jB_RByDQwjrfyV7V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHvkA2-Dj3tUl7FSvylFdSQv1bck_z2znJ81R_9TNImi1dwvK0N2dWN5M56XZWuNR5KL5eI5XaEDVKGzKqItANR5uJrx4hbjT8scl1Lmok_dU4vhXqdGk9qcAfGiB1VI14dE7nuDIL5xZ2u6DQ1Gc7G_D0_rsVZ8mDMBuYh_Yu_BwV88LSnYq1WdoBNwKgbOEQ6dR3peSyeszuo51UmWBQidFKy_ojrdPwyKns9-64bCparJVEHjh77Fi9k2InkzmelO0vfVUQY5Gh3Yh5x1DtPJPdF6BiUDisG6cnvgGzr2eyesoQSEQFrpwOjFSaq7Kgbf3kpN-C9XLD5N13jIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDLAmLMqntkWAq4FiR4rftfLoSrCB-Y0gRVwASiMkYwNmoN2HtxDA0h8969Q0pEz_yXE7XzwgA5cLy6SaDdKIfxpFHBUf-xm_fLJuAFGfwfnfuBtAm6qT3sAn_7nG2oWl8Ps6hcnCji2nWrX9YCk4NHDb9jq104sfye91pbNRCGfdiDo8nw60xfPsjiyMRNmnoadADlvppFLNLvyEjcQYOTLgthuVpMbhEu2qM8T-49_H9GV_k7abPe_wHF_QCDpzBBv2KZBef1XQigbehFX6sle8iA0FOBoRwZvebejUFfjyRkLQgUaS1JLl1LnPZHsKJqCUT7aIiVbxdAtXC__6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPPFuosB7B7NFMW16cRyhpD1360JavBG1BGsedE7lpypkZRH_ZFvDygBxjP3004LCec-rW2D4tSGiZlt4AZPh4oLTAaDtDotz6us-ts3TVg0GKzWD88fJ6Cvr-2LZmQI6TSRpnXKh29pk0rjKkNXuo6tECw_pTr1xbjadXymp9R0Rqb0re-_mMHA1FGWxR-ut7-Y8pc4qDQUhHQZ1AfZBWlhKzNBgPKY2VTqMcMUI0_uF9zpL7svUdL6Gfn9988RfR3Vc-hKOhPW1nl4xVaoVKZ0wZrXL6zEJb02r5eqF8apy6bTWxld5hAhypgb5P5ISYWeBoLeEIl8t63iISMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAg4d9m3z2fildsIFEeiF_hxvaCXPfhNuCe1kpgf1CtsIur_c-10yLssnoGsAllr2txX8Nib4gl_bmXHLlYsoE8DRgsrRPiOi5bQYoL93M_dD0Y55vS8FEPD1owpetQ_0CjpnrOS0mQYM3BQ8CxxuzZ1hbZWo2lLCeJgirtWh-xTdJa2CmkLOHWI4PDleBXQzSy5k1YrQua53DMGPzzPoKsiXdubji8yv5sGS7Ji5gqpPYEb2E-p6oeJYhy3Lt61pNJkUaoWiD59zolz3i0JNUAVrR2dnWuuz1Gcab5haxgivDgnbky6PqOoPmHg3_kDRvh3CaK3TAOvMDanjGdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1734ESwsqR2o5BfnS3oqPFzI_AM7D9UotvMeaNmmjDKK4H04dH8YztKNgBT-0Q5MarEpOhBSYlxJuZmatt1OlKfKrrswm7XGShks5gbHiaga3G41Pmsh3X1EQgBGwVwxJuEBniWmEWfJlEwnIY2CrnbHdERtBwPhhhhVSMXJUxZc7yDMwlGhkrwvsCwJuK1Zl5xUtZiuCDsJ75LbVvu1Nri55Wy13HJU9R0t9NNMMyPB7z5oCbKMWbsPuvPufs8fI7f4TSaPPhE7mAhzFlIxR4hiQoHXnj57gMwZ0MVYytEufX5TrBo1OkVLlzF6-eXBq42lL5hqHIHf61zuJUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg9UrjkJUsJkot8EOtdanfFoBF-KAJOxXJX1hUv-2uWDUIeNIQaKdskVhAraneTbP7JL0EMcSbvVGtP8Y8WMkXgepV-I22IXgSLxd3ptcfZ0XIE6Cu_Xk7KfLxipqgL-zZRZd5s6FYoTS2sUOt8t_ghSY6bRkg3HfTtKIqHcCWtKPegkzEfRe3vBUq8n13QsGFzZ1m1dpTCz24jflgdowjSPtiz3s23AxOEcBHKBwd8MZl2jOz6by0wIDtMT2d1io3Ueuo8uhXS9jsfvxuWuhMHdIc-xh3uEOP_DmYeeow6Dc6uMHzVclCFPKoBWB9NCCWq8Ito7-_5GLypEXGFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=uYOSZSP4UegxOSpFFzOtU7lQ9tk0HR0vvESAhbA0MU2cLbuEx1iBff13JmGK5R34H9gXSQ1mDifivUZkyX7ZSuhx2bvCX6ho2HimWf35CT2ioS9ktXnmLfOOUe2-a47TOuCzqu7FebVJWIcYZ6uGUR907PQ5KlKXqUZKzsXEzIihIusVozD7TVdS4iDrDNPdeQLzIq4iegMJClNAEkRm-931-03dVF4txt50ebLPTH3cSGQPsHbNJmITxECJUAL8zSmbFR9e_fjBCG2MSStRXC9bJINYwo5j71eySjnCb3qoQo9lgBzmzcgPR6c1xxNCLFXlCw-O1GEmbqWPiHab0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=uYOSZSP4UegxOSpFFzOtU7lQ9tk0HR0vvESAhbA0MU2cLbuEx1iBff13JmGK5R34H9gXSQ1mDifivUZkyX7ZSuhx2bvCX6ho2HimWf35CT2ioS9ktXnmLfOOUe2-a47TOuCzqu7FebVJWIcYZ6uGUR907PQ5KlKXqUZKzsXEzIihIusVozD7TVdS4iDrDNPdeQLzIq4iegMJClNAEkRm-931-03dVF4txt50ebLPTH3cSGQPsHbNJmITxECJUAL8zSmbFR9e_fjBCG2MSStRXC9bJINYwo5j71eySjnCb3qoQo9lgBzmzcgPR6c1xxNCLFXlCw-O1GEmbqWPiHab0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=pe4EDJ_GBQCHO5OPVkhlfq9M1_37ymsdulJ-gRbf20W0YWO6lNzuf28c2tBk6kKXhc0Uys4Njz1lKt5ohUC1vq3GssPpFqGvZhi0xinJGBn8dN67G1S_JdJjsdjVDOFhhSK1EPoAJonI4YvsK0Qz0znirkFJpih4jWVMHh3yWpUswrpeVar7yVag-0MZNMEJAkp2r_QShAdKtsYhkAcwPGTpU6o5AvATxd9aWWszJB6VvDAf9Hn3H9FSXevUlgkZxfzjFXsW8JwttQWByAWQgHYfRVUjisfcfQyUD-b-ngGGS-F8KBYWPbOpgxt5u161m45JBFk627Z52d3F_eByAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=pe4EDJ_GBQCHO5OPVkhlfq9M1_37ymsdulJ-gRbf20W0YWO6lNzuf28c2tBk6kKXhc0Uys4Njz1lKt5ohUC1vq3GssPpFqGvZhi0xinJGBn8dN67G1S_JdJjsdjVDOFhhSK1EPoAJonI4YvsK0Qz0znirkFJpih4jWVMHh3yWpUswrpeVar7yVag-0MZNMEJAkp2r_QShAdKtsYhkAcwPGTpU6o5AvATxd9aWWszJB6VvDAf9Hn3H9FSXevUlgkZxfzjFXsW8JwttQWByAWQgHYfRVUjisfcfQyUD-b-ngGGS-F8KBYWPbOpgxt5u161m45JBFk627Z52d3F_eByAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxLqeP6NfD-G3LnEWSAAOCawStuFP-ceQa_eQ_aaJzhWjxaWipVwIp77cr74LO5Qc8B64kM8to0aTx1f6xIZ5Qd3mb-IX7RWgfHBjPKGPlzvdgNZI7J4mKTmfrCnvrf7LDgP-qfhAc6e4Nr_uL7nBQREg5rK4w2acOvD6TKJLonSsNVsC7MZC5kgwGvu9Xyw7kCRwpRLzzX7YO5kO0_1vXfl-M9BB6_op7k3IvT1X-O1vDY3Uur3Pdwln5mU1ezqULgCM8WmHBP-KFrCbUdPub7v_P_zRKF67_sfqRNxDKrweaMeAo_zIDkopVquyA5mu8YQ-rpkNp4TWqTce_Zy0LKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxLqeP6NfD-G3LnEWSAAOCawStuFP-ceQa_eQ_aaJzhWjxaWipVwIp77cr74LO5Qc8B64kM8to0aTx1f6xIZ5Qd3mb-IX7RWgfHBjPKGPlzvdgNZI7J4mKTmfrCnvrf7LDgP-qfhAc6e4Nr_uL7nBQREg5rK4w2acOvD6TKJLonSsNVsC7MZC5kgwGvu9Xyw7kCRwpRLzzX7YO5kO0_1vXfl-M9BB6_op7k3IvT1X-O1vDY3Uur3Pdwln5mU1ezqULgCM8WmHBP-KFrCbUdPub7v_P_zRKF67_sfqRNxDKrweaMeAo_zIDkopVquyA5mu8YQ-rpkNp4TWqTce_Zy0LKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjdDKsZkH58h5mTjLQMREdqsmjlaKElCvWDXht6vU_fSr-pD24d2S005P2_ZwnXpbgQ7q0iR0ll3wBhgvNQLOGvRI6yFeczxjVXnSyf42wXMTkSrhE4LMWrGOV1HgXn5IBzQl8eASXPx89TKyYABsRHoGaSIROGU9chD3yVMRQBdbnWBQ7omkY83eP5rs7FkI9tBbmQoPInRsyaPa5sBR_J82gsuqkDnDgJDc88q34v616hsUgPHzf_5ZDAAV7fFV9USRaezhgE3WtFDIc7b6MeC7jz_8n7VOI_Vfb5irWNjVoLUU8klXNBfJtUpiMIuyrbnZgtQXs4Ze_FBqiu2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad1M5mf56tyAGWpMOYGO2WuBxSDtYCX7T4EnPlkwv-wezICg-MKkTGwYIBYF377Y9Cttz9H1Sm87DVGuHpzh4e2AtTUj0ECW631KX-4FxCvzvaNLubI-rTxsYSnFg9FT1-SCdlIsR-PiQ4l4vMkCDupqBbbzoCcdCC5Uxpz-5SJ0SGgR3zO2Ib_8a2VHyUgchPLO0djDlL6JWjePV8XSZkC2nu_tmnjgGvHRKBtxtglovjLN5VMcSEaGAxy0m1Gg0OHT0QrDuSnDcEDKfKTVA5kWc9jZQPuiSDKg9yPOd13nnbWQnDMSZHFIB47KNZpjI6PKmtz2cRx5Rm7Vmporhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=efa45G3KEZT0v-OKRfofgE3kLiVh6dX8bpXgn2rlzS539_JYYxGr9czYowf4A01gapU2WxGaTeIlkwq_8a8oT4zGoglwhKZmB1Njq54A2nu2Kxjmywvvnay547n8XYr30TEyZXi7J0XAj9yBKMD_gTni1tph3lC7dbZQ8B-iJ4MB3l59tOJq6f9VlEvo2vPcYD6PTz4zi3oG9nhZNcqHDZmWZbvgJ31P-KCfytxCiHpKiOWtuREiJMpMGQ5GfcQrBCYlKsAgvkVkJTS7le6RF0W1U4dVpkbMq76dW5Gg7GmekzKgsceCkuNMY0kleKuycUIxFaLSklSNunDyTuWVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=efa45G3KEZT0v-OKRfofgE3kLiVh6dX8bpXgn2rlzS539_JYYxGr9czYowf4A01gapU2WxGaTeIlkwq_8a8oT4zGoglwhKZmB1Njq54A2nu2Kxjmywvvnay547n8XYr30TEyZXi7J0XAj9yBKMD_gTni1tph3lC7dbZQ8B-iJ4MB3l59tOJq6f9VlEvo2vPcYD6PTz4zi3oG9nhZNcqHDZmWZbvgJ31P-KCfytxCiHpKiOWtuREiJMpMGQ5GfcQrBCYlKsAgvkVkJTS7le6RF0W1U4dVpkbMq76dW5Gg7GmekzKgsceCkuNMY0kleKuycUIxFaLSklSNunDyTuWVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYF-RVjXIjux2K8d738GUybbVqxyI6yO_AI7d5Rc5ep_mbPlrvEQPTuklxQUQL5-4mzYKH_EPgIZD1SUG1lVxeXkS-L8iRXCreWIdWicS3-7VQK4wfCnef7X3SaDQrbIntUktIK7bNMSr9T1SOxp7EDhXQw57gwu2T0pg-D2oqrShXpuWOeFcw0rkSXyvwaEIoj65mgvOoyodXBiKVAW1lZYbBalQLrYLXzItxFcL3Dq3DlHBED5u9vGpnElZKMT_6nW9VwIT75tA6rnpHL3pfVNG0cEJmjh8Azjhch1sbo5RMa9WoLCjXtCTbhP3RdjFw4KkF1zxGF-ufxWZGEO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=iZzoiLIRS98HbXSQa6Us9z0ElxL2bKTJm9cSGoPOkWtp2xUNyNQNXaOdItsLGFPIg6X8bFGBWv51WA-bgiiS9CLNnacsEOeC5qxLBnubNuytr3gSULL6_DOvLsK8XajPU6CI5efXpFD8ClrD_0NorsejQxV6XbEKLH8K2Asq-FSTPCe4uat22jCowUj0SAF3a85aHQVcepezyG9R5QsY29RBsgX00uQm2c4a9QnRJA8oqTKKYanN4IaeoZ4_jpPh8sUsvK5dKXo0kTRGuYMH0ac4TOgdRroizxLC0oxrrU5zsJj_MeIZfrhqs-aUmwWwgQhhbh6lmeOMs29Lctp6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=iZzoiLIRS98HbXSQa6Us9z0ElxL2bKTJm9cSGoPOkWtp2xUNyNQNXaOdItsLGFPIg6X8bFGBWv51WA-bgiiS9CLNnacsEOeC5qxLBnubNuytr3gSULL6_DOvLsK8XajPU6CI5efXpFD8ClrD_0NorsejQxV6XbEKLH8K2Asq-FSTPCe4uat22jCowUj0SAF3a85aHQVcepezyG9R5QsY29RBsgX00uQm2c4a9QnRJA8oqTKKYanN4IaeoZ4_jpPh8sUsvK5dKXo0kTRGuYMH0ac4TOgdRroizxLC0oxrrU5zsJj_MeIZfrhqs-aUmwWwgQhhbh6lmeOMs29Lctp6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Z4cXtuSlHQPo3XxSunDpDcsWfHdduiphMZPtJA3r4wHFO0V5PbqW45gygHtpGoW72zAKir3YT7MMOFtFGyF5C7aHQFbjFuCQYKLukp7kMj2WQg-slpofLYVax12hxroOWWslF11rj6mdP36NO11psOJgw4zMpXpy7oJSw4DkK6fLqJQb3CQo_-bZgdp4EyRx8lp2BxhumTC_NfZY1E1NOiI6gawVXsAt0ez0VxM37naxPeE4QPguOhEz7Tc47C-GmXgPcN4Vy67n7saNN_Abv-ZROzCq3C-Q_WRe30xoGAzaVD1RlP6bEpjoz8JzNvdeJp51ZesCZRJhSg3aIDu33w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Z4cXtuSlHQPo3XxSunDpDcsWfHdduiphMZPtJA3r4wHFO0V5PbqW45gygHtpGoW72zAKir3YT7MMOFtFGyF5C7aHQFbjFuCQYKLukp7kMj2WQg-slpofLYVax12hxroOWWslF11rj6mdP36NO11psOJgw4zMpXpy7oJSw4DkK6fLqJQb3CQo_-bZgdp4EyRx8lp2BxhumTC_NfZY1E1NOiI6gawVXsAt0ez0VxM37naxPeE4QPguOhEz7Tc47C-GmXgPcN4Vy67n7saNN_Abv-ZROzCq3C-Q_WRe30xoGAzaVD1RlP6bEpjoz8JzNvdeJp51ZesCZRJhSg3aIDu33w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=Urcl1xEDZnGy3_UzlHnQhC77_4uoYClTWlZqbndRO50VjNNXKfxTsynI6qCK8MmYIPFxwuKxFYDoKZPD_3b3Blb98XQpg4KT4vsYxYjR98XbtnbWFngxTFsP0gdQDv8Bb8Fw1YsOooBlmIJFVB07Tfey0hKwcIt3tdcBpCkaQvtbKuwn87UDkX0CcyoVjj1s57wsJ9aqgNt7tVyMq3TdHWKnPYrOLL3VrcTJmRWDRYVwmrVJ5RSL6g17tMpkW4_299O3UVQlxU3NHbdAXgLqPcQ0PpG16nvNW6aWchs_wMkGzt3ZGUv-5e19Osl7jvVWb7fmRh6C5drim3imWRoONA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=Urcl1xEDZnGy3_UzlHnQhC77_4uoYClTWlZqbndRO50VjNNXKfxTsynI6qCK8MmYIPFxwuKxFYDoKZPD_3b3Blb98XQpg4KT4vsYxYjR98XbtnbWFngxTFsP0gdQDv8Bb8Fw1YsOooBlmIJFVB07Tfey0hKwcIt3tdcBpCkaQvtbKuwn87UDkX0CcyoVjj1s57wsJ9aqgNt7tVyMq3TdHWKnPYrOLL3VrcTJmRWDRYVwmrVJ5RSL6g17tMpkW4_299O3UVQlxU3NHbdAXgLqPcQ0PpG16nvNW6aWchs_wMkGzt3ZGUv-5e19Osl7jvVWb7fmRh6C5drim3imWRoONA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=cnADBJsWd4hsXusgMbpM4oVWpPeu_BmQGiOVqzcBYZjs_MvloogDZ-mSeA7RI05O3VaNxTi3Do0ME1nVQbgNovkus6PJY2cezoWvWAn2BRp6K4A8Ec_H6K1aPeyuiOmR9gBAMfddzFGQHz1ziecMBpeYKZjemDncpo1C4FMRUbtiIJg5pp9_RQMEw172omlmuQGXHB6_SZgvHlvJ6d0ETCbzqUEmjXLKHHt5KtrrBDDFIWfXAqE3MqX-M1Ew8QRHgEkwwm9HLgpPtRBIZAZRNrYMrflkXKMLOg2qkxqNB5uEi7VOhRlGd0ZeSf9QLcRZwt-VRFvauw0SGeleobTGzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=cnADBJsWd4hsXusgMbpM4oVWpPeu_BmQGiOVqzcBYZjs_MvloogDZ-mSeA7RI05O3VaNxTi3Do0ME1nVQbgNovkus6PJY2cezoWvWAn2BRp6K4A8Ec_H6K1aPeyuiOmR9gBAMfddzFGQHz1ziecMBpeYKZjemDncpo1C4FMRUbtiIJg5pp9_RQMEw172omlmuQGXHB6_SZgvHlvJ6d0ETCbzqUEmjXLKHHt5KtrrBDDFIWfXAqE3MqX-M1Ew8QRHgEkwwm9HLgpPtRBIZAZRNrYMrflkXKMLOg2qkxqNB5uEi7VOhRlGd0ZeSf9QLcRZwt-VRFvauw0SGeleobTGzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTYfnKUK6KMBH4iF83aJoLQ2TIZdyAg5CYcgxsgJNxIN6G5MrtuooNZDVKPe48YFtNqCtbWtXDKfLWoJ12L9vHd3Rq3OAnXw1jMWcJa35kDmoMDEY7h1HApVSsQDZUwsWvlwvczCH3loL7PNYv7IddXO3OyBJYs8ooG9CbLoZXMG5T5d1RYtUeiRlHCZslfPi4z6LJQFUt1UDn0LHhD3fQgKiZFyG_92jo2Vd0fk6ZhxXwrXOLvhe-kwSWLeunDKHSEuqdE2EoiOa0oMeSvdHOxteK0A_anHQip2eKfZ1Dq1ASaysM3W2hlj8eB01qAPEMd3OONhByE7jcLYfyi_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGvzINrgoayAekYcR6GI-S3GvqyYelm7u55AxPAg8nJMmwOi8QfDTQSYEojGAjKHL9O62efoqAnl5rXXMPWDg4ErNS79PaohpuUTw4fKgQtKj9kfGruKC2eSjND7g9qJtiqpC1HWVP_Ly5rfZKN5U1xJh5oijtN6exgUv5rboU0dNpGpuMa_ZtY9aAQGUdvYkI-NMUir8zUWsWwvanZHnlr3Df-47ATtjjxHBwfRb-NkHmKcwnlZKMUkTIX_MV611ofnEDg2Kc7cVi1tmlU0EER7oSkeGRfikvpQNiRjJ-weMFAdUwhn2ScmLRhS4L6LIuBv9NKgw_fj6rIV2XkncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVv3PQGhATzfYqVnBd8Vc0_l6HlJjter48kiRRyuFv_IDxco6w46Whx4jj0u8rgi6BrqY3ip19l-ui-rT0AyOXUdErCDw1WtPVn8_NxTTOPForY2pOBBgiEnf8iO8FxWd3M1tban38HEQ1tfP66DSH3JYQF42O0nvOkovzRWiZqqISiFwZb2Euvty1M-jXrXF8JkdpHiIqE5apE1ZbDrE8wUkNhv7TtG8l57f49JtVvxCBP_hs5Ate7ZK9064hYTdmEo8pDw9bEacnZ1SjjhTPK-krSsNggNul0hYtgaTsYhNu8S4cRJe5O6rrnrIDsYSFBzmY145XKIkKhRZh03CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw9K94GxG7NGaZpjGjbgKGmNcBzHKrbPDw_ji1kc1PAtMLr4XaHt9xP5ft4Il2ziBPvN-Eb49fwDmj35bGJIAeAbf-1w7bOsWCRz9MJFs8LizWOlxdkDQHTVykscaCqj3xRH6-Hxa3HzaF2yNfczDaIZyFxyuyRPSTGMCTPSGxNAUtXctiU7YsElDPKa10ZLJ9WabBjn77ynl3xjTnaH7zquSY7lI2kF05QPg1Dbj4bj3C3pJxEGUX-sP1zPufaUTPjUIkuDoQ-XEgra6NLq7TnEoN6jye6bhdcnEvASQor55UFo1qQ1V2tWlH0JUMBlA_I3X3duYj1b7BSWtEkGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5wUJGqDNnrcoVDlcxI9Zwlh7k5hVNrFDzCcbEr9RC1eNhCIXEPOG_ECe5Jrb-bQkyYRbO_67ls5IV_9p5VGupaXor8NHOrjDQjO4105_2K1SCpxWglNUeOgEREPXSHDllC1ipvEzv0IoBlVzH9MhN_kruTvaLf34OLDNUd-l_9qetDrtAbRnm8aUVDTt_czXSQkNWny8KyJ_u1KLIuQflSCAB74Xijwv_gr4FESfuaJOpFoq9Y2pxEakWCnJlRvwDmhKzi468KwCTxQxFRCtK7W-PRvghzrv98dN2Mhnupcj2G4NHHJQZZ4oOqAIIQ1GvtA7-LvsjUG0rM7nWSz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng4dLUTYx6XOuhAGzjc8-1fZRyG9NWWCT3nHlMZiagEMuaIGjMtK5LWJkYkeLJlQIKdugdzCTnmqZofqXZwxZMmO7FELpkn3V5JNEkWsedaRB-Xe9E_6dtMjFAj0SsRw28Novi0j2Ij2K0Iu8phFoXZA7kYLGIFULaFu6Q4MeuswTadPW7xZvxuT9nGdvO3H1bZDP5u-gmcsdO128k_oV70A0ZK2klVFWNDxiHlpkjKQ1y00z_DXEfRpg1WoGkMq5vWnMrpzAa5d0rPA1lXZVNEGTZ8tN5nS3h21e7OBySka0ToMRZIPtzUk5tg7A62ORd2Wlo0tvg-UUEenjpUikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl0xkIlXeHGySDnuy5wx9DKOxkrJbQAw_x1WdbviG7DsoAS0QBOsYr6q4k8imDzkRgqoA0SyEf-Rq7TsGUpCLLSQioQu8T49sNRyfeYP8Wgm8p4r6lpYD0YBDIUtDDcckWwUCgrIJh3GuKAgpxA8gysx1b-_LRM1IOVZkRGaeyG1zL7Z_0xLAK-GvbTOtFVcI23wflKzfA2gPnQLwvyyTQBCLPPD4SsjHOIYIM1aZJfNI4h5QJLfXhFncvAelJwtPiOPlhbfKYmf0Js_WtWJSB7sMvom0kZodG2BkNKavNUrrITkja2bA68oY0bCM2icqR5VxvM41EkYXWlIktdYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=r_pwNiaYcUxMkYZSa2EHeBeFQ8RmWdOPI3mNek-W-qCdZEneUKbZuj1_MvIVLNpExNfFmOSgspT0k3rRAtdpEAcq6jMr1En14y1SNuwDW2uTzzDSGwCjZV5R2_wWzhPrkEd63118ZHsX8irOemJuMQM4EMitrbxYrbKSEykW-NAFjb2ikbZUkDqL0cM_CMNfGvFhX_1mJAuvmfStq4XUfWxdN9VmDT5ylt5mGdh3Si9Pail2qeEH2bNF00NhAHdKWaro_8gMKTPWb3RP3KHt2u_8RN6c9T8mAlAi187vILlp7WddMsmkM60G9h4FbGr_ubJSSiQdFSzJPDaquk-0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=r_pwNiaYcUxMkYZSa2EHeBeFQ8RmWdOPI3mNek-W-qCdZEneUKbZuj1_MvIVLNpExNfFmOSgspT0k3rRAtdpEAcq6jMr1En14y1SNuwDW2uTzzDSGwCjZV5R2_wWzhPrkEd63118ZHsX8irOemJuMQM4EMitrbxYrbKSEykW-NAFjb2ikbZUkDqL0cM_CMNfGvFhX_1mJAuvmfStq4XUfWxdN9VmDT5ylt5mGdh3Si9Pail2qeEH2bNF00NhAHdKWaro_8gMKTPWb3RP3KHt2u_8RN6c9T8mAlAi187vILlp7WddMsmkM60G9h4FbGr_ubJSSiQdFSzJPDaquk-0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvqyQyd51uQt0lV0R8ugifRhNf-RPT3hihxCydgXyrD3uR3D_g84AGQKolgLrS_5fFfTpHuh63bwsLNT2fZRNcnPrLXOdVWCouWg4o_AP72fBf_1hhMoLg-4_a0RtLbtOHU_UY0OHm0jJawlU30luArDFkdIf6DW5cYyrSS3s6CfeK5B1P__5X-Cfzr_MKMw1c9iszuf7m3hr2NA5XTHicTfYpooKJ-mWo4z6P7C-GfY-nTN6NRRrn9slNOUzYOD0GERJqzOGvWqKVDe6SWIcoyc6vkXU_0LQpCN84a9XPrY-6k1ctKB-YbnNCTFbaw3DCO24kh8VuHMWP59BwHFDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP5KVI0ItnHJPXPstNjKLZVQ9DzApfOVu13g3oLS6VLogx7IilfK1W6wJoQzW4NVHcxCOr43yXYEOlGMxjoO0-JgsQnNKzbjCI4Q1FCH8_N1ESt_xPTsjCaH_9euLGElfromnRFa-lWZTu5vKU61SS8UPlSRUq6qALdgvOkEP68tP-YcYtyeftZHyIkUE-FTYge5xKMEh81EmHgtypm_E9bAuq4y5te80iG4_XnokznIQoZAIfBWHfuHnyEEu24Ep8AdJ-0S1wNzf6i9cyqhOhN_o-j7-TNILXLwLSg_GviMJjBNmj6PhlKIF6Gibbr80Fv0WPE7_p-LVydeT_g6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvW1pAgdA9Zcu3vc7yQ6oSjE1d5k9u2VR9sSIzgvf8aNhS3ku-X0R_0Kck-49JRxUhWMC2qxhT1IHjo_652ppOixS6feYCY8OP5vjjpfrSSNXzzvxOlc3-VASyrSyOnZkfmVxn8h7ddrGMoFyNbnjvsZ3NS9x78tQGGE8Eyr71wHW0ZLXVg23trmd5BdfpNFdgRfsrDpCw8Hi5JFbfxGt_VBPLgRLy4CJuTGx5tbNNGFr2oG38XyUSW8BQjFEUZlsOTzd40yQOZEqcg66BI4zOI0JhQaCqzdz6qiKlw-nQJuMCEcAag3y7QsJkSW0KTVDDV01ygPF4556Cb31P26dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhh8gs9hfOajltiCwQl2tgPGu_o8PKS6akIAhUDSCv_sOx4mM-w83DC9zIELAggIkwM3NqwujZQPo_MkHl5qIRPKNkbGgk1BTxB3cw6oeJ2mynBgIXh2GLDHVLVnU0iSDkqFYaDDqQuhtFxzjgQurgyZXfNdemEoBqpuIlGrS1ONa-cAs6N9ZzcSaD9UPcIR1eoCyk--FudUXfIuPy3A1wJ-QuPyxLhmvZhMQP8uaGI4yKyrDdhgaqjzvfR6ytVV3Z84sMuSjxKO-PhIqGcu74z0BnyB02lBDWFhFYtnAkPS1SzKUKauwVvBQw4Ol2decfATGvYneneFxs7O9zeWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-W5FxSMKDqeGhq5Fz68cz0xhU5iE2lGbOVXRAFgSjRJ97gEIZAUbvuVla1DaaaiPuj02JI83rF3S14cVwl6uVO3z07uF0gLHdVjtnS0AU6Ld0CWRyfKGpQcsd6kX23WsuYD8e5xsvuajPXolad9LbCsuYSEgBCTZUD_xmFwugPSK9giP128SOg2USnqfN45MvCPu5pax3ah3h7Uiz00PKA3vAG380acWpyLaPmxeA_byU0avwUVVkszA1VKizod-6Jj2ZHTgUZ8854HfPXjTQ308wFVeumvS7NlpAIksN_7UZMbsEgKTRRIDrgv1sshRjzwn9lYHLHX46YjAhA_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4vUUG-mMVe95qXeVvAoGl3QBJoIdNxiaSU5MqH4WhJgf6wW1Uc90EryObQ-WPC8xA3N7qiONfyIcyxwJkrC4mO7mNsETnavC0j0pL6B5DkkfT2G17m702A9AzU1U4Pd1Fd3JmUpnlGMQJfpnaYKXh7DA6EJIPIP73tnfUKhrQXk3LE3HBtbLhOzAmfkQkfLZ4Qk_68HmYvxZUHRIRKykE8-g7_gDMcvWGa75mC5HBWH9TRB1PKEICrm9z6UmvB6rgXEj-iUB905pULKNTbV-xeAhtZsc47kCRU12e1ZVBGOzFqTchZWudZRU5xsVP-u2jrYflKEkbdZ5jkFBVHHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcJMqOsXA55ywzV5wx8acHi3Pd7b7XQXiikA5c2yz9IUvtajQfE_4LpZRR6HfTw1lS_HzkQnp0gV9ZcvAqt7AB9IAJaJG8NnknghDz41R84C-QGv4RHGH24QOyvkZW-AvEJ9F9xGeHIiHdAfpzRMColkDZ26g856vtyAd0y65A4VhIR2XDJ6s4fUplM2Rr6ypxrZ0eO1Q-aUPNBcGgyhO44ohgu1nAZxUR-B0WSqFO-2Gav2AXt_Efk3MJ7vd7SINoaVN-iLBTeyNsSes_Q6WfoxjqFO9EAGPddqnR3r0B_L6W9FImbQMQd7VcTb1boGJ2FsCSJxtvab3NIWcWNd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twdf_qUAwWlseqgne9KoYJSFTWVf30ZiSpOHcKjg65a0sg-ohFFNClfzNKjsC8qa_BcXr5M6J11DZtWv8avcc_noHe6j_aq9kOylBfJnssu19kB3erPWAorPIbHYahIJw_UZ9Za4b-9ba33YqE4WMYaIPz-lPiKY3lwhEMRGXaDm5ZMc2qdGUUNRpGkVHuaFH9a1KAyYgrE0nVAdwvRSeytrMsK6VjPSKYdEmXpSS7DhP3XdLPXMstLz3ZE97UpK-_Z2HJEzcYXOM9V67dvLzvXMdYjlDIekWYUb_eGkNH57iUBeW-nqJnPaA-SxSdd0W4WIn5n-PnGka0EX_vguvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=jfowmQy_sSR-gw-MqrqsOzMdX2vUPcEVlTMr4wj7ECT3bkPLzKK5Fahfhxll5v3M7A6icqXPS6A6qjofIEC7aGxzI0qp1RzSVpNY4lcq0WxxIJb7-ucGuf9g4q35YvVv590NYQfVCO82CR29Iqj0jY1Vbfon9rib2Pp6WZJeF-bIJ5WcucWQN2PDt7g2YiPdpcpX74KF-Inxjww_wx-ulkjauz_M_FNeHDLvGieAOTvSKHhH0QbUi6HeO9yW8xjR5mIjz4GvFQ1n6tIdNYi_DtfpDBIqR0Q375KDetO_RgNOg0-tQiYcXTkSlmw4Zjyn30MOhsV2f3ZgiOgdQ_rYDww3bbUPv-sip0OjxzPvb-ymEvxGtTSqw2d_0qBQC0Ftiwa9_CsHz0vR-Ht5cdEgAFda3K3IpgdXOUWI72BXkiK6mxHtNdLQbq178eV9SucmrSU4GhpfZt5PGjSBtYO1xghjPArD2la-uu5sPgow01TMHpIIygp62U8xsSYK9DIEflIBnmt_a80zOwabY1BisseBjdv2p8BP-uwW04xdKW_orkIDtMFPNK3kgd_QZP8WtIiXQY6iSc37vyk-f4jD3v-ifF2NmeDnbGkDBFB_rrn7oNTI6CCCoedvDG_FB002qH5BLIdviSuGZiK06sZqpWNd16oVtWnasJNCmiwAPMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=jfowmQy_sSR-gw-MqrqsOzMdX2vUPcEVlTMr4wj7ECT3bkPLzKK5Fahfhxll5v3M7A6icqXPS6A6qjofIEC7aGxzI0qp1RzSVpNY4lcq0WxxIJb7-ucGuf9g4q35YvVv590NYQfVCO82CR29Iqj0jY1Vbfon9rib2Pp6WZJeF-bIJ5WcucWQN2PDt7g2YiPdpcpX74KF-Inxjww_wx-ulkjauz_M_FNeHDLvGieAOTvSKHhH0QbUi6HeO9yW8xjR5mIjz4GvFQ1n6tIdNYi_DtfpDBIqR0Q375KDetO_RgNOg0-tQiYcXTkSlmw4Zjyn30MOhsV2f3ZgiOgdQ_rYDww3bbUPv-sip0OjxzPvb-ymEvxGtTSqw2d_0qBQC0Ftiwa9_CsHz0vR-Ht5cdEgAFda3K3IpgdXOUWI72BXkiK6mxHtNdLQbq178eV9SucmrSU4GhpfZt5PGjSBtYO1xghjPArD2la-uu5sPgow01TMHpIIygp62U8xsSYK9DIEflIBnmt_a80zOwabY1BisseBjdv2p8BP-uwW04xdKW_orkIDtMFPNK3kgd_QZP8WtIiXQY6iSc37vyk-f4jD3v-ifF2NmeDnbGkDBFB_rrn7oNTI6CCCoedvDG_FB002qH5BLIdviSuGZiK06sZqpWNd16oVtWnasJNCmiwAPMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=pjVU5DOIojaAZDjONzUeTm77v16hMpIAk9Ezo5t1Ra-VUtm6-exjxHzpEFL3IEY_byBErLKKDfP2w421Jo_x1y9EMoOTNexRtKsuo1KLnUFuPfN3XsgmAkjZXqFCLrrmBlUj23hhQ1thV5j5DOTL4BMLFY8BDKED5C7hhyFrq7nh1W_EamSiAAAr5_ifcv66t-B5L3i9KPRbk73IPHUpocAYhESdMDKlXoLAS-cxlCOHMK0BIo4AXVvZXslS1I-ru2MlQV8ifY3zbKerB2Jo2XGCRR0o0X1LycqPmkNjLD9gVjkEP6DP4bvKVeWY5vE0Uoj7S1vLJGUAkchHE2fOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=pjVU5DOIojaAZDjONzUeTm77v16hMpIAk9Ezo5t1Ra-VUtm6-exjxHzpEFL3IEY_byBErLKKDfP2w421Jo_x1y9EMoOTNexRtKsuo1KLnUFuPfN3XsgmAkjZXqFCLrrmBlUj23hhQ1thV5j5DOTL4BMLFY8BDKED5C7hhyFrq7nh1W_EamSiAAAr5_ifcv66t-B5L3i9KPRbk73IPHUpocAYhESdMDKlXoLAS-cxlCOHMK0BIo4AXVvZXslS1I-ru2MlQV8ifY3zbKerB2Jo2XGCRR0o0X1LycqPmkNjLD9gVjkEP6DP4bvKVeWY5vE0Uoj7S1vLJGUAkchHE2fOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3XNZbiX1k5E63X9gzWztAPqCUoaviYQgRKAJbFph1BmoKW7JCX3EiJgnwbWxErYjS_qwzZ3RE3htPANl7ktdBOh1jyLnWvWsuVnAPq5D1qe2ezCwPnmOeSIHh0OXakrhU4hES-CEX_bnfAUvRzuMs5TvXn_pYbIHRguJj5sQyP0eyXMge1q4fC_OPNi_KELHDQ3ENm-Jaqz0R0nxin0dc6VMEZfeJAPpE2U-wvOvPgU4iFbHI58InCMwrYq6ODpDN59OMTrsh9rsMdMbm2V9-CYma1fM8V2g_2Naxj6hLiWYp8tWNmLsEdSdqGXne6CmuJksufvug_L5_1kmTEj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD-BhBLoIA6kz7IvJyHHw339xfP2vkum8ItzObku8EuahtSvHL3G9hJjBxKPnAB30m9DNWqgpprH7_p1sDvA4BRpaSQjOwjVNy1U-93ukNCm-Pve1sLch7WlDXpIAescT00153mwwCtY6dptSQQI6AK6x7NbZ14eYzlv7rolHhzAfhq7060s7q0vbgxSTjLXLx57ByffPULuh-VOQmyF-XCaGkM4gYmKwZ51yrixTJzEu0-_p_Mfr-X7JeJpJmt9Tbdz873KmmpmJ_vg1H9enGnafApQJ-W4y4VWmpitJOUcQmF7NR_EuCRkxpn3NXR6K4HdIYXaRDrrQY-fZBWbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0j4DL2nPA31bj-CYH-SHdf8-fM1jRW4eYc50L0j4cFJYhB1YCQ-Gr0XISvPdX8liylVNV5XZ9Sb0fKtfsORRlwmqaL3yCV9E_oH-1hbAX7QIRNRa1Vt9s11WdzlUW98iqLbDky8zBnvq3NjYm27CH4WgdcdBV0pXylQgI2iLrw62FLJx24CnWy43D_9qMNdwylJOIW_7t6fecgXJ5xKC_PyVqu107wkY4fuq_3WTIW7U8SmpF7agoZ3TnKWE6H0onEFbagQxuqt4fwBbP-icajo-47A1rVuNY7M73VgYD2dOmT_LNqcAvyKY4ieXud8nOD8F7s9PbVQq8wMuy54rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsDoRoSshLCUTaNVk2_GVWaJvQDd0InnKwuIgLz0pyDgBbSiophcxvEuFmefwogQ5JyvLp1s_vocs9InnJxdZ7-T7a4ZcNdJKYJTE8c2fx6h261cmWqxT7W53HFRBScvN1HPOD9UVOLAX_wPrkmM6CkTSUUtmlyZNzMGeSVQE_Rh95O5BlkQulMI2u0NxwY4eIMVG3UZmp5q_Ybsir9w2zCaibdz6SfmcLs4gAnBU-rsnVrs2mo8DBEgiEaPpxIiai_JJSHyH5VSYcz58N8sC2ScYT1-02Z5tfIUJJYow-vlHv7xFHxfUtMpEjxSHH5AbuLDbPpcWH01z6tdsAzBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M239nYziV6p7DZgBCROLecMZyej6OQh6Tgy9tDJ58vkiN06XSynohw20omFYEXY3bjtFi_uixc6PtfQc8TnRjvZ5h76zd8WcCWg3oDS80ecbWXR7sIoXPhJ4aosh9WqfTo-bWvEbbt-hxhWWpkvymOmqOy0mtGa4O3nHyNyTqz5BdQQSOixbJlEyo9YoSKNW4Kp8DbM36nwmrf7gic6raCcGj1Y6mEXF6mJDQ-JRYgYmhBKtCe9-ti65t_MK5NdhqpRvDQ6U-H24_05lfSmEETL5B5mgF9eReQabIOkKtsyQYps1Gr_wTk3iiR14L_lWU34Cyti0rgUdGNJQGBwmxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqDQrXVOTsVZhAzzGtTRd8w2Lrhp-lr892gAK0wPUp4ejKgBN3pO6QRuQ_roxq4IPQgFkBtwJYuJF-P08jBEamJV82KlXSC9lKeaysq_-VyS6ChkI_LzLKn9v_PuL1ek-uhlqWXycpaQi_8ClYUQC0fUaznj-QFlhMAyV18WTjJFc-VtKI_O9JpYxmqIqIVwBlOBfpn3xc0B--pDO-7uFc1hc3fxJjkuttEDo6v0-9JaJFIsh6BqDKEhY77hSj2lRnnQkpZfrmrkZF90fDlpPBIl2l7xkpOayQh4nBL67bOipOUjiwD2qaqB7eqckvB0UGyTB4oc5NMhTzMOfjOVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg5Ge-wrgKXVR7YhS8Zp-KUNsfNcNSeVLg4rDyAEkDiH17PCwYHm5agBlYk9tFbv0uwlmV67bCYKz3ZUnm8PThWIBxfEQWBAdW-ZUwUMLViddLHi99b0Dnijkjer2v3ynViqcJA1rK73XnkseOWD9CDmTSwT_SDgtBu9kPlO_T9DM4UpjamkbWo-7zGTMmtvDza75hih3oLExuI8kAugDrcy_RIgbU9eoo7l8z9kSMcgQUaU9YGmLY1obWkJ2ULw4tGyJbl73QZf0peCuv9AecwE5VXVeL6aOg0wYE3GKuQpKjxGLEA-5QFHoyTaQooJZ7PRv99Fxcyb-fPL00nFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nroMw8RN_DPKuE7vyAVXgXnHqgimO_uavYjaVHfw4VOMG7LYQeAAMfK_rux1ziiRCVzqqdxX7PXLDHpcnZ96oTZFLlE60owcHAHUgDd8zEci-DHNhk4n8bfqs4_FtJDBFJiwHaUFcEPDzSao7AoujmAWL58Gr_3LV8bFgJNXVZ08T-tWpBJ75UfNcRizhMatj_AmuicIpeehsUI504ft69igywD3CPzfW8s-HOOJYhGVvxg4J8iFSRsDge1xiIbSnTAgOQU8abrh_G3Rt3zh_ocWpIx0KJuDo6Z6wOhQV8koMK8rqPIbOqGMUrSMpnJFsS3hL_whzZfqr-MdZK45Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gugr75cnHhUIMm72CLnc32T8m8wLAoMSsweKWg5aF-9RvscD_jvWNJ98Jq8LAJqk_k-nUEyu0ds2GwBATpF-pMFjspj6SewfekPX3V80PcqqoKUpxrnsrNlz-JZOE68RBpKKGSie1J6cILUs9GRa8rzE1fBLknqh0iIfTgBp4OdZeRHuVuVxSe4sOqwqXiBSNyJV-Pr6L--lhodOlLdEdHHYXmRe4Wkn-NdnKX20mVocddEQ62QpU3xJ41mRkSBSt8XYXntEPjfYQ2ZZaOGrOHg28fGGLotQSGDQ1DuES3HoBQs-ZuW6t42lo53Rh7ZI3ZmIAgWUTn2SecKM9M1ubA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=KK3Mm32-vsmshNbVtXOFspQfLO42rmBEjJNOCpWG-r39vjSv5X3QPj25sW4nr064OoDS6_cEpMbP5Z8nuG9tC3rEukdyxmM6sVJBjNEs8OtM7-Spr6brfsr1tvTCIugt-5v0eU5QyZOwlmXYYoOz9QyfUyFNi1jJn5Ax6BtkgMNH-UC81ejirS87homlIkN89hsM2u7cslxTmLy6BiOkwQFqLNvhpQiQogTjaTvoISnWbJKRmDJ1aXiYoLlhmHjrtaTuMBVVsfwSdgFwcNJoiMpQ82teQQlYn3YziO05Y4ii8K_XGCGZLvzJRJdXXzUzrTIwN60o7zcnB9kkwe8G7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=KK3Mm32-vsmshNbVtXOFspQfLO42rmBEjJNOCpWG-r39vjSv5X3QPj25sW4nr064OoDS6_cEpMbP5Z8nuG9tC3rEukdyxmM6sVJBjNEs8OtM7-Spr6brfsr1tvTCIugt-5v0eU5QyZOwlmXYYoOz9QyfUyFNi1jJn5Ax6BtkgMNH-UC81ejirS87homlIkN89hsM2u7cslxTmLy6BiOkwQFqLNvhpQiQogTjaTvoISnWbJKRmDJ1aXiYoLlhmHjrtaTuMBVVsfwSdgFwcNJoiMpQ82teQQlYn3YziO05Y4ii8K_XGCGZLvzJRJdXXzUzrTIwN60o7zcnB9kkwe8G7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQJzXYXai2VY_qv6pSNTC-cfjhfaTnrYMTAbUbTTz4VM-ZcAi3xD6QV2TDnorhtlftHTkAUDpX4djczVsg-_XcIVp3S6Vq6NntVL_88buMtxqchRaSMvT_Ra3L8JI1hym2Uu4y4hsjMgkI4o_V1FBMHq_JFGxMI2pmtbP1GPDFj6oyVotvZOfKtvVcX69nSrpNEh7FHYI_UvoJh7EopotxO34eQg7qmA6WJLmZ8uxigoMq6TCGxZ9linSdcxa7Gdecv2ZKNLMZxnmsloxGG5urdtZiwzn0xZv_-qCzZVF0TuGwljDAETiPVrD_oimD7kw6LI6jOgPEbKQDFiH_jaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=eYzJfmOnkzZFcWAzY6xxrpzxpj1RJ9rJYzsxO7-ZrGiCc6WzI7nCLG1zt3C6Oi8zUbj5zxZPkYA3kTpIqE_fWVTaqWusaEn3pjYQsTGLsYAvHuzlfyjFeysiUCLrY98pMnHQ5S6It0rqiirmax21opiwBqmE08grkL7Wf7im1cYbmQjzw2X7Q8C0BLEPhPcDYBeJFeJnJ1iPudY0VPK3wwq5Je_LyGChjZoeTjr9dLnyN1vDsMZIJSxqQCi-rGDX87EDZib95M3IvQ7lYPpsSUgrmMH50TRRSTikCpDLn0UTLSNQwg8DIgDkiwgXQ2b9L6eu2RVD6lCkO2nF0uHgbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=eYzJfmOnkzZFcWAzY6xxrpzxpj1RJ9rJYzsxO7-ZrGiCc6WzI7nCLG1zt3C6Oi8zUbj5zxZPkYA3kTpIqE_fWVTaqWusaEn3pjYQsTGLsYAvHuzlfyjFeysiUCLrY98pMnHQ5S6It0rqiirmax21opiwBqmE08grkL7Wf7im1cYbmQjzw2X7Q8C0BLEPhPcDYBeJFeJnJ1iPudY0VPK3wwq5Je_LyGChjZoeTjr9dLnyN1vDsMZIJSxqQCi-rGDX87EDZib95M3IvQ7lYPpsSUgrmMH50TRRSTikCpDLn0UTLSNQwg8DIgDkiwgXQ2b9L6eu2RVD6lCkO2nF0uHgbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=I3aLlAbPtWtdruu7XN1YAZDd10bu8No2n2g9KEnKdxIj0OID7nxQ4rKW9EUbTwyfE916luXHYXL0-_EKTFhd_lfDTP2bzSBATD4cC8U_qIL2H-IoENHCNmbOZV-OJatRPlG30FHZAI5bRT5degdAlFjUDv4DsPbNxox0hbg54EmcLWJo4nfLMy0QEUVH24xaFM9ywmDPLeV1JrjFDiDHkYvfWLWh3jx3qkMbwcL1jH65ddki8-TT3LPkxSXktfb0pEbCwiuIbl8ou5TJTH7pLpGLymaKMBAY-8_6lRd3uaOUR-KMDJoYs2cZaFCSKCsUwwuRmzzheIjMI4VfAetVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=I3aLlAbPtWtdruu7XN1YAZDd10bu8No2n2g9KEnKdxIj0OID7nxQ4rKW9EUbTwyfE916luXHYXL0-_EKTFhd_lfDTP2bzSBATD4cC8U_qIL2H-IoENHCNmbOZV-OJatRPlG30FHZAI5bRT5degdAlFjUDv4DsPbNxox0hbg54EmcLWJo4nfLMy0QEUVH24xaFM9ywmDPLeV1JrjFDiDHkYvfWLWh3jx3qkMbwcL1jH65ddki8-TT3LPkxSXktfb0pEbCwiuIbl8ou5TJTH7pLpGLymaKMBAY-8_6lRd3uaOUR-KMDJoYs2cZaFCSKCsUwwuRmzzheIjMI4VfAetVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stAtcND0OXM59qr1U6SyBf6dR4iNoFDwwKflVu7wh1Ks1YZguL3Pf75UanRUS8GQqjdZc9eFloi9XsdZAPkCijwOIFfpnNWJ-3oSWhOFXQzXXsb6KdkghC6f_Dowe4Yegrih04NOMq55yXYnTrn35ULzEYuEHONKudYWd9Fv1J11fnYcJXEbnHYNaEfO0ckAFcztPsCyQAwu4ncLesLcClUu2EVU1Yut6fCs3uGdo6ozXnhCM-_h7VOnHCZh1VM2VXxzWvlB-ee1ChOXShuMu31HR938bnGjEOpbqja2f2ztYADb02zQ8_TbxntSFz4Ix2B7MLYCJ9Zkj4UqWrWyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Zdmhlv8NkEwKYaPJzSKNxGzT7omGGnZmxgG2TMcTuriPC0zmx0F8eG5bREny_0zW5iLH7J0jVfWsZTFHP2sypNQzCqOSzSkltdLhozwVBRKOpdafnCvIX6bsdF8n2ZlRZo6MvNMLYlo2imEr5PPyUIsyMh_v6tyMd6RQN_g57u7RKevLFRntvLN-Z2eq-gPWWuxVH7nFrNx1fQuZl5G7Ztw8PFAfV9ukPPqioWFphEoNs0jqG_ufje5suY8lZ-ciGCiMOSPCdbLImKaV6nAulZc1ZPuvb4e_qKmZdg7WRBm4ljDiCnUH6TrjsTdSev24c5wLE6pcCpdECJ908EdDFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Zdmhlv8NkEwKYaPJzSKNxGzT7omGGnZmxgG2TMcTuriPC0zmx0F8eG5bREny_0zW5iLH7J0jVfWsZTFHP2sypNQzCqOSzSkltdLhozwVBRKOpdafnCvIX6bsdF8n2ZlRZo6MvNMLYlo2imEr5PPyUIsyMh_v6tyMd6RQN_g57u7RKevLFRntvLN-Z2eq-gPWWuxVH7nFrNx1fQuZl5G7Ztw8PFAfV9ukPPqioWFphEoNs0jqG_ufje5suY8lZ-ciGCiMOSPCdbLImKaV6nAulZc1ZPuvb4e_qKmZdg7WRBm4ljDiCnUH6TrjsTdSev24c5wLE6pcCpdECJ908EdDFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxJVsjMVwR7737nkuH35EivMQssOgb8qcYMWJEQYG0GN2C15kwwzvZ1xbjox84n9ndna5TsVBJXwGTr29h2PJNbsScQyFrX0xbnwdsOAfY_sh6m5Z-pXkEPkwSQjZsReXoqV4hJPc5WK9FpOKIJ8v59I9nPSCHfwkVBwGdcIDfUrJ78H_O-NR6_Wmj89HnpDGH5upzJ87Od3e-qmZJqx755ncJNunRPJCIPJjWAib0c9wpnM4RfExuPrNRxyT3Tv-_z7rrsRNj3pafGncciVYO3K-zpK64Tw_BISYqs0c_aAysv00KHFT3Cy77Bx4u3C5FxRSUqvH3Josf-m0GN7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBhh8Kp2XIfqi8OQry5Np0L8JJaVF-NamCZFyJQJR9IkwHEVMIkNAV7mR6sV3RLh0TiYvipA-WI_PVq-YeiRyl7bs3AFFbw9Y7LMtsqR-x0gDfEQTkKsqxLxzZ2TdmBIArWpghO2oq712uS7VcRHFPFIGLJSVYjc82GAKT7eiZ7y8HkbV3xgMUFIUoFgnZDpWv17-NZPOg9Zmc8ESIf4gOHRyazVS7XMCl77Z5fY0foCl7aJ230lGLEVPfvt50AzEFdGFytXNkjIqA6AEmTNEWFdBPH5z2Fy8H_cuOgL1T8jVTJhuZsN3mJE5JM55dw4xcVZefK819Tj8PDcmkeGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZvy0BNIDNCvWs8avZuz6-ggjt-5B45bg7F73hiyegDWCwM87zKHehQiXThclvWN2PvQUlnNHq5fYdW3xlZIVw1kH9svREBY_n-PDjtS-bmyqwH6SP9SOAx22T09-l1yrQ_KmtYRSfYuRdPfH5FQPPYbhJazaVL0IQIP0DcVk4wpmX7RdB8SsBlLYRlfr08BYnWOWCksCTD466l5pJXnSl_XSSZWWqWHVCkN_3_HQCjC2-7uG25n5qgHTB-evp6hBMl2kt_A00uH1TK6cakBJlzogxYeMDH2JfBEtEYMHz7iIfavut38SaQz05umfjAwwf_pn6Pjk3SOygzdIeiREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hqs0LRF3GTAM6XfaZepRxsQltCBdzf7ied7Q5v8LL45DlmuOYXA6QOEpXLbf3Mtg_xUPy3IXkOIDT1pxHKfgvlDc4e6pmN-1eRd_40DvKGZKOFygH8imiaaBiYPnbIkmRbDRCEUo_82V5OUpDPZkWG5EiL488OrhXcaV_Yh-k00MqLMokjvG9jpGDmtiqXtMvQJAwB8oVhOAQXXKDXi3jOa1evQdXDUU8niZBvwkp20L7tpjJ8pIVhN1wmOJP0Hp6FEK9GVEtwQkTqEfKSnKDIG-xZziUDifQA7EUlTdb63jZapuxIXS5nUNiCPJprUku1VuQ0rB6nqUB4tYC4uBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVFxCb-UiIvkVYognPR_Kgh2bQdXGR0PEEZsUrfr-_QqkTdN56XnJdCiJgW5EPMlkQnb_-DpXMo8kMhs3CRS08-cMgJoJvZ2m8omQ3JMNoF8UthfUd1terItfAkBfQm2DwIZ5Y2MbuudJvry41Vcjp9_yt1lDhHJLkiijnj3Zf_ux8hfoaUc7KfbnC24m9msx8gSq8UlW4aJheXVVcF7ptxG80XHrm3qyUW05z5NmuAuKGraY9zKLu6vuGWKeNOEJ-vvkIJ70nGq3N0FpxrFxCNZqC1Z9Dt0ZN9-XkbxDKRBEbXBq7uaHYIYMcsWWIfzf7M3gEyfCNKvINThBRsVqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gufuXRBOerwR6tN989IO3L3NiDMlJEjUl6lidtDKqfrNnnhp6svQDcVc8UQgGlqDJia367GrMozvH9l4lH0s1b0ESQCQT5foJm8jCowBb50azZ9FlOwDfNhNFSz_8sSQMr2VrZcl4zUtLKOsxbFUiC2DnVGF0xf0lEewRNIR9ZclKEOGoYsh5qNEokYSovhwtKH9DuEoeAGMH76pdBgnOHYESkHMYPqsp6GDoSpjQGMrQ2tPVH9WhrRx2ZRLM-RlQL-3KtU85NaEKudHdvRoSzu_Dg3H5nuAaJkkOkgeuQgvAPz8jkDr8WPuS4XFd-vo5shteeQTkDJh6yKUIVsrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWNk5fLVmHwQD748t1q3sKgmuOkNBQmtCZftFfDLgqbJDTjMqMCybnXEDstgjUmZAUvFAr_0GqT_TVdzJeHZNju_uPe0lZ31mqdz6jJ3f8G5QV51cjgHCVyq36bRNx0ZvthLzoXHJuofB0eg7UHARatQjcUhG3ZqnxHLbGJxWXUDVuHJKpUlgD1mGf_HePc1MZyCiP56YGwcktIinzDq6j9XDrj9KTZzx1wowBNFKqHltqxPOhmwLlkmOO5mL07YN2qJMnEDKxKQyVF9zWzmU0l9kxgU3XfQaFlxjyZ2MxA2XKGLRQWuxdiFLDifOKYwta2zVt09QgRTqSVTO_TYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3yp3mp09WG-sh5CR75tAUX1bgsi8K4L8RynzXePDrzj52e8JD6XL36FmAlEQX2la8pDysc3GBeF1G1JoPoMlyx4ot45uipGDSOd9uZ7dtDYhxV2iN3q64y7z6rLuuigpj_tXUXiIQaZ16A4tdd51GfzjSUiP0CPEgMQisV3nIEGRUZ-vGW4tYZ9BHw2_3jfIpKzyZZVIdD0tc0FlHao163Rb5KK5-3P_9UXug2q0z93CPhTiiFM8sGKh74xsj3FXQUoSBZ3p1040te8zeInhMMpsLgwFiHtL6WzXKr_ymFf7EQcUEipcHuZbmmkrSnH9hP3niNyoD42uPbszDbKsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=N-2hdqzQ40ou0_qYxQFtK_e23r4PjqVSaJ5RL0Gncq8x8sJODubj5MaAQjq6tj3S6oaO0K9sWXFsXoN2P_07U5vUhukCBJ2TWtjUHp0lZn0lfdvYV2TZ6KnllNks37wrIMfA0D2gMxQph3_-3SUi9KLuABL1dBGOkYwUfIqYPCLvheESYIBf_8V4iRrFptvLyznRRT4fK8Y19klukqqOEWywrYKVvXD2fZgZcytaIl4Dz90vckJxkfZW133X_J7E2i0mPIrGGJsxKr3F_k85cziFjVreoeTBwDrUtu9hB8ekVSKP_qMSYuor0wSB36nVLCEanM4IKk-W3MHs3fgUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=N-2hdqzQ40ou0_qYxQFtK_e23r4PjqVSaJ5RL0Gncq8x8sJODubj5MaAQjq6tj3S6oaO0K9sWXFsXoN2P_07U5vUhukCBJ2TWtjUHp0lZn0lfdvYV2TZ6KnllNks37wrIMfA0D2gMxQph3_-3SUi9KLuABL1dBGOkYwUfIqYPCLvheESYIBf_8V4iRrFptvLyznRRT4fK8Y19klukqqOEWywrYKVvXD2fZgZcytaIl4Dz90vckJxkfZW133X_J7E2i0mPIrGGJsxKr3F_k85cziFjVreoeTBwDrUtu9hB8ekVSKP_qMSYuor0wSB36nVLCEanM4IKk-W3MHs3fgUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=dzoYHQgZCuwwfVtnP34hPugcVBfBENtELBKTYk_xTty2RQl-We7i-rfCtiaUTOGkLjVXYk8s-9lj2ctsu_RO78sDnjANE5nAs51MIZT9vW6MdYa75oIKb1Ug2HnOgMZhEhibNZEaVaWGm-Vd3TU3elujdkDJbrFnYZ4swYq3f9TIwzwlpLjhZXmG-I2X9Y9FF1c8dUYUH8i3lqoa7YH3Z62opwDz8HlfY-dM3NE5ZFav5cf3eTIuBFzTfMlT0Xe_blIq9l752g05gMSbJG1kDNMsNd2VIHNoxiVM679Suq93AkmIHqSPm3ug-1vvxaqL93SbrhFY6gEgxRTxXBfJKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=dzoYHQgZCuwwfVtnP34hPugcVBfBENtELBKTYk_xTty2RQl-We7i-rfCtiaUTOGkLjVXYk8s-9lj2ctsu_RO78sDnjANE5nAs51MIZT9vW6MdYa75oIKb1Ug2HnOgMZhEhibNZEaVaWGm-Vd3TU3elujdkDJbrFnYZ4swYq3f9TIwzwlpLjhZXmG-I2X9Y9FF1c8dUYUH8i3lqoa7YH3Z62opwDz8HlfY-dM3NE5ZFav5cf3eTIuBFzTfMlT0Xe_blIq9l752g05gMSbJG1kDNMsNd2VIHNoxiVM679Suq93AkmIHqSPm3ug-1vvxaqL93SbrhFY6gEgxRTxXBfJKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=e8IQ1o74r-EYU862KR9FxAmppZY3mBvmBQQd3TeEj_o6Z4kqVvgdCOhhQfJnVZ8vn87bgbKkLqr-Dx-283pooAQ4iRABdFfFj_iM_e1YQaF9ttsCMBgDP9HXlJyqFAg9rEiotOZGWR8vIaZeu0bqMfAxr94twmfSMDDTFf4OCRYALnl4f-RRB0h-8T73Rc1tFURUAuFDpbnAMeKwNSPcAv49x2Co3uXz9MeDXQtJYcQciX07y21kWJROnVMJZyYyNHAZwj9pfetg3aLkEOEiOKlYc2eTxn4sv-hZ0fM3j5K-zI2RzAVWKad6bQDWv7VYWj5GeeEpDIdEhF7iMSx59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=e8IQ1o74r-EYU862KR9FxAmppZY3mBvmBQQd3TeEj_o6Z4kqVvgdCOhhQfJnVZ8vn87bgbKkLqr-Dx-283pooAQ4iRABdFfFj_iM_e1YQaF9ttsCMBgDP9HXlJyqFAg9rEiotOZGWR8vIaZeu0bqMfAxr94twmfSMDDTFf4OCRYALnl4f-RRB0h-8T73Rc1tFURUAuFDpbnAMeKwNSPcAv49x2Co3uXz9MeDXQtJYcQciX07y21kWJROnVMJZyYyNHAZwj9pfetg3aLkEOEiOKlYc2eTxn4sv-hZ0fM3j5K-zI2RzAVWKad6bQDWv7VYWj5GeeEpDIdEhF7iMSx59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biBehplTeH29IurcxP35hRplxLa1_HNt3azdTHal4B-OLQrMau0_wES8CghheJqj2DemrhcMRAVgBLdj0-Y1yZrDel2n1daINvGObUsRilMRKAYJMAMMEXkEf7SBcAF7s5v3gpALyivXAzMi6F-d5T10lf0r_3owZLWVhq6yDlz7Tb69O-IcTkVHKlXLSAWtAbM_MJ7MBY5qDIDe_Npq1GFNFkQLHVN5D1xbXqvu12pBBVDv-NK1Lbv0U0lOQJt_eHwM-2Dm_lY6XcBlQRd86hY09trpV-HZ-Glt0aYq_t6OH-F5IsYJFXey8CbeP1X6SPA6awM-Uyc0RvJW4G5ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0_x74V96UOFe_T6M0UPk4X_rK85YsPOuF0AhWaDoDKldlKad4Noq97E_lu7VRQksrXqj2M8NPeWSlAp585FVjSk6DdYof7Z2x5iCBLt8zRTMVCcvLv3VYqqRABtHTFGfBQ8gnHzhxAK7DTudXOfxhzgrJ8EuEUpOTol1RCiTE3aWwZ8PLz2O0054rTHCQq0Z7z7Ckxcncibea2Tkjf0FJJjy6SigcLReOiEuBtfLWmd7GbrfzxdqhBSGjlBkw0jviBkQNLgXUFKdyya4BBvKf1lLuVECBZx4lt8229xyNuBl2Uf2s1YORAC2Qw7TvZUY3qSUGVnMx0pLIT2tW8AOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pygkPnvAEiJrJUeFj8Eh0RM3-Pn9P53Gxw2unJ-kcR8zOBx-xkgfCXOYanoDyjjtcKZb6gqG0ETWRMUWy6zOXvGKxQchBJWaika0qzyB4a5pdVpea7_Q_g4bEOGfV9p_lDwUIpfqA8yGg8liZ_VeJcwaVLOP9nfMVc2sjli3x8ZekzDmGT03XR-7bE48MzFlgch0OjaIxhpl75DU1sy1nQ5gZM4V7K88a9UnBUxyRS-ohP2VB4eGAGS07U8yOi3YxhkGFlK03IqpHz4egBIajY_UuP-4Qycci7xhHUbCi8UyzngDnIOOrauWKbrU1Z88O8AEDhCWJSx7pi9aRHZx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaLzGQv5oWMjhjtkNqGl2E_rPFagA3gSjaqdbGY__9qbF8t9xRNWlMGpEpQT5kugBWfCbBgNhXOpxhQaGMKkWrTVNUHvxLbmkIr22ri1owTLq3NGRR7VfeEjqhjzkZCpaUhsg_XCZNRSOMm3wCDyvrFl-qwYU5szXUPaZ0FJNHpg15QLEzbkmlgWSvya0eevUkQnUgRepiSMC2FVVD7t9VMhQkIDQ0ytkqa6QkVELnQEbYa6xgadgPrM43VtTJA48rGYQivA9Qkbvtp07vx19YV8bI_sxDFtLcr3UyfUySwOMPK3E8t7PJfPdYvB0EXZF3GRbT4jY5FqpiV0UH_r2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=me8xrSYgsgycgLlgs0-yqiEEkZpo_Xbqxr9xQymVXu7CC89X8gdcckYe-aQEF6_z0CzJAvDeUs8qfWRJMiJvghaM9iXAFwl2fGAJ0ORA-jZflmBjYlnt4PaPxiArCSdoR_-3pwekpLSYM-ilJ1hYK1WUibTst68vnJJFJXpUqRlUpIrkX9Qy5JBJt4c59u69IXKmA8rj5QkG8jeRnhd1luYl9Tt8UohAhpnEk1btV-w28AxQh0d_LTME5aIbtorYjGT2elpTK6R7CBgSaEuaEwWP_XHDo4KJxo2ywnJamXclZgVwBxzcffuZ-DA93ZMxMZFgikvJ94eFX6aPeQeK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=me8xrSYgsgycgLlgs0-yqiEEkZpo_Xbqxr9xQymVXu7CC89X8gdcckYe-aQEF6_z0CzJAvDeUs8qfWRJMiJvghaM9iXAFwl2fGAJ0ORA-jZflmBjYlnt4PaPxiArCSdoR_-3pwekpLSYM-ilJ1hYK1WUibTst68vnJJFJXpUqRlUpIrkX9Qy5JBJt4c59u69IXKmA8rj5QkG8jeRnhd1luYl9Tt8UohAhpnEk1btV-w28AxQh0d_LTME5aIbtorYjGT2elpTK6R7CBgSaEuaEwWP_XHDo4KJxo2ywnJamXclZgVwBxzcffuZ-DA93ZMxMZFgikvJ94eFX6aPeQeK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PLdy8ut3S-5Sk2SLyy_z50M9WWZKWC2mHEulIIMACTgpKd4l6jTvSLRkE5OWOKWr7jcZZvCqOgFR0s_BRmluu1rAmzZKEBsX_oDWXl2M3zg7P1sVHigIp28utOVl2Wot-9agT0yzTxJGzLr9rZ2qtzWT_EX21aqoBzw74Dqr6_oti0F-1VOF3t44QyiuhzXTC6tETq7eJsSGP3Asw0TSHdmV7GwIVXTuieiq56OA1muhpFEaF8cxjSjDM7O1gWhXGYPo0KbptCQBBRM2Cxr94NT5iULFd0weO0R7szQvAIIjzBDJlGKkWKaE51jAeLVTMzi8D06HBqOyeVN91VLvrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PLdy8ut3S-5Sk2SLyy_z50M9WWZKWC2mHEulIIMACTgpKd4l6jTvSLRkE5OWOKWr7jcZZvCqOgFR0s_BRmluu1rAmzZKEBsX_oDWXl2M3zg7P1sVHigIp28utOVl2Wot-9agT0yzTxJGzLr9rZ2qtzWT_EX21aqoBzw74Dqr6_oti0F-1VOF3t44QyiuhzXTC6tETq7eJsSGP3Asw0TSHdmV7GwIVXTuieiq56OA1muhpFEaF8cxjSjDM7O1gWhXGYPo0KbptCQBBRM2Cxr94NT5iULFd0weO0R7szQvAIIjzBDJlGKkWKaE51jAeLVTMzi8D06HBqOyeVN91VLvrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV8oKgxyA86yOsWPZVSscKxF39EIl19grQ6W_pNNQbjFlWUuNYX-o11slpPL2QbmIw5IpHQ_sUOym_WyflJKHlOA2YD2YDoRd3DaKb9QZoza3oZgkcEKZ-y-nALv7IBYC9WZZsLotIRnktfQ9gNszNc06pQ4WK9Vc2ZRqrmzQeNRDryc7CZEYMaLU0eDzcxGI5SBc41LMAR7NVS7--jBW0gzQzjLMCEFoXwbIM7D8R4DLmBU0sak1l71jUWklJtUFp1gNQod0kw4T4eK3Apcf24PrFhxsP_dbSTUw7AUBJLC7cwD2iZv0fGUaVMgJiHfWN0aHLhjRtxARF3F6qXPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcwQ_djv1TeJR_VU37jzn85KGJgeaz1OPWYDd3vmPl2t-sWrDFZoYsddXgZBHnC-SdcCIrM-RQWlyAxBb4gK7CGKFbdghnfd3fMB6Evyqf4h-3Z5R0WaiJfZIMCD6sAVII5mnte6XexW__FUzpaOKDl0U3KaO1UwbYZv2neIZKollcw-oQdfTR7EOl0eMwJs1QZY8a_6s3c98G-VAocAmTMrbiaptdx7fFzgO54EtXhUxoXrMiBE8MZIdcabWxHzSiLrcvmPLnx8keGdGAMKBJVjXfdVwgmNs6UIC-YVQgMrYwcwllIA6FvBgK1ZX3nt4tgG4QTRHyQ2GuyG5e3u3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxBEO1laDsvs1Ac5gJcrnNMO2NPHQTMCo1_ZAaOtHyuwfOBBS2Am539Biujgq64LOtTbjcgB8w8VSkpPCvmdNmozmhRttRXoHFJ4LDaL2KJoJnd41PVGlj2c-RJr2H0fcf_qeHCCJdLrY1zFAZ1wkAf8CgypJex1inb_Occ4FpZ9UAIIWoJ8Be7h2RSLrDwNzYSGRhAJTZDfQP35YYXHR_CpqxS1S8ILBoXItAkUeQ_C86TgJ-VueTPVTqcdmi9K2AVowlfux_15HSFEsEdk66pRYI0E96E4FqUMgrimG2E1kmMinBCeR3Upb84BEO05-2L53yCIdZzzLe3YZrjN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrK25wXvne7qOBEtlJDrBNuzW1uVTT-wTSbqykXYCTFM5eCdQtvqCk6G8WLAzfa5mrFR_hpn7UBCnClQC3UcyjsuN5K_BCqYNFncZKYAW80lraSQnikKdVn1JU3pqyGzMQIp5mPtnOW_l5U_TFFayOc9DHlbHCTXqDZYJbCirNFBKYCXkPSQ7_5glpNCYydSw-RHcmimH1r_FbTSTS78UMAOYr5Gcqp7KE1Dl-EDyVkoITC896D18PI_NoK-QxKK3LxV2VDBtBqM29ptm2vLI0Fk045QHY7yZBNfKXqPp27ndfEkxJQ2ooiaw-yYl2qyuJDaWBzz1ixPvs-OVcwDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhd-BUllysme-Qkm_nlzrvx_Svfq7TkWpJGWKiRSqpGti8fiu9VwIaEcykCioIEEoIpU62CvZm_XcE5tKJ52kMad0T4_sgp4RQlY3Z8PGtLVnEXZMH6ahn9FuuoMZ8dSzk0ZviPHVSF354t7v4_cRLHekCKJe_vBuFJ53aAw-EDjWfKgVkJvDqVkZB1xJ7WN0iCFqfhal-8eLlM95X467N7IeKeQE_U9miI0craNU3uQXeQuzR4cyMF8c8JUMWbqryAd6Kl7bLUl1slWF2CnbRdmk7Y4EnX6aClcvald46u-MjAsNjlXCQ2oUJKaJPB11YqzoAILY9upKWlg0_Hb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACS3eXlYE-byE9aUieMUbTqXp5HZlQWlS-L-8l3B6z73kQZxar4il4iXpc6_MsCokPQNltM8jfyaWKqwK3bdnmM1sjxJDB1SUIotUl4RsP-MW174QXCmyq5J-waTMJyCiES5J3kWp-hRX5QLeISxX5k8dKD_vwS4fy9R5PSWEY9UCyAuIL7yi6otoWmpVtGgIHxUK6Ys7AtA84LBZKiwOcM3qLvZsmcPN3n1r6XCC-zHNKowYAhqwe1mhkqKoopbLUyaqZDcDKYX7KMTG-Xm3G8ruEworTZpsX9yAbTa1oTS_B42J0JzWeCeyAaJZOiVd7jAA2itRnlS8RGmQSLb6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
