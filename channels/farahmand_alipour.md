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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هیئتی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU5FQmIvF1wom64UWca7ZKlfD3k7B-pAmTGzBM2FqD-QgEoBo5ERh0H97GkSRKsypX7w9_F0sUnhuzOMsK8DJk4ZwAr5FBm1qFtX03BsFGNOXC4UDRhxQPtBVbHE11Dt3Ky48awdGBbg6YEZTKjdEhbWbdVTkbRf7uoJQtIdv8W7fwwsMjyYznlf7iCsKBSK0uS-niMfX5184niHj86-1D46Oxp6IZVVOv5K5weK9gpt8lY9qzfanSg_FWebNrAFEo7M1AdMV7hbnv03J6gAUxu7Y9i_G5fBMEjy_r3KgFYLA70LN2oAhj1i7wxJ8t7hfjHRo2guYUK1T1YzJQmkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWK3YjDqeqzxH3Ej3bQHsf0aynQAz8V_pUfw0zUuRadJZ8fHzejokSynMVkLE-AaMnL4_0y4tleLP8d-c_JK9PQZdgTwluUmoLnTbeVujbMICREhNwuJe0EW6xhieWoguPycNjbh_oXT9G4VWOdbmNZtSnAMze5-MPaUX0B69KOJzRbUpLQD5TDNGrTe-6_GVYiFiLGS-zJsnEhc8Bu80R3zg2QCE1ZhK8AwassKtYwXikjVSP9UHSLFQpcAAGpvoQZLlxdpAljPRd5q-XLKEJJmM7nuL7UVF9uZKQOtlG27J4OtXW0ABRZQn3W0znzkKBdYA0R9wAXuF6hpooiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=D7zJi7ZdNc36HDDvbckPZcgQDKaeChlVtial8SDqfmCqOagVnaRTJ0CUpkv1Dye4Nwitn6u4lGeYuyTRHg4aM6FqEoCagmRa5exUDc32yyWC5m7EN2uewJ_4wqFpR9WEyGIF-v18U49Pi8tCK_C9EwSkoaTUQEJ0XhGJLEaE5tI9yLc8oW8m7wxJjYqwyBF9FIPWE3twcqneMb9KkbFZ32jAigKxMGiVopX001O80hAcyF1K3iNAC4YMo_hZCLgYCNoF686FL67Ms6WQ5DIVwYOjVwkYSFh-eEs6dfao0VrFL9Kmb1xbcStZuYw2Q1H_JBZ_ehRLgfUtDn1jRVmerg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=D7zJi7ZdNc36HDDvbckPZcgQDKaeChlVtial8SDqfmCqOagVnaRTJ0CUpkv1Dye4Nwitn6u4lGeYuyTRHg4aM6FqEoCagmRa5exUDc32yyWC5m7EN2uewJ_4wqFpR9WEyGIF-v18U49Pi8tCK_C9EwSkoaTUQEJ0XhGJLEaE5tI9yLc8oW8m7wxJjYqwyBF9FIPWE3twcqneMb9KkbFZ32jAigKxMGiVopX001O80hAcyF1K3iNAC4YMo_hZCLgYCNoF686FL67Ms6WQ5DIVwYOjVwkYSFh-eEs6dfao0VrFL9Kmb1xbcStZuYw2Q1H_JBZ_ehRLgfUtDn1jRVmerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=oiBrYpg2YYB6XWYPA3Qd4cVs11xRdoFkawqwGqQSwZkAc_--mC_iH-dTppC5PXmfJMsX2H6WXQbxf-FcAGerjlDKJm2az2CnnWb3CbWfkQNtGAn2Gad86W5vwQDtfllMxQGw9zcZe5R_PKdU_edmI32XNmvC0W4Dy8SY9EI25I4pOQGK1GmmaEGu2VdWMCDRT119_8L2JabyqJfC8VobqwB1dbyuWDEMz9In7iNGQVOTd1t40o0kWUTW1zvECb_i8t95fCjLeTEpzbaKcc2eAgKCt-4nSd7QnTdrr3Zvky9SwKUGPs9yFcCbTDWjIB1BNDUtFMsk3D_a_MDOhR_e4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=oiBrYpg2YYB6XWYPA3Qd4cVs11xRdoFkawqwGqQSwZkAc_--mC_iH-dTppC5PXmfJMsX2H6WXQbxf-FcAGerjlDKJm2az2CnnWb3CbWfkQNtGAn2Gad86W5vwQDtfllMxQGw9zcZe5R_PKdU_edmI32XNmvC0W4Dy8SY9EI25I4pOQGK1GmmaEGu2VdWMCDRT119_8L2JabyqJfC8VobqwB1dbyuWDEMz9In7iNGQVOTd1t40o0kWUTW1zvECb_i8t95fCjLeTEpzbaKcc2eAgKCt-4nSd7QnTdrr3Zvky9SwKUGPs9yFcCbTDWjIB1BNDUtFMsk3D_a_MDOhR_e4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzpaWAwmS_TxoOfxqd5PE0SjyW_zz6pFvYPpJcpNiTfq3en4h1AZFj3rKhbYtseq3xf7Xt7E8GeRh9jJn85cTeybstaI315IPmRF2RC7byGWkPUj-49l9IOw__eUfnZ2uLKAp8kXaRDU6_EYHH7Bgv-TXzWsRVPC6s81hNordeAy9uYicGfE05-TYvdqin6p495d-O4Dp8bCbV7r8yuFogn3PxteG_Zvh-qOBTz3k8W22QATECYKjWJ23y2d6zxppvFs7iSCVyBCfZ176YhpjnRAjGiW3vxvVYyVGROOVcTz6FJi55uQFswbXOYvyMIyjy3o9sV-QyMZqnECfai3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=JXpRNa6saybWa8a88X_-XJPP5rziSQHhpvaxsDJiMLlL1U_WdgmwIzBg1lexjSIvpFsT-bQqB-LeqGgh8VJ0tT8M3G9aG3b027eOfD4hJinD31gv4_dH1NSaIRYsNePO-CxDMaXy8YwwNaG2NY5fEArATDp0H4jU0Xm4frJYDLt4jOnM5rdx8f1R5oMuUaJ7MHEYJNO80laSFZLq0ONNSXvqi4wWtqYHTzealQAjXdYmW304vHfgqC0m0PXmU9e4uivOMc-jgwjNBZlJc1Y02WMUluvw6AmsreQ9SrA540gtnWNrkh6COU723_eyw66eT8xuQ9eGsmNstfaC37bkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=JXpRNa6saybWa8a88X_-XJPP5rziSQHhpvaxsDJiMLlL1U_WdgmwIzBg1lexjSIvpFsT-bQqB-LeqGgh8VJ0tT8M3G9aG3b027eOfD4hJinD31gv4_dH1NSaIRYsNePO-CxDMaXy8YwwNaG2NY5fEArATDp0H4jU0Xm4frJYDLt4jOnM5rdx8f1R5oMuUaJ7MHEYJNO80laSFZLq0ONNSXvqi4wWtqYHTzealQAjXdYmW304vHfgqC0m0PXmU9e4uivOMc-jgwjNBZlJc1Y02WMUluvw6AmsreQ9SrA540gtnWNrkh6COU723_eyw66eT8xuQ9eGsmNstfaC37bkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=MLia5WG6hl5E4ml6cQQyv8QTjk7bQEOLQ-AKz5P9T_Xo1iDkHIHoZJ75npV1Bqh4ZiyL8cSsCF5MNcWCieXSbrdelr0wdxI47pdNfkJreFLA4hQCVRohhByK9tVB4YVbCY3YIICsbdufdgrRt0BeB7sfPAUY6Bf_56zK8KbGNUU1W3HEG52eI2gLvWu8FTkAcFSc-FrgMXaUMJ_4msMCxAcS8um9GBCVqdR_ZJVM53Dg01q54qlItEgHncLUUKizDmWp_EpXG9c2RAkjejmZaPYqucGMgP5Jzf3_NPdlAbOFRlGoXPXKw53h-pFh31KcwzsZJlNmIZykf0FkN7OLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=MLia5WG6hl5E4ml6cQQyv8QTjk7bQEOLQ-AKz5P9T_Xo1iDkHIHoZJ75npV1Bqh4ZiyL8cSsCF5MNcWCieXSbrdelr0wdxI47pdNfkJreFLA4hQCVRohhByK9tVB4YVbCY3YIICsbdufdgrRt0BeB7sfPAUY6Bf_56zK8KbGNUU1W3HEG52eI2gLvWu8FTkAcFSc-FrgMXaUMJ_4msMCxAcS8um9GBCVqdR_ZJVM53Dg01q54qlItEgHncLUUKizDmWp_EpXG9c2RAkjejmZaPYqucGMgP5Jzf3_NPdlAbOFRlGoXPXKw53h-pFh31KcwzsZJlNmIZykf0FkN7OLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyuLD1rrPJgZ6Cq7n7iTSivzzPYVlWX5QDDhmXD8W8kM1dZY75A1qR9SA2yX42x7P-DgCCd6cHWkFa-Vdfzaa6Ff_3DC0Lsgx5BrpIeZTyQgLt_NNGHdsBLTrHoMMAeFCqQCX2WvDwf9Nbzk21ioqkdE2ggDDnjGpY1McI8aBcREOTGPWJSGZrLMP6sYbiHa03PJ-ia_AeB5NHbJRFa1lKLWHIastO9S5imAvVu2781TL2gzwnp3mTIlWdIdEi5zdaN2kxuU7nnE1onCgEqqThUFtEOaInifpnhcCb7SPlEyG7Sa83T25dIW4BT580fs1R_XeOuNme1U4w2jsVaNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APRMUIkKy1vswYLGwplURlyYoiBzd83BmnLwtOYECk205D7UM4oqRIA-GPGZrcawmu_VS37LnasWpKxXPxUmDIEHIv2nW91IP4LOMPrdox48GPerRcpQZ9UB1RJU56H77ovzAYr75_2TccBmk6B50dlUoEuuebGszucB9EP3dEvxoG9BaKqhhhaoL29NyDCCT_DNrcW2Je6R1Xxn500PIccpHQUrZgK3xEjN0SLQWJTdZF_OHGhmGoM-l6arHsyqmDmskH6zU70WRyLdCv17dnHTFALTsDq9Z08kdV7ysgzDp2hNeSDWIVKPnbplxx31fbfRfO7UQAaxUiar0bhUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3j7LGV0-2LzKdCKbE1N0maapBkrgglSMj4dLYYQtZzWPfDt1EIBwDSHZJeDFlJSAl2grCrH3PdIBfhFZdZPn5fnBWqQ8Y6KqlNLfIHBKu2wCtQSfTpd4LZZOwc9AntFWTOHA1B32pzKHj0dF_owxHUg0rEkLgIVC3QFl7OZExxjDzZaSq0INmBDgSTJx-tAFE0QK3mWs1eAnS2oDACWc4fT-TNVnThSsgnjSIGrwSs8NCdnsYpVshiePl2KN-8MBb7CyyvRrFaM-AiazrM5-6RGVSPXRrumEjScmZHeY7QATDgc40QMDPPlFUWQNojNIdrLEBmmQLQErltOuNKYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3GsbYM5Q_z5_FobMUTzbbDiCct9WBkwECy-wFF6IMfnbZYntLCUeE8ZBLjq1Vd-KbtpfV_Nm_iIX9D5YQT4RHHsMuYy8kp-xnetEdyS7B73-_1PLPkTms0OhJVD_829yLTEc6UtN8whCAgPLH2g56Q8tolu_C06VBBJg4JwTgmNJxINX2s51LdnSwOrbenSvfcA-F0DDfz8L5zrnafafVLofm9bCZpOlgkwKFCgRoBR1M7brgs8FsadFPZnvvwPMtEoiRw1gjgl_gz3l3POz-IAbbQfCcUXMDrNfsHYl1Y4UzNqqnwa7jzCi6mYZfYV568NfRtA8Q11xHf46NmK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqhnnjnHlxJCKzyWrJvGoKWx4BRRMORes60QV_edUYaiD0ghx0SVvRB5Th_QcW6mS491ZmAYg_trLgqwtwX98TKbilyimnDe1ez2Exk4VeD8WaOSNnEwUsRy6uA6i99DY4E4ekbkxwYM2-swU5ThBeC5S83d1HNzOYE9QYeTP3j3pnszKdYMPZlbx1A4T3EqiwElbNG1-EuWYOSiJ4HMIEJ3pt_C4esaI2_X98b83-KUMPd8HM0xn2Oipn_8a5BQlLKR64K3vszCrj76pp9AuJa8SLVUcHMlxdC3Whepor_TD86z6DokKv9pkh03pR8UcneUy3GP7PxMkQ_tTqBOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdnZdsQw9wv7s7cGtgJkSoN1gTIDW6Zulb2mu9hLbXjcjIxYANz7XtdOl0kb5cgyUw2onStemj00dWQCQZh0Czc5592rvWRZrNYAwOsyUDnVE5_UsajMg3CQYQ_5hAn2Ap8AFanl0Bv9QmaCgu50qToyVgzgPyxxCCsIIJbDfik-U5t3k4SjJM1-cOZTyGpZMXblA82B5O6txjiX9eNyUXkoWmMbtpKljpppZzNq9TPOuykovbwlBak3y52gvmHK20yabX1Ogb4yucSIGZSzXfAaAxkFnwAH4B3rO2T4RzuKcbCB4R_iKdCmvSCC_yzW2as9HCCItdYiPt2etuPd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YK9DtV0_mQoGeDTm6FkvnK5X27Es1WTHum6kEHKEZEajuLuETtcumAhyJ8KsTugJKUk44VIH5vxiI35RcMoslHedEBddJUJ-SLHlvRAMZQ2NFvAgULjsg4thYYapvdl406zmc_HMeJdiuFUhiCJN04qfbgN6lbUcQt0L2Bx8Hir9yymRwOU-YdxIP6fpShZ1eg4tInamOhYozKzqKE74_R7jBoO9UMJcWamtEXTBgjQD9LIDG48b3h6KFRg_uKZl70dqCEzN-vcFb9PcsmU4PDkk3QZW8ZpUhvCmnWNDiQVp81DcSuQ-Jd1P0qRU7YRd-ILX2yOjGGS_kSnZgSUmfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqcnC1AF3aJnQOgGxJ-4a-jVlka3anEX6qZiaAL5pCgM-ETcn0hzv4Kw6lXW1q2jCgr20KI5-70EfIq4atLOKHytW3WCp0A46FNsfuV6Y6Yk-ks5Q9GKPgUZbpKzU8dBd04_yUtS3ky_BTlXAaMlqP3x2lXvwhUT7xnuYAFROLn1h5SxptBfuVWnZRAbjSfpt2oqiwbja9B8dcZyprxl4bhdsKnxqaLjMgOFIl5ABr4RJIo4vuIe9sUgDWlEqO8i2DFVzuOMBNUlYjtxlMYXeg4VFFFFUN-nGXEYTeEGppvLmzpGxWcNjcpLtgdSyCPjQhb8pdqIShpSEU4SRAOz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmSmrfS7mV1iKxxVNZWf5hXzXvAasqoz0XjgnJzJ4ntsBG3qEdn1xbTj_1wR_T7Pb3zbMAKgSCi0XLMNSA5uwqPfc4Rzte44CLDYgPEtdCJ-U5VMhuFu8SWagfKA82TjZktr0nCaptec3r7TC836CSjL4EXFJhbaCbJGpC-SlJ2H0An3ICpr5vvclnDKNdloJS553FWWrYiwDxdNE6lAm3HkhVVUu-JcQiaP6l9Wte9qloHoPu6kjyhslGb9MVlGhOgJCQmbQ3Mpgh0GZqKkTQGqYbmnYlTLZPI1_Q2nYBuk6dkWvdu96jAb82HlfhkFt_ZIBfa3QJk76HbFAT1OSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohT8V0iMlQM874M7HSuXvRx6SgsRxZ3cizOxK-RhgihokFdz5IUdygpPArUUlKQC6FTxXYjHA6XNTQxDlk1S7qU1jVXOz6-o-UVKu309c7WbtVzaxA-7rEJZpMPFl15DvDZ16lYfcgfYWhr7Khg2W1d0jTacaCeJV7HcRPlfVk5kBbwT2Zk3fRC6y-YQ3u04ICEmnFK_SOuqa3-ZjxLkB5iAfv-W73ChSPsmZxxae5YBSMSYXKjUYxbVrnVEdsXvL1kK1H3vT6NE7wWi2myXSbRXyEXwyLVuZS8w1SjyATQ4Y49NCzsVsGMlp4H1F2-d9SC178Jn6qakV9y9pElT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgcZzUSRWjq04G8VkptLaekwD_h14gblY-AVueDmD9p6p1orHew4eZ-h7l_n5eBkH6tHdK--R755kx9HNn_5MRZ8ZNFTNdkt0k9bpjbHfU8xPjWe08ZWNToyMvnAZ8tS_rGEtADG5kN_96aiSUERUKWIyXfHPdBvoXEkpcrgVN5De8OgsAvBO52WxAJRqidVIAyrlTSi-M40PY74-41IZLAfmL5kASAvHjbhZoiZHL8g3o-exJBLn-zTGMsKHhPoSCviwxAIXY1fdZgkt1ZU7O7G2ps_fvsJO1uHoAo_6f_G2YUJMHmEKFdVzUpKDM27JZGQMTy5X47eCF3CUKc4sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=L6RC7bd3XaS6K1gQt9kzFZeoXBg2pZFteoR1vrRXSlnXAITAWmYxxcRap6ehcMIAWRVW84hRH4rOCHnPuMX_A8mB6L-NRMd38YtCI_P8h2gWYouCx6G9B66ixr1OtENQmS5gG7bWUpJCQPSpNbeOlT1VRf11QgzK2xqvkW9bkqrghoWQF7RxpKVEqHxrhk73brIbDgmW2o6vZJ-KFMeKloe2Xiqgj_YjuWJPvlFYphArheMZvtWRkQBhGQd_M48e1iBdAMOjPjUeDfQc9ArKLChaYddFA8HOKZl4YX-VZntlD5360HSKrP-fVB_py92dKd8SLvA7mwU8BmF-6ULUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=L6RC7bd3XaS6K1gQt9kzFZeoXBg2pZFteoR1vrRXSlnXAITAWmYxxcRap6ehcMIAWRVW84hRH4rOCHnPuMX_A8mB6L-NRMd38YtCI_P8h2gWYouCx6G9B66ixr1OtENQmS5gG7bWUpJCQPSpNbeOlT1VRf11QgzK2xqvkW9bkqrghoWQF7RxpKVEqHxrhk73brIbDgmW2o6vZJ-KFMeKloe2Xiqgj_YjuWJPvlFYphArheMZvtWRkQBhGQd_M48e1iBdAMOjPjUeDfQc9ArKLChaYddFA8HOKZl4YX-VZntlD5360HSKrP-fVB_py92dKd8SLvA7mwU8BmF-6ULUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nACUgImuKtgZVOldkeAwYYRgHAvXtB7xxM9Y0q9t6imD7CDfAraACnDbOVevN-Wul6eahhY0UkfZVW9r207dfUt_Q7JCPc8_q1cf_4jcQlWb2B8oDf1Z2e6Pq2mRUOu4-cdRMRZlXW80DW8Of6ih1wXkwqG6xOY0XsdKUW8fDg5zZEFMEy4T5KXj9BWoMlMIOKiK6FyjRkah_iD068xIuQuJO2WvadZt-4FMBh4HnkQ8hZp8cfAuKmYZjoRp-aIe_wN8IgttBIZ81_Sgca9trcDYGAgfUusa6qpAF6ekRxV7XAbHqQW-NCcit8ET0FhXpiEpGWKRghaSF464cY-rcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nACUgImuKtgZVOldkeAwYYRgHAvXtB7xxM9Y0q9t6imD7CDfAraACnDbOVevN-Wul6eahhY0UkfZVW9r207dfUt_Q7JCPc8_q1cf_4jcQlWb2B8oDf1Z2e6Pq2mRUOu4-cdRMRZlXW80DW8Of6ih1wXkwqG6xOY0XsdKUW8fDg5zZEFMEy4T5KXj9BWoMlMIOKiK6FyjRkah_iD068xIuQuJO2WvadZt-4FMBh4HnkQ8hZp8cfAuKmYZjoRp-aIe_wN8IgttBIZ81_Sgca9trcDYGAgfUusa6qpAF6ekRxV7XAbHqQW-NCcit8ET0FhXpiEpGWKRghaSF464cY-rcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=BgHnXVFjIr7K136HLSlxJK76e-mE5BC3VjtVylwmtW4EEMdOwJlWhNPsGnk9zGyXoio7K4uxV_p4f1una1sCwbaofbwflcrk_MlcyYG4Q7rGD-sT8WY--sGy5tYhe7SUmnganY3e92BFRGnTk3fzNQrrbHzTuuA5zRWSflahzujBAbmDNGJkhRu3LYCLyV2rTWZwe7oZYGrN5NOt15Kgv8qQ1RRO6qNGgtTBJ7rrkxC3j_-CoPUGIytqOgjVnQTkBf3F5ngiSWI0gTjcHE6GQBbN_viQlmfe2gUqWjOa6jXftp3IR_y4HtLn5twvjDfnthmTx2ZpbjliGJsVFkG-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=BgHnXVFjIr7K136HLSlxJK76e-mE5BC3VjtVylwmtW4EEMdOwJlWhNPsGnk9zGyXoio7K4uxV_p4f1una1sCwbaofbwflcrk_MlcyYG4Q7rGD-sT8WY--sGy5tYhe7SUmnganY3e92BFRGnTk3fzNQrrbHzTuuA5zRWSflahzujBAbmDNGJkhRu3LYCLyV2rTWZwe7oZYGrN5NOt15Kgv8qQ1RRO6qNGgtTBJ7rrkxC3j_-CoPUGIytqOgjVnQTkBf3F5ngiSWI0gTjcHE6GQBbN_viQlmfe2gUqWjOa6jXftp3IR_y4HtLn5twvjDfnthmTx2ZpbjliGJsVFkG-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=tksRGBOmbdnhQLvzBMKxoFmKenLMKPCM9zex7apDAckrE46XUhSEWRKSQcNi-Dn7va1vYAQDFNmVngO41jYItjG1wVJjidQftlmDq4cxWIobZHtHjvcTA3vfB_mNgTUCOaQpfOdUfbrOn9g-bp9cbJG6N_08lPIiGsnYW3k_nu7q_4FSWlaYXFMfimY1ISCqrxaACBvy1aCTOBP23ZuWsS7CfJn1rXDv604EWcVohVVsLJB5rUNonsFtyunk73zpxnU4DLM4vdFE9x3RLIPbVQ7_kbUXSvFM3selZDo0thjZu2H9Ge12htJ67s4A-d6TyWYb102NqaJJF9CA7OsUWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=tksRGBOmbdnhQLvzBMKxoFmKenLMKPCM9zex7apDAckrE46XUhSEWRKSQcNi-Dn7va1vYAQDFNmVngO41jYItjG1wVJjidQftlmDq4cxWIobZHtHjvcTA3vfB_mNgTUCOaQpfOdUfbrOn9g-bp9cbJG6N_08lPIiGsnYW3k_nu7q_4FSWlaYXFMfimY1ISCqrxaACBvy1aCTOBP23ZuWsS7CfJn1rXDv604EWcVohVVsLJB5rUNonsFtyunk73zpxnU4DLM4vdFE9x3RLIPbVQ7_kbUXSvFM3selZDo0thjZu2H9Ge12htJ67s4A-d6TyWYb102NqaJJF9CA7OsUWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oo2fXxYfdzF-jgIglC6DN5Sd8rm72YG30Caz-C-PKV7LS9ZjWwDXq8Z9VxKsnU9ZvXrfpM3EF3x3SgcycOXIhDuKXvbX4np8-yVrZs7qj6Nkir2EQ5vWpYhQuPZ3slp89uqQwxXvVQAEpxpofh7EFTBwLzSQWkmq97gEb4Fr_MYG_K98YF3O4h9bpMTczZzJ4l31euToqE5yjvBmlZ7rpQArlZGH2fc_BCOc8zkOw28MyaiZCVMvh3-BpfBmNwpXXXIhWW3Uv9WQ28W3dYsl4UeBsg5HpWGhVNbc9BerhKpvHUlBGZ7Dx1RY7gho838Kp97KUZHVuBT6cmiV76b6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oo2fXxYfdzF-jgIglC6DN5Sd8rm72YG30Caz-C-PKV7LS9ZjWwDXq8Z9VxKsnU9ZvXrfpM3EF3x3SgcycOXIhDuKXvbX4np8-yVrZs7qj6Nkir2EQ5vWpYhQuPZ3slp89uqQwxXvVQAEpxpofh7EFTBwLzSQWkmq97gEb4Fr_MYG_K98YF3O4h9bpMTczZzJ4l31euToqE5yjvBmlZ7rpQArlZGH2fc_BCOc8zkOw28MyaiZCVMvh3-BpfBmNwpXXXIhWW3Uv9WQ28W3dYsl4UeBsg5HpWGhVNbc9BerhKpvHUlBGZ7Dx1RY7gho838Kp97KUZHVuBT6cmiV76b6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=jXN_9jqCahyJtXtmouludlcOg1muOsr6KPKCFHE_WW07TdDJBPK4pzSMPOK-nIDeEnFMNsmuuXG4VN8SpPkppwRyPSSV-KNBJN9e0PxqbcAQ0EPdCnsFRjOQJCbWnMT3evk02CSoNigfBxhlNUPre4fNKx7gk2vGTYdgq20RX39TTYxOvjltX1jKLZJ5QZ-OeRhFTOf2l6o5AM8G2Zk5fks9WWJcBGNWd1842CS3ZzwzwMw40G25zz6fhcQ403kCKL08kr-KR5Xh9U5a-VIFr2sG0KFzI_nsbFrvxOYzloghFBjc-N5DMTbeJvwQLjZkR2SK5kJXsCjWtORFTyURRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=jXN_9jqCahyJtXtmouludlcOg1muOsr6KPKCFHE_WW07TdDJBPK4pzSMPOK-nIDeEnFMNsmuuXG4VN8SpPkppwRyPSSV-KNBJN9e0PxqbcAQ0EPdCnsFRjOQJCbWnMT3evk02CSoNigfBxhlNUPre4fNKx7gk2vGTYdgq20RX39TTYxOvjltX1jKLZJ5QZ-OeRhFTOf2l6o5AM8G2Zk5fks9WWJcBGNWd1842CS3ZzwzwMw40G25zz6fhcQ403kCKL08kr-KR5Xh9U5a-VIFr2sG0KFzI_nsbFrvxOYzloghFBjc-N5DMTbeJvwQLjZkR2SK5kJXsCjWtORFTyURRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=q2PC8CJ5GAb37qX2nDZVKMY7-iyEgSgTTjwkrNMd--YF6A4gjf33A9t_e-9L6i0sjJANVIU8ugrSsLvJNy_BgA4LoZTBc__alF7nspocycfMrxY2F2HqUc_SRyXo7qrNl_KO2QVR8mNlHZPfi4Z9U4Ocjil79tFjIIm1oZxBkBCSCsBB5RcBqdTQPZMfxiMLyGj_keFlPzG6e5PD8NcX-pMYPqhFTwkxFCiC5CqPe6gwCJdadF9B9h2uezOHDX7bcIS8saOEaJfkvRiojuSFpqQN_1sb5ieNCjICJ7fYeHg-sIBKeeAk3Wv-iATQBeZEilwie7shu3IoWhkVM5KOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=q2PC8CJ5GAb37qX2nDZVKMY7-iyEgSgTTjwkrNMd--YF6A4gjf33A9t_e-9L6i0sjJANVIU8ugrSsLvJNy_BgA4LoZTBc__alF7nspocycfMrxY2F2HqUc_SRyXo7qrNl_KO2QVR8mNlHZPfi4Z9U4Ocjil79tFjIIm1oZxBkBCSCsBB5RcBqdTQPZMfxiMLyGj_keFlPzG6e5PD8NcX-pMYPqhFTwkxFCiC5CqPe6gwCJdadF9B9h2uezOHDX7bcIS8saOEaJfkvRiojuSFpqQN_1sb5ieNCjICJ7fYeHg-sIBKeeAk3Wv-iATQBeZEilwie7shu3IoWhkVM5KOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1c9s1c-I3GtwXTCn-hmyBO3-Xgsz9FBr3lm4_72XFu_3AMSE3NUA5wM6DbL-qLkhOXfQXXvZFp_qcgY3S0HuJ2dM_19eTZ1dm38vOVyhwyZBX7fK7nWzYJIi_4iyVIhYxuPmfa_C1do-7HeRJKyhi-oFCEKfKZR3pIXsgb9vnPKvtVptE8NL-IMbmXXpai8x3djKtknN02Xd0yncWKwmBgvHtnUsLXxTzVJoy5WrM2yyRvujIxK4bOuTMnCT83WaJF14MfpdRp4uyhlMbvk91lgqHDiC5xOC1axmPsLbTXfPiW8fwJwQ9h2be_NA9HOnZzM3E0uFExzuu30QCOQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=TnUqblpOpXxdstpxEJdmD-cEuUOaUufIg-IH-sQxWFAjwty2l3g2fOOFfs5Zu115I7EIzYsPPaKaSk5xnkhBE-Vt3UfWVaieIh7uB9YlvvR9Fv7Uwa0Z3eEyj1tqss7wyjOHwIcXkAxuWrytUP5or31ROUDTqqNyitKXM-cwFInPoNGA84hXiLGhgPvJ7_OfYmi9ZvLjvoxzm8f36yIHoM4fSCqv_2IYEuqpwy3aqLiYmwmurBP7B4yNyeGkOGhq9mu6b4I3n7DiZgA46TGZwzL4jxu2F2RDLRpCNp_l5cNFi6pmZm4A6n0v8IQQ7Feew-a8wzYTVIYdbLDD1CCDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=TnUqblpOpXxdstpxEJdmD-cEuUOaUufIg-IH-sQxWFAjwty2l3g2fOOFfs5Zu115I7EIzYsPPaKaSk5xnkhBE-Vt3UfWVaieIh7uB9YlvvR9Fv7Uwa0Z3eEyj1tqss7wyjOHwIcXkAxuWrytUP5or31ROUDTqqNyitKXM-cwFInPoNGA84hXiLGhgPvJ7_OfYmi9ZvLjvoxzm8f36yIHoM4fSCqv_2IYEuqpwy3aqLiYmwmurBP7B4yNyeGkOGhq9mu6b4I3n7DiZgA46TGZwzL4jxu2F2RDLRpCNp_l5cNFi6pmZm4A6n0v8IQQ7Feew-a8wzYTVIYdbLDD1CCDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=pbwyE9VXOJtOXOkszBOzdWW4jd3uu-rQRcUULSHZo3Aa1z_xiiWjAVLp37fexWHDuF2lL441ZenoSqp0m-CCYIgKaAnLjB0JxceNGBR37746JJWUuuvwY4F3jK95sfNpNJBhWlhQwBhEYPwqFajR0pvAd0myIZp_0lJxqb7eXbBwzppND-go-xjBRqbOCTdSrfdlqYP3Wo32Ux7s1s1Or41Ol1D5gq0yAdzl0ROOVi_zB7xdJM77zherQY8WFMcCJg_rRv9SwAYx9xRLP1SDnr_b9aGZrBca0uZD51THHcN_U0GaTUMS9_s4HfaXvrG32izmLxGev9w7FpIxKIFRZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=pbwyE9VXOJtOXOkszBOzdWW4jd3uu-rQRcUULSHZo3Aa1z_xiiWjAVLp37fexWHDuF2lL441ZenoSqp0m-CCYIgKaAnLjB0JxceNGBR37746JJWUuuvwY4F3jK95sfNpNJBhWlhQwBhEYPwqFajR0pvAd0myIZp_0lJxqb7eXbBwzppND-go-xjBRqbOCTdSrfdlqYP3Wo32Ux7s1s1Or41Ol1D5gq0yAdzl0ROOVi_zB7xdJM77zherQY8WFMcCJg_rRv9SwAYx9xRLP1SDnr_b9aGZrBca0uZD51THHcN_U0GaTUMS9_s4HfaXvrG32izmLxGev9w7FpIxKIFRZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=OXYjE61YOyDV7yqx9nGiWyLtF7Bbg-DSAVA3QRmhNh-GE6kmhC7mrlH_mcjQWKj-Zy-xUxNKIAfn1stWC852fCFlK1oLrIqgArbTcHRMX0YcuT7ztIbyZeFkpWbvaRRf9WKv8u6ckj0Z6Dy5_99mBRxtRBoEUR1Z7GgAzXsf_K2Es7zDIL8RFrvlgMSDOj_TPjlnDKGmreOpv5PH4ljtpmE37He_eU0UWfY_sxr4VglHTVfgmIWBV9T63NGHQeJKVjHsz5hkt9YhIV50tKlYh-4igU0HdwTDwOnMZnjc3pcVXFRreCSw_rYKcPg4ZP19r4CULWOZF_rA7ZB3rpm8vSg_UlXUyrQ65UM0Z4u07xKZIvVrmvk2TX8Klmnl7jiau9PA449A1ZhnRo9BCeYc7nxncsauf1ro8ViuU9EMYoJImOr1m3hpmAEMrOwLqO3xTVqu4xGmDSvuw5mSRPyFnFXXR7ppjsfNjvI046MbR0OEpbXTrylSl8SI4mder68g9UKp5DhUYv6ZEm0spJy2zZuPI5GnMBdufkeGyb3m3MWlWDbWVMljJJZ9zseLdiFL9HQ9VuWaiM46AmBhGYf_sEW5EEB9KmDWwAgKtWvr-ooGDMrEdHYE_NmKYYgyUkkfGyncCJWV1ZCM9OWveuMcS5ZCT2KJTtFC3ILGxeERVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=OXYjE61YOyDV7yqx9nGiWyLtF7Bbg-DSAVA3QRmhNh-GE6kmhC7mrlH_mcjQWKj-Zy-xUxNKIAfn1stWC852fCFlK1oLrIqgArbTcHRMX0YcuT7ztIbyZeFkpWbvaRRf9WKv8u6ckj0Z6Dy5_99mBRxtRBoEUR1Z7GgAzXsf_K2Es7zDIL8RFrvlgMSDOj_TPjlnDKGmreOpv5PH4ljtpmE37He_eU0UWfY_sxr4VglHTVfgmIWBV9T63NGHQeJKVjHsz5hkt9YhIV50tKlYh-4igU0HdwTDwOnMZnjc3pcVXFRreCSw_rYKcPg4ZP19r4CULWOZF_rA7ZB3rpm8vSg_UlXUyrQ65UM0Z4u07xKZIvVrmvk2TX8Klmnl7jiau9PA449A1ZhnRo9BCeYc7nxncsauf1ro8ViuU9EMYoJImOr1m3hpmAEMrOwLqO3xTVqu4xGmDSvuw5mSRPyFnFXXR7ppjsfNjvI046MbR0OEpbXTrylSl8SI4mder68g9UKp5DhUYv6ZEm0spJy2zZuPI5GnMBdufkeGyb3m3MWlWDbWVMljJJZ9zseLdiFL9HQ9VuWaiM46AmBhGYf_sEW5EEB9KmDWwAgKtWvr-ooGDMrEdHYE_NmKYYgyUkkfGyncCJWV1ZCM9OWveuMcS5ZCT2KJTtFC3ILGxeERVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Bz5V5O5PA72XCVJI_NX2CmkMhHqjU8PK1bCu3OcdW8FKHA4L-SXHwbh3c7QPQI4bABdJ_7rfiZ9WMstZ5hlrujD1g-M86CU8QKKgMVxLpea_om5fmadhbOWNu6IqoU7j1yMnw5ZH5GwusLrI6cfvpms4-309Cradpsr3pEwkE18Q6bqjW_By13NLJjlLztFkqTf_rAE3gW6bMZj1c322KpF5pW68TGchWFXy0PY4p3cIO7t5t672fxBRiQ_SuMN7uKPMsPxR9l52KG6iFBpzsfVA56vM4vAp2Nyij5mkFcunPiHZRIdE1ow5W4kLB5XZzWafPIVwG9vxNp5lDfsFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Bz5V5O5PA72XCVJI_NX2CmkMhHqjU8PK1bCu3OcdW8FKHA4L-SXHwbh3c7QPQI4bABdJ_7rfiZ9WMstZ5hlrujD1g-M86CU8QKKgMVxLpea_om5fmadhbOWNu6IqoU7j1yMnw5ZH5GwusLrI6cfvpms4-309Cradpsr3pEwkE18Q6bqjW_By13NLJjlLztFkqTf_rAE3gW6bMZj1c322KpF5pW68TGchWFXy0PY4p3cIO7t5t672fxBRiQ_SuMN7uKPMsPxR9l52KG6iFBpzsfVA56vM4vAp2Nyij5mkFcunPiHZRIdE1ow5W4kLB5XZzWafPIVwG9vxNp5lDfsFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=kxNlkzL6y8_cPitBu_TY2BTPU2PYIJGlLoDpntaoVfBe5PYQg-MV9VRzcMIV1QdSN-a87aLhMqHwaDYkpQbDRPB0RwGefeUdIQGvMsXgZPu0ATAR8iJjaaUGhHOhBy7xwugxQ4MX0TjXcPQnS2AsAKyhUTtH8-TDEK9ru6Tg93WP5VMahzlmahnLNX2BhJTgbURh2qptq7HdAloglWytNrroYSJ9LK5yTGndD3shZZeByO8htUxg7R1IF7iBey1T9TtHiDoZ_ewp5p2ro6DgssbJOb3n4j1qI0OMN0VkuABRiNuQW25BJ0FYwuk3haMOXsmt3-GfsCNBTSFstYE4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=kxNlkzL6y8_cPitBu_TY2BTPU2PYIJGlLoDpntaoVfBe5PYQg-MV9VRzcMIV1QdSN-a87aLhMqHwaDYkpQbDRPB0RwGefeUdIQGvMsXgZPu0ATAR8iJjaaUGhHOhBy7xwugxQ4MX0TjXcPQnS2AsAKyhUTtH8-TDEK9ru6Tg93WP5VMahzlmahnLNX2BhJTgbURh2qptq7HdAloglWytNrroYSJ9LK5yTGndD3shZZeByO8htUxg7R1IF7iBey1T9TtHiDoZ_ewp5p2ro6DgssbJOb3n4j1qI0OMN0VkuABRiNuQW25BJ0FYwuk3haMOXsmt3-GfsCNBTSFstYE4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNdUXEopzJOYvrRl8zKdDOMu13KGR4E5LMfsC1SAEFJoEDNiO4iv089M5HDWSqSLb7gZpw05UGhU4lQfg6e9b_tvtnTkEzeAv8MndAj0yCAsQ0VJXn1E2QzIgQ7nBA1DDHpqkMHkJqhMEK2hnARO9qXDuPK5pM2gMKc6yTw2m0hE35Odn1l_M1Tl-BJvOlpW4KTwFdto2UE9o4BKFBacZrjjT5ihtp3nb_WfoJivorQV6B-M_DpQv0_jnO-dVfrm_LIZGQiTaMmU_H1DVpBS1J9ksmaVe-vaG2zvmjnGWNIcHHLtJNikQWvsHkkY5a8uRbThAsIMNDuBCo3G_dQkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHWTBwT9oAvMsOz3JMARa_qi7HEs1Q_g_WpIaeIbOyhJ0dj2qr9uWFW2shReuTyaG5BRiPyubPV_AiQ-QgTl7rQ_H_5uYPcOrqx481O_WhdVHdyfQS4QyKqJWOh9YCZcUGKQJX-QCqjpyTnKvG7tbv7nkWCimfxcU7NlhIGxhVlkmnIhQ-Q_zddRkXA2X97iv7923wLBSfS3Gg4fdSQn0pcFQ23v8mUHMN-OaGuVz3tGppQS6_eEHZqlaAuM0TgS7bzib7-6whsPJzT6rVGbOoooCT-K9_gTV09iORleerFbx56Kb5tcxtoZXutRn1Ncb0zMAOBd_RdbqWD9qbLp3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=T3xvEIDsWy-0MXTBfnCnJ4PzfSmczOGTKkdjV2-GH_cGXZ_eVGn69d0rbalwTN-0UVaHcRqkuQ7ePJbtR_-fwys8kk3kqwYUDT6fqsrn5W_vJq1E5mk8hzj0YbIjla2lT4FsRsuvWQKX7fgpiabnbxEnYS-zftJ2UyV7skvJpqWl4bZG9x41JlB5Jhyjs0Bmw-3KW217c9u7JPpOt_tcJwng1TdZprfzeeiIL8VFb5vw8vKC5j322LS0tGWtmvv-ifXatYSTV3e2G7OmH0v2ngetdQ7LEgPBtsW-hQnh1Fm2SjzAZxLtPPgx2b_H05e-zDQS_owEcSXDLjzs9O1S7kdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=T3xvEIDsWy-0MXTBfnCnJ4PzfSmczOGTKkdjV2-GH_cGXZ_eVGn69d0rbalwTN-0UVaHcRqkuQ7ePJbtR_-fwys8kk3kqwYUDT6fqsrn5W_vJq1E5mk8hzj0YbIjla2lT4FsRsuvWQKX7fgpiabnbxEnYS-zftJ2UyV7skvJpqWl4bZG9x41JlB5Jhyjs0Bmw-3KW217c9u7JPpOt_tcJwng1TdZprfzeeiIL8VFb5vw8vKC5j322LS0tGWtmvv-ifXatYSTV3e2G7OmH0v2ngetdQ7LEgPBtsW-hQnh1Fm2SjzAZxLtPPgx2b_H05e-zDQS_owEcSXDLjzs9O1S7kdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjvENq0d2JGC4UMSBtcKEFXOY9PQzM1Vg2iPtwYQ-x6YCq1scy2NuWqfiGDk_B-jdX7yPD6JRedZd4cCftTcOqGSXU4RdVoJo5Ba7RidCULcc-KOiLQBT6q3t-fOllkWGUaDwMGBmrWpl_WqKZxovuANVsv4EeM0dW4M7ZyNNTR0OO8FWT8Jq5xfBw5jXiasL9_6zHDVnn-gCzbUmhr-8nf8ANwEITSJG0Yg7kMNfEGeD-5FYjjcH78ptqekxX2MxBkO557Y_Iq0IqBFIKXOyyRLv7DLABDWfxXLcU3wf5KpBt1xf9jLQNjiy6Ls84kgskuN_YYC4R_5zyALUWYKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8cLxa0xhVnlHNRjMWZBRQt8VKECypizLSE9jcb5HlMU-2rUy_oLFCC1WuEE6K8ku6zzHl5CyjL1dc91sLipt2hPCJPShkKHyH-R0xEGvXnUdQx1lfawMouJD-O5BI5PvnDtF3W6Rs8wQcCIhNDDrNqfuQWXZWmh4D3uzHjy8Isao7b1G-Xy6gHz7zdXHHXRovGDVlVPKbsZxrU7s9TjCKltI9NN2pqiLcaHpiAHfEStpb7cFVpV01AxEZK2ALQQv0GyT-foEPPCSDM7IYRx6wg6Y-WwG64LPw12qAjzyU7n6L3s1_rc2a6e9hMDRUomCy6KD9RCa16ivxtfnOM_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNNKiFEEXAFUYBor7IIgoI7gXDS7fwZp_xKoJhsA1Uqt9yCB6xj-z99tYZBCop00mD-fJ5HT5-wuKnuyEY25YGWwMXVmAJm_e1NxgQqANBpuapOmSBSEdHuXyIFX3mLoCAyvolp9Vzp74JfQtsYPeFblE0-S1Uyl9qFaw6V5JMQHiYSuqNpjladj-dz_bC863VutT56oTWJf1v0QkjMvw7uiz7Y9Tjzar6rM_AbdGk5ZCC8yqHplrrgxBt-wr_fXABuZgq6EuGTCWuv-GW1WJxWFgMCDBVQNn4YWZKmWyidx20DSPoNPKHeu1KpjmSU3hgEnJKzJexai4zxixrEeAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBeMK8ahPKBosgey2BJ_2-5ZJ-a2TtEZ6RQ97f92z7R9k2ZGHdDHCf_ZXgTnu9sSkP1_IEkvfIjrDyX3XFCs2gl7iqn4iZxMO9I-ThrBuqy1Pqp5Lg8ZPXRxJynY13gExXWNnwI2TnfrP7VaAfDDMvOBAKqV-YZO5siowEoAK5LEqNHpC2Xb7HOiW_GpLIVOXNHEBPuQVHyztcjxTM2t-FBZgS-zJ40QYay5EUpWwU51tYlTrVR0hZoNzKjzD8X31XKnVLT1B9PQZNk_VMoWMdB2fpcZdpGfQVHGWgLkTUAdPe46US1E68qOZNUNYUevjrRVwsADxkF9hkdxqD-pFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rd0vck7Zj7QK8a4twJUIMslw5nJf2_WuzCVGbp9xF0K8vXnHDjObJWeSlrvVv24W7k98p75hWmgNb0Yd-Y3pTbp6ikjTSQVfd5i8Jwv1-WNNDBH5jMqdjCNnOTV0lqLwc8lrzSdKBT4gXhPIqpaIFFxWtKcI6Vaxeg5FrIU_hpJVFMFRcWJZaYSXN87eJwY8Uwr0all8X_9_xbFInYmbuWJoYc_gk9ny0E3OxkH4fThP9mVA_LQPFjuu9uIXdBPD-ZPECdNiPMfcISwHA5v88E6Qq86hxQnZcDlUlylDOHKz7OTVQiAgcWA2Rxh_MI1eTuUceHXvraKGfQqUfbKhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rd0vck7Zj7QK8a4twJUIMslw5nJf2_WuzCVGbp9xF0K8vXnHDjObJWeSlrvVv24W7k98p75hWmgNb0Yd-Y3pTbp6ikjTSQVfd5i8Jwv1-WNNDBH5jMqdjCNnOTV0lqLwc8lrzSdKBT4gXhPIqpaIFFxWtKcI6Vaxeg5FrIU_hpJVFMFRcWJZaYSXN87eJwY8Uwr0all8X_9_xbFInYmbuWJoYc_gk9ny0E3OxkH4fThP9mVA_LQPFjuu9uIXdBPD-ZPECdNiPMfcISwHA5v88E6Qq86hxQnZcDlUlylDOHKz7OTVQiAgcWA2Rxh_MI1eTuUceHXvraKGfQqUfbKhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SRo635-UetlO6SLVRv3i_LQ_dNaED46qMtqjZVK1at0-YdHLzRIHlezsZba5SgqrzWapMFZNALVMfMhAtq1PRBl-ybpzaTRnYNXuje0Zo4a2oNE-fEzsT47wuC7CjMO2JlH4iBvZ6SOUZvgslzBHwslIJ_5_CbvVIZDuLbtohWRooiXiO5VskF3-FsO7suoUqs8tUIBOzmiK2hECAdQaOOCIkw3GnZQazKxvns9_DcfNVtHCY4GDR4F6UPDZEwoWbKwZkJAq9GsfKtbCB3fsuxXS13XnveZmLY3hDic_vqxmaOm-Jo6tIitLxJIPRqV_PKtjjcTLVag9pHKj2sjZ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SRo635-UetlO6SLVRv3i_LQ_dNaED46qMtqjZVK1at0-YdHLzRIHlezsZba5SgqrzWapMFZNALVMfMhAtq1PRBl-ybpzaTRnYNXuje0Zo4a2oNE-fEzsT47wuC7CjMO2JlH4iBvZ6SOUZvgslzBHwslIJ_5_CbvVIZDuLbtohWRooiXiO5VskF3-FsO7suoUqs8tUIBOzmiK2hECAdQaOOCIkw3GnZQazKxvns9_DcfNVtHCY4GDR4F6UPDZEwoWbKwZkJAq9GsfKtbCB3fsuxXS13XnveZmLY3hDic_vqxmaOm-Jo6tIitLxJIPRqV_PKtjjcTLVag9pHKj2sjZ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLXx3OaVqsjnRrAUKLtVLiwul_CziO1HylutWNJuhCTqBr4KE6u2ne1WvS4Uu13OlXBztFJDLo4JzAHqZfTICZ-xpk70aPKR2M-Y1MgMNLMvaSu36_ZRcwVF9PoY3s_wY6JTdGsdtNhEOYurQZeTd48nSALRIMmLxolCJ2r9uOcEGQsFZWGDjEXxeaGPnd0gJ-99JCi9KTyRlsZbWHsL5scme0tjkN_Qy1S2luHcIJWF-qWZ-hn859eBkxo93lzoBTqOQgSlUmzvVspJnjlnJ0FhR2SYT9G1ejIQcVCuwJ-2xbPu7n7YWFm3rQ7bbktChbRMej3c5GplbR5F0CeDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Hup824pTK8FVUl1xn4rQfdMN-eyUlqkDNcuU3dtD_rYbNkWu-ORqHNM099Fxo0TfsgnvH0aAnrXgIcYH4dM0e9v4IOSXe7f_Pg78o1ORE7BAubDLQDxvnbTykVITt7WGE_2VtbE99jTArAN7w6cEM8y8cb4PWPI1Y2oHKWfuHE9Q9W18TdxaIe1XzElypr74s7GHKhxHSE6rmo2bCah1zG0hnyU_K-H6YAtGix9Cr_pNO4lQuu9bgDI31eFlNLKB1VWkf7IQJThLkuMgp7ghjY9aQhJiu5DpVNIS3ERReOK6Mq2ZK299ETbW1TEfFpf6nx49OS177MPoi4SOj6yi9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Hup824pTK8FVUl1xn4rQfdMN-eyUlqkDNcuU3dtD_rYbNkWu-ORqHNM099Fxo0TfsgnvH0aAnrXgIcYH4dM0e9v4IOSXe7f_Pg78o1ORE7BAubDLQDxvnbTykVITt7WGE_2VtbE99jTArAN7w6cEM8y8cb4PWPI1Y2oHKWfuHE9Q9W18TdxaIe1XzElypr74s7GHKhxHSE6rmo2bCah1zG0hnyU_K-H6YAtGix9Cr_pNO4lQuu9bgDI31eFlNLKB1VWkf7IQJThLkuMgp7ghjY9aQhJiu5DpVNIS3ERReOK6Mq2ZK299ETbW1TEfFpf6nx49OS177MPoi4SOj6yi9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fOcvQ0-_eG_eh8tBs2jbYeVO6PmIV9EuYY0np5Bpqys-qcjZKcWt4QXvLXgY42TSbAEWVH17xQMktHN8K0hAxHHaVRu_ngL9AmtxjxKapSak1jZdaiKUd28BZhdmEa1nb_z7YlzvJB8bJPyEopcRCwRUfIDrlx2o8508Jt3m9xRf9CzU4SUUYTH7wYgBsatfSmFa-I-Ds7ViiV8wwwvXemmCOQp4W0XOzfzZZaLzvtqBu1tUr2hgXFLYj0H79e1SVwatanJkM7Q2ywkCbsgnxWJynQaIZ2COtWcl7vP9VdG19K-9_m5DC0Sv_-f5skkaXk54SDrKlf_Mxx0UStqrBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fOcvQ0-_eG_eh8tBs2jbYeVO6PmIV9EuYY0np5Bpqys-qcjZKcWt4QXvLXgY42TSbAEWVH17xQMktHN8K0hAxHHaVRu_ngL9AmtxjxKapSak1jZdaiKUd28BZhdmEa1nb_z7YlzvJB8bJPyEopcRCwRUfIDrlx2o8508Jt3m9xRf9CzU4SUUYTH7wYgBsatfSmFa-I-Ds7ViiV8wwwvXemmCOQp4W0XOzfzZZaLzvtqBu1tUr2hgXFLYj0H79e1SVwatanJkM7Q2ywkCbsgnxWJynQaIZ2COtWcl7vP9VdG19K-9_m5DC0Sv_-f5skkaXk54SDrKlf_Mxx0UStqrBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=BcWOeHG-t5jvkfu2z2lgg2JrpEupFAWoOJptyhxA4sKd8_90u5MDI3_BdQRw1_q1mn-ebl6d0uWQa6cpSvx9Guho83eyqUiACiXk_2ms9E6Q31hwBi5DBVcYBlnuvL6B_6qVFx53wskBA8Sj5naAlT458A7RimaGKsHM-23JHqqqtkEHF5UzYWap8nrbnSD1O6BvjAP0_PcN7Ird7QrCtIiMr-hfHQk54-JC1MsDADLVeSP_7pavaUkZItEIik9uXdmLZ_Ut4pursRxhP09AJtIHopCsQwE2g4rHNARMt0FLJw_Byre_YSQYVIqolMPJ7AhedtG1p69MjVJrvk705A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=BcWOeHG-t5jvkfu2z2lgg2JrpEupFAWoOJptyhxA4sKd8_90u5MDI3_BdQRw1_q1mn-ebl6d0uWQa6cpSvx9Guho83eyqUiACiXk_2ms9E6Q31hwBi5DBVcYBlnuvL6B_6qVFx53wskBA8Sj5naAlT458A7RimaGKsHM-23JHqqqtkEHF5UzYWap8nrbnSD1O6BvjAP0_PcN7Ird7QrCtIiMr-hfHQk54-JC1MsDADLVeSP_7pavaUkZItEIik9uXdmLZ_Ut4pursRxhP09AJtIHopCsQwE2g4rHNARMt0FLJw_Byre_YSQYVIqolMPJ7AhedtG1p69MjVJrvk705A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=kzWZrJCF0I2yIDB6z2WawdI1o-GRjvaHHFi6D3h_RYkXtN0QJ_F9scOfAwItvfcM-7zkVsD1A0qdlsCRb6SG7BzwSUCSMBFAAx6YQ8riNW-kdMvcBjFvmXUxlgaKqGRXiuw5qMBkLFTLzjzfiV3frmloYAQVyvuTQvtsQNWWzVoWaaQeV5b83ysFgIdjgbetfDpBmhrMgKtFl6VWnsCtih-VJCivLquZ43XmBoJzctbEEcfgzc1Fub93jhmoVJDg66oLqFELbxZahKDl5JwV7-mVv1oVACybTR3UuahGvJkSl_c8ftc7IaOXj9KpSKLgHry_x3Amtr0p0BPufUBgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=kzWZrJCF0I2yIDB6z2WawdI1o-GRjvaHHFi6D3h_RYkXtN0QJ_F9scOfAwItvfcM-7zkVsD1A0qdlsCRb6SG7BzwSUCSMBFAAx6YQ8riNW-kdMvcBjFvmXUxlgaKqGRXiuw5qMBkLFTLzjzfiV3frmloYAQVyvuTQvtsQNWWzVoWaaQeV5b83ysFgIdjgbetfDpBmhrMgKtFl6VWnsCtih-VJCivLquZ43XmBoJzctbEEcfgzc1Fub93jhmoVJDg66oLqFELbxZahKDl5JwV7-mVv1oVACybTR3UuahGvJkSl_c8ftc7IaOXj9KpSKLgHry_x3Amtr0p0BPufUBgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4XeMgDXHtEIyac-ClTBIqQMcHz4AR5dH2bZL16TRqiRzbtqZO8b8D5wiWYW-1oyE1RruoQCHwhM8VPd-OVpUYwRQEf9mFNv2bbkvtaVvWbFWUeB2EjJRL1kzdL4lKVTm-7wxs8_3ti-m9FYQPkiVXNMp7HFzJg5BjnrxeZIGTwDYZHhOlYNPowZb7SK3kksVVjcLzRaHlGY-b0ncWW7wzO8T-w9UidD9xTFuqJ-o4lJCp6gzBCLmZQ2VVUzjQjR7v9F-0ojUGa-rSRmLwNc-PfQkvcxZsen-KFqPKed3fcaYcfRrHEcjcrDPCcOt0aVPYZqPeq2N990VsJtBIBqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxXsvnL3hrEAj-NsCF6SkL0fAKWa3b0ICYG9f9jZws1CVrjse4fnxNmpAwvx6eMajYdrN6wkFjyOttLM3rmGwx-NF2j7RKMQHw2CM7U726v1ghHsiwtGMgIc8BXMaxCKnY0u3x6Gh0_EGm_eRP8zDPjCfc1unehHFVSV78ewTN9xwJ-tgsVu-W0gVXJztpM0CuA8KFihucfUgeqNfUUSvtzA2YURTcnVXZ3GTSCOmcPKkrLxvdaLv1Usc51pH4m6xfaM--SssFlkm32kWwMvnFLEa5-wJeREwtZRYyWs6893paDQjEo73yyZ9oBcJiWhVO8zTCNlBF8QgHT13p-ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=IhDquVTA91tj1vjTkGpCm46r7TuMf3jZzVNaLHE5uaH3g7Yvdo6ufDbtQxu0Acb8KhluO1oIoUWgymZYrpMuIDA-EZaS_EVM8Ttjdnm-Z1SV6neYIrhaWQjMa6gXiQgOUseyNA_KfXDYcdMAMWUH7LG_Ur03JShsAoO38inrqto9S_m8rjle10Zwu3LhoTCjg8L_W-MNssPBRZW_AHdM_v2X8A8Kky64CH92mxbbrOLa12BifqZZzpW99X8jHMmNs-eNs-iCaxCAqtJFLw1pjJbKyMr0BDJdFhTjtJyWHTRtM3S_q7pLVVlsUTojhwXf8qR-SelhMvTqTjN3lbWiag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=IhDquVTA91tj1vjTkGpCm46r7TuMf3jZzVNaLHE5uaH3g7Yvdo6ufDbtQxu0Acb8KhluO1oIoUWgymZYrpMuIDA-EZaS_EVM8Ttjdnm-Z1SV6neYIrhaWQjMa6gXiQgOUseyNA_KfXDYcdMAMWUH7LG_Ur03JShsAoO38inrqto9S_m8rjle10Zwu3LhoTCjg8L_W-MNssPBRZW_AHdM_v2X8A8Kky64CH92mxbbrOLa12BifqZZzpW99X8jHMmNs-eNs-iCaxCAqtJFLw1pjJbKyMr0BDJdFhTjtJyWHTRtM3S_q7pLVVlsUTojhwXf8qR-SelhMvTqTjN3lbWiag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9SSPzh0Gr-684imj-nZCT-hweMa7cc_9FyqzmDfrLD4ERfba6F_z3EvPBAiW7Vlu3tMhzldcP1bj1TtgkecSxmNvBquorScaAhkLR4lkNDnszFD5sbtLWohJdqrS6VNcZpIZWW1o_PhRUdiBJvYhWZea4FSCELpH5dikZfRG5lOpu1wRmp5z90M9KM3QH3R_APoyIDvlI-d1eWUF5ttb6BesqQ8hJYd4_-i9sDqUrUs634Dyaf_y9M2D9Q7FsVkV-2BSihTXAvRY5_-CuQaa3Cfh9QqjrR4K4YEwWW2IFKuf3iEnnvZaDzKZz4DmQDTSwCE73yvIc_-cMt4RY6DaZrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9SSPzh0Gr-684imj-nZCT-hweMa7cc_9FyqzmDfrLD4ERfba6F_z3EvPBAiW7Vlu3tMhzldcP1bj1TtgkecSxmNvBquorScaAhkLR4lkNDnszFD5sbtLWohJdqrS6VNcZpIZWW1o_PhRUdiBJvYhWZea4FSCELpH5dikZfRG5lOpu1wRmp5z90M9KM3QH3R_APoyIDvlI-d1eWUF5ttb6BesqQ8hJYd4_-i9sDqUrUs634Dyaf_y9M2D9Q7FsVkV-2BSihTXAvRY5_-CuQaa3Cfh9QqjrR4K4YEwWW2IFKuf3iEnnvZaDzKZz4DmQDTSwCE73yvIc_-cMt4RY6DaZrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=YXDq3vZypo3sOTpZxfRepQSyDMsnkHffnhBc0OZokziC5hGomkOqJM-t7QyqB4Q-tR2mPSe6hdkGyuPFAI0LZkfKrSHRKb5vLWpZlS2LCQvfX9o_KBz0Q21dkrElttG6RebIegs9o_3qh_krpMa-ZplUbgieORaQuPuJ5_aIssyHnyKFzpRWfa6nnQEC80HaqkhY9ohqUki3frspcn6JLN13VF6UUUa62UKqG2K_KzEkLJpU0C8IK6mphoFztQ7-ZYnBmR8EsOoRL9x2x8uJH9g2tpAdMUFpNsTVZEkqOi7VSlPuUQA2v6jPr6fI1g-4c6KMbF6ldd9JEynPTbU8VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=YXDq3vZypo3sOTpZxfRepQSyDMsnkHffnhBc0OZokziC5hGomkOqJM-t7QyqB4Q-tR2mPSe6hdkGyuPFAI0LZkfKrSHRKb5vLWpZlS2LCQvfX9o_KBz0Q21dkrElttG6RebIegs9o_3qh_krpMa-ZplUbgieORaQuPuJ5_aIssyHnyKFzpRWfa6nnQEC80HaqkhY9ohqUki3frspcn6JLN13VF6UUUa62UKqG2K_KzEkLJpU0C8IK6mphoFztQ7-ZYnBmR8EsOoRL9x2x8uJH9g2tpAdMUFpNsTVZEkqOi7VSlPuUQA2v6jPr6fI1g-4c6KMbF6ldd9JEynPTbU8VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM_1zWb06TuEeHOf3fyw8Vl53KzQwdNwSUlbAZh6UWybXiUkUIGfIRhKHKa7MAdKpFwHyBp_gmcdv5GmmKniJLLmrF-0yjxW_a_jWGxoJuR0NIloD_p6xCXAILS0ozCAAgmAcVIx-AH20-yq3d8DG20B-hz4-ob7yNy-nCpfTBSvgOBxRCpydiwyd-xF_itJ0A4oNyeiw6irUcieZ5-q23pEwQ1XhY8iQ21_vZd8MTKiqgh2Z6vLLNdim5B8P3Agnix_BHlPyuqqMQGo-88XnGC3MtOYFiWunNL2Tuib7hPX13E7GbYJXq6v09ezMWEbl8w01YNMhsXNsbHqxeVkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=oEEt_esTHImnvMuQUUxuh-HnUnfBjecDyofsPZ3ViL6PWIP5By2fYu4K6q5Fp-MKnj9WbYFPGTlyq5l6vJ_6yNvRiryTJ7XSL3qpsjAAO2d-CpqK5mrMzOUWjcZg21baXwEfRTjr-h1d2d2cKEGas3w3n1ZWOhDRq5SZ8rjqZtH8RQxZxB9Z9jveDbbOOkNFumVbqCMR5EWMeC7IsIPKyeYyAGUkQaans8kCzFR0DvvSikr2Y8NNZqm0eJEtLHW7JvuEZoSbs-lZDHJMc633TsGa3gVLXACNDHbBTFTEuljLm3NTdXfPkAhmdr-FsHtqBnpieubD7Z_Ptg9QED2E3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=oEEt_esTHImnvMuQUUxuh-HnUnfBjecDyofsPZ3ViL6PWIP5By2fYu4K6q5Fp-MKnj9WbYFPGTlyq5l6vJ_6yNvRiryTJ7XSL3qpsjAAO2d-CpqK5mrMzOUWjcZg21baXwEfRTjr-h1d2d2cKEGas3w3n1ZWOhDRq5SZ8rjqZtH8RQxZxB9Z9jveDbbOOkNFumVbqCMR5EWMeC7IsIPKyeYyAGUkQaans8kCzFR0DvvSikr2Y8NNZqm0eJEtLHW7JvuEZoSbs-lZDHJMc633TsGa3gVLXACNDHbBTFTEuljLm3NTdXfPkAhmdr-FsHtqBnpieubD7Z_Ptg9QED2E3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=av_FYCrs9bE0v49TZ4yRZDq8dwl3YQBCklSJ2FP0eYNrgtwluD5Ijpvg5yxYpbyihhZ2-8wSiRQOVfPRHaLSPLcsAEieDI1z2qteS46aEpB0NmQHIt9uFYRZRpbaRmiL1cXlzC595vW3qammr4UdsipxZzn9oFGaeOXxXj3MhEAOA2RhUWljG7I-WHiBzonXh8wX4RYVR6LLfac5Z2df44yo0l_rjqZ_nWtidfRoypSelVC_2YMLkW8-Xle24R9x2wf6kqS1xFLBe9-vVR05JQPnVYdGqnsnkC_VZLMUhfNhGx2EO6s4i8vnxKy1W4GOO_YkpZvaip-7qjMD2AydxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=av_FYCrs9bE0v49TZ4yRZDq8dwl3YQBCklSJ2FP0eYNrgtwluD5Ijpvg5yxYpbyihhZ2-8wSiRQOVfPRHaLSPLcsAEieDI1z2qteS46aEpB0NmQHIt9uFYRZRpbaRmiL1cXlzC595vW3qammr4UdsipxZzn9oFGaeOXxXj3MhEAOA2RhUWljG7I-WHiBzonXh8wX4RYVR6LLfac5Z2df44yo0l_rjqZ_nWtidfRoypSelVC_2YMLkW8-Xle24R9x2wf6kqS1xFLBe9-vVR05JQPnVYdGqnsnkC_VZLMUhfNhGx2EO6s4i8vnxKy1W4GOO_YkpZvaip-7qjMD2AydxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=C7bbs4bVxLyZadkPGkiODyPYnXd17BcUIWrOiN9dfHCHFu427yfLe7Uuyo3YcGnKv-T2fIK_tAXqRCHug7gpum-VSdeR7w-zEHcOgc9Z8l37NQ94VAv7gbmilF_AQVVDTAOSQA2VBr7sQA69mjVdjukk0YfIIU7IUoTXnliXmkhQ8oNhaDrWeQ6crj6sidtycu8ZKob0uIgLABR0it4s78fZEAcn_o6w8kJYJTgtn7ZdYjYjhBMfs4pqQOu7TsODQ4c02wkar5ZzCUMKd3iY-NdpdaTxSog8AQ2MrKq-C-NiuZ99bEGUfaWeDYgwg0yCh4DiDsUXCnbNl7YnyYkKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=C7bbs4bVxLyZadkPGkiODyPYnXd17BcUIWrOiN9dfHCHFu427yfLe7Uuyo3YcGnKv-T2fIK_tAXqRCHug7gpum-VSdeR7w-zEHcOgc9Z8l37NQ94VAv7gbmilF_AQVVDTAOSQA2VBr7sQA69mjVdjukk0YfIIU7IUoTXnliXmkhQ8oNhaDrWeQ6crj6sidtycu8ZKob0uIgLABR0it4s78fZEAcn_o6w8kJYJTgtn7ZdYjYjhBMfs4pqQOu7TsODQ4c02wkar5ZzCUMKd3iY-NdpdaTxSog8AQ2MrKq-C-NiuZ99bEGUfaWeDYgwg0yCh4DiDsUXCnbNl7YnyYkKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=FFvQTcGXwwQLILn5cjXff0DRxws_UoR6DoxFOv3LoXVTPWFoXHUAVA0mcxV0ypv0pYhXR4_VfwkxgS7HMGXfSS4cJNFgkOf55sEksvcGb2yz5TsGVPhN_N6Vzu9EZ4EsPpTmh_gobiZHEpWy1xgXDPKMS1kGsLpVqAUgaEBuM7ccB5KXTCskVLkmoAiAGUHJbMzbYgwN_4a4zOSQV1RVoXNNUx9mQiOrdLpCUM0hmp1bd0Efd8WPBkEiAmv_1V38T0hJ1XgTRZbgn4nIf33NNo14AMHnypRKgXqMAKGVZxXqfi_rAx7uftfnknPKLmoAF7LJetNibbZAD0dTGoX_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=FFvQTcGXwwQLILn5cjXff0DRxws_UoR6DoxFOv3LoXVTPWFoXHUAVA0mcxV0ypv0pYhXR4_VfwkxgS7HMGXfSS4cJNFgkOf55sEksvcGb2yz5TsGVPhN_N6Vzu9EZ4EsPpTmh_gobiZHEpWy1xgXDPKMS1kGsLpVqAUgaEBuM7ccB5KXTCskVLkmoAiAGUHJbMzbYgwN_4a4zOSQV1RVoXNNUx9mQiOrdLpCUM0hmp1bd0Efd8WPBkEiAmv_1V38T0hJ1XgTRZbgn4nIf33NNo14AMHnypRKgXqMAKGVZxXqfi_rAx7uftfnknPKLmoAF7LJetNibbZAD0dTGoX_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed4EMSYY6jugqlCtAXcRApigb1Mn9Y2S1fE8MNgLfutJFKejOmSG-vZkeE8KhDdDT2ohRTIuXPGU8od8NC3yKMOlwEJNtuhsxRSGkNAs31ENr5t1EVIsivui2HMIbSbPObfjGo_3UHMC82lY0Lh-KIOcUcolm__3vnCOVnIHWbl1tb7WU1ouS3rHuadU8x-cFuqNIskMXcd3I5q454s2CRLbsP0SmdLsNNMc9qabfRp7IB67aEqyT0Ky1PoTRBtIgKnyFzRDbbsj4TrBDE-kGf-GjS8VZoq7TF8do57u0DkBFmvcNjdnIxMrMW851qj9YDrqBUMSjkt2_Mt-BYE7nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=mQ-F3evDF_3YEbwUshGhyxn29k-rvLL1QYdtEjBamge6C3w1mam_-HLnCw4hNuAaUgWVqkgqbqkHoldcQsOcQeAf6mycVaA2W8s3a7nltS1q_eAfrgpH05utHDK70CDG6aMd9lhRcC-TLanR9kBJjk5_67FXtkQNbmQ8P-Z7o7Qap1dyrPEoy9jZWqu_0W2sjovHKShtC0mIqVJVXXdlu4zST9pFZgCOwAPybPKfQDP6nGukbjfhpsKn67bJbpXaexmx_6cAfBJFleq-xJjs1HXj6tu14Xf_qPnlaom_s28GWiVC2pFbVksJiBRB8mTcmz8s0ueF4uJWrTx2rVNSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=mQ-F3evDF_3YEbwUshGhyxn29k-rvLL1QYdtEjBamge6C3w1mam_-HLnCw4hNuAaUgWVqkgqbqkHoldcQsOcQeAf6mycVaA2W8s3a7nltS1q_eAfrgpH05utHDK70CDG6aMd9lhRcC-TLanR9kBJjk5_67FXtkQNbmQ8P-Z7o7Qap1dyrPEoy9jZWqu_0W2sjovHKShtC0mIqVJVXXdlu4zST9pFZgCOwAPybPKfQDP6nGukbjfhpsKn67bJbpXaexmx_6cAfBJFleq-xJjs1HXj6tu14Xf_qPnlaom_s28GWiVC2pFbVksJiBRB8mTcmz8s0ueF4uJWrTx2rVNSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ha7tpkAAPSKFmZgcWB0GG9qGZJYVNEwYxSq6XwM-VPHZIPgNKWQUDnWP-0e0O8zy5tqCo_DZ2ZdvXG5JD8S2diHvCgMgcUfQASzR2xK0AOO6JuYJuJTGE_-IBiTi9pDkg3XAlpgOm2XBooU72yQ5WAHOmYVeINkaaC5Uq6l0J-LWI_5Po_oRzCsz-a6FeuQp2VsfLVwrjHtqV0IxnVJpWn8KA95zun-dQOBmYIJiYvDmtKFvYpe_S79WrpwoO2UTBqPQ2wTWSmjMOfmj2Kgsn1-thPw_0NLSTubitUuENzWBTF3ox41G8A7G5jh72ozUacCWmKvT6uWqUEL1NGFJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ha7tpkAAPSKFmZgcWB0GG9qGZJYVNEwYxSq6XwM-VPHZIPgNKWQUDnWP-0e0O8zy5tqCo_DZ2ZdvXG5JD8S2diHvCgMgcUfQASzR2xK0AOO6JuYJuJTGE_-IBiTi9pDkg3XAlpgOm2XBooU72yQ5WAHOmYVeINkaaC5Uq6l0J-LWI_5Po_oRzCsz-a6FeuQp2VsfLVwrjHtqV0IxnVJpWn8KA95zun-dQOBmYIJiYvDmtKFvYpe_S79WrpwoO2UTBqPQ2wTWSmjMOfmj2Kgsn1-thPw_0NLSTubitUuENzWBTF3ox41G8A7G5jh72ozUacCWmKvT6uWqUEL1NGFJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp2_Urp2vvMYddyHZy9Uu29g_dta364GsP531SKcnyHT0XvdXFJaOp1gJgLlWOkATEECzy4kaghITmFFadYpgfcAWqB0eGHRtZtAjC6QKJaSoQlEcobhOlToCmaCkZcSnwRBOVsI_zPrC4JIuOuOH186P5Bq4aY4x9jQPvG-Pns17iKEkSeo60JVqiZJVKWIfC3PJbVv3INLEZe4j0npQ2NRrbXSGLkCDnX7RhSEElA-KaUcfuQPy-78ChIxLo5CLLj5fdcKDtnjjvSXlweKt2kF7FfFPvt9AfpqFgQMQPwdUA0NGJ38zUV_3EOGaoWcONPDRvUtrJ6IZG_oz8F5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=KW2KKNFraLVh-5baoehK2vR6Wdikc69ruI8W9iZxqeinkbn1IAZKU_zFQi3flDEZOJtVxhTebiNcBq0WkHXTtPBGfDfbPddVFeUeFyI_cHS7vctCPUEhSunbldZBiGnBPuZPNwu5Lg7691SKUGEA_vi-oUBlLTVDUWn74sc9TQy9KNwVOJp3QmjaTcFoJuuBgi5OypZrxZEqxaMDW3795rAtP5QU-hcAYI2mmg5dTKFXwnluY4ADluaomVOTmFMdMIeFdraSqsbJDh8f2d2ckq43LMleo59RZYpYiRwq242uFlcK8rbK2GEmJCQfNkx2HbtOUKgMD74CUsCs_rVxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=KW2KKNFraLVh-5baoehK2vR6Wdikc69ruI8W9iZxqeinkbn1IAZKU_zFQi3flDEZOJtVxhTebiNcBq0WkHXTtPBGfDfbPddVFeUeFyI_cHS7vctCPUEhSunbldZBiGnBPuZPNwu5Lg7691SKUGEA_vi-oUBlLTVDUWn74sc9TQy9KNwVOJp3QmjaTcFoJuuBgi5OypZrxZEqxaMDW3795rAtP5QU-hcAYI2mmg5dTKFXwnluY4ADluaomVOTmFMdMIeFdraSqsbJDh8f2d2ckq43LMleo59RZYpYiRwq242uFlcK8rbK2GEmJCQfNkx2HbtOUKgMD74CUsCs_rVxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=dw3kpior4nVcCREaCsliutqXZRZTqF1gyIxaMTk8wlKnQuQTsbD9Gbvb2PzImA4QxX7j7dMAy-e6GviijQBxPYOu72DFXjWmduWOiUv-fIfNwElEP2KYKlcUeulcUK2_WwI_YHU0C6Jwwcla15JImkQ2npHK600K9F9Y3iJz8GO0y1eBrfsJb5gEjBb6f8gHLvz9NgcpXXQg8kaorGbdJv5p_W1SHG-Wwjy5_ysG_gu2iaBOPlZ-PxhLTyK5EHhvQC2G_a5YMMclJbPmBpDw-mvEdhECQ8Z6UfJCzre1NdTi98LhxPGvcgD4jwJvPW3MPZmaMF5kEQaKXLUg10CfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=dw3kpior4nVcCREaCsliutqXZRZTqF1gyIxaMTk8wlKnQuQTsbD9Gbvb2PzImA4QxX7j7dMAy-e6GviijQBxPYOu72DFXjWmduWOiUv-fIfNwElEP2KYKlcUeulcUK2_WwI_YHU0C6Jwwcla15JImkQ2npHK600K9F9Y3iJz8GO0y1eBrfsJb5gEjBb6f8gHLvz9NgcpXXQg8kaorGbdJv5p_W1SHG-Wwjy5_ysG_gu2iaBOPlZ-PxhLTyK5EHhvQC2G_a5YMMclJbPmBpDw-mvEdhECQ8Z6UfJCzre1NdTi98LhxPGvcgD4jwJvPW3MPZmaMF5kEQaKXLUg10CfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=B8m0hVoAAokpF3LFik8nR8J_gZ0xB6YzJXBpEDt6684FnRbXlbDeDQuTGJ2G5UNDy61vJUDZu9WHqezX8UfaiZqsG6ZgA8b5pGzjMZZi2SqsBZYdZxg8nJwCdGlMhrJkBt5N9Dbq1m2mS4fVtg4Yo0nCOsciswqePw2rBigG54a-OztBwxfWcxBGSnJiB95Tv4N6Hzouo8zdo2YPUJDAl5HAum0Q6k9QYIjTycYLls5JDHsmy1RwAHFcVjNJ05mQB8Jnyc8kLtw36kH9lQiRdm-NxaRNapOPtNRx-6vC5Q7kp1LQpl2--LK5f-kKCuvnYbZkTRwnueEzcP7Bvk8KLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=B8m0hVoAAokpF3LFik8nR8J_gZ0xB6YzJXBpEDt6684FnRbXlbDeDQuTGJ2G5UNDy61vJUDZu9WHqezX8UfaiZqsG6ZgA8b5pGzjMZZi2SqsBZYdZxg8nJwCdGlMhrJkBt5N9Dbq1m2mS4fVtg4Yo0nCOsciswqePw2rBigG54a-OztBwxfWcxBGSnJiB95Tv4N6Hzouo8zdo2YPUJDAl5HAum0Q6k9QYIjTycYLls5JDHsmy1RwAHFcVjNJ05mQB8Jnyc8kLtw36kH9lQiRdm-NxaRNapOPtNRx-6vC5Q7kp1LQpl2--LK5f-kKCuvnYbZkTRwnueEzcP7Bvk8KLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTM7-VannDVLDbhT-cHp4Ae8D9z9dFRXVZXoeoxpB7KvbnG45WUpXpR9bErXrPpjDW3Vvax-ABXbX2Rl2oZCA9-wityw_HaMdHCngi9E92IAsezu6oPjpVnC28Q3UdMitqhAvouJE1AdyVmjeKrmIFmUKvvWkOk14m4kfSegfLVHJGiYIJ7N8JJlkFM40q3gtrHv5D1AwxBCzhQAI6FbiDk2c5wB2SspoheDdOg3YGoh4dhA_nypdB30kEa-9I9ncIH7aRMJs90X5msKGtldZrSxDkysttZr8503CiJNT3ODYylVKYb7nh8-UEHJR8Lv0cmY9FsBpQuw_shPAnc0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR3imCqtPN9PtF_qvHm8ZVbLzTowmbKk24LS_n9ZbjPtX51Qyd3CPwE5FN55E40JdxRV1-lDer1M-CoUlthXn9LUyk9Fzyf26YvmEbVihlnodfsr46ez5WeQnHtHBUTvp_EYLsPtW1hlr0h0YMvwB089cX7pktN6CPMS1Ti223m6vtDJBk3Eff8ioQuB1jweo1hw0V5BYEW3IbblQzN3oWBU25vwpzdIrNylPio3zJJ1tHZdJ3sRGG4U_Y2_LV4A4hN0cMm-O1vNi5C6rA5EXNq1_-GatX5BEoJlLBQb7kjlxZYz19DanlRTNEEJwkgAiD7B0JcdVcjP4pddrfNAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3nRMc0tPGPiFWn4_6uRUhfokFyT8AkWMdijFXqyWJsbjAVTXbav7s4EH46ddFXkQTgm6B8Ar4RNVi6ssL5bb8s9vIABjtrYSTBLl6KdAA5AegjLMqB2-u3j7ow8g6b6-mZto1j9uU4hlWkImGqXIk2wRqJcw3Qm1dZdzqtQ5nVcNqPw7jscn-B1IO6ruNS58Zyy1LKzgC0Z2UGcBFAdbsgTW1b9Fx1akzinmbJK_2qNDXFcumUAwi3ncdH3APJs26piS4CB0Jrd1Iy7KY7uzaFVor-BGNyEKUElWroeEmigvZvaPEsI8aIoxBIy-fBGeoRWt9s411ar4bxoRMDLcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=BDNNDyYv0va-GXauI4soO1d9lvXRDonpWZBTDZrWm2d0ZqfRlafMQ6e83TpbJgnohD2EFu8iqI5CFazV55LTc6e9GV8X65xxPH49ajxPlUXuvwRcfQ32m6veygtOX1K2BZ_DDBd3vNEe7hgxWNA8ipu1YmazQzLj1RtUlDTcOn_2sfIyEHFOScVjyEWGohaFOfus8Sc5LJbxETELl6n5BOuCY1-EYRBBsb_jUxGcoXKHQaR5BxwhfK1pGaWmvk0MkLWbeLldfq8bt7J1jCeVdINXDsI8vk2Y9Oxh5lsb-_s3Y11Ts0MjLL0SRWs38ABb274G3OPIb3RFCNRxVIXulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=BDNNDyYv0va-GXauI4soO1d9lvXRDonpWZBTDZrWm2d0ZqfRlafMQ6e83TpbJgnohD2EFu8iqI5CFazV55LTc6e9GV8X65xxPH49ajxPlUXuvwRcfQ32m6veygtOX1K2BZ_DDBd3vNEe7hgxWNA8ipu1YmazQzLj1RtUlDTcOn_2sfIyEHFOScVjyEWGohaFOfus8Sc5LJbxETELl6n5BOuCY1-EYRBBsb_jUxGcoXKHQaR5BxwhfK1pGaWmvk0MkLWbeLldfq8bt7J1jCeVdINXDsI8vk2Y9Oxh5lsb-_s3Y11Ts0MjLL0SRWs38ABb274G3OPIb3RFCNRxVIXulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yl3n0isDeXxNUDy8q4SwVreOuyOeDFaOba06XTU-aaPVvSpmDTqHFGm9atexXODbBKq-cfxFCzkFOhjm_fkZB81GAEeMITiODuOVlHZSceCf_2G-sE65uq2kVH-iNnWK1xXNkjZNGhDlLHmhhKSbMRrwxx6wBQCQT9ssg2hXh9GKU7ZOPXJRXelcFik-PXhgblQwJyG3N1ZyMNr8LIIIuZ6iXpJURSzSQ2WhARIfT4bW5AHBSp-3osVWqY_nyCgN4kxJbYIWXTyA9NepDK0K16QCaMR0O96MIBcASwgpII5jwbwr-vHW-EmgG1Y35R8t2ZS33lxvlmmvU2yVGeegIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yl3n0isDeXxNUDy8q4SwVreOuyOeDFaOba06XTU-aaPVvSpmDTqHFGm9atexXODbBKq-cfxFCzkFOhjm_fkZB81GAEeMITiODuOVlHZSceCf_2G-sE65uq2kVH-iNnWK1xXNkjZNGhDlLHmhhKSbMRrwxx6wBQCQT9ssg2hXh9GKU7ZOPXJRXelcFik-PXhgblQwJyG3N1ZyMNr8LIIIuZ6iXpJURSzSQ2WhARIfT4bW5AHBSp-3osVWqY_nyCgN4kxJbYIWXTyA9NepDK0K16QCaMR0O96MIBcASwgpII5jwbwr-vHW-EmgG1Y35R8t2ZS33lxvlmmvU2yVGeegIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=jEgJxwm8_Ov8c0ryB7ZsCUVLpQonaWurd0StJF3aWVAP1ecF_Rlb_Yg4Y40DtaYGMUSMpi7EDQNVO9fAbWagtF74_JS6ou-1rDaSBtpVDhMskPWkA02EghcJNVKDciL2Q7CJ0hP7FCsygVVotaFg7VMITxGlnOr9JjKPZr_a1BN1zPU6P7CkD1COkb3Q0wF0kGNa_S9KxREeYAvzzFpw0f1hv2UmaISch6CCKU1Zab8vKCKiMLkSAK9eCfGQudIIdwnBvIR4YaGOpl87Bc7Z38u3KybHlWoRfcwyaVV_Y2ZGGHg91t2hGn_4261fa1ManrqaI46N7w_ra4J8m2D3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=jEgJxwm8_Ov8c0ryB7ZsCUVLpQonaWurd0StJF3aWVAP1ecF_Rlb_Yg4Y40DtaYGMUSMpi7EDQNVO9fAbWagtF74_JS6ou-1rDaSBtpVDhMskPWkA02EghcJNVKDciL2Q7CJ0hP7FCsygVVotaFg7VMITxGlnOr9JjKPZr_a1BN1zPU6P7CkD1COkb3Q0wF0kGNa_S9KxREeYAvzzFpw0f1hv2UmaISch6CCKU1Zab8vKCKiMLkSAK9eCfGQudIIdwnBvIR4YaGOpl87Bc7Z38u3KybHlWoRfcwyaVV_Y2ZGGHg91t2hGn_4261fa1ManrqaI46N7w_ra4J8m2D3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF67PhOfs_vIj1PWregw7FDCgGXuWDp0Mz5pKZ1TtOqxrevBnL6s8q0WDv9c3roZQpPIEMFaelkMlK_7rmpzygM4dGlDOH5CSKtSjAp3Z0VSU0YhsR-Ot9M3UN_Vh9DXi8mixAzp36m29TJKR5Db8s69ySS3YOMpv6E2o8v1rm8QXGIXDxRVoXzEYoDrQhWtBWEY5FxU0xDDaqXKK0B4wmCZDx_sJS5Szcn4vgJ23kMAyiwxoKLRFzst1tT-I4VF1ZARBJm1P2BoMRWeH5kjKsjbnWWPS2ZbKskPgiVs8TD-yfMxAe8f8QjLgEas4kFORPokusOodNr504-s3l-hJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiIijq25G_Sm39Akteb5AsmMHOH9WhFuTdWxJ9kUXK5Qp71fyXnhziTam9wCbT-XTl8nWMsH6ME7FDIMXNPGEosSWNaX41-OdqrO-T4ZrWfwPTi0r3UtK6hhTbvpxlg8fyc_7lc8dvFEC2l0xWflK3tXx1MGMX3pCHB5PB9Kcbl7HKWieney5QRZAjxxVID6TddeO40yaKSzVtiw_-GQqVGjNvjsQQZMMa1T84gukNgHDImdAootsOT8CUGry0liWvEbYC9A8lCaDjPKv5Wu0QjDFP1JrvnIiCpMH-fGcFrD8edkv2YRBYXM3veLbJI19i8JoKfALL998iKxqyLTcm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiIijq25G_Sm39Akteb5AsmMHOH9WhFuTdWxJ9kUXK5Qp71fyXnhziTam9wCbT-XTl8nWMsH6ME7FDIMXNPGEosSWNaX41-OdqrO-T4ZrWfwPTi0r3UtK6hhTbvpxlg8fyc_7lc8dvFEC2l0xWflK3tXx1MGMX3pCHB5PB9Kcbl7HKWieney5QRZAjxxVID6TddeO40yaKSzVtiw_-GQqVGjNvjsQQZMMa1T84gukNgHDImdAootsOT8CUGry0liWvEbYC9A8lCaDjPKv5Wu0QjDFP1JrvnIiCpMH-fGcFrD8edkv2YRBYXM3veLbJI19i8JoKfALL998iKxqyLTcm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy0BtNgu-nrY-TFCiIPQk8jIeLKPxU3veJFN3z3MME0fYmwKNd0Rzc1u7RwqyU9phS7th7LNm23GI3ufuuMBTrVWk59I8B97QtVyuR_fkUNpRkWXdrI0WIHqUZIzN_fj1eyrYcAmforGCnAsBS2XblN7z2fNB4rwaEQkAvhx4uIXFnhkZINnG72fQKEBqRZTOFY9Ln9Ghks6KpeHRIChtVFbMLJTIw-xWHF1U0GJJyp7Y6eZmZTg7gba910-5O2J1NjzMV3-dObXIjwq_GylSOwk9ne-bcXMgvSwmLgLqsoM3xK8sOl4QJliLKbMDKA5m3pULc--W9Ra-vBPAwBlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=SmIdYhAjxjlIyLr9hEby9j590B3-J_4asl5PlMNKI94MjetEuc4QnASYojsGCOjYh7wJmEcTT7Ml9-047BXTCINRo01j0Z8Sq1nRW_ml8aCQ4GuZWOEr4898kaN-OtG06wUHL7xpg0DinlfwJiX5NnGfjxFjWa030MmddbvcFriMxJ3-hVVUNjIPj2G9Tft1NLdeos2gxDz0AmIuBwmLtiiiXR7SavhKUYAftACLigyii2ug3FoP7QvhSsF7bDXqmpyBmiMPEyKYRkjvN4y8SmvLHdJPrHi9sP4oFY4tNw0k_jKowNNp46PmXbUrZ7MLMgczc-xjoHBEGKfsXWOI9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=SmIdYhAjxjlIyLr9hEby9j590B3-J_4asl5PlMNKI94MjetEuc4QnASYojsGCOjYh7wJmEcTT7Ml9-047BXTCINRo01j0Z8Sq1nRW_ml8aCQ4GuZWOEr4898kaN-OtG06wUHL7xpg0DinlfwJiX5NnGfjxFjWa030MmddbvcFriMxJ3-hVVUNjIPj2G9Tft1NLdeos2gxDz0AmIuBwmLtiiiXR7SavhKUYAftACLigyii2ug3FoP7QvhSsF7bDXqmpyBmiMPEyKYRkjvN4y8SmvLHdJPrHi9sP4oFY4tNw0k_jKowNNp46PmXbUrZ7MLMgczc-xjoHBEGKfsXWOI9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
