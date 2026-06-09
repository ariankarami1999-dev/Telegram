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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-65632">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام ارشد آمریکایی به کانال 12 اسرائیل گفته؛ هم‌اکنون موج دوم حملات آمریکا به ایران همین الان در حال انجامه
@News_Hut</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/news_hut/65632" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65631">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwWK13XEROMKWKNyr_Tmgy1n2puMt_-qHTtmRb0jd7My8O1ofNoHte8xyosWMBow0w8j_LOe0f3pAli4mXCe3waySNMVr3axizNz-r9h43b45ZWP2z6TI4KiwgXaq8a_21BJGPM8ci3iqpD8Oam4bBvl9zIaI8-gwf0Vvda6lro-fqMcCNUbasUAkytyTcmtONCG_JtYjsLy-Xf9tlNDTdsS1Bc8WQiOAUVg06-tYAlzdcuqkSkxXXLUjj7Ymp2HnF2xZ8tjed3j3X6xB-IvzxmTlDcNOYC1Z_v_7r4NakTBmXO9uvlLqSLDFG3uIUHPtDTvRI-AZtMoUMdtzdUB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🗳
کانال رضایت ها :
@AtlasSmartTrust
🌐
وب سایت رسمی ایران :
AtlasArbitrage.ir
🔥
ربات رسمی  :
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/65631" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65630">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/news_hut/65630" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65629">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vd5I-gVCnnoYAfwJlGTAn0L7Wg4WcYOSbXIh6BU4XKvSvgWAveWqiSKrQsdCpx0Kdd3Wbzh7CC0D2PJOscKLJuy6aC3vJCOlNAUniH2d-koC8j2BxBYjH1s5pqjjuAEALg5qKbQXlYRkTfSutRd0omiezuev1DfS2MIRpJlTO-Cxa9UPlet_QFFT0rQ2uC3VYqigkt1jWv5ccKgIPboelgDaXLFrJ1eTKNLVZFtOapWN2uVNfGCqG1oglG0Yuc0ByyIcccwCHyWbzqbCZiOg8rQRQcGRQlmCxDQVKubmKXOrBwX05aSB6h0k41meOPyEWmeWsWawAXSagpoj2-KGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/news_hut/65629" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65628">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارش ها از حملات ترکیه به شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/65628" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65627">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم  @News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65627" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65626">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پهپادهای سپاه در آسمون عراق
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65626" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65625">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUqU0avyjjYd0KVs7pCDynP4qzsMFInlv-Z2AO4i1MjFWX0P15qxKUEfeYJW2fCtcyY_yaF2lNX_ymJR4COkkQs5Y7uFN8MDsRqN1olWe7R3XoEzwk1BIb6hWOiOG1ezHGqTvX8RFoQAU8CphnAALCVbW_oSfqyR6g3q6ua0ANOolReW69YsvTy_I_GRndVhPTwP1KFHpbl5S69ma7MunNVfvq7UnhSdM5bUK8wvY6_r8NJrzHJDfWMIxy_CY2F4Q814XEMPXSLpj2SOrM43giF0TqKMzPAonMmtcihPxHR6CxtwNpFpsQsHfMDlbiH7AMv43PCEAxg2wUBBrAJ4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار تخلیه سپاه برای بیکینی باتم
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65625" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65624">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2yplze-8QHgZqgrmlJurDcadxdiJbtb1gQ2JvZv9HmvRUSUJ2B_xi-wrg4HH0Izm-RAozOnzpJqgqrg3aZg24zbf_bgXcDJnq4AnuTrZFl2CbhloHGSwOatHFgTH3fGZuL6lJNqs6ihQQAP5Ssc83v40DPCEeqdezhZ_VW7mzO0dI03mcQ_lAuA4O_qSHucDNrf2edUJ4sMSSK5tWFkbtvTj3juTLoNa1S0Q66pRSozw2lVRQLpD6CuhmMrUHZte-Nwisoyh3Qsghd4Yodz4-GOSrblHTogNDnyAg_aigu3J3ctcxl8iyY44CcbCQQtiHDo56-6OksLkEtTYd2NjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
علی قلهکی: برآوردم این است که سنگین‌ترین پاسخِ ایران پس از آتش بسِ اخیر به آمریکا داده خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/65624" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65623">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1aWSh9uHSfLo09qTktGw6fYIB8DQNr9BdQjdHtxVoR9a9u-dRZnPYSGNAL8jCmA5-uKm4g_SHr-aTHf_9WSUBvhmoKuFcd7En6a1PS3VKlUIZjHbQ5PenGb1LguTiROXXxNx_XizTJwHDk4xACRY5HMEM2_-kYV7m3nSn6GOaA7QXOPmz8u1Q3X3SQBBsCMoFI11EZ4Q3EVroL8ZYneowHuOCys3aWGWlzh6I3gfvGqbdXCDWfdWX2I1ExQ1AEPNtsO7ZtXrWKrCxL-cQaZuQSXw6hlLhZ2gvdgZ4FEs97JoQlTo_UcRK8vbiTyNcCW-2Eb-lR_Hp2w-_l7BRojeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شید برید سر درستون کنکور به تعویق نمی‌افته
✍️
#hjAly‌</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/65623" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65622">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/65622" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65621">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
کویت و بحرین هم حریم هواییشون رو بستن
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/65621" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65620">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات پاکستان به افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/65620" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65619">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4g-HZcM2ETs-g0V8hiQosk1vSJD-fprzV-vjeV3KNFBqMks-1tbSTvWd3oeCfZOHOrSgYQ2LxrnQTVp4uyIk3ySn8qH1z6JdKp1b40x36LH0fihhqyz_h-6ze_NWQOo27gAX91Jx31mtHvy1MuccLLjXzDlPW4hdJudu_piRpTacBZXCpKTKbCxbZJ7gaAsloieYoM7tjs_ZKmbtUMyqb6KcIVSiLvLxgmXkv1cxRpNSFv9xz7HkpCK5v_JPe41sV41tjCsGY8Hh_BztSfLGWu_-HPpg7YSXbUrQ7L0HLmz5x3ovJYS40iQ7hFuRtwGwkwCXcS9tWGPmLlKzCD5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65619" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی قطر بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65617" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇱
گزارش‌ها از حملات اسرائیل به لبنان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65616" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
سنتکام:
حملات نظامی علیه ایران با دستور مستقیم ترامپ انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65615" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود! #hjAly‌</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65614" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65613">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛روابط عمومی سپاه پاسداران:
ارتش متجاوز آمریکا به ۵ نقطه نظامی در خاک ایران حمله کرده است و باید هزینه سنگینی بابت این گستاخی خود پرداخت کند
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65613" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65612">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ناو آبراهام نه تنها نرفت قعر دریا بلکه با موشکاش قعر مارو داره میدره
🙁
🙁
🙁
#E</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65612" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65611">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیمای جمهوری اسلامی گزارش می‌دهد که در چند دقیقه گذشته یک مکان در جزیره قشم هدف شش حمله هوایی قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65611" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65610">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از هدف قرار گرفتن پایگاه دریایی ولایت در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65610" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65609">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ :
فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65609" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارشات رسیده از حملات به مراکز دفاعی میناب
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65608" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65607">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم  @News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65607" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65606">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
آمریکا گفته حملات با موشک های کروز و تاماهاوک انجام شده
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65606" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65605">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7LF73n7M34D90kw-_molEaHhceP6mjcjInef4kIM7P54Y5dqaw6h0lgYQ3Kez6xCWdHJ8zIvP344p4F5F2hDBH1X6yEslLHo7U7d_4X_bGh8VFlB3cRantkIHBhduzIFgz3XkU4CoPVgBkA6qULAwQ1xLTUVfp5Y65rYnkx2_PWmeVpOHAnMwSc8KMPH1_YzgF_maF9RSBiD3DUe7fRAzvlemCaQRaDjmxyC86LbCACD5hcd8FIDr5JD9M5w7C8iskPwtJzRJSWQBIw7XWOB-2X8RVphTm91rLoM3Sy4IecYchONiDsiLN8hnNal0Q1VTmJ9lf3hq2bCCPmNIIzGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65605" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65604">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود!
#hjAly‌</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65604" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65603">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaleh</strong></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش
اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65603" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65602">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrMxlMOe5K3l6LDI52paEwNw-KoH2DjTuQob11tMaW6gJ2MTSirgK-cDwjKMVuBILW7fD3rG0aDqMbKCEOiAKv_bgg42tuRrKBBMiX8B4BtyA8cEAjupbk47j1E02Ls8bcANCGESr07sW3e0JGx3oXLpHHY09DtqVpIDSNRV2v_8FiD8RHFtDgcroUT5bM2yG17LhqDYxKiKy3Gf5ZppEmxKLl3hOwxvQWAFsb3IT_oEh2cp1jHs3bIffQSVth6Odnqhcz8rxXCSf6J7xu6cOtN8uxCbBlISXvlHqlWUBlJoouZyIkK3QcYAS1kjVtEIzLTBpGfTyrWu1sZ5zkqgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65602" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65601">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
گزارش ها از انفجار در پایگاه نیروی دریایی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65601" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65600">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u55e_Kc9dSO3FooB1CqZd-JaxXn3QlUxaClYaWjw493QgUpGLaXo_ZAzuq2iaN2v7I9a2uqsCLahS2g-bCIgGBt2y9Ue6RuBvd6dZtuyhTahUQdYbHkLJqI1CtGVV3R7Cot91nu2c3TUS3kKSYXc2gATYVpqrm5aFZKAlRCf5yGuO8qHTwsBevFTWbTVv69e4AYSiUZSOXBfqgJ_UFv_7dRf-bT1zqix0Ux8fGqtWAZY_Cu2KYRxMFyVmH8BiYWjiWTT_Lji61-_iraNrVdkN-Xlb1SnzKxHBhbaTM85P0mOcA7G_WU9B2Ev0ChMNI-OuspUmaAYN7GFCDG3EsORKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده
#hjAly‌</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65600" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65599">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65599" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65597">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65597" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65596">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbGwq93koul8c00EToZWA29ajXwxd1xNVBXxelPHqA2yCpoclI1MQsk1S1WFUNfhLaC9H2FirMh5iQL0TGUvWnU9yQhwAKy-94iRqf_iyr-cdCp1MLrFfM4ZStwRKVn8HZkEoyPJq5slVoaIIZkPe7jO4-xQ947y9oMzt7pB_iMg36-KPRqL6GN64lzkRRVy4BOJvmRPC4XiFAPEOQ4l1zCfq3igWdgq9t4Y9elBHYWRaqNkaH9rvZxAUXqQK1ByvwVWRZdDBCCelIRlCIJA1RSKTC6aSiS0n2bAvfsxMvQZ8IWfkdoCJ8H5GHDoGjvuLI9j0MZcXEqppDYWrDSauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده سنتکام، رسما آغاز عملیات در جنوب ایران رو تایید کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65596" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65595">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65595" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65594">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
انفجارهای شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65594" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65593">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس حکایت دارد
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65593" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65592">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65592" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65591">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش حزب‌الله به شمال اسرائیل حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65591" target="_blank">📅 00:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65590">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی: دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.  «هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن»  @News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65590" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65589">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ما که از بیکاری و بی پولی رو آوردیم به مجازی وگرنه که تخمی تر از خودش نیست
🚬
#E</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65589" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65588">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده #hjAly</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65588" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65587">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده
#hjAly</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65587" target="_blank">📅 00:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65586">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:  محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.  @News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65586" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65585">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ کاکولدزاده حاضره برای رسیدن به توافق، ملانیا رو با عقدِ یک صیغه‌ی یک‌ماهه، در اختیار کینگ‌وحیدی قرار بده #hjAly‌</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65585" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65584">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSiSXFnXGAjNlo5HdlhzNrXKPStv1CJ7i82tLPcLVb0b1rjo-f8h_5Z2_HL_5Rk5Px9DTasptk6sSCtz9P02tfocWKFaQ-VUlFOvya3DeAbiNU033JTDUrQPuzusoIWOGbwEmiMymH3dTG6Ykd4Ir5YuPbgjijM1KfvYSSEfWnCWSbxdEe4WJtxlKcHZ1wO51Yott96s5YW5SpNZezBTKt6PKc7saIWP9hWreGxFWU7Puen9qtupXVv6fQT0zh-cUjayAdMSmNpOWfxNy2TXrng0uM0dfAjFw7d4ZSg3VovCYYui4SaqP5yQptjjokyECz1L24eQVBFw1o8SKx1pQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی:
دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.
«
هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن
»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65584" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65583">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه پاسداران: هیچ حمله‌ای دیشب از سوی ایران شکل نگرفته و اخبار مطرح شده کذبه و ترامپ داره دروغ میگه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65583" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65582">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:
محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65582" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
شلیک موشک از خاک یمن به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65579" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65578">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65578" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
شورای امنیت سازمان ملل رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ ها علیه جمهوری اسلامی ایران را تصویب کرد. بریتانیا از فعال شدن تمام تحریم علیه ایران استقبال کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65577" target="_blank">📅 23:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65576">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود که هیچکس حتی فکرشو نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65576" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65575">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNTkn_lEo8VO1ba0YrtG8uJl26TFRsRMFEG4htgVpkCCwxAfUyDyP7HoGEKd3g1rJuLqYQY_gIhCKIlBJNLhXNAHsE57kA9Uso1zgp3zjbmme7N91PVnCceVncIMA3VJYjfdVTgWGwGEmPk1LTwcy1TDOkG3mAf_DtBb1bmVNiOzEPr105nENc7D2W5Bonmu2Ak3xreTk8Ao1LHT8OlDWzNoltxNoqfspnBSXOxWdynf1m2gwVwDImG_875PISXrfPRHaBeWo3zyS5CETpXQTkH11BZAZaXgzSh4m6I_DRlxGEqLKLCDBSF_kOtmw99kdwnKBSpKFg08C2ScdRU3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
لیست ترور منتشر شده منتسب به سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65575" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65574">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyT8GQQWXBNvrRB5wAuAZ0NlNreSHCbmqbFUufpWELeH1Fw_0PkeRsRHZuNeYBSjeeXArL6TCBXYuec9OK798OB4vT-CEKOpOraYUGN54DaTzdlwraPRShXB9c0AufCWN0LAB1_I0vrQOUacnHAeYaQvHfFMf6El-6z1_TBCoU8wl2JuC75YcRtSWgaV6vqDFURDRu9Sb3Cav7_5C4Mj21wyqF7Dtl3x_Klk1HnK2mfO6vgtu6SDNJAlpkVsZmz4MMj3mqV6Nds2AbYSf3IUyIYeEV-gh6GTjWW82gy1y92p4mp--hgxsftIkwOJpXYnxTiJae2ZkGTogzV7Pk63RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فضای پروازی ایران کلیر شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65574" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65573">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
العربیه به نقل از یه مقام آمریکایی؛ شواهد و نشونه‌ها نشون میده که جمهوری اسلامی بالگرد آپاچی آمریکا رو عمداً مورد هدف قرار داده بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65573" target="_blank">📅 22:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65572">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
♨️
حمله موشکی سپاه به مقر کردها در عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65572" target="_blank">📅 22:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65571">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=DbGUfUwKdK_x7chzAMxWt7G_BOlYnW37Apo3fkUcZ1M3PIg_RDbXAcb28Io4rrsjBxRr4ccm21ux8g6xuGh8vCHbhJgIuQMmdBW69njM6QaFnZi_amtxcDcmk9SZef7gk3nGW4dfLGVpcW6-8Cg5vvCb16zBDOPFwO-LSLutRCmxCk93JT27DWLh05Q1G265dkXTjqYTOp16s6BQmYEbR5t0LuoSB-e4COwsOy_-BpdZFgFTcDoycnIko2m3ljiCwFUr1MNvH-a4H3T3UPLpstwR_Snbwn1mIw0pCklg7jh3VZy9FWPyeP5zQAdUbkh97dsPvDLtwLDIoATifh9KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=DbGUfUwKdK_x7chzAMxWt7G_BOlYnW37Apo3fkUcZ1M3PIg_RDbXAcb28Io4rrsjBxRr4ccm21ux8g6xuGh8vCHbhJgIuQMmdBW69njM6QaFnZi_amtxcDcmk9SZef7gk3nGW4dfLGVpcW6-8Cg5vvCb16zBDOPFwO-LSLutRCmxCk93JT27DWLh05Q1G265dkXTjqYTOp16s6BQmYEbR5t0LuoSB-e4COwsOy_-BpdZFgFTcDoycnIko2m3ljiCwFUr1MNvH-a4H3T3UPLpstwR_Snbwn1mIw0pCklg7jh3VZy9FWPyeP5zQAdUbkh97dsPvDLtwLDIoATifh9KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
متکی، نماینده تهران: قوه قضاییه حکم اعدام ترامپ و نتانیاهو رو صادر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65571" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65570">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3LCCM0heaqlLvofyIJcinNJF3bNXLAiHo7m0yEvCIQXnQsDWMI3aWNRFwbvU8TppeX4KFuBPV15YL5BV6L_wMRDihdDlaSfXYQADqhcCXwmVuwr56IVBBUl3SNVQrnV1y9wZP95RElVLLidYYQPzUkgp7eEqNANTIyiwH1xwhJ_V0vXhYd-JEFcluutG5-Fv_8X-jDeTueTeka563JmbTez7FMieLaI1cHf0f82IcSq6khMRP9lHkT8L-pLfJghZuvE4T8XbjcHYz3_aGqYj8qxnzCc_sEVSI77JPUGK_PNj3ubgvhoh-tQvDD7hth8pdk148pfxovfEM7T_jFdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65570" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65569">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
♨️
قالیباف: در صورت نقض آتش بس توسط آمریکا، ایران دیپلماسی را کنار خواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65569" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65568">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=ZjvfbgaHu6PjkkPttSNF9EYDf6ZlqQ82zgBoNSM8BGfnWpDvskxBN2-2Jlub5ICtnG5uqd_pBNlmS-Bm5zX0bnmtuJuyS3KpFYP99PmMwN05S5aUQzr03mNDMWcMTtTGpVVyZcD9yKq3OFMBAU8kzqN-dRYIMhNKu6QvFotH849xmgPMWRs6lFu79nbs7a0h6YmoemfXuTffqd0vIpd-4u5Mn7HsfnDErRqucSXfILLcxcfmlajdsgclsPS9NQHNt7E-SrgayHvMwtVOcAdEoyVgxlaGyLGW9HSDK-OVHo_jXeIu5fg7Ar5MXJYAne_47YiqZGh5KkJSIfAGh9zaRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=ZjvfbgaHu6PjkkPttSNF9EYDf6ZlqQ82zgBoNSM8BGfnWpDvskxBN2-2Jlub5ICtnG5uqd_pBNlmS-Bm5zX0bnmtuJuyS3KpFYP99PmMwN05S5aUQzr03mNDMWcMTtTGpVVyZcD9yKq3OFMBAU8kzqN-dRYIMhNKu6QvFotH849xmgPMWRs6lFu79nbs7a0h6YmoemfXuTffqd0vIpd-4u5Mn7HsfnDErRqucSXfILLcxcfmlajdsgclsPS9NQHNt7E-SrgayHvMwtVOcAdEoyVgxlaGyLGW9HSDK-OVHo_jXeIu5fg7Ar5MXJYAne_47YiqZGh5KkJSIfAGh9zaRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت گسترده جت‌های جنگنده بر فراز بصره، کردستان عراق و مناطق متعددی از جنوب و شمال عراق گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65568" target="_blank">📅 22:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65567">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZeJminVKNdqJtAXv_mwAgTG0wdCNTkgFvI3P8Ot7c1v5mspTWfwKySl_CH0lcvUSdjIAVXrWOL0Z39Z7sKc3h4A9uHgrxGCh3GXRmn0Tbl8GLU2NXNU1PtJWHxtU3hF25sPQel3xiqj0fhKv9pVZ5itS1i10Kf3C3Dd8bTsTB90iqdBmjCg0hcj-0w-qoj6VrTyxZlu2grns-rlIQhpBFVUh2HrVWZDvijAWoGWkpKwaahdCN1joOqSCmLtWfwSi0ze-Pb_2ncpwaULd6Yw2g45rvC6EifPeUFByPnAfivGaa7PZWoR28qOV6PdCgtMsbriO9PWyOz641gLhauk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فعالیت حداقل ۹ سوخت رسان ایالات متحده در خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65567" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65566">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
صابرین نیوز رسانه سپاه: امریکا به اسرائیل اطلاع داده در ساعات آینده حمله را شروع خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65566" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65565">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به ای بی سی نیوز: ایران اگر احمق باشد تمام زیرساخت هایشان نابود خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65565" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65564">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
رسانه‌های اسرائیلی:
«اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65564" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65563">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از سوی اورژانس از لحظه اولیه حمله آمریکا به شهرستان لامرد فارس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65563" target="_blank">📅 21:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65561">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">من از این کانفیگ V2Ray گرفتم، سرعتش واقعاً عالیه
🔥
حجمش نامحدود واقعیه
، بدون قطعی و روی همه گوشی‌ها کار می‌کنه.
تست رایگان هم داره با ضمانت بازگشت وجه.
تک‌کاربره حجم نامحدود: ۲۴۹ هزار تومان
دوکاربره حجم نامحدود : ۳۴۹ هزار تومان
پشتیبانی
👇🏻
@khadamatsup
کانال
👇🏻
@apkdownload_sup</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65561" target="_blank">📅 21:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65560">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
♨️
فاکس نیوز می‌گوید رئیس‌جمهور آمریکا دونالد ترامپ «در آستانه دستور دادن به انفجار یک چیز بزرگ در ایران است»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65560" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65559">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8IE1_5D0PYnlhMDA7pKa-GcypiPQ6hjAxoblEgirY0gBSfrms2FCe8mEU6WTYfauc5PqnRPLgA79VGEsh6IbgqtOyD_oFhMMffWKmxTwC6aLtocYnZRwtmRzeOwJF3gV_QljKfVXKog671g_dQCNzQYYmiPuthknXv7e6HEe4zeXSQKXmcNZElozhBH8fKTcc2sST6kGQNSPpXXIKq8r3JuJ8uLeK_37YWV_FvlpAhekK3HUrnWy4WGIH6_DFBi2MtVOo1G37hV48TBC05U6HsLRyc_0FDkeg3dgLPM11_GVdYWD9yLdIuHcXJif0WvvgeIuiM5ANwX-Wsv8a-n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اکسیوس و‌ سی‌ان‌ان:
یک پهپاد (شاهد) این بالگرد آپاچی رو منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65559" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65558">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
منابع خبری آمریکا: احتمال یک درگیری کوتاه نظامی حداکثر ۲۴ ساعته از امشب وجود دارد. آمریکا در آستانه افتتاحیه جام‌جهانی قصدی برای گسترش درگیری ندارد و فقط می‌خواهد پاسخی سریع و قاطع به عملیات دیشب جمهوری اسلامی بدهد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65558" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65557">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
‼️
اکسیوس به نقل از یک مقام آمریکایی: تحقیقات مشخص کرده است یک پهپاد ایرانی به بالگرد ما اصابت کرده و باعث سقوط آن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65557" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65556">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02089086e7.mp4?token=GweXKGTNedvx7WZhGqBwFV_RZA-2RCx8Ds6VvCKgKEF4NYyFOfPHV3e4AP1vLQIQ2GNVRoJw7uPyCK2NlbVJjk-BSVPHHwcpbA66YYg4WlF222hMufdoy6ymBI7mQgE_Mbv1HXIknXLCjBt_LQAlAgwF44wY3lApP8AhlXW_ZNtGUoQwTrBQmzlhz1bjKdI56Dnb3qoLeePVdhtl-1bdjFA9bEwIV5J6O5kyLkFGU00aBsMtG5IeXtJ4r-NZhA_0mUuSlcpZfalzqbXPk03FmjYhHQkp7yO53CQLBm9Tqp0jLO6-svHfcEnUbkc1_cI6eA8SHfVVT2N9snUBTY7ghBNHapTKfEgncd6U53czo0cMF_vxNgW6e8ZJIAOrOVGatv0pAB6hTqxEwDL8tymzqEUlB0vMg0qdg_LLWqanF_qz4JQM6hdmCbPxrTO55bIxN8RN6iSD6ff66sqPUm0XgthDMlFbSplgqS_KkM9r9OWCHhkRsu5mWmmiVu4Lvgprw55iO8_cwhGA84MzzJlPdBQ7OpJs4N0d4VbXLAy6WKcU87nm3AQLL8Qb1Nyx0J1JYFIue2TWM89Yu9AiwsgJiGeXkS4MS8mjVEFG1u8zrir5GWVOfh5DyDwpZr7P3_Qh_bF8F1xpcgt7xU0mLP--CNKn_StqDuU9eBCTWyf3X18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02089086e7.mp4?token=GweXKGTNedvx7WZhGqBwFV_RZA-2RCx8Ds6VvCKgKEF4NYyFOfPHV3e4AP1vLQIQ2GNVRoJw7uPyCK2NlbVJjk-BSVPHHwcpbA66YYg4WlF222hMufdoy6ymBI7mQgE_Mbv1HXIknXLCjBt_LQAlAgwF44wY3lApP8AhlXW_ZNtGUoQwTrBQmzlhz1bjKdI56Dnb3qoLeePVdhtl-1bdjFA9bEwIV5J6O5kyLkFGU00aBsMtG5IeXtJ4r-NZhA_0mUuSlcpZfalzqbXPk03FmjYhHQkp7yO53CQLBm9Tqp0jLO6-svHfcEnUbkc1_cI6eA8SHfVVT2N9snUBTY7ghBNHapTKfEgncd6U53czo0cMF_vxNgW6e8ZJIAOrOVGatv0pAB6hTqxEwDL8tymzqEUlB0vMg0qdg_LLWqanF_qz4JQM6hdmCbPxrTO55bIxN8RN6iSD6ff66sqPUm0XgthDMlFbSplgqS_KkM9r9OWCHhkRsu5mWmmiVu4Lvgprw55iO8_cwhGA84MzzJlPdBQ7OpJs4N0d4VbXLAy6WKcU87nm3AQLL8Qb1Nyx0J1JYFIue2TWM89Yu9AiwsgJiGeXkS4MS8mjVEFG1u8zrir5GWVOfh5DyDwpZr7P3_Qh_bF8F1xpcgt7xU0mLP--CNKn_StqDuU9eBCTWyf3X18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو یک سرباز چینی در حال تمرین برای فرار از حملات پهبادی FPV
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65556" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65555">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگه بت میزنید هم اصولی بزنید!
با این ربات میتونید هروز بین ۱۰ تا ۳۰ میلیون وین بشید با کمترین سرمایه اولیه!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65555" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65554">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فووووری مهم برای دوستانی که بت میزنن!
یه ربات پیدا کردم که بر پایه هوش مصنوعیه و کامل شانس برد شرط‌بندی هاتونو بهتون میگه! یه هفتست دستمه باهاش ۸۰-۹۰ میلیون روی فوتبال و تنیس وین شدم! هم میشه ازش فرم گرفت هم همچیو با هوش مصنوعی آنالیز کرد تا هیچوقت لوز نشین
😐
•
@Algo_Winbot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65554" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65553">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO2HIt7mP9rYurWaix-hfZpd3yd0bE6HF7pGfNyaXi8gDlku3FGMFNgp6XPAxO0EQJry7eHJeexrQFxUD9Ez_c3TYi5F2H8n5vIuYd_aiqOkVD5mspu7-ezdc-DJgStY9tAw6TXExnec3P5fURHd9CZDzSPbuKP3kd442LwFY8LOT0KpKf8aUS-dnivbNxExWn0yVppQCj7kBp5JWCdTdb0JKLZJXibPgAjQnbDaB-cNbTygPz7MEdTW9jqcFk2UZNvn6AWhSvYgcCpenWqXxNsiUOd-gF2oGcrdsiIBKfd1FcK74TCxHm1f2PmQ0jyQLus6BmlBChxvvDE9-kp2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کان نیوز: ۳ میلیارد دلار از دارایی‌های ایران از طریق یک پرواز از ابوظبی به تهران منتقل شده است.
بر اساس این گزارش، این انتقال در چارچوب توافقی انجام شده که هدف آن توقف حملات جمهوری اسلامی علیه اسرائیل و توقف حملات اسرائیل در لبنان عنوان شده است.
کان نیوز مدعی است یک پیام آمریکایی نیز همراه این انتقال ارسال شده که شامل تضمین‌هایی درباره توقف حملات اسرائیل در لبنان بوده است.
به گفته این رسانه، تبادل پیام‌ها با میانجیگری یک هیئت قطری انجام شده و هواپیمای حامل این دارایی‌ها در تهران به زمین نشسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65553" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65552">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=CfnFHrH-lvYOW8eATLaiyEP1hEx9JXN7Gr3ybNBNs3xL3josYtK2Lnpzmi9wSlb2MgbM4ocafZv4CyUaFpyVW8sMFji2rXfc1OWZsDy51rLk5hF39osR89hXNZqEcCKXd3TeDLUzUAY8SL_3UG7DKxZHPh7p3dS-xBbJHYChIhXlx-0BHvQ1nijFMKGDC5EYEbtMETpL6UJ4dqgEk25576aehqEpGiZAd2mgNGp-0SylA2g0zL0ziY9j4VAqhMuORXAGBMgyQbjfL1LKC7EWyVrpyFNY1O2Ykoixi81iOLzU0k8OL1rjE8gjHPDgzcmFoPnL-QkPxPr03BY55hAbi1Z2pbjUEeen98Sm0YD0XoVnuOgqV482hteaPIkzDdRWhWAHUSq9ngORrBIZpCO-1mIBH0mpQREYiAN7rICfacs5btta7dphuc1h7DGQ0zvG5wc-Vl4b6xpjQ3FjRtyob_rgpQzGmr0DkhTvvaXcyqR-moeRTyd2AIoqXsp3exmff7wpWcPAxDecRqd1MQ-lrxvNNqMCsgXSoUWmFEziA_r2m1z9KGWhM-uToK_QlrztGkpSjcTqVQWxZzY0ND98hfvDV_h9wzqpnJ93MURiUIQrhr25GuhhMIdzVGzyXTgpqWSqXeZ6JMknJ2A7jDnCTSO0CGRukpTIf0cgNEc0Xfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=CfnFHrH-lvYOW8eATLaiyEP1hEx9JXN7Gr3ybNBNs3xL3josYtK2Lnpzmi9wSlb2MgbM4ocafZv4CyUaFpyVW8sMFji2rXfc1OWZsDy51rLk5hF39osR89hXNZqEcCKXd3TeDLUzUAY8SL_3UG7DKxZHPh7p3dS-xBbJHYChIhXlx-0BHvQ1nijFMKGDC5EYEbtMETpL6UJ4dqgEk25576aehqEpGiZAd2mgNGp-0SylA2g0zL0ziY9j4VAqhMuORXAGBMgyQbjfL1LKC7EWyVrpyFNY1O2Ykoixi81iOLzU0k8OL1rjE8gjHPDgzcmFoPnL-QkPxPr03BY55hAbi1Z2pbjUEeen98Sm0YD0XoVnuOgqV482hteaPIkzDdRWhWAHUSq9ngORrBIZpCO-1mIBH0mpQREYiAN7rICfacs5btta7dphuc1h7DGQ0zvG5wc-Vl4b6xpjQ3FjRtyob_rgpQzGmr0DkhTvvaXcyqR-moeRTyd2AIoqXsp3exmff7wpWcPAxDecRqd1MQ-lrxvNNqMCsgXSoUWmFEziA_r2m1z9KGWhM-uToK_QlrztGkpSjcTqVQWxZzY0ND98hfvDV_h9wzqpnJ93MURiUIQrhr25GuhhMIdzVGzyXTgpqWSqXeZ6JMknJ2A7jDnCTSO0CGRukpTIf0cgNEc0Xfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر ارتباطات: سیاست وایت‌ لیست در کشور شدنی نیست؛ به طرفداران آن گفتم ماستتان را بخورید!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65552" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65551">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65551" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWU0l10leem5l5OtNOczbFsOPZLGktklx0wbxWtFr4Ys5U5eMjadYHIzmYnqgYOGlMABlF0xfjRjvFCFGtndMi1U92wOv_SSFls9NQTXEtoPp7ONarMs6rklJ6OqRivNErlGuc2I8CBl8y9hqoB7SlY0RilDL3lHsxk4jC3AItGxpWnWjYdkMVhrOko0X1282fSyyAPQEMiQwqiDYpL7X6VqRO8Q-1vEHm_kHKJvJbijHw2FcGcz9tGGGdBzFj-QML860bmZxMV9wQ86Q7pD0quVlHNpTUyKAjK31VV2YBo50Fq5gNAO0t8fmqCddP-QqvH2gC9rgWmp5L5zYdIG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65550" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8cv_VtMgtiZWK8_NpVikG1Op2SlNduSKZ_K0HeiC1_Hj1vMSgSDdwj9Pb4fRPetEVvT1NzUgVxAS0VqHXzdUJF8C77kZNCT4nlNPuwUpIUj6gxz2qRuytGbxYEaRFNJzM06khXznbjoAL29lBDcOWe3Ixk7_Hl7pPZ14WcTkVwt2IIalLIdOa2MHpQSjAmG_rt3mbINiqKG56d6UDhbimjRJOEdSew8xpOiHisva2VLfgOwqPD6uy3clD50mBs6-i0kgr9BmycQ10f6nnBiDdMKCc_tPahpBK1rtoJE8uRr-dRckmz5BKeuEgGGqIqjaDBO9JK6PQotcX3h7vwMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛
رئیس‌جمهور ترامپ از طریق Truth Social:
من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده باید به این حمله پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65549" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65547">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9sv7SbB8b5Lp4KaV9BbEkuV8TlBwb9j1CamRcyelZLsQwL7EgDTdZALSA-UAm15bpIY9w_VB5X9JJxtKZtgWiQquAPzWcSSfz4VShAnGWv6s28LWkOaCWMpRuZBMkcwxhtHXe1zxO10To1NTM2SqENRxnv1aeqwj_iY3FMBdML-Gx7XmG1xgZNsFgeUFCAKVCx-eZh0vnh_6mLkSU7cEMCxWFcvo5RIOvbPZ2jiWM0AdM5--gvjuN8Y3uGOJSeai7YlqCA0ZSFaCzcTE2Z--9UiaVFJfRSaiIwTkfnhdrJ6YqSyzVfC3Ft26eTQyH8KPVCbhp7qGw58sAE9eUKtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جی‌دی ونس معاون رئیس جمهور آمریکا:
جنگ ایران یک سال دیگر به تاریخ خواهد پیوست.
ونس اطمینان دارد جنگ ایران به باتلاق تبدیل نخواهد شد و یک سال دیگر به تاریخ خواهد پیوست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65547" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65546">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
العربیه:
حزب‌الله اعلام کرد دولت لبنان باید روابط خود با ایران را اصلاح کند.
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران برخلاف منافع لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65546" target="_blank">📅 19:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65545">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNbdxX_YTpSCAkrU8H1ZY2aCXIBCVHNKfmGxvq4RSL1aaH4bjCFUBLGTvfxdZsNuwymBZ5iy0jaNxDgAisjaZXoPr_BgnYaH5msz2nNLAorMrkGZ6L9v7Fg-_CMvNWHcTJFdibE0OjFT1RSmnNvyfYyVAgCD8M7SHV5qcRBMM6TobEb__x7DMBhrGhsW02gERrw5rLYWEQQadtHBKPlkjg-0TuiHT4gkmyWb0Kw34ThLz5F2ZPdDgUOrdvUD4JUzJmmTrXGhzETlRkmHo1Xiby6c-jmGINpfXFk3LnmK2g63777sM4-tB_k6fwYOQITQJHslF-jkE7Je2kax1pPDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب رسمی کاخ سفید در X
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65545" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBeHEPPrZ3KMaKGHN5WNTcFuTMkao_xUlltEJiMuGTKR0hnIL277KWs2v2y69s991dkR6u5xlhOIRMuH9zQWWY2R7utOVin44LoeSzfNbz8652oL5MJqE26y7GbNUKiO9ayUhrOkCZ9FHO5uDrFTyIe-qSgCnaVo7jOoL2vl246Uh8zqjJLc_Tvm18RxmH20fLb0LzZLkFODFK9ApRmS2hxfPVYFFDRpSh8IIkCI3cjPYPk3quku1F78F5SZ80nonGbdb0SrJHOl0vYIV5QoSYZc97NnlRmg4dSSCL9vNub7xaX-FwwzYW3m0tyUakOkDeZ7frUpjjibpKYzUuI_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=pTQX1FhVNTMhCVSwzJZzN4nmams_q0KYLSqVhyhwJKC7K0vmkeC5lxeJ23YSvpx9tKWn8p2-6FnHr7B0yYsoeB2nbK9848rhPjJ3IRcKXCXA8rMYRkG1089D_P0Zj95gh9_EomjUPFn-3AD6GqC9W5AZQ0tOf49WPw4o5ENhVmbeo4tm8JItfWrLnOy_ZUbfJTJ1wyXKlsQsojKgNK6fFL-xC1NaV5RoOpdS7Jzx1HUA6Nau7eSgHisZtrBDQlPMsTxGigj-gcFE07pEPpeYA-ERZciPzz9mG-z0kaWLMMKQlefSE9PnodJwhe-weGOP2dk1ZeMbFjZy-pM9X7gjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=pTQX1FhVNTMhCVSwzJZzN4nmams_q0KYLSqVhyhwJKC7K0vmkeC5lxeJ23YSvpx9tKWn8p2-6FnHr7B0yYsoeB2nbK9848rhPjJ3IRcKXCXA8rMYRkG1089D_P0Zj95gh9_EomjUPFn-3AD6GqC9W5AZQ0tOf49WPw4o5ENhVmbeo4tm8JItfWrLnOy_ZUbfJTJ1wyXKlsQsojKgNK6fFL-xC1NaV5RoOpdS7Jzx1HUA6Nau7eSgHisZtrBDQlPMsTxGigj-gcFE07pEPpeYA-ERZciPzz9mG-z0kaWLMMKQlefSE9PnodJwhe-weGOP2dk1ZeMbFjZy-pM9X7gjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیروهای اسرائیلی در حال انجام عملیات تخریب‌ در بیت لحیا در شمال نوار غزه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65543" target="_blank">📅 19:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN5i-rVa-TJn-4bCEmgBIVlUxd1fIos64LI3rmwHh_0lqXjIvZKZhRPOW9jbYrbeMTQnyMwce1Ee49xsj898iOuhlPxJHZPmAJxX4rTVjRsQ8cbcJfpIENaiKPygbr13cYhp0ZpckTEqirwP_ic4m9EShQW3t9JYYyQWC4-9NWyR-p1RL1O5aMWCfc8-NTKxPtYHUApDXNJN54nppmd6IEw65QrdnUtH7P3ixfHlFMFSRvPEqN4kYbG4kWRoVRDZYjD8SGwcObgji_JsU4afYFXNF-TD4euso8fojxilkJmK7kHct8uPSsKLzinf_EaF48WnetpsUHT_eZ0NKSjByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوژه و اخبارِ موثقِ بدون سانسور روز رو از چنل [
اینترنت نیوز
] دنبال کنین
👇🏼
❤️
جهت ورود به بهترین چنل تلگرام کلیک کن
🗿
جهت عضویت در [
اینترنت نیوز هات
] با محتوای علمی آموزشی
💦
این (
مـتن آبـی
) رو فشار دهید.
🔶
اینتر نیوز گاد فادر
🔶</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65542" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMCdAMORojUlPen37JLYRJW5Ub7vKakOYbo9E7M4poxe83tqhyUGn6olv7RQ6g1VmYlOYDjU67P8Du1vNiz65HKEnmAjXLIcFRvPNy9yHT6O5dcoplBOzB9HLS4VSmAvcdY5rK5IJrbst2G2pVCxMuYR9KdifG7XX74vaW91yUFu_6KiBRLT6xHccyyjVnHd6wPm9F0h1xSCCGlRf_B_ffsOYfgRCtf5I8a2O0af5PZn6SaYuwJh25PvKSU8zh8PMeJvb_hMPs9UN45JeLzHBSswrh3UsLcBNmu3fu20WcZsTWBkylgiKZdoOQqCXTTBTEd5QLGUVRpmMrNl4IdXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=gitCnqleZZ2d_teS5uaD2zE4F9foPbaiCvO2954CxAO9IednJdT2dj-ODMDIwZw3Co1E9MLbqp6_UPGiSUn3zsDxUOMCkxkyp6gHx1BketspW2eK5qCx5rmSryxRnwqpBvM_XsZd-poBTYX3YdHu1st6kLwtvhij0DI1-U9MqL5ij-E2PJ0JIEZ_pjGx2SQO03b7-tDxEATFfhn7GniasC3j8Q5gkYvJEmr7NkwUiTuHFRRPnec1kABlbDseeniLg8dEXxQEijL6nqS-lX2SF3t7AwPB9fMCsJqAxz5x78nPyBtapzE54e0JhrSKdFPPd5oW8SDa6IcZ_DMivZetlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=gitCnqleZZ2d_teS5uaD2zE4F9foPbaiCvO2954CxAO9IednJdT2dj-ODMDIwZw3Co1E9MLbqp6_UPGiSUn3zsDxUOMCkxkyp6gHx1BketspW2eK5qCx5rmSryxRnwqpBvM_XsZd-poBTYX3YdHu1st6kLwtvhij0DI1-U9MqL5ij-E2PJ0JIEZ_pjGx2SQO03b7-tDxEATFfhn7GniasC3j8Q5gkYvJEmr7NkwUiTuHFRRPnec1kABlbDseeniLg8dEXxQEijL6nqS-lX2SF3t7AwPB9fMCsJqAxz5x78nPyBtapzE54e0JhrSKdFPPd5oW8SDa6IcZ_DMivZetlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر صور در جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65540" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfeVKwdxzPBFpntaSPtgTxHXwGrJJvVQiNreI6U9Git5S-eeij_gneSJPxUVvJKgZaJ2aCuqjsTA70_5lwKpGfiwwS6SS0XDQ6yYoLeKGTIAix4tce9BZufVu7OzZWBNXv9rt5ugdg9_w-ttp2Jz70wBjPFO2vbkxRWt7-0NwgxqB1_c9gRaGq9Fmy1Ifirc2_b5rsgMMysGDZBDwI9xXwtvD2U9vj2Xv1kTXyVmA18hGHBueizVfz5YiRdA8p2iAEi96AxDFx216fg9vkaNvI_8AJRCf36UqehBYJgHbV5nEEFbrsR6umGBoD4EB9E0jaltURfpFSwDJMrts7KtSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر:
نیروهای دفاعی اسرائیل هوشیاری و آمادگی فوری برای بازگشت به نبرد در ایران را حفظ کرده و همچنان حفظ می‌کنند.
تمام سیستم‌های دفاعی و تهاجمی ما هوشیار و آماده بودند. تهدیداتی که به سمت ما شلیک شد را رهگیری کردیم و به سرعت و با قدرت به ایران حمله کردیم.
حمله‌ای که در ایران انجام دادیم، آمادگی برای ضربه‌ای بسیار بزرگ‌تر و سنگین‌تر بود. ما آماده‌ایم بازگردیم و ضربه‌ای سخت و عمیق‌تر به ایران وارد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65539" target="_blank">📅 18:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65538" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XreEFiP1RMT4LD2zrLLFM9VI7UyMf7HhIIb_wjBtgDZskhhzZXKDZoEyVBxF2vfZ_6nB3bNchSpqMEuVMBB9f_HIXPUEUOjEbUYkpoQVN6IyqoZCtnZUiGRg_KY2OCVj_2vlPYDNiGtdI-ccMun6DOdL0TERRbL0ISYxiT7bqoZwXF9lZydBQF2fVhTLljA9lC2bTI3CBZ6ymvtqE5uURYds9iL21Q0mlFub736NsUuqDkLIiNzyesFwT_QzMPIcTnz4v82r_qjCo7HsJY8vHydou_G5UoVYTlPSNJPX58xHtfnB79nBdPknLcSBzFxvD8zzU66fBWpSLZNQLLqxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل در حال شخم زدن شهر صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65537" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
♨️
پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65536" target="_blank">📅 16:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQI4xPumnTzR8NKdHLhvCVfw0JOBujv_EL5kNJmLsAfyqNJ3N0w9a4-t-uuJI_sXuKHGwTL_Mh07CpqJb-6HfEwCVtIKWT4p16DREigmNPPdZlWzaTDLp_UEW_F1qIfEC_OIkdp0qZOhEBzgTp9DisnaOGazBAXlIkpEFOX09Y_ujDbDVTiTqHfqy_pBMGOxp_hnL2wWcNAwpQyVJ6j5E_Zzy_ZsTjZ5JIdJe9XYoycImSqNy-kjAU_jxeDD-eY8UqoZA1VL8w7fjz40cQ39EuP2ju1QR-EZgtC9lQlx1tpQ1lXusiEIDqCebA0ZVFxiBA8CWxOX-b7Et1_VslOSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65535" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3egB-XDG_WotW2KUlHjUMDTzJUpn-2dFPNuk7G0IsUwcV15JjsbAGKpErBjadSJ2-Tk-HGIxULnBxbGENjD64etvhJSvspVhTz5HWs3M66q4LKeNRaCsDaNE6ndsKdJqVmWz-jS-Gpl5DnTlKhLK9MySdPnE2YMwsS2xebSWjfJM3-uK35AmyorqFH1EoRL_cva-lIGlP1jWbYakn84AV3bhssWXmk6P4Zrrlg7r_x2_37S37SFtth4hi0w4_CB-qZFBbGB05SipQ7d7X7MTAlTs5fk11ncah7H7BNuOec4_qUfd0_fcuFgarFH8bvwWrCNdnFDvDcprgkMmf8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اکونومیست:
ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65534" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=rYXs6hpWbLqkAmCbBibSXTgHftKB5tJJ_78S2J9mRz-gUZhkHKSLl0CyJqWvM64UQDppS_bnK0CcrbNoas7hal84Y50NNag2y5YScLwVc2gFjSh-zoQm2f-8JOiam4SBUlV7GjiagDo6rnKWTzASvICVemKBDLeUuBjUEWe8vl2xuVtyEUbh8IuB1ojmlRo5JiJ_ykvn_d9_5c2M9b41Ag4dESoXTpngVN10c7HgGscQsYOqKRn9fRd1xxGslwZYMpEAX2CKpeyXjeDzYT9PAtcmMc9pf7rvYJrZQf1i_u1HN40yRKqpI2PGuFug1SK--pkzjVVjQvgJja_Qmqfhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=rYXs6hpWbLqkAmCbBibSXTgHftKB5tJJ_78S2J9mRz-gUZhkHKSLl0CyJqWvM64UQDppS_bnK0CcrbNoas7hal84Y50NNag2y5YScLwVc2gFjSh-zoQm2f-8JOiam4SBUlV7GjiagDo6rnKWTzASvICVemKBDLeUuBjUEWe8vl2xuVtyEUbh8IuB1ojmlRo5JiJ_ykvn_d9_5c2M9b41Ag4dESoXTpngVN10c7HgGscQsYOqKRn9fRd1xxGslwZYMpEAX2CKpeyXjeDzYT9PAtcmMc9pf7rvYJrZQf1i_u1HN40yRKqpI2PGuFug1SK--pkzjVVjQvgJja_Qmqfhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❌
گلایه یک زن حامی رژیم (پرستو) از رفتار بسیجی ها بعد از آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65533" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدند
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65532" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
شبکه ۱۳ اسرائیل:
شورای وزارتی کوچیک تصمیم گرفته هر حمله حزب‌الله به اسرائیل را با حمله به بیروت جواب دهد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65531" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i58Gz2-mxtf4mtcXrHQ1DvDar2o2dg0I8nTD4z_QElWfNVDEXadUCFwJDVG1JhTHnWeTm-w9EVAYokLCLtHDTOu_s8I6mhwC7KJbQbINBtU5V8P7fXFAjjFVR6027sElMSmrWZEuyy3ZI0IV5IOpo9eoCytbx7bictLZLok7RvXwOpgeUN1s4AjHNCfdHUZ6R-n0z5c6HWAFM6O4i5VRJnXM5yWOHGAJREbUz3t-ma_fmYRTdWLnsBszeJdW7YhFvUSmHsrLqxslGXmjTXeDMXlBsoKUbVh9CmsoRH-tXHpdB1cYsw3gq-SFGtfR-JJSOD_XEs5AqZxfBlWePqxUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVGXhtTbeTuOLNPc85I8nNRVkO3De1OOLsNSK94rBKFpm3UmPUHdt2sffWT_nG7PD0m4UaqBDZMNQ0tF6wgZw7JUih3zC2ojwbf7QnisLFLu5d-lnwn7rNoJujanukTzbtYX2uTqujcLox9dmYn_meq8iJw1zKIJKzlpsUuZfALkYj31rNv77JjyoFTHA8PL6q7CcI0Ar9w6CCv2OR3th0opbtswCQ34nw_AB5nkSctEmhm_FaTOLz-xZhPVhBk0qHlfsOLxh0n3YNLW5uXLvMF3Q25umfdRLJGFmAPLaAVN72lmDuRcvvEBziFdsKThnuKhG0YJeNzpYbnH2TeRbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
حمله هوایی به شهر کوثریه الرز جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65529" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ستاد فرماندهی مرکزی ایالات متحده:
دو خدمه بالگرد آپاچی ارتش آمریکا که در ساعت ۳:۰۳دقیقه بامداد ۱۹خرداد به وقت ایران در نزدیکی سواحل عمان هنگام گشت زنی دچار حادثه شد و سقوط کرد توسط نیروهای آمریکایی نجات یافتند.
همچنین علت این حادثه در دست بررسی است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65528" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=DizhfK4bjtYjbnoV1LLxvWxngFLueICR4cxKO7yVlrg0ArW4LgJM3C9C1mbUIDqPvpe7tjEpDookIE9vdT8NM2nAOsO0TKRgJWs6rLO_WkqcDdvVJbF2PnYrFr7NhRABfzzEGKc6MFQilBB5YY3LPt14xuA1J-b-MAkIrF0HlY6wrzJtxnWBlY-89UY5HcdmsVhQhzEBAhUDm6LYGoWRM5TbVWjJYqe9pODwQPMjLhr4nMoL53gv_dcop_uIzvsBvGkEKTM0LCs2EHQVlOrCTur9O3fY3J-AzuRrZfVo_1VJdUz4NH-yxUz6eos1bRxjKrDAn9-NHlttcbE91ZzYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=DizhfK4bjtYjbnoV1LLxvWxngFLueICR4cxKO7yVlrg0ArW4LgJM3C9C1mbUIDqPvpe7tjEpDookIE9vdT8NM2nAOsO0TKRgJWs6rLO_WkqcDdvVJbF2PnYrFr7NhRABfzzEGKc6MFQilBB5YY3LPt14xuA1J-b-MAkIrF0HlY6wrzJtxnWBlY-89UY5HcdmsVhQhzEBAhUDm6LYGoWRM5TbVWjJYqe9pODwQPMjLhr4nMoL53gv_dcop_uIzvsBvGkEKTM0LCs2EHQVlOrCTur9O3fY3J-AzuRrZfVo_1VJdUz4NH-yxUz6eos1bRxjKrDAn9-NHlttcbE91ZzYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از ساشا سبحانی حرومزاده و آقازاده‌ جنجالی حکومت درحال عشق و حال با پول مردم در خارج
تو این ویدیو به دوست دخترش یک ساعت طلای اودمار پیگه به ارزش چند ده‌ هزار دلار هدیه میده
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65527" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65526" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
فاطمه مهاجرانی، سخنگوی دولت: میزان قطعی‌ برق در روزهای گرم پیش‌رو به میزان همراهی مردم عزیز بستگی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65525" target="_blank">📅 14:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=JXdyCGET4_e1eqgOEas1_pRAJ9IVZ6C2BkGrv1nc4U_IWTd4uoXDb63lsf0oAXcaeeWhGD3o3kM4zEHxXB5twBZuJZVwyCn6ZwYdi59Id4LJO1styQs3T55DgP17oyHyunMzeajjQdv2CyARSA3FXfEuWudCu7F9TZLzLy-AWGSCN7PkdRAu9KfdXtFAdkXn1t1o9sov0dkt-xf-DKm8ZsRewmcOAS5rAOeMFrJM_KpDX1GQKUdUk3kMt6p04lIcoJY4dxIOHr7vCQE_wd-n9Itfxd5uAMOUWvi2aetbKHT0362G85lTeraHsICfWcRsHZ1kcCRSEDHFTAf0mfPfkwlIfPljjV3cZMrAxITHTFN4_OYVsb5t28nM0xhC5WboAm5EVsv4OjbmN84k4jcb2kCKw_MeX8Zgl0u4_5YOdaAfjv5eozIgV1F0M9V6ZG0hXC9fo06fgqVrzYGNur0kpDbzMWb5O7B1iBiKxNMu-s4B_0mkgmnZ245_3u_a34CtNrGVMkZLB4YWzsjI6qVWCACYbBr4Zbm0qrlQLW3FYmNacCKxtEU244WuJb3s3mAm22H8HlO-SLz-WYE49Kysr_mx5Q4L7gJcFs8CNCJfhBzMvoUL8RUDyR1CPPGV0Mwu8oI4Kkfj5hklBhDG1vxYnYZufvnlATBtnRNGifJzZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=JXdyCGET4_e1eqgOEas1_pRAJ9IVZ6C2BkGrv1nc4U_IWTd4uoXDb63lsf0oAXcaeeWhGD3o3kM4zEHxXB5twBZuJZVwyCn6ZwYdi59Id4LJO1styQs3T55DgP17oyHyunMzeajjQdv2CyARSA3FXfEuWudCu7F9TZLzLy-AWGSCN7PkdRAu9KfdXtFAdkXn1t1o9sov0dkt-xf-DKm8ZsRewmcOAS5rAOeMFrJM_KpDX1GQKUdUk3kMt6p04lIcoJY4dxIOHr7vCQE_wd-n9Itfxd5uAMOUWvi2aetbKHT0362G85lTeraHsICfWcRsHZ1kcCRSEDHFTAf0mfPfkwlIfPljjV3cZMrAxITHTFN4_OYVsb5t28nM0xhC5WboAm5EVsv4OjbmN84k4jcb2kCKw_MeX8Zgl0u4_5YOdaAfjv5eozIgV1F0M9V6ZG0hXC9fo06fgqVrzYGNur0kpDbzMWb5O7B1iBiKxNMu-s4B_0mkgmnZ245_3u_a34CtNrGVMkZLB4YWzsjI6qVWCACYbBr4Zbm0qrlQLW3FYmNacCKxtEU244WuJb3s3mAm22H8HlO-SLz-WYE49Kysr_mx5Q4L7gJcFs8CNCJfhBzMvoUL8RUDyR1CPPGV0Mwu8oI4Kkfj5hklBhDG1vxYnYZufvnlATBtnRNGifJzZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
