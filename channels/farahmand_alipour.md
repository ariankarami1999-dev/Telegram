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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 09:36:20</div>
<hr>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm9QMm5wHRuy6EKHD-kdwjppZbtpx4S2POhcJyiT8bUvPZ34IUHAv_Zj-hp-I_5JMWFPTGdo4NsTqxmdc4YDdX1E2h73mwMu5Li9HahAjfUIJu_XWUKg2GzNaWooUIHAAQTAzFPuPoYKKpITSbMuzepE3vWludCRpj6JBOi1nJE5utAuLDBnjJiDzOqj_tGnxoSwWDqLroogjy1xH-3PvwQueGTBZ05C4CHpXBz_VmJWJr0nOZ522pRuFTILguWY9FywEUfScUk2JtiJotQ1R9Z6bq4w0FAkjGCqYH8homfR-GW4yBw7SCfoIKMMiLTHMbeLcH3pVm-g4QHumdQjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDLAmLMqntkWAq4FiR4rftfLoSrCB-Y0gRVwASiMkYwNmoN2HtxDA0h8969Q0pEz_yXE7XzwgA5cLy6SaDdKIfxpFHBUf-xm_fLJuAFGfwfnfuBtAm6qT3sAn_7nG2oWl8Ps6hcnCji2nWrX9YCk4NHDb9jq104sfye91pbNRCGfdiDo8nw60xfPsjiyMRNmnoadADlvppFLNLvyEjcQYOTLgthuVpMbhEu2qM8T-49_H9GV_k7abPe_wHF_QCDpzBBv2KZBef1XQigbehFX6sle8iA0FOBoRwZvebejUFfjyRkLQgUaS1JLl1LnPZHsKJqCUT7aIiVbxdAtXC__6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPPFuosB7B7NFMW16cRyhpD1360JavBG1BGsedE7lpypkZRH_ZFvDygBxjP3004LCec-rW2D4tSGiZlt4AZPh4oLTAaDtDotz6us-ts3TVg0GKzWD88fJ6Cvr-2LZmQI6TSRpnXKh29pk0rjKkNXuo6tECw_pTr1xbjadXymp9R0Rqb0re-_mMHA1FGWxR-ut7-Y8pc4qDQUhHQZ1AfZBWlhKzNBgPKY2VTqMcMUI0_uF9zpL7svUdL6Gfn9988RfR3Vc-hKOhPW1nl4xVaoVKZ0wZrXL6zEJb02r5eqF8apy6bTWxld5hAhypgb5P5ISYWeBoLeEIl8t63iISMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=SvOC74CdGCLe1OC3COZAtQ1AXqCQt1mB_o1kS9WDK1T2z9IGeauJzKaIhurDQAShGP1vjBC3xO0MfwLdzhhPYBgJHl-CiIAE_G_8Hoco0qv00pZPyIUyMBxclcjNq23K9TjMWSh5TLPpC8cqYVHdik6onVpVZPDfxaL7OlFgoU_upFNm0gHDeHRT0irZ3wGiw7-NnDly_JTnOHnkEhdKqCrbdv01jXc0gDeluTQd4_kz7HRPQjzwv0ch4Dvbb7Lhq5GJh8VezMlMcXqjt4NcnhpNwt5TNoLCuYON58fF_hlqEFbwTD_G4mWcRb9vUkVIUWxFY9hptmvglH8de6SSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=SvOC74CdGCLe1OC3COZAtQ1AXqCQt1mB_o1kS9WDK1T2z9IGeauJzKaIhurDQAShGP1vjBC3xO0MfwLdzhhPYBgJHl-CiIAE_G_8Hoco0qv00pZPyIUyMBxclcjNq23K9TjMWSh5TLPpC8cqYVHdik6onVpVZPDfxaL7OlFgoU_upFNm0gHDeHRT0irZ3wGiw7-NnDly_JTnOHnkEhdKqCrbdv01jXc0gDeluTQd4_kz7HRPQjzwv0ch4Dvbb7Lhq5GJh8VezMlMcXqjt4NcnhpNwt5TNoLCuYON58fF_hlqEFbwTD_G4mWcRb9vUkVIUWxFY9hptmvglH8de6SSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV10PVqRRD-H3Eq7r8izeCPoFfHVZ83Rd0hnQHygco2dA9DIJK8rkqG78_b5Up323mf0uptwkiTPmDL3JkKlIdCldHpWNDmy8rXKIIm-ftOhXh0V6wpSmcg9HAGTZbUtzRrGhLmsYffSC4tgvFZsO4oD6WpGzDIzhajOCMMusmvZyx83ZQqN-n59gNg8O-jqhOaBT-tt5qZWADkzMn-1tAyPpZ8gPXV2_E_CIT9wOF2IlUW6z7xvqXcUB9lu7QJuh2aJFGmx5HOo69M58rf0Djzpy0C39OcBg3fKp3qiLwIg7sTbOj7mIwBfYIgmETfqy4aI-E_5swtkBpEUNqYXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmD7YB4iZ7f27X1laT7y9bm38g_uMbuDw0Tt4hXLMPmUVZFMQ2-9gUJuF_VaAAxcsf3vdzTMQ4BbtfzItrRXQDsUHlMqrnpthvQEH-DwB0D8t_qp6ihKy67SjFLhCYl6MiWVf2et2hxWKwJ_Ikv3uB3qTVWDRQ8xSwOfK66pTdUQPo6b0VD9oYAq3BK44Pk5vowDGXKEEtQKWuQsBGCkO5oG5OrbioReLogZSEp2jtIR_ZN1x_Fg9qCV7y-ydYP9Ukjyn8Iju0vroTMDpTfVs9AAsP0WfRRyVjRAppPhO7rACRSbV6Zco8_eGSl9UtIY_apKtQqaoYQt7trxXzjQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIIL668BtTRGHWXX6NjqlxzZF7dYcGGKfsi_XLtvsBv_747_zzVKPplhJqxI3jpCRPdngb4wXozRdZ-NFBfqk5UUQwF5Lc8vDjrs3Igo5cwe6rHx2YuTSK8RpTuPKVScI9ky0zNnqmJyxS0Gpj1R9BuOJ7NtqNxiXeZoVAaQUu4_gsAI8f6qdcz7XvYSA_UjoyTH4USv71ftvTKGyksBrK0PMUGEYiEg4hANjROXZgc4lmxaHdDcGXr05ACOANijDqI3fRNilj0Kv5dS-aZVNjz7etKq36tIfkr1eCycsOIQSyVgvosFc2ERYT5SNlMwwmOmjEDYyfnYC4NVcoYeEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=EADOFr2gwuRKfb6a8oUkxsLKA8rUX7Krk5_QKZ5AUom0XWsE1359jU8wQ5KDt4mmYy2vQx4IfC6n4jaybBUK7LBB_PEk6MUtdv6Yoa2pB1dnuex-g3QVNwZN7GIAUWggcTb_rgm2XFsxVoDGtp1BPybGJRQCDKnrkrBMlFCFWDHrIfwM4tJvPpd6qRDRJx5za5In7XMZkaWGCDOzocSBGd0jf9huB8R3nn5kIdNbEwioWbmnURSnoOwXhnTUhNUdc5LqXVEsutgtwfQAnMcTucTMBvNG7s1pA53XD6tTDYWCe_MWGkj_X1lMVOpgQABSoGdvqsK4RNrSzrByjdXlTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=EADOFr2gwuRKfb6a8oUkxsLKA8rUX7Krk5_QKZ5AUom0XWsE1359jU8wQ5KDt4mmYy2vQx4IfC6n4jaybBUK7LBB_PEk6MUtdv6Yoa2pB1dnuex-g3QVNwZN7GIAUWggcTb_rgm2XFsxVoDGtp1BPybGJRQCDKnrkrBMlFCFWDHrIfwM4tJvPpd6qRDRJx5za5In7XMZkaWGCDOzocSBGd0jf9huB8R3nn5kIdNbEwioWbmnURSnoOwXhnTUhNUdc5LqXVEsutgtwfQAnMcTucTMBvNG7s1pA53XD6tTDYWCe_MWGkj_X1lMVOpgQABSoGdvqsK4RNrSzrByjdXlTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Pd7wR0YWlZ6Cgn7Ze6ACC3RC3tKywq3HjbaGwnJU2PEeVvY-L1OGr-YQO7DBNOLGB1p61aT6ZQxFUgEmH2V7vmB1OZDseOtLZ8VZRJnpXu8v0UxBVKuy0MTlWwAo29Urz9I-9zrso2fkCaORJcca_wMNaK56YrU1PrvgPV56293tK_wh0IvA_HWcikRiBG_nRUW8m7xJRb4lDd1M2q87gXQoKnnNqvs3jOR_8qw2-4GyI9-MBUi5c4OuHHIG21CXzmYJn9gdcflZS5R7GzNX4X246j0vlIWlSGkqMACFgwaFA_jDL32-oehpGuNZRLhVEhq9Wy9Heb8I7rHGedVJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Pd7wR0YWlZ6Cgn7Ze6ACC3RC3tKywq3HjbaGwnJU2PEeVvY-L1OGr-YQO7DBNOLGB1p61aT6ZQxFUgEmH2V7vmB1OZDseOtLZ8VZRJnpXu8v0UxBVKuy0MTlWwAo29Urz9I-9zrso2fkCaORJcca_wMNaK56YrU1PrvgPV56293tK_wh0IvA_HWcikRiBG_nRUW8m7xJRb4lDd1M2q87gXQoKnnNqvs3jOR_8qw2-4GyI9-MBUi5c4OuHHIG21CXzmYJn9gdcflZS5R7GzNX4X246j0vlIWlSGkqMACFgwaFA_jDL32-oehpGuNZRLhVEhq9Wy9Heb8I7rHGedVJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcK1O98eMFCcdbkzh1HQxb_ZDlHRq6O-Ft-CBb4H32-kT3jUiuL_YxHimODkr18KiOWpARMs5VjRet134367MHuqCnVNjztk_dbjNh7-PN52-O41cSOMOUHPVKCtdyoC6cdwlaam6hgW4v4aR4nMDbjdKoo5AUCvJd5ntrc-uSjV73jX4EkmAWIsuW-vd9AkpLZIosfsKYjcXRyZJ_OZJ1GzFhwISLqmn2F-_BvxqxzBHepPxV7qRJbjU9B8pWzvbeMx0J8y8-ors8W0dQdKyUxAypOhivcBNLCZSZjtFNk1t07jMyFS-o4Ye4UVB9plamm5IvyHbD_fuAIgL_8Dug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7uxKd7nrK2MGLzYN0qcgxF7J49bRoGfPo3R3ZQw40o1f4Jb7snqknPpr-yTrTiw8qTl-IC7B1HfkIea2yhLE7ZlO5bDAtFhK3rssOaZTs3DCZAE7LhgbeVYNBhF4PS23BBglyUESSlxrtpU0wdY_HLTkcyy6g6HSpAcYwSLyQHrC26P7aFLDQSpKxqfWCmaZ6HFs7bk2dLo7tRl5KoRuz_snoVYnbJX71P4NMEipaoBZrfOUyDM3Qb0JA2BSb98fz33KU3XHW-ED_xx9s3EFm1c5chOAeKoUDQEzpIhFfmMuI_WAZKbAO9HGAUEKJN6eAPopoYvMcNIwUhneOT_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=CT6XYpSHGSBfM4De2bpSkgTiTfG8-UdhOtnH0xs85VQajl7aiUPNG7lBxNLDB87nN1EbjhoQdeAPk9bGwC6TlSoR19l-2xOUFYEQpfw0_t7AsCOV7ebg7Qv2XcgWK_GwXcP_a4Kuogl5qYANd7NKeFthrf8pDsrF8IZMLk0H9ildq7EhekN9uI32udBSroc6M4oFjajSVGyJ3oV8VfVcmKa2qUNwJyFMtO0Cain9Yv7_Wr_f1F5daUFstwupxX692hWqPCl48N4QiF3Y6jdsspa6qvOiqIKM2Et6vVlZY03Dku0cVTUGFaI1cYoBPxAAklxIrFRwVDsDDg-RQnOsAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=CT6XYpSHGSBfM4De2bpSkgTiTfG8-UdhOtnH0xs85VQajl7aiUPNG7lBxNLDB87nN1EbjhoQdeAPk9bGwC6TlSoR19l-2xOUFYEQpfw0_t7AsCOV7ebg7Qv2XcgWK_GwXcP_a4Kuogl5qYANd7NKeFthrf8pDsrF8IZMLk0H9ildq7EhekN9uI32udBSroc6M4oFjajSVGyJ3oV8VfVcmKa2qUNwJyFMtO0Cain9Yv7_Wr_f1F5daUFstwupxX692hWqPCl48N4QiF3Y6jdsspa6qvOiqIKM2Et6vVlZY03Dku0cVTUGFaI1cYoBPxAAklxIrFRwVDsDDg-RQnOsAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8ZS91AXY5JX_wsxhWICah7HDMjen-kzhO3tvVZG3AFyK0tbO_YW9zKm3qU_jVy7GlIHVzQRC356PQh_w2_ufmpe97Mz2CgEcJl6ds6PMjz7wDRa1_Nl75W5fAsOkIcB82YOjlf6nMqzw7dJSrEzBpyKZ5W46cpZJXUv0qk67XMfGaYJyhajaMKnCXcteyAWx7JuuGlCT7cacv9bTLHBYYFwpppY51nEPZxWNAyM7ed7Eb7XLoUzK9kbITgA6TA8QMeH18up7qDIhsfQ6JUvajRFzQ30iDMdoed8Rl3eGKBJGAw4-amiwgFRyjwfCOglV-Z58ot4TiU2WiFMYL8U2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=WjPBWyOZR8PQqNEGRc26C4BXACf7c4_WTKo2h6PUksmxX6g2A6zBR39a-LDGChLdgAP9njaXnEWqqpcFCuhhPxAlqwczFuROw8o6-MtM5UZzQ8kD0BW4QX6daYCmGD-dggQb3ET3Rhq8eLhi2-LQuWyfHfC-8KTm0umiMqvvANuz0FZXDoxgd5OojYZZjvcAnqki1gxUVBr1aXLVgOjaB7hC_6h2v1L8uLMIiNXeUhUOdh0w43ctAgdAC4_B3SN-HEWWnqgHC-irHDGydTBwfq7mmkXZ0tQkZ2KTKxViI1l41mWqoNB5ZhB4Sy3nX8oWjx24HgEkCoTVqLOiA6YRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=WjPBWyOZR8PQqNEGRc26C4BXACf7c4_WTKo2h6PUksmxX6g2A6zBR39a-LDGChLdgAP9njaXnEWqqpcFCuhhPxAlqwczFuROw8o6-MtM5UZzQ8kD0BW4QX6daYCmGD-dggQb3ET3Rhq8eLhi2-LQuWyfHfC-8KTm0umiMqvvANuz0FZXDoxgd5OojYZZjvcAnqki1gxUVBr1aXLVgOjaB7hC_6h2v1L8uLMIiNXeUhUOdh0w43ctAgdAC4_B3SN-HEWWnqgHC-irHDGydTBwfq7mmkXZ0tQkZ2KTKxViI1l41mWqoNB5ZhB4Sy3nX8oWjx24HgEkCoTVqLOiA6YRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=PGFPW9PhrVXQ7mW5Kxn54amL6NBZAr-Qo6GbAqnJkZ8CVL5zZNANGAJpzDem4RTi-zCKU41c2w__w5VFogvAHl5GYMQ6oVZB8JfjyjMPAGR0uthN8J-ebBR0tt_X3Ybn7dKKtL8ih-P8OONhuOvC3ugmSlACUk2FaMFTXDcdzQ5lUW0GxTyyMe2c83yRPz8qosJNn7_ft-5MgSGUy0kjCTejRTofUkrOWxvqX07K964PQXn57p777LgbFEpeTdGtYEGK8cgmQHbRz6gYeHTL7ZKpSDjagolb0aEXu90Q3vVUn70lJNDgzLqncBkQ35LW7auv3qZDDGSoucTkehmnbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=PGFPW9PhrVXQ7mW5Kxn54amL6NBZAr-Qo6GbAqnJkZ8CVL5zZNANGAJpzDem4RTi-zCKU41c2w__w5VFogvAHl5GYMQ6oVZB8JfjyjMPAGR0uthN8J-ebBR0tt_X3Ybn7dKKtL8ih-P8OONhuOvC3ugmSlACUk2FaMFTXDcdzQ5lUW0GxTyyMe2c83yRPz8qosJNn7_ft-5MgSGUy0kjCTejRTofUkrOWxvqX07K964PQXn57p777LgbFEpeTdGtYEGK8cgmQHbRz6gYeHTL7ZKpSDjagolb0aEXu90Q3vVUn70lJNDgzLqncBkQ35LW7auv3qZDDGSoucTkehmnbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=O9oMkVhlNsFrCUxuemAxXYImFTYIDRNowSeyN2B9NORt1o7hmiN31l20pJZkep55FhmkDjOwZ_lPF-Y-wPIky7ztL4SvFUqDKmcqltKzuES-FvSusp1bIjCDx-mNuYSCqyAWqBFG8pONWBEzsfc2WV0gEtpTZQR0vqrInAmuD0b6TImvlQ8R4h2_ICkBTxuyLIxrMo1tMXhm7apKJE83PvHNX1XbJgi0lgED8-sPYl-Shx-EkYx02KHBQsvbNcX_1WdAie4WLHDU-8Csbc6fkydNg91xJBnOXcd6eRPyOW8dYrDu4NW5k9cmV4ZxpOEE8Wv4y3Mso8k73zVF3TsiGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=O9oMkVhlNsFrCUxuemAxXYImFTYIDRNowSeyN2B9NORt1o7hmiN31l20pJZkep55FhmkDjOwZ_lPF-Y-wPIky7ztL4SvFUqDKmcqltKzuES-FvSusp1bIjCDx-mNuYSCqyAWqBFG8pONWBEzsfc2WV0gEtpTZQR0vqrInAmuD0b6TImvlQ8R4h2_ICkBTxuyLIxrMo1tMXhm7apKJE83PvHNX1XbJgi0lgED8-sPYl-Shx-EkYx02KHBQsvbNcX_1WdAie4WLHDU-8Csbc6fkydNg91xJBnOXcd6eRPyOW8dYrDu4NW5k9cmV4ZxpOEE8Wv4y3Mso8k73zVF3TsiGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=slEr3nQBHjS_gKlaFyJQDx2KUsDqvwQfZ2dTBAT3A9MhhqGUVHkZsAZ3sUKEt8a7xobmaGESmjjEm2b_QjS9d4NX9cGlhF-s1N8U6aKTU2Rtqc2pWf3lt3C9In13svovKm5VrhH_bxX_jSfR-C8JUF5phEWwIOwWOUm6iQSF8iUt6OjZn2ky80m0E649nu5XbP4sF37qe9rehm1lK5Coo48rpyBazXWoTeVdDm2QwVDVhgklVdIGtg4ixoOkWRAkR1cORfPFysJ0TJHFkZwugTc-DQBy_29X9CLXacavPDqzVKMG88oABQ3FFvFqHF2AWzlPtLWIMcu8RwoD4cqIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=slEr3nQBHjS_gKlaFyJQDx2KUsDqvwQfZ2dTBAT3A9MhhqGUVHkZsAZ3sUKEt8a7xobmaGESmjjEm2b_QjS9d4NX9cGlhF-s1N8U6aKTU2Rtqc2pWf3lt3C9In13svovKm5VrhH_bxX_jSfR-C8JUF5phEWwIOwWOUm6iQSF8iUt6OjZn2ky80m0E649nu5XbP4sF37qe9rehm1lK5Coo48rpyBazXWoTeVdDm2QwVDVhgklVdIGtg4ixoOkWRAkR1cORfPFysJ0TJHFkZwugTc-DQBy_29X9CLXacavPDqzVKMG88oABQ3FFvFqHF2AWzlPtLWIMcu8RwoD4cqIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNV8amTKPintvEF2xsyrIueigvlvfH7d5QWSKcdblIMiUbQX-h34NO-oRSo_dmoBRbiw9uBRb0IRe-wwc_K0iFQtSuSkEQc_Xz22e26mqrQEuOlWdvd40DMpJohBs21CXg3uSFClUFa4zjpPBegPD7uFpKUpfYT-byzadOp5jp3amxDqa-NhXHrUZ6oIz6_5veZQZW2VcPAsHXBO7pEd6rWZlZtyevMgsyupPwRTfU5K-dqFSOWkm-8a4KI38i4V-ka-RN2Q4YkVXq1hX7hf4_YiJOVIPLy4W1lQKDNMb-BMBTtwF8zO2ojvNj1ra_VNb5YCxGeKF9GjYsgXlhIPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb_UkV0sy9Vp_0GfUbGHPeJTWKwWNbGSuSsfYq7lvkJ5mhrUJktKiylX2AI_kB2dWS1p5unng9MtjP5yJFslhtISVKYiDic9_y72w_KsEW05S3fPFx_FxDg0RyWrEoVGVMWOzNm9HwW_vxi3kab9OmSO-SW09fSAUGveLMA8CMIvmNTSuOf_aT2Kk179BZshKLAB53TC798bdcOf31Q6VmtN8yk2g9HRmBOlak2PnJ2fYGAghK3rFAZEM819YwOBehXVyRWOSyFvdQX989hXG9xdN40yyUtVLol4ZSlZRE9VJQmMemlYp2AuEXjBY6HFPAOHy754MzMIhWX0ue2o8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4m-xyfvEHL-VrGPFMV98vOkmH8uojvtFojKW6ZWq8ToOVeYBWjbJ2Xu_Csjog5DNfhucPN7-_W51gXedsxlITpM0UryxP_O2p2tLbxdCXWM8xTOB6-0qhWnJtx58gE8h2Ehhj2rseyoOKrf1BuyU8piX2maog4Sw0-nO98yluB5Y4Sovz502nDmd_U-ztCriHV5XglyU-OOJ-ThTu0JI71iblkO_RQ96JVbHrvbR27O0UmZbcW8bNbB5McnUWTluHd2SdlsIPJe0tLEd-1T_RNC5hHhpwWSHL7h5M6QAFfLYmF8k_c-shbkVipNzanfhCh2J_p3qlGlkGitgR_jWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQEtszMkkIwY10Rk_oocb_G6A6zFRMqVtltp1B6aqtjCMLdRIRCpDGrED2_naKT1MvzZTDSS7S9jFOoQdJTdgmIxVodrH-eqRpQ382VWTZxj9ZAaKpXwSAwisZ2JWCIKAN_K3UcFiHAIQsMEHolYwppyKwl_nyShkdZGIxupZDQFJOws1k3hxcOwSQk2Ra4fTqXUBNqKEox3JsKpPkwfbF9FGloRR42SiQfyQAS4LtcgEF5VTt-I2KHVkcpV6c23atQ8taejUo2lhUWI5NlJZSJGAIhiidO5rbYJgKxzrRdixBBMQbGiYXPFjSY1cGQnZf1kmCT6WnH_IcZmmiKguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaWIzA_ZcaEAZndnVs6TvssAHuWo5aO6Q5t9nrtu96L1GSRLKP1RxKOHcA9NwsBshxAjJHGOWDAbfvVOYpenMaDb6HTB-xsTV68d8TSdsqzdh-dtMJskAQMvXZ-z2DwQWFMu9AeFzmDvIVBBs8VCy5Fym-5GpsTyUdTd2SjUAIx5BINT6xKuHqEbwjmoCoPHj_iwSCIrzAERdys0zeTz2XpVho2FvzCxqpqiuiQuEB-N1isG5lIqGdTIbk-erfW9KzHVDZgodGzyeKYoit64gBqt5TrHASJ3GECfTMJpN0cmS_aKe7BwcPkgLrLSlD6TNUf9UAfITryaJ4Q3ZNFfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if7TZ2T2hytP9HR9OJyyttSX_BKaSibbAwhyy3sW3OJivRSFj8-Q9nQLS_z3Y1BfUjRGCGgc-QkxWN5WIYgpmKLt56GnsvyydbdMS3gXSw3NKWWsWaniyQkJ0tQFVkEiDj98N0Db_yz4nwtC9QOZmXjVg211iG3bEh-RMljWKhbRBh8IgY8qSYo1_ggf1JZwB-E5g2ONjuqRxZWTO6UGkqFNZhMo0J7B9A8ezARDtwPhn4b0X08bFReElL48aycUUgy2MThf85peRRP2tufhhZVa3JCOeHrRmEzmXd9BTYKwf2iorv5HVu2nxsyIJcDObiCbWh7HOoAjVGN2YTuong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9pmtLkspIttwj4FlefFQkQZrxUotvzIQYqyoEpHznoGeIZfzb1Bnhjmdn6Hfhk53oLGmh4CxsrOxfDTnafudmxjJ0uyZrHezA9XB7feoMPtAcUbmT_e_yU5Ua8-dXukXqU22DK7mG6qD4xUXNw78VRUt9SZ2-nCDnA6PTf_LmYu4PKK5yC2BOtARKCithjHETwWqzEwSx4BhCdtD4AxA_bzIfVAQurm_Fj6RbvJPkPfjVi4VhfeFIZVfPWzC0FDcxGC3Ql_K8Ldvu71qCRBlK_EX2oDeuYyWd3jnP1aDlNHg27MGEduBgsRj7QzlH2hv8rxCJOuaAGeAetjEQi4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=VjC-eh1FfW-8H6XquWaMLsnj7d-GpPYTa89cK1i5VORJGqbVWkyhVXS5iLsvjC4kyozrhfthbBl_dk3YyZrftLOKa0pScqGeJ5AJsRlnoy9S--9bDynbpMtayNl_1NDDNCSWhgmipnHYEpgpzGwSjyz3mBqtA7TMB2SiO8FSBkWs9OcWbzuN_gTibqBUZMAz907JNbq077VQofBTYQ-ueYz_Nhac1hVzQ1HLzhqhpqdF_ogVdTGzvZL3cKJegSIv7lZVy0PcTR3kN3CqNziQ8DeeV_CH-K7smrYGhZiyPycxZ3yxjK71uw8rAvhIgoONIzmyRk5TIJ2v6D8XktR_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=VjC-eh1FfW-8H6XquWaMLsnj7d-GpPYTa89cK1i5VORJGqbVWkyhVXS5iLsvjC4kyozrhfthbBl_dk3YyZrftLOKa0pScqGeJ5AJsRlnoy9S--9bDynbpMtayNl_1NDDNCSWhgmipnHYEpgpzGwSjyz3mBqtA7TMB2SiO8FSBkWs9OcWbzuN_gTibqBUZMAz907JNbq077VQofBTYQ-ueYz_Nhac1hVzQ1HLzhqhpqdF_ogVdTGzvZL3cKJegSIv7lZVy0PcTR3kN3CqNziQ8DeeV_CH-K7smrYGhZiyPycxZ3yxjK71uw8rAvhIgoONIzmyRk5TIJ2v6D8XktR_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ips99VkI7Xh5_mqGejZqayat4r5TGVPSZZKJFpii3wb_Azyh4_sKKr-AuhT8_w9sCNguQ3Qd6DUxNMeGKv7xIniB0gt6bNVs_iWo5DhyJAtvGXUkBIwD0lgMyLuIJwJa-UCnTn1XAa3F1_m6DjLzpgcSo0rpA09LkqoKpBI6MkdcstY_rqnFMZOcx9yc8ljTdz731t82_WUlVqP09ZlAPHWpzX-jZ949BFiG_CZXWYV5ChNjTZ37AJ0sG_Ga7HRHbJTdC_3rqR-hZUop6zuYHYk3tfbHA1mYYH4DEJ5o2_nUFd_jKxe-0L-F7Eep3zRuS6txyzB9mEnuRYERCXwmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/me_6f8VV9YbEkYgXdE29c9Mg7ADwMST5sd06MS1we0Y0RfOf4V0gxCSeDy5g1UQeNvc8-OT_bf59PTUGaZnuoVRyUD4xlzykiFZMtB-10uuwHdOrkXa2xTgdgrDK9daP_oIYMfziO7Ft--7aKJ4ZMRjIeLQGmO8qKOJiu_oUqCFEhJqMdKBy_twbhc5ylHBAPxMAPU5ZLw1h5FZ5gP2-M6u-PP2aPIY7_8InxZKgPJH9kmjsFBaVZhB9cSNY9GJh8yzqY_yPcrOj1ZZKCkbm7-1rL7fFhT83mpqV-dnV2gWP3LdbHLm8aSWn0tNJcjiOvqsE3WY0e6RthYJrvT06tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2XbVa1TmhMvHX7-woy1lNZm3grm7FhHcEbSYOvXkwojywAw-lP8ZGp1taDnKBCAb9-i8Uu72VNPBly65czvsh5lUDgpOVtoBAySEBA77qBUvDOjdN_--Qw2OKBo08BzxQ90c8LQ6knco6wHw2V3_Tmt7Z-x0hbblLEukAdkcf8ZQVDKwIcmHrK2t_I8fy1yCO3tyFxStetYKsajN3NI3fL3iHOw04ACjvuqiWdkUEzydgUUB3GtPpchd-7AWX_cB_EXaAIqpzjrMdpZzvrlb6pgdG0f02K1FDb2LQj7Q7wvDY_7if_16-vCiV2Crl5FaS8CNeUwVEEYknVSnb5rUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsRGw06Yb1NqKJPanl3OfP_x31iEEzElyZM4KzYa6qR_PoHmM4_JLZIzZRFIHSeOjOCwbYFZ3AohRMEEtMmVv1CJfop7nKLo7GkoDtlmQBXBc6N4lkGvKNOy43A5dTwkTQtXD8B_kbT3XBIKyvsojd-fq0Iw27TaBUcMsgy-bOTa2_hp7RqSldXS6-XJv3aJO-5gxOJH4MDCarBaNipF_DPoLrXE7nC4xFgb_X46Y6n_ujyc9z32NfaSMiAx7Jm3YxgJPYlLRRykeisUq4AneikH7CM8e1WuElvGd9vv3nnbVAhKPLaCxb7qCTOcU86v_oooG7DsWaDgd_yjmIv1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJtHMWRhdA_-p2lt69nHE6rDAa9V3ZDy6rr5SGdMC4-utOqhciwXpTeRcu5bMkOZ8mmTKKXnGizI60qK5D66A7T-6lxGxUCvSmlyp-G-Fpp2Iitk2wlnu-P7giXqheTtmqagfVmULQgXzwqf2Wt4mjIPFPmPjF8_PCSYecTSz3MvjFXs4rrut1sgFvk-u0Wl61xjBBUx0n5y_5o9Faha5CehsD6e1_kqmDahG2ZYdl8nVhRi4LsJh4yiGCbU7EIJaB_E4PSLTx9BBsqnslUKhMnMZK8ffwWDd-v2joLlHQfDwMC6sExte0-JD9-JcaZZ8H9baaiT-KzP2VjiB5G8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD9qz3IxUAvnjMbyTY3F2pUEZrkPiUQzUifzuxQqQZQ0dNFJ-poAClvUTUD4iPBzeyGxASh7Rl-oM1w0mlFz2ENbxGZD76Ac7SHeoTFjU3qPN70RSQ3RgQbPrKg5hL3UuRzqD1C2pMwDAKsoEtISqndysqwrSn8DRRgRUccuTPJKfwhySXDOHPOdkKCtaJqAh0myAO30aiXd6hky2WDFDkHt4IIjurTYRPAr-7Z_faMJbD8xnkSrQ0kjP0LNP2g3D_XVYcVH4382Sd3UpqYgpV568djKDw6pZtCt8a3NhDTLE_JgHwi4mnG_0gr18XsoQjMNmkzp3wVuvoGw9-gyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1ryBEauDGabq7mISVp-7tjvWnk59tmEAHRT4IfWl7Ytfle61_PBirZ-SdUywTiVvNvDscAXAQnIjxIM2Nu-wVpY9hsGiVe-mW7LW040mAnzUH5anoGa94SLTcxi8PicruaEwolvKbFAFklFWO6ba_9gn4yWKMAJEGK0UKfoZyhhOSqm6IvSSeWMGpyIeOLk_BAE5N1IbKHRHa2ZypDzmF6Uj4yfQXcSRGp6iu9jl2A0p1aYGpTsgNh4zotgYMrW548NuwlZIkXNQjfKxqodWNytSh2eMaMFwAdXK8O1CTmt3QWXl8qLtl7iI9EZKsmmxusDY_bdKwSGu-8Mz2OvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHNJjU6l9FgxQLJolVx8RKl-cP3rYPKvtjMG9D1mfn5g-y_A1XaKqUewIjYBFSG2mDHSKAJelwbP4cBHObOUQnulxRS9uFRohGRMSKRYemrHWXne-07Etn2W873I9A902_d8_tyF6J8WRNZmelurZskyDrqoQzaIfN8E_dIY69mKg1QKwidCgx_u040x4eCjY0n2DgT0jKHa5quRogR5QyJ2uVlrT3GikL260P41Kppw0ANEgtlRtScez6C_uMz5GjEzp83FPdPSWG7BPT0d0tNpNUA9Dw5_eW7BJw4raUHqa0zzn0RhKEuaPRs42Wdnj_3-ZGHYyhxsQ11wbfRR3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=Azkx6V7G19Oi7jyvWPh1p23fVwnINKRc8zYEmamB-js6IpLPe6jMm_7hWsXMPMSsJKTlIKwdgPf_Nbz4zmFDSVVtu2vgkypuaFYbXKISEEgSgmtgzWWIc2TVl9QgsRs6OBEMfjnHS7vtj_qofHFs91O8aWV8LPP9HpKHLikW_hLPRKFUXj1l0qTySWc8AqNu0inxV1Ye4Fv2vC8zvpL0CYcedkE8n1Kw7VqUyCaQmMNU71KMzR-lBWO1SqDGoUfjsID27E0ta-LxkXPRds3K6B3SlpxGrDtsKHDuy0XfpHxzAA2hXrHxUJYxzenecA-5yYKySIcApxuQPvGT2y3e-2Lo0AO5vhd5JPEzls7nY2VYAb-dCAfbGCg3oH0PM65kxHHjqI5Q_pi4nyACZTsDxSdHiWvyGJGS-NQcNXBBLCu4fy7fuQTbbR5iAlz_Y4ORdoX-lszCupNQGSB-Kq3_BmAWDyvTQb-QUNwWG3Ffd1IxpyOIc7_emRV-lm7V3JiVv6uDJxrzOicJeDV8PTpXDBj9IMw3H-hzYrgviid8glBWL_V9l4DEga_ZbwhApYKmhAUiV5nQ17EftomNJr2Fks2wEtimDazutOI4n_wGU1vcgAPOwH4-w8FL-yz9HFggjd473ue8mluf0md2uTVsgqr4aGyyZDYK0zgdgxdUYpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=Azkx6V7G19Oi7jyvWPh1p23fVwnINKRc8zYEmamB-js6IpLPe6jMm_7hWsXMPMSsJKTlIKwdgPf_Nbz4zmFDSVVtu2vgkypuaFYbXKISEEgSgmtgzWWIc2TVl9QgsRs6OBEMfjnHS7vtj_qofHFs91O8aWV8LPP9HpKHLikW_hLPRKFUXj1l0qTySWc8AqNu0inxV1Ye4Fv2vC8zvpL0CYcedkE8n1Kw7VqUyCaQmMNU71KMzR-lBWO1SqDGoUfjsID27E0ta-LxkXPRds3K6B3SlpxGrDtsKHDuy0XfpHxzAA2hXrHxUJYxzenecA-5yYKySIcApxuQPvGT2y3e-2Lo0AO5vhd5JPEzls7nY2VYAb-dCAfbGCg3oH0PM65kxHHjqI5Q_pi4nyACZTsDxSdHiWvyGJGS-NQcNXBBLCu4fy7fuQTbbR5iAlz_Y4ORdoX-lszCupNQGSB-Kq3_BmAWDyvTQb-QUNwWG3Ffd1IxpyOIc7_emRV-lm7V3JiVv6uDJxrzOicJeDV8PTpXDBj9IMw3H-hzYrgviid8glBWL_V9l4DEga_ZbwhApYKmhAUiV5nQ17EftomNJr2Fks2wEtimDazutOI4n_wGU1vcgAPOwH4-w8FL-yz9HFggjd473ue8mluf0md2uTVsgqr4aGyyZDYK0zgdgxdUYpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=NHEz_4UO-aKzd7Sr6727zt574KoRydBrbxZixDc9Y-GHOvdwBVEKcekdnTC1S-odLn1_IzRV1S1EiQ2hXroWQAsPvNAXq2KDeUiaf2FbtFw39sYLVM3HLrQ1O-mknI4s4c6JAffeHre6-Mgf2MgJWKbZW-0W4t1Ox8aBM4ih8q1usK9Bg3q7rzddNLi-p0lammQ52mhZjMM3EipgW74p0xqMfjFV21vR8Dv4DdgCjv6YnaY3r8GcJdCYd6fcTkBB4NI74oFFOfLRzvPV1uYV1HTL2NrNChjTQLZPNfFwQaOHgAqHuN_eJA7lp1iz-HJNIfxltsSM0CUrOwHYf7v_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=NHEz_4UO-aKzd7Sr6727zt574KoRydBrbxZixDc9Y-GHOvdwBVEKcekdnTC1S-odLn1_IzRV1S1EiQ2hXroWQAsPvNAXq2KDeUiaf2FbtFw39sYLVM3HLrQ1O-mknI4s4c6JAffeHre6-Mgf2MgJWKbZW-0W4t1Ox8aBM4ih8q1usK9Bg3q7rzddNLi-p0lammQ52mhZjMM3EipgW74p0xqMfjFV21vR8Dv4DdgCjv6YnaY3r8GcJdCYd6fcTkBB4NI74oFFOfLRzvPV1uYV1HTL2NrNChjTQLZPNfFwQaOHgAqHuN_eJA7lp1iz-HJNIfxltsSM0CUrOwHYf7v_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5c80auQGJQ-N_fMukAdFMYTaWJ_462AZSjKar3ZjUH_jHo13IiJuP8ANUUUeahp3wFY_1WsAfoiuPuLsuFkrgdwAuEHMH4YgwUpT5nejbVwLwGxjYOfdHt_-K50EfIO8UvPB_K6gFjuGHF0nnPgMd6bObPKSyZF7qm-5V2cq1K7QT_aBE4j04lzqlPn8JoGETU4IHvd1TRXS9xD90B2wB-Ix6L2nRhpTCfurfzHIRu5JPOAe4353mg1OFdY2SoMF6vMpZT0TPW6LrSPtpfjcA71ILdzN7d7lWmIuCJg6-xgiMMeabUC5G22NQSN2QBeiPd_35dfKHOP6FqSowd1VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhswC0qA4szplSOyHK5CsFQNqq9RWqxmrAGnVNztb4IOYofwI-w1_0VCXxvGZkkof5ba1WmVkxQvfajo_acTuYedH5uoXYpg1Yw2sSm7HPWaxayUzv0zHzovKmg30GwjN6L1u5KS2JKB-xgi3RciyYm3kpweAvOinpxSLNIXlbqlQHYT4tSwmvcSCXT4wTAa5FYY7JuoBcPM5LkirDl1ZDO-bdasTIhYH28zogvjgzYBfGfJ8PD5flfxcRQ3ch2rQzkold4pE6NUT7L5khu4ySBlr5H0MGqOP6GrxzTENZeKzmPx8pD1wV5KqC_FPnObq1PMZYN_FODArkpE2qKnkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfNUY22SeYzxxxHNLJgBn8HuHiBUwm2smVPzGnPHGsmSd0aQHg1gCK21hU9o-5cwMSgbZqfASpMwFVhNwzwp_SyRGVIQYMjugBzogVEE-Xzo3H9vFym7GUn0Bzv1fhc_2m16rNVau4tL2OJai2jC9XceRM7rQPP8bvDYONlgJxSsv_wp7ksNDtcQbMbRIC-hDH0od60b20GmR0p3_40792oJMa42ywyrnOCxdcAadgIbGq7Shged38pNJNuatqzYn6t37Uo7w2VYXwSDI8m3uPgxa125M1NZ7tdlke7W47aHybP-z1o758l_vL9Fr_5a5o451WH9C2g_MSIIWisAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKh39hzBApQPRxrZ2BAjV_p1gzMM_s9FAfaC_ELq_Jwdj55pnui62rIQHNeBEYle3Uw4ERodK4MkBQQYa7oNpCWWR2uDrHSDHqxUOAV4qEggL7x0nHey4K26YGhgJHfzK-S3x7XJ4ofXC-RRv6tTmzwUsDSxh6OEpRNkKFOgVy6DNL8yEGNXeHJr56LlcuuMvjntBM3V9y7RHfiBOj6peokNc9BKdYFVOxwZin0Ei5TtmXc7fax2UBr6BXW7CeRYoQQKHMcaDz2XtKLzTT7Z3tv3AHMBlkvhMe07AWHl9NV5HyLXcyBOD4WMI9KEKOmrhHrye-HW6W_7bfszqsfOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKbonfp-fkuZK4z1xIc_Gax4VaABXHPcCKwxv7eVbnv5JISnKUXDlgZ8NuYWvM7A5Zsxll2zgsdRFjD_K5FBqO9hBN4otPbzXuVjoeozW_QaNLW66dDC49FitooMwQXnRAXgrDhio2GYR6zpJT0o3WA2gAmbR351YguEyL8NQ-wlc4qY2grU5QYbCePCu-998w-ndVupGkHck8N7Nuykg9-Vxw9uzpTwHHxsn1Xlv1IUpZ2bitVgqeqMdeO-F0EPE2JIRZWSYp-cKoTOsZz-n9TyDHNoKDttZEUnp7uWQKJUfSHW0083nGnzDks0afPa_445qxY_mvczm-E3bgKlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ambBGK5I3jX2Sqx8TidPFnhfGH7XzMvs9L-d0Es9WYn7_TX0-lfJGjkgOtctDxNH3qZcvXTn_5YWaqWw03fby13AI9hvJ5zkZZzfGKqvZo0nXNMQ6DB94vq6KAG4zNXMuYrre02FBviYPf521zV4QdUIMI0Yr0MBGiIdA9dNSuwncnJXhMzznzAhPsxqiiXQMU3aBdbXZCqsX-Vzn4RGuruRm1dKzFBmJ2kkfeb-yYiGNDKQllFPLTtD3IPaMOK3atqtdBjXaCSXrCMwQMR8b5JugR0XGpKAWeqdieV3SW1-8HYMSJ80lXECOw1mKuy6-2hfR-bqEj141oDg8nx65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3IIhGYjWwpyGq1HDWJZvgkCulttlizaQQZ6BfQ_g1mXCGWr3wzkgQ5T_XmkAbHkHW6tUSQq2aog0lByZi_CUWPoeKu9zctpgVx-hT5ai7XKM9TuP4afXtM-LSU3xfIrpyiKOSeqlxcKX-LcczfUJuytNCz-8UcM06txGNElzy8WyZTgzeZeMB7Iv3qjzrdUWdOLozBFZ9u9y4AOBrgzRTHIE8WzI7pWIlsl--KPO0aBpav1nmNohdj32wGivkqXcJMdFurufKqgg-tpHmmSNWWVAMhggIEyC8EoUiF7tMij0YdSyNFXXEHcVX_P7oACeCL0PN29ENgX6ZSaZbT2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzY19fKF9Q92ssVyQC0tuQOyUv-sscNm2-gJ4EYF7t486pwqKU2PICe7rQwaYhjEcqchPSm8CzcT3S_3z6SOY2qNPmBDGJLUGzSEkBgZH8r7K0R3umldSQqKkRZhxCRKsRI7J0imdWcU26dPzoYeNgJkY3yYIQX6iUuHJrWdgpa7MSiJwld5fYO-JngD9sSR-aGgQdfnHKHaUk5qATSRmp4HDzOSx4AFiv1zjUIwsyr-vDfOJiwWQUpC1Xaw3ztXA4iDyOFfXU86b7M74YKjklCUKRNiSbI9Iei2IcNb8KEeFBD0wp3XDJSoJdY47xN6DVo4MRNKzbRh_MybyP2MtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwhnUA6JXd7Ajdr2EGk7xNKCONxJFKCO1sw8TjLNCzmaXJ82ltTzeK7_wtiyX4TBE4SS_NjMZbwfEP14pvAUL5cJcKeC0e0fSbCRd4bG40maZawbwByIM8F5o_KWtD__7BSvCldZY_AvSroHblAZW0Tj6Pq4Pmmrk4HRpsIs0nTEbmbq0NFKsr9tGLVzt-DptIOk6DFRsFK_0GDsmQoBoeWIvoJjuSTd8sIGGA3p7rVpy91x2rmHbyyJIdKh8ukLvIFDdnYsTo1gPDvKwUFbnd8vurS9ZImqyIu8pufIzELmXV989Ts0lT3LG2ltQcHKHhyX1_q-m19PzvPTpcVPTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=hEOO-pHirYU3u77W3-kuEpfKVKTz3iE4VcanEdhGSV9HQJ6DTo5IDm_L4AvDg1eW89ZiFzqpP0O_HhR7Qf_4hp5IXezI6J-FdHI6uTkgcaFJTTWMhxT6lPyar3bPxkj-ptjZ5SUonHurpZzwYUvuczaXu0hLn_kM9Fhp_10q6ZJtNyHPxefo5EnhBmBZs4Y7neUnZ3nNe80FLF-_Yl2Q4SHep8dZCNRtvsHMtjcTPDPCBC3_1vREpN2geEYaCKYVa3OBYBmSwRAQfkTUWVynzmIdXxNSDGO1ttJ7zJvL2D4xczQJBDBy40vRQAWFnTKXmu7SZq0RcITgdEv5v0da3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=hEOO-pHirYU3u77W3-kuEpfKVKTz3iE4VcanEdhGSV9HQJ6DTo5IDm_L4AvDg1eW89ZiFzqpP0O_HhR7Qf_4hp5IXezI6J-FdHI6uTkgcaFJTTWMhxT6lPyar3bPxkj-ptjZ5SUonHurpZzwYUvuczaXu0hLn_kM9Fhp_10q6ZJtNyHPxefo5EnhBmBZs4Y7neUnZ3nNe80FLF-_Yl2Q4SHep8dZCNRtvsHMtjcTPDPCBC3_1vREpN2geEYaCKYVa3OBYBmSwRAQfkTUWVynzmIdXxNSDGO1ttJ7zJvL2D4xczQJBDBy40vRQAWFnTKXmu7SZq0RcITgdEv5v0da3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6LsXCG3TV8qrUBtqjesk3kQ_gfn-PfO27SNsXSun_3wlv-9qn_tC3QnT2di_NSXSKLCHReNgNrl2OA2hNHg7xyqGLxAo4r060W7S83atFv9Of82dq-I224hQzal5BBvVxDSS16YWYpOS24KQzeSrGRAc5cs89xJi5fptv7LgIHJQ_TxIGHbh5YCCfWLCoSjHcYSCmutBdWQmexu_RaJcplVTE-fkC_xmAmguJ4-EWOPxsukTuslloCBJ0Ib9EvwNQR1fa-zdXWMryeRqpE_P9sPgXL3YlXalEazPNCeNZkNC9veMmkFQw2lDJFAqhOdKNCij2EYHnSqMFhWlqWJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=WBEdzf0h_WtoSCDBgSAqq_3Sy9xm1WaAKntmC3AEeFSyRSJZS0ocsDTXh5MAE9OHued2mdp4s9IElZhixC6dNQ40mPIjY3XkxRS4DXyOsSsrpsUSUW4WLQBM35oLPAUsGPMxS-8Sp1H7276MRT0al0IdxEYho4h6SoIB8Hi6tmNGufQXiS4y3MVocG5-NmT0Wrqw6YuapRftEDgmJowfffjG8YbR9tWDFcLHWNia7Jjrrg4piedh3c3ekBicRfUBglAKIjLHUY9KGcWakE1jFZ2Y2NGDJX3Hjx_E5zvRWrz38JxjgVoz5YH6EKqL8PV3FyRVvz_ex_iFSJsfM_tniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=WBEdzf0h_WtoSCDBgSAqq_3Sy9xm1WaAKntmC3AEeFSyRSJZS0ocsDTXh5MAE9OHued2mdp4s9IElZhixC6dNQ40mPIjY3XkxRS4DXyOsSsrpsUSUW4WLQBM35oLPAUsGPMxS-8Sp1H7276MRT0al0IdxEYho4h6SoIB8Hi6tmNGufQXiS4y3MVocG5-NmT0Wrqw6YuapRftEDgmJowfffjG8YbR9tWDFcLHWNia7Jjrrg4piedh3c3ekBicRfUBglAKIjLHUY9KGcWakE1jFZ2Y2NGDJX3Hjx_E5zvRWrz38JxjgVoz5YH6EKqL8PV3FyRVvz_ex_iFSJsfM_tniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=iVsSA-OuOw0bQkpyc6qpm0BCazo9BK37nkWOrt0gNn7AvvlQwIU7Xyix6yd26FvaAmThTv3L7T0PEaZta6clWOlnM30Y8HssucU1eiVxrc-VHVMwBQLx6e0brRiSQaNqgxttf6yKz3cuXfXEvOP4VEemVWA4gqWpfNhk6cmqpyeKv5A2PLcz-XzgeKFTiXI_K__w1iIFIdUxKK9kRQFMKorCni8GEz35C9mw5iq42gaHas8hGESrnR6R8xEvlzWmTTqaO2hhLY-oyuiWJgXtuGh8e8vwiY5OkRZoi_L67CL_1EaR9GqpTFQM4FJjBiW1bOaoE-TVMWssI-o2gBvhuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=iVsSA-OuOw0bQkpyc6qpm0BCazo9BK37nkWOrt0gNn7AvvlQwIU7Xyix6yd26FvaAmThTv3L7T0PEaZta6clWOlnM30Y8HssucU1eiVxrc-VHVMwBQLx6e0brRiSQaNqgxttf6yKz3cuXfXEvOP4VEemVWA4gqWpfNhk6cmqpyeKv5A2PLcz-XzgeKFTiXI_K__w1iIFIdUxKK9kRQFMKorCni8GEz35C9mw5iq42gaHas8hGESrnR6R8xEvlzWmTTqaO2hhLY-oyuiWJgXtuGh8e8vwiY5OkRZoi_L67CL_1EaR9GqpTFQM4FJjBiW1bOaoE-TVMWssI-o2gBvhuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stAtcND0OXM59qr1U6SyBf6dR4iNoFDwwKflVu7wh1Ks1YZguL3Pf75UanRUS8GQqjdZc9eFloi9XsdZAPkCijwOIFfpnNWJ-3oSWhOFXQzXXsb6KdkghC6f_Dowe4Yegrih04NOMq55yXYnTrn35ULzEYuEHONKudYWd9Fv1J11fnYcJXEbnHYNaEfO0ckAFcztPsCyQAwu4ncLesLcClUu2EVU1Yut6fCs3uGdo6ozXnhCM-_h7VOnHCZh1VM2VXxzWvlB-ee1ChOXShuMu31HR938bnGjEOpbqja2f2ztYADb02zQ8_TbxntSFz4Ix2B7MLYCJ9Zkj4UqWrWyqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jk3vVlQWeWKbze4rEefY02jK7sW3rI-Ymate6lqSRkRnEYfjxQgb-JrPVyUaHIwTdhzBf1AtEU3I25bbo0OT-enizNylTfpSJS3R4dTLcXk-I5h_sI1vqp2q4Kz_kmt5rlNx3kNxyTwMA7CIUpMC4KEByLQshdBFE7shnmNCNyZ5xQ9ShwOtbMVkTGGgcRLCGDpnLKk9Q9qOzSyJSNTnBLlj2ENjTLinRjs3_-e-lQtoeodimsTOFTO3S5qSInHviHFd5qETixd1M1lwj2WMTIIwvL8jkRhgKjDH1rqzRklaWs1BD7oTysBB2Tp7Vjp2bQUhd10X6tl543VP4_yphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jk3vVlQWeWKbze4rEefY02jK7sW3rI-Ymate6lqSRkRnEYfjxQgb-JrPVyUaHIwTdhzBf1AtEU3I25bbo0OT-enizNylTfpSJS3R4dTLcXk-I5h_sI1vqp2q4Kz_kmt5rlNx3kNxyTwMA7CIUpMC4KEByLQshdBFE7shnmNCNyZ5xQ9ShwOtbMVkTGGgcRLCGDpnLKk9Q9qOzSyJSNTnBLlj2ENjTLinRjs3_-e-lQtoeodimsTOFTO3S5qSInHviHFd5qETixd1M1lwj2WMTIIwvL8jkRhgKjDH1rqzRklaWs1BD7oTysBB2Tp7Vjp2bQUhd10X6tl543VP4_yphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvn3-uU4YWt03xrA5A-d4g7325UhfMmRegeH6jcHwpb5VXQrSdxqR1Pbf6iSOZLpUG8lGQonYmuVDbZFfaaze407Q8pki91Ce8SzjkMB0IQC8KI6_GFfaSwEJVM2Hl1x3jMoPoGDIluWusBkWTtGlzIauwnf-6bziUp9vviuP5R1AsEwsZBf6ulOQhZwkGonTwd_qti5m9a3RJj2k0WzQ8mQaw1Lv8wqfdVcyMlQfN5diWX1F6wZYu8RJ-P1-OmbAv_ciHjVS0aGuQxa74X1CVQqlf_wUyWlgCBiNr1QRCt9Yo7BCIfFrmHEAPPR8H0G9O-qLPCC7k2p5qgQQADpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax7rhuzXJlVOrDuj0xjTik5w2H77TPe5x2GUZoMDTKAkA48E91L31LqJNsLlNOL9C5gtx0xyCHV5H6sB3fVnkEILtCl8tVO3eZxDsYgH__bpl1KeQqEKKr57m9f_SM52YDVy0dVJ8mFhgjaZaKrdRiQiwUwl8G6nSSXX0znRSWtE-pvphpf2hd6RpGDfI2h2I9bqxJM8J1JN2Tv78FsKJL_M-Ak45E8be_nmOIdgz0cmezP3yRNDxuiN_NyoKeTkxUGnCVohMERdva9v9E5rtg9c3zJ7WAlLt63Bqs1XY9Z2P3ndEIFoOKjcMowVngwCfE71vgz41a_O_qMuXqL2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIyb08YTeDBdCi2iP6Xia4fgserfr_2mR8_S7ZF7CCpiUcM5JJrnpqyZoV2P7CQGc8eb7UuzgdB1BnM5jDTEtlYqKlBdp9FsI0fAzlJAa2d9FIHcOkgnVcbWNxCEJ6IFzZpLApub90sanuZ_0j9khD6rVq75X9zRO8cjWs1CGudb5B7Jlorz3apOXsfdCf7eyzULCX-mNfLxwAVjtVbRfTzHkVFKWXSoRtsl7al--agfA8HloEaUh3GUcvld5V8p-SwhmhcSvlvOd0zNVEd4aP-u1_54PS-KCtbLvoRPwot68GcmrKNYmHgR5fiFvN02P8RXhm2bwjTtT9YxhF9y6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoZfn_NHSGVMHnClLJWQ3RMAD7hzGhd-qLM5GJYjZqzgZizM818-nSg_E5CEitQn26eXE7AMKaVMqHhuRw0Hygier1MRR2H0xvw1jRrkreKIK3kzAY-3Y0Ybl-0rnSoTtEVf6t_bapUWBCNWz0Rz5tbIJ_w0GM0Is0g1U1340FSzzNkZLd9q7Jz6igbCYISc_U7_BZAHucEyXieVkmjLJmLdb_LYEdKvDn6mEhlDEmr35VflQ3HsUyu8sE2NzSvdHREm8lRdxr0H3e57dIwSm2WuE0gGkLx8r-AhGKcbrauf1dDNP-dWi15pP3kQoBqUTF6ZtdP-WuuC9-iYV5FinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnYUpgLCwfZzGcuqwQkHz1vhKWHrnh5DeCsAvDcEfqeCWyjpvU37gL16D8VFpM4IAuZtAIzW2ipYwvt0TW1RXya3tfl5wS3HFV6bsNqIgN-z_9t4Yooq_uw0al8ps-RfkuY00bzeO-u8BEFimiEQmk6USD0eOzo56Cxand86Fua7Ey9V8uff5JRlO0W_Psj58dbavC3aIVF1TK0UhYbe4NjmPv9U6lSRGUVrXnNzo6paTS-sk2LkYeZNCNTF_HMm0yHu_tFNfUupc647K3iioEZKImZO7q2hPvKxYhSBcA-k4yHmPvY3X6IlMhKV8SONc-rMRR9JjQkE7s71u4PDkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuXQ7PC13zkZYNUceMJp-1P7vxAGj78n8ASyCdZlhxK53-97weWKGf8VB7Y7cY4BYiqyITHhxxvt-ekRnZQDsH65sxobKcMIBtb19Syt5u6pOeK2BYd3-cyH8jF5xP02gNmKCErHHsxdA5SJPpqO6LXRGpDJQJ-go-XTQTh3FwIXtztlOJxu1TrXzMlNg34ubtB8rLBHAMgr-UcS5qQbEyLOeDpkBxVXdibVMc2vZLD9oaylYItYtKw6XvZm5H7QGrUhTFMhEWBnj7e8iLobsEWHnhDP2dML_-vid60wXPfuAh5j2AsqQ1znYum70k_G__Riznr0eE2dsUczbg0PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTUuzp1BKbb12tLN5lsFE4uMBAlGa_YY3AxK-ezklb53tBB-KaV15oZkc8ox-ZZ6nqwuIZFp_KYL1PCR2X5YDlfVKE4gJFPuI9cv0x7KcCTfBECIBp6dF7_E4K5ew_gl5OQZJhPpof7H2zxgCeb0c439SZx3eTQtsFJVMtNc32dGfflQ99AhkTOZPQPh-hhbnW5g6Tsbbn39hJ0uRw29kQkQLCMJQFFnu0R7FFon8pM8hliPte5BOYxMz9iaLSHsCaASNJ_07E9oNF7IOpcwyvamkhJ66hqSYEpUwntmh9uiRO-5khqWe2zcMT0WuEUDF_oYZIxCeoBGngIcHTXyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYVUwywY42yN4ZzaqtjJs6Sq8k_v8lcaLa3_EFElwKC5KuF1dN5zxNqVp_3AgDU1uHb3EL07x5NqMqI2BPLt36Fu6l5uKlbHIL6iVlwJL1Pxs5ygeLMLmsa-fNoPL1VTL2BEpWhR0xXeBJ3Iktw816V3JEZ7mkZ2_69A5x1JC4vzTUxlGYRZjR9NG8lw-QI_Nzp6lrxjWWiWRLThouxw1_VohaHAVZ7cl447RuO0nzqwp15Uejus_n7OQjKMkJg2xhmmxVdc-MNZT5kTigD0K-Fxh-15rUkuHFsjUxhGOQjqV5phIlXMJhjfFh1kavujX5Vv5OumKMv6bXU1Az3NXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=ra0NiX8_TzeGY1zCR_0CAOF9yF1Tk9EetEC_uA5Uh5dQx7UtfDUdQoC-eJ8QWaTbVNC4-IvYDQ8rT9sZd0HqcIoFltHOVjK2i--hKSkkEhz8x-pzIlpeCh_Dz_WFXBpOgds7kQ1ldN-X7LPwjsADOWFnJx_euaWM-6bV6NiLz2uhcYsZV1juT9jPyb8ZTcF6y5ajCNLOixfRFP6dWgRtRKcJwS2mx6NXx0y0vkiodMBIa2NBKNJ33QJgGghXug84oRoofyqjYuNFm31gQa3TdiWdNnpuuthnjsAMyxoJwi0831FX9wQRzC65ze7RpHaZH_d2MNdpwcqmv9j5mdRlrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=ra0NiX8_TzeGY1zCR_0CAOF9yF1Tk9EetEC_uA5Uh5dQx7UtfDUdQoC-eJ8QWaTbVNC4-IvYDQ8rT9sZd0HqcIoFltHOVjK2i--hKSkkEhz8x-pzIlpeCh_Dz_WFXBpOgds7kQ1ldN-X7LPwjsADOWFnJx_euaWM-6bV6NiLz2uhcYsZV1juT9jPyb8ZTcF6y5ajCNLOixfRFP6dWgRtRKcJwS2mx6NXx0y0vkiodMBIa2NBKNJ33QJgGghXug84oRoofyqjYuNFm31gQa3TdiWdNnpuuthnjsAMyxoJwi0831FX9wQRzC65ze7RpHaZH_d2MNdpwcqmv9j5mdRlrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=c7On68K6MVf0gROXvSteu_h0zEVUqnke_rVP6WNJhy2UU7-B_inC_GcQx9ArW6TbLDSeQd4XHFgleDtlaG2H2dNRgnweUWfQ6EJVA2ApIY0tR9-zNyB229SLQIEdLo-S5RJC21dpXJ4N5Aa4i81myoNhV_8prPdYQX7wbsGWGOEKbxMQyqoAMvuF4nUNDAxg1vfqlH0AcAq6qK8ty4aKDGm5bOI5-yKwHX6U2rOhQerfg-rxhsrHZWp0Ij67xmFi2JbZ4loFRnPAKllQ9D_AaJQUiBGA3qDuwFksyHgKOx9OVvQUKEv_5LH_BqlnL-BoEu4Obv2TX9b7AvOzPWg8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=c7On68K6MVf0gROXvSteu_h0zEVUqnke_rVP6WNJhy2UU7-B_inC_GcQx9ArW6TbLDSeQd4XHFgleDtlaG2H2dNRgnweUWfQ6EJVA2ApIY0tR9-zNyB229SLQIEdLo-S5RJC21dpXJ4N5Aa4i81myoNhV_8prPdYQX7wbsGWGOEKbxMQyqoAMvuF4nUNDAxg1vfqlH0AcAq6qK8ty4aKDGm5bOI5-yKwHX6U2rOhQerfg-rxhsrHZWp0Ij67xmFi2JbZ4loFRnPAKllQ9D_AaJQUiBGA3qDuwFksyHgKOx9OVvQUKEv_5LH_BqlnL-BoEu4Obv2TX9b7AvOzPWg8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=DbH29Jijpi1v1qzGeWvkrPTVarw8KLVOpE-K6GUEm-WLBqG9Dc5kwUvGcYqMVxzQravo_Z8MuxtcaWqybx4jwKnU6wse1wLGJLIRBFJPeGwEBEXM1dj3VmKa0UEpEWNegeHTGhPNpke3jR-3rcbrkY6rDtwmqRjU9xTIWMclNiMbVhv1e3MymPCUrJagoNBlpdfsYndVMUke6gAtwWC_7nDWnvNnMSgwpATx6I8kUkmtxKXtWEmYiVSw_NVkS7M3qrD3Aqh5HMstLd8IQCUNQb9Icnllzyj0iKwQCFKoPbFmPxYOm_MNMIC45VohI52CE-LDZE5u73qeoXoErKSaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=DbH29Jijpi1v1qzGeWvkrPTVarw8KLVOpE-K6GUEm-WLBqG9Dc5kwUvGcYqMVxzQravo_Z8MuxtcaWqybx4jwKnU6wse1wLGJLIRBFJPeGwEBEXM1dj3VmKa0UEpEWNegeHTGhPNpke3jR-3rcbrkY6rDtwmqRjU9xTIWMclNiMbVhv1e3MymPCUrJagoNBlpdfsYndVMUke6gAtwWC_7nDWnvNnMSgwpATx6I8kUkmtxKXtWEmYiVSw_NVkS7M3qrD3Aqh5HMstLd8IQCUNQb9Icnllzyj0iKwQCFKoPbFmPxYOm_MNMIC45VohI52CE-LDZE5u73qeoXoErKSaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGLSRamAdaX08oopsQzJSDUBls0YKgYLdqYV268vFvuPuLJCCkBs1iZhmH-YmTvn0kFlf_fdkAUHoPvd7zKJitQnZGq0rqVxnAgMI7cqEjCgEaS4W_phWA_AxuW-4Q-5VAiDgrYm9QI2Hpj9_g3PwgCkToak8Rno6BkaVNViYTFR_CwDkOFqK4WqZV8ImVWSLapKnZuaw1kHzKRHSlRlXdtdcT497jFbuFx9tFEeCUOAYqkJGcfUM1bdfMUnFFvFzk7KvN5Pshv1MJYQMOrGOHKiPq1mqJWOybgykc9XnpZRcXNtvZbGplraLjMlttgxUtmjnf78pgjwCD44kF-sEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpnRCa-uJF92TAITfYvc_NLYuKBGGpMLXXWvFLmNnjHjmwRcYo-hJ1lJi0WMfGHgBclOq5TaJk8BLOGu3WX0jv40ShTWVSarAENb0uZrmF-xJwO-_sWO4fYi2C6CXUltpJDtaEaXsvw38IBHIUVdyP7dFCUO6pAGCkOslbmh8gkh5dNJS2ZoKqV-5yZuyLYvXLdqZxxyzTEqapqKfTskESn9Xn_oyqNWH06uN-LfhuEZW5aLsmn4Q18c1EJuTLGyFFd7IB8Ys5naUtBbu9zq0rqqWZrQtkGcxuoJLZ9lvJe860WtgVaEw6Wjy-IsHU2oTBOTmba-uHFCn0xqqSOSig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYpbnho40EFeI_pTpMSP1jHeUy3GhvgRxlriRBfk_joKsrWJCOUmmam3BmfArll9CR1WKXZalyBGPWmrk1Pd6GhNd9IW_MHv76yzpJeiKcz8dKXOajLyBJqnNrB3wsq8nyDhvb3RW9l3U1HDrShNJm3-avzr38rcDfj9W4OQdH2vecoTDxUXWptCAIKVZrERShzokgsrwmqwif0DEEkjpgyWk8IFTFhuO5Z0Etc1Zfnu0vwaxWLwWXp_6pPdQbRg0Ksr1abrRzWfwFYelc1IVsqmjKO_jVdJ2jZFBRS1PaGqRXMnGVrw3Q0ulZHhNl9504xF7RFlHXr0eim7RyXrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed4IBQqj0OoSE6yn0ytGdHDSdh3kkJWrSWSOd0EB5en2D9nQjIxmpRm32CsesgVCisaOTyAWamhCicf1kFbdVQhtW7gg2aS6xYaf_5v43yRIi-s0WQh_bHHfSB4f3NKKHxTVMLrksMXJtuV6LvC4ZALcDd4ZUTSWNrXF3mpjosU9ok2srm91o5ARNOb-edyBh0rMzxgAKxtq0Gy6VDONXodBC3s-E8quLRHfm7yDOGZbm4Ksxtf6UC_TRSFfE-C38X_8z5g-EnjJjlzvr4_atmbqw9Pa3HmzmbYWPFe6QJXNG_5s-_MycBc_9ftmhoARAbqNob-KY78bDeaOkW1oTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=U4tHt3kNcdiMSipPwhA-55Sb3KwXNyGvaG45hKH7Oa9k69lFF30t7gZGqLgXZixh5rgbaW-YaH-qXuXzO13_cas8F4Pgm1gLQ3UKOPpyswo7YBNkJY6pIUsU8ordsoBTSzCtZUsPOFXc2cMwb2Bc1e5h3HWs14sX9exlbAEAnk1PnXePHHLDU_5xJdNOGPbo0wK_YeeYYufCEtUMCerZHMH_Qdxr7CO5HYLtlzkPxca7XN273WJaG7rYjMzfw5sfNQ31_BxX06t4SaUym4Cyp_3wMlY-2sNHmE7z4ykzCMfKKq_M5h6tRHtgAhspzTtbsVE8Bd_CZII383boWiLwwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=U4tHt3kNcdiMSipPwhA-55Sb3KwXNyGvaG45hKH7Oa9k69lFF30t7gZGqLgXZixh5rgbaW-YaH-qXuXzO13_cas8F4Pgm1gLQ3UKOPpyswo7YBNkJY6pIUsU8ordsoBTSzCtZUsPOFXc2cMwb2Bc1e5h3HWs14sX9exlbAEAnk1PnXePHHLDU_5xJdNOGPbo0wK_YeeYYufCEtUMCerZHMH_Qdxr7CO5HYLtlzkPxca7XN273WJaG7rYjMzfw5sfNQ31_BxX06t4SaUym4Cyp_3wMlY-2sNHmE7z4ykzCMfKKq_M5h6tRHtgAhspzTtbsVE8Bd_CZII383boWiLwwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=vucvCDGfl2_UilmTOaIln_n9qoIVyBB6iLyVWwspyr7bz6js3sd_fZkFC4pJ7U8Ohpg3OaryYVvyDMSVIyBh5We3IAd2XMZhC2LXWAAzmw32fTGj_Pp1z50pAxSI2g-TGsrvI7_IQON6n0Gq3jvuOToJKc6cNFUnuzGyCtBwCLIBZ49DY5itfpbpy28hLGMGAV9_1jD-Uij4ktJvYVyYic-MgQpcqB1Gr95sHJhcle4ZeOq6trG9GqLBK3w59U3S6zk-OhKWZ1zQ2dqMVqjDSXEyYxB5xd-_8m2zebKiQxRPoUSeDhE5dtEDv5PJ9o6_AXBRt2MFIewASbOEzglj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=vucvCDGfl2_UilmTOaIln_n9qoIVyBB6iLyVWwspyr7bz6js3sd_fZkFC4pJ7U8Ohpg3OaryYVvyDMSVIyBh5We3IAd2XMZhC2LXWAAzmw32fTGj_Pp1z50pAxSI2g-TGsrvI7_IQON6n0Gq3jvuOToJKc6cNFUnuzGyCtBwCLIBZ49DY5itfpbpy28hLGMGAV9_1jD-Uij4ktJvYVyYic-MgQpcqB1Gr95sHJhcle4ZeOq6trG9GqLBK3w59U3S6zk-OhKWZ1zQ2dqMVqjDSXEyYxB5xd-_8m2zebKiQxRPoUSeDhE5dtEDv5PJ9o6_AXBRt2MFIewASbOEzglj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6IpWi1L-F9hZ9fbZZrbAWS_CTqwVAIoxzSWFmokIuSQv7q5ysdGBesBfOJb845OfjWDzJ0XjSn8O0rqZ5dU8qiz7wnxgjxhJwM5549HnUJlXFcXEXPEi2AA1XUET1Lzi8zOV8QqGCtcBg8_CpL06Kc-rdJiLHRU-FzkTsWZK0nJExwBcpCoGk-xNdvLb1t7NeaUfJaObgDCcF4_1FtfHzIePkhWo0RMgjmXJaFbfxblfrJ5lrVbZy8-xY56eUyOtwAOsVV75pIo0Fee5BJQMd2txJxmZWBARRWgSHhtfQ47OhdrTXu1_GqKD_VxzSrfDGuVylf-ShKopC57B9u9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
