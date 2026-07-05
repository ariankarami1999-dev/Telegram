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
<img src="https://cdn4.telesco.pe/file/R0ukF6YuJGfk6QR4W_kUt4LZoWXyR68nGhgAaGRupxOXfzeIIvxIVHchkX13f6nYxRluNLgGnGxRryGHZsg5Gz_bYJ0i_WlhCmKCKJJ3vOQlSM0MDEV0lJOJt3C33K0YPgOf8DjgSW0Qwjequ2px8d2oOXbHLewFGOSJcaWgxVRrYhHs3NKqBRcCQSQIg-hrRlTKxMyBFI-XM_qtbkJz_YQW6S-CCXRXBI0HZXM_YB6EDvYxY7Aihn-05mB4weml-2o_hemEB5_nXvP-KdD4adsn5uA6sEzs37Dc8ckoQlAy7yNLxeMx8afLKYpmYCGsFg8c6qLDawW0-MRi8cViJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=PtPrIdECUAAJeo3D4DPRTEclqEuDboVBt_wgtaIdZbeg0D0ZWHlqBglUXBdgSyljDGtB_55O7q1FpzfwFY0EqULKRW9t7L_aBR70c1qbVIzW3MtZIK2y4e6BWre822T8aD1gBD3dVeUGIy4Xp-MQ09k6Y6EtBHPXX8H8_IPshSLTAk-QROmH7ahAKy1oKg1RP_wju66CXX3Tu9tdz5NObErZ4I9iFvkgvoH8YemAaPhjHFalyQQYlDogfrBW7wS7VHmBInyhYK-5VlHiv9UXlQU7ozO2LqapTY6G7ffc4roGTihA-y85DmSIriN9srtd_E3jpzr5MQELE5nTz6FWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=PtPrIdECUAAJeo3D4DPRTEclqEuDboVBt_wgtaIdZbeg0D0ZWHlqBglUXBdgSyljDGtB_55O7q1FpzfwFY0EqULKRW9t7L_aBR70c1qbVIzW3MtZIK2y4e6BWre822T8aD1gBD3dVeUGIy4Xp-MQ09k6Y6EtBHPXX8H8_IPshSLTAk-QROmH7ahAKy1oKg1RP_wju66CXX3Tu9tdz5NObErZ4I9iFvkgvoH8YemAaPhjHFalyQQYlDogfrBW7wS7VHmBInyhYK-5VlHiv9UXlQU7ozO2LqapTY6G7ffc4roGTihA-y85DmSIriN9srtd_E3jpzr5MQELE5nTz6FWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=hcLr0lPgBWpt673HV6_kxiRYojBhfrUTnzSIA4ipBZb3nSFO0qRLomrEOYR-AgrjRwpUqZWSf1a1e4SIn2LBfXgewo6n3tX1f2-5cuuGgvj0u_56XcET9V7prFWJnnC-VDTk3XpvOovDLWXg6k9nR7mY2D3iTSbFz1oDytARdd-61lubQCdjv-E7HILYxdxVJyx9z7sS05iqjquxHz-EDA1Q7mTGR8hRH-sxXfDJjjOxvPPY1kUTXDwrxx0BdKlQM4-jeKCLUnn7WZ0brhz0itn_KjfIoPbyjUjB9xYJ9RrDajaWI_nJgMWN2z0MEsjREfXu9ycroF7p-fnT7Rm19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=hcLr0lPgBWpt673HV6_kxiRYojBhfrUTnzSIA4ipBZb3nSFO0qRLomrEOYR-AgrjRwpUqZWSf1a1e4SIn2LBfXgewo6n3tX1f2-5cuuGgvj0u_56XcET9V7prFWJnnC-VDTk3XpvOovDLWXg6k9nR7mY2D3iTSbFz1oDytARdd-61lubQCdjv-E7HILYxdxVJyx9z7sS05iqjquxHz-EDA1Q7mTGR8hRH-sxXfDJjjOxvPPY1kUTXDwrxx0BdKlQM4-jeKCLUnn7WZ0brhz0itn_KjfIoPbyjUjB9xYJ9RrDajaWI_nJgMWN2z0MEsjREfXu9ycroF7p-fnT7Rm19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJcmnNIrdROT93jUDFe16HicYX-kbjTEaLzBUWy0R_QbLUNh4PJliyZ4kXErbfaW-VIqicmP0PHKHP6TE_n-1dccalJvzeBTt44asoXAA0sglWaxMwPvYqZQADAoFp_vcWiaDlsnNoIg62hiDFY0FaYAL9-ESZ3Mzi-cl_lWXJMjZNSdJ7lLY9-63GFakJM-7xIPFdMgf4f4sCUplmCe5hs3I2pBK9pzBBtqWHWFh7Hdhopa6Vqe28JYG4Vnn0tABb71hDEogzns-JqNQuheogk7yxSVCHcaOlzH0oyXL-LabxJnReayoynf1qlZV5kxlZIyv0h9gLKmCeXQkO9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU5FQmIvF1wom64UWca7ZKlfD3k7B-pAmTGzBM2FqD-QgEoBo5ERh0H97GkSRKsypX7w9_F0sUnhuzOMsK8DJk4ZwAr5FBm1qFtX03BsFGNOXC4UDRhxQPtBVbHE11Dt3Ky48awdGBbg6YEZTKjdEhbWbdVTkbRf7uoJQtIdv8W7fwwsMjyYznlf7iCsKBSK0uS-niMfX5184niHj86-1D46Oxp6IZVVOv5K5weK9gpt8lY9qzfanSg_FWebNrAFEo7M1AdMV7hbnv03J6gAUxu7Y9i_G5fBMEjy_r3KgFYLA70LN2oAhj1i7wxJ8t7hfjHRo2guYUK1T1YzJQmkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFAKKtADXspnczadcDCULO632uV3rT8mVGpdjj6p4tdnPDgz6HhiFgL8Ow-ZfFk437V9BfRkkmKOaXv0GVYlpArZya6tuxkmnrBvIsSFSfVlnYZuKHYk-4TqkxD0YYUwCIZ7o6TghImmMdkYt_plAAX4rTIDMSdVLZuBT2WrEq-2jIGCPv0vNbPDl45z91rlZLuhKaMwk4o-a8ZGGASFClgVNXF-XsPDVPck-T4CbmZDjG95M11LcH1DrFyqKd7vCtb34jtHx8Iy45i4JCMK2neWAWCwsG8_U8xQnlPwSA8j09mKDLqjmSl1OYJfFRwrxR7lNMn_NSc7_DtMkLeFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWK3YjDqeqzxH3Ej3bQHsf0aynQAz8V_pUfw0zUuRadJZ8fHzejokSynMVkLE-AaMnL4_0y4tleLP8d-c_JK9PQZdgTwluUmoLnTbeVujbMICREhNwuJe0EW6xhieWoguPycNjbh_oXT9G4VWOdbmNZtSnAMze5-MPaUX0B69KOJzRbUpLQD5TDNGrTe-6_GVYiFiLGS-zJsnEhc8Bu80R3zg2QCE1ZhK8AwassKtYwXikjVSP9UHSLFQpcAAGpvoQZLlxdpAljPRd5q-XLKEJJmM7nuL7UVF9uZKQOtlG27J4OtXW0ABRZQn3W0znzkKBdYA0R9wAXuF6hpooiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=KHIDFRcZ8gJNDYbFhe4LwKXZ6Oaa7F07xnLE3Ze4J5DxVbD04d9-RTC1Ft5_eVodOw1LmL0NoLZ-O0eXtJc-5pkbzMhzHVdNaE_0Ukzjes5FKyuZc_L0qaZ_yb198wlKRHJ4VWXGqBtILvZNI84QMxKEZcbnnXqCr1qMkSPoq7UZRaP3jRT0AzjdC0ap2bWaIUnOOaMIG4OVce3AsfOYoiXkFZ4PH0uAu-jeuNJ0w8anv8uPTrkcX5Mr77-ldKrl4d6BT5tD4MqGDHHPKMPFhVMrjZ4kUDkIrVKctUzOnJImHglBgCDp6odARm4DlGDB5MG3EnwTFMnZbWeKpGeWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=KHIDFRcZ8gJNDYbFhe4LwKXZ6Oaa7F07xnLE3Ze4J5DxVbD04d9-RTC1Ft5_eVodOw1LmL0NoLZ-O0eXtJc-5pkbzMhzHVdNaE_0Ukzjes5FKyuZc_L0qaZ_yb198wlKRHJ4VWXGqBtILvZNI84QMxKEZcbnnXqCr1qMkSPoq7UZRaP3jRT0AzjdC0ap2bWaIUnOOaMIG4OVce3AsfOYoiXkFZ4PH0uAu-jeuNJ0w8anv8uPTrkcX5Mr77-ldKrl4d6BT5tD4MqGDHHPKMPFhVMrjZ4kUDkIrVKctUzOnJImHglBgCDp6odARm4DlGDB5MG3EnwTFMnZbWeKpGeWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=lSiJdX-1Zn3q8MI4-2GLooesm44VNJ23nGc3d6F7cY1ZYOc2wzdCGeydLc1wjytiNihQLdNTRRb30KolGu_g4OUjwIzpedtuOdTdvxxRVzosqKUa-815AD0qep80hAxsagYy7Eef1OtNkGURXRlEUh6fv7DJZADMGmZNIqfkVp5M9l_tWNLIau3AWGPEOFPx35-RSrAac_6uahqpJs8v6TaIfPfT6HtxSgVzg-3H5d29zoXA8Mx2XSvT2nuslWy6mqsaMZAvzL4WZzLaZOlKQ4WNu594MSHchseATy7KU6SRF6tCj9D0ubBATmmaFwpO7hl33yewpBBaMQB41QNBZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=lSiJdX-1Zn3q8MI4-2GLooesm44VNJ23nGc3d6F7cY1ZYOc2wzdCGeydLc1wjytiNihQLdNTRRb30KolGu_g4OUjwIzpedtuOdTdvxxRVzosqKUa-815AD0qep80hAxsagYy7Eef1OtNkGURXRlEUh6fv7DJZADMGmZNIqfkVp5M9l_tWNLIau3AWGPEOFPx35-RSrAac_6uahqpJs8v6TaIfPfT6HtxSgVzg-3H5d29zoXA8Mx2XSvT2nuslWy6mqsaMZAvzL4WZzLaZOlKQ4WNu594MSHchseATy7KU6SRF6tCj9D0ubBATmmaFwpO7hl33yewpBBaMQB41QNBZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=sHsBoJmsYkIikRf-XLGuJtKI-bFEoGNmlufiLNiGZxSMtqJP4s1Vz-Ihsn-gXmFMmuAs7DPsW9pbLTj6rmAFN3oAlIIGmSjWsW8LuW7Fssv6DKpdX8NpVtHruKmVPw4-AfnTIi-cdI_mm8dfCc0-2O3bRWkdcQoUf7_MZiQFKRdaOnXjP9adJuDwFQVpKifFa_7iDG1jLapATqo-tnuToBC4Fhz4PR2QiON3xZQ9Y5DRjSna3KjiErpqGfYgzqZo-uVxd0nXhhDfvr-2ZI6z15jyZnsoK_yvYuZW__C66POGmHwYxj0C2CkIYiumb__agbeh6d_KjYlCPcvc-g91xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=sHsBoJmsYkIikRf-XLGuJtKI-bFEoGNmlufiLNiGZxSMtqJP4s1Vz-Ihsn-gXmFMmuAs7DPsW9pbLTj6rmAFN3oAlIIGmSjWsW8LuW7Fssv6DKpdX8NpVtHruKmVPw4-AfnTIi-cdI_mm8dfCc0-2O3bRWkdcQoUf7_MZiQFKRdaOnXjP9adJuDwFQVpKifFa_7iDG1jLapATqo-tnuToBC4Fhz4PR2QiON3xZQ9Y5DRjSna3KjiErpqGfYgzqZo-uVxd0nXhhDfvr-2ZI6z15jyZnsoK_yvYuZW__C66POGmHwYxj0C2CkIYiumb__agbeh6d_KjYlCPcvc-g91xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=nfnNzOSkIGP5jhvwj8KS3pRwG678Odqg9nI2m_u09TVj2xKja58TRfZNWqrkUaRNuwexILF4dkWgaLc3Q5sKGE8BJ3qoi2mZcZrCxQQbJUYflSJd_vk-WfTOYKHkXAotujb0zWi7xwWVX3Ez6o4RBVLy5Frl6ABe2t34gRQy2c3x5WbkjNZgWIlZn058zw5LVZyFzM8HVEOkayxiiEJobAlG-gaTkf3xYxUJ__ms8EFVkQwk-DyicO_1wx0hPY0xx01HRMefT1wRxEuKRtNsvYN63AztmpMoYWV5bjvUcJ1JuGnKFbkl73MlfaJ6r0xW9mRPEcpG4VaTX4Kj5hFWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=nfnNzOSkIGP5jhvwj8KS3pRwG678Odqg9nI2m_u09TVj2xKja58TRfZNWqrkUaRNuwexILF4dkWgaLc3Q5sKGE8BJ3qoi2mZcZrCxQQbJUYflSJd_vk-WfTOYKHkXAotujb0zWi7xwWVX3Ez6o4RBVLy5Frl6ABe2t34gRQy2c3x5WbkjNZgWIlZn058zw5LVZyFzM8HVEOkayxiiEJobAlG-gaTkf3xYxUJ__ms8EFVkQwk-DyicO_1wx0hPY0xx01HRMefT1wRxEuKRtNsvYN63AztmpMoYWV5bjvUcJ1JuGnKFbkl73MlfaJ6r0xW9mRPEcpG4VaTX4Kj5hFWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hW__kRfsb9TyxWxiz2GhEybjoihirq-EbRmQ5Gw5DOOtMOROL0Xo7MADTbZBfAxJVHpojBFsSTwOhZ6tHwQDJlUYb8bCQSfT6QbJVs9xMeDcFCoD3J62TiPPy14qnglyC5ZjwCcs94WQtzEIGyAnrrccMpMtatSdGi9P5Z2RvImaXFhz_2j-HEdoNYmh9owUbWT0VxumT8UZWsS1Mu_dCxhvn_0fRlx6OHuNPyI6y_e2s_npnu3D9j13myaRzRSuJshf7tbPQZrMRC05XRr6uUcfO1zCFW4FzE-hmC2h8iq0Pc-oAZ5DLELCBmPfAuJr3LbahSF51YstEeQsRhLXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hW__kRfsb9TyxWxiz2GhEybjoihirq-EbRmQ5Gw5DOOtMOROL0Xo7MADTbZBfAxJVHpojBFsSTwOhZ6tHwQDJlUYb8bCQSfT6QbJVs9xMeDcFCoD3J62TiPPy14qnglyC5ZjwCcs94WQtzEIGyAnrrccMpMtatSdGi9P5Z2RvImaXFhz_2j-HEdoNYmh9owUbWT0VxumT8UZWsS1Mu_dCxhvn_0fRlx6OHuNPyI6y_e2s_npnu3D9j13myaRzRSuJshf7tbPQZrMRC05XRr6uUcfO1zCFW4FzE-hmC2h8iq0Pc-oAZ5DLELCBmPfAuJr3LbahSF51YstEeQsRhLXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=IUppGR92ZifpWL0UZXAzyc6HY3aNQtMWCcnikWVx9VQ1ByhEnbGo2mLL-aQDbLFZCSHqXohHby9KbLRJH2aLB0nGfaB5heGlTE0ORyiKntrX4hbXJl358CzVNXFwYoMqLDIQvzijqT76HOFGD2f6GMIJXhtwH9iVz7SlvKYkvfg93UyQT-8VBZ-d4ELxgTZWf7A3h5Ynn1wD1L1AtVLtVazMLpKL_XeMWFsyUivdYl5E5hm1xTzR_pLwb4puJqypr--NHu2NdcZlMTp8ETbKdOH-6G-EhtPOT9UAg9ywbNaK5Uf37Um_p-Koijbtx1KHr0MhSxxKXbIGm4BvZCppTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=IUppGR92ZifpWL0UZXAzyc6HY3aNQtMWCcnikWVx9VQ1ByhEnbGo2mLL-aQDbLFZCSHqXohHby9KbLRJH2aLB0nGfaB5heGlTE0ORyiKntrX4hbXJl358CzVNXFwYoMqLDIQvzijqT76HOFGD2f6GMIJXhtwH9iVz7SlvKYkvfg93UyQT-8VBZ-d4ELxgTZWf7A3h5Ynn1wD1L1AtVLtVazMLpKL_XeMWFsyUivdYl5E5hm1xTzR_pLwb4puJqypr--NHu2NdcZlMTp8ETbKdOH-6G-EhtPOT9UAg9ywbNaK5Uf37Um_p-Koijbtx1KHr0MhSxxKXbIGm4BvZCppTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE-LDijPckXOEoF5DRtdpURbfJE5UjTS-iEuwOrXrPi6Icog7GK9zbwNOeQ8l4me51rVZKPeyRH_rHyb0v_RaEy4gwThcT2bd5UbCpDwpCZ2fK4jzOWZvGN4EVDnUZq7m1q4Jwu8hB5_mfCZBMhyvz2mU6Oru2ryYbWE0pLaFwx2HUyT7nrG4z7oblElhdjorAlqgVo-dYiLyeCRwlyk7ciG1hiV2Ci7sl6PUQ2hGbEFQP7xtYaqbUpA7lFZYb5ccGsiCE7xTZfXVLuwzJ-Veapnhu8Wk59KmP8SyKKUN21gr1ASnppmv_qDN2TRb3yNAmhJnwFDLHKya30keScQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=QcMAYAJzx24zkyshcIJdKJUse1sOZL61pd_kH5PDZFtoSvnXqWCaMoZ1skxM7771XWGxJyFO5QnPO6pMt-THWMKwye0srdf0qRZoFyTatOChsMWzJX-UuF-bLF85cGZnbrlVoKyf-zPaVcNlib9XJdu2trUSPBZBQmFYc3vQLIQi8iK_ANvXmIiXR9C4Oj2tgb0zXNOz5fti8a1kdyWFFkPmfhufR8cqudtGTkPzqcCEquAu3rmP9VUtyORBb5KsOEPKFSxg3MFqmCovi71qNg31vW-p3lTgDMxmd4GKOXdPP7k-8ykaFuFvmiuKDUyG8ojdNBPLcKGX184hfxhFvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=QcMAYAJzx24zkyshcIJdKJUse1sOZL61pd_kH5PDZFtoSvnXqWCaMoZ1skxM7771XWGxJyFO5QnPO6pMt-THWMKwye0srdf0qRZoFyTatOChsMWzJX-UuF-bLF85cGZnbrlVoKyf-zPaVcNlib9XJdu2trUSPBZBQmFYc3vQLIQi8iK_ANvXmIiXR9C4Oj2tgb0zXNOz5fti8a1kdyWFFkPmfhufR8cqudtGTkPzqcCEquAu3rmP9VUtyORBb5KsOEPKFSxg3MFqmCovi71qNg31vW-p3lTgDMxmd4GKOXdPP7k-8ykaFuFvmiuKDUyG8ojdNBPLcKGX184hfxhFvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=YQ8pIIlTZacrq0DiVxNS_df1xBdUNYlkLne0-zx1D7wHQgrWwmA6jcytISgq48gPpb4_2qivK7_F5dGeAUxCbNrIkNPZT0qj8G14FfYyeEMSfqbe-mgcW3chteLH7FnzLrZgQVYzpehjOMTE0O8shelJSCa3RbYjCT5ao8IbycRAmHihbIAvm-gFAZa3uxAfJhv4PG9nv2WfD6usD-ZvSK45T4w1kQqjknmTaBkn-dJxDlwI98NsIBBFm8DyAnzR4OVOR2DJiwXqsie-KQRNgfVuS-iuE_D2bh_3Uj90RvqM3-c4UWlak0F7I2Vq42quN7bPnDSxceHlha4fr56JAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=YQ8pIIlTZacrq0DiVxNS_df1xBdUNYlkLne0-zx1D7wHQgrWwmA6jcytISgq48gPpb4_2qivK7_F5dGeAUxCbNrIkNPZT0qj8G14FfYyeEMSfqbe-mgcW3chteLH7FnzLrZgQVYzpehjOMTE0O8shelJSCa3RbYjCT5ao8IbycRAmHihbIAvm-gFAZa3uxAfJhv4PG9nv2WfD6usD-ZvSK45T4w1kQqjknmTaBkn-dJxDlwI98NsIBBFm8DyAnzR4OVOR2DJiwXqsie-KQRNgfVuS-iuE_D2bh_3Uj90RvqM3-c4UWlak0F7I2Vq42quN7bPnDSxceHlha4fr56JAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oROuTwTUrN6257j3pSCVZ_mhE8yE-b4cVC9ssUUPBeLYhzS-eNihSktJsfmGa5cf8a1PQI_qeE8I6dHQTTWT_-GHQThKRso9BBYlmSx1H16B8JzVHUHLKhmAlgPLMWPZiTNvGTO1wcJmGocHVajIoXHDnJltQXJijutMus5EKsuOSkqOtXrwqjgcGuXKCyNMjwBZdWr3K10b8OnBkgSIGU6VYVKDbsUrf7BaQXqPv9V4nhwZXkJfckNytNTIITG0NycYmG8Cpnl7YCF0OwM1ESUTZGPDn_mKy-Gs_Xxugkl5TI3UPHDdlTKQndCLp64Y9B1CEfGOHb1MLi5xZH1QIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luoc7pz9aTO16Kkd4Ef9YmdABgx_W8VVH0nB450RPT9-SZ2Tnp1bneD07s90FrH_eaDoKgZDE4pvUOMerJScQ5swuyBrmHuwr2FZSX8sWEAuOxBPQghToMKNgbNfwF1RiMQPwCN6U3QrBesZIc8_EeTtyyfILCxYR3dJpkXxD__m78AYh1m0aVD3nLKVpbxmurttqZzEPKXD_pCscfVxC3qdQCcQ-zp5okdddeWBS5NxJvT9a6-TxXWWoPa5O8-_EpSNPxZ0YSglNBvaV9PLAMsU3PFCdFK2xFdQE0xc-F6mOQlwFb2LK_fffkwa2Att_ScLiMFlE3vB4mK_YSkTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvTuywpVNJWigSS_PiZF2_yDahQaayAGiY2kwojIv9440CToGdqVD2MPZj6YyseB7JOssvfdfukSJaKlR3obM1f68fswCrjlXv4c074R8X735ZyiTSwk7lzd6IMsfPUHxSvZCRnfLJt-lAD6ZYENsgYh22S1CYNFu_kR0_photo6Zmv01fd0q-QbwRIB9SMF0oddu4LmcXuSmzwP8wN5WZqeSyqpcxVGuG-_m4oNeDrD2DHK_NmebgoLWRmZUQOYx73gkLIxgo_3LSKyJ1Csju_YXuGOGFuiuIQsat9oY-xQixig_MvudSHLDpXE568eFgM9MGe8Q7WvF1anu9mbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajeg0ML8WsEPVP0Sw5CT3EqmCdaZ1M1bZARrGvj44B5ULxMAHLvpe-K6l9Qvrp6LW41tXz-9ss0TrtkV8PbXhZMDTK64MzhtERXuBeC-x3R15wKIJ4Ddh_G-G54ZiiMu_9QTQuDPzETaQ-b-DmY0Oy3VyhrI_HwiQLE2bgM_zLRy-u-yl24Mwlz5d1OOWhZQhqlHbTxsExZfXq-Yrhi3Sq5qbirXjmiIPjytIacIq2Jywbqv5FEFtUlHVpAZRQIUkKS1IV06M8iCRfXd-IgyOgCerujQ6IQiHNZ3PiRbZyeT1itGXprXHTf6JbPNyyroN544g3U0U-JMcX6ebTn7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rngpzz_6Z24joMWk1SrLCltlseBg9eI5klBifeZzAkv3SJQjZgMKlNpwfyOJ_MFvS1aCeqZO-TWbl_cX8vdG3zegU10La1-Sr5GgycRaKMysnun6G9bIL5pB1kFP_ByPPZH9iawMXVD3lTCAvqVNJKy3jkglqnmTxLoWn1ejn37IOOxFz1SPfi3a5B1sdTCl_3hsJVkouF1bbVWWPR_DOWUfANllCUI84j6yf90ifPvUPeajsracGeThVAxkSFWMO1gp7YsmNCUt7x256WnW5wAUF_HrwJFrG14HtTSMUQhbScDpepnTjxIQKAdb5kNxLXzeqwkOZOlRSFK8rbbsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgshe_5Ze4dOI4eb2ytDHtKkcXASUp69TB0Ajexz3odrpKSC9xdOjrxxhhbhh1F0nS_sugZ4IOvPDU05nNmJdL5D_edIWsCBRxc9XimjpfbYKgmKf9ltXtR9SPNXEIF9_CbBZm162QZt1qpaFLeiJz8HoEQe1QIh8deYxfqfk4x-gsGD4MF42RSKk7MonDeq3LtZwqvDJzfOgY3ZlIy8oKnnSVAzBM-_iDV44BSzx2GdCSpp63Io6dVdjFeN1TYJqKOrEGrJoLKLQXHZYouyVj8OFeUT4pazbbR8eF2v5RXe7lWiNx4Gn1r4QgZoBA8Bbb6oORckQzuuFqPDptkvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKx9BppY4o4NYebrTfq2aL-o3_z9kmsJkhZgYE1h9z02Rd0njkpVWzUpCiW2RuDKs_ORwwpwybuzL1WLXGlTdG9uwkk5d48wFM5FGex1vVmtk4N0Gv2NtQrBB8YFF4Ys1RBEJ6wipNbRWoCbcBqZJrAf6eAM40vp52wJdNGVOGbV3sNJ1XPmuZutUlpTtuEDjF6VVrFEJL5HMvVakfVRrxSrcP7qI0zuzkCX0d29pgEXSCVzO7hjH_V5RalUeejaVRqWPxecl3Ly55K8sbkS2DLdqLj0NtjQ9PTiHyIoRS-72aGutN9krM7NRhYUZ_ef89nMscWUc3-FuA7CmwRMvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_-Vi6gcAHIzgatcxDoE2Si3YSiTNC6LWopgCICOQpf9rLgtfyEKopRscFAku867RxGrtCc4mmon7AOhHARY63zvzB2e3_JSSwRqCKNZE_hXf9yrwOzF8swgvjjUkDHV59bgbc0n9_s_ao65pqX1N5jsf4FV3reDfXlcEtqEVazDM94X4BNnW6n5JgBIW0TGbIVRfGOpczFySsZ8BV1fOW0gIG6oCT8hSTVxzN23FZHkcmVdTec2HI2gv9j_FkCmHqJo12EmDMtYpZLWhuoSHM6Xoayc5zUZ4hjaf1r2GiF-j427xQKGV95NqApCoURU-1IelrM71vMIKNZDjcOm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWlfvykqdor2GOJ__8dueb8hBz8qYx7ZZjhfJ6FfRZzOYZ3lgBal0WNJ_19Aubm6jdCzGWRREOobqcamc1_sNw-WxPjXhYctzXmhlNxOJaVKlyPCEqhl0sD2YoOq9R4071zxhTn-EKSStU2QTzrfgBKIlNqAWZVJKTKYWGmzKdV5yHRjGAGdBoT3XoruUyLP7DdagEIYkYomQ_MejlHG6aIsgkgH5t5QmLewIBYLjGTebP1tYpLBK2XoVOil3X_MMJovsXXlNh14RxUyY4Cm28Rvm7OSC7rgxHiAIVjJxLYKsyOOSax8h3FDBtfUAfH1dNtZcImJiHYHU2Zu9arPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDuUhMon-WefrSVoLYymMK_eylmuLyiXIq9vEvZWOb0ZLb4fLiafkBvVtI-_g2TumxSs3QniakWflK-4VCoesQuF-__u1y1qjyG4Bq_xGEEG-YAFoWL_hrVLgTQkW-hTzUHJ0un9BQJ-kA2HJ8-orJBEvz9AF37XBOFaXHeixNHhfzG0m11XCvDypBBdeL4hLWc5k-6hxRZYf3-9818k-QjpCjJJ-7-cfQIp3nbrlVJtHRIWI4-QX-IjsXpAO5OhtM7GZlxuog0zRoOs8oC_SCNvkxoAl0JL9nDz9Z8K2caVYOKADQqxvF_azWS-3xrCi1S9qmfnbNvhq2tw8qLyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ5oAYn8tt1BRH93ya3gmKFc6dj2j7I2ipEAnTE03tG9P0k_MGhwezw_584dT445gVEPBAwyhJf3PCYgcizCxuqb6wdroxGWDSU5xw8wPo8ZH6PyRxdx6_QG_CBQMXMDblUEZaUIr3EyykDqjHSPSjEvBIIC_-gmwh1KtfLfTZilhMrLjrPrsyTiBSDnbvSetPe3S8oyd05XmAlBSPefJzXR8WlfI5L9sKO4fj0wrVEuLWuNsVQH-j9rp61M7b5x3xWKjG2CsmfzwiBWDOYlSr6m1gO4unBaLNo7YAeotc2KvJ3N23sYMzrOlzWG5f0jWyz9ZM7SMF7lwZvtqN26cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=crpR2OC3sMPAOXG9-SIOzfz24-oUXWHBgnyk8w-exArbb1mZZGx_Dtk6dxQXRnTB7EmsORovc5PTsYY22Mg5IrTScfwEsPOONRMVfxQevo8Sb4kSdnYIRscp0f-Bp9YLg3PufRjO4WZQgvfqn3nShshg0t1QoKEoWq39vJon555Djm5TIVKxEaMFTNF4Dkk9fzPNHdhlKf_I3GlgvsEqmbgOvx9auNAsI_O3kk_KtuEoG2fUo1r1_URWYLCIEGkrsk73wzgAan4bqW641uajgKOGrUKXccXFAGvnfHU_z4K_IoLH7jGuw3UqkXAIMsRUKE-sc9yQQB9MgTkIdNLO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=crpR2OC3sMPAOXG9-SIOzfz24-oUXWHBgnyk8w-exArbb1mZZGx_Dtk6dxQXRnTB7EmsORovc5PTsYY22Mg5IrTScfwEsPOONRMVfxQevo8Sb4kSdnYIRscp0f-Bp9YLg3PufRjO4WZQgvfqn3nShshg0t1QoKEoWq39vJon555Djm5TIVKxEaMFTNF4Dkk9fzPNHdhlKf_I3GlgvsEqmbgOvx9auNAsI_O3kk_KtuEoG2fUo1r1_URWYLCIEGkrsk73wzgAan4bqW641uajgKOGrUKXccXFAGvnfHU_z4K_IoLH7jGuw3UqkXAIMsRUKE-sc9yQQB9MgTkIdNLO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=mdbNETHOJXAOLqFNGuTpQUimpHnIzoO_YT3lLlOecbjRF_bvEzrpHUJIgZoRtGpA6schKlGmV6ZnoPWJ69Z76Q6hkQGV2EzD-TP3PQDItHoOi8c5BvAenEcIiHlwr5ng4lLj8afdmbIGnKUhxeiUgsXvIqQBFCn81CaJyGqjocxmq0GEZwXIOiDiiai2n8zll0b1Nxop0h0HHD4OE1WJVFLJTupwAE4c1AMTBgw9hi7TdRqXG1mVnIez85EDOVqu7CU51S1G9G-oSA4L6pRJhhWXg7Kxi65fi53o1V4TuXid06SEPc2U6R5p0S-Aml9TfMhdFLj01bz6oXZyJ19w5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=mdbNETHOJXAOLqFNGuTpQUimpHnIzoO_YT3lLlOecbjRF_bvEzrpHUJIgZoRtGpA6schKlGmV6ZnoPWJ69Z76Q6hkQGV2EzD-TP3PQDItHoOi8c5BvAenEcIiHlwr5ng4lLj8afdmbIGnKUhxeiUgsXvIqQBFCn81CaJyGqjocxmq0GEZwXIOiDiiai2n8zll0b1Nxop0h0HHD4OE1WJVFLJTupwAE4c1AMTBgw9hi7TdRqXG1mVnIez85EDOVqu7CU51S1G9G-oSA4L6pRJhhWXg7Kxi65fi53o1V4TuXid06SEPc2U6R5p0S-Aml9TfMhdFLj01bz6oXZyJ19w5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=jt0Xu-DK6NbUphIWLrZf23JeJ7NXN_yqD5_sUmWW2i9Sug97GDT2oL-uha92UTPsQ6oWnL4fprztOfnOVtNoXbB0HTQGJrIOQ3lB9QoeGIgaFhJEzabO1uwxhgtW0ysTHK7ljGOsnGYBUE9D_pNnmsQ7uqRFTLkl4-lzconbTNexXFa5tvoeM8qwUbg1KlhcyzBxybv6AB-hEJxOSvlPSxmMmI0eY5CGLw03KVMyN10X9V2CAy_dGQCX5PXd2Mr99M6RMKLdKjgeyfU9erwjZUtq8pv63WrSOoysEXxwshEJk8GF6nZFYL4KFzhuebAiJ3m7a0VMRUV0OOf2xHIStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=jt0Xu-DK6NbUphIWLrZf23JeJ7NXN_yqD5_sUmWW2i9Sug97GDT2oL-uha92UTPsQ6oWnL4fprztOfnOVtNoXbB0HTQGJrIOQ3lB9QoeGIgaFhJEzabO1uwxhgtW0ysTHK7ljGOsnGYBUE9D_pNnmsQ7uqRFTLkl4-lzconbTNexXFa5tvoeM8qwUbg1KlhcyzBxybv6AB-hEJxOSvlPSxmMmI0eY5CGLw03KVMyN10X9V2CAy_dGQCX5PXd2Mr99M6RMKLdKjgeyfU9erwjZUtq8pv63WrSOoysEXxwshEJk8GF6nZFYL4KFzhuebAiJ3m7a0VMRUV0OOf2xHIStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=iGJRFSbovBCIfaRbgM5B4zaw-6NLeMN4jvers95ViHS_gtOjCcHHJ4aJD-csPf0gyCZTqeea9otGKtm_3GIK48g3trwT9HcOiH33aDdj0A6RavXIMKaOTPB4FlitQNBEwcLPzYWr8-MBT9aWeuqTPoDTFjix8U2yO7KnT6N9LQr1nClgDjYs-Aq5K-6q8MOFeORA7HXAFmexou6y07jsUqJRKKPl9LcI49llrDdQkJuefDrhByfJ_s3-mgujvK396jipISP7qAyYlmcBpeEYE9TjJEZOnUvrrj-YZXGev87QQFuFTcaxyHDPsP3M1MQKt3FWvY2BMZqurs19L04clA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=iGJRFSbovBCIfaRbgM5B4zaw-6NLeMN4jvers95ViHS_gtOjCcHHJ4aJD-csPf0gyCZTqeea9otGKtm_3GIK48g3trwT9HcOiH33aDdj0A6RavXIMKaOTPB4FlitQNBEwcLPzYWr8-MBT9aWeuqTPoDTFjix8U2yO7KnT6N9LQr1nClgDjYs-Aq5K-6q8MOFeORA7HXAFmexou6y07jsUqJRKKPl9LcI49llrDdQkJuefDrhByfJ_s3-mgujvK396jipISP7qAyYlmcBpeEYE9TjJEZOnUvrrj-YZXGev87QQFuFTcaxyHDPsP3M1MQKt3FWvY2BMZqurs19L04clA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=JXBiyweSxaYaes7IMih2JuD9HhAnRhxLwcRqS-32UGv8UyudDH4PnW_MJAGMsivpqEcnhRt7CzTWI0emkEBfCUjBiKJ5oGmsVbiLmkk9gUx4Sn58hBntHHs4LRI5pz7ATfTFN1zE1nUuo-B6Ox5EMW5gx8nVIuTa7atthgBIqw597qZdRlmDupYkfr0dZQRbQ4qqB-Tq5lU_vM8Tdv7xvMsoBJ0hy4msLKoSMiY5p2ogoS2oi_s7NElDac6xvcTNYhzUc3zS8FNrPjxnXjNIkOBz2j9FSgG20Aqw-mDu6DPyrE0kDgRiR2qtDbwyJMktnvYRGq0TVu601eMdaJZ2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=JXBiyweSxaYaes7IMih2JuD9HhAnRhxLwcRqS-32UGv8UyudDH4PnW_MJAGMsivpqEcnhRt7CzTWI0emkEBfCUjBiKJ5oGmsVbiLmkk9gUx4Sn58hBntHHs4LRI5pz7ATfTFN1zE1nUuo-B6Ox5EMW5gx8nVIuTa7atthgBIqw597qZdRlmDupYkfr0dZQRbQ4qqB-Tq5lU_vM8Tdv7xvMsoBJ0hy4msLKoSMiY5p2ogoS2oi_s7NElDac6xvcTNYhzUc3zS8FNrPjxnXjNIkOBz2j9FSgG20Aqw-mDu6DPyrE0kDgRiR2qtDbwyJMktnvYRGq0TVu601eMdaJZ2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mH5mgXp0oWMPCJuKFiGEC8GIWkCldRCsbUvqqfjv8eW2yb2TCjRyIMpPFxwqIV--rIJwICHE8TmJwZ9s925rdwPcV8o1JPGeV6JF6YNo9uJG3CVr9t-O3dUIpuwXgYjbqYtKurJ_17xfcgMKhVfBnZnk4byQ-Gv8DpiVSRV2IdgpzJlqkGgxYVmlE0jY6yl_jqM4FArz1vLkRof3RgezQwGALmBJjsLR6QkLL8rd-WtjDml7GXQ7AYk-HFhGDaukGh54pH0BTKWv8sjsmBJ-Ni4DEDmEk8x2PCGSv8HEUZyKlxVBo75eMJbnYUenGlp3Fayzcjm3u5rYLAUk4hsQEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mH5mgXp0oWMPCJuKFiGEC8GIWkCldRCsbUvqqfjv8eW2yb2TCjRyIMpPFxwqIV--rIJwICHE8TmJwZ9s925rdwPcV8o1JPGeV6JF6YNo9uJG3CVr9t-O3dUIpuwXgYjbqYtKurJ_17xfcgMKhVfBnZnk4byQ-Gv8DpiVSRV2IdgpzJlqkGgxYVmlE0jY6yl_jqM4FArz1vLkRof3RgezQwGALmBJjsLR6QkLL8rd-WtjDml7GXQ7AYk-HFhGDaukGh54pH0BTKWv8sjsmBJ-Ni4DEDmEk8x2PCGSv8HEUZyKlxVBo75eMJbnYUenGlp3Fayzcjm3u5rYLAUk4hsQEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=hcSD8J_UN8LEpqxvT9MFqrtZVi1x0Ux17Y-YUwQF1zS3k9gm8Z-H6Ve2wbR1nmir_-GB0zFy4iFa9M-ty279x412knVs7Ar6vpxvRONghH7pJMB-gvFllVqqgUxNY9tu0iX4x_9z0uIhw5YtsJbrJ6dQMLk8wt0yZZCxmQWAZufWEzxxUVsLYds1uLZH4FjqkLA9wj_uzQc8OkrBZw9brAxjsMgeGS5Gq47oxWBSBcAugjqsHk8joscAg_7k4XzQHr2zgA1DrJQknEr9JH0fLXp7zR1J5EWlccJpQ4CrqVrKL8BO1GUiQjriJ2pxTmgGpqWc609rrcvKryqrp7PaNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=hcSD8J_UN8LEpqxvT9MFqrtZVi1x0Ux17Y-YUwQF1zS3k9gm8Z-H6Ve2wbR1nmir_-GB0zFy4iFa9M-ty279x412knVs7Ar6vpxvRONghH7pJMB-gvFllVqqgUxNY9tu0iX4x_9z0uIhw5YtsJbrJ6dQMLk8wt0yZZCxmQWAZufWEzxxUVsLYds1uLZH4FjqkLA9wj_uzQc8OkrBZw9brAxjsMgeGS5Gq47oxWBSBcAugjqsHk8joscAg_7k4XzQHr2zgA1DrJQknEr9JH0fLXp7zR1J5EWlccJpQ4CrqVrKL8BO1GUiQjriJ2pxTmgGpqWc609rrcvKryqrp7PaNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NibPfI04XUVR8Z8QzC2L2_KuMNElL4KxdsIXnE7N1AjvcpW_wnApBSmDgWlQZs1295uZQYPtS72g0YnFOG4v-dfCW7tC3MSK_ImDYStBslykB0lx4rt6nUTjXbd8_S_43kkXzsqoLCe5m7DH0wYonDW4olBGj1AmwmBNybm9Zk-uEn3guAhEhW1HgehitpbeK3JOz7UaUnMUvV3Aw7uYe6xultxe8o4BgEO9LE95SZrQgOvtu94bN_hJGtcX1EsZhJohQHAAeFNR3IREYCC-ebYIa60atZDg1dOCj_2ep9IHxAiEckZ1RoRxBzdYGqTcRcEIwc62e69WzpP_dN7ynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=toh5cgF3vIS5hzHeYr8wzkRh8SzF3RyuvhqZR1Q71pT3fGoU_nh6k9cy4V86PAbKpsW9xsZy5p1B9DRI46h07zZfuFguSB572IRSl2CvyaCnPM1YtobRsblFos-3SkzrSqXohWCplbTpGQufQMYnvtRn_r8viixjfF2foGXdu5eGQvAYy6q1S0Gy_wQIvsL_HTssUgGU3VnYl5ArOggX2FhZtD6h8sXn99f5JAMvTgUjMom3NwvIvMJ1rbzQSqCsv1iiQeSVEL_UuIKe-Psglf63eIOh7U72JQKjsFW2kX4v9e9dxYyhH6gR7wshaakSvXDhR2Hpays2uef3UvMUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=toh5cgF3vIS5hzHeYr8wzkRh8SzF3RyuvhqZR1Q71pT3fGoU_nh6k9cy4V86PAbKpsW9xsZy5p1B9DRI46h07zZfuFguSB572IRSl2CvyaCnPM1YtobRsblFos-3SkzrSqXohWCplbTpGQufQMYnvtRn_r8viixjfF2foGXdu5eGQvAYy6q1S0Gy_wQIvsL_HTssUgGU3VnYl5ArOggX2FhZtD6h8sXn99f5JAMvTgUjMom3NwvIvMJ1rbzQSqCsv1iiQeSVEL_UuIKe-Psglf63eIOh7U72JQKjsFW2kX4v9e9dxYyhH6gR7wshaakSvXDhR2Hpays2uef3UvMUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=G1FYqmSgtDHteYJs81iQxzxW11o1gNvz8rV_bDjRgj6NFuuaYUdec54l2TF5grfMtSeax-IsJ5Ch3S5c33qPpOZOCNnhxqUBQZWe0V7pYgiLPRr9KlV03Mufffhnz9uo0JETq7QgPiiwuy37HMzHjocTUuEqyEVkkQVYdQFU-8oI5ccpE95PX4QfQewvkCXWsBPMKlYrhVBqtDMeoP1PyKgNVqD4T-QAJGT7BI05K9KSesEwKuDxxKdyPXElsj5oQ38nCIKfa5of7OupclpELhL8_U66BHD8R7FTKrjA_50IGydDKFKPiEtFcN44N6Dq5BVPvkyh4pKjwR_mrtiF7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=G1FYqmSgtDHteYJs81iQxzxW11o1gNvz8rV_bDjRgj6NFuuaYUdec54l2TF5grfMtSeax-IsJ5Ch3S5c33qPpOZOCNnhxqUBQZWe0V7pYgiLPRr9KlV03Mufffhnz9uo0JETq7QgPiiwuy37HMzHjocTUuEqyEVkkQVYdQFU-8oI5ccpE95PX4QfQewvkCXWsBPMKlYrhVBqtDMeoP1PyKgNVqD4T-QAJGT7BI05K9KSesEwKuDxxKdyPXElsj5oQ38nCIKfa5of7OupclpELhL8_U66BHD8R7FTKrjA_50IGydDKFKPiEtFcN44N6Dq5BVPvkyh4pKjwR_mrtiF7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=bP3hxGDK6KUoMzz-PSZld0JxIKw__B9ZWtvrW7P9jE_OusrqANjE7S0QE3QXn4Ubh9wiXhqArCrQmavTn8FEjBlfTSwaEIlaFPTFTpHIUlN_6TJgDjjg6wBX2t3UHLd5o_ohAxDW7XUBO-t-6kf910p2CRkXxhWVP4xtzZ3zOSwfs5aDveZtTbc_GdYNfvAVb6rMnyy1W3a2eRjGkmlPKZut7vPngQi2iqghtrmWV3knC7lpQdAdmteyqNUzrS4z4HfGwBPybQVeMso6mr4W6SXPbz8IsMYOYEyjqhWdoDw5Dk-E9gBVeDTcypdWS4uj7AG1VTiRaT1zM1B0E3VUu5c11kbnFKca80XV-IbziX7kY67ppA1PiqLGwOrHRuJDuoktfqUObd68vZsXXQz-J3HYwqu7jV8CkPLgLOn46BnRh0QqwByYbiNxFJWw5q08XUM7lFFNW175JESJuH2ewBXQFSxroGiheuQz0ghacwNruhH1N7mQ5PpeJBCRT20TZXKi2kpUA-of0cA3uZ67TwCw_8OVhoc-RH4GkxIMZkBtbYdxCQsjZm9aisRLue4oN3DXw_JS1bZp4xQ596ASxnsYx00Zb733mf54iFRTHfWMlF_j_YJjWO_lnsmaZ9-oLOwXeEWMv6xj1RJMShGwRl1doVfGJFPoDMmWKuXt8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=bP3hxGDK6KUoMzz-PSZld0JxIKw__B9ZWtvrW7P9jE_OusrqANjE7S0QE3QXn4Ubh9wiXhqArCrQmavTn8FEjBlfTSwaEIlaFPTFTpHIUlN_6TJgDjjg6wBX2t3UHLd5o_ohAxDW7XUBO-t-6kf910p2CRkXxhWVP4xtzZ3zOSwfs5aDveZtTbc_GdYNfvAVb6rMnyy1W3a2eRjGkmlPKZut7vPngQi2iqghtrmWV3knC7lpQdAdmteyqNUzrS4z4HfGwBPybQVeMso6mr4W6SXPbz8IsMYOYEyjqhWdoDw5Dk-E9gBVeDTcypdWS4uj7AG1VTiRaT1zM1B0E3VUu5c11kbnFKca80XV-IbziX7kY67ppA1PiqLGwOrHRuJDuoktfqUObd68vZsXXQz-J3HYwqu7jV8CkPLgLOn46BnRh0QqwByYbiNxFJWw5q08XUM7lFFNW175JESJuH2ewBXQFSxroGiheuQz0ghacwNruhH1N7mQ5PpeJBCRT20TZXKi2kpUA-of0cA3uZ67TwCw_8OVhoc-RH4GkxIMZkBtbYdxCQsjZm9aisRLue4oN3DXw_JS1bZp4xQ596ASxnsYx00Zb733mf54iFRTHfWMlF_j_YJjWO_lnsmaZ9-oLOwXeEWMv6xj1RJMShGwRl1doVfGJFPoDMmWKuXt8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SFWDvHkZZDuqX-QKJEjhy3j6-9I_0KFZkFnVSMhlyM_29Igby7RFGPve0xR1BuQRYF7IrdSfGlZe-TMZOZkSivkxADfJp4fwDdeI7TD1H7V4pcX1umD8OyFomWkrtm5KB4IIIIS7dGQEyuTqlX_Z0-4WGZB0XhaSsmy-1Dhl-CjB59tUiq90YhuIn-rGs72EjjIB035cqW_qGtf62b7xcgHWedgmPbqEbFLtfUAKZLVcK-LDwvCyQUFPwpIg1H21uxfPD_WSs5kV1AjztR9_hjxbAMLM5rRaD1xw6NIdrhh6NTA1wSvO1zBNUDiKkEkknrp24bTDcpoJj8Xgz7gbgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SFWDvHkZZDuqX-QKJEjhy3j6-9I_0KFZkFnVSMhlyM_29Igby7RFGPve0xR1BuQRYF7IrdSfGlZe-TMZOZkSivkxADfJp4fwDdeI7TD1H7V4pcX1umD8OyFomWkrtm5KB4IIIIS7dGQEyuTqlX_Z0-4WGZB0XhaSsmy-1Dhl-CjB59tUiq90YhuIn-rGs72EjjIB035cqW_qGtf62b7xcgHWedgmPbqEbFLtfUAKZLVcK-LDwvCyQUFPwpIg1H21uxfPD_WSs5kV1AjztR9_hjxbAMLM5rRaD1xw6NIdrhh6NTA1wSvO1zBNUDiKkEkknrp24bTDcpoJj8Xgz7gbgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=cfgKid22aYf6kkoFnDUgNAE4hsP6fSVm7jaARichoX5z6vYcGj-trDmNihBmG5UhOLQ2MPe2RMSNq5BYFFETLokqgbQBVcpSnFrEGt22X5muUSzVZVJ3WiBP30oLdwbohjkTeI0o59SnUOCZWYi7_yX9reCCBHuBQedpAOJ1WpjOovOBOf8wghflIUBrZ31E0MMlxYbpuVGJJ_jXjZvRLQE8bQ3dEofyA9_CB_9_Wf2cGJZZTiQ0QQ3Y0VcDzofZjyUsDurEG-h5enOKy3OM0c0V3GbkCVBXS_R5127Dduzh3Ff-65uesaoNPz1ZQK_9AM5uOrdKQ0j7RMef_lXcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=cfgKid22aYf6kkoFnDUgNAE4hsP6fSVm7jaARichoX5z6vYcGj-trDmNihBmG5UhOLQ2MPe2RMSNq5BYFFETLokqgbQBVcpSnFrEGt22X5muUSzVZVJ3WiBP30oLdwbohjkTeI0o59SnUOCZWYi7_yX9reCCBHuBQedpAOJ1WpjOovOBOf8wghflIUBrZ31E0MMlxYbpuVGJJ_jXjZvRLQE8bQ3dEofyA9_CB_9_Wf2cGJZZTiQ0QQ3Y0VcDzofZjyUsDurEG-h5enOKy3OM0c0V3GbkCVBXS_R5127Dduzh3Ff-65uesaoNPz1ZQK_9AM5uOrdKQ0j7RMef_lXcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dKYMlm22a5SB5SLG88-YJ7JPeIkETf6uXLCRzR2K7hXpMydCurCMybD09VJTSaqFAPjBralTFQmv-dkMXIuUtL933KFna_ryb0pYpgELCUbxXcoLVJi_zQztP_rTh4-XsYUw0QaFUlK9_2ztZvN_0yJoQ6WHqAY--qL3DHQTtlj5Z7lggvGn9aJf_kCQC3Rx7emcynRa6Qf98ZpNm0qbYXQCvNvKEEOQiZbgDTAqqZNxy57Dc93rP1ct1AK42n6YtfKky1QNhCx8l8VhWeY6Zy3NyvOJ43dGrmGRBMWzIqAklAPc-Vx8Tim1U0AQzJC-U0DKr--X607CwJEMf8ZZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P217Xh75l5wZ__CCY_KadyFP2AjyHlUGkul0hoBjAq-xX3GLOnTh9SSWmN8oeF6m4Bw33MdqeH3kB3QYkk8K3SnCzssJjLLdwrKor2p826wUdQuI72leZp5Fx4aTfHjTnKR-oKKhZhFJzx-6IPZH1NUpRgY9SLwVzOMZs8d_G4BV_myMk29RsyJu7-rOEAOH93_lKL_rokbTykCLhJYaUHEs7gNJRbIsMhHe9w7KZ3hgTP1LCjONWbuPm37WKfd4A4rFMcLv_ez2IUiADQvt9Oetxp0zNZSYup4j8GAGZEZ2WXYPeRL3QJKgM-eK-axydqcOv0NQaRXFlbqupI3wsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=SIDFBbS1wqyq2Gq4Y-XYq58m4a60QWGnVgX2ovEBaroxqdhj4rgVy7-eTzR0KVzgFmi5V943-haiK185iAyS0VUQV-_PDx4S4DB7JejC9pOIuXceQasJT1dfrP9Ae1vyiEC8mUhGWiLja3ue9HOVfU-1dbwyQSRTkvBL1BC6iL_yf3z_vh-HgrYpwxMDOutlc-4LWwigRvnuVcMzy8Lf5RVYaiFHk7Aq34ASFVAq-iQjIqV5AuEL1JZQ2p-ij917nCldpFei4wqio8pHyJJyXLGQL0-VuXgcf6CRnCVl1bWIsYL6ZACRXGJKpBmxjQrFlxvECbpwOFYXjYPGCVP8tYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=SIDFBbS1wqyq2Gq4Y-XYq58m4a60QWGnVgX2ovEBaroxqdhj4rgVy7-eTzR0KVzgFmi5V943-haiK185iAyS0VUQV-_PDx4S4DB7JejC9pOIuXceQasJT1dfrP9Ae1vyiEC8mUhGWiLja3ue9HOVfU-1dbwyQSRTkvBL1BC6iL_yf3z_vh-HgrYpwxMDOutlc-4LWwigRvnuVcMzy8Lf5RVYaiFHk7Aq34ASFVAq-iQjIqV5AuEL1JZQ2p-ij917nCldpFei4wqio8pHyJJyXLGQL0-VuXgcf6CRnCVl1bWIsYL6ZACRXGJKpBmxjQrFlxvECbpwOFYXjYPGCVP8tYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYYgz3NLvAK8PYXn3rYfbNexEa9BLMaYrqH7e5xgMQqssySi6JFt7KuXPLWqUyAAfs7ymcOgyTidZhCFzju9vWRDEgewmUgpVypjB60XLD5kH6FM5pD_mqMKB8rAJBm84RiCRUBMOCReYDbgqoCqjsJkj9qRWAIuQFrFnxFkbRh5Uiil3L6n2qVRXvBJRTjYz8nT8MT9C7q_VlGw0peSw57hlsl-q9N5PEKNfpD9PtSXmJDSXUQ1Lr-iRldde26i3RnXu50XMRbrbJyQ1jVI5NhZl84LTr319t-g1CSoPuSIcFsmuhbMxvTkjuH1WZbhdHmIXh1svoww5iUAXY1cRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZSaYktOEVNRFttSooFErTSOQb0dEGwNrUYQWZ1YAIJ9lZYvSEG4DnJ5zQKGACxWkVIQyxEEy3S038oYup9ZilDu9VpAYdNo_2gprFC6YumCpMRdMyhIn7dZneBQ49SuRcW_Tj-2_vs0x9CcJZuB9FZ7r_-ZAR_RONmhyQDylYXZWBl3dF6JgkroLM7myM0FGHMYXGdq-rMt3POhV4GIY3unRre3pMiuWhZWNBwnOv55v6MMxC_7Wwc2gSOdxB4oLlWMZyuvPV3o7Daf4by1peis0J0wEQRHiLDDhSFsjHzX6cLihXNS3BdgU9i3VCRCZDeDNfiQcFdd4y8oqZTJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNef3Y_UWY6bfe925IwF2KZKykhTzaYA8VpEQRVKjVVB-8sBxTcaTaVBFVfbxzOhG2_hsthsgUOuwg1wNfSXTEEYtAiPdsNoEggiWQ38yX7h1G24dIuu8C--yHJl46J2bc-YWdaZziT-ID03iiOAvSDW5_Ws6f46nvRmrKcqfO4nkNBVVjBqnGGbLRpvBfCDyKNLegTrxDvxwSyM8ZTWHJsBjhG6wlwv0614sALVQteZVsbeRylNsi0rc_pTuhtp7_afljsJafsH_E8jvowEKxSfVDpZYxLr63OihhBK4RPwWDrMixonM92h-x-fk8yfjozARja5W2nWfOxya2kYFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibT_ql4dwTAvsWh6aTFF_WZ4AU0L9fL9ERNi-1aMYZVZQKo_kTPTLQoXuYHkLOuc4UJP4F6JWhFEZUVfCySmx-qJSecEREvMqjLX9XLeDol3E6w6_KvlPpaIvnecqvYxJroSOeESq_RjB3z22XyM_cFeFa5BQ6j2hyjxg_aoF0kzhEcnoaaIXvCzQAvHJ7cuMg-FkPFB4cwl3dnYIwXUMrsa5LpurlgKjjJraccza6TT0APIyxj-UDZ-ELG7a2FeasYp9dsH02j1oLE8tluCn6xlQM0RqQzq_0nt4F1qH_NGhU-4Y32CBfXGpFHmIMtVPM67Aqf__RFlyoa7fN-22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZKDJBKUFvkqQ_zq1yZvIY-0T3MqMY11tnngiedAHkvpwOa3kMQmJ_Na1v4qCiuZWE7rbhjuM4nRDULjLLPJTzzJxiL_v2jPyiQt-Dthkp27LoquZPED69ngALh66_xwWc29KWUa1k9DcPduQQKb7SoFEhnTcx0IM9Cf9k_wphKlRL-eL1Cj8Y9rrtc8RNRUXZYkKA5axJHz2G_ti2nIZ4j5gKxQMvZRY___yIUKm2EnECcdGvLJsHq-pva8pP6yISGpNqnAanG81ZiShkwgG4QKI_bDN3JRceUCu8bbhGoQhWERyn8PYdNVpRgb-v2mVrfRY05SU4px344HNcl4RKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZKDJBKUFvkqQ_zq1yZvIY-0T3MqMY11tnngiedAHkvpwOa3kMQmJ_Na1v4qCiuZWE7rbhjuM4nRDULjLLPJTzzJxiL_v2jPyiQt-Dthkp27LoquZPED69ngALh66_xwWc29KWUa1k9DcPduQQKb7SoFEhnTcx0IM9Cf9k_wphKlRL-eL1Cj8Y9rrtc8RNRUXZYkKA5axJHz2G_ti2nIZ4j5gKxQMvZRY___yIUKm2EnECcdGvLJsHq-pva8pP6yISGpNqnAanG81ZiShkwgG4QKI_bDN3JRceUCu8bbhGoQhWERyn8PYdNVpRgb-v2mVrfRY05SU4px344HNcl4RKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=tCLSRxmBFGA_R_HTRNnE_4QJ_6LCaidnrUzjFD3t4OPyc6wEXTEzXNKatJUx--OiZ6WeT5Q1Q1ctYR0p5LpZe5anY-TwgjOW7xqK6F2xiDzfHPueRXvDAGQM_qi6k72rR8CdqDn8o5X66a_9sV1WqkWp6_e7gGxGG8h4iNtV1xQp5mOwoe4aWgXJwsiBaC_Nn4Y9omkpwPk6bYjCnzqysjw6OnwDiJ0KE1EFaF-0Ei8Yws3x5ebqvtRE6fLFn8RXOIB3TLxEPQFWBW5VUYJ1YmA9c5PUQ_HiceyNrM7gvkP_M0vBKIa14j8M1WdiQ6DULiY4RsSnkCphMjQzHTpfZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=tCLSRxmBFGA_R_HTRNnE_4QJ_6LCaidnrUzjFD3t4OPyc6wEXTEzXNKatJUx--OiZ6WeT5Q1Q1ctYR0p5LpZe5anY-TwgjOW7xqK6F2xiDzfHPueRXvDAGQM_qi6k72rR8CdqDn8o5X66a_9sV1WqkWp6_e7gGxGG8h4iNtV1xQp5mOwoe4aWgXJwsiBaC_Nn4Y9omkpwPk6bYjCnzqysjw6OnwDiJ0KE1EFaF-0Ei8Yws3x5ebqvtRE6fLFn8RXOIB3TLxEPQFWBW5VUYJ1YmA9c5PUQ_HiceyNrM7gvkP_M0vBKIa14j8M1WdiQ6DULiY4RsSnkCphMjQzHTpfZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCuDt0hD964SB3xnLJBU9tN9t7HuATGs5sHz7MXJKWmi8GaMjYdmCNyGtiXS0T9b4POed8p7vyqDHvld4M6zjnvHv0pL0p2G_nefT52IXYZUMUnNGfD9jLoUkRX0hXY6eA6PGf1lM5qBQLCxD1vWOFzoWwYOiWH7ZNeMJkCHiQQXYfzFnICivaImVmvGdtOwATWEO9IIefmPPCcwQy-j5UY-kSX1o4Pr0OGucCrDTThl_bchRnxYT0-Z-MSkjNmuGlSIzwKARjoXDIyD-YKLlSPXiY05hR5d79S9NzkeQYaECkuhvBQIb0n2_BLpWt-JpjZc7WlbpNowys72i-Fqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=nNVBg0iwHl4UW4U57peJyZbDvcBl5NwQ8AWlTZRKHGTDp0kSd0LRRV-aoquwPbXs1ykaUAC5XLr65Nmg1FE2e5XPq5ISY0r9hORQHVVdFE1tMCtcW02koGS2KbDJ5CKmnc0thHhZKdZxo0_RSsM9et_gMGiQwRVUQWvFKKQj1FK8yOfa_eeksV42xdrZeyJCrwZNJqr61jinQv68OuzUCj3c97tCfxB01fyT7FWHswQuuF2ZJDJkDowXtqkraLRlPj1JcC1fiShfaE9BkJQiqfND3jw23iup5gfBIBzVIZNp4ojOTOXVMNatqa86Oq5bSnDIzJmxvwD2SoyyePfz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=nNVBg0iwHl4UW4U57peJyZbDvcBl5NwQ8AWlTZRKHGTDp0kSd0LRRV-aoquwPbXs1ykaUAC5XLr65Nmg1FE2e5XPq5ISY0r9hORQHVVdFE1tMCtcW02koGS2KbDJ5CKmnc0thHhZKdZxo0_RSsM9et_gMGiQwRVUQWvFKKQj1FK8yOfa_eeksV42xdrZeyJCrwZNJqr61jinQv68OuzUCj3c97tCfxB01fyT7FWHswQuuF2ZJDJkDowXtqkraLRlPj1JcC1fiShfaE9BkJQiqfND3jw23iup5gfBIBzVIZNp4ojOTOXVMNatqa86Oq5bSnDIzJmxvwD2SoyyePfz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=hDmfo5jdTj47Xd_G_XAI54t_txKmII8-gRSC--Fz7u5r9jeIwGtfoVnDgPc3csXGl4dxwox4oFKt7B5tVCsrrmj6GHQDK_O72qqK83YZn7aiVYaQqRAtFCZ6xxw-9lEFd55GAcr8HdRHdHIFA1DknURDVBtGKd4Fw5LFAzCfgO7jI5MJx5yQM44zjNAHj8o_P62frnTfQvNY6Bi6shb4ZcNkI6ngeb1pJjS7l7o1j4hD4jeo26QmBSo1PF_inoIO5j8CkuUHzAc9vxAUPn448vUXdYjCV8h4-v_6Jn0yX8ZA4mDpue34SoJ57KRFHanAYKj-Fauxsw8RO8RmXlD3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=hDmfo5jdTj47Xd_G_XAI54t_txKmII8-gRSC--Fz7u5r9jeIwGtfoVnDgPc3csXGl4dxwox4oFKt7B5tVCsrrmj6GHQDK_O72qqK83YZn7aiVYaQqRAtFCZ6xxw-9lEFd55GAcr8HdRHdHIFA1DknURDVBtGKd4Fw5LFAzCfgO7jI5MJx5yQM44zjNAHj8o_P62frnTfQvNY6Bi6shb4ZcNkI6ngeb1pJjS7l7o1j4hD4jeo26QmBSo1PF_inoIO5j8CkuUHzAc9vxAUPn448vUXdYjCV8h4-v_6Jn0yX8ZA4mDpue34SoJ57KRFHanAYKj-Fauxsw8RO8RmXlD3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d3gPF0syjj6YptdwKbEPEks4R771e-05R6InyBcnaYGYLZKLL7JdLiSN1v67C6Fk8uONrxoIpIZgsn1Of9PmfRX-6HqOUwsY8MXrB2eNS6geAvQOGAg7dVL2o5CZHXqCXCtPrWKR0ZXHX85Al5v_Xv4JUMuyAPU37GP1U9lUIR7CMQJle8dra7Bf2l5LjvgotgcTbl1J7MelzyGfJRZal096lHNbpE81JcwZxa2bm2AkLjjFVdlkxIyFExKStNB1f-jrt5iopHtrzb_xCwL32lsFYMwWMlcpX3no-cNcRWA1_NiO0A26LQvlL_cmMVjkHK_DgPfpctLuJQOsvxoJEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d3gPF0syjj6YptdwKbEPEks4R771e-05R6InyBcnaYGYLZKLL7JdLiSN1v67C6Fk8uONrxoIpIZgsn1Of9PmfRX-6HqOUwsY8MXrB2eNS6geAvQOGAg7dVL2o5CZHXqCXCtPrWKR0ZXHX85Al5v_Xv4JUMuyAPU37GP1U9lUIR7CMQJle8dra7Bf2l5LjvgotgcTbl1J7MelzyGfJRZal096lHNbpE81JcwZxa2bm2AkLjjFVdlkxIyFExKStNB1f-jrt5iopHtrzb_xCwL32lsFYMwWMlcpX3no-cNcRWA1_NiO0A26LQvlL_cmMVjkHK_DgPfpctLuJQOsvxoJEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoqIfq_zesm7aUOoFhzUHinXC3hl4R_wZJziiRjj1ipjgbEZEX6rU_jBxsR79JeoYIDOhIzXhs567n5D3C-JXYy6fX72NGM13AXOR9aCZZS_D4Q0v9CmVd-TjL5I-3uw3wH3cPqImdCSG6X2c_9_VvFiofOYyv5dzFt-D0J9djv50xn3HJyjGWydYKtASuUjzyRbmElSSkVWQ1_jPRu-0RmhkOzke_qD0Y9stXi1QauyLpTNeGipm5_6hcMtSRvKMIRHIwEfObFd5we8rwFvxWfO-EbTCn5kj80aWR2nZwxfxvhD5V9_0AIoW1fHwFD370dbZlMx0s-XD5gLPTYLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=v7cMFiYuBI3-ma3Vo6Lj7kEDs3qtIXhtpHaQVCcw-aWN0M_0ccqGU6O6IzYIeenG5YA0mo6KvB1JKEkFXHyw9tL6AL3Zjb7H0zP-Z1MHPWi2OQA3EvEtHWLTlagy9KU2ASXZcQ9LqfTgnszgj-mgj7JVFxgGoNsvk1zK3izP4rBV7GxnCJoEq8mpmkMovfFX_Y68irwCM295TMjSu3-a4dAuNcmgyRy3_Ktfv4yTEmBnWmqYwbvPJ0C781GCvbRSO8oPK_Sr21YDgxGv1R2gvtCY0SKeoAqFdjU0Oqkuz8vj-bxoGeDMT34FeQ9inaI-Rqh1ZIa11FHF_LyRZWPQTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=v7cMFiYuBI3-ma3Vo6Lj7kEDs3qtIXhtpHaQVCcw-aWN0M_0ccqGU6O6IzYIeenG5YA0mo6KvB1JKEkFXHyw9tL6AL3Zjb7H0zP-Z1MHPWi2OQA3EvEtHWLTlagy9KU2ASXZcQ9LqfTgnszgj-mgj7JVFxgGoNsvk1zK3izP4rBV7GxnCJoEq8mpmkMovfFX_Y68irwCM295TMjSu3-a4dAuNcmgyRy3_Ktfv4yTEmBnWmqYwbvPJ0C781GCvbRSO8oPK_Sr21YDgxGv1R2gvtCY0SKeoAqFdjU0Oqkuz8vj-bxoGeDMT34FeQ9inaI-Rqh1ZIa11FHF_LyRZWPQTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyOsHQQdEVRzRQ3Y8cbdUv9eJu0Pn4M3jqAgDLn0QAWHZI6x0EOhcWPpxnq7_sSiguUo1wkRFhJfyG56rVRWzNV1mk3Hk2gf2yc7GBuK47V62d-CNsMxd_kyhaBx4sQ4d3hQ1byiD94BkNPFT1mMoAniA67A26vwCY4RUskezf20yoYQfk3jciKYw9NBG7XQPWRgvHHA7NAepFL5dFRpi8u_z1hJQ9Bf4Zj4z4Ld5VPFG-d9wh_1p7qtfvh6fITTmo-so-JWzsNiJxX8QJ-8zRMy7dgFBKYRPPb4H1vQZHooGteLkszAEGIQGbZZg8FwWi0PzlLtOTX2JOAC4L3qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPgWryUGOIxz5Ax47fAKXrlCwUtAlOOC6ook427qnc8qLM8ogwegJ0EGWXf8AyPznQRZO1PcE7wD6Z8sbWFMRkGWJKUf1Qf8uqlv_uNH6Q5m0guyhEj3C90Ogkg9JKp7XBmHtli_1evDnU-nTD5Nv0pMnC03mdWlKa_SAwWoo-FX9oz--CQRIrlgj5tegDKBGayND-UQEFl1GNmI1h7YD8T9snCiiq-B-XyaqgK_RJMDrRgXrfR3mkgrpolCTsAdUT3j0qFEn2lAnOseNvUSGo6bcLDPGCH0W2tLeoMiR-MnEVJKOCoV5FSxAjRfmvq8WuAh2AAoPur5rlERN40DEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=jEYA7VAyc1tJeRIpC2oLntFmnGD8SvVDi1r0y1w9kwvdQ34SsaMyuf4Tp7NvS6S_Pvt36oY5L3o-y8Ajii3xM5tNa6hNJ7jUzj5JiOclyoeZVf8OXxTPSqy03wzWzwg7eGbFJhhMq3yjD5cx8xN9dq3TDZGO46fk0laJrypmuHCgkQFIrGD8nagmpJy8EkWxwfiSRCLBAyXuAKoDSYjrk9TdAvlYPbhQsKYbTCtGvUZAJNKdQzxm9Wmt2ish3TVa-tC_VPQOROQtsnROd4H4cLvAqPo-o0hFE66gT9Xi0yVqZyC5CC0tq_xwj467xvfYTY39YYo6oKnQJETMQuFN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=jEYA7VAyc1tJeRIpC2oLntFmnGD8SvVDi1r0y1w9kwvdQ34SsaMyuf4Tp7NvS6S_Pvt36oY5L3o-y8Ajii3xM5tNa6hNJ7jUzj5JiOclyoeZVf8OXxTPSqy03wzWzwg7eGbFJhhMq3yjD5cx8xN9dq3TDZGO46fk0laJrypmuHCgkQFIrGD8nagmpJy8EkWxwfiSRCLBAyXuAKoDSYjrk9TdAvlYPbhQsKYbTCtGvUZAJNKdQzxm9Wmt2ish3TVa-tC_VPQOROQtsnROd4H4cLvAqPo-o0hFE66gT9Xi0yVqZyC5CC0tq_xwj467xvfYTY39YYo6oKnQJETMQuFN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZBbT4SwxDmuna30wu2zolq6VDX__T_DPTkgbG_BPQL0FTzviOzXrwvfkgkuIq9CvLwOpfVb-PcLYAoxg_KjrM9oKXBw0ia-OW8-QX12ZUH5W6pFMDXJ0HGSdiDlR_Tt9tZg6mdDkqtK0WZ3me1P6jVbUkdzFiV9v7n9avIVVGFnnqc0l3fwBIYLCYeOP-VdjX5CbGSxXS1eGwjiicOV8gppy8MRzStMu_sh3ZOKh-MSdMqT1zHXmvzKDIzEj8yPPEB_l7ttjCuyzBgaYZcOVjCE6BKvbJXiop0OOcC8-qa7PYC4ahOjyMNsR2njikq2mupW4g_58x89jrb4eZyVK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZBbT4SwxDmuna30wu2zolq6VDX__T_DPTkgbG_BPQL0FTzviOzXrwvfkgkuIq9CvLwOpfVb-PcLYAoxg_KjrM9oKXBw0ia-OW8-QX12ZUH5W6pFMDXJ0HGSdiDlR_Tt9tZg6mdDkqtK0WZ3me1P6jVbUkdzFiV9v7n9avIVVGFnnqc0l3fwBIYLCYeOP-VdjX5CbGSxXS1eGwjiicOV8gppy8MRzStMu_sh3ZOKh-MSdMqT1zHXmvzKDIzEj8yPPEB_l7ttjCuyzBgaYZcOVjCE6BKvbJXiop0OOcC8-qa7PYC4ahOjyMNsR2njikq2mupW4g_58x89jrb4eZyVK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=mvskmXiecKXKCtsWc9cNEtoYaHcKB0ZBah-JJg2cKeG7yO1ov21btzR2ZcMo_KXXWXm2b5H1NOzV5XQfBrknOPKhPXuIEecaKWIYzmn1pt5MaAbTT18idp_ni76mHXsflFVKPy_YGkns_dCf4IWVeEVUVQysIR7j4pz_K4Pm4JZQQVyFT54Nlo8GsiYVfxUp-WOKN5NtrfvgZNCP0jfkTShaGhuQdA5QiHQLXG7UcWEEN5aJRkz_2OPW_tDtPnKWQhu_ts9P1DdKWhPchD6SnGEOWtIM0fmQ4JsjC2JwbAu--IJvMBgNCsf5Jfa2nsfABwTYV12iHZmchBu1P-5yew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=mvskmXiecKXKCtsWc9cNEtoYaHcKB0ZBah-JJg2cKeG7yO1ov21btzR2ZcMo_KXXWXm2b5H1NOzV5XQfBrknOPKhPXuIEecaKWIYzmn1pt5MaAbTT18idp_ni76mHXsflFVKPy_YGkns_dCf4IWVeEVUVQysIR7j4pz_K4Pm4JZQQVyFT54Nlo8GsiYVfxUp-WOKN5NtrfvgZNCP0jfkTShaGhuQdA5QiHQLXG7UcWEEN5aJRkz_2OPW_tDtPnKWQhu_ts9P1DdKWhPchD6SnGEOWtIM0fmQ4JsjC2JwbAu--IJvMBgNCsf5Jfa2nsfABwTYV12iHZmchBu1P-5yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sirxIzM7oumSbly49Kixzn6yOwfAREn4Ztush1cerLYxpx1bsSziMMCPYDBDXf1iotWsg9emkDLaKL7ij7qMr_9JfPXk9osZ11EVP_KCeJhn8eAzteG6FZqOsFIa25pu84S7Dyb982XPbINx1qWiRmFFMEw0K4BYBNKqB3sF5YhEo43VwImO65ddaeQ-PURzLLqw48xd1wV8vJJYfKFMZdSLfBer6waspIBF0NXKF1LXu_Ww7_vpd-4CUVfuGvnPFDjEv9XNs0RKUzhRecBGOV_M_PgchlApswWKd5n-XIZSGghy6PsMtz3Kj66FEIg_zKJkCQpedGq7-v9_CFAyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=esdc6gNtcdzAJGjNchk4FaHHhoDzbyJqscq2uyXYVa56HcLL07UaaH8Brcg4Eg6-NDzoY9FCfPTclVdlHePC-z6Vl6NmwSA0npVIrhKizPlMfsDA-MFYamaatPrdEitYJygVBkG1HqMjLZKHiwjC3Qy7hf1e6DS2rqTiYT3IVQcSdI639Oy1VEeAdUh9-asAoCOdOEF2RWvxsnFTli32E99QHggkYzTWHo8bjiRA_Ui7zK3V7t7ljjQ8t9SvWnEeBZ-pgsp-EQd3UFBXDYvC3zulvwmjvYMBrgvLxYpK6-6UDeH3K7HW2vbtXhmNakY-TiXraa6YjRG2wIY55nqndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=esdc6gNtcdzAJGjNchk4FaHHhoDzbyJqscq2uyXYVa56HcLL07UaaH8Brcg4Eg6-NDzoY9FCfPTclVdlHePC-z6Vl6NmwSA0npVIrhKizPlMfsDA-MFYamaatPrdEitYJygVBkG1HqMjLZKHiwjC3Qy7hf1e6DS2rqTiYT3IVQcSdI639Oy1VEeAdUh9-asAoCOdOEF2RWvxsnFTli32E99QHggkYzTWHo8bjiRA_Ui7zK3V7t7ljjQ8t9SvWnEeBZ-pgsp-EQd3UFBXDYvC3zulvwmjvYMBrgvLxYpK6-6UDeH3K7HW2vbtXhmNakY-TiXraa6YjRG2wIY55nqndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jvcAl1hE-N15OXVess_a76UliyzIkE1Uoh1Q4N6XKFmAszIigUBZcQKMUv4ED0pZqXPcpHYrBh9UG8f_CoatVG7VnROOfpkgoIXyyW1aGT1JgNSAFf9Cib8hpe2mnHVzY0HxQm3rxvSPJU6gxyYgrVC8XC2TBM3jDLHPwI8LKJvoO-N3QqNwE_ILcgz-TBAPyK1pGuMAUt9lpm1waleuQDxQPhwLYnRhwJobHeSSpb5XYTJOmDU7nkGj5gGAwQOsc9BDOz1GmNJZUKSio6p_oMtg13FXF4C7bdO-b5zX0YI7Zw3_tOSOO8UV_wnNMDgPVYh44d_HT4eCaoXOTEX6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jvcAl1hE-N15OXVess_a76UliyzIkE1Uoh1Q4N6XKFmAszIigUBZcQKMUv4ED0pZqXPcpHYrBh9UG8f_CoatVG7VnROOfpkgoIXyyW1aGT1JgNSAFf9Cib8hpe2mnHVzY0HxQm3rxvSPJU6gxyYgrVC8XC2TBM3jDLHPwI8LKJvoO-N3QqNwE_ILcgz-TBAPyK1pGuMAUt9lpm1waleuQDxQPhwLYnRhwJobHeSSpb5XYTJOmDU7nkGj5gGAwQOsc9BDOz1GmNJZUKSio6p_oMtg13FXF4C7bdO-b5zX0YI7Zw3_tOSOO8UV_wnNMDgPVYh44d_HT4eCaoXOTEX6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KZV0dSDVN0R-0OW24CgLC1xeLJBiEZg3VMKmTD6dIY3pO72kcQ2SVluA_PVxtAYtiy8ZGhUjpDtslSr5WUPuHSP1u5OC60xOG-qOPcUvHVtkk-NdxHBq0DmMVcPKMLCsYLTwD55bDLr3OF-PSmEVEdhA0k4GlXO7IUX3SJbHCrJeHsemLTKXG7yYyO1TrVWMi-4heRxXNu1aQxt0QnWzrWm17IChOhby9yVF41DkUrHtylM__YH09J_DPrFGOnpgPfn4vlzdOC6KabE7Pe9vY_R7oa6DJLHTiQatIu2ILnbIwZwpE3xfVGeSD4Wr7pc4bHbEdaxKvmHY2p4VcLddfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KZV0dSDVN0R-0OW24CgLC1xeLJBiEZg3VMKmTD6dIY3pO72kcQ2SVluA_PVxtAYtiy8ZGhUjpDtslSr5WUPuHSP1u5OC60xOG-qOPcUvHVtkk-NdxHBq0DmMVcPKMLCsYLTwD55bDLr3OF-PSmEVEdhA0k4GlXO7IUX3SJbHCrJeHsemLTKXG7yYyO1TrVWMi-4heRxXNu1aQxt0QnWzrWm17IChOhby9yVF41DkUrHtylM__YH09J_DPrFGOnpgPfn4vlzdOC6KabE7Pe9vY_R7oa6DJLHTiQatIu2ILnbIwZwpE3xfVGeSD4Wr7pc4bHbEdaxKvmHY2p4VcLddfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meUevdQVv-WFei_GMljr5EwFjHNarc3UMyi1Unq9O6_MhoG49e4-f8aQG5YVDbKxs6TovHiO04NbncYQZYje5kQ9jC5g2ZOvQRpf-6wyNZy6QkMM4CgnTBtIiRIc3oNFGNdPzoCWinIoT3iKhnz_x-SguWXXbteMRpdEFVSkENAMZttYegz4J1vlFDFr8qrzy3L4sN8ZZdCJGnbclW7F-XQO9OziCq7EUisHCC3f0yrBkH0U5rThj3ZAsBV3HeWS52EZ-1FmXsB5TMU0JpWXrdDJ_WywzdKaMsjplkByEaM5yHfumY4G5MXRo82p_gClFWYaIawNijtdXUhIZBnleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meUevdQVv-WFei_GMljr5EwFjHNarc3UMyi1Unq9O6_MhoG49e4-f8aQG5YVDbKxs6TovHiO04NbncYQZYje5kQ9jC5g2ZOvQRpf-6wyNZy6QkMM4CgnTBtIiRIc3oNFGNdPzoCWinIoT3iKhnz_x-SguWXXbteMRpdEFVSkENAMZttYegz4J1vlFDFr8qrzy3L4sN8ZZdCJGnbclW7F-XQO9OziCq7EUisHCC3f0yrBkH0U5rThj3ZAsBV3HeWS52EZ-1FmXsB5TMU0JpWXrdDJ_WywzdKaMsjplkByEaM5yHfumY4G5MXRo82p_gClFWYaIawNijtdXUhIZBnleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py7LXldpEoWYpYXCkUaD5ma9ufC7eMyymG6g3ymAGbh7w__NFfjhuhgKVfI5yCF4Be0ywig54_QTdNQWYS7qFcD7jgXJJYG9M_0jUFhUa4oy5f36FnSVGL_bYG7KUSUV9sCZDpAh6AfHPT8uvewNqnr0SwC8EsR9240AVQ3lwNsDDI33ffA-ku6GuZrNmhrphWzzHHxqmsgA-kG96UBejS-nrw5t4UBECR6Sq5HbSiwwFENBTE0yoI00bJ_oK445nl0To6F8Xq-AlPw2iVkxXw_I5jVy6zHY6yaX3NwpkAk2WETX0T3v2RrVdWr1pVyIyoya80rckYB_lF6HRmKa5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=AmExdtqVZOKcXZhHgGkVThS0xCSMsoBgewnt_5spicDKYO5VjifkMOvyuqR8yfPTqEobK4_tsPTT671p55vzmKQxPZkMThusU2m9cROvrSMdSKeExJOvx5kG5LuSwyoZd2Rr9JVg3xSTbcDJ6oEnDqBmxKbyOUJgAKP98wddi3hLry4DTBofx4h6vimbf2j7VBjFsfIDHOzQ8sGfZ3yQ6oTPX7BJTrbTyaOOZIx2zr-AOn-dSZUYYUA_8hT3fkN2FvPwd8YmVv6lSqDOL_wz0F1AQR-D7YdrVyIoyCK0gXI-kBQTWjIi1FV20_OQu2U2h87O4a-cS-vQgqtENZQ3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=AmExdtqVZOKcXZhHgGkVThS0xCSMsoBgewnt_5spicDKYO5VjifkMOvyuqR8yfPTqEobK4_tsPTT671p55vzmKQxPZkMThusU2m9cROvrSMdSKeExJOvx5kG5LuSwyoZd2Rr9JVg3xSTbcDJ6oEnDqBmxKbyOUJgAKP98wddi3hLry4DTBofx4h6vimbf2j7VBjFsfIDHOzQ8sGfZ3yQ6oTPX7BJTrbTyaOOZIx2zr-AOn-dSZUYYUA_8hT3fkN2FvPwd8YmVv6lSqDOL_wz0F1AQR-D7YdrVyIoyCK0gXI-kBQTWjIi1FV20_OQu2U2h87O4a-cS-vQgqtENZQ3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=e1nre8z-MbwZMlm0Psr9ju-DzJAoBVL4iZ78RfwM9CkQEbrnM_2UavwDX7iI_tH5ENjVHKtRFDdtN_A7JHAO5Nx1wez-iVW7XQJsa5eO60FQOdVEHI737rOr-3KaIIFW9RDU-GaXkpsTVDGoKx7xPxoe-EJkNgdsk03l0WuT1V-wM3mInjDDcj9GraxdWvrekJUjWOmJlVsa36428HcMwwUNK-osybXVUMjleLCzKeenKwm6xm5uhjPfNXMVyv7sIwK93RYScd3goLtyMdwCLxZsUbH1OhWFjK7NRwGJc9W-N2sdlqk3V107R4MefnEDsegxAuFPtIH07lE70OoGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=e1nre8z-MbwZMlm0Psr9ju-DzJAoBVL4iZ78RfwM9CkQEbrnM_2UavwDX7iI_tH5ENjVHKtRFDdtN_A7JHAO5Nx1wez-iVW7XQJsa5eO60FQOdVEHI737rOr-3KaIIFW9RDU-GaXkpsTVDGoKx7xPxoe-EJkNgdsk03l0WuT1V-wM3mInjDDcj9GraxdWvrekJUjWOmJlVsa36428HcMwwUNK-osybXVUMjleLCzKeenKwm6xm5uhjPfNXMVyv7sIwK93RYScd3goLtyMdwCLxZsUbH1OhWFjK7NRwGJc9W-N2sdlqk3V107R4MefnEDsegxAuFPtIH07lE70OoGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyYaQq4q9JAQiihPsdzP55gUljsqa1RjLtzopmvyBLmnhA6BO7pyugjv1py3aKBQ8CV7Vs5kPmW0mZQvqMp5iJAMmXTF488SGOr1fAwIYjRtH-J_1OVfH6k3HWcrdNpWbwPcla-BAm3je0_7dstyi2-4ENoABnSPp_lob_ENEKSOTUuCq7c1oN2KlmODLFOXTUs61juIMWnIp9f-xUVbMSlWyfKKai7tmji3MNWda0yNjF0Pk9TVXMc8SaRFZT9CXuocGpTZTj-yRTnCmPrAedCKnuJC5wFdHqXnKXqkirT9oduDcMFcoNZp62-EG2e7jQWu3cbuMTWk-3AkrihBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bDZSViRTbdsChlLQYgyWuzxhHCN25p1xEmXsufMSeFy_lTBGv0sTuaAQ1E2lgVzl8xiJA3-dvgLu3qAkMi4MoTicOwFNTRibLv84tafiKR5T-wut97-wuvtsWAzqfNvz5q2sgYPYKaSRTbGLW3azjnTU44pl8R5eLIC89KZWLuSstMxqNwUmrjRKKCHdKeV3i1uGcU6gR0ShHut7tm9fyKsN9HJWq8hrJOvJeQY0x8-iWIQWuc2wyTuziAEqNihl4qv-JTPBE75-ESI8UtPljB3ymLUW1GNrBrrRENOEUpPl96Sc-sCVKodTycLenoyk4jOC7mL_pKZEHv2X7fe0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bDZSViRTbdsChlLQYgyWuzxhHCN25p1xEmXsufMSeFy_lTBGv0sTuaAQ1E2lgVzl8xiJA3-dvgLu3qAkMi4MoTicOwFNTRibLv84tafiKR5T-wut97-wuvtsWAzqfNvz5q2sgYPYKaSRTbGLW3azjnTU44pl8R5eLIC89KZWLuSstMxqNwUmrjRKKCHdKeV3i1uGcU6gR0ShHut7tm9fyKsN9HJWq8hrJOvJeQY0x8-iWIQWuc2wyTuziAEqNihl4qv-JTPBE75-ESI8UtPljB3ymLUW1GNrBrrRENOEUpPl96Sc-sCVKodTycLenoyk4jOC7mL_pKZEHv2X7fe0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=noeP8p5DioAUdN0K7hY2XyvPXPyYvneNT8sc-OKEqaM1PnBHJ51dKoj2ECs5dWKFfa--eDMo3mreJig1_KghZ3zcHu92POcYYI6EX-94ex7KvpYVSfQ2qrcXlOOZEqkFVtwoK5evpxKTBX2HN4ffjnFnBGMiX1D-O-8MLJs-c-DN67RmaWy8DmtjhMKo-W8EvcYsL-GGVBCTRVhndzrfsz0BFNNQNuXzj9L1xEKQSR8icWqxUf_9CcDxrsgI1NKOmq1t-a2cVynzbOknCvabTtqNCGHcruPShQqkDf0oTtH-v9AKrI5RxExlJPCBki1OK2JPbHV1GNIzZBTGZksc7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=noeP8p5DioAUdN0K7hY2XyvPXPyYvneNT8sc-OKEqaM1PnBHJ51dKoj2ECs5dWKFfa--eDMo3mreJig1_KghZ3zcHu92POcYYI6EX-94ex7KvpYVSfQ2qrcXlOOZEqkFVtwoK5evpxKTBX2HN4ffjnFnBGMiX1D-O-8MLJs-c-DN67RmaWy8DmtjhMKo-W8EvcYsL-GGVBCTRVhndzrfsz0BFNNQNuXzj9L1xEKQSR8icWqxUf_9CcDxrsgI1NKOmq1t-a2cVynzbOknCvabTtqNCGHcruPShQqkDf0oTtH-v9AKrI5RxExlJPCBki1OK2JPbHV1GNIzZBTGZksc7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=HAdCtlPDWuHd-tPWP8IToSghphIiqfJtuSQHDhJ85kcMkijN2ehqPFHIaHt9qSu-7F4aSR5OXR1qQvYHl6VvcrybQ_2oEdNfh4z-CYV1zBEQ7KKZnCdAW_88BkWWLBPsPukL50-rQrjiRrqijzjWMYFavzcHedLpgNII7zc_JRFbtQ5EKWKyAStNeIVmSZbd1I1uJm1OXmG8QTOiZDUvsND_znE0OvWRTy5sHYHeacJ9RCfN4VW5Mxy3UUoknbK4v5JVTQ2zMMPSUxFqh3nlZQ4sdX1q7zkhqumfMw8HbcGLw7Rd-rc-i3d2_ViKE_QPH-236Sdo2KswLqCDNCjZ3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=HAdCtlPDWuHd-tPWP8IToSghphIiqfJtuSQHDhJ85kcMkijN2ehqPFHIaHt9qSu-7F4aSR5OXR1qQvYHl6VvcrybQ_2oEdNfh4z-CYV1zBEQ7KKZnCdAW_88BkWWLBPsPukL50-rQrjiRrqijzjWMYFavzcHedLpgNII7zc_JRFbtQ5EKWKyAStNeIVmSZbd1I1uJm1OXmG8QTOiZDUvsND_znE0OvWRTy5sHYHeacJ9RCfN4VW5Mxy3UUoknbK4v5JVTQ2zMMPSUxFqh3nlZQ4sdX1q7zkhqumfMw8HbcGLw7Rd-rc-i3d2_ViKE_QPH-236Sdo2KswLqCDNCjZ3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PidPtrPvBn4AXpNwnoqbHf0lsNbpbGrhyuZk84LLD2gY0ZroBEJOSQ1S3cmhskeAkZWvqD4XEk7us2FYtWyc_A_bQRLtXosTAvCr7Hi9qgQE3f6qtnc3EnF_quNTZK-rm4Dr-Z5aJCpT4qBJiPvepm7hotXfMCwrCCJ4UGbPv1gvEBv4Lx3BbvJKpf18-Bo5-h2jYAnhK_p5T0uhV9BPuW1IdgWXUEc1MRk3iSnvdsztn9hJlDK_exJYzkqvUxpzLlaPHa9rGdeRNrDtueosAQdRd3qW1JHskYixpdAgQeEKBBXZ8AXjllfzgJ8EGBEVgkLUahQiLsYm378z0B5rBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4wOvn07UkU5nHY-2cCg5ua3DVsRKQjwmnJ0NE657EvONcOcKxznqGPHqBB6G-zxjOjEvJvULga22xfVmkSskOAltzQoVs38jjfF8hmkAjYtZjEV40rdWlDcCj6T5ULnhQEJMaf5_M_u1YbrbGA6fnakWSeiswVM5O0fId44PsBRpf_m57a2woS9OJgEV2ZOXaXmSqGN0u7Jbpqp0z0gxfquvRIQGdvQiyWLBWRuo-BzU3SfVsYD6uEKntdcLGQiofBs5rGS_YQBX_NF7sSxeXizFMbQsCcJJHCfUKeNISaTrtxvZipdpGybF4Azu-iplT-nwLY4RMEWy0anFo426w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtvS1TYR6TqG25LYSzoqNZLsQRLcxCo0zaoMhy9ieZCz_gQRbKGYIwStieTMuhjpd_F0avbcfjeBsEoplSZERuuqA36xRIHX8ncpPoXI0CBRstlqjHZX5zNjX9k0q-OL_4JmthXPdVlAesmJ-AbI3qunXtga_ilL1uijgVTHLJ1kYV3NdHq4iZsN6XhURzgBoABzVnN2J_XymgQGaKeYlEtfvXjNp63FWJkBpLx7UjmHJt0cmO-4O8lOp63qyGgbUeYFElyqlhLybx2XrRb6RmhLpVbofRTUSFdxwnlpziAsGn0Q01Kb1q5cx9gP6vNlSvbjIhGlP7Y6WpK2r92S8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=a8KekPyDocL0GWhMj9zdmOCOpSIus85Ic0bRoDevMDpM1Cig752rQfv1xvlGwvOL9TVIB1gHMt1ZbMdJ8GiXzj-MlvIJ2Dh1S_MI8MGeVGY7zGKCT6OJJ9mLJRRaFJJggBSWHF8KUjyqlKZYp9VazoY2d9SeqwFGSnb-FVX1ke61Yvua5FGiYfvb4qN_j9YzzEUxb6WPwsWNC7OqwsA0KZpoM9Us7Xj5wRSExZxojHCZJqbz-vsHBF_xKmpegqH2894w014FHhVhYCngnZbPUua9ZIh6EomzWzP20JiOoaTA-R8vV8wj_8j00k9z3xvHYAcr6kuM7BR8sJtSnccldw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=a8KekPyDocL0GWhMj9zdmOCOpSIus85Ic0bRoDevMDpM1Cig752rQfv1xvlGwvOL9TVIB1gHMt1ZbMdJ8GiXzj-MlvIJ2Dh1S_MI8MGeVGY7zGKCT6OJJ9mLJRRaFJJggBSWHF8KUjyqlKZYp9VazoY2d9SeqwFGSnb-FVX1ke61Yvua5FGiYfvb4qN_j9YzzEUxb6WPwsWNC7OqwsA0KZpoM9Us7Xj5wRSExZxojHCZJqbz-vsHBF_xKmpegqH2894w014FHhVhYCngnZbPUua9ZIh6EomzWzP20JiOoaTA-R8vV8wj_8j00k9z3xvHYAcr6kuM7BR8sJtSnccldw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_7yz6S26sXSsaxptfp_UzNbyVviTXUTsLlf8-GOV60L4dWc_w5u5HgbKoZ6NOBH-jyepyrmPv2LXzDtXUUdqkmaG46JqAOkAJucExtrNzzQi_MxpNdVx3oaaNF1ONvr3jgjsfZ26IjKUXjjUmK3_ReE7vAr3z31DvHDALjgTWTJp7ZdRBYsvslRHoK5dF8RJou-r-4n_s3SXA33BB18Ghd3UFLoYWErXRo1Cag0H5iyZg8tO_GKv6rHaUbBZLaCj_qzgOrRJJ1om7qSdqRq9tsjYUtS8e9ZwrjyxEny7icgCVnR0Lz7Hdwz3SZMheQzGfZ6mtctkIsGOo5fUIH3zdds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_7yz6S26sXSsaxptfp_UzNbyVviTXUTsLlf8-GOV60L4dWc_w5u5HgbKoZ6NOBH-jyepyrmPv2LXzDtXUUdqkmaG46JqAOkAJucExtrNzzQi_MxpNdVx3oaaNF1ONvr3jgjsfZ26IjKUXjjUmK3_ReE7vAr3z31DvHDALjgTWTJp7ZdRBYsvslRHoK5dF8RJou-r-4n_s3SXA33BB18Ghd3UFLoYWErXRo1Cag0H5iyZg8tO_GKv6rHaUbBZLaCj_qzgOrRJJ1om7qSdqRq9tsjYUtS8e9ZwrjyxEny7icgCVnR0Lz7Hdwz3SZMheQzGfZ6mtctkIsGOo5fUIH3zdds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=B1FupPRqbzkZl6TZffbOT5utviRgS8uZqvKpTjXmD7wqRQ7PGrTx3NWSLNTH2yaSrLkkm0R5SY6wrgmW6pr4pXSYPDqHm60gI0seUnZRmsoEqyIPJrAR8jBa4dq4T34W7Ja53Ih3vupiMJLTCqeBEHVOkbignHDvB-c4cUbLqc3xb1aNywoe1cB1TATkHwIdG-CS-ENjljvhJcFNeJ6OWt0VuXxgR0LTqNF0bHfr4yOw-ppatW3fWnhXALw0s6MOf6BtK2mw48oBBCjuiNiBCtH9-HRQXFY39Ic7zyCRuiVUwJ46RwD5KWIa5djx1aH0oIKATJlpUlIJ451RmA-IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=B1FupPRqbzkZl6TZffbOT5utviRgS8uZqvKpTjXmD7wqRQ7PGrTx3NWSLNTH2yaSrLkkm0R5SY6wrgmW6pr4pXSYPDqHm60gI0seUnZRmsoEqyIPJrAR8jBa4dq4T34W7Ja53Ih3vupiMJLTCqeBEHVOkbignHDvB-c4cUbLqc3xb1aNywoe1cB1TATkHwIdG-CS-ENjljvhJcFNeJ6OWt0VuXxgR0LTqNF0bHfr4yOw-ppatW3fWnhXALw0s6MOf6BtK2mw48oBBCjuiNiBCtH9-HRQXFY39Ic7zyCRuiVUwJ46RwD5KWIa5djx1aH0oIKATJlpUlIJ451RmA-IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBjG9yespYOHSMII9b-C10a2VJX5eY2eDVWfhAHWabUFKedYx4osSsST6831GeEZMMAC8VtC1zPiw9EYpxxgqZMN9c_nVkl5IC6S5ny7ZkoCRMDpOE5PGNYNMOKSxsBqU28u2SZn4PiRNL0eChcOK-ZX4oGGfvncH53NwLRpbDR13ZhJ65DyWvXw7A9Yk0Wx4c7Sm1Y8GUq1ddZEuAKGS4css62t-nPLVmYpm3LWp_YzgT3FWCxqHXz4Ccphq6Qm6savCP6UkAv0I1nKpsCk1wxSF-YIQJli8ZLJly47-rO2S4CvsEECOSVoSVX34H6Sfpw5ArG9lJ1EiHYTzbFBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThJOH23udE9QheSHoal6XPR1pcHHXdrTe-xJVP-0dSdjP6dni7OoN-BZ2DMlaSaSP98lb0yVf3c33iDV_tpyqcz7EqdtXNQEWLRwofnEE3sVxWnAuIw1xRE_4TJYu1iqaptgIN7ilBKZIqRREMWEkU7GrHEd-qF5rwcZPkxL13SyQ2d6clw6hPtPxTvSMiVZ1ndNp5-wzzUSPyUS9MlG1u5cIVKHBoAve_s_JM9IYRLRFavf812WWOxVFpZ0AwPYrOQUv9fFlaeYj9O0ZGu4Te-H88grBC0n2YA5u1gqQwpYYm_f1NovBueXUmth5c2n98YZSarv5WHw5VaL7ggRZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThJOH23udE9QheSHoal6XPR1pcHHXdrTe-xJVP-0dSdjP6dni7OoN-BZ2DMlaSaSP98lb0yVf3c33iDV_tpyqcz7EqdtXNQEWLRwofnEE3sVxWnAuIw1xRE_4TJYu1iqaptgIN7ilBKZIqRREMWEkU7GrHEd-qF5rwcZPkxL13SyQ2d6clw6hPtPxTvSMiVZ1ndNp5-wzzUSPyUS9MlG1u5cIVKHBoAve_s_JM9IYRLRFavf812WWOxVFpZ0AwPYrOQUv9fFlaeYj9O0ZGu4Te-H88grBC0n2YA5u1gqQwpYYm_f1NovBueXUmth5c2n98YZSarv5WHw5VaL7ggRZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKmGSedcJ3HHwaO1dTqxatKn1vuhWVhu5lCb0A56yy_nQtLPj151_H8CRllQiAom8L-YmHFFp3FiU6Cc1c_2DKY0_LTb-xWT_IhISgC8ZoMeeKjtbQ5GvfLJtE4XZKUUxQeo6rBtS1TVDiPdDhJPPLd--V91DL2gj7XtjwYT953K8MNG6TvQlKZnBFCP9mfaDlUNxJg89X5nXoMPwobS28McDNsEly8k964gs7ftooDh7KpBUK2ijghyDSHND6Rpux6V_PtfAhXwj9OWq4QRr4GKKBgcST5KmEYVPqNWKf-OOniPkKguoyFoWgmm-Gx7LYwSXNdK2AUsOtgj0qlsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
