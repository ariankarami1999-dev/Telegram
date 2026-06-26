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
<p>@funhiphop • 👥 182K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویناک خطاب به دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/funhiphop/78745" target="_blank">📅 10:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcrEcyX4IWQo6QnEcqa4ZKTGSRONSRnUUP2uph3KwZUVj79lRk_L-G119GFvp1uT-N_xo_uFvc-Tu6-_gsvqqyH-8-jHyuCRqo-Qjxhsw0drB1AKKFz6QzYyCE_xcxTisoiQP2VrqJ9-2-Dah8WgGXVsFkngeAtE4154CM-6n4xfFV3FLJXVIL2jwnJgLUnU2QfH0SiyFaLNjr8a0oh7TgZkjWUjK0frpWF-xstugF-2ItR0HhtGCMxvbTxzKl21OpE3lB8dubFQSFjYMcKMBbjBMKmWNlZIRrvfb_FepTu7fG-eUQ7_QAF-qd1adwU2YnLjH6TJSmIMiNdggaiUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISToCchcVXqliwmIUbr5lKNwtWJ98_zG8DUoCGucWb_ATkPicggvkX98tXAq3b4_GCANTkw5XHh8uE1DqY9ocQWjtWbTIggDX_NQXWEhzGcGuTbW-aFVlCFar9vyeJ5H1Wfg0KcyixjgHlbjpLyUB9wGomqriFeenjioZLEEGjGeAywzsaekC1RESlE2rnxlbgoMotjKDsJA5Yr0JUO8l6Pk8xGmsDDvJ6ZIVBFQGGSzb5vKAceMDXUsLmBCrb_W9NDQw6QOvA6IPWcwx8rp6Fz_Gq2QNs8emxm6esv1MSwemAqU4ZmBsLIlrn_qXmFb04TyeNPw-EjGGzFZ6rt85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffDIS7eXRdKeq8tQZ1mZ2pk6O66bzMVRlH_DNHph_eB3RGCSrYPMqcOUiCjj4MzD7axpz4qPkBbi-ad5KKTg0R7Fo7PUFw8knQdMdQ738let2YI-Y85AEFlbd697AIdVUHo4XebKzjduBEu712tUsbR6EuN41k8QtanMVVr4r0tJNyqZC7XsP2NhMEfrUEvdJ775DDr3CRgxGXaMDmD9yQw6a3PHMSEYcvKuNbcuC_7Rh802OI83k7fHyqe-s8eifkzVD58vw9eQFHHWsPXZpAD4eDOzVXu1aAMkouoMn3uZJnfXmgxdVsrtkpW19GG7n8IDGCDmCa1y-JCefpeYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwihilxDqZGDb_hjO5Hb6uGpR-fe8b6GkCqEcYzEr70XtrAOJNIVtMxbZKfq3rgt0QC-lOSeUd9onGfTp4uZTJ8v4PgvXBR9OLl-Q7XuhEJxTHFFMqeJ-TeHL5ogFJZAzEAQG7ZKGkYUfbRvdkA5EjtpP2N33POGfGmfY4_7D1fGREhNv1MHX7-ZbFgbqbsFMn2MgVHJTJdwkmd9AhCPUYfMECEWEIeJ7tJMdkT3F1HyPjzWx3wGO7ChPxplFQZxTUShrOXurxcEobtWu6e08kRIEZoS0jfiYq_UOcf6nvfCiA0s9bMYTD6Cf165kw2DOoPWID_DyqWfZqsRrmK0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqD-gwNULJXquTYnNzEXonr5GAolPS8UIO8J_9r44Kmgh1jST2p7vU9bgOXFmnL0UsEgp3Lh5FoY9wfQIM7Ad9IM3wfadIGKcDXYLNL_Lu2z2hcxRtfIPRYyaMoDgg4QihyruAlIoG8jAwtq0n3DTxAmzGqszpzcBB_i9jJPzbzVjfXhA12FxoGg1GmMc7_CDyf4iXMmtIh10oc8BlOu_jSlWj-3ZN4stmn0Q4MBDdvX7DorRxy4wK6cnRKfk7ZN8FvftNmFV26RJ2PyFN3BBHfzXeC6ecEDSh0kLHfhMjvCau_j9U338IR5sLqy_URtxABQPxzapdA8XClN7e3rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdbxToxSJS1MH17V5RUX37zu-it406oWJq5kAnu5QZb7MAZRCP78-0U15popBVWq2u4p4ZYJ1dQXozsvzACGD-3i2EPwh2JwbjnbiCvhMvaGaNbyPkVtnfBrwVDqxwnaWUaynVlI7XFtFBTAAmLV-CExN9Gze9gVwHCST_QMjlxy8_Orgk94_GGog5pRbF58KwqbUioQBL_fBHnQyFBrQtHG_rFLoYKSFmNQV9Wt0qCE-gjBKdK1XYGP9JzkL1NUt716qMJXg5jY_vfHpQ8xYMnKliSHIQwzl-th0KRyFOIcqxIH9-r93qVKMvB4a5HPHhgvHpPQ-L6VvzeZFpE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4szutpZWmHAQ784B5zJfdqSvb8NwDZSp89j_eQSAgk3Qpj2eFVN9aFVFKJbonHZTi_GrFAkBagqKuuMTuPjemn4LkoC_kqmB11X5tyJdOYnHrHULGqrt3a4tkvluP4Tun3iJLI2EjGJzfG32dwb5qU1_sh8xhgaP2mtGdgyEkAGk5sQGSTZIIXaWGFGSJWVMTmr46Nwe0QBwVh4iz0YxbsAj1DRjb_XaDz4_0kRi4_GSAT_Om9FgWgDPvcdAqyvJI0j7_F5qmxuXlc_cBnJZ8qKzx6x8zmFhVHBqrogHsOqf3l7VIhVHGsPD6PooLJ2PrP5PSSeJSuEElWRQro_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTpSH6yq3ntlBlPQ7LjBdiHSDhxGbsRaJIoh33fZ-WhS05ROkdQvu9adMHgj3G4JlfjF5UFM36dotYOhcgyXg1yIybVcJCjYthFCYsdSwewPDaYnyDONgZHUfmLsuso6XRiY1mlcVeh1Msfn3uWYUkc57HwxqRN-B58DsjYQQbQ22UJ_Trn8wjSGcV1LYbWFOE7POxfCJQNnnX7CRFnWeeqxyJr4E_ha4P5fNpyIWGjAv3NQmYPHwBNjNoxDlI6TGaWpNWejSDBisloDDIeDEKvxnX2XZaf-8_ufF6FhKENkacHhwdmg4mbdjhOZ2_M9tp5ixbB-P6QQM2otxmnfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ_n7Ry4CyV9lcf2DOI5mqoLnI_SyjXMQg5Dtkvn20JZRRlK_5jFUlHfRa8vwazjspt5q1RHUK1T0XVX9il7s_OjqsjIAKAjYf3RRtKs9Ysg-uw8JMI5wPbMqDBOYsCE6cHkKrOpZne1m3EvIGHISRDDMghHyCdjq_BN0p9ZUeul8HlE_By6OjmdOBFTBlMpk1CeCsRlbNLkQigkNNMiB0zVjaFLUx_5203t91EsEpFRvcqkN_mgUUu-Ybr5v6JcQoS3WvWmevYtDfdGToDmU_JOx8XB4uatX7a-u0jeeuXR0AZ7LsL7v8qiddoUkXkAZ6GnpGVHJeGmqz547TdZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=dKVvb6YkOThB5XtqJqukRfCjacb2On94GBqqdNLnG1O5zTrivk71HOh1SBqJmvl-lJWlIV8BXkvlDnt0gBZi9GSzBYs0TVtdayQcHdWRfVpQ2TpU2HE2zw68potnWFMxp625Z3LU4hRiVUw4DTcjIvA1iDk2iRo-yLbpppXSRc4guyNREHPnuM_f2we8P9UDFoMbm8nwDHh1fX0zsArx32DkhGIWqDA1B3OEgIMTLRPsWLVZKhZ_fK_tYaLwWsX1-uH_QjdZEwjzMNG5N6gjSuZwvlXbBadFHy-RRvbgKfzjq-yR0LSMRyl5T6I0XsZgnGK2C6oU9hg0ZYzlSwEnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=dKVvb6YkOThB5XtqJqukRfCjacb2On94GBqqdNLnG1O5zTrivk71HOh1SBqJmvl-lJWlIV8BXkvlDnt0gBZi9GSzBYs0TVtdayQcHdWRfVpQ2TpU2HE2zw68potnWFMxp625Z3LU4hRiVUw4DTcjIvA1iDk2iRo-yLbpppXSRc4guyNREHPnuM_f2we8P9UDFoMbm8nwDHh1fX0zsArx32DkhGIWqDA1B3OEgIMTLRPsWLVZKhZ_fK_tYaLwWsX1-uH_QjdZEwjzMNG5N6gjSuZwvlXbBadFHy-RRvbgKfzjq-yR0LSMRyl5T6I0XsZgnGK2C6oU9hg0ZYzlSwEnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEZ8GRGJ8ArTFrnG_SoD6Q06Vk8LWcY_AMduwxwTnC7U_qTiytOEOomhNY2pGBKclDHNA8Q4xO5AH74M-1hXffFxe6a-M8GDQF0GcBszij3RBGoEyqpGecHVKkDECeovkW3Qii4QWCFx9NuTT8cNg-1bkpkJyAAN5p0cXWVVQyGJNCc3QL5eWCNBjnHylVEalpX-5KDWb-T53gaeCr89lVIf15u6SKFsd3_7H05ytOAyPHs2qDMgNyGwX7BqZItbUPthoPsTNzBOPGglENf9V2VTnbsECzeYGXlZF3yfO3AufqT2XZoA2FonELUTBNmLZhNmjdqXsusjOZi7IBWmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7-pNUr3FpD6N1XnYQG1GQeZwXvIuIhoRsqavmSR4gdXvSeredM4SY369k7WrhWMvpTo3Aa5yfqzQoN9MQKZDgvNegH6H95lTa8P1SUayDzPqYDyXW_-cO_YmmgzCGR7ePPKoXqXEZYGvjK3rPDfH89mbXt1ZnGMb4wYKsPYzE4QEwCYsbA3j1kCFCzMpA3VKZ4c9qjOiMztVk7g2ZWFPclpZm4pUPF8G1AGVoxyj-45CIHHKZUL4ty-ys0c6u1zuSbY4jO5Oxz6whtxH7Dji8QA24H7SZTxy591-fWOIHRICTRjMRzFDMOKWwbrMUQzQi7ynsy3JPNJX4HOiRFqKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=VRhmEkZg6ra2js8XzYj_LrXdYlmyvqQHxRxoCL2Vl58m8Bj-UiyKlVH_xW8ZQH6m7SeWU4hG8xAhvuuPEtvAN4eu-DaqGwURcJUFrVNaSB0FEblBbLdNuny89YmflBbSr4lx67kuw-k_wNIJmZO0SxcQewNYvAHBXL02aIgeExPjHehbCMp6F9dksb3-IX3wj61TkuVH3X63sLXI3IfLYQ8qSQ1QfsdHNgFi_ItrVmkI3nayANTvPGbMo_Uy02983cEefq9cjRqyP-iO904cefrziPYR1XwoHcCS2rDbiYTIEctTv9TpFX8vuamr1Jc5eJzxgK6S7wc3tyZN-PqXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=VRhmEkZg6ra2js8XzYj_LrXdYlmyvqQHxRxoCL2Vl58m8Bj-UiyKlVH_xW8ZQH6m7SeWU4hG8xAhvuuPEtvAN4eu-DaqGwURcJUFrVNaSB0FEblBbLdNuny89YmflBbSr4lx67kuw-k_wNIJmZO0SxcQewNYvAHBXL02aIgeExPjHehbCMp6F9dksb3-IX3wj61TkuVH3X63sLXI3IfLYQ8qSQ1QfsdHNgFi_ItrVmkI3nayANTvPGbMo_Uy02983cEefq9cjRqyP-iO904cefrziPYR1XwoHcCS2rDbiYTIEctTv9TpFX8vuamr1Jc5eJzxgK6S7wc3tyZN-PqXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV--ViZinK2L6C--Cz9dMnhFkXIuZVQlJnAr_9yamhpj7JsS4dppCY4fycRSC7cZboNyKDMvkea_MAXRfX1R6nof5i9W_B4AoFCZ6hIk-LacG_BPz18fjjbT_6mQ1GyLjJc1vgRkcOMfA8OJU9PD1Jej5J9hUlYaVFCOYrdcPi0Cwm-2Xl1Sv_Vj-2FnBdZDzFpPDgqm15t62dhrdQIG9n56T9Bm6d8b-SkcO7KJvgevdO4lqaRBohcolb6d6-bT4dfkU5UnFCtsNPTWYXSwELsXq10rrfMqWeF8HvP5l7ZFDRbzSqk674o-dmn10QLOzozfrxZ9_g83x-r85Gecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxRqZAAe3D89dPcltHBJFaMFx7eWXBpwW2luITNaPoqYXJJfbwgSyNzQno2HsyuVT5qo7SPnH7iMg314j1XOVyfPoG0xj_6XfHGRh2q8dseaqQqxgtn8OGbcKvqT8Q2sfuNMKKJxGtbMfRG_QovyNkl0nSFDLk5hZco1SXHzoYLtJQwql4WvY__9kzdvJNklUulUjjiruIoxpJ0TZL8eQRXr7yXei39ZJ86EGzWCM4CE4pQy3yuJeBmCjyTdkHiatx5yQHyCZpvOT650d6Ui7FZmWvMI82sRyxsNutSu3Jofj_i_Ie8AlQWGJjChBs_eEy8JTDke78ORFfG92uAScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAsPHTQGQXRGd4BSqCtWb0b61avCwqjdOrfpBuLnbcpxQvrQyHVbJvFki0pUOzF92KGkSWejrWH6LU1ifsVXFVRIg3uVXx3XMNzRhAA2MV5ks187yw60D0bgggpglriVmvGge3d6a5SZo6fwdxTxx42FA9GzfA2TlG0Jv88LSOGYF0gii8f695sp_WpDN-oQfpm1ocb_LmSLgJdYnsTlyn1i1jPDHHOaBrzl2gX2h-nPuwp3CPXbUt-JP2vO9iqVZH0KblF2gZv-CJc88pVHihrggvoJnR_qzQH4dOWSAj4AXJT0HSLdTvAHPyessrmZa6ZxBIYwKT1U7oUnxKmyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkefbOQZ7QB-BqzkOldmem_L8BbD0sNX9OSz41ybf3xFGRxprAYkccv4YqDUL0czV_XS_PfE5Z8st5477Aj8KZLamEoa3uwjxXwJ6AbfMC5HoTqDP4MyBOMXeKgzQxxpZeooCBNU40XqWqSVRf4Qz14Vu1OFRRaBDNiSps569x83Pc2lFbHyyZWZPDTGEvjtwzy-0zyM0xlqBkhMBRXFOiogQzKxFFDP6TK8I3501JqBuF8Qy-ypG3bAKWY7XgHwSSSFgvFaODIg6FMMTP7s3oSGqzJnn_vNQuFeAtPVHJcrPOhv6zwrWBzNkMFt7UqzaJRaRvfjMn9f1JPuB2PXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=hOubd5Pn0x-sggaAWS4yf-Re5T4_181jTNmrL7-gB976JMlK7nV6dqS1-1_os9VmHTCGUT_EJBvsEeZjPGGJPiNVNp9yum_dJEY53IGIFW70SIPiHTklMMYddp05zxIDTKM_NX62NbZ1gkSb4bbrSrTCrvGwTUC8gHJGwSRqZH2xD17QnFJopJoR0up5wwVJ9aAGLKqlZwuBSRBtreSrT9gRLlgVUIMsgO_cKvNjeUoiZLxb6BMv5XXe1qRI92Snnv4b-96OgX3tRtOPEmesnIQfw1G6hlwR8VUWOxAlsrOwFVZsvMj3B-jePgRUE5QHyAcFu8lO8P5HIBZUIwNhgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=hOubd5Pn0x-sggaAWS4yf-Re5T4_181jTNmrL7-gB976JMlK7nV6dqS1-1_os9VmHTCGUT_EJBvsEeZjPGGJPiNVNp9yum_dJEY53IGIFW70SIPiHTklMMYddp05zxIDTKM_NX62NbZ1gkSb4bbrSrTCrvGwTUC8gHJGwSRqZH2xD17QnFJopJoR0up5wwVJ9aAGLKqlZwuBSRBtreSrT9gRLlgVUIMsgO_cKvNjeUoiZLxb6BMv5XXe1qRI92Snnv4b-96OgX3tRtOPEmesnIQfw1G6hlwR8VUWOxAlsrOwFVZsvMj3B-jePgRUE5QHyAcFu8lO8P5HIBZUIwNhgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=VJ1mCoq4MxENqIa8s_WM3Fmswp-0BTApRS-4Z_dZ4hGNI7yXuEzToN8-JWDYTFVc3xYqKHSHqg3w8qHH8rWa3rMurdriY1-aYviVH2OuhJBXFJnho17Bfb4ZK-F8U3ODYHRBK3YdkFZ8OeAE9KlBQkMVS8ZV-pluv-0TiYojeWLSIp0MF4nExwEjQiUVpVN-B8uOeNuf_ijqt5P2GijnsFR5YEDd7GxKpaQ3kmNJeGngb_xXQ3xu8fpmazmDTkjQLiL8DjHxtY3RZiXbx8OWOm8IJKm7Nahzj0f0TzuXSbnXXDP0iwTtVZqiSxkYWwhX1yXMiyt3otCl6f29ddU6xbKv2AtcHpMInGeIiHkNU3cIS1M-vMu4fS9gHNwfiThQI7CmAJ93E1vO2sy6qZkYO_9pWIER5HimTueZbDfa_EmfyiWJGtTrI8cZqvvJ-C3mgdatMToSGoyx9glXETlEhhMOI7FnsnpI_b8VdPPAtH3MpljYTbkUXnDW01W8IfOBEcuROhNmlWFWWysq1lAUeMj7JQSdUXIyZh5TJi_mjnOdb9lwHcH20nPxlXIvFbtU2v0opXDhkhWIKGgiDSBKuWSgLv448CxqWYzHzu4bObdltJwacTLPXg4SC5gCJhLZ4sdZH_5M9hXkMEr96aceEDZ9e_1XrntI2L6Gs4438ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=VJ1mCoq4MxENqIa8s_WM3Fmswp-0BTApRS-4Z_dZ4hGNI7yXuEzToN8-JWDYTFVc3xYqKHSHqg3w8qHH8rWa3rMurdriY1-aYviVH2OuhJBXFJnho17Bfb4ZK-F8U3ODYHRBK3YdkFZ8OeAE9KlBQkMVS8ZV-pluv-0TiYojeWLSIp0MF4nExwEjQiUVpVN-B8uOeNuf_ijqt5P2GijnsFR5YEDd7GxKpaQ3kmNJeGngb_xXQ3xu8fpmazmDTkjQLiL8DjHxtY3RZiXbx8OWOm8IJKm7Nahzj0f0TzuXSbnXXDP0iwTtVZqiSxkYWwhX1yXMiyt3otCl6f29ddU6xbKv2AtcHpMInGeIiHkNU3cIS1M-vMu4fS9gHNwfiThQI7CmAJ93E1vO2sy6qZkYO_9pWIER5HimTueZbDfa_EmfyiWJGtTrI8cZqvvJ-C3mgdatMToSGoyx9glXETlEhhMOI7FnsnpI_b8VdPPAtH3MpljYTbkUXnDW01W8IfOBEcuROhNmlWFWWysq1lAUeMj7JQSdUXIyZh5TJi_mjnOdb9lwHcH20nPxlXIvFbtU2v0opXDhkhWIKGgiDSBKuWSgLv448CxqWYzHzu4bObdltJwacTLPXg4SC5gCJhLZ4sdZH_5M9hXkMEr96aceEDZ9e_1XrntI2L6Gs4438ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONl4bRMC4HHRLVHOjS2_J8G5cIyY8_NeS2Qp_xQS6pxOvRiMWP3Im1PyQvmv2573aCoKbbP_pDkMI0kF7YsoPExCGDDZYxoSBPAscVxs_4-AjKdhUuXnmMEmPOaRWyvV9gknPPCUPCxA4qvoiOeImUmr3Dy6JrBXLcuHggWdWX-9DdeYBHFvMVcF4mvP79P9TPJK-d0hr5QkXTjsl0m3pazugzrGYtirHghhNRNiwdmeMEO74_RL1_b4oEEMDHzpkn8RqK178kFIY2RE3Xr6v4ZBu16I0jIgqGzk6_Ajhfb5xvi45u56wndcPndx8xJJNNuyryKnR7yaoNHMvZNoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAuNthnoiZJAxkNwee8mB89hFKexijM9AKrBF2KsAzLq2B7-0JR4VGZFcQuUMBovp5nqqcCW6qtnGQVw2w6bUkZPJZLcoUXB26Y0mM5WTxW6Qvegacm6DkSU8dI1EzUV4vyt_ZyXjBRJYvRq1tRDTJQWGQJl20kCKJUM37vyhVw0wm7zjCWAH1oQcXxGMi0T3DCLXRQ9m5E7btEztScVvyV34HyJwPt9W8coIFBsT-pzpQQR-Ntg7dTu6PyV1JP1qUIJm4775Ym8NaqqpZbL3fZ8eeQ7Ha7f8-B6wlt6DvcM0WzAV3khgiBBk0eBNS52pf1HF3ODtxf0jTa1lU5CBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=cy8wTT0bCk2Konfe8guPDQKlvX2PPxAk1lJFH3AiDogRUOwzsthJTjwxtwpN8GkFD2WOilmvY8xAuNpxoaaLX9EY50fqifIjDvJHQfWJMzBS9K1UsMbbW9e4gT4KRPulOELeRwme6rHoqOfdhkeQ8hZEtdhmWHWOJ3LxoqaJNzjeC0hyCrKTx5wq3LCkpmBPCJ2A6xR-r4WZjsE2laauxnTYHY0UWke7YvwJDAFBIuZflSJfD0SyBpLmNNOEG-8_LcSb6ZSTdWe_TDsTMPNa8K-8NHZApS7uwavWQV0o-rfXHZpfucw96fVKKgicrdWkrVmIyWuP6sVrHsF0WL-prA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=cy8wTT0bCk2Konfe8guPDQKlvX2PPxAk1lJFH3AiDogRUOwzsthJTjwxtwpN8GkFD2WOilmvY8xAuNpxoaaLX9EY50fqifIjDvJHQfWJMzBS9K1UsMbbW9e4gT4KRPulOELeRwme6rHoqOfdhkeQ8hZEtdhmWHWOJ3LxoqaJNzjeC0hyCrKTx5wq3LCkpmBPCJ2A6xR-r4WZjsE2laauxnTYHY0UWke7YvwJDAFBIuZflSJfD0SyBpLmNNOEG-8_LcSb6ZSTdWe_TDsTMPNa8K-8NHZApS7uwavWQV0o-rfXHZpfucw96fVKKgicrdWkrVmIyWuP6sVrHsF0WL-prA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZkN2X7Sw1VrCM-ZXk1ZbXj-sL4zklihi3uWZsKhls4-RZKS6t14EWtYjy0fHDRVc7v-CuOUtxuP2lS7NczaJY_Ntird1uYt_Shcd0NaOZEYITx8E_Rta1-L8El9aoaU4xN9xw2KAZKahmrs6Rw0B_9B2IQt77UFKOmKFKDeW_vetwSlrhc60PKN-cxkH45sDJq-AimbT1acSXiQvcBEZs-sC_duQLbVHJcI1XyyWw2__aC3V0DlHB5fow7fSOB9JD3eJIOwFxJ13W0oDyVQUg5M2lwDpyszWgImibu9qHF3FwOeOrbKdpux3_O1VnNQn0zJSCp73i9a8oJFKaPqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpwoIPW1yMkaok22cP0z0uV1vD6qJPPMR5aOr4kNYr-f1qwdK7htzbx7TQKZr5aA6PZ7GehP2JTfyyp_8WOto5-vRtGCrV4dzQ7TEmBtPZVvLdGu_Z-3vVaKboFDxMutbqGRGgbYsoCGUzIzJlpp4lceUsXM25qGAjaeg3s2h9ob_6_T29R47mEU7OSRw6pFca3vxyRMUSrj0hZfBEDuRgNcjLBF59xGwL47Somm-gi5bl8-4dU7Cj48Bmuar-A3L9HOGIkV74CDYwkSf8y6n19XSD-9MjAqW3VRKZR2WawoFO3jBUkI_A4AsF-w6RaQ84t7PowfLDaPpQp1RqkwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IERYUEAMwuJmQv853C8kzibPwHBy4uT4_USc3x-IQwY9IiNBI5hajB0Zn4Ji1Ou25zQvRKRjkIqqoeSxThQHRzO9vkbPCKyfo2mRTpmJl96Z0mvkinEnYXjLsve3AIK-VGGMNBLJStvbSdjiVoCKeRfjzXZerk_JgHVTTPbbXpiOm7CA-bINxEfh9zqEFqEeqnIzZHbiU_ekAp_vmuJD-Omd6utrckCd7bkEwXPMBsp-HtjW9UqojdjLKlmLzmSmFz8ZkajorBk76fbw0mbD8CviVYvk-0SQk1w31fO4lhEqFFbBgk-XzZ3ZS7cvBzAfvBeY7ciUAYYHfaCrl4hp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgjlqX96143JpObm5KAgZ6spUGdHhnJuA8KZ4qDsNXBKK1ji6U7tjAtKQgBHk0kHKO3FjoP_NORbYsQEhlsb27vrPjhGdSMwqKSVTQe4LH6DUUyx8gO9XCtersILkatYVmPS5ZodtEX-ykAIppNGiBR2Ey6AeuSmY5VQYFXP9kqLRYrqQEiB68B6lNrFXjpfjPlqqlqGA-OCtg7k15m8xVlFKSJwylGOWMkpGrRSRwwdr86Bp9V3Zm2TokFzpOaROypWxc4vITYNFtx5bwcxB8jUVwYq6DnPNmfHGjIL8tFfYjEKqLMtmlIrxQxT1iBgVeTvIj8NSuuTvnD-XlyC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHkg_bXpu-L6zQt9Mci981p_0MDBxBkx6xm5IfMz-tMPCMj4OYbVTBQc6fLwiz01VtaeyrDfkz0xLBFdGW9FMxXw1zU0wRL3PyH8jomhbMU-JSx9dTCIpZBPw9Zj2IH80hrXaIwZQZI22hTe5MYUCkxFzImgN4Ik5d74jZDy0VpWZDUQ0gCpNQz1XR4S7_sAaI0vLtt6WSAgl6Y6eToGZZBfGwPRR8egVcArQdaqo5bZg-pvwJQTjUYwqSOgk5-6E4uFHUYGzarFp8kmOY91RUEuYdbEP5TQyamt6R0blbxVdCSeY5mUHiCwBnVjO8v7PEByBG2pllyVe2hViTvagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhE-tMJ4HSLSODyk7H9Z0NH2SejPVLmMuxdoOzWmeKVYYTPGJLotogDQz5dQzTRQHdWYcNEBDb69Q2CHd3hf8O5zXVDrEpCjmeTXBBAyRhdPvF4XaNMDodEWN4P4EgyNvuLMiVAgdtAtJu2C5R7UQ9JeLKuxn418YCSZMofWyxj8dbMib_dtn_-kVhuxCvz_DnrngCbjtL2VYnb0adtFO118wRaIjcvC-nGvHVjPZ7V4Lp_5YFS9uB4m1CvRs0MT7No0vZcjqg3JLpYBb0kJrhkMEpdeARbQ7jngylS92hFIJQikaa0rpxpB-r7W_2lAfN76MjSp00vOAaUZT-ZfaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH4dwVg2aoYg8sQcxltqnZ2v6g4HebnIZ-YFUMx5jRGnu-szetwmKROyeAY74seIlaGQCzuG0X9a6fyFZf0v29rqEJIOIza-zIeain3fnPeBdZ9PWQX7Z1dLo82WZAxJlwcYZL5bwxenucsSViRSsRzzl2otUjOZNrIjCR5oIt_xJRn93J6_V7yqVjCM0GF6PCZVdh48b5c63l9pgPWPRJXsn2tNFUnVx1JadJBGtcnHGpTEcgF_MgwflAj2xpBv-z6c3dvnsPEnrpAdfsSR6R7E0QmNu1nXm2zjoxH3ZP9Y0ewNty359egg13rDEc6aa6aCXSluNnUrFA_omdc4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=oSaNckDXpIUvsHevRPV_fOibTbUnBNW7QJYTVXhlIHdauJUmtvHV8S4V_M9qDWvN7UE_WVr9pWbamJ4FCrxKAKEN7Ajopl7vfXEktacjJkSp24xce44yC1YCPM4GPl9i3tbH6exaNdwXC-xMdT6xD6C3gdBLYWnb20LhX38BknAGuQ8IbvVmruix9x637iePuu7k9lgCNdz9-iCEqKZMkyEixogbHg1SiCuMG_JpK10ZJLH4XaddhCqFT7tavECXhhwer5A9S2FYHhbY1Q8a_gggxXLqgiwcK_6iDjfMDlOefr8a8EGbo9DEFDMsQ5Kgy_YjostyTQxZSop5611Lug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=oSaNckDXpIUvsHevRPV_fOibTbUnBNW7QJYTVXhlIHdauJUmtvHV8S4V_M9qDWvN7UE_WVr9pWbamJ4FCrxKAKEN7Ajopl7vfXEktacjJkSp24xce44yC1YCPM4GPl9i3tbH6exaNdwXC-xMdT6xD6C3gdBLYWnb20LhX38BknAGuQ8IbvVmruix9x637iePuu7k9lgCNdz9-iCEqKZMkyEixogbHg1SiCuMG_JpK10ZJLH4XaddhCqFT7tavECXhhwer5A9S2FYHhbY1Q8a_gggxXLqgiwcK_6iDjfMDlOefr8a8EGbo9DEFDMsQ5Kgy_YjostyTQxZSop5611Lug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE9-Ij879A-e4jcep0RMYa4aMdL7wzDO4FR83wjmWkqBprumvh8NXnfZ9TCbzny6LMHUWBAzTbArfEuHpYQxxprC2QDOk2iFrcQ9gqd58WGh00s_CZRCZqR2mBb04UqdvoHCOM8AayB_GLnbj3CHzPcU_pqflz5gs8Ju2lC1kPQgqI4ty7n7Ic0oKmylNB6l4bmTpzpNOaGjT1PleYh7_h9N-dsI7N9PopgqQsLe7AZph3GUE-FL2Pj4jZQ7aBoo3k-oIncR2SCGAFaMWddTuE3wgS7LhGWlGuQyzZlC72zFmsf9jmqweVqe4xv72-4XkzXOcmvTwUeZDXJJ53C38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTLBpfnm6R-yAqjDBruaKESGUpVoTSVaTz3i3JJsT4OvGYsq9L0rkBcnJ7F6o5p-gy2y2GcGWDy0nA-giIKEt3z1xn1p2v4oVb2j5wJJMdafpaPFgf6JZtywfmjIX5stMT4JS_XVH5bgk2N_I0hzWxVu9Ed9hsGrDkAiMJamYuTUSg8pURHzv804qOIrZKekZ1H7STUoNloSTH8pz5SeuC3jVsYpUPEfS4q6ZHi2gkZwgWUdy55i2bBNhOJw8LFD3bNSe-_3mp9LrH7QB6BQn0hITmmRJc1FAn23CkhAl8QZPIyR3g56U8O8wKJOfPR4yzCnMbXgjOx-2rxhYo_JQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5OwUDR6h7IBt7IGGCybltitxqI9hQtCjUtxzKVv1V5T6V-IRLMtYmY5z1U2fDdBMIFm6dAcarbpdJQiADY0NZJaKMzdYafVVuFF2DxAW2DRV0h0bQ2iizk6_ecETTEtBdL138LMRSdb3yaFI73XKsn9FwEjogHuF5BCnMnTY-Tpg-EbziCSdx-rKz5qw8JGdn_sPxLAXTbZXU_RoCG5ywSAOXF_QrO3cDNfreFVpiDwfADuCLYcz1EK8nrOV_NyyGsDSzUGYsuVPlZo8aVMZ0E8AqqOlXdPdwaUOviH0u4VkACsUiB1dU2stAUWrvZYWzEKnWjIBOXVq9vKsRK6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKroDMHtQkJTGU9lYIduWsWaeJ0vzTgI1vr2rfU8_zmudLOcqZUc-6wWkCb7Q4sFJtYZOhiEZMdXpR_oN89KluNjUwnxrSfpGd_Whn1Edvdh82m_Zmj3DeETer_5JZCJHfDX2dNmk8iQ-QfuPzyUxKzpeelLkYqaXgyl5NHVV7aCeV2NVTy5g0XkNnMcR5mCiyblREBn_19hyG4w2gQhn-lRZxNwEC_11yMqD87mQFKJmyeo6DuCp4OP1vMPmsiQcE9T88gyOjTBr7dw2QWeb_SdYAkYK0Myu-2Bgsc4LkUifwFbhPyT7lCIKvm6sMwArYGO1WP4RGAL7wieGn6kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDSxNFfMxHtwjikBEsNTU-1FUBkQqUKOiG2sXKggWxMZbvHfqLxlc2thiuJUuzl8BBMAtDGLPJdY3K6Yh_1p3dZzoMvMLTaZPs68nFtIPMbP2PspN51nGz390ZfSm7rDd5GV1hmSztCmU-M5bYTFVPq7EKwoZinLqlMKUVwcU16LtOokXUis0zHdiptMyF1XDs8tMxOKFdzZ411YSghVZDLSymkP-ZGU0y3kFux74Kzvw9AJ_egiWJJdEohqwj5r5rQ05afUx39aN_7Js-onizbgMkfWVx8ZywZuy31iv-1AcM5OBc0d6PISQTkq7n3fkT-39ppEZRa1xOcdsW55xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=Le5yd_1idBfQhUjlmrJPilgcG5b3RE6Lukd1pbTdB9socXt14yI0zjAD1MxkDo8qxSOvM2_opjwNyWMZM1Fjf_D4tSXkERzWRUPeT81DyOTXpclA39xYZZyEAIC75tVK5-lHeU14SvLmuyTaVV2WZsL_G2p9a0AVoxMJcdrIUFEa980DCpH3Ub_cG-_IJ0Z0-UdFUmTXtDWO77H1IB5hmHsUIjrKxOpxafY7pYWu-GjfYKUbQ2uxeww_zH3Pou4rOSbxQksYNBN6TPx-lQWFhTrvlPvBbN88H5PXOPzSBNTWMXv_narz0QWKXZhT9TSsGdquZkkY6k4dazeCwJ1tNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=Le5yd_1idBfQhUjlmrJPilgcG5b3RE6Lukd1pbTdB9socXt14yI0zjAD1MxkDo8qxSOvM2_opjwNyWMZM1Fjf_D4tSXkERzWRUPeT81DyOTXpclA39xYZZyEAIC75tVK5-lHeU14SvLmuyTaVV2WZsL_G2p9a0AVoxMJcdrIUFEa980DCpH3Ub_cG-_IJ0Z0-UdFUmTXtDWO77H1IB5hmHsUIjrKxOpxafY7pYWu-GjfYKUbQ2uxeww_zH3Pou4rOSbxQksYNBN6TPx-lQWFhTrvlPvBbN88H5PXOPzSBNTWMXv_narz0QWKXZhT9TSsGdquZkkY6k4dazeCwJ1tNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juk-oTo4jeFW2ncrgF5vplT3rycLRSAi9rDUxRvT8AR7uqJt95BgC6LzZ02NjEzSUZxao0sxlm0n9eHOSJ-VecBEl0e0Ro2Az9heQei7oteZCLww4vUdFtHpNKFndoOOFk-ETlVY-yG6xBWyGUW8ju_kNcfSGIfmbEva21GrlriN2kb2eDoWFxk3C9qjUca_GlY3vRWu0_tJznsbYJAAOiABXyapuKrGoB4GrBl1bFhmJIjyodA-FlqNGbRTmDADbI4dyzS8zYwweIv7GLxfvhTMDeOcbjmvNGyg62kjK7RDyOnXQgAqDqRkgEzNOO7xLAsBNRPVnKgZ8UhmajN1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
