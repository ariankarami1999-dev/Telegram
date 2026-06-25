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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwihilxDqZGDb_hjO5Hb6uGpR-fe8b6GkCqEcYzEr70XtrAOJNIVtMxbZKfq3rgt0QC-lOSeUd9onGfTp4uZTJ8v4PgvXBR9OLl-Q7XuhEJxTHFFMqeJ-TeHL5ogFJZAzEAQG7ZKGkYUfbRvdkA5EjtpP2N33POGfGmfY4_7D1fGREhNv1MHX7-ZbFgbqbsFMn2MgVHJTJdwkmd9AhCPUYfMECEWEIeJ7tJMdkT3F1HyPjzWx3wGO7ChPxplFQZxTUShrOXurxcEobtWu6e08kRIEZoS0jfiYq_UOcf6nvfCiA0s9bMYTD6Cf165kw2DOoPWID_DyqWfZqsRrmK0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqD-gwNULJXquTYnNzEXonr5GAolPS8UIO8J_9r44Kmgh1jST2p7vU9bgOXFmnL0UsEgp3Lh5FoY9wfQIM7Ad9IM3wfadIGKcDXYLNL_Lu2z2hcxRtfIPRYyaMoDgg4QihyruAlIoG8jAwtq0n3DTxAmzGqszpzcBB_i9jJPzbzVjfXhA12FxoGg1GmMc7_CDyf4iXMmtIh10oc8BlOu_jSlWj-3ZN4stmn0Q4MBDdvX7DorRxy4wK6cnRKfk7ZN8FvftNmFV26RJ2PyFN3BBHfzXeC6ecEDSh0kLHfhMjvCau_j9U338IR5sLqy_URtxABQPxzapdA8XClN7e3rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdbxToxSJS1MH17V5RUX37zu-it406oWJq5kAnu5QZb7MAZRCP78-0U15popBVWq2u4p4ZYJ1dQXozsvzACGD-3i2EPwh2JwbjnbiCvhMvaGaNbyPkVtnfBrwVDqxwnaWUaynVlI7XFtFBTAAmLV-CExN9Gze9gVwHCST_QMjlxy8_Orgk94_GGog5pRbF58KwqbUioQBL_fBHnQyFBrQtHG_rFLoYKSFmNQV9Wt0qCE-gjBKdK1XYGP9JzkL1NUt716qMJXg5jY_vfHpQ8xYMnKliSHIQwzl-th0KRyFOIcqxIH9-r93qVKMvB4a5HPHhgvHpPQ-L6VvzeZFpE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWy5-BW6jwjSp9Nh2iYnm0q8RPnKQSjbstSmJO1uwPXHf1P5s3udI3tqpOwQlmJYwnFjkqaMQL4cczQOHXZ6XRCsM3ceZ2wKuQhsXvLGa3LPorODwrhn3lV6xFDcPzUeh71QJyLau03yNZUVQwK15Ca8rxFbzYoPoZfwLCNvBRbQmVwaf1IKbiNUz9ZMQaYPxFGEkydfhBkdBwNv3hpSxM7NLp0DQV6pU2Lwmk3GP6-mbzChTPkdHxCU5aNB_Y-7GWIkP_AX8BEe8EIvnlBxIkM8cTTAgj1zNw59jiJ1KFFT6qm0CNOstEIgxJOKmxAGCuuzu1Tc-qVbU5DsKNWHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MnZ416rn7VhHTW7zUWEeiPXJuhLA7qFUsK1XcLo_Ms7WiQHUU0OshzGaND5O1lGcPefY--cdblFwKk79SwoddwcdPKCPdpD45rjKEwIjzHnGgD_VDMAerh9crgKu15zBeMnZXiGTBpI0bFyaLhXnVd7RZHS2lAg5Tecv1BrPCknmkdQ3cshg1FOSgn9wKCM9o5HGL1queP5YMl_aGvceW1mv8EyEo0gSxI9wzfMKtEI4GYVRxgjsUVJlsPF-oL0B6jQyY-w45Th2-o6hbM1aquLq8tMK6Qyi85vQU99KfhnJ5bXXp2grf9P2yR-Giz_JdyU5_S7SB1QyZtWr_UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT-bt18AY3Zi3bLQSrAub6QqldukgNJrSf6VcX1k9VU9FIayCALuVXzAYY-iXZNPTcMQ3HyZ2RVVAcM_bDJqzupVAEKlZUhOi0VX2SV9PnufKXkcD28jrlgFmXYJlFxPsH_AZaWexMuklpQnuKlD8bBiOgrf0w294BetCdmb6OTMX5UzCfmM5JX6fzQvDTrNvHTV3l56YEDfl2njwDcPHNFPIcWk7tK5q7rmjvr56x-NdVvbpomDdU_I-XeUQtOsP-UbourH4gECpETFhai2Ei65ePzeZ1LwPgTSBW4cmI2te2cgdKmKcUIcZX7lpka9PIdkzhxSp6wgMGwpk6u7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB-O3R4PMHMqBdZAQvaLssK_tWEYp0JoTgX850_dUYYKDWdUyHPa8qKEWpaBW66BOa3h1pWYH324fszfsvBYlnt3EYSgmt0cH67AHpCnyhYn4edg00R9a85lkpi5ENlcdw48ArJN50II-x84rWfon-v4MzE8T8EC7QMa1tH7Y6_7917znK1ojS6JBhTMzuwSsIfbRm9Rwt1bRKmhRhARGYpQ4GyGBS4ediLBkGXniJr5rVyxwwDAuVKMUHI360QTA3y6759NqhRI0g9kJLrE4ebr8um3w9oLfAKxOXYQcddqptgGoWth4l5bOEvcRodc09xTLev0Xge89PfwkU53aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBZfgYbufgyDXGVBqtyLjPD5ksR7mVdF0eL7uZ9-FNmoe-vR3FkAbmYVomu9xjs4Wjhzfr-xeqdceTI0dm3mw9nB3f62BPzAMNRnEiNbHc32Cg5S4aPgAflwcO0teGGt4_FymXQ3tdV8VK1FQtraDHazW4hsNPmEVDyHG-LWfSusy2RZ1Hp0srxuKl2IO8BUOrm8LqJ4r0jaTKU_Yx_a-qNGa-53KJAyyu_9Hol0QzQfDsxdDdD7x9npdJrAPNJ1B31CVUP1om8iQM44dsQSua_QffEL3PGCzK3bcpH5M4eM5x_xMtBAdhlbX57DN_yubNSF8NaLHe51VK9GK73DfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuTY8bQ3CyuwQeX8pFhiZ9OwKlPM4GcmnW9Aydbk3htl07AE5VZdK4ecCSDJFks2hvOr0R8KnknaV5ymuqRB31FMoh3br-l2keECbwVRHko8w3VlJb77X4dJxbQsf2cy4afIdDoUsQtUiyKd4iIvQwbd69ly4L16_pHVyofn-3Un-jSvXWJRqlPKkbEYp7ROrICcCFnImBn-x6mO8U94a9U86xuk5anUhKIcYxPJVRYK_Au0QJJZ2XtK51YyjEX5KbBKdRWHVSpYbqF6pulbqfPw4TXbYZ8sBbegp6ReePLXFvfdC89_lcD5XP8Hx-Gy6S6JHtmTQPsz9qMn4nNMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4dMt8BQp3RWbXAu1o3ge0SChE1EbhlYjAZe-9NEbovsh6ccAHxEHgaETtFiOvIpUqLSHvI4rBo1JmJeGLZsKLCgcP4RCU0ySljDHDE_xmM2NHBMJDhHlt31R3FWCaKoLmAg-RXCF0RpTGlfPqZq-59F4_C3CdX9ppIgI1dHM73jdVD2XQS8Y0ErOehrQ8kr8ZzcMDI1t8cOIuO-knJAieI60Xtc-NUL59WbaE1IdTB7WqtzNS4mzIfuE5Ryw49RdKcOLu0F3b-SCl1zh3xJIBA0iaPvEv-KPXUjiGAn8pg6E5RzLNk3uZr5fKM1y5Shp1waeKHxWZbsAZMWiQr2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4zqi4WBUMs-7jc2LW4yJiDUbMJHkINyfJA9qhr45S-ICltwFn5VhPmRKOiigmXDOmNEdMncZZhyGVZ3zg7L3D4RB-qwsV3R91KWOTilC7EPVO19lvYqtJhZFYLPGHjwcTge-Y0D89OOcndMZhEPDA3v8QiaJC-3c3eMo8g-d-o4WvROiDGemzV6-EE1qJiZvB50awBxmENCHib0hbTFq9KHXkR8PTBlpaYCt8lhWduzzgu2aiqsKp5vF4P0Wp3lgji36FIOOdLe3bBxrIzapNJW-MtQndiicPUUnX-OGiq2k_p2yTSuDTfjyqdp0yI38CHDQEYPOf-zsyB9flDfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVBOh9JmXunvEfGRrboSGYMANgu8YOmYGaF4MGObQ4efgqHcwvqvniIY472ppe-wWgjM-MLP04vNgQx23QSl30Tu4EgfZAjPiiCZAcf7ci0rKyWFL4xrKrq9_H0vv8XinVLPeWiI3emarUypsZwU9Gg5pNly5Wp17bogDxO2hNDeJEH90KDP-SYGy0n-7tEcsRx0eNExE0mt0WRxgs8RE4v3GV3YxsYCdVf6823uZ-jnRJQkfzH3Qb80Bu_HLk6AtBB90oTeq6FvkuW6uYaIofVukVwqLgXizz50g7CNukBnt9V7ymwVxY8CHy8SEbdBfVhDzeolPxQUxDZck7pgug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=vz1lgEG8iJM7ehXUPN_sP79pFU-fVsfUN0bNfD2eE1zelBQ3w4YVDEGw6fv6ZiPQW4nkc-dWeKPzc5H--3L6YzOECNEe8F7ZmP4UUxivJM26pcPnE36dl4VEtT-0KQm44StFGCSkijWedKURgxu50cCIIY-HWXz6XS6A9MdDseFGxKHvFfWYMfJJ4FBCcYfEi483LAb_OCs5uZbkVLts2QZGQSRSDD7k3U-kr6GeFI6jXImtLCtjXpNklfIM1j47TCTDXJW2Tv8saw4PpxTXcK9J3Hw3Uwgjhp91VB1wWL4Vh8cROt-UByr8U3BGta-5ZqRnNaTaYJLL8NywxhZAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=vz1lgEG8iJM7ehXUPN_sP79pFU-fVsfUN0bNfD2eE1zelBQ3w4YVDEGw6fv6ZiPQW4nkc-dWeKPzc5H--3L6YzOECNEe8F7ZmP4UUxivJM26pcPnE36dl4VEtT-0KQm44StFGCSkijWedKURgxu50cCIIY-HWXz6XS6A9MdDseFGxKHvFfWYMfJJ4FBCcYfEi483LAb_OCs5uZbkVLts2QZGQSRSDD7k3U-kr6GeFI6jXImtLCtjXpNklfIM1j47TCTDXJW2Tv8saw4PpxTXcK9J3Hw3Uwgjhp91VB1wWL4Vh8cROt-UByr8U3BGta-5ZqRnNaTaYJLL8NywxhZAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=oLBwqLMGiHlfoQWNXRkmQCp4IYcKjQhnN-iFDwz1F9oWH32cOOr1arw-mZQv2wkMJfXQXmmJSg3bCB2F-Pb_0Fst8pGUc4gNyW3pNihjmNVqKACqQsQbKyRbxn9EvKCMcrcxXUDB-Llkc54YkIep_SvDU-8nhHrpRb8VW7ON5TrNt0FSlDzvDy-4nwpIzi1IdUw-AXxopVlxMk08NPdKBLI_9iAnfl4JZHqIkQT-W7fZA5sZFOe5uVwBv9U27RRc5BKPvkm7vvCGYtVC4myyl74XooJ6VBRXgpb-VuuilYfYskzly3DVoDd--Rz-EZCwDgJo6P1_0msfkYZDHTRAL5XdURUjhZC3Ps4dwG5RE0GwUZFxjKIqZubndIC0VkT0aQZ3goD_DQJC_0JllkjDu5fFlr9OGaEimxf9gddR7paH2Acclu8MABoE2XP9TfIG4N5omRm_-5XBGWXxdc8kEx7KYwvpI8sq3cxvqtohFQV6bB_T092Fd0ivunSR1NZ_DXriOGiSU3HRKlpjCOzJ2z8fi5Tv3XfBXzRDWzO1LQLSeE2SsoZQSPA_Z18l0jzSjZ9GwSP8KhdYRlgVilxSbcPMRUnDfu5q0AvC_V10ZlbgqXBBoWtz2ELj5Ybthb2snz0sQPinZwaxcyca6YvWHf-GojmhgSu1UgsijIBly30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=oLBwqLMGiHlfoQWNXRkmQCp4IYcKjQhnN-iFDwz1F9oWH32cOOr1arw-mZQv2wkMJfXQXmmJSg3bCB2F-Pb_0Fst8pGUc4gNyW3pNihjmNVqKACqQsQbKyRbxn9EvKCMcrcxXUDB-Llkc54YkIep_SvDU-8nhHrpRb8VW7ON5TrNt0FSlDzvDy-4nwpIzi1IdUw-AXxopVlxMk08NPdKBLI_9iAnfl4JZHqIkQT-W7fZA5sZFOe5uVwBv9U27RRc5BKPvkm7vvCGYtVC4myyl74XooJ6VBRXgpb-VuuilYfYskzly3DVoDd--Rz-EZCwDgJo6P1_0msfkYZDHTRAL5XdURUjhZC3Ps4dwG5RE0GwUZFxjKIqZubndIC0VkT0aQZ3goD_DQJC_0JllkjDu5fFlr9OGaEimxf9gddR7paH2Acclu8MABoE2XP9TfIG4N5omRm_-5XBGWXxdc8kEx7KYwvpI8sq3cxvqtohFQV6bB_T092Fd0ivunSR1NZ_DXriOGiSU3HRKlpjCOzJ2z8fi5Tv3XfBXzRDWzO1LQLSeE2SsoZQSPA_Z18l0jzSjZ9GwSP8KhdYRlgVilxSbcPMRUnDfu5q0AvC_V10ZlbgqXBBoWtz2ELj5Ybthb2snz0sQPinZwaxcyca6YvWHf-GojmhgSu1UgsijIBly30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3NckOhPYAmX5O7bZ_jY_1sz-LSMhzPKmTIVjH0YqfDdxt7OaW_yBSuAGMk6zDs1D0Ap6wZI_C2iEsRKKjdmHMP_ZvCqvrjIR01Te8SswOnJ4rPVBpSvNxnERau0cKoCAS4JVsKiVWhhytoeMpMfG8SXQEonsA1esBUgGeGTn7GhnybjZ5e4F7vlZprrCiDG-MM6cRsWc7vYHMTJzIt0TtYowpmltplIkEDP0zggkTAbLPK_jVLaodT9YYBa_WQuFD9aQh0gm8rMF5TaWSVobmtNbHGd8amINY7htknxGzC1bqaUaK7VLhaSu6rLwr2RSXgrlMWoneQg3_NN3dmpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S62u0TmkCyJdxyt5wsdp5Rr8pJrcDKlP3fZqsbYmH2emuSd6yju4khl-7CAWhGZCzhRTL-_LnnwzDlhjvPGZspoU-GznWQCPm8bXO28N2Z2ZZ9B7iaqsfSAOrEdTeHHqbFDmCDuvtyjzgaIRJuDt8_fS1Qv-8fHyJb-g8dWU2RkJsWapNXXA_qpVdzCXAN8uM_1hIGMGAXIhvpoEKMbpqfQaTWCS64Zg228XcAdlh4kkOT-Lzzo9SMNV7mFm10lbEdNaEoMt3ct3pZWExIpqlRufyfnCzVXXmIGN_D6SRDTczUqIiypbuD2he2VGQZ_z-700JmRnZ1HmaXkANV4LLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=jaJyrJvpfRlqz00cmhgPYysG5QshHOKYMYhOft8f-E4pKZjLgwWcD6JSQAFkES17mxJm2833Yo65O17lBS-QzaDBkgaVD3pSBVI_w86C3e9rQzS41EI7N32es0sYaup7DTxDQquqJOs1WcxEMuDCwdLXJ4bjuVjzIR50yXwu1fL7yGNQTyOYTLkeKq8mpXRUyoboI6w5Zm-m0riPOnEGtfSuJOmn053BUCX7ip6fSZhUBtaxNB3ssRc8qsSc5gdSbgGfk28bn3lzYbVPwnkgoPfzR2U-n8TjLhoLnh7mJwJPmxHljxbhL4xUuoXmUGOoWOFMiWDDiYXfUwgN2AkdGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=jaJyrJvpfRlqz00cmhgPYysG5QshHOKYMYhOft8f-E4pKZjLgwWcD6JSQAFkES17mxJm2833Yo65O17lBS-QzaDBkgaVD3pSBVI_w86C3e9rQzS41EI7N32es0sYaup7DTxDQquqJOs1WcxEMuDCwdLXJ4bjuVjzIR50yXwu1fL7yGNQTyOYTLkeKq8mpXRUyoboI6w5Zm-m0riPOnEGtfSuJOmn053BUCX7ip6fSZhUBtaxNB3ssRc8qsSc5gdSbgGfk28bn3lzYbVPwnkgoPfzR2U-n8TjLhoLnh7mJwJPmxHljxbhL4xUuoXmUGOoWOFMiWDDiYXfUwgN2AkdGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1gtcwI_3xodOSc4UPRL1vH2jGTN1WcMYj93ZF9MVvRq9pggHgjZdA7KhmDRz7lWZsMQxiXbpG02M_60aLlHv__OQ4Xr7W3ivSgAzothgle1_JI38WNzweMSO_a2_5BDHH7L878asbRleU5Da3Rd1L0ZccwXk7WQ8GqDImvllqnKpv-f01dXUxI_jxQ2olE9fKS7S7snwoF8ZUWsoMs-IKe0OlxuTfu1y0p6Iz6kMuoI6dD1BWx8oTDCsCbM-JiVCiVKsWDimD7IIFMXutalbPrurTWa3WDpAd1bfLqbUEdM13vj49f1USwGnfGC-VeyVZQoEpA7bZ06wEPdwBk5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knw2xgHgjiGFgXQVsqk6KQs3GOABsdMPTPZ_57RKi2IZgYRmCWOAY9IzZ6ywotH2L3b85I-XHM-3utClUuyFU8eLeK0RPhxbSnU7fIujxS77mAzczm7xXScgSQlYSZFwbWaR9rIaiUGHcuGkcEq2ZAMqiks-t1CKaf-Q2i2XVLyBwuYMUufCLDzEAhB89VozLLwNGIW06sE9Ekh8WK_pnpcvQHkzakDoNHTajF4tz-ydl2Gn64JsbbvJeDzkNidHPOgaOajYxp-J66A1cldTTgiP_ihKeAIIHccyUfwiw5paqq0vDEZpTPXbuzJ0KBBVIdYoGbnSr6imSo_0AcYBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU-A6BCuPUvpgHOT_SUL7eHI7sblgVF_URqiGn942h5L1WGuyv6iBmS3YbGinU1d_ervtnUtcUhE1J9-9PHwZBVO_PGUEZQuYE3Cy1FXh-R9JVHxkUmnORxxCWx_HPcxIQrwWVuraiwm_uDdc7pBpqjroh5u8WxDr9NLZrNl470DTE41w2ja0kWLN7nrZUw-TwD8eZ9mo5tYaBBkPf4IM8hAsCOTQ_TLC06W1GJo0-rJnERECZGjcaWLhjDoxq-_c3x4IuVSlFbPYQCOztto2B1YvVsRRH5KXbGLStxd77-j6OsaqfILf-pKkdMRD5DfvPwG0ONmlVYSK2Eud-RUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2Rjt8ZEqj6-Qucg9AfVKANTIIrysLpITZU0ZTWcHYT7clxYQLnbriWs1fwUzWdlZpUeQK65rBSq9pxdMezzGxLWIOsFji3RqLAfmNnsDkYAJ8WMYo6R4fIhVP6ebFl17PgJL8bZtv_1p2eg4WiZpiFzI09cLDkBaMHBB0FDE0NU1OLW0tuoScy3bvhU5xW6xYQEcJ_XgRE5y6hK__kMkM05rFoxN-EDT5xyMwl239NeAbf7ykTxE78ZG2IT0N_f4bhBDkecvKmD_SfWWm31obQlnhLBDrWgi1hZHwfaDEdJeZ_DEq7aIvjSIljzWDaQ3j6fg7ELo2hrqQxRxFLydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic3yPuRejuuT6yaiwG8OHy3oFNFk99cYASWnkxy7fBTrI8p2TmyINrRPUpNbCdytRcw96E3uXtPmeKOjSNjzu7EtB7W8VbQzMTN0l0FmZBYbQWIC5x_xPvbDaEN1AFjsTXKUVZgcbPHmAFdjAHRDTOAdiL9VsoxJEmgZFCWH6uZFJ_HN5oMiwiAV_Mo_h29r1gybQS9YRZC1THkqca_-F-OF4eMcDVxDnJSEdY-7suK1VCkyReD26rsQNECSaWcV2jh8ulD1aw2dmiJF2Kx1CXHekF9eMxK1PY47iUFKjor-r_ATcSicQcMNGDhWS9QBsVtH7uiYg1mSb4fvMkY8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9yVYxQD_xL-SUic5LMsU32Zg2MU2QG85J4tIVdhU1QqKHxaywjcP_d5HLYbi_MnZxfOw1cPp9DX_3OjdkcGxZOYuyyzAyQiP3dnwCWS2fX5WsS54WhRbWQAwd0JSHUGbVTbTVbFVhwrNzolODY6MFFjRC867CAcvH8QdC7dzT0M2dU8waytppOAOG34L8QmbRpuFqQpel_AZoK2UGYg4pZ8_uoak-R12fNjj20KuppsVbPkBEnOd1TkAY8UPi9jctwaXpzm8kTjze1G05plTnDEpJaOvjZz3XEbu7Sg3y7oMchAbAym2sIc92Xiv4KUIsFCTWJZL4TE1-3VH0tr7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1njxU7c0SHak0W_o5ogluAM0q5sdRljPJyadXpPvcRWPNGF9ibmSXGcFpD2lg0m9om7KLkVCM1nxfT7Q3vJv1AYkxRPDhO7sJrziS5Aey02_QgrFD7o9gNH9datD_n-z0hajM_vtzOYAxf0PiW8UjcDpONzRG3oQu7zas3Rsn8cB4un54Ys2CNpn_VEuiQ4dX6SQP-tgo3Z_8fKjorAKFImUrssRjVLJCMhEL2Vvwvwjs4VZUZR29P6c7QyuTvsPPQRrv76BIKESLKC6MSPxQfUYnDhRxbINTaMvaAeQmUuQqQbArqw7Z5JobeAHFHz9tq7p7fKUHZgl25kJj10cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=WGx-MEQabLjYTkQ2C1dKuyuFAohxbWxEs86XG-pe_652SwFWvn4DY3TA5LkN_FIjF-qb9BL5lrNz1ciq7WjMla3hZV29turLZypLiedCFQrXO9wB3q1-mxTwrppAQidsmtkazuGMYp7Z--SMG83GxrKgXFYoq-Yxy-vbsVZO3gbKFYIjgdEMU8oyE5lwEkv8Jy9DusQ12G828TjGN0kP_cxi-XDKyPaEdwRvaAKeu9fzjknmDqH5nmHynKRtVZISwuyxy0gOt39pYSLbFz_iKC8ydpDOMv-NnNEvu_Xycl2Rf_QyvOdQHwvNBG8DpUyvJ_VkffLXW6Qec4K-ECFfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=WGx-MEQabLjYTkQ2C1dKuyuFAohxbWxEs86XG-pe_652SwFWvn4DY3TA5LkN_FIjF-qb9BL5lrNz1ciq7WjMla3hZV29turLZypLiedCFQrXO9wB3q1-mxTwrppAQidsmtkazuGMYp7Z--SMG83GxrKgXFYoq-Yxy-vbsVZO3gbKFYIjgdEMU8oyE5lwEkv8Jy9DusQ12G828TjGN0kP_cxi-XDKyPaEdwRvaAKeu9fzjknmDqH5nmHynKRtVZISwuyxy0gOt39pYSLbFz_iKC8ydpDOMv-NnNEvu_Xycl2Rf_QyvOdQHwvNBG8DpUyvJ_VkffLXW6Qec4K-ECFfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8PZMwkZ79IB3f2PrfXjucmQ2PzGRKrHc4fmrdImAFRhThU7QAWVBWtWsE8DO9mhxHloUJC8pC-mgf6wAOwMhxmYDnN69taCJqFirXR2tq2Rx6wq_54GnSliTZ1ZfB3OfyNKEi8E4np-cVJccLZEkechgUaBln0sOggvI9uzf7p1QfV2B2BvG_FRWZwns2FaRdVaRn5JoGUkUX7Zx0N4jCs--3mT5kpXpuQ9tWna3WV-Vs1uki03IUHboA7tYsXe9PtSedFCduUc2ekhewAanx_ffRZ1q4yFB-NYSQmCNq1o-WqzuU2whPTheLvkCbCdqQWaE2GlHPfKk0bUDQS5Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyDuDh37AfuWynOwMgPLdEz_sfjVnaj-OrXtz9Jl4kjPqzaf8gj4dN-6GREpLn5WU1aJjOynnulI4Qz2mQImHDxwVvghh6v1kSEKcC2EP7AXUIF8AFfivlFJsKaBizlvhR_-jzsOUL1t7AbEu1kHLUkw_MNX1rGNc-muJBjNWLkOyY-tENl_T4HNuNbyVKlaxRvpRPonl4r-0d3Ug9kOoBJamc_ddg-4BlsyEFxIbJpIAa_TmCbgxgcuEPQDz7_xUIf3MYYRXdj_jqpW8u6KOdA-l3SlDzDueNRVWXvNwVe9ubmA9QKblrBdn-jgyWSlfvU3M8I3F81RdDZryYFu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r79Wxs7sJAQw0ZKY209LHNWz8-kY4UP9uXhNkbnQiXFMp7Z-P6Bawp4pj-8T5rF6a_UKwDVziTTgYyIPs4NagL-K0ysa2AxgyjUcMg1huWu35Myi2Jc1rRqvlGuVc7NoBJyOgyXWQGvw_w7vmHKUSTll4N1vpZA7ClUOiQz2AqeMZ3iOYJVvUA4vmZG6H0oc_buuyQxDyKKuWKsY1DWgPTWU1NhYFujzjDErd3X-pmuBEMuYyRfk78K4HWYajTiMBeCpCydtcG3xc202s2WD1j5Z-4T7KoM1QMbR7eR3wY7bXCKWLEiOfiRvTNjMcGy69Q4Sc76mnpewrDuPCbteXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulOVCxHT1O5AAJnLHfJmDv046NBzzsk1XbTdkn5nfN4B2Ofu9SNYdgb0UHkOqg97qf1CukybiJ2EHjJnKy8Sx6DE1lSQndYlzvarOG-wBK0S_d0ccO6C8TQbTIKCduGFSAe_sE6O12lc2STiLdfnkYBZx4TvKq0wCjJx41EMRnWVFWfEVuPZ2fp0vrUrav7bpwbssT41eK85C9RwK0oWB71JZypCOGxh3sdyPcd7tTSX0-eFUnmy7T5e0ZhE5fh6zNRCwkaHbX9iNiWhMx-thoJbpX67tvMdA56QAwhkl9W0klxObCDXCatiWfhjIetlxVjTn3iTSuoz1fnqJfB0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngACTvmgmT8cfaB1zQ1bObVhRDaBrFix4MKDMvpgtzgBT0ELewTeKBUAnc4DOYVTjYKwIOHwUbzW3mtWU_sdWv20PCD1bkg3US_KzT-5CTtuamAec76O8CAiPcf4kMNyETsiu9pFf2RNbn1XvpgWNaB_LLj6nmF-beyjM51y6Aycx3Qk0B6O2FDhuJzrPRQTWv6VIKnR9YBGdo9ndBhSGaKqwToN3HtVXE7QUrADnUlv48F_k9uXrv9qXtcX2Fs5XkN-kkdPQGWe3__KHkM48OKhQA3Y64kkONrtf2dV33P44HuE3PwN2MeoyqaCdXarTwLfkGW35MQuU_5Lo72MEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=hlcOT1p8E27CpaOlU39BXRXOM3gUX0CrMlBl4DTNgcl28AHoum1raTCw96eU6RpOC-K41P_xixaNcoB1B0DP4j9ER-lEoIHiJWTjr_OjI0Y-ERAjjkJgqmDutXSe5lCOsfZAaWGVDW7wRqNU_vw687ntCZzE6v9xN9FGAGwX_waOvn0Qq_VWma20nCdPRTuHCXNDBNDkm4XPcUg_yzghVfGbpKmjbjsp6FolzMr8qZfHCQq3ZwaabsPtMmwyMp5dMd85ZlQLgQmj0F_UT7BGwWMf4SLNGnqYjYCJKCe8UsfRtVrTsmMhDkPJuSMxFtdpzZEvmAXsB53GQB1gQaF2QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=hlcOT1p8E27CpaOlU39BXRXOM3gUX0CrMlBl4DTNgcl28AHoum1raTCw96eU6RpOC-K41P_xixaNcoB1B0DP4j9ER-lEoIHiJWTjr_OjI0Y-ERAjjkJgqmDutXSe5lCOsfZAaWGVDW7wRqNU_vw687ntCZzE6v9xN9FGAGwX_waOvn0Qq_VWma20nCdPRTuHCXNDBNDkm4XPcUg_yzghVfGbpKmjbjsp6FolzMr8qZfHCQq3ZwaabsPtMmwyMp5dMd85ZlQLgQmj0F_UT7BGwWMf4SLNGnqYjYCJKCe8UsfRtVrTsmMhDkPJuSMxFtdpzZEvmAXsB53GQB1gQaF2QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXmg35HjCkIEzzHncUU8isC218NA5u9ZgZjZVzxwwPvDQvwmfQtmLrluXU6YFc9cKxgsHFXhrv9RE3PTHZyF6-CUdWdApmQmZg2ECqxFh0-VIJMdo6DI6YzVoSuMkoKEcR5sYZaOrBs0unu6EiVwXOaP6rMWZ4DicjF7ccpm6KVCrhOHeFU7NgMxG2BCD5RvjM_jedwhcnv5rYLfrAwU8FEtt17Cu7qi5HSdcOsiziDExwa0jO87XrN5DcakoXDuq6Kx-JCO6QCxCXMwfhbsBp7Lpm5e4TfX822ptpC7thMZTHzmVOuCW6orynxVYWvneWWQOU012M090qRntn5R7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn7zus67bMjZwoTJd1QC4WQFQBFnrMedXpA_saUhIjGFG3lqhH1mKVN-o6grTJZFTNNNrIKFduPiLePzWpff45oVBaWvg98uw0PlNlB2ABWq8lqt5Sucma8ZXaZeAynVq3ugDnzYw220njZ3QkqY_DB3WEoqp7rZH5FozG5wNBGpUrA0sYoH-3tfxpbGuaQqrG5oFZoekUj3RtLYq5C18HVP00RUd0zZjOMujRlYP7kybf9kO_E_MAKuT48s8IdDYo_y4dUoKJE4u7ucYG3HT9Zbsx4lp_Ak_DSyCMV6DLSORWoYU_rfaQbWHw9RQ3wetUjbCCOaynk9_ko1ZfZsdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
