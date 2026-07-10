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
<img src="https://cdn4.telesco.pe/file/H4bqKjD4rdv_c84_ZlYevoNSNt5Fbx56UKNzSnNDexAwB1uzk08dXaCerJV5s8WXWYgntjm-lSDZga0IL0uM88ref8ablTkhJ5niu3LgjILmiPhWJma3IlZW1JdByzkdoLOiLWjxuFnTqkmHlkP6djCOtkRxZqMJ6aeQZqRcX4KiVexo6tSTJtjj9sXtGcNm8O0RpXt5vWT3oImsjpRGxbI2Pg47vP5yEQ64ax_UGtGcHvej7wqs3q3GevQ5Mt1jli29MSBRZbOooOIJ4UWWLV-oUj7WJO1kv-MwgXX_xOfFuDljjiFnzQfAA0Zvirb8rGilM5VpxPpqqHc9D78tOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 365K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 03:21:07</div>
<hr>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هم اکنون حمله اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/withyashar/17361" target="_blank">📅 02:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سی بی اس : ایران در گفت‌وگوهای محرمانه به مشاوران ترامپ: در هدف قرار دادن کشتی‌ها در تنگه هرمز اشتباه کردیم
به گفته مقام‌های ارشد آمریکایی، مقام‌های ایرانی در گفت‌وگوهای محرمانه به مشاوران دونالد ترامپ اعلام کرده‌اند که هدف قرار دادن کشتی‌های تجاری در تنگه هرمز «اشتباه» بوده و این حملات از سوی یک جریان «خودسر» از تندروها انجام شده که قصد داشته‌اند روند مذاکرات را به شکست بکشانند. همچنین ایران تأکید کرده که مایل است گفت‌وگوها ادامه پیدا کند
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/17360" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باراک راوید: دولت ترامپ به ایران 24 ساعت فرصت داده تا به‌صورت علنی اعلام کنه که تنگه هرمز بازه و متعهد بشه حملات به کشتی‌های تجاری رو متوقف می‌کنه؛ در غیر این صورت، با پیامدهای بسیار سنگینی روبه‌رو خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/17358" target="_blank">📅 00:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGazy3FUZlRdf0JED0wU95KAyW1ZaICLANveURd35GRfUM3YR4qIfx49-B6pDUt89IoPUeMcxk44iYRw04eirWTtKzxxHnRhA2eK6islX8S080_jZRZnECxxuNzJyjEVNkoz8YzuNA9-c-LdQupn_poQOW-wPDigibbUPt6SmsRqYSdWDzEPlx5o6QgINM2NX4QZGxsD4GWNlC_zw85s_lokA7Fb5w5QfPbcnpj9ImZuAxcbKu0RtptD92Vz6Ftbnec-AVDnW53spm0na0CtK_vBgIiM27hbyeEP0QaS0l_0cbyeiGq1B5Hwj1jgxqiZhcWLWhHm6nxy5ts2hvnnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : من تو جام جهانی طرفدار آرژانتین هستم.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/17357" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فوری | بر اساس گزارش نشریه "اکسیوس" از مقامات آمریکایی: دولت ترامپ از ایران خواسته است که شنبه‌شب بیانیه‌ای عمومی منتشر کند و در آن اعلام کند که تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/17356" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=f66i1c3QYG2DhrqI6aTB5S7Y50QipEYuuTkbcdB_wx0qWBegUTbe7kOCn6x5e3dF6tLq3rTNquC27iMBKYeTgqGVgYtzoHK8yGezqV0TEvmgiNzHaK3wg__-5p6GGOCJxwYJwM6qpEjCASCjJVQBtZxtoO8UCfDNUqaHomN660kL53xvT0t35VV8eMVesCh6bcUGu1XdSDjccklkM2AnUMIKU72bm86_7rVUIREeSXt1WR2wPriO3eYW8WK09Yx_kryiIB226F8Y9TNeI05BY1w_mi8a5BJ35GL-cCv8_01k9fKUME8NUaVyMpzM0LKArhQ41Vj8TIu-0B1_hYqdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=f66i1c3QYG2DhrqI6aTB5S7Y50QipEYuuTkbcdB_wx0qWBegUTbe7kOCn6x5e3dF6tLq3rTNquC27iMBKYeTgqGVgYtzoHK8yGezqV0TEvmgiNzHaK3wg__-5p6GGOCJxwYJwM6qpEjCASCjJVQBtZxtoO8UCfDNUqaHomN660kL53xvT0t35VV8eMVesCh6bcUGu1XdSDjccklkM2AnUMIKU72bm86_7rVUIREeSXt1WR2wPriO3eYW8WK09Yx_kryiIB226F8Y9TNeI05BY1w_mi8a5BJ35GL-cCv8_01k9fKUME8NUaVyMpzM0LKArhQ41Vj8TIu-0B1_hYqdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام با انتشار این ویدیو نوشت : ملوانان آمریکایی در حال انجام عملیات پرواز شبانه بر روی ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش (سی‌وی‌نی ۷۷) در حالی که این ناو هواپیمابر در آب‌های منطقه‌ای در حال حرکت است.
@withyashar
ناو بوش و لینکلن در نزدیکترین حالت به ایران هستند</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/17355" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=mKkj7GK_x1tH7hk1zoYahtTV0xNo7_eC8aBSOWXn55OKHOroTvuNw13wyyWicTAOUeiUZ2u_D3GjDVxBqYPbeNNpBwluvXGxI1OH1_OwbQJEm-Rdae_h-0BVNJGV7CDteMknL948Iy4CpvaSMpZmAVaqbZcDjU4Jq8MgcunbwbUFtXi4SuO-z6Jv_sqtXOmyILN2c6xgaeBj-bcfwRICTb_FfJXXNhOwZzLFtEgpzuNlXZrVTAbGp1ZRIDgiCbXO9v4Wdypw4dgK1xiZj5C2_GJl0aKGZ31JrVa34NmI0FnVrvPM_unjBxGttdalKVabcSUejCPm2offPAzCwlKTLYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=mKkj7GK_x1tH7hk1zoYahtTV0xNo7_eC8aBSOWXn55OKHOroTvuNw13wyyWicTAOUeiUZ2u_D3GjDVxBqYPbeNNpBwluvXGxI1OH1_OwbQJEm-Rdae_h-0BVNJGV7CDteMknL948Iy4CpvaSMpZmAVaqbZcDjU4Jq8MgcunbwbUFtXi4SuO-z6Jv_sqtXOmyILN2c6xgaeBj-bcfwRICTb_FfJXXNhOwZzLFtEgpzuNlXZrVTAbGp1ZRIDgiCbXO9v4Wdypw4dgK1xiZj5C2_GJl0aKGZ31JrVa34NmI0FnVrvPM_unjBxGttdalKVabcSUejCPm2offPAzCwlKTLYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا این شکلی شده
💀
از کاباره تا کان پاره
😂
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/17354" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی خواستار عدم به رسمیت شناخته شدن حاکمیت ایران بر تنگه هرمز شد و تلاش‌های ایران برای این کار را محکوم کرد
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/17353" target="_blank">📅 00:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس ستاد مشترک ارتش اسرائیل در سخنرانی خود اعلام کرد:
احتمالا عملیات‌های بزرگی انجام خواهد شد، برنامه‌های جدیدی در حال تدوین هستند، انتظار می‌رود جنگ مهمی در پیش رو باشد، آماده باشید.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17352" target="_blank">📅 23:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزارت امور خارجه ایران: اعمال تحریم‌های جدید آمریکا علیه افراد و نهادهای ایرانی، نقض آشکار بند ۹ از یادداشت تفاهم است.
@withyashar
😁</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/17351" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع عبری  : هم اکنون تحرکات نیروهای آمریکا در تنگه هرمز
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17350" target="_blank">📅 23:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
به اصطلاح “رهبر معظم” در انزوا پنهان شده است در حالی که رژیمش در حال فروپاشی است.
ما این پول‌ها را برای مردم ایران حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17347" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری CNN: تصاویر‌ ماهواره‌ای‌ نشون میده که ایران داره تلاش‌ میکنه که تاسیسات هسته‌ایش رو بازسازی‌ کنه.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17346" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیل کاتز
: خلبانان تازه نفس ما منتظر موج بعدی حملات هستند
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17345" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آتش‌سوزی در نیروگاه تبریز، استانداری آذربایجان شرقی ادعای حمله خارجی به نیروگاه را تکذیب کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17344" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=nP23_su4syOMD2K_b0ZbUEcKgYmAdEWq-QC-5yVaQb5M5Jd6x3uemxzNQiD6K5XSw3nkLxtAjxOKQweAYTE7VcQBfc-4QnRpKKl3kgzztAMDmm1Mi0JNG2FCSiEAC-43LtOAapVbtmjRJIvFwn3L_7tNDyYKOld2j9ryiKr5-i3nrBjlI5sawYsShsR0DXVBolDJx5H07r_uCc8S3iampuLeKvndsHhOkY-_Fcirgqa5CgydUnyQPeBcYc1zdxA-3BWRssQeVYhQ0zGplp5Io3aYeQd4Tm6pcrRuUV-2TgIVSHcCUF-ZQG2mOuZvDsBxuYuflrWc2_Kc4LL5fRtxdoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=nP23_su4syOMD2K_b0ZbUEcKgYmAdEWq-QC-5yVaQb5M5Jd6x3uemxzNQiD6K5XSw3nkLxtAjxOKQweAYTE7VcQBfc-4QnRpKKl3kgzztAMDmm1Mi0JNG2FCSiEAC-43LtOAapVbtmjRJIvFwn3L_7tNDyYKOld2j9ryiKr5-i3nrBjlI5sawYsShsR0DXVBolDJx5H07r_uCc8S3iampuLeKvndsHhOkY-_Fcirgqa5CgydUnyQPeBcYc1zdxA-3BWRssQeVYhQ0zGplp5Io3aYeQd4Tm6pcrRuUV-2TgIVSHcCUF-ZQG2mOuZvDsBxuYuflrWc2_Kc4LL5fRtxdoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انرژی بدید امشب غده سرطانی رو بزنه
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17343" target="_blank">📅 22:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شورای رهبری یمن: از رژیم ایران می‌خواهیم از استفاده از یمن به عنوان میدانی برای درگیری‌های منطقه‌ای دست بردارد و از تشدید رنج مردم یمن جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17342" target="_blank">📅 22:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbf7psvqLqQ_ljs1JUuxK38HRi06Nu_0mP99sWrenxPSheP9YZn7ZsLAv-n1AyTYR7Sw82e_XgNVwGHB9Mf7a6huwU1vKVXZ-kM5UNQ-bfVYfT014NWWbGZI1d-lmB9qPW3SEeGWsVsErYAuVcpfsqBsjvCyhUGGxOpBCiFYjXD3N7lBEi73X1N5EJYmKLp5V1T9NREoJ8jvNFWIpJfiWEfwgXvpXPz37QdSqXq3W4SJ076NWrBKLh3KPweVE_cjeejtfoSJJdDmqJYH5tf1Fi3OJVJ8abs83525KYUk_FmfssQnJdC7en_Gv5o7ghTuD3vFNBXCF9IPCTalrUvlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، کرج الان مثل اینکه یه چیزی هست که کلی پیغام اومده
@withyashar
به علت تاریکی زیاد نور تصویر رو خودم زیاد کردم</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17341" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آخرین فرصت , طبق گفته رئیس اطلاع رسانی آموزش پرورش فردا قراره جلسه بزارن برای تعویق کنکور و نهایی
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17340" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کرمانشاه الان  @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17339" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بند دیگری از قرارداد تفاهم ایران/آمریکا به فنا رفت
وزارت خزانه‌داری آمریکا تحریم‌های جدیدی مرتبط با ایران را اعمال کرد.
@withyashar
یاشار : این تفاهم نامه رو رو دستمال توالت نوشتند !</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17338" target="_blank">📅 21:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=YCxxrgl5DAAYkhaKk34_wzj0RSNYAnXP6WIT9L1vc0icG2w1c_HrVSyxXzF3IVcHUz2OVVxuUy1TPJxmzyvHxWYx50FISzbuACezR5xm8mZSo9iBC8ZQNQ5xoGitGn0dkgU7Iq2yfX5rP8OoT_L_WuAQ-4gC9aAOem8UZIZpK9JpXXW6q7o4asxF1y5dsU5mxVnL_l3gCwhtZTcd7YzMjxMd0ac49n2uDHrfx-UaFAWWhBp3Pall9zcQvDdGl_9CYUPPri6210RFir3rcCzqNd3MGsgIRrO-p0FnG_TA6xVNcf-zrbBdClBqNwmNsGnZO4aTpyISGLHiKr9K8hrxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=YCxxrgl5DAAYkhaKk34_wzj0RSNYAnXP6WIT9L1vc0icG2w1c_HrVSyxXzF3IVcHUz2OVVxuUy1TPJxmzyvHxWYx50FISzbuACezR5xm8mZSo9iBC8ZQNQ5xoGitGn0dkgU7Iq2yfX5rP8OoT_L_WuAQ-4gC9aAOem8UZIZpK9JpXXW6q7o4asxF1y5dsU5mxVnL_l3gCwhtZTcd7YzMjxMd0ac49n2uDHrfx-UaFAWWhBp3Pall9zcQvDdGl_9CYUPPri6210RFir3rcCzqNd3MGsgIRrO-p0FnG_TA6xVNcf-zrbBdClBqNwmNsGnZO4aTpyISGLHiKr9K8hrxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17337" target="_blank">📅 21:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله کنکوری های کرج به اتاق جنگ
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17336" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HorChGH2VMn_dTmI7QSNgYuIE3fnnHdXlzVdBH1Jf4r-tabkJiWg2vvUAxuJhwFmCE8bySfWvzWLOKYaGFBXnLLbTLmNPoS7chaUHmPmbIAxM9TKB8djobOjtqTE-ws2xZEHVU1_nVcImgyLU2HrrpoG7ZuKN2uKdIPrKd9gzl60rpMu0WDm17XUs4mNDnNVJBXvo80rzbLGFzKKNcii0uNcWV5NT5fcuD2r9wT3MhRtIoHomxJ06ESU-vmN1BfpZtTf9V0B5sABk7F495XoGrNi-BmIlvUUnGcRZxWD5G2ALMSYuAKHS-sxUd32zwouMgdODfwLBJfO__hJUL2nug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرم‌ترین شهرهای جهان تو 24 ساعت اخیر
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17335" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیویورک تایمز: ایالات متحده و ایران در لبه پرتگاه درگیری نظامی هستند واسطه‌ها تلاش می‌کنند تا دورشان کنند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17334" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17333" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تایید نشده گزارش زیاد از صدای انفجار کرج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17332" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17331" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17330" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن @withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17329" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17328" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اقوام ایران
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17327" target="_blank">📅 21:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تسنیم : بررسی‌های میدانی حاکی از آن است که اخبار منتشرشده درباره وقوع انفجار در شهر یا سپاه ناحیه قائمشهر کذب بوده و در زمره عملیات روانی دشمن قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17326" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانوک : ساعت ۲۵
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17325" target="_blank">📅 20:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">@withyashar
ماتریکس</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17324" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17323">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17323" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17322">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">@withyashar
اتاق جنگ با یاشار</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17322" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17321">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد». @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17321" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17320">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد».
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17320" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17319">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه دید بهتر و نزدیکتر
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17319" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17318">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSnhMNgl-V2imRPrTyzxOmuDdcQ_dVs1zLHL9UrW08e-T0qTUvKgq1BbvGk0k76gDjEYzsIfiiaioDs6bLzpnmcv5mCh0BTYbMDW30J_WAELdCnmtqxWgEUUeEAsVIZsEhndtorCQq8yk5l60jspueAYXO-C-KQmeRtVgon6JY-xi0PCk-E1VH3wly8ZcPJH5CeGtb3ucjeeWWKJC9JXoNg6TcdC-KNY1ufQUtRnSq9ZZEEwJUtpDIE1qdlJRwSaN16hPchV4ndyyPYYCVmWKw9449YXYLm1kP6EVz6wvq0_R4NZv-tmdc39zpbQD_z6UpFOM9RZt8q8h3FiiXk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17318" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8dgrSwcAbMxutks9s3AmQ60tVP_9Hm-sKOrGZZVLc4e9u8jJ--LYSeoPWefQ5EMnYQJnvrcQbVKx2YvS2lZj9EcZcN0vGseINSVka-sKlXMWA-xUisl1DqSV3-Z9x2GEL5oJn8aLNsynM32QgQDprl4MtseQDTNbxTPDF4SpywRBfsvi9m3xyGsxBPKGSwKXt40mm4QZchrW8usB0piTV2dvA9Zzs_O1IBavJvahdze1D6VlOZNGhD2fRTIfcWTQRqnchOPBP4Tp5Hz10L0wvpz_UJZ-ZXMJm7CEI48OuDVuXBwCQ2IEqnO-umwsoVxgp2N6kaNKTrPaxRiCOB_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17317" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فارس : تکذیب شایعه مذاکرات جدید ایران و آمریکا
یک منبع آگاه در تیم مذاکره‌کننده ایران:
ادعای العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات در هفته آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17316" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkkqUk6qU2U_Bmc4v5BkB--H87eMGquz0PjGPOZEhBqd3KJuNUFtej0NZE2ICuOKmOYbD7g_bR27jW9SEkjYEBo2YCylx5c7H4_67JpXaLLIWBu4e5Lk0HUALuM-DwYY7JtzHRvWqJioymQUIBNBPHs3ob-J-4xpu5DMSEFJNulSDyxbNHfhvTfjzNIgVF96xxrtwHfDamUKpKCmE0SOKXozh-PuE0lhbfvFPiAIjoo4przRA8nVpAHTLsKitC6fWnFzWXuuCGNSkODCVKQtaucuFKNyvFcls02_4zmuOwThEs-aLzvVfB66HCwxA5yFmdfvAvrzSU80Db1lh1wVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری انتشارات فرازمینی ها پنتاگون این عکس را که توسط فضانوردان در شاتل فضایی کلمبیا گرفته شده است، منتشر کرده است. در این عکس، یک جسم ناشناخته در مدار پایین به دور زمین دیده می‌شود. در اولین عکس از مجموع سه عکس، این جسم در نزدیکی مرکز تصویر، و سمت راست کره زمین قرار دارد. این عکس در طول ماموریت STS-80، بین 19 نوامبر و 7 دسامبر 1996 گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17315" target="_blank">📅 19:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اکسیوس: قطر، پاکستان، ترکیه، مصر و عربستان سعودی در تلاش برای کاهش تنش‌ها بین واشنگتن و تهران هستند
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17314" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چندین گزارش تایید نشده از انفجار/زدن ساختمون سپاه و اطلاعات (کنار هم بودن)  در قائمشهر مازندران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17313" target="_blank">📅 19:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش‌ انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17312" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده در ژنو سوئیس برگزار میشه!
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17311" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=RuXgegABWQKz72-El8i2_E-XFauaKkY9DFgX0CR6brRzSuDe73p9SN0g_draIt1wVgopJas-7_py0JMwxTdJV7OrGDLqTQ9fo0IDtHRQrTHGUFAssxUsj0tpKeRxS2Sso05sHzSFbSer7Kl3MMuzc6mR0YdSWncMqA67V9a8dqXwjLO39FNzRb2gLKTtSFpTwE7dwc2hrKHMuyoMNW8W49zq6zQEFEXQ_LHaM0EM5jrn_N92RHT8VQM5CZOBFf4Q5Qk15_F3m2Zyo4HIBvHmNPaA8r7E25_pVahCoEPHiKM9KjKgKeV-PkHHaHDg31n_zYn9vI_9vUZoG-aSdyOL3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=RuXgegABWQKz72-El8i2_E-XFauaKkY9DFgX0CR6brRzSuDe73p9SN0g_draIt1wVgopJas-7_py0JMwxTdJV7OrGDLqTQ9fo0IDtHRQrTHGUFAssxUsj0tpKeRxS2Sso05sHzSFbSer7Kl3MMuzc6mR0YdSWncMqA67V9a8dqXwjLO39FNzRb2gLKTtSFpTwE7dwc2hrKHMuyoMNW8W49zq6zQEFEXQ_LHaM0EM5jrn_N92RHT8VQM5CZOBFf4Q5Qk15_F3m2Zyo4HIBvHmNPaA8r7E25_pVahCoEPHiKM9KjKgKeV-PkHHaHDg31n_zYn9vI_9vUZoG-aSdyOL3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجموعه اکسین پلدختر
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17310" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار جدید از بوشهر و بندر
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17309" target="_blank">📅 19:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb5h_kDr2Idex6ObwZ-IPzkUl0lTS4_SstWnL4BS1Rvjsw6Pj_gB5kiWT3T7LBEVV4rCsWCvFIqUYy14wUHzsBMdS4WgmOqVuoFAr6IarCRj6Wo5uA3a3cwUU0JvShLTsW0LnthcTfQNulcC2NPDXC9yLE2ujHCz2ZmUn49RoJdBD4wncfRQ9ZzBXjN-5wrF56XBFjtI6htvMh86VFQcgedGJN2xv_5XLWqlXzkP9tMKhg1mv8X3p-CUDRoABUOcS7iY-V3BWaNlBCO4E_49ruC7QBBxx8rvqk6D3iO4Rznkc6EPh6zQKCYhEg7VmXPcJKTCsUSyYfy0gCLgU9XLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر,
یاشار : بعید میدونم کار آمریکا باشه
پالایشگاه نفت پلدختر در استان لرستان، در حاشیه شهرستان پلدختر و در مسیر کریدور انتقال خطوط لوله نفت خام و فرآورده‌های نفتی کشور قرار دارد.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17308" target="_blank">📅 19:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxl86vXaNXY-W3xeIWswvFeDEZIukS7DPA43JcY0z1LkRp7zyZoS5QQOnOZDb0q7bYwDAMJnJz8c76cviQ3h5xESKzM6motFND-oab4XXvbgWbIBJ0zpzVlTAsC8_zDOtXuxql_tfHme9m_iOvvoyxFlgMLQYW190P9ZlnNR8DrsuCtdUU8-zWh_xhndHwgzmrHQxk_N-tw5lLf5Re12BSK85XnBgCVmugkiX3si8uCQNgiIbrxpMiXjVHHM47MYcDYWn47GsETxoY9xHpYVpYIA_QFHe05eQOKv2S673zHKeeZI3CD2efKuyREbs-EW-yD-OPll_zWYyYxNKGlT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر, همین الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17307" target="_blank">📅 18:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای، خسارات ناشی از حمله موشکی اخیر آمریکا به پایگاه موشکی ضدهوایی بوشهر در جنوب ایران را تأیید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17306" target="_blank">📅 18:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای اختصاصی با روزنامه نیویورک پست: «اگه مردم ، امیدوارم دلتان برایم تنگ شود.»
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17305" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17304" target="_blank">📅 18:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVO_3p3B8Ryv1oshFP7hdESKcNfEQRdkWXWNnDCNlOwCpXKeNSaVSZ3-xkBt_OlzO2I1-E1BXuU2DeL3_EnkEhXvyO9pygESfmc-xM_34pRwRsmOCCDnMOoW5GfNzLtJVmLwsCBGvwJDgb9PRFUrMB7NnrD14XpM8k3whkvU17rIQZl_ahK8-CdHhLQeqZuDvROuXL4_tWhGbAoJ4gy7SDlrW821w-lF_3pO-MF6QC8VvLaEpKjfC-ctkewyoDwSSSzEiCo_058uSIf8K18LRbc4pPGiJYQwhzLr2osefDhGj7dB6MqMBxtZG8CDIhc0e5vAaMaMZnyBpkg8_b6CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17303" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17302" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ62biSsUA9_Qy3W8DvoQBiP7zKUn0KStB7PUzGcLcsq1erMiQUKOseV1tNH5U91nbchXqD-VrVEmcRi92jEcUvTlnTK1VF01102ZOU1zZDpfOFqIUhlpyKBT3Iq6BVn2Et3Q0tiLLFWaspikG8TDUnUHQwDfpmWliNRNTtmpnJI1n5rj2MDoQU6tauHkJkkYcoDFng7OIkkdsdQd-CqlAc2FrLRMo-stfNqtcILUI3hSLTb7FTvrIYTcJNXi5OO6oXC_rtRIEBd2MxvodsZuDLZxGChj9958xHJfuWIF7R1X7akLm-k-k1GazF1VBh2vWAhlJZI3yUzuLpUdVgNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهراً پایگاه دریایی ارتش در کنارک هدف حمله قرار گرفته. @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17301" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17300" target="_blank">📅 18:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زدننننننن
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17299" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش انفجار بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17298" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17297" target="_blank">📅 18:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17296" target="_blank">📅 18:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqJBYB9jqdDVit4XRhxwnnNvjTAIN3CrHIjo-kELlzCA9zwDFEGus6YlLjNeKt_fAjrm3j2isX8XsZbnxL1xlAf-DYgfCz891AAsAkZvm7e8fshtEJ_82qMcztPiJM298mdvI-0yJOWtRiNUokayZ1DXjmzAWtXOwReyHcP8UK_Hd3zrwbrAZeKa_bB4QroHpLR97WTEuNPSfXW7N4zPhF_LpI-NHogIokq8yU9JOkqEFotybUe8db8rcOY3cQlt1N0KDsQfiIT4p-U7FIapjlQYSLAf20tWJ9ZuvOS4K3nOOr7DrRpmWVNp2cv4KlqeBos7YUVoVQm8vwwXIM6o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است. آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند. به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17295" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: اگر جمهوری اسلامی در ترور من موفق بشه، از قبل دستورالعمل‌هایی گذاشته‌ام و در اون صورت، ایران به هدف شماره یک آمریکا تبدیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17294" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqE7Qhbtk628lAkmPc7Pvsi2JEEAD7WwftxO2AxxysfhZdrm1azUVAI0OVFmro67Odub7FCKXVtQYyGsNQip9nYiCxRuMSpzR-syCw92fAWnDJl6oXYHoZnB24VnEXZTK8TZnaryIoF9jieNFsVVA-CXjPWFYNtORVnIhw0BcmyvVeQUdTKICT9XwCjbd3jYkN5Df-tz5iXXwK4Fv-E2jfrP-MI-hjhVRZBrus4AO5VQXDEH3Xr2zrzdAyrRpzuhd9UQOugu3fIlX_SPpKwPKAOlWsT71Wq9FyTnZBZGQtNQMY_E6X69kOjpUnPy6ZL-tPjA8sxCjELXJQY1DpaiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ایران از ما خواسته است که به «مذاکرات» ادامه دهیم. ما با این کار موافقت کرده‌ایم،
اما ایالات متحده به صراحت به آنها اعلام کرده است که آتش‌بس پایان یافته است!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17293" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRgAm8fbw32AdzbWVgCW7RhkgjFS-ptK2XeHmr2o7QSIOuPCx1-HLRz_uFI_WMNxGYBgSMOECBGsIMk_HI15RjeML2xDNEQFe7C1MRij8jLvwd_RsstNmBgcGbIj9zdUHU23eJhf-ruQTG-o8YCuESBqOh0rzyRzGdd-AULkZ2_z-dKZFd96Tr0yJQj6NStyehDJ-0NxDuDpOXunqKxx_Yv2iEAWw7b3a1Wd8Nj7CbnX3YehBu6eZnVYgKNpjrMA5j_MThgWoFtq2jl64FQChBTc_nLoEjVk5VjRpn7KZHDoKE6_ahOLnasd4JWVuCmIYLz196yZButiukdNZKLf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17292" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX-ewq4ZK0gMH5Kmx9mi-Jhg2GDm0_SeB8fwabF1UQInVIbx2Qbk_xWFN97kkWxmtXnmcolnqAPxUUBGhabnTj3SDgFWkCi_ztytym91hVInwtMYluuYWyPqDxGEaLPqAAioVrUnC89EZ9knkP4p33TmUwcofLl6WYP0nGAqZbXjfbFWC2AuzbrBMgggccBrCfati1TsDqOQuTAO_LfD6kJ-8ElOyyQXUotIt6r1oxf3fDVBFOPTv9km619nuOKCSNmYtiklSqJg0NBKLoBFf4CMZCwUqwa6ETDFAPhlhZuJRSzRk3-QkKsiB8Gnl54GoCB6s6FlppGydVfQTmXlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر‌ ماهواره ای گروه رزمی ناو هواپیمابر آبراهام اینکلن و ناوشکنه های گروه ضربت ناو هواپیمابر ۳ در نزدیکی چابهار که شامل :
* USS Spruance – کلاس آرلی برک (Flight IIA)
* USS O’Kane – کلاس آرلی برک (Flight IIA)
* USS Frank E. Petersen Jr. – کلاس آرلی برک (Flight III)
میشوند
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/17291" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بازهم روسیه و چین با طرح بحث درباره برنامه هسته‌ای ایران در شورای امنیت سازمان ملل متحد مخالفت کردند.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/17290" target="_blank">📅 17:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FME9FQVFJJKCyOAeGn26o2RD1QUcVMV7s-JY-Uu2rf64qj3ujmroJAdxyhOl0QqmXWvXvbLGJ3Cj5_5jU0CDGpyTePMh3AFlHORfK18_o5FqYURXEKMIwqfcmD0da3zODfYNBmIVJwN-rq8wNyzz56XKv_SNXYl52Q8b42V-mVQsszRnDnrdGO9KwhnMfxjDyi_VAyYZjl1Dl4BUnBg3fSUYEAwE0HKCeS2eCcdK14dmaNOPixdSccPNMyIc5vVBdgtp0YybAkWU6XJpDJpJRBSk1CHvsW_zhUjIVds_SQOfHfbGyWdGPSfE_aqVz4yfE7OS_8WowcnD9_B5om0cxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن (CVN-72) و چندین ناوشکن مجهز به موشکهای کروز تاماهاک در خلیج عمان، ۲۵۰ کیلومتری چابهار آمداند ، همچنین دو فروند هواپیمای P-8A Poseidon نیروی دریایی ایالات متحده از جیبوتی از صبح امروز در حال اسکورتش‌در این مسیر بودند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17289" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/17288" target="_blank">📅 17:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تسنیم:یک هیئت قطری به منظور تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای اخیر به ایران سفر کرده است.
گفته می‌شود هدف اصلی این سفر، تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای سه شنبه یا پنجشنبه باشد که در جریان آن متعاقب اتهام زنی قطر به ایران در رابطه با یک حادثه ادعایی در تنگه هرمز، ارتش آمریکا حملات گسترده‌ای را طی روزهای چهارشنبه و پنجشنبه علیه مجموعه‌ای از اهداف نظامی و غیرنظامی ایران انجام داد.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/17287" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرگزاری CNN :
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/17286" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/17285" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/17284" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=A-931137TXGg3DMnqPmYGMQWzchFLq8Sfl_-Lzmsjvq7EvqnkAcFW-QywZVYl-9ohDS_4dUzoNd4gM-rSOcu-j1ot_PnZ9Rv-wkAkpMvR1afnVJWGjiXBlorkheGUm0sxOxcENqO3U1cb0fpm2xbZR0YkGWBcEnqtv2VSB3OBTddUEyfG_hh98_8trGl3BqIyyCNLwxZV8OV_kNAcdOqt1JpNYSLMS9Q9lFDc7mE-0qb_3ET3UGnPMAAiaQ5JYAAf0yrPmeiUF7gdmdaevF_gZRXHdKKnbRUdn5BvjZL_q0GtC6UC3nouMSwjPPalo4ZTuyZ6FRXDv-gXRQSCNxveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=A-931137TXGg3DMnqPmYGMQWzchFLq8Sfl_-Lzmsjvq7EvqnkAcFW-QywZVYl-9ohDS_4dUzoNd4gM-rSOcu-j1ot_PnZ9Rv-wkAkpMvR1afnVJWGjiXBlorkheGUm0sxOxcENqO3U1cb0fpm2xbZR0YkGWBcEnqtv2VSB3OBTddUEyfG_hh98_8trGl3BqIyyCNLwxZV8OV_kNAcdOqt1JpNYSLMS9Q9lFDc7mE-0qb_3ET3UGnPMAAiaQ5JYAAf0yrPmeiUF7gdmdaevF_gZRXHdKKnbRUdn5BvjZL_q0GtC6UC3nouMSwjPPalo4ZTuyZ6FRXDv-gXRQSCNxveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از قبر علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17283" target="_blank">📅 17:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گیلا گملیل وزیر وزیر علوم، نوآوری و فناوری مصاحبه با اسرائیل هیوم:
"شاهزاده رضا پهلوی و من، «پیمان‌های کوروش» را آماده کرده‌ایم؛ آنها آماده‌ی امضا هستند و نتانیاهو با سقوط رژیم شرور در ایران، این پیمان‌های صلح را به خواست یزدان امضا خواهد کرد.
رژیم ایران درگیر جنگ‌های داخلی است،
و هیچ شکی نیست که این رژیم سقوط خواهد کرد!"
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17282" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HRe5s0C6jV10Ezg7l6f2aHYQFhpSqeaKTKFW1vFHrqud5LK5X_2Eeb_m0ouCaBhxpoNky40dgJwUAIm2rvQ0hs27y3GoVEngP6KuF2znDiPYS4gK4WC07A3Rdpqr2ZYURtBmd_SHT0G-LUi0uu-bdzJp8HcaoVw_wzsgT4He6x6VFbFHlt0Pbb2tbD9tVNxtwJct4ceJsmMqHV4ZoGDc3FxM5eb7mikyN9VBAaoILlYtAGuJWNAB4ej0dsESstWFlvJy77PLBa8IigTC_vJ6qxkfLbJmU5GGz1mCm_ErpKZ4ctUR6jmhlTYhsC0pNI_0-JRJ4TSUMCZ1BZUuT6MbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HRe5s0C6jV10Ezg7l6f2aHYQFhpSqeaKTKFW1vFHrqud5LK5X_2Eeb_m0ouCaBhxpoNky40dgJwUAIm2rvQ0hs27y3GoVEngP6KuF2znDiPYS4gK4WC07A3Rdpqr2ZYURtBmd_SHT0G-LUi0uu-bdzJp8HcaoVw_wzsgT4He6x6VFbFHlt0Pbb2tbD9tVNxtwJct4ceJsmMqHV4ZoGDc3FxM5eb7mikyN9VBAaoILlYtAGuJWNAB4ej0dsESstWFlvJy77PLBa8IigTC_vJ6qxkfLbJmU5GGz1mCm_ErpKZ4ctUR6jmhlTYhsC0pNI_0-JRJ4TSUMCZ1BZUuT6MbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آفریقا جنازه خامنه‌ای رو بدین شکل تشییع کردن
@withyashar
🤣</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17281" target="_blank">📅 16:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات اسرائیلی:
دولت ترامپ تمایلی نداره که اسرائیل در عملیات نظامی علیه ایران شرکت کنه.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17280" target="_blank">📅 16:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار آکسیوس:
به گفته یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و در تلاش برای کاهش تنش‌ها و ایجاد شرایط برای از سرگیری مذاکرات باشند.
این دیپلمات گفت که جلسات در تهران بین مقامات قطری و ایرانی هنوز ادامه دارد «اما واضح است که هر دو طرف می‌خواهند به یادداشت تفاهم بازگردند».
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/17279" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZZQkNyWcXoSJlj0Qa8pzC3X5fB6YADRn-8cwlgKXfFWCUbMH2XJv43Vsb3cEOHUZY2-IleTJHNbClEIuQgy4b6MaYzAZqbuGMaKwgJi5osq_Jb2tsQB0IUBpkJ5cFKt0Cg_HZVh29y8YFslp6rkvSO8Sq5Zj74qQ7l_pxhrXSX08Y_Pg9Ohe-V5mkXmIxIqPG7x2j-6nDOqXOoP3k3iQiMuJNQuGkYSQTVuv68hpUzSqP_sseuHpFd4H1ZI6m1gRJD8Lj4iijZAtAqlPBm34W3K17T6epGR3JUi5QBDKc_sj0ao-hE1rbJEN1JnQltsWwx7am_EGjrjtcR4309k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون  گزارش های زیاد از ستون دود عظیم تهران فکر میکنم سمت شرق(بزرگراه امام رضا-جاده مشهد)
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17278" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV_KOIecbgUMZzZ3a67pZG-vYoUTKIWCQY2GKUR9byPU3c3UtcRCCbNFNhMUvifDYA_QAq436wYBe0HmZje7jDCzLftEBnC4C-2XCgj106DukwFHDRh8fKoLq0ZhnqROB24CcqmV5TOUuVS63LAPJKANS4lok9JUPg1X48Nzv8ofTFSsuu6CNpetNnoHb8T_wdxGcAmKOFa6E1pTf3kIM3rtEEOXBF8CBX7LRvDKVjwegu9I2NJqB957u7SIeotIkm0b_L5gkXe_SVhNCgbKW4cAgSG4dy7IqK-9t8Q9jUMUeA78fEbvGpqs7vN5vhu0PZVJ7bveAWOvC01AdkG-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دستگیری 8 جوان امریکایی باتهام تلاش برای ترور ونس و ترامپ در هنگام بازی بوکس UFC در محوطه کاخ سفید . این طرح از ماه مه شروع شده بود . یکی از این جوانها    Tycen C. Proper, 19, of Danville,  تایسون کوپر 19 ساله هست و عضو گروه ازادی 250 سال -هست . این طرح خیلی خام بوده . امنیتی ها هم اجازه دادند اینها کارهایشان را بکنند 4 روز قبل از مراسم ، با شواهد دستگیرشان کردند که به ترامپ نشان بدهند تهدید برای وی جدی هست . این 8 نفر از 8 نقطه امریکا بودند
@withyashar
حقیقت یاب اتاق جنگ : خبر پخش شده مبنی بر ترور نرامپ در‌ امروز و دستگیری ۸ نفر فیک نیوز است</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17277" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترور ترامپ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17276" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع آمریکایی به شبکه CNN: آمادگی‌ها برای حملات بیشتر به ایران تکمیل شده است. در حال حاضر، واشنگتن فرصت نهایی را برای مذاکرات دیپلماتیک با میانجی‌گری پاکستان و قطر فراهم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17275" target="_blank">📅 15:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محمد باقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی هشدار داد اسرائیل پشت این اقدامات خصمانه قرار دارد، آنها از پاسخ ما در امان نخواهد بود. در صورت وقوع حملات اسرائیل به زیرساخت‌هایمان ، انتقام خواهیم گرفت و به آنها حمله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17274" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxA-fEdcK5WnV-OuQrh8rnU4oEafpKPtkOhdw5lz9vJfn4V85-F4gtw01VYyBeqruDhE-KU-F8mIpVcn1EvCke8HQ4jimoCpfklGD0WIQNsW7Cie33MXR9oHSM3Uq0DgDh70c2WG9Ic3fnS1jANfvL9-Dv7SEdwo_mZCxRRSbg662MvH4tVuYNAsuXy3g-JFik64inx1uJfW0iH67xwXV5hB_ojrD_MZ0FZP5kOi-S6ZLErtXikU7YE48BoUv8PQ_HfYV5vs3SWtluTmhb0wx-dxcfe32mNz7R7_jhWg0ht86JO9rRu0ltuAsbqNhaTBo35o0-0er2pieljxsxvk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند اف-۲۲ امروز صبح پایگاه هوایی عوودا اسرائیل را ترک کرده و به بریتانیا بازگشتند (در حین پرواز توسط KC-135R مستقر در رومانی سوخت‌گیری مجدد شدند)
چگونه باید این را تفسیر کنیم؟ فعلا جنگ نمیشه؟ یا محافظت از مهم‌ترین دارایی‌ها قبل از هرگونه حمله بزرگ احتمالی؟ زمان همه چیز را مشخص خواهد کرد..
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17273" target="_blank">📅 15:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=pEn4KyTwP6_VwPFwntq1gyaKq3O0vMRKEGit3wyQO-xTp0NyvkblFBlgxRA2dUb_7uA_mrc2onBQ75T_POeAw8MlZ237tWMpXUIvkPild0MHQvL4gsyRGsQ_UAyBYGYIymF-_rELCoc78Q0qapNzisaFKtn2Ha7RiJ_f8ELp1dl-T9bRoWOwCGX5R4eGo1WkjLP5Cax6fVDQdnuMu0qiK4tZD-vut-rQlxISDc4tLGIjIt6RJTbUd306Z237XhRRihB7ZEwcHl9gxbj2rZGl3tGeuTWjqxQatCQZx41PAJnmpv6bimgWsfUvYBGhBfORLJUPUn1bwSyxdXOsPRKNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=pEn4KyTwP6_VwPFwntq1gyaKq3O0vMRKEGit3wyQO-xTp0NyvkblFBlgxRA2dUb_7uA_mrc2onBQ75T_POeAw8MlZ237tWMpXUIvkPild0MHQvL4gsyRGsQ_UAyBYGYIymF-_rELCoc78Q0qapNzisaFKtn2Ha7RiJ_f8ELp1dl-T9bRoWOwCGX5R4eGo1WkjLP5Cax6fVDQdnuMu0qiK4tZD-vut-rQlxISDc4tLGIjIt6RJTbUd306Z237XhRRihB7ZEwcHl9gxbj2rZGl3tGeuTWjqxQatCQZx41PAJnmpv6bimgWsfUvYBGhBfORLJUPUn1bwSyxdXOsPRKNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم خامنه‌ای در قم یکی از محافظان سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره
@withyashar
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17272" target="_blank">📅 15:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17271" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر خارجه ترکیه: آتش‌بس میان ایران و آمریکا پایان نیافته است /دو طرف واقعاً می‌خواهند به سوی یک توافق صلح‌آمیز پیش بروند /امروز با همتای ایرانی‌ام تماس داشتم و آنچه رخ داد، سوءتفاهمی درباره سازوکار عبور از تنگه هرمز بود
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17270" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2511809773.mp4?token=eqA7SF3nJszkIFgkYvA-grUNgfqyvQUWa3QWUFGm_aWPkNrKHNQ8pwR5yEHi5PjGETG8j-XcV2hm0E9p4sGg2l3O08w3bcBoEkyI6JWslKy5yIYpPDFME2YCg5I3hNYVuAF31pldwfISAUSZMbNbSpXGNcy2qWrIGcu78RyAX5eavL4m3WekZ5eQQA1KhtKnt9-htKziV4cVOJ00V4uEYSr5_7wZUKF9I07xUHxIxKT7RRqhRAWH-zTPCYchCIJFP7ZIOIw5OZBO0Hx8b0goxwmYSJj7aff9wpos7ma-8tShZ9LKArveJU4x4OPXN2PlRaoMzaxq_jJSihqqS31Fxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2511809773.mp4?token=eqA7SF3nJszkIFgkYvA-grUNgfqyvQUWa3QWUFGm_aWPkNrKHNQ8pwR5yEHi5PjGETG8j-XcV2hm0E9p4sGg2l3O08w3bcBoEkyI6JWslKy5yIYpPDFME2YCg5I3hNYVuAF31pldwfISAUSZMbNbSpXGNcy2qWrIGcu78RyAX5eavL4m3WekZ5eQQA1KhtKnt9-htKziV4cVOJ00V4uEYSr5_7wZUKF9I07xUHxIxKT7RRqhRAWH-zTPCYchCIJFP7ZIOIw5OZBO0Hx8b0goxwmYSJj7aff9wpos7ma-8tShZ9LKArveJU4x4OPXN2PlRaoMzaxq_jJSihqqS31Fxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل اعلام کرد یحیی سعید محمد حمدان، فرمانده تروریست یک تیم «نخبه» در شاخه نظامی سازمان تروریستی حماس، در حمله‌ای هوایی در جنوب نوار غزه به هلاکت رسیده است
.
او در حمله ۷ اکتبر به پایگاه رعیم مشارکت داشت و طی هفته‌های اخیر نیز برای طراحی حملات تروریستی علیه نیروهای ارتش اسرائیل و بازسازی توانمندی‌های حماس تلاش می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17269" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کارخانه فولکس‌واگن در ولفسبورگ در معرض خطر تعطیلی و صدها کارمند در معرض اخراج قرار دارند، زیرا صندوق سرمایه‌گذاری قطر، از توافقی بین این کارخانه و شرکت رفا جلوگیری کرده است. این توافق برای تولید قطعات مورد نیاز برای سیستم دفاعی "گنبد آهنین" بود. صندوق سرمایه‌گذاری قطر، سومین سهامدار بزرگ فولکس‌واگن است و با اعمال حق وتو، از انجام این معامله با رفا جلوگیری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17268" target="_blank">📅 14:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی ان ان:اوضاع به شدت متغیر است؛ احتمال از سرگیری گفتگو ها وجود دارد اما احتمال جنگ هم همینطور
فرمانده ناو هواپیمابر آبراهام لینکلن در دریای عرب به خدمه خود دستور داده است که آمادگی خود را حفظ کنند و منتظر هر دستوری باشن
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17267" target="_blank">📅 14:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جواد لاریجانی : باید لیست افرادی که در ترور رهبری دست داشتند را صادر و اعلام کنیم که از نظر ما مهدورالدم هستند
این جنگ به پایان نمی رسد مگر انتقام گرفته شود.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17266" target="_blank">📅 14:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال 14 اسرائیل: اگر مجتبی زنده باشه از ناحیه دو پا آسیب جدی دیده و روی صندلی چرخداره، به همین دلیل مقامات نمیتونن اونو در انظار عمومی نشون بدن
@withyashar
یاشار : اینو خوب گفت
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17265" target="_blank">📅 14:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">با تمام حالات چراغ اتاق جنگ امشب روشنه و ما امشب رو بیدارم
🙌🏾
همیشه احتمال هست مخصوصا وسط مذاکرات اینشکلی اونم اخر هفته که مارکت بسته میشه</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17264" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17263" target="_blank">📅 13:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17262" target="_blank">📅 13:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">@withyashar
امتحانات ۲</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17261" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار : عمو اگه امتحان دار‌ی خواهش میکنم درست رو بخون
🙌🏾
این خودش ضد خواسته رژیمه اونا میخوان تو بیسواد باشی ، این خودش گارد جاویدان بودنه ، ترس رو تو وجودت راه نده سنگر رو نگهدار ، ترمیناتور باش مثل شیررررر باش نسل بعدی ما نباید روح و روان خراب…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17260" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17259" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
