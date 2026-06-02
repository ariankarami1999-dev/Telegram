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
<img src="https://cdn4.telesco.pe/file/EDjlUR64-7dtKS-Oqj-V1mDVdO_ARXiQr5tJC7WCZfydz_qiYjUmtrfaN6bhScpqZ2D6Zswanz6PZFQ1eGHMXXVnRQXf2Zh0mKDt89u192-qE0o7MYI3UtZA1DDY9OhsOJ_K62ps8A06TLqZrnuE0yegN8gmvR5DQmA06R71K4Sg3Iog_8RZAhkH_K0XkGU826I_st6A6TpRfqcE3aQYnVk88bCY7c5Vr3u4kYb7B2VAdcyRBzMdi4k-yVXZuS3vvIHXbsB5kUKK526cb149NZpsaiiH1A5lVIvMjYiH_vD2aztnb11IL8fXifJnbbKVPuyuhpm58PtskigT-UjP1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رومانو:
کوناته به رئال مادرید
هیر وی گو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/76657" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دور چهارم مذاکرات اسرائیل و لبنان توی واشنگتن در حال برگزاری هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/76656" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">معاون شهردار تهران:
برای تشییع جنازه سید علی خامنه ای ۳ روز مراسم بدرقه در قم، مشهد و تهران برگزار خواهد شد
آمادگی حضور ۱۵ تا ۲۰ میلیون نفر را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/76655" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میگم اعتراضات امروز دانش آموزا به کجا رسید؟
انگار تاریخ امتحانات رو یه هفته انداختن جلوتر که
😂
😂
😂
😂
😂
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/76654" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حصین به نصف رپفارس رید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/76653" target="_blank">📅 16:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/76652" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/76651" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چقد داشت تلاش میکرد وقتی میگه کون لباش غنچه نشه</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/76650" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4W3vZJJqC087EreGHazOABkAiNUnmLoJu037Jijx-gU4R4PsyxuYy0xML9lh7VH50Ct8sf68iBZmDgvYYKLH1fPZmnSxV_ziS1SgrXN3JZmngH7UmmMiMLHgYoMORjiS9HEC_fKhN9snp3Ibd6zQLPv2LPYN_eEx3FtOJ5L2pWxNzC69JUelD9hYsM5_NqVdpfUHS2W35IAGPZQS0CvcAV7Wuxg1xXvJRPBcSgcYSAYW_SH4veYcvYqLUPbd_YreLLfOySxJltMQAky63jwmYFTly6rlR8jAWtAwCRqfWalOUmA4af9GlLlXBgJ2DEOutIAIkZrU4WHePHWuH95sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی مشت کونید همتون</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/funhiphop/76648" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76647">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حصین یجور میگه ویسایی که ازم پخش شده کار Ai عه انگار من موزیک دادم گفتم "گنگ مثل رهبری، مثل حماس پی حماسه و..." دهن سرویس محتوای ویسارو تو موزیکاتم میگفتی دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/76647" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76646">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کصکش دیسای پنج سالو جمع کرد تو یه ویدیو ۲ دقیقه ای جواب داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/76646" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76645">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حصین بنده خدا انقد فضای رپ کیرشه هنوز نمیدونه دکی مهاجرت کرده فک میکنه ساریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/funhiphop/76645" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76644">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آنشرلی با موهای قرمز
😂
😂</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/76644" target="_blank">📅 15:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/76642" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به حصین دیس بک بده</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/76640" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پوری پاشو پسر</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/76639" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گنگ مارو تروقران، به چاقو میگه نایف</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/76638" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حصین به نصف رپفارس رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76637" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FblDyhL-7IP6pG2R_EqQSHyW5eps8VJ9t1g935KRwdcu-jJhYSaXNrfna70O9EvIK93XBpt0RlnTelZUkRWrCj0aEUVatFBA889xHkIgXPgWGea6fMmKBS3cHgeX6GfRtEqhtp5dZXcir74kDo6Ah45pm71XRkhn2UzutvmzHsQHfKT12tav3QxhLdo9wht093qjUMGCckhzdM3PIGsgvrqykY7RSI1VGnQ6VYLTZQIZMAdQQMBYsUm58kXZ0jw3Cdh74PZnlSQBduOzbqcQKp7y04P-s1zVTq4qEFHQTO61ESuqkzzpNHqVGMZG5HwMiyzwFltfUymBB-to6p_HaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط ابر بنده خدا چرا اوبش زد بالا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/76634" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده، فروش سرور های نامحدود اختصاصی باز شد  یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰  برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/76633" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده،
فروش سرور های نامحدود اختصاصی باز شد
یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰
برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps
🔤
@Behdad_sps</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/76632" target="_blank">📅 14:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینترنت بین الملل باز نشده
درواقع فقط فیلترشکن های رایگان وصل شدن
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/76631" target="_blank">📅 14:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سفارت اسپانیا هم مثل سفارت فرانسه و آلمان تو ایران باز شدن و شروع و از سرگیری فعالیتشون رو اعلام کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/76629" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxI0wOH1iNiTu7o4IZQsKM4-r5OhuGy_6tx103XrfMgzAzdWRA0Ck-HmI_9cYp7oLCpU8b9T_26dO2OigGw8hxU4YktD-Ej-d8mv83WdKcHMeJZox05SXiGoNxA1loI410iLoX7lghLqqSAB0y3AzwYhzJrD2PNB6iw3Xxct6Ark2W8V6oO13XyeEhC5-04SzltLZuJcwuvmWJk57l8PQdWV8PhPk78taSIqGnBE5ndFrajIlHuPse3XNyUXN4RkmSM9PybmdjPGj4poFDGlpArnXFC43QIc4HdkPOJJerg5vLLSmQAVt75s2hOUD33vxTSGPoKaOUmcaFcMxPF2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76628" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۰۲۱کید من هی میخوام مسخرت نکنم، بعد تو رفتی کیت آرسنال پوشیدی با پرچم ایران داری آهنگ انگلیسی میخونی برای فیفا که پرچم شیر و خورشید رو تو استدیوم های آمریکا بن کرده، حله.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/76627" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تنگه کص نمکی رو باز کنید تا کیر اتمی نزدم بهتون</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/76626" target="_blank">📅 13:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کارت فان هیپ هاپ هنوز استفاده نشده و زیر آستین ژنرال ها و پاسدار های ارتش دو کشور قایم شده، برای همین تو گزینه ها نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/76625" target="_blank">📅 13:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوبار نوشتم در نهایت، ببخشید سواد ندارم شما یه بارشو بخونید</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/76624" target="_blank">📅 13:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 به نظرتون در نهایت کیا باعث میشن در نهایت خار این آتش‌بس و توافق گاییده شه؟</h4>
<ul>
<li>✓ تندرو های داخلی</li>
<li>✓ نتانیاهو و ارتش اسرائیل</li>
<li>✓ جمهوری خواه های تندروی آمریکا</li>
<li>✓ هیچکی نمیتونه کیر ترامپو باقرو بخوره و در نهایت آمریکا با ایران توافق میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/76623" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فایننشال تایم: رافائل گروسی اعلام کرد قزاقستان آماده است تا ذخایر اورانیوم 60% ایران را در صورت دستیابی به توافق ایران آمریکا، تو خاک خودش نگه داره.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/76621" target="_blank">📅 13:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/endSKoAJmW0Xr8vsPE8IaHa3UQSX5qakWrARgeujDvz-8sjM5Ly83mNv99MpXO5TzUAOC5Nw_xsoKPDVFSu9ftELzdpA0RunbemRA_1SvzRdFQ2PpxqeeQ5iJ-oZuqewlob0pWY6WJqfslzHLUm3a-V0oklaCdiMHAtuig93As2mD9sCRmz4LsfSnia_ODkNf2zw-FKlHXKIBDalUYM7IUyrceYPbR7Aurxzmis_Bqlwbi9M0Y2NhFsGdhu8TTKq9gM9Et066TCEIaP9fQvTen6lUwywx81TfyaDwMApW6M5eLjRLT-nJX4rBW7h1H3Z8mMklLspvSjzP-o9PURrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دستور تخلیه کل نبطیه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76620" target="_blank">📅 13:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76619" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍓🦢</strong></div>
<div class="tg-text">میشه اینقدر با مزه بازی در نیاری این بچه یه سال تو اتاق درس خونده رفته برا حقش دختر بازیو جا دیگه هم می تونه با اینکه کنکوری نیستم قشنگ نبود حرفتون</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76618" target="_blank">📅 12:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76617" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=Rf_QPJZxO7d2lt0Del5HqDcqpX2PYf08D2HFK4tH5sBUG5ZYYEnw9pZgW8VTG-ZqZnczcliGujWWA4nJ5TFeZCREIUWhqjmdy1nqyV5_XWsgauuiO7AsHj75u-xv7UzGpgESDslNl6zXIoI3ypc9hzRG0e_ZUiN-86GARD6vPlazRWr1jx8Jw2zOx_hVQbq1z9qBPFJkezUk43vyGC1tisQRGRhzNO_aRWmyupbZCmwVYpF4WQeYPMQoYZKEAdxSVwaxnjG83Dct_a2W_4_yTRAhXG1W9KnI3BTrKU8Bwt878FoNry1vIAvll3evkt1t_y63q1SfQwGh435io9-d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=Rf_QPJZxO7d2lt0Del5HqDcqpX2PYf08D2HFK4tH5sBUG5ZYYEnw9pZgW8VTG-ZqZnczcliGujWWA4nJ5TFeZCREIUWhqjmdy1nqyV5_XWsgauuiO7AsHj75u-xv7UzGpgESDslNl6zXIoI3ypc9hzRG0e_ZUiN-86GARD6vPlazRWr1jx8Jw2zOx_hVQbq1z9qBPFJkezUk43vyGC1tisQRGRhzNO_aRWmyupbZCmwVYpF4WQeYPMQoYZKEAdxSVwaxnjG83Dct_a2W_4_yTRAhXG1W9KnI3BTrKU8Bwt878FoNry1vIAvll3evkt1t_y63q1SfQwGh435io9-d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76616" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76615" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYoung Roque</strong></div>
<div class="tg-text">حاجی توافق شد؟؟؟
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76614" target="_blank">📅 12:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evBBdw3dQeaV-mnUsSxLKEr8B_5kX51eL6PFkKz8Mb9Ocvu52oDrJ9_8vSMOSuHolDnwpQte0ryYy1wI4WPIK7__r6aq-QVyT6oprHumMbyTUr82iWOwI10x1WtpUsIndjg37PzVLeA5bDtjjd-Gdrs3zYQkYPkoMRcCdhMf5G3ynyF1EXOisbttDvb3VhXqGfms_iMGDLeC22LC2_BLhapEf3LhD29cod188_xczbWa6W7v6KqejBDiHkZXjx64cSE4ZwWXqNzM7owz8YAtJR-7aa67h2BnDWTlXLkCnM00EwxB5rLR4aQLUALIVLFuhFRej9M4Bg4LPimoHJAZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ به نتانیاهو گفته تو یه دیوونه روانی خل و چل هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان همین الان حملات به بیروت رو متوقف کن  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76613" target="_blank">📅 12:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دانش آموزان الان در مقابل وزارت آموزش و پرورش مشغول اعتراض هستند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76612" target="_blank">📅 12:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس:
ترامپ به نتانیاهو گفته تو یه
دیوونه روانی خل و چل
هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان
همین الان حملات به بیروت رو متوقف کن
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76611" target="_blank">📅 11:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suisWaS0OoiuQsVbZMYm8p6svVUF9g3Q0_HQCsyMEQGw4rmd-SJyoSeXHhErr98SGKNsnrrlmZ075kGHrZ39DCaXR2bz2ly6q_qGj9nXIWvVFv6ulOog1XaLWP8qpejfNKUiktj5st5gz4vVoocG6uBpbmOqO-5zyRjA3BossuNdBZBUh19vMIRWxRosedYw8vqZnCg3N-wTvu7qJmr1aQG5j2ubsY0Ivh5maL7HmGDYVs5GiwlY3fL3F6x5ateMOVQBlepa7gKG1-IMxQr4v76BMfOSBZdDk0269W8JyV5wyCAyWw30OPCeciRNCl9EyHds-Ei7dxfQVThnA8ogZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه مادرجنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76610" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdjphtfk8e0YdkaTxXBTVlwVMSF-5q55vZkYmKlcwpCDiZe1yxu1M81zYlbjOTMAAKQabVNlM79hxOWxZ4h9qkDRLEnboVV44MUw5BRdVTX3eiRALDVzyyoVIWben_sU8ck1moJchs2S0i9vtDnh2czW2FnNFrQwBjFv-h2LO363b9BMjvhOqLhLCJnEdrWSwzEvsPfCrhH_svvAEdz1GaoqNDHMNa8fvHrVlx0miPp2oKQZYC1ddVGT_VSpmvrbEW9729lviS2pTiuSBHJwV-7_QUFehIQdLX-LbyfURGaE0oFEYhqSkNhdSTu32QZ3GgVgl9eI9EQYyhMaiuUqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون شبی که تل آویو اینجوری روشن بشه روز عید ماست !!
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76609" target="_blank">📅 10:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5CpX_pLq4-ftJpi1PIP4NZdl4_VbuDnu2SXg9bpE76pX3_BXuWQvAbCvw5XBTX5lgP8h1bTTCHLiHxk8DYgWOBGjieCxAcQqU2pLoD74RTK9sazQmGo56qdiertWZk4Iq32FH3E6JbvT5XI_LYfUKchvTYqa1F3bkTTr00rxJome3w4aX6NGE9YwqjJadSz15Z4TtEwFyVZROjXDZjbI6Njj44JaKX-hdExKQXMhtW1HuKevB2f6MHOGc1_aujK4_p9MS-_9iZWyz1Bdi2NJx6LfCAJ4TX7axJHSfwGiTvwK1JnEU4s_TebJ3iKEMmxURGSh0841D2_jFmlpixeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت رو بخونید و به پروفایلش دقت نکنید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76608" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/76607" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCqvkIcWw9VcqOkcg-cr_HuLdiecrYPXMPvPBR7pXbey1370CYh0xblBh7qIpW40-i3qtoNhX0IL6kSANPFpIsBY7pZ1x_c5yFnGh-vdhWhC652T4P02AlpRYAsGZA36fp_BnjDeyHz6Eo2TaDaNLTCD24k6FZXV5C6e_imiEOslYkiKefXWxAvK-GACzNMDM7mKHjvCJR5V4Rxlv5mYV5P0U39ZtcFzSMsPsLYBzUeUGQSeD3_a0yqHtueHiqmlO_-qcpvXKbvrxe4YgJrukzfoLBYaw8NVH19mcIj0n256yCu7Ge0Xz2E48-RmJBZKCuED8k-xYMnp6lykyrps-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r12
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/76606" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جدی جدی یه لحظه داشتم فک میکردم بیبی و ترامپ با هم دعواشون شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76605" target="_blank">📅 09:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امشب، امشب دیگه آتش بس نقض میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76604" target="_blank">📅 08:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">م   ج   :
ممکن است طی هفته‌ی آینده به توافق برسیم.
یک توافق صلح با ایران می‌تواند حتی بهتر از یک پیروزی نظامی باشد.
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر را بگیرم.
امروز یک مشکل کوچک پیش آمد — ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
پس من با حزب‌الله صحبت کردم و گفتم شلیک نکنید، و با بیبی صحبت کردم و گفتم شلیک نکنید، و هر دو از شلیک به یکدیگر دست کشیدند.
🥰
😊
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76601" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV7uFDz_G8CBjH88s85CHw6DpFDK_U21JKRbNYFn_YihwgFUCN0h2I07508Ku_DvkCkVwrTh6uudXxPFShJC4NBXAm4TeYvXc2BpV-_8_HwNMWq2854MxC3sbEW100_cz6-Ifnj8zHOVrdw2w4e_Lj9Ztu44pAoBsxSvWjU-IKGhYNCL5R9fRWs6fOXWV_FRZORI1nenuSzn1Y85Dx18nZuVWNQ3S9Vt0pdbVauAbyz6qLIQCzN4Fin0sR8hSJ2WQWbaBp_FPMjgt3BTRWwe57NKkaUr4NknUsDkB-Yqf03GVi-HxSxjtLeoVzEIbcn1JjkluM4jHF0K1hXPcd4otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76600" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76599" target="_blank">📅 00:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی ترامپ را رد کرد
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76598" target="_blank">📅 00:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو:
امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم اگر حزب‌الله دست از حمله به شهرها و شهروندان ما برندارد، اسرائیل اهداف تروریستی در بیروت را هدف قرار خواهد داد.
این موضع ما ثابت است.
همزمان، ارتش اسرائیل به عملیات برنامه‌ریزی‌شده خود در جنوب لبنان ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76596" target="_blank">📅 23:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر دفاع اسرائیل:
واشنگتن ما را از دفاع از شهرهای شمالی باز نمی‌دارد و به هر جایی که در لبنان لازم باشد می‌رسیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76595" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تشکر و قدردانی حصین از بچهای سپاه قدس که امین منیجر پخش کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76592" target="_blank">📅 22:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏تحرک جت های جنگنده در تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76591" target="_blank">📅 21:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76590" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حزب الله پنج دقیقه بعد از توییت ترامپ به شمال اسرائیل حمله راکتی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76589" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دقت کردید که الگوی آتش بس لبنان هم دقیقا مثل الگوی آتش بس جنگ ۴۰ روزه بود؟
آتش بس بعد از یک تهدید بزرگ
احساس میکنم همه چیز داره طبق برنامه پیش میره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76587" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76586" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توئیت جدید ترامپ:
من یک تماس بسیار سازنده با نخست‌وزیر بیبی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده است. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردند که تمام تیراندازی‌ها متوقف شود — اسرائیل به آنها حمله نخواهد کرد و آنها نیز به اسرائیل حمله نخواهند کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76585" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یادتون باشه ترامپ داره یک شطرنج ۶۰ بعدی رو بازی میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76584" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری تسنیم:
اسرائیل از ترس ایران به بیروت حمله نکرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76583" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
اگر حمله به لبنان متوقف شود امکان از سرگیری حمله به جمهوری اسلامی بیشتر میشود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76582" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کان نیوز  رسانه معتبر اسراییلی :
ارتش اسرائیل قصد داشت یه حمله شدید و سنگین به منطقه جنوبی بیروت انجام بده، اما تو آخرین لحظات بعد از دخالت آمریکا، این حمله لغو شد
گزارش ها حاکی از خایه کردن ترامپ می باشد.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76581" target="_blank">📅 20:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تلویزیون ارتش اسرائیل:
عقب نشینی میکنیم
ای ترامپ کصکش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76580" target="_blank">📅 20:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه i24News :
آمریکا حمله به بیروت رو متوقف کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76579" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی 3 هزار با سرعت خدا میفروشه:
@vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76578" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76577" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNSbI8FvxPUHCfHRzUK4A5nOtkv70YWccWpFzTfIUdOcy_TTOCeWLMSkBSQd73b8IGQ_Vm9PczXO9VS7Bvn27rRlWrSbvN3AMLeR3O5ziMaE8oUgbkfhohs9Gt5-pEPjrVHxw8LvhJmhpUrAzyyoWapoA2So8oi5VnzjMieepOYTSwaVZbPSjbPYFTnib7Zrv5oDkprKr8mbCkbEm5I7zaZlASjIuAeYovTaw-KZJpoiPZ9UCfvyF7ILHrvOWFLz3lKCf_ErS6dvskxTv02gZitAn08D4wiJpkuRuRJtrLm6qVu2_IRyS5CMgqzV3HWHNZ2ULbn5sdHlfzVzOc_moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76576" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ولی ناموسا الان ساعت 4:25 ظهر
با کانفیگ علی وصلم و سرعت ایده آلی داره</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76575" target="_blank">📅 19:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانفیگ گیگی 2 میلیون موجود  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76574" target="_blank">📅 19:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی به علی عبدالهی یادآوری کنه عاقبت کسایی که برای اسرائیل رجز میخوندن چیشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76573" target="_blank">📅 19:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:  اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76572" target="_blank">📅 19:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:
اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76571" target="_blank">📅 19:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/her84-bHVk35Z92equhs5P7AJp66M9t8idqT-ViTHlsYeHMYMUWOda_Qjp8RkEnv4hJaEKXHRd5PRqAHwIRqZJBLygjWRekN0If-VzsZeKuhNtexnUzLkNi-ssKggRFTJ0YZGthLc28wUymKRzqSswASivwhqBNWC2sx9um3tlTNNmXdnja9nr6-PlK_zBRIXwv1bz-rpU1b-XM8g2fehYtsbbTM3cMLQODkciE5yFarY-mrIRMoeiBrwzBkCf-h4y-tblKjDBKqcws3b4aWPcdazaMfOo68-ZTJhaSwCG4Xz12qHSnljLhkXwGL1FOTH5CDbh5iGnWgMLAmxQoSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جهت حصول اطمینان اسرائیل از روند به شدت مثبت مذاکرات، الان ارتش اسرائیل برا جنوب پایتخت لبنان دستور تخلیه کامل داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76570" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داده است که احتمالاً یک حمله موشکی به یک کشتی تجاری در خلیج فارس شمالی، ۴۰ مایل دریایی جنوب شرقی ام قصر عراق رخ داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76569" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=MFix852Zp1WgMbCRhjjlh2F7C2HymVUnjzPGcymTloE0y9gL5rnkaUlaC8MYyC30MFe4-dChMwM_Ke3y5ZOBFzi6DxHjEM2nuDKlDJXs6z5vvcMeCR-Wo9PhMPnfxOjq1XAtqtUK_X_uWAoIjLt4Gxe25SrZ6VzFDdf06TBhGQ7z2FKnAp12UpHlmMpas80J5wJBlr2rBY0pVYeRRlv-2GFgBVf_OYjEtB3r64bVU4Zhbl8Vg_PHYGq1H3MF19O2dY1paFE6G3VhAodxdhqwgq5GEr38hrzXYtTRqkfq-nCEnMsWawgN93cmkPkdjMai-kr6eblmAZdXrdYkesl_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=MFix852Zp1WgMbCRhjjlh2F7C2HymVUnjzPGcymTloE0y9gL5rnkaUlaC8MYyC30MFe4-dChMwM_Ke3y5ZOBFzi6DxHjEM2nuDKlDJXs6z5vvcMeCR-Wo9PhMPnfxOjq1XAtqtUK_X_uWAoIjLt4Gxe25SrZ6VzFDdf06TBhGQ7z2FKnAp12UpHlmMpas80J5wJBlr2rBY0pVYeRRlv-2GFgBVf_OYjEtB3r64bVU4Zhbl8Vg_PHYGq1H3MF19O2dY1paFE6G3VhAodxdhqwgq5GEr38hrzXYtTRqkfq-nCEnMsWawgN93cmkPkdjMai-kr6eblmAZdXrdYkesl_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.  @FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76568" target="_blank">📅 18:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فدایی تو تجمعات پاریس  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76567" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=v3cyc2WhF3MIjwRTue-ihQuhrBho1CGHJRyTOuHMfaHZGEt-58uHHNT3h_EaWBUsBXm15Q54lycysy2quToHF1Z7y7Wz8apYTn0dh0Wp2KlRXp2jZSHwq7XJ0iPCbdlpDAB1H_CRMbaklD_yn3AFEm7bQf8H2K-tiwwgvb9X_YaWv5r1UYTNYc07TDbyhr9jWWk15M9p7EtNjT_aD0t0fkvjbFaUn2U8sLRTBcFrVS9zKhstWvGnG4iEsIHWGaAkyGvNQBNzx8_6_RP6n2Y6q67OmiCN8xgmvKLGMq-4WETV601kwQiLk483J4fUxQ1tm9ufRPxSbvrqZbTNBmWb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=v3cyc2WhF3MIjwRTue-ihQuhrBho1CGHJRyTOuHMfaHZGEt-58uHHNT3h_EaWBUsBXm15Q54lycysy2quToHF1Z7y7Wz8apYTn0dh0Wp2KlRXp2jZSHwq7XJ0iPCbdlpDAB1H_CRMbaklD_yn3AFEm7bQf8H2K-tiwwgvb9X_YaWv5r1UYTNYc07TDbyhr9jWWk15M9p7EtNjT_aD0t0fkvjbFaUn2U8sLRTBcFrVS9zKhstWvGnG4iEsIHWGaAkyGvNQBNzx8_6_RP6n2Y6q67OmiCN8xgmvKLGMq-4WETV601kwQiLk483J4fUxQ1tm9ufRPxSbvrqZbTNBmWb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی تو تجمعات پاریس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76566" target="_blank">📅 18:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">با اخباری که از سمت خبرگزاری های داخلی میاد بیرون
منتظر پرواز دلار به سوی بینهایت و فراترازآن باشید
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76565" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDTK8iHnzRmn5NNV7LXcCgkSb6MFdJiKjyxsL7P-v76XKI_fEvouhlf-iId-qOD6dKd28GY65_jP0kGhR53cIrU_i8GBotZyLJivpmtaVf3516KBKP3IfjaNKDt51V-VN8wh3fURTe7MH1O26KaXX18_atNGxJxW1pHNHLrZ8Efsp8QTG38m3QJ-I6zHqpzSTfZirJJwdcIMdstWj8dn6L7CtfwSeV-5jx_l_OchC32HWELUC4bu-BqHGVFrIMdqVzsgylXgTDwk9lIW1mEZBUas5RdseYmVPNjQwpYadOpQJKY7L1fJKk95FdwPlhTDjj5BOCyOQaQUREorDF8yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پنالتی هرموقع یادم میاد تخم میکنم.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76564" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWynp9OAQAus9ub9uCCXQilYPLZ2syk5pDZNrV-xj1nooa_w23TiFZN_CadHJBjEgvAjyE4m9Ojzd9pGT2r5Dd3XnD6aCiWBzksIvO2EbpZ-evoRJ7wCH3CkWn3_PYPDuGIdd1EB-ImsKq4cr2hJp5QBYdWlrtKdTq3F45Q9dn1PiuXNtLpw0xE8wjRRQihVn2x9j8jGEnAr-VQcMHmFMESXLHpQel2lZNcGfTzCmSqhtNiggxEtjNjnkO77LFLnhcyaCwtZ9QB7F23QI9vluQrsOogQ5kIoFloJWPTUh98i4bZ2DDZqz99LAZddBWeOr8uDwRCmzG0oLYPMmJyShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده چجوری روت شد با این وضعیت نت همچین پیامی بدی؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76563" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIK4fRPyzqucpZ6gnCZwRoDeOjth5LHN4pQzn0rI_KWWbzPuBjqwSGl5KxZ3fLUQ9JJgOVbjJOB5gXK6t-yTfnOB66EuncXG-LxNe0FBb2fpbMImMXmny7Pbupeflrj-2zLHn-hvwq6I8CPwVDXoWJrBxKHH8ON7YPMJshQ75NpkzhyWnl4xUZ--KGlCXnBE1URyr35tBHZ5v6SK8LvPChdFy-L4Cap4Ck_HajKih2j4i6svAfwe46HaMJeM9DMuI0vGDDJoKRsU1Ryy51fGnBfSAHwM-fnK4anhwTZSjSqagjzViOdbTMIn26dGIKPZxOfoe6_aAV062T9Y2CaMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76561" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شبکه 15 اسرائیل:
ایران تو شروط مذاکرات علاوه بر لبنان، غزه رو هم اضافه کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76560" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری تسنیم:
ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی در لبنان و با عنایت به اینکه لبنان جزو پیش شرطهای آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
▪️
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان، مورد تاکید مسئولان و مذاکره‌کنندگان ایرانی قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
▪️
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76559" target="_blank">📅 17:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع داخلی میگن مذاکره گوز شد توش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76558" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANwBxbajOUXmAYQzNXRtRtBr7Cwan3rh-h5izJ6pLqztLiEsvYjW_VcQbd_OHtrcLekPYwaErz66KlSZLEjmrW5GtA2wIZ9bltfIEqW6PikngSuUO_26GW2ZG_bjV-4-PnJEcFFHFssiKA9Z1IYVqI8Umjh8D-raFawClV3bQFF4K1DeDp0rXG4Pb_stH7LClfW_y1NoLoP0Kelapgb2FDVRRCB54XAfwR394xL5RkdYZVp71K66e7OJ6qfBS1DNwwvzKpGw90U_2PwUvFyc-8R6N6grB6Vpea9XdtYq_PjKZiR-2r2MWgpLrOrVPQvQ8IgmfYb3q_pC6FknAf11eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رخ
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76557" target="_blank">📅 17:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVsB4hAyX_Kh4IiD_SQFwp-z_jwkKoryJFojVQyaJiRKF7qyCJXhIbfjui3-_ft1Ma7_8kCLlQ3MtFS-t__wAajr389QQL6kE0xPZIVmSOwVdqLvyJ1sFSeGU3uDAVannk8105w5_KQWEuGBDEfT-MZu_b2y9hNmr80F8YKKtHh5KG9f2qvq26OiurAeIAQ-M9T9VZ2vQGyvwOvrJg846qxws0bwfFyv5gBM-JwB2lvMxCsnV7LiO4TsR3VgoS8pfIABwdF4d2tLaxC1_DVPCwaZf2Z6IqLGbXULEOOBFIbk_vYimdUJsBYwvfxxV0vOQ_hClOpkB_oViBxt0b3GHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزو انداختن وسط کفتارا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76556" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دعوت تتلو به جام جهانی مطالبه ملی ماست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76555" target="_blank">📅 16:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آمار رسمی تورم اردیبهشت 1405 منتشر نشده.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76554" target="_blank">📅 15:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تتلو بعد از دعوت نشدن به تیم ملی:
کس ننه قلعه نویی
👿
۷۸!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76553" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG-DSl3SKg3ObEeYNMDAI0PERJbr4fhkWu8DnOaz2lXJWAUfFanpwRlSndoRmclG5iqjBuDDJmUNuGIK8LQn2FN7VhcvrkDn8DezF_PkmWWXX8lnVcbMnK8a94FdY2EvDLPojc-gdC6uMCY84HFayH7JdaccRGe41TbBfG9xylg4knzNgD9TGExIV9lAM1nY3M3WojBCik8414HEU0FGPwiX3BeJEjObCF8Bhu5mdJFMhixa7R_babVqR6tUq_V_RI04OdVSmMKqPzGoEWFdrbKR0rLVqvevSne5StrENr_1yV9uOalY94JvrSjzaoJEfsfkvUS4pjiIBIvi4ty5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست نهایی بازیکنان جمهوری اسلامی برای جام جهانی
پ.ن: حضور مهدی قایدی و خط خوردن سردار آزمون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76552" target="_blank">📅 15:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">باقر جون چرا داره یجور رفتار میکنه انگار من پشت پرده لبنانو فروختم صداشم در نیاوردم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76551" target="_blank">📅 15:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76550" target="_blank">📅 15:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76549">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQgmI4rgW9ytrrHB9-x-wNd645R_offKpnoQlr6zpLqyrq9rZWk81ZVje8lKKV7GVw6F__3wSGwEXqz63Bo03IkIrKhZQDDb_sEJVW7yeDhfCd3Cg9HYKgGlWz7npAks2WJoD77jrnh8t1SLGWLcgQb8m86N3sKame30XFljHK-t-aJ-qwXvfnpn9JplbMFghoyWtu_OtAP2nkwhzrBkXvFVSHegDpzPldv4p1JkAjjbSGIzSroFGbTfP0a9v6d2TobgSiDzJqJojmfm6lRA4GlQZPuqiLl6tJWDdfeyUpNm2czURSBZsKxQwqUzrDTIoXMC6LYr5JOVhlvD32p_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفسور
عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76549" target="_blank">📅 15:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حاجی اسرائیل داره لبنان و میفرسته قشنگ 1400 سال پیشا
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76548" target="_blank">📅 14:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ix0x2bmuai2i9n2b3GU83w-dYpa6koTQRm5XDwCLUvsfj-bZfFzoqXbv7by4flaTue1-AMpOu6SpEfWrraLPyOSpyRxKvUpxzNs3nv4JzdAZeYNAq2vc35G7nJuCGLsvx8SbfwPCA9zbpZRZeyYCzN0Sb8ZAxMiZW4rqzSJ-dbD80QnCYdV9za_LZrY0UjN39PB3QrsNaHAcbmCBHNJIB_R-1X9mIoRuQyg4HwZtJdKcB-LjKCA903vOwUY03Wr9eOXgzakPIGHxrBAG7pdf-zU2QKd3ZZGL7NZOmao6wH8XyevxfhGoA3s93Z-rFpSuYf6fRKphgsNp5MuRiRRDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPD7Pu-pRTy77pcaC1wQ6DCbprspjRi7B-MaCbUGDxj2RMfa2YFCkeNUnIm5E2ZxLiTQlqAowZzE5yE76csea8Hxm6u2MMvlIw5Z9of92DxiToFZlivT6x9U3CCRjoWwCxPbZY_j4kpC8qwL2apLeuTNJcLyJdUxIIUGBQDh7dXLKEM4EPhkLHDd69wsEZKCZU63PO20ERI6EpQoejPuJdi9KTEB4Nwdb2UHPxkqa7XzVIBbixulm-6CR03f54kkF0kMNTuXiqa_WfvQzY_fvxhmZNpA6HWenkrtPUZqCG6beA2b8K28OeNyYdzytkpIEMbcdZ16xPdcu1HcLzuk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76546" target="_blank">📅 14:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی به من بگه این رسایی کیه
اصلا چیکارس تو مملکت
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76545" target="_blank">📅 14:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده   @FunHipHop | blue</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76544" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده
@FunHipHop
| blue</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76543" target="_blank">📅 13:32 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
