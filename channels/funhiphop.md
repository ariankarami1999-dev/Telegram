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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw5xEH39-jISZ_AC6flT6shKOLRJ8EVRoP06OZ6qrlxBjzj6a2PezY2Vkx0N_-12QPoVsoJUau-VRBpXlpv8hmWGvUtnPxSVcC_mJzjySDxBICrZlQBqggVJE7B_qwYpgKVtK1Scw0Jxug09NjXvWKgDxuCFpPGgdV4h2LxRvzUcmJrrh7hIgeflsfp-nbvJe49Z4K5iOM8eqybxF0tGPEFDEUBGFT6SZM5bSIFYCgCq_0aK_3_pWqYnswTZDAwmBZD-WRuYekHZAVZa01bRDID1bzKL1JFEQ2VAM-M1XCo4514nsO1mIzKLtuMxjViIHoCahItqbCL01E_VrDdj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rivx9hgQqKhbJUfS23FZNO7gKZ1pZjkolTShR8U1WRZh3Yj91oeJLGBVPeQ_Bi9BYeeFQeynhy_inodiqLs_apAOkImlfTb7CrQsJ-qNMNnMj-Rr4LND5wR_NtCr38OY4HHcx1FCKeUfE_zEsvZvcoZMs64CUTdeY4-4gFwrpswLQ3AxUhpuh6Ii_9XXclb0LWKiLFlPpJKvw-mPv8CTSaRjYwy6daLyDzqhycC71iOO3UjQIXLManVxCIoMHwvrd9NTryBJ0y3f8sYM92VDarjYmmSwx6PjR5c3bS_saRyk9kr0tZ4D2fUeRSw97UZDoXHlsxhhiSb5lebOzF2qBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkgRjoDXpWy2y5yEkEKnWjowQ5g37IqemRHXkalY70QQntNzGLiI9g9521YTQFr9vhZot-jLTCdz1lDIF1kpyX9n4njGW4sq5HRiPoaNzfEiIYIlshx2bkS4wXcCU_rIUPQKTwKnsnlgjwIW3DoAShoPzeUC0Q6WIjRugmXsoSwHlRCUUf3Y7V_YbVVNrDxRLIRydgmPpxEIswfavdYfAEn8op-LiFoNX_6cEm4TZoBIxWGJLLlbmqJ6UVLF1jt4XizE4yKI5QTo11Yksl_EFUthjtka58Q1SPXW6PNfPcmlCT7ZMkLPaXwm4LD0mSaDYdLiuGvMoWIRRlZAicKesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=tMwuN3RfoW_Lc0zmP-majErnrnbGOVBXOcAwmD7tP0-yXBM2Eii8lXvHhbLykbTUg6kt2_CdLFUOPtYwtPcThsDIlxqvn_V3GsoNzVN7C4H92_mTSg2SeNSZRvxrKd9s9tuG0xrSYZeog_liWiCXXryMEizLpFIKd3rYS64nApTuCArs2fOXf26Af15VKO4SaiXOv-rwhj8dvq-LO_fZillkjf9HpEYWNdxnzm1M6pnHPH8CD_0TycyKtWOA3FhW1tDPwKGXyWlB00PnJEaXEvH2txo-Yui-r_g3YATeZhQ4IgfFHTcHxWZxx6MDkrLlAXu0Wm54FTXYIGSR2_qpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=tMwuN3RfoW_Lc0zmP-majErnrnbGOVBXOcAwmD7tP0-yXBM2Eii8lXvHhbLykbTUg6kt2_CdLFUOPtYwtPcThsDIlxqvn_V3GsoNzVN7C4H92_mTSg2SeNSZRvxrKd9s9tuG0xrSYZeog_liWiCXXryMEizLpFIKd3rYS64nApTuCArs2fOXf26Af15VKO4SaiXOv-rwhj8dvq-LO_fZillkjf9HpEYWNdxnzm1M6pnHPH8CD_0TycyKtWOA3FhW1tDPwKGXyWlB00PnJEaXEvH2txo-Yui-r_g3YATeZhQ4IgfFHTcHxWZxx6MDkrLlAXu0Wm54FTXYIGSR2_qpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=cmwjO9PWiN7RFkvbjoK2lUuQGy7rH_iv5lDM_91V_hu4WMlkYHCOaxoXkFbNApuSe11-9yyD-qt0Wr0Cf1-O4u9Bvem60lqe7NDq_YZPGu2eGVxkvj9oLyknwVgXSYf6Kg9QztELt50N8nBb_i-sewE_dDbud7i-dtQ6E_8sxuzISSA1wORbkL9ip4XEXDeQ53gqTXnUKh1xWoY7EFhdkGalM3MqAHp9TeBgx1c_LICVmTeAMlNlq13W76kVfSjt06QZQEfPZuWqYAuGyobMBoDpJaizcPFcw_WZOIrCRa1koj75cMGHJvTDcHvbFst_FO-ymz_PUVcXLA4vPjhiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=cmwjO9PWiN7RFkvbjoK2lUuQGy7rH_iv5lDM_91V_hu4WMlkYHCOaxoXkFbNApuSe11-9yyD-qt0Wr0Cf1-O4u9Bvem60lqe7NDq_YZPGu2eGVxkvj9oLyknwVgXSYf6Kg9QztELt50N8nBb_i-sewE_dDbud7i-dtQ6E_8sxuzISSA1wORbkL9ip4XEXDeQ53gqTXnUKh1xWoY7EFhdkGalM3MqAHp9TeBgx1c_LICVmTeAMlNlq13W76kVfSjt06QZQEfPZuWqYAuGyobMBoDpJaizcPFcw_WZOIrCRa1koj75cMGHJvTDcHvbFst_FO-ymz_PUVcXLA4vPjhiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSJn-gHKVlAjs9HKy3QlO-nlCfoVKN1_fzJls-7uw1VpcAUpwuHKkjIGpNUumqO0SgQYgMRUhZTDxeFNkLoTJFiU_NLjVwIfnCGvaEOfXN4xW6QLiXK4l_89EKrlByym-n5f8gWYeIJUf9k4EZk3Qg7ACMSKJ5hFeAhlYdzjGO089XQRHrjHnkoUJ5O2XWo97vb9vDBSwPZacmgKQBr9PhZzuWtnjH_xJ7ouoObV65Rh2hEEkxSPWY8Cl_TmbuLzHvtR275ccdcwkdXmeRry-meZAjJC1p8uyJollg5W8oOeaUdZsuzqgyLM06sjxdaufASu_h5rsp_Kk0h_UXnYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2ZcX0e4mbuUror1zaGjGEezNKF2F4dZhcZo7uv8nmY7LMeJYLl-KF_0AKwolIzn1KTtTmjF8v0ltmbmPb5wmF94fUCYvKQWeYf5LTWb901XhtHnL1aPLb9TvWxOKihLwJmWykIgY_EVYldL6t7c_YgrOYbr-VLr5WsdfIeowkBK3WutadupItDV5IpAo_WhMtXP0f5gHfpedPdOBtgLH6qCyg5VmD1iANgJRFE281TEc0dZSrYUoj745r8ceelF1xFatmL1E_168SBIoIydkUkMrv14CvowmfqGdMGfTdOC4LDZPGU6L4Azdw31MXYVWtUEx63MdpeuhSKyeIM2MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76760" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=CXsvGiAVYdFrg3GL4dV70IupTuK936yozc1jYDgWvXaSgNR3O9IDI9-0m2PbxRDq8a2_CC-PJprQkJSxfbGJOqDG6PMjzilLaIs8hKrJgAIQKbHIriQZe16lvbQY6n0HstSMfZKfRvZ9pJsuPgnzK_8LT08SbgmDejJI0gLO7IGoegFm3ohV5Y86sA4UgzIaRYZ0n2lRxpPCueK_AB1zZzoTOSrlV2BpWJXRRrhz0rR6UEvsXGHo_FJk2ZUk2uMuTt0lbw10LAYeGz_uxSOjKGcpkdNITdfqVy8IKOUy4AhphwIn-UEJ3GTZb7j8uLOIhDQ1CiolKlAMkzYt6nBPZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=CXsvGiAVYdFrg3GL4dV70IupTuK936yozc1jYDgWvXaSgNR3O9IDI9-0m2PbxRDq8a2_CC-PJprQkJSxfbGJOqDG6PMjzilLaIs8hKrJgAIQKbHIriQZe16lvbQY6n0HstSMfZKfRvZ9pJsuPgnzK_8LT08SbgmDejJI0gLO7IGoegFm3ohV5Y86sA4UgzIaRYZ0n2lRxpPCueK_AB1zZzoTOSrlV2BpWJXRRrhz0rR6UEvsXGHo_FJk2ZUk2uMuTt0lbw10LAYeGz_uxSOjKGcpkdNITdfqVy8IKOUy4AhphwIn-UEJ3GTZb7j8uLOIhDQ1CiolKlAMkzYt6nBPZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=tB27qMDQiohyiiiGVIxxikZLytNak7wcq4qnkQB9Dz986KEhrjzgsmssOIjhqpbW4g7Om79Zn1cLT-dNHnZiOHTSCFEpkIKEucRmhJ-AA8O7DB-eExdQzK2W_6PE3xN5CiJpCtBBiLg0Bgo8HcTtlVDjpAxYfEPG40RlBzwmVMGBe5Ly8M8zRxP75pLGbdMD2o6juE8bLZoZk0mN6OgQISUAJmVuLXmH4U1NqgjeXu1y2NL7dqrBlDr-FPpPMEaxJLNSu6mUafDoVKh8JMUmNfZa9GmBRP1rVj_cNzVZYSRNnRpRi5MIDosquvLrdMAwbIEb1X4pdn_q6gDNZ5kPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=tB27qMDQiohyiiiGVIxxikZLytNak7wcq4qnkQB9Dz986KEhrjzgsmssOIjhqpbW4g7Om79Zn1cLT-dNHnZiOHTSCFEpkIKEucRmhJ-AA8O7DB-eExdQzK2W_6PE3xN5CiJpCtBBiLg0Bgo8HcTtlVDjpAxYfEPG40RlBzwmVMGBe5Ly8M8zRxP75pLGbdMD2o6juE8bLZoZk0mN6OgQISUAJmVuLXmH4U1NqgjeXu1y2NL7dqrBlDr-FPpPMEaxJLNSu6mUafDoVKh8JMUmNfZa9GmBRP1rVj_cNzVZYSRNnRpRi5MIDosquvLrdMAwbIEb1X4pdn_q6gDNZ5kPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlxIvkIzKM0nrzyeDU2HpoNafpz9oQymwKQlQCMEh6jBqAcmwCZGKuU0scLGP1Kf6vtyuwGjpFp3ZK0LTv3QMTuKivDif3xd30y95ZxxaeDT3f9KqBz497AufroC1Am9cr6bA1retGvfQuKp2d7iGR3xT9DrmxMZr0DdpZa-v63sHpQ2UX1CL8SR6cM3ub4emHGLnQsa1ebzb0qIpuIpnDf2V278KiJ2xqHBFIuBSvKexQzHzSnnzM4YF9JhYNGBlgiVEdpFm-xHs-icvQNM_bHPZ_wnfP6-ROWpUPivDJt2NqjYSnNtfhiKLer1tMbQ6sHSMjkeYh5cLJ5He8EZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MI-ZV8uy9jBYZO_1V9LjIvOu8wY-g8T1OYsA__6VtiO9AaPEl9LvbzPsuFQiDLHx0paznRFOLsV0Qjzdd_MTvpMHWzFTIi6NlPfuD412xUCv3HlcH-nGYQNlH_bVsQ8xbAMW8KgsRkiUrxaPF5EEt5tU3upFBjB9tdz1SPZTUONICgCayCL29HBtMkbHthQxpeYam4eitxv2D1ZuyFcO21COAnszj7NUkdz7o3VxQA5mrZWHYu2nfCPQ_d_8AlAn4fAUdOSl0311FvCeC57aXBNktZICtvJg2Ipq9ZzeDlpYBHJoqJ_zf_Z7EQseLSjA-M9HRRWREWSMPtT51XjvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6VjeAVM3WE_U_KjD29Vlo_znQbS1ql3BEVjYPqmp45RT6VXbC-SS7PaGJ3tM3rfkI9bBuHiuEmuL8C7ddQ9g27kUIF1gupY7jIr2Xr0llAEuU0lO-e7W-OmZSSffe60IrnsZH6P80VDm8pO_vPKx5JqAlRqyptvnVLPIICufXC3kEL8PE_ro7_9Ao1_p-sprRUEeu3Ilbq_hnvRxQcN3BP_K6WRXp4nZQGbu8_tOVpX-S1uDumFQxpUXhlbq8cUiVBA5IRQt9Bm11Prk1grmulf1iIA8lcu43f3dDYNk5XGbPdTS6a43-60SPQVcPALw3_DEjOaS13EaQUHrl3d_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_bPeGsfpbE7yzFEmm4yQq2ZIHVM44IJT76GMmt5yRZYBJKmwQZ1qgLpNCu8x1DwvBbsWACUtRJEkkUDOMqCzujgHsIyMhPYH2-qzfw-h7-C0Mvtmql9oA-Op1P5Db_NUJRs0yKKtPWOy-MLlp9N_k8pe2Nreob3Vh_XRpODzgHcZnUY6c7oJCjgabGKMxSOYl_T2mIsHHBfkJ0acpN6WWmuShoUZw7dtaeXE7M6tWuQFnOsib-E2tfw3kIOGi8guUlbspx5JgTlImhWboRXzhJGgYfHD9blAoBatLkWlxcmwhScJf2x2ljAJpwFXd0zpE8HTXxuxH_BG5QvqjsvoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=X1mNL0G6InEfk-gJZ5IL4ZF__RQ8eaItfJ81LK7xL56PxvzVO5Gf9y8mTjycM0HbKa9u4qfbgoGtvGDYGf3MT6Yt9az6hg9NM3SigevP3TC_f6e3BlVZ_1a7PTMiOXC1hdCXhkbm9zk00RjrdbwkJJgWpnzgASBuz8V9k0OYXEGy9_hqXSUahCgxuc0-OuTdJTYbFCJ8Sc-aSSS3Fda9Q5AyvfTYvUW26LZMeofXRLYHNj63CNZ6f5bssbTLfjF0mipu6M8MB--oYu8409QqtO5t-F86lIhBl8RNwlzEyKAQdt4G89LjZHjXzAz9Nk8gpNQGJ1pMTVisMHM1PYQGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=X1mNL0G6InEfk-gJZ5IL4ZF__RQ8eaItfJ81LK7xL56PxvzVO5Gf9y8mTjycM0HbKa9u4qfbgoGtvGDYGf3MT6Yt9az6hg9NM3SigevP3TC_f6e3BlVZ_1a7PTMiOXC1hdCXhkbm9zk00RjrdbwkJJgWpnzgASBuz8V9k0OYXEGy9_hqXSUahCgxuc0-OuTdJTYbFCJ8Sc-aSSS3Fda9Q5AyvfTYvUW26LZMeofXRLYHNj63CNZ6f5bssbTLfjF0mipu6M8MB--oYu8409QqtO5t-F86lIhBl8RNwlzEyKAQdt4G89LjZHjXzAz9Nk8gpNQGJ1pMTVisMHM1PYQGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3W7VnfmBlq9SK5gESjiJhMBcY_PPifPb9Fs_PDx2hZ2diuUX72yudkOj48rtUcPgFpWp0Ks6noNIdqWHa009e9oBG3ugfLvW1Cztn5ZhK1ipRIUCtfQjbkAPh8-pPpQs32QiDfJOfpCUEAKRAviupGt1r48FFb0gM6QOoR6pHIq0wT4VVGQCOCwXP1RU2czTLFlXuZqazwIHd7FG2Y1Lcy6sN-VIO639W4x6BVN0eSZs85kPp7Y3ZJROyA7I7VYhG8tuVfNV9_dmjNjkTv1zAt0EUzvWU1o4jPgGO-laILE5-2kT7wkPXZSi6Sx80Hw2UgmgyAUix0Gq3kWdsgSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=mQw7nJbL3gUxmL0-wDn1Q10_WlBQzyfq5xrQB-7rSyXcsKEA5_RDzf-EQ_vf3pLP5XTyV39ILZk4RYUiuuWxCoBk7o1QxFdC7Bg1t7CUCK1L1OVL_mmkcH495Bgl_3FLpsvBNGmY5Doxu2g9k5NI0dNUJx4kmUJefTeMdMvlX8tlGNTtYiOpetRItVd327uAnLLpbAlZ1X86p1Ye-E39ZLgyignCzmosTeUTMB0JPbenYHab7H9HCdWVkAq8KDYIE7RHBYjbSq37jCVAj9DYbLvqPfG9PVvF_AzhoDspDRDkJtx_n_VMxkHHa4hgwxeAF8SZ1PPIQgs_eY1M9ttKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=mQw7nJbL3gUxmL0-wDn1Q10_WlBQzyfq5xrQB-7rSyXcsKEA5_RDzf-EQ_vf3pLP5XTyV39ILZk4RYUiuuWxCoBk7o1QxFdC7Bg1t7CUCK1L1OVL_mmkcH495Bgl_3FLpsvBNGmY5Doxu2g9k5NI0dNUJx4kmUJefTeMdMvlX8tlGNTtYiOpetRItVd327uAnLLpbAlZ1X86p1Ye-E39ZLgyignCzmosTeUTMB0JPbenYHab7H9HCdWVkAq8KDYIE7RHBYjbSq37jCVAj9DYbLvqPfG9PVvF_AzhoDspDRDkJtx_n_VMxkHHa4hgwxeAF8SZ1PPIQgs_eY1M9ttKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLKNBnjcG3pbmKNWN9Jp2etIT_tFckizSJ3yjEU6neSWtJnMMN9y8lPkqL63o09rmKn7K_dByWCVU3NkK0M8gfCiz5uAIKN4_-3Nkrashi-Q7vxy0q-N71-r6ChfEqTigY1NRqxA_A-bgF4KtM7I8YiaiLcabh-hltl3V6IMlERClhQxrlonfeWxU4d16MbAp5r-6eb03gsXIWTXiN7XjEcnZl60BGRvbg16haO96KKuZXs3JV6giH5BRdsVEcOrQGTBE8P7REPtf20Y_2qNfa8QrhCHY-zCDJif8ygFwdcrWf7LXAm7TvPd5dw0g0mUub_Rd92ZeLLdoYb_MWqbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=ZndlHAddwmNAOQopZsWcKiy2Qtqg-B6r_jBsx6BDce2-B-UzCNBptx14AnrNs9RAdLmlg8T89yHXSfchkaQ5Yg6te-h_QknIKFxUCx-tFutgmIubBaeM0jUWlwk6Wfe12m_bHPNhSmwwxrCV8lomzrtPzjvEvlN9Bqyg5FIB13xDuhk_Fh36FfBtj6I7kazXhzlO62k4gQ4UsYjXEZi-FDeMfrXqxKcDjBWY9aUOay77VD_OTj-H0d8d1y6CNg4ELxAhW5nhR6bLfNCZUB4DYUsXS0ttsl4QJmdVqAXN8bHg_aMvPqRR8CTOE8mQEheeD-YWQe7RpRQ2McXPOOqt_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=ZndlHAddwmNAOQopZsWcKiy2Qtqg-B6r_jBsx6BDce2-B-UzCNBptx14AnrNs9RAdLmlg8T89yHXSfchkaQ5Yg6te-h_QknIKFxUCx-tFutgmIubBaeM0jUWlwk6Wfe12m_bHPNhSmwwxrCV8lomzrtPzjvEvlN9Bqyg5FIB13xDuhk_Fh36FfBtj6I7kazXhzlO62k4gQ4UsYjXEZi-FDeMfrXqxKcDjBWY9aUOay77VD_OTj-H0d8d1y6CNg4ELxAhW5nhR6bLfNCZUB4DYUsXS0ttsl4QJmdVqAXN8bHg_aMvPqRR8CTOE8mQEheeD-YWQe7RpRQ2McXPOOqt_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnPPI_kldMAQg9v6IiBXDO3w-QnD6oRaDZoDdgRFuMFaLwrb2_J-W00E_--MacXTlLyIxhumlsqzSjiNYfNWwLRODxtG48xQpdi-vUbPvwV8smWiKYfQOBGEIeRRm8LZzUCEKY38iVaW5WbhWQML-inc8hIBBvonrGUB7AdgiwcV3mkc6owTFSzzyuGk7Zm_zyDuCx49Ax-zZ3beJh6ASkNZS8TufAB8jAgW2KSbmKBz-DeHvtV8pNv7Cp0IRm2bTVQrU0BAk3Jzmb9CDBFcy-D0P3WcyJZWtsLdCCLYRL25IAtGkSe1XtNLq2oKDYMXLjxuCaya4wLaRKcYepMj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBu2E_48RAfgp-0DskC1pT1GMXLb-cTB3N7lL3Hw8ObO03LSVDqYDcj1MKmCUOmhSgS46vOjDFrlv-8yUV87m5uww4uLUk6ORTuhksp4HbTYZB0hXR4jP47Efa6hncHwDsJ4mN7YZJ_3u289Hd41Gi7sZZZdgGEh7jPtN7TX9Mm5_9qayDYVv9w94oKiSiWg-uil2IV2Mf5bIpGBlAnnncxhesV4nYpwb463SDFSfRFNhzj6B0zQ7NA_HXPUeb-VIdIzi-8zQhP_KC5msCs0NI7lRCt9KokbAFHI7npKN0d2bVWc_XWHqlXAcPC8f_zZ4I9Xr5KhfANruOjvMb8p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Kyi4Kt0sXAgHV2kMjTrFOqACl8YvzNOjPDgjexHAeaVie0P2703Us_hw32ahrpkaEmw96KgbvC-LOldZebJ5Bo6eallE9S_gBe3m0N8svEA9reuGeRONcRmxdrgrwqMYPL0lAgAdZ0Mi8WWQqmXDifMsDSOrXBwv7qkqECvO7Q4-sx2PU_M2VeDfF9xTxmFoKODM_zL8uAPoWbZ-Mki_nk5iVZAXQOIFt3ItibxQH-eG2B7MVKK-UloL9jHaWDetZ6l-YMC9mTvRDRN3-fm8pXfRv9JU8eIAktYwt_CLY6-Y4M-b5UVOajgTtBVKOcLS2NAeH0FbFKSv08HUOIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqrxAds1nK-R-VKflD8Ev4qIrf-MoUx_ZAViYSTfTMd5y7KBDwHBp1e23cspf-826ITOPx14uqES3-AEXk8kea2lDAAvBUWjnyzGdmqb_kUjyiztejThGHIEKmYwBgwhpF4R8_HJiTnwNAJVfUyV1BbaMbSv8Qgc-sBFzyQOruPVZcibKPisBEusxcvaimrAb3grQmUQ9SzXbEqGaAwdIjcORDv126WKDUt-TPIpLuSOMqdf7NdS8pgVhg-EWLDq9y_gFriZv4Z8mfq9CxOT9Aa2KgGvsqF5A1HNB_OYAwGKU66fbWEpO9YmhM_V4TTpjsruFRNyTjXMJNNTPIQzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGOq3mEXsJ2MbiNFpXKRszjgD1Xva23ZmlLZWzagViQceGQt87fLbH1RuBfXHeafcsiVU5pMZk5YYe7u9folMr9lbjTTJqskRrYg1_cPT_K0E4qrUBXX_ef9h9PZIOWuzhWZgUfX7b3w3GQaMIJRLjjw0ZY5u1qs-Fw_9GjtzpWhr2RrW0yK5hZFod2Hu6t2q3XUVydieVn09wlmlVWaptlNs4yg15tZ11VUGm1mt6GqgmsEUKTjEKoyqnaHwSqSKnUfHz1bZIP7umF6wFATDgV0Ec1BnyThadAWqbKsUC5c7Fj_aBNpWEyLiC0GCVjLqy-s1uZ1QEELpRgiWtwd2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CSvQBCr-Q9czyBPcin6pLcQm_CW4CP9YNr0if8LDFvaLXEOnukk5vLxLnY2kPcTUZXiNd2MF5O-mQ4kZaoNCbViwoupiX8TnZbj0VBQE02x29rPp8IGnJ7c3rapuJo7QY78ujMjD-C7tAuZQ4EfDMU07OyhjRdoROpCxBnYFkPL-07ffDMjrEpPJ6Jh572x023Xl2oKLrL0bgUbxQkUrJTFSCJ6aLgCr93B0V4UcnCF6loq8EywCRO62wZJGTnjN5dDQfU_qxyEmNFZA1bp1yfuhbyhrzN293B_urEFLRrZyvyW6rVwiNmIouStKfr0zAvDrbHYr8rfSC0hmVjIHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmWjIOCj4WideyN-HR8xmX-gyj4mvk5whIdEE5xdbJlbuW5Yl5MqU7HEumYD2lmMkJAra1R2FitfexxMA_xO5_KlAd5zb8wWXuNG5Bdrh041G_YsS16sd-pQ70a6Ye7SMYGULcSDJiGbT6r27bGofFiisIvsJyDnrKoQ4WPnn1lZYVD-W9g2lf29wm3yTkvpfDB1UdSfFDx5DjKMSpBAWXpuuzDCZf6nW1mV4zrhaxZRCRLYXOxqyHn9avtU8BUJRuka8PLQPwr6-dLz_cKEbseCPGrv5u5QBbdsBHNfZ8ktFLgz9VS7N0baINmHR7-zRmqI9oHYrtnGoe93YNUGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76718" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIpYNo6kI21A-LkyquP0tbKlmIbxSS-cr0GHZbeJB-y5W-4HdGr0b5jK1fM1DdF7Bnhjgx859GVI3mJ2IcjiY_3jXbvXRjz3B_tDxiOjCQbm5J4JUPEWJsWktrBgFXHmI2kipG94osJYVhthPmT0KU5NF2BNBPWliJxLdUDsgAvNHtu1EMBedAc3nedy74UGDg5CYc2fpNFerF_9o6-gkoBR1f6iNuiDSLvNYSWq-ovz3EHQJiXvri3WIniq0RXRTwQlSIR3X4pt9xyKtz7n-xB9J89RakGS9b_OSbpuwJJMXtPgLpc5Rh2OI7xyzkpEV3QZBWOa_418fFHierRfEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76717" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVhKFjpvt__C5rjl2cr0XXEJy2qBn0TMBKkFfLR_IAlv_YzE00S6RLtKjCHXxhhtCkAslQGP0MC1PpX0AlNAKFaO8jU9KNX6Sf0lVKtik1WIGbBubQIRjE9HjrAVnkVEYl8vxqOBPIyWCczPD-kr-cqQPL9j6eOh27sZlTezW2YYP8E5Ruy-oZDadGWP7D8LXmSKin7V0t0MFmeyf7eudNqM388YJCX-SbDj0mprzmdF11zXTFqWrKCS0AI6Ru3bdjAtMSyhxo5C9Y7aPJN1YjTNbI2qhbLLSn8i-M00NsOfa2zS8y788QMFMpkQaI5ptnidKiwmHip08HozR9xL6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZSjWFZjZzMVmmNI0Pn1HzTEilyxQISqbNHG9ZEnPc8c357HfxIJ6by2Z56MAZ1MQI3Dh0gGtxSgiJClTA4QS66QYPDhV9mMsthGF4fb6pSNB_Uj9JBkTekk5gFMnG-XifXD1ue4ncFLIi5r2tu9BwOPTLMtWT7Z_jLyEN5gsPi7qvVWk02fMEm8HZRevz3V-c8KNTSGC57AocHYhmPgfiSWob1xlZnVg25oDZwry_3nsAqCthaPO2T1-gJvA1E_45DxUFl3_F9cCPNvz9F4SAk_VBLPTjlKfnSJz5VelQh_tBlADe20Tk6ZMkxamahwPCMPVZ_6cQ9APQ3oOSv_rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oikezl8f0GX117UgCfR2VNSmXgn_KcOF-aiVHdKY_yV7x39njpunKYSi153q7ZYp-nJa5xy33ozuFp2qX4eZ5l_23y0JFus5OIxsuT1LXtKoclryAk1vHi7-RokB7VfM2KhGfi_oAd_XpUbV0cdbJu0E3uqufn0kqnE4fm98QEIU15VxV6b7YYk0LZnf2Gni7dYV-yNTW4ZWAVmiIHJZfpr_7Zg9mrk1n67z_aXistCYZSfNkOXIRjaOOyZ1Bi5Tspkx3xNVNgQ2QqSZPPn46WYwR3tIu34asxl8jzjAS67M3l3nog0UjFFvh_BHVMije6DoEnw4_DQ29xeXQR_zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhgNHD5y2SOieKt_L3Vytb0VWzrhwHIR1aANx01KbkLf7F5gvxyQzG9Xx2Ud5vEV7cuuzUnBKZPJ2BYK6ixPMBcNKXrz5TC6tilywh6hoiCHCR3WZ0RZOe_9PLPYeHaCS7-HyoBXhJR1ZAn7001DRk6KrlrWGGVCEDlHpXS3JAA28Gioq1IAFMOkp1TiFlwyQwvcdYetmf613DMN4ERxDIBsT7IH7cbT_mK-gpUDO-fa6hW2SiBcT4XYOtaf2IKYFC9UTrj02ng3EjLUYwLjYNmWLTsPjeXpyeC7KiAzg4boU5DJfLsZf_ac_dE0cO_rohopNQWAzTWlWkpI4fYFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcYqJRUPYUdvufOjQCL3NT0t6GOEd9uSUwpgwRUnjUXw1EUkPx1TtFQgRnvwUWfOCpEQjBkUSLMeQCHAJU4F3dZTMUuNpWjzWZUvPgRrr1Y55khw0BrLoat0YLwDr_1pqn2ap50_CnvkKoBgFqg0tVSwWFUDZz0RmY2ROdHIa0VLEFAT7QvW6h04pAggVPRyK2TzKZ5IPQgRT0JABioot6IVm59oJXQieTN0AMSQ7XMXTbq8INp83sfP2CNhJ7OD_t4uYbftaXDXzN1lw_0uKbmmp_of39ib0EDcrQ-KSHrK4BqnyTqRgQl1y6yGW5zxot02p6rxMnhtc2moxQcLeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti_2gFvyThE-eG425j3NzlesidQRpOZjR1g7YQVSvbo0DilBMoO7ZfNBkTcaY-FaEctkHEop3PoZfG1xtWi_dVf13Tze6z-qB9K3lE2SB9JQGQO0AlGGOuEbFqH1vue03wg4_0YhVIpRu8sRBVVovWoxo22sQhdWpiIjYOZzwjP8MKUvbXXdowyd5iU9sxU8smpXTH2ZO9A5ojko7DNWrLel-FmjLGa17tVfoqQ-XxOTQyP-gPEgMsjuHubA9d2wcC7ntZULRDNgs506yUgvMQVlvMzmcBnNf5mUOBeYD4Uno3ym9MMxngjRb7Srle2sGvqAgZ8X9o6PDbky6URqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
