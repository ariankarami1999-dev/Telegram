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
<img src="https://cdn4.telesco.pe/file/BH5E-dUd-WW-7ytskn_GF3xtuhInPFbmfSyRK71mnm8TjkcVVxTYhhtxF4aNjGRAqbhaRdOZPmbO6enerQDrqgdWmBePPvQY3HZhgdDBUX8jtwXu3BhVbCXlQf34zQsHnF4haykmaNrPDaW8hST-1lx1SRt1IGEfQHMbEQwXxzDkiA8MkAbRUKLNxdxXuTo8erI5VbsMqWIRz1dIsR62Ny0Ud3HOwpfL30aqA-bfjbABa9xR-_EzzZRWL80ovIU4_vPl033mpG3VLfcgwxjNEDBcIcbTDBRHxexhzVwi2oPSR9aasAuXGUtUNNanS7r_gVATz8tOOZaL58CdwMaYXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 23:41:53</div>
<hr>

<div class="tg-post" id="msg-652933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a10808b7f4.mp4?token=Xf3eQw_8IZWl6KhKWog_s4ZmiO6fyFQs9iv-fiSYYo62s8SQogpA-FhNA2kpSRJtRakbc_KWgAmgOm3H1xwJnpJ_8nW3qAHBSCDcKdIawlO6eF-1ZtFL1mce0n2ZudnleAyq0YaFqUvvWk7-_Yr27gCLo8u8gXILNz1YVsV8UGw7C7v5ApYDhEXFk-MtLNaBZ80cEJE1BPVhB7twZRSWMowsYONr2G8FFZKqirtBVDf84ObL66A0VdGVpwg34NTHi38oF5yja22ivJZo6jGu7UOo4UsweJFNCentQacLGBe2z1X16vDKmILW-tfCBOdd2-A9bX509WiUdtZxeKLg2WUfudAmugOxPTZEHIxt8Wv1wMhQdH3hJUOiuw_oUHVcHU1JwTCRP8lJIMnpVDfFkj-xi26kSVasx6i5_0E3QB36D6tID3hDTC6ZB6K1rcL_UDxFyZUdX4wnYHiYEupGt1ykSNhVSf0RcMgwVofb63un9njE6A8XoS7BOmKYHLOQVONH5LQXZ3yl5QUTJ7cEDOekjK8kuryeQze-lEYcqmcBI4aGTXXmNMQ8s5IWzoXdB8Wcc5Mn_92Bg-9c5Y3riWkfpy0zupxJkl3921zcCKOLi8ZDhP3lHdzXiEfrVdjkqvzMXieHIOcwzBhUOGAdgbPXqPTrUEnJ7YxrljIPjms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a10808b7f4.mp4?token=Xf3eQw_8IZWl6KhKWog_s4ZmiO6fyFQs9iv-fiSYYo62s8SQogpA-FhNA2kpSRJtRakbc_KWgAmgOm3H1xwJnpJ_8nW3qAHBSCDcKdIawlO6eF-1ZtFL1mce0n2ZudnleAyq0YaFqUvvWk7-_Yr27gCLo8u8gXILNz1YVsV8UGw7C7v5ApYDhEXFk-MtLNaBZ80cEJE1BPVhB7twZRSWMowsYONr2G8FFZKqirtBVDf84ObL66A0VdGVpwg34NTHi38oF5yja22ivJZo6jGu7UOo4UsweJFNCentQacLGBe2z1X16vDKmILW-tfCBOdd2-A9bX509WiUdtZxeKLg2WUfudAmugOxPTZEHIxt8Wv1wMhQdH3hJUOiuw_oUHVcHU1JwTCRP8lJIMnpVDfFkj-xi26kSVasx6i5_0E3QB36D6tID3hDTC6ZB6K1rcL_UDxFyZUdX4wnYHiYEupGt1ykSNhVSf0RcMgwVofb63un9njE6A8XoS7BOmKYHLOQVONH5LQXZ3yl5QUTJ7cEDOekjK8kuryeQze-lEYcqmcBI4aGTXXmNMQ8s5IWzoXdB8Wcc5Mn_92Bg-9c5Y3riWkfpy0zupxJkl3921zcCKOLi8ZDhP3lHdzXiEfrVdjkqvzMXieHIOcwzBhUOGAdgbPXqPTrUEnJ7YxrljIPjms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پیشین سازمان سیا: ایرانی‌ها قرار نیست تسلیم بشوند
🔹
جان برنان، رئیس پیشین سازمان سیا: ایرانی‌ها قرار نیست تسلیم بشوند؛ حتی اگر دوباره شروع به بمباران بکنیم، آن‌ها تاب‌آوری بسیار بالایی دارند. دونالد ترامپ به‌طرز استثنایی لجباز است و حاضر نیست بگوید که این جنگ یک اشتباه بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/akhbarefori/652933" target="_blank">📅 23:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a490a6b7.mp4?token=JvO_jroVNwk0ESBmCmtXe9f_PNU7mCFXMHPtnjSaKEJUqJg1IAG4vRW8kdmLLMeDYvVgObEk-YIuOI4jASceaQeb0V1j6XLOaMoki1JMd52l318tcZAfGHbiZ8sZROsCusSNx9PgyVgv8msDTvfdnCpZP-vq7XNOR2LdIBTwwd08c0Aty0gzeZDRJEvcFG7YizKB6jIBmQG4ZV4qBnU7VEMaOKlFgK7zm5WWNkMHoR2o2Xat33km3gUDi_j1Uj9fRiK-uHhw3BWxsu_WSJfDmPPBsBDaYYAZNF-Ir5wB0vPiwCqgBZjkAZiZnd7vLLMkXeYhOPTmdr6LrtBCj1xF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a490a6b7.mp4?token=JvO_jroVNwk0ESBmCmtXe9f_PNU7mCFXMHPtnjSaKEJUqJg1IAG4vRW8kdmLLMeDYvVgObEk-YIuOI4jASceaQeb0V1j6XLOaMoki1JMd52l318tcZAfGHbiZ8sZROsCusSNx9PgyVgv8msDTvfdnCpZP-vq7XNOR2LdIBTwwd08c0Aty0gzeZDRJEvcFG7YizKB6jIBmQG4ZV4qBnU7VEMaOKlFgK7zm5WWNkMHoR2o2Xat33km3gUDi_j1Uj9fRiK-uHhw3BWxsu_WSJfDmPPBsBDaYYAZNF-Ir5wB0vPiwCqgBZjkAZiZnd7vLLMkXeYhOPTmdr6LrtBCj1xF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای‌بی‌سی: نزدیک به شصت خودرو پلیس در محل حادثه حضور دارد و بالگرد پلیس در منطقه تیراندازی گشت‌زنی می‌کند
🔹
خودروهای آتش‌نشانی و آمبولانس نیز به محل حادثه اعزام شده‌اند.
🔹
به نظر می‌رسد که این یک حادثه بسیار جدی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/akhbarefori/652932" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q82qZn83NeW9E-XszOv4fkZSlVrxjCEzfK8Gs_WxpstBPa-CORO7dp8Nw09f6FW62024kSDEzrb1LYWeB1YwWvOEdvJsYrRRNCAQVlI3oZefzfsUOtbVa4RL-ccm-s3-PtTAyOUSha9Fr0sibUbBAISCQUo-hUAyWxcFOWiEDUPiAjlhAPsamTAFmENsL5Q6_b_1dfyFJi-67Jr3wxy_ofq5OrUTLS7hdueJyZdyyFiy70RpSIbjbdW8uQy386dMSmo6gZ1W8EOmHEtUUDK4wIyKfhwSiWS8ENFwsb7GVoYTZ6TJJDTMCrL7cpsFmzyChbp6gIYk_OgnY37h-IxVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس‌جمهور ایرلند به ربوده‌شدن خواهرش توسط رژیم صهیونیستی
🔹
رئیس‌جمهور ایرلند: ربوده‌شدن خواهرم توسط رژیم صهیونیستی بسیار ناراحت‌کننده است.
🔹
من بسیار نگران او و همچنین نگران همراهانش در کشتی هستم.
🔹
«دکتر مارگارت کانولی» خواهر رئیس‌جمهور ایرلند، جزو شش شهروند ایرلندی است که از ناوگان جهانی پایداری ربوده شده‌اند.
🔹
دکتر کانولی در ویدئوی خود: اگر این ویدیو را تماشا می‌کنید، به این معنی است که من توسط نیروهای اشغالگر اسرائیلی از قایقم در ناوگان ربوده شده‌ام.
🔹
من اکنون به‌طور غیرقانونی در زندان اسرائیل نگهداری می‌شوم.
🔹
من بسیار مفتخرم که در ناوگان پایداری شرکت می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/akhbarefori/652931" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله پهپادی علیه گروه تروریستی پژاک در شمال عراق
🔹
مقر گروه‌ تروریستی پژاک در استان سلیمانیه عراق با چندین فروند پهپاد مورد حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/akhbarefori/652930" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9TCX9jjAVAEM0QLIACapM4ADCPNdyHpbCvH7tz4uhQfv5Yhe_2DWJ96vaznLAZm3_sop-VzulPV4v1EwR1k4juoMPDDMhT9oUHXIctq1mTerg97sG5zTurlI9xOePPFWghKPs2utwEiFQOO2OtEAwDGhk2FnehrlRhGDk8LUirP2hMYzmD_LX5BQFT-n1_wd18c7tmAwiY_gXfjHciINDJaJ4gO-JHVmn_wviP_SsWHnkG55K6C4Y_0tOVcn3kypmP-YvhOptY_jsvoJ0_GaIEZP2Ok5vnrLBPUyYsw6CHubjjQM0bGEauPzgKLNssEeTmfTrMAwpC1ffpUN8Ozxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر| کارشناسان: علت فرار مجدد ترامپ، ترس از پاسخ قاطع ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/akhbarefori/652929" target="_blank">📅 23:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSnvd1ohFw5oEaBJgsfyjovIrUzv3ZnJBEkYDPLi1Vbc9r_YyWN3ob_JlwE6xdO2ONDsTEhgtBVm0X7lmR37aek7YJ2LxCzG0DATHrlrtYEwdngu307FJpcni6kk3OSuc26n6rnyMZs5h4TyAB6KSUf_jeK_uydff4xqRwE_3GYI7EEIq85fijSGNGCWqN-30GGBMcuGLqU0Kb0nnc3R4Z2p16Ac_Gibq_rlR-b9c-nvwbdgY7qH_K1vSizSFksGk_djmnzHZLIVcY8ydXfI69ca8SWZ_P_JuZ2z4IHLzX4M2nVQBvZAYtf1bH52ub6F6gIF33VLv1WeIlwXOzdBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش فوری ویلا جنگلی در نوشهر (نخ شمال )
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن لاکچری
داخل شهرک معروف
🔥
✅
متراژ زمین ۱۰۰۰متر
✅
متراژ بنا ۷۰۰متر
✅
۵خوابه (مستر)
✅
استخر چهارفصل،آسانسور
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/akhbarefori/652928" target="_blank">📅 23:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
استانداری هرمزگان: صدایی که ساعاتی پیش در جزیره قشم شنیده شد، ناشی از فعال شدن سامانه‌های پدافندی بود
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/akhbarefori/652926" target="_blank">📅 22:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j488fvwpCVTowj7OGlYLAm5sGcv6prE2R79hHeNVYZmnLbpahdwiXlglG9iBTV_sfXBkxgcankWUG8hsKrF4mzlfMiFtKALV7eZI3AHRAm4qYvKTbtND7ELqLPN1Qid7I69zuaKofXhXlhRT7mvkZtZRc5jUx7-qWHJ2_7u5U9t1XAf2silD7SmQ-cD_Nc2FbSFif-_zmxf7a6GSLbqXOW3gJOfu-YoMfb5R_1LbZbsyFxbWT4DCIndb8v6azfgH2-f8VI8-f4sWEGHFaHCmI-dgZC_V7UkD-yVFmbaP3x1QihvcqCu_C055mSh54KF7syXm--goPBuIa0FWxKI2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پهپادهای FPV حزب‌الله مانع اساسی پیش روی صهیونیست‌ها
🔹
یک شبکه عبری گزارش داد که ارزیابی‌ها در ارتش این رژیم حکایت از آن دارد که ریزپرنده‌های انفجاری حزب‌الله مانع از حدود ۷۰ درصد از آزادی عمل ارتش در جنوب لبنان شده است.
🔹
شبکه دولتی «کان» اسرائیل اعلام کرد که بخشی از برنامه‌ها، عملیات‌ها و مأموریت‌های تهاجمی ارتش این رژیم که قرار بود انجام شوند، به دلیل تهدید کوادکوپترهای انفجاری حزب‌الله یا لغو می‌شوند یا به تعویق می‌افتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/akhbarefori/652925" target="_blank">📅 22:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بهم ریختگی بازارهای مالی آمریکا، وضعیت قیمت نفت و ایستادگی ایران، دوباره پدوفیلی را مجبور به عقب‌نشینی کرد
🔹
ترامپ دقایقی پیش نوشت: «از سوی امیر قطر، ولیعهد عربستان سعودی و رئیس امارات متحده عربی، از من خواسته شد حمله نظامی برنامه‌ریزی‌شده علیه ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛ زیرا مذاکرات جدی در حال انجام است و به اعتقاد آنان، به‌عنوان رهبران و متحدان بزرگ، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین تمام کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود. این توافق، نکته‌ای بسیار مهم را نیز در بر خواهد داشت: ایران نباید سلاح هسته‌ای داشته باشد.»
🔹
او در ادامه دوباره منتی بر سر حکومت‌های میزبان پایگاه‌هایش گذاشته و نوشته: «بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای نظامی ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده علیه ایران را فردا انجام ندهند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/652924" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
علت فعال شدن پدافند جزیره قشم مقابله با ریزپرنده‌های دشمن بود
🔹
معاون استاندار هرمزگان: صدایی که ساعاتی پیش در جزیره قشم شنیده شده است، ناشی از فعال شدن سامانه‌های پدافندی و درگیری با پرنده‌های دشمن بوده است .
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652923" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
باج‌خواهی آمریکا از شرکت هندی به دلیل دور زدن ادعایی تحریم‌های ایران
🔹
وزارت خزانه‌داری آمریکا مدعی شد با شرکت هندی «آدانی اینترپرایزز» بر سر ۳۲ مورد ادعایی نقض تحریم‌های آمریکا علیه ایران به توافق ۲۷۵ میلیون دلاری رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652922" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ باز هم عقب‌نشینی کرد
🔹
رئیس‌جمهور آمریکا در شبکه تروث‌سوشال نوشت که حمله نظامی به ایران را بنا به درخواست ولیعهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/652921" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
فوری/ ادعای ترامپ: حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/akhbarefori/652920" target="_blank">📅 22:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylb1fCL_y3TYDEEzsLF0i4tlidJJYPlUSg4gTiGmiWEvXGgHCXwNqmLfqxnKcHKzPazoye_QRFTRHtyxT-IheqRoTB1WelQdCBY_cPaB4B9tpVP-hQFWCcIEAmJDFPhoiyfRGsDpOuwFdc6Py6IvCvj-U89_HRE_uyPxi0D3zUXdUg0AQ1TVb1s_kyqnzNXtbHtf-YO8miol7zDdVZtdOIu-ENwFrxPRzG-HfjNWsB83EIdLip4BsvX6w7vfPluobYnJo6CMebNTEQWleemB6_reQUffYbdmNlUFZmY8A-D1HNYlaUn0RBjGsl8l4GuSt4AWyX2fP3sE9-w0oOx_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالانه ۱.۵ میلیون تُن میکروپلاستیک وارد اقیانوس‌ها می‌شود
🔹
تغییر از انتخاب‌های کوچک ما شروع می‌شود.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/652919" target="_blank">📅 22:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=RPmfedyYbP0uLmhZtt2bQdPofKO-urTu034l3jFcShcIyfhgv-_z3xohY_goyqwlQDQFnLihdSmqTxAjAeeprIdHHaAee2qKP2q9iPLfVqOUKKzIZ1KuS9Xcl22Hf0ujO5p3WML4btpXnylkMwcpKgtCBB1WWvE-ehQSxEaqqjQ9Cf8m_vTuExPq22LtF-jkfUUzz5i86W1p0XWl7GL2_hYXpCp30-WfxW6-8Q5FytBLMgI1u1XvDOhY7ofu0go3brn73HQ3DSR5unebzjIUYf-e3SAeI0QJCQXHxuEOxBfLWMae41o7gDjgQTS-6lm2rdTjtyf4iGA-3YcVe-v90Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=RPmfedyYbP0uLmhZtt2bQdPofKO-urTu034l3jFcShcIyfhgv-_z3xohY_goyqwlQDQFnLihdSmqTxAjAeeprIdHHaAee2qKP2q9iPLfVqOUKKzIZ1KuS9Xcl22Hf0ujO5p3WML4btpXnylkMwcpKgtCBB1WWvE-ehQSxEaqqjQ9Cf8m_vTuExPq22LtF-jkfUUzz5i86W1p0XWl7GL2_hYXpCp30-WfxW6-8Q5FytBLMgI1u1XvDOhY7ofu0go3brn73HQ3DSR5unebzjIUYf-e3SAeI0QJCQXHxuEOxBfLWMae41o7gDjgQTS-6lm2rdTjtyf4iGA-3YcVe-v90Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان ارشد نظام معتقد دارند که باید در مقابل اقدام محاصره نظامی آمریکا، پاسخ نظامی به دشمن بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/652918" target="_blank">📅 22:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgAk5OV_XOEvcwZzt5_yCBGYzc7UJCiUrTRkZxtWemjAUuxmzq6Ayxl4WIKsMuREE5nwZmm4AYy9NZOWWAGguzgSpIXbUnjkwB7pYHT67tm8iwYMkU3hMhrgnWJhP7Keh3RKIn9ak-SmvbomErUKbRF5r6hsxhirk5pPzrxlT_f9mvF7VRi6-vsCJjZf_bWERW7mb3xMbqq2AhyG1CReyX-zw1gBB8myoyYn2PAk7on8eoxuk7XcTO591L8YRB9I4PcBwJqzAapviTZrAgiLP0sCiMrbdu5u27zHd2-YalDpjRw9JN424dAn4P9cN69-OyDiDpF3LpGg7GxLKWigxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برهه حساس کنونی
🔹
در شرایط حساس کنونی که تنش نظامی با آمریکا تحریم های فلج کننده و محاصره اقتصادی معیشت مردم را با دشواری بی سابقه ای رو به رو کرده انتظار می رود نهادهای ثروتمند حاکمیتی و دولتی پای کار آیند. این نهادها با تزریق سرمایه خود در اولویت های کلیدی اقتصاد کشور، نه هزینه، بلکه سرمایه گذاری راهبردی برای عبور از بحران و پایه ریزی شکوفایی پایدار انجام دهند؛ ورود به موقع این نهادها، ضمن حفظ آرامش بازار و کاهش فشار بر اقشار آسیب پذیر زمینه ساز اقتصادی مقاوم و خودکفا خواهد بود. چنین عزم جمعی هم به نفع مردم و هم تضمین کننده امنیت ملی و استقلال اقتصادی کشور است
🔹
هفتصدوپنجاه‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/652917" target="_blank">📅 22:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پدافند هوایی جزیره قشم فعال شد
🔹
شامگاه دوشنبه پدافند هوایی جزیره قشم فعال شد.
🔹
هنوز مسئولان توضیحی در رابطه با چرایی فعالیت پدافند جزیره قشم ارائه نکرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/akhbarefori/652916" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671233beec.mp4?token=JQ4WIcdsmAQxTQ3Y88XkLQA6dfaXpaDFIpNp3U8xj3dI5ZBkEcmytH7LO7cjvbW2zqOuC8azsJVHwNyTBz6rmM--iEFOX56p8JK6BqbYyAW7wM067_VXtcu27AJ7K3ocE_Rbb9M2mqi5IJ9-Q93VSF9NuvBYJeWKgxnMkjlnEgQwENWyk79xq6DYRM5_zomc5N8o9Q2VZLw-Xkoq7WeBBbAIqo_BsR4GuzTW39fhGPgHXofGJXNfpaJxTCgh0OA7KNMUJynJVKtxUdmuGrxeXLqrepBtMJEXrwIT5cUjdVDModeoG0R4ruz87lK6lQYEIJ01EfUOKDS080DmCPlZmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671233beec.mp4?token=JQ4WIcdsmAQxTQ3Y88XkLQA6dfaXpaDFIpNp3U8xj3dI5ZBkEcmytH7LO7cjvbW2zqOuC8azsJVHwNyTBz6rmM--iEFOX56p8JK6BqbYyAW7wM067_VXtcu27AJ7K3ocE_Rbb9M2mqi5IJ9-Q93VSF9NuvBYJeWKgxnMkjlnEgQwENWyk79xq6DYRM5_zomc5N8o9Q2VZLw-Xkoq7WeBBbAIqo_BsR4GuzTW39fhGPgHXofGJXNfpaJxTCgh0OA7KNMUJynJVKtxUdmuGrxeXLqrepBtMJEXrwIT5cUjdVDModeoG0R4ruz87lK6lQYEIJ01EfUOKDS080DmCPlZmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان ارشد نظام معتقد دارند که باید در مقابل اقدام محاصره نظامی آمریکا، پاسخ نظامی به دشمن بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/652915" target="_blank">📅 22:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4a8639f1.mp4?token=YaTtUv2rp9ez81lca5XSvPcIm-RtUZmpY_c7IBLEORFLflyHkXqn4-H7JGDrIfMtdqrFaEh3pHAOaTjOPe8bkxfOty6jVStV8lrtPnwHX7apCa3MtroYZb4HzP7Bc7TKBP-0ztbgdGeDMnlmzXlC5ubExddlj0MKyFmzFlVNNWSjlsQCRhtqgElb3pbPrjNdDyeDCQdLsK997BHeN9i_c0O-L5lKTbOlS6G13pVEMlBRjIbv_2wujUqBLgu0ROzg2uMiMmI0hOPYWZ0droG2LRLj-paihLIF40i2NJZrJMbR2C_VwvGSymr5zLqzT_HLxvz3Ut-sOGU8AbH2dAryE33rQS-Q1NPhkOsa_roTKGQuE3uD41XkacnBQmMryF9SJbgZSs6fIPuO40Bn2hmbWUAzRxXjUGG3kXxJVWSbJGGn-VTHugknZYVwmoqO1QqlvXDWoQ9CAjr9NPgTang7mdCuXksf6Xo89M_uFx31dZuIfo37hbrrV4XX5nDlfo8wLMR8LjIzsR6er_XboX_Nt18q-6KriLoM3voDMtmu0Kb9V7b2lqNG5G8YBiMM673P8WPA_t0VuATRz9kUQztP4QX1RxsYFfEZTKKlM4WuU-4loHkKmNauRw3YQb_A-Ozm6GBTIdhCmZ47mC01BJAGeLqPy4aQenHzBq7nbR2SrIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4a8639f1.mp4?token=YaTtUv2rp9ez81lca5XSvPcIm-RtUZmpY_c7IBLEORFLflyHkXqn4-H7JGDrIfMtdqrFaEh3pHAOaTjOPe8bkxfOty6jVStV8lrtPnwHX7apCa3MtroYZb4HzP7Bc7TKBP-0ztbgdGeDMnlmzXlC5ubExddlj0MKyFmzFlVNNWSjlsQCRhtqgElb3pbPrjNdDyeDCQdLsK997BHeN9i_c0O-L5lKTbOlS6G13pVEMlBRjIbv_2wujUqBLgu0ROzg2uMiMmI0hOPYWZ0droG2LRLj-paihLIF40i2NJZrJMbR2C_VwvGSymr5zLqzT_HLxvz3Ut-sOGU8AbH2dAryE33rQS-Q1NPhkOsa_roTKGQuE3uD41XkacnBQmMryF9SJbgZSs6fIPuO40Bn2hmbWUAzRxXjUGG3kXxJVWSbJGGn-VTHugknZYVwmoqO1QqlvXDWoQ9CAjr9NPgTang7mdCuXksf6Xo89M_uFx31dZuIfo37hbrrV4XX5nDlfo8wLMR8LjIzsR6er_XboX_Nt18q-6KriLoM3voDMtmu0Kb9V7b2lqNG5G8YBiMM673P8WPA_t0VuATRz9kUQztP4QX1RxsYFfEZTKKlM4WuU-4loHkKmNauRw3YQb_A-Ozm6GBTIdhCmZ47mC01BJAGeLqPy4aQenHzBq7nbR2SrIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: اگر تنگه هرمز باز شود جنگ بعدی با شدت بیشتری شروع می‌شود/ اگر اورانیوم از ایران خارج شود دشمن احتمال دارد با بمب اتمی تاکتیکی به ایران حمله کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/652914" target="_blank">📅 22:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 50</div>
</div>
<a href="https://t.me/akhbarefori/652913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاهم
رائفی‌پور:
🔹
0:07:50 چرا ائمه را واسطه بخشش گناهان قرار میدهیم؟
🔹
0:17:30 گریه سند محبت به اهل بیت است
🔹
0:22:30 ارزش قلب انسان ها برای خداوند
🔹
0:31:20 جایگاه بهشتیانی که به مقام رضایت رسیده اند
🔹
0:43:30 سنت خداوند برای مؤمنین
🔹
0:48:00 طولانی‌تر شدن عمر با انجام مستحبات
🔹
1:07:00 تحلیل اختلاف نظرات در شیعه و اهل سنت
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/652913" target="_blank">📅 22:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9755b4156.mp4?token=N0oqNqWV-7sJ_SuNkmZuDfWUO5buISp4T2j-lgD1_JJAlm2nfVi0_7-K2yzqr_mRcDWEXnAVI2UU4Xk8efpBAgvqVeA7zpMk9Edz4rI5J_it-8b6hQApGTtcUuewaTlrEx_fQ_X7ZNCqxzKl5Tito8cvva5iZ0IaA-jIDSgHj94nPew15Uh2kdvwNBCsLMozF_HKUGc12LZJyZkR_WI5j-e5BE3FOj-AbQeNoNqe1GQ1mi1V9DziymUn6EfaAakp-oWddFnzOr6qK_DW63nMAayIUrmMvcrLpQ4OHXTE96cNiK85PqzLtZu283aC4MNLpV0c1ws448YK6Ku8VlTOf12uYnO907nUZ5HkNxsM6fZaf859jCanL4lpLMJwxA8UW6g82Dg34oW5PRd4xeulWF0xL1ZreYh8pfyJoDbF6QRz6nZWISiw60pHIZETmSBidruIvtHn3EOGzYNKwe8Nwa0AxW9YfcRZdQxFciCtu59bDggdNPGOgLYvIZZyQfLv2MHT3R8iZU-S7uxnkTORX7Aw7DFe0VGQOSWB3adAxDAumLuUxWE1zGUxS7kCDOw701jg2EykvT6uRHvx8wi0H14fl13DmRgXU0mWuPBmRhUMP9p7D7wZIG4ZkEi9UVC00e4luvPqjQ9geuk4o6jN9ViEsTg50pRPJe4mWKPgCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9755b4156.mp4?token=N0oqNqWV-7sJ_SuNkmZuDfWUO5buISp4T2j-lgD1_JJAlm2nfVi0_7-K2yzqr_mRcDWEXnAVI2UU4Xk8efpBAgvqVeA7zpMk9Edz4rI5J_it-8b6hQApGTtcUuewaTlrEx_fQ_X7ZNCqxzKl5Tito8cvva5iZ0IaA-jIDSgHj94nPew15Uh2kdvwNBCsLMozF_HKUGc12LZJyZkR_WI5j-e5BE3FOj-AbQeNoNqe1GQ1mi1V9DziymUn6EfaAakp-oWddFnzOr6qK_DW63nMAayIUrmMvcrLpQ4OHXTE96cNiK85PqzLtZu283aC4MNLpV0c1ws448YK6Ku8VlTOf12uYnO907nUZ5HkNxsM6fZaf859jCanL4lpLMJwxA8UW6g82Dg34oW5PRd4xeulWF0xL1ZreYh8pfyJoDbF6QRz6nZWISiw60pHIZETmSBidruIvtHn3EOGzYNKwe8Nwa0AxW9YfcRZdQxFciCtu59bDggdNPGOgLYvIZZyQfLv2MHT3R8iZU-S7uxnkTORX7Aw7DFe0VGQOSWB3adAxDAumLuUxWE1zGUxS7kCDOw701jg2EykvT6uRHvx8wi0H14fl13DmRgXU0mWuPBmRhUMP9p7D7wZIG4ZkEi9UVC00e4luvPqjQ9geuk4o6jN9ViEsTg50pRPJe4mWKPgCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: اگر تنگه هرمز باز شود جنگ بعدی با شدت بیشتری شروع می‌شود/ اگر اورانیوم از ایران خارج شود دشمن احتمال دارد با بمب اتمی تاکتیکی به ایران حمله کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/akhbarefori/652911" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDdZ92QK19UF28YB38ltT27qdlczpPPMmo7Uyv2jNJtZmS6imGbSeq4K_yvwhMgzHL3zO-5TteHRh3uGobSvs9XHIsWR8gE6D3XsyXDQCY4falxHdpAYL_fUhRq0ua_38XNVbmCdXcmmlP7L_VuljgAl0BhaQPHlNCKQ0TuSedR3CfO-I--WMfY30sUrxTlJTkqU13W2bFqrAfcQq8bqiQ9nnuGZrZEhb-Nwg4pdlLEXwh5VlC9a21iw05bE1we3v4HTi7vk67JvtLdwvlU3g8bjZGBVM6eTNFdaePdgwrCwnkdbz1A8fBaihZwKy9V-GUr9sSCjOqkD_KCds3I7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود
🔹
رئیس‌جمهور: گفت‌وگو به معنای تسلیم نیست. جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود و به هیچ عنوان از حقوق قانونی مردم و کشور عقب‌نشینی نمی‌کند. ما با منطق و با تمام توان، تا پای جان، در خدمت مردم و حافظ منافع و عزت ایران خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/akhbarefori/652910" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3lB_kHDZBjTxr27dW9gtcejawTprYEDDdVH9EqrmeeKx9O3j4jbGJMNCfmVpWV3YvPs7WYGBOVe6Taqf69wpmXDZE3qr2mrMYL6u0H7E2_4eovdrgobG3LU8hWCWvDfSseMmyqLuanYRWABsvhSRijnXuuSefcJXVSLpxQ3T2enQru8vtV6e8At3dF4xYqoxAmgyU5QGDzMGD0P-n7se5jJO_0SzkMyA2nyfROzqaaMWh8RwL1h4HemuiZtJy8_OB0PLBdCo6S1FiB8X04iyJCzL3f-oMo_gZ__YMa3jXU-Hvk-qiRsrN5Xb6J1GIi3wUGROUNXWsws_aBv7mxEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: بحران جهانی انرژی در آستانه نقطه عطف خود است و احتمال دارد قیمت نفت به ۱۸۰ دلار برسد
🔹
جهان با آغاز فصل تابستان به مرحله خطرناک‌تری از بحران انرژی ناشی از جنگ ایران نزدیک می‌شود.
🔹
تقاضا برای تهویه مطبوع و سفرهای تابستانی در نیمکره شمالی، فشار بیشتری بر ذخایر نفت خام، بنزین، گازوئیل و سوخت جت وارد خواهد کرد؛ در حالی که ذخایر جهانی با سریع‌ترین نرخ ثبت‌شده در حال کاهش است.
🔹
تحلیلگران هشدار می‌دهند که اگر تنگه هرمز همچنان بسته بماند، احتمال جهش قیمت نفت برنت تا ۱۸۰ دلار در هر بشکه، جیره‌بندی گسترده سوخت، تعطیلی صنایع و بروز یک رکود اقتصادی جهانی وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/akhbarefori/652909" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فلایت گلوبال: آمریکا بیش از ۴۰ هواپیما را در جریان نبرد هوایی علیه ایران از دست داد
🔹
براساس داده‌های فلایت گلوبال، ارتش آمریکا در جریان بمباران هوایی ایران، ۴۲ هواپیما از دست داد یا به آنها آسیب قابل توجهی وارد شد.
🔹
از زمان آغاز عملیات، نیروی هوایی آمریکا تلفات جنگی قابل توجهی را در طیف وسیعی از هواپیماهای بال ثابت و بال متحرک متحمل شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/652908" target="_blank">📅 22:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fff9e2e.mp4?token=YRVgUC5Izp71q4Y7nOaznQpPpHceAo0ZiCUjZhRgoTTTpmf0W6B9vVTHCUISgO0NhoB7YSUvO6V77sfOcnlNB15HLWjmBXJXI3Jvnx376cdlZ0eQgXNA9Mcgrp-C8u4cJWH7p-diJsT9gr9rL5TTgGEns9Pd3CAr6TYdwaTXT9ltMiT0Htk4BomI7M_a4N-_sf5M_5neNuYWSxCWs3rwg5oss-9_955JoeonBEbfPpe7yjdI3PNZtnnAguOx56IKV2fDGbuHXdpGUANx0KM2tZdLjMbQWQf__ni5ywM-NNwJFlCG5vXg7BPj5gSAy2-HX7KfvPNsP8oDabu1TTQSbTt4-5WSXrLKwtR-kXiSSyYCC-NzHixbCo3bJ09-GYoG3NpV9qE0MooJrNbgz29XxCyJwg0HzuKtJKyVcVtzH2p-9QZB2IsGp2j4Ht2_4umMbZaj6LzTlysNCK11EynvvOB-OrLF649sUORtOJrCDdQ5sqPjyPTnDebiaYf9tMzRQ_REjol-6cBwAXUehpTvlh-rDrlu7i70N-Djn1ezdodNz3Bfux-W11pxfV42Y5GIKORB-Zu4xWtpeJnY3p5K2vIvaCN-D_ivczeAHqhfK6d6vC9TSFQRWJ-ZP067Y25fBCYOn5JQN1YSgx0_HsWQafLmU09o7k9D-L8YZmiFP4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fff9e2e.mp4?token=YRVgUC5Izp71q4Y7nOaznQpPpHceAo0ZiCUjZhRgoTTTpmf0W6B9vVTHCUISgO0NhoB7YSUvO6V77sfOcnlNB15HLWjmBXJXI3Jvnx376cdlZ0eQgXNA9Mcgrp-C8u4cJWH7p-diJsT9gr9rL5TTgGEns9Pd3CAr6TYdwaTXT9ltMiT0Htk4BomI7M_a4N-_sf5M_5neNuYWSxCWs3rwg5oss-9_955JoeonBEbfPpe7yjdI3PNZtnnAguOx56IKV2fDGbuHXdpGUANx0KM2tZdLjMbQWQf__ni5ywM-NNwJFlCG5vXg7BPj5gSAy2-HX7KfvPNsP8oDabu1TTQSbTt4-5WSXrLKwtR-kXiSSyYCC-NzHixbCo3bJ09-GYoG3NpV9qE0MooJrNbgz29XxCyJwg0HzuKtJKyVcVtzH2p-9QZB2IsGp2j4Ht2_4umMbZaj6LzTlysNCK11EynvvOB-OrLF649sUORtOJrCDdQ5sqPjyPTnDebiaYf9tMzRQ_REjol-6cBwAXUehpTvlh-rDrlu7i70N-Djn1ezdodNz3Bfux-W11pxfV42Y5GIKORB-Zu4xWtpeJnY3p5K2vIvaCN-D_ivczeAHqhfK6d6vC9TSFQRWJ-ZP067Y25fBCYOn5JQN1YSgx0_HsWQafLmU09o7k9D-L8YZmiFP4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا موشک‌های ایران، توان انفجار در مدار لئو و از کار انداختن ماهواره‌های آمریکایی را دارند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652907" target="_blank">📅 22:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520d4aef71.mp4?token=XS6t2QoVhWtHc8szq5QbFnBoxPN8_2XrYH6kIZvhNJT-0guog6lyo1TjQIEJCnK1JPagVx6CLU5hD5Fsk4Ma_H13DBYc-C544DbB3bSj_2fpzfiWzSwq_hyxIljKZ7PYyKF9P1YAE88ZIe54ukblOjDpQS1Tqaw0Sp5gQ7B6_P9iX4XpMic6JkT2gDMTwx2EVt1OhRAEGQLwgPrGRZmybNH5-rysLvChmT_NxPhbsRyIaf8MxOe4i4MlH0vgtPVaeAfwyxKgq7Sx57Pzg0EbCp5gg8v6xG1QbKoMPAN8QoA-VD7sKDXdzjg0dIGnhfKZvEvOXG5uaby2O5rQOfCYhngWVTHKWg4whkAWB2ZMG7_oHDj_jwUw7F7kNHnX9Joh0H85UfDHU7KyMd64CfcB9PmzxGVqPwglpsZq5hA1vWwaTCXABLXhdTaN49wUrydLQN3cQ_p1_ZzahSGBa7CD3pON27JcPXeIk4e1AvKpIc5OVFMTE_6X_SnQ7FR1ELHrzCTxxKstLbaBZ8UldHGUJxOVzfkyOBzntnlslU7LPGk--sxw9NA7uzPNRJQZyWod_BfZrJQqvU8-q_B2LmF075LyiKCbnkYxDYe6vbXe1O2vx8nW-GhviB1D4iqbVVKtuvZ6Ad2Izxo0pXuNcgGnJ7CwimbPXz8k-084PuP-qS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520d4aef71.mp4?token=XS6t2QoVhWtHc8szq5QbFnBoxPN8_2XrYH6kIZvhNJT-0guog6lyo1TjQIEJCnK1JPagVx6CLU5hD5Fsk4Ma_H13DBYc-C544DbB3bSj_2fpzfiWzSwq_hyxIljKZ7PYyKF9P1YAE88ZIe54ukblOjDpQS1Tqaw0Sp5gQ7B6_P9iX4XpMic6JkT2gDMTwx2EVt1OhRAEGQLwgPrGRZmybNH5-rysLvChmT_NxPhbsRyIaf8MxOe4i4MlH0vgtPVaeAfwyxKgq7Sx57Pzg0EbCp5gg8v6xG1QbKoMPAN8QoA-VD7sKDXdzjg0dIGnhfKZvEvOXG5uaby2O5rQOfCYhngWVTHKWg4whkAWB2ZMG7_oHDj_jwUw7F7kNHnX9Joh0H85UfDHU7KyMd64CfcB9PmzxGVqPwglpsZq5hA1vWwaTCXABLXhdTaN49wUrydLQN3cQ_p1_ZzahSGBa7CD3pON27JcPXeIk4e1AvKpIc5OVFMTE_6X_SnQ7FR1ELHrzCTxxKstLbaBZ8UldHGUJxOVzfkyOBzntnlslU7LPGk--sxw9NA7uzPNRJQZyWod_BfZrJQqvU8-q_B2LmF075LyiKCbnkYxDYe6vbXe1O2vx8nW-GhviB1D4iqbVVKtuvZ6Ad2Izxo0pXuNcgGnJ7CwimbPXz8k-084PuP-qS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: آمریکایی‌ها حتی پول بلوکه شده ایران را هم آزاد نمی‌کنند چه برسد به این که غرامت بدهند/ آمریکا قرار بود قبل از مذاکرات اسلام‌آباد، دارایی‌های بلوکه شده ایران را آزاد کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/akhbarefori/652906" target="_blank">📅 21:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل: اسرائیل پیام‌هایی از آمریکا دریافت کرده است که حاکی از آن است که ده‌ها هواپیمای سوخت‌رسان آمریکایی که در حال حاضر در فرودگاه بن‌گوریون مستقر هستند، انتظار می‌رود حداقل تا پایان سال در آنجا باقی بمانند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/akhbarefori/652905" target="_blank">📅 21:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391adcbf76.mp4?token=rbbiNbhHoIYv-YTs-DcrNg2m0TnZju-vfsS-wQXMHkbFYuDUK0_rnjtYixMuF2_9daEFrr-MlhW3MtMVyl5HXD9HvcPkQBtgnbnEUckzo__rLOneQG8sVRJ2paJdI6Jo319Lasq9Y9VZhufv99QoRRbLsPCLhviKYDBrwlktQva8TPvJSNsjFcObzw_qlF9qgocSmGysny9s-ExZUijyKjhB_6lFmu8ia4HujMOTXWReZ4ps9Sa7scbM3RHsj19Ps4UTueKuzuSp8lfYVdwj2_Ey5NvIwu8TwzLGB2Qjb6Oe-igloMyQNeRVrdI99joanBKFjB9RuNFLPck2Ob_pMhOT_OrC7qG_Lwfl2h6ccrJbCYvdVWh71mF6-pJdVjWbmXlPNTdEuvko_HBjDxP_nKOvnXYLnIy_2OWHLat03ayO6L4O5uhaDtdZCv4WPUAqCMkjfVoSVJHqOKbwlGz7pqzg1JUysnDcq1ivdXGqVg9PEYdnYj4BD0G1xd75Oa1dOvfug45jebS2DqOdfXMXTRKKmITuY3H0QlylVUoYlM-j1XDWJIQwpDh3be1jT0L-KAsUODonF1VqRNT4iEyMzPiyPCZIsJ8LY6-uTEvgOJX6bqqJIVgyRt0We7oYMfP2vj-801T00Nx-bgKJ3rVrM1ri_M1p9Kceds7VsQTZqe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391adcbf76.mp4?token=rbbiNbhHoIYv-YTs-DcrNg2m0TnZju-vfsS-wQXMHkbFYuDUK0_rnjtYixMuF2_9daEFrr-MlhW3MtMVyl5HXD9HvcPkQBtgnbnEUckzo__rLOneQG8sVRJ2paJdI6Jo319Lasq9Y9VZhufv99QoRRbLsPCLhviKYDBrwlktQva8TPvJSNsjFcObzw_qlF9qgocSmGysny9s-ExZUijyKjhB_6lFmu8ia4HujMOTXWReZ4ps9Sa7scbM3RHsj19Ps4UTueKuzuSp8lfYVdwj2_Ey5NvIwu8TwzLGB2Qjb6Oe-igloMyQNeRVrdI99joanBKFjB9RuNFLPck2Ob_pMhOT_OrC7qG_Lwfl2h6ccrJbCYvdVWh71mF6-pJdVjWbmXlPNTdEuvko_HBjDxP_nKOvnXYLnIy_2OWHLat03ayO6L4O5uhaDtdZCv4WPUAqCMkjfVoSVJHqOKbwlGz7pqzg1JUysnDcq1ivdXGqVg9PEYdnYj4BD0G1xd75Oa1dOvfug45jebS2DqOdfXMXTRKKmITuY3H0QlylVUoYlM-j1XDWJIQwpDh3be1jT0L-KAsUODonF1VqRNT4iEyMzPiyPCZIsJ8LY6-uTEvgOJX6bqqJIVgyRt0We7oYMfP2vj-801T00Nx-bgKJ3rVrM1ri_M1p9Kceds7VsQTZqe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ، ترور، تحریم، محاصره، آیا گزینه دیگری هم روی میز آمریکایی‌ها باقی مانده است؟
🔹
وقتی آمریکا با کارت‌های سوخته‌اش بازی می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652904" target="_blank">📅 21:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkK9ousmcllm39yrGCcxka3WSOqZYaoEc-HjS8L02xpJSQXip5uriPwNFJRNZtXIfJwhbVmc3gVChX0glQVFK2ecy5lMNZB1Rdyzz6WFWTwp6LLKL2KEYlB_akVc2izbphU8Oewg0nNhgaH5LDu6BpKPMRB1bk33ByKNNy7Tl5u2igKP-ph_IlAVe9RwedqmKLW1TbSDzOPBW-gvAxHiiedS9ZfMY6t9ypFvCLvsdtuwK2mLIBusmOs7C_96ONTxmkjelAd5KjE7075svqg9LnMJdTh5ArO1eOjw5rizmauiC0cjd5SQtFq7iAoC8mFJ93CaxtWh391TNPXO0KkV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از روز رئیس‌جمهور شدن ترامپ کدام بازارها سود‌ده‌تر شدند؟
🔹
از زمان تحلیف ترامپ در ژانویه ۲۰۲۴، نقره با رشد ۱۵۰٪ پربازده‌ترین دارایی بوده و طلا با ۶۸٪ در رتبه دوم قرار دارد.
🔹
شاخص‌های سهام آمریکا (نزدک، S&P ۵۰۰ و راسل ۲۰۰۰) نیز رشد مثبت اما تک‌ رقمی تا ۳۳ درصدی ثبت کرده‌اند. در مقابل، بیت‌ کوین با افت ۲۴٪ تنها بازار زیان‌ده این دوره بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652903" target="_blank">📅 21:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، حمله رژیم صهیونیستی به ناوگان صمود را محکوم کرد
🔹
اردوغان: امروز بار دیگر شاهد بودیم که چگونه اسرائیل با ذهنیتی فاشیستی اداره می‌شود. نیروهای اسرائیلی به ناوگان جهانی صمود که حامل کمک‌های بشردوستانه به غزه بود، در آب‌های بین‌المللی حمله کردند. من این عمل دزدی دریایی و راهزنی علیه مسافران ناوگان که از شهروندان چهل کشور مختلف تشکیل شده‌اند را قویاً محکوم می‌کنم. امروز بار دیگر تأکید می‌کنم که ترکیه در کنار مردم غزه و کسانی است که دست یاری به سوی غزه دراز کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/652902" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuuhQH-t1U4rIjWQXqY3IZQRW-3OWlYsjDuRKIjJsimCIp0ZMwGTrPpU4ZZISSZNPqsxgKva7559_x9XhFUJw5GJsIP8BmKc-m0RbHAoZbJK90W7_jM9clRgFemt8qPw5fqVKLKS47kdT7_uq-6cXnSQpsUzRt_8n8j0BVoTW7k2NBiMqurgy7x1X0GwrNJvU6kUXHXVHgoX-jfLapQuF3QI706mJMbN9TH6Q54DvAHdyyklv_pMQGbFM3ZGYggKbSDWuooH-04aB77nzp3UNjXLJ_y_oUvxF_oY6cYHO2v41rK73poSP0lm1WdQ_ybsCw_93O1nFjjJrkX4iAZykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت نیویورک تایمز از «دو پایگاه مخفی اسرائیل که ماه‌ها در صحرای عراق پنهان مانده بود»
🔹
اسرائیل بیش از یک سال را صرف آماده‌سازی دو سایت مخفی در عراق برای عملیات خود علیه ایران کرد.
🔹
وجود این پایگاه‌ها سؤالات سختی را برای عراق ایجاد کرده است؛ و نشان می‌دهد عراق که در کشمکش بین آمریکا و تهران گرفتار شده، همچنان قادر به اعمال کنترل کامل بر قلمرو خود نیست.
🔹
افشای این پایگاه‌ها می‌تواند تلاش‌های آمریکا برای مهار نفوذ ایران در عراق را تهدید کند. همچنین این اطلاعات نشان می‌دهد که حداقل یکی از این پایگاه‌ها از ژوئن ۲۰۲۵ یا زودتر برای واشینگتن شناخته شده بود، که به این معنی است آمریکا حقیقت حضور نیروهای دشمن را از عراق پنهان کرده است.
🔹
این پایگاه‌ها برای کوتاه‌تر کردن مسافت پرواز هواپیماهای اسرائیلی به سمت ایران ایجاد شده بودند و کاربرد موقتی داشتند. اکنون پایگاه النخیب دیگر فعال نیست، اما وضعیت پایگاه دوم مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/652901" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت ۷۵ همت گندم خرید
مجید آنجفی، معاون امور زراعت وزارت جهاد کشاورزی در
#گفتگو
با خبرفوری:
🔹
برداشت گندم در ۱۰ استان آغاز شده و تاکنون حدود ۱.۵۵ میلیون تن گندم به مراکز خرید تحویل داده شده است. با توجه به تامین مناسب نهاده‌ها و بارندگی‌های مطلوب، تولید گندم امسال به ۱۳.۵ تا ۱۴ میلیون تن برسد و حدود ۱۰ میلیون تن آن توسط دولت خریداری شود.
🔹
ارزش گندم تحویلی تاکنون حدود ۷۵ همت برآورد شده و قیمت خرید هر کیلو گندم بسته به کیفیت تا ۴۹۵۰۰ هزار تومان تعیین شده است. دولت در حال آماده‌سازی برای آغاز پرداخت مطالبات کشاورزان است
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/akhbarefori/652900" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak8lSbgKFLWg6Ck09fM2x6BMhZh9Qq7sAzV5MW9vuNxpFvUtLD2p5-4sQbhI8iwlW3QnnpLJz_1B9US9vPRMfo3J5tzthjyzVHXiQpfN-iIh9N57XK2rlUkPjVB5FxMz-ymBEEbtIh7A_rlegFIY6nV5L3sD-6CXSpR7ket5esFR6nLwCJKar-BOJQziWAU61OmkaGQkqNiPmACazAJJdKF9odPUumwTaL8vi1yVk6lQfTYgIPmZbzpoQVbKALKnf42XasMx3Sdc7MOEdimzHPGVQYMpMTMBP_t_YfAUzfIjV24Q4s4uJwuRymWva6WmVM5AS6BityzyM5VcuHVLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه کار در ایران را تمام کنیم؟! | حمله به زیر ساخت، تصرف جزایر، تداوم محاصره، حملات شدید به شهرها، ورود زمینی به ایران: توهمات آمریکایی‌ها ادامه دارد
🔹
ست کراپسی رئیس اندیشکده «یورک‌تاون اینستیتو» و از چهره‌های امنیتی نزدیک به جریان نومحافظه‌کار آمریکاست که سابقه فعالیت در نیروی دریایی و وزارت نیروی دریایی آمریکا را دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216031</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/652899" target="_blank">📅 21:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40c662626.mp4?token=M5i0U3EtRzl0C_42qqR4QEHQhc5A-q7vdUnAI8JBESw3KQ-zC-UKO_pdZlIL9afK7sh7sK0kG88XYxdOncekq7t39Tf-aeOATzFry_Ij8UFq5Tt-4Lzg2gg1418Kuyh3oYgPeG-944LTsHA6BnT0Gm1EQSqmo7km6O59EA0o0eVLWKFLd2Nhggj00E8M10HV-qChkuO1bI4dAZwqr4qICzpmVZTIQZNcDJxPjPZTBhzYsBh7Ot7MEG2q2Ju-HlfSIDKMgCMCGqsCqa_i_CwUjYV_wZk13RVuQjIyrZ2g_l9lOOxkl3wW63MUj6bONwQB3jLBgqH1uuzkjHEcbTUBpl6ua5bbpQh1e9x5Ob7LBs-PcFaEBSVnvLAq96QX8IOjFUAKRfXbRLazz1Xg0RnCoaIjv4trLasJkgGIDkjfQ4dwiQLPvRr0JLFX-cHwaZzRcPtG4rP2RgQj1K6zxmPCWBOwzlF-iIwQMmezyF6w2ehn9-Rj9pSSdFGYgWjdZptmgjZ_oI_IUidp5bDyUHfDr5I9HXSVwTr6lKjjjPN766C-OiBOYQdr-wUZhMQv_e4cwtPtUcUyz80L8ChQqFRl4Doil5FW_l6vwnCglcofF4R9rGeA9tGD_QlN95QR7M7nlxjGodM3NVEvtTr4FzfnPPgDC8en-zB9dBlToY7B1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40c662626.mp4?token=M5i0U3EtRzl0C_42qqR4QEHQhc5A-q7vdUnAI8JBESw3KQ-zC-UKO_pdZlIL9afK7sh7sK0kG88XYxdOncekq7t39Tf-aeOATzFry_Ij8UFq5Tt-4Lzg2gg1418Kuyh3oYgPeG-944LTsHA6BnT0Gm1EQSqmo7km6O59EA0o0eVLWKFLd2Nhggj00E8M10HV-qChkuO1bI4dAZwqr4qICzpmVZTIQZNcDJxPjPZTBhzYsBh7Ot7MEG2q2Ju-HlfSIDKMgCMCGqsCqa_i_CwUjYV_wZk13RVuQjIyrZ2g_l9lOOxkl3wW63MUj6bONwQB3jLBgqH1uuzkjHEcbTUBpl6ua5bbpQh1e9x5Ob7LBs-PcFaEBSVnvLAq96QX8IOjFUAKRfXbRLazz1Xg0RnCoaIjv4trLasJkgGIDkjfQ4dwiQLPvRr0JLFX-cHwaZzRcPtG4rP2RgQj1K6zxmPCWBOwzlF-iIwQMmezyF6w2ehn9-Rj9pSSdFGYgWjdZptmgjZ_oI_IUidp5bDyUHfDr5I9HXSVwTr6lKjjjPN766C-OiBOYQdr-wUZhMQv_e4cwtPtUcUyz80L8ChQqFRl4Doil5FW_l6vwnCglcofF4R9rGeA9tGD_QlN95QR7M7nlxjGodM3NVEvtTr4FzfnPPgDC8en-zB9dBlToY7B1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادر یکی از دانش‌آموزان شهید مینابی: دخترم روزه‌اولی بود و با زبان روزه شهید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/akhbarefori/652898" target="_blank">📅 21:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9688024d35.mp4?token=LBRjE5C7Xnc-Xp_3QtESTaYhdUGgId22TP7uOktWSAaA8C4lotYdPXVMDQmK-yPmkxnIBWfYBgh-S-T8JZknFSaIPpnqCVo9vhM8D1WNfXf_48qJ0HiXMBebbidlseywZsoqLK6WhtuZ-UlPXfMvZk5ZaFd4qIuZqenkt3xZItQ_kqL1zcw8IRW0Mugx46gxlGgiC-LCzPru2pjdnKoq4Tc6CuRp-iW5oxp34uyqjBFpiE9jjcPZnzWXMLNYd592JfhEab0lHSgjQ1FFYUsXTks_uUK6m8zfpaTob1w_3u8Ked3EiPOM_6IMLwDzCs8-UT52V7bUz4tEb2gyQi18bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9688024d35.mp4?token=LBRjE5C7Xnc-Xp_3QtESTaYhdUGgId22TP7uOktWSAaA8C4lotYdPXVMDQmK-yPmkxnIBWfYBgh-S-T8JZknFSaIPpnqCVo9vhM8D1WNfXf_48qJ0HiXMBebbidlseywZsoqLK6WhtuZ-UlPXfMvZk5ZaFd4qIuZqenkt3xZItQ_kqL1zcw8IRW0Mugx46gxlGgiC-LCzPru2pjdnKoq4Tc6CuRp-iW5oxp34uyqjBFpiE9jjcPZnzWXMLNYd592JfhEab0lHSgjQ1FFYUsXTks_uUK6m8zfpaTob1w_3u8Ked3EiPOM_6IMLwDzCs8-UT52V7bUz4tEb2gyQi18bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از سردار شهید محمدصالح اسدی، معاون اطلاعات ستاد کل نیروهای مسلح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/652897" target="_blank">📅 21:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
کمبود مهمات راهبردی آمریکا پس از درگیری با ایران
مرکز مطالعات استراتژیک و بین‌المللی آمریکا:
🔹
به گزارش منابع نظامی، نیروهای آمریکایی در ۳۹ روز عملیات هوایی و موشکی به ایران، مصرف بی‌سابقه‌ای از مهمات داشته‌اند. برای چهار نوع مهمات کلیدی، آمریکا بیش از نیمی از ذخایر قبل از جنگ مصرف شده است.
🔹
بازسازی این مهمات به سطح پیشین، بین یک تا چهار سال زمان نیاز دارد؛ چراکه تحویل محموله‌های جدید زمان‌بر است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652896" target="_blank">📅 21:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec7a93b6b.mp4?token=UUZgw_BefFgMP1Mh5GpiQSAFA9b_mTVDVY_Q_4rZ0g50H1Nipoh4b68iuZ4vZBrIt1eXljGFxawFnglCt8TvcWvwAAUkqm1V7l484C__U9T7iJpqJNxJeeqxK5CYn2wb5fLqlzNLD5A-LPvdkdHa1VylqiNYb8vrM5blgeGaf4S7oScodiV3BOmJXmjGjjUPjnq3GV43HXbjfvHYO_QdoWHdUP2oCzWU626xAHd-Hi2UQnrM2EhnMcZYzVMRY4c5WFOYzXd3GACqFPJfPOtZRw38_OcCTQJxJPsD8pCs1LB9upUsdZx9v7CfbLlbs0_oeHBcG8hleTmPCnr6X3OjW67hYntOc4kQHyo9sRXpPyMiXY2026pr1Ax3LaMXZvj02LQq_OnQhF0MvqRdoRWPCH6r09b32I0CoUGIc2jvMlqIyjBcFIHzhdLtVZcTGPVXqrMl1O3Oa6sfv6iqN8bANE6VNFY4vTvifCRNwkuZeojJkaMTbUVgqAUfv6nejMsmBDDCiipDe2Q1DP7gdTRekgj1ZCtFoxw31aBsm-rW3TI_YEEb2EapLZJ7pAmDOKuCKlBlnvSXzvwpH9DDh88FtALGn-Z2B1e1j5iCb-H1OSqE-F-aSsyG1BS8ADTOniQvNglxv_1w1TqUsNCe_cCa9tw-6IHBPO-GYJEEIDZJn1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec7a93b6b.mp4?token=UUZgw_BefFgMP1Mh5GpiQSAFA9b_mTVDVY_Q_4rZ0g50H1Nipoh4b68iuZ4vZBrIt1eXljGFxawFnglCt8TvcWvwAAUkqm1V7l484C__U9T7iJpqJNxJeeqxK5CYn2wb5fLqlzNLD5A-LPvdkdHa1VylqiNYb8vrM5blgeGaf4S7oScodiV3BOmJXmjGjjUPjnq3GV43HXbjfvHYO_QdoWHdUP2oCzWU626xAHd-Hi2UQnrM2EhnMcZYzVMRY4c5WFOYzXd3GACqFPJfPOtZRw38_OcCTQJxJPsD8pCs1LB9upUsdZx9v7CfbLlbs0_oeHBcG8hleTmPCnr6X3OjW67hYntOc4kQHyo9sRXpPyMiXY2026pr1Ax3LaMXZvj02LQq_OnQhF0MvqRdoRWPCH6r09b32I0CoUGIc2jvMlqIyjBcFIHzhdLtVZcTGPVXqrMl1O3Oa6sfv6iqN8bANE6VNFY4vTvifCRNwkuZeojJkaMTbUVgqAUfv6nejMsmBDDCiipDe2Q1DP7gdTRekgj1ZCtFoxw31aBsm-rW3TI_YEEb2EapLZJ7pAmDOKuCKlBlnvSXzvwpH9DDh88FtALGn-Z2B1e1j5iCb-H1OSqE-F-aSsyG1BS8ADTOniQvNglxv_1w1TqUsNCe_cCa9tw-6IHBPO-GYJEEIDZJn1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک عجیب به بازار موبایل
🔹
گرانی موبایل این‌ روزها را که کنار بگذاریم، یک اتفاق عجیب دیگر بازار موبایل را تحت‌الشعاع قرار داده است.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652895" target="_blank">📅 20:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
آغاز پرداخت مستمری اردیبهشت بازنشستگان تامین اجتماعی از فردا
🔹
سازمان تامین اجتماعی: واریزی اردیبهشت به صورت علی‌الحساب و بر اساس آخرین حکم سال گذشته بازنشستگان پرداخت می‌شود.
🔹
احکام جدید با احتساب افزایش سالانه و متناسب‌سازی تا پانزدهم خرداد انجام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/akhbarefori/652894" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
چهار دسته اصلی نمادهای بورس که تعلیق می‌شوند
🔹
آسیب‌دیده مستقیم از دشمن: شرکت‌هایی که بر اثر حملات، دچار اختلال جدی در تولید یا فعالیت کلیدی شده‌اند.
🔹
آسیب‌دیده زنجیره‌ای: شرکت‌هایی که توقف تولید یا خدمات آن‌ها، ناشی از اختلال در شرکت‌های دسته اول است.
🔹
هلدینگ‌های وابسته: شرکت‌هایی که بخش مهمی از سودآوری آن‌ها (بر اساس آخرین صورت‌های مالی حسابرسی‌شده) به شرکت‌های دسته اول و دوم گره خورده است.
🔹
شرکت‌های سرمایه‌گذاری: شرکت‌هایی که بخش قابل‌توجهی از پرتفوی آن‌ها در سهام شرکت‌های تعلیق‌ شده سرمایه‌گذاری شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/652893" target="_blank">📅 20:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzOH60RzpV8xwP1JpBYHYI4OzFtJ0qmZrEkOWl9EQih9th8vR73-Eq680mwBRfDRbLxJsqMC_tfYOzxepDrwYaYA2lqP6JpYhb8fOiC9VODxvpTcNRqJGq1F0FADTVkkUfhhetEsVCqBLxDG7VTKwtAbyJfGpbVv6QDetHkacWYGl4RE6MIEpvhNr-_o5hZ3uF-5PefQdyYm8P1i7GE_5MO3mymgCzIO1oL6t-I2nXTpPA0vHFP672sBAZ4mJfYSONLDHCOqoIIZZSrCdTbJzsRwukSuZJ6N-n1EEnq-3c28-3u-LtbeVj2pGDo4B-gBCilWQlW4kU5dJSEbzWVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMsbEwPiBtwdUh_LHFbq8gvfRoA5_o26oVXzMNR3cYtYpy-LZO4Ksu5WN2myhZw4I0gl9iWnQCgvuxPFTC2fhiKZ8MMffgmgJajpC0MmpiPLKfjk5Lsm6XtDh5HTuqrZ1BiSFq3PqTjUOyXvzXDg9Dyt7lhlqjbVWlJ2mQwa_R4CzpX2SYwRDmYMJxUK5EjkGcaq8mxSM0KFyZAmItiqZZR2KAivDX_bvNONl3RV0j8_4VyQCegDes2K-w2yi0Gn4uwHkntok17GYoQo4nk_Vx-pcVSNJswnmLzPzhIKJdX0M4HyNLvGNslreQ68NmR0PvOoOepm3etq37OjGrHiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe9elpj7s-CvCyqdsoFsy2HPpnJd9QsUWKqnaFZBJsHsK23AkPCDoxkMxYhCKdCMp6_zg7fWU0mS-ckFxeZjdiU5jXzafo2yRXMki7lixrc1LWhy33MHQ3uUbdWHI8vJL66D70iI9vRl_h-bzHMWQHu90AN1Bvujud_T9oxYrkme7lTfE8mVVYAODY3LItxf46Env-2vLlnPvma3vnYd8Vkue9Odf8pRPHyRuPIjMylZa1jc-UTmNMiTYsgnHrF0NO6chu8vt_rduegS33zp06w_6RZ7aCoKwdzAofoQvifyz_SVg95JJSyQgmHUFhdJyCD7a1yD0bE_b2oUSjcYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iahqXZq2fiUCZO2dz4bg1G-wkbXFjBGsKWRAOubLncye7oGwtgAXZK3m-N038ckdy-vPv6e9ZbxIt1P7T9QtWlr6o0XVdwVEdevkKrdZbX211DqpsYXJgggCsMm6P4SIuKODMizaAyQQ61dwioVGIXBvccx7R_67_agccdiMhobpFZfumxTA92waXbK5ba_i6Q0AIsyizjPNrPC5C-38MoAHtvc_Rp_gKOQLnIy5fROTTwlsN46_i9tv8QfUR3QT0eaEcxEYjuezLKvjARXTo0oUjv6VKBkYeAWe3oVGM9V-41wHJ7v8rtCGKyrcNvJiaeYpl3aNlfW6VJBAqyPdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwkDPLlaHc1oz5YymmmKK_uanFW18HM6Dg5yNCTfBCcQfCQ7oThODRmS1msKV-UBUsDN2JMKBXd-jwRJOI7O5ZF5i6086OFCla68T6SWhO2267DDz_MhQGkOgwd7WyhP8RuHSnxIXW7Rhd2S7REsn0uGG_608vPPHPxxzNs1PUu5LMX3Dv-7S6arbezdZEHNUh3J8pcRrlAdSaoiI08zuAOJPsupVWiT9PGu-TVPrXAlvr_vHL4u7PrLqvCFZY_6QWc9fZs7flNg6zSdm6is59NMvGHiYoNrf-yyhyfzcP8OUg-WiXgIL01cGXK-MAUZIbEWXyU_-7qE_SCr6wOxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvkH4hutIWScLpuT50O8pNqFN54xB9iUPkzCTHBR6UYEqwwSdMDrEIAKQ-0JqfAQpwKPWIWwpgrO2L7495F-TyrHKh8x9DR3iE0iCdVGOoLutiFFzOXY8BTRyvNdUT_qVAxObEwS4GzRZN8V2i7c1sbRpDBdN8YvZR0jxihH62eQhnHpVQ0-Elg6jgfmO2QY8BF34C2KqFVrYNgLkinuBOJayug4ooUNdhltD29sCuh0D_FBZf-uaUjNCXpda3XEbDYZlsw4eNXlpArkJMSjt3bi_G3ZGFCZbhWwORO9hY6VqRt9DmmQ9X6CGZW9h0BYOJRFCv5BXIsTQKHbWQXh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yo_BWof7mTmUra3LgouEpOGt8FaSTfCIeBOiJvVVd8MPEhmQfaWdfuEZjR9QoAqdn4ytVP8zzxJt0RvHKEnECyjIdBCIICEjluIypCXHCMRfyIUOEVhhpJ3arHMlp8aXtSzNaEmFtnjkZMleVrXVTKQVo7hh_lVFcjjPeH8ark85ALiA1EMLnquq0iYAKhw41I4W9eyo_mvd6y6aCPvDUgd8HU_fscdp84JoleWQyRP-h8WbZpoA6PW3iZEi5jEEBIygWd7rHmBZxwMsdz_Xdtx6e6VjjDRW38YfM9dC1eEimPfo-d7M2ZIf2FSvkP3nNjcZmfTi9uUUALyIdZyTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndb0SlkxL1qt2R7YMxjiBCxPyQ7bCS8mYM5hZzRvp0CVhO75mtvRF7GomKTR1HrB6k_AMiMNmpQvaecQ59kga5ZWH2I_Q_G_GVHtOZeTZmwLtdVbIYq6ITRK8Kwxsk-i1ytn55nAZwo-9urNDtOsi0UaYoVtoX0W_cKUkMWVPxH5UtZrJxevv9DQTBziietwkNkUuSXN3iuuI7xmoRmrvHaBOzB9A8jMQDJrsmuBFNVd9vXNpLlop0EugdclsruqdOohzr_BbVvW-sTuRZCjutcXyVaPuOGSZ4SnGYHHE1SX4Na5i6pteH55TUAWIxsBGiJn55ONMwE0WGOt_HmQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYTgCsoWY0n92LhlPhONAJGU5odCzwYlE66HxnZ097KjGjXeqYwN-3wBWAC4Fkh2jodcr9zdRwWxwJyBm9fCDLhq5QnMVUNbOaR-JcpNDSio08BJYeCreVC60NJAhAVfV63ei_Vk6Cr7dw7_dRKHUrX10FS_v9hm2N-vt4IVFT8WhxTELEE8OOKgUxgyWb1-pMGs-nyxBlfh0_McwhlrwGr1l6FknVl415hKMHiposN4-hOgLENgeTvFl64CumN6T6gzZk6uaeZzAfJ1FviT_lsIPMFo0_AxsDbujDKjPKF7pI5Z9EdIyaCMhvtPxy358iiLeJR59fnjzmnH6SELMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLzpzFz2-pUj5gMjHTDQhVs0uQj6BPIOecGpGdIwRv8XTaZVskItzscRzuXlyjkdt3WesMBPUUg8RQJKPyjbdjmonok3P489MI5MYEp_iBocBnyyzFuyMMNVBqWLeg05gqd_I3O2z4zmb7k2U_9DVk0dSYc-LuT_-Lz8NC0vMUMtcxZX4uzl1GE7pwEh4w8k5eUi3bf82Mf7QFwkp7pUgzEuK03nupB9BIDccW7_ZwR1Nl62yukoqeB0xV9uvlMg33my62ihZNpTnhPeuGFZ0puxXuOzBSBMNXgBw22Bdjxgb2ZdpHQJN1JKqg0brucNJvGsLIV4ekevrr1ZKwDZrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
لبخندِ کرامت در روستاهای مرزی زابل
🔸
#گزارش‌تصویری
از توزیع بسته‌های حمایتی در روستاهای کم‌برخوردار و مرزی شهرستان زابل، به همت
#هیأت‌قرار
و دستان مهربان خیرین عزیز در دهه کرامت
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652883" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
گرچه متن‌های ارسالی بین ایران و آمریکا از برخی اختلاف‌ها کاسته‌شده اما هنوز شکاف‌های جدی وجود دارد. / این شکاف‌ها شامل مواد، غنی‌سازی، پول‌های بلوکه‌شده است. / در عین حال در برخی موارد مانند اسقاطی‌های نفتی یا پایان جنگ پیشرفت حاصل شده است./ در متن ارسالی آمریکا به ایران که مربوط به هفته گذشته است، طرف آمریکایی شروط ایران از جمله پایان جنگ در همه جبهه‌ها، ایجاد صندوق بازسازی و‌ توسعه و پایان محاصره را پذیرفته است./ در متن آمریکا پذیرفته‌شده که جنگ در همه جبهه‌ها از جمله لبنان پایان یابد/ همچنین صندوق بازسازی و توسعه که مربوط به غرامت‌ها است ایجاد شود/ درباره عدد این صندوق گفتگو همچنان ادامه دارد/ همچنین در متن آمریکایی، پایان محاصره پذیرفته شده است./صبح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/652882" target="_blank">📅 20:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شمار شهدای حملات رژیم صهیونیستی به لبنان به بیش از ۳ هزار نفر رسید
🔹
وزارت بهداشت لبنان روز دوشنبه اعلام کرد که شمار شهدای این کشور در پی حملات رژیم صهیونیستی از ۲ مارس ۲۰۲۶ به ۳۰۲۰ نفر افزایش یافت.
🔹
همچنین به دنبال حملات این رژیم به لبنان، ۹۲۷۳ نفر نیز مجروح شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/akhbarefori/652881" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-3cEpcAU3gmQYDQ_dsDepK4yeL3uLVv36kBT2AotKb2j3eWAmD7wcDPztSeTnubqwBmcupOh082q0-EzLbXpzMxfWLZXxNzFrrFv7S9kIA__py32ye_WvqZs_WGejbwadWSFYh28SAMgABS8Ot8s3Q-SDz0VNt7bJxF008j9BhlF4LCrwyeE-20CBowJM9u4PIIm3SjJuQDLIfTf08F1KMBGY4e-hMUAsVQkgyDg7jh1OFHiH013kMGi1_OBfLtuiulpCkITHFcAKvaB646WkAySv1_BvDk9-Je9lpEOVQ_8pYPLZ32P26wfCHwNIEvyOT5atGP2TtYiRKPMUTQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: حاضر به دادن هیچ امتیازی به ایران نیستم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/akhbarefori/652880" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار طلایی‌نیک: بخش قابل توجهی از توانایی‌های ما هنوز مورد استفاده قرار نگرفته است
🔹
سخنگوی وزارت دفاع: اعتبار آمریکا به دست نیروهای ما از بین رفته است.
🔹
به هرگونه تجاوزی علیه کشورمان با شدت بیشتری پاسخ خواهیم داد و برای همه سناریوها آماده هستیم.
🔹
آمریکایی ها یا باید تسلیم دیپلماسی و شرایط ما شوند یا تسلیم قدرت موشکی ما.
🔹
در حال اجرای یک نظام حقوقی جدید و تصویب آن در مجلس شورا برای مدیریت تنگه هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/akhbarefori/652879" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شبکه CNBC به نقل از یک مقام آمریکایی: گزارش‌ها درباره موافقت واشینگتن با لغو تحریم‌های نفتی ایران دروغ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/akhbarefori/652878" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ترامپ: ایران می‌داند که به زودی چه اتفاقی خواهد افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/akhbarefori/652877" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: شکست آمریکا در حمله به ایران بازارهای نفت را تحت تأثیر قرار داد
🔹
امت اسلامی، چه دولت‌ها و چه ملت‌ها، می‌توانند اقداماتی مانند تحریم اقتصادی و سیاسی را در پیش بگیرند.
🔹
تحریم اقتصادی و سیاسی ابزار مؤثر و فشار قابل توجهی بر دشمنان وارد می‌کند.
🔹
جهان از پیامدهای شکست آمریکا در حمله به جمهوری اسلامی ایران در بازارهای نفت تأثیر پذیرفته است.
🔹
نبود اراده در میان بسیاری از کشورهای اسلامی برای اتخاذ موضع، وضعیت خطرناکی ایجاد می‌کند و دشمنان را جسورتر می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/652876" target="_blank">📅 20:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRNiUWmQklPMWwwDWgmMPcEhbLfPUAt7Ys6O6QgVJsj-YmTsXU3lsayWhKLM9xSz8GaOxJR7iUg8_6OijKy_co1EFwyPym0FWBTV71YsHgUBUCWxkU9HzK3Xd74s9RN97xDnUosKlQvRnw-7uZ6a07T7v0oplP7dJcDXxBH4f1Jgh5ZxWXLrF8dvCbVU8FSyVlAi9FiPs3GPpowU4pM7LSw4NU-3ekrKQHuz-7tS6ecQBegrOJhx2tf8FUTNnaAjBaJAHU14avhZVFpb-H9MimUDuD-SXJBWbwrse2ljqccq8WvYFntegijamrGYQ30IMxFnRx4Zw4Zkyu_nOFFX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار حزب‌الله عراق به دولت اردن
🔹
حزب‌الله عراق: بخش اعظم عملیات شناسایی آمریکا و رژیم صهیونیستی از مبدا اردن انجام می‌شود و این مقدمه‌ای برای انجام اقدامات خصمانه در داخل عراق است لذا دولت امّان باید از اتفاقات جنگ اخیر درس بگیرد چرا که کاسه صبر درحال لبریز شدن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652875" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_1NkmcZ2_aIwnLB8In_4eAZ4MeBx6O2x83ypEF1Qf4dgHRAK43gTPSyPi47mAtjxOjQszQKLl35wsoWxD6Dh5FOR67DrDy0R4BBE8IKqLRpoC-9WaiAQf_CH5x4Q2jWkEoiC-91n1kqFhqRSOaBo7VYYJcnlTaSo6iV-Htxs9fi7kpFeloeLHjiVRvBftA53kJXTLd7W7AqSYd1oaugqcimWpg2QN1wy1JPT-D1hJK7vUmiZT3grBUQn0yVgAz-RJeNdybOlG2i13SafoVPLAH2GpUR4Cea2SyVTLovAjsubimhNLBKaMcNppg2BIqCp_3_m9h3ByGhduidtndDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت پراید در هر سال معادل چند دلار است؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/akhbarefori/652874" target="_blank">📅 20:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_JqzdtXDFXo7GRUPX4g4gvYjCkaDd8YSHefUNt65VUX6aKBR3iUCyfb6k-f9vAedbW1q6OuzJ-DzaeWWGZhonDqzcpPjopKebWYauCRD2llFHHKoAvgcR1eB9URos7z2At86uOfCGwlNyxKNiCgF5E2K18bHmaNMsNaSp672naPN_uZchA5P1Ql33BwUgpKYUulGC8xHvkCmIZWnR6ydtWnIA4FjX6JNHtgXaOUBa_kribRErXnpkk0aHGtzrpNMXuMzUgTnTQr526R-46lpmfw_hkaQFshGXqHbDwM_jB6Pt7_mQiJZkK-_6T8mSVb9AAx1ZWrfA8SWOTiOytzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای جلسه محرمانه ترامپ درباره جنگ با ایران/ مقاله جنجالی وال استریت ژورنال: ۷ پلن واشنگتن برای جنگ جدید/ نگرانی شدید ترامپ درباره آینده
🔹
اطرافیان ترامپ نیز در مورد ایده از سرگیری جنگ با ایران چند دسته هستند: الف. طرفداران جنگ بزرگ با ایران ب. طرفداران ترک سریع مخاصمه با ایران ج. طرفداران توافق سریع با ایران.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3216025</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/652873" target="_blank">📅 20:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652872" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myKxCIPNkHDXlVcs_FpOyphe34HrKH152kSrnUC9jR7qXVR-P-dn-JfNaEM_IS8tIOFCrzNfNg0aTlV3pw5DDdJE1XOBmXmdD8RwnIu94ajodTP-9GHCmIb768oqm1KOkiMKMEzzKvTU_kM6CJi_1QhWkfRiNVovgi6ox_NCgzyrJ4-TFo81NjJUOEak79wpphc4UeoB92a9TU-Cr9fLJAifNOr0LyYRucrDePTqUKDoStmoGBLXnCM3lJRa0dcniSSV-oQk-Md1ggBNtqxHRhAmRuVtbg_SSGtE9EEW9YlX35sm5vyWrfkafFxX88j-8pvgtRDnyXXFAIRXq07_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌ استریت ژورنال: حملات مخفیانه امارات و عربستان به ایران، همزیستی شکننده و پرتنش در منطقه را فروپاشاند
🔹
دوره تنش‌زدایی محتاطانه میان ایران و کشورهای عرب خلیج فارس عملاً پایان یافته است. آشتی‌های دیپلماتیک سال‌های اخیر، هرگز به معنای رفع واقعی رقابت امنیتی نبود و تنها نوعی همزیستی شکننده را ایجاد کرده بود؛ وضعیتی که با جنگ اخیر و حملات متقابل از هم پاشید.
🔹
ایران اکنون نسبت به گذشته اهرم‌های فشار بیشتری در اختیار دارد؛ از توان موشکی و پهپادی گرفته تا شبکه نیروهای نیابتی و موقعیت ژئوپلیتیکی در خلیج فارس و تنگه هرمز.
🔹
حتی اگر کشورهای عرب یا آمریکا بتوانند به زیرساخت‌های ایران ضربه بزنند، تهران نیز قادر است با اقدام متقابل هزینه اقتصادی و امنیتی سنگینی بر منطقه تحمیل کند.
🔹
عربستان همچنان نسبت به ورود به یک جنگ فرسایشی محتاط است، زیرا نگران آسیب دیدن پروژه‌های اقتصادی بلندپروازانه‌اش است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/akhbarefori/652871" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ddb09517.mp4?token=BhSAeeBSlODFQct2kha7ijzMuP-fKNttdqOHJ4paA_rrGUlpES4bc3ulA09q_pahMbRArkUdKdCE164AyE5Kxo4tF7VjJwItdkcHDFDYjSWFRIredlZoCsQrO51mx7Cr8X8TLlmuh_Qw-idUjQiXs1iPscE1iLh5548xT6sY4PG5NExHWTSECITJe7EB1iilAg31opLZ8awqdJUGg-QX5z4gdPvKGurU5nzbLFY0xnMeFfxJrKJgwVz1edNPHJgu1LUe1NC3sA5EGDvXpYvKHQfTM54EuSmv3mBP8irfETflpC8NhzSqusbB3KcCluJzeLWpRICPvo5320i-NOYC5w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ddb09517.mp4?token=BhSAeeBSlODFQct2kha7ijzMuP-fKNttdqOHJ4paA_rrGUlpES4bc3ulA09q_pahMbRArkUdKdCE164AyE5Kxo4tF7VjJwItdkcHDFDYjSWFRIredlZoCsQrO51mx7Cr8X8TLlmuh_Qw-idUjQiXs1iPscE1iLh5548xT6sY4PG5NExHWTSECITJe7EB1iilAg31opLZ8awqdJUGg-QX5z4gdPvKGurU5nzbLFY0xnMeFfxJrKJgwVz1edNPHJgu1LUe1NC3sA5EGDvXpYvKHQfTM54EuSmv3mBP8irfETflpC8NhzSqusbB3KcCluJzeLWpRICPvo5320i-NOYC5w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز اگر کسانی بخواهند از منافع ملی صرف نظر کنند برای خاطر رضایت آمریکا، ملت گریبان این‌ها را خواهد گرفت
🔹
به وقت شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/652870" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwElvKA9np7LcqYAH8rZqDlugG_nQjSBRWsTXz6mcyFXOcgTe1b9wQrWS6qQQhxWYuh4VGDWoC1GJupRQNkgcI4zNVuvuxKGbfz6SCrQ8d-kG2Al6g6L5G93KoIl_-7T_YGFg-HvCwqYEis7uF9xK1mpHVsLlmJIY0C1UphZjji3m0blW_T4sZEruUF6uct58fTb_O4Zp7igM5Z1rATpQGgWgO3XSBRQ5YVcw55MmfBPia8J8JVosgxp5x5KVfxe3AKDlkCknmfXF_Fd2_xRUcyEGijhroSV5_cyBP8HacqfjV-aCX1-kSQbXJKdVK3QAFO1dHiMQc0Rtsbqr2MRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند به بالاترین تعداد از زمان محاصرهٔ آمریکا علیه بنادر ایران رسیده است.
🔹
این شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران می‌گوید: این نادرست است، تعداد زیادی نفتکش در محدودهٔ محاصره وجود دارد اما تولید نفت خود را مدیریت کرده و ذخیره‌سازی‌هایی هم در خشکی انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/652869" target="_blank">📅 19:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd98eeb7bf.mp4?token=kp5MfFnsO97sjFKdJbEr3kZtt_QDIWfv675g5jm-VFZC_JfyWVsEIVi2t5za4pDzmOBjmTdD3hR9PORDMMHumjD4vi7GHWZ4hSZiXHaJ6xjtYxMRqVX53x-7WwHYBbowJblITBn276ArqbHhc9e8iqv_v5I6bEk9UfXgbeZZDJPTUCTajmzLBrFB8FYtTHDoY7WexLKnkpW2uFMTDO39PshB8thtOIx4hYeOtFJM_-0bRICJeQwtiQorWO7bLB4-R0YFzelEjrZnMcosiT8A-DIwnklvTWxX8beQLSV-44R-HEIq2ZOyHMgqcOY3Ok3u3mx2ck44W7yTdWsXqkCSLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd98eeb7bf.mp4?token=kp5MfFnsO97sjFKdJbEr3kZtt_QDIWfv675g5jm-VFZC_JfyWVsEIVi2t5za4pDzmOBjmTdD3hR9PORDMMHumjD4vi7GHWZ4hSZiXHaJ6xjtYxMRqVX53x-7WwHYBbowJblITBn276ArqbHhc9e8iqv_v5I6bEk9UfXgbeZZDJPTUCTajmzLBrFB8FYtTHDoY7WexLKnkpW2uFMTDO39PshB8thtOIx4hYeOtFJM_-0bRICJeQwtiQorWO7bLB4-R0YFzelEjrZnMcosiT8A-DIwnklvTWxX8beQLSV-44R-HEIq2ZOyHMgqcOY3Ok3u3mx2ck44W7yTdWsXqkCSLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چالش‌های آموزش مجازی از نگاه شما؛ مشکلات نرم‌افزاری، سخت‌افزاری و اینترنتی
🔹
«تجربه شما از چالش‌های آموزش غیرحضوری چیست؟»
مخاطبان خبرفوری در پاسخ به این پرسش، از مشکلات نرم‌افزاری، سخت‌افزاری و اختلالات اینترنتی در دوران آموزش مجازی گفتند.
🔹
در ادامه، بخشی از این روایت‌ها را بازنشر می‌کنیم.
الوفوری را دنبال کنید
👇
@Alo_Fori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/652868" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUyBF9krdZbi72vN25ewxTlgi2_CIQw1PYyZez9qL5Cb_6ZOVc7bOdmg8onOkrBOfCA55uhwhQrY--emEauelYml-sqcN3L8c09kYwMLJtWztDQ-yiOXlkHYAvOwQhn18H5_uT-djxFTAectkaQ7F2Dmf37s5XfX4HTFA6Brgvs_HXmv3VjNKVwE0Lu4WO4NmWBREis54ecNgx9cSZGguxOAML5OrGT8kevEpPQzz90RH07osEBI7k8CV22sCLdu8RsmbGx16xSD-RwliQz996wfe5LvbXvrvBlIOyCf0LyQYq0ZAxsNeQ8YB6wyQuIXvhVm2Ymal_nEWgw9JVBX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«یک انتخاب، دو سرنوشت»
🔹
سمت چپ، غذایی که با احترام به زمین سرو می‌شود
🔹
سمت راست، زباله‌ای که آینده را می‌بلعد.   هر بسته‌بندی، یک تصمیم است، تصمیمی که طعم فردا را می‌سازد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/652867" target="_blank">📅 17:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6e8d401a.mp4?token=Lz758UhTu0Rw_Fze6KJMdBFnea43_UjwU1fxe2fB7xCjFKVG3H53yy1wcSmauQwgTx5ck8jKLQp0_vSVPnztZT57bclgjPU94s0LbYoENloGSNipj6LUYzl8KAimCmE5hwVnT0L0UqyAjp8b4_sKdoOcelERq69vmQXQdvIs18U49gbXlDFzcbb2gVh05gShMuiEAkMmzVYUw_ESKGytxD--Kg-LplQlSRiOFQeHpuvQe5UuwKPuxjydtUwnWxTG3me-VPOlA5tgfq46bctk3udSew5Oj_C_FljFjsZluXfXic4h1Kf_XT-_RMIPZMNHXjahbMjRatzGmheDheSh26bryqDCFeZyDgrqiqz0ey4o8-gD4svGWhlI8gYhxcgk0uTx7Zo_b-ZHVBs74W50PPX1hu4oX7WnVCjK-yUxltiVZ34rP4gzMmXWIB2LbGQQ41azrbeyod3lsw5G23JF2yv8SzzMOu1wAusomKX_3xuceulkmkpa8YlPUJ_A3MlBoZnCmiUPZ51NLM4IKfETrbtvOWrm3aj-UkJ21jT9hPtT1wUw9T4GsefqtIo3TojU5T2f3tiKHuTuDgiK9u7DZpFUWzOpw3nVCJfnCO3gq1WnPGGwi8XrT2CKFjO_3fkRkt9kbNB_Hv9Z5Tax0bxAgCSJR6sBtqPQVJpImVYmpKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6e8d401a.mp4?token=Lz758UhTu0Rw_Fze6KJMdBFnea43_UjwU1fxe2fB7xCjFKVG3H53yy1wcSmauQwgTx5ck8jKLQp0_vSVPnztZT57bclgjPU94s0LbYoENloGSNipj6LUYzl8KAimCmE5hwVnT0L0UqyAjp8b4_sKdoOcelERq69vmQXQdvIs18U49gbXlDFzcbb2gVh05gShMuiEAkMmzVYUw_ESKGytxD--Kg-LplQlSRiOFQeHpuvQe5UuwKPuxjydtUwnWxTG3me-VPOlA5tgfq46bctk3udSew5Oj_C_FljFjsZluXfXic4h1Kf_XT-_RMIPZMNHXjahbMjRatzGmheDheSh26bryqDCFeZyDgrqiqz0ey4o8-gD4svGWhlI8gYhxcgk0uTx7Zo_b-ZHVBs74W50PPX1hu4oX7WnVCjK-yUxltiVZ34rP4gzMmXWIB2LbGQQ41azrbeyod3lsw5G23JF2yv8SzzMOu1wAusomKX_3xuceulkmkpa8YlPUJ_A3MlBoZnCmiUPZ51NLM4IKfETrbtvOWrm3aj-UkJ21jT9hPtT1wUw9T4GsefqtIo3TojU5T2f3tiKHuTuDgiK9u7DZpFUWzOpw3nVCJfnCO3gq1WnPGGwi8XrT2CKFjO_3fkRkt9kbNB_Hv9Z5Tax0bxAgCSJR6sBtqPQVJpImVYmpKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده از لحظه ربودن یک قایق ناوگان الصمود توسط نظامیان صهیونیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/652866" target="_blank">📅 17:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d0577e1.mp4?token=SlC-YxV5TwGQkmUb-vW4SwIt_S8b50NYPvhgvZw_zYceEK1NvxGjbks4ACuitr6ftdArK8Ah8SC-aDRTwGxOOTWBlpCftuNgq_GZOss3iXnoyx_9LbwMv-4Geo8-ijmQaZR7wwje-5k3i_YTefmuzQg6mqqxgYTcpLQY7hMoVT9GCHC79HPkm9pcsP-VfHo8NhQEC3eHFX-n9KL8KawqMiOR8RYmYxJul1jeRDyiZE10A0FtTMXCsnY4CjlVjc7slvPqF2BRZD63TPg5K6m0WDDDD3JS-OxcPpanPesVvvKZOKb-OuPLKB9HY9vhdlTFsproNhOTSDDuBIoQsdToeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d0577e1.mp4?token=SlC-YxV5TwGQkmUb-vW4SwIt_S8b50NYPvhgvZw_zYceEK1NvxGjbks4ACuitr6ftdArK8Ah8SC-aDRTwGxOOTWBlpCftuNgq_GZOss3iXnoyx_9LbwMv-4Geo8-ijmQaZR7wwje-5k3i_YTefmuzQg6mqqxgYTcpLQY7hMoVT9GCHC79HPkm9pcsP-VfHo8NhQEC3eHFX-n9KL8KawqMiOR8RYmYxJul1jeRDyiZE10A0FtTMXCsnY4CjlVjc7slvPqF2BRZD63TPg5K6m0WDDDD3JS-OxcPpanPesVvvKZOKb-OuPLKB9HY9vhdlTFsproNhOTSDDuBIoQsdToeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Stop scrolling. Start exploring.
Dive into the best Telegram channels—curated, categorized, and just one click away.
🗂
Add the entire catalog</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/652865" target="_blank">📅 17:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
لحظه هدف قرار گرفتن خودروی مهندسی ارتش صهیونیستی در دیر سریان واقع در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/652863" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec851f999.mp4?token=teA6MKQ6aOvA2-ZnKfLiMRakhTqi-YE7Lat-uh8MUAgGDiGR6_2GlHubtmmfhRJOuGLiyJvmIBap7SOLa3tkWgGGE6oD7CSKTzvqGaKNFyq1HY7owfS0cgZKDj7zL1NymN4u-RWfpRLiFK8LLusZ4Dd3s2DnYHMXUQCiI4XDqoHKQDvXokiJYOA57juFL9pQf55FPspJHBRcuX_TBf3xqHOvhakcc31RZkoOC9aYOVjY7D3h8shyYr8uetiO3w6f5ege4QKP-9PyqmYpd4hUUISNhOQgIlJCLJVdwqVOdrBgBUpEKBgMEISaHcgML4Wreq5bEX2MhPG3UXwYmgmmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec851f999.mp4?token=teA6MKQ6aOvA2-ZnKfLiMRakhTqi-YE7Lat-uh8MUAgGDiGR6_2GlHubtmmfhRJOuGLiyJvmIBap7SOLa3tkWgGGE6oD7CSKTzvqGaKNFyq1HY7owfS0cgZKDj7zL1NymN4u-RWfpRLiFK8LLusZ4Dd3s2DnYHMXUQCiI4XDqoHKQDvXokiJYOA57juFL9pQf55FPspJHBRcuX_TBf3xqHOvhakcc31RZkoOC9aYOVjY7D3h8shyYr8uetiO3w6f5ege4QKP-9PyqmYpd4hUUISNhOQgIlJCLJVdwqVOdrBgBUpEKBgMEISaHcgML4Wreq5bEX2MhPG3UXwYmgmmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری شبکه فرانسوی از پشت پرده انفجار مهیب و مشکوک بیت‌شمش در اسرائیل؛ مردم اسرائیل روایت ساختگی دولت را قبول ندارند!
🔹
خبرنگار شبکه فرانسوی BFMTV مستقر در سرزمین‌های اشغالی: انفجار در پایگاه ارتش و نیروی هوایی اسرائیل رخ داد؛ تردیدهای جدی‌ درباره روایت رسمی اسرائیل مطرح شده است و ساکنان اینجا سؤال‌ها و نگرانی‌های زیادی دارند!
🔹
چون این منطقه، مسکونی است همیشه قبل از هرگونه آزمایشی مردم را مطلع می‌کردند اما این‌بار هیچ‌یک از ساکنین در جریان قرار داده نشدند و همین مسأله نگرانی‌های بسیاری را به وجود آورده است.
🔹
در جایی که این انفجار مهیب رخ داد، تجهیزات حساس و نظامی نگهداری می‌شود از جمله کلاهک‌های هسته‌ای که در آنجا ذخیره شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/akhbarefori/652862" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0569b312a4.mp4?token=ptzzvNDes8HPOpFZiJ7IUtMu6xMO_kAoe4XzrY0-ynqTzxMM6y0wcVhTVUIP0IRYvRJSs48ruPhiUseujDKhjIeUs3dhUbya9DUj7LjIA9V1zRrxTg0HKlZP_z1VO3kunXd6NUqk-qL9cazyzUtEEAi2aamJt6s15HVC9KSL8b7iosZDTsEFiTMkxsCiRUJM-G0jV8D0AiDFdO2jsWgwJdWasLK9KeF7qYM3B-j8qO4nRIr07-ZwXkJoUyMK-2wTk__gG1yDJjAYH5DoB2nuN6AGzx0Q6g9if7plgvIwCcNMUayhjQtsLwjJzXY_9o9eiMSMFvTl7TYcnuWRQrzR2wSeo2L_W_p0a0dpVsnhSsMgyuhn7DWJS33regPjNeqSKpjggA7GcL3DlMPWarFatOwBdYSnsJJxY_CujIYR7KzBWxk_Prwr57KeNT4N0MZqCWiKitFLL_KlD_ErCga2VpU6Dbxs0CZcGtxSHVtPyHYjeFTIvAladkWZRp18x50cuV2su9CHmVFLU9f6xrYSpuXbCegaWg9uCAUXFiMvUvHyWNwSwINtw-yT9ypq9kEbWkjciGubn_iRdfHkRqOI4M7Atu23aNXKN4YLkeKDeaI9nx7SiepoFVQ9QQ-orH0ncndoHfOO8JvKrT3vILK8OHyWQurkWp8h8SGDlXRP1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0569b312a4.mp4?token=ptzzvNDes8HPOpFZiJ7IUtMu6xMO_kAoe4XzrY0-ynqTzxMM6y0wcVhTVUIP0IRYvRJSs48ruPhiUseujDKhjIeUs3dhUbya9DUj7LjIA9V1zRrxTg0HKlZP_z1VO3kunXd6NUqk-qL9cazyzUtEEAi2aamJt6s15HVC9KSL8b7iosZDTsEFiTMkxsCiRUJM-G0jV8D0AiDFdO2jsWgwJdWasLK9KeF7qYM3B-j8qO4nRIr07-ZwXkJoUyMK-2wTk__gG1yDJjAYH5DoB2nuN6AGzx0Q6g9if7plgvIwCcNMUayhjQtsLwjJzXY_9o9eiMSMFvTl7TYcnuWRQrzR2wSeo2L_W_p0a0dpVsnhSsMgyuhn7DWJS33regPjNeqSKpjggA7GcL3DlMPWarFatOwBdYSnsJJxY_CujIYR7KzBWxk_Prwr57KeNT4N0MZqCWiKitFLL_KlD_ErCga2VpU6Dbxs0CZcGtxSHVtPyHYjeFTIvAladkWZRp18x50cuV2su9CHmVFLU9f6xrYSpuXbCegaWg9uCAUXFiMvUvHyWNwSwINtw-yT9ypq9kEbWkjciGubn_iRdfHkRqOI4M7Atu23aNXKN4YLkeKDeaI9nx7SiepoFVQ9QQ-orH0ncndoHfOO8JvKrT3vILK8OHyWQurkWp8h8SGDlXRP1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ بیهودۀ ترامپ با ایران به روایت رئیس سابق سیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/652861" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2WBNQcGGfRzprW8uygR-dCMAHpEO_ugC5T0uzJ63vbAYHhOr6dovwMzjF6N0dv5WYWPSRqOhjp76-z7VW-YE1Fza-R901HCILFhp3yixGqQ6VW4ZtHPR7-FsPBTFBROglV65LXSjIfrVb1v8PNvRZzlpmKlFoRsUXlx_VwggHprrmPwLl_iWbUIRzh2anNUle8e2puz-wZjl-LKoyC3lZ_r0di0Jfv3Bb8D6XBbvPOae4ztYHcsX5clLCsX8GhLzuC-pm2H5l19blWYht8HGh1KnnoumV9N-Qi_puPT-JgjMZPIqBgXk7thPFzanyohqBDAWWxqVHWsfyrJq1ChFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا و اسرائیل در حال آماده‌سازی نظامی هستند
🔹
به گفته دو مقام در غرب آسیا، آمریکا و اسرائیل بزرگترین فرآیند آماده‌سازی نظامی خود از زمان برقراری آتش‌بس را آغاز کرده‌اند.
🔹
روز گذشته، رئیس‌جمهور آمریکا بار دیگر به زبان تهدید روی آورد و ایران را به حمله نظامی تهدید کرد. ترامپ تصریح کرد که ایران زمان زیادی ندارد و اگر فرصت را از دست بدهد، «چیزی از آن باقی نمی‌ماند.»
🔹
این تهدیدات، بار دیگر تنش‌ها بین تهران و واشنگتن را افزایش داد. مسئولان ایرانی بارها بر آمادگی کامل خود برای مقابله با حملات احتمالی آمریکا و اسرائیل تأکید کرده‌اند. با این حال، همچنان مسیر دیپلماسی نیز در جریان است و شب گذشته آخرین پیشنهاد ایران به آمریکا ارسال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/652860" target="_blank">📅 17:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
یک کشتی ایرانی دیگر خط محاصرهٔ آمریکا را شکست
🔹
یک نفتکش ایرانی تحت تحریم‌های آمریکا که ۲ هفتهٔ پیش در سواحل هند بود حالا در جزیرهٔ خارگ پهلو گرفته است.
🔹
این نفتکش حامل ال‌پی‌جی بدون اینکه شناسایی شود از خط محاصرهٔ آمریکا گذشته و وارد آب‌های ایران شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652859" target="_blank">📅 17:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_7i6nmYVkBJMoRtKmqIDwKDOgi1lnjipw__-2G0Dxx2RqeCLXCX-QCPkESxla9BgyxCSAR1Zj4vIIc5fI-oW9pyEpNKYNspXpMAZ4LzSE5xTEfOZHooaInpse8tlT7J2STCheZwnY1gjg5PKY7fVAmxE75mrcSGeWZhrc4u7tSPGKW_gdXKE9z76bWXzAmulqKL42vfz5UUCUgOkCZ6kXBphERwLQPPON_adM1zNGtY_m2aTCevHQJ-tdRvZaQ99jMxRDqRJcYnhHLwZwaCnGoZCktr_INUb8FXf5nelcqkXzZKkAw8tDYIN42DOPlALNrALzkBR2m4w2I_yfhn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: وزارت جنگ آمریکا به صورت مخفیانه برنامه قانونی پیشگیری از کشته‌شدن غیرنظامیان توسط ارتش را تعطیل کرده است
🔹
دولت ترامپ در بحبوحه حمله آمریکا به یک مدرسه دخترانه در ایران، به قطع برنامه کاهش آسیب‌های غیرنظامی متهم شده است.
🔹
بر اساس گزارش بازرس کل پنتاگون، ارتش آمریکا مخفیانه برنامه‌ای را که به موجب قانون موظف به اجرای آن برای پیشگیری و پاسخ به مرگ غیرنظامیان در عملیات‌های نظامی بود، برچیده است.
🔹
دولت ترامپ متهم است که بودجه مربوط به مدیریت داده‌های این برنامه را قطع، جلسات کمیته هدایت آن را متوقف و بسیاری از پرسنل متخصص آن را اخراج یا منتقل کرده است؛ امری که به گفته بازرس کل، وزارت جنگ را در خطر نقض صریح قوانین فدرال قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/akhbarefori/652858" target="_blank">📅 17:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص مصلحت نظام: گزارش کمیسیون اقتصادی مجمع تشخیص با سناریو‌های مختلف جنگ نظامی و اقتصادی در حال تدوین است
🔹
پورابراهیمی: به زودی گزارش کمیسیون اقتصادی در مورد تحلیل وضعیت موجود اقتصاد ایران و راهکار‌های اجرایی متناسب با شرایط فعلی کشور خدمت ریاست مجمع تشخیص و مقام معظم رهبری ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/652857" target="_blank">📅 16:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO63KSQfTz5MieLWPO516hYLvKKaxriJDAGTiQtyT8D6_clPh8zmMNT7xJh6Jy8a3lRI1PIr6Xskx-TGL9OcL2F9_PpL29JmAAeK5XI6gxxsEMZpWz0ue8DTVxjrIxU3icIMH1t2QITuNXxZpaxd4KlTxUFwnU1LmtLlcxUOUYMwVc-3Uft5e-z4X3hv751I1upfjtlx0yNTxnY_pft7t9stMmOrtqqSgnKd8MfSFZ3fh_4EtD3rCoJyTKID_W27GJ6Fh4aVsPKQekM_Qw--ljbS_X_1htmIOa3kp2St13md-4Eldb1RxURzRlpC21sk0GGAmbfQEjIhrQnO1s-CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کرملین به سخنان زلنسکی درباره حمله از خاک بلاروس/ برنامه سفر پوتین به چین
🔹
پسکوف، سخنگوی کرملین: ادعای ولادیمیر زلنسکی، رئیس‌جمهور اوکراین مبنی بر اینکه روسیه می‌تواند از خاک بلاروس به اوکراین یا یک کشور ناتو حمله کند، چیزی بیش از تلاشی برای دامن زدن به جنگ بیشتر نیست.
🔹
پوتین در حال آماده شدن برای سفر فردا (سه‌شنبه) خود به چین است و روسیه انتظارات بسیار بالایی از نتایج سفر آتی او به چین دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/652856" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اعتراض ۵ میلیون بازنشسته تأمین اجتماعی به تأخیر در افزایش حقوق
🔹
با گذشت تقریباً ۳ ماه از آغاز سال، هنوز افزایش حقوق بازنشستگان تأمین اجتماعی به شکل مورد انتظار جامعهٔ مستمری‌بگیران اعمال نشده است.
🔹
بیش از ۵ میلیون نفر از این قشر زحمتکش جامعه، بر این باور بودند که طبق مواد ۹۶ و ۱۱۱ قانون تأمین اجتماعی، حقوق آنان باید بر اساس حداقل دستمزد مصوب شورای عالی کار (که پیش از آغاز سال تعیین شده بود) از ابتدای فروردین‌ماه اصلاح و پرداخت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/652855" target="_blank">📅 16:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqEArXr4uh0-Yq5c8ZzLRDLPPZuNrg0hYggkDFSD0-SeVyNhX9nmQ4PXLq4E9-C9lz6PaVUpkFT3dxGmdoy3FJBJWvH1MjWTnVlT7CsOlNtGp68pJGbYeqhh9G4KVkv9anxSmiSSH7R-fdZewK8xEr7f11n1pLdY8uj4lsq90oq1IX0Ecgd47TkYrUfvvQ_-JIUrtPzm-Pw2G-jNzBrNTHV7_9V0cRdw2iHkTXWr8DchvOE8Qvj6LWZ5lzIDX46wO6CB4DR7Ny94VEqVSPrKCTqW2QnBPcgUKpf3DKdr7AAfg_-lQ1NueAozcbaXoTLU6xJg2m7KuKnYLyIeq7ldrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنها چند هفته تا پایان ذخایر نفت تجاری باقی است
🔹
فاتح بیرول، رئیس آژانس بین‌المللی انرژی (IEA): به دلیل جنگ تحمیلی علیه ایران و بسته شدن تنگه هرمز به روی کشتی‌ها، ذخایر نفت تجاری به سرعت در حال کاهش بوده و تنها به اندازه مصرف چند هفته باقی مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/akhbarefori/652854" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
براساس کسب اطلاع فرهیختگان ایران یک پیشنهاد ۱۴ بندی جدید برای پیشبرد مذاکرات از طریق میانجی پاکستانی به آمریکا ارائه کرده است ارائه داده است
🔹
تهران بدون عدول از خطوط قرمز خود ابتکارهای تازه‌ای را مطرح کرده است
🔹
بر اساس اطلاعات دریافتی، اکنون توپ در زمین آمریکا قرار دارد و تصمیم‌گیری بعدی به طرف آمریکایی وابسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/652853" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784a660e16.mp4?token=BPeSDnSGU6H8LVMWAhoZlhQzagzB6iehDl20iP9v0CaJxzSST0nykuEurpfi5a1YOT0vBastst5LBoD7-XaAK8TA4N6OBZUH1HYrsK0UoeWOtWb1N8N1RVuKvn-N1NcAlSGQr5_tuEiyD5fPkiYhqzAic5NcfaLq4NYHP_rDHc2MlsNQHZptF74BmNFUKapYGNzg8euynTSuD89K4q0AbeQhdmatu1EYtoW8Xi98k_nfRkNtjgPiuw2J3PkWUQ9sqqt2XpjrqOBUKQRBtnsnmp7Q0Ajcuf_SUA8p0wQfnyReo4S2YGVRkSFY8SL5wsmgQTyotVTJDmPJRMNqGFcxglXoxxrO5n3SXrTcyR8u-igSIapPX-xfG5fq1aK4dUijhqJvjsDGR2KPLpy6EvpFwjJx7t01o2Ja7e3Nrg1_b6Q9HIapAL3dm7OjvBROvtysaTC9_EFZ_u-DRFGknkZKxLBB4AJR_gU8alERd8iDz8cAaZEBBE6c3tm3XgRiquPnSKmHFWLIRCaT29FC700MS2MzW_iOWDOXW8r6elAG0VEPnrFrFdB1cRfH4N_fb4hrHYcAREwLW6uwUyf0Q2fDwO5FR4-v6huA1InXUY64RLDYOS-VrmtRwtqYujleSYgJER9jRGJp6uBtiHE5Wl4tte9Ln7F5N6po1ZUu_tHp6RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784a660e16.mp4?token=BPeSDnSGU6H8LVMWAhoZlhQzagzB6iehDl20iP9v0CaJxzSST0nykuEurpfi5a1YOT0vBastst5LBoD7-XaAK8TA4N6OBZUH1HYrsK0UoeWOtWb1N8N1RVuKvn-N1NcAlSGQr5_tuEiyD5fPkiYhqzAic5NcfaLq4NYHP_rDHc2MlsNQHZptF74BmNFUKapYGNzg8euynTSuD89K4q0AbeQhdmatu1EYtoW8Xi98k_nfRkNtjgPiuw2J3PkWUQ9sqqt2XpjrqOBUKQRBtnsnmp7Q0Ajcuf_SUA8p0wQfnyReo4S2YGVRkSFY8SL5wsmgQTyotVTJDmPJRMNqGFcxglXoxxrO5n3SXrTcyR8u-igSIapPX-xfG5fq1aK4dUijhqJvjsDGR2KPLpy6EvpFwjJx7t01o2Ja7e3Nrg1_b6Q9HIapAL3dm7OjvBROvtysaTC9_EFZ_u-DRFGknkZKxLBB4AJR_gU8alERd8iDz8cAaZEBBE6c3tm3XgRiquPnSKmHFWLIRCaT29FC700MS2MzW_iOWDOXW8r6elAG0VEPnrFrFdB1cRfH4N_fb4hrHYcAREwLW6uwUyf0Q2fDwO5FR4-v6huA1InXUY64RLDYOS-VrmtRwtqYujleSYgJER9jRGJp6uBtiHE5Wl4tte9Ln7F5N6po1ZUu_tHp6RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری، دانشمند هسته‌ای: روز اول جنگ گفتم کار تمام شد و عمود خیمه ی ما را زده‌اند ولی ساختار حکمرانی نظام چنان دقیق چیده شده که بعد از ۷۰ روز استوار ایستاده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/652852" target="_blank">📅 16:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_E-Cuoa-B5JcdsLQNxzpXGAKI1KwK461bJxXxcJzHdWiuNI4fV74sR9EdWZF0uXU1RgVdT3qxccv0T_lL5XN5Qidr-dr1u-ytJMF3AhOHXIsEW-9PZBR2E2Ilkn8rdBwZV0DZNmaS43LKtU9Z4pHGAdM-PsrYadyuIcpAMqITiZSCH9qV61W0j93ayTIc7jrQJkHITlJ9pwP17Ul5fZTsZ7ATfHon3ULwSLN2OZzR8AkP9EWrVFKFBEZiaVCE0thwVHFS5pIkWYx_GMXZIJgdQGNiF61dBRR50NjMxEXAm8hcmk-BfUyOYyqP1J_xkSjYs7P1qYkXyoyviXcyQsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشدید حضور نظامی پاکستان در عربستان در بحبوحه جنگ ایران
🔹
اسلام‌آباد در راستای توافقنامه امنیتی خود با ریاض، یک اسکادران جنگنده، حدود ۸ هزار سرباز و سامانه‌های پدافند هوایی را به عربستان اعزام کرد.
🔹
این مقامات امنیتی تأکید کرده‌اند که این تجهیزات «آماده رزم»، می‌توانند از عربستان در مقابل حملات احتمالی پشتیبانی کنند.
🔹
اسلام‌آباد در حالی حضور نظامی خود را در عربستان گسترش داده است که تنش‌ها بین ایران و آمریکا و احتمال از سرگیری درگیری‌های نظامی در روزهای اخیر افزایش یافته است. پاکستان همچنین نقش میانجی در مذاکرات تهران-واشنگتن را برعهده دارد.
🔹
شرایط کامل توافق دفاعی بین پاکستان و عربستان محرمانه است، اما دو طرف گفته‌اند که این توافق ایجاب می‌کند پاکستان و عربستان در صورت وقوع حمله، از یکدیگر دفاع کنند. خواجه آصف، وزیر دفاع پاکستان، پیشتر تلویحاً گفته بود که این توافق، عربستان را زیر چتر هسته‌ای پاکستان قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/akhbarefori/652851" target="_blank">📅 16:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48ea2e889.mp4?token=N9-Qq8ERwRQ6QFntD2FUjpo0y7ydAEC45HagdWA_uE_5TeVDIVb9p06MD8fSzUgEfhsuqBkazJc5RDEpV0oydjmYuqG8wFCCieu0Tgv-KaxH_0h0ntXXfxMCNJcJlvF-M8NUKoVJZ55S-Y1bAu5aRDz6mzzjwmYFmtlzQU3arYSSmNnlFU5dnBAsYAKy4F0dObzLO9TQQeX-KYjStYGa4w0_lVK9Vm7WBUhGEkn2D6woFaKb-6bBVo-KDE9pCC0lEJNiowupRJToXWOEJ2BMkQ31n1SMewCTh6rHddDWl_9ovchAu7rDSv2CPDZcY90OEnEAdKsRteb3joHNIJsFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48ea2e889.mp4?token=N9-Qq8ERwRQ6QFntD2FUjpo0y7ydAEC45HagdWA_uE_5TeVDIVb9p06MD8fSzUgEfhsuqBkazJc5RDEpV0oydjmYuqG8wFCCieu0Tgv-KaxH_0h0ntXXfxMCNJcJlvF-M8NUKoVJZ55S-Y1bAu5aRDz6mzzjwmYFmtlzQU3arYSSmNnlFU5dnBAsYAKy4F0dObzLO9TQQeX-KYjStYGa4w0_lVK9Vm7WBUhGEkn2D6woFaKb-6bBVo-KDE9pCC0lEJNiowupRJToXWOEJ2BMkQ31n1SMewCTh6rHddDWl_9ovchAu7rDSv2CPDZcY90OEnEAdKsRteb3joHNIJsFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">*۲۸ اردیبهشت*
سال روز تاسیس شرکت *بیمه پارسیان *
گرامی باد
۲۳ سال آرامش ، اميد و اطمينان
همچنان در کنار شما هستیم
#بیمه_پارسیان</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/652850" target="_blank">📅 16:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAfAUrqeld6EU6UJPTz8EkFlQd0dnrFXgceHlUEGk2h6bk8wLFxNs0W4jigJ66cuSdGlnsJMH3rDgm1kKnOr5S9i5qvVdGulnV67WbMFh2YW95LlclclL0tgNejfEcchyQx_yBI-lbD_0ViareqkB4KLVT2bQ3rcvfxbstog7aqgwPN2nXBnpb9XZ-MvM1PN75FTHxmKBOV5q0_rcaHdfiPM03rgzIKXdD8hEeXFbOHr5k4Sr1HOzi0Ffda7gZdj-dNQ0Z8wnTSxq7zMyFdDRHg3vWRX8adHJwv3qj-KcOwn2ihnMPTRcb2FDL8A6mjZWKdGC_ME97P7y557n5Ta0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت وضعیت «سلامتی رهبر انقلاب» در روز اول جنگ
🔹
مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت: وقتی که ایشان به بیمارستان رسیدند، متوجه شدیم که رهبری یعنی آقا مجتبی را به بیمارستان آوردند.
🔹
همان موقع که خبر به ما رسید به این فکر افتادیم که چگونه باید روایت‌سازی کنیم. همه جای دنیا در حال ساختن روایت بودند. برای ما کار خیلی سختی بود.
🔹
اتاق عمل آماده شد؛ دوستان شنیده‌اند و بارها نیز گفته‌ایم. اقدامات لازم انجام شد. خوشبختانه اتفاق خاصی برای رهبر انقلاب نیفتاده بود. فردی که در محل چنین حادثه‌ای باشد، طبیعتا چندین زخم بر روی بدن خود خواهد داشت.
🔹
این زخم‌ها نیز زخم‌هایی نبود که بخواهد چهره رهبر انقلاب را مخدوش کند یا اینکه همانند امام شهید ما جانبازی بگیرند یا قطع عضو داشته باشند.
🔹
چند تا بخیه در محل جراحات زده شد. بخشی که همانجا تصمیم گرفته شد که بخیه زده شود روی پای ایشان بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/652849" target="_blank">📅 15:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مبلغ کالابرگ به دو میلیون تومان افزایش می‌یابد؟
🔹
فلسفی، نماینده تهران: مبلغ کالابرگ برای برخی دهک‌ها حتی تا ۱۰۰ درصد هم قابل‌ افزایش است حتی اگر لازم باشد قانون بودجه ۱۴۰۵ اصلاح شود، این کار باید انجام شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/652848" target="_blank">📅 15:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
محدودیت واردات کاندوم به کشور/ فعلا کمبود کاندوم نداریم
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
ارز کاندوم غیر ترجیحی بوده و مشمول قیمت گذاری دولتی نمی باشد و براساس ضوابط سازمان حمایت و هزینه های تولید قیمت گذاری می شود.
🔹
به دلیل تولید بالا در کشور، برای این کالا محدودیت واردات اعمال شده است.
🔹
میزان شناسه گذاری تولید در سالهای گذشته ۲۵ میلیون بوده و در سال ۱۴۰۴ بالغ بر ۲۹ میلیون عدد تولید شناسه گذاری شده است.
🔹
هیچ گونه کمبودی در این خصوص اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/652847" target="_blank">📅 15:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBaVtF_FRcqsDePj73TxaMJ0H9hrfaaSa_oPt8jiFxZ_z6EFp_JPKlj1EL7r-A6cF2CLazVlnguzudDCnRv6QWZ2jgUkkgm98LoEACsq1R9WKQdSHwk4PwZ1LpHL8dVLStrJSen32v8fLzCNY5No5N-yP2dbxMsGq4rsewFtbfm0EU4kIl11_czwIMIGDOeiNgFcNcJM-dLe73EK3ptZaIirBr_aH9-fzIEe5RUFMlc1-gTT5yxY761KriV9XwXdhfKSLfDfbhy3cQkyJ4bZxmflusuLi6xabbdfw3f2VPxh0hvh7IJYpUBOkeHo1jooUVeIsAL2mD4LQv8r7u1dIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwdb5ZnPE_OBhifPhAYDMc2gvzYWjceu-OGt4OBZrZi3xBMXWKUpCZyzchxQcvtK9_MV7ZRm6gToJLHzU_HA4XyuEW23EPnQu_tLVFHJY6GfeYVYrl7WtoezbQ76cPGWtW6uxSNuUT0oXykJgrYuXQowSmxpVVUW7wij1hRPiMli2w3rX9XdTUHCpm0CE0GzScJLfkSkASbBj4B4JkpIF8sZUWzK1VtcjN_sddxUtzMfhA53Zl8jYNsEnb81rFfvUUIYDY1c7UvlbQga8LESiPxth5D99SNea61vPJdkO1h0TmqeAEbZRXIip4wDyTPXBF4RdI-ZTLq0pMLYRFUydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjlNgNOnCwnUC4WTMY30mbEJZxgmdXOe1AE679mXW-caao4ZaZ7ZjEudJbhikkm64MpfmRiUcft0yNOSmjeTPgEAkYYTsOi2HcP8L08_sqDwmDK88ABmQh4k-LD6Jn9RLbtfjP7OPN3qT2FuxPAFvrp_KzcAm22yXh6u6QakrdTOGF655BjJtcISemGngyNdPhM2YIqQc21zh_f644KdGDzuwmX-SkZbDTfBZneW6CWLqcHqxLszSbRRT8m405YDJJ5PT4nIOyTzbyXWDsAl3Kyb7xdmtPE1PoJLtbxZmVQtZLRq98yTPgK9QRDrJY2_FUB_MuAOz0ZQjRtZGAmk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHcvvfmmWUqH4vye-TGLhkZBohhTT_9qjRojJFmZnd-6EQiKhsdYGYCL-JVFBgSvdLXqdevaKcNkK4J16PTHkKziE5RIcaF2139m_MyLI3TVEtp-JSz0mmd1Z16BXAw54OpkTVuJaBtt9HSlDlaIIx9wYjznrqac6KzTi3Na-F0getTGqnTnKBu7rmf0FlJXCoPI-0XInrMHemguVuygTunR_B_zqqkc2txIaLPfJhbwn5Uvq49nFD2NRlHtse7zb44gXliQjzBaSdFAMVFgvp4a7m0CPvKmeHP-Prsu1ogvRrq5NSOD2HqqDsz3adO4U1zt62wwQgeufFBy6JZPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4S8zqn6VJ3H-KT1qwihw9L-N1Z8BIIVRXVPmFPrFiKkaPBHCz0QJL39LXEE_Ayrrcb4MXGuV79OrLPeweq391SbQAuTEktTxDcS4BTDPkqvmDZiwaRhA054ibVSQ7EkCPSAGktGitNQaimMKwv-wSv1MaAkxcqGBv3kZXvT98tueUXfWWFuThq_HsXrq4KF0zUOslezJnhQ3NWwMT5R-tIQExY4MDynefOm-oDWh0QkqJDradp-TS1x7nDaS8JuXVqHJui2MBnIvZDVY7M_m_gwK6IbhBSFXxAGCEDurOjfAgGmjGXnHdKl3uecTWVDsPbRbmLwdPy9ahfwVP97Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaA9519Dr4Jj8x8JR0pcbJr4WNBcKiGn9wZpDLjDD8HhivGzFsD_4iahCQ2ZX-5Q3DtVoRYQUAygrKkuM7lJkyEDdeosc57TWxu7cpo8814Mn9P-kJjMUWNyrmSQiyRqJG5jZ-YTcsEuDAkVTfMcUMbUE244iI5vFKsMEGxR6JwXTc1byFqq2B4XCIHxDsCiQJVEnZlzH2ThyLHyoVsUdqw5D4m133btOK8dEY-Vp3g7AmMAwQBVRL7jj1SVZj-UaFwUMB7Zkpq9Wq0Cree_Y44HD0nP9i-2Zc2LYsDyJtDNM8EXcEnDwZG4767n7i2HiBCXfkDF6wClbOWij0jNAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم یادبود شهید دکتر علی لاریجانی در مسجد بلال رسانه ملی
🔹
مراسم یادبود شهید دکتر علی لاریجانی با عنوان «صمیمی با انقلاب»، ظهر امروز دوشنبه در مسجد بلال صداوسیما با حضور رییس رسانه ملی دکتر جبلی و مقامات لشکری و کشوری برگزار شد.
🔹
شهید علی لاریجانی دبیر شورای عالی امنیت ملی و رئیس اسبق سازمان صدا و سیما در ۲۶ اسفند ۱۴۰۴ درپی حمله دشمن آمریکایی صهیونی به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/652841" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حملۀ تروریستی گروهک پژاک به یک معدن در سقز
🔹
حوالی ساعت یک بامداد امروز گروهک تروریستی پژاک با سه دستگاه خودرو به معدن میرگه نقشینه در سقز حمله کرد.
🔹
در این عملیات تروریستی ابتدا دست و پای هر دو نگهبان معدن را بسته و تلفن همراه آن‌ها را خاموش کردند، سپس اقدام به آتش زدن تجهیزات معدن کردند. مهاجمان پس از حدود ۳۰ دقیقه محل را ترک نمودند.
🔹
براساس گزارش اولیه، یک دستگاه لودر، یک دستگاه بلدوزر و ۴ دستگاه کانکس شامل امکانات کامل رفاهی، ابزارآلات، وسایل تعمیرات، قطعات یدکی ماشین‌آلات و موتور برق دچار خسارت شدند.
🔹
چند بیل میکانیکی و خودرو سنگین نیز مورد هجوم این گروهک تروریستی قرار گرفتند. هدف تروریست‌ها باج‌گیری به وسیله گرونگان‌گیری نگهبانان بوده است.
🔹
گروهک‌های تروریستی و ضدانقلاب با هدف جلوگیری از توسعه اقتصادی و اشتغال‌زایی در مناطق مرزی، زیرساخت‌های حیاتی را هدف قرار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/akhbarefori/652840" target="_blank">📅 15:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk4k71EV_j58GeJNjE2Dd_SOteZD9ZIENZWX4UMTcLWbZO2f4q7D63vczPxi7PVr6OEyKL6pB93Em_a0soWnoM_XEUxnR6QPRB34KnxAEJl50fvgz1qfq51Tj1JouL54omJiZk9obHu7Y0YXOEmMbZuzpmEYGHHN7s4zTWEAhdfC4LuSAsDOoRLkH9Gq6H3D8XhcLpVstS_k5uvfAy5JzC8MkfAaO-bWUlYQEbbOi44PhWP7-y53E-I7RT6fVVmLLCscKCLzPn9_j_96E6hWrra7TDxnc-2wxnx-hlWGZWgTJqyaZN-K5oMzFs8zJD63NrlvHq9JG5xBmc8Crjc2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای حملهٔ هوایی بر اثر حملهٔ موشکی حزب‌الله در شمال فلسطین اشغالی فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/akhbarefori/652839" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سرنگونی پهپاد آمریکایی MQ-۹ در استان مأرب یمن
🔹
رسانه‌های محلی یمن از سرنگونی یک پهپاد پیشرفته آمریکایی در شرق این کشور خبر داده‌اند.
🔹
پهپاد MQ-۹ Reaper از پیشرفته‌ترین پهپادهای شناسایی و تهاجمی ارتش آمریکا به شمار می‌رود که برای مأموریت‌های نظارتی، جمع‌آوری اطلاعات و حملات دقیق به کار گرفته می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/652838" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-SxJvgHkEbAfQTlmOcQV2IipwhRRVr7W7Fs0zRkREBdCpri2zUc7wHOn3Wk-Eci4Tow4EXyQLNT-_yrb5NaJdbZqtJMrKRAm7amnq2Wk2pZ227ot0mGs8hkThIN-PwpH-vn6hA83JvufFuXCvANbjdu7ipe3scCtoh7p2q5wcZhPGXSgJTPje9tdgrlTXu73c2oXxSnCnpBJr5gR03NO0S2hpoVR8zeLoH3pBfBcZHtudzubuOhhDk5Wb3_8Jnp5Kr84zhMEymgfN_c_BeqPGBT3EqZ2RjbPt4ScE_MY8BKJygwINVxPAPV6ye45fudbscl4FFdw__j__fiYX4aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات پیشنهاد جدید ایران به آمریکا به روایت منابع غربی
🔹
خبرنگار کانال ۱۲ اسرائیل در توییتی مدعی شده است که در آخرین پیشنهاد ایران به آمریکا هیچ اشاره‌ای به مسئله تنگه هرمز نشده است.
🔹
آمیت سگال، از خبرنگاران کانال ۱۲ اسرائیل ادعا کرده که پیشنهاد جدید ایران شامل تعهدی — با ارزش نامشخص — برای عدم تولید سلاح هسته‌ای است. این خبرنگار همچنین تأکید کرده که در این پیشنهاد، هیچ اشاره‌ای به مسئله غنی‌سازی اورانیوم نشده است.
🔹
جنیفر گریفین، خبرنگار فاکس نیوز هم این توئیت سگال را بازنشر کرده و بر وجود این موارد در پیشنهاد ایران تاکید کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652837" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آمریکا در متن جدید خود اسقاط تحریم‌های نفتی ایران را پذیرفته است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در متن جدید پذیرفته‌اند که در طول دوره مذاکره، تحریم‌های نفتی ایران را Waive کنند.
🔹
ویو کردن تحریم‌ها به معنای معافیت یا اسقاط موقت تحریم‌هاست.
🔹
ایران تاکید دارد که لغو همه‌ی تحریم‌های ایران باید جزو تعهدات آمریکا باشد. آمریکا اما اسقاطی اوفک را تا زمان تفاهم نهایی مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652836" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وزارت اقتصاد: مهلت ثبت‌نام در طرح اعطای تسهیلات حمایتی به بنگاه‌های آسیب‌دیده در جنگ به منظور حفظ اشتغال تا پایان اردیبهشت‌ماه تمدید شد
🔹
تاکنون بیش از ۵۱ هزار متقاضی در این طرح ثبت‌نام کرده‌اند که حدود ۴۰ درصد از آنها مشمول دریافت تسهیلات شناخته شده‌اند.
🔹
افراد می توانند با مراجعه با سامانه «کات» به نشانی
kat.mefa.ir
برای دریافت این تسهیلات نام نویسی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/652835" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رئیس‌جمهور در نشست تخصصی با مدیران وزارت راه: پایداری تجارت و تاب‌آوری لجستیکی، خط قرمز دولت است
🔹
پزشکیان استفاده از ظرفیت کشورهای همسایه در توسعه زیرساخت‌های حمل‌ونقل، ترانزیت و سرمایه‌گذاری مشترک را از محورهای مهم سیاست اقتصادی دولت عنوان کرد.
🔹
در این نشست، بر شفافیت در توزیع بار، افزایش هماهنگی دستگاه‌ها و تقویت زیرساخت‌های لجستیکی در شرایط جنگ اقتصادی و تحولات منطقه‌ای تأکید شد.
🔹
رئیس‌جمهور رکوردشکنی در جابه‌جایی کالاهای اساسی، بهبود تخلیه و بارگیری بنادر و تسهیل عبور کالا از مرزها را نشانه ظرفیت بالای مدیریتی کشور دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652834" target="_blank">📅 15:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دامداران در انتظار افزایش قیمت شیر خام هستند
🔹
نایب رئیس کمیسیون کشاورزی اتاق تعاون: متوسط قیمت خرید هرکیلوگرم شیرخام از دامدار  ۵۰ هزارتومان است در حالی که حداقل قیمت تمام شده هرکیلوگرم شیرخام برای دامداران ۶۴ هزار تومان است.
🔹
با استمرار بلاتکلیفی اصلاح قیمت شیرخام و زیان دامدار، تولید شیرخام کاهش می‌یابد و دام‌های مولد روانه کشتارگاه می‌شوند.
🔹
با اصلاح قیمت شیرخام و حمایت از دامدار، تولید شیرخام به بالای ۱۳ میلیون تن می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/652833" target="_blank">📅 15:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a808ae49.mp4?token=O4_XEYXyzMFdHa5SMnAr0uXsJouOrXchqIJJIyEzWtdfjwHksv-taCI8e_lZ07n9sxx3enxNjY0v3Q71m8fro-x3vYCbeqAQy92wXer6KXvTXzKlrb1VGkYQqWrxPi8KpFfZ99oxaGO80XjiACIbYcGvrFiEuT_0_4DYxxIxGp5VkRl12HR3-tHTi2wDdSeOfGSaW3UU9pP_VDZNPDZX6SpgZkL8qCNZEs_d48Ns9jZ6rp5GRSBEVQsUSFpq73-El1LRqFvUqMCqXTtDipo3ez0jckJ7OGlzq5_2pjYQ98O-QHnMyOicvNJhAXTy_2lkTWmVQYJU_L_dJzrZSL0WDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a808ae49.mp4?token=O4_XEYXyzMFdHa5SMnAr0uXsJouOrXchqIJJIyEzWtdfjwHksv-taCI8e_lZ07n9sxx3enxNjY0v3Q71m8fro-x3vYCbeqAQy92wXer6KXvTXzKlrb1VGkYQqWrxPi8KpFfZ99oxaGO80XjiACIbYcGvrFiEuT_0_4DYxxIxGp5VkRl12HR3-tHTi2wDdSeOfGSaW3UU9pP_VDZNPDZX6SpgZkL8qCNZEs_d48Ns9jZ6rp5GRSBEVQsUSFpq73-El1LRqFvUqMCqXTtDipo3ez0jckJ7OGlzq5_2pjYQ98O-QHnMyOicvNJhAXTy_2lkTWmVQYJU_L_dJzrZSL0WDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشنگیِ ریشه‌هامون به اینه که تو اوج سختی، آشتی و همدلی رو یادمون نمیره؛ برد واقعی یعنی همین اتحاد بی‌قید و شرطمون
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652832" target="_blank">📅 15:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwTtUffmtSgARsvdLS7irLzajnGpUjqOlLp9HXHySLg1ZgYg-QGdN3O8pGSoxdkfqtsUSI49P1pDDUsYVXddcTR6olzliB3F5tOCxrKEAf-EoTPgGR3sl0Yw3TyFn6TJrpzIZjCx5dlteIZfimfjZ7p_sIUcfyIv78v5JVmxisNXmPNFGe1Unuia3-0Yb97c28lH2KBmSqKS6uAaQgyfmJ_8tu6O1-BH-Vc1xwu_if9mDmXatUL_1NZgFM_OFeT-u0mX0n2epGqAvDZ_rJBuJ1gU8YlwbS0RPCiJWJpZet_BBB31zkAzcXi0wUOcNTbyEHGlcOakZehEZl9tOzOeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر بطری و هر نی پلاستیکی، ردی طولانی در طبیعت باقی می‌گذارد
🔹
بیایید مسئولانه‌تر انتخاب کنیم، تا فردا زمین قابل‌زندگی‌تری داشته باشیم.   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/akhbarefori/652831" target="_blank">📅 15:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jluthzxAiO7t4yrpFoQvz40lBkC7nXky_9pDixN2zDOekhOk6OB8vzZnOITNp_-ZLcPlAAoxfD3oL3M1VUExt00aIfcyuLUeDDcIVagUjo5RZilplGbZ6ypi79CwT6LaAciWhymXhwa4HugpCEu3KgqAaeK0JAogherypH_4i8z_XDiquOArhCxTtdd5VAKSYtYY0IUEuaAp7TxqrxKCkJd33lqVaWa6OoBOu3bxZaPwWp__rMcN3ZL7YR5y8iesT2KzV9NshuSIrCL8yHajuAAwA1rS_SfIXMn7Ch99I1Hkoriic78TpqFYXKZ3Bvh-y0onRb1UBxGfBC2A6bVrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای سبز ایران قفل اروپا را شکست
🔹
اتحادیهٔ اروپا پس از ماه‌ها مذاکرهٔ فنی و سیاسی، محدودیت‌های وارداتی پستهٔ ایران را لغو کرد.
🔹
این محدودیت‌ها از سال ۲۰۱۹ به‌دلیل ادعای وجود باقی‌ماندهٔ سموم و آفلاتوکسین اعمال شده بود و باعث افزایش هزینه‌های صادرات و کاهش قابل‌توجه فروش پستهٔ ایران به بازار اروپا شد.
🔹
به‌گفتهٔ معاون امور باغبانی وزارت جهاد کشاورزی، این تصمیم می‌تواند زمینهٔ بازگشت گستردهٔ پستهٔ ایران به بازار اروپا را فراهم کند.
🔹
برآوردها نشان می‌دهد صادرات پستهٔ ایران در سال جاری به ۲۵۰ هزار تن برسد و ارزآوری آن از ۱.۸ میلیارد دلار فراتر رود.
🔹
همچنین بازار چندصد میلیون یورویی پستهٔ اروپا دوباره در اختیار تولیدکنندگان ایرانی، به‌ویژه باغداران کرمان و رفسنجان، قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652830" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlutIe2LDLQitxrphUp2_Q220OTNxgOEg9_lu_UcjMJFnK7sM-oSKS8YR8GQUyfIYUBxeyFwHxgcIw_YLPHrWV0srhBujo-zHf0fhM40aOu_rYBt7v23ndWe750Sy5qNlRG45YnM0SIWs0cASCKy6SIqMSp_Ca35YgksYyylDfTzYD9SwjDSUVkyxq2gQ_yIKYPYaH8uKhTZwCm0zskPAGvv7yvWxbIfIZbr-rb8nZgjz4meO7fALntIMtwQhuuwZq81NQ42cR0XEZy8xJ-E5S6iyRRO-hMFzCusEJOXSsAo3_2HrLXANplPLtwtg-o3c4fbAE_wzT5DDTYkAhACzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور گسترده نمایندگان در جلسه مجازی مجلس؛ خانه ملت بر مدار نظارت
🔹
برگزاری دومین نشست مجازی مجلس با حضور ۲۲۶ نماینده، بار دیگر نشان داد فعالیت پارلمان در روزهای جنگی متوقف نشده است.
🔹
در این جلسه که با حضور وزیر تعاون، کار و رفاه اجتماعی برگزار شد، نمایندگان مسائل معیشتی مردم، اجرای کالابرگ الکترونیک و حمایت از تولید را بررسی کردند.
🔹
همچنین از آغاز جنگ تحمیلی سوم تاکنون، بیش از ۱۰۰ جلسه کمیسیون ‌های تخصصی مجلس برگزار شده و جلسات نظارتی و بازدیدهای میدانی نمایندگان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/akhbarefori/652829" target="_blank">📅 14:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
محدودیت برق برای صنایع تابستان امسال اعمال خواهد شد؟
🔹
عباس علی‌آبادی وزیر نیرو در پاسخ به سوال: صنایع کم مصرف و ضروری که منافع زیادی برای کشور ایجاد می‌کنند در اولویت هستند، کسری در صنایعی که برق را با راندمان پایین‌تری استفاده می‌کنند، اعمال می‌شود.
🔹
اگر صنایع اصلاحات لازم را در مصرف به عمل آورند تلاش می‌کنیم نیازمندی آنها را در اولویت تأمین کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/652828" target="_blank">📅 14:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
طرف آمریکایی اعلام پایان فوری جنگ در همه جبهه ها را پذیرفت
🔹
پیشرفت قابل توجه در مذاکرات پایان جنگ رخ داده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره کننده پایان جنگ گفت پس از چند دور تبادل متن بین ایران و آمریکا، متن‌های دو طرف درباره پایان جنگ به یکدیگر نزدیک شده است.
🔹
بر این اساس، طرف آمریکایی اعلام پایان فوری جنگ در همه جبهه ها را پس از امضای یادداشت تفاهم پذیرفته است.
🔹
ایران پیشتر تاکید کرده بود جنگ باید در همه جبهه ها از جمله لبنان پایان پذیرد و متن جدید ایران هم بر همین موضوع استوار است.
🔹
پیشرفت مذاکرات در حالی رخ داد که آمریکا با این ماده موافق است و اعلام کرده پایان این جنگ پس از امضای یادداشت تفاهم اعلام می‌شود و در طول ۳۰ روز درباره ترتیبات آن و شروع نشدن مجدد جنگ گفت و گو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/652827" target="_blank">📅 14:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwfGL5Syx2ghKhyvaAb_YYb6mcb3bCtmLq_xqB2AmA2rMYQfmBzNmrCUU67tSE_GKM8rcNpuClGGpJNsGK5kxX4-nnfoxKHIVwftoUeV8PfkAVM2D1120Rtrf3ja7F8BWKowjCR4_6zn55JrA0AXSAnd80q9BRlpQdEVE_pL7Fq8wHeGkgNMEdcAI6wfbS1oEWAH1dW-5nL9Mfl22fuvO5DOZgkTk53JZR8EmmSSZXRJZYH79DQoGvOuCzQtFtKM1TaMCdDvfXZAwUL6X-qbFgZ8tq2_7pbKT5AC_gKEAK6Ua0mErfQgJqdFXszPvVgTkPgWiNchsho11lCb6ZXldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه و بلاروس رزمایش هسته‌ای برگزار کردند
🔹
در شرایطی که تنش‌ها بین مسکو و بروکسل رو به افزایش است روسیه و بلاروس رزمایش هسته ای برگزار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/652826" target="_blank">📅 14:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3615db4f22.mp4?token=P4IvlTG2917nI0YuQPydT_9C_Nk8LsPMi8tpDANksgD_ghOPVT4rIsbcxMIkAfdr1jeBFzK5r_9lr_izZWzO46xsNzJMngdJUJuo_EkfDKrloWMlDKoEizl69jSb3f9_y01N_fJjI5du3ncMx_PNat1qVQCTVHW0GYcSUD2ZilYyAepmfxKhGdJ8SmMmxa7V0CVaStejxzSFkcnmv3oxqHtvdep1gsopVD4e84QJXki5tUIogfCnfeYxrtXc7-XsPM02O36Lumo3U_X_RrJ_5e6JTO_Rf9AcDyE7HCM-szvyOnehbuf4AMPsIayuhRJFjadr-Qk7RymjtGq7BB5xHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3615db4f22.mp4?token=P4IvlTG2917nI0YuQPydT_9C_Nk8LsPMi8tpDANksgD_ghOPVT4rIsbcxMIkAfdr1jeBFzK5r_9lr_izZWzO46xsNzJMngdJUJuo_EkfDKrloWMlDKoEizl69jSb3f9_y01N_fJjI5du3ncMx_PNat1qVQCTVHW0GYcSUD2ZilYyAepmfxKhGdJ8SmMmxa7V0CVaStejxzSFkcnmv3oxqHtvdep1gsopVD4e84QJXki5tUIogfCnfeYxrtXc7-XsPM02O36Lumo3U_X_RrJ_5e6JTO_Rf9AcDyE7HCM-szvyOnehbuf4AMPsIayuhRJFjadr-Qk7RymjtGq7BB5xHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما بلدیم تنها بمونیم... ولی تنها نمی‌بازیم
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652825" target="_blank">📅 14:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
منابع موثق خبری از وقوع یک انفجار مهیب در ورودی تنگه باب المندب به دریای سرخ در شب گذشته خبر می‌دهند
🔹
سکوت موسسات خبررسان دریایی و شبکه‌های خبری غرب در مورد این انفجار بزرگ در این آبراه استراتژیک جهانی محل تحمل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/652824" target="_blank">📅 14:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFMl5Wu_eDqaRivwW9VkVsWt6JqF6zpYRtkckT5I93E6PgWu6dyDQGc7phdyhSfUEyrK0N6pUXvY-ah2STNaV2PPlGdkS6MvWUSI-Up5SJCZF9TXbczYT0WHl4YxX9Rf9oejBSt4vsThEcy4xubM-wVZeNTk-6QzFtvnjIIFQyPVDb_w49iv1jlazoHL4U8KVv_XY-rSuw9n64fVhfkce9vrKjhA_eyrJ7Sqw6m-s05eY7J0Ppd2GfsXXZe7b9xX0cC9ZoDXpdku9o6sbl2TB2PefEmL0kpy0w6tJ6AFfq86oHvcaqRW2lw8R9ljlhEIgQonNbaQPi05m8biT9sRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده فعالیت برند پرحاشیه؛ از کارآفرینی تا اقدام علیه امنیت ملی
🔹
پرونده صادق ساعدی‌نیا، مدیر یکی از برندهای شناخته‌شده صنایع غذایی، در دادگاه انقلاب قم بررسی شد. او متهم است که در اغتشاشات ۱۴۰۴ با فعالیت‌های تبلیغی به تحریک ناآرامی‌ها کمک کرده است.
🔹
صادق ساعدی‌نیا، وارث یک امپراتوری غذایی است که پدرش محمدعلی ساعدی‌نیا از صفر آغاز کرد. اما این میراث نه سرمایه‌ای برای خدمت، بلکه اهرمی برای ضربه به امنیت کشور شد.
🔹
او در جریان ناآرامی‌های دی ۱۴۰۴، به جای حفظ آرامش و حمایت از تولید و اشتغال، با تعطیل کردن کافه‌های زنجیره‌ای خود در سطح کشور و انتشار گسترده استوری‌های تحریک‌آمیز در فضای مجازی، مستقیماً مردم را به اغتشاش و مقابله با نظم عمومی فراخواند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652823" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3311ac51c2.mov?token=obSIdbPa4-N7ApRDLB6lyZ0ZvfaqDWPMGqVbWXOhjzBIgWJE5ycE9Czwv9QLQGkxEDF5xweYzW6xlugKWwxEZxhosmv4DR1AS-pstVsKjvXBsTLpgubJB3zI8FyB3oTZQnQS4hdmiNjgaRfNDihK2CgZc5EF3qdf2oqlzH4EgHFvsMW00XSnL6reuqzdwJ0-onorXrNtkKHsEJ91Q3uy4T5bBNcfrvhwV8JHCA_EkjWZHtuCZGzVbveyKWkYdLY96-R_8n5w8hXmhRTN4LWSrTx7l2P1wOA8by50UgsmnqS19NPSeff6NJYEWTRFgPTdIVA-uh9w5nTuAsepyPVpDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3311ac51c2.mov?token=obSIdbPa4-N7ApRDLB6lyZ0ZvfaqDWPMGqVbWXOhjzBIgWJE5ycE9Czwv9QLQGkxEDF5xweYzW6xlugKWwxEZxhosmv4DR1AS-pstVsKjvXBsTLpgubJB3zI8FyB3oTZQnQS4hdmiNjgaRfNDihK2CgZc5EF3qdf2oqlzH4EgHFvsMW00XSnL6reuqzdwJ0-onorXrNtkKHsEJ91Q3uy4T5bBNcfrvhwV8JHCA_EkjWZHtuCZGzVbveyKWkYdLY96-R_8n5w8hXmhRTN4LWSrTx7l2P1wOA8by50UgsmnqS19NPSeff6NJYEWTRFgPTdIVA-uh9w5nTuAsepyPVpDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در صورت کوچک‌ترین خطایی از طرف‌های مقابل، ما به خوبی می‌دانیم که چگونه پاسخ دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/652822" target="_blank">📅 14:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828df3711c.mp4?token=CkADPyNXzc4s8sQdFfLCw9bLT5YnkoMGqz0fPsxPU2hkZ2GS--pLXHFxlJQxQodDiViB2Ronm5cqQ4AGvqvPzo9hKUxL8LKC2uNDQ0waPGhUAXYKh8Tja9cPMgcS6WG-948QuCd25QL_tm-rAHAN4EEG_MH1HtEmz3DnU7trWrPky6MAYZb4xfTI_Csph_m6CeVJrL5gUOaUdyOgcLhZ0Pk4mARNij4gM80v1we9eJp7AwibP-_FYZz_aA5I_He1qO_g1G-BIjfBAuRp2XiLXLWbpSLCCoG17DVsMTwQ28-lX5xYT2SfRyrmwMsWeS7N4dZxXkk-h_86N9-0D8TVE4RGRmoiyVbeLnvrgS1OkshV8PgbHoQlfNiMEe9_rxRudImG4Lm42-LoxLYmTA2tw6XBe6xP9u3El6iWdKM2HH8BoYGZneHzHRGleru3Mf1jROcPugFZGev6E13zH-joBBs34CYb2r4SaPsBG7u-KBGs0Zf_Caj-VCMWH3wQrCxLuKPesXzzNmbNvdPC3aE-jXZM3kYMofmJ_MeEj3HdIdyOuP3ABd5YfXFNjO-MeVVoItztoVvcstVccjjWhGBckXLREhev_rzBKQkygyx0n2RsxbwpIr-Lfh-9HoOFxncBkiL-dxcJJuF_02sPP2X-gDWdOVVSQQMExFZj9cRwO6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828df3711c.mp4?token=CkADPyNXzc4s8sQdFfLCw9bLT5YnkoMGqz0fPsxPU2hkZ2GS--pLXHFxlJQxQodDiViB2Ronm5cqQ4AGvqvPzo9hKUxL8LKC2uNDQ0waPGhUAXYKh8Tja9cPMgcS6WG-948QuCd25QL_tm-rAHAN4EEG_MH1HtEmz3DnU7trWrPky6MAYZb4xfTI_Csph_m6CeVJrL5gUOaUdyOgcLhZ0Pk4mARNij4gM80v1we9eJp7AwibP-_FYZz_aA5I_He1qO_g1G-BIjfBAuRp2XiLXLWbpSLCCoG17DVsMTwQ28-lX5xYT2SfRyrmwMsWeS7N4dZxXkk-h_86N9-0D8TVE4RGRmoiyVbeLnvrgS1OkshV8PgbHoQlfNiMEe9_rxRudImG4Lm42-LoxLYmTA2tw6XBe6xP9u3El6iWdKM2HH8BoYGZneHzHRGleru3Mf1jROcPugFZGev6E13zH-joBBs34CYb2r4SaPsBG7u-KBGs0Zf_Caj-VCMWH3wQrCxLuKPesXzzNmbNvdPC3aE-jXZM3kYMofmJ_MeEj3HdIdyOuP3ABd5YfXFNjO-MeVVoItztoVvcstVccjjWhGBckXLREhev_rzBKQkygyx0n2RsxbwpIr-Lfh-9HoOFxncBkiL-dxcJJuF_02sPP2X-gDWdOVVSQQMExFZj9cRwO6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون | چیرگی نظم ایرانی در تنگه هرمز
🔹
۱۵۰۰ شناور در تنگه هرمز منتظر اجازه نیروی دریا سپاه هستند، روی فرکانس ۱۶ همه شناورها این صدا را می‌شنوند اینجا خلیج فارس است مسیر اقتدار برای عبور از تنگه هرمز اجازه بگیرید....
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/akhbarefori/652821" target="_blank">📅 14:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxJ-SddBEpTL8D9y9Ay3iEYe9NCjXsU3NSFeIJAoo79Ake__EPQOi_-Nb_7GQPUEwmdLFNyoJ-R72XNvcrTjQwZUppnfyIX7vhls8kSebnvSF88XYb7QkkNoqHwPE_oeMVjpjy0DZzouZXQelTk69nABsHacT3AhZZ9O-aTcvuuAI2mlWcP6A7ehJPgvltDanTuAH2SUnjijjVb_4S-mvs2Z6AnMeilZJaLk_MHTze9qc9xxMADLQ_ymLO9wK98ulGNlJeLU1hc0-1TOaJDWnq9FJ1GWoDfMkeR0DAC5iiMzn6wJ6wFRnrep8SCXQpJyYgW6mUUCGyxWupZpW-a8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنج ۱۰ تریلیون دلاری در کف تنگه هرمز
🔹
پس از اعمال مدیریت روی تنگه هرمز، ایران با استناد به حاکمیت مطلق بر بستر و زیربستر دریای سرزمینی خود (مطابق کنوانسیون ۱۹۸۲ حقوق دریاها)، می‌تواند تمامی کابل‌های فیبرنوری عبوری از این آبراه را مشمول مجوز، نظارت و عوارض حاکمیتی اعلام کند.
🔹
براساس گزارش Policy Exchange، این کابل‌ها روزانه بیش از ۱۰ تریلیون دلار تراکنش مالی را جابه‌جا می‌کنند.
🔹
هرگونه اختلال در این گلوگاه، به دلیل عبور کابل‌های محافظت شده دارای فناوری DWDM، می‌تواند روزانه ده‌ها تا صدها میلیون دلار خسارت مستقیم و غیرمستقیم به اقتصاد منطقه و جهان تحمیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/652820" target="_blank">📅 14:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQNU34utQOhOA2_nI_MeiRP83DsPJsA0RS27HLHCUT-hIMo12fWkx9-huf_PwSykKmVK2J07DMsU3xjvOgAKfhBrMY81rxwkhUw7Sp08UmepoK-_w_YQV-6C4WuJqe-TdyGtyGo13bUmeVNeKl6BQVEY9viqDcFZym9H0ABoOD6oev49jTwGm5pYhJfUAj67FkloseAOMrzSAe1mNMxkiKbAZ-FqjBz2yDpJi4FgUDlmuAqQvnQuxHX4x2LKfpyb35lRfcMSlTiU1QIIrB__JMIO5Cp86Gm60P14AEeMge04KHvj4UB-VKtcbBp5xCLG8gxgd2SJOAV_LQYmlZudTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برلین: جنگ با ایران باید برای همیشه متوقف شود
🔹
لارس کلینگ‌بایل، معاون صدراعظم و وزیر دارایی آلمان، امروز دوشنبه پیش از عزیمت به نشست گروه هفت گفت که جنگ با ایران نه تنها یک تهدید جدی برای اقتصاد جهانی است، بلکه «خسارات عظیمی به توسعه اقتصادی وارد می‌کند.»
🔹
کلینگ‌بایل سپس تأکید کرد که باید تمام تلاش خود را برای «پایان دائمی» جنگ، برقراری ثبات در منطقه و تضمین آزادی خطوط کشتیرانی به کار گرفت.
🔹
در نشست وزرای دارایی گروه هفت که از روز دوشنبه آغاز می‌شود، شرکت‌کنندگان بر تأثیرات اقتصادی جنگ در منطقه غرب آسیا و پیامدهای احتمالی آن بر تجارت جهانی متمرکز شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/652819" target="_blank">📅 14:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae6d4bd95.mp4?token=RVuKpUPoJChzwAwX285Qhd7cWzGIf2z2W3d2rbsAENmUMG1Rx57XXwZvIk5W6KOJp9N2keCNxMy02ocMJKck3pWZOmD02xVfEeD_a9You4QpJpuNjc126VKFd4roq1T8Q7rDcOqT8WqxWHEXj6YY09H6O1ZpOiFdE_Er-70kDu5JyD3Ti-GrlZrxseQlku2DVZrYKp1kzD0VdJmLcMZxD8A4-nWJIopnaQdMjHg87KVtPMPtECjYzhf-PkwNzcFgFliVz5AvagiHby6XICjUgRCXSqKxtoKtLdJISTgA2YSw7OKDNejtfqludiaiPH0MAgLpK7NHV2kGK8OysOETww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae6d4bd95.mp4?token=RVuKpUPoJChzwAwX285Qhd7cWzGIf2z2W3d2rbsAENmUMG1Rx57XXwZvIk5W6KOJp9N2keCNxMy02ocMJKck3pWZOmD02xVfEeD_a9You4QpJpuNjc126VKFd4roq1T8Q7rDcOqT8WqxWHEXj6YY09H6O1ZpOiFdE_Er-70kDu5JyD3Ti-GrlZrxseQlku2DVZrYKp1kzD0VdJmLcMZxD8A4-nWJIopnaQdMjHg87KVtPMPtECjYzhf-PkwNzcFgFliVz5AvagiHby6XICjUgRCXSqKxtoKtLdJISTgA2YSw7OKDNejtfqludiaiPH0MAgLpK7NHV2kGK8OysOETww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظارت مجلس بر بازار مسکن به عنوان یکی از اصلی‌ترین دغدغه‌های مردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/akhbarefori/652818" target="_blank">📅 14:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
دستگیری عوامل وابسته به محور آمریکایی-صهیونی در ۳ استان
🔹
طی اقدامات سازمان اطلاعات سپاه در استان‌های قزوین، کرمان و چهارمحال‌و‌بختیاری تعدادی از عناصر وابسته به محور آمریکایی-صهیونی که قصد تولید ناامنی یا اخلال در نظام اقتصادی کشور را داشتند، دستگیر شدند.
🔹
قزوین:
🔹
دستگیری ۲ جاسوس وابسته به رژیم صهیونیستی
🔹
انهدام یک شبکهٔ توزیع سلاح‌‌های جنگی و کشف مقادیری سلاح و مهمات
🔹
کشف ۱۴۰۰ تن مواد اولیهٔ پتروشیمی احتکاری در یکی از واحدهای صنعتی
🔹
کرمان:
🔹
دستگیری ۸ تن از عوامل اصلی اقدامات تروریستی در سطح استان
🔹
چهارمحال‌وبختیاری:
🔹
دستگیری ۲۲ عنصر در قالب چند شبکهٔ وابسته به گروهک‌های ضدانقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/652817" target="_blank">📅 14:17 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
