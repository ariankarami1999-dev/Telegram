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
<img src="https://cdn4.telesco.pe/file/q7btbIWmJNxPbtsN00J1Zi4cY88SLk0JgU9gtsLuXRYDwwFk70wZuIGYEgyrpU9vpA_FCzMyi9qCVlXIHJzuKj8hTg9qZR4FkvR4maYaRdBEZQnbRtA9arG80gXUDj53vasPCUtLUU2ApBzXfnYvH9AyMUKaikeGFwyIFB2lv1QAMmC_23flN-xjvYaExg9ASNsThwCVom0bY8xChVdNU31d9HoMdM3jme67LFfYwphT3CV6iUFqYlSleg9wSCiWJ0o4uAw8WN2Gv7Uz4BBYSPkRwV7tSqRNxeebqHurVgkBwJqNrbatu-Griaygm7jH-CqdCQ6JQ4vPSfphSWhVUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-670105">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h04H9RWWMnHxXFjqDXM03Wb-ozgWTzjpMhqfEkuZ5v2H-XGJegqad_w3L_x6rRxIQuiwGMIa1OX1pGAzrhD3lTWI6PV26a2yl72QkTN9LNKKHxmzfgpWm0bDWXWCyu_s13Gqt_C1CK_b_RUI5f3Jm8qhb3hcvxYLgIJdNC7TVEz9rjWWKVG3CImA29znaNWqFMptyiu9Ljcj3XQvGxHqS4tWbcPvbjot8jikdHuV98Q9IOTnSCXhq8Y7UUNsfShQkY6_zIgOc6AhdrtyTwMagvCOE5WzVfq2Z1ERL0_m7vbSW_EbwvH-HIlhyws3s3s-W7QuHprOaia3Y-KeAhW2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل
|
#واژه_کاوی
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/akhbarefori/670105" target="_blank">📅 13:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670104">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjaSGiFNgcfefFNt0Pdp1DoUauBjE3eNmHKzvPNxtFCsHoAmWqbCYfr5H4oqdtXASTgw6O7lMJY2-Z1hROR4BPcB0R-hLpMmqGg09TnE7fdx9zCRuKPuWL6ra5FILLXbMmLriR9doiaS_Xcfqmxd5ieKFiC4xLGqxIc0pAneUhhgRZP_frQ0GUk686SwzDG3aWHCvJZNOGLPAs_5f8fo5-2O9dQv5vTpu7uP-2YiuG_UclsluwQATc11vNZKK-o9ECPA3_7tbGWJoKm5uNosfXkHPtQYiuL3TZ66WbvMl2NjFnDECbpKV4h59wdxrPE3YFqy_vnLTv_TahZLGCSbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف محراب تاریخی در محوطه جهانی پاسارگاد
🔹
رئیس اداره میراث فرهنگی پاسارگاد از کشف یک محراب تاریخی در جریان مرمت و ساماندهی محوطه جهانی پاسارگاد خبر داد.
🔹
به گفته او، عملیات حفاظت اضطراری و مستندسازی این اثر در حال انجام است و نتایج نهایی پس از تکمیل مطالعات تخصصی اعلام خواهد شد.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/670104" target="_blank">📅 13:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670103">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBRMFLFmCzDqKsk5fifFNz9yMhegVybGVpqx2OeMwiLpsqRDCCt4AyQrdFFI__8F_3AcA9FmpCQ8HQQssjMBAlu8GqBUVJAEq_aBAyA-hOiuNMVCMMO2Dyft8Ww6-qmfQJAEmoUaRoV-teF3lWBJ3R8D07finDkFjlh1xGJFiTJYwWp2pYGkPiXl10bAmWIkcL3eC8qynS5hsN05zKFxaDnCh_JGJ_FONwi8QgPHVyGZ0fJ8xS4uHGHOrquDdecNXXospSTWscg7aEe_MXCxCr74F7QQAgsOrjiVjsxYWykPpQYfO3ktCkUtV2kx1Kmd1XbC9AmuV7efAwNGfXgFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه شرکت توانیر درباره نحوه اطلاع‌رسانی محدودیت یا خاموشی‌های احتمالی
هم‌وطنان گرامی؛
📢
اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری (جاری) صرفاً از طریق درگاه‌های رسمی زیر انجام خواهد شد:
🔹
وب‌سایت رسمی شرکت‌های توزیع نیروی برق
🔹
اپلیکیشن «برق من»
🔹
نوتیفیکیشن و بازوی (Bot) «برق من» در پیام‌رسان «بله»
🔹
کدهای دستوری USSD
🔗
جزییات بیشتر
روابط عمومی شرکت توانیر</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/670103" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: سطح تهدید دریایی در تنگه هرمز همچنان در بالاترین درجه خطر، یعنی «شدید»، طبقه‌بندی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/670102" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByQ9oBSA7oDNlL8Ux4upC9cBwUqzSL3wTfSCOhaI0SO2GwLPewv3_8abhtaVTawbxUXAB4RV-VfmzFKOdsdj40einpLSCq15apHsCY5osRr8upjX7YdG69RuupmltL9CAQMmM0ViKCtwO_mqGXvBmAOULZkKd0c-RDXJA9m3tv_bms3ryqomQJRzK79vwraUnVACNUSzC4ues5feKBW7MUASWyTo0vOzA9Zr_hTntUbadjqB3rmn7pLVtrVEy4jQh4Vt9aBKMlNUVI_vWk2CwAOgLLiw0seu1G8EtYbzZoDNpRDl4JjkTOjSZn_uzjoVQOWtxC7U9RgSG0S_dpjqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670101" target="_blank">📅 12:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: نتانیاهو در حال بررسی امکان سفر به مراسم تشییع جنازه لیندسی گراهام است
🔹
در صورتی که این سفر انجام شود، به احتمال زیاد با ترامپ نیز دیدار خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/670100" target="_blank">📅 12:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آتش‌سوزی در کشتی کانتینری در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلستان از وقوع حادثه‌ای در ۹ مایلی شرق عمان خبر داد.
🔹
مقامات نظامی تأیید کرده‌اند که یک کشتی کانتینری در بخش عقبی دچار آسیب‌دیدگی شده که منجر به وقوع آتش‌سوزی در عرشه آن شده است./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670099" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجید، بازیگر قصه‌های مجید: ۴۸ سال دارم و ۵ سال است که بیکارم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/670098" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJFx-o8BCmEK7j93PlMBsHSlxhZuXHgbRLX2GlLE7eu5ZFcOwcOxkt2ycO_ydjNSnrH9_4NKfZTBr51pze2GzEzlE5dbZ7bsjsZD0lYPEsNb9-z8J8xTUiCtH1GyHlvJytE_yDk_z8jK7w2MUi503heP4VVIbypl5-eAFr8zs-r8lLEJQkMDGaFT9ajC1oUmGMLIXBil_4rgdVZqjeBwgXZaD6ufk7ab-5aqSMvMAQs9A_J4SfTMrVA3V2glcCD3P1oeaSOsc3HibHeN4YPqYj9HRVRQmU8YKdhvg9lXjtNppyzOxWwoIAn2_Rfmeej9CCrjYJdzeCUHVL3MeZXc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز را حفظ می‌کنیم؛ انتقام مسئله اصلی ایران است
🔹
سرلشکر رضایی، مشاور فرمانده کل قوا، با تأکید بر اهمیت تشییع باشکوه رهبر شهید و بازتاب بین‌المللی آن، خاطرنشان کرد که این حماسه مردمی موجب خشم دشمنان شده است.
🔹
وی با اشاره به نقش راهبردی تنگه هرمز در تأمین امنیت و منافع ملی، تأکید کرد که ایران با اتکا به توان دفاعی و ظرفیت‌های ملی، از این گذرگاه به‌عنوان عامل بازدارنده صیانت کرده و آن را حفظ خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670097" target="_blank">📅 12:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE603t4ntRVyYiOC_paJv24F0sPpjK7O6i__oZ_NPRNW97qp882G0NOmp9DZF8sLm9H8cH4xuWGMjq0K3UTIUylJKB5SB3NHJ4cnZXnhWgsO_ybtD9nr4HPp5bqMXf9uIzwqKnoZpL-V8EuYpGA5ZKikoHHbHKzHW0Nf6DzUKRsLqyNQXqgXe4b0t8LAiYThaojgJv1uWg-CelWewV54qKmU-UBpE8dTN-6u6wfRHkzlQMgWTELFNNXaL22H3TEWUamweXtEBOzdgkZzzaBw_2_SYZhCB_eJh6PanMFMv82XtksXQ0T18eBxBCZHKXmqzA2Er-QZqKmavnz7kLkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670096" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtrCUsUIFUfaW9eWJYhX2XA_P9pE_DM2vI_j0zT0k7IBFQ_PlYFhz5JZdLgEDzdwWYh65CaIrZAT55HZYT35uzO2_EnTPHi6wQ3yvholK_5TrPkgfgUAqXHFPBY6QNaZtC-5_iuG2ZcyEa1pl2_4CJgkjQKm5akXx9iNwzFphii8RE9t0K7h2ShoLWZZsPYNr2OwY4IfNGrOqDz7nsxUuk_YrBlXCupaAdn66V2RtUuQmVGIanPcBNukQZPszl9JrnzppVD-6TWkZeSF5d4rMsu-4nXNM8RQhpYscWD5klMG24O1lYsdZk47WHUdXcaX5uGq77Bx9Cd5w0gN8GnIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_8DbyJYcjbpZDBV1N6VCbqGztXdZaH9ecbBip9e4oZA56vwxixMSdQ_1ZfyWJQBexWBF-NJ1eFJ53-RFROUr30Rt1nyKMsvFBi0dyDGjG_4iORA4hHq0farqFBrXIoho2yIqPX46hd_1hpEpAcd8nPyXgU623p-PLsI08xypBdJejnp2mhG7fBK0XhBlt6csBixpUVFttiNbW6BpdeEtHHGGFKXZPzrcjqYnj3lg01Vy3ZMLIc0ajauo7SSTcm8XdUbtbeyVtgCzbBSn0vbqTlukdSA3RW3QM_pFFfsQG1S2R5QOSo93IIivrlhae2V-cUXIRyLbueEUm0EprJfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAuLlFqpr28SRM8IQB7l9PzHER8O7UAkXtfMJJzji9qOhI80bQPzdcDguw_COYsRZoNwbNc97DTdNZGBIj7Qyq1TyWEMQGWUGHT369eh9CcHrz6WztwcL52dSLcdHFEefsd9rS3MY_QGkleyZldfUIFOZUIDF9B2E_1cUGt07Q6Ca9r79qr6Kt6yb1iuwifKPRY4cZwQNtgUy5JS8w50xlwOKB7g3K3a18d-54sSAtHRlASSrT55aDSqQeNkJ1J3iDkhEFzx_2ys6mF576DHC3iBDW9iT7Ww8p89HvclnJtIPPU7LQaAp1Q0GT1lhaa28Rcm_OPQ5RG0ONr61spi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNOBl4LjCORShrXiYFHqDgkf3Hlqb4JyOPWF84o4jxkyA5o_nSIspSLw0r5gHYO8SKI8UQRz2_QUz4HXW4EzLkaqTec9Sy45lxRjakbkFW-Ify7qweKDfQcdlDHurZ_m-tXUKnpZnEgaNUZRHmwuCwWgS3f3kRQ3x0x7lcxFlSETN_vCvBSlwBkGWBDm58Frwj1E70EdO9365It_Lsrf7a6VCcbnemZniNGweKaCA_mbeg6O7paFt__VCsGV1MvE6rexTi8o9Vc0acK42XUiJnGwgY9NZnE9HQX9DY1a46-qx4RqjopgX8fxW4_xZUcb7h-bJ-njbOj3IBtxwYwAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3JeGNVSZZqvtLk8cSmPOkzpgBbtdZGSJ8XvoIS7eha9VvTEIYjquifHrKV-xDxz6spUZh7RBy9uQ5BoWc-d9VbmH5zz8k-cf_vRxaGzhmycwjvK0Jvqui6xFhKV4zpy33BQIYWAijVWq7YJ_QGmYiTnyH1IDdaNpKwNajkOr4bg53oapZgvfyQ5K0Jm1LQFUklIbY4lXhuxWRWXYQco-uPEb1m7pSRLuV6EDPOyybCHpLDS9z31sIvC-_4hPPu93V18L06wuajgruacOI08axwQLE0veElzWWByLc65PnbaQvIe0Rj39PWJjVAkQwUtfrb4dG9i9BQWRE4aII3u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne8Ks8Ymzw0SrM6zrgWFJAH9XCfbQCQO2zSCO-ylRvmh0NPR6ybK4rMYFv6EjYZnP0qdiT96EcJDsQaw7yAHCZUFlju5TRQ_tdhB0gjV2or3rKDiumIOrzJ3IpHytrwMEDaEOu5a576R9VQpJXFZtH3QyqH-XRQhvUXwGTd4U-8Xy-FEH9f9qt-temSIKofMIDBSsv96uw_PXrDI8qLTNvwhE6ojCFsyA2V-sxD7ER-4Cmt8EqF2qt7Vo9pRQNPUS-uy3pq-msZEcxiMZSj8qtCFArH41igP9jiOmbc9hbRFhMjDbSL_iNroh35OgFAxQL_mXhNtuccb_-x3xMSoOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شما تنبل نیستین، فقط نوع خستگی‌تون رو نمی‌شناسین
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670090" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/980d7c9713.mp4?token=m1Q-kty1IyWoOCL4Ydd91SSslcFyxHESV1hyhCMNZegU5BpgzYZfFfOvmtEet9xaklOvRgV6VB8fHEUveokePHnYCWD709aLTr0Xp6TtmBJbrGLhfSkx74Kc-BNy-Eyg8VZwx7uc3NmxaZoXuXt-cfGTALhFZzYjakGwYb9GPeYpdsn539fCDXj8JUSyCGGmnHssa4qxMCJEuTz4k5FNFk5st9_PNCGEbiMqE7_qz8DhxWul1_c-VmJpBpThwfaxZLTnBpbQRYJ-XF5TJJ-Lyg-8TJw03GzM1YBiyKkpWgYhBZrf1YRT2XFz5RlOYZpEdYy5Nx6t1fg4Z_ky3GZfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/980d7c9713.mp4?token=m1Q-kty1IyWoOCL4Ydd91SSslcFyxHESV1hyhCMNZegU5BpgzYZfFfOvmtEet9xaklOvRgV6VB8fHEUveokePHnYCWD709aLTr0Xp6TtmBJbrGLhfSkx74Kc-BNy-Eyg8VZwx7uc3NmxaZoXuXt-cfGTALhFZzYjakGwYb9GPeYpdsn539fCDXj8JUSyCGGmnHssa4qxMCJEuTz4k5FNFk5st9_PNCGEbiMqE7_qz8DhxWul1_c-VmJpBpThwfaxZLTnBpbQRYJ-XF5TJJ-Lyg-8TJw03GzM1YBiyKkpWgYhBZrf1YRT2XFz5RlOYZpEdYy5Nx6t1fg4Z_ky3GZfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله سنگین اوکراین به پالایشگاه اسلاویانسک روسیه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/670089" target="_blank">📅 12:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlc1qEJfEe3YWrI6N5pLkGkoOOYd8Hpb2CNBnwSFIvMZLURQrn0bd5eqBTdO0myBre3Qo6AxW_tiwB0mwWDA1vNHtPaG-5tLVMtc0pR0naFpTNWvfm9DcaXNXel61Sru2FaUQHEInpHdpU3GiwGvO8pOPHYryIB-p8_CqSffV9hA8DZU_IE3NPs2xhdy3NdsTDEGCYLyuDcEhe-_RG4NaEmBNqoC3z4udIMXeQWilShwJVEvwiatlbWwoXGlly26yh6B9w_uINzv9kQ-eldbXAYDVM-mCTwGUxd9OKxt0EgbIm4WQa42lqLzD9LEMdpbYjSlddR5z-1k8q0qZA75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلاق‌ بی‌برقی، بر پیکر خسته‌ از جنگ فولاد خوزستان
🔹
در روزهایی که هنوز گرد و غبار جنگ چهل‌ روزه دشمن از شانه‌های صنعت این سرزمین فرو ننشسته، برخی واحدهای بزرگ و حیاتی، مانند فولاد خوزستان، همچنان با زخم‌های باز و عمیق ایستاده‌اند؛ زخم‌هایی که نه از جنس آمار و گزارش، بلکه از جنس دیوارهای ترک‌خورده، خطوط آسیب‌دیده، تجهیزات ازکارافتاده و امیدهایی است که برای بازگشت به مدار، به نفسِ برق نیاز دارند.
🔹
اینجا سخن از تولید نیست؛ سخن از بازسازی است، از احیای آنچه آسیب دیده، از برپا کردن دوباره‌ی چراغ‌هایی که خاموشیِ تحمیلی، خاموش‌ترشان کرده است، اما در کمال تأسف، درست در همین لحظه‌ای که این صنایع باید بیش از هر زمان دیگر مورد حمایت قرار گیرند، زیر فشار محدودیت‌های شدید برق و بی‌برقی قرار گرفته‌اند؛ گویی بر پیکر زخمی، بار دیگر تیغ گذاشته می‌شود.
🔹
ادامه گزارش
👇
https://www.khabarfoori.com/fa/tiny/news-3229687</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670088" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRbnXGnN4W49Hf7q_WsfAvlssArA6ELVQmNRxKQyy1y3lAriUV4Df_UmOj_ORKMQoNZcsG8pconwSDFRM4D7trGnrYy533-4caOcRHGZz-NDYzcuOf5TcKAbCM_dhRr96kLnL1oGpqieVp8wqnuy1KIz8eRz359aJrRSgs-uhjtSvP0D6JtdfPJH5TN_nXioQ58fA7oakPHsUTdtRezE_Obbz4kQmEuaDIA06jpLlp3WeWsMGQFc1B4GrRCE5dmgP08MegmRjMzvFvjF92Qptp-nSdvQ9RzzZ4nLqhNUY9mr-9hbIb7dyazLi_e6dBOD0qj-gQ4vGWybWkeXHBJ1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نزاع کرکس با شغال بر سر لاشه
🔹
عکس از فریبرز حیدری
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/670087" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fVX4wTOi1G2CfwESDyg5Iv86VGE85adsJKm-13RpLFTYGbGsGBP04aZKeCHHuRtgWeB1jmUyGjyuhZhif9-KnAYvLgfGzkZxhsAc6SrrkV0u5uG_qJaqo4OlR9J0Y5cxBp6up_GU-mYWwi-QqB3dBLWlMzgH460jYz2gQv51i9Ld96kJUOqRGTuITcsCbPA4Npx_rW9ge9XHJgub_Gw30F9MYHiZZuwOtQT2I7TOvygxi4LQytaro0QJZoc_48URUBD-vEGZS_XbLYomKUqFYhWauK7MLZYnvTLHicHfkYTWD8qJfM4C6No4L1lgkbcS3UTRgc4wUqVwZ4c6mL5E-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOuZoAoE4LtL6rUPKqHspM2DSn5Spg4zV0DUuVLiaA8BVNEi4gl1gTdfNrmob2IAYllIr1OBDdVKaoGY_Gpvh78yrvbyo2_Dlp211P_02B-hXtSDC30EGj56ObV4TRxEftSGMoQNad8mvGfjx7EH9cI5_U7oKghBIi20hiwEHdiQp4hn6DOzhyzWIx_jZxtxMXAOjjgIY_njhs6kD0ytNHUrN_lHjSF1sydLfWk5-X5CXRHg1E5dqdr8gLdZPPD_HsgT_6RQCfImCiCylQrEXfjD3XDDouCIs__skyYZphE2vD9QlO6pO1qVZ7QtBvY9GQdvXnT93HHMfNy9b7-a4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فیفا شروع کرده به فروش چمن‌های جام جهانی ۲۰۲۶ با قیمت ۴۵۰ دلار
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/670085" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پروازهای فرودگاه بوشهر پس از ۱۳۳ روز دوباره برقرار شدند.
🔹
ثبت‌نام حج ۱۴۰۶ آغاز شد.
🔹
۴ روز عزای عمومی در قطر در پی درگذشت امیر سابق این کشور اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/670084" target="_blank">📅 12:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بانکی‌پور: تجمعات شبانه تنها با فرمان رهبر انقلاب می‌تواند متوقف شود
امیرحسین بانکی‌‌پور، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تشییع رهبرشهید از نظر کمیت در تاریخ بی‌نظیر بود و دیدیم چگونه کشوری که ۸ سال با ما در جنگ بود، مردمش عاشقانه در تشییع رهبر شهید شرکت و‌ برای ایشان عزاداری کردند.
🔹
همچنین در تشییع گروه‌های داخلی مختلفی را دیدیدم که مسیر فرهنگی آن‌ها از آن‌چه که رهبری اشاره می‌کردند، متفاوت بود؛ هرچند که رهبر شهید بارها فرمودند آن‌ها هم دختران ما هستند و اگر بدانند دشمن پشت این قضایای بی‌حجابی چه برنامه‌ای ریخته، آن‌ها هم برمی‌گردند.
🔹
تجمعات شبانه در ابتدا به صورت خودجوش و بدون هیچ‌نوع سازماندهی ‌‌و دعوتی از سحر شهادت اقا شروع شد، اما ادامه آن با خواست رهبر انقلاب، بعد از مطرح شدن موضوعات آتش‌بس و مذاکرات صورت گرفت.
🔹
بنابراین تنها با فرمان رهبر تجمعات شبانه می‌تواند متوقف شود و مقام‌های مسئول نمی‌تواند نظری دهند، تا زمانی که رهبر به مردم نگفتند که دیگر ضرورتی ندارد و به خانه‌هایتان برگردید، حضور شبانه لازم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/670083" target="_blank">📅 12:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏆
آرژانتین در مسیر تاریخ‌سازی، سوئیس را به خانه فرستاد و حریف انگلیس در نیمه‌نهایی شد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/670082" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-text">پیش‌بینی وضعیت طلا، دلار و سهام
🟢
00:34 آخرین وضعیت تورم
🟢
03:03 سناریو اول پیش‌روی اقتصاد (تنش زدایی محدود)
🟢
04:21 سناریو دوم پیش‌روی اقتصاد (تقابل مدیریت شده)
🟢
06:07 سناریو سوم پیش‌روی اقتصاد (تشدید درگیری)
🟢
07:02 پیش‌بینی وضعیت بازار سهام
🟢
08:32 پیش‌بینی وضعیت دلار
🟢
09:52 پیش‌بینی وضعیت طلا
🟢
11:59 بهترین راهکار سرمایه‌گذاری
🔵
سیاوش غفاری؛ مدیر تحلیل اقتصاد کلان
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/670081" target="_blank">📅 12:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
توقیف اموال ۱۰۰ میلیارد تومانی در پرونده کلاهبرداری طلا در گلستان
دادستانی گلستان:
🔹
در پی شکایت ۱۲۰ نفر از مردم گرگان از کلاهبرداری و خالی‌فروشی طلا، اموال و سه ملک متهمان به ارزش ۱۰۰ میلیارد تومان توقیف شد. مطالبات شاکیان شامل ۱۱.۵ کیلوگرم طلای آب‌شده و تعدادی سکه است.
🔹
این پرونده با اتهامات «اخلال در نظام اقتصادی» و «خیانت در امانت» به دادگاه‌های انقلاب و کیفری ارسال شده است.
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/670080" target="_blank">📅 12:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvh-jfBR8tXMZa5ooYKzGZU6tcJROg8m1WIUFN6mmUwB6hJrPonRAsuUC9Xbf9Ooq-GbzxRIj34OVOTqMMQbz5aixT9UVYmB0akkgUOCDlGnFXjqNNopPb0aUZB2j0LexIW_GTlrIUDeGzJUOq15QRCrJsZAVcIU5MPZwNjOXrAFakcoqOvuwRWOEcyLTK55s3skuS5oPL57S6CBp9VKeoHP_8Gw5blj-DIxXx60uh5qoZP1S4I8V8mcmzN-3osfjP_7uzFeKIwwVGv16qMzd-jqv-1xOTTP7_moVm-XCNPfbSVxdw0iXvHBJAP6wbuVpTVY_8-Apa8HG57ExO0SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسلیت رضا پهلوی در پی بدرک واصل شدن لیندسی گراهام
🔹
بازمانده خاندان پهلوی با انتشار پیامی از درگذشت سناتور لیندسی گراهام ابراز اندوه کرد و او را حامی مردم ایران در مبارزه با استبداد خواند.
🔹
وی با اشاره به حمایت‌های گراهام از آنچه «انقلاب شیر و خورشید» نامید، اعلام کرد که مواضع این سناتور جمهوری‌خواه سبب محبوبیت وی نزد برخی ایرانیان شده بود.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/670079" target="_blank">📅 12:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzzBzh9kU96sP5W87-_XcDc6RS11yPPVcpT8chvZq5iwUcpUeO-9KLczvGs0ekY8qGMk-6Rqyz7okOjrLXz8lnynNzxYwOuccDaZoDzmkGYaRf0JpgB7BCSVG79HRVwnU2CD0Zw1oQp4c972WvcaTDUUF6dkVnKtx2BVB7_G7HcLsBZk7KDmvfpkGJUOs1eoGpThUjwlOBAMX8wN_8ZjoE4vcOVzqrRipzqSlyEIL1j5RslsDsZvGqHrNzfStRc392FaAi55J2WHVBFqjlJ86AyuPduUgiQ__KClXNR_QUzURsTQAX4beQAwIh45AMcOeoYWX9WZnIO8UHGc3SFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۹۰ درصدی تردد دریایی در تنگه هرمز
🔹
اعلام مسدودیت مجدد تنگه هرمز از سوی ایران، ترافیک تجاری در این مسیر را با سقوط شدید به حدود ۱۰ درصد میانگین عادی رساند؛ به‌طوری‌که در ۲۴ ساعت گذشته تنها ۱۱ فروند شناور تجاری از این آبراه عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670078" target="_blank">📅 11:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670077">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پاداش واشنگتن به امارات برای همکاری در جنگ علیه ایران
🔹
وزارت بازرگانی آمریکا با ارتقای جایگاه امارات، محدودیت‌های صادرات تجهیزات نظامی، فناوری‌های پیشرفته و صنایع فضایی به این کشور را کاهش داد.
🔹
واشنگتن این تصمیم را قدردانی از همکاری‌های ابوظبی، از جمله در جنگ علیه ایران، عنوان کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670077" target="_blank">📅 11:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTJwajUtECOTMmxPCO1_DLwkcsTnaNs9sIrLfqc5WvaltfYLqeaViwpoeHDcIeJW1LQ_RpgFkltLPhG2kRhiBHb3sAFn6Dw-cMEHs1X269e6OjLhVqM9ULLEZV8m1NHVJ7UFzApwkRUi9a0vPb0PpDGtIUkFEkOgoz1L2Dra84F4jY6NoeMUzn0Khawx8dq-vvACl6R1rf6ERihej2NgS9mwiZYuxZNu5WtdZnSe60Rq8MTZZYqO9O6GGT8P3jUkahodc6IGOXw2elRZ_5lZzzSGeC1xHCmB1KD4wHpiUxJH_BLzOcXYmbxV8cAC5-bmC_QjeEbRF3j_Hx8f2Es-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
لیندسی گراهام، سناتوری که سال‌ها از تشدید فشار، حمله نظامی به ایران و حمایت بی‌قیدوشرط از اسرائیل دفاع می‌کرد، مُرد!
‎
#تقاص_خواهید_داد
‎
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/670076" target="_blank">📅 11:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a901796a8f.mp4?token=YJpSSTTXbQzINHr6tpcz8Den5Az_1yQF7ajyO98S0DsD19nkIT_Z3CHN5a5CzeYWPX4ehmRNy__MgAhBBRAyyLhlC7wWogq6aoDKa6cS3-3bFuSzp3Mymq4p9HQK47KwJl8AVNiLBO9Ff71CmmJ-quXMSdxLApcwHgQlNECEM9_icl9dchHDbTJ6qBnywyDi-l3ciiuMGQNEsANKPhB7u4599qvz9rc8gXqqdsSN5YX-rTdEUExXNKIlA7jwB8ywu1p8sjEwOPig5ppOGZjq-PPWnTGm5SklQhJGrGx2caxWwTV4nCWLircBHAdGJn_J5wzomzAqVMQjkooZNXKI4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a901796a8f.mp4?token=YJpSSTTXbQzINHr6tpcz8Den5Az_1yQF7ajyO98S0DsD19nkIT_Z3CHN5a5CzeYWPX4ehmRNy__MgAhBBRAyyLhlC7wWogq6aoDKa6cS3-3bFuSzp3Mymq4p9HQK47KwJl8AVNiLBO9Ff71CmmJ-quXMSdxLApcwHgQlNECEM9_icl9dchHDbTJ6qBnywyDi-l3ciiuMGQNEsANKPhB7u4599qvz9rc8gXqqdsSN5YX-rTdEUExXNKIlA7jwB8ywu1p8sjEwOPig5ppOGZjq-PPWnTGm5SklQhJGrGx2caxWwTV4nCWLircBHAdGJn_J5wzomzAqVMQjkooZNXKI4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع ابرطوفان باوی در سواحل شرقی چین
🔹
ابرطوفان باوی دیشب دو بار به سواحل شرقی چین برخورد کرد و به سمت شمال حرکت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670073" target="_blank">📅 11:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وحشت در مرکز اسرائیل؛ عملیات در رعنانا
🔹
انفجار و مشاهده دود غلیظ در شهر «رعنانا» باعث وحشت در مرکز اسرائیل شد؛ارتش اسرائیل این حادثه را یک «اقدام خرابکارانه» اعلام و فرد مظنون را دستگیر کرد.
🔹
در این حادثه یک نفر کشته و ۱۷ نفر مجروح شده‌اند که وضعیت دو نفر از آن‌ها وخیم گزارش شده است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/670072" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803170b955.mp4?token=Nr8xRMiXa6LT9Ky7dJeVKvYHDhlN0eKW4pVRGshcd8SntV4LI9NlyFsXwvBJl6mGRYY5x4akzLzHBm9a2vGbMaJNPBVsm4OSyKppgEoM4cnPdU8eK3d3ld6XySs38iSOXuTJ-WI6cRi92nYBnJwJgpAuwtEKPkxLt9WLpYA2wYRv4V3KSusz1AvkwkvbJPoAB_cdFEjIojmSqTUtHdlgRDXMo7M9Z7aNqYfi4EwcjDMTevyy99N6XRDSoWv1jEFHXt-HykEAFb-2JUBl8a4-PYWoxLgp0kxMDj1izOkeVxF5QxPaGMW3uF0pWdTqF1a_cqKTSgX-XMaQoukV4vfXCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803170b955.mp4?token=Nr8xRMiXa6LT9Ky7dJeVKvYHDhlN0eKW4pVRGshcd8SntV4LI9NlyFsXwvBJl6mGRYY5x4akzLzHBm9a2vGbMaJNPBVsm4OSyKppgEoM4cnPdU8eK3d3ld6XySs38iSOXuTJ-WI6cRi92nYBnJwJgpAuwtEKPkxLt9WLpYA2wYRv4V3KSusz1AvkwkvbJPoAB_cdFEjIojmSqTUtHdlgRDXMo7M9Z7aNqYfi4EwcjDMTevyy99N6XRDSoWv1jEFHXt-HykEAFb-2JUBl8a4-PYWoxLgp0kxMDj1izOkeVxF5QxPaGMW3uF0pWdTqF1a_cqKTSgX-XMaQoukV4vfXCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش گراهام نسبت به تهدیدات یک هفته قبل از بدرک واصل شدنش: حداقل یک عکس خوب از من استفاده می‌کردید #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/670071" target="_blank">📅 11:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نجات ۱۰ تبعه هندی در حادثه کشتی کانتینری GFS Galaxy
وزارت خارجه هند:
🔹
در جریان حمله به کشتی کانتینری «جیافاس گلکسی» (GFS Galaxy)، از میان ۱۱ تبعه هندی حاضر در کشتی، ۱۰ نفر نجات یافته‌اند و یک نفر همچنان مفقود است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/670070" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPhrchTgm2br2S0GLqVLMzK69QdgcMe95dEFA8pFITw-5R5YtdyOA2WQg9qGo73HeoR1Lfovzj3S_KFLwMfvIRNzxwoBJ3vTFkSbgAfJhyU2ArtbOf1_gzyue2G8R_K17xwYlKUMfhJ53Rg1MS5G1cVC4yXicJWTF7cMlM7-AzdiwZyhDNihTQe_-XlZHsh-m-l-_Dj7ODftr0IUIKyx2Z47spRmRPW33P45MHP8YgxPN8y7PcTYQax3IYB3YiwOcUM9MDlpekzbPt7pFl4zb55EtXc0REkD0owSSihkuoiZdMrpSthD-gqVR6ItkZV8nCcmST4detFmZTcFK0tjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مجری شبکه خبر به خبر مرگ لیندسی گراهام: این خبر آن‌قدر شیرین است که دو بار آن را می‌خوانم #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670069" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbf218e97.mp4?token=fGqr9uc0P1Ja-cdc9dPv0OxkxRsRMFenkbgbG0R8kFwbOtLh2BVDD1ZyTmiKlAVx18RoDQfOExHcEvWiVV7aNHH1BhnQA1x7_oOvFZHevGvJiOv8dwaemZMJylWE3vKPM6jU1O0OkK-PK0qvWppchNt1eS8O5V07l-wPnQdl1g236RzXoZBvQeOuEReEEl5BKHlPDN3JvxahbkATZBRKcDhnYTDMaon-q2jXiud9FlZArO_EbnPSLSc7jj7rH12iLuW5osuF4h-5TdgU1pGISfcwibd2yYmBv5nExqTXk9sV_ualVxsBFiaqqqsE3fYEcHyilXWgwizplvJc9UeskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbf218e97.mp4?token=fGqr9uc0P1Ja-cdc9dPv0OxkxRsRMFenkbgbG0R8kFwbOtLh2BVDD1ZyTmiKlAVx18RoDQfOExHcEvWiVV7aNHH1BhnQA1x7_oOvFZHevGvJiOv8dwaemZMJylWE3vKPM6jU1O0OkK-PK0qvWppchNt1eS8O5V07l-wPnQdl1g236RzXoZBvQeOuEReEEl5BKHlPDN3JvxahbkATZBRKcDhnYTDMaon-q2jXiud9FlZArO_EbnPSLSc7jj7rH12iLuW5osuF4h-5TdgU1pGISfcwibd2yYmBv5nExqTXk9sV_ualVxsBFiaqqqsE3fYEcHyilXWgwizplvJc9UeskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مجری شبکه خبر به خبر مرگ لیندسی گراهام: این خبر آن‌قدر شیرین است که دو بار آن را می‌خوانم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670068" target="_blank">📅 11:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8836a59f28.mp4?token=N7tHM9QiTctc8ldjayA6D9XJJoPwkSuxs8VL0iXdLkPYcYM11oi4fsmdSDKncK8wrAnAzbuK26qsCZx7_IiCEJBtBdLF6A5gzMxZ2GU2xT_OEbhyIqTpeg52KOncWXOJ2Bhw9KyELDPrGOAbbo-49mJ--JkhBn7E1OekLu3DkeyYo-L4nGGVAsm4t9yb_IQStK1vulLeTbgGMqBa-SnZZC4VvG5WeDSagnkg0gEBYcOwl2B32gXC9rWDujQ2TEiBuU-rUkl7Rk8YiwE-jzSoHAWnH_Zn0mnjk1X_hwhE224Tdws5bzUJHsunvD1E8yyh5H48PinSplSp3IkFBySKkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8836a59f28.mp4?token=N7tHM9QiTctc8ldjayA6D9XJJoPwkSuxs8VL0iXdLkPYcYM11oi4fsmdSDKncK8wrAnAzbuK26qsCZx7_IiCEJBtBdLF6A5gzMxZ2GU2xT_OEbhyIqTpeg52KOncWXOJ2Bhw9KyELDPrGOAbbo-49mJ--JkhBn7E1OekLu3DkeyYo-L4nGGVAsm4t9yb_IQStK1vulLeTbgGMqBa-SnZZC4VvG5WeDSagnkg0gEBYcOwl2B32gXC9rWDujQ2TEiBuU-rUkl7Rk8YiwE-jzSoHAWnH_Zn0mnjk1X_hwhE224Tdws5bzUJHsunvD1E8yyh5H48PinSplSp3IkFBySKkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از بندرعباس تا بوشهر
از خوزستان تا هرمزگان و چابهار
دل‌هایمان کنار مردم جنوب است
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670067" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
نه کین، نه هالند/ بلینگام پاروی وایکینگ‌ها را شکست و انگلیس را به نیمه‌نهایی رساند
🏴
2️⃣
🏆
1️⃣
🇳🇴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/670066" target="_blank">📅 11:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_MyD3frxZWCEBuUcxdnsA_NN9AbFvKBKcdrojJn-r2JJ8-uHVRRjQ7icurkANvjrY60DTZCf-SAixC3NWC6qfzSD88akygnC_a6l_32HItvuaBvSOcCFSZp9J4opdzzEN43dn4dPaNG4LnnILF6Y6DPnJAkLdO0FzvYAn6Fx7X897QBSBFt4mNkP8Rk8BKjOfFEKietzqz38huwS1wEG9ptBUkUkjzYSKvExxdauyZvMGtImHcFvruLk1RmjEFxY3heztjWfvINGKwPR4QyCwVMbo2R5xNxTXjZ2ltTYi_XWPDeo6zanCI6JnzwtegSzCL3-0dXZbuG8OstNnQ54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش نتانیاهو کودک‌کش به بدرک واصل شدن لیندسی گراهام  نخست‌وزیر رژیم صهیونسیتی:
🔹
در دیدار آخرمان گفته بودم که «ما هیچ دوستی بهتر از لیندسی نداریم». اسرائیل یکی از بزرگترین دوستانش را از دست داده و من یک دوست عزیز را از دست داده‌ام. #خونخواهی #تقاص_خواهید_داد …</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670065" target="_blank">📅 11:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: عکس رهبر شهید باید روی اسکناس‌ها چاپ شود
اسماعیل سیاوشی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تا زمانی که رهبر شهید زنده بودند، اجازه ندادند عکس ایشان بر روی اسکناس‌ها چاپ شود، اما الان با توجه به این‌ که شهید شدند و خون‌‌ایشان قیام مردمی ایجاد کرد، لازم است چاپ عکس ایشان بر روی اسکناس صورت بگیرد.
🔹
تصمیم نهایی این اتفاق به دست رهبری، سران‌ سه‌ قوه، شورای عالی انقلاب و سایر ارگان و سازمان‌های مربوطه است.
🔹
همچنین در کتاب‌های درسی، شهادت رهبری و مباحث ارزشمند آن آورده می‌شود، اما در خصوص این که در کتب امسال بیاورند، نمی‌دانیم که به سال تحصیلی جدید می‌رسد یا نه و باید برسی‌هایی صورت گیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670064" target="_blank">📅 11:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670063">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سازمان تامین اجتماعی: ماهانه ۱۴۰ همت بابت حقوق بازنشستگان پرداخت می‌شود
🔹
استانداری آذربایجان‌شرقی: احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز تا ساعت ۱۲ امروز وجود دارد
🔹
دولت عراق: هیچ پایگاه خارجی در عراق وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670063" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670062">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKZpOI2vyIcvwrdeWXzCGHQNzkvvpeTWN7LuJr0QVEsqM_2dONJhUIRxxdtBQm3Me5G6cNSEoHTP0BkdXU8sP-MF_jUCrJG5I4t4uQADjSX-qBQssQjT39D23pV25-4lqx_JEMCNSEafPcK0zgdZ-tsTGQsyVXAaEiD-v8I6oDJ0VJHXyZJsj-oAKxGh1yqB8UsC_ExPOY3i2oUbfyn5xsX4yXdMs6h2FyRoK-g3CNXwuD9axKVM7MdF5viTD_9CLM-9_LUOpnYiSt6nC4EGW53rbs7Bvi9ljgCLRbCH4klkqcMCCIZe4UHyDyFewoRWbUYPqvfOlfved8QR01yafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وکیل و روزنامه‌نگار کانادایی به مرگ ناگهانی لیندسی گراهام: دنیا از همین لحظه جای بهتری شده است #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/670062" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKkOBwB9x-swI_xfTBjS2gowkhMWSRClFlmst-Xfi1CJoaDZqHVv66OltsyPIOUro63iSc-Q64fHK2McFTYiLTTem4n4_ygv3fvUb_waZSHFJLLJK6ohOYpASbCPze5judNBgYm6VUUs3boSW6eKbsXrd4F0wDPT0J1kQMiIgBn2x6s8a-q-Ssm3SM1bOlqquTcXzstT_wTt3I4VXke91vwdsHLUe9nO5hheG1AC3LnN0UrBKIlzVfJUUC1Vssdwyit239Snp_JYts8MLviY5Dbb7OdMXxlypYOTSJz4P4q1RFYjuttxPu0ySCANrxGNZubgrc8c1R3iNRECYTPbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد در سوگ گراهام: سناتور لیندسی گراهام، یکی از بزرگترین افرادی و سناتورهایی که در زندگی‌ام می‌شناختم، فوت کرده است! او همیشه در تلاش بود و یک وطن‌پرست واقعی آمریکایی بود. لیندسی بسیار مورد احترام بود و فقدان او بسیار احساس خواهد شد! جزئیات و اطلاعات…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/670061" target="_blank">📅 11:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حمله به پایگاه امریکا در عمان  روابط عمومی سپاه:
🔹
مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیما بر آمریکایی در بندر دُقم عمان با یک حمله سنگین و غافلگیرانه در هم کوبیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/670060" target="_blank">📅 11:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ab7e11a0.mp4?token=MnIgSiwpanX1h8S4lxSvM78BVKJGwyMls9ffHNYAYTino9eo4ljyQTOnGIkb5P8lBaSJqzVpiMwguqtVu_MZ4AI4acbaX6R0DAJrfmSdnqv-VfCnUhY4XRLxU-KF4pVJCDUQcneHvtKtaNwJbSaFF9DJ5zTTYX-ysP9SUp0a_DxGzjer6eaZh_9nUfARMGJdCm8B0KQywF7jWca2MF2j2amCkpQ7kqJzUYXCYAQwAJGC1oiIe7tliSxS8OkT9LCeWMCoq5qNJ77GMAZ2UxbWguF_7UOI3o7ToWVct6W3LACyV-wZF8xgiL8v2EuhT6h0SeKXY-9KWLVDriC6e6heARiKkXBKow8Pj3AUvj_5wn1L7WOkGTwI8ugOoIVjA7R6pXd3J_psqeqrf96g736Des0CJXGTuFcdWYF6370MTiqO2EPGRhMVJUcS_GMEYwMbM74ceYKaUYvQIokpDnWMt84ahf9CXwlsiLqfb-MtaKHNjYa3IifBOfWRJlwxAAnhF0RylonurRYJuJzkCCSpPblsSxcRe1gzFvTq9iJzRH20kctt_sTuFteRgCDlCkZTusv8gtJmhQHUwo2mQ-liw8lBy-nqnQuYXdZwu-UjkbAQgLAqOcrPobdjUsqxCPK8CWp0d0Qwv-SI5G7THSIjZgNZPUWDIG7YfaNS3tAAyXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ab7e11a0.mp4?token=MnIgSiwpanX1h8S4lxSvM78BVKJGwyMls9ffHNYAYTino9eo4ljyQTOnGIkb5P8lBaSJqzVpiMwguqtVu_MZ4AI4acbaX6R0DAJrfmSdnqv-VfCnUhY4XRLxU-KF4pVJCDUQcneHvtKtaNwJbSaFF9DJ5zTTYX-ysP9SUp0a_DxGzjer6eaZh_9nUfARMGJdCm8B0KQywF7jWca2MF2j2amCkpQ7kqJzUYXCYAQwAJGC1oiIe7tliSxS8OkT9LCeWMCoq5qNJ77GMAZ2UxbWguF_7UOI3o7ToWVct6W3LACyV-wZF8xgiL8v2EuhT6h0SeKXY-9KWLVDriC6e6heARiKkXBKow8Pj3AUvj_5wn1L7WOkGTwI8ugOoIVjA7R6pXd3J_psqeqrf96g736Des0CJXGTuFcdWYF6370MTiqO2EPGRhMVJUcS_GMEYwMbM74ceYKaUYvQIokpDnWMt84ahf9CXwlsiLqfb-MtaKHNjYa3IifBOfWRJlwxAAnhF0RylonurRYJuJzkCCSpPblsSxcRe1gzFvTq9iJzRH20kctt_sTuFteRgCDlCkZTusv8gtJmhQHUwo2mQ-liw8lBy-nqnQuYXdZwu-UjkbAQgLAqOcrPobdjUsqxCPK8CWp0d0Qwv-SI5G7THSIjZgNZPUWDIG7YfaNS3tAAyXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهره سلطانی: از مجلس نامه زدند که این زن سلبریتی سگ باز را از جلوی دوربین کنار بکشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/670059" target="_blank">📅 11:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAYZC8AzHXdrHBXl0eMhg3NEZzxA-iy800Osc08EMkA8lhGvsabYORL7EKqc1ArwO91gnaWyTGjx2687Jopgxrej00AZYOr-JW_XhSzPKRjUp94aNFmLu1RTUW-sFdfGYlWjxi7IusvCZugUQ1z2QUCotOMKoLO01omYQGLOqaAHjlfA5hfoPoPwQZegKhHfNACyIICJHs7iXd7Q73cSBiu-seFrR3FOWO4AFnFR9_wPhCuedT9JNfOC3UVXW4iTdIsIA2srdaRN-hMd3pM3VdVoaY-1vvSZxDTmSLUelrNqTx7xi5S8g9y1bTPz-iAW9AkBl5yIU4UdMzI1-nJmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگاهی به کارنامه و مواضع سناتور کودک‌کش
🔹
لیندسی گراهام، سناتور ۷۱ ساله جمهوری‌خواه که به‌تازگی درگذشت، از سال ۲۰۰۳ در مجلس سنا حضور داشت؛ او از حامیان اصلی حمله نظامی به ایران و مخالف سرسخت جمهوری اسلامی بود که در نشست مونیخ از اقدام نظامی علیه ایران حمایت…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670058" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670057" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
برخی رسانه‌ها از شنیده شدن صدای انفجار در کویت و بحرین خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/670056" target="_blank">📅 10:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=rBhnOX-01fw5CUu4Of9HIg0VHrXrVLrVP09WYloZ52cVv31RX9YcerfYGJ8tkzI8H2c8gJIir36XN-Di61T9BxEK2nv_UWJ4JJm7KDwxK3cU-ViJBdNTHy1KpewJGf-9_OlJI1rBIqXp_pBvXxeuMsWel6llKKc5Dt2QzVR8hfXa7kW9oGqPeJ2DSwTwthQ1bgVA5maNurlnmPgVZoc2ScZkQCD5HmW8XViRm_8dkC2LKx8acTfcEp8IFgCjuZSUIm1vLOIprBLA8pwRb4IOvL2xZQRWqpIwMNfUglRRkAP9dkvhWCw-D6JY6W6kUN_O-WPMMybeeOVapALvYR8hwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=rBhnOX-01fw5CUu4Of9HIg0VHrXrVLrVP09WYloZ52cVv31RX9YcerfYGJ8tkzI8H2c8gJIir36XN-Di61T9BxEK2nv_UWJ4JJm7KDwxK3cU-ViJBdNTHy1KpewJGf-9_OlJI1rBIqXp_pBvXxeuMsWel6llKKc5Dt2QzVR8hfXa7kW9oGqPeJ2DSwTwthQ1bgVA5maNurlnmPgVZoc2ScZkQCD5HmW8XViRm_8dkC2LKx8acTfcEp8IFgCjuZSUIm1vLOIprBLA8pwRb4IOvL2xZQRWqpIwMNfUglRRkAP9dkvhWCw-D6JY6W6kUN_O-WPMMybeeOVapALvYR8hwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات امروز سپاه در پاسخ به تجاوز ارتش تروریستی آمریکا
🔹
در این حملات از موشک‌های بالستیک، سوخت جامد و مایع و نقطه‌زن قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/670055" target="_blank">📅 10:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/670054" target="_blank">📅 10:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بن‌گویر، وزیر تندروی صهیونیست: اسرائیل یکی از بزرگترین دوستانش را از دست داد #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670053" target="_blank">📅 10:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d40a15b.mp4?token=HgtwBVLV5ZF_Ci5_-kEV4_4UO2TRUa2RbPLm7UpyYnMjta7MjPZ8dRcoYiGqel9RWfRWVXDq_8mn6_M1R4Ql8j6nxGaw8LM-ZA3oWKCJGLWhOhHauEo2fezZLMyjk0Pr7-kwIvaMCfkQ6ZBDZMl_PmrmHngTkVveE0BShTdcuSwlApcedWt7b4hz8UbxGHMEBENZ4DPDaa6LQDHzJZ4soeIItpw_z_Rfo29RkXaeAV2TjJxIgNWxD8G7kIdrf9mGC7-aYu1qXnsS2J-H8GXZOGfcDA20VlDchIn6QN-lHOO_hd8RdTVEtWrXYXcDrEifRGqSBFgpUaVoTv--36QP-q_N1gxmofPp2Uc6zg9n2-leejqntzhd4m6-xuCVhsDAk_sl7QDICIOOrlxW472dqEgMZCd3ROH0q_1ey2KFm-28wFxlqFS4gW2hGYnlcy1NMVXYhe0TFig6QzLKZYY8OqNiw80fOXyYfryyyhVqch7X3fTgrKVfiDc7swCy7K8KabPZmAT_9xZLVpz-BCwzLDizx2TKSWiIqC0vrIMLM43D0i796v3dVkWKCUhCzbzSTYjBolL6V8IGnKr8D_CGuHPgXSE-UOw0IVme729HIYXrVwCGrV8WDW1kto6TsuRaKH4oOT4f8hI9aG-hYRPDhyCGneAjSoElFc5Lv_QU50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d40a15b.mp4?token=HgtwBVLV5ZF_Ci5_-kEV4_4UO2TRUa2RbPLm7UpyYnMjta7MjPZ8dRcoYiGqel9RWfRWVXDq_8mn6_M1R4Ql8j6nxGaw8LM-ZA3oWKCJGLWhOhHauEo2fezZLMyjk0Pr7-kwIvaMCfkQ6ZBDZMl_PmrmHngTkVveE0BShTdcuSwlApcedWt7b4hz8UbxGHMEBENZ4DPDaa6LQDHzJZ4soeIItpw_z_Rfo29RkXaeAV2TjJxIgNWxD8G7kIdrf9mGC7-aYu1qXnsS2J-H8GXZOGfcDA20VlDchIn6QN-lHOO_hd8RdTVEtWrXYXcDrEifRGqSBFgpUaVoTv--36QP-q_N1gxmofPp2Uc6zg9n2-leejqntzhd4m6-xuCVhsDAk_sl7QDICIOOrlxW472dqEgMZCd3ROH0q_1ey2KFm-28wFxlqFS4gW2hGYnlcy1NMVXYhe0TFig6QzLKZYY8OqNiw80fOXyYfryyyhVqch7X3fTgrKVfiDc7swCy7K8KabPZmAT_9xZLVpz-BCwzLDizx2TKSWiIqC0vrIMLM43D0i796v3dVkWKCUhCzbzSTYjBolL6V8IGnKr8D_CGuHPgXSE-UOw0IVme729HIYXrVwCGrV8WDW1kto6TsuRaKH4oOT4f8hI9aG-hYRPDhyCGneAjSoElFc5Lv_QU50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ‌های کوبنده تحلیلگر وطن‌پرست ایرانی به پرسش‌های مغرضانه مجری بی‌بی‌سی در حمایت از آمریکا و اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/670052" target="_blank">📅 10:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jehESRBCfP6XvvNST_2Wl9tw4bpUEtztvkDXnA3eGrCukRmz3JCG7z0qTOeTkJBrK2-RqzJDUCsnNk65qfMSM6hM_lP7gmOOcpbgVlc2gXwSZ1NSqJINo-OAuN97MILklxcfAYlrNjy0u7grcNqPWCZR9M4Rdmvd-YT44xYCFtJAROEzG_Kg-3xGpjejpMAZ-Pa9Elzj1F0_0SCKl7cdNZQuDXN_wgleLMMMI4LSYuVF49B0Dtn6XTRVPIrWhDFSQCyxYRHASu3F0rNMK0DTwwScgNwR2-kYSYROX9SU6zn1feEXlljQa05CrhYFQyjW_V1eGy5kuXgxmRGKGxxl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای نخستین بار در تاریخ جام جهانی، مرحله نیمه‌نهایی با حضور چهار تیم برتر رنکینگ فیفا برگزار خواهد شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/670051" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj6h8bzc-FTJbwCoiS-MeJUyUTXiuktHBsql3-zwjHmUb8BllZ-Zn43Z7xqyKQoMxxgnJj_aBXZO07mgRxKGXzhBQI4MTNxd_TeWVSB8IFpPPKX8qkvDpXwc89KzmkSuQWdmmDz4qvn-uwoX-FGiB34mQ0KcUoOL2bLXFHsZZe-jIGD5Edekl_HXl4KW3Y79SejceaUrqOBfTOrjqvJrOKRkNUZwrnHnT4fL8zQH7HMGYaJvyMa7SVRtqKbFjKNOUi2d1ZY2bcL4JK_IJKJXBX59sWClTbQ73Tkvn71JuBsEo1FRtPEqY2aHrcmxIP8mO85CDY2R8cqqMr2m0nfOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفیق شفیق نتانیاهو کودک‌کش آرزوی فروپاشی ایران را داشت؛ این آرزو را به گور برد #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/670050" target="_blank">📅 10:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
در پاسخ به حمله ارتش امریکا تا کنون غیورمردان مسلح ایران به پنج کشور که پایگاه‌های آمریکا در آن حضور داشت حمله کرده‌اند
🔹
اردن: پایگاه پرنس حسین
🔹
قطر: پایگاه هوای العدید
🔹
کویت: بندر الشیوخ
🔹
بحرین: پایگاه پنجم و الجفیر
🔹
عمان: بندر الدقم (مخازن سوخت ارتش…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/670049" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHp5eyqCAHGozjy4PT_20_1PVEI5aqgbI55nuaJ5EK7lDER68cLhKsZiLzHFiTh8STdQ7eM26jtXNXTBNwfXFpAS0FRhLdg143K5TSluJL-y5mhrLnBZWp7sFL01ZX7WBZqSajm3WLqwgI0UzlLD3fsT7LNzmmLhBXCPLuMo7GFAwkwgUYgYi5YA9YnrcpQaf3gQxHfnyafIEk8V1PjcnZwBEE_8qrOR0a2Lz0CWD22Je2YY9ziQXZOF4Su9erIVxtNeTLuq8UMGymD7rpLTSzsEnciOclvAXHjx-bQkcoM0MCQ3EqVa9myh2zB51oURrks6K2Ey79txBITI6FKCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای گسترده‌ترین طرح جابجایی با ناوگان حمل و نقل مسافری عمومی در مراسم تشییع رهبر شهید انقلاب
🔹
معاون وزیر و رئیس سازمان راهداری و حمل‌و‌نقل جاده‌ای از جابجایی یک میلیون و ۱۳۰ هزار مسافر از طریق ناوگان جاده‌ای در قالب ۵۳ هزار سفر ناوگان حمل و نقل عمومی مسافری جهت شرکت در مراسم تشییع قائد شهید امت خبر داد.
🔹
به گفته رضا اکبری در بازه‌ ۱۱ تا ۱۹ تیرماه و با مشارکت ۷۹۷۰ دستگاه اتوبوس، بالاترین میزان حضور ناوگان اتوبوسی در یک رویداد ملی طی سالیان اخیر رقم خورد.
🔹
این عدد در مقایسه با اربعین سال گذشته که ۶۹۳۵ دستگاه اتوبوس برای جابجایی زائران مشارکت داشتند، ۱۵٪ رشد داشته است.
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670048" target="_blank">📅 10:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
در پاسخ به حمله ارتش امریکا تا کنون غیورمردان مسلح ایران به پنج کشور که پایگاه‌های آمریکا در آن حضور داشت حمله کرده‌اند
🔹
اردن: پایگاه پرنس حسین
🔹
قطر: پایگاه هوای العدید
🔹
کویت: بندر الشیوخ
🔹
بحرین: پایگاه پنجم و الجفیر
🔹
عمان: بندر الدقم (مخازن سوخت ارتش آمریکا)
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/670047" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
موشک‌های ایرانی از حریم هوایی بحرین به سمت اهداف آمریکایی عبور می‌کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/670046" target="_blank">📅 10:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405bfdb289.mp4?token=nmF_QAZ2bpiifos6oKZ0PEdhKvgzE9BpSiT3P2kE75FcEO5nlNArBG06yc0U8mXlQ_YXB5HB3q6kQbfaIlOMtVznqjhzZiwnh6rrFTJF8PII1eznywVuTDwDJ5yiQxaJDnVszDpIIGv7L3IdeWqikX-z-cQjXQj_eNOAWilj4Lgf7qb6X-ThsrizXL4BNWmyg22bAzVN0gvxXYq0ajt3wCED2Ebbgn28aQc6yzHW9eWSizWZrtMnEbCu0AVmzMocljFwGo_0jWyy8te0nsPQvMupBXE0wj3Nl5grAKDNnuOddFaV2QInjRVn8AvJCgJcwL6DD0mNfFjdpJlLgVqTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405bfdb289.mp4?token=nmF_QAZ2bpiifos6oKZ0PEdhKvgzE9BpSiT3P2kE75FcEO5nlNArBG06yc0U8mXlQ_YXB5HB3q6kQbfaIlOMtVznqjhzZiwnh6rrFTJF8PII1eznywVuTDwDJ5yiQxaJDnVszDpIIGv7L3IdeWqikX-z-cQjXQj_eNOAWilj4Lgf7qb6X-ThsrizXL4BNWmyg22bAzVN0gvxXYq0ajt3wCED2Ebbgn28aQc6yzHW9eWSizWZrtMnEbCu0AVmzMocljFwGo_0jWyy8te0nsPQvMupBXE0wj3Nl5grAKDNnuOddFaV2QInjRVn8AvJCgJcwL6DD0mNfFjdpJlLgVqTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این بندری آدم رو میبره به ده‌شصت
😍
مواد لازم:
🔹
آب ۱.۵ لیوان
🔹
فلفل‌قرمز دودی
🔹
سوسیس یک‌کیلو
🔹
پـیـاز متوسط ۶ عدد
🔹
رب گوجه فرنگی ۳ قاشق غذاخوری
🔹
فلفل سیاه نصف قاشق غذاخوری
🔹
پودر گوجه ۱ قاشق غذاخوری
🔹
زردچوبه ۱ قاشق غذاخوری
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/670045" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMGIzJrSHUozQsXfrBEJGs-yQeWW0jpzM7xuP1EO0eFoyFGRQZ4y5zggOHS-yjyKr83AZESc7arM1gQ34vMDI3C_wP2Tlw0OlVt8RZU2-hDNip496gDvreLXGRHsTk9Pzc7EKeOxu2PUniBokvYhEM5Taas8QaCwXfyBGC_D2s3Um3DFHn8KDWlx7prlDhecOlivb5PiNL93WziM4WvIPDWqNM0KaSpuxuG0lin3PXX4RTybpi6JmK6uPnc9Y9FBxY4AiuXUnkjFH3VeKNqdz1M2B5ctQ5YH9nVfoJAy1nMGc_b5m2UD444glOZQLa0TM_7TnAimf5kUHfgCBYY7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eENJqd3Snx7XqbjZrbJ7BVwJP8sVuN8uu1bCWNgn4nAZpuuvB1PuLzLT54QoS49Q7oOi6lh4guumX887trcv21AAPwr05sCILL942LSUnPnSXuFdBKCqeZqjiBexCo-Yk2zmiP3Z3Au7ZUxWhZlbdPzEQguWPq20a0r9k5U8LYUJJtxaNVzWlST8FUhE3jzvKLsPBWqNWpOs0YeOR__Re704hd-rWPP6-5fS_4jug62F-aS3l-nYrmet8p_o4XU5nynE5OSe4TTopuXlx8WlsUq8CQeDTXJ2RZGGfTXBZ34Zgh0hri93qTP0gxeD2o-moVcwb1Tv2xcDzFQrfZu_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfvOxMBssf7KMQFTWFExhoLNnXSIY5LNS7OITZBRlMNzSpCgu3WFn6ZawOZ4w4EqKnxr8Kb_ZrjqdXoczRhgC5YA9N8TXH0RopgY-By-J83jmqhWZjFwkSeSTdO8gyjQQgn6vqg-5a_DBzvUSZs8eRkP8XVtO00H5rapQYB-iP_F1-J6PMad9lt7PY-OipwSV7SF5lZoosYCvyWouPM0vKo2mOMh6SoKHBv7HP3ZRzHxnfhfbSYvIrEDglxUj-VrgFKU7EgiqbH6ZgTEBIQL2Gn3QYbL53BeZfMjdq2jeGldlA4AoEyJp0lZuDsFndyCxrrrunddtCA8ZyNRIgff2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkhZhMSH8qwHT83VUBQj9aQCQQqcptRQILGpw79Ak_IIE1XT9-CbmYSMCOEWEAqtv8QgUwc8lzL7H_OPpNxY4QdQ-WQVmRy5EFmo3D1ykbRZM4yyJ1yFudgyXmFw4aVInXHd6QntxZmfMoNOL4_l_JCsozY6APndi_EL2om_VoxIdyAzxeC3C8jpP8zzmlhsLHpzpihaahcfzIACRBBc9fk7WHu1l-3wOoddtkxzR3sj0oYdU36a3kTBdIHBvA-oOIpG5yNZAjHWfCbLidl9xNUIqJZaNhgoHaPYBRnqwNoYHMbRqcbms50AXr65DG3yzVHA9AQLKvSMq9_P0TD-Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری از دریاچه هامونک: جواهری در دل طبیعت_ شهرستان نیمروز
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/670041" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzgojqwQTVZBeHBalKyKn1k2WRD2C-boKRUiRe8SF708SHDVOElamcK8HAUKA7LKmtLZIZj1E1Agjo0RefEPaCc6xej4AXgwKcXpthq3motBbYRt-TkoAFksfUGSfZnIVexLGwCxoyRV9MydIqRxXKivf4qrNbOVDyg71Mv1jILqQ-hvyVNwJsMC5FroN-jc6rmup9v-M0VgemXLcByN5fTwmiNuAP7y0rjvlBvMLIARQdBT8uodJXa5WjZDIFoIlCeNBPJAmzkTsSswyZZf9psRD94c__q013-u1zXtHeQqUNS2e_YdeuZ_juvr8X3z6Jyndq8pjGa-770rtROOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670039" target="_blank">📅 10:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حمله پهپادی به عمان
🔹
دولت عمان اعلام کرد که مناطقی در استان مسندم هدف حملات پهپادی قرار گرفته‌اند/ عصرایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/670038" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seoIME35ZUse9sWmuUNlLvCBy0r-OjxeH8PfJ7bafjf33qHhN4fGR5frbn1UoXc_hC40ArTYUXPurU54LNopars0dvY_dBDqQRyE5E41lT5dpS_2ph5ffA95RaeCLqQBD9qsJbm6ILbj3DebpcL76L3wFReqJxL4ATYybio2zCids5gXIUThEA6E9C4SaCpxTD3zZ3zUzPi8NeptWDdq_03fZZkmirUXc3qty_Jf6XxHwduA1PjGKl_IDhx6nWosuOjRTDcaGSgvzXjHTj5AjBYCJEzN13bc_OmZCgyvxefEC9kGTkVBJlL1nDS1MyXsFu5UUEziBK3_Bda4tf3QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسرت بزرگ برای بودای کوچک
🔹
در فینال ۱۹۹۴، ایتالیا و برزیل در فینال به هم رسیدند. این بازی در وقت معمول با نتیجه مساوی به پایان رسید تا ضیافت پنالتی‌ها، قهرمان جهان را مشخص کند.
🔹
روبرتو باجو، ملقب به بودای کوچک با از دست دادن پنالتی‌اش، ایتالیا را از جام دور…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/670037" target="_blank">📅 09:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670036">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWsYOY5c1mwaJxE9i2PyZGoPTp4z1YBDXpPg1kqgCmjVMrT6HJrdtz0uLZ5iT-TcqlxHz9Zx5vakX0sDBZztRdOdJrP_l6MSrAw6k-056tNMizdcabqtXwODLk-ai_ehOL2U4sNGOF9QLEuG-uQFPxIKBy21qAMZJLF2YRo71-5wqjfZ7oN9Ff9UFpjG02nLQwmB-wLd59sQ3htxdgJejij82IV62iZZGaWGdHlgyPcUqiVrNqlcZ8UPgeMnaoSCRUkvJMSH1fifzy4Eylv-peF0mfXuWghu3dK__fZ9xGDm_VWFedYjMIcEaEL_SpkWtc6RW5twcl0po1ptxGMoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با قدرت گرفته‌ایم و با قدرت حفظ خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/670036" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670035">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah23B8FDr1WkDsKgOR90-2M47lxqSgEEJO3HKO7cY5-huw92_aQX0K8iiQEIvbZ8HSWtkLIUvvmo-sR1_kg24zctgck3eb5EYr6lzhNZm4015ymnQwHK-fMxMeeL0iq5317z2ixDeMWAifI686s-pxyYjJJFtfFhzciiLetkvygOyz2ah8M_8uzdwsYWTIDivI0DBjICSEzktARwm5Cf7KwQskYQHlBjjfyPLVVHsTqMcZXfEZJV1nwWiX6c95fQIMVQyblEX5_6c-DlKEQchRMGDNBjyAyNjJQ8k2_-xx9TVSrzEgsGLA-R7K54ak8CZuEIXIR1up0vLSXe8xZ3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی
!
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670035" target="_blank">📅 09:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670034">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961db740f8.mp4?token=YCgVc0cfyUNUB3jzcbzEXojdehat5CO_yiaIYDI92e8ewHX2YXlar-3cUc9ivp6OsS0d-5H-x-ptySL1oj-dmgqhMlH3tihPi_auVTnRPGShIygzbvlFlJM4IZparAGLIRhJuMaV-mm7ojoDs9IzOkkijjtkjShi-CIwGG7n5e8EQ1J5plgcXMU2jpfFB8oZkDnkd5t_otA-KS7kimAgBAcO6JRk81Z5jzNKzgNnkR6KyTcfLCN7Myj1pbXDUFFBuBZl4JIPGngUxgJRsKE1Y56DY_jIpiYYIqA6wjLrWVHanI8Bf4Q7ZekZlio7_EeAmFf3hyL45OiUNX5P5V-iRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961db740f8.mp4?token=YCgVc0cfyUNUB3jzcbzEXojdehat5CO_yiaIYDI92e8ewHX2YXlar-3cUc9ivp6OsS0d-5H-x-ptySL1oj-dmgqhMlH3tihPi_auVTnRPGShIygzbvlFlJM4IZparAGLIRhJuMaV-mm7ojoDs9IzOkkijjtkjShi-CIwGG7n5e8EQ1J5plgcXMU2jpfFB8oZkDnkd5t_otA-KS7kimAgBAcO6JRk81Z5jzNKzgNnkR6KyTcfLCN7Myj1pbXDUFFBuBZl4JIPGngUxgJRsKE1Y56DY_jIpiYYIqA6wjLrWVHanI8Bf4Q7ZekZlio7_EeAmFf3hyL45OiUNX5P5V-iRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه ناوگان پنجم در استان چهاردهم ایران (بحرین) در حال سوختن است‌‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/670034" target="_blank">📅 09:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
معاون سیاسی امنیتی استاندار کهگیلویه و بویراحمد: حمله پهپادی آمریکایی-صهیونیستی به اطراف یاسوج بامداد یکشنبه بدون تلفات جانی و با خسارت به یک خودرو همراه بود
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/670033" target="_blank">📅 09:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNKa9ed8SUlZ76PFgVZC4Jgd8nw-VoG6eirfRgEn0cUmJioLIVuDgypQAL31pYSIE2I2oL3bIcHApi38EoByxK3eXMpLJ7MfH6tkn72p4G8AcJGoRT4PtKb6lRS-bUn-l48U-4ye-dk5YJ-Pd3PpwcKuYUSDM0W5SkZUuLXUDTGJEmRKbd4VNTTLiz541l6JpPMYDobj5mjJQ_xupPgiv8phtF-tdm0NFwBpIlXE66eIj3kH85EWOjLfURWmEHCNqVPihDzZHqbghgi3hnMlY0LwgSlTT59hXkZ3i2C_trX36entlzDqkQiTyjZ3Sf_1HrFPP6PPGrMSOrjlAuUf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عقب‌نشینی ۱۲۶ هزار واحدی نماگر بازار سهام
🔹
شاخص کل بورس تهران ۱۲۶ هزار واحد افت کرد و به کف کانال ۵ میلیون واحد برگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670032" target="_blank">📅 09:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDm3OOGsWyKUweK8Fb0tWoP-LsnDhdYdxt1S0yNFI1_EwAC3COUkr3QNa9PbtSKcljI8CcYaz44HHgPLWHvvlbIXTxNmXvy7saeZky3kIolZJgdzEfmhdVpyHxoXCyMHUEY9XY259P7SQlRst3AQ_ZEWRzwi2brT6OrBhMRmTbC-31Rehwbvoyh2JGepzyYhrcYv6xQac9KeaurTk6mULTJakKoooS62cG6nw6EmqiR_hio20d1QZWfCBDQbZl40QUVO7u8kC1BfXfq8IMeXxwN2FMGV60aTNhVTYr_Yz1hYtERx2jDbbjNTYJXJYhMncHtsUgMOjAT7am2zqmIkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخشش تیم ملی المپیاد فیزیک ایران در کلمبیا
🔹
تیم ملی المپیاد فیزیک جمهوری اسلامی ایران ایران در پنجاه‌وششمین دوره المپیاد جهانی فیزیک (IPhO ۲۰۲۶) در کلمبیا موفق به کسب ۳ نشان طلا و ۲ نشان نقره شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/670030" target="_blank">📅 09:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای اکسیوس: عراقچی پیشنهاد جدید عمان را به تهران برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670029" target="_blank">📅 09:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTYTNc1qLtosNG0ysmHbV_G_vn6vLe_VwLhxfYPhTvsy1NY9s5TjPsKNFsYm9yfYIrs_3YQYhDGB69xrm-GpBaROSoOA3kAeZJaK1t8mBEnGZi_Fqwu0MNdUiF_lEnqReaqzwp-qGM3vKRW5-QaCCobCr4jflqaCtJFdXp9algLr7--yhMS7KDcAUp_KTIx6fLwDBIpmVlJHoVpBSUPFJxlh439BUh5Ikm4Tem5Z4bIj4l7awYzU_VmyDjnolxClqA_TqjxFW9W3Y4lo7-gkDyXopaHiM-J72NGN4HiMz_d4QRbWrRuhPvCgyp8xhrOEU8cE20F0tao3Lo8b3RfP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه منتظری ویلا ارزون شه تا بخری، هیچوقت صاحب ویلا نمیشی!
🏠
با فایل‌های متنوع زمین، ویلا و کلبه سوئیسی، با هر بودجه‌ای می‌تونی سرمایه‌گذاری کنی.
💰
📈
🔷
با اقساط بدون بهره
🔷
🔹
معاوضه با خودرو، دلار، طلا و…
🔹
همین حالا تماس بگیر
⬅️
خانم رونما 09126227033
وارد کانال ویلا شمال شو!
🤝
https://t.me/+np4AG_H23D4yZWM0</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/670028" target="_blank">📅 09:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه سیرجان پس از چهار ماه وقفه، مجددا فعال شد.
🔹
سخنگوی ارتش: بانک اهداف‌مان را هر لحظه به‌روز می‌کنیم
🔹
توزیع کارت آزمون کارشناسی ارشد ناپیوسته از فردا آغاز می‌شود.
🔹
آموزش و پرورش: امتحانات نهایی دانش آموزان یازدهم و دوازدهم از امروز آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/670027" target="_blank">📅 09:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
یک منطقه نظامی در خنداب هدف پرتابه‌های دشمن قرار گرفت
🔹
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی از هدف قرار گرفتن یک منطقه نظامی در شهرستان خنداب توسط پرتاب‌های دشمن در صبح امروز (یکشنبه) خبر داد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/670026" target="_blank">📅 09:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی در پاسخ به تجاوز ارتش تروریستی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670024" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54687295a.mp4?token=rHA52MWTVMnncsfXdBCGdO0iTk7sBH9UZ_ZZBwvWyoWlkYKeTLtVqXMKOqy_2yV-0dZ3deoYWovZA4DrQ4ahVuxledJH2cht7IchztQcHoxJOmO6Qe0RVX6Kv3Z8GIEDWxdic3j1NPVfqiWVVYwBOH1PywUEMVFVq1pjyaXNKQP5sQ8IIoVRE6vhatGLipC4PNP6zkKXARhG5tDXRfmsLRYAuFZuKOmPplZOsQ5skutj6PU3vNb6mWloBppg7lW1r-CMNgevwin3gND_gFOh5e-gn-uftsVUL4AFHhCSb-LfIQjRGGrzDk32_2MJ4i8S_On1lhCWEKrFqZ_vPZR6fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54687295a.mp4?token=rHA52MWTVMnncsfXdBCGdO0iTk7sBH9UZ_ZZBwvWyoWlkYKeTLtVqXMKOqy_2yV-0dZ3deoYWovZA4DrQ4ahVuxledJH2cht7IchztQcHoxJOmO6Qe0RVX6Kv3Z8GIEDWxdic3j1NPVfqiWVVYwBOH1PywUEMVFVq1pjyaXNKQP5sQ8IIoVRE6vhatGLipC4PNP6zkKXARhG5tDXRfmsLRYAuFZuKOmPplZOsQ5skutj6PU3vNb6mWloBppg7lW1r-CMNgevwin3gND_gFOh5e-gn-uftsVUL4AFHhCSb-LfIQjRGGrzDk32_2MJ4i8S_On1lhCWEKrFqZ_vPZR6fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه ناوگان پنجم در استان چهاردهم ایران (بحرین) در حال سوختن است‌‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670023" target="_blank">📅 08:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZf4VVy6b56ynEsZsYw08oFDJICVPob7Z49D5_ldSTnWvVAmjY-sPGiYh6BG-TnzlwKbZj1_n6YClf0jFzcqiYY2O1XyUIHekW_Ioc7osnG8NLSsmi5ozBOoOKqAGu80AxX1qSAerWXdez0tvfiQklE1pjzPUOVoVy60Sk924sZEi0SUTS8owtqc6K8HCpDszYjOSGXPYCOdo5KqWqHZy9Xuy2DwG8NCBVOmLGz4Glcrt-P94IMhAssvY7UI0kjQawkAW0eMdpwX8xW8vI4-mBOl2k67kqQVd37YhusfImLETIALladFO_07PrM57LD4CWD8l4YSakWIVULjiZTYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیر سابق قطر درگذشت
🔹
دیوان قطری اعلام کرد که شیخ حمد بن خلیفه آل ثانی، امیر سابق، درگذشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/670021" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670018">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون وسیله شکم و بدن‌ات رو فرم بده
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/670018" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670017">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم آرژانتین به سوئیس/ آرژانتین در مسیر تاریخ‌سازی، سوئیس را به خانه فرستاد و حریف انگلیس در نیمه‌نهایی شد
🇦🇷
3️⃣
🏆
1️⃣
🇨🇭
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
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/670017" target="_blank">📅 08:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ناوهای آمریکا از ترس موشکهای ایران عقب‌نشینی کردند؛ فرماندهان پنتاگون دستور فرار صادر کردند
فاکس نیوز:
🔹
فرمانده ارتش و هگست در حال دستور برای عقب نشینی ناوهای آمریکا هستند تا مورد حملات موشکی قرار نگیرند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670014" target="_blank">📅 08:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حمله هوایی به شهر ویسیان در لرستان
معاون سیاسی امنیتی و اجتماعی استاندار لرستان:
🔹
صبح امروز یکشنبه، شهر ویسیان از توابع شهرستان چگنی دو بار مورد حمله هوایی دشمن قرار گرفت.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/670012" target="_blank">📅 08:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebf40c099.mp4?token=gT6_d4kXL0L8sIO9dmZDgoz_LPZZ73-lDhamQBRKWHczT2bnXA6i6QeoHYWATxQJ1YSNQP5jfTDixLiTpbWnJ82v-KzbUrNPmTyUtpcnOqzq7bszWozh-f38TUWM7o-0Kkja4KWDwW1c9a6IMmexY8gDD85B4CRghjUTg2-TcrUDWl70NyEJGOY2GKkNNS3FKWcUNoe1RzGPK9r1KFL5abQHvUcT5FnmoVVbTrhujcpRrRHI0S1O5vTWJJ-vkVSIMpisFEjW8Ke6GV1iVwY3DP7GZXwGFVHSTGcqjR-rZ2da2fsDs8dzQiZDawSagf0hr6X0AswGWde4UkExov4fhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebf40c099.mp4?token=gT6_d4kXL0L8sIO9dmZDgoz_LPZZ73-lDhamQBRKWHczT2bnXA6i6QeoHYWATxQJ1YSNQP5jfTDixLiTpbWnJ82v-KzbUrNPmTyUtpcnOqzq7bszWozh-f38TUWM7o-0Kkja4KWDwW1c9a6IMmexY8gDD85B4CRghjUTg2-TcrUDWl70NyEJGOY2GKkNNS3FKWcUNoe1RzGPK9r1KFL5abQHvUcT5FnmoVVbTrhujcpRrRHI0S1O5vTWJJ-vkVSIMpisFEjW8Ke6GV1iVwY3DP7GZXwGFVHSTGcqjR-rZ2da2fsDs8dzQiZDawSagf0hr6X0AswGWde4UkExov4fhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به سوئیس توسط خولین آلوارس
🇦🇷
2️⃣
🏆
1️⃣
🇨🇭
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
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/670011" target="_blank">📅 08:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5QxNoRDdQ1t7zwfvdEsNbmkPI4JWfOXF4Hh3BWuWjxx46jKfdOmeG9kK8pzJk1fzLr0fHmSBcl-JMa8rBcjA3oKs-FVIvPjkP1Zkc4LVzfQ1yyymQeNvdH46zrQ9gOaAKgPsBRauLs1ZEvfKdsvB7Ci6tlh_hPL7c9O5SMoE9NuJPfLzOyDRBzMbux4Jl4EBBdWwxEXAdxozcIMxxsM8p9zisfOC6EvMNjZoPsIo9Euemc6HEXrG6PwpL76N6BWGBvr9b6fVh0I61hiZ6hzm6bAMB0iqiABBSciEjmqXSkGp0DvNinJGbdElIIuMMsep95gAI0OoBx3_5NP2A7nSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دوران توافقات یک طرفه تمام شده است؛ به تعهدات خود عمل می‌کنید یا بهای عمل نکردن را می‌پردازید
رئیس هیأت مذاکره:
🔹
دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.
🔹
قالیباف همچنین بخشی از بند پنجم تفاهمنامه ۱۴ بندی را که در آن بر بازگشایی تنگهٔ هرمز با رعایت «ترتیبات ایرانی» تاکید شده است،  در ضمیمه توییت خود منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670010" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92140e47c5.mp4?token=KPlACI77hqG8cDDrNZDuqZqkPsd6cxQ-PFZ5l1lZRHJcAd-JbpvR112kXtl3GJzN9G85WIa36ImLKmflpqVZWhMHo0Ss5uvtxlixQ23C5tEKF54Ez47UA1DX_URDzuIDOnOazgil8Ka6LT6Cs-rfkFLZF6BeFTrLij3ekmStxLVTnoqWI9KkUWBKapnlbVvnxWC5D1J_nSUJs5g7V84HrP-Om2TNyAPmfJtzGDT7ALmyi1Gsb-zs4jSQwX5gBfEV9AMrVsKrAXPnsYY6bCV3AKCkKGBxplEuTvO8ymPNAM6FToqUquMhhwJ_OCua9lvctwcxc4l83NRPM6v1NGA_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92140e47c5.mp4?token=KPlACI77hqG8cDDrNZDuqZqkPsd6cxQ-PFZ5l1lZRHJcAd-JbpvR112kXtl3GJzN9G85WIa36ImLKmflpqVZWhMHo0Ss5uvtxlixQ23C5tEKF54Ez47UA1DX_URDzuIDOnOazgil8Ka6LT6Cs-rfkFLZF6BeFTrLij3ekmStxLVTnoqWI9KkUWBKapnlbVvnxWC5D1J_nSUJs5g7V84HrP-Om2TNyAPmfJtzGDT7ALmyi1Gsb-zs4jSQwX5gBfEV9AMrVsKrAXPnsYY6bCV3AKCkKGBxplEuTvO8ymPNAM6FToqUquMhhwJ_OCua9lvctwcxc4l83NRPM6v1NGA_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول سوئیس به آرژانتین توسط اندویه
🇦🇷
1️⃣
🏆
1️⃣
🇨🇭
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670002" target="_blank">📅 07:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a7f25c49.mp4?token=A5wbipsxJOGpvM0FlalWkptDz3JjtR7U91c8xGeWXMTswmp53b8qcolw3wEtsr8LdlKTEsoL1-LNAB9ZoKjZdfBIkJlrtrJOnwEARB98RodiFAzI8teLvKFKtjI3UxqQPyxVMiMrtwFsvRFcS6OVVnu9l7FTjqIyQAbAMA5QOEHlGxbcD_GVO60Czx-Oe7ZNViPmk9P0CULcwOYzyXi3WFtpSO8mKUOL2NmDTxKFeEMLo7O7qDhRzUghHWMZikWHSw2RNYDLE1k2cattMxu7MHbPLCYeoo9Vd7x29cMuY9g1_WvKV9YcN98uKYLjulrmgDVTwsPBHs01w0o5OgTG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a7f25c49.mp4?token=A5wbipsxJOGpvM0FlalWkptDz3JjtR7U91c8xGeWXMTswmp53b8qcolw3wEtsr8LdlKTEsoL1-LNAB9ZoKjZdfBIkJlrtrJOnwEARB98RodiFAzI8teLvKFKtjI3UxqQPyxVMiMrtwFsvRFcS6OVVnu9l7FTjqIyQAbAMA5QOEHlGxbcD_GVO60Czx-Oe7ZNViPmk9P0CULcwOYzyXi3WFtpSO8mKUOL2NmDTxKFeEMLo7O7qDhRzUghHWMZikWHSw2RNYDLE1k2cattMxu7MHbPLCYeoo9Vd7x29cMuY9g1_WvKV9YcN98uKYLjulrmgDVTwsPBHs01w0o5OgTG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به سوئیس توسط مک‌آلیستر
🇦🇷
1️⃣
🏆
0️⃣
🇨🇭
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/670000" target="_blank">📅 07:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669997">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8c23df8c.mp4?token=jUj0AIKhrj_m1YEvptarL4ep10m2hDxOb9pvMTJ1GECtY8AMpZ0a1Js8I3KMc3p3c3lSqsWMYjDTVc4-aVG04pOLH8L12aJPT4asR1-bwzM0jSRhIw3wSm_LxRXOg3fvPAM_58a81UcjqkXSl4QZcSUXAucg6gG4J21RmPQZ0xyJgDuuj8I2dh3ZYx2lVM7V5gCOpMnRbfPq7sZZ4KsZFYKmb6wRBrYjttMl27kNx442HoMPB7OBzyCuxM3rOt-u__IkjKA9MM9kJ_eu9MF5Xw-zLJe5dhW-uT1bwTThf0jRLkjFnEGegNKNxrJyP9iVxl75wg8Tvv7Oi7kttJbYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8c23df8c.mp4?token=jUj0AIKhrj_m1YEvptarL4ep10m2hDxOb9pvMTJ1GECtY8AMpZ0a1Js8I3KMc3p3c3lSqsWMYjDTVc4-aVG04pOLH8L12aJPT4asR1-bwzM0jSRhIw3wSm_LxRXOg3fvPAM_58a81UcjqkXSl4QZcSUXAucg6gG4J21RmPQZ0xyJgDuuj8I2dh3ZYx2lVM7V5gCOpMnRbfPq7sZZ4KsZFYKmb6wRBrYjttMl27kNx442HoMPB7OBzyCuxM3rOt-u__IkjKA9MM9kJ_eu9MF5Xw-zLJe5dhW-uT1bwTThf0jRLkjFnEGegNKNxrJyP9iVxl75wg8Tvv7Oi7kttJbYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به نروژ توسط بلینگام/ بلینگام پاروی وایکینگ‌ها را شکست و انگلیس را به نیمه‌نهایی رساند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
1️⃣
🇳🇴
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/669997" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669996">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Ljk3RQY8EXQiQQRpq3jAFh8uIQva1hfCrBMHF9Xmvb9IllX8_QzakzTN6RnNYc7qK_YVhGMeDR2K4OZAVWVlhIJh-Y0Ptn-ctPZA4TC9OgH6yQ2Rcj64XiRhnl2u8wFgv0-IET2P_dBhoCVmFzDLeV-66RquvtLOyEQh93G7K5Wk2xeoAZG1tgfebr2XBr3NLa9Zk5shB5rgU-JdTemTGZIjky5OjKYYDCq0JIgTZldpWr5J2-0z76Mxxf-DIuxC4MhaseB1wkvKcEshENcclgb5NdgBOzKL29pRAKU5tUvA5iiPuNYY9QpO4YM96LiO2-5vHgzcz3qFJbtsDfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۱ تیر ماه
۲۷ محرم ۱۴۴۸
۱۲ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/669996" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669995">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حمله به پایگاه امریکا در عمان
روابط عمومی سپاه:
🔹
مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیما بر آمریکایی در بندر دُقم عمان با یک حمله سنگین و غافلگیرانه در هم کوبیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/669995" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e6bb57d.mp4?token=sBIDYwSZojKwj-6g6k57q4DCOvo_VvuT84bU84BT1EZ1fIhsw10eYs0R7CafmplBNK7z6wf2oKKMQ1866rS_erAhj15kEXF8auJCq9Sy8kbtj3zWR14-K25_gdJo_XDbsu_wQGn9qzYDOk_5rbZwRvkoXXm7jnIay9GqTdxh6_HBljiF08h8C2ileK4aq84yYkFZ01i9aCCyCGFDoKo9mgh1QGBbcN8qjA7zIu3WOLRxOdeni5lwDega-uHI65K6AQWD9RpbwV3j-6LANW0IEF-CLQcB-R-jAFxktEegQsDMFo8m9t37csO0JSEuXI2ZdC0gdmiaJ7K0RJLe8x4vtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e6bb57d.mp4?token=sBIDYwSZojKwj-6g6k57q4DCOvo_VvuT84bU84BT1EZ1fIhsw10eYs0R7CafmplBNK7z6wf2oKKMQ1866rS_erAhj15kEXF8auJCq9Sy8kbtj3zWR14-K25_gdJo_XDbsu_wQGn9qzYDOk_5rbZwRvkoXXm7jnIay9GqTdxh6_HBljiF08h8C2ileK4aq84yYkFZ01i9aCCyCGFDoKo9mgh1QGBbcN8qjA7zIu3WOLRxOdeni5lwDega-uHI65K6AQWD9RpbwV3j-6LANW0IEF-CLQcB-R-jAFxktEegQsDMFo8m9t37csO0JSEuXI2ZdC0gdmiaJ7K0RJLe8x4vtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به نروژ توسط بلینگام
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
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/669993" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0968545801.mp4?token=qKaB2R1L7E0YqDpiE2TDHjCjEZbqwFDom3GiubRhdrGVRK1tFv9lCYveVnLA3lFY4iOL4bL5YiJaRoS9--Wi1Uz8vAvnQgj5Cpi-jnIWX21YBjwxh1GvEspr1QPj-Nlfxn4m2Ibl5-fH6YHA8RH_vfJ6AhtP2wU8eIQZj0oeTtBQxQLd71kAoCVSNCdZkM0hIRzxRcERi9qHwigjGcmozFIs3XY8c9kaDfiY6Qd8xgQbnhJpqHIdTB0z5tIfzMsUlUvS3KkOK29C8vx5esggpLjd8UKYjQTuKAd-ABEDF9SR6wjURXjfOWxpvwmrFr15FVZoIkeN549LNbv2LV9fOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0968545801.mp4?token=qKaB2R1L7E0YqDpiE2TDHjCjEZbqwFDom3GiubRhdrGVRK1tFv9lCYveVnLA3lFY4iOL4bL5YiJaRoS9--Wi1Uz8vAvnQgj5Cpi-jnIWX21YBjwxh1GvEspr1QPj-Nlfxn4m2Ibl5-fH6YHA8RH_vfJ6AhtP2wU8eIQZj0oeTtBQxQLd71kAoCVSNCdZkM0hIRzxRcERi9qHwigjGcmozFIs3XY8c9kaDfiY6Qd8xgQbnhJpqHIdTB0z5tIfzMsUlUvS3KkOK29C8vx5esggpLjd8UKYjQTuKAd-ABEDF9SR6wjURXjfOWxpvwmrFr15FVZoIkeN549LNbv2LV9fOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نروژ به انگلیس توسط شلدروپ در دقیقه ۳۵
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/669992" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIMzFayCe6pmLyeo8Wd35it_F0psZDNxy46IA19ZgUwXgX7E-jdGxPSYo_OhHrp-nN6oc_6tkZgG810980Sp524j95NT2JCLbzALqxpop7Cfl0tp7IxDI6GCOvQHtQ4_r8U1ALxD2Cbv8-JDUGRJ8EkH3VQsSbbzyxAn7A09b9lVMGpi9R6eZxq_ubgHMduo-0HgELmUQJl4VUyMEan0umZeblmIlmzNdNw_ypFV6idR7If8Fe5uJFeJQcOnt9HI_lM4Qfqwu9m9CWe-vCmIB_lONLl1ISx0R_fQphCAZdMhX49B66rEQWTcF9RThnTneqDPOxP0TMAzBSoHX60tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶ پس از پایان مسابقات یک‌چهارم
🔹
تکمیل نیمه‌نهایی با فرانسه - اسپانیا و انگلیس - آرژانتین
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/669990" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سنتکام: حملات ما در ایران پایان یافت
🔹
سازمان تروریستی «ستاد فرماندهی مرکزی آمریکا» اعلام کرد: تازه‌ترین دور حملات ما در ایران به پایان رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/669988" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
روابط عمومی سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  پایگاه العدید قطر در هم کوبیده شد
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پادگان در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت. بجنگ تا بجنگیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/669986" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
موج حملات پهپادی ارتش به پایگاه های آمریکا در منطقه
روابط عمومی ارتش:
🔹
در پاسخ به ادامه تجاوزات آمریکای جنایتکار به مناطقی از جنوب کشور، ارتش جمهوری اسلامی ایران، از ساعاتی قبل، با پهپادهای انهدامی خود، سامانه پاتریوت، انبار مهمات و سایت رادار ارتش تروریستی آمریکا در کویت را  هدف حملات پهپادهای قرار داد.
🔹
همچنین در موج دیگری از حملات پهپادی ارتش جمهوری اسلامی ایران، سامانه ارتباطی و سایت راداری ارتش کودک کش آمریکا در بحرین هدف قرار گرفت.
🔹
ارتش جمهوری اسلامی ایران هشدار داد: عواقب اینگونه حرکات و ناامنی در منطقه بر عهده دشمن آمریکایی صهیونی خواهد بود و در صورت تکرار این حملات،پاسخ های شدیدتری خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/669983" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
‌تنگۀ هرمز بسته شد
نیروی دریایی سپاه:
🔹
با توجه به بروز ناامنی به سبب مداخلۀ غیرقانونی بیگانگان، تنگۀ هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت.
🔹
اگر دشمن متجاوز به بهانۀ این حادثه که خود مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهدۀ دشمن آمریکایی-صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/669982" target="_blank">📅 06:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9181ac0230.mp4?token=ZJZpK-oWLe_oqXYGrdzeDMXLVqGaecsjhU5HmpPhewJt4CMpOMam2Xexzh43IB9eTYAzpio7_wWq6womQQBTe09esJ56Gf5LRg-yMMSKboT3_8HKmdJmOszyz7nB-RNUWqdRjQIYBiZSIDzUlQLsY9F1EH9wHjrDITKRCrjSjz6-HMiRH6xcjuiBMYCyEfktpaNKOdB2cr5dFWjPgpSXzzOXhT6K9ojiAhzdLJWNjYL_UEtwGkCa4xPH2yNg8jYK1aMg4WS-4HHw9MxS9O5znN7cjvjkRhUOmFSUdidlxZSY2u0wJBormFPTCwwltulmpo7HuKLx8I5dH4ydHXt0wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9181ac0230.mp4?token=ZJZpK-oWLe_oqXYGrdzeDMXLVqGaecsjhU5HmpPhewJt4CMpOMam2Xexzh43IB9eTYAzpio7_wWq6womQQBTe09esJ56Gf5LRg-yMMSKboT3_8HKmdJmOszyz7nB-RNUWqdRjQIYBiZSIDzUlQLsY9F1EH9wHjrDITKRCrjSjz6-HMiRH6xcjuiBMYCyEfktpaNKOdB2cr5dFWjPgpSXzzOXhT6K9ojiAhzdLJWNjYL_UEtwGkCa4xPH2yNg8jYK1aMg4WS-4HHw9MxS9O5znN7cjvjkRhUOmFSUdidlxZSY2u0wJBormFPTCwwltulmpo7HuKLx8I5dH4ydHXt0wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/669977" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس حسن اردن منهدم شد
روابط عمومی سپاه:
🔹
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
رژیم جنایتکار آمریکا با تحمیل اراده خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی آزماید و با تحریک چند شناور در مسیر غیرقانونی در جنوب تنگه هرمزد ایجاد کند، که با پاسخ قاطع نیروی دریایی متوقف شد.
🔹
ارتش کودک‌کش آمریکا برای جبران این شکست دست به حمله هوایی علیه تعدادی از پایگاه‌های ساحلی و دکل‌های مخابراتی در سواحل جنوبی زد. همانطور که وعده داده بودیم بلافاصله پاسخ کوبنده تجاوز خود را دریافت کرد.
🔹
رزمندگان غیور هوافضای سپاه پایگاه‌های نظامی آمریکا را هدف قرار دادند. در مرحله اول این پاسخ زیرساخت‌ها و تاسیسات مهم نظامی در پایگاه هوایی پرنس حسن اردن را هدف قرار دادند و مرکز فرماندهی و کنترل این پایگاه و آشیانه های پهپادهای MQ9 را با چند فروند موشک بالستیک در هم کوبیدند.
🔹
ادامه تجاوز آمریکای عهدشکن پاسخ های شدیدتر را به دنبال خواهد داشت.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/669976" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در دوحه قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/669973" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
منابع عربی: انفجارهای شدیدی دوباره امارات را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/669972" target="_blank">📅 06:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
گزارش‌های از وقوع انفجار در امارات و قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/669970" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌ شدن صدای انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/669968" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🔹
برخی منابع خبری گزارش می‌دهند که اهداف و منافع آمریکا در کشور کویت هدف حمله موشکی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/669967" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حمله موشکی از ایران
🔹
شلیک موشک‌های کروز و پهپادهای انتحاری به سمت ناوگان دریایی آمریکا در دریای عمان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/669965" target="_blank">📅 05:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
۳ شهرستان خوزستان مورد اصابت پرتابه‌های دشمن قرار گرفت
معاون امنیتی استانداری خوزستان:
🔹
شهرستانهای هندیجان، ماهشهر و ابادان مورد اصابت پرتابه‌های دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/669964" target="_blank">📅 05:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
هم‌اکنون؛ شنیده شدن صدای دو انفجار دیگر در بندر جاسک هرمزگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/669963" target="_blank">📅 04:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
انفجاری در روستای شاه عبدالله در جنوبی‌ترین نقطه استان خوزستان و در ورودی شهرستان دیلم و استان بوشهر گزارش شده و تلفاتی نداشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/669962" target="_blank">📅 04:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUDLnapEyWA95wrYtmpoht0bl677WRm3Ax1FiF0NgCIif7JUM6vpSLM7PDqgsijx_w1qqH-061Re2uXwfnc4mbf8FjgrXoulCImkrqcl4hs0QfWadP--fcGf-Nb7FMyMuGBULQZlkNbrwso-lxeuSEfsS0_qbHWLCVeEARCZWE-2TloPs8TQnzotVzuSKXhaW4CNze9YJbyMwrMqozq7gPI7Z68-cMygX9j0sMMauXXd2hhwe-nnZrmoZI9Cii3YFfdtc_RbJDxHUxOf2wGScV3mDKFfOPHaOIbymEkCdghtzJ0dI1NIF9uK04rkNQva0gry8vUxnefiqYF30f1EFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در حملات بامداد امروز، تمرکز آمریکا بر نواحی جنوب و خط ساحلی ایران بوده است
🔹
آکسیوس مدعی شده که تمام اهداف در این حملات نظامی است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/669961" target="_blank">📅 04:45 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
