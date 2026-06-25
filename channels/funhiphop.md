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
<img src="https://cdn4.telesco.pe/file/H2FM_5IEDeMOrF-i7-wkP1WoMNr2CYbgUL4y9ZaeLgUOX2w__m5MybFM3HUUhqj3sHymSQWR05cpPZO3YefN_oxAsUw3yFbAQbxhS3wgUvNh0HPYeGMwlsryaCllKcDXhNPjcm7_dVWR5WfMPIUX4Ybpdz7-OvseLBcRfnKveN5KqKh6UT6hLR06smeBg0HqKjY56Ph2yaeZOp47LYmxZUSgDZv_6uniwl1cSrLx16Aiw7hyW2mPiL1M060DBbUJabHNrGavlpb8n8SAhiENd9jv8ccsgubHPyNT9XtG5uUHdiMHs-Iwm4eCMimBER8JudlAo5RakL83bBZtg2vOvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 181K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISToCchcVXqliwmIUbr5lKNwtWJ98_zG8DUoCGucWb_ATkPicggvkX98tXAq3b4_GCANTkw5XHh8uE1DqY9ocQWjtWbTIggDX_NQXWEhzGcGuTbW-aFVlCFar9vyeJ5H1Wfg0KcyixjgHlbjpLyUB9wGomqriFeenjioZLEEGjGeAywzsaekC1RESlE2rnxlbgoMotjKDsJA5Yr0JUO8l6Pk8xGmsDDvJ6ZIVBFQGGSzb5vKAceMDXUsLmBCrb_W9NDQw6QOvA6IPWcwx8rp6Fz_Gq2QNs8emxm6esv1MSwemAqU4ZmBsLIlrn_qXmFb04TyeNPw-EjGGzFZ6rt85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffDIS7eXRdKeq8tQZ1mZ2pk6O66bzMVRlH_DNHph_eB3RGCSrYPMqcOUiCjj4MzD7axpz4qPkBbi-ad5KKTg0R7Fo7PUFw8knQdMdQ738let2YI-Y85AEFlbd697AIdVUHo4XebKzjduBEu712tUsbR6EuN41k8QtanMVVr4r0tJNyqZC7XsP2NhMEfrUEvdJ775DDr3CRgxGXaMDmD9yQw6a3PHMSEYcvKuNbcuC_7Rh802OI83k7fHyqe-s8eifkzVD58vw9eQFHHWsPXZpAD4eDOzVXu1aAMkouoMn3uZJnfXmgxdVsrtkpW19GG7n8IDGCDmCa1y-JCefpeYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwihilxDqZGDb_hjO5Hb6uGpR-fe8b6GkCqEcYzEr70XtrAOJNIVtMxbZKfq3rgt0QC-lOSeUd9onGfTp4uZTJ8v4PgvXBR9OLl-Q7XuhEJxTHFFMqeJ-TeHL5ogFJZAzEAQG7ZKGkYUfbRvdkA5EjtpP2N33POGfGmfY4_7D1fGREhNv1MHX7-ZbFgbqbsFMn2MgVHJTJdwkmd9AhCPUYfMECEWEIeJ7tJMdkT3F1HyPjzWx3wGO7ChPxplFQZxTUShrOXurxcEobtWu6e08kRIEZoS0jfiYq_UOcf6nvfCiA0s9bMYTD6Cf165kw2DOoPWID_DyqWfZqsRrmK0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqD-gwNULJXquTYnNzEXonr5GAolPS8UIO8J_9r44Kmgh1jST2p7vU9bgOXFmnL0UsEgp3Lh5FoY9wfQIM7Ad9IM3wfadIGKcDXYLNL_Lu2z2hcxRtfIPRYyaMoDgg4QihyruAlIoG8jAwtq0n3DTxAmzGqszpzcBB_i9jJPzbzVjfXhA12FxoGg1GmMc7_CDyf4iXMmtIh10oc8BlOu_jSlWj-3ZN4stmn0Q4MBDdvX7DorRxy4wK6cnRKfk7ZN8FvftNmFV26RJ2PyFN3BBHfzXeC6ecEDSh0kLHfhMjvCau_j9U338IR5sLqy_URtxABQPxzapdA8XClN7e3rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFykXuFJZ6DZnixxovyfZPOxy3EseOpubpUWm_zrsmXiGWvC-9Esqvo1a4iRp6tDdGYK7XL9p_zdgQbsLlkkSlVSM_3hPN8TDUHCYR5DStmiRer69sEcTYQX1XPy_HeWQsqG_XTRMDA86SG-C9Kj1ACEKRFqSj4Oavu5rSdFQ22CskqQS9OFz3aiGLadQjYAfkWeYfkAcktrrgBWO5_Vpab2s36Xorzw5FXWcvFO-t8LnWUU5bqO2gjAWgfJAyPqdvOi8tm5Pdk_aH4nzURhTyGASUyC1gplUXLI0LzsyiuQKvm8uYfgOEYPImyzxv63WSuPrriYUf9pKxazZAw8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
G4
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdbxToxSJS1MH17V5RUX37zu-it406oWJq5kAnu5QZb7MAZRCP78-0U15popBVWq2u4p4ZYJ1dQXozsvzACGD-3i2EPwh2JwbjnbiCvhMvaGaNbyPkVtnfBrwVDqxwnaWUaynVlI7XFtFBTAAmLV-CExN9Gze9gVwHCST_QMjlxy8_Orgk94_GGog5pRbF58KwqbUioQBL_fBHnQyFBrQtHG_rFLoYKSFmNQV9Wt0qCE-gjBKdK1XYGP9JzkL1NUt716qMJXg5jY_vfHpQ8xYMnKliSHIQwzl-th0KRyFOIcqxIH9-r93qVKMvB4a5HPHhgvHpPQ-L6VvzeZFpE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWy5-BW6jwjSp9Nh2iYnm0q8RPnKQSjbstSmJO1uwPXHf1P5s3udI3tqpOwQlmJYwnFjkqaMQL4cczQOHXZ6XRCsM3ceZ2wKuQhsXvLGa3LPorODwrhn3lV6xFDcPzUeh71QJyLau03yNZUVQwK15Ca8rxFbzYoPoZfwLCNvBRbQmVwaf1IKbiNUz9ZMQaYPxFGEkydfhBkdBwNv3hpSxM7NLp0DQV6pU2Lwmk3GP6-mbzChTPkdHxCU5aNB_Y-7GWIkP_AX8BEe8EIvnlBxIkM8cTTAgj1zNw59jiJ1KFFT6qm0CNOstEIgxJOKmxAGCuuzu1Tc-qVbU5DsKNWHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MnZ416rn7VhHTW7zUWEeiPXJuhLA7qFUsK1XcLo_Ms7WiQHUU0OshzGaND5O1lGcPefY--cdblFwKk79SwoddwcdPKCPdpD45rjKEwIjzHnGgD_VDMAerh9crgKu15zBeMnZXiGTBpI0bFyaLhXnVd7RZHS2lAg5Tecv1BrPCknmkdQ3cshg1FOSgn9wKCM9o5HGL1queP5YMl_aGvceW1mv8EyEo0gSxI9wzfMKtEI4GYVRxgjsUVJlsPF-oL0B6jQyY-w45Th2-o6hbM1aquLq8tMK6Qyi85vQU99KfhnJ5bXXp2grf9P2yR-Giz_JdyU5_S7SB1QyZtWr_UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT-bt18AY3Zi3bLQSrAub6QqldukgNJrSf6VcX1k9VU9FIayCALuVXzAYY-iXZNPTcMQ3HyZ2RVVAcM_bDJqzupVAEKlZUhOi0VX2SV9PnufKXkcD28jrlgFmXYJlFxPsH_AZaWexMuklpQnuKlD8bBiOgrf0w294BetCdmb6OTMX5UzCfmM5JX6fzQvDTrNvHTV3l56YEDfl2njwDcPHNFPIcWk7tK5q7rmjvr56x-NdVvbpomDdU_I-XeUQtOsP-UbourH4gECpETFhai2Ei65ePzeZ1LwPgTSBW4cmI2te2cgdKmKcUIcZX7lpka9PIdkzhxSp6wgMGwpk6u7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7G7hN8Lp3qEx0lwJy3DeQIonGI2IwRvHcXsLb7dQ0y3jLb_5pQ3EaS_C1awsZGxNXu2sVHsD_CbAmZE4brUyTVOkxD-rU5Mb1ALlZZA2a90MxcbKgzkCaWdQ2o4xdZIgj8fvIl1jcfKEi8ABw76yMTmcYRNxAI0hXcKowrd94YJeR2ckET2e5v9re0bVYbEs_JTkfdsKcgRQQ8WB33VScdNAvZm3kcaiYIox5WgcXHf0YWUw71_xEtufVeeo2ThhHLla1ZvjP3KXWi_V3QPCXutDiQDUnASK7Usb4fKR6gjAAG49qvg5LW0gB1XdmiC76cxxE0x1CScxq5-ZxMxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrHZLBxlChro99VWsi68qsxKgR8vjGUeQpcglZjLiuOYyZ6bg_3TsxB7EvAetNbcIHY0D6TUOOp-br1J45Td6GijU04VFC2lf9zPBLhhhMJzP_M1-TZcYggILWyhqDlAcGFpZ6o1HzZuM60sh8YR7hWGjclKQHZe5DGeCwYm7GwmMR6inbjyA6lRdz1bXqAwX7ZRUGZ6lbWsS7WnXlEPXnEffI7HjRPSWZc6zYhcZLDgOK1UbSHI4-BVJ1iOunm6yu8i1i-SxR8twfbyOls7c_hOHegyYa_IrvuADWTZQx7bmk54ADWoJxcBE7hg917B0YkYhvMT-MrQh4xeDRdE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
R4
🅰
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrABP3gSjzoHEgnQVwh3WWR9LCMqtryy8HiJFE_NmNlwxS_m4mgwCOli0E5VLd9rQ2GrBI_wF8eyVOPcrJzviNhWyoj_o2zxP1VoHZXLLR5Q1dCo4I_-tYkRUt4NX1Ps_K8X2y-ckhNop6wti82TL7THk4MvTuPYObSoanbIUxg-WI31iKuS13gqdjsGOcyWIhZiAovdu_0puYI9LnEoPs2rso4QIsnE2mGfuKQVS4rYQt8BrFpYM0xueG_b0XlnvSqH7jwZofUHj7rXIowYGa5gefCTreIIfhNg5ORR7G941C4uLy66cn7RSOg7MEw4lDVbA1IxBK0HTHqWSz_Xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-C0SRiQFdmSog2ujoL1y26NjFVvu1dKMJW-ej29oBv7vT8s0Pk_we_ozIQx3TbpgyEvH5ezMXPlpGPvYuaEY-wlqTfIq6aeXk8Vf2oydvfiZFpU6CVEDHJJO4ubezZoCmWoyKetJtyV_DvUyO6JIipWC3FUpiCkwVJIvd_DYeAtMmgCiQLqz6qf7zxW9O5vG3PFM-Yift9QzG5jYcGEEAV4fn-mdngDlS9WbmsPl1tSgVad5b1BXlI0JLwY5tUgzPML6be7AD-4onzpJp43HqpwVJmWJiv5ztbVeLxC6S4nPu1cGdEv2KpFi0tEd476wNMQ5-fFxDOviZVsNh-Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu826qeV28K0AZpvxY8MjE56OJvGaA9SqTCuP2OTgPGNA2gz_47gW9luXJnYNZnQvn0RTJ7TZ9nKqNZv1VshKkMYazRO1NSMYv1Xckx7jl4zNtS85lXn8R3-y2ArNPhlTrRN1ShRhOkXFF--f3ZpGhn7gQbArKcSciPa1yToj3Qu4GuLwwWWqW6BM2k8PkeCRHCKDhYG4RSNWBAvVHLnPhOjyuwxAm9SrGUBOrZc67zhvDvN8x9g4PwUzVtVngvjuBfYCcKW42iuBz1HNGd_KygB3EScxhXBbw6EjrflKTNrw2bOvZgtyxzh8RRgqOqyNMpS0pyRIeIWcFV-FO69yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaWot9fUFGATYYJTgKRlnskNTIyFerC53J9KLju2xCo0YZtpSDUfKkbB43kgYpjmT3CW6dd3vKN0s0btcfDFjjpS_fEP86cwiS68MbYh0VmCyCmubWlGVtAdeOWFj8UT_4wsmhs17wIu7J0M5RWMPCM90WWZ9gatPKCL7Ghs-NiHPwjXt55pbF-rqQs825PORIgwD1zhUsruA8JxY7_lhsjXn1fBD4qwzoJuHBtOmiN5nIHMGnDtu9al80o0pZsrQd_3y66wU6B6hsUDfPfMEiZ94thH4QN779ZRnrqOddq3RTqWrjwGtox0yvH82Qiz0izckpPAn8M8eXQ1WYjQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=qmVgS5aXDspVXW6BZmAzUdfrVISJvI_zaZBVXa-dSrUwdJW3PIrZO1INYou8XduKdcw1JMzzJK5TJq5vawmfnRJThjZAv5K-wC-WPRP7d8MLZnKCGt_MiJmEkaZpJStoL5-6svMn33FmAqNxRjyYHitujiqs0PtZXUa3gyRGbrTrs7-9byUJS5VwIsKz3AkPCpbhFSBTpI8LcuDPzrRVjVpj_e1Va1iLCLrbP6SV85pm64aVHvISDoe1Tciv1M3dITOeWAosluUuUfS5mhmohFWVhBghj9rpGqrmmlW-vERTjazxcQ0SVuB1oT-SKOt5uh0r8gxW5ja3PYd_euqXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=qmVgS5aXDspVXW6BZmAzUdfrVISJvI_zaZBVXa-dSrUwdJW3PIrZO1INYou8XduKdcw1JMzzJK5TJq5vawmfnRJThjZAv5K-wC-WPRP7d8MLZnKCGt_MiJmEkaZpJStoL5-6svMn33FmAqNxRjyYHitujiqs0PtZXUa3gyRGbrTrs7-9byUJS5VwIsKz3AkPCpbhFSBTpI8LcuDPzrRVjVpj_e1Va1iLCLrbP6SV85pm64aVHvISDoe1Tciv1M3dITOeWAosluUuUfS5mhmohFWVhBghj9rpGqrmmlW-vERTjazxcQ0SVuB1oT-SKOt5uh0r8gxW5ja3PYd_euqXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=jM-OT7bgE7-r6d5WrrVrSpWVLWxr-blg1ZHfGI-seGWlGFHFhDKNpmoKOMwBB8EwKK_V7PIYTyinvoVG-wTEaa9ryTQ1fO2R7QvuI43mmTyCdk69BJNk0xKDSORiKQGeLcLUV1FUgMeoCa07BBdI2dbAFsdYfcQH26KdZLcixxZ8xtHhsMfGK8YQQcgQhsyurNW42-JpQtXeXxBJOaouD1gk3qBZUQvgpj2spBWVeMRl-KpenAjQkzg8JIihZt0j-WlUfMpD64V5UR7u-42VNqYwF4s-mDsEQ7F-p6XQ7wf4UuzNKVOEVVLlVH1ZlQ8AG5F1bQwV1YiajPA4-QZcyjeCQ8vXtkfyr00cU-X6u6BuO6X8FqPeeNoy75pAbwncl9LBGonbL4hw1hEkrYFz4KAxpV7oCEc7feWMkQgtuD-W8uTL13IfEloJNQVrhNsipH9dmzYbPmgTmo-LuXSOdbk22tYfQdJ-7fipEdrD5uz5gafhXumMCZaO4H-FTV-yXuvCmzB2jviGwb9zUjRxIy6ZEi7oqjngPw1vrrGOE-mz5FWVZGGoCnlLUk989cBUA3_bf5d6vboYLn0x44gJAXVVwW6S-FvTedKb1Gv47Z5Ak4-VqhYty_1OafNE4_v8KWh57zhJA78E8-rDjbCHq8xWIVigte8ucmQQTQ9x4Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=jM-OT7bgE7-r6d5WrrVrSpWVLWxr-blg1ZHfGI-seGWlGFHFhDKNpmoKOMwBB8EwKK_V7PIYTyinvoVG-wTEaa9ryTQ1fO2R7QvuI43mmTyCdk69BJNk0xKDSORiKQGeLcLUV1FUgMeoCa07BBdI2dbAFsdYfcQH26KdZLcixxZ8xtHhsMfGK8YQQcgQhsyurNW42-JpQtXeXxBJOaouD1gk3qBZUQvgpj2spBWVeMRl-KpenAjQkzg8JIihZt0j-WlUfMpD64V5UR7u-42VNqYwF4s-mDsEQ7F-p6XQ7wf4UuzNKVOEVVLlVH1ZlQ8AG5F1bQwV1YiajPA4-QZcyjeCQ8vXtkfyr00cU-X6u6BuO6X8FqPeeNoy75pAbwncl9LBGonbL4hw1hEkrYFz4KAxpV7oCEc7feWMkQgtuD-W8uTL13IfEloJNQVrhNsipH9dmzYbPmgTmo-LuXSOdbk22tYfQdJ-7fipEdrD5uz5gafhXumMCZaO4H-FTV-yXuvCmzB2jviGwb9zUjRxIy6ZEi7oqjngPw1vrrGOE-mz5FWVZGGoCnlLUk989cBUA3_bf5d6vboYLn0x44gJAXVVwW6S-FvTedKb1Gv47Z5Ak4-VqhYty_1OafNE4_v8KWh57zhJA78E8-rDjbCHq8xWIVigte8ucmQQTQ9x4Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqQu6zroLEr6fisYIy5l5hGTe8chiCYf7cTIFgvEIACvB0sgyr6kyH4AH9Bm9i7TxbSoAizGFkzWVDra1CekjRHFJXQ69fEDYbXoh7D8yuz9iMZMUkQywb5BLDrNVzRculKusSxYe6M1_8Ex9KtSuI6ALhLFbyXnVUsTM9k_FF3z5GGaJ9p919oe7kADPsuA730DkSz74gfqPxo-9S513HmgpY29IVNJ5mx7I8aSvvjn_ehXVXhISCMfHqFI9J4OXA2YrEAF0Y-Kw8YqovBlD0rVqAm2lEvj5xWMubRK6lUI-GNuwLp4_81XzdaziP985f-oToPJNhxx1k3iHr9O3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btOZfK8pKQiiFJmVG29CF9PMBZ0c2GzLW5JI5r3L5GXGROY3rO_lVYM3H_c3EebOFMNeXdUyI6PsRSttO-mN02I8_CQxRw9xw-25_O08ed0gzZBTsYAqmPUAXyeqtxZCMM9ygBDUVoDuz3Bi19K5gRHOnf1EyB5Tc2DrkeEwD8DIafDKdJAkOOmq_eJN6iTGlVr1IZD04JoZfoxQbow8FhIrd2FxtFkQWn6fNzAClmnTBavd7msUgfDQcrJPc4crM1Jh2JfuDrazru0TB-Mcx9qWktH4VkQ2vfaING1QrfxwEdAjgm7eUIILbsE6y_o3Y8zc443ynK6db9osh0nCTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
میلیارد ریال جایزه‌ی تورنومنت  جدید Winro
🥇
تورنومنت‌های هفتگی و ماهانه
وینرو
رو از دست نده
🔥
جوایز شگفت‌انگیز و فوق‌العاده
🎟
⭐
بدون محدودیت تعداد شرکت‌کننده
💳
با مبلغ ورودی دلخواه
🔝
بالاترین بونوس‌ها در سایت وینرو
🎯
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
ضرایب ویژه و رقابتی
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش مسابقات
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
G3
🅰
همین الان وارد شو و در تورنومنت‌های فوق‌العاده‌ی وینرو شرکت کن
🎯
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=pjV_usCQgwbhkjQx2fAJ7p8RggqBGimnOEMkFpP-fVwRhA0xBX9fvnEVahgxTXGlubG0REZ0Y0SvLhAE0ozW6rz38vGAAn8XYr-rPUq9IV81LFNAzFQJ7gEx0Bv5RGynIV53s99gkf1PvwJDt6XiYFvrDgXCyt9kPhehvzqIQpESSo9y70MNQESGlxPdWNBPU0i2ZPP2amSOluP2ibcUHwdwTLs3y5Ql_ic_iQSEpufeXO6t7Me0l296LA5gwrcYS_BZrDfuNHchArH-f_c214CxQRI81X-lnBENUICuYxGmNyumavvOBicx_G-7KJAUjMiA5yNCVaTkHswJH-Lxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=pjV_usCQgwbhkjQx2fAJ7p8RggqBGimnOEMkFpP-fVwRhA0xBX9fvnEVahgxTXGlubG0REZ0Y0SvLhAE0ozW6rz38vGAAn8XYr-rPUq9IV81LFNAzFQJ7gEx0Bv5RGynIV53s99gkf1PvwJDt6XiYFvrDgXCyt9kPhehvzqIQpESSo9y70MNQESGlxPdWNBPU0i2ZPP2amSOluP2ibcUHwdwTLs3y5Ql_ic_iQSEpufeXO6t7Me0l296LA5gwrcYS_BZrDfuNHchArH-f_c214CxQRI81X-lnBENUICuYxGmNyumavvOBicx_G-7KJAUjMiA5yNCVaTkHswJH-Lxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2OWy_kfOIWbKgv8CHIRUROqpJfaYKjG0iWA0uVQIkqPlROK3IcRVOuwQ2YlSK1rgdOARTfec624tkzNolidL-rjz_HRuUHA9W-7ItDu2iCwgMOamtxsL_h7kmsSOzyRp2hNXh7tBRneE-W-Tbq7Nq9pnvz0959BBW7pjCny1EO2z4c2_VUDUR0wkXiWolnUqEdNKIQF0YGeUMG-N-QDOo7-uyTgCk26E6Vx0W7LHZQ1uajcx4HBn0U2ap9tkNuZD9-9Mm_gC1Q4Oheqf-vDrwAd3MvK3AFcnYYlGTM5ZEEuLo9JVBQ3s3nFWeKVNzsdjTEvsVR4l7RqfwF1G8nTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqSQnEu2Gr9NC6CuG5bKaEpvM0z-eI409z-ghfJdLnSlEOgqwfZAcAoT8gnbj2L4ojOMk-4PrAIvE_mVaBSLxGkxuRsL0vG-pvW0HkO1n6IrLxQ2oD252fYfB5xjXzIGIYj0QGxYjU1okPBs1NCfRfSL_NPvz_f72mNDLT9MDLoHyUDyzM5uklvg-oGt3tTaCjry5w9wgA3VJfc2f5oFTdW-2RhSPCsU_KBe3TmKQqsScUEwAHmcjPqmyNPOxKLDs06076_1AZQzh8rKXdmZmMfQlMDFSJ55qKe-v-88hJOjpWbK6_KqiJDIDgEJsQituWqtE2BSxGxz24_F8HGy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP87FQEIk4onZ2oftDM4JMJnnO1BsugPP3zjJss1b2h7I6Fx3TJz-qPvG_K1svDxLV5r191rqzIVeaP0GyOPDgCgJ42iL2BYbwD4gmEx1cRrBeUW0X81zggdRJAvBmHJGKs-9XtAwRTrIkjEgOd2HD02MFLjeqv1WOlR0J4gH_DywxVqgJoGIZ_wSbeDv7caZL2GsP-XF2aW0PrEuPCxAKYPYb7QsnoF1TxB8zfT7aidNf5UuhFBxtx-oL0tbaUed-D74pw6dsNehvF4Bj-DjAgMj54hO59XjamdznEjw_1CneUfF_sCkRBTYyjVTKwlZc1tXHjTDRpMKk59pudLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9uW3A1fr13uHpsclranDuh38P5SwrY5j4Pz1E88ITgdro21fUqCYJ13VFFM9q9E7Lk8dscuao0ZKPFEbVAmITNdQdeU4I2It4AGQ_l_fy-ts9B31gCPL0CBgUjxvRu2JeKRBf5VwyB84JNCd5sntb8YxJInaRxI8UXV581E3vJHS3eLbz1AYkV4wWWHjlGQcb8ELFDeEOhp6-zCbr76eotHcYJ89uBUhAzktmMr97L20STxXE4ffLXGWFXoMrOsL2yzSMiH7f3cmM-r02AnXBB51T3le52GGG9LKEu4gSvprYwT5Pllvio8DDLPOXNoe83V2WFUUICIKnc_QhKlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCcsZY5PZwowu5YxxEz0TAoPWrs8wBVLyb4sHqdOb-LnYqsH6Yc_Q_vP-J1S8qfCBQSWGeM0GMz8nYOi_PNot1iIZia213BMidqmszkMZoEwzrg9Fd8orp6C_gYHjW_YW22WgO7ivd6h0eblNXg9d2i67AS0UTyyskchNjGJy8HQeCoDm07xfwWIhX1IiecJ3h_zVp6yDkOukO2xP4W5EjNQKvnGKVwxGF3Ni8df587Lx9DjPbdnorVXnledt895lgTQvdtDHlFY4QTXtbPl8Phfmc74hCAJI8_K4-lo5nFISGT6Me6GEp2z6ZQjZPdokUuBaS87ACfsyPDvxeCiJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUGSDe4KkgbAGQZyKhfh6qkaEvOrJQ4lU1kRXj4mmAre26m70EkecRs8NBtP2suLEmfB_03XgShTGUCoCfIQs16DlXZdKOVWjDIbEqFUjFlO7ovtaOqMt6jielMDtartoELOVUehGTrYB_xKkjg0IRiO1-1gvvopttowcpou-OvhFzN7rj5V4TqM8nMegBqhZIxMN4AqDHwdasQR8UIKNCqOIc6j0ASHhQfzYoKiR9HX1sYcgmQY0nroSjyigNmIJIrL12Wi6hOWi78-BBNjiu_xCt9aU_cLskQTAq4St6C0-OrQhOyWIfc0R0ZXEPdtZuOcQF3S-Sp9FJkl91cXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R3
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6poL6cUtjC8RHKumesLyLQsPDO-8_Q4QkTpIKZ3QR4ZKAEH1s0UOT1OSQV3nvFac5l3jp9GiTwKjb6T6Ta8uAcBrIYF8GrZB6PCnvqIO9m14oNjZzTaQyvAHxIuCkfZTEagK1Wbo4WUPoQfWpTdetgSbDewl9YRyfHXe5OPqxIdMVlmPnsY3AKNvnDXLt2Rt9lfszexhIhDrejnvXVkJIW3eD3nQf0c7wZMC8N2ThH3I-btiExXOm1bFsSjmjcUsBdsy2TpGgP2C3SwBXYk_q-Zo2Tozsu4mC-oURk2Q_wW3lJFxgG8rb2n5HHCxPEhmmF_GE871DcNr3Dpnn8NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=rFf9XU2OgeA6XOJIU_siw_hK_ivjAkxsqYXiHsVnfGRFG8i1sLBdRoGJVlAZydJasPx-bP7AJ1PgusxCgBEk7xCYvaFsoxxdKmw4FHwRKmKjtqqNUoZJdLUjyw5GTm7zT8zJyez2NTUEQ4GeCMlmf_NXQGnCRkF21a1G7PYg3MuM9_JWA2vwtubXh9mi1u6enZUF_E1tstKBWjSPrsVywG9iqGl9ryVyv4k17TmFewEXCn5I9n_dqdbMMoJaZd19LttgR70hNSjmXqWUZo5kZgbEZWxYay4Axpu64eys_jM3wgCBc5CG7kbBFQ7jJ53vfwlx6vlrgBFeUYA0kfwrhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=rFf9XU2OgeA6XOJIU_siw_hK_ivjAkxsqYXiHsVnfGRFG8i1sLBdRoGJVlAZydJasPx-bP7AJ1PgusxCgBEk7xCYvaFsoxxdKmw4FHwRKmKjtqqNUoZJdLUjyw5GTm7zT8zJyez2NTUEQ4GeCMlmf_NXQGnCRkF21a1G7PYg3MuM9_JWA2vwtubXh9mi1u6enZUF_E1tstKBWjSPrsVywG9iqGl9ryVyv4k17TmFewEXCn5I9n_dqdbMMoJaZd19LttgR70hNSjmXqWUZo5kZgbEZWxYay4Axpu64eys_jM3wgCBc5CG7kbBFQ7jJ53vfwlx6vlrgBFeUYA0kfwrhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u46e5L5OupKFEojVP9vELM4rErXZXsrlcpG1Yebj-i6AExA7MWJR791hNi6NZIGPWNa07CB4jXiG5tUl_YcQ4q-S8cwjL_Z4YIRBmgpD20d_k7416CVV1sJgQoQXOu37lit0cqDPQSX_DqvF64FP-67M1PxzH1pPQriXV0hRHfR71sldMof4AVkJ457xPpOYrVu4tQwNUYpQGae3-FP3xC-KwHvygW4QpV_Lo2gYRff4NWVleWMCO5bDXD_KO2od_59Q0x_2hYy3izTErjypBo19JS3a337Rg5jSC-fpwHYLKmu4cYqkzTwo1WK_G-_F7uifsD1HMQ2Ic8CUFjimRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wobf563PucTVfZDSXg01J83RGgOEcUTGDmALAc2FiFOU5Y9ebDkqgOf1zsEVz5l5wVttu-CJOsJm_roEFwBagt-izwqkn2ttFhBFwzuWJuY6y2fi9bVUpqgbYCiOWTi4S8mv5K2j-S4BJ1_W29uak4SIKtr7GhIuN8Zw_3zhKRDCzoaiUm907JJUmHGKQixSmsvMFrKTOhppzi9hXnN23iyCWiSSSvNDOsrmWnO-wcc_1q77_HIrU0VZVVzgSqq-I1Sgi0GSsrOFKyX73evZcrCQpIn7Uyso_lfCYGr1248odO-kUFXrYHsvito2DavrcU8p78COkzJDbDUPU-9VPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOaSPmReI_T35ao4jxbumKJd1UWVG909uVLCYr4-LuqSGHjqHKuFoSrs9BrUsGWiKJ6K5IPSMdo_g3iNzNtLEPrssIpZjnRDpKnKGPs1fL5XShnwen4YUVtj_Eas3M3MhuGDhTNydhqecNv_LtPdNCkiq8EoNUdv90hBbWuaZXUsl_CrtSid1xhESn2zuJTFoPK--WVONLIdUhi3JJJSVaaPBPWoB0YIpgw1VRQNEcD9tCYZ0zrNtFlDKgnrFdt1cAfbXQ63gNtYoOhqIZVuqQMc6W1ysR3LxMlg7gxhF8AB7k2PLbQEgzF6WnXGjF3a5oleBBkwZgP_cHn0-q_9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUl8hioyH82eK9nE0DksEXZiohdDNibXRR4ntxUCp9DIlpPC9YfEtqpb9g2Sqr0ZCwUwB8sdmZelO1g49ua0pAejEt2v1fVJjwdHz8q3qnB25TdMS0FpyqSYbQZUCCpWVCOfkMcVelT52fwsE9KHvW3AxNhQuf5PhNXFSl76wYe_VoDlsMU4lxYypBoql8yxedsiWmaST3Zw1RrJZctX5F2dozUeyaJOX3BjbvoLUYEFVKN62R0tMoFZXxirenRMPXxdsOruOy-6Gc5pviWZlUYiS-pdYz45SZuQ_hHVnxlZm24d-zeNG4w2651w1_ho0SJIVOVEtna5EfzvODRaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDSxNFfMxHtwjikBEsNTU-1FUBkQqUKOiG2sXKggWxMZbvHfqLxlc2thiuJUuzl8BBMAtDGLPJdY3K6Yh_1p3dZzoMvMLTaZPs68nFtIPMbP2PspN51nGz390ZfSm7rDd5GV1hmSztCmU-M5bYTFVPq7EKwoZinLqlMKUVwcU16LtOokXUis0zHdiptMyF1XDs8tMxOKFdzZ411YSghVZDLSymkP-ZGU0y3kFux74Kzvw9AJ_egiWJJdEohqwj5r5rQ05afUx39aN_7Js-onizbgMkfWVx8ZywZuy31iv-1AcM5OBc0d6PISQTkq7n3fkT-39ppEZRa1xOcdsW55xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=h26STn5rjqFu1dikYxfSK0w-sg7sD_RIPjVjEjr7kaTpUjBI4UJ4U-B11uNWyxWaqIMNFRH1qnECbPeCdX_YkXPw6Pb3NAmpP3NdnAMcprR8y2uQcp3xvJx8PphotMJ256mp0yQDF1CPsbNtqseAB50IX8RuJyf1Bhe7LVNoW6hiq5NQW71g7PDaG1YTT8UKbb6RT5Vh9NUmo-G5TmgVYXlHJlmzDemclGOtvoGGqSKaCnQBLr_JhUVVkaWjPNFkVC6fI5_cCGAfuFjHr31uSLAIUVKmHQufotS9BJBl480tBM3OtnWQdhoYOt_KgmLtJ0zTJko2HWvWsLo0vdvZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=h26STn5rjqFu1dikYxfSK0w-sg7sD_RIPjVjEjr7kaTpUjBI4UJ4U-B11uNWyxWaqIMNFRH1qnECbPeCdX_YkXPw6Pb3NAmpP3NdnAMcprR8y2uQcp3xvJx8PphotMJ256mp0yQDF1CPsbNtqseAB50IX8RuJyf1Bhe7LVNoW6hiq5NQW71g7PDaG1YTT8UKbb6RT5Vh9NUmo-G5TmgVYXlHJlmzDemclGOtvoGGqSKaCnQBLr_JhUVVkaWjPNFkVC6fI5_cCGAfuFjHr31uSLAIUVKmHQufotS9BJBl480tBM3OtnWQdhoYOt_KgmLtJ0zTJko2HWvWsLo0vdvZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrxXhS2Q2ZuzTw8VzOQuTQmMx5Uk5r3xEG10fE7kSr9KIDg7iXytXAlluazY6mMIE4zAKYsoxGhnUGreMJYWMmJ201Ykgyvt-H04yDiUl3xxCl3_u_GxNm_NEXna1bC8xgYu7HSJvT0_54-7KVmDrRzg9ktGp_KDz0ll98anMymUXuEIKuBz3QAEOFxrSJCppVrjqgy6xYOK_pvZ-HftJXQARMOjgdsjEzmzg3uI5Zhbl4poDPam66qiW69J8XGxhy99H84sDpDecqzuuZMorEdjjD3QoYv9WEY-lo2D1ma5tVDWklos1rReZND1jGkfLz0HUgmMRtZ_ctNY1A2pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCXYcCQaieMCz0UnBAefMJilybZNZE2R0qxfmI9rqK1q_JtQzH45cdf92a9bHK7qr68yM9gJTQNQU-qpBul9pjU8bsvteaSIHkkHW48fdjWDGuWaYkOLQV1viJRdJfaxJl7DkuuFPJFpV8TwUgHtaGIT9siGvNUA1gXRT9Wy1tO1es8zJ5COYxhNwabGr_UK6AiZ27IDwUio7uMtOiRDWKBXjql6MLsHavM7Y15-lfBCxdLSmCueED4KhJlmOyTWtG_vRN9k3vB1rDh8GhxsXegzogxgetjZwQEzEAD2qI2fhLtRzOBw6N-B5lJWGdLTam33QhHDkeE9jcEXU6w2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
