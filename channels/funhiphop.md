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
<img src="https://cdn4.telesco.pe/file/X_-e6lMsEVsGECStl2MxiYm7fD5NtfG667xkgdFURD5mblanx61_mvDNFT9CHpF3cB-0FOLg9ebGqwSypLaBxUod352XvDqI3NL7SQMl6P5fHLujekxhCn2JeZ_DOtXkhTfSFid1dGKXZGcCy8YG_lPZWnuZ5qH9auzhJXZ-q8sQ15AVg6ZlxoFiwQ6g8xgWzZcyywBagCuggXckN-KxulGg8lEXbvUJPdnn7kkl6_yRYzyjpz-UL6z50cGhlFAL9IgYaqXxr9GVB_w0LUNbHLYa1VTxz-RQ921WUYqBeee4XdsHJmnGfmweOci7pJgVe0A5yedV9cnJfHaNp9z1lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 533 · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=WxScwditMidUaI45CsEb8-hl9CHTJ6MYQ4q88blMsr4Q-JnfIxcHV9ZC7-KE-MMrEjne7yxRnu3gGVKlEyYRKYjEB3fZ5R-31jIZ7iEAo0x29uOTBjZG3FWeUEo2b3SAWydS_PMuytojJKMiyHhB99BH-dhMAbMYlbPl217FeXaWegqD3eW-30WDjHOF4_JAcFQGZmAnRZpBLr-wtYdfgn58OXDAAH5TBlg_dSjfB1zWLXgwxLOOUHeremTD6MP_oMAUJ_ptD7Dd_yafWOoLzncaEJ_zq9WSBphqcc_Cd6Bdp92FjByIpADpXTSn1ps3K29gXFW4mNfmBvuwPmMYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=WxScwditMidUaI45CsEb8-hl9CHTJ6MYQ4q88blMsr4Q-JnfIxcHV9ZC7-KE-MMrEjne7yxRnu3gGVKlEyYRKYjEB3fZ5R-31jIZ7iEAo0x29uOTBjZG3FWeUEo2b3SAWydS_PMuytojJKMiyHhB99BH-dhMAbMYlbPl217FeXaWegqD3eW-30WDjHOF4_JAcFQGZmAnRZpBLr-wtYdfgn58OXDAAH5TBlg_dSjfB1zWLXgwxLOOUHeremTD6MP_oMAUJ_ptD7Dd_yafWOoLzncaEJ_zq9WSBphqcc_Cd6Bdp92FjByIpADpXTSn1ps3K29gXFW4mNfmBvuwPmMYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw5xEH39-jISZ_AC6flT6shKOLRJ8EVRoP06OZ6qrlxBjzj6a2PezY2Vkx0N_-12QPoVsoJUau-VRBpXlpv8hmWGvUtnPxSVcC_mJzjySDxBICrZlQBqggVJE7B_qwYpgKVtK1Scw0Jxug09NjXvWKgDxuCFpPGgdV4h2LxRvzUcmJrrh7hIgeflsfp-nbvJe49Z4K5iOM8eqybxF0tGPEFDEUBGFT6SZM5bSIFYCgCq_0aK_3_pWqYnswTZDAwmBZD-WRuYekHZAVZa01bRDID1bzKL1JFEQ2VAM-M1XCo4514nsO1mIzKLtuMxjViIHoCahItqbCL01E_VrDdj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rivx9hgQqKhbJUfS23FZNO7gKZ1pZjkolTShR8U1WRZh3Yj91oeJLGBVPeQ_Bi9BYeeFQeynhy_inodiqLs_apAOkImlfTb7CrQsJ-qNMNnMj-Rr4LND5wR_NtCr38OY4HHcx1FCKeUfE_zEsvZvcoZMs64CUTdeY4-4gFwrpswLQ3AxUhpuh6Ii_9XXclb0LWKiLFlPpJKvw-mPv8CTSaRjYwy6daLyDzqhycC71iOO3UjQIXLManVxCIoMHwvrd9NTryBJ0y3f8sYM92VDarjYmmSwx6PjR5c3bS_saRyk9kr0tZ4D2fUeRSw97UZDoXHlsxhhiSb5lebOzF2qBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8VVwY53x-6xuTH9neN_GHWd3Wq6o450Fx3l37K2ZiaCo6wlDR_l3cAxxHavka25O9cteyf2q2GtDkf2o0KROUoAAcrEbx8fqmRAZSJMksTwzOntoFAH56P9cB0W38k8t-d54V0YeK9-4ZXu6KmC06VzwlAWXHeHgN5rAAukWTIKVwttZV5iCJYx6cEeGtuYFu52hfqwa0VL2OPFTqEz0NXYQxk7qn1yEATDNv21pKjKyK0Qk1Kshphjyef2HYUpFmIqg5Ts7jQQbEvJfHI-T7-B3D80-WLAphs3cY2hxPnzod0ROlLvKFxOFUcrzZQoZfEYVJVSo5QYDAWg9hxGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=YMZr94s7VZtCNJkmBPtlq01xLxvLss0EmTmQaYUJqYzAz0hbYq2ZsFpEc3WTgGZQNHQZKu3mAoOjLMhrRMYn2A4VLUepuc-aKLbVOlOcVmkQqx-ogeEMIxpqC7s3gRmtKsnuS1ku695ywvykd0s53dLczWCcoc-kv6HydGrB1KTxJMUmGOHANAtmeUQEO6C6I5BDRvCwDWfZVS183P1eQnjttbzSTB5OkhIbJpnIdaiPRMIxeAYtG8ngiehbfkCC4Y-3y2jVG_URXe17fFNop2KjmEI5QJ44L8Ve3R45hhw943pmRgIV8OcS2VSyN53eTqhVSqD2jY9RApsavmoNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=YMZr94s7VZtCNJkmBPtlq01xLxvLss0EmTmQaYUJqYzAz0hbYq2ZsFpEc3WTgGZQNHQZKu3mAoOjLMhrRMYn2A4VLUepuc-aKLbVOlOcVmkQqx-ogeEMIxpqC7s3gRmtKsnuS1ku695ywvykd0s53dLczWCcoc-kv6HydGrB1KTxJMUmGOHANAtmeUQEO6C6I5BDRvCwDWfZVS183P1eQnjttbzSTB5OkhIbJpnIdaiPRMIxeAYtG8ngiehbfkCC4Y-3y2jVG_URXe17fFNop2KjmEI5QJ44L8Ve3R45hhw943pmRgIV8OcS2VSyN53eTqhVSqD2jY9RApsavmoNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCcAwtlZDXEb25ZYi8kTEn28aL21LFX6oIp-zDJS16EqT84CSFVDdXWkrdC3S6s1Zljar3osDnXbI300ArJgmKAVhYegQTFS5rgCoNfVww4klDLiF6ompHaEabNuTqoHzMBHy1TZ2J9VyFyccC7RtsyHyueNCKdCXdzR6R7JNkZQIo1X1p9cwyc-l4brGoIfQK6Wn42iTbdJr3sRN-cUvJJiP3Z0i8tF_tYQrwe8dllqdQCIsZlIhiVfYjeD5smAvx9AWKIiRGs9bVnJqc722TfXJCsXNHDhovCwr0aIvmIRcwp2RTUx93Fq6dK9J-_OTa5aOsxKD_8wZONo-wq4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5tyhDwgetnvo8WrRQAjPa2M2E2bDPlBs03lliBtGzqlP1bF17A1swq-EheB9_ZfoOsMwLisK2yRugq8YvGFfhFAZfOt5xUQt9v8afJct0gDjB62p68YW29BJiBkPFVH1Wh5RF6SOb8_n14h620fW9CVAGhmalAN_M3tMef1cdpI-NETTcPBRREFE25b5nRueYNEbBbdCzoPHU6E752xBcv3OcYvBNIF46d2FglskNW7BJwtHMNEqUDyHYe4F4dk08kANmBh_bQ37hsbgZehelU-CLgvPn7yQYzyxQleA27Jno3unQVgB1NxNbgCdsaDQ2zGQ_5EqKma59WYJmb5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl00ybTLk_rAgdCSk9ekYQGuSX42ACaJ1JyoZlDwioH3uLLmgp6Ox3g1arYVw1qFKE6ab6-zX7eWert5E4hGVrjsMH_SaFo-S0CShjm4fKOHTVBT96vqWAltHh_T9gnO-_ycNCD2Sfb6gnvVyNnbWQND9H9oCDLVV1fKKgaNnPPUkQDdyG6L4q2vHpq81Nlf5E_M0REIuZh1L51hriXSu-qyjcUyy38AyRl6wp1asVrNo2YP9iXOF9SQ1mA9cdLcoY8ePc37jcrf9q4nEjkbM6Zq2exjQlXD399QMa1fzuIjoXYeGyRPabwojM6VPrxpNuq4GLfLNScbvdsJMt1mmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g13
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76760" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=a2O0szjw2x0STkSN0QWaZA1ShezVY-Irksue7jQvABiSQR_dxCiAK2Ez2nBXET-AM64GzSs2Hc_zKb7uI3MjQtfI2DlewVkCB2TAiQetlauELlibPzUUFktEvTJTy4akLI97LJRnf5Hos3X6lCxkmT6wCTGF8s9rDI_-ba2cavIV4OKczc2vYFtwhOMc0wiAMuYBLv1XcCx89mMP9Sa0tTT3UbLGCNaJODNRYmApW2P8Trj-t5kypiZcKylolyKWYLjancqirN1FfUIU7L7KrDdrr8qUczJx7WABp1UqpL8zzw5YhC4EBl_YK6jqfLwld6dJj07-It1S608Wg-idDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=a2O0szjw2x0STkSN0QWaZA1ShezVY-Irksue7jQvABiSQR_dxCiAK2Ez2nBXET-AM64GzSs2Hc_zKb7uI3MjQtfI2DlewVkCB2TAiQetlauELlibPzUUFktEvTJTy4akLI97LJRnf5Hos3X6lCxkmT6wCTGF8s9rDI_-ba2cavIV4OKczc2vYFtwhOMc0wiAMuYBLv1XcCx89mMP9Sa0tTT3UbLGCNaJODNRYmApW2P8Trj-t5kypiZcKylolyKWYLjancqirN1FfUIU7L7KrDdrr8qUczJx7WABp1UqpL8zzw5YhC4EBl_YK6jqfLwld6dJj07-It1S608Wg-idDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKEf9aKJSrL_pCq1KMsVDUAjPAHczEU0QrrQfBKKUMAhE3JtC8W-6bidAvJnvlo1UBqP1sek7HIJY-WvJSoivXrnEakhizTlzlROgDE3QEpex7DaWx9J8A8zU-fnktbxG_rVROou3LACmF2G-tovhFAJ-RJokq71gDS2yKkoWFRMkjPFbVDPFdtImC_UwE87Z3-WD0TxR1bQXAvxEhlF6pg7_50a0yH3YNoR-5YUgxxiACED2MbPYLtJ4-eBS1d1AWEh4cLjG2MJRPUkFUrA3JBAkNBsik7DFMEYTmnl5WgA_21u4mqa-bG156hUNesAEL33zQnjkz36F2s4zeKriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHsS018BHXMSw1jdTZsZyLpmbCAc2GoIr9BRrY-1J3PrhteLWw3fMTAEdtcRyiJ8YRqSchZc9IBKwbJ_GvQ8JqsUrkAhxDiFu0JC9OIfeEXZ3EakGudc_tCWyS9ZTOCIPF7RYuYpFwuz3nBHSy5mgoNVS-kcbJ15MS6b8yYN1ncVUIdnGHWWtPETnAs7kwKqW8FIJ3fmHSqiJb8VRyQZpUAqRcFFi4hmQ7xaecHFFOZ0UAlnlhG2AVf3MehXMLHRHQUVX7poL-beCdcQMaAJNFIxvPSBdOlJqdL8AGJ1AQ5EROJK_QxKUpoVp4rJgJOHz0m-wDXRWkYPS7nSGqhWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIYOgisCQqnMzezLmG4YbjwhUB7a6oarH84LRiKTjKXSAvVpQMyJ0PF-rfTYMECGkwHP6LKDffasvo4lA7yae4zbJwlmRYbGulHkis7OGPdPz1HNUbP6B3waoUA973_687a86w7PG1ziLpuYK8oHQLzU-iZS8AHSasV7N3Q2N69_e4-2SOV6VHZpVw5cY9HWxvPvzjWniA1gCPUHb6B6qPEJ9y4wI2yg0IFiGY-Q1Lm9dlmTV7tSLbuk8O6yubWhKXRjqRSqQyqMrMcgGbDQeUieIwSkRPGLW3z6K3pZ4nsbQIDgPjH6EjlkTxf3b4d0jJRrtZgYM43sPWji2VCcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-DiJX34PCNujmlNohAoDl7diCwXVwTgfrP9SFf8RO_4iN_36-1iPOFE6k13xiqDEjptyTnK_B-hbjiwuDTw8XjOOZsWShB5DJnodJOoZAP27uT5KXgmaVTKoIMixg7zTcFhl7cXE6BPUJlwD0Px3z32jr7vGHMG1CPAoYGCM5d-B_KEqcLOJYVNaXAAtmG_5mP8xxMBI5CVllmPi8AyyGOlDIi_h83FC-hsiovp8yGITvXsojr2-nmHF5VthXUBozT5rMWIY3o8OP1BtEV9lt3wmS-dp3tjWNyQLEjmS2kGbj1nPlhc-I_90Txwek99nkYHU_V9KjbDhPTpL8-1gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVRercLgqh_3oh96m8hrdfzyIHC6KCIBT2_huj_mWf4oe-KdhEm6jSwyf5HJS8u0DqISuXieZrc9jWcGz9IeQOFQD5CuPCTFuJBiQOGlXQQlSDlcQIUwJ8sqUEMnfm4c7gWtRL3WBM2Ou61iiFo7yXtWjwOLp5lffxV2ctQuvAsN1jk3NwKY0ehW4mFEKRHIh8_8iWYXJnsVui8EXDu7BL37_qsZp0DFfZeJAhFrQSiiAfJkmqPyvM9y7j1OicIOankMRyUNvl2LSq4hM0vmLohK9Yh6MtUnqkaQ-KYguXxtRiRCBJA3NYhJOcrsVJn0EKR7LQohG4or79aTTI7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=RbKgCsVYGYutCdA0vHZ3LcRCgczzhmG8P6lrTq13lBT52kHTJePm4wnkIcaKIE_rKB0usJYhDo1q66dy-IqjiHKnNO6IvHsOX0H3IdkCduycJtuxthEmvzxu4OoDhHtupmHFZUJOvHcfdTkKF7rBdtmDXlnZbRUriDbTN47WEh7pjatd227zgGgLzJ2OHkM6JXrMMHXLPP4fL4y71GHvAIemTcusLKPhbog7EfAOGl3yggh3isJCRs1XMs4kb8UWudxjf69rRssVKWnXNzcnpgpqXa_14B568U2-P1ERooSC8EbmVswEr3dzE7ALIa_jk6hnWwyrdjVJ4FG4mzG0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=RbKgCsVYGYutCdA0vHZ3LcRCgczzhmG8P6lrTq13lBT52kHTJePm4wnkIcaKIE_rKB0usJYhDo1q66dy-IqjiHKnNO6IvHsOX0H3IdkCduycJtuxthEmvzxu4OoDhHtupmHFZUJOvHcfdTkKF7rBdtmDXlnZbRUriDbTN47WEh7pjatd227zgGgLzJ2OHkM6JXrMMHXLPP4fL4y71GHvAIemTcusLKPhbog7EfAOGl3yggh3isJCRs1XMs4kb8UWudxjf69rRssVKWnXNzcnpgpqXa_14B568U2-P1ERooSC8EbmVswEr3dzE7ALIa_jk6hnWwyrdjVJ4FG4mzG0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcLrYw-HaN4n8n4qnMCiEKZOPE8qHBUPU31vfJcr_m3JQbLUUX63XjpsYgavtk_8LXAUh09UxCT6k1XQ1VEu799021VNVpHw9SKXiDa0lm58IHvBWyOeKUQ2Mo2H_KjHXOjzCMDlN9SiOtCn2rweAXwUY5OSykRGnNGO5QxgYmnO2udI5HyN5_-YzVlhUz9FC7UpdmqM5OeGWIKYi5jfS4Hh0SKVxvZczgBV9lDiKySAvJJPNsUa-bsqzMyDXhMyRZSw4O0TbFBjUGQ6yZWJ8JbqYM6ttXkkjaOI0L1k2zD_3_uiv9X8wnzH87ry_9eu2IzQ-zsQI5_ZPA8xR1ncuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=nU4c3lBbGaAXMpEibuK7Dc6ta0oOyRj-8eY1n8Yg3AIXSZZTHxV34hPQoudpeLqO7CyG3tntAM5AOan4CWzDKU2gy9iDe3D0L6G0kNRx1ynnm-Tdrcbt14ByNpUxN2fl-NrYy3zHzfdwfZES3UECcgRwM1QWYFMfMyb6TaUd_eOpMSe0sB5JzodZOeS_M4TWjwNPdP5c-8V0AzKopKjU0dKMwofpXhO1ZwO1623bUpVqwn58f79fha1gQSQ2dXw7INMGCvf3sZj_c_jZMTQLZEOmvj70xCxljGtu7niq2S-373BBHjB197zIQ5vQdMpT7NpMoiLDEwzWvdHB9ukCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=nU4c3lBbGaAXMpEibuK7Dc6ta0oOyRj-8eY1n8Yg3AIXSZZTHxV34hPQoudpeLqO7CyG3tntAM5AOan4CWzDKU2gy9iDe3D0L6G0kNRx1ynnm-Tdrcbt14ByNpUxN2fl-NrYy3zHzfdwfZES3UECcgRwM1QWYFMfMyb6TaUd_eOpMSe0sB5JzodZOeS_M4TWjwNPdP5c-8V0AzKopKjU0dKMwofpXhO1ZwO1623bUpVqwn58f79fha1gQSQ2dXw7INMGCvf3sZj_c_jZMTQLZEOmvj70xCxljGtu7niq2S-373BBHjB197zIQ5vQdMpT7NpMoiLDEwzWvdHB9ukCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNZokLQ3tIA39shAMAH3DKE8UyLUzVHaKkEamk63z834y895KYlm88m0WTUO1Bbaaupo27aaVEL_NjT0fW9bwt-mQsPsO0mqPMUG5ETyx6IswUVeFgw6fagcwTQFx8NHMJ46uM7FVXTmJbI9rCx6Ci7Pv4O3sIHgy94SB1mpr1Qp-tmXY8ZGie59h5mq97d3dYmjxhAwuQYYBvTbODqj6nX27xRO2eNRPK-xAN2Q62Jz-o9vkbneGGq6hXcN3DdlM_hG8CbJreBbhzX3DKnc3nX_RBwJtnTXYyFCBuAQ4KlJOOXff9K1k5zVk5WdvdvTHE7NPDXWb00Jh7QK0ZspiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G70JcC30bdij_9JuzjHSQI4N-ahaM4lQfonu06sBt_lmmQoecd2sxTxJZDtmyMgMUOt19_0avIkPrLRPkBlquj0tf_ecCJAZObF_Ad2m0HoljoKFmJBpdDzDIknMy5AMVxT7sr_jUcNYUz-AodvcaXJWOoCR9Z7kRg9Xh5FuEtAHZffv6Oyh9H4gLwDjnEpeoLATB1xmvt8BU3vsQ4Z3vS_WVN1tMU-8s5aM8WbrlMXmnHPbQ3iLpBcdnrXnGdaIcpQZ8IASXrrU0r5dATGI-fG7W6tVsN8NLevJrJ4Gv7BBGKgrOexvjewyJptndCMFZPZ-UxrGHIL67zDVLw8-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFIIzvy8icvo0aq0NvYWYovNfmc1TM_gI-GxHm6mU6YQnHc7yGEuxUt07eeciwRDE8f9L6qRSP0MTq2J5ca6zenkDbRxtdqvXSUFxjULaNoT3ERKQdjE_9tWOEbJAwJPXgO1jt6Sx5lnOVyDowahNRbKXE0yJFhmT-ZSDgqYYzAHMk8GFqJ46wny2JZ--Z15s7N4Uzxukn739AvnRtl_PS_ShghQLA7vBkNeE7u2ImdlhrExu6HSb4xcnrgWkDex_A75mUaFgxiH77P1FLVJiAQZNGLH6ok8u8BEK9aTakVvAHoO2FR6vP7XN_K3AU7Z6A3GugPPlpgTxVm2mXzfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSg1LZnCmXs1_NmzPkyvwmGXrr9T212ffg4KUj-m2C23ERaX2G1SAAjdZuixjacIVNF1-y4DLLsV-9ZRy0wB8Dd2WXhrBAj2zZbvPEwAMqInI4SVi8myj7DXecpHM1o8zQQLxMCxQE5W4JzL6sgPTDg2a0PNPf6Bp2SN3HD46Pp7YtzLnzhQ34YhgL8Zqy7SWV48x3uOwgtvteZausUEIUAxQ156QAH0zoHEuxJSA-m8zDg5CUW3pGFAeXVTZyTGdwBPtkzH_brJzHUoihoyrs9nfMk-1wY1DiAZ2lP4hDRISOLdPGapJncX5Kn1QW-KxZcG_-2XyFZAQZIEtgbTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDIO4DB4FdVrulZvcKDGkGP1YES7eKnXRIpsuUrMbKix6PplZcS3WSdkaXcyxpE2bnlNXGnsnkNa3qhk68sKcffqmAu4uYg3JsxTdWF9ytXiEHxPU08VbkzuoVYP_aJhyIYacBimL2pEdK4CJN4hWJ7CxCK8BHLM3mP8iLouWvzNHHvO79M0zKjnMbY_9Imo-S4pdkhjXfAYzXSDNcvY3-AZwXp4aMCem6UPMbQ_dHJCdbkMCsv3N84tNL29MkEJ6wGo_6CeM-RjS5gO3Gdq4BVVmvuUgZa4xaXJjrh3SycfXF9F_-fZCNIpcFXZd-xjLl5t6BE4iw29AOuXyzD45w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8g0B8cvElNtrHz1ZZFSeuBzTQwx1HzGbP15zlh_LILJhQQybvlzbb3B7i1VXo_9MlkxOip_Jb6Onf4x6SZG6hQ9axzEbXeHqEBQgRUPB8vNmfYJ7lIB2947dzsZbrYr2wyBCaia-oLdVX-igOEieTNyf7e78yQ4eawHFAQsjsMQh7zgqMIaLR_CXkNqMgZa7ZQWU7NlRt1Pb_PP5EuNX1Y1UZ5DEqaiqrFYIMqvUx3RFGTdo5hfIiMXFPwxjhxWR4D6xmQdjIUHaeLukGieJzY-YChRkUjcjSp0Ghf1SjmWCWxxL-s3fBQg-drFePDKL3jOVda6AiqBp1rnA6wPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVBurQM3qmunvZ9Lz6VTCxzYgJ1ToVgXTnYnMZcQyhic6OQlrpJYC8g4cqxyhQfgZNG1vUa1CZ4RhuUviWecZ0tEF2Jdlp0mwjl1M0XqaXr9qwWZ6QhgzgVFXGQYgFG9xsH581cpt0yG1zYWIMLb1h_5i0_PFhY9lXijSB-0-rxITCNJDQzGCwr1bOzuIOCi85-iWjtHRT09W3UIprLbAQZhc42YQLaaKmwux4AYE1oabtm4_KdV2U_ySHZecwjY5HG3EhJGn-OEPj6El2PxpRT0spOhgzl3T3TNGY08ZdDm0KAMCuO4y8yYVYYS8j-eGfNvd4mx3VIPrzo9xZztHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76718" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76718" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEvjQSHEDUCvMEPpLp-yzOEHnf1vWWAYlaAB-1ycCZPQwSpZYnkK_njHKc_KCBlpVhnquLljl0VxEkKZMFk5m9SCLkl26j5bdWlq89y_lnVT2odu85z1rnhlqiefsJZkdwAOSrA2TjNxjQwG_hr-hkwJFm3mpn5Hohf1H07y_KPSs6IAL0f54jENQQWB4_1hVSsHhLJq0Sm6BlwgVgM85E8n0_m8VU3y8vHxCmVwdlOFrdbr-fHouo_MpScEKQb06K1mIhfiH_ZM2tCZNkT-f4yck_yPlqwaKF3LsB-iWJG20VC7A8siTWvhNmnuWWJXTidr7-PC0dRagzjqDpa7fA.jpg" alt="photo" loading="lazy"/></div>
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
r13
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76717" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوبی رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/76710" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عربستان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76708" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=emcSmaCsrxuhLqPjqvez1o4rQ_NGlNthuBi_LmdW7M4iLQkAff3m6oCIwRYgNdFJowgj3bx3HXD1jf1VAUebYZsp96mKU3CgyWJbozR0DjHKJeCvBBGqMpLNxdIe7h6cgs0yQbYT_5J03sP2qLd9VRMsgV8f-4BhVla2-fSGTM9vwqEZdd-YJA10oTvsTbFto5hyeoc6BIYaHcW9GZUO5ykAU0ARxFAxDZwCzEWyaIvpUdBB4sjpTmo4KZAzFqNUF-zcpdZpCRr4as9KvAZr1mjQc_KIHIqRIFSJzx92cnxHRz4Ukryw-5MFApYRAKg2ZgM5DAwRF0ofeUVK_h62uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=emcSmaCsrxuhLqPjqvez1o4rQ_NGlNthuBi_LmdW7M4iLQkAff3m6oCIwRYgNdFJowgj3bx3HXD1jf1VAUebYZsp96mKU3CgyWJbozR0DjHKJeCvBBGqMpLNxdIe7h6cgs0yQbYT_5J03sP2qLd9VRMsgV8f-4BhVla2-fSGTM9vwqEZdd-YJA10oTvsTbFto5hyeoc6BIYaHcW9GZUO5ykAU0ARxFAxDZwCzEWyaIvpUdBB4sjpTmo4KZAzFqNUF-zcpdZpCRr4as9KvAZr1mjQc_KIHIqRIFSJzx92cnxHRz4Ukryw-5MFApYRAKg2ZgM5DAwRF0ofeUVK_h62uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPCK8_tOwB0nPQNIj8pEv7YbUxMQeIX42yOTlD296puFkg7IAH753cCvyRFw_dLzmcBFpIrE4UJ_4ZXP2-8uuvZW_thwFxTSlZHAFsXKiF7rzysCzABqEjmUxpzXOYgoNrnzQNBSqy66xs1KSMolH99WCz5xJoWT7YZGsU66sUpF_C1_ww-0M3f9lIDP7-Tj-xLU25YMPWiSCAjcrKlx7huZQHegoAmR9Z8IeCx1GZC2Ni5QqeEwhVihB_P7LXw1gxCfuDchO9sp_NL9ZAchFjYEc9dqPfIOdj3DAk80wKk6J2Lm93uKRkRNSnsXcnefSVsZ6E9CUugiDO9-6BUHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF7ZrNQi6_BmqnfrSSM3UF2esUfCt5k1zwXFHGu7oEcdUJWbJ3pUqAewDySWQM-gZj0cxeFAwB158YaRfn88m_xEKjUm3BqnC8osj4hKIemx6kRM8LzQ9Q-_fRju9F7j9AimmiPU_j3Nl4ZhJ8evUs5LjzpgH3VUj1zMgTJw8oeJqlIXSPPeHtvThTibgPPmopI7MuD2K6dNcHFQsvezsxaWhSpaLjZ0tmn3wX9YSYne70voFKgFMUW-pzZn_wqxMkAsIY7OV-8hmL5FDMAMNLVB5DYYIOHUilDTCiJcTxfbH8IziFXqr6pbwBnmNwXV2Z636gthjwb3xxMxUxeBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خیلی ساده‌اس ما الان میدونیم که ویناک و حصین میمالیدن و دیگه نمالیدن
ولی مثلا دکی چی
کلا نمیمالیده
یا هنوزم داره میماله که چیزی راجبش نمیگن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76693" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از نظر ویناک هرکی نگه جاویدشاه پشت مردم نیست و خایه مال سپاهه، عالیه وضعیت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76691" target="_blank">📅 23:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شوک قلبی به حصین:
وزارت خزانه‌داری آمریکا چهار صرافی ایرانیِ نوبيتكس، بيت پین، رمزینکس و والكس رو تحریم کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns-XTBjGoghWElN7dmmlGGPX53DatHOZ-y3iHTtsMZEgZDLB-blzQ4zv0V1R8GKUD3XxCoc8d9QMH3cIYPEmchyh_f9xELcG4s-Auh-OBfkHGxAafPUBdtghXQ339uKtH9swrb4J5-fSPmLORCubfoXqEjl5MJVel2j-b1cdmNP1qE7A43-hmb7Em72zBbrOdVlXP4CeMvdCiAi-5QAQjhaisfJp-WC22UDXkp6clz2U8h_tGaDzdUaxmhb_LOe2skT3pzHL1Bazr1GNfR6UV9Cgtuv5rOPoKPkv9VWZU4qYnHLLOpfUC-SErkXOGJf3AJIjX8aKTZIV_tuUZcD2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyT2xlLH3ppqcFzC9BGGJe8C-0JtVwRs1KgLXR4TMT2_PYFMPQyyN-WyxejFwDH9nyD3JGMgI5VB13VFHpm8BuwMZBEQLnFYKr_moG9WlWd_9e7KX8fwy3eb3QGwM_-Rg3C_tXioCxB102XV_z3R9sW_z82HiEnNIR-zDX2LKsLc-hn1etluReCm3iSNiqoKdXC1t2pLwD5mHujFcBpOS4YDYp9DsgCWJin69P3hsVR3rGmvd9_vsBLYMnx2UTSHpCsL4Cxf-EeputAHn7lRCiKQ6K9oaENZowFKoXQcQJvRWnOVFxrquv9bQUfOCDaLYMXMc-i_pNdm8aq0VqfCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOAXAcWrS2kImRe6SpuUiU3RNsUX1_QwPPpWdj9x8GBC03Q4UbUe-alfh_yre9YbWZRzLK8cNa4dzSIWhXl4dk2NMb8Zb-IaOXvRtys4K8majSXbH_O3U2I5frq00kWmUF4-DM9IGFwKKxZ9GIjW-aB-edBk4b8u7Spi22gwXU4Gq1JmfnwTAdIILfrNoTVaZibMSykvVZZh71ohk8LMQ9BcRNUv8Lb48Yg5cs0PmFymAq22aQgkrPoJdfnyw7wpzLVo7PZuma9RseT2S0O8bwQghgq1LA9klBhDubjZHAoBj95qyvXeKupwbkHD7iZqVjBmR2aZS2CKdacP8q5few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76684" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76683" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">رپفارسی دو بخش است
یه بخش مادرجنده
یه بخش خارکسه
یه فدایی ای هم این وسط هست که خداست</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76681" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3ykrBCN6k2FoCYOUuh-8Eww1wfYOsevBxjOFOiNlmC9tWhXQTEAGBddeOt86hJeC_vW1OGYCLJMirvA_qAKmXDapCWIjj6iSYVL9BZHLcmq5ugGEHV0E3TDPdxMWShkcT5RnHGI3rghzPuBvQ9ou7xDYSg7Lz4_n-mH-KIeF2sTd_POaELfevRkwJZtsIVMVgZGlm7K8QXm7_AOEW6-vkgClUX03oCRLwDNkfaiQnnrwTYim1srrYNFeR8-l1m_DM2t1HpVnzHyvId_Js5Hp2ciLoxPNZV2LKOYfH0-Y1kOPvzWEzGe47kvLE_Z1_sgXF6o4lQNKL3e9kwo_1aghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
