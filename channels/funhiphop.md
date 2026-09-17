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
<img src="https://cdn4.telesco.pe/file/v0hZe25SdQvc3ExeX_cQFDLjjvyMlVkRW2xuD-QpV3MtXfPZbZITGBOb2WUTfYSP8hrevWFyn13F174I0xRwqOsx-9nzUCsfuyJoSuW6_RJvzErUdRbSYgRyvTRKqyapulg-f7lskrOZhE1mxcNw3Tuo0qqkDuboQrY2ircj6nfqSI33p91q5JlwuTiDVSjiGUERQHY1JgEJQ9pIhfmNu_3pGRV_vqAsYKem4GUB-SXJdA4LWZL5-JsHgJvEDRr0wwsFk_DJfQO45-kIvT7Ov5kzrLt11figKT9A5tyqCnbEQC39QQ_VarzSL9bQxkvl1Y7RMYlHydyYGkiy9ToOhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 245K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 01:20:28</div>
<hr>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کوروش: من مثل توی مادرجنده نیستم ناموسی بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/funhiphop/83653" target="_blank">📅 01:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تو همون دوران وعده وعید های پوتک، کوروش هم موزیک سیاسی میخوند میفروخت به رادیو جوان
خلاصه کون هردو گوهیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/funhiphop/83652" target="_blank">📅 01:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استارلینکا رفت تو کون کوروش
مگه وظیفه یارو بوده بده</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/funhiphop/83651" target="_blank">📅 01:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کوروش: استارلینکا سابات چیشد
پوتک: مادرت جندس دافت جندس به دوس دخترت خیانت کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/83650" target="_blank">📅 01:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کوروش جان قصد دخالت ندارما ولی این که اوایل ریلیز ترک لایک رو بیشتر از ویو نشون میده باگ یوتوبه که وقتی اتفاق میفته که حجم زیادی آدم هجوم میارن برا گوش دادن اون موزیک یا دیدن اون ویدیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/83649" target="_blank">📅 01:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbRp-I_Qt6pkjC0zQQ3cxG5Na-OX1hiBj1uInIeYTZwYMVMoWpV05aqSfrptg4_D8gkTWGCBKzaU1wDL4NvxiHPTuaH4Y8s8mkPva_b48_aaF2xGkPwtLZQ2SNBoZmoHmfdu7glxAFUmw0rUJafyPxG9Trz_oYZgOYpuxY4Te53n-kP0Ru2T7YTZMHfsMHv2v9IiS4NHZT0Bk1rBHItPOpdD1ScfLsExJVTUj59rlNwpOE-3roE_nD3WPkapMtTo5nhI1CR5JyYB5515RDUBvo8p2GrOrZCoNE7qWJ8--X1Z_kROc09UAbY0HmKbuiEfqMsE2yZwtmCCbhmlRbngOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/funhiphop/83648" target="_blank">📅 01:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آقا کوروش یک گنده لاتا مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/83647" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/83646" target="_blank">📅 01:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب دیگه بسه خیلی حال داد حالا وقتشه طبق عادت بگیم از بیف ملتفت با تعداد کثیری از خواننده ها رسیدیم به بیفِ کیا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/83645" target="_blank">📅 00:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNYNblqZEqZPsAl_uOR2h8Zps_qpjcOBzj5izUzhptk94GkGmxdj_hD1aQokpLrsHZirIayOfhlgrK2QOPMZzRytAYVl4O00_SjY6Q8-D-YfderUic8ZzeukZXpZX0UFgo6r8u4og5IknVFMM0M-7YJ5a8Ju98FFW_w9rukI_R_rAGy4_AnHqIvWB3c9rpq6Q4TGTuO8vsEFbPk7KDzy6MI0vQhis34ZAdg6-sVRrruh_IoUhOYkXOot417vjTOLwWbwIrmi-4VrLzRdIeik9Q_IoEvnbp499xw8pUHK0jzoLWGEbDXi294X4ufN0HbJ2fNTG83RxBqByodRYlngMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زودتر از ما گوش داد ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/83644" target="_blank">📅 00:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 تا اینجا کی</h4>
<ul>
<li>✓ وانتونز با دوستای فرز و شیطونش</li>
<li>✓ پوتک با ریچِ کصکش گو</li>
</ul>
</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/funhiphop/83643" target="_blank">📅 00:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عاشق کصکش گفتن ریچ شدم حاجی</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/83642" target="_blank">📅 00:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/83641" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/83640" target="_blank">📅 00:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/83639" target="_blank">📅 00:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آقا اینطور که بوش میاد کوروش به هلیا خیانت کرده</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/83638" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/83637" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/83636" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بچه کونی اینهمه مدت بلد بودی همچین چیزی بخونی و ده سال کصشر به خورد گوش ما دادی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/83635" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/83633" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVC8v9__T4vH-XHsFvr0tRhKRqWYz96MmtCFh83jrSTcCPe4QEVfwYP8UPDolT3-ZKghSOcPHTWQlxg1eJsup9AYa2t0J2Kj5yDzlj4AIF4_Hr5-5Bd1s_NNwErt6lHNnM1fFl12hIa8FoSILpOZTCizi-xtOTfpDfMjW8OcCdAkjVoHEndPjKmBtGPv5WE-wY9eigJX5naqd238kL11zYZ7aV541oe-wOihdX-gMd5_lWDAh-0ykLiTeLBvZLGrZVTE7Yms3loi5ek-0xDTt2CVYKhqs6OFbTGOR1_6S_0nKZ6aqq3Cuj1Pk6ZI4dj0oI4dbggL7fA-NCSM93b0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد
YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83632" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ریدم چرا اسمش هلیاعه</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/83630" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پوتک دیس داد</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/83629" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoC0DuzCtLj3qZFp1lm-87-YI9L-9Xvj6At02iTmpAC_baenlM84746A_tzRyXZ8Eo3kmku1IhAJ7jLkVfBfBL8GIy8X4C6-L5rWf3P6fliJ-Kb_jP05cpgfNQhOnjDNgQpCRYfyJksUFvlCBPgmpjrhGe62QAHa2B9Tibl2CIl0VHXa-Ydb36NUjxu8tlsp4otHZr-X34tChmPlsvlfCYvpJubeLPVCLXNkTwcggQrkQ3zmBLvDk3OM8Q-l8A7DTBZuf9g7ue5dYryl0cEKM_AqGhNX53dwAc1O9Qve-VV-RZWbJfJilVb9_rVLUwVKQuH0DmpSETlSlNe240A3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک: داف زدم روی داف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83628" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شب زیباتون بخیر عزیزان
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83624" target="_blank">📅 22:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کیرگوزی سمی لو کم بود فقط.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83623" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حالا که جوش خوابیده میخوام با یه حقیقتی روبروتون کنم، بابای من کلا یدونه خواهر داره و اصلا داداشی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83622" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پوتک ترکتو بده بالا میخوام برم بیرون</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83621" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محمد باقر ذوالقدر، مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83620" target="_blank">📅 20:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینایی که تو اینستا میگن "من از این نسل نیستم" منتظرن جایزه کیر طلایی بدیم بهشون؟ خب بکیرم نیستی کصکش به ما چه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83619" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هیئت حقیقت یاب سازمان ملل:
آمریکا تو حملات به میناب و لامرد، مرتکب "جنایت جنگی" شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83618" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMZ2dQSYTZc4sNSdzKPSz-EukmsD-NinixpCas1yLlT0IcnPiVGFmXnreJRE1bPOnZ0W9jAgHY-jm1i_FfyOygwtborzi_73W9iPQdYfYDUjdb-tk2-4YSkLVwMGR5o5-VXwMWVlC2TD3gh9xVnBhK8wdiXvfi-9SppSXCvwcUgdF14X66-KKxQbQuqtv6y7caJT0gKzepkKuRX9do-HrO_0v5KQK7Fq2OV1mVpaK-kQnxATT2R6Jf3ukWNRXvpygPKebHSoSl24Kd1fYHiGAnxL4hK5eBxzjG8g0XhuH69tIA21DMbWNelUG7q7lbPa6JemPcToCzA3ImfpIf2f6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی والیبال قطر یه دریافت کننده ۱۳ ساله داره که ۲۱۰ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83617" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این نزول خورا چرا ورشکست نمیشن حاجی هرجور حساب میکنم تو ضررن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83616" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83615" target="_blank">📅 18:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83614">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=rWiP6fciRUTlsA8EN2CN8QzzxhWzs1HVe9gqlTWvKBCC_C3W07AAuGJFGaPZ_dz_aNjcgsHPrAcwbuZhR9Vodo3EfyGTTko2yNWkuJv24fQKHWbvaEQSBH23OjnQNsJel4kMaddC6ii26rHsokYJbm-c26KALQg8_ub5zI0e1QnOmVAHf0kMPRSxEpZcZOwfgAU4mxPuXQNZU7Lm2I2DkAGAZupXIDi2bda3u48WrjFRg3523gBHpsbe_MDhLWgfXUlx1KXMi323Zl7xYJFrGhbUKBs0oODl0OyVYPsGP3ljIeoP-7Nco9Befjws8i4zzGmnqK-o3GZLOE4hgCWSMR7oNc48Q8Nj_EyS3q7RB_vuMy6zC9yN06C8rK7l4EL-VDVEeVHONtmAXNms__1aV9WY1w5acLJb9m-n4vVbBNSVNHsSpf1zdQ6tRI-lfEKf2NvJAHk1ZkIwTTasAQtaAcK5DpmT_0_75aE-aoUb-91G1W1bCUF5FVTJqJQYe1fzvuny374GJlkBq3RSpinghnqh5bgQgnTM7HfSl_JPCsJb-q4kr6Z6Ah1e8Rp8ncHkZ6XYQmRuwnJQnNdMZmkOByvHepE36Ju5iBcUwhNAstJfLq5nOu9TFFNF3K9b6t4i8lZJJVIsWiYhM88R2vRvk3sF_iC8bvTC6kUBXRKJzt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=rWiP6fciRUTlsA8EN2CN8QzzxhWzs1HVe9gqlTWvKBCC_C3W07AAuGJFGaPZ_dz_aNjcgsHPrAcwbuZhR9Vodo3EfyGTTko2yNWkuJv24fQKHWbvaEQSBH23OjnQNsJel4kMaddC6ii26rHsokYJbm-c26KALQg8_ub5zI0e1QnOmVAHf0kMPRSxEpZcZOwfgAU4mxPuXQNZU7Lm2I2DkAGAZupXIDi2bda3u48WrjFRg3523gBHpsbe_MDhLWgfXUlx1KXMi323Zl7xYJFrGhbUKBs0oODl0OyVYPsGP3ljIeoP-7Nco9Befjws8i4zzGmnqK-o3GZLOE4hgCWSMR7oNc48Q8Nj_EyS3q7RB_vuMy6zC9yN06C8rK7l4EL-VDVEeVHONtmAXNms__1aV9WY1w5acLJb9m-n4vVbBNSVNHsSpf1zdQ6tRI-lfEKf2NvJAHk1ZkIwTTasAQtaAcK5DpmT_0_75aE-aoUb-91G1W1bCUF5FVTJqJQYe1fzvuny374GJlkBq3RSpinghnqh5bgQgnTM7HfSl_JPCsJb-q4kr6Z6Ah1e8Rp8ncHkZ6XYQmRuwnJQnNdMZmkOByvHepE36Ju5iBcUwhNAstJfLq5nOu9TFFNF3K9b6t4i8lZJJVIsWiYhM88R2vRvk3sF_iC8bvTC6kUBXRKJzt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83614" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83613">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF-pcHQdMrBF5QkSkACbM-ekUSRW6Imhi9UamS5aFg0SMJKejjnbBsiPCrk9V4c-myXdWL4DIQgsXpmKCOKftJP4UTjMIODewy0FusREiTl5ul93Ydf9IKbBjXXAM5M5kqisu9ecuWMdqk9BWW7xV4y_GnaGdE4wMe0SudN3u-Jdcm0vvk_xcmDgmRHmMejIKFn66nV5Nu0vImsqNf2PofAGMjOsOmybRKgzl8Y0gFR16YRi_DmRnhsxdS1SDKEz7v-eGlmBDoxjTjrHy381x5y8wO6ZGzP65eKft3Cf12nxmdUkfGknjBG7X67vG8vFP7SYhtr6T7iUqlESzPSS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83613" target="_blank">📅 18:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83612">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2mPugfMhUeZ_SBlIEQ1MeC-9mi_AijgRFJUqET_g7VVVSWDm0-qp6IIBNKpRdr0q4AbPD1VQie-bl_4e-5_bwnvgzfkujD2l7v0MBhenelN2BSbICwNnn-VMbsYL851L3nAKuw-_2YcvQC4bGFVNJFn-crg6gHVMp3dez8z5v9kKL9IRRXj92FJy-mK-t_EMGlPqpOfarqKyIyWDNDe4TPPVv5XmOjVUQtWdmmJZ-Sm4a7Xbq6JpRrEX_4B87fTeuISWAc9veJVmz96T8J3Fxd7omARDiDnzmJdT_tUSOSgW3mCEqnf1xWNgMwsZqTKSHLlEPD0NUWB7npRvt-ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایع بازا به محسن پیام بدید برا جیبتون پلن داریو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83612" target="_blank">📅 18:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکل ژنتیکیه فکر کنم حاجی زود قضاوت کردیم
پ‌ن: داداش علی گرامیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83611" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83610" target="_blank">📅 17:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83608" target="_blank">📅 17:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tITBcwkphnLq5lfxbOpt9cs_DEBN1ZLfCfPgGzYv9q2DhdDJIqbPSxJU7oyu4KXoCuXwzYdX9Hf7J9M7yjCmkYHMAXybF2OVPt2f3F32FdEsfaq2a5cM7uocdMNcASyw3BCiOZfxb2v2GqvyrVhxMKy5pwBlEESVLtbg40egTMTgRlBkbqmK_qNnxjNWUPOK_j3W5XLDY4C6ZMxiKbmLsNxu2QksV_WCrzjdmc_vMTCiza5vYhcvNWFOC_PpWDTyycl0yCgDg1Mblg5rimUkBLuu-1Q0-bmIvLBTn9oNV0jBegJsTECUes1gF_tHeq4AAFOu7GS4e41VEGmE0tZi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewReleased
🆕
🗣
Artist: Young Lean & Metro Boomin & Future & Travis Scott & Mogan Wallen &…..
📋
Title: GTA VI
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83607" target="_blank">📅 16:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📶
منبع کانفیگ های رایگان
📶
🎁
هرروز کانفیگ رایگان میزارن
🎁
جوین شو عشق و حال کن
⬇️
⬇️
🕺
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83606" target="_blank">📅 16:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83600" target="_blank">📅 15:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83599" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyIR0SdYgF92ReTZB_VpWBRnM1TDxPxLGqtZgfWmtqrTi3r6abruDJ0DmIPccN_MMKr61YhRavUjdlQKTk2HKjozcUotDxLzFWnQJuRQYeI5mDfH7Jko_CjLA5jH4PAuQUITUBMzqpC__QbMOQC__idehfte_TzihhWxowBrwkU_qhshNTE2bGfLVkimKicuXAye7lS9sot6rEouljkCArtrA7eyECx8iFvVh2Mk6J1BE_W9m6PaTebGiRvan6klI46sRPFZzlgp1Br_Y-Xui-KAfjOO_venWbWzVIiNNdfTiuKQOY2YpvsVIfzd4Ku_8CKUk1psJMkl3SKj_3IE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts2Qlnl8RD8n_EWMXVkhTg1hTdpywh0LD_2w5Ul2DAOC8T2IJQ7fy5GxnPA_MAJDbIFNrN7A6l2UaNJvxYhsbFxXzK3ik1RPg-b2K-lBo3-tiISz03tPsxc8k4e-LXi7eOD4fKu9XRodqJeHyIjZEV4AmrblxTUWxzGZcUnDVLgmuvFyq57uIpDeGvWCJvfwvJtFV063F4a1MF8ydCTzafHWlCig85PlV6gWF-0OBV-3_0-pnxkAmittZKUMSG0oTBeTQ3XEek1sqw_LqWzNYTfP8b3Qy5Vg7CgtI4Ksn3VhM1-Mhc7Prah1nrX-iZfvqsNGxmNWGq1cvx-Vtdkm_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استر و پارتنرش تو فیلم جدیدش کم مونده دیگه برا مارکتینگ فیلم جدیدشون پورن بدن ییرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83597" target="_blank">📅 12:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqh7XleFP8FZdDRKPFQSw31bb1P-R7yCgBESAgHRp8UBYQqpNtU9CgFT-ucyprUt8k-7fwYI7JqwsecNf-bpV2Wz_39ytdFK6MhVJ6ZjOX2SoehHlGmgc9e0PKKnMHK4QZ7sh4YmJ3bNeB3L_EgAUkpRojJ5c-hUCcqQQpnWHwUDKqyUVOrR2PTztGZYIQS16nFN3HBmJ_kg85EJCFhlCa6X3MAmCDnGMMPLLbUv04aNk0I_ynNxCxCYHMhhf362e_7y670GizUq5XE2CbwJRxkrm13s3e-M4yM_5YVV-tIqxRfYR62lSsXgQVPE8ZB7w7Q_h_BRlaAvQO87KE6QDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی رضا پیشرو از ویناک نپرسیده واقعا صورتی بود یا نه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83596" target="_blank">📅 12:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNEcZmoTaXl8X1IWyty3D9IwbsiJAmQgmfHwrtg6Z0j4L6ITyZXCHqN8xcMP0cSNcB8lmg53PKJ6Jeq8OoRraF5ze54V8qYPQOohqXDuwiOC0Y8BpSdQDs5FNWEQXG8puiRMB8jiKwXc2hwT53tK9pYkvo4bvvEQeAJj5P96E0f59nl1Rr_9RR4TTMgwrQ_WwWx8c_4VR9HamS32JFoKmAt7SPvJ9wiLV6zWhWCizzIQh1ymJ3vZu76XS-2hZYUU3SeFeORvC0b4UZ_2oBHIyheLJBwNtiIjOLfsV2nhoBTvC6sagBRtfmPaMQcb8eF1T-Px4OHnInJyXpQhdY-iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیگر ترک پیشکسوت که قطعا بچگیاتون تو ماهواره دیدینش هم به جمع فوت فتیشا پیوست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83595" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esd5bjyIhLZcZ1J_DJjH8YS2ybQCBWlFfDOKyElBm-CIRIt3rMzH2EMe6eNLC2gticYVZDKumbxRhMv3I9_RSTffHMWh8ue1HvVsqzUdaIneldytDxXcwLNH6hcqB8FHLzJfLmUYBInWjjZIff7te7fQf6nVCXqesx4YVka5-ZRjjrD5vWj3LuGngiSUneLgcmzFH5KE9JDvpKI1OrWKRoCoJooWB9n4VM7Zx8hLKiL8sdGe6bXmTCJG1CkZF6WjjFlthGwt727o_hV407PHsEg6Uqo2L-DkdC5jRH6HglSkljbhMvgWKvL5cyCoFSRtl1QyCB3qpbB6ugcKJ6rtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83594" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=Q6sAgZRjZy-aVB37IuZAGQffxvaKbbqYyiIQ-QfcQ-qIN1f6n2TYZQ1pxfTMRfI_Q9Bv4IbMP9fmldOWbj80L0uzh4336vaHcCERsDfN4DIDxMeRC-H6lEwl2Pid4ChHkR4vKUz6JAg37keRWQzoNwLtBJhJmjfBuKJq2uW17BkgfKH-9j7gqMdcByDddxy707PBF_xOVCH5wI2meVt1iE8IxPW0Gnac2MQK9Qc5tvOoPlSluWyVAXxIfC-voM-KFa30YQGqBW_wKTG0WEISrFoRhN8sKmIrJHbGePRPgLapgNG4VB4fwt3XV6bq-Pbh7PKhbBMywI8NIGADGj03Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=Q6sAgZRjZy-aVB37IuZAGQffxvaKbbqYyiIQ-QfcQ-qIN1f6n2TYZQ1pxfTMRfI_Q9Bv4IbMP9fmldOWbj80L0uzh4336vaHcCERsDfN4DIDxMeRC-H6lEwl2Pid4ChHkR4vKUz6JAg37keRWQzoNwLtBJhJmjfBuKJq2uW17BkgfKH-9j7gqMdcByDddxy707PBF_xOVCH5wI2meVt1iE8IxPW0Gnac2MQK9Qc5tvOoPlSluWyVAXxIfC-voM-KFa30YQGqBW_wKTG0WEISrFoRhN8sKmIrJHbGePRPgLapgNG4VB4fwt3XV6bq-Pbh7PKhbBMywI8NIGADGj03Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بیگ شگی که رفته کنسرت ابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83593" target="_blank">📅 10:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCvZiUVmchn6YDDdPUpyQVJfmiyXO8nH9aF-zBfczUcXnpNtSHyFH1rvsA02PcFFbmPDymVt7vWM5WDGadVjBD4D6UuEPf-Xzw8AV9HsxZp9mavYTdQrH2jwIXLfVku9wJEOFYpWvx6dVpyn42qcgPpr784vX6g8naG3YYJMkkINBjjZOcXw6-YaQQWw9v9pYzsv_EwfIXC-kEez4uvOQEU0p9afAjvXs38oteq82EWcwEIt2sDvLdgdOcfX7_V5WZQTs3Fe8_hjAvMm5mk7e2C0sdu0Ic75-kdNGn1kF3URJXkfECFBYS2lkDNvL_vXqpkI_BnDimnCNS3tQ3uK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا کریم؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83592" target="_blank">📅 09:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از باگ های تلگرام حامله ام
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83591" target="_blank">📅 08:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صبح دختر خانوم های عزیز بخیر، پسرا ایشالا بلند نمیشن از خواب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83590" target="_blank">📅 08:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkDrhnx0WwRKxENMRZ1G8k3lgW3cp0RLg-nPw7mHZZmE59ikuPIeJLe9RsKBHYbIBMVq5zr-IkZJYvMsRJD62rilygoHiqK999G79KY5vZEUCdfNuNFy30yR5lbGWCeCWgjXVimI3TpD-IGMWpYSJlkY9d7sr_Mj6qfS-3e9Ltb9y-3koRhjVNzUoW6w5YhH2nh1oHDLhMZuJSHtkhRcqV9-YUC_EAezCjBQb1XH3lraZRzqVoqvNH7_fZnOkYG_Ku2nhL_Tw-gUntUu2TgQq8NrmZ3wIGieukRKrsg5JrJSx169lkwLeEDvZB_0T0ZHQHwKa7phoGscbwteTtkEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5F__3kuTumwcix85PjMVZpOsyKdIO8NnPJJgBpJsw08am6Y4z605AykI5n7n0PjyTRjiA2fNgsO2sGkg91R_vNGklk3xX5TP0PL1rFbeR3yVpDRN0jrcdb1_e5p6oCFT1eXR2Ywicf7Q6wAH4tIAIk8RkqRP1cJoLHcmkybSOt8ROG-rV1hTwe5MQbEEEBp1EUfBTBmxXmUqcN1PFkGTcJ-DVfN4EN-VdZJq3if6jX6zbyYP8o2VEcPO9L14Z4V2JMX3cikBBGpvUwGqjnuI4VwRSxT0nEVa13_capRLg6gSPGGCpDN06CsK92i29fERzUuV6AXGnMO-xlAoqi8Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علی ضیا و زیدش تو ایتالیا شکار شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83588" target="_blank">📅 03:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83587" target="_blank">📅 01:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8Tv6wPxS4qfqI9d53lBHRZIiOEj0Ygb5jqSAkflMMHU2ZaPVCTN6-EJ1yQyj8funbTlqkxQ90m4_uMazmGqrj5yIOURbXtIGvPc5Sw3gyh1PaZ5XZU2rMHyls2rtEn5J7mZxyLTfxV_Rgh6O14ot0UZnk5CIlm4ik-pAH5wq7myAz592FWw4YkiNq_J44AtBcyBmWPpOBit3YKB58kGEEWYrzs7tonOBdPcQw-DpzDlYAwzC44AZ2IR947vSzKZ-ABRlkEJHnnZuJzbFoHgQr6gYx-S_A3hP0vh7CNfNgWE8Znsy2yhoiANA6kh6QOrrLECuzE3CXMZ-D7KB1cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83586" target="_blank">📅 01:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=W0QbB2HUCSQ9ozgmMrLg32WSjxDOL-9JCTu_tI1r_h6hpHzcz8hCShZeeG0UfP7Emij62uh2L9VxYha2-_GxDE6wN49bLQNkBmGQR4SMd6e8bCu0q75uHPNJGVRJeqbX9Tb1AUIhjUYL1lnjpcSpRwY7v7XVHZEgsRG39Kwt81H2d3rBpcWT7VszqjFe9AMgHpkd2TuDYMLGPxHe50SBOJmv_1SX8nNG8NP1tqgcXJy1fmDC17eGdaVcDL5RAzT4JFiC-HAnHfd4TVKAvBS63MYK3nNhapUy6uRcGuW7qvRmuUaKgVPWe27uohQ5v43OZYtXO81aAXfFQPsWDbV0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=W0QbB2HUCSQ9ozgmMrLg32WSjxDOL-9JCTu_tI1r_h6hpHzcz8hCShZeeG0UfP7Emij62uh2L9VxYha2-_GxDE6wN49bLQNkBmGQR4SMd6e8bCu0q75uHPNJGVRJeqbX9Tb1AUIhjUYL1lnjpcSpRwY7v7XVHZEgsRG39Kwt81H2d3rBpcWT7VszqjFe9AMgHpkd2TuDYMLGPxHe50SBOJmv_1SX8nNG8NP1tqgcXJy1fmDC17eGdaVcDL5RAzT4JFiC-HAnHfd4TVKAvBS63MYK3nNhapUy6uRcGuW7qvRmuUaKgVPWe27uohQ5v43OZYtXO81aAXfFQPsWDbV0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجوری که عملکرد بارسا رو میبینم بهتره باخت فنی بدیم حداقل ۵ تا نمی‌خوریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83585" target="_blank">📅 01:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عاشق منچستر شدم، هربار میزنم رو‌ حریفش نا امیدم نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83584" target="_blank">📅 01:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه تحقیق کنید ببینید ادیمی رو تو بچگی همزمان زلاتان و مسی باهم نمالیدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83583" target="_blank">📅 01:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83580" target="_blank">📅 00:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83579" target="_blank">📅 00:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">منچستر فنا واقعا بدبختن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83578" target="_blank">📅 23:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانسلو رو بیارید جا رضایی چه موشکایی ول میده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83577" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی به فلیک بگه داداش زندگی رو نمیخواد اونقدا هم سخت بگیری یکم شل کن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83576" target="_blank">📅 23:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جا پوتک بودم ربکا رو میاوردم تو موزیک ویدیو دیس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83575" target="_blank">📅 23:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پوتک و آرتا چرا متوقف نمیشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83574" target="_blank">📅 23:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اون موقع هایی که آداما ترائوره به خودش روغن میمالید میومد تو زمین باید دنیا متوقف میشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83573" target="_blank">📅 22:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اقا اول تست کن بعد خرید کن!
گیگی فقط 3 هزار کانفیگ پر سرعت
🫆
شارژ حساب کمتر ۱ دقیقه
✅
@NetingVpnBot
@NetingVpnBot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83572" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه (پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83571" target="_blank">📅 21:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه
(پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83570" target="_blank">📅 21:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینا مگه تا یه ساعت پیش به هم ناموسی نمی‌دادن؟
چرا الان دارن با هم رفیق می‌شن؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83569" target="_blank">📅 21:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پوتک پری روز گفت من جواب دیس آرتا رو نمیدم کوروش دیس بده جواب میدم
واکنش وانتونز چی بود؟ این حرفو قبول کردن و کوروش رو اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83568" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پدر عجب چیزی داده</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83567" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حاجی تهه ویس ببینید چجوری با خجالت کیرو میگه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83566" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">از بیف تلخون و پارسالیپ رسیدیم به بیف این دو تا یتیمچه
عجب پسرفتی کردیم پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83565" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آرتا درمورد رابطه پوتک و نسل چهار و خلسه:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83564" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حاجی این بدبخت اعتماد به نفس درگیری نداره، تو ویس فحش میده با خجالت فحش میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83563" target="_blank">📅 19:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83561" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83560" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCIhxPbvhcD0NfzmO9LFAbEJ5qu1L3MwY_w7wypGKCCeKmczF_AUQw-lhaCo0-vcAhZXA5nFN9RRSLBaPzY4XDCNvZ9xM9TgmfTmfBGObAE5ViTCVFZ0iPZnf9bqH2LVwSROA0G6PbtpKQMISDI0adUEq5-_V0TO_TGRohsv-BdUtNgb81Ac6ohGUoL7zivi9VJ8NE8_8Lw0xaGHjJrL34R1BqkH2ySIls1bCzrqahqmMRDg-jn5o5rlbLtwZJqs1-NiY8eXGtA7gMHeI7-YAUAEhYLnZzSFWd6CnBW7l2BcaVJwh4ZbbI1Qq3QePo1ml_o7qswoncgseG7t3jQ1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یکیتون این بیفو گردن بگیره یا آرتا کص میگه یا کوروش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83559" target="_blank">📅 19:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpsKSW0WG20O7LZxM97lB1TK0JKWkj8TySuKKIpmS6cJ2-dkvYs5oo-3mtk32wTk6GZeUh6Rnjf1uMqEfIGAbc_sm2CHyiHTpYHHksbK9cAsXpqV3g6HWIO4scj_KVVKyPPOiFrDQd5GahqWaVMm1AmTEuYiURIMj32uC7cDHL0niYeMAHUBOQWk00NZ9x5UnpI-jVsE5_nDNqOEfO3QyF_X-LetdF5gll_D8pFAftqTxqzTUDyGcqLjn5fVkOCXhlj4ecsTtpNEUHXBpsZNhSb7UmjMzZM476NcnXIZFoo-KLGJOu7AbCX8QroyBn52Vrmq92wlW6_28xMHZVkqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک فردا قراره دیس‌بک بده به وانتونز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83558" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83557" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkC6TVrdGS43fEU1Xtdr7VtOcTe6ZJiFqUH_ilz7GzQiNI-_3VWHs3e4UrBaolJ6F5spGAcwwRZeyDdn4sFOeAKlTktzR1JWFN3XgvDEfGP6f4nPlNteQArAIGdOqSUfnbtzriKUjOyaIKvZ7Y-U_LauaZfYy2nUMrgovEVaeB7tv_9n6gczyEZm12DdDs3TId6d6nGHQcjJ5loyh5-2LCOKqBkAMsMrtJxE63DJ-gNHDjsDMUes57dyiDDXsZv8ee1YkiAfKapATI3lQF7fnZZm8x6bdf4srYoqRPqJl0IjXVKIcsNfXI15vWl2MYVp4TwLNkQp86Ri41srLlYbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
25g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83556" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمایت از هیچکس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83555" target="_blank">📅 19:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آرتا و پوتک یه لحظه متوقف شید پدر ترک داده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83554" target="_blank">📅 18:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtfIPpN8zMiSgi41MHYkzH01ycmPV_p33XmejnaWmsrYvu3B22M_GeQCx_CwDvduEZv-huSNom2-4nKthCaCoXSEBFkb-mW_W4Z72uzVGi5x3kfGPd3v_RRk3WExzUdPrs-l6YGASh_VPXKFlRLl9pM2Du6eybntRoqjqW5NquRuWZmOPvdijBDrh3Kix7bwxEUKTbzKx4QPWUxwIvfzQCm5Ptbhc6WprPtpR141omA-t0Tvd7QsKjnbGpzPqWJnjsnJaS89EPsPPFZKeHWP2s_uKUJCrNtz0Etiqwhp16-9JHykRYpreaUYUclFJ8GasZO4zaRJyQSJ-BsCPcpt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=DBHRVhfdpKH_4nYA7DUVtXaIlyZmzqZu2CHr0JaZFNT-hJ66z8wdp3zf-jpKQZVNQBdYwVC-G2FgBvfraEgxpVQrhE6fGV15b8I7JKNqynB7DCTTObxdoVy39oGIFlW7fJNqgeQor5GBP1nUgguJv3wcbvHVBbnzuSoE1RU_OO07lzTurpKQyB-gCBd-dMIWOkUAOLz1BmVbO0IMktwO3A3zNS75Kk_I7jqdf-HYBVg9UCywwvpVGq6vk-UOS9K5wN78AZnirKe6iRZYLAloV5awB2tDNzEJT29R1VGsCQSre0QXomQLp-T1_iA_o3Wa4vgi7imnOt7tnFL059bPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=DBHRVhfdpKH_4nYA7DUVtXaIlyZmzqZu2CHr0JaZFNT-hJ66z8wdp3zf-jpKQZVNQBdYwVC-G2FgBvfraEgxpVQrhE6fGV15b8I7JKNqynB7DCTTObxdoVy39oGIFlW7fJNqgeQor5GBP1nUgguJv3wcbvHVBbnzuSoE1RU_OO07lzTurpKQyB-gCBd-dMIWOkUAOLz1BmVbO0IMktwO3A3zNS75Kk_I7jqdf-HYBVg9UCywwvpVGq6vk-UOS9K5wN78AZnirKe6iRZYLAloV5awB2tDNzEJT29R1VGsCQSre0QXomQLp-T1_iA_o3Wa4vgi7imnOt7tnFL059bPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83551" target="_blank">📅 18:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مستی ناگهانی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83550" target="_blank">📅 18:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83549" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83548" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_A6E9pQVz0U2lBRq3HenTpIX52CnKCQwGAe3qkXZ6ZxxAchefza0UgIhNM7FsOhOuIvld56xrMPOF9o0gwy383-susWX4hMYcm-kCwcKpcnDPef3P9QHRaUmOYhnrcqI8y-RwcWFj2Yo0f_n-li6eQZkx63X3whkgXbfNb8AxQM9Smle9h77BV3803abZBmcKXxUVjW3CcfK-09DumhFbyGve88N3ZV3EESxHPCu9xxJGeyVHoOiUe4Wmnkmwph9nA8q7wQnDNPStwyIYzL0gkxK49bLLXp51gDNMv-nFr1hlrOfpRIyW2HFrhumd68sS0sRjVHw3i9lwZ-Y9bZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83547" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بسه دیگه گاییدید پوتکو
کوروش 7 دقیقه دیس داده بهش
😂</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83546" target="_blank">📅 17:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKljqFP8BbFaBNZ0GFEpSMkYvHBI2vAfHhUFdlHTJvt1pLPZ4uZkMsA6kUqEpEDLjO4yvBFKauOerNrWNVspoxuhhRwqbzbodb-TrrBeHTaEZ13YxiMuE9IbfRR4SC_HehESDBTiVuvU04hCP8O_RwvctHIac4pvh8dshcT0Rkp3Fc1nWdSh7Ts300VjNsQww71NZYgR-jh8jidUZNuji-3_YiM_4qQWMTOgAWYWtvsGpvjlr7oer-t3Ct65LHoJDQ1msvxKW1hGAQpB0cM8y4s-Niw82FJMdOwWU6fVWvB_Wu6DLMhiTiMkKK-qmx0z0Q6XB9vwIpoH9t1OUGDDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کی این تبلیغو انداخته رو چنل حلالش باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83545" target="_blank">📅 16:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83544">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به بلایی که خط حمله بارسا میخواد سر این دفاع های رئال بیاره فکر میکنم، تنو بدنم میلرزه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83544" target="_blank">📅 15:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پولدار شدی ایرانی
کالابرگ قراره ۳۰۰ هزارتومن بیشتر بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83541" target="_blank">📅 13:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi19_w0arWr-USCi1y5cgQc-vKyiHbOWeQfJT3WXrCiJxHQ6l1aJBIEV8yjl0qQuDlg-XncJvGSfUZ-X1kMeHwnIb7vLwQPVBvCRjGCTWqTF0dpluFB-issVooTzAqmlOGBitYNuihqpghLGX7C4W5G3HYYmWv99sPVPLrTGGqXxbPnlSY9ZS56sY3ODC0Jxs2IEJ993di6jdUhoTh-IPOYAHIGaJ-re9TjTdwOLRA6pQyXTV-bBEmSHLk-JSn8XLFuXYAXOfB5FO7giDolNPSde0Bx0HzgTtltOuW_zKp84xJxilqfHBkt4HNIdfsQ_PFThnFyjUiHJdApzGSQ7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی منتظرم ببینم کصکش نبودنشو چطوری قراره ثابت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83540" target="_blank">📅 13:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5ontiJSxtTHl7s7S1ADIHPFogDb4Tazz8J0S1Sk9MsbYPvfKE6BSMYyIKrT-2OoEHUCMoBQdCG98MD8eWdYK6JWQClvL1_2hMSlm8MRu-eAXyQbB37JmwXWeR7z-dVNc7NcV78k7BliWkwUgOzAKUG_NVgx9nK53sPVMWgZBLh14mPJxFQSjd2vMMLEaPunVbz2XDXcM7GHgj-ASH-1e9HqIEsWc1EOc8LQpgICoSsYmyBNoXBdJFcXFz8NHlOR6b8NQNiI6kYnnl4cWa8kYjEYfJpY8w-Gj1VPLOrq50pzQvDT0uSo4HXkW3IUmwFIVFzdQoeYeXJ9GNpD5TyxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک الان در همچین شرایطی با آرتا قرار داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83539" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spinner</div>
  <div class="tg-doc-extra">KVIRO</div>
</div>
<a href="https://t.me/funhiphop/83538" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83538" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV4oM1sXvV6pgd9tElhDwRhrR_uXbkly9urSYTOBr7NaWifxOQmNCiUT9w37pfFYJIHBymtgvvMVar46CIe_Iot-jbZdpMSOSsz6FLKK4p8bXvQ5dw695f_VrP8uDmEc-ismmuiA0duF3sO5w3KdtUdz9-wr76cp9dsIgwpBbZjv1AsULt4xfl1nuuJeAyVSYQRmlCSATvDMOpWx1_f8FbDmSfCEqcyR52Prtm7GgnbQle_5J37hmt5xVgfVlyjhkraxQe_V_lm783_maiHGCY3jHEUlYWBJ8zY5d3nveTZFe6ngq2BBPZ0-o0XX6NPR_J5zYUOX5bOlA9uOFPQa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "کای‌رو" به نام "Spinner" منتشر شد
SoundCloud</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/funhiphop/83537" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83536" target="_blank">📅 12:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOkyUbah-T6LfuobaqiEwW-JOIxDZoDzZ66c_sVKPV72tXjzju1c2inpGy8DZLCvsJsE-nCgZMjYIuAaLj38C8d0rnDI-x7aqrqA40nt9q0rg5I-KHif_XbNLKR2UG5S_EO0KjE2o9tLx79dHZCi45FUjVtePXWNnz0ASd67KPB5QVuSfCuXaQr7bRDX8lce0D1mMzh-wp9Rda_Z6_yqsn3Q9NBKxf5tQRQNLWqMavs57ya5-Pc_1uMEK1bgLXeXU8Qm5BgjzZhBmoer_XYPfzyeyiZ6bJPD4dzlhhvS1zh57tWliUC-_R9lk6yxsLxrHnep8XQaC-qW-r_GTqSs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83535" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83534" target="_blank">📅 11:11 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
