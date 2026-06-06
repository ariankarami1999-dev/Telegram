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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm9QMm5wHRuy6EKHD-kdwjppZbtpx4S2POhcJyiT8bUvPZ34IUHAv_Zj-hp-I_5JMWFPTGdo4NsTqxmdc4YDdX1E2h73mwMu5Li9HahAjfUIJu_XWUKg2GzNaWooUIHAAQTAzFPuPoYKKpITSbMuzepE3vWludCRpj6JBOi1nJE5utAuLDBnjJiDzOqj_tGnxoSwWDqLroogjy1xH-3PvwQueGTBZ05C4CHpXBz_VmJWJr0nOZ522pRuFTILguWY9FywEUfScUk2JtiJotQ1R9Z6bq4w0FAkjGCqYH8homfR-GW4yBw7SCfoIKMMiLTHMbeLcH3pVm-g4QHumdQjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_U9xkLeiHppY4y6Wus4HAVQcbmdy-D-5vZ8dKiLE4n5aLfcplqIFiDbA-Me5EdyGxxs7lLYU34LBC394Nyg25sLMmoGPOMWFxShId9kkv_fh-B7h-YOYaRcjQF2aMZpgUIwQKECmalayGwuiBzkUNEXWYg9DATty4dxyVFz4Ua-u7dB3cR7DJuGwKkk9PS4aeA7GQHkbTFZAGqiq9iaqQT1Z04s56evgWihFLiBa21BPtUCGT71B_R3KxUIzuk5t2DCZ52HMN39rR2bTJKhA8pkA1ooLA6lqC6oSrVpzv40L5ul7jThPrnkDElmihStGYRkekgqNIGf_lRED2_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7DJ9gGTd4H3G-BNXnON_cxz2ELfUPAaJQNv4oCyhcmGlxq1HIy8vBkNjRSf55LHeffonNfXJV0vBrjmcEshp_8_TDoPmlYjcSTPZHZus28NQGFtxwHtrgttP9kVazvGd7-jYqStWgWuv_Rn5pc4zjP3-x_iUO9m647859XGWM6Yc0wLTKH9pqUHLsWz1aRGGvLVMN0iE7rq5znqGQSeRZVal9MK4zTdHX3EpxREo2_XpzZaGyHRxa6pgJWEANgXQ4-HK1lNYJdcBD9v4zavCVIWt4YvR2SHcqd8e019DLsQzeN36jFKflCYhlZ57U1DHFroOancz_OFTgEDq_9qXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah-kIZYPjebSPBEtPafDZiHtxJ0QHB-E1rT2M0FN6Xr-nv-RiBatHRgsJhu7XVrOW9BYBDNGlHzvO9r0h5q5vMcwaoYeF43zkD8hxdIvbFM7Let6zJp6aNxf-CJGqAoos7Jm4MyGcLpAbs7FTZiBeftEv1eDRZTNE_iPtCH6M9C5dIdIlFMwtM8XE78R-YDW7CTx702tBlJ4erb-7i6X3LDTKTOyU-cODf_SOWovqXHliOBp3AAuxFDDQ4aJcLgCouhgQvQKcy3ApsD2FGfVfnCjvwzrhJBN5MOehkRW9ZKfF-DznSS9BFxWZU1W2ElVD9bVSBz4h8x4okE_TStZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=ux-wkoxb3xRIcQtaO5zl99bNc1UIFQTNUowRPnZ2pBdYuLqqbig6yNItbygKQsAlSNcS58R9lw_MQVuB2AzSMUif_p5jJH_kkflKFmOvVe6HivCuTG9fBTJ_339g_u5BH6Ey_Aijih0CiLeZ7MhyHGfuR_GzFxloGMTEJP96zG9JnCCUPvBuNKqv7O5-73ZQRznZ2GfwMlsp9LvmdR-wGCOJMroTLSxT1n7V9qcKIQ6tWVpnvVTXfNm23huTaLsyyrBj8bQCU9g-29sljAIqh_GM5ngh3YwrYOoU7gWiE6vSNVKJGvwZpdRu-pw18bczJqG45xBQ1cn5R16gJcpXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=ux-wkoxb3xRIcQtaO5zl99bNc1UIFQTNUowRPnZ2pBdYuLqqbig6yNItbygKQsAlSNcS58R9lw_MQVuB2AzSMUif_p5jJH_kkflKFmOvVe6HivCuTG9fBTJ_339g_u5BH6Ey_Aijih0CiLeZ7MhyHGfuR_GzFxloGMTEJP96zG9JnCCUPvBuNKqv7O5-73ZQRznZ2GfwMlsp9LvmdR-wGCOJMroTLSxT1n7V9qcKIQ6tWVpnvVTXfNm23huTaLsyyrBj8bQCU9g-29sljAIqh_GM5ngh3YwrYOoU7gWiE6vSNVKJGvwZpdRu-pw18bczJqG45xBQ1cn5R16gJcpXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsatpWEQNkCe0h7RiWrbWO4COSWJKFHXlD5Fy64Hw1QTioSeWGd4i80M9e2nnbK7nZhoLQ4tUFKvhkseEwzIdeUOXIdYMYiMDM2vszHNADh4tEEPpRjOAnSjFR2sEduSBUHxh1tPSulxq7I-f1lfsH831exnpBIjzAxFjSAsyCZY7zbpQjbnnVoYPh2N5FNzKhl0V-ferZOiJ-iHuqwHIqreOi7dbsAC4Ir_Kv5J2uBxB-XjRSUGkmu9xtG4yK2uV-JE7MgxQvlqYqkJCsANjenvHqF-qVX7m8cS3Gd7cIJA8mmH0JvOuoHRKUDuruEoM8vBdBmTlc8ELjx4itJVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGEfWi015V5_HeoynJCNX8-DqI4rDSp045Fe07NHziT0WbyvUuMP5-NorroBSbL8TxkxeZvKLZMMgEtGcVfaZcuxgmEwOLDwwg0PZkLQ053vRJHOTbka-UQTsde2MMJ1dcoRc84JpJzwvtL0waXnd9DWj2LY8jsby9BHnlfmVkVdf10YINDsUQPd0y4zzVoRRjDAPkrg9dugc2mM9IFOCrcTGt1m95sLcUAPf7He0o5UR5IaohNpkg9T0i7etOmDBy4umXzWxWbqukTSDQwkPh_x71avqyXbOWVvmuVEO75R4FM-DLVFhpCAQCBsV89lqBGQaEBo5DCjwsA-Jem9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vf6soUKyWaARBbdW8v4zlRHZKEligieinm1LKFE2HO1uN0GociLf6E_rceUTolL_Wlx1QSas9X5MH4C-C6ifYipPUQ_WkAUyPcRuVLALn4HBw2RsvHlutZoBjrcmTvSnQUldbc7RPPSldNmj8zeMIUua9qErtW56W1oxbsGTc5tKOc87X9ZGQeNWebiKOCb9YleIT2Mrrm1NgRxL2b17Grf2NG2rjg2RqAObLtIGhN35Fo1rPrE-f6Kq3cfMNO7wHK30GLu51XlC7tX08FS2zlaBTUg8ykQogJDSi7He2BE7FSvGRfta70N8yMSbcmxejyX39tIXT3oOC9mPrTLopQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=RkWWpNq3hB3Mz9NV0TmWYMBVt3qhWdzprIY0bSqw_hmYoHOFWRHOLigCOXdY_-NBHYraq3q9KGiHoyRSwas4zSFoukhpvl8h4XVJjdg58hqqvvn6ilMlRBC1SGFJwckZjuI-angwyCdUaxgseSpemtAZgy168UMaiZeQfwrQLjsOBVCM9RfzdVU5XnD7LG7Y53NEBhADOA3OI5aIloO_rouHhUPxdZA02VkaZXnZVZ2O6-v-WqCaKytPJFZ0Tq4QjAQjwTg8IWhDApwXrWlcGtirHXnsJns4fJSrQdWTNORykMvuxc2nk9MKPBYEkjk1bLiQ5IJm5Xhn0bCAx6nFJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=RkWWpNq3hB3Mz9NV0TmWYMBVt3qhWdzprIY0bSqw_hmYoHOFWRHOLigCOXdY_-NBHYraq3q9KGiHoyRSwas4zSFoukhpvl8h4XVJjdg58hqqvvn6ilMlRBC1SGFJwckZjuI-angwyCdUaxgseSpemtAZgy168UMaiZeQfwrQLjsOBVCM9RfzdVU5XnD7LG7Y53NEBhADOA3OI5aIloO_rouHhUPxdZA02VkaZXnZVZ2O6-v-WqCaKytPJFZ0Tq4QjAQjwTg8IWhDApwXrWlcGtirHXnsJns4fJSrQdWTNORykMvuxc2nk9MKPBYEkjk1bLiQ5IJm5Xhn0bCAx6nFJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=IpvL68MiTQbSUGC0d7uO52cDN9lYwcNrxVHdY3tWrynCdfxGRmrjxOhOxNcg9qH01T5JJSLSEt5FN6IYlcLx0T0f9n5YiAGzkqH8ErC5JOcYcmDPoOdSiDULl5ZYCAvDAeoJknUUNiuZ5C9jvibDi6KZSYKsJG6vT2-5gEnfZ9TkwH8PJmpr_2y8JIywKTpVB-ECSgF42a-2J5sMqK4n1mKisNmhYUrlTnEaXLeS3lhSLdoHVsmSlhe2VDQJD9k7iVX4YAKTugpYli1A4SGiZ6sNYcmolDNl_WJfVQHGUPT8nGZ0BesWhAUHBHiLm2YBd3YnRkT0bg86phKGp0assQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=IpvL68MiTQbSUGC0d7uO52cDN9lYwcNrxVHdY3tWrynCdfxGRmrjxOhOxNcg9qH01T5JJSLSEt5FN6IYlcLx0T0f9n5YiAGzkqH8ErC5JOcYcmDPoOdSiDULl5ZYCAvDAeoJknUUNiuZ5C9jvibDi6KZSYKsJG6vT2-5gEnfZ9TkwH8PJmpr_2y8JIywKTpVB-ECSgF42a-2J5sMqK4n1mKisNmhYUrlTnEaXLeS3lhSLdoHVsmSlhe2VDQJD9k7iVX4YAKTugpYli1A4SGiZ6sNYcmolDNl_WJfVQHGUPT8nGZ0BesWhAUHBHiLm2YBd3YnRkT0bg86phKGp0assQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxBoPool509xkkDPeCQrp1GEnlN9aNuuSwK9eP7kZngOMjLfKDT3sMb4ywJOTQqYyKvte6auVfD-Fblzr4p-TDo3HU7uBZSA-C7e5jViLcILiY3b0krDi33Dgpx4Vkp3mQb4sJ5iLY00k1QtuFpRf1rpoFaPHAYq3hVD9QJ6-a6KK63EN-DVvycUyFTZQReuJ37ZyB_I-8AUxt-l3USUOTibE8Jv3bmgW7RwqiqcDHbuTLhhbXGjnDsxJqxNn8QHrY4L8iaJeQilnnxkA4YALyGYU2Az41iw1QTZBOpJ4XsfWuWQltx-jIu-nxB1VqfznpZC_ye4x-kgsJKkElm3rWII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxBoPool509xkkDPeCQrp1GEnlN9aNuuSwK9eP7kZngOMjLfKDT3sMb4ywJOTQqYyKvte6auVfD-Fblzr4p-TDo3HU7uBZSA-C7e5jViLcILiY3b0krDi33Dgpx4Vkp3mQb4sJ5iLY00k1QtuFpRf1rpoFaPHAYq3hVD9QJ6-a6KK63EN-DVvycUyFTZQReuJ37ZyB_I-8AUxt-l3USUOTibE8Jv3bmgW7RwqiqcDHbuTLhhbXGjnDsxJqxNn8QHrY4L8iaJeQilnnxkA4YALyGYU2Az41iw1QTZBOpJ4XsfWuWQltx-jIu-nxB1VqfznpZC_ye4x-kgsJKkElm3rWII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtLzzm4Wo6iIrN1P7Tcp5QgTwWgiBmKCc02rMyStBgUzKiLSo9VufdmaGV2886a1hIc4q2SfK6gszGoJdPjjEum1MDRvPhA5_MoQ9OiWsWWqAx3RPiJxFsevHWmqUjg0sms_it7YBx4IA3DDiVGdFyMv1kmeJA0w92Wlk5oBsdlI_adDcRSilt0b3rQQNo-iP506Lr721fJi3Ia7LoB88P8Gn1-CRh90ZHnmr3qPKRxe58MgnsqeKbj82lQm0F84H0ioheOeQfELTw1JWBzDyelSNy8OaW4hcmt6ORTVuWQerDwPbxncwNAFUvGL25-cPqSjEq70aGSFkobjOwFsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPi9peE6nj55cs_Nl1SWvBq-n71pseu-L5ov6s6ov27xef5kH1gLKK-2X_o87FEZgtNcBa4z0JvFNNZ95_Qa4mvY4pi4Mft58w0IfyWDaJDdZKdH2cfGp1nOSGBUScJdrkA46ntDjxiOYCUiisfteHRy5jrCe4Ic9rtw056blTdKvPmxuRyt8nrSa6g3BjXKK7Zirg9vXbQLZI5snSCPFHQ6KycJez8W3cGl4xEFxfl-B6_4LTsCZkSZDBZv8ERNvy_UEu4W-gF54YMSf5HQHv9cbIGby9Hv9w_QYNtlLW9nyjCUM_2ZSd4GoZ-FI_HyDhgsUqIVxkipFma_r7PZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=cmuVPC10EgXcb9s_ufElupUGlyo6c52RFeygLGmU1N7xB7N4IxuvlsWb_q4b4fyQwQGFJ89XInM-sJIFalEgAl1tXBx5rLhgwR_NygDyhMwNTWxMzTwCiGIN64EVEHh9S_AhpzrtLDRmYi1dWkzknxTv5SwM-ox9ClI87LjJhy8SuJzr0-Fa9mh9XJ8MnbJ91FOkpJYfBXEmXFfdEzJP4a8G1QguOVkno26H3P2jkI5XfKd1il_haUrp5ng_bXTF8N873peR-jXrUXg4NeSPmm674FJKos57sGOdSVitEbMtupPp_BFvt9KJGijykfVxNCm-cmLAPLu-wT5gPEoOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=cmuVPC10EgXcb9s_ufElupUGlyo6c52RFeygLGmU1N7xB7N4IxuvlsWb_q4b4fyQwQGFJ89XInM-sJIFalEgAl1tXBx5rLhgwR_NygDyhMwNTWxMzTwCiGIN64EVEHh9S_AhpzrtLDRmYi1dWkzknxTv5SwM-ox9ClI87LjJhy8SuJzr0-Fa9mh9XJ8MnbJ91FOkpJYfBXEmXFfdEzJP4a8G1QguOVkno26H3P2jkI5XfKd1il_haUrp5ng_bXTF8N873peR-jXrUXg4NeSPmm674FJKos57sGOdSVitEbMtupPp_BFvt9KJGijykfVxNCm-cmLAPLu-wT5gPEoOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0vDbxAtyBr8xB--cDyMpKvxjFN9tTQnjzZ0KAL8zkpSqVeEYswcoMJK3yL72doBHzHYU2_sCFxRWgZQHnTe8G7nORtjhqcA0BQQi4mgRTM3AJGnpap7RW54faavHR29uQVYLD_psj-9Krkn5rrL8MBovRAXedA4lyZxluKgBfWNRAXhv-l8Pqi4aGidIz7MK7Ryt8ihCJRjVHcvGmLuSFRUDZoDu7_rH0kCwrTfTRCCs19kUoZWKBb7KxSjECuLgfYKGupsgXeNpPGmp8LfUHeUuiYZJHJ5KdjRKeLIiPkEpBoeaTiqbvMJtmhsejNQfDPnE6KEH00jkAxXVtIZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=jcvItlIvP8ZRYdYjWbbK-6sPMKYr1hYDw_kgfURIg1AGuWQUCLr5lKz59QDK1F26Ad7CXzjrLWYzeE6Ie-mGbPcM33qw-1mStNJzUG33s7RmbEk0MWjz7Pz1jXOmOXbD9seR7R_uSbp3IN3cgsFFS5P5vokqPXGHUUaFU-xIOuZ9lkcumv6iJsvAbsi4hR2F5Cw7yIwOQWck_v1cCiUF3H_BhaSqpxq4WQHiq6y6cncmVGrUbOxLmOiKyDN0attc-x2ZjTebGFGYV55ylyYf1arnxVJ_ZpVyIYDxt0LhuiksZphjED1WnyN0oZXKjFevxtPGoyZx3C8c62Mzs1DnCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=jcvItlIvP8ZRYdYjWbbK-6sPMKYr1hYDw_kgfURIg1AGuWQUCLr5lKz59QDK1F26Ad7CXzjrLWYzeE6Ie-mGbPcM33qw-1mStNJzUG33s7RmbEk0MWjz7Pz1jXOmOXbD9seR7R_uSbp3IN3cgsFFS5P5vokqPXGHUUaFU-xIOuZ9lkcumv6iJsvAbsi4hR2F5Cw7yIwOQWck_v1cCiUF3H_BhaSqpxq4WQHiq6y6cncmVGrUbOxLmOiKyDN0attc-x2ZjTebGFGYV55ylyYf1arnxVJ_ZpVyIYDxt0LhuiksZphjED1WnyN0oZXKjFevxtPGoyZx3C8c62Mzs1DnCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=OOXV55x2DUM5VQtGekehJJB4xAX1PFX6pW1_yrCLaQ92sl_7WyoTkvcWWsWqwv0i5X_gMahrpJavdp0pvTytXo8MVFQv8z3jMtfi1gwW2Xiv1KF0ZtR4NkLuWD8qWVNece4mSCsY7h11tM1zBhqkW1cq0Kfi15TGGhIbo8ao8ujubyh2h2WOsQR-BvL1I7Jpg70ZGrEwB2ILlGXnkYqlkhyAZvUkmj8YGQRatdvRCY5o4wT8DLQvCilsHqmkAxAtlCnLsOdNIzIHnBi17ogISnRwWz39nrrxp-ydkKqObYOiRUjlYCN7vY7sVKsyZ-ONYBG_d5wiBrBrUK6u7CnRtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=OOXV55x2DUM5VQtGekehJJB4xAX1PFX6pW1_yrCLaQ92sl_7WyoTkvcWWsWqwv0i5X_gMahrpJavdp0pvTytXo8MVFQv8z3jMtfi1gwW2Xiv1KF0ZtR4NkLuWD8qWVNece4mSCsY7h11tM1zBhqkW1cq0Kfi15TGGhIbo8ao8ujubyh2h2WOsQR-BvL1I7Jpg70ZGrEwB2ILlGXnkYqlkhyAZvUkmj8YGQRatdvRCY5o4wT8DLQvCilsHqmkAxAtlCnLsOdNIzIHnBi17ogISnRwWz39nrrxp-ydkKqObYOiRUjlYCN7vY7sVKsyZ-ONYBG_d5wiBrBrUK6u7CnRtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=F-Ys1V-g8nWT0LkQYje0hHQKvZGS5SEkxSblPnP58G2jI1i9zM9UilnCkBkiJPqZnxEg-4cxJ3PlBuk7w_ypzSQ6W30ssOPiz5l9bz0vZFWXApgAPmtJ4y084yVchsX4HSlzzNgFugQkrNTsLhUqd7k26n-rfz6Zeq06a04Kjdi7TGAQHL0ziId_kym1VeO9TjCWd_mrJNXrOqmbl_QibQZocK3em36umgQAJLN2q27yROM4PLo9koHl02Pzt8B8HyAX7YLvC8ZiHlz4sqDoTMh9XqTVVWEfcygiugu4_NUp2bMIJvXEbqCVU8tOW74GXSlye9R83xW5m75G_4YdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=F-Ys1V-g8nWT0LkQYje0hHQKvZGS5SEkxSblPnP58G2jI1i9zM9UilnCkBkiJPqZnxEg-4cxJ3PlBuk7w_ypzSQ6W30ssOPiz5l9bz0vZFWXApgAPmtJ4y084yVchsX4HSlzzNgFugQkrNTsLhUqd7k26n-rfz6Zeq06a04Kjdi7TGAQHL0ziId_kym1VeO9TjCWd_mrJNXrOqmbl_QibQZocK3em36umgQAJLN2q27yROM4PLo9koHl02Pzt8B8HyAX7YLvC8ZiHlz4sqDoTMh9XqTVVWEfcygiugu4_NUp2bMIJvXEbqCVU8tOW74GXSlye9R83xW5m75G_4YdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=hYwaSfUIpBjuIVkHPvKKV7mXFVzCK4RiEiHbZuKjz2mvzZEp_w2W2RE5rKAiL9vP0E0tEApOMmCWtNLOJrPbgL_dgk1HtAxT81492nsYNDLUCoGwmCKPdpSIq4P47pXlOPb_Lj45eqk8whta400ZHBz9WAzEJwi9owRTRpP4Ljug-0FRk9-zoHd9YPWFkeCWhejlZemIUKqNfibetpy-MqujiL3sXuH_YxRZkm5LHDFE9LAkEvNPCyEofkNPCn_FDPIkH3LVSm4bzZpQXHAZh6lp6_y9cIuekqRBA_YrL8TPW3hP2Wb-VZ4WsWXRBOfV7VYcg-2SlYfMJjrY-M50dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=hYwaSfUIpBjuIVkHPvKKV7mXFVzCK4RiEiHbZuKjz2mvzZEp_w2W2RE5rKAiL9vP0E0tEApOMmCWtNLOJrPbgL_dgk1HtAxT81492nsYNDLUCoGwmCKPdpSIq4P47pXlOPb_Lj45eqk8whta400ZHBz9WAzEJwi9owRTRpP4Ljug-0FRk9-zoHd9YPWFkeCWhejlZemIUKqNfibetpy-MqujiL3sXuH_YxRZkm5LHDFE9LAkEvNPCyEofkNPCn_FDPIkH3LVSm4bzZpQXHAZh6lp6_y9cIuekqRBA_YrL8TPW3hP2Wb-VZ4WsWXRBOfV7VYcg-2SlYfMJjrY-M50dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPesQVYGf6Bgo4FhF1FH2GWN-qeBHZgtleGvzZvazSGkYmOT1rKyfuB0Mw2XysjsYmGQYHgA1eubRuGiPlPov8Jw3Fr343qo-Ut_RCVGm9dSHd6FNxfpQfl9ZSwf35Gis-wSa-06fFbR6ThQVYmWKDFJo-Z5YeoGfnu6_HQsMi8U1-STsCUKdLOrt1Z5FQsM4X2aQnQbhAAMGfL2YFM0JynOsd-Xroxm0D9eZSghEkraQKOPgftcVAqDh7ovLLW6CbIMRYismRj7e8tgIKi4itVM4upRFLjHxJqXefnlrvD8PYzRBmp6QDh7QIbb9V_K9RrmIaD0jwjAqUB3iCM50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNanUPYyL5Q4j9ieli0_0cBRkDdD_YAGbXis5MBxazW_usBBZljs-ch1PESva5Tz41Q6ysHy9UMnDNzvwSFeixX2ru0QRHTaqoGULWLPTdtAUibtRTnJpvkolyaZSJNElJx7XkK9dvsCpxnb4IbjoM0snZhrlyw2PuqGtX4S_cCGZJd_saf-ybKx6ZfayYe2UzIrT6QMPEO-vaDEGPluGuUrYIp2vgddkIDUpba7uNTCnWTBh82-QeHKyLob39SDD68_XOo2Qp_Ij-mkUwuniK5rDVuMyAm-P7nr71NGnhLEJfu6ET4WfvGZgOBw6CvixxSqqQK_0Pihji-s5AiTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1rnuoOO_HChitJbz89DYL3nUC9NKHyAlJx3Dctzp9zV9_ERbrGODJFL63MVoHM9cxQFt2K8LZt1jFYK4xhQ5Koq-fuO-paCT53a_65Fri63QRWVaWUEpWUpHB9cBY2gFVo8WqSYH9d-FopE_FXQOnpJZ3smAOHTdeE2fJZCId_cjVRla3cIUWmamJo04XBH36Ih-cYhVTTZ-0KYJ9-D8raXQJFCMRftNekVwtt_gU7hse_GNm7_i09Dqv-BUkh7bfBVu88fTB3vzEIotr99bPFJTUoAntun6nJjBjz9WVgtGHlGzB8RIwq59cba4YTUxwJ5iSP4zcCShIObZLHbVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLVH2_sRSFuEtoIfrETYkkHfmf210aoGTfeoz2lvuFeAmVub1dGBx2e_qjhvlpc3_dypnb6PYfocmuoKf1WTfwdlB-TZpQ889uB1VrqYRsGEIjCt738uMddRl-0gN6kwGErWsAjBQqVTcgSnEqFn8pRF6_WupET_HiG5gQB56JFEGqbQM7ArhZ5Na-fogY7Acpib09-Vw9nQtODXaykDC6eHi2lq5bSKxNQOvqJBYSwC7fOW4wFEBILss9vvYgybPlzGYCFkH5wTHl-1_MIne0N4rUNv5Cj9qlwvZqNpE8nFxPTn3xDQJd7VTxouQmyLqtvIe1HfoCx2jfZl44N4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Elx3RdtKartn-tcnRWAvA8dC1at8ZRasgzP_BYw27h77MZR2h8h0fWkAovCLTFq4KekgXmECpc6UXtNaB0C9L8r-1_q6a19QyR3tAdGodtSCJyW1izrRTSsD3YcTPPxUbHVuC2T6dF6MCUMSqR7JFAB9JOnYCp8IdcwUPITE33_cEPAGSnoKV40RaiPFXXlMC7wWfwjNdoN076ASH70lyielU4QlAOuVI9QUUa7_JZftDryfa-PSi19VboXCab4XIQMJe6Ge-Hry0k7XnFy-p5iAMLkyfGQUNdPCgV8tAB8WP7xz8c2yXEwp2gGiSVZdoo0C3IIk4WHdicuTvBnOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EltAVMoJl2dMcyAYe64HVcEag2ETnb_iworLCpUq2p5A23I96zllw1isajEBxu4_yndu0ieDWFcAi7r534OaDM336BqoVy2AY-o1pCtOclORP4dJPTf5Efwj0AQYA7FJyvb12fzArCjtnaS94uGf6uf2vBRubWcjhcbZUGif0YV9g1X22Nt-LfkkyFEDuFiQJDee_kHbZBEFyrzJEokwe9Cbk5GFbsrbvkaGrNjePO0cTknFGqg_OX1kKl2zxKUjO0dqryqSdWQqkOEaFBKB0nSGcE7zW3jL99VVwvvEFryhmb5fa9bw0lkUc66lEZs5QRxO98ezeQLrQ-RwjaCx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRta3KGKxTfhjmgWVm0LuDaGdFfTYSNR-vliwrPJWyx2rYMGDtA2W5aY99idRUnoTb-vubnNcvE0jFiaefd92rrFjDcYUruw41sqFSl67EH4RHAQ2pqqhdY5rxV83PpdQPghxyRz6MgRHX9tuuY4sC-t1jMYSjz5lGNaFqGwf4ag7kumSwMdNlEmGTLRWcByCj4OaFpyofsbW1qGTkjBi_Wy4vOjgEYBHjKWERcuoGydgiCGXDOKVWUvVn9tXU5JdMftA92LLslXJT6ZzWOgYqCB0Ofqj_gyQdtqCAAuO0M1lEFR19ZOQFvHv8uj1QVKusZdAukgM1FpdMqm1GmX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=m1Hi3NB5-DimY1DP-zVF__b_y-9BDRNhSTrMPhfhL2NkaNMOyWOlKouWM2K9p6gy0tkCXLGFFe_EfWJM-tAGYj7wUrflYPGFJhPYlPOAMOBBF-9W7i66XfGd0Ieg8cBubB6G_D6IYRE9ibMmaEjgqfcImDx-2JjHurUbSZ7i_PoQG_7gj6T0b6UVcyXY7UvWzIcQwKdJpt4KP1AY0cipN5G7nw8B-3-_i56Wfza_5_ZMXUSlZjMSTloi_Uj22v9GNl7_EobP37YzVSEkAV7n_pFlwTc3F8MXKpBlnmsl_rtpE2zXupX9AiSRdsjv2qTamiwHk9bFq7hkge6NaLAZsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=m1Hi3NB5-DimY1DP-zVF__b_y-9BDRNhSTrMPhfhL2NkaNMOyWOlKouWM2K9p6gy0tkCXLGFFe_EfWJM-tAGYj7wUrflYPGFJhPYlPOAMOBBF-9W7i66XfGd0Ieg8cBubB6G_D6IYRE9ibMmaEjgqfcImDx-2JjHurUbSZ7i_PoQG_7gj6T0b6UVcyXY7UvWzIcQwKdJpt4KP1AY0cipN5G7nw8B-3-_i56Wfza_5_ZMXUSlZjMSTloi_Uj22v9GNl7_EobP37YzVSEkAV7n_pFlwTc3F8MXKpBlnmsl_rtpE2zXupX9AiSRdsjv2qTamiwHk9bFq7hkge6NaLAZsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz50UvZgbBcKvWm0wi7MIk070h-bmmH3mqy_6s7IqFtBdSGvwyiJ7MFrefGjc-Ztrp9FhRuc-12yQz9wPOGunQMVQYa_MaYTucwHUknbYt-xOiNyC3cqUzI4-uqYmtzM-gnrOYXEw7tdgjnSk3emmtAsljyrXcov8HyKYfe9JsAPTWxmF0I92iyryGyaL2_xMR_9Yw3UHI5NTfKlHU8wygMIdPt5cG-0t5yqepYHCgv00pyFgh4BGMj7Pg1g1sG5jPJ3F4B4gsZfw4jUlm_BCdWyY6wxHcaPVw0pIm2EBHKtsMC6KkaqT3BcJB_0c65DnWKGEbCCfK_7qgw1-5FXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJxuQc8ytNnIqFDWX8OHKsvepyjbtiHCPDa72QkV4Wfy5Rlzgb4XfzOHpQ8Bsaq8HbOlVG0DOzX4u4kJpJxiYCHT8acp214cpKeHyYbv0g2EGJZEsd3j8GaLwRfx0xyjKdJ8e9XwQ4ZKUmJIIK6Csk_qNdYtmy8iNeCKISuhWarvg1z9c06myQPdvoN7nHqpcEnp82x-qFBHpff3zRxc3F5jYPZ2oICLgwv48hj98NfKoLpzajRuEgXeeGhop_LCyhfFzLyqsj0X9bMNj9O0Tew_vtSlr-coutmgCqX_oXyy9XeWadpKKOGKVv4Ucgrf2GNU50mQmVPkFTbsyv8GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTrnniq9dtLSNnVTbCt75y1vepKi2rMacJu8HKPLejXa8-pFDxD2l1k7-whvAFb6mkcpg2wsfQSWUWkqi73eqlQiexHFDKHDAxIp3-229a0tgzswci33xmJh6SR-tYOiAF_XrUIaARe0e1c-LqDqEhBSHKAb5f4p8jNLoCIS9MEZoSQidNYEdY2qwEHwbzrvkbmkjvzNDufqyIYqRiANtpNqzwfC8c-EZZ1k_xLNttu9k2SwrMHeCh6l6_HbpF9F-aM2ehYSfe1faKpO6vdM24-cwAE4r4e-FhVY35uFcewEfApBoznWOXj_o7SSANkC3OgQlnHwyc0VYwq93ymOcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWBX8Sg4wOEf6jIzT1J9R6pfqwjVY1RnwuU1kJMrrkmO9-Eq5TbXjzRz1QCA6zmaJFsHQNj4fnMo0GSv4-rsxo8nlNsbGcmJo8TVPQcVEdlMDvnx-ff9uU_7BMHC2mFr9hZMKyuAuDopPqtQNib7kM1B9a9J7GoD7RXzKyIRH7CZg19LqK4sVBROw-pKEyBtOmd61LUrDzoGqQpkSTxPEYqHzoiso__IzbFd4KdWDzZfnk4jQmdL77ugPwwxOh0yKMITEZFPyUJRy1WVvyAKmz_OCwj0MPm21I0lXvkcEB_6HnNk7_DXRR3ENr6LTI3ynrrGTvDn2Z-tJaHLa2ENrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3BxJiJN_IdT2pjaLp59TkPXi3c9d_E843vHc5KBJs0bXUfd6LCnYYpUzbtqqBD_mxgbevvPSzI5S5avhyGReKdFwF1JTT78f91ESWTI15o3Ch-wGozjdEWiA4C8a3FP9jwkDfCEM1iMpXtvdUq3V143kpc5EBZBJWkCfN3hcRdLyYhk6OJS5onE52m_Ft0gsGiDEhYGWlGIuOIEDLnC41EAhE8u3qfcZ9lm9NSleGHdW59YhwVvp3p5BwEyBehRIBxP_dfekF80gHTHfW7otuiTD_Ib0FCUVmk7ZVJ-WIVki0kmr67g3z2oykMRaYHmtz0XMhgW0ukb789M_sENQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3qZIIaXUY2vNzGR86RnXR17fu-s1stnxZD-eSrjUJWH3GW9YDGZbCdMwJjnl-xoqKfZP77kMulPaHZ-Wt1AdqyW63CTqK1dcoz57Eek2cjmc2TplhWPFsKpZoKY4Hp1Q5kXEYU-gqCx9Zc6EH8m3jR8_xtkrxTx6IlVJazgl3T8w2wyH66mN44qTIGXv-tHcEqqEv7yhdlIut77w4La7BBD1oRjT9P_EXKQ0HYQT23qWL_j4QwNbDF24mzAnpxqavCRhCaFDka5MnOwW_M_fiaPuU-9SpUvQVEfZJfBGBwkOflFTgMX-C8-r2z4MT_F5xXBu7xpybcxYtLFkRVRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dM4STBy_cS1zbnrIeOhzkyqbqkNRYVvrgMy1lrO66r8snoQ8NNMSDPprGFiiQak0dl0kn2LAFJhP1RO0U_fQn4iVfy3V0iUMLqgqOhu4lCBPJtuEAlnKTduzZzBjYz0T6u-lJYeDO1_VKst7KGAIE2HT1i1D5Gq5FHDu00pVuN-kX9dbM2FUWe5mH1I6dKNshH_fchdyR-JRebBMz5MuSgTqOqlehQnAKYFWwNAcJkRXiykPxqCcRrjgN5w-Ja0X68RPGrktC7uJTco6pt5XHAWHb63Bp4hD7FXEwMaXqj4iE96l_EkxG85DgJ874M5MYNtFU2o0_qdnKEdJUHsqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj8IEx5mMhRAtv7H0g9UHrURDWI9ZLZNBCdVIGchjOFa6L6cCBU4JZlZdzx8xPIgJhTcL9S22yHOUhc24Ggc5In3mP_wNXs0lZn4H0dVNOc7YdxJlv_QzW3sWNghSfwZiF2mNPIKpFoP5gYhz6_WUm66qayC3YhJMDL1Y-DcLqtM7HiNtAvQz80T4BCbqnDr_HUqguHVPnrw3I7Hz6updfYNbIZG2s-c2jpqZLn5MPVCUAac-bWB45rgMgx9kbno8yYm8YzqLZja1oSYpmminXH6wRR9Qs1mb4NuVOFAWoZDGw3q1xUobjcJE2LilwfcxRKt1DlaDNA-iksv6EvJ4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=oAfzn8b8g9_DlVmqcoq3nV5Ar4MSAuU0TDEt0AEzDZ3l1hbNE-lazUqRUaVYOiSOU9SuKBgnnA8X_X2231k6xPMRbzAerRiBbQZKWYHf3k2Cde3cZHa1Q_kGcOELVqfhsUG33_XyInMhhtAjrOQpyVKid6M0B9EhHrnyVFYnDKY2_9Q4Ys6oxHT2n2XR1JGeVIjAu2X_xhBChxkfqSINhQCxmumehpTbOV_PBOU0vz8H9gN1QrF2ct7OKKs02GSA_C49nU7tNBffFKfwI5Je_-nSGs1J_1ksnK56B2KK0Xl7HFeZGHGbhlkW6emb_ZQBLJhiOsdpn7052hxkGdLXWXImFHheaKPkaTC1nDAPx-JXzSuZofj83VdWlT526kjz9fnD-B-ST8EX9SkXPfT2uCcvyWEYbppHPcsS5zv-0UpOiIkWavGyyzMpiz2U3WW01qGkmZwtid7UHXPV9wr08kq3LunTMugK_7q3t9MZk76mUpU7Zme3C7Nd7UPb7TTxL-C_kqmnNXgq1yXTvYwOqU6_h8BlkzWQLq-Kg-NCac3nuHW5epbF_oQ75Qq0rb3PClI4BLa6ONZys0DiSMnZzSP-W-iiYFE5yBNAcUx2Mk3-JzNSDcKBNBB4o2x0eeP7dOYOK7w0k1BK_S2L85IM7iH3npHj-igelmKkM5EC2Y8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=oAfzn8b8g9_DlVmqcoq3nV5Ar4MSAuU0TDEt0AEzDZ3l1hbNE-lazUqRUaVYOiSOU9SuKBgnnA8X_X2231k6xPMRbzAerRiBbQZKWYHf3k2Cde3cZHa1Q_kGcOELVqfhsUG33_XyInMhhtAjrOQpyVKid6M0B9EhHrnyVFYnDKY2_9Q4Ys6oxHT2n2XR1JGeVIjAu2X_xhBChxkfqSINhQCxmumehpTbOV_PBOU0vz8H9gN1QrF2ct7OKKs02GSA_C49nU7tNBffFKfwI5Je_-nSGs1J_1ksnK56B2KK0Xl7HFeZGHGbhlkW6emb_ZQBLJhiOsdpn7052hxkGdLXWXImFHheaKPkaTC1nDAPx-JXzSuZofj83VdWlT526kjz9fnD-B-ST8EX9SkXPfT2uCcvyWEYbppHPcsS5zv-0UpOiIkWavGyyzMpiz2U3WW01qGkmZwtid7UHXPV9wr08kq3LunTMugK_7q3t9MZk76mUpU7Zme3C7Nd7UPb7TTxL-C_kqmnNXgq1yXTvYwOqU6_h8BlkzWQLq-Kg-NCac3nuHW5epbF_oQ75Qq0rb3PClI4BLa6ONZys0DiSMnZzSP-W-iiYFE5yBNAcUx2Mk3-JzNSDcKBNBB4o2x0eeP7dOYOK7w0k1BK_S2L85IM7iH3npHj-igelmKkM5EC2Y8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=utak-VnhEVdYRRBwxG-vA83pe-0t4eqsMK8H6BGPKhkPYSC7BayTWdnDPoGzZWPdnimeWnKg0jwoufRmBTYWxHGmHx_Jg2UIdIQ5H-DeGkTiQ2yMuUqvO6rOIRLqkJ83JyBbtGm76at3Y7WGA3Hj29OSGeFH3f_3FyZRqzaJ4T2Ypza4LJHHO94OUYOrgb_LYs31XYPEVH8qVCWwpXtP24tjMlkFhgiqTNV94CtLSVrpW03JdKDeUBOKSSd1kf43dGJ3bYmMN6m84sV-Zpgg7_fq5Di1H0T3R0Z_GvYFvwx4tImm_-R7yIXIG3Zb32utvUdoUtemUvPAbDp6LLZwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=utak-VnhEVdYRRBwxG-vA83pe-0t4eqsMK8H6BGPKhkPYSC7BayTWdnDPoGzZWPdnimeWnKg0jwoufRmBTYWxHGmHx_Jg2UIdIQ5H-DeGkTiQ2yMuUqvO6rOIRLqkJ83JyBbtGm76at3Y7WGA3Hj29OSGeFH3f_3FyZRqzaJ4T2Ypza4LJHHO94OUYOrgb_LYs31XYPEVH8qVCWwpXtP24tjMlkFhgiqTNV94CtLSVrpW03JdKDeUBOKSSd1kf43dGJ3bYmMN6m84sV-Zpgg7_fq5Di1H0T3R0Z_GvYFvwx4tImm_-R7yIXIG3Zb32utvUdoUtemUvPAbDp6LLZwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amOZIa29ZE3tj7KsdE2ns9bybNKOSQloIM2W6UsVSXdAJ5Nx59atRPZeI4IEuKXWCQLJMYOKQ-qKTQ-xSDF_3G9-z4aXsWgNQ5sJowS1-qYQaaLQO88JTmw2r_yL9f7xyWdq8nFGMhMKGjGZ_4s4W7cGxCcS2lzF0T5G-Lw2L74jkCYrqlfzpEG_0RXxyjfolxRfxUCkpCUjKnaguJYxO8thdIlK2Ps_TU6CB0nT6OHijBssLY9D8Gef3c0AVnhJmiz7hYI22S9yNLiRC0hOxbLKAloqsEY39FR3THJQmuFRKuAMtrDyIJJssaxP9wFBXIKEcBPaPMPtpdI07XIVsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN4mi7EOFuiMkC3QeFA9_xZr6tI10D4U60lnTKAymPmTRwP1U-Y5XH65bPZUsvNQY311YI0UnO6SjvARJ0tWmcEKhEEtdgOay43vsR1m5wGMc8oS2VUJQVIsfJx3HHcjrZrgjJ0T5xNXH6WbJoR7YeZ9-hCpcOKP7oI_VYZMKctF-fArJptaV57eA0NSbxz6H4BTknMctKj-5oesO1Ec116EOWwpHFin5BQjjSalaDAXSpSXX3A_YP6_bJNDXJWNyLaai3IuRUMlLHZQrRD-0TVkHg2BeCXlDobBJ_QyXHvOtEqADID3788LxMERwyVD3k0pbvu7pALmh6PPUs3cIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT_YYSxqOaoANLPA65JI8629D9EwxSjcpNNrsIWQJNx7B5tr222mFMpIhndzSdPVRrIi4hbbA7vBi54a3HgYyHzlkR1riJWDonMIwYBsgIKufOFCDDgbShtHP8HJOmRNWmQrKvcQTYa8Lmf5SmmOoLAz1BPK_WoSRq1fBcSHFxzAWFJ01UM-VO38hs8-RVRIjVK1ZGpLB9wbAQCSCxm1D6w0qZBe1sMtfVoQyuWLftOXBJffhtGL6ST_jHI5GShKI06qvQHxU_RHscFjoeFhoR0_MS46EkJAOTALi1QpyOikfwjiu4E3oQUePofF0x-Kzjdx7Q9aI84Sb161KS0QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9VjNn367qVImRi2BNe401jsBvWtqHDL9ZbaBrp9vOePBPire7OUgfM3Num1P3nVFK8SeMdUAOal1lYcaHqXHVt0R8Zj8WJcCP-xIzzY_8jTmfwyRKzZHkT96f8ifh1xOwR3MHBMSem0DWJ2-QyNaqXsv3GEODudYgKqgYfWteOajqj5L6HVhcu2dLwX-MhdFkhCr3Nj76ujWWR-gYJZBhD_YHaTGKj-9PoSI-FB6XoyvNHtn47Wq76CiPXTf8LQAZ2cSDIAshaN4Ar2U3TvKN_U6tHnaNdzbSbEU3PDcbM0o71OL8PpMkzW0fPoWevZFpWZtRHp5gVqNIBb6zwyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLEYR8tzFNjA0gGsegjMykF3nWXT2hT7kdKc5sOF9IwLJNXe-9SxDCkik7vR8_XeKQSUr8cOeW0O7S2vQINUAeRRo6LjBeOhbUOFSE_et7Z0K4PXauBV2Bdbk7WFLDzgLAIDrfFLdSt5atsQML8QX3mmHwvvZEvRqg4_ieZZfyg9TIZRw_P92LdKqFjlQ-Yh4XB8kc2t4kz2GIoCZeb8rzB2aToEubLrL67rvd38jsnfzXvhmei2_eKad_8vXGd62-R6Q7JKPsHbZ7sPbSJ2ujUiVMoiknAuHaXbYHJpb-nimLltcg5UjUTEnFFGY9KAzcgTlf6LgAjMZzoeL2uwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7nRGqR6GVV3NxIqBySfZ6EsqGD0XjHRLktJpWckO3h1UhfnhWqkKkocdMcRu4O8GIIkT4FpLggpASXTqvPZVQKafaaiJWqILPNsQNRaIXcEyUaWir-z-rKKi56FsFqG4fY6kTn0ld2h_WWD4svNnPV6RBjKL0YYKGkPipl0LxEd6ybzJ62R2FuJxENXME0FaD9-12i2gwIJxSKAE_9WSdinswN0dsaTQFzjBZRdLGFz6-NBUnBkNw5IX5bFmfYWNefOIekojGhk7fd9dxYRRLhGKSioEs4i1gB38uhxsc12ZpsNGlI2YkX21FdUbJ0WN6zcYHu6nkAYceMadFl7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s09Wsjgr7NZuvvl53A21__Y0uuLP47vbmjDALroRalUhhTUzMvjtIebeRX81Up73sS5ehU5bUw885dkVCneRwnMeMMplcBYsYKnYFKHQFtFHVbmAnG4v5zv1S7VUPu1AoDdgcM_aUA0LpyUpWKtUQwHllZyhS2QDAshYKfRrpNUQrdj9vad9FY4sGwZNc7PCtZ_Jp_vFakY2u4bI44YPAi3frHyn81EgMx8tt2T07WEOrQkEXa4_a3FjO347ee2tnjyQQbIUoZIedh2O0DogCLQoVr6kexJp_KlobjQKPi64mbo28bDp38TqJsQYvWL0eHltN_7Zq7Nw0vMXbgX9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQAvcEcH32-mdrrkKxz_uwmlQuSsJZeEZgbbPxPevM_mmLyCAt03euqLLdfDMoc8KOiZzCH0_qd-cObY2I9F7fbPEKSIrQZbg0y2KvInpmeCCZwsNeI3HhuplngbbbBOyTUljlXwflvXqeLmUnit-_AWetphm3uSLlv37HxM_mtbmqo8XyiAE_vPav4_nDdHBBTeU3oFM3i9gQnxapQVkbX4vbCaWx4aqkoYqVvDLjWffSVs1eKZL9q1bQCdq9IajDEOk6iUxgx4kZoXi_ugwiiHg4uh5i4KNzErBkvCx2Qd4RHMkhUvEUJXztjpN_6pZhI5Lz596NdgMfrmAmc8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCyv_CsyGZY7hdZfP1XZK9GwQY6RDCCpj0rlFU3fNbNMvzm73TEvPUkdPnhPPLcgUGwtKDRITFPZYRvf_xdjJoZckAS3isew1-zeFO3K-g0ARJKyPTSuFJ3xv043Jh37XQoRaTLjBq8tnUqACdez-V603lcniPbgY9-jyIfBCxyrA-jUr14CWNHkqrngEK-98icjtW5S3BEwskL1BTy4JD1gy64ZGu-FXgzeg7vUdaQDsFDNRSgE_fWYgSh_vxkVIbux4OJjbBE-bWHtvNGObaP8vEsCF2pMeXnmH68YoUFD0MYByQC1LFCZ1DBd-vGrb-pAvl0Oa-6W0PHK--Rnyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=tUVvv8Uygpn8pCwTp1AvEk3kVjEUUaByAYY-gIsfkAzuEHANH8J1Muy84MpezmvbP7aCaH_Y46h1lFUqademzUztyF-ekx5ed2phSsMO7PYtv2lPj_ZSGc0cpgzY16nTbaZd5H0jR3sYQ59j3seS5JivT47X1ULqmIkkTA8lvy1BherlZGjHVV-9UdTzlON_YilAPK-z96e6qM9G7CBYW4kQLDS4KLKXsLrgsftcYp0VNGL3eUmHx80rngXQlzDVhwul7QGmXb4tsu__N83yHDg79MQHezt-NGLn572sSc9WDtgPCtxuU1uU1BmEXqwH8q2H6qSrfv1qA2xD0EKDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=tUVvv8Uygpn8pCwTp1AvEk3kVjEUUaByAYY-gIsfkAzuEHANH8J1Muy84MpezmvbP7aCaH_Y46h1lFUqademzUztyF-ekx5ed2phSsMO7PYtv2lPj_ZSGc0cpgzY16nTbaZd5H0jR3sYQ59j3seS5JivT47X1ULqmIkkTA8lvy1BherlZGjHVV-9UdTzlON_YilAPK-z96e6qM9G7CBYW4kQLDS4KLKXsLrgsftcYp0VNGL3eUmHx80rngXQlzDVhwul7QGmXb4tsu__N83yHDg79MQHezt-NGLn572sSc9WDtgPCtxuU1uU1BmEXqwH8q2H6qSrfv1qA2xD0EKDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ6hwzl87y2YQinBp0W4wVplNtDMiFuL3sf0QjY-xV_Us8_91Vy7TggnGBqNP0UX4T0hWyHq4dCJ2nhIAX3F6H4R5z1i0fPZ3yW3vw6s6wo7TYwnu9NlhG5FY9p9VMAqypTsggGlHqc_sKZV6mxCuE_Q7K1tzYt-WZEkNfXARVvXSZ7rBGLEMdw08yOdmOX2h2qk0LJAaYszB5DiLENMS8pFlppx14mn5TdC-5VVf19DZWBGMCiolQP9L7gnI-xd3cJn__FBVOzeR-lUGPKBYvTz9JqYWPU7VexKthrqho_hRFcC7rgG_oZCxgBeZCE7tPkUVr1ygR47HG088NDcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=rJAisRmmhlRKZbNu4hxXQGaK0FP-wPUgD3OouT1eLwDHo16-oEMNYrfAajnzoH98DqzX5xLOvq05pfhBtf_-a4nblSoOj2jx_B3V5pKHaEE1ktdx3WG3PEXy3hS_M0-09LpGvXNFUEb6vAtg8dgjv_IBk3S5eOHVtrq1xNc1XoMFs49ueYAhWExUNXjvTFeOlSFewBLpL22pA3cyIeWOyThbgCjnxi6c0oAxocyt_vQT7roAD5JsyuHtYqcgj5U-Ro1Wbz5Apk_7etbH90yKuIpDqCTTz1xFB_BLOGYKL0JXL7mqdWdSD9cuPfq0R_YXWADZPQlP4jSH27fMAEFF-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=rJAisRmmhlRKZbNu4hxXQGaK0FP-wPUgD3OouT1eLwDHo16-oEMNYrfAajnzoH98DqzX5xLOvq05pfhBtf_-a4nblSoOj2jx_B3V5pKHaEE1ktdx3WG3PEXy3hS_M0-09LpGvXNFUEb6vAtg8dgjv_IBk3S5eOHVtrq1xNc1XoMFs49ueYAhWExUNXjvTFeOlSFewBLpL22pA3cyIeWOyThbgCjnxi6c0oAxocyt_vQT7roAD5JsyuHtYqcgj5U-Ro1Wbz5Apk_7etbH90yKuIpDqCTTz1xFB_BLOGYKL0JXL7mqdWdSD9cuPfq0R_YXWADZPQlP4jSH27fMAEFF-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=swoD2oxkXWNAGNp-oa2y2Cm-xMPLMUqGR3zLRixKTxpr0sxFgtpE44vO3xL2lUwj-LkkwwYao9KyiNV_26sE3Hcd8ZJLAxRTsRTjUAP4waADpo-LFYmSoVAADkIiqFfhGGa9dVac-5ARF3df8MqvMBoNdBKa0RiTrEEAn_jjxZkcAgyga5inxGmqroulSPcrSQk1RdHqr-r8bQziZS8F3LEIFItfrFNk6afiBSIDV9CDLrkCmsOYJxw7q1i3_qD4PwvpFK4kZVCE6lPh8MkVh1aAjoYR3r1BeIC2L1R-xwIYD5bNnG19yyDeUGsBUWWeO4b3GCnJYty5TMGfQvKJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=swoD2oxkXWNAGNp-oa2y2Cm-xMPLMUqGR3zLRixKTxpr0sxFgtpE44vO3xL2lUwj-LkkwwYao9KyiNV_26sE3Hcd8ZJLAxRTsRTjUAP4waADpo-LFYmSoVAADkIiqFfhGGa9dVac-5ARF3df8MqvMBoNdBKa0RiTrEEAn_jjxZkcAgyga5inxGmqroulSPcrSQk1RdHqr-r8bQziZS8F3LEIFItfrFNk6afiBSIDV9CDLrkCmsOYJxw7q1i3_qD4PwvpFK4kZVCE6lPh8MkVh1aAjoYR3r1BeIC2L1R-xwIYD5bNnG19yyDeUGsBUWWeO4b3GCnJYty5TMGfQvKJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I20uSRt1NgcHRT_sb1Kj3UpdR0LS6Vzepy2DeJI0f06hDsEQq_lxur7ApkwxE7I__WhPFdpr4smpikNKMGLKKLjNGlE0C1X7vg108pA64MLrzmjZCvqHJv62sIQKZopoH39KDCHDsDUOvzAsEdH6fXUjCj1S6bh1lKdOe_swLeJHqwX5awrttjQ-EFh4Utqtik5Pd1PABJ4jKGgvxLhPWs1XxSAhsDFra1yUJsBKq5SpJf9nHxdZTP3yw7WQ-tE7NJfSdI_15KaXbcjoEDOsnoelFVS0SC1SoUPDGa8YnotdAYMGvYOqlYHIlq3Jl3lBmkESeABNyLMbbHpFk_PIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=D9YKvCMqCxZUTMEUz052rntY9hnjD5k77U0nQHpuFl2U59DDU1sFfGK8iHWFRGR38HfItNTHSMCM4TCF7chIR7RkAph8dcrdqKtzKm9AexDKGkQUY1-zC79_kH3eNxeGCl3ELLb4LO_Y1JKFtpzWWwSVugEzfAYmrP1uCqPDt8MkhNX6t_2IOf5vKme4IzDresVz4ToaQNv9IMwWERhPeBNmSLwf0bmZ9QWDxYIa-jigIR_XdX4tLsBzJmnlHaDF34JJl1_8sflDtLRpT62G_uqRXaAC28ciLK74aSi9zCsbM-XcogybR2fWMph8w0G1r0eRv64fT6ynsvdNqjW5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=D9YKvCMqCxZUTMEUz052rntY9hnjD5k77U0nQHpuFl2U59DDU1sFfGK8iHWFRGR38HfItNTHSMCM4TCF7chIR7RkAph8dcrdqKtzKm9AexDKGkQUY1-zC79_kH3eNxeGCl3ELLb4LO_Y1JKFtpzWWwSVugEzfAYmrP1uCqPDt8MkhNX6t_2IOf5vKme4IzDresVz4ToaQNv9IMwWERhPeBNmSLwf0bmZ9QWDxYIa-jigIR_XdX4tLsBzJmnlHaDF34JJl1_8sflDtLRpT62G_uqRXaAC28ciLK74aSi9zCsbM-XcogybR2fWMph8w0G1r0eRv64fT6ynsvdNqjW5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcAGjQyPwaNnvAEEq9xbcDmzCsHvHTGAHRLFbLsfsDLNX1C3Qobr-Tq8v__K8bpfxyHYqHAEDvwUquDLYPzLEtPQ3y3wDp2nUvm2jUg_epyjQWnunejPqwvKiqpiAMIwU96gHsOvquWYRPYqZ129LDlqmyhl4rAmU1GGxdJcLUTF38jJ7DcR6oL8Wg55btCsP1PEIEuFVBz1BemYDOP4SpQ4mVpofSxXRA0y-ENk--o-DEPQqFaVoiCwM-7Bp87WGh96pf9bIX2KjplCc3EU_6M7m_3z5Yp4GJbugJ7ee3665tHIIRPeNc2hIvnT5GUtUbAjcYbrySUV3n8XVFF0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjAkJNX_Rjbhh6_mARSqxjPqCiiPnh8nEySmz_cCKFZdFvpjT6dcUGdRwMTuAsAEVvMIo9XeJKx3oIMinbMsMlYsrxEASpBDpsqGC1Ha5dMBgnZwJGCifql3LnSJ--9ZhKbrnk1aJ3nHez7K4GgqiXQEAXc8T1WjBdg7hy6euZ4wI_1CZ5OQZ0_y1ICuSTxXBroTOp1dnsuZb0Io3WQo3pP_bwD36VQEDCcJRboydpQ4RvCeg1c-DHyUjgV76Zc4yZeCEJR4QoVV610C7JeckSHT-ZObzvGlM4_vum2DNZ84LDNddvbZyeYnFlLTHKEJ_jgKc0mrfHD9Px3VbnHhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkyXAx-8RB1Sb7VCNxuIdeD-cZ4Sdm1dwV3Cmsl9K2Iq_Ic5jYluuCXW86q9iUSkktAR99oR5Ko2TGIPKTMaK0ofZHPYYvSlhaP-XjJtiETs0eXfEDqpGdAoYVmCAl-wBBZueAiEfwuIe9m9dlyOd-6xZABN9av8Fs25OITgtiiOfF8urUft-nzIUHZkxr9zSnlGDjFm3Cfy0x5ZB4wKEZZXDAplCQJr_Dvej4P4LpgZ5QHXbWDIsJqhk3r1TO_zu452o_ZHKrBuXjOiMhkgfy9qiP6V-ZMv3M_uqSy3y5IWj9pQM2C3hW8A1rk4k2LdotSzAkV-B9KdBVh3fZp6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_lNhTKmg7qUi_BJ_uskt3m2bwa5vHStcEH8aLnnIkl9f7Qw_jjbOPj2PdViSCjFZqWcQklU5jh_NADMKTxPhlxMiy3wHFomGGITVZZCc8blkpoWh8Zf8lKe_S4P0mo9PQLERBuFZWjZZ4Vn4tmzDxEvNKmCjR8AIBhVSMCSqNtDi6Es3IMAnwog3F-KDcK0ini8o0W48mitna73M7AgGfipRfNwBuntzYbH2SbcBE7H7wJ7GrIuqGGeyU2pTB_pp3oJJmpdVBKm4oYkQd_3t2pSsWUhI2riiKpOnUhlU5a6BH8jjbG8M98L8O_fdT5Jpj1NZIDDIuWcJ86gDBLXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWYRC08LnO_gpfVu3QaUrs2wKNyKLQVjvD1VopggF8i3sp1u7sDeKaTckOVNac3foHrerz2mgFT1dovltjo1rXzgajTrGtUsvODZ2hK1_TR12enLNnhgGb0pvHQLbtkIuCzpaeeOvcyG6zeux-Gw0l1kYS35QAmPtR7ixFHTsrpPRH_DuX3V7kdvGMDvk_YrjO4gg7SRAKmuS0E3uI0ctizxNACvjwxd8SZjvN4wTe_mGz6Rbml4oj4iAyTAxl97-Jco_gqAGX7OU4VUgXjg_-hjrHroUAH87hCdFEF-arUnnu0lvoD2LVqPXqaV_Yr41Qajv3WKdmrGXl8pnPr5dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snXxTh6y8jt54sDMjQCwnUagptER_WVh-XHl0Bxgp5ThKoI20xV3cYd5l38ZS24rHXjMoORjswNPklw42oPwQzyYVux7lq0ozo6UNrOFwO1JCBhcH-Su_ZMogYWcOkFnOEu87Unv2bTngnu702gi2-J8nbSi4GEQcRIF6huoEBodSk4Ch6YDGRVucDiObC62PG1yc3iDLHP6EB1RDaqdUPKbtkwbwYxzbVQPIiBD35ML7cu5xpClMGhut5G3T3QklFFYWJiLhyR78N5YBam6J8uflodrKASzkMsodmiv1YEyPeoS93_PRmAdf733LiTeDxskAP5Kq_UgQBGqmmEgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsaWZcafhG9uQzQPItrWudwOxNCm-TWYYUsJtBHrBT1GtYnyVBBR0lAASpfhhfuG87i8tD5SQxkyKeM2I-a08Wneex6YrHY3aBysGwa7MmoirwDKg8-IXiFxM0eR_Fcg19oc9SLLZYijFIlUNo0mYM2V6cMvIeuCstbhJZdr526WYtPR-sq1Wc2O_bdjxkhRHb3tJuQxXchM1744_0CaMImhuCSe7BqWqmsm0mzy0VAFHyPX6-fgSqzDjQShBJLx44ljxLQyPnHfxeflsVDHP2CbRNJX9c_10a-VrlF_PA3yqJhv4JZs757gX6NFX5JxXef7a9FkETS4KmI_ZvbA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUS2n0WhAuGI01o9v7NuBYMlSvuvpNRYTOkKpST_LArM8CU4uOwVtZZKoeoiFWB1lrSIq_QAq-kgIljjPRCorAwBANnsKtVPofcqi7Bl09f5Zu4dfd6TlSiAEvq9LFJXa1x_wDJxJRMEztobfPLLNU7TgzG_h9ijuv-ev7HIML0vK6OCkpNVdnXrs_V5r6O9DrBHC9OXA-2pjR7C7BibyAYYTgZxNoWP0RIXloQjx0Lb9IXcMxVDn9t4VAnrUmccrvoij3_mcGLMccvdG4Pn-U2XSULlXwlqE8ZNOLk8Gp6DgP41verRKD_BG5iBEv9NCAVBbn0mXJn5O4VCgi28ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=OkXTiiY0Gc5DAWQNDNieZJURnKhcA56-xQlfEos1o2B5jTYwAR-P5oEVC-rDZWnskQCNrAl4wPpJfQdEZOkAA50mORYEmODHTiUXgSKa0SCmIdZ2lN6HVvCmapAAMN8etsuYG8Y5JOU-O5Lmf2NQG4YHz2F4oh5h4pdE5iskTuhOAgknoNRAFiuyV2kAaTbwQfbGMlDKmZSoTiceDx7iEQ5FHUhAcKZTZJwGtMtW_JHhTlNe2gTrQTR4qcJcujA74TcGtP7BerQzdJAfT2N5BewYVcFGgkBRo0M6f_zYO_Z2DG4CL0vDge9N4xRBv1TR662OjmpLnr2c6LTbPURqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=OkXTiiY0Gc5DAWQNDNieZJURnKhcA56-xQlfEos1o2B5jTYwAR-P5oEVC-rDZWnskQCNrAl4wPpJfQdEZOkAA50mORYEmODHTiUXgSKa0SCmIdZ2lN6HVvCmapAAMN8etsuYG8Y5JOU-O5Lmf2NQG4YHz2F4oh5h4pdE5iskTuhOAgknoNRAFiuyV2kAaTbwQfbGMlDKmZSoTiceDx7iEQ5FHUhAcKZTZJwGtMtW_JHhTlNe2gTrQTR4qcJcujA74TcGtP7BerQzdJAfT2N5BewYVcFGgkBRo0M6f_zYO_Z2DG4CL0vDge9N4xRBv1TR662OjmpLnr2c6LTbPURqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QsmnU0bCZwPt6ehY5TJcUhxCe7V-1tl2hyN3qM5-dawgsecJ75D9Eybt5rzlNt2M8Gz-2zdr9fEo5RXYM1juZ6sp42ISaJlu3p3L5bJXBAgHCzjS5DevEpwU2vjJb_UUNNu16swwS3bgCfO24pZRytt7S31t4aVAdqKDVROIzLt_kJDEki6Jpq4cj5_aAUTfGQA_tjUOfP8c8hc3uE9m7XinX5zONjxPE9WUsJsj1OR7iFYwDCUI8zV75V_I3PdMmrQGNQqIwdE7wQdyvSBLAdciLp4dpDzUCjxEFc0tcsTNWYj6g74HXp6LoAcKGzJucSV-O30aFKDNSW9czwyutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QsmnU0bCZwPt6ehY5TJcUhxCe7V-1tl2hyN3qM5-dawgsecJ75D9Eybt5rzlNt2M8Gz-2zdr9fEo5RXYM1juZ6sp42ISaJlu3p3L5bJXBAgHCzjS5DevEpwU2vjJb_UUNNu16swwS3bgCfO24pZRytt7S31t4aVAdqKDVROIzLt_kJDEki6Jpq4cj5_aAUTfGQA_tjUOfP8c8hc3uE9m7XinX5zONjxPE9WUsJsj1OR7iFYwDCUI8zV75V_I3PdMmrQGNQqIwdE7wQdyvSBLAdciLp4dpDzUCjxEFc0tcsTNWYj6g74HXp6LoAcKGzJucSV-O30aFKDNSW9czwyutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=f9vXq-cF_bK54D725NcJOh9N5h7CKNhfSTmMckSPaU9U0QSXlEOqfvsnxwBJYAyzOOJK5QD8Mt-Car2jcIfasG-cOkqU3t0VxvR58uhRJbfJzuheoBzRznGv1vYHOpMunnCCE-n09GbXPgLrd0KjFmRjVLqNAln5zib7dYZabaejim5Ul8IuSH6lXbvatg9kbs7DOYYOdDRg4EyIT7GTB3rw9486YOCdBh-LQ7V238lwkS2uNquDJPlEOj603VAtybTQws54fzBr1eh3AUVU55kSDAKm1mm6L5_AmqzXDlaUt-MF4oHFsNDxL_hS4aWZ2kuRJ6e_bF3en1-tOy_3OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=f9vXq-cF_bK54D725NcJOh9N5h7CKNhfSTmMckSPaU9U0QSXlEOqfvsnxwBJYAyzOOJK5QD8Mt-Car2jcIfasG-cOkqU3t0VxvR58uhRJbfJzuheoBzRznGv1vYHOpMunnCCE-n09GbXPgLrd0KjFmRjVLqNAln5zib7dYZabaejim5Ul8IuSH6lXbvatg9kbs7DOYYOdDRg4EyIT7GTB3rw9486YOCdBh-LQ7V238lwkS2uNquDJPlEOj603VAtybTQws54fzBr1eh3AUVU55kSDAKm1mm6L5_AmqzXDlaUt-MF4oHFsNDxL_hS4aWZ2kuRJ6e_bF3en1-tOy_3OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6BjeWRvMiJuwEepj-6SFfonXWecalA57mfR1pxgX_X3gFqYZVBtY6O6HHfd8GN8C1RJA6TrW67OSpN71-cqbXcC_yb4bJlMnEhQvBl6C-MW4ExxXTZnx4aVGIMuCvIf3KBb2Kv6J5geVHXasWm41XnqzU23gYpOxOUW4034NFxdjJB4sBs31nUtctItpMkIhMyfE-7GsAY-_iySHXKZp73i_X4dNNcrAz-FnI3vXbgy_SUw-7ivjPPN3efAPlWdL85UT9JrIm0NLSMmiuUqAacfLPLQ0JATn0hBiMJkAT6yoWEuFTfuC7LNVYEgHcaGfAgp6PDfbRbVNp2Vjhl-lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DizfhsVHKi_opA_oeLCJj9AZNUEincs8_tCmVB7cx8viFqBt_L8dwpiMnxqRixtk9lLEH6XycPsvE2h2ljQo04Rf_gM6Xv0zwfm-5hOPP4qVTcqYQYUsqrWbLt4L-FfnlRK9MyfCaAnWErWfalvmxQb0r1hBtfyd649b_l1ytclN5Kk43f_yAukXnFSmC7LYoM6SSY4ANt_n1F4EcyD7GwMmamXRd_vW65rQw1tt-bfF5kmkAksc7z3ivYdxYRsmzUVbdjma4L2k0hcWXjMFxdwb_H9CA5BTjrXpuOEVO3CYTb1mTJ6J0aUeGfOxS9aLcyHHyXPJnzimqid0ZYLhqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6t973uxsIfJW3CCumxRH7qxLgfYEcchKRHb-ptevj9LbX3Ea0C9_CmTCseFCZf2CgQofk4roeMeyF4tZzYA5k09iNCH2hD22UKozGjTxKdykyxWEn7cdR1eSCdcWUPsSWvAsg13G0PFfZhkc5nrdx5tqKBHLG8nHO_cT4qfBIkApdfpVjwVdw_5CWz5Z236VKPKf8M3nJkRGScPB3QNTBeN7ZpBK8r8E7cZDZzsyONEIujFWjv89DI7DGt3gNPzEhlXqQRJnkDlR5_so2rJViZB0USNPgVauOVVV2SGicCbzvk2gI3TmWSWxgp-eRCJMOdpOQCjdRcWGYOHQkE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvwkPXWoO-0oVIJo5S_dZhTZbqNOS36tSw4HYiOzuAu3eLTZufgpVIOnHZD8qhqZgrMkVlUvNoM_ygVrxXJfCAwLUYmM13c7Pb32nXGTgpjf1TtbrevC5ZawxXAOyU1aL8QRqABg7-t2G4pYdVHPr3yIZgCrRV5TgAFbcLSLjEn5tnTOC_uS5OdIQPHacP9VMIxpBFk34meld2naUZ3Sy2vKPKy5mvJ1gu2AdtwQA0rSO244vhrgGx9pxzOA5oArlNsIZO9nxfXvn1e0fWY0AXAkjy_lnachZTmgE9AVpz4_r2rMVTxoanr7ZtJ3cyWtFbDZUrHPTXw6KWtMzVfMzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=jHDoNg_cwR74If3bQ0pLV5tnFpUipeDbMGrGeqcyrV_YEgEraJPCzOa0q6PxU0TZoFgkPqvN1uL3QgBamTDF28ltxb5zsUZqFbobXG31t-0ObZSNluTdetp13A1yFgqocxfBpy7Er_Zhk-_eR3tgQMwF5YNpE-aRoW9O7MxV74b5X5Fu2KSuU1ErcjBzQTdZqTcXoE31rYRy6Z3TOtyf62UamcfVk1nqs4dSViVBHOdiMmXf8-RhKs4m-_B8vfkvZcwcQtAZmGyy5swFnpa9M2yBUnUDgqO3wyxJ17EUaCWD3TLwWCwjp6OxJC26kqJgI_GhjplHAqTn3xOg8Z6asA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=jHDoNg_cwR74If3bQ0pLV5tnFpUipeDbMGrGeqcyrV_YEgEraJPCzOa0q6PxU0TZoFgkPqvN1uL3QgBamTDF28ltxb5zsUZqFbobXG31t-0ObZSNluTdetp13A1yFgqocxfBpy7Er_Zhk-_eR3tgQMwF5YNpE-aRoW9O7MxV74b5X5Fu2KSuU1ErcjBzQTdZqTcXoE31rYRy6Z3TOtyf62UamcfVk1nqs4dSViVBHOdiMmXf8-RhKs4m-_B8vfkvZcwcQtAZmGyy5swFnpa9M2yBUnUDgqO3wyxJ17EUaCWD3TLwWCwjp6OxJC26kqJgI_GhjplHAqTn3xOg8Z6asA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=bCN-bzaiWPFwwo3ekw8SVqVdtbzjbS17Z14dJ6afUFRnCu1ZDnh6rapEFXTLdIbWZR29TVI_vt-4hN1nAnnL4OBKzOR26tZTicsky9nt2oFS47D9sfcrKg0BlIist4h95jngs03AyZgJkhOie8fgmKII49iNc-VfoZLHQVBvG80wpQe-IdrqCaX9VqstcPnuMtdTW4Uxaj_hFoPJxCvpXPHjfMehQH1bSU4dX6qqiAe3sCxjgZkHwY2fLbyqLWEqyAtGt1JeYUj7RK_b3yKLpz-pngMmI9-7hd7adD_iYWs1Z7G5gM5_es8GUP6wfjwdVpGNWWOTcbf57zrgQCO87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=bCN-bzaiWPFwwo3ekw8SVqVdtbzjbS17Z14dJ6afUFRnCu1ZDnh6rapEFXTLdIbWZR29TVI_vt-4hN1nAnnL4OBKzOR26tZTicsky9nt2oFS47D9sfcrKg0BlIist4h95jngs03AyZgJkhOie8fgmKII49iNc-VfoZLHQVBvG80wpQe-IdrqCaX9VqstcPnuMtdTW4Uxaj_hFoPJxCvpXPHjfMehQH1bSU4dX6qqiAe3sCxjgZkHwY2fLbyqLWEqyAtGt1JeYUj7RK_b3yKLpz-pngMmI9-7hd7adD_iYWs1Z7G5gM5_es8GUP6wfjwdVpGNWWOTcbf57zrgQCO87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
