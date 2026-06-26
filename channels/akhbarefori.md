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
<img src="https://cdn4.telesco.pe/file/GF-xu6iFIVpSV9z7HIaSBtJY3D--QlQqFiEHza23tlxtv_Tpy5G8oEHBfyyYCJjUl_o9zS3IeFkpcUukoqxQs8SQoZ4G64ApaTyj5B2pn869DMyhC7TQn4IJigR3dSW1KURFIRfTRP0c_yL8p2o2uB0BcA4aSA_gAIUP03zpWQTCKbh0WS6c5mufhtn0vtGB9l8SAI-FXi_KzKEY2_nIRZYLakqNt-XU3tROjkshUmDk4Jm7x1-E6K1JtnEt-AkSVChHQ91qxDQpTxKbfvQbYuRzR9FcZY8KByvn-9ZZ2VJxErCIhzzfh4UcQV3j3pLC8HTbrgrXOk4G8pDhycXnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-663439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
مونته‌نگرو مدعی دستگیری یک هکر مرتبط با ایران شد
🔹
مونته‌نگرو اعلام کرد که با اف‌بی‌آی برای دستگیری «امیر براتی» ۳۹ ساله که گفته می‌شود تابعیت ایرانی و ترکیه‌ای دارد، همکاری کرده‌اند.
🔹
به نوشته روزنامه ترکیه‌ تودی، پلیس اعلام کرد که براتی به اتهامات مربوط به جرایم سایبری و سازمان‌یافته، کلاهبرداری، هک و سرقت هویت تحت تعقیب بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/663439" target="_blank">📅 13:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ2SF5Tej9QTb0UND8KetcIFK7MG5X9vcinvTnD1Z0_XZOSMwts__v9K693MEA24QaBS_RCcAjYwDhp0A5t2AMtEw0P5CGbZVpMy258V2_49GhU1AtZ4a5Fj2Hk85OwoLZZky0UHZPpuFPolYCUxYGvnxSMKZmne78SeE4kf3BDl1JA6AEQGrn9McWvNuzqZaxEsBlUQFhWeFI-51t-0LjX7OInuHzwWekWOIIQ__BH_myWRxgczrULzY_c0ESdG9Hgam4ctRDyVF90SPALAqNn-F0qyfYky0S5vXKSEFFq1JQEBvun_ZxjbaB9UFgCWOLG16y4_Bd0rCT0TylfZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه: آمریکا نیازمند احسان و خیرات برای حل مشکل گرسنگی است
🔹
طبق گزارش "سازمان جهانی آموزش خدمات گرسنگی" «در ایالات متحده، بیش از ۴۷ میلیون نفر، شامل یک نفر از هر پنج کودک، از دسترسی به غذای کافی برای یک زندگی سالم محروم هستند. از سال ۲۰۲۰ تاکنون، تعداد افرادی که با ناامنی غذایی مواجه‌اند، ۴٫۲ میلیون نفر افزایش یافته است.»
🔹
طبق گزارش سازمان "تغذیه آمریکا" «چهل و هفت میلیون نفر آمریکایی با ناامنی غذایی روبرو هستند — و هر روز با چالش‌ گرسنگی و تبعات بهداشتی و اجتماعی آن دست‌وپنجه نرم می‌کنند.»
🔹
البته خبر خوب این است که مدتی است مقام‌های آمریکایی دیگر نباید چنین آمارهای ناخوشایندی را ببینند چون بعد از ۳۰ سال گزارش‌دهی مستمر سالانه درباره وضعیت ناامنی غذایی و گرسنگی در آمریکا، وزارت کشاورزی آمریکا (USDA) از سپتامبر ۲۰۲۴ بی‌سر و صدا تهیه این گزارش را متوقف کرد. بدین ترتیب اکنون نزدیک به دو سال است که مشکل گرسنگی در آمریکا حل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/663438" target="_blank">📅 13:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZx8QPlSG7NFRjnsZv9-EjGtsmwgw9pkZswnW7YCA3W2p6EnNBumLCCJwzhP8NDg-zc1snys5EcVr9sZtPSzlFW_RrnF735Jtvcja-QL3VXsxjw37Xmpn9MpJhgXSK-EscvcItoYxYWOhzR8unS1OVPC-hCCBq3HEqH_Mk7NLo25P_E-na40mV4zLNY7jEHG0OGXJgXdku8FVCiLO-WbVLP85vZYsCQnWfK16sdgdVCKvjJXjB9PRHoP1a07kdY4GDOQMCAc1qzXDBeHI8zIIAAORDxysPdlTXWzufSdMd9PsIhaHCrDy9jy7w_HHxxroDcLLFlZxCCXxpWCRFN_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG6qQ2YuvTq4TjjlHvksIq3Nh3FNHHz8JiXcbfd1KMCju08175HD-iDyZwheMRmrMCQyfvdtzYW9PPa3__NxtZqYNKWIgSdo5KQwpMwiblaUpOEJ4L9P6cLw3FAbqsdKmUgAl4ugm7O6xUFCxQRtY3e2Oc1I_-LcewgBR-dQlaBwRH47-fXTGt1R1ON4LrSaRV9LAQrry4-opVz1PJCR7xuHL6cxq7QzvramMR3_Sf8b0kGjgdlLPSEWSe5x4k4kt2obAJ0gyY6xBy-NUmYj8Ure30ugkDo8RignenbrHsKaXCwuxf1An2C3bvk_DWpShK-8QAh9RIFItEn2thsFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8NydjYmhMIcF5yz3hUj3SoWfKag6VsYOc23NWyKwzA14PkuPKcsC6M0gPxQkubZGqBuhOG2IhESbvRYL7K9O0V2KHu8aBl4gdINadfSleR6hegGyR0Blj0006eshw9yNuPln_czZBc4zawwD5n__8Lfq9ZMHnX6g0-cEUlkiqGLnvqJSyccpNDfkEljKdvhz1AvGvi6ra_6BUS7Kr-lKGsTpBDBXORi1ooeT-WkPs_XZjJigWSnt0NEwhm8Sl7gyxg7T50KgUQdeCAOGM3tikULuifABTCHF40cD8tjf5Hn9ucOE_5XLI9X2jht5AcAzc9pvpETKqxHwCuaO9vwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRWn1ViidzWEz4fie3kUphIyfeiIHcUhXYZOYUm7OV5to2NkrjyOLNSyj3zT4SGALi_zdmQmc7VfLDp4NuKbbq_a9NqhkpWttNm15UdFeSBydGHfg-vYYGCSLtRiFGa6XCbOv-_hRB5d8Epb8ZNTI4uxvxtdAGOpdGjDeDOjbYpYzXrsxKXQMA1Gb3TVVv9vHskumbGr34QivFGI2F9rhX6R8g3GtBooW9SbxaGyFtnfr1ZJgiqsPUo-O8hX64wubHd-ZqJh4gFgdTJ64BQ_IwRjHz2CZuF-lDI5WolmM43xB7EVFnQemF7DeIvuXe9b4fdO7gFO-HL77kURP44_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFfrPaclNxMCA_iFjgxcnMREHeMXFbtnWIkTw7PHpRtx7otjTc7dS72-875cjSFAYWmqLPsFqE_TWXtr16yH0_5KkeCHWhdapDLuPyGTYib1prOb7C1ceF9Ve5GHQz6-scIJGIMUIBmSKmHuk3ooi4U0QvHmunA4F2F3SLKSFXxi82vqK_f3kiGEuZE2kAdgauKnmr44ug5E0w6kolsfFbvDncKo6SyO2NyF5OcyojWUkE6b_41LAGS-xI_7IVCkWsneO-QqY5VipUZZKmmYSHkvXmPG_14OJp-ET0L9RLNRR5jH27G_QxOd7gV2iuDqyOrvVzxTnPZCZPsgCzveGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fla2qWhAJHCSmNYvVtmCYTvhZtTEwY18Y7XzglFwn-AuU8DWgRzxLku-Dg7h1b4xRNbqOaOuSJcqPcLvWwhCOj5L0vG8ARVTgcXg3Ci0zagsTX76s_R_u-FD2Aw55SF9uP3O1xNO4ETqACJa98rUJfKyFcslGA0eoDTNCptPnPL4OqDPmvphaRzdElobP6mIcgtKDooEFgu3ZBi9sFHZmCnx3J6Mstb63NBMTgikCxG8uXP2QLT4RXHunylViF2zjhWI5873FDivgOK7Tr0vanYz6FxIiLJ_Agcd60M2H6oM_R2SWsZ_XIEVonRihMzDSv84WFVKNkaL8PNAJ_8z_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر جدید ماهواره‌ای
WSJ
ابعاد خسارت‌هایی را که ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین وارد کرده، آشکار می‌کند
🔹
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/663432" target="_blank">📅 13:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S20hePo2Cq3GEJSfj4aWXFyNXzRpiAOyJsY35eI9qC0vC6O2qkOWfFxOHim_cSBcnc6khzWf2Bofb9seHClxsT9a1fWX0eUN7Da6DsNphwuwttk7fXJaMNWxXgVeENA1negZgD3LWjC4xdv2JJM8tocmMNm8ZvYIP2La8cyxtN55pfXeKaiz65dR2C4tg8v3DU2-zOA-s_4AXSY8a0R4SLP3x7VPnYG58eQ8a5iNWgCyEnuEiYE-nNMcshnJ77NkHJGAigc6EimmVjIqxrmjp00Tx0FMgUW9YFHk7rxVuek3lbU0rlu06Y9wdZuLhcfRpLqz5b7-D_h7lGyhYcCBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هشدار آشنا: جایگاه رهبری را در حد فهم ناقص خود پایین نیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/663430" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMcW10zBhoZ7dbrwSkyueiWTjEvAhU9tKF3Ikagrwo_jBc9TAgbiYOX9RnCcDyUOBdAwsR3dG6F--IhZKmLa2k9d1_dizuBsocQ9yA26xCu12P8wkM4ZqCp8iNgAdE47ckBo2MUMpUPbm3PmoCyaaBAcRCHPU8NmZklWQ15RHJmLwltfbXePZ7S8M4KUndGSU8nNC75QfwRttZks1WIY2enywTN7HUJeMQeTIIUdINFWplyDVbc9sJZM0AFeD7lsirdmDDl5DZLDgIf9M4a6PqjrkVxkEyHLIYp685X0whf0sfyyxQRjjI3Y8dyswHiWtEbCDKacff1hfL8wasn-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چین اولین هتل کاملاً رباتیک جهان را تا سال ۲۰۲۷ افتتاح می‌کند
🔹
شرکت چینی Pudu Robotics اعلام کرد قصد دارد تا سال ۲۰۲۷ نخستین هتل کاملاً رباتیک جهان را در یک جزیره مصنوعی افتتاح کند؛ هتلی که تمامی خدمات از پذیرش، حمل بار و نظافت تا آشپزی، بدون دخالت انسان و توسط ربات‌ها انجام می‌شود. این هتل ۴۴ اتاق لوکس، رستوران و باشگاه خواهد داشت و با مدل هوش مصنوعی PuduFM 1.0 فعالیت می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/663429" target="_blank">📅 13:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مراسم عاشورا در لبنان
🔹
این مردم، سه سال است زیر حمله اسراییل قرار دارند، رژیم صهیونیستی خانه و کاشانه آنها را نابود کرده، مردم را آواره کرده، فرزندانشان را کشته تا تسلیم شوند، اما امروز سربلند و با پیامی واضح به دشمنان گفتند: "كِدْ كَيْدَكَ، وَاسْعَ سَعْيَكَ، وَنَاصِبْ جُهْدَكَ، فَوَاللَّهِ لا تَمْحُو ذِكْرَنَا، وَلا تُمِيتُ وَحْيَنَا"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/663427" target="_blank">📅 13:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663426">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
امروز ۵ تیر، آخرین فرصت ثبت‌نام در پذیرش کاردانی به کارشناسی
🔹
آمریکا، مذاکرات بین لبنان و اسرائیل را برای یک روز دیگر تمدید کرد
🔹
جدیدترین رنکینگ جهانی تیم‌های کشتی آزاد جهان؛ تیم ایران با ۱۵۰ امتیاز در رده سوم قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/663426" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663425">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
آغاز مراسم عزاداری سنتی «ركضة طويريج» در کربلای معلی
🔹
در سالروز شهادت امام حسین (ع)، میلیون‌ها عزادار حسینی در کربلا، مراسم تاریخی و باشکوه «رکضة طویریج» (با پای پیاده و هروله‌کنان) را آغاز کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663425" target="_blank">📅 13:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663424">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxQ9UtvFH5MRcdNaVGn18CEUmpJh6qv5NG-0q9UMr04f17LOw0EMw6mNuefN9OK7lVJ9aLCINRsk4fY34mCM_839EtI_bJrt86Q1RF3kTJf2Z_Ub7XI7XBBjPNwzqdENolp5I2Rulhu-hQ-6BqPvwu4yzvC-BfAeqKLTJKIs6I99arHdimYNJgSkl4nkOT21Pm2VmmmYMg1WPGCTK7_hiisUj-zd-SQQG4JaGimqtgVSuvO-ZarKLH-7q5tX6Icxhb3KyoVF-G3acrRXpLJh2tEaEb3hB2a0jYiXVn8Qb96b7dNgMZTFfSvlPxoLiX0QZQClTiwdP9DfOH3mqFP1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غریب‌آبادی: عبور ایمن در تنگه هرمز با تصمیم‌سازی خارج از ملاحظات ایران تضمین نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663424" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663423">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e439b39199.mp4?token=Ei-0HnAkvsDvC7bCkaSp-uPFDbmgKRyn_HyZuXoirEbbhgmmOOiywpb_KVHvdtHJ7TaYzpbDcoAfGBw9dxkhczv88vqydT99DD8Kfa8rq_wE-zIPlGySBJXr6cGo95KRFcK5xHSvf083Mhj67wAalZeSQdUERn0wrsk3J4IGKJtVGYI-B_JQ_6bCOVyaBracH-LaVYvSo93NHt_VXB7ixkcMWEphZI9JcTSwH2hLCmtntrnP7XU8gw24NhSN6Dd2TJlRb3QwmUv2if_5N5qHQsUWGf4ceHdufrklATp2YmXZm8IUgnmy0kR6BR8L2W5mDPVpxxbzcPeH0ZAMBZ3ZThahWZ3o_33ykzwJQksgN76QoP9wlw5Gv0L2WSccqgx63hLSZCTW1zcYf_TYOtlGOVN2jpRyr_Qmj6XqmDUe1EEeeTPkcXV-wVDsh7x3sI4xx6i9IRD2OzMPTerMwq5syeSl-EzyFNcLuE8IJLTE2k4M9X17TkeQLIRQzFtHo9-dn2UhRzz7t_-x473k67TRSxrr6v2s57ROg97hjmCg5Y7GG7_z6SM9I3qMx2hMWbFIpvdQzpl2Qb1fz-nazHG6dsktC40UEWD2YSuFb6C74U_QJvR7wTipr40AldZpgkfBojLiEVZG3seH_EgoKw9Ul-5qfQFISB0cvApUA_73N5k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e439b39199.mp4?token=Ei-0HnAkvsDvC7bCkaSp-uPFDbmgKRyn_HyZuXoirEbbhgmmOOiywpb_KVHvdtHJ7TaYzpbDcoAfGBw9dxkhczv88vqydT99DD8Kfa8rq_wE-zIPlGySBJXr6cGo95KRFcK5xHSvf083Mhj67wAalZeSQdUERn0wrsk3J4IGKJtVGYI-B_JQ_6bCOVyaBracH-LaVYvSo93NHt_VXB7ixkcMWEphZI9JcTSwH2hLCmtntrnP7XU8gw24NhSN6Dd2TJlRb3QwmUv2if_5N5qHQsUWGf4ceHdufrklATp2YmXZm8IUgnmy0kR6BR8L2W5mDPVpxxbzcPeH0ZAMBZ3ZThahWZ3o_33ykzwJQksgN76QoP9wlw5Gv0L2WSccqgx63hLSZCTW1zcYf_TYOtlGOVN2jpRyr_Qmj6XqmDUe1EEeeTPkcXV-wVDsh7x3sI4xx6i9IRD2OzMPTerMwq5syeSl-EzyFNcLuE8IJLTE2k4M9X17TkeQLIRQzFtHo9-dn2UhRzz7t_-x473k67TRSxrr6v2s57ROg97hjmCg5Y7GG7_z6SM9I3qMx2hMWbFIpvdQzpl2Qb1fz-nazHG6dsktC40UEWD2YSuFb6C74U_QJvR7wTipr40AldZpgkfBojLiEVZG3seH_EgoKw9Ul-5qfQFISB0cvApUA_73N5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هم‌اکنون کربلای معلی در روز عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/663423" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df46663276.mp4?token=gJFhJ7L7bSfZUnfVW4sOg0F8ZgDZvSIYhuO9yY7cC3SgfVZr2l_SwrOhAgKbXzCLD01X-qPqKOWfSdkjSaWRU_17jCmp8ElPBIoKpOfhQTWcy19Ij13Us2itQReHh2hOjfYHlpOrfpcUSthXKnPmONMmu8uoM2Ly2IK3O1erArDXeaOFlQl0q-p60ByaTQvX26K8SPYjLTS9tObOMdSFwqTnd9xE2ob_dYaes2JSIOkT4qV5RaDf-xkRI4yTQVgkPUNeciZ302A2-ogbNXTMig2vOjlADHYqWwDbj8odooMweh5MIt6P_Ft-Ff8SqTmhk_ZkZJbHRm6P8VHfHp26Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df46663276.mp4?token=gJFhJ7L7bSfZUnfVW4sOg0F8ZgDZvSIYhuO9yY7cC3SgfVZr2l_SwrOhAgKbXzCLD01X-qPqKOWfSdkjSaWRU_17jCmp8ElPBIoKpOfhQTWcy19Ij13Us2itQReHh2hOjfYHlpOrfpcUSthXKnPmONMmu8uoM2Ly2IK3O1erArDXeaOFlQl0q-p60ByaTQvX26K8SPYjLTS9tObOMdSFwqTnd9xE2ob_dYaes2JSIOkT4qV5RaDf-xkRI4yTQVgkPUNeciZ302A2-ogbNXTMig2vOjlADHYqWwDbj8odooMweh5MIt6P_Ft-Ff8SqTmhk_ZkZJbHRm6P8VHfHp26Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تجمع هزاران یهودی ضدصهیونیست مقابل کنسولگری رژیم صهیونیستی در نیویورک علیه رژیم صهیونیستی و قانون خدمت نظامی در ارتش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/663421" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
اکوادور غول‌کشی کرد و به‌عنوان تیم سوم صعود کرد؛ شکست ناباورانه شاگردان ناگلزمن مقابل اکوادور
⬛️
🇩🇪
1️⃣
🏆
2️⃣
🇬🇶
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/663419" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روسیه داره باقی مانده زیرساخت‌های اوکراین رو میزنه
🔹
اینجا یک پمپ بنزین با پهپاد شاهد ۱۳۶ هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/663418" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پیش‌دستانه‌ای که شکوه را به ایران برگرداند...
ماجرای کامل این دستآورد بزرگ نظامی
👇🏻
https://youtu.be/AXNLsCbNe7w?si=DA0CyGP385V7uitO</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/663417" target="_blank">📅 12:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
وقتی نوه ترامپ راهنمای تور کاخ سفید می‌شود!
🔹
در ویدئویی تازه که در فضای مجازی منتشر شده، کای ترامپ، نوه دونالد ترامپ، رئیس‌جمهور آمریکا، مخاطبان را به گوشه‌هایی از کاخ سفید برده که کمتر جلوی دوربین رسمی قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/663416" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFRORvIgsfoV4itmd_mnZoIAArkCNQppxpWXbeR0Nwdj9fVPZvX2PrEf00zM90k8CZTvkC35SlMKW0T8_B_szSPI2IAAR9ZhDXSiweUBWdGZj220dAUWzoAKDmQjgOzKg85JYdKoY1tZJv6aSxRu9irR1NIwhm4lr1IlTPz8rY_gOFNuM8CEf2xIGaTmf_UaeaLG5ahELAOYnKpkMpp6Wofq8tlGTXO-E9Lqc8x3zDsQorreSOA3F3G4YYwevZV_oZSblErXOjVumwQzg92Ja0zmX1DpgLEYgr7i1rySO6GIJRBfu_Ab9ZEpPThyMpJeFJgdkihEn7FP86Al6_A4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۲٪ اسرائیلی‌ها ایران را پیروز جنگ می‌دانند
🔹
طبق نظرسنجی دانشگاه اورشلیم ۹۲ درصد اسرائیلی‌ها معتقدند ایران برنده جنگ است.
🔹
۸۷.۸ درصد معتقدند اسرائیل به اهداف اصلی خود در این عملیات نرسیده است و ۸۲.۹ درصد می‌گویند این جنگ امنیت بلندمدت اسرائیل را تضعیف کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663415" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توزیع نذورات در میان خودروها در عزاداری شب عاشورا(دیشب) در شهر دیترویت ایالت میشیگان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/663414" target="_blank">📅 12:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لاابالی یعنی چی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/663413" target="_blank">📅 12:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔹
قرارداد ۳۵ میلیاردی پنتاگون برای فرار از بحران ذخایر تسلیحاتی پس از جنگ با ایران
🔹
وزارت جنگ آمریکا (پنتاگون) قرارداد بزرگی به ارزش ۳۵ میلیارد دلار با شرکت لاکهید مارتین امضا کرده تا تولید موشک‌های رهگیر پیشرفته THAAD را به‌طور قابل توجهی افزایش دهد. این اقدام به‌عنوان بزرگ‌ترین تلاش فوری آمریکا برای جبران کاهش ذخایر تسلیحاتی پس از جنگ اخیر با ایران توصیف شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/663412" target="_blank">📅 12:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
طبس گرم‌ترین نقطهٔ جهان شد
🔹
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663411" target="_blank">📅 12:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImsY8fTugR1sLoBKs1jBWjolnXYpVsfFo6ayZaDFlhbsHRwdw9gxDh_lfA0pAoRABhCvVBWQAWUOaLiSlU5FOdnoQWrQiyrKKXM0mTbIdTn9q_ALVtPpYB4tUm2hFa5hT0quAyt8JDS151biUe2vYqtEAfUqPXR8bvUwqvC7aekURR-h30GW0C4ZMOvLV6YS7uwiZwcJxDw-W0l9Y1q0fiXgBPSmVWo6JPYknAOsa1pyH1YmRgjjrOJvt6bAacJ5W2L5KzPr4LvDUCJ9dE8pkTAyltC8xa-lyy9YLS26h-bclStwJRjw25p8sqaHUKTNa8wznVH8iWovHZWhFbB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اقداماتی که بسیاری تصور می‌کنند به کاهش آکنه (جوش) کمک می‌کنند، اما در واقع باعث تشدید آن می‌شوند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/663410" target="_blank">📅 12:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
شیخ نعیم قاسم: پس از خروج اسرائیل، راهبرد امنیت ملی را تدوین می‌کنیم
.
🔹
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد.
🔹
مصر خواستار تمرکز اقدام بین‌المللی بر مساله فلسطین و طرح غزه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/663409" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
کارشناس نظامی لبنانی: ایران باید استراتژی خود را در دوران پساجنگ بازتعریف کند
روی، فعال رسانه و کارشناس نظامی لبنانی در
#گفتگو
با خبرفوری:
🔹
ایران در دوران پساجنگ با مرحله‌ای پیچیده روبه‌روست؛ جایی که نبرد اصلی از میدان نظامی به جنگ روایت‌ها و رقابت ژئوپلیتیکی منتقل شده است. هم‌زمان تلاش‌هایی برای بازترسیم تصویر ایران در سطح جهانی و تغییر موازنه مسیرهای راهبردی منطقه در جریان است، موضوعی که نقش آینده تهران را در نظم جدید منطقه‌ای تحت تأثیر قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663408" target="_blank">📅 12:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
بازداشت یک ایرانی در مونته‌نگرو با درخواست اف‌بی‌آی
🔹
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
🔹
بنا بر ادعای اداره پلیس مونته‌نگر، این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663407" target="_blank">📅 11:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=sB0nEAjj1K1p5akBSIGHIOhFIdzeUS0IoLxj47-bKAA5M64z18gNhDYN7P5pg6BJbkHxCr3H0OcNp0-RFe1d-6abU62OpoliJD3GAtL5TNFulpgC-L5j1qQGKGAMouivGOvPmV0Qy4YwIvTiXNd0iqgeL5cEzJom-eSVWJmZcoai0K2SfvM89fZkfp6X9elckwgmWAeC5iaffnsL5lJJGZgG4SEPjSAkPiqkrbnd9oEt-O_dHI3wKC4iEnJIuCE6isqm_8Tq9_6pSM63VjQHhuSvXlI7ExSvlvLzq0siFbYGZjHs5brmL_gkcN-6wufIBwO7wQBaoSeVsSUKQYfQuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=sB0nEAjj1K1p5akBSIGHIOhFIdzeUS0IoLxj47-bKAA5M64z18gNhDYN7P5pg6BJbkHxCr3H0OcNp0-RFe1d-6abU62OpoliJD3GAtL5TNFulpgC-L5j1qQGKGAMouivGOvPmV0Qy4YwIvTiXNd0iqgeL5cEzJom-eSVWJmZcoai0K2SfvM89fZkfp6X9elckwgmWAeC5iaffnsL5lJJGZgG4SEPjSAkPiqkrbnd9oEt-O_dHI3wKC4iEnJIuCE6isqm_8Tq9_6pSM63VjQHhuSvXlI7ExSvlvLzq0siFbYGZjHs5brmL_gkcN-6wufIBwO7wQBaoSeVsSUKQYfQuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قاسمیان: نباید فعلا مذاکره کرد؛ باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/663406" target="_blank">📅 11:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad86b4ad7b.mp4?token=dRGwAfDZ1U84ir5BkTIAOg5nY_AcXzpgOec21tF0ou7mY6CSOA3CEHnMtsGUPGACg_b3iKJLL_HDBxRNAxwTzHxIKr781Avt8O3rfBJa6LOyVSjGSBTF6w1FFA3QFBtPTzerIyx241_tpDOYoyU9Gz_X0RyA4VVa23ERhJtGcrfEu1ZilJ8HR3lqDQzrEBnewEumfRy-39ux5pm3E4ZMquriJHJPz5fEaOrLKrcILWDOPtREGmuN4mvxF_B_P5ifDyUyerILrfVLYApn1rWWtGOUFm01__b9pcsuU_8qACKK7CR5IN3DJIhBiGf0jYTwWVv-aWO4nhcFq_B1Go3M0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad86b4ad7b.mp4?token=dRGwAfDZ1U84ir5BkTIAOg5nY_AcXzpgOec21tF0ou7mY6CSOA3CEHnMtsGUPGACg_b3iKJLL_HDBxRNAxwTzHxIKr781Avt8O3rfBJa6LOyVSjGSBTF6w1FFA3QFBtPTzerIyx241_tpDOYoyU9Gz_X0RyA4VVa23ERhJtGcrfEu1ZilJ8HR3lqDQzrEBnewEumfRy-39ux5pm3E4ZMquriJHJPz5fEaOrLKrcILWDOPtREGmuN4mvxF_B_P5ifDyUyerILrfVLYApn1rWWtGOUFm01__b9pcsuU_8qACKK7CR5IN3DJIhBiGf0jYTwWVv-aWO4nhcFq_B1Go3M0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برگزاری مراسم عاشورای حسینی در ناصریه عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/663405" target="_blank">📅 11:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=a9S8g-10FD4Iu35mMV4N16AeHLAEj5QXr7pDC0Iuiodu8wvKRGvaj0prc4zXMYw3IQezeEfvPC5GdLoyb7UrzFdAviuxAraEW24igLmEOP5A-yAAn6K2UiDGKL1LN0IFVjjECbNitTWd2oN8KGugVmRm_svP_5uftqBjXFoF4I5i_dOXfkQMBSpP3MHkmPtaxq2dLMO-VHZkI7T-P11WTfLDG_KiGgT1R5CSoR4B0BXC55v7ZFOPz-R0n_MjvrKrxq1OcLnQM5IM0Q40IDAfTtU8d3EWkDOVPjAyEglCrYfnSwG7ZFMxOq7GuLZRsOfoOacXXm4kLi_tn0T02c0o7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=a9S8g-10FD4Iu35mMV4N16AeHLAEj5QXr7pDC0Iuiodu8wvKRGvaj0prc4zXMYw3IQezeEfvPC5GdLoyb7UrzFdAviuxAraEW24igLmEOP5A-yAAn6K2UiDGKL1LN0IFVjjECbNitTWd2oN8KGugVmRm_svP_5uftqBjXFoF4I5i_dOXfkQMBSpP3MHkmPtaxq2dLMO-VHZkI7T-P11WTfLDG_KiGgT1R5CSoR4B0BXC55v7ZFOPz-R0n_MjvrKrxq1OcLnQM5IM0Q40IDAfTtU8d3EWkDOVPjAyEglCrYfnSwG7ZFMxOq7GuLZRsOfoOacXXm4kLi_tn0T02c0o7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یاسر جبرائیلی: اگر بناست با آمریکا ببندیم؛ ظریف را ببریم
🔹
یک بچه و بساز بفروش و پاساژدار را به مذاکرات فرستاده‌ایم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/663404" target="_blank">📅 11:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgQNwYZv4TAX_CSwkQM3jIbygno0PHDuPtV9b3Ow9fqcWO85VOuVAGu1-b-PxWjA0SYxtkT8MMfwRlDDsyqDHNTcVx98z-ii4Rd7zDYxg6gLP2WYRO_DOq9kQYHGpHIDK553qKd9JnoCS6xbgfYesyyk4QI8QvsmRQ3hdPEabYgWjT519HGTMd7eS95Dxp77ILRAQLVt3gYfQiWjNEMtljuFDnwT3TxoU5fUoVheYYmbhnOO1onweuh902IFxN77ySBX7_kOEaASrxNQ9e-RYbi97UZpVNwvZlqNch4Nkb9_gwhbBrK5a8rEh96zw8s3mzOtJblJ17_XPVvaebAPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هفت دستگاه موسیقی ایرانی به زبان ساده...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/663403" target="_blank">📅 11:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663402">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔹
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/663402" target="_blank">📅 11:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igstEMSkxB8yvzEgLr2DhTvW5IQuZra--9Apn4skd63o5jwT1q9bfl3g06DHCIIBOiM5Q79eJE2VyIh0Bdz-IPzwnx2vxYgxFI3ODVC-dhezrYYN47wOWCo90k2pPVyfTma5-18MCtYsAq2_7BrBcF5KvPiWcaDADPDu4tC72TBqNkyXiMbsc2TQwLIGuvxFrSN__z1fUiFBFlHMxshbzByyg21dlpRCJFC-l99qHo4LeZl3MTYxZNmtCGl57rvolKMmwhW1E2oyOcOxEACJlCt388ptyoiOV2OpQ-GSP9uFX17Cnr8NI6d_CCTmQAnGZuh4Z-YrgsC3V2wE9sCETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlEZC2-nU5HebGeNTN-4KxkN_-u-j2n2numglkYILT_8KkQJhPdxKLv80aK9Wj-reIMZoA_R3ESWzPbBmSdXMVtxJch-wEN7Su11ZrgV7fFTC-sB39d1H6Wts2P4Ljn5n1R9FGr-k07l2W4pFk1dqSVKPuFpH_YWYtZcNKjuVIM4UqObzIbEdzHaQ0GVzXRtaxBvJxZe-hhL3Y86dy-7wceBMN2I-lSthmUkwJaM-k2KlwhVew96aODuJ_MExlpBFpJv5yrzBN2gEwQYaaFJDh84jVbaP5NQ916SHU_qCJV37e_h_mvO9FcvRIjuGg1GJYGW4KYh_XxO8FL16kHLlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بیانیه وزارت خارجه درباره بیانیه مداخله‌جویانه وزرای خارجه آمریکا و شورای همکاری خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663399" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhmR_9QdIf7b3MXIiRTccKYiGtBf0egchPLk-qh698gRuliBL5qM3ia9_u-fNEMXJZMQMK__3kQVkTDXzPkWTr_Ln7itV-iyT7YwKV45GPvY8vbpi56q37ImCWer2oqLrccYhHGlhOJ01YLS_tRgSbcc-j_s5nBopUTVYE8FgJkjDsCig0UgqHmcx_H7_WHxBgbpBgOJvsusp0IIlLP6KO4rwwr0tIuvbLNgaD8LvGaRvNZSZxtplEQMPn-GALmpvPRHZNYYxcGbIl5wWSz4gBkohdboxrNm4hxTLgAzj7mVR9VOU1-GMJFbx5kP1nVyXPuZ4EwqvrFG5U57nkfUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه مسابقات روز شانزدهم دور گروهی
جام جهانی ۲٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663398" target="_blank">📅 11:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75094a4f3.mp4?token=Vm7rplq-RzfZYSeXdpM4UZ01m_lGUAKr--S_xlh6bWQrxYeT5EyKTZM3xKliQ-m-1JAZ7CHcsMweWk6oyxkhZ1iBCNzRTearBP4FtDW08VH0XgyhAIjfKNVpEWlAZXn1Sc01VcUh0ga0XjuSdD6Thkj69cd12euPzjWjWYWMRXBLWaNSQgZZIrkWVragNy_lzV1q5RPHqxccagDAdLA2uILGFTc_qdIlJ92R4yAEZ8nL2AF6d14-jyrjYBQsvxfsYUGGGl5MVo17w_8ggKk9am1_02Spxj8t65OPh_Nv3kfEbDwLgNvPybrfMHZo1hyItdQYe9LE9T2gz7wenTJa4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75094a4f3.mp4?token=Vm7rplq-RzfZYSeXdpM4UZ01m_lGUAKr--S_xlh6bWQrxYeT5EyKTZM3xKliQ-m-1JAZ7CHcsMweWk6oyxkhZ1iBCNzRTearBP4FtDW08VH0XgyhAIjfKNVpEWlAZXn1Sc01VcUh0ga0XjuSdD6Thkj69cd12euPzjWjWYWMRXBLWaNSQgZZIrkWVragNy_lzV1q5RPHqxccagDAdLA2uILGFTc_qdIlJ92R4yAEZ8nL2AF6d14-jyrjYBQsvxfsYUGGGl5MVo17w_8ggKk9am1_02Spxj8t65OPh_Nv3kfEbDwLgNvPybrfMHZo1hyItdQYe9LE9T2gz7wenTJa4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
آتش‌سوزی جنگلی شدید در شمال انگلیس
🔹
همزمان با ادامه موج شدید گرمای اوایل تابستان در بریتانیا که باعث افزایش غیرمعمول دما و خشک و قابل اشتعال شدن پوشش گیاهی شده، آتش‌سوزی جنگلی بزرگی در شمال انگلیس رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663397" target="_blank">📅 11:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
دبیرکل حزب‌الله: در کنار ایران خواهیم بود
‏
شیخ نعیم قاسم
:
🔹
ایران با ایستادگی خود موفق شد به تفاهم‌نامه‌ای دست یابد که به معنای اعلام رسمی‌ شکست آمریکا و اسرائیل است.
🔹
امسال، شاهد باشکوه‌ترین مراسم عاشورایی و حضور گسترده مردم با وجود آوارگی، درد، فقدان و مشکلات بودیم.
🔹
امانت شهدا، جانبازان و اسرا بر دوش ماست و از آنچه فدا کردند، محافظت خواهیم کرد.
🔹
اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/663394" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiI_iAu5xDiyXSQbRYDOPa1Z82cE5Glgvgs8-go12-lYlu-7b5LVcum45kwBQMQETnm81J5GQEgkT4wK74r4PmiD03pq64cRLoC8qsUAnmASuB76KkemxdU7P4U7t1hXiMZgC-rzFqLriDT5GZECx8ere45S3dx7EYAvBq7IsBH284flTk6JzKSlA0_BS0P-hvSshZn13eUJYWW_TIZZ3tMPIig2m1DB42tr0Rf_xnkSRrkBcdISKWI6QdG4Cekvp-AFIyThSZaFC83HGeJVhaWvlE3PGSq3IvWnrvY9wjiLYtCvIKOwu5jeY8UrIyU0ha7z3ld2wdLeDFBt8t9TBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دانشمندان ردپای بی‌خوابی را در دهان پیدا کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/663393" target="_blank">📅 11:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
سخنگوی وزارت دفاع: دشمن با روایت‌سازی‌های غلط به دنبال ناامیدی و تفرقه در کشور است
🔹
خطوط قرمز نظام همان شروطی است که رهبر معظم انقلاب اعلام کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/663392" target="_blank">📅 10:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/663391" target="_blank">📅 10:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=dZGFUbgQgpyxdcnVbGhnmTLNIlKgUAJj6NXlv_NHjSq7btlFffm4RyLHDJ07ekrQR7w7eQEP50qTfshqNcsKNQAE_cgMfa6pUx8PH-MZ7Qri2ttKma8uh_uJ9L5MpP7_F6m4UHTeO8CbtXJ3VUDusrxTo3uoNr_KPeCvjyT38BUml-skz45jyUTmpj23rsCqPCMM4LlYJB6Rgt2CMcP0jl_9YKCdb91oaFPXMaUxVh0y3V8nCt1SLqKxA3ClHkwxDGSWccWmM9_E2c6HZaH1XY4BpOoFsUk4DCVkjLHmfVevhJQHpvglzw7tUmnivaXc0xZgX7NNx2GI8zignN4O6g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=dZGFUbgQgpyxdcnVbGhnmTLNIlKgUAJj6NXlv_NHjSq7btlFffm4RyLHDJ07ekrQR7w7eQEP50qTfshqNcsKNQAE_cgMfa6pUx8PH-MZ7Qri2ttKma8uh_uJ9L5MpP7_F6m4UHTeO8CbtXJ3VUDusrxTo3uoNr_KPeCvjyT38BUml-skz45jyUTmpj23rsCqPCMM4LlYJB6Rgt2CMcP0jl_9YKCdb91oaFPXMaUxVh0y3V8nCt1SLqKxA3ClHkwxDGSWccWmM9_E2c6HZaH1XY4BpOoFsUk4DCVkjLHmfVevhJQHpvglzw7tUmnivaXc0xZgX7NNx2GI8zignN4O6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداران در روز عاشورا در استانبول ترکیه، یاد و خاطره دانش‌آموزان شهید مدرسهٔ میناب را گرامی داشتند
اخبار به زبان ترکی را در کانال زیر دنبال کنید
👇
@AkhbareFori_TR</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/663390" target="_blank">📅 10:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
مذاکرات غیرمستقیم لبنان و اسرائیل برای چهارمین روز تمدید شد
اختلاف عمیقی بر سر نوع توافق دارند:
🔹
اسرائیل خواهان توافق رسمی و الزام‌آور دوجانبه است.
🔹
لبنان فقط "اعلامیه نیات سیاسی" زیر نظر آمریکا را می‌پذیرد و مخالف معاهده مستقیم است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663389" target="_blank">📅 10:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آغاز یک‌طرفه شدن جاده چالوس و آزادراه تهران–شمال از ساعت ۱۱
🔹
شنبه، ساعت کار ادارات مازندران به‌منظور حمایت از تیم ملی، ۲ ساعت دیرتر (از ۹:۳۰) شروع می‌شود.
🔹
سی‌ان‌ان: اسرائیل از کاهش موقت نیروهای خود در لبنان خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/663388" target="_blank">📅 10:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hQ8uk93Lp2Oe-TUMMliwqMd7wrAa9gMU8Tn_ohyiilX33ALfhnE5v5y1ohX-jG0RV6jsG8x8-bypfXJx2qFkrklcZBqV-kOHXr62gQjXsHJer0WY3LEB_cIOqDUHf3jfcRXGANdvsS55x9Q7XXM9WxXlUCiESjJoqm2yHIYvuP8dtW27tWUjuO93p_9k3sZpRhmgUC3n2d_a7daJgTjgZp1aMUqBYu_grUpttbE0sCmY2IuDSRi0ofNaQ3wIlxwNbNWwY9aqRUeMUc-jZzLG7cuWW-Lh_bKbfFynk4omT6CxMtuzi2Q7haTHPRl9IY_VrY5x6yHcL-wEXUgTOG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور شهردار نیویورک در مراسم عاشورا
🔹
شهردار مسلمان نیویورک با انتشار عکسی از خود در مراسم عزاداری امام‌ حسین (ع)، تصریح کرد، عدالت امام حسین(ع) الگوی مبارزه با ظلم است و این ارزش‌ها را در ساختن شهری عادلانه‌تر دنبال می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/663387" target="_blank">📅 10:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=BnAnLIdPKdvNphaJqzpuXbMy2zUKwnoA3BpV6AsRkaiCproJlCH9q17Vo_B36Pp2BM_01kfKqIr7hrwO9mGDIVWf3hjEI1BzIvvpQ3gwe3T0SF8JxDD5lskMnKLkZScKK5u4N4CXB0mWFN-Yscx6Ydo42tzy-3EKGjiKvsodXaFhFHdG-0CchwJXbYG4JVNLaTNhIFP-3-oKszc5jZa8dzneeluYQrcGNfV8SOo-cXXTGtGDIxULBwjVxsxJpL0F_QPSA0Qa7yF8qvwThpCqUd7Z33WvR6zsMzQ6bnTo70mDJPCUMSUxRGqlwSdHSy_vW9orL-D2U_xuLye4Gt1UwYClO8gLVes4yXkN4oyZv-o_g-D5SbqTyewJ3MADnGpgPgsv_lRuy89-MbBvevKV_B2VGp6riO5f55a-RHXn1YEtLq75nyLjnyFsCjx9JSm1o8axt3Dv4eWRhGUnuSM-xGS_lunHqmbdXLy9ib9JotQPQLA2-u_vQfQkMJ9KqPBdUe52WsRF6e32QGWk8C2IgBSUn22_BFXdP5aw4wVmUpxd4lg0I641AkOt015ksyju14U2h5MMI9KshlnApZOHzqZ8qnNQxFuVfgfHELhFSJyLHgaF6TACZvZ9v2psJ7dIOY6TW8GtvrR01sIH5Rldunm9JEENSNOrCSSEYDtxywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=BnAnLIdPKdvNphaJqzpuXbMy2zUKwnoA3BpV6AsRkaiCproJlCH9q17Vo_B36Pp2BM_01kfKqIr7hrwO9mGDIVWf3hjEI1BzIvvpQ3gwe3T0SF8JxDD5lskMnKLkZScKK5u4N4CXB0mWFN-Yscx6Ydo42tzy-3EKGjiKvsodXaFhFHdG-0CchwJXbYG4JVNLaTNhIFP-3-oKszc5jZa8dzneeluYQrcGNfV8SOo-cXXTGtGDIxULBwjVxsxJpL0F_QPSA0Qa7yF8qvwThpCqUd7Z33WvR6zsMzQ6bnTo70mDJPCUMSUxRGqlwSdHSy_vW9orL-D2U_xuLye4Gt1UwYClO8gLVes4yXkN4oyZv-o_g-D5SbqTyewJ3MADnGpgPgsv_lRuy89-MbBvevKV_B2VGp6riO5f55a-RHXn1YEtLq75nyLjnyFsCjx9JSm1o8axt3Dv4eWRhGUnuSM-xGS_lunHqmbdXLy9ib9JotQPQLA2-u_vQfQkMJ9KqPBdUe52WsRF6e32QGWk8C2IgBSUn22_BFXdP5aw4wVmUpxd4lg0I641AkOt015ksyju14U2h5MMI9KshlnApZOHzqZ8qnNQxFuVfgfHELhFSJyLHgaF6TACZvZ9v2psJ7dIOY6TW8GtvrR01sIH5Rldunm9JEENSNOrCSSEYDtxywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جزئیات حمله زمینی تروریست‌ها به خاک ایران
🔹
خودروها خریداری شده بود، روی آنها دوشیکا نصب شده بود، به آنها قول داده شده بود به محض اینکه جنگ شروع شود بعد از ۷۲ ساعت وارد خاک ایران شوند و چهار استان ایران را تصرف کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/663386" target="_blank">📅 10:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKenSvo1Ou2fjsfk4bfAWpvCTm3-1Sdr2iRz_pjYUwoGOtredkD5iygBQLbUqblBsBCWCM32d37jIyiLHtMMrQTA3wKy852Imagn9unwmAsRquMVlX0oMwF0jn24TbzHJCeQRFTKqybVYzfuLkUbo9OZ07y8ZZ7n_ZLx3I2BsnS5dlzWQCilg2WvO6rdGqUl8TT1z_x5XTDnzgNrMASpjfNgXNv_muvSTVnYKGtUh00SsE9Q8MSCYeVKjmt0pCykNUKmWjry_EqlxJc0Wdt602jHqAyUJ0H0AgkxzsiOROQNuo04RtiiYoQMEtoFp9Jp4oMMcQDmAtsOoKHwaQ9rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی زیبایی‌نژاد، مدیرکل فرهنگی شهرداری تهران: حسینیه انقلاب در میدان اصلی شهر‎ تهران و در ادامه حضور مردم در میادین،با شروع محرم صحنه ای از شور و شعور حسینی شد که با شعار ‎
#يا_لثارات_الحسین
به مطالبه خونخواهی رهبر عزیزمان پرداخت.
شعار ‎
#یالثارات_الحسین
در ایام محرم و تشییع امام شهید در کنار شعار ‎
#باید_برخاست
محور فعالیت ها می باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663385" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a96TbPIKSGUu_NFt6M_0OD0MNdhsTzTvrEDsShkm-Xa2VFfzZxhbtLlDV-AZFowdcAOZQKy9yGz-o3XR1D4XMeBgXiEn51FsKtRyu6adKXRMg1Uq77_elyJv386znrQMSqdevBqDuDQZNv6eij6neVcX6ARuDn4iujDwntmYJi-qL7JPPKK5fVP2EPUTcUhdbFOFqSzZ2JPVrcXtl0_4TWQIeOAiUdflx052hcDhIb0QBRkDGddvizocFiQlP17ymomNbebs6PD4aUXF4XrZlKn7bv0CGGKgG-BaSHf5daDTQM5R-m2Miiaw6eWa8dzgLsUGXXpe0pjO0CjqV1SdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهنمای طلایی قطره‌های چشمی؛ بدانید چه زمانی از کدام قطره استفاده کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/663384" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
قرارگاه مرکزی خاتم‌الانبیا: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/663383" target="_blank">📅 10:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43843f73b.mp4?token=lHPuSdcUaWLy-awKMFPLXHLq_IOWeVrfibWDXeeB-K91AYju373GsDLRiyyy_MrMFe7PC6BdmpbgrgO0evuRUd-Fabcz4KZG6j_BDjASW7l1NUXReczCzebbUHX_pkO_RZtw9bUSvxQZbfa9tK3hybgOeqogF_xP4ak7BEsJGLBsgcL2mo_4f4Wk70zx16qNQIvxzFPODzCXkwBYI1AJYMMEg7PFr3ObQfFlBusmDi5HBDtJk7mjO8mDbMdtv18FHf0tfwrvXMu2aezteRSQDxmq4juG_jWapeHQXvPYeLwnc9pbwjf6mda0Jk1QgoYWElAgCb9RzgGwcvNlSiq0EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43843f73b.mp4?token=lHPuSdcUaWLy-awKMFPLXHLq_IOWeVrfibWDXeeB-K91AYju373GsDLRiyyy_MrMFe7PC6BdmpbgrgO0evuRUd-Fabcz4KZG6j_BDjASW7l1NUXReczCzebbUHX_pkO_RZtw9bUSvxQZbfa9tK3hybgOeqogF_xP4ak7BEsJGLBsgcL2mo_4f4Wk70zx16qNQIvxzFPODzCXkwBYI1AJYMMEg7PFr3ObQfFlBusmDi5HBDtJk7mjO8mDbMdtv18FHf0tfwrvXMu2aezteRSQDxmq4juG_jWapeHQXvPYeLwnc9pbwjf6mda0Jk1QgoYWElAgCb9RzgGwcvNlSiq0EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اعلام مخالفت ایران با عکس و کنفرانس مشترک در نشست سوئیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663382" target="_blank">📅 10:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwUeZRw3Rbwwf4tJQhm5Vj3Uieex_eHSZITucWX2ETswOnwVad6s_5WOCXk9vov_luKD1xQEJFExFf9H-URZUtXazXLyZXiYgHjMW_RPvBCD2clGSp1V1xHVzRYmyYByyq0YozwLX3_Fk-rSKDzf5fTflxKzEOuPlOh7V07np9P14Q8_00J_bfyHJhw0ffkYJeMD0x2vA4kB4zncqlVtKBLVkV5MOO4YBYWXU-Jw8qhsKEi1YckiJWoOh-ElDvoZD2T1nEvrIafcfVofThlfiCqcyUY8wC1w8d8zPtk1uO7gQ8DT6dFCzkNzCMosyLfVtHwJxLaNiHWmDPV9aDYXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر فوق العاده زیبا از دشت پوشیده از گلهای بنفش گون در دامنه دماوند، امروز
🔹
مجید قهرودی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663381" target="_blank">📅 10:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f558033c8.mp4?token=F_HbMfgG4meL7CQlCdextAxdtDnYR6lTseJaaiUQPN-9jsPj3cMGKXarZa7oOvDkKBT3DquRgLqQTjr6rvFNGtrbxk2hQJh5vE0464Ff_qRoFcnl4yPJY7KifYOO-4XxcxetCqec71DzHrw4cEI3zGevfzn7h3tfNqUw2JqizhA5Ox-NCNX97tQOmv-E1I0kUGMLK-YotEyP6kmOjgGM5m77JcXPI39p_7Gn-KvLJRMs2WPcJ6dhRXdiDRVso2AvdJXeNU9LQmpvpCk7XYBYqSkoeoYf85ASqXmBZVY-cMEFaxbcSAt6JNyhWXJOR_4QaAnlWz6z-K5WejxniLpFWJdL91u9fLtwKZT__GTdiziY0qPSkcr0ONFCNXDi8zPCf99SyuCkdO96WWgPKeWybRIhqEkMryTG4lgmFblppTn4B-j6Tvt9TkaDAoTB4oY_I9COUWFP6b41i8pcLM0mako8YEa4xEndd0cj6qrcr-XCZCuvZrk-dJVO6JG-QKJtwcGUtZrleTa0KdJ68rwsJJU4moR5zRxTqqpGD1tQ4GDcND6fg4aycUaB-auY3sz4L5e9xBfxI7nB9ri09ArqKbHB1GcQimmUTU2gCp3mGpqpVVMp1NFgMp8spK5R79WlqGp6UbnDo7GnVO2h0fbrH94PdZIRSGcyDqcy9QFm1EE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f558033c8.mp4?token=F_HbMfgG4meL7CQlCdextAxdtDnYR6lTseJaaiUQPN-9jsPj3cMGKXarZa7oOvDkKBT3DquRgLqQTjr6rvFNGtrbxk2hQJh5vE0464Ff_qRoFcnl4yPJY7KifYOO-4XxcxetCqec71DzHrw4cEI3zGevfzn7h3tfNqUw2JqizhA5Ox-NCNX97tQOmv-E1I0kUGMLK-YotEyP6kmOjgGM5m77JcXPI39p_7Gn-KvLJRMs2WPcJ6dhRXdiDRVso2AvdJXeNU9LQmpvpCk7XYBYqSkoeoYf85ASqXmBZVY-cMEFaxbcSAt6JNyhWXJOR_4QaAnlWz6z-K5WejxniLpFWJdL91u9fLtwKZT__GTdiziY0qPSkcr0ONFCNXDi8zPCf99SyuCkdO96WWgPKeWybRIhqEkMryTG4lgmFblppTn4B-j6Tvt9TkaDAoTB4oY_I9COUWFP6b41i8pcLM0mako8YEa4xEndd0cj6qrcr-XCZCuvZrk-dJVO6JG-QKJtwcGUtZrleTa0KdJ68rwsJJU4moR5zRxTqqpGD1tQ4GDcND6fg4aycUaB-auY3sz4L5e9xBfxI7nB9ri09ArqKbHB1GcQimmUTU2gCp3mGpqpVVMp1NFgMp8spK5R79WlqGp6UbnDo7GnVO2h0fbrH94PdZIRSGcyDqcy9QFm1EE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری تاسوعای حسینی بر روی قایق‌هایی در دریاچه دال شهر سرینگر کشمیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/663380" target="_blank">📅 10:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663379">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XH-Eth5Odgw3sNOBqEVAG4tjgmj8-gia2bGPXSqtQQ908K4RGTzfFq_ZQm49FZW0bhR7QfFRfLTqdyesQgFhY43CkT7oQkDxNDq-f-lMvqZCNYNUKpEBOzJD7KyK6cL2k7mtHBG_ahFikfB1S5cRFdQF2iqEuDrkBw4JE566e4rRUea7UZ3byNpEKxVXEv8snFNhBTiwhdbQXDTkQxkg3bnM4zAmoKEVD7XmKP9m0yphTXCh8Sw0IKPpPt44679i7Uuj724N2m14uNCqMcovLGNgeCfSP8obCHzQjFgStxvCOCyhd364_4J6hH18HVY69rgezfXPMLGwwoSjlvsO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۶ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/663379" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663378">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
سخنگوی وزارت دفاع: دشمن با روایت‌سازی‌های غلط به دنبال ناامیدی و تفرقه در کشور است
🔹
خطوط قرمز نظام همان شروطی است که رهبر انقلاب اعلام کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/663378" target="_blank">📅 10:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663377">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpIfJv-ZDTYzvW8IhfSqrp56XDBPu7izXaxhBTb6Jhz6F3-JwZ7NHlX6_kOsh2MyAmRtpFEMmdGsz_c07fvbbrPAD4ZVbNLc7Rrmpk_S1Y2r2CDDE4LSH16HVLlD7HeD0ySZ-ZiKYr9A5JdLWM0rQvX8HG_b9lOK2vf1_9-QCUbh-dZ53DlMDr4MDUAorDjlcWWRgNw1oWSyb4tzKymNkHPuNSM08CKJ3IVSriWcufxrWxZavQ7tpY5YG5VEGWCuvq6Um15ifco2Vb6sTrC70r4wD07ZePlgY9hGJVbCTDNdd-TX5vuZyY7_CV6S9bkC09Xhem2pTD46TTnHvBQ6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل دو تمدن باستانی؛
🇮🇷
🇪🇬
پوستر فدراسیون فوتبال برای بازی با مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/663377" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdZHDwcPrDNYCmQl4vVfKVQDWYQsZPPr3Iv9gnNdXCnLn6vTl7TG236poOW8Bg6f4vHHrHB6n85GcVs-z0zMsHBzo4O77acTJpLdISm7UK3japZkk4XhcTF2yAbujDy5WEhIZZ1MBugvCq0sDAGLh8XIKlWdJepFoNhLfrEI8ZMmbdUJSMZBk19VC5If_4sUr3dsmh3_Mot6SKRdThVLaIm_Ay_87E0nTEuZhlnkyE0_VwaKAQtjQijxYeUcfx3AcV40Qe3l_lw76dfIqGCHFM1Yip2kcECQUHSvvOTV8D4v-mZ0Ny8LqhKSdbx7JKDwClSk-oaMFIVouUxHRD40Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDUIv8805mGKa4G70s0SEgGIlclul76kHtMeDV-DKj6v6EJyRc2ZEchT8z3zVjmY57ZrNwGCriOkGGXa0wxfiboLmtS71TosMV-Y9slq26hxO44PnBM-RncMn8b2w3RmiLQCec9zNgxa7kAkOC5VYVpzW77cT0q1NE4aLn1_FhAgPOVLHQdTGjU8Qq8sz_eOmm9pOVmOppskGPPOM0EvE4Wm7Gn_x24b_qd-edCnVglSmU_Kx6Itm7Ob8Q6Rj9Ot0opnhtZEv88KOKuYcHWRcfNfRY7JDZg2Gt-XmgFsdZyzs5ZZnao354TVERgFz0TwZOfopcWRLN88A10BVfKJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNxmI8RsOCOHT1GTfRkpznlsqsbpOglxbFxQ6kISk6WvXWgK9jgIjIy93vbpjPTXT41pqmVEL-feu7TOznymiIE6BYoulObVSvbd2iOX2W8yPgsgAe25n5lZlQOnNCjGi0FRiiGzOt4fPHu6J5qBvgM6CI4pEGFPWxPJl1ZPyjMx-acC9zkTY8dQjnxaLbI8FCKeF-RUfxAua8FKJjYFFGU4hLRZmC9Em6vRlENEi2ElpMjuigQCmUyG3238DkGcaydly_2IYWwsDPPtpd3g0uC241XKZFrNxMjWSpSWWwmzGOtSjw0CMVbu2Zn1tszmSCphomxrobWSiOaFMBwpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLmUHInosEWjGhVFAGAt_EOiG8_wt4sV5chMteaF439oAWzuRReDczckWqnRytgq4lyW1KkLwwh5-HYFJcmslYN5q_pmRWmeYEtTheBqVkgUHNdLCav6L0tjooolqgiG_82TsC2MG2XO-krmHMdfqtc4ZpZjwwMqkR4CeT2YlqMvblYWDBBnHLHhu7pV_hN1UMQiIKha6Mu0YJL_nTPArAOXn4TEttPpAdS2_qGmdXDMo7aRTtVRUyagV6CgOKI6YBS_q9KOAKy6x6W1KGHyvmvdDdfC_WE1RjN1OpARIHzhh4dupZ4pHX1rS535pdCnNSNjxCuDpWiM4rAMNjswCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_ZQsOMWYvVPneKfgrIWlWHUOBhhrKBQs4vHELF4HfTy6O__ej4pxnCeU6-s0xiigJr0MPnMDAbEz6On9MLGC9JTzPC75Bbrbv7QX-QNLjm2K1HI1KYuUIMHfbH9tU-SzC1H6lG7JuSArVB3w-FCGBrUmt8KKPnFfirheAUP72yC50QY334qbfefOKks0YNX96on9pSviCgTNHM_yy_rYt5UHcb3Ckk2zBjLUOndDlI3ScpdVmXdkJ8BZ4JHYuIvgIIpzrhGK2ubUJ_D1Nl-cQjw-gkjs4U4GTrCwvsoowSlIifr8eW9591jnDuO4S1_6htaqnAaONp0HzdZNZw5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcmgIsjCXTWaAfTlj95aF5ioG_3uIq683lY5tLO16cuPlzkW0gXroTp2uKDw_59o4crMPIv2CBH2c9tBw7UPU72EskKFJDx87A8jVkfMaKNA6DTDyGuoFy-hpOQnc49ORW1vCphpVSygKXL7XHlfy1PLXV7BevbdQv4v9WvZgCgtCRmbO8D6BeaJQtA9lzpSDS4X1yfSGD7-IMDyzrjYXz5nXLJOg_QHBw_BqYbZV3RzPNd_M2jY8Uz473e1o1gelrD_DriKF7r1tr-NdPjOJ0jJwjoQlh7R-dFXbK3S8-z6GpVKcC9iqSbRSe_b4X7iST6Kqdx4NlV_mbsl5-FNvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
فقط با یک کنسرو تن ماهی، ۶ غذای فوق‌العاده خوشمزه و فوری درست کن
🐟
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/663371" target="_blank">📅 10:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2OpuwGS7-U8adfe1csumWz7QLyEOSpqyGl2PenUg2bsBuRaghXv9pMDc6G8ezp9UwaD26s5D3gSk8KX6EOCz-oD-JK3PqZKOgMam-nggIaHuUoiPfNzL4JaO_H3EP-wm5u8sVooPCO_TZEwC0LbBhj_Rwq7WVpG95qYsF-DGlUTVKI-mPlvbNzizhzl4zR6WDQLfs5B708SQay0LrswjK0qGtmxCFi4TE15F3X1C8rv3ClB5_5vtP588ukBqr6jkvL-vivOwJGeEIVxqwcMyVFLKMcBOnbo3w8IW6z4BvcB89VqxIMLWnUeo_W0ckoaPFsboBIdzx46rblZqJfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کار ایران سخت‌تر شد؛
آخرین وضعیت بهترین تیم‌های سوم
🔹
با مشخص شدن ۴ سهمیه از ۸ تیم برتر سوم، شرایط ایران سخت شد: با ۲ امتیاز قطعاً حذف است و با ۳ امتیاز هم صعود قطعی نیست (فقط از کره و اسکاتلند جلوتریم). همه چیز به نتیجه بازی با مصر بستگی دارد./ فرهیختگان
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/663370" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI_jcNxHZlpKmViSZwu89OBDjCWjolp2_JV9hen4QRiPf5GkY0gbqv5fZTvBEcpFhmY2bYx00sJ-WqiteI7gQSf-kCb-uaTCw3AYxTtATa8H6DwuDfv-rervd5q8va7mDcN-CylcnQzQMK1r1lwy7loOB2QLlNdZMnkBeH0A5RtEYLOyhf5VydvVf7hRV8QyQ4HfbxTDhCo_IDRk7NJJMGzDiZ4r8aDiXtcIu_DSb_jonBtpwBaKBeJZHCSrwR-YriSMETaIT7of76BFx9NGfnIvdzEEHy49xhqQQaMM2VaDX6J7W2wS7hno5O0zr18udndg_tCxtnFvScVa8eSAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
وال استریت ژورنال: حملات ایران به پایگاه آمریکا در بحرین ۴۰۰ میلیون دلار خسارت زد و آمریکا را به تغییر آرایش نظامی خود در منطقه واداشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/663369" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
تقویت حضور دریایی آمریکا در منطقه آسیا-اقیانوسیه به بهانه مهار چین
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:
🔹
واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/663368" target="_blank">📅 09:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برخورد صاعقه به فواره مشهور لهستان
🔹
فواره معروف در وروتسواف لهستان، پس از برخورد صاعقه قدرتمند در جریان رعد و برق، آسیب قابل توجهی دید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663367" target="_blank">📅 09:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
طلا در آستانه ثبت چهارمین کاهش هفتگی
🔹
طلا تحت تأثیر تقویت دلار و انتظارات افزایش نرخ بهره آمریکا کاهش یافت و در مسیر چهارمین افت هفتگی متوالی قرار گرفت؛ نفت هم با کاهش نگرانی‌های عرضه، روند نزولی مشابهی را تجربه می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/663366" target="_blank">📅 09:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYQdgEl4NC_0vsJ5BdFG8Q4Fl-TPp9zTrCmPgS4uI7kodfUcRbR3XNQyHl79k6p9Pbc0SMD4MhPoeCLokdW3NiieCksHJ04ewcNbblaSixRF1ecINm2gyng6kiRvSNjwYiNMGAM-FBz9L18klHCW75NVtuqskHb_KufjeVNWz9W1oCaMo9vx7QNMjSpvfoYd4m8grQQEN2s1Huhxwc3X2hICB60gFiMFhHv3vdjfIoE9fraNb61A_42U8qwagnicvlvRA07SHqTeLZvUa2CXjhmY-Mo_0O5x7X5LQv3gIvbNHW47GRNOa6eUEabYlgxmNmYk54rpNhMegvkveBUUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همه سردردها مثل هم نیستن
🔹
سردرد همیشه یک دلیل ندارد؛ از استرس و خستگی گرفته تا مشکلات سینوسی و میگرن می‌توانند عامل آن باشند. حتی کم‌آبی بدن هم یکی از علت‌های ساده اما شایع سردرد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/663365" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیل وحشی به اتوبوس نیروهای هوایی در سریلانکا حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/663364" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
رقم کالابرگ چه افرادی بیشتر می‌شود؟
بر اساس گمانه‌زنی‌ها و اظهارات مسئولان:
🔹
افزایش اعتبار کالابرگ هنوز قطعی نشده، اما در صورت اجرا احتمالاً فقط برخی دهک‌ها (احتمالاً دهک‌های پایین‌تر) مشمول افزایش ۲۰ تا ۳۰ درصدی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663363" target="_blank">📅 09:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3rEp4L8Db7Gizcy5S6rmY7lVhsG46o1THnd2EpqgpFbqKrIN2_bLJGAd7AqFfgvCUGX8XTshCyLvVaK_oHKX1GFTLSicgrtsWSrQ7ZoUKft58_L3U--pi6Gk_HZHyAmlVdOy3yN8DQ5KztPD35R_awvH35TkSjBVXb0vHO5o7RH6wqFsWrOAgznwshQgKMLIPPnBe1ByXZdR71Cb-jCipvTLwx2ndvoyrwfU1c3ek4UOQ6uUkW6Txf5kGhzq-Pc789RS7tb2m56y2KGVbESYX9Ha6nBqFZalxrY511cIAPd11Cjs2TKFTh8Ch5G3c7AmS6f6iiUMxPbZe8t1eIibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بازارهای آسیایی در سراشیبی سقوط؛ بیش از یک تریلیون دلار دود شد
🔹
جرقه سقوط با افزایش قیمت محصولات اپل برای جبران هزینه‌های تراشه زده شد و نگرانی‌ها درباره حباب هوش مصنوعی را شعله‌ور کرد.
🔹
کوسپی کره جنوبی: ۸.۲-٪ (۳۴۰ میلیارد دلار)
🔹
نیکی ژاپن: ۴.۵-٪ (۳۵۵ میلیارد دلار)
🔹
شاخص چین: ۲.۱۵-٪ (۲۲۹ میلیارد دلار)
🔹
بورس تایوان: ۳-٪ (۱۲۷ میلیارد دلار)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663362" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE59kcBWxz4yJBmXYG9SN-pPEZTBQCuvQrasiVB7Aq3lFlSRQ_G5khnyPZOb8M9GtnF80eFz7jATHirAK9zYh7a_Y4GG2ZuSu7334OxcXg_d7qeOb-_-idpqlvJHahCdB5VLdSUlcC64U5AkF91mvA19PwK5BjXSK9f1jWK8K0gsJO4Re06KCJ1ICkYv-3ltZlkHY0ujgCfYRhmALPFAN0s1BWxi9ANQJGPgwjb-xW6hzg3LGACNtYAGpk5PwsLAsSJ6LEnsLgFOJhtscFU_0g3YSkhop_FMS0QyvnELOIR19p-X3PhdNDLO04OThFYNCWNhBfyexhl7FAy6kkzJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgQ2VI3w1ouBiILivafDio1DGqmOOcBJJ0wagkVXw2E6hSqHtFVqaVFAcsycqXKam8FY112NOq2vqvnu0hrcDxrbbSSSjnFHoHNQpyJdP1-qRowVG8BqomGAo3o1BLn79sgeBFD0-6StUqE8EtaXafpLKn1xGJa0Qwb6uSD5Se8hoFVm0R6fFYdDfEnki3XsgbwepSOpRzvqa54yEY_SHjSbRnt9vQ54J_BezlY946R5fK3r7k9_RxZwC9QOnCfXR28fCKygbnZEloqwOuRKBvE6QeCt9x1rieXlhFkm3GWhdlRQD1ol4X8A7MCnh2yodYFYEtEGmyGGyiNjbhCn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2GPTx9m85Kv70Dq4iTX81Hfb-YN0WKk7q6QdPJhdRZXTKTCEVmjrIsBYYIS68ZlOj8hvDw09zgubMsP91sMhRsa5rimu7r18W3Hb2DkP5x4RCJnq1yqrPOaRPvGUiipRUfWlvCcLr_nKNQFscBqaU3Tru9Ba9Rl3B4eE8CXs6p1d25ykkIThgA0QOiIuRbZ128lI_B4xgu09GyMr6u0Fvap3EPCmIj20ddzaySgiWH0f2_6fgZ4sG1XfYDhCeWR6GF5GmkYB7eaBReEsA97IYGOYgba4wsXU08IewHi-tVf2_K8cavPlWRH-5qHSNb4Ro9LYi1PXOIKR7rOMj9L_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iio5jXDyyR8Qup4cRbbyVfZEq_XX1KpQS-6PuFh-AnFvoCZmg1s_WLjvkC2RnATETf1QC6xaqu1GwGL0vR2TC9_G278EpVJcMkBr4hmKvm8iGLfmq8v18eSUi6O1YWuyBTjVIn8hQT0GmJucEeEuqhwO3PXWRZM7R7dJwayc5clzjAtD5AOLWmDsUrO6bFT4T2hFrjTUR0e2qn-cy6RhDcp-ZwOlIckSjBXOot6hXRXONj9dOI22qOMsbe839WeIcDr4eMoQBDhjWXy4wu5ON86_HYnnnkKdfKK92GEeaWXzhWoDZrMP-mOyq9tKnREJ56qOWH8hQrUQuTvZZMEE6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید ملی‌پوشان از ورزشگاه لومن فیلد(محل بازی با مصر) در میان استقبال هواداران ایرانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/663358" target="_blank">📅 09:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800f11bc4a.mp4?token=QslSsKgjlGJwMM51vgXkiuc5FNOIWyCfJ1rHxosjKoiH-k864mrXvnTDT1O9NlG1uED3kKVQY8ZmVWSonYl1OXYlGd4uioY6Mv3DYF5VajZCpWlmV-mJTZmuPsxqyB7ZsEheIMVgOr4DiMGBaM6NMXr3LWFg5_FOS2FE69oMOGTomUhMSJhcoCYFMkA-BAB5K59N7raMgAcAr4VRJZXY6ysQHIeICXEfSqjsuWgvaCDoFUz69cDQss520PVJUjVnbnB0DoWxuoCg3PoK8eGJh1CJNYNhdblJWzMLV0muR69aUIhxrfdC0h2HRPs7rc1XS4big9iYQUgoe_eLcIzrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800f11bc4a.mp4?token=QslSsKgjlGJwMM51vgXkiuc5FNOIWyCfJ1rHxosjKoiH-k864mrXvnTDT1O9NlG1uED3kKVQY8ZmVWSonYl1OXYlGd4uioY6Mv3DYF5VajZCpWlmV-mJTZmuPsxqyB7ZsEheIMVgOr4DiMGBaM6NMXr3LWFg5_FOS2FE69oMOGTomUhMSJhcoCYFMkA-BAB5K59N7raMgAcAr4VRJZXY6ysQHIeICXEfSqjsuWgvaCDoFUz69cDQss520PVJUjVnbnB0DoWxuoCg3PoK8eGJh1CJNYNhdblJWzMLV0muR69aUIhxrfdC0h2HRPs7rc1XS4big9iYQUgoe_eLcIzrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل سوم هلند به تونس توسط فن‌هک
⬛️
🇹🇳
1️⃣
🏆
3️⃣
🇳🇱
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/663357" target="_blank">📅 09:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da765a3b1c.mp4?token=FTGJhy5cKrEm2zMRbQJxoGZoy7f-mo8bBZFeJvI67lG05Jg_6v6Br_2fQUEkVblbgJ2uNpQyt1Gj7bgWARX_bbcRjD8fGRTrccsqKiBggoaAXqslsl5CCFjzwG4NouY2s-saY8DcppyE6YMLrikbv-u92DI4Lava6alJotAtshcs6LrjA5FWMNpY1ALUGmqjg3b0-Bhm_qywMiLXTNJHpzZ3hymiQ9yh5Ln39o5a7K-K22LRxdjhtGkVI8A5RR6ZwDHY2nDGTpnBXAUaZ_46MrSLtndgp2yZkacPD6K0AMoCJpO-W9eR8gcSEeuYeduhXRBpPkrDnywF4uL4IjMvhKGSasnDXnkaejJLDyUTqJYGTVI4bWPA2fnH_igIQj3vRNq8lINU455aS1T2OyEsbmTFcUTZastsggtmPO3SKE0_lpuuvv2URyOqHd-5Z2Dl2UBCBHq2Qq6ObAdhOcbN7oFky9fcpJCim65Gp83DmvYnm8ncIRDpwFJ6CobmlCFgXUgwEcAM8fVfrUchRMLMLwraFBj2CGwp6uRsk3INwje6g3biC5Lu8QNTc047lYiMxq2fcrwQEru5CY6k_49kIHVFpRwp04_RTW6XlTre-YbJXuz7pP3llzE4gF9rEo184tkFbEWjLQntaQAD2yMk3IQN06XKtyDIxQFj54JKumE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da765a3b1c.mp4?token=FTGJhy5cKrEm2zMRbQJxoGZoy7f-mo8bBZFeJvI67lG05Jg_6v6Br_2fQUEkVblbgJ2uNpQyt1Gj7bgWARX_bbcRjD8fGRTrccsqKiBggoaAXqslsl5CCFjzwG4NouY2s-saY8DcppyE6YMLrikbv-u92DI4Lava6alJotAtshcs6LrjA5FWMNpY1ALUGmqjg3b0-Bhm_qywMiLXTNJHpzZ3hymiQ9yh5Ln39o5a7K-K22LRxdjhtGkVI8A5RR6ZwDHY2nDGTpnBXAUaZ_46MrSLtndgp2yZkacPD6K0AMoCJpO-W9eR8gcSEeuYeduhXRBpPkrDnywF4uL4IjMvhKGSasnDXnkaejJLDyUTqJYGTVI4bWPA2fnH_igIQj3vRNq8lINU455aS1T2OyEsbmTFcUTZastsggtmPO3SKE0_lpuuvv2URyOqHd-5Z2Dl2UBCBHq2Qq6ObAdhOcbN7oFky9fcpJCim65Gp83DmvYnm8ncIRDpwFJ6CobmlCFgXUgwEcAM8fVfrUchRMLMLwraFBj2CGwp6uRsk3INwje6g3biC5Lu8QNTc047lYiMxq2fcrwQEru5CY6k_49kIHVFpRwp04_RTW6XlTre-YbJXuz7pP3llzE4gF9rEo184tkFbEWjLQntaQAD2yMk3IQN06XKtyDIxQFj54JKumE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تحقیر بی‌سابقه ترامپ در شبکه اسرائیلی
نه هسته‌ای، نه موشکی، نه تنگه هرمز؛ هیچ‌چیز به دست نیاورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663356" target="_blank">📅 09:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdmOPxuJ-J1vozUZvFwq4_I3ljpPeY6PV1hZckHw5f1KpqXMVYOrViXcPOBCZN6398lscIZ834CjggcBFnGjLhRHrUFav-zo8w8grQMOlMSBF3lKerNPQHSr4DgSWrd9s5V4BmgP6L49X9WyV8ThSzV-JPjLHMo4A5kvM3SPnkXAp3SrOzeI64HBWd8jtW8bKlu15qq7l4Gd5XVCNBSzbKpb45i3-qV-YqdugsEpNjH38QJwDL8O_fL079qlpOERlrWhkuD9MLo6pM27DwUzo7h9GrGtnH42h5iCDd-6rNQGYLrIGc6Bnhz7R2on-mZpvezTVl9NBLobk0DGpRMo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubaOvqyWqQq2Wh_w-Cs0JhT4Hd4TjM92B1lEmWud03ipd8FOGIV7vVaZd9Zft-LfHtiNbkK_kXd3aNFfIL5rnoqO9EGs8x-MiVhI0DPwvmDgiAR0gN9TJYWu0Bdub0efb3oJZ8n5ryrmCrk4pMF8yzh5OAOfw1pTH-8ibyE8WU9SfZGlt_Z970u5FypevINb6BtaABVOdIDfHGEfTnbj3Rd_UUzvTMBIdlaBz-NDx0uGYYKqj0cVt_B-fBBCr-V9dLJ0NKHq28gGbClL7r4dffk5UnFMjOclZ2tBC14aQEVo78d-q9JiOt0hsqmKu467_ocqe5ZYWsDO4vO-jKVbCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پوستر باشگاه‌های پرسپولیس و چادرملو برای بازی امروز در تورنمنت ۳جانبه برای تعیین نماینده آسیایی
🔹
این دیدار امروز ساعت ۱۸:۴۵ آغاز می‌گردد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/663354" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b6d420eb9.mp4?token=Wrk-EHP47tX74y317Ji67oeGhR5B8S0eviAI4qCaaIs95UmR8RwMdeTKkRy9-7aPdTur4uab_hUDnIq5gIyicrkSJt0eYXB3hWKw3DDn_nfwFoLaW5a0D0cv8uSPAdYeI_-vb0LtrsYkJsUDhDuVw1L5MuGr4xFan9COGSiaK9C8JPyws2X_zkpghB2w02btSH_Mo8DlqXha0zkrnd3DKM-BhK7zIEIAlrdR3wTsaycu1ro2SM6McFCkIWlrKDzTQlajf2V60gbpSzex8BTHCE5KNUoGNejO6tH-g_QjjSdZvA7E3rqYam9sXKvQv0Sp_s99F8ONPT8nZnlOG88yZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b6d420eb9.mp4?token=Wrk-EHP47tX74y317Ji67oeGhR5B8S0eviAI4qCaaIs95UmR8RwMdeTKkRy9-7aPdTur4uab_hUDnIq5gIyicrkSJt0eYXB3hWKw3DDn_nfwFoLaW5a0D0cv8uSPAdYeI_-vb0LtrsYkJsUDhDuVw1L5MuGr4xFan9COGSiaK9C8JPyws2X_zkpghB2w02btSH_Mo8DlqXha0zkrnd3DKM-BhK7zIEIAlrdR3wTsaycu1ro2SM6McFCkIWlrKDzTQlajf2V60gbpSzex8BTHCE5KNUoGNejO6tH-g_QjjSdZvA7E3rqYam9sXKvQv0Sp_s99F8ONPT8nZnlOG88yZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بارندگی شدید، شهر هوانگشی چین را دچار آب‌گرفتگی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/663353" target="_blank">📅 09:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
تداوم نقض آتش‌بس توسط رژیم صهیونیستی با حمله به جنوب لبنان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/663352" target="_blank">📅 09:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93323a9d2.mp4?token=KjGOIT9uwTBNho8EWgC4Umilcwk_w7b25zxM0JDjw4WiDGkQ2itte8fOl3KigiykONN_hT5bU8KbnN59rwcbeB8K-KHvJGDqPOZwlLsXOvpDPqUwakWAQtlNyaiGMs_oLUnTYIHIoVmy2gY5gvHCWElgGqYw7VQFzU1noAth2IYrmN5e26Idy4hBl31dABnqwVTGuHH1ifWeDaMEDB2MJ04S95rmbH8VIi1C8_wi86nlbBZcOMeHGDIPcKe-gArDnp53RAGkJGjDlN-ikNF0WFXoy9TTKGIg_cFlY24Ti1-2TgxZuD0LWzlSKWMkUAX_Eb8Wdo8l0cn2o98UF4AVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93323a9d2.mp4?token=KjGOIT9uwTBNho8EWgC4Umilcwk_w7b25zxM0JDjw4WiDGkQ2itte8fOl3KigiykONN_hT5bU8KbnN59rwcbeB8K-KHvJGDqPOZwlLsXOvpDPqUwakWAQtlNyaiGMs_oLUnTYIHIoVmy2gY5gvHCWElgGqYw7VQFzU1noAth2IYrmN5e26Idy4hBl31dABnqwVTGuHH1ifWeDaMEDB2MJ04S95rmbH8VIi1C8_wi86nlbBZcOMeHGDIPcKe-gArDnp53RAGkJGjDlN-ikNF0WFXoy9TTKGIg_cFlY24Ti1-2TgxZuD0LWzlSKWMkUAX_Eb8Wdo8l0cn2o98UF4AVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول تونس توسط مستوری
⬛️
🇹🇳
1️⃣
🏆
2️⃣
🇳🇱
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663349" target="_blank">📅 09:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3211ef190.mp4?token=aed7BoHUDhLrGAj1UFWvp5XJpCFxmauZ71EZ4sBGHABPQGQ-RMlnhWm3RlR4SP4xp5VqJ5Ep3Xc1G5PX2mkkvUNbntTLb6OOYXJl6B4Pi3Q8IgHgL5YhXn6PFk9l8U_GkhqgD03xfk3eDVKmYYH5wM6DSOgZroqbtRp59mZp-LAtHdr5Yj8h4kLBYzyvjUtxnqAvTJrrP_CtGsiZGisBbNbFk6WrZdPHFud2vB4J29aMQQITTAKdqdfG1tuMuWUiX-jdVBB6vlL41hQt9VKPtraSW6Zo6F-iv5TY_eHjEjgfhPMrE8dJs8okeHXvvvdOCMzMbWdqalyR7sJO71Vblw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3211ef190.mp4?token=aed7BoHUDhLrGAj1UFWvp5XJpCFxmauZ71EZ4sBGHABPQGQ-RMlnhWm3RlR4SP4xp5VqJ5Ep3Xc1G5PX2mkkvUNbntTLb6OOYXJl6B4Pi3Q8IgHgL5YhXn6PFk9l8U_GkhqgD03xfk3eDVKmYYH5wM6DSOgZroqbtRp59mZp-LAtHdr5Yj8h4kLBYzyvjUtxnqAvTJrrP_CtGsiZGisBbNbFk6WrZdPHFud2vB4J29aMQQITTAKdqdfG1tuMuWUiX-jdVBB6vlL41hQt9VKPtraSW6Zo6F-iv5TY_eHjEjgfhPMrE8dJs8okeHXvvvdOCMzMbWdqalyR7sJO71Vblw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر غریب در دل رویا؛ آلیس در سرزمین عجایب - ۱۹۱۵
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/663348" target="_blank">📅 09:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
گروسی: بر اساس تفاهم ایران و آمریکا، آژانس بر بازرسی تأسیسات هسته‌ای نظارت خواهد کرد / تبادل اولیه با ایران انجام شده
🔹
وزارت خارجه پیشتر: برنامه‌ای برای بازرسی آژانس از تأسیسات آسیب‌دیده نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/663347" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff2Ew7Ug5Jg_gw5-k_ke2ysqzoJ4O6oNrO4F7LIhvRdhy7AFcsIYZ0EP7iPrz0G6o3aLRz0nMISJhfm9BKKvKC-RimXFaIgo84eVvD33kWDdKw9BSnHJcceovtrFe2XTp9aMQmylKdSkSPoHzkdna12L4AgWeR6JTMkq4y1j6rkOodJ2Lzg_YSpq9ZtAPhj0wmkG9ImNaniwazu4a6UENgnnLuROs70T_uWi4HKeEpwKDA3xtEJ8jjMe7wqdjQsHm1I-R4j8wZbxTaQw1jeECi341u19_4nWKdVfpiLamrPnzvcNur_v4hnR2iP_X0D3_MC0vMDDyfUgOs6X2Yhlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر برگزیده رویترز از بازی امریکا و ترکیه
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663346" target="_blank">📅 09:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760af42690.mp4?token=Hp_A6rXWV_Dn_lbOVRe1cwBrSUAF8c1QAdfYVxZEpzBthgQ-xfQB68gfbUqk4iL1w-cWYZGkdi4UujP9RXbPiyux5zDFEHyEfciX-QuRoW3OSlsRb0Q4EkYZ4M87XJgJ9CAMytvQO_roQCdNlWLVr0fRR3dbCtNgQvADCWsdO4P9weRi4nKSNLDSDE_YBY8JpFzia2CviKZnVPhc02wf7laUXDfAQCznaI7WmCQK0hmusjbdbvmfl4Yv6aKKdQFZ9OYKMWphmB4BQqob9Vo8e8HguiPcHBy5YdrnGcgPfnTGCrd8TZMm3vhIXJaOMbGUxy9jHlXyD3aqH-TNJIaNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760af42690.mp4?token=Hp_A6rXWV_Dn_lbOVRe1cwBrSUAF8c1QAdfYVxZEpzBthgQ-xfQB68gfbUqk4iL1w-cWYZGkdi4UujP9RXbPiyux5zDFEHyEfciX-QuRoW3OSlsRb0Q4EkYZ4M87XJgJ9CAMytvQO_roQCdNlWLVr0fRR3dbCtNgQvADCWsdO4P9weRi4nKSNLDSDE_YBY8JpFzia2CviKZnVPhc02wf7laUXDfAQCznaI7WmCQK0hmusjbdbvmfl4Yv6aKKdQFZ9OYKMWphmB4BQqob9Vo8e8HguiPcHBy5YdrnGcgPfnTGCrd8TZMm3vhIXJaOMbGUxy9jHlXyD3aqH-TNJIaNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قلعه نویی: تمام حرکات مصر را زیر نظر داریم/نسبت به بازی قبل آماده تر هستیم
🔹
هدفمان این است که بازی را کنترل کرده و به آنچه مدنظرمان است برسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663345" target="_blank">📅 08:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAV--3Fo0CbEFwuStkYkBxl3wwKfdHfL7BNZ61BfhTCJowX-A6WD7CE7svlXEHyKVAtFEOm7u6CdyowvvVLEddcmEIgEJ3inldhzbn17wgpM5oIX8eU5bedd5LYdJ0ijPccFcRhPgS7lFnCXA_Fgj_i_eYsvBaNeejblRaFo94cPkD8AFdm3nc4Mzrzp7QStelXDmZnX5YxgbDJIdFxg-7I27sbFij_OYpfAvKLiURQ25ChVE39BkrwEHQQRUWqsJJ7Wf07_eqTXrc575Amf8gXbiYqerbsI8xJ0zVDo0eZ0zmn4zV723AroYBFJxcRPJq1P3NUVi2XfvanUuU2dLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر ماشین به شما زد و فرار کرد این کارها را انجام دهید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663344" target="_blank">📅 08:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e4026260.mp4?token=uVtt7z0n1AcgtGvsw7hTK9AOMl12EeQ3tg6O7ewaAqMHvoNtOrvXvQJDp3hsOQogrLRhpaaMYxmtFso4GWZgHXMo1TtfqJ87bY-xCSalU_uPdflGm-KhiaTQON1Ds_q7vCkfL8TdFOFXbCKUhe_ZHgIuy0rT1dvmlWa03jxQdRG9uvmVyCWC-ZEtNnOKkJn59RU4B0hKK5Bci1c2dVet3h4KTq298oxEPleewFH-fuKOZWD7wBQo4UGVE8QztCDpQQdpF7hpRtpg644Mq-n8t5rUVnA_MapPkBjGZCPSsMRRs8tuXauhDEF5xopnYxt25539AGM4yxxmPRPT8e3wkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e4026260.mp4?token=uVtt7z0n1AcgtGvsw7hTK9AOMl12EeQ3tg6O7ewaAqMHvoNtOrvXvQJDp3hsOQogrLRhpaaMYxmtFso4GWZgHXMo1TtfqJ87bY-xCSalU_uPdflGm-KhiaTQON1Ds_q7vCkfL8TdFOFXbCKUhe_ZHgIuy0rT1dvmlWa03jxQdRG9uvmVyCWC-ZEtNnOKkJn59RU4B0hKK5Bci1c2dVet3h4KTq298oxEPleewFH-fuKOZWD7wBQo4UGVE8QztCDpQQdpF7hpRtpg644Mq-n8t5rUVnA_MapPkBjGZCPSsMRRs8tuXauhDEF5xopnYxt25539AGM4yxxmPRPT8e3wkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل دوم هلند به تونس توسط بروبی
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663343" target="_blank">📅 08:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogHX12ws7lStjQ2lARlYOk4OflYmmRphjXj8TPWRr77bSKKFXrrhmVtAh8mxn14bZoOqAsaeEXvbs8tsqMZo7fD4aokTgNHe4l6pjKw5IRdQ44muV0ejJqWGfNmH0qBpiCDaXq381hts3_uDc3LENJglpZOXvwf9lqMzqwNDk9WGOs90EYN2abIPPLuVusyBxb_AylxN9NfXPbmSabmR1ESkvGiNSA5-1ErTqjnBX_VxGsTFWPZoVjZPYy61SmN3Xt2fPe5hqoiJfGUk9WnQsT11_Jr9R2UGxmJ_2HvhxsMDezFbE6ks0pJ19eztgkA7QdvX9nGlOx8xLAUlldzKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصاویر سپهبدان شهید حاج حسین سلامی و غلامعلی رشید در میان خرابه‌های محل شهادت
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/663342" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW4jTV4u0UMp4WH7DMLrproqbRTTQYzM20q7LQWtmRqxy07qx7Stk4_7NqBlD82AObE98Xrd54WfvzWiiplxeUh3LLLI8bLqtvq16E8Ke8LvU13LZiBObBof-G2eXq0EmAe98AT9yMan1ftiKc-pUkyyjlyO2X9fxmwHvemNol1URLMaekjKQON6GkjpQBFIgoa7Wgnby1BmyRt86F7YPmLRn2QopJwDFx3VySlxeI-XHV_5TJCX6dmSUjIdv9H4sSprvRvMYVsuLLsC6TZFpZyWHMeSvaLQlTj7IkZak1wK9Dm7LRWLZvDC-vhY5nO56YQvmRIgTBe1wbFnOhgHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیه بخش رسانه‌ای تیم ملی درباره احتمال ایجاد برخی حواشی در بازی برابر مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/663341" target="_blank">📅 08:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a678551c37.mp4?token=O9hHcEzSsdxvVJGl0e_EyKwCZhUck1tpnKe9Lzn2_OqsbZwbuCBamM-pFsZQX_u-Zls_sScm31AzYfGNfQZieRvLiIiTO4tzhUxkQSCCXHmUxuHX4E_0NQd9PZDFLU9KyIQrbP7-obC-6m6Opvo_gfdGuSe7X4l-jwXPWdTIRJcOc2SJ25syKdZN6-Fyt1DyS9Gi7D-k0stXNfEpYjV6x7byWrHaxpyOvEfkU6FGzJqk1-osP811G-Bd675hBSRdLkxv31XIiSfFWKz7Q7i__vx--5-AprbDtFbkc_zV5d9EmHKpzs4qEClA4jcezqa_vUIRzti37X0o1iFWm2z6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a678551c37.mp4?token=O9hHcEzSsdxvVJGl0e_EyKwCZhUck1tpnKe9Lzn2_OqsbZwbuCBamM-pFsZQX_u-Zls_sScm31AzYfGNfQZieRvLiIiTO4tzhUxkQSCCXHmUxuHX4E_0NQd9PZDFLU9KyIQrbP7-obC-6m6Opvo_gfdGuSe7X4l-jwXPWdTIRJcOc2SJ25syKdZN6-Fyt1DyS9Gi7D-k0stXNfEpYjV6x7byWrHaxpyOvEfkU6FGzJqk1-osP811G-Bd675hBSRdLkxv31XIiSfFWKz7Q7i__vx--5-AprbDtFbkc_zV5d9EmHKpzs4qEClA4jcezqa_vUIRzti37X0o1iFWm2z6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تداوم نقض آتش‌بس توسط رژیم صهیونیستی با حمله به جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/663340" target="_blank">📅 08:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de93bcff08.mp4?token=mbH-1aPgubm-Ipb2YBSzpQDGcdRSZIhCpMZYRpbMnWe763ol5xBqnR1v-AHjWI70dvv0PuTfa209jwV0ZqsbgtKf-4ehBYywOQRCMVS1yNdaSboLAtEPx6rC6Ha-rQ1IvJP0UyiWSBldrdPOx9XopzdPbjHfMmmVGKHpPDxKS8gE7grkFfKCqNgp5YYxaImbSBEnkUwJLPXbpZkqtYZPvOPoSPaycmtY0VXjJ-VsRcvSfbQEXY1qN-0v_EV8xYb-rCTvvdnmNdRo0xw-BLjPlc2Kf_7l6Y6-vewZDUtwPXsbme8e9VIJGHIsULct17R9uFVQF_OzTfhIwJN4sa2baw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de93bcff08.mp4?token=mbH-1aPgubm-Ipb2YBSzpQDGcdRSZIhCpMZYRpbMnWe763ol5xBqnR1v-AHjWI70dvv0PuTfa209jwV0ZqsbgtKf-4ehBYywOQRCMVS1yNdaSboLAtEPx6rC6Ha-rQ1IvJP0UyiWSBldrdPOx9XopzdPbjHfMmmVGKHpPDxKS8gE7grkFfKCqNgp5YYxaImbSBEnkUwJLPXbpZkqtYZPvOPoSPaycmtY0VXjJ-VsRcvSfbQEXY1qN-0v_EV8xYb-rCTvvdnmNdRo0xw-BLjPlc2Kf_7l6Y6-vewZDUtwPXsbme8e9VIJGHIsULct17R9uFVQF_OzTfhIwJN4sa2baw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول هلند به تونس توسط اسخیری (گل‌به‌خودی)
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663339" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fd050189.mp4?token=EPlGDtGUK3dNhQ7krhBDgotuXuXjaeTNAbfiwiNRbrDfxgzJcqoRMRfKpKWZ1qCreDOOIw__dgxw30RLEsAf03U_ZcMD5GFVV9j2hONA9jz-hESnrvMOc7m1th_gG2xOvQXU1izPQgLE3FWjN9VKDRiMxwm3q3maBxHA9gX7ze-db7NPBi6XQtQgvajfvqDbNYqSwFt78dpnupyZKIM7zrphEU1xkuv92QdUYeMsVwKS4vfhxi1NmI7jiFZbGEwALRcsgREAE8iFjLG67OM4-JQkKxrVfbfYdDkhiX6NNm1jwUCsj-qDDB4hd2gbhN_FQBR4DgD2F3ntXb-4BN425Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fd050189.mp4?token=EPlGDtGUK3dNhQ7krhBDgotuXuXjaeTNAbfiwiNRbrDfxgzJcqoRMRfKpKWZ1qCreDOOIw__dgxw30RLEsAf03U_ZcMD5GFVV9j2hONA9jz-hESnrvMOc7m1th_gG2xOvQXU1izPQgLE3FWjN9VKDRiMxwm3q3maBxHA9gX7ze-db7NPBi6XQtQgvajfvqDbNYqSwFt78dpnupyZKIM7zrphEU1xkuv92QdUYeMsVwKS4vfhxi1NmI7jiFZbGEwALRcsgREAE8iFjLG67OM4-JQkKxrVfbfYdDkhiX6NNm1jwUCsj-qDDB4hd2gbhN_FQBR4DgD2F3ntXb-4BN425Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تاکر کارلسون: جنگ ایران، سرآغاز پایان سیاسی ترامپ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/663338" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdT7zy6Dh9psaq44fA96bwojWiTVRPT-pCu6ob3RiZfkZFBqzJv7DztW2ajHXJPBz0MufPwP8KOagyseQ3_smUC50hA9sS7sUJytbpo3rJEA97Go_N44-G3AuEzcDHb54CGjN9NhA2S9nUxXJKX1cfD9PsEi_aeEEISD6j_M4CC15MnbSHAZ9rFtzedW48Cs49AqKTDD_fy3ImFP7z4zbk-pTUwGLHXWt6RdOkDgBy2dC5yKSb0wQeHIRj3lhzoMfKfeBuTngdzwBaOrU485Z8B14wASUPnKIzMKCA48G0ucIAQKYluLbkTk4msAUyURYVY10PNDsG9BJMevOFu1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عراقچی: شهادت سید و سالار شهدای انقلاب اسلامی را نه فراموش می کنیم و نه می‌بخشیم
وزیر خارجه در پیامی به مناسب عاشورای حسینی:
🔹
امام حسین علیه‌السلام سیدالشهدا یا سالار شهیدان شیعیان است چرا که او هر آنچه داشت در دشت کربلا قربانی کرد.
🔹
به همین ترتیب، ما هرگز شهادت آیت‌الله‌العظمی سید علی خامنه‌ای را که سید و سالار شهیدان انقلاب اسلامی ایران است، نه فراموش خواهیم کرد و نه آن را خواهیم بخشید.
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/663337" target="_blank">📅 08:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd2a937f6.mp4?token=W7TFpSfAOsYQhqMp7qFjfy60dxP28fXnHkl2qTcc3Uq09y1eAwBuPvucPI1C1CeL6_X0BgKl_nuNastho05Z8Doy54f03WmfTcmRs7Ppn7rK9nAdDaWFtMz5FEre3pWzIr9rbA4ktcieHOTW8z9ChqHZS-GstEw2An7kw2YGH8FxZDn77P0RX6WajGoucnUA4by_sbWeSLNY-rSBINIwpezVRZCr_zeeNBoxibkVjlO8r5cxB3Ao_zZAp3efbZLvSfT-_2cDXpuiocH3LgeB5SUKobG2BTU5deLXAkoOs7TV6322FLXnNyNM-Pwfboy6FMYTFgHog8g0U5kb-nmh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd2a937f6.mp4?token=W7TFpSfAOsYQhqMp7qFjfy60dxP28fXnHkl2qTcc3Uq09y1eAwBuPvucPI1C1CeL6_X0BgKl_nuNastho05Z8Doy54f03WmfTcmRs7Ppn7rK9nAdDaWFtMz5FEre3pWzIr9rbA4ktcieHOTW8z9ChqHZS-GstEw2An7kw2YGH8FxZDn77P0RX6WajGoucnUA4by_sbWeSLNY-rSBINIwpezVRZCr_zeeNBoxibkVjlO8r5cxB3Ao_zZAp3efbZLvSfT-_2cDXpuiocH3LgeB5SUKobG2BTU5deLXAkoOs7TV6322FLXnNyNM-Pwfboy6FMYTFgHog8g0U5kb-nmh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل دوم اکوادور به آلمان توسط پلاتا
⬛️
🇩🇪
1️⃣
🏆
2️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/663336" target="_blank">📅 08:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e77d85031.mp4?token=BCMscArWTlG_R5fjUal42djxKMbS4THtFY7cyBdPrqo2baDTBfaoslkf_o6z42UjcP6EzmmSf6Ri9IpVob-sl8I84uuf_f9zmR-dlcFh-ZRuL_W6Hp0lagnDBWmhVU-JGnO8CLrZc2f2b1aOZQPBVuJnoTILo45X0bwTrocEvZbDjVrsxGq7lra4I0_CTfx4g3r1p_HeDvFm84y1Z1xkBfg8RECsv6uqhaWKhI0rFTNKG6n177_8nP0dOsw9rT44NnU7kXY0fUSDnnGbRruIQF4z1e_4qe-eBXJ_rPDu1ZTC2khxk9L757EspMjFjA5ea5efNco1S74BAFPCfseCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e77d85031.mp4?token=BCMscArWTlG_R5fjUal42djxKMbS4THtFY7cyBdPrqo2baDTBfaoslkf_o6z42UjcP6EzmmSf6Ri9IpVob-sl8I84uuf_f9zmR-dlcFh-ZRuL_W6Hp0lagnDBWmhVU-JGnO8CLrZc2f2b1aOZQPBVuJnoTILo45X0bwTrocEvZbDjVrsxGq7lra4I0_CTfx4g3r1p_HeDvFm84y1Z1xkBfg8RECsv6uqhaWKhI0rFTNKG6n177_8nP0dOsw9rT44NnU7kXY0fUSDnnGbRruIQF4z1e_4qe-eBXJ_rPDu1ZTC2khxk9L757EspMjFjA5ea5efNco1S74BAFPCfseCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۱۷ زخمی در حادثه زیر گرفتن هواداران فوتبال در مکزیک
🔹
در جریان جشن هواداران تیم ملی مکزیک پس از پیروزی این تیم مقابل جمهوری چک، یک خودرو در شهر کابو سان لوکاس به میان جمعیت رفت و دست‌کم ۱۷ نفر را مجروح کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663334" target="_blank">📅 08:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5eb1e4138.mp4?token=NGqOCMen0ezhZ_1GZa3jCqHNoRfwQrcyrfpQf8y0wPL8lcrl6oE8aB8QlxVFNxvqf8HgstlhOlTJ4VTaswjTjOLoWYtSFWMxv1YfIPxNYGpALs377UoPDLiqco-MWul1Dv5ESDosfvIJ0ytNmsZD4a8912mE7e1HDQKiycJz81YubXzwx6-CO-33fm4nQ6Z2kh9q7tUaBrWKLtYoiH1Q26xemt5n-7l83N_BES8CyRKwDNls2ioid0rc-mQYFXM81k3SlbrW75bI49fM-I1mQY8Be08tyItCNXfafiC1Vn6Nzi80AMqrj_VywPtVF2J8HJYUNwwiXTIhQOsH0J1E-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5eb1e4138.mp4?token=NGqOCMen0ezhZ_1GZa3jCqHNoRfwQrcyrfpQf8y0wPL8lcrl6oE8aB8QlxVFNxvqf8HgstlhOlTJ4VTaswjTjOLoWYtSFWMxv1YfIPxNYGpALs377UoPDLiqco-MWul1Dv5ESDosfvIJ0ytNmsZD4a8912mE7e1HDQKiycJz81YubXzwx6-CO-33fm4nQ6Z2kh9q7tUaBrWKLtYoiH1Q26xemt5n-7l83N_BES8CyRKwDNls2ioid0rc-mQYFXM81k3SlbrW75bI49fM-I1mQY8Be08tyItCNXfafiC1Vn6Nzi80AMqrj_VywPtVF2J8HJYUNwwiXTIhQOsH0J1E-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول اکوادور به آلمان توسط آنگولو
⬛️
🇩🇪
1️⃣
🏆
1️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663333" target="_blank">📅 08:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426b696e9b.mp4?token=rA9jipskQWnFsCcDFVokHIiYzMBRqX9TjMweS2466dJBtIR_30rq_zN2wJCGBCfuLK2BI9dV1Fpf3Xe9blg_mxniEOnCIFvgaRHEtFWL8xK9bTGYdUbgiSgnBOG2sKbT3O3t1rI2MAm5raWLhu4A5_bp5xOYM_VADbwSoB05PqmzhnKfLO-1E5gXvuTcy1n67RnjuFGfWKqavgbO0J-cLR7fmKZnHPFuPl9Qjy_YZq2LRM_DRy6swMT3Jn_I-Ugld0W2DWQJDCpNVdxr0fi7JfH_ioO0iaRdjXcPxCEmLmNha1f1-hQZh4z9UKi6JWEwN8UiB3o6zwLVPxFlo6mdrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426b696e9b.mp4?token=rA9jipskQWnFsCcDFVokHIiYzMBRqX9TjMweS2466dJBtIR_30rq_zN2wJCGBCfuLK2BI9dV1Fpf3Xe9blg_mxniEOnCIFvgaRHEtFWL8xK9bTGYdUbgiSgnBOG2sKbT3O3t1rI2MAm5raWLhu4A5_bp5xOYM_VADbwSoB05PqmzhnKfLO-1E5gXvuTcy1n67RnjuFGfWKqavgbO0J-cLR7fmKZnHPFuPl9Qjy_YZq2LRM_DRy6swMT3Jn_I-Ugld0W2DWQJDCpNVdxr0fi7JfH_ioO0iaRdjXcPxCEmLmNha1f1-hQZh4z9UKi6JWEwN8UiB3o6zwLVPxFlo6mdrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جام جهانی، ستارگان دنیای هالیوود را به استادیوم لس‌آنجلس کشاند
🔹
برد پیت و ادوارد نورتون پس از ۲۷ سال کنار هم نشستند و بازی آمریکا-ترکیه را دیدند، و دی‌کاپریو نیز در جای دیگری از استادیوم بازی را تماشا کرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/663331" target="_blank">📅 08:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=QD5I8rdKk2xpajuCw7ESH8x80EP9iLEg3kqkqV65WTr0GknAIfs24yhpsm-3zO_SSQnE9CiRdMyuYnS7C74O9Aqb9Ms7Xd9MPNJJCa2SKTPtWGS20nX5JgmJEtW5R6-zxTdJGFXJGcEk9n_MVWtlwlXYxqsJN6g7EyH5vxlAfpNQQ3YeJcuwqZvJPQSyvWQd-xh_Q5GkjA0Q2C2GobwLXPve6x_Yf7Lx3sVuixaUTLqbrcLdZRK9qlVan36vmgC9EABguJde75f7VUpeW5S67T2O-AwO9ZSCK2F56AbeJt6Bax3j_UcnCOSMkoOWhe7J1kOakBS1DpIavSQ2rKkPKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=QD5I8rdKk2xpajuCw7ESH8x80EP9iLEg3kqkqV65WTr0GknAIfs24yhpsm-3zO_SSQnE9CiRdMyuYnS7C74O9Aqb9Ms7Xd9MPNJJCa2SKTPtWGS20nX5JgmJEtW5R6-zxTdJGFXJGcEk9n_MVWtlwlXYxqsJN6g7EyH5vxlAfpNQQ3YeJcuwqZvJPQSyvWQd-xh_Q5GkjA0Q2C2GobwLXPve6x_Yf7Lx3sVuixaUTLqbrcLdZRK9qlVan36vmgC9EABguJde75f7VUpeW5S67T2O-AwO9ZSCK2F56AbeJt6Bax3j_UcnCOSMkoOWhe7J1kOakBS1DpIavSQ2rKkPKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
این سگ رباتیک در سرمای کشنده هم متوقف نمی‌شود
شرکت چینی «دیپ رباتیکس» سگ رباتیک جدیدی معرفی کرده که در شرایط سخت عملکرد دارد:
🔹
حرکت در دمای منفی ۳۰ درجه، عبور از رودخانه یخ‌زده (عمق ۸۰ سانتی‌متر)، صعود از شیب ۴۵ درجه، عبور از سنگلاخ و فعالیت در ارتفاع بالای ۵۰۰۰ متر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663330" target="_blank">📅 08:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
پیامک‌ها با بیشترین میزان کلاهبرداری کدام‌اند؟
🔹
در میان پیامک‌ها با بیشترین میزان کلاهبرداری، آنچه بیشتر ممکن است وسوسه کننده باشد، آگهی‌های کاریابی است.
🔹
بیشترین آمار هک پیامک‌ها، پیامک عدلیران، سهام عدالت، سبد خانوار و کالابرگ، ثبت نام کارت سوخت، یارانه، بسته معیشتی دولت و سامانه ثنا، است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/663329" target="_blank">📅 08:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3708aa.mp4?token=PUhgFKurC23tNrI2V0lL7x3QuGBWoY7baaXVEgN0b7LANf2AG28WB-qWASmgIS5v_UwDBCZ092TYjYRrwMYAljrGjNW1JGDVeMLYspJA_tU0IJblg1XVtwhbWjSOI77EvtHIjrZQdPXDYXPDJLV20hm0llKEqpr9ehLuE_xWfLhJQu5mWqmQCRpGlECuv2Zqian7KwCDF90t_togSBV4Erm1rwWWRYJch7xk23vTfTGon8NZONSKs-iYReYyktFb9yMUWgoJpOFubbzpq7J4YaEb3AKVIQsiAE6uc7Jb80KUSbnbc1XBhb7V-SEGAWREVWeW8gWBy4cGrAFBR56hqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3708aa.mp4?token=PUhgFKurC23tNrI2V0lL7x3QuGBWoY7baaXVEgN0b7LANf2AG28WB-qWASmgIS5v_UwDBCZ092TYjYRrwMYAljrGjNW1JGDVeMLYspJA_tU0IJblg1XVtwhbWjSOI77EvtHIjrZQdPXDYXPDJLV20hm0llKEqpr9ehLuE_xWfLhJQu5mWqmQCRpGlECuv2Zqian7KwCDF90t_togSBV4Erm1rwWWRYJch7xk23vTfTGon8NZONSKs-iYReYyktFb9yMUWgoJpOFubbzpq7J4YaEb3AKVIQsiAE6uc7Jb80KUSbnbc1XBhb7V-SEGAWREVWeW8gWBy4cGrAFBR56hqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول آلمان به اکوادور توسط سانه
۲
⬛️
🇩🇪
1️⃣
🏆
0️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/663328" target="_blank">📅 08:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a353cc23.mp4?token=U-v1KNVJpM_uUUsS4P_8yPaJ6tkfyvbZS87R4ebrQu7i10E-Jd8psQt10U94zaWe5sN6bCaFAG6F2UzhnuIkPNnnE5AvNLktJgVyS1cvsyvvmxSNXq4GFgJFZKgO0w9j6W79_BJA2sI8bb5gAAVOJxijFtQTzIM5Kp4wrlBY415fnmkb4Nvl6Lc0dN5MA5TLbs6-mqvORTalBZLQSlVytoV6s-JUAwozHNBMJRLmzofXVDROeMwAgRuh8cK1VUZgpw0-29S8-GYAaAWD2LQk3Ppo1RN7bzZPJlgVjy9yRHz2KZlCfpg_zwNMMs8RjStP_AXJVrOP3_55PI2jyk_zuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a353cc23.mp4?token=U-v1KNVJpM_uUUsS4P_8yPaJ6tkfyvbZS87R4ebrQu7i10E-Jd8psQt10U94zaWe5sN6bCaFAG6F2UzhnuIkPNnnE5AvNLktJgVyS1cvsyvvmxSNXq4GFgJFZKgO0w9j6W79_BJA2sI8bb5gAAVOJxijFtQTzIM5Kp4wrlBY415fnmkb4Nvl6Lc0dN5MA5TLbs6-mqvORTalBZLQSlVytoV6s-JUAwozHNBMJRLmzofXVDROeMwAgRuh8cK1VUZgpw0-29S8-GYAaAWD2LQk3Ppo1RN7bzZPJlgVjy9yRHz2KZlCfpg_zwNMMs8RjStP_AXJVrOP3_55PI2jyk_zuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر انرژی رژیم صهیونیستی، الی کوهن: موضوع خروج از منطقه امنیتی در لبنان در دستور کار نیست
🔹
حتی اگر ترامپ از ما بخواهد که عقب‌نشینی کنیم، به او می‌گوییم: «نه.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663327" target="_blank">📅 08:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
نخست‌وزیر کانادا خواستار بازگشایی سفارت این کشور در تهران شد
🔹
قلعه‌نویی: شرایط بدنی بهتری نسبت به بازی با بلژیک داریم
🔹
مقام صهیونیست: درخواست ترامپ هم مانع حضور ما در جنوب لبنان نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663326" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ede5c1.mp4?token=Jd0nboIG_AhAPLbGe_n_TalWptuM3KMU2F8cw3H7hGbQB0TSIqXBj9lp8FljGNzOWptglYKG2rt2uyZIiD6j4Oz5S12XX7dWRKlgN3DTZKkNFXoEZqNFonLr0_iWWrOpvQ9-ez_K8-795G5vrhDxZFLzlaD99FkZy7PI-Ywk_KSdQQVjrgHfavhIDJLwCYjx0usP65Pjo7U4w1EuPUxzPENKtA8HXsPLh3tA1ac89QdU9miaU5ofZ6KRrUADhhX__1RMFC1MBOUJYUrcLeO62b0uZcaHzoIK075TLCWJblbgomCH9OajNxlHfon7OZkRRWNUGZZ-kvV8kLlNBY53yx-0IdXfmmK9lJ6wN-OFEaYpHXXU4fpv3YB1h-vhjiuS6fHmIpaKwLAf6NDUc6SIX2BavFT-OXBLujGeivtsmYFCNnk53bYzG5J-Jt8Zdrm0koXyRIyMNOHSe1kMNmIp3i3-weUzKXJJm80ar_3xevGOxLd2JBbbaM1WhmSicNWSB-Ab8Scqq3oOO2CwmKb1l2o5cXwyjbn_ANzhnMuxMDmgLvWIYw71l6KnuGaEBg-ObFvAX6NO9rqd0cUS8bbqR_QsEsBGHoRSh54BpSxxb2vLEP5gl9UZxu06Mj2kDUAgjVG49SkT_0weygwNvtj1VY8rJe2GewblWZljCfRuf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ede5c1.mp4?token=Jd0nboIG_AhAPLbGe_n_TalWptuM3KMU2F8cw3H7hGbQB0TSIqXBj9lp8FljGNzOWptglYKG2rt2uyZIiD6j4Oz5S12XX7dWRKlgN3DTZKkNFXoEZqNFonLr0_iWWrOpvQ9-ez_K8-795G5vrhDxZFLzlaD99FkZy7PI-Ywk_KSdQQVjrgHfavhIDJLwCYjx0usP65Pjo7U4w1EuPUxzPENKtA8HXsPLh3tA1ac89QdU9miaU5ofZ6KRrUADhhX__1RMFC1MBOUJYUrcLeO62b0uZcaHzoIK075TLCWJblbgomCH9OajNxlHfon7OZkRRWNUGZZ-kvV8kLlNBY53yx-0IdXfmmK9lJ6wN-OFEaYpHXXU4fpv3YB1h-vhjiuS6fHmIpaKwLAf6NDUc6SIX2BavFT-OXBLujGeivtsmYFCNnk53bYzG5J-Jt8Zdrm0koXyRIyMNOHSe1kMNmIp3i3-weUzKXJJm80ar_3xevGOxLd2JBbbaM1WhmSicNWSB-Ab8Scqq3oOO2CwmKb1l2o5cXwyjbn_ANzhnMuxMDmgLvWIYw71l6KnuGaEBg-ObFvAX6NO9rqd0cUS8bbqR_QsEsBGHoRSh54BpSxxb2vLEP5gl9UZxu06Mj2kDUAgjVG49SkT_0weygwNvtj1VY8rJe2GewblWZljCfRuf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سخنان طوفانی میثم مطیعی در شب عاشورا در دفاع از سپاه پاسداران انقلاب اسلامی و خونخواهی رهبر شهید
#WillPayThePrice
#هزینه_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663325" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
ترامپِ قمارباز: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
رئیس‌جمهوری آمریکا به عنوان دشمنِ اصلی مردم ایران، از ایران به عنوان «بازار جدید» برای محصولات کشاورزی آمریکا نام برد:
🔹
ما یک بازار جدید خواهیم داشت و آن کشور دوست‌داشتنی ایران است. ایران جای زیبایی است. آیا کسی دوست دارد به آنجا برود؟
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663324" target="_blank">📅 08:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a76c28e1f.mp4?token=h4redDS9GOQiEryQGBwzKrPDFbaFU-QPY0Ws25skmHG_dpD3690iqn6Yd_dn_6wKR2CCSPwAqXyBT6IlBaNDvRVcfySBKw1XEjOKx3u23liZvskGZzxEHbD4YNtRIRyIa5JXTioJx7oehyaR31QEU0vOA1RADFuagq4RlgGV26btbOZM_NrR_B0tTrhti75dHOQGEHpxvW-XuqN4DpftA32So7kVJ63h1Cm4AgD2Z67Ff7PkQmiKY8NN7emjvIEJGmSm6wxnHRNxMih27oR5AH5rF9WEPZoc_agJRXUn5t1FN0AMwY6CYCWUvRf_oyv8CyDLs71iGSXpkD5kd1oX_A8iuy_IHl351pv5tezGxCoIIhqL-GeL6Eq2tBMSOn4Bw8R_Owkmply-FDCDdNAq98415EhLjLzBZvmsLwedssZfAO2shOeIwa0bW8JHQofCJbPK1AIf1-JwO6as7BrkMS_GKRCdxzROmTtrrbjt5y_d3nBYGwxw8VB7HSk8Ly_aEje2TIhWU3cdZeMUJ7YoUr9O5bgcFS0XdA-iBnpMTnifjJG-oUkG8qM71ym56gJTSVhx3rSntlml_CTJhflVuz591dc19hR8UEa9j3440Jiai6jXkvMtj_ZLTgpeKHpkwfkg5sfxrbdOYj1b8oiekv-6raQixIZjx287qHSEo2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a76c28e1f.mp4?token=h4redDS9GOQiEryQGBwzKrPDFbaFU-QPY0Ws25skmHG_dpD3690iqn6Yd_dn_6wKR2CCSPwAqXyBT6IlBaNDvRVcfySBKw1XEjOKx3u23liZvskGZzxEHbD4YNtRIRyIa5JXTioJx7oehyaR31QEU0vOA1RADFuagq4RlgGV26btbOZM_NrR_B0tTrhti75dHOQGEHpxvW-XuqN4DpftA32So7kVJ63h1Cm4AgD2Z67Ff7PkQmiKY8NN7emjvIEJGmSm6wxnHRNxMih27oR5AH5rF9WEPZoc_agJRXUn5t1FN0AMwY6CYCWUvRf_oyv8CyDLs71iGSXpkD5kd1oX_A8iuy_IHl351pv5tezGxCoIIhqL-GeL6Eq2tBMSOn4Bw8R_Owkmply-FDCDdNAq98415EhLjLzBZvmsLwedssZfAO2shOeIwa0bW8JHQofCJbPK1AIf1-JwO6as7BrkMS_GKRCdxzROmTtrrbjt5y_d3nBYGwxw8VB7HSk8Ly_aEje2TIhWU3cdZeMUJ7YoUr9O5bgcFS0XdA-iBnpMTnifjJG-oUkG8qM71ym56gJTSVhx3rSntlml_CTJhflVuz591dc19hR8UEa9j3440Jiai6jXkvMtj_ZLTgpeKHpkwfkg5sfxrbdOYj1b8oiekv-6raQixIZjx287qHSEo2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعتراف
ونس: ترامپ خواستار نابودی توان نظامی و هسته‌ای ایران است و ما از مسیر او عقب‌نشینی نمی‌کنیم
معاون ترامپ:
🔹
هدف اصلی، نابودی قدرت متعارف و هسته‌ای ایران است و برخی می‌خواهند این مسیر را تغییر دهند، اما ترامپ بر استفاده از اهرم‌های دیپلماتیک، اقتصادی و نظامی برای پیروزی بزرگ‌تر اصرار دارد. تاکنون پیشرفت داشته‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/663323" target="_blank">📅 08:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
واکنش پزشکیان به شعار «حی علی االاصول»
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/663322" target="_blank">📅 08:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO1SZqYBIMB9mvyYXbE-0Afgx_mdoTHnZpsgJU2_d3LWMokQD3xBeFkfgPWhAbWZSM3KRReuFtsrju2u6JWrX5lOsuIKueBoXxmcE7H91UwGORgBvssBkq5qIqYzH26Cs4DkCXKtqL1X7pypDnneMfR5bKbSkXh4DwjyqqxD6EB-T0Ks-KPY4UrIl8wHEl5tvl7LtejBes5VvNxccsI6JECTOLR4YTAzPXE7tq5vtde3Dqovh_2qdytuqHDTPDSaZSNFmdsEUNR3r6dGHqBWmdGZw5-gqpPVzHnijqM4gb5B2vZF--3bmw2XoGszswXO3452kRC8D4lZmJYpSKOi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۵ تیر ماه
۱۱ محرم ۱۴۴۸
۲۶ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663321" target="_blank">📅 08:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB-DLqyoxjSmhk4qUCx-KDCr86CleHspGnGlQITC4kqnVayka4w5vnkfM4pYf5Qd-5S35XDS9xgs9HhdGHCeiHKJ03zz8b0gFQDQRF6DAzKw3s7gfHIUI2-wUA6iE8Fs24noJGF_oVAhNUKaVLgJPmbCLnQHfJJGXskO-4bE19j80Pkst50c7j_XbK7Q4MgZ7QziUjymUbSeJNO8KDBhNJlKDQEwBcqavqvlpHIQGgE7R4ca8mjOig-Fgf4TvxKl6cd12EVju-cCbGeZ1Aq3AIOvOVnBzhRODq-xtgbwSgVs3sTdRjGHz47UyNeY_r543ACrcv8ZH0qHf5JMeRGTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بسیاری از کسب‌وکارها تصور می‌کنند مشکل از تبلیغات است.
🙂
✔️
برای همین مدام پلتفرم عوض می‌کنند،
✔️
بودجه را افزایش می‌دهند،
✔️
کمپین‌های جدید راه می‌اندازند.
❓
❓
اما سؤال اصلی اینجاست:
اگر تبلیغ شما به آدم اشتباه نمایش داده شود،
📌
بهترین تبلیغ دنیا چه ارزشی دارد؟
🗓
موفقیت تبلیغات از طراحی بنر شروع نمی‌شود.
🌐
از شناخت مخاطب شروع می‌شود.
📊
سن، نیاز، دغدغه، رفتار خرید و مسیر تصمیم‌گیری مشتری...
همه چیز از اینجا آغاز می‌شود.
🔽
🔼
شما برای کسب‌وکار خود پرسونای مشتری تعریف کرده‌اید؟
⬇️
⬇️
⬇️
مشاوره تخصصی تبلیغاتی</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/663320" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لپ‌تاپ استوک وارداتی
-
به قیمت دبی
- مناسب برای کار و تحصیل
- 10 روز ضمانت برگشت کالا
✔️
-  ارسال رایگان به سراسر کشور
🚛
📌
مشاهده محصولات</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/663319" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
هلاکت یک نظامی‌صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی خبر دادند در پی درگیری در منطقه بیت یاحون در جنوب لبنان، یک نظامی‌اسرائیل کشته و تعدادی دیگر زخمی‌شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/663318" target="_blank">📅 00:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx4W7OlsvK-cRlJhWhtqYdUvjBWOukQTltSoOSB_pdExwOsA1ThGI-e-LWrLpcvSKfz95wQD7ottZVXXE_oZUznUMe1kws9jC86nfFmzy_KkY40gKZ_n61MHFN4nSSyi2HfVKrCmTZ5UWf2mkxYaCV41mjhqP2zUOMJXgCbVSImeB7tvEtxbwiBf5dD0hc2guGsl32OpjGWnXJesTW91sE9bMMExA8BFVI3VmcOZwdD9JpwQvWtk9bEPsBTfGzgou6WlFtcz7ntJA1wsOUdqiMy9te4b44cRpdfwzP1EVVjSoEN_YRGjf79Kk7VN_91wUU8e31EAtyiVMZBhw9d03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تاوانِ کارهایت را با عزیزانت خواهی پرداخت...
You will pay for your actions with those you love...
#WillPayThePrice
#هزینه_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/663317" target="_blank">📅 00:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
چرا دانکین دونات هرشب تمام دونات‌های فروش نرفته‌ رو سطل آشغال میندازه؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/663316" target="_blank">📅 00:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهید حاجی‌زاده: قطعهٔ شهدای مدافع حرم صفای دیگری دارد؛ ان‌شاءالله خدا ما را به آن‌ها ملحق کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/663315" target="_blank">📅 00:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQwyCG9KwOo5KZRG5L_sqd6-TLA7P5k9uSAqa1R5zv9B1_dgDcz7tUMvaqQGElbmp6Ik9uaVTR9qNAx_l4EXqciiEC9wxgpwYZYNZP0wMF086gyMyoEanLie6Ha6TvE-zcdZjUKgLoKo4S9_Xyi_a_Q4akS5GYiz2CuFEJsmr3FCRkQe7dGmSKGZf-HMwcQ10nmQeAf7PTiOsNRiU18r8Squ660KrlvQTgV9ZipKAoKZtaxGb4OI8L-cpGtHr2Yv6L5wVup_Jh5adMZX-Atlivntp0fwKrveaxx1gLVxDCSJULTNf2ig-ftRHrjyUjQo5S8bUgZr6vdxLP6Nov8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyErAp9ysG2CuFCFyv4hLIXl1zbkvnq6sIDuhy_QKO7dp92zrZmQCaFV0Ap1Uc4kpWzfEvB2NJZzbZY3Vuy1BEqkU3E1CVuncuUp30l_RC4VqZkN0l3E2WJTEFFNo7nv7zDHmU--9Vif9OAmREgA7xkDZhVPTdBO_yGq9GZwJAP_FfNDO10GE57fp_sRVN4mJdliaQHSTnff1CQfkHR5fNmEuHVimtny038-qf6B15oE9IFBc0BhcAWhXZg5HLJzFH9u1mSR2LTp_S1M2xUCFsf0o5sTCMZIjjM2jPXxNUAB3HP5zkTYamPFp7P1qo5blOz1bAbldhQ2BmUNWlAUnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور محمدجواد ظریف وزیر امورخارجه پیشین در مراسم عزاداری شام غریبان حسینی(ع) در منزل سید صادق خرازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/663313" target="_blank">📅 00:14 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
