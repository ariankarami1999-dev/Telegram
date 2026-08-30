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
<img src="https://cdn4.telesco.pe/file/dEjn1k701NdgYIDlJz2OyyQvSGPgMWeZR00S63XLAgORKvd-i-CEfKtcQ7yDr1hMn4sKFSd1BkIHnEZlKOOpLzKEGsQgFg5rBEshdzLbqrJYoj_IDls6g-b4Rabac6-vWtw7NIe22OApOl0Au14DwtBG-dU-ok3ov7XCRA0yLPKhrQXkYexgbfZw9Kb1Sm_APxegBF6zJ-_hXRaqQi4h9sTsnrin7Cuw9AHkfzRtB71hd54p5qFKywktF5Vue5Liy4_HLnpdak7RbI7-kQA7mjq0XP9Aqh2xru5nTSHnvEMiEsqUItvN8MkQzzhH8bYYOg-jnXdJ9IS39rCWwmqJ8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-88786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇱
هيئة البث الإسرائيلية:
سفن حربية تركية اقتربت من سفن للبحرية الإسرائيلية وحددت لها مسارات بحرية.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/naya_foriraq/88786" target="_blank">📅 21:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a957ad2ca.mp4?token=rXkTGEGViVbEjTE9qfA0HWntD2QyfLapWxUQZ-RCcZCwO-hCXKmVvHSFreEpRR0Rgv4O03-_CyOtxQBBv7lYuf9u1ZSM09YqtfoYKKVgaLd0H9OMd43pOyesuw3ICcGHGaAKsDZ_SOipb1gGfSrtifoqYr0TgXUbPTnRYauzQaQUsBiA7_VfO7660M7tYxoFoPTFL2v9Q0dAAVW3sZCp22VuktLD2Tg0uKIpSMTwKM8Gui7TKFg9s_ZyrD-rwqdAREcVCKONM4aymEclmDFNmQym3ChiiCcsj_i2DV0CI-M8kH4fN83ePuaioPXhUZ9Q_FuawMES_uA2HXAB2AjtxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a957ad2ca.mp4?token=rXkTGEGViVbEjTE9qfA0HWntD2QyfLapWxUQZ-RCcZCwO-hCXKmVvHSFreEpRR0Rgv4O03-_CyOtxQBBv7lYuf9u1ZSM09YqtfoYKKVgaLd0H9OMd43pOyesuw3ICcGHGaAKsDZ_SOipb1gGfSrtifoqYr0TgXUbPTnRYauzQaQUsBiA7_VfO7660M7tYxoFoPTFL2v9Q0dAAVW3sZCp22VuktLD2Tg0uKIpSMTwKM8Gui7TKFg9s_ZyrD-rwqdAREcVCKONM4aymEclmDFNmQym3ChiiCcsj_i2DV0CI-M8kH4fN83ePuaioPXhUZ9Q_FuawMES_uA2HXAB2AjtxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
السيناتور الاميركي تيد كروز:
ما أدعو إليه هو أن يقوم الرئيس ترامب وإدارته بتزويد المتظاهرين بالأسلحة، حتى يتمكن شعب إيران من ذلك، وتزويد الأكراد بالأسلحة، والسماح للمتظاهرين بإسقاط هذا النظام من السلطة، وليس وجود قوات أمريكية على الأرض، بل شعب إيران.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/88785" target="_blank">📅 20:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇳🇪
جنود متمردون في قاعدة نيامي يطلقون النار على مواقع حساسة في عاصمة النيجر والقوات المسلحة تقول انها استعادت السيطرة على اجزاء من العاصمة.</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/naya_foriraq/88784" target="_blank">📅 20:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
🇮🇷
وزير الطاقة الإسرائيلي:
إذا ارتكبت إيران خطأً بمحاولة إحياء برنامجها النووي أو برنامجها للصواريخ الباليستية، حتى لو كان هناك اتفاق مع الولايات المتحدة، فسوف نكون هناك لنردعها.</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/naya_foriraq/88783" target="_blank">📅 20:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLsh5WMLnvHfgnf4d8wrwS-Q2ikSn7o58L9symB6txDykM6yekO2SAL6wjzgMO7DVGEVKyPJFeryrDex_QG7sI2iqQ6griJRrA_1MmDSNJj1qTHuORaz6BmRR5B9iH37tUwBkXTj-MN3E8kOwnnuEMqAOuvAuyqLDdtqStmbeIc1tFfizuIhB4Pi0uWSC1DKvC4oIcFK19u4V9CK3L5zF8O9QWDYt1K_gSjbVadYuOR3lbjFf3d_cUukjhfZiDCmFrfIHc9GGFgvSIYiojOvUKJIm90_4EV7x7dY8o-2XQuWdWlh7FRSjxDYrqnI_eXs8GfLkJPFSko27hldhIS3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلـة نفط تتعرض لصاروخ من الحرس الثوري أثناء محاولة منها لعبور مضيق هرمز، على بُعد 12 ميلًا بحريًا شمال خصب في سلطنة عُمان.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/88782" target="_blank">📅 19:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇦
انفجارات في كييف.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/88781" target="_blank">📅 19:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0c37ed88.mp4?token=B4WhNh1KqcFF4sZ_ST-yPUuwz9BXCajLgHppzGAca1RYCCf0GC0xr5b6m8wZKRIX4irKLN-LnA2fNPMWe4Eck3SKhDbHFAWFhY2mhsFrMwxOc1DMTZsSIckwqpTccuOC4S6cDSEA0ea6HPoZOwVOvnvlOoS3vmrnnRGFa60h606iVw88lA9nnJJk9DNVqxnwQ7mWDQ28GdnBrbh1aLgUpDNgdI0YwmcbntmKMN19VndjHtj2xu_GFdxoWVzKeLk7OAg03d-f-F9fwAVObQzBFL2f_TWph586guwXgMUB1-pYjKKnXylqDyjQ0uZytMNzCnnDQxsxrVtKpVNIx1D6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0c37ed88.mp4?token=B4WhNh1KqcFF4sZ_ST-yPUuwz9BXCajLgHppzGAca1RYCCf0GC0xr5b6m8wZKRIX4irKLN-LnA2fNPMWe4Eck3SKhDbHFAWFhY2mhsFrMwxOc1DMTZsSIckwqpTccuOC4S6cDSEA0ea6HPoZOwVOvnvlOoS3vmrnnRGFa60h606iVw88lA9nnJJk9DNVqxnwQ7mWDQ28GdnBrbh1aLgUpDNgdI0YwmcbntmKMN19VndjHtj2xu_GFdxoWVzKeLk7OAg03d-f-F9fwAVObQzBFL2f_TWph586guwXgMUB1-pYjKKnXylqDyjQ0uZytMNzCnnDQxsxrVtKpVNIx1D6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
في حادثة غريبة في المجر،
أقدم لص على سرقة طائرة مدنية خاصة والتحليق بها في محاولة للفرار ما دفع القوات العسكرية إلى استنفار طائرة حربية لملاحقته قبل أن يهبط بالطائرة اضطرارياً في حقل لزهور عباد الشمس.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88780" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slIBM3X93RHzy3N2afZS0RJqgiomjO6gFjg9-uy95jGRuK8gfdeAom2De2D3wK6WCFNslmNsUgZYuz8Q8F-INBMfhTA_Oda7xhfGhoDUt_VmSCn_qFQhYnPfjaUgf5z5QvuEbNPwsUioOdoLvzUOxb5An6tUu7LDBylYiygTfqbIeII-qk_lL2MJPe7WKsfChfahcQOcoqBz8X4ODaYC1G8lZKN52to3YcWzn4Fy_RAFYJnR9M6WqD1XXPUFoUM_pXpQihDMxjkGtmKPMcD3OleKdlVb_DBT4a-MonkP6MFkcP_R4QLUWbZDtwUWRowDWVmVE4SUUqrITSOqR80Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTvKvQA0ozFQAy2FFUFcUWITwrNUmctDhdJ01TKyx1qiH7FfYsiyp6OZflP2Wg3BfzrrQBZaeifZDdfWAJXrbn-8GcaYn7xAGIQ7RHF87ZKNYH8YBgyjbVQdww3fOLEE6haTxCVeDQ2RgXyWmShLVFrkxAAt4K_iW7u1PkZFCcINnw0--8al2Zu8JbYCfNEQ_LR-EPCzs0tXz-Bhu4WVVyeuec-zTi_Nbg8p46A5huJdjOpUIQsjHY5WxhO3557UqdJN3ETqG_ycQVa9PqAdOZUCnvp7KzABTnyGYkxr6W0B_5iScBvjef3A1f49ulMngoM3ePqD_SqsHKbgOdIvUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇸
رسالة سابقة من الشهيد القائد/ حذيفة الكحلوت إلى إخوانه مجاهدي الإعلام العسكري
.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88778" target="_blank">📅 17:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kanIBQS5tsqcyFN_d5eW58HOdmu7DYAqVtdK8p7CPviXTwlwfxk-5WT2F3g9r7Ubzt3bxejawsc27GBwal6MO1dPS_BBNSlif713I8VkNais8jz8iKoEpQ-KeDcgxUomNBqWOkeMOVoxyJ_tgNss_GF_1lJ-PG5bYyhQbqwxZrHKyFjTIu8yFpdFIw4bBtjgDq6_chAoh-5TMu5UC9IkFWwOBo5S1vlNp2YXfgtlvCkb_bv88gd4wbQzvbngoy9jX1ns5VVt0ojFh2tFnpZcW2ewPMrBIsDrbjBG4Cz_SuPmA5K0hKd5wlHuFO5XPwhsbo9F4BtxeNBBCYzZ5tfp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lliuAe9mxNVY2VEFqjz87qbS7u0VwhtqwijAxl_V594lIkTjvnomvNvd-zrOldgsjCx3ApG_eIHNSWplqLVgQk6yJ54Vn2FE0HNrwsT3D_OZiiAVsFMAoOVPeEQpTmIeTczQmQCDKavzr3_mBGndhoEAAd16LVZ4aN5ZepVMCTaarfZd3PQoiEvE6Z_GomnRTPTOyOFrVDKU1tSfPlS3sWD1f8Bomckwrepl2rzoENiyvMCIqvbV0_D-0iAhI5o0O-rVshhTZ2-eyvXYDSm6EL3NX0cUsjtMZIc75LuzyMNoFnP0O0AjSLg1HdRjOsmCXdMW6SPlhWqU65_oRkvKCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور جديدة للرئيس الشرعي لفنزويلا المختطف نيكولاس مادورو أثناء تواجده في أحد السجون بالولايات المتحدة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88776" target="_blank">📅 17:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في محافظة أربيل شمالي العراق،
أسفرت عن سقوط عدد من القتلى والمصابين.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/88775" target="_blank">📅 17:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88774">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
مشاهد نوعية من استهداف القوات المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88774" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3qtqHgN8Ad02VTFvZ8PNFMV5sZQvv_q93myD5UpHf_VIbQGqEyUFEI2X1MLflB0LYJ-BrIBKC9gveiWfrFi_3xPfq5HQcm6U-nTetmzCwnq1XncO_7fmXTaBY2F9rskRPsaiCr3OFht7M7GyBFqKjWzEcT94GT50lhSsaA7G3GuMXO7mV-itjYvdNPA472xmluqOJjpQaWHFxOJzwGX7rzytKgvSpjeVcN1wawvrl-h-wAsQG-oCpxu5TFkXQkDvqbIhzUkSL5DsXdrTHwDhGEvyLB6cqbauM7agE-zsitkyRwGAaHGBy0XHjRxYQcRchfaHULCOWhGJmGnYCwZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKmcBsAAR4CsKY9fNLw0l5TkggKvPNkHyg0fGpMVSHqBX61zMia6Ju1mSNdDCNeTY-rPxgZ4i9QEbG5g_zm3RJpDGI_FEL-zIYPl4sZhU2LsG_irR0d4A5ueCwSzdfZml7m5905bztPldM5-hSuC3PgK3kiib-l_VNIkceC8jP_z4PsVYbpeIjNt4DiLKmsg89gSm4VeL5hPzrT_hThwf5bs1N9OnS3sdv_cPys4vlFujs5mnITwyWmTT9lH63J-FKv2B0yuBYTkrGj1KvGWOeEhOq6TNoFsrfQ_mku1wmrlstJNjpxY7wiB_I0rr4y-jUA_C8lblGsYGE1vN7afVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njn9PCHYzDYXjtaPWWKX5GDukb7fFHt8noYtVuKbbrmk4iNpfMVSW4bZgZaac1VoY95YQ2eM7bclIpXqfwMNk40NWbHy5UesnNJ8Sul0omx4QDSzFAuV4Zwaxc__aRsopBZgJXBYhjFe6puvTxMz93JQiVC4lo22xIdFyXCzZIUcHjTMjlm0gXRnPla3f8qpEolP3OjFqqyKA5wSFZeWE6zjsPv6z9M_vjDB7axk2KhPF6xXLkOSwNPHoBx1LPwiOlpmupWOlogetqeWI--7rjuhzsIf75poI_ZM-Vb75oR4Panh5Et6rcfcifPEUdwcZEHPRim27wSJeEA7MG-WoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGFSS7XFThHyTMrva9OdcFvnvHRJP11ccmLUe4ZtIyPqKXlUjgUivfAGjrMSlM_gFLV2PZLTUTryly1t9CGxhbQGTekduPqXXoP1I5vAZNVt94kmEdx_vuBZvWqwk5Do2CsSImA09wtKc3hGVyqh1O4Nbbgvftu4Xaco6jNvoYJnTuX3wTDh_YjAj12te0W8KeAhVL-ux0KcdentHpJQTarRVWkQU_cnyCNZviOK4cP3XecbMhqvUZxfVyH2qRxg3JYkm7jsZxApVK7YjA38n_6m6LnJoaWgtyF0k85x6CB4Jr4KAm7X0Atricc73abMK-ud2hlEKkftAl7mN_3Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVS2gMRlHK3O2JCzY-FO8Pka_XLyo6Oz3hPEML-F989gCZewS89sCKuXge4b6v6uARANjutcoU6QD9s6lLan8OdbqoE49_GlBLmdngbrwGHWTiX-1bYQ_oRiIKDMklU7mOvoy1lSrrLRLQs-5ExQavkG7ETZ-nYAFA8aSqdsypEwXbbCbRgfAWqMVlUH2PZQc-Wj1_cr4xK2oC-Oj_joJPSwjaALe5IoaniEc7wGMuDrV1k_jZWhAFdz1Di2tX-95MBERB9Oq34f9ycDijLEeNntLSEkkGl7Q9O2BNsspb9ygmOIAHWfNS6L4s3b5v20bqibxpUohGgGcRqbQPoe3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyiXb0SL5dkGUSwvfAm3UdyD63sOJSVUUI7AjhTcD0sZ1nGLwCdi1ytGm0kusseRDG-ZiV-1qxscZFU87TkVs6HPOtmxeNVcooMlT4_8ePgitvarLGFwKFRD5H5LkvznPzGRn5xbPa4pNoihHFGvt5U1pRDrgrDlIg8pJKKlC83llnfY7YckFsUBDXvJfaV5iV4Lkp7QtgA-VV6Roz7W1cX93HMBz98TMGFp7ypassmTg6u55P1Of4PxmohPnT9mvNE_LgUSLIdOho3m57qCV5Piq6uQPMd7cdx6DZCWuS7lStguiNBNCceZX1dIpeStBBMBP1bPdwraSdKtBnH7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqR_vt4xahw3marOOu-ScwW8iFqE5ZJTPAGFC0Tjq1PwrXI9XpZiBsVOKmTDof-5huugLfM5WEuhdaPGC428nIJN7DRq6UKujmzCC1AyQHCvNembsLiqjLUJtxsK_7HlGTUnSDfZPR2OZuVWTt5kaIBS3fwgNz3h2-SiOrO7o1ydhPthyHphljX4kq5dz93SZLIaIjiUgMvXfiw__ct574DvLlm7NQgoWozOGT8NgSX7SHZrFm0OVFloS5csrCzrrL3mtyU_nZcoHI4Qrb6yx9giZSkccXMwVfNRSWhGX_ojzryKIJn1jZNBUS83VVxCHt5cC3Mo6VkgbovQmFoAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDeHq4zxf6POyGII1I5dwoHvimEgxGUj4ZaQh21HFnp626KxljOFXOcSMpaM_Xq58BziluOy8DXC98KYvEhzuexBn0mGN-2qTMB3rljUYJEVx_71Dq-PAWiM4v51GWOKEqr2Z2igXHka1RCAqy03UVgtXHn3OZNYDtexxsyA-x2Rd_h127Q8SfnMpjeStBX_p9Zk6VM6_G614ldT_eAaVMdAmMCKXvjui4tXfoDmn7vnDNirRNqhx-WKiKSt9Q8fY1iPyU_93b9d2Rf6egiF3ylwk0x2LgWYlz4C1IvNJYc0OdQIBa1_md9YN-48Bf76D32coL1tbpe1hm2r1_C38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8e9LHWUE0qfD2Ku4O5wIi3jEIRe3yRl8NEqV4v2M_gQfhVT4zP_gy-IQ8TkqlM7r35cfGBucojq27xEMm8pLNo5AlzWHOiTxRP3SaG8UYMkyIrEHBtAi4NBsC35z6L0PksDtYktCy4M_UmAL4EuqyDJSnJ9_H3bVXXDQgRshOS8HuaWWPGfuFeFox5J6g3m9ArUp_pntzFu5Rg1RT052QTN4lit6ODHsgM_yQ9HntVORwCKNGtO7lQ0BGUlCSMzKe71er1JZc_6ss7Ud4FuAq8gnON45Tt54jiHzTRcgOjY5YaAPCa7zPIomhF1fQLSEmha5TTweUaHuTcvOtB3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujD6dyBo2IVtYq8wDm_6VAMDf9L_CruxfBCPKrpS7XE1ur7MPD867pqKno7nazDSPNif_P31nhRZ2nDd7L3YW3TTPhghHtdzEcfXB0881E_lTGr57ViHshOPzFbQioXs0K6hRcW7cNhxaiKmXmCmeM1U_J6a8xGVyeVnww7MopC5aSrM-NzXqcKIgmPX2cEaQCdBtmsxKKnbSkARK5MFEO7EOOf-JSQEqxSBit_0ZtvoFmV2GSY0348hw8ZJodqG_IV1ekoKJkT266OVrSU9gvmUaGLrPBCi3yEvDUnZyjx8iZxNoVULF6YRmoVKjCF86mxhoVkM0amJXFyQ2naMjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
صور من استهداف القوات
المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88764" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCukDZzWnc6hHwLQiibBYEd_kbyo_H3svjEWWzqthsiZXo4vDreWtK_Gcj34ODWPine_TSPwVyYr42wzQk-oMjxXBd-dABJYVgKWK2F5ZcV3hWjXLwt87m-wfeCmQ0am7dsOCWyQVJREYG-J3vtwVsVz-hNS3vn49vqnIoogrumY6jjmGZ5qARJXZd8lZ-iOmhv1fYmaoVYtFVu9GMwkwsnZb8II_Uk4CgPrK3e4dz5jw9Un4l5HM4up7dqksHHApwHXcL-Wkwg2pDp85GQhGUcir2ZLoU7Q1vuFmLvDwQKIJsOTJG4_g35lDnEGQpjAAMJkTc6HSbf8q8q9d4-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب منزعج من الاستطلاعات التي يخسر فيها:
الاستطلاعات المزيفة التي تستخدمها وسائل الإعلام المتحيزة لدينا خارجة عن السيطرة، ويجب اتخاذ إجراء بشأنها.
هيئة الاتصالات الفيدرالية ستقوم بحل المشكلة!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/88763" target="_blank">📅 16:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
🇮🇷
تحذر قيادات عسكرية أمريكية وزير الدفاع بيت هيغسيث من أن تمديد الحرب في إيران قد يضع قوات الولايات المتحدة في جميع أنحاء العالم تحت ضغط كبير.
يقول القادة إن أشهر النشر المتواصل قد أدى إلى استنزاف السفن والصواريخ والطائرات بدون طيار وأنظمة الدفاع الجوي، بينما أضعف الاستعداد في أوروبا وآسيا والدفاع عن الوطن.
أعربت البحرية عن اعتراضها الأقوى، قائلة إن العمليات الحالية غير مستدامة وأن حوالي ربع مدمراتها فقط جاهزة للنشر.
وافق قادة الجيش والقوات الجوية على التمديد، لكنهم حذروا من مخاطر كبيرة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88762" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiOvF4rhDAXuhnRa4wt2msHB241qW_XudB06qp3oaW8jSgz94RjPI_BdCM69ZI4IUeXyD_x1bko2HD15c2ySeGPEpsod06IQNGV9wsYilh599P20CWfr1iE0S6K0Q2_MZ1feYzp98m6qCy79LsWMXFUqI0zYuh5xElwXx6M_QM0ORQlDYp8pmBieAObu-TvnmLRfnKGofBw_VpHujfgPZb0aA-vvJmUXfZbXLzSt8828DADOyGZA_BL9hT9NoUtWBjTnx9ZsYupkxJME4bMKU3fxfux6GtlusYoAJUjqQgKjT7EuAKSrsy29f-QDmyvcyEiKl-CktB53NGu0AyY__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/88761" target="_blank">📅 15:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحق وكيل وزارة النفط لشؤون التوزيع عن جريمة تضخم الأموال والكسب غير المشروع
- قرابة (26.5) مليار دينار قيمة الكسب غير المشروع والتضخُّم في أموال المُدان
- إلزام المُدان بتسديد مبلغ(53) مليار دينار يمثل قيمة الكسب غير المشروع والغرامة التي تعادلها</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88760" target="_blank">📅 14:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحقّ النائب السابق طلال الزوبعي عن جريمة تضخُّم الأموال والكسب غير المشروع
- قرابة (35) مليار دينار قيمة الكسب غير المشروع والتضخُّم في أموال المُدان
- الحكم ألزم المُدان بتسديد قرابة (70) مليار دينار ردّاً لقيمة الكسب غير المشروع وغرامةً تعادلها</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88759" target="_blank">📅 14:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ان الأمريكان قد توغلو في كل شيء
عراقي
حتى لا يستغرب بأن يتم وضع والي العراق والشام توم باراك ضمن المناهج الدراسية القادمة ..</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88758" target="_blank">📅 13:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نايا - NAYA
pinned «
ۗ وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنْقَلَبٍ يَنْقَلِبُونَ﴾.
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88757" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ۗ وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنْقَلَبٍ يَنْقَلِبُونَ﴾.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88756" target="_blank">📅 13:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61e9cd2db8.mp4?token=qPwZVg5dunrE6zMrxVyX3Gdbh1xN4DC1pVC5bpThnNAzN3IQm3TiBQaXSzYmziL2xl_2Y6dwcmDpzzd7TulgCmk5Il8wZVz_x3Z04C42-bJdwq_P3huYPrgEhRuLgSQjaR47zU225OPwB-ctlcqyYLK8y5yyttrEEkvJfhb31XfPhcnGXYpNm82UalHVaEBPHXm65KAwf1LWCcP2WHTQ1RQqbU8kcHKM-dM36eMehZGZ5xUr11xQQt72HuG7Q1glQLkGJptGhlI4p6DBril7dTPSJtEecPxOWs5TZ-wq25MDblC4nD3qhpa26LHS0-NCDId2pOl0wrPOB2jBHrIR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61e9cd2db8.mp4?token=qPwZVg5dunrE6zMrxVyX3Gdbh1xN4DC1pVC5bpThnNAzN3IQm3TiBQaXSzYmziL2xl_2Y6dwcmDpzzd7TulgCmk5Il8wZVz_x3Z04C42-bJdwq_P3huYPrgEhRuLgSQjaR47zU225OPwB-ctlcqyYLK8y5yyttrEEkvJfhb31XfPhcnGXYpNm82UalHVaEBPHXm65KAwf1LWCcP2WHTQ1RQqbU8kcHKM-dM36eMehZGZ5xUr11xQQt72HuG7Q1glQLkGJptGhlI4p6DBril7dTPSJtEecPxOWs5TZ-wq25MDblC4nD3qhpa26LHS0-NCDId2pOl0wrPOB2jBHrIR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا:
هبوط طائرتين امريكية في محطة الشاحنات بمطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88755" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqagR6wgIbaRgBeqjcrujDeenkLN-gpaEjqOb6_nmDCAiOzZzL_4H5hU_LFoFa20yqyBSYgYKn3BAvNvyv-cGW3wKZjk9bIaxm3nkSj8fp4xVVpXuHWAT79qp0ByQPzozxjXNbNzJuvQ6MHOOmiXxNKIE24JwjD5yVSjeAmg7aLfftxeB59bJ1licBhZ8HA2XeEEL-yMMNMPWAAhYgo8DdyGcQ1R9HL4FZEMVtzpQVX8OXntxvfXsVSHy-7wfZRCp57_h7yx6BKwAvKeObn7VNVa2Aovc-aYpQnGb5RuuWvwDDMV9sTnQsa-brsG6eMkBMGQ9YDFppf94nKs0Glx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
ترفيهي
🇺🇸
السلطات الأمريكية ترحل المعلق السياسي البريطاني المتطرف ميلو يانوبولو أحد أهم مؤيدي السياسة الامريكية ضد المهاجرين لمخالفته قوانين الإقامة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88754" target="_blank">📅 12:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇱
إعلام العدو:
مراهقان يبلغان من العمر 14 و 16 عامًا من مدينة كريات موتسكين متهمان بالتجسس لصالح إيران مقابل الحصول على أموال.
ومن بين الأنشطة التي قاما بها، تنفيذ مهام تصوير، ورسم كتابات على الجدران، والعمل على تجنيد قاصرين آخرين لتنفيذ مهام لصالح هذا العميل.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88753" target="_blank">📅 12:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
إعلام العدو:
رفضت الولايات المتحدة طلبًا من ولي العهد السعودي الأمير محمد بن سلمان بأن تتولى واشنطن قيادة حملة عسكرية ضد الحوثيين في اليمن.
أفاد مسؤولون أمريكيون أن واشنطن ستدعم عملية سعودية، لكنها لن تقودها، ويرجع ذلك جزئيًا إلى أن القوات اليمنية تستهدف حاليًا سفنًا مرتبطة بالسعودية بدلاً من السفن الأمريكية في البحر الأحمر.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88752" target="_blank">📅 12:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae5dd28e.mp4?token=SN6VNgI-_GUsfpJDDmZvytvinndH2SSdPrEkswHlRObq2hOJbvxq-h_q8uc4aNh5dPqPJBVYfJZkynaQgt242Y1_zdkHWjgdSuXguOkIuK1ogoMrvvyvKIMZojxwYx9L4NhGIylLd3OvnSS3us8TQtX2dHeG6tRgrW4M7LPcchr2AmCCTi0cOo_OyNsJsBkPFV0taeBZHwyiYWFkJOLyXLbEfiTfxTbtwRuwl-n1GjX29nw2sochgv-CUFWSyiaPEq3gmOWU03XQ_fi2F85wCW2zsx3CSghDCssAue8NYUqGqqGYmOnTp3T3yffu9Yyq1YpuXLecAIgSB6TORdiEVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae5dd28e.mp4?token=SN6VNgI-_GUsfpJDDmZvytvinndH2SSdPrEkswHlRObq2hOJbvxq-h_q8uc4aNh5dPqPJBVYfJZkynaQgt242Y1_zdkHWjgdSuXguOkIuK1ogoMrvvyvKIMZojxwYx9L4NhGIylLd3OvnSS3us8TQtX2dHeG6tRgrW4M7LPcchr2AmCCTi0cOo_OyNsJsBkPFV0taeBZHwyiYWFkJOLyXLbEfiTfxTbtwRuwl-n1GjX29nw2sochgv-CUFWSyiaPEq3gmOWU03XQ_fi2F85wCW2zsx3CSghDCssAue8NYUqGqqGYmOnTp3T3yffu9Yyq1YpuXLecAIgSB6TORdiEVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمينة:
ترقبوا الساعة الرابعة عصرا، مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية لتجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88751" target="_blank">📅 12:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f21690e4.mp4?token=NgJFmDwfBi_gw1g4MeMoCUe7r24YNGYOHRMptHcqluf9z7p2wy9-VBjQ2pzXmSuXZNSP3V8pkP6SUfnqj_rrBpclFfoD9A8KvOE6uZrr4eEb3O_44Dr-S_RWWtOPwlpWDVBzztdRLUe0zq28_vWdbo1qdYnoZik--H58dAhqXIYx6Xr8MbZde4aMNjihCqMCavsOp5nz6J53NrVnkYsiQ0AlhEN-Wu_dFfCqog4Vj2YcsL3fmUocRI6gRqf5Se1xvB8PyN1UCwi1pwtKsYgQ6m8uVhyN-4-FUjY_AXl2yzZvF_ERX6fpt4_JvXiNiDRFbRaNH3ZXlAtCNVJPVQpmTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f21690e4.mp4?token=NgJFmDwfBi_gw1g4MeMoCUe7r24YNGYOHRMptHcqluf9z7p2wy9-VBjQ2pzXmSuXZNSP3V8pkP6SUfnqj_rrBpclFfoD9A8KvOE6uZrr4eEb3O_44Dr-S_RWWtOPwlpWDVBzztdRLUe0zq28_vWdbo1qdYnoZik--H58dAhqXIYx6Xr8MbZde4aMNjihCqMCavsOp5nz6J53NrVnkYsiQ0AlhEN-Wu_dFfCqog4Vj2YcsL3fmUocRI6gRqf5Se1xvB8PyN1UCwi1pwtKsYgQ6m8uVhyN-4-FUjY_AXl2yzZvF_ERX6fpt4_JvXiNiDRFbRaNH3ZXlAtCNVJPVQpmTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
طيران مروحي إسرائيلي يحلق في أجواء منطقة مجرى نهر الليطاني - زوطر وينفذ عملية تمشيط.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88750" target="_blank">📅 11:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
إعلام العدو:
سعر اللتر الواحد من الوقود القادم: الأعلى في التاريخ؛ سيرتفع سعر الوقود عند منتصف الليل بين يومي الاثنين والثلاثاء بمقدار 16 أغورة، ليصل إلى 8.25 شيكل للتر الواحد - وهو ما يوازي الرقم القياسي المخيف الذي تم تحقيقه في سبتمبر عام 2012.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88749" target="_blank">📅 11:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يصيب هدفاً في العاصمة الأوكرانية كييف وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88748" target="_blank">📅 11:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606c24273a.mp4?token=B5JA28rZCt99de88ZzLdGs77lbI0EvOhFBq2LzzSNEthaFchVFFAmK8Xm4Y_c9QFZPtBsi34sdoiNK0ujDAy7K4Lo0KuGBrS3epWc9PmaNr-Gnx4Vg5TCjS7xaQIoNMbGTnoLybNohoJbOOZ3irQqg5aB849aUyCD48IiTOLEqWEVUTyRHlM7UwOKRgpkYmhNdZvbSBI2mwd8e9iWkXyjHrfCIf9W85feMPavyYAJ21WDnZz-0HIpxCyYSqhnArc7O35qMlDAn7trFuiF4h6rmvOfyBtwAtqa95NWJzBwednt02Cdx_xnS-pOhMBxsMQT5dZ75T1XhS3WPGaHaNtSII1XAofvd8W_JwyEdPqABlhlgXGcVZTqMxkMfcBRs9fvy0zYs1Q1_SPVuM1GveBqvX8hpdRz41Nj7RAokj-kaki7Lmv-JYaZLqYADMrua7TGeQjR1hwlRm6F1flSQrCCRpeyz4gpFI9W8ZWF_N5tmRh_CHQ9SRKrW4YO2OkcP0TIk3nyNLs9MikCbGEgTiJNf9AnN3o2hUFlEh3aTZVbVI2TsRXCUSrHzdnW8ECj6GIlCe2dDHLfKiMQEHqxNibAl01EypPDJm2XqpCNPy0JAWqliVCXDYxynQ4ZKS6_QofTZ38pBUIa2tbk3iiBtOnZWIDHfRsM1_t7jvwnM5W78o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606c24273a.mp4?token=B5JA28rZCt99de88ZzLdGs77lbI0EvOhFBq2LzzSNEthaFchVFFAmK8Xm4Y_c9QFZPtBsi34sdoiNK0ujDAy7K4Lo0KuGBrS3epWc9PmaNr-Gnx4Vg5TCjS7xaQIoNMbGTnoLybNohoJbOOZ3irQqg5aB849aUyCD48IiTOLEqWEVUTyRHlM7UwOKRgpkYmhNdZvbSBI2mwd8e9iWkXyjHrfCIf9W85feMPavyYAJ21WDnZz-0HIpxCyYSqhnArc7O35qMlDAn7trFuiF4h6rmvOfyBtwAtqa95NWJzBwednt02Cdx_xnS-pOhMBxsMQT5dZ75T1XhS3WPGaHaNtSII1XAofvd8W_JwyEdPqABlhlgXGcVZTqMxkMfcBRs9fvy0zYs1Q1_SPVuM1GveBqvX8hpdRz41Nj7RAokj-kaki7Lmv-JYaZLqYADMrua7TGeQjR1hwlRm6F1flSQrCCRpeyz4gpFI9W8ZWF_N5tmRh_CHQ9SRKrW4YO2OkcP0TIk3nyNLs9MikCbGEgTiJNf9AnN3o2hUFlEh3aTZVbVI2TsRXCUSrHzdnW8ECj6GIlCe2dDHLfKiMQEHqxNibAl01EypPDJm2XqpCNPy0JAWqliVCXDYxynQ4ZKS6_QofTZ38pBUIa2tbk3iiBtOnZWIDHfRsM1_t7jvwnM5W78o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حادث إطلاق نار في حفل بمدينة آراو السويسرية؛ مقتل وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88747" target="_blank">📅 09:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
اليوم، أصبح تحقيق الانتصار النهائي للحق على الباطل أكثر واقعية من أي وقت مضى، والشرط الأول لذلك هو وحدة المسلمين في مواجهة الكفر العالمي.
المقصود من الوحدة هو التركيز على النقاط المشتركة بين المسلمين. يجب على المسلمين أن يجعلوا "أشداء على الكفار، رحماء بينهم" محورًا لفكرهم وكلامهم وأفعالهم.
الأعداء يتربصون بوحدة المسلمين. أي عمل يؤدي إلى الفرقة بين المسلمين يخدم هدف العدو.
هل كانت فلسطين ستكون بِلَا مَأْوَى لو كان المسلمون متحدين؟
يجب على حكام دول المنطقة أن يتعرفوا على العدو الحقيقي وأن يواجهوه.
وهل كانت الدول والشعوب المقيمة على ضفاف الخليج الفارسي ستواجه هذه التهديدات والطمع من قبل العناصر عديمة الهوية والفاسدة التي تحاول التعدي على أراضيها وممتلكاتها من مسافة بعيدة جدًا، لو كانت قد أقامت وحدتها تحت راية الإسلام؟
الطغاة في العالم، وعلى رأسهم أمريكا الإجرامية، قد كشفوا عن الأهداف الاستعمارية البشعة التي كانوا يخفونها.
قادة أمريكا والنظام الصهيوني، أعداء جميع الأمة الإسلامية، بل وحتى قادة هذه الدول. إن استخدامهم للغة البذيئة تجاه بعض قادة الدول الإسلامية لا يزال عالقًا في الذاكرة.
الاتحاد والدفاع المتبادل ضد الكفر والتعاون بين المسلمين، ثلاث خطوات لتحقيق حضارة إسلامية جديدة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88746" target="_blank">📅 08:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي:
وجهنا بتقليص قطع الانترنت لتكون من 6:30 الى 7:05.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88745" target="_blank">📅 02:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d252835d1a.mp4?token=ZXRdydqfV9cYwIRkd1kI7_JUmlBc70At0oTX0nNQDx_tMIgrHWgKm47ObJDDfsfDnsQjxKCfyf53enauDY5XVzLleOK7-4ehZo0HGjeY4mLiVmveMhd-_rY3_JV9opxFO7CCa6WoHFcRgWQgo2SJhh2iZE-MVD6J-oxeKd78R_M0h7fPxdBQStEzz7fRQoiBnuvLxY--eMzD7hYxKEKvmdhgPFMvnJRatRrXbswSTMP2cvD910sQqwDeN8KpLTqUShIJ8raKcVbFw0FCFA04TtdoGOxO2qBcAFZSrWHnH0S85bgTPzG_AlhsYSzzENtOuEIBTKMO82ei8Qwx5zcZNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d252835d1a.mp4?token=ZXRdydqfV9cYwIRkd1kI7_JUmlBc70At0oTX0nNQDx_tMIgrHWgKm47ObJDDfsfDnsQjxKCfyf53enauDY5XVzLleOK7-4ehZo0HGjeY4mLiVmveMhd-_rY3_JV9opxFO7CCa6WoHFcRgWQgo2SJhh2iZE-MVD6J-oxeKd78R_M0h7fPxdBQStEzz7fRQoiBnuvLxY--eMzD7hYxKEKvmdhgPFMvnJRatRrXbswSTMP2cvD910sQqwDeN8KpLTqUShIJ8raKcVbFw0FCFA04TtdoGOxO2qBcAFZSrWHnH0S85bgTPzG_AlhsYSzzENtOuEIBTKMO82ei8Qwx5zcZNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول امطار في محافظة النجف الاشرف العراقية على الرغم من وصول درجة الحرارة الى نصف درجة الغليان.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88744" target="_blank">📅 01:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
العامري
-رئيس الوزراء من المستحيل جدا أن يتخذ قرار الصدام مع المقاومة
-الإخوة في الإطار التنسيقي لهم الإدراك الكامل لخطورة الصدام ولهم الخبرة والحنكة والقدرة في إدارة الأزمات</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88743" target="_blank">📅 00:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇦
صفارات إنذار في كييف و8 مقاطعات أخرى.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88742" target="_blank">📅 00:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
المستشار الأمني لرئيس الوزراء العراقي:
وجود قوات حزب العمال الكردستاني بالأراضي العراقية غير شرعي ونعمل مع الجانب التركي لحل المشكلة، سلاح البيشرمكة ضمن الدستور وسحب السلاح هو لكل ما هو خارج عن الدستور.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88741" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الخزانة الأمريكية تفرض قيوداً مالية صارمة على فروع بنك مصر (ثاني أكبر بنك حكومي مصري) في الإمارات نتيجة التعامل مع إيران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88740" target="_blank">📅 21:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8d72455a.mp4?token=TmwPd6SYGbcm4EKCLev1XtDGi0T9AG1HpSTXwMz3_dzA7di0lryqlVkcufale9wC5TlSfCJ4jHcBrHnI7o3DTCjdgIWilz-byKJEd5orrixKftXRPXsODSMReYA3Zrlvl_HH2-GNReFE8iCFA9Rry_9-zsHcCGoHgjClDvQG1YnkeSCPF0Pl21A8-M4MfZ3yNcA21uMCbWC0eeRwYFPyNEjykh4y2mlGsTj9jCGMS9s5uCmp8kZ0TKJWndXOjle4uwr2ePDTuANCIMPmQvY38I2-K4S82TAwZeKZWG_MnFEX_C_dsOSwHJ5XE3dlm7FbOl7QU8z3e3pnPiHYjETGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8d72455a.mp4?token=TmwPd6SYGbcm4EKCLev1XtDGi0T9AG1HpSTXwMz3_dzA7di0lryqlVkcufale9wC5TlSfCJ4jHcBrHnI7o3DTCjdgIWilz-byKJEd5orrixKftXRPXsODSMReYA3Zrlvl_HH2-GNReFE8iCFA9Rry_9-zsHcCGoHgjClDvQG1YnkeSCPF0Pl21A8-M4MfZ3yNcA21uMCbWC0eeRwYFPyNEjykh4y2mlGsTj9jCGMS9s5uCmp8kZ0TKJWndXOjle4uwr2ePDTuANCIMPmQvY38I2-K4S82TAwZeKZWG_MnFEX_C_dsOSwHJ5XE3dlm7FbOl7QU8z3e3pnPiHYjETGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88739" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88738" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88737" target="_blank">📅 19:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQQQVc-53rEYfXko654C519VuU8ZkEBG8mao0CI5RWMO_IfaTJAuuo95obHdcKdB0jatB5U_NtRfqOmogH_MCq34EJ03plrqeYruQxA9QBxWrAH2wp_4m34TbrEfhJqmsu4epzIst_zOQ2xr5squV5WhNuC9xw5l9D2TAa1SVN3J401WZ4m6sonpS0wSpawPgbYqW2AWUytijjEC8pE4qe2EZ63hic53hieOwymqK3xS43tFieltXCx1n-0n7wt-8t_9mevxTSNneMuTxYxMFTTt5akeS5I0rjjWcw0CtCS9Vbs5vI3FzP3tmbPZEI1pS2ij9u_Gqame6-IIknpT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر
.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88736" target="_blank">📅 19:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUqu-sCJFHn6aqw_WNEzMAvYplbKRve0vw6k81iuT9_F-q2Y7jG_0hvcfEcI9DwMbHuqxQLeF8EeoxORQGDEXEqDkn_4oTCK_SooYslvK5CmlnlLFBppCVIBiqOJVmaC5DJGNq_4TouAC2IM9MMktD7N9GGuPmxkndkf0b0Ajc4oPmprfFTcQ3jK0b8o4kQNSkgVIghPgoVd04S9rW37KlOBXWULmYJJoy50p70mHCg4CvPZ0CRkCh9LasozI5WAfxVbxAG0vSQ29EJA1FnovY7lPScfdS8SgdZeCmC2Xdp_MZs2Pi4bmbl4oETZ-1vV3JRCjjR6gtHj9Vam2AUtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
رئيس مجلس الشورى
محمد باقر قاليباف
ردا على وزير الخزانة الامريكي
:
كاذب كاذب، بنطاله يحترق.
للحصول على أرباح حقيقية، اطلب من موظفك أن يطلع على تقرير موديز الذي يُظهر تكاليف حرب تتجاوز 130 مليار دولار، واسأل موظفًا آخر عن حجم الخسائر التي تكبدتها شركة جين ستريت في بيع النفط على المكشوف لصالحك في جولة واحدة فقط من العقود الآجلة، والتي تجاوزت 130 مليون دولار.
كاذب كاذب، عوائده مشتعلة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88735" target="_blank">📅 19:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15c704d61.mp4?token=VQ1wmDSQwnFnwtRHSKwQ3-3AOIuQDCUAwRipZAKub7FHqk2lQMj4XpFsTSCY3jlGw03sL23SksjWmD9jp8zfOq17vl2rL7LBCIZ63LgKpn6VdWF96GY__tbUw7wF98YMi_twkstf2AJuD6zYYZtrUDdgOUcVdJLG3S0Eszh8kpxBaK8xw1yIQH0PV7UCqrYMQqlNfaXsKZxv7J_Bq0GcBRx30gldfp6Ixoa7AfXsuu5UGOT_Na-4_bjyROk7aMvhf7vz_nQXzmdoFkLHnFfl5WI7zbiKEgd0UGhqi1NDRqoi5A7gNuLBPK6QMlhtrwEZ0heXjbgGDbLmq6DQZp-fPJ04P_n7hySOTIFAUmiudUyMZwOf9j7HeIr2IExqE9HYKtOsMNRdh78xkuHLsGeSxRYsc8HGyyon54d3-NxFknt6Kq_Ez2c1kMQmVhTrR-BtbOlnSlAeFrzbLEzctkyv-wYKEiQQoALXUxWISiUDVvPxJPwPyF_4ia9s0ZuBdJJKCOssc6rd0ZcIgIYETIS0fmY5D_TWDckFpgAxCrQrC6w_3HHiHFP0MNqgbVsWTayJIu-Y7mwOsDhmuPMjcPU1jkjmr4aTHnZ6F-1cvs2hrT9hDq4j4840TxUl0_QK5hy3brdrnPvJiIlTjEvuXtyQHHJuBssd4BzXjHv0d230cgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15c704d61.mp4?token=VQ1wmDSQwnFnwtRHSKwQ3-3AOIuQDCUAwRipZAKub7FHqk2lQMj4XpFsTSCY3jlGw03sL23SksjWmD9jp8zfOq17vl2rL7LBCIZ63LgKpn6VdWF96GY__tbUw7wF98YMi_twkstf2AJuD6zYYZtrUDdgOUcVdJLG3S0Eszh8kpxBaK8xw1yIQH0PV7UCqrYMQqlNfaXsKZxv7J_Bq0GcBRx30gldfp6Ixoa7AfXsuu5UGOT_Na-4_bjyROk7aMvhf7vz_nQXzmdoFkLHnFfl5WI7zbiKEgd0UGhqi1NDRqoi5A7gNuLBPK6QMlhtrwEZ0heXjbgGDbLmq6DQZp-fPJ04P_n7hySOTIFAUmiudUyMZwOf9j7HeIr2IExqE9HYKtOsMNRdh78xkuHLsGeSxRYsc8HGyyon54d3-NxFknt6Kq_Ez2c1kMQmVhTrR-BtbOlnSlAeFrzbLEzctkyv-wYKEiQQoALXUxWISiUDVvPxJPwPyF_4ia9s0ZuBdJJKCOssc6rd0ZcIgIYETIS0fmY5D_TWDckFpgAxCrQrC6w_3HHiHFP0MNqgbVsWTayJIu-Y7mwOsDhmuPMjcPU1jkjmr4aTHnZ6F-1cvs2hrT9hDq4j4840TxUl0_QK5hy3brdrnPvJiIlTjEvuXtyQHHJuBssd4BzXjHv0d230cgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد تعرض لأول مرة للقائد الجهادي الكبير الشهيد ابو باقر الساعدي "رضوان الله عليه".</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88734" target="_blank">📅 18:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#متداول
🇮🇶
فيديو قديم للقاتل محمد الطائي والعميد الشهيد هشام خلال حديث سابق بينهم لازالة التجاوزات في منطقة الدورة ضمن العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88733" target="_blank">📅 17:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارة التربية العراقية تغلق 158 مؤسسة تعليمية غير مجازة بالتعاون مع الأمن الوطني</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88732" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw6VxcnylRR1rur0_2Cn1a3xyYhXQBhynxKtEDontItAIDBDmGw84bZ5HDqOGBmSSeCBC-PXs4uh8u-qoBwfUzizSPDEW4HVAovIj8lmlzI3LRYK5FKK8wblZKj55X95lewoh--TeG-keFzouQjhhF_UEXEzvUixZPFvvXmA_MujRnIb7KQ0wf0-CSGz_UygXxJha1bwb4QQuLJ7Z1Nt8omxSsDPtepAo2ZJzR2NVELXsjQmByLIPCI-Pzq9ukxMT9FRteAzAsoqf_7vfJgEGEQcysE09hwrqDxvyyemkETTd3BEEdcMl8z1WK-IWtRGxMUQvGjTMVF6CEV8_e-HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkgFi07-LYCu5NLCjB-IrAT387X1Bd8ezk3NGKIQft92zDTvHLTzpoGOYtQhVkXml3YON3bguYjOZNrO7WcWQTOB2y8g9aWAM9RpLA4nu5MVh6sV5NvxWqSoA2TZZUpHpUTejr_Y5a01P2Oamcj8lbyUbNE_kr6KFJhuoUtWQ3i3orR94sU0Gle_7s4XCrgPhJEDNujmYM-C7qm6iFbSxe2TBdFBqYWudfAu7hs7KxyQl8IVHKZ4ewBt82ZXCOc_0jbzJ_fZGOLYqC9M0HrnfY1Outr3R2Jt37SLjQwYf5RDdVsayRNC4YYz0VLKjAO6USPTrHi0qqkImxpjifTN9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسم الله الرحمن الرحيم
إِنَّ الَّذِينَ قَالُوا رَبُّنَا اللَّهُ ثُمَّ اسْتَقَامُوا فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
بيان الموقف من ملف سلاح المقاومة الاسلامية كتائب سيد الشهداء
ليكون العراق سيد نفسه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88730" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4172d25c3e.mp4?token=tjE_5OCJxchxeI8hqxVee8IUXv1coFkfksfXI7fatc1G-dbvII5DMlOpg_a-ncv4hsLAGMsUcuQGGrMroipIF0xaCa3uu8wAW36MWH4e8HqO6qh6SNgkjK4cKN8ascVkGfS1uA-AteLMUvVqJKkQwPQs6FTixJNtvfBUSZWDxxw0bl3TVfN2gszqlpmBzcfocB3YTd51OEDSqgONj_Zd658swqDQv_cliATgHLsPuXF4EYDhmzTRFk5l2bRALI5yvjmYt9Krc_N4L-XJ-yeKAdWa7QFqdT_g1fpfFDb1yuvc2Xd186a5Ekgl6zSkk4La0lQbushRgOyXKLWbp319XTxJDpPp9iWdhUNV-QLlTaHW-uMOI99tojuCifjgwxqXLffLeMj6HL7M_L8ht0GOt1vrpB2hvLH0xjw-FFyqSli4O5QnbU-kxh4xbscqLUhIlux-gZYAXSbJsJiWdU014huuOC6JPTpWATzrafR_o_s6Q16Q0agYaKvZBlPYn9X4CtKxdNPsTrPGjyQ-U1PvNTMTYkMmC8jJ-xrse4JkvUeP69PZi-0uqwvU72ihzMCvEtppkS8TNmJVVr_0r3YLhHb702VU6GdG-7cllrTqYzMImzbqwilxRxVLG3f8nANcY-zirUfquoOIC6nyCAH3DZ-XP1DLPEklRTkR01wSSFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4172d25c3e.mp4?token=tjE_5OCJxchxeI8hqxVee8IUXv1coFkfksfXI7fatc1G-dbvII5DMlOpg_a-ncv4hsLAGMsUcuQGGrMroipIF0xaCa3uu8wAW36MWH4e8HqO6qh6SNgkjK4cKN8ascVkGfS1uA-AteLMUvVqJKkQwPQs6FTixJNtvfBUSZWDxxw0bl3TVfN2gszqlpmBzcfocB3YTd51OEDSqgONj_Zd658swqDQv_cliATgHLsPuXF4EYDhmzTRFk5l2bRALI5yvjmYt9Krc_N4L-XJ-yeKAdWa7QFqdT_g1fpfFDb1yuvc2Xd186a5Ekgl6zSkk4La0lQbushRgOyXKLWbp319XTxJDpPp9iWdhUNV-QLlTaHW-uMOI99tojuCifjgwxqXLffLeMj6HL7M_L8ht0GOt1vrpB2hvLH0xjw-FFyqSli4O5QnbU-kxh4xbscqLUhIlux-gZYAXSbJsJiWdU014huuOC6JPTpWATzrafR_o_s6Q16Q0agYaKvZBlPYn9X4CtKxdNPsTrPGjyQ-U1PvNTMTYkMmC8jJ-xrse4JkvUeP69PZi-0uqwvU72ihzMCvEtppkS8TNmJVVr_0r3YLhHb702VU6GdG-7cllrTqYzMImzbqwilxRxVLG3f8nANcY-zirUfquoOIC6nyCAH3DZ-XP1DLPEklRTkR01wSSFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول امطار في محافظة النجف الاشرف العراقية على الرغم من وصول درجة الحرارة الى نصف درجة الغليان.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88729" target="_blank">📅 16:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc68bb52b.mp4?token=oYXcP5zDHzdzYDXpm9RkPG5LSBGmA_5Av9lVrNy8QzeknEHDsnms8Ff9PRFQGkp4C1pq0ngBUz6gtt8sDJAdRNI0VIvaGKpkLJnFHo3OL1B5CetRh3ge80nLxpsyxzBcEXdSSwYNkBrIRo5Ze_yb0UlZjr4UDQietlWA9JnFWJB_c_RPU7g4ym7Vz3AuWhPy84n624rCr76b_BZKyPsdJcrkUo7DEjab5X2xdPTRiCzsp2qAHONMOdAi8dm5Cge9ey294fnAU_zd16ORWBz2frhy-MlsJElh--WkK9lZlezDvj9WL9u7lDaspoxzj_vBv9Y4xGcXz9xTNvGIi2nmb0BcHExgQP6KNaz_2TnZ03B-n9xz8MhNr6kkXhy-BihOPLVWOZEj3IvAQ8r5t_UkxpI6OubQj2ixT6NL24TzFEdZOqEiCuZJD0Cr7AX4I9UBHYxE2FgQ8FIMcUcoKbVw4N_WA9KzAA8NBj0HbuNOzAbw5urIw96YnPTpsz_TtcUwhfMxi7beJA0pZBQseTrzI7ImKGctp7msGoepqGkUN6s5-upzu8ExY1WeZ0C6bsE0j7I-TNjCpakix-mcckBpmD64zo4TW77ssqs5mrSJC-SFVRufN2R0en5LpH2I6jEMq6Fi-VfIQh2lwuP_4YOzdTPE37d01ce2_jZkJsxHhh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc68bb52b.mp4?token=oYXcP5zDHzdzYDXpm9RkPG5LSBGmA_5Av9lVrNy8QzeknEHDsnms8Ff9PRFQGkp4C1pq0ngBUz6gtt8sDJAdRNI0VIvaGKpkLJnFHo3OL1B5CetRh3ge80nLxpsyxzBcEXdSSwYNkBrIRo5Ze_yb0UlZjr4UDQietlWA9JnFWJB_c_RPU7g4ym7Vz3AuWhPy84n624rCr76b_BZKyPsdJcrkUo7DEjab5X2xdPTRiCzsp2qAHONMOdAi8dm5Cge9ey294fnAU_zd16ORWBz2frhy-MlsJElh--WkK9lZlezDvj9WL9u7lDaspoxzj_vBv9Y4xGcXz9xTNvGIi2nmb0BcHExgQP6KNaz_2TnZ03B-n9xz8MhNr6kkXhy-BihOPLVWOZEj3IvAQ8r5t_UkxpI6OubQj2ixT6NL24TzFEdZOqEiCuZJD0Cr7AX4I9UBHYxE2FgQ8FIMcUcoKbVw4N_WA9KzAA8NBj0HbuNOzAbw5urIw96YnPTpsz_TtcUwhfMxi7beJA0pZBQseTrzI7ImKGctp7msGoepqGkUN6s5-upzu8ExY1WeZ0C6bsE0j7I-TNjCpakix-mcckBpmD64zo4TW77ssqs5mrSJC-SFVRufN2R0en5LpH2I6jEMq6Fi-VfIQh2lwuP_4YOzdTPE37d01ce2_jZkJsxHhh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق يلتهم محطة وقود بالكامل في محافظة دهوك ضمن اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88728" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzpPrGpMrZZKIouYMOcvb9-JuA9PwlO9MhdOwDKmnKopYwWv3-CfSVMzWeViZO2DEvKhHfo-iJNfnOIgH45kYakQ5FM3cHrh3SlilN6U6pq4JS-BKb8GMzjXV3LnrGbuXOtg308n76yWQCHEzUUEH4kAjj0mxzI28daIErPmg1PKervJ_qWgtBXKGhGWB945gSa_tvlAf74nSgt7wk1Q3Bn9IYXhW4dgeIgpvIoJcjq7l4JjP_3GYOmahDJ3qtdTvMYTcC-gw2b_3TwW4k5tLVZ4Qq8JmQQPRzGV4LXiGtsCUZcU-hWGQDYr4iTPxgNn9cQJKvqv1KPZJRegUTy38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
قاتل العميد بحادث الدورة قبض عليه في دار شخص مطلوب وفق المادة 4 إرهاب في نينوى</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88727" target="_blank">📅 15:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydfkh-MxOa8V219SUeoQ-mhy5sfQLIMOthGmx4Zk_q3DD5fz9k3VTM_yJea-kKl6NQCM2irg5T0rua-y-zl5sKx1l3Amx-G7iyDqGLtYd_zeeVlHavHnPEg3TDGvElMJCXz5whT20pn-ttzZGpkJRMEO6j_H9j3eLHlGwEBeFl1T4kbhmbFoE7TzVaklzIzsZZUzSaT6c7GwaJeIM6rDyOKMbZvtDVe9TpBD9nwT1wZRI6SeqE-72Q_YbQszuX4Z5vLHhifa7KdJoL0n281K-Er-mL0jDk6JpwU2GiBaBTGQrIxRPbR1UNItyXaVkrKJQDPU6_0PB10AnXJ-Iic18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
تُظهر معلوماتنا الاستخباراتية جهودًا كبيرة للتلاعب بأسواق الطاقة. تستخدم عناصر من الحكومة الأمريكية وسائل الإعلام الساذجة للتأثير على الأسعار لتحقيق مكاسب شخصية وإبقاء الرئيس غارقًا في حرب خاسرة.
كما تُروج جهات فاعلة متحالفة مع إسرائيل للحرب بتقييمات وردية.
يشعر المستهلكون الأمريكيون بالنتيجة النهائية الحقيقية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88726" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇳🇪
جنود متمردون في قاعدة نيامي يطلقون النار على مواقع حساسة في عاصمة النيجر والقوات المسلحة تقول انها استعادت السيطرة على اجزاء من العاصمة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88725" target="_blank">📅 14:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي: تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88724" target="_blank">📅 14:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=hkPJOGMfgOrZqBtaLf8aDEOMXSfT4bQHZw0je4WjQ1_C4caYhd12m1FegnbFUF9BhxQhxGFgVeWeZog4Jq0F70GDtZkGxwHzk46KcGZWuzpdxyJpGAKeXmoh6cI-HE47TBjGz2CCInAktiDn9vCdH6RxCTM43d04iyCGhPezaMwa_4_jWGpDuqRly381f8huSSgIN00Kr2ddChGEypz5xcVEMV7teRCmNShp7IwkyzHunh_wTOQsq796hhZ9BAUAvlN89Pqgli6Hw_2aBo7mb-N6ucc31BNVvwa1UfbV_Lc0hhRKLWPXpiVdrcuhdm0z2nPBfPWxg2MPFJ2HRwzsyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=hkPJOGMfgOrZqBtaLf8aDEOMXSfT4bQHZw0je4WjQ1_C4caYhd12m1FegnbFUF9BhxQhxGFgVeWeZog4Jq0F70GDtZkGxwHzk46KcGZWuzpdxyJpGAKeXmoh6cI-HE47TBjGz2CCInAktiDn9vCdH6RxCTM43d04iyCGhPezaMwa_4_jWGpDuqRly381f8huSSgIN00Kr2ddChGEypz5xcVEMV7teRCmNShp7IwkyzHunh_wTOQsq796hhZ9BAUAvlN89Pqgli6Hw_2aBo7mb-N6ucc31BNVvwa1UfbV_Lc0hhRKLWPXpiVdrcuhdm0z2nPBfPWxg2MPFJ2HRwzsyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق يلتهم محطة وقود بالكامل في محافظة دهوك ضمن اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88723" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
إعلام العدو:
محاولة دهس قرب قاعدة عسكرية للتدريب في الأغوار بالضفة والجيش يغلق الموقع.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88721" target="_blank">📅 13:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uV-FYIHasdD6t2ZKcIUcuz68bqfbRmKW8MQRBaqVkhIUB8O9PSrPUWsW-AgAYwZe506Kl8Vz5wiDHNkIZi1JgkkD5vD0C7Te7B8Ly3x0ZLyJegAotP403G-mQo03CF40Y3SlzsBZC-5QTZn2noBbpkaqTurLzj1gaF_cuWwgpc_j6mh0bX0lpPZNBNIntCKQ-8B91EqpWAuOl8U8avO-Aq9cuNf1l-GMpRbw-mxOCHRGUWZg7beigH7MeaXeogwWbmi0TL1k8H8KGF4WLIS-XNjR1Bng28Q1Q_FDvrM1akYqd9ca9G-MS60dUDCeZf-DX0PHJ7ti7yUSnBcF5IZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سفينة تابعة للإمارات حاولت عبور مضيق هرمز من الممر الجنوبي لكنها تخفق في ذلك وتقرر العودة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88720" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني: سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.   في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:   بسم الله الرحمن…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88719" target="_blank">📅 11:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
اكتشاف وتوقيف شحنة أسلحة وذخائر حربية على حدود محافظة كردستان الإيرانية عند الحدود العراقية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88718" target="_blank">📅 11:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4.4 ريختر تضرب قضاء كلار بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88717" target="_blank">📅 10:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=Lpm97UnWlxGsaYLFBNZlm96GpJaJyIdZ2EXJmcwXoYqdmGTOCYBOMcXp5KN8JxB2skMpovSASRXbgyoHzHopxI9XP3gL7AC0_HX-cpADsBAucL6NxVOcqxum8g4KC0oxszEwFtMEJ2SG5knaKpwZZEAX4yftfosY6p3WSz49lPbNoTw3V4GHL4TH9JeOxvv3D0AdsxuybDRq9XgQUDnofAWUiC4MAKSi2_9dVAz_vqiPfdSrlUC6IvgzAIdb6OLzLNsljms_C32gz34v8WFjQ-_zQCv5rKVB02aoc2lA1Odiemt405_D-sLQCkMV99hqP0Q1XMmmYa5bmJ1FEG9SbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=Lpm97UnWlxGsaYLFBNZlm96GpJaJyIdZ2EXJmcwXoYqdmGTOCYBOMcXp5KN8JxB2skMpovSASRXbgyoHzHopxI9XP3gL7AC0_HX-cpADsBAucL6NxVOcqxum8g4KC0oxszEwFtMEJ2SG5knaKpwZZEAX4yftfosY6p3WSz49lPbNoTw3V4GHL4TH9JeOxvv3D0AdsxuybDRq9XgQUDnofAWUiC4MAKSi2_9dVAz_vqiPfdSrlUC6IvgzAIdb6OLzLNsljms_C32gz34v8WFjQ-_zQCv5rKVB02aoc2lA1Odiemt405_D-sLQCkMV99hqP0Q1XMmmYa5bmJ1FEG9SbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يصيب هدفاً في العاصمة الأوكرانية كييف وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88716" target="_blank">📅 10:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة العدل الأمريكية:
تم رفع الفيزا عن مواطنة عراقية " طيف سامي " كانت تعمل وزيرة حصلت جائرة من إدارة بايدن لدعم المرأة ومحاربة الفساد ؛ حكومة ترامب عازمة بمراجعة ملفات الجوائز الممنوحة في زمن بايدن ، تم وضع الوزيرة ضمن الشخصيات الداعمة للارهاب .</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88715" target="_blank">📅 05:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
واشنطن سارعت إلى نقل كميات كبيرة من الذخائر للشرق الأوسط لمواجهة إيران، وترامب قرر تعليق الضربات على إيران في يوليو بالتزامن مع تصاعد المخاوف داخل الإدارة بشأن تراجع مخزونات الدفاع الجوي.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88714" target="_blank">📅 04:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_XwnsSyhAUwMv5Xu3IIjIkJ1Pot9-hk4xfBONQL31THAb9xypqp-XC29Tax0wJ4KWBaRv6yGycxt9surjH-od8xXTWo9768UypArTh2PvcLL92LyYx7_ZVvORigB-sRYpAnUGe35SC5Ekv6ot9V3L8qR4wP0VGaVAgRWkNgATSLCi0KOQfvq4-0yyDpMRzIK3svcpY-XgsxLSCrX9Cbbwab_s1jnGiS36-wQ_CeySAKapDgfXLA054uWYR8fdggNn0GKCjiAmQ-CV7IfCIz_6A1uIU5btvW1xs-7KZg7j5Ooiz238tSsSBAEDUntP5XkLA4MgzkwKCk1bcXw5qVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: أبرمنا للتو صفقة نفطية مع فنزويلا.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/88713" target="_blank">📅 02:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
‏الحرس الثوري يطلق عدة صواريخ باتجاه مضيق هرمز.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/88712" target="_blank">📅 00:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=NeiEk8CISbV2eBP-OpNZ_RTmPX2qop9l5YviCEjIbDjGyUBfTPFPmu-C_5h-DE0NTMLGn_s04del5WmE-vtjhOPy_VJZmBSgEstGwty-KefnKXuwc3dhON9joNak8XLPY4CcL1zU4bgqpjzdHNQYgw9eItukgXPQCZVsZDO6MLUxmVgNqoMOPodp1IUFgTIEF5AJJPaDRIIb36IqemQyePhFN2iH8XmrtvT-HJbMLb6akYg23R2d0XSMb1YUJFrobjK2jL-vArjaf7eyufTgsfqtkNjpyLPCqJCB6YR3R5wC88up93WvxRCCfOCNAsRikWK93MblAWs78u4vlRuyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=NeiEk8CISbV2eBP-OpNZ_RTmPX2qop9l5YviCEjIbDjGyUBfTPFPmu-C_5h-DE0NTMLGn_s04del5WmE-vtjhOPy_VJZmBSgEstGwty-KefnKXuwc3dhON9joNak8XLPY4CcL1zU4bgqpjzdHNQYgw9eItukgXPQCZVsZDO6MLUxmVgNqoMOPodp1IUFgTIEF5AJJPaDRIIb36IqemQyePhFN2iH8XmrtvT-HJbMLb6akYg23R2d0XSMb1YUJFrobjK2jL-vArjaf7eyufTgsfqtkNjpyLPCqJCB6YR3R5wC88up93WvxRCCfOCNAsRikWK93MblAWs78u4vlRuyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقجي
: في هذه الحرب، أثبتت صواريخنا كفاءتها بشكل جيد وساهمت في الدفاع عن البلاد بشكل فعال.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/88711" target="_blank">📅 00:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSUQzbw6RbFjmtPoL87JdcEInMHlug-PLUXLDCqka3nDPJXPSR9m4Pr8g3CSOA1qojl0QM4DNSqvY-oJlH2EFuTTu_SMc4QdmngBbnV9uOhc4ZkSJK3wFSqIt7YzJEv09BQrdTK9oFkWwI5Vp_bcdA1JcphEvzxX7HqDbDclNH_p5QUaSGkoDwaRzDncv46NLsUU37IlRXjIiYreRSwC90z2WV247fL8ZRU4_7nhB9mE6A17FpEDYILURka_RM8wRUkheuAvBXgYiff5FTURH3wEMnFNGy7Dc5qn-7kED4rVPOAj_LqhDrlhPm8sNxK2xfEMOZ2hEKV2RWTztsX9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهاجم صحفية نيويورك تايمز:
اختلقت ماجوت هاجرمان، المراسلة المزيفة من صحيفة نيويورك تايمز الفاشلة، وهي شخصية بغيضة من الداخل والخارج، ولا تعرف عني إلا أقل مما يعرفه معظم المراسلين في هذا المجال (إنها محتالة!)، قصة مفادها أنني في 11 سبتمبر، لن أذهب إلى مركز التجارة العالمي في مدينة نيويورك، لأنهم لن يسمحوا لي بإلقاء خطاب، وسأذهب إلى البنتاغون في واشنطن العاصمة، لأنني متحدث رئيسي. هذه أخبار فاسدة أخرى، لقد زرت نيويورك مرات عديدة على مر السنين، ولم يتحدث أحد قط، إنها "مراسم رسمية!" لم أفكر أبدًا فيما اختلقته ماجوت، وإلى جانب ذلك، أود ألا أتحدث، لأنني أتحدث طوال الوقت، وهذا يوم لتذكر الضحايا وأفراد أسرهم الأعزاء. ماجوت هاجرمان مزيفة، وصحيفة نيويورك تايمز تعرف ذلك! سيتضح كل شيء في الدعوى القضائية المرفوعة ضدهم، ودعوى أخرى ضد المنظمة المانحة لجائزة بوليتزر التي فقدت مصداقيتها، لأن ماغي حصلت عليها عن "تقاريرها" حول "خدعة روسيا، روسيا، روسيا"، والتي تبين أنها عملية احتيال كاملة! إذا أُجبرت على الكشف عن "مصادرها"، ستكتشفون أنها إما غير موجودة، أو أنها لم تذكر ما نشرته. لقد دأبت على الكتابة عني زوراً لسنوات. إنها متطفلة، ويجب إجبارها على تسليم جميع الأموال التي جنتها من خلال تقاريرها الكاذبة عني.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88710" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي:
تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88709" target="_blank">📅 00:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXGNy2ZWrLpUTvPR8FuCYOn3PReHwcjUw79R9r62cZIvXh4EVp5qCpBPNYve_pf7DAA1_akTtRm3b5_SQG-8dYv44eGyhZOECwmPBXOCYbZNQobYJ6hIONmd3YZlGk2wZdxBds0zA6kRkVwmAcaIX_ADO_jZdcfU9F_riNNu0QTjxr9wmvnaHLIqMp4v9KsxTZhdhS02VazD1nxP0wtz_XtpwXAXYgBcb08f03ieg-fLIW_8WI71EgaZf6hOO2aBfOSgtV8RFzexVIEixtIvJJrSvsjhPuhd9JtRS0vfkKckw5nZwML74gpC3Zzz-T5-TOUCL_dNpBfRBLd_1udT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني:
سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.
في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:
بسم الله الرحمن الرحيم
إن تصريحات المسؤولين الأمريكيين بشأن انفتاح مضيق هرمز كذبٌ صريح، ولا تهدف إلا إلى التلاعب بأسعار النفط والتغطية على إخفاقاتهم.
إن سيطرة كتائب الإسلام على هذا الممر المائي الاستراتيجي حاسمةٌ لا لبس فيها، وبكل قوة وسلطة، يُغلق مضيق هرمز أمام جميع السفن التي تنوي المرور دون تنسيق مع الجمهورية الإسلامية الإيرانية، ونؤكد للشعب الإيراني الحبيب الشجاع أن هذا الإجراء سيستمر حتى نهاية شرور الجيش الإرهابي الأمريكي ضد بلدنا الحبيب، والوفاء بالالتزامات المنصوص عليها.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88708" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇨🇳
وزارة العدل الأميركية
تعلن أنها تعرضت مع هيئات من بينها مجلس الشيوخ و"الاحتياطي الفيدرالي" ووكالة "ناسا" لاستهداف  من قراصنة معلومات صينيين</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88707" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
إستهداف هدف معادي بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88706" target="_blank">📅 22:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxUzbvpGBwXX3zsYQVb2UZq447nVkkyuwvYcUXEAtPUfbFTpAJwXILH9wn5Ynns-IshCjeEfbLorIWxn_ycI7PYveO9AhQmlsa_M4bsndcJdtyRDfFaY0mq2kek5zqrK7caRZ_I8vHfG_U2ZtPmE1CN6ZK6UtCn1P-Czm-E-EnpjGwK6fxHLf-Z-tgz9H_qaFnRkuCancTC4sFDmXATMe4sF63uqgGmEOmNH947Ti57YMPMEoCL953Y0YTWPI6v5xjSudollEO_DE-zi45DrBAbacXswfVpuDTDtNMSulmq_-EzCDV_cWQfQWtbj9ar6FUPzLB2jdm_BEcv-3Lg1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88705" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
التضحيات كانت كبيرة جداً في فلسطين ولبنان وإيران واليمن والعراق.
التضحيات الكبيرة التي قدمت في فلسطين ولبنان وإيران واليمن والعراق أوقفت المشروع الصهيو أميركي الذي يستهدف المنطقة.
نحن باقون في الميدان ولن نقبل بالمشاريع التي يتحدثون عنها.
أنجزنا أننا كسرنا مشروع "إسرائيل" الكبرى ومنعناهم أن يصلوا إلى العاصمة بيروت.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88704" target="_blank">📅 22:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
على أمريكا رفع الحصار والعقوبات والإفراج عن أموالنا وإجبار إسرائيل على وقف اعتداءاتها على لبنان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88703" target="_blank">📅 22:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88702" target="_blank">📅 22:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88701" target="_blank">📅 22:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMbAMc_IWkRRkacO-spBbsTasSGQcucFtwMCvkb4blCW8d-2hHaFCwbObSeaf47e2qPCu5RA4l8R8Tzs8sP13UeYqtrihDg65T1_I_oNtJCuEXJCrBVBfEwTAnEBaMQ2pZfApMrsSnLjbD1PV9Z1awmbY5fuGfGaB2_alRHgZ2TwNlVyxIKoR6v3hryvSI09unIyk7vKfmoYYudvg8t_iFTcLho9vf5nwRd2wTea5cTPT_4XUrk75pWzZwg1HxvlAU8UvREacdWO_rVCng9Nt_b35tOYNiWXrlmu8LcgyPyqkslvibd6AjtFYVjBqGmQU6axAOuOqqkUqYaMaXnlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8J_Rrg9QahjDg5W38ltYC-xqYp1USN67mQMIY2url195ukGpctB5s1fOrrfyS8lIUssywgauMT4kC2mzMyPMY257RIkbHchlZNmbKvA2gZc9N6mO_-Z8BaCs9QtVlOtJcYlrujuSRkhn_jchxRlsm7ZxxQsFasAL5X45xgFLHVPbQD6_yupAv-dlNvMLI4vcZZEgeBy4RnROsdTaP1vD-adPxgVJ7rTYMbeXJzZXsnEu8caajYZApZr_HGq1HK-QHcXDEXEl8SjfbaudyfUeAX-m1X0Wx9OOuCqkFf2esTVxocf6OahvddfkuPViOABAGgJnYsCNQ7i0Si18lxgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuJNv1NN6JAIgXHy4u7vuq5hD7sz5FFuf55egmZ3eD9Z2ilq69YeS6KUITms66B8UXkAHg_yCVGKxrRc-6NxAhHCCiEbbaZH_Xc-wfpFKnHCsU9OJdE2d-BpsPMmxK2Xvjv7b_c5dXpCacPfWYNCEm8zjevUgVuK4ncjSnJPuprWXb1LL0nKvsrVLpbzzHwf5bzU2didxYb9ojMQGQNrQ8ZT_zYmcqDGcJ8w1ZigNrM2vaStEwnrpeqgGiMmOmuug3aoa6PjfFyOIuI97dRCRQe965WemeowR86G-L2Ud_6dYtXb9WQH5s6xDi9swAtHKF1uaBqoRlOFsD_OLZPDFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنفرد نايا بنشر وثائق تؤكد قيام البنك المركزي بحجز أموال 12 مسؤول عراقي بتهم الفساد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88698" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63010842fe.mp4?token=b_EWb61Iq8TLTXc_3Taxa1_mGh16sacaxvsnh1CmLOG7I_DHoQHcUcnpmo1JiAmP68TKYWxRnY9zPD6n_63NaUI1YdfolQhwJ2BUd6ys_VuJmaOQHy2Pksa3aqK2s7KlFlf0XtFjGhaU5heOMVP60-TZxix02JnPuUCf1Vaj5rom3DR1MJ2kCNQSj9N8Ww6PjU-HI0IvPGQIX-Pj5xjxEs1YkeCdsmJRqdLKroXGr8W_0Z9yy9KRZqo661A36vO04R1mpO0wwPn8OT6vfiviRh-x-i11XpLfRM_HY1WmXASjFxBTLDV35ktfPvd19wPRQ_0Ohhx595jWGVHFUH0FyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63010842fe.mp4?token=b_EWb61Iq8TLTXc_3Taxa1_mGh16sacaxvsnh1CmLOG7I_DHoQHcUcnpmo1JiAmP68TKYWxRnY9zPD6n_63NaUI1YdfolQhwJ2BUd6ys_VuJmaOQHy2Pksa3aqK2s7KlFlf0XtFjGhaU5heOMVP60-TZxix02JnPuUCf1Vaj5rom3DR1MJ2kCNQSj9N8Ww6PjU-HI0IvPGQIX-Pj5xjxEs1YkeCdsmJRqdLKroXGr8W_0Z9yy9KRZqo661A36vO04R1mpO0wwPn8OT6vfiviRh-x-i11XpLfRM_HY1WmXASjFxBTLDV35ktfPvd19wPRQ_0Ohhx595jWGVHFUH0FyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي.. إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88697" target="_blank">📅 21:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سماع دوي إنفجار عنيف في الأردن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88696" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
عراقجي:
لن نتهاون في مواجهة انتهاك الهدنة، ولن نسمح للعدو بالتصرف بطريقة تجعل انتهاك الاتفاق عادة. لذلك، قمنا بالرد.
فيما يتعلق بأمننا، لا نتهاون مع أحد. مقاتلونا سيردون على أي هجوم بنيران أكبر.
نحن ندافع بقوة عن مصالح البلاد في ساحة الدبلوماسية، تمامًا كما ندافع عنها في الساحة العسكرية. في ساحة الدبلوماسية وفي طاولة المفاوضات، ندافع عن حقوق الشعب الإيراني.
لا نعول على الانتخابات الأمريكية ونقوم بالاستناد إلى قوتنا وشعبنا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88695" target="_blank">📅 21:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=YHwP2aZhb4LlXew9CjCElgWa4f7VQFTSrDE64zMt85a1mfF32qytVCW1mM_jhTRPiILR_qnk1ss8dN5F4JnnJ8hrc_SaDkYwAOfTrvvD3YUxvKw_DJe9brtE3aHoEqk7vclowGaQw2tSeYVJvmpwT3F1-E6vxnHIPOk2D_w15h1LLcNJMjdBR9zVCmm7TWOvMmjzaPFL7g3l24pWiRKSSs8TYlvXzT6XnnMbDo6Y2AbCvtBU5AaN87Vw2eNlGfr0yxT5BgSKkP082mTRwi_vjNQhGISKB6w_8ZuqKB1kEul4FO7pmY9Ip-8ZP7gG8I_VRSqh42xfJS4h2shZo2Dcn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=YHwP2aZhb4LlXew9CjCElgWa4f7VQFTSrDE64zMt85a1mfF32qytVCW1mM_jhTRPiILR_qnk1ss8dN5F4JnnJ8hrc_SaDkYwAOfTrvvD3YUxvKw_DJe9brtE3aHoEqk7vclowGaQw2tSeYVJvmpwT3F1-E6vxnHIPOk2D_w15h1LLcNJMjdBR9zVCmm7TWOvMmjzaPFL7g3l24pWiRKSSs8TYlvXzT6XnnMbDo6Y2AbCvtBU5AaN87Vw2eNlGfr0yxT5BgSKkP082mTRwi_vjNQhGISKB6w_8ZuqKB1kEul4FO7pmY9Ip-8ZP7gG8I_VRSqh42xfJS4h2shZo2Dcn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي..
إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88694" target="_blank">📅 21:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=brOhzQ0B5_LG4pOcZ6a03bVnpx2wsYHuxy8K11rdJYw1IZNCX-y0MCPYKOB8Ps7AZyfMgtsfTOohaWNHb-rG4qyN-KIQ5-XdOXSZN6eKRu6F616BZ7seo2__Mg4h9H28zvXuybYkaa27r9TPnlCdegeG06Gh4ryuB5qYcJIoYLfb7PiGRR233FfVIIcYh4cIDVOJ3o-DJJ7CDUCpHY0elqAr3ARoqZOmutJxhW7NRYTGE5vSk53I66hT8UciccySE5hCC0cV0NBLs7gJRx7xjCXJ1_HXH3PRrKnFCzeW5flffEBGce-KSqWp3GK3SadRoJ4uuo1RY9jIcmMyhjno-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=brOhzQ0B5_LG4pOcZ6a03bVnpx2wsYHuxy8K11rdJYw1IZNCX-y0MCPYKOB8Ps7AZyfMgtsfTOohaWNHb-rG4qyN-KIQ5-XdOXSZN6eKRu6F616BZ7seo2__Mg4h9H28zvXuybYkaa27r9TPnlCdegeG06Gh4ryuB5qYcJIoYLfb7PiGRR233FfVIIcYh4cIDVOJ3o-DJJ7CDUCpHY0elqAr3ARoqZOmutJxhW7NRYTGE5vSk53I66hT8UciccySE5hCC0cV0NBLs7gJRx7xjCXJ1_HXH3PRrKnFCzeW5flffEBGce-KSqWp3GK3SadRoJ4uuo1RY9jIcmMyhjno-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88692" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib1lHk6JWPcjmlYC9LSH5Gx-RIFUTEI8Y4f93Oi8tssrucciI7NHjSuzy4jPw0alp53LXciNgX1Uhn6pVaUa7UqOxvKnSBt5tLQn8TPA8x8UvBcgxBxrx8D8Rq8heEdXADxgf2ngSGxvP_Wp8KSg7tensO2xAIEmIGUkFXZGwuo9G8i-a0G9PBPE9bkWrPAV3M3fEcNcFhahe_XYZ8jn1T_uj29_3YiGNhLWQ63DIKEiKlOF9HP5a0S21viSFo2X9ukKu94D9VBSHb0jrcqg86LjpY4Nk_1dxd_JBobl2WEuvNxNCUBHgyRi80Y0aIHUGLfOAI4OH-tukHdY9wlBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88691" target="_blank">📅 20:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
مسؤول في حلف شمال الأطلسي "الناتو":
لم يتم تحديد أي موعد لإنتهاء عمل قواتنا في العراق، وأن مهامنا مرتبطة بـ "الحاجة"؛ تم نقل فريقنا من العراق إلى إيطاليا "بشكل مؤقت"منذ شهر آذار الماضي بسبب الأوضاع الأمنية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88690" target="_blank">📅 20:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979455137b.mp4?token=RD7o6o-igTBdxFqcwmidWlUsCJFih7Azj39XvDJpLuhB7IwzvMItcrf5VU2H8GLX9tLSYjUC8yeBZiRndKqtImyhdv7YCSDAP04lsLEZOoSaAUVNDcXiYsnBKYfheAjZTYEvjFdxJqAuqiIYpFBKFTWKxrC0KqVtPJ8Vo46I3eMacU97HzA_o3FL-hGSFk_lsYg1h4KPg_GLHv8p6ZYWjvf1U0pQEvOgYk0v_Eut0p-64p95HxwGklk_ig4vT2DHs4-R62ctlbwA3euk4P15oFGP4xxjohLPOleehOtTzU7kj4a4RctVic7qZQagu4sxBcxtV3yvyEqhtAA8dsEPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979455137b.mp4?token=RD7o6o-igTBdxFqcwmidWlUsCJFih7Azj39XvDJpLuhB7IwzvMItcrf5VU2H8GLX9tLSYjUC8yeBZiRndKqtImyhdv7YCSDAP04lsLEZOoSaAUVNDcXiYsnBKYfheAjZTYEvjFdxJqAuqiIYpFBKFTWKxrC0KqVtPJ8Vo46I3eMacU97HzA_o3FL-hGSFk_lsYg1h4KPg_GLHv8p6ZYWjvf1U0pQEvOgYk0v_Eut0p-64p95HxwGklk_ig4vT2DHs4-R62ctlbwA3euk4P15oFGP4xxjohLPOleehOtTzU7kj4a4RctVic7qZQagu4sxBcxtV3yvyEqhtAA8dsEPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88689" target="_blank">📅 20:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.
أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88688" target="_blank">📅 20:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
‏
الإعلام الأجنبي:
قال نتنياهو "سننقل المنشآت العسكرية تحت الأرض". ويبدو أن سياسة نقل المنشآت العسكرية إلى تحت الأرض درسٌ استخلصه النظام الإسرائيلي من الحرب مع إيران. فخلال حرب الأيام الاثني عشر وحرب رمضان، استُهدفت العديد من القواعد والمراكز العسكرية الحساسة للنظام بدقة بصواريخ إيرانية، على الرغم من أن جهاز الرقابة في الجيش الإسرائيلي منع بشدة نشر هذه الحالات في وسائل الإعلام.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88687" target="_blank">📅 20:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
ترامب:
أنتم ترون كم نحن جيدون في القتال. نحن نقاتل بشكل جيد جدًا. انظروا إلى فنزويلا. 48 دقيقة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88686" target="_blank">📅 20:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0568799d32.mp4?token=k9Qxi4jbUmL3Y_A8FtA_Lm8qY-UGeRKsFPljyoAQn4A0pm7dh9-skrgBzfQGieAIzk_knqxIXpNdTMly9xQ87UA0WEBs8TobtwiJRJtslBjo0f9daol0WzGIr4-_-d0jjyzWTF99C_-YhAOZ7LMqqpbYsA5TrDRE2DbfuYA2x9Geyl8zYgMJNp8OBPsfs5qxf1WsbSK81sUIVezsv9zCNQqD2QfbKbobHo25wbeJFcvIzRehRyugig7oUnAQIioqztVtISKvdv8fLPHYvDLtqOQtKADCPV8CE-Zn5eG_IZZ_0CK_e0QeLtQIrjBjLzet0hJz65GSJbZhjYPg3RtO3C2WIiHQ6ktYEIygxQyeupQO4OJF0XNdetTN9-Yc4aIZr9rJ4kSp_vf5I5Zn96f1aPnqfQTUxSxKec31BcuGnBDa_CQvxvWKX0V8HhbHT9PXMqEx5ReZC5hsfpNw8xnLbduDPhKmtvKo1kCT7e-EHh-wAGvZDoTC4LVkln5EmesqOvOrPkfEmdTdX73TZWP7m9q6p5i8kYvS5-7RNZ7N2-iLf9hNzKQoctgGe0nuAUUePJW7e9NFM6MEucVet-yvTle0LEKXsVDRY98xL-uXUaNXfe2kZlokZHFoe1eKa9WDoi5a2TwpkqYrzmfMFalir7uFBWhoCkuAtxdoKWsDIX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0568799d32.mp4?token=k9Qxi4jbUmL3Y_A8FtA_Lm8qY-UGeRKsFPljyoAQn4A0pm7dh9-skrgBzfQGieAIzk_knqxIXpNdTMly9xQ87UA0WEBs8TobtwiJRJtslBjo0f9daol0WzGIr4-_-d0jjyzWTF99C_-YhAOZ7LMqqpbYsA5TrDRE2DbfuYA2x9Geyl8zYgMJNp8OBPsfs5qxf1WsbSK81sUIVezsv9zCNQqD2QfbKbobHo25wbeJFcvIzRehRyugig7oUnAQIioqztVtISKvdv8fLPHYvDLtqOQtKADCPV8CE-Zn5eG_IZZ_0CK_e0QeLtQIrjBjLzet0hJz65GSJbZhjYPg3RtO3C2WIiHQ6ktYEIygxQyeupQO4OJF0XNdetTN9-Yc4aIZr9rJ4kSp_vf5I5Zn96f1aPnqfQTUxSxKec31BcuGnBDa_CQvxvWKX0V8HhbHT9PXMqEx5ReZC5hsfpNw8xnLbduDPhKmtvKo1kCT7e-EHh-wAGvZDoTC4LVkln5EmesqOvOrPkfEmdTdX73TZWP7m9q6p5i8kYvS5-7RNZ7N2-iLf9hNzKQoctgGe0nuAUUePJW7e9NFM6MEucVet-yvTle0LEKXsVDRY98xL-uXUaNXfe2kZlokZHFoe1eKa9WDoi5a2TwpkqYrzmfMFalir7uFBWhoCkuAtxdoKWsDIX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قوات شعبية إيرانية تنطلق نحو مضيق هرمز ردًا على تصريحات ترامب.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88685" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم يمني بالطائرات المسيرة الإنقضاضية على معاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88684" target="_blank">📅 20:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga7MRgEVzlzjEe20KMQ68T7hDRx3Pb8xZtoBo262KeEnNQzrueoiQLYSPnh89q8Np2YWVeUK0UveqZwez_0GxcMkdPyME9Sy_7mz2UeJdQw9jiODsm1h45du1Ws7qW6kMOKjEGCzsVGqWOXwvG3MzH-iQ_jJ_CPbR9IL2AMOyXeP2zlKiiDjm15c0MpdCJIwfBWaivhgcm3vAheX6ryBhMs6C-UqiK1JTgALvWgiU9lH0CmSwxlX8yrHP-31Fl0h0VABpfk5zlf8WXC4OJ0kUyVFlCvgfrUVfc1FLsvQacKlpdEF_649ynoyFhEHxszMP_h_cl35LVFaKYbU4xGvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇷🇺
روسيا تشير إلى ايران
وتفتح النار على القصص الملفقة التي صنعتها الصحافة البريطانية ؛ ماريا زخروفا في عام 2010 بشأن سكينة محمدي أشتياني (ولا يزال بدون تراجع) - كان ملفقًا بالكامل. ساهمت القصة الملفقة في تأجيج الضغط على إيران. ليس هذا بالأمر المفاجئ، بالنظر إلى سجل الغرب في التلاعب بالمعلومات.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88683" target="_blank">📅 19:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران؛ مقتل إرهابي وإعتقال 6 أخرين.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88682" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88681">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
‏
برنامج الغذاء العالمي:
نحذر من نقاط الاختناق في هرمز وباب المندب والبحر الأسود.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88681" target="_blank">📅 19:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88680">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
🔻
الحاج العامري لشيوخ عموم عشائر العراق:
-سنشرع قانون الحشد الشعبي وتحدثنا مع رئيس الوزراء وهو يؤيد ذلك
-فصائل المقاومة أناس عقلاء دافعوا عن العراق وسيادته وقاتلوا الاحتلال وداعش</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88680" target="_blank">📅 18:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88679">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇾🇪
الحكومة اليمنية في صنعاء:
امتزجت دماء شهداء اليمن مع شهداء فلسطين ولبنان وإيران والعراق بمواجهة العدو المجرم نفسه الذي يستهدف الأمة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88679" target="_blank">📅 18:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88678">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
🇺🇸
أثار حرب أمريكا على المنطقة
ول ستريت جورنال:
‏توقف مشروع نيوم الضخم والمستقبلي في السعودية، حيث اصطدمت التكاليف الباهظة للمدينة المخطط لها بالواقع المالي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88678" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88677">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736924625c.mp4?token=cOXSA_8tmgb5B28hM3VbgAvE-VIbRuD5G4lDev4Oda842ZGydPymgh6E1liAIqwVI6dfsBWmbstatUonmvlHFHX-V7tBy1jnU2X8ThZuldE01VWOoj6-ub7MqrqnGa7h18Iet2IF6DCVIlin6eUa-CHzGF3BGZ4nEQpIjcXdEH01VKfsSvnGVG1bHPHC2H7md9IylsrNfWP3yM1OSaUYEOuOlHVtzlTuVvBx8n3KkMefP4SCboDcWcbiiUEE5iNwdH3wlWkJXjAHtrXbjIvO40pMlLjGNmdIVTMYy2y1dBPBiyol31KYRhbJXwpAYA5iHhrPpUXCwyF3z5Ha0tKUv7o-SSThuY5KfjFV4xgUrKq2WVolmaMeBc_9p4QWX-P3zAe9rG4k9L0TtjCm0GNqEnAy2W9Rv2xdqMcRJvqx-hbFaFq5qzdZTW-FbSMNum8uMJ50uQy8-uWI4RukOk-OHAZJUOqZ-jeui02F-CKcJNMHeZ2x9otDj1duGCDShiXaYb26ZZAlfDzGsSK-IS4TwQaa1j2hNhhx6CrlsCUn0Giq28BMwAhDliybR8qQ0-Xk3FsK3-9oCThQu5M2fqJfQ_iKNED6wEDAWzJfUHVC3nTp0NS44UvaxTCTAZ8SGIEOgCR6gRqOFU0rs9HmGcHGHoafC1XLmuG0cZqU9NCHRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736924625c.mp4?token=cOXSA_8tmgb5B28hM3VbgAvE-VIbRuD5G4lDev4Oda842ZGydPymgh6E1liAIqwVI6dfsBWmbstatUonmvlHFHX-V7tBy1jnU2X8ThZuldE01VWOoj6-ub7MqrqnGa7h18Iet2IF6DCVIlin6eUa-CHzGF3BGZ4nEQpIjcXdEH01VKfsSvnGVG1bHPHC2H7md9IylsrNfWP3yM1OSaUYEOuOlHVtzlTuVvBx8n3KkMefP4SCboDcWcbiiUEE5iNwdH3wlWkJXjAHtrXbjIvO40pMlLjGNmdIVTMYy2y1dBPBiyol31KYRhbJXwpAYA5iHhrPpUXCwyF3z5Ha0tKUv7o-SSThuY5KfjFV4xgUrKq2WVolmaMeBc_9p4QWX-P3zAe9rG4k9L0TtjCm0GNqEnAy2W9Rv2xdqMcRJvqx-hbFaFq5qzdZTW-FbSMNum8uMJ50uQy8-uWI4RukOk-OHAZJUOqZ-jeui02F-CKcJNMHeZ2x9otDj1duGCDShiXaYb26ZZAlfDzGsSK-IS4TwQaa1j2hNhhx6CrlsCUn0Giq28BMwAhDliybR8qQ0-Xk3FsK3-9oCThQu5M2fqJfQ_iKNED6wEDAWzJfUHVC3nTp0NS44UvaxTCTAZ8SGIEOgCR6gRqOFU0rs9HmGcHGHoafC1XLmuG0cZqU9NCHRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
اندلاع حريق في احد مقرات الحشد الشعبي بقاعدة سبايكر شمال غرب محافظة صلاح الدين العراقية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88677" target="_blank">📅 17:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88676" target="_blank">📅 17:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88675" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
نتن ياهو يزعم إحباط هجوم وشيك من جنين.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88674" target="_blank">📅 17:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=l9KnAEMKrQNugkgt310Je4syQ4e8FeLoA96_WV5C_eGK8RUbnj15kpCg9JKldeHmGydWgBwS_S2VHIBLEa945S09l05Vg6upZxDnE5yB9KltQYRz2DZizVL7-N7Q9gfkyndyul59kH47k3zg-h-6YKVISJ_VUGH0oO2oqD3_Mkv7pwZtaDx2pjFh2JJMMOuRSQ1GXUNXdEjF3itrEcZ8yO5N5bWv5VHU5TEn24c0YcTIAruCqlmoQWEUGZEab11ZAF82JDCZQ7SwVaIL1OTPN-7QCrawLaus_TH1Q3eDBw3qGmYRYuzA2da8aHBqFg5oIl8u97zsPIUtLd276dxS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=l9KnAEMKrQNugkgt310Je4syQ4e8FeLoA96_WV5C_eGK8RUbnj15kpCg9JKldeHmGydWgBwS_S2VHIBLEa945S09l05Vg6upZxDnE5yB9KltQYRz2DZizVL7-N7Q9gfkyndyul59kH47k3zg-h-6YKVISJ_VUGH0oO2oqD3_Mkv7pwZtaDx2pjFh2JJMMOuRSQ1GXUNXdEjF3itrEcZ8yO5N5bWv5VHU5TEn24c0YcTIAruCqlmoQWEUGZEab11ZAF82JDCZQ7SwVaIL1OTPN-7QCrawLaus_TH1Q3eDBw3qGmYRYuzA2da8aHBqFg5oIl8u97zsPIUtLd276dxS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازمة الوقود متواصلة في محافظة اربيل ضمن اقليم كردستان العراق ولا حلول تلوح بالافق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88673" target="_blank">📅 17:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">المنظمة البحرية الدولية التابعة للأمم المتحدة": نحو 6000 بحار على متن 400 سفينة لا يزالون غير قادرين على مغادرة مضيق هرمز</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88671" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
🇨🇳
موقع ذا إنفورميشن:
الولايات المتحدة تعمل على وضع قواعد للذكاء الاصطناعي للحد من وصول الصين إلى الرقائق الإلكترونية. الولايات المتحدة تعمل على إيجاد بديل لقاعدة الذكاء الاصطناعي الحالية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88670" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
