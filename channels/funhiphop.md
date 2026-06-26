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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 06:03:55</div>
<hr>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcrEcyX4IWQo6QnEcqa4ZKTGSRONSRnUUP2uph3KwZUVj79lRk_L-G119GFvp1uT-N_xo_uFvc-Tu6-_gsvqqyH-8-jHyuCRqo-Qjxhsw0drB1AKKFz6QzYyCE_xcxTisoiQP2VrqJ9-2-Dah8WgGXVsFkngeAtE4154CM-6n4xfFV3FLJXVIL2jwnJgLUnU2QfH0SiyFaLNjr8a0oh7TgZkjWUjK0frpWF-xstugF-2ItR0HhtGCMxvbTxzKl21OpE3lB8dubFQSFjYMcKMBbjBMKmWNlZIRrvfb_FepTu7fG-eUQ7_QAF-qd1adwU2YnLjH6TJSmIMiNdggaiUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISToCchcVXqliwmIUbr5lKNwtWJ98_zG8DUoCGucWb_ATkPicggvkX98tXAq3b4_GCANTkw5XHh8uE1DqY9ocQWjtWbTIggDX_NQXWEhzGcGuTbW-aFVlCFar9vyeJ5H1Wfg0KcyixjgHlbjpLyUB9wGomqriFeenjioZLEEGjGeAywzsaekC1RESlE2rnxlbgoMotjKDsJA5Yr0JUO8l6Pk8xGmsDDvJ6ZIVBFQGGSzb5vKAceMDXUsLmBCrb_W9NDQw6QOvA6IPWcwx8rp6Fz_Gq2QNs8emxm6esv1MSwemAqU4ZmBsLIlrn_qXmFb04TyeNPw-EjGGzFZ6rt85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffDIS7eXRdKeq8tQZ1mZ2pk6O66bzMVRlH_DNHph_eB3RGCSrYPMqcOUiCjj4MzD7axpz4qPkBbi-ad5KKTg0R7Fo7PUFw8knQdMdQ738let2YI-Y85AEFlbd697AIdVUHo4XebKzjduBEu712tUsbR6EuN41k8QtanMVVr4r0tJNyqZC7XsP2NhMEfrUEvdJ775DDr3CRgxGXaMDmD9yQw6a3PHMSEYcvKuNbcuC_7Rh802OI83k7fHyqe-s8eifkzVD58vw9eQFHHWsPXZpAD4eDOzVXu1aAMkouoMn3uZJnfXmgxdVsrtkpW19GG7n8IDGCDmCa1y-JCefpeYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwihilxDqZGDb_hjO5Hb6uGpR-fe8b6GkCqEcYzEr70XtrAOJNIVtMxbZKfq3rgt0QC-lOSeUd9onGfTp4uZTJ8v4PgvXBR9OLl-Q7XuhEJxTHFFMqeJ-TeHL5ogFJZAzEAQG7ZKGkYUfbRvdkA5EjtpP2N33POGfGmfY4_7D1fGREhNv1MHX7-ZbFgbqbsFMn2MgVHJTJdwkmd9AhCPUYfMECEWEIeJ7tJMdkT3F1HyPjzWx3wGO7ChPxplFQZxTUShrOXurxcEobtWu6e08kRIEZoS0jfiYq_UOcf6nvfCiA0s9bMYTD6Cf165kw2DOoPWID_DyqWfZqsRrmK0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqD-gwNULJXquTYnNzEXonr5GAolPS8UIO8J_9r44Kmgh1jST2p7vU9bgOXFmnL0UsEgp3Lh5FoY9wfQIM7Ad9IM3wfadIGKcDXYLNL_Lu2z2hcxRtfIPRYyaMoDgg4QihyruAlIoG8jAwtq0n3DTxAmzGqszpzcBB_i9jJPzbzVjfXhA12FxoGg1GmMc7_CDyf4iXMmtIh10oc8BlOu_jSlWj-3ZN4stmn0Q4MBDdvX7DorRxy4wK6cnRKfk7ZN8FvftNmFV26RJ2PyFN3BBHfzXeC6ecEDSh0kLHfhMjvCau_j9U338IR5sLqy_URtxABQPxzapdA8XClN7e3rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdbxToxSJS1MH17V5RUX37zu-it406oWJq5kAnu5QZb7MAZRCP78-0U15popBVWq2u4p4ZYJ1dQXozsvzACGD-3i2EPwh2JwbjnbiCvhMvaGaNbyPkVtnfBrwVDqxwnaWUaynVlI7XFtFBTAAmLV-CExN9Gze9gVwHCST_QMjlxy8_Orgk94_GGog5pRbF58KwqbUioQBL_fBHnQyFBrQtHG_rFLoYKSFmNQV9Wt0qCE-gjBKdK1XYGP9JzkL1NUt716qMJXg5jY_vfHpQ8xYMnKliSHIQwzl-th0KRyFOIcqxIH9-r93qVKMvB4a5HPHhgvHpPQ-L6VvzeZFpE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWy5-BW6jwjSp9Nh2iYnm0q8RPnKQSjbstSmJO1uwPXHf1P5s3udI3tqpOwQlmJYwnFjkqaMQL4cczQOHXZ6XRCsM3ceZ2wKuQhsXvLGa3LPorODwrhn3lV6xFDcPzUeh71QJyLau03yNZUVQwK15Ca8rxFbzYoPoZfwLCNvBRbQmVwaf1IKbiNUz9ZMQaYPxFGEkydfhBkdBwNv3hpSxM7NLp0DQV6pU2Lwmk3GP6-mbzChTPkdHxCU5aNB_Y-7GWIkP_AX8BEe8EIvnlBxIkM8cTTAgj1zNw59jiJ1KFFT6qm0CNOstEIgxJOKmxAGCuuzu1Tc-qVbU5DsKNWHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MnZ416rn7VhHTW7zUWEeiPXJuhLA7qFUsK1XcLo_Ms7WiQHUU0OshzGaND5O1lGcPefY--cdblFwKk79SwoddwcdPKCPdpD45rjKEwIjzHnGgD_VDMAerh9crgKu15zBeMnZXiGTBpI0bFyaLhXnVd7RZHS2lAg5Tecv1BrPCknmkdQ3cshg1FOSgn9wKCM9o5HGL1queP5YMl_aGvceW1mv8EyEo0gSxI9wzfMKtEI4GYVRxgjsUVJlsPF-oL0B6jQyY-w45Th2-o6hbM1aquLq8tMK6Qyi85vQU99KfhnJ5bXXp2grf9P2yR-Giz_JdyU5_S7SB1QyZtWr_UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT-bt18AY3Zi3bLQSrAub6QqldukgNJrSf6VcX1k9VU9FIayCALuVXzAYY-iXZNPTcMQ3HyZ2RVVAcM_bDJqzupVAEKlZUhOi0VX2SV9PnufKXkcD28jrlgFmXYJlFxPsH_AZaWexMuklpQnuKlD8bBiOgrf0w294BetCdmb6OTMX5UzCfmM5JX6fzQvDTrNvHTV3l56YEDfl2njwDcPHNFPIcWk7tK5q7rmjvr56x-NdVvbpomDdU_I-XeUQtOsP-UbourH4gECpETFhai2Ei65ePzeZ1LwPgTSBW4cmI2te2cgdKmKcUIcZX7lpka9PIdkzhxSp6wgMGwpk6u7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7G7hN8Lp3qEx0lwJy3DeQIonGI2IwRvHcXsLb7dQ0y3jLb_5pQ3EaS_C1awsZGxNXu2sVHsD_CbAmZE4brUyTVOkxD-rU5Mb1ALlZZA2a90MxcbKgzkCaWdQ2o4xdZIgj8fvIl1jcfKEi8ABw76yMTmcYRNxAI0hXcKowrd94YJeR2ckET2e5v9re0bVYbEs_JTkfdsKcgRQQ8WB33VScdNAvZm3kcaiYIox5WgcXHf0YWUw71_xEtufVeeo2ThhHLla1ZvjP3KXWi_V3QPCXutDiQDUnASK7Usb4fKR6gjAAG49qvg5LW0gB1XdmiC76cxxE0x1CScxq5-ZxMxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrABP3gSjzoHEgnQVwh3WWR9LCMqtryy8HiJFE_NmNlwxS_m4mgwCOli0E5VLd9rQ2GrBI_wF8eyVOPcrJzviNhWyoj_o2zxP1VoHZXLLR5Q1dCo4I_-tYkRUt4NX1Ps_K8X2y-ckhNop6wti82TL7THk4MvTuPYObSoanbIUxg-WI31iKuS13gqdjsGOcyWIhZiAovdu_0puYI9LnEoPs2rso4QIsnE2mGfuKQVS4rYQt8BrFpYM0xueG_b0XlnvSqH7jwZofUHj7rXIowYGa5gefCTreIIfhNg5ORR7G941C4uLy66cn7RSOg7MEw4lDVbA1IxBK0HTHqWSz_Xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bptC28912XKHkLmQ_CwVU8vL26228H183oYlMVPKKg0m4Xz8mFG5DiLqPjVo9GFtehZBC06mmXh5nPvwkYC0QVIyTGzO112j1pidMiNNQ0pUte1Za77B1bO16XXgFJsHZzWgbHzygZUUTXmx15eXv-1dZDHNS8UquOf8yjmQ6CyjWexya740kilg8iyt7l8Ku_qY6G17Aza636xK5H2n1TxVGOzipd6vN3lyJLwcwovPrvC_CnUnmpYBuZcQlqR8whPLJQC4NM0L40CHLvIPW3UJhdmwzoYQLrZaJPkmCdIKrgvPNSBl5FcF9M0Q_Ir4deHqgkoSSbEz6NOt53xtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu826qeV28K0AZpvxY8MjE56OJvGaA9SqTCuP2OTgPGNA2gz_47gW9luXJnYNZnQvn0RTJ7TZ9nKqNZv1VshKkMYazRO1NSMYv1Xckx7jl4zNtS85lXn8R3-y2ArNPhlTrRN1ShRhOkXFF--f3ZpGhn7gQbArKcSciPa1yToj3Qu4GuLwwWWqW6BM2k8PkeCRHCKDhYG4RSNWBAvVHLnPhOjyuwxAm9SrGUBOrZc67zhvDvN8x9g4PwUzVtVngvjuBfYCcKW42iuBz1HNGd_KygB3EScxhXBbw6EjrflKTNrw2bOvZgtyxzh8RRgqOqyNMpS0pyRIeIWcFV-FO69yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaWot9fUFGATYYJTgKRlnskNTIyFerC53J9KLju2xCo0YZtpSDUfKkbB43kgYpjmT3CW6dd3vKN0s0btcfDFjjpS_fEP86cwiS68MbYh0VmCyCmubWlGVtAdeOWFj8UT_4wsmhs17wIu7J0M5RWMPCM90WWZ9gatPKCL7Ghs-NiHPwjXt55pbF-rqQs825PORIgwD1zhUsruA8JxY7_lhsjXn1fBD4qwzoJuHBtOmiN5nIHMGnDtu9al80o0pZsrQd_3y66wU6B6hsUDfPfMEiZ94thH4QN779ZRnrqOddq3RTqWrjwGtox0yvH82Qiz0izckpPAn8M8eXQ1WYjQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqQu6zroLEr6fisYIy5l5hGTe8chiCYf7cTIFgvEIACvB0sgyr6kyH4AH9Bm9i7TxbSoAizGFkzWVDra1CekjRHFJXQ69fEDYbXoh7D8yuz9iMZMUkQywb5BLDrNVzRculKusSxYe6M1_8Ex9KtSuI6ALhLFbyXnVUsTM9k_FF3z5GGaJ9p919oe7kADPsuA730DkSz74gfqPxo-9S513HmgpY29IVNJ5mx7I8aSvvjn_ehXVXhISCMfHqFI9J4OXA2YrEAF0Y-Kw8YqovBlD0rVqAm2lEvj5xWMubRK6lUI-GNuwLp4_81XzdaziP985f-oToPJNhxx1k3iHr9O3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=EiIbQITg9y_MPO8DCtj7UuSTWeEAK0lyQGW42NM_D8pg4VQ7oRXhLemJaauIK5_rKP0huKqeixOtvsjKur7sci8OtZJtroPPdZiA8a2OoKJGcyy6IilYd_B82-sRtaiT7ybh9t0g3_1j5KkTrmhlVbsadPS90mYJ2WDAM_DPqMjPgjbT83awtAzj6tY2v7h18Jk5dPOP20XgPjVQUdutkFO39EMft5wxK9kMSk6aTRGLHxitf3GKBPRrhUef-cTJrCTGy0PA_IIC71m3DS51FJOlT03uVO_svocStHdaKT-yTleHuwsIRR6uxhLjWeYkS6FL23noDV9YV7ltP5KwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=EiIbQITg9y_MPO8DCtj7UuSTWeEAK0lyQGW42NM_D8pg4VQ7oRXhLemJaauIK5_rKP0huKqeixOtvsjKur7sci8OtZJtroPPdZiA8a2OoKJGcyy6IilYd_B82-sRtaiT7ybh9t0g3_1j5KkTrmhlVbsadPS90mYJ2WDAM_DPqMjPgjbT83awtAzj6tY2v7h18Jk5dPOP20XgPjVQUdutkFO39EMft5wxK9kMSk6aTRGLHxitf3GKBPRrhUef-cTJrCTGy0PA_IIC71m3DS51FJOlT03uVO_svocStHdaKT-yTleHuwsIRR6uxhLjWeYkS6FL23noDV9YV7ltP5KwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll9RPG7G1lZLPFiy_CpGTwZQXH28oLb9X7_BucqKekwDpGeBOqd4YhHIhCZcg7TYuNM93_4hrLeFLSycWyPEi2z9qUOoVl59ljuNxHZQB8bhnINDarEJCoirB7gVY2Z3PkyKPXU8NafWm5JThr9H3QwsZ4FJvmPCHIWC4GnO099cEBA70zqdt8UROkG1obeA_IPAm5nNmdhPL22NJIOAUFP25iRNnK9g0Rb6TT1X3oftFRhbZUGa9PsqO0GzdyzKRtZazEyd7C4j4TXHRMnzWca8UsL5cZLghoSE4KGss4a-YZNdcpaLZXw1oJgfc6y7u1VhnxFRGBGOMuxE1T58iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmbyg3SZ5jRV5IDsxkqAvwi-fvixbfl8NAd9wiSLUxu4eJGjp6Fw1yiXuJzI0F-hPcGQfghTQKgQErZIEthtU3XagZpBynxN8ZQCkQj_rZaQPSN8eXya4PL_8fshnbCHmNlKcti4S5PI196ybfEoAGvJRnaorJSNBBSFv1QSPkjxgAM6-D-uPyan0QkIF9lQ8UdIUP_PYmHCXydyG5ElzbGPnOhfohclVNDvpmfa8lahkUGYzX75xfHwBPfbkPrZ4Xb_RBW9Yvn6_m1U4E2o1sW9c8kLba03tbxNE1tJRyww40DuqXxHyY3GzXuD1mM7yIxf8AhBjWalGsSFLFTAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSew77DH2WbmEt0tIkoggUpVpHOFvfNKpEaQSogN4LWMRxiOqNOmQO544vBxYaTo4aaSy_PiR6126M6HMKVq48KvnF4-OaF0OQnjJs7h3WoUBYk-w09gUJsbDSigGTDs_M9zuD4-L9cp1QYpkWskZ6mIuD8e36fedkLXxX89MUOggF6v5-aCyolUWwWS-V3EmaLu4aEiNp48jBsT6IJ5sNAFd_rC6SWA4Pq4f9vDsn-D8MXeJ74OJSbbzEST44hjDoQGVEu6MFPS0ZmcboHl9doygdVnZuoMsy8IZcWiGuE1-Gy4M2uJICbNGrCPL0rBCoAIox5S0069r95zzjLnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvpDrDCV0SIElrwAdnlz3xBlmwmSQ6PZatK762__sSgTdMygQ3s4AbjSu4cd9UWtcB5QuYJ5ZSeSwYrrii1s01djz-GcKoUMr8iEQoB5htfomzlXB0KvHMtolNCoMnv05jmw6cpV0H9bwVFU2nRx9L7QuwcrTVhpU4hZPG6f8nB2w2vUysoRbcfyB4BoQ2KbNYw748iT3TX6Mmlbp-lJ4JtGLEGen4oruZNfrCBoxARJtxSx4-I_O0_KYFfL4UCov8CchhW-HSbmzhCYLF6GgzTeFMccQQAp0WZ6CcZhWEWIbvzWQf9SMdkycjRYdfaVwGa1-_LWyPTBGRiu_MfswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLrSuCigYaWusvzQxOo_SnmavKfKy9eZAkIAPl5P9NAosXsfrXonhkrLo--0byRfnTJ95S9XZ6xQVza2xEvbF2737tpf_gItsrhYzv2YFRgVQXIvP4HBmS4uz1RYKDsHdCmxz6mOypi63G_B_SKbp_u5NOh0vWqUCRQbgOB3kk1CFs2eN4A-4hYnthtsPZVuiBaatnUUOsA9D5aCrkubzn_2zNhB45KrzQH3vEMBxudGd7yOJFZGpmGqwoDrcrrav-uTi5iff0NB0EENleQmo7jYhbrdm01B-jdgY7RGR-3cmxgQrGstC0EuCcnj1nS24vbaW_wmUfEHcT5EAASc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz1_c3vuANGijLVH2oXdU2Lyuw9mAfHf72L3-moGkPD7jqEFhZjg7eeXei8g6hmfMTCPlggMmnVK85MOEgK6wCFnXRrviNnNgMTNVejdjqBElwRJQhmPAizRt4adcuNNRGUaiLOeZq_h1tf-v2acXk_n6XoTGWTI5QMqHkeIRGE4L2hXy29CscSU8eYn2wzts6pd0UBzL6M4BeZPOrpw9HHdsS2fj1Be4OmiJiolJlVoAQV5lD4s6j8lRPzYkkVF7Arckr1Vz1lBsaTYMvlw3e3nuvGi5jqfwB3BLoi3DZ97xXpSIyKgoi4p-A6U_xnaaqdbafoJbKndbRIsg1k54A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0xHIGJU88rLhazxQGZujnDtlCU6N64AwYXfUkUlTdEE4BgooqOmqyUxU9Do4YJFvYTeBSkDwPbw7wbLJuGPQ6FG6M88-zIJmnzXt15puM65EERQoVz69M94bZcpzAswj9eeKbYWz_22kvVql1YJYm9yqbegVV9ISw_6iG8QqVmgpo3rM1tRZTK75YT9R0mOgr1Ck5hpaZsJTTPFq5Cahx6fJa-lEwGCJaN1I46uX_-U3t_3fQYEWuc0FsQXkc3WTWDQ3FJjxH2Hldll2Ebey-nN_BxQdNhk8A5ohK9h96Ncwe-zdICcDWxKsbEXZ6nRTfVCY0wuyho5PGumDet-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=NSIfpODdltlCaa8-O9CmGa54XTQfJgZWrPDGmr1xx9Q95RgCOTHt6ZLH3aQJpV1V8XAOGO9dct0XVm1uLIHrNBt5R10AddCzFFwC1Z8HiaXRamnraCsiV1pDYMP_t7OPDlBJMuWGGLIunPyUW56KIfy2xg3u0g8Vd1mrJyNMELJBfc3rrLkjfnptZhaH9Irc1Cxo4e9nIzGJ7nr6z8_2frcjtX6bs6GsKBAMeUk_F2uAdQGWeAIB6uS5LxwZpNWIqHDlK0Z328RLkzqYKr8h1oV7DoodYNB1WltYFWg6D3pKre2rqeSUuiGL9Zfy_poe_M3rOlaPlV3Lyybg9lwMiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=NSIfpODdltlCaa8-O9CmGa54XTQfJgZWrPDGmr1xx9Q95RgCOTHt6ZLH3aQJpV1V8XAOGO9dct0XVm1uLIHrNBt5R10AddCzFFwC1Z8HiaXRamnraCsiV1pDYMP_t7OPDlBJMuWGGLIunPyUW56KIfy2xg3u0g8Vd1mrJyNMELJBfc3rrLkjfnptZhaH9Irc1Cxo4e9nIzGJ7nr6z8_2frcjtX6bs6GsKBAMeUk_F2uAdQGWeAIB6uS5LxwZpNWIqHDlK0Z328RLkzqYKr8h1oV7DoodYNB1WltYFWg6D3pKre2rqeSUuiGL9Zfy_poe_M3rOlaPlV3Lyybg9lwMiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_rTeVPY9T3u6WhxkB0Ksy6NO31XIqOb1wgFwue8RTh1_Yz14EURSBlduvCV0qzmrfFA6FylNKthNcxYRPRFgR0ycaTmHNDDE7j_S6_GQql-SpStgwz_STaKfcwc8wwcoMgZH0CcpKShPAOyL_bV4T3N2l67eeiTcPnonihPRbyo2tu8CpvbaN_JC3vCSM3_MK7B0D3Gr0_JBadObmo71t23PK5ccuMOMK2Tn1D23ZXF5sRCj6uKgcwWWwoow-kNlr-iFvTxtK1HNbV5DsgNzEKvZ4h87nTHDuB5WXlvpGysJMktQvogU0ao35hSU5KaY_gryPkinKd-4UFNNVl4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHyQMOipjHR0Aq6L9u0C5hb2F7dX0Ptb0gtSo1uC3BdZmka31I9FFnO-XPbW2jYUoSifp06G6frv0K7GybQYguXJkWraCiR7uoRN7uPH7gUwD_i_7rFa6lgUgbNfmFSLe18ST5BdcMCx5NMre3QeSNMEUebSULeCBAAWiTlVMaIZP9GIKy3ODc4sD7z0hZEzwLadTAxpqWXt7q29P5GZ1c5BgJ2mIA2rEEpQn62eUL5xOtSwADKL6XD1gGjAaGTxAhnEQ3bwyWvFWRd73YUs7jM4cBsbnhnuijLZ8kV33Po3Qep9V-g2QWUmLhx2thMYpofcvOnAqlsMD9HMhvxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onXt8_QEb_EEdBuCsrBhelcwB1YlSzxCgnreT-n-b--q1tzgykwi00zoqwNmYxNXYFakJ9i5vR1B5XRma7eo16oPWmb34T5yH7lYxwfPxVIYQpryas_k2-DbsLmleg7wPGHLWoBE3heUYNq99fq0Ct2jgvF3QaRfaXG6ZWJeLb25dvp-KW_1wAaJPUlrJaAy1HXVZiz23JZH8IWm8ZtysYkN3pDB2iqNDYkEGKtIZyI4CiKymzcSzu6NO39vi5XFUZMNZY9MkQa9VsK-pq0HhFYN39kJUaLpmAA6rHkrdu9GC6c8LpRgk_bnZNPAoQz-pBACfkhoVRKzHgpkrZOFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAHCQ0djXAZSpyB_D3n7hDn07_4eMRYdAzqSG31Ag0fAMwEP013_-zxaqCUp5gn89GzqVBx0oN7c8PovEv_ytenLxGaXAuQC9vCBdi1ypWv7dEfb15Wwf96h5ZrsYMNMuHIDTCmrTep4JD5SKG8R-vw6YVFpFXY9PAekLDNknIeC6HgsX39pE1KfaOKnEpfKZqlY5-TkcVFsccZ8xT9KL9o-0VUWo1o8rZfNxztCL0TVlFRFSzmZmx-8BTJh9u_YOIaX2D0Go19VQWCtepodwN9XiCRIBbJOqPrhSg6l3PxJOBWaIbyUlbYKAwP9CYHNdw6lYKXaeIkPOuOla6UIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDSxNFfMxHtwjikBEsNTU-1FUBkQqUKOiG2sXKggWxMZbvHfqLxlc2thiuJUuzl8BBMAtDGLPJdY3K6Yh_1p3dZzoMvMLTaZPs68nFtIPMbP2PspN51nGz390ZfSm7rDd5GV1hmSztCmU-M5bYTFVPq7EKwoZinLqlMKUVwcU16LtOokXUis0zHdiptMyF1XDs8tMxOKFdzZ411YSghVZDLSymkP-ZGU0y3kFux74Kzvw9AJ_egiWJJdEohqwj5r5rQ05afUx39aN_7Js-onizbgMkfWVx8ZywZuy31iv-1AcM5OBc0d6PISQTkq7n3fkT-39ppEZRa1xOcdsW55xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=uQQ1lP6_5da9ovdiRT-KzI1SG4tdhpQVxqoFCIJ3dhfTL_27VA25cIBLAwVkOudt65SdNlYVSukJoEVId889EKbvpz6eghGSEshoV7WVX4eRiQN-J75dIA5O2PsceGK30cyvQ0oJD4opSOgP4qqxj0efasCYbqwt6tUpugu0UPcRxX8z4z2w3hyWXDmtgc17yMSZAQh4ymLrYhNuc4fI36w3-WcAfyZF0oNiMdHGquLTo4LT-MsaUCKvn-tK4rynB-U6-ijnxHv4f9E9wNRZn2V2opucdssaQt4qyKsw1vcScVgXIg3fp4B-35L885tjV-HbtGS-9quapZriTmBmRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=uQQ1lP6_5da9ovdiRT-KzI1SG4tdhpQVxqoFCIJ3dhfTL_27VA25cIBLAwVkOudt65SdNlYVSukJoEVId889EKbvpz6eghGSEshoV7WVX4eRiQN-J75dIA5O2PsceGK30cyvQ0oJD4opSOgP4qqxj0efasCYbqwt6tUpugu0UPcRxX8z4z2w3hyWXDmtgc17yMSZAQh4ymLrYhNuc4fI36w3-WcAfyZF0oNiMdHGquLTo4LT-MsaUCKvn-tK4rynB-U6-ijnxHv4f9E9wNRZn2V2opucdssaQt4qyKsw1vcScVgXIg3fp4B-35L885tjV-HbtGS-9quapZriTmBmRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwNFieheZMW-3QGMMjxZUFIaIPnSb-tOMfQ1QOgKs7-27REP2JnU6p1PEytDL3Z9tKrRU6OUPnl9S0nAtBOouQbX01d4N3KlAtg9yIJJv9KBDJCGR7aaCWA4CtjA61dk9JV_vgBbhqfOEnS-Wp10IQ9f_P48vvfvSTg9h29NWTSNjcQBY_EZNyNKY-9INb-nzOob74dakV5BOK33MUQR4evcN29vNDMulAY4XWp1VRsd1YitDMsEJCEFV6iht6p5x9aejZnspSDVf8UfGBOPyUQOCwQMhpsegXevmth1VEIFCPvUoy2AyqIrQV09-mhd-h9MQVUC7oonISM31a952A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpDHE0TSgkodcjJhpDjifecmjQm0_RHyU8D3Hs4qhCEwSAUXnhDnHHT7I95pYa3Q1jkyBD32Uxc31LWS5pRHyv6zS6r7fkiaOJSHQMNxd0lnaGfNpg6787DGJqYu4y9aY60e2aWLg-quWRy5PcFrFn6yolrFXvLSalXq1cT0GUg8MBeuT7EuZ8q-CYMLtVPL7SL5aIwTraqDvhzC7llVvLpVTWR9iaqPimhFAm4AhjbW3_CUJAe8i4gMLnEYfHarG4xvMxMU-On_nrJtOoPfqlZamhYNfkbsT3aRPA3xWRBWEjaD3oyk-NFR7nS7bpFioUH_zfRKbMe1kJC0vk3uaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
