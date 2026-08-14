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
<img src="https://cdn4.telesco.pe/file/k1Ysu6uzzdxB7ceUNoYWSFRoy-4nQhNg0kuMT4bYML-AIFchJUsO68ub7WaOEiUO2Nyf0OIzjgDJisezcvvPVY0cdf_zUH6nJ2BYCu8KsY7_Ay4fjPY2NlUgeZmDXN52mk3V5TYBr8Q9Vt8tp3dVK8mDFOSODR3A_H2Jqo6o6UGdFIR3CeGGnzVKLL6UyFR-xIII1coKtie7I66cjPT7EAvIfDj7E1giZtyE0fkm7oYzPfQYs7lsQNh9fCr_81J5TaaMZ26PkEOQ4pipV19Usro1w7btI5x96CL0N3ysJrb4Ys768g5USbBaeB_70I1rE0zRFv7USR4RYlN158P_iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 07:03:48</div>
<hr>

<div class="tg-post" id="msg-681023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlfDwI044nF45pLQPb3TuFB3KbnXJ0cDFu8BmstXWks1aWWOpSSt6gtrivsZEf9idT4q8eFxzzbruOga81VNNpKYc9xEwiHCIWlVm9__eiVbUvXtquyXPOdtN_EtdVYnxXaq-7-bA9BpwATSLHsQJz-N_YaTHT02vFRu9mi0hl2nPvTX61a1RQMAgjjTR6wTdpzEUNf6GB9DdpqGfE1c7C2Vv6a1DV58RQTdbztmhLnH-MHGz2pGeiQMUBaHnMofdl_ysaNll0mbwOygOHF_YpsGgqnBAN03JTq_s472UoLPzK2adSDoWdheA_zuTw3mUhogCYGzksDeuPQN3tschA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/681023" target="_blank">📅 05:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
عربستان: ۱۳ کشور به طور رسمی به ائتلاف دفاعی دریایی پیوستند
🔹
وزارت دفاع عربستان در بیانیه‌ای از پیوستن رسمی ۱۳ کشور به ائتلاف دفاعی دریایی خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/681022" target="_blank">📅 04:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
‏منابع امنیتی عراق: چند فروند پهپاد در اربیل رهگیری و منهدم شده‌اند/ بقایای این پهپادها در یک مجتمع مسکونی در نزدیکی فرودگاه اربیل سقوط کرد که تلفات یا جراحاتی به همراه نداشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/681021" target="_blank">📅 04:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
انفجار‌های شدید در اربیل
🔹
در پی حملات پهپادی به نقاطی در اربیل، سامانه‌های پدافند هوایی فعال شده و همزمان منابع عربی از اصابت چند پهپاد به اهدافی در این شهر خبر می‌دهند.
🔹
تا این لحظه به طور دقیق اهداف این حملات مشخص نیست و برخی منابع هدف قرار دادن تروریست‌های…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681020" target="_blank">📅 04:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شدید پهپادهای انتحاری به مواضع تروریست‌های تجزیه‌طلب در اربیل
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/681018" target="_blank">📅 03:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رهبر دموکرات‌ها در سنای آمریکا: پیت هگزت باید برکنار شود
🔹
در پی وخامت حال خدمه ناو آبراهام لینکلن و انتشار گزارش‌هایی از فروپاشی روانی آن‌ها و تلاش برای خودکشی، چاک شومر رهبر اقلیت‌های دموکرات در سنای آمریکا به شدت به پیت هگزت وزیر جنگ دولت ترامپ حمله کرد و گفت: او باید فورا برکنار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/681017" target="_blank">📅 03:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZFvryvPsVOAwiLK8GecUCWDhbegvawOUqM15iUVs9PcxSWEnM51vBHA-ONuXWErwgii3Z1aRMfqwiXOu3bikXTIa1n0NIN5FBE0XYo00ErQFSBb1JnDvbDzg_AgbkXpSjiipIBWmpNQxmuVPlYZ6b7G9jesnSJfxSxZ8Z5MwGC_tcWQQl2esk2GNfWeCQSM--xE0vsBKlbus-YJVv6QRQXBFf_3-9_wgjqmQFKFf2TFVLhbFv5qKb0xnN49TUoLWQBkxYp6QsNUzPPIYpzERMsQUCXkRtMc330BZqM5UKViOKFXl9GPKFR20R8fTvhASFJTD1XL3p6rQsYfo-IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت بیش از ۱.۳ میلیارد دلاری ایران به پهپادهای آمریکا
واشنگتن پست:
🔹
ایالات متحده حداقل ۴۵ پهپاد ام‌کیو-۹ ریپر - حدود ۲۵ درصد از ناوگان خود - را در طول جنگ با ایران از دست داده است که خسارت‌های آن بیش از ۱.۳ میلیارد دلار بوده است.
🔹
ام‌کیو-۹ یکی از مهم‌ترین پهپادهای شناسایی و تهاجمی ارتش آمریکاست و هر فروند آن، بسته به تجهیزات و تسلیحات، بین ۳۰ تا ۵۰ میلیون دلار ارزش دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/681016" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35e3c637f.mp4?token=WKy1ddjM_OBzMAZD_uAfWgHO_yHtanPeUlwivPB4tzYO72EZDKOhDGZX0gd0FggGzOCki7A8qIZIw0aQGlvbJrN-EAnIe9-F_1KSpjXDKdOFvoE7Zoy9oClhx7jxvwBDC0rDHnaabNx6MVoKE4gRBkN04v_x1GQ02YZjw9mGdyEW9umzV_ayM79SE7E9oK_RRGAmdI6ZXaOah6OvLONMq2J79Y_cJgPctdXiFaZ_dh23G5mcmpVSnBudPkeqBuIl-SzZhKpa6JdFYK9XivuWO_77VNH3B2gobectFKAXPCbgNe14PU2gRhSPHM08uxRVcNPLjrk8_v6HFHXd1kq9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35e3c637f.mp4?token=WKy1ddjM_OBzMAZD_uAfWgHO_yHtanPeUlwivPB4tzYO72EZDKOhDGZX0gd0FggGzOCki7A8qIZIw0aQGlvbJrN-EAnIe9-F_1KSpjXDKdOFvoE7Zoy9oClhx7jxvwBDC0rDHnaabNx6MVoKE4gRBkN04v_x1GQ02YZjw9mGdyEW9umzV_ayM79SE7E9oK_RRGAmdI6ZXaOah6OvLONMq2J79Y_cJgPctdXiFaZ_dh23G5mcmpVSnBudPkeqBuIl-SzZhKpa6JdFYK9XivuWO_77VNH3B2gobectFKAXPCbgNe14PU2gRhSPHM08uxRVcNPLjrk8_v6HFHXd1kq9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شدید پهپادهای انتحاری به مواضع تروریست‌های تجزیه‌طلب در اربیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/681015" target="_blank">📅 02:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترامپ روی واردات پهپاد تعرفه گمرکی وضع کرد
🔹
برای پهپادهایی با اندازه خاص یا دارای قابلیت‌های ویژه‌ای که اهمیت بالایی برای امنیت ملی دارند، ۱۰۰ درصد تعرفه بر اساس ارزش کالا وضع می‌شود و  برای پهپادهای کوچک‌تر، تعرفه ۲۵ درصدی در نظر گرفته شده است.
🔹
علت این تصمیم وابستگی «بیش از حد» این کشور به تامین‌کنندگان خارجی پهپاد است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681013" target="_blank">📅 01:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فرمانده سنتکام با محمد بن سلمان دیدار کرد
🔹
خبرگزاری رسمی عربستان (واس)، از دیدار فرمانده ستاد تروریستی سنتکام با ولی‌عهد سعودی خبر داد
🔹
به نوشته خبرگزاری واس، دو طرف درباره شماری از موضوعات مرتبط با همکاری‌های دفاعی میان عربستان و آمریکا و همچنین تحولات منطقه‌ای گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/681012" target="_blank">📅 01:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
توپخانه رژیم صهیونیستی وادی زبقین را در منطقه صور در جنوب لبنان هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/681011" target="_blank">📅 01:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
زلزلۀ ۴.۵ ریشتری در حسینیۀ اندیمشک
🔹
ساعت ۰۰:۵۳ بامداد، زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر حوالی حسینیه و اندیمشک در استان خوزستان را لرزاند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681010" target="_blank">📅 01:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مقام لبنانی: با فهرست نهایی کشورها برای راستی‌آزمایی خلع سلاح حزب‌الله موافقت نکرده‌ایم
🔹
یک مقام لبنانی در گفت‌وگو با المانیتور گزارش خبرگزاری رویترز مبنی بر توافق بیروت با اسرائیل درباره فهرست نهایی کشورهایی که می‌توانند برای راستی‌آزمایی خلع سلاح گروه شبه‌نظامی حزب‌الله نیرو به لبنان اعزام کنند را تکذیب کرد و گفت بیروت همچنان در حال پیگیری این موضوع با واشنگتن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681009" target="_blank">📅 01:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سنتکام گزارش‌ها درباره تلاش کوپر برای حمله به ایران را تکذیب کرد
خبرنگار روزنامه جروزالم پست:
🔹
تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، به من گفت گه گزارش‌ها درباره اینکه براد کوپر (فرمانده سنتکام) در جریان سفرش به اسرائیل گفته است که برای ازسرگیری حملات علیه ایران تلاش می‌کند، کاملاً ساختگی هستند و صحت ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681008" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa556d2c4.mp4?token=KNdh3C1IDcaFZShip8SyVvknxHBRi9__ksvRjvJNfOE6N0YsriJjVUkpqHZcd98SpdRzaLsxaPxaaz5pInf8Q85A-JvY7a2PUn0SHyUErBHYER2Z_Y1gkuMipZ9x-Zy1iWJitUiAMNSsxiDcVwFO1AZlIpvodxmPIaeNRjkVAd0bSIm6bk0aaWfFDaY18rADTS4i91JgZZTXZQQWGR3Sq5vvJ8w2CNdJvmAOsgR1JuRmbLO2Ye6GdSFqcLE_JpO4Pa1UVRxnczCQl1mj9eEKEYxlhOPLG6f0US-Q_GADhH7WZahYvF5puflMUOHbjUPBEyClhGDz69VLm7hBB3_3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa556d2c4.mp4?token=KNdh3C1IDcaFZShip8SyVvknxHBRi9__ksvRjvJNfOE6N0YsriJjVUkpqHZcd98SpdRzaLsxaPxaaz5pInf8Q85A-JvY7a2PUn0SHyUErBHYER2Z_Y1gkuMipZ9x-Zy1iWJitUiAMNSsxiDcVwFO1AZlIpvodxmPIaeNRjkVAd0bSIm6bk0aaWfFDaY18rADTS4i91JgZZTXZQQWGR3Sq5vvJ8w2CNdJvmAOsgR1JuRmbLO2Ye6GdSFqcLE_JpO4Pa1UVRxnczCQl1mj9eEKEYxlhOPLG6f0US-Q_GADhH7WZahYvF5puflMUOHbjUPBEyClhGDz69VLm7hBB3_3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ونس: قیمت نفت امروز نسبت به روزهای ابتدایی درگیری، به طور قابل توجهی کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/681007" target="_blank">📅 00:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صدای انفجار در شهر مارب
🔹
منابع یمنی از شنیده شدن صدای انفجار در شهر مأرب خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/681006" target="_blank">📅 00:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyVgcvEgS5EREpz-RrWuGq6DVQBuWb3Ka7K8pMK9F3SD5hyckxEUWPm_bjptvxwWNXFyEJVCMU5LY-sFwgQy3YMLRfE9V790TA-C8RqIE06CJsSBUzk187zeRjWgdHNAZBsAncXIOC-JSywKP4gvBaGV4-QuGWAD6ob3eM0bhH21rUTCeEMB7btSER-Hjhkkqkbrwdv6HjlF5QeESaD87aayrCDp8ewxLuifYtYvyZlA59ifzwEZbHwVAHNfneIBDAEn92ohgzbu1L62rTpSIJF2EHHNJU7ZdzIrEooTM6BQTPeHYWKPeCSG7B8c39MKSqxBwbxZIkob8w7W8eYIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxiwLjOabwAbQIbMXSfmenaNWKpK-IWUoUcTDrIBf3FY0Eq3v7UXY9GeS7veVflwGZVeC-GK_c0givts66_2vkaff62qZTRkY3o3SSlusOt1dHeMdwV1Fx8_0f2xbbrrLyVw_x4VVpwpl6ZAyFYdsh1R4Uhct_HG2Fa_zsmne18Piv-lMw4uCt1sKMbxJoCkaOyNxEyj7b5iz5_NEWROstOUArYIo004SHvDdPU_NFUBI_VuTol-89bcvLtEQgJhljkfGOiW9uVDX_tDLLfI_Hx0Vy91OzmMAyTLRTHpM0LiAMPL1a8PvLr5SMt9VbOq55spzH_f5HeWAEnNc6Y9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovnLx_RElkOB_b1BqoFXtWFUP_UWio90KEdiJA7XUTXR4Z05SgcAeGmfT7b6lmZ3geZ8NxdXFl0ndwaD8Md05DwbGpr4JJA0rU8D2ahnsY25iyZb45e0YRw0RNNWGPXSpKE0lEaWTw3KowVhvLcgOgJ6SCvPdkAaImLinCg41BOWG1-Y2_Qi49yKnKMRoTrIK6DRWdh_Berkx7bYklGtCJcyyV1fGeEOgDnTeIFXY9f3-I0VT0r4dszstdcPUjb8axiIAIm6WeB11K54gDqf-e5wH_ajjcDoJwyynRQLkmkMCBdyIAj4xVI_4PokXCCrNNAqoEDawqXOEUHAII7qqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCyG1o5H6rs4uy7rS8tJ3eS5S-yjVWQY8wfajnJjjB_aSh4raQ2T7DNjWyqq8B2DWyk5hjPSVieh6HlRiA1e7dgT_aXMbe5YEa1xKIBuLXZmpYK_DIE-1eX0tVaTZ09lLrMOopGF1AFVSjcEbX6yU0JJC8I--5aqoZUyM9Ki7G6cMqegLq8GvbSdN5Bx_9Y7F2GbaOOpfvOzfOtbNkg26ZT-0XGeuaMiQS7cUpyrKTecgw645Y6LrSdMrQbWyJJHfeIjmTiiiwsgrZ2MzcWSYhEwTtd8yDgVBRZ3d-52NprJmpZaHd103Wgm55F1wyEDxGI0R6TA0FML3VVsN28DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf3YXo9NHoOctFqJph2fT19-Igu-15wPQeSSaPu1Zx510HwuRclATNe_fwkDPNpDDVyEAALl7S76w0sYlF8aPsyqZsYL4Rp2iaKNjmRWIoRhKpPhBSSIlIMX43-5igP4Zu7_wQG4cjq6wAmOpc7n_xgKvPXcURfsvQIh1xq1lMoJz_gEPCkSe55n4HCzpSLYva7du_roXv627f5yWHjy7kFEdRh7Gzo-XmsPDgaZG11b4DW0Rj6N784Up-j3IGDjNh3r1WYmNhrZtW0BET2Hyfcxic9Ljx8QyxTuaCExqU-fCNJea2BRzKGzzmV4updZqYY_GfBoP_NO2Ks9-i7QNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLUVRQCaXZPS5LRudk-j2v3_nt456wx3G7rnBJFhClVCSWIC4OXOLE4XbbWm15PvuvtRWV0nQfUyGyaEtGXgRCnQLMT8TnTLgiuE50B7K4b4DXbPsbOqZiRgk7emACR06g2SS7L3VhRSooumgxeEYZDOirxfcVQ7wkAFL4L_3zxDYw1109Iaif2IWT3_B__hSjCWNWW9ty7_ZzczPceWWcgY7y53a7XXXgvwePnvT-TwhXzYx36bBU_IsT338i7NCNRivYHkUpEUsBNg4PhU5Lvg4FmGSXUTGILjd_WG_16CoTOzh9aAJ6OTNhHaeU2PWAOutiD4t6F6EbjoygQKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_HlfjTklYLFFz2Ljb2sYnN39etnPsNtMMOiU8sDeGnyfCNYVJ81gjPnLBiy9V_a5SLcd4vvJQyupZsr9a1OaPnq4u-EpRzGAuoIgyBdzzdVgahqMe6nSTUu3EFimAdZlYHgTOLdjNY6yQJOUmwUdeeu708pFp3_D2isEEdG-etTbzWeovmHWII065B4PHaXGTNGKyee4SuT26P4cfKhZ0SANAKpQRvZl4dHvDXHHXgdGgqFirEF56UDEqaObfWwVQUexkNJg_dx5YB38wTiZYZ6hw7v-8HkBH-zGfin457j5DvfdnoKyoSkV9ianwVWOgLtAYqW52sBCwf0jxFWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFNvR9TcRUk77KyTf4bYI2FiW1B3vHZarBxxknYZFQJB_ejnQFodlHnOJC762Js1HPwzl1OFe4FSw3gb5VGFvN8qVVjDmXkYcbszadLCsA4mMq8q4F8pmXFHijLRlqgiwRB3fZ1iuFrG5Z5i9fsXJHVzkL8CUsLiT3vh1qGoUyoYkexkCbG5Hd8888wcbF3UePYBAVlWBgjfEK7OHfMziiZ4uaskJEZVbcnXP4EXsL05ExBic_PqKK1889JhaKZE1OoLFBS0Tqmn2rH6FjMJFhg2k-lnEQn5wgGG0G3BxxGcgDih8mC9mWD5NKKGpXxFIGx6sQMve3CU7QGrCNDoaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ردپای شهاب‌ها بر آسمان ایران
🔹
بارش شهابی برساوشی یکی از تماشایی‌ترین پدیده‌های آسمانی سال است؛ رویدادی که در شرایط مناسب، ده‌ها شهاب را در هر ساعت به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/680998" target="_blank">📅 00:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
کنگره از ترامپ بابت شرایط بحرانی در ناو لینلکن توضیح خواست
🔹
قانون‌گذاران حزب دموکرات آمریکا از وزارت جنگ این کشور خواسته‌اند درباره شرایط داخل ناو هواپیمابر «یواس‌اس آبراهام لینکلن» توضیح دهد.
🔹
این درخواست پس از انتشار گزارش‌های متعددی مطرح می‌شود که نشان می‌دهد فشار ناشی از ماموریتِ طولانی‌مدت، سلامت روانی حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو را به‌شدت تحت تأثیر قرار داده و باعث اقدام به خودکشی بعضی از آنها شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680997" target="_blank">📅 00:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شرکت ادنوک امارات: دو فروند از کشتی‌های متعلق به شرکت هنگام عبور از تنگه هرمز مورد حمله قرار گرفته‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680996" target="_blank">📅 00:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrEE09NlkNADrnKT-OKySAssUE_IGNyBQt88O_nnas9eH-AIf8V99yjn4v6N8xh-oCoHWN-YqCC-QwsqQgSjmttSjQfkZ4z6yVDnJH1KVw3IKJuCwgCurCLQrda7jK9vkV3kSfaQ7T8Y6wmxXJ4anQmjdBN-s3MumWPv2QggTx39tLnES8vrPv94O1giwZdXpIyCTf9c3N7_0w4oxTgmuQDDLvo8BDbV2BgCA8u-Dz6C-hXUe3r9YvSPB0NPh9Xxy-74wwvNbHYw1JYZM7Nk3i5N3zq9T6hR7Mcp0gDyAjAx64UCP8luEi1oMwuuoQjPCV6tAMk74Wm2W2NVUuV3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندازه مکانی که ترامپ در جریان عملیات «تاکو» در آن مخفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/680995" target="_blank">📅 00:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgSnvnmWbsmkjQ3HKj_6wn5UtfAY9iZdiO7q-jlyEnPczVwiG2r8ko5KLchwOkIqeDYAl2T8OTj_4wVsXJzqP3rhhkMfwFdlJF9tLYWXwHmkuK09hPF5ZadOyS4cQ8cCTi5wqpDJUF9i9P3iT2BIXb0dbRtl3a1Pg5yu7L5QgtVxrhz0eiEADJueB3lSsqpTYQ0opki85RNY7RqzXMXFnfyfEBtRI_S4rLxWfYFPLVuIyvT0M0dYqYTLbmqQUed2vREimdtKjxtp4F4oCn-H-K0DrTIWhDbof4NEPyVOZTPqYTYtfkU7KJDMN90wjO4r6Vge-N_ryyLy4-C5O6Sciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: آلودگی نفتی سواحل جزیره قشم، ناشی از آثار تجاوز نظامی خارجی در منطقه است، این قبیل خسارات وارده بر محیط زیست سواحل ایرانی خلیج فارس، ضرورت تعریف و اعمال سازوکار مدیریت تنگه هرمز توسط ایران به عنوان کشور ساحلی را بیش از پیش، برجسته می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680994" target="_blank">📅 00:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSmW2TIMczNx5pCJfg8x62PHnc2oE1tQr-vQoo6JsR8a9M8C3WJ75J_6NHvIMAvWNM77fcRwdouHhrH9vg1RTnAxth62uREdVR0z_NYEfx_ElOwX2VvrakjhBn-kIBzD_df6IgEIqbi4CxakT47MEYBpsAt0uNX_fHcV_oZaQZgoJx2Hu-KOIVxiCRKut-XgoY001rxnLB0s77vjcihUiG31rOVKoDPnnbqfJRIZF3fRKW7L4XzobLo4EzGxuCn-VoEe_diJVgmlOUNLpQC2KPaueIdZZMIr7e6brNabQ7sW2O1kX51G4MkbklBTIqjX91_D3O2qxyOD1HsU6VTS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط ملوان آمریکایی از ناو «آبراهام لینکلن» در دریای آزاد
🔹
شبکه CBS گزارش داد یکی از ملوانان بال‌هوایی ناو هواپیمابر آمریکایی «یو‌اس‌اس لینکلن» اوایل ماه اوت در دریا سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/680993" target="_blank">📅 00:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnDfnJG53avTYNySzCCr8z56yA4ahGnlI-HOe-VCIib8h1FWyiAThXdn-KMp9XM66HgfnHmMVF3y3B4hVSTSoJswDPijywizM5zIc5o2Au2DAEPnCMi4nBj0WmhXmWOXwLAGaA0GeWriXTNI4w8rzP3rOJtpLW2kvQJCsih50bzj20XBCRYglxvj1DTdjlzrApxbA-d1URhcC96edO-Uk8IqZwkR1V5EGEjFyw1U2p4tmhqaHlFr44-OQNc2Shg_bUWXh_4tOwjkVwYPOfmpEZLegxqBvhGObgvnuA0TdSn_oG1SVE2wbND56aSmIng5bmTva_h__A9w9yHHjc7TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsWRivLHgY9gfcFo3qRA3MyN9xSo45o_T_7Za4Lp6sVqM17RkEtRLsz4cBDxG7ylo6xIRZP8x6OxUI6e7EY_ckalN0fcsyZPAs-UuEsAQ2tNhCwZCOFghRcrzTLUaKJ198XivaXc8z9W_0i-GvU6bT28sMKh1sU-ewVoecgGg-t4_9M5dQLDAqZTohd9vKGBoDFrPT5HP1w2x6rvLZnnmW5u9StPNMqSmGuJ1Ytby3JLCchvbOa7j5Drhp5BkRbyqmqzHkxEDE5FsuG4o-efgAGuM80xPpP0CduPh2Cx-nQpcryKETvs7_JkjKjEvJ6iu5i9fEC_rC5-IBVGA9ICmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازسازی فرار ترامپ با ماشین حمل غذا
🔹
نحوه فرار ترامپ با ماشین حمل آشغال غذا سوژه کاربران فضای مجازی و رسانه‌های سراسر جهان شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680991" target="_blank">📅 00:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای جی دی ونس: ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند  معاون ترامپ مدعی شد:
🔹
من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت.
🔹
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/680988" target="_blank">📅 00:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX9ujDk-nrr45d8y_YCaWZvjqtzKXkoiDaJz_fzs6KF4oDsvFgzVLys8EqqoVM7TGgqzMupgKi6gP_a7L8relktvt9_GsjZbDD_ZsNuOhnOpqniyzkJwYbPDhH-y6K5xrou-dWOKkAnp4ND1nUTGB7iOvaWldlWIu5z8b2mawW7BnNni9FkAvQMGm0kfp9pDlHw6enjNS99zZklCBPyChLL7CGGD1gKg5KCDi7uFlt6r04-0NDsbJDya3mhACiiRD5LGhbkySJsFsFmO7yPnIdb9TuTG_yOgnrtsOUJsO0oydbtLxOKaBFa4DSYlxuCovQgueDyynpl8KnSr9jeVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از شگفت‌انگیزترین کشفیات زیست شناسی اخیر
🔹
اسم این موجود Bubble Snail در آب‌های گرم اقیانوس هند و غرب اقیانوس آرام بیشتر روز روی شن‌ها راه می‌رود و کرم شکار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680987" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2MISRHv51ggu_M1e7J7X8dHlu3W1_8a6vMArRqzp3Eq2AgM_FKaLeBLZxUzY6ZzpIRYyrDo_KoP1spQZqWXW8mSuJ8Oz3pFvIV4Tcc3UWzjT20TiyqbGd42bIiEubqCvmfhwS4X6WpzCUOjKVQ-nEgrUKsksCTvRgyk8u5fx2z5soeW4uTQE-4FcBSULhlIKoUvPZReQ5OzZRFfzycbsivOdj8F3senx-FbtzbSxh_vRpv2I-VPYEUQhZLS1HwXboIH387vLE0fR5o5_O_q-pb_TCFqtqd-eVL3Z2Rv_R6ItA-okw8YfxE3YTnEHCdxiX3hxd6J4rULSnFOd1Y1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایده های خوشمزه و جالب با هندوانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680986" target="_blank">📅 00:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
شرکت ادنوک امارات: دو فروند از کشتی‌های متعلق به شرکت هنگام عبور از تنگه هرمز مورد حمله قرار گرفته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/680985" target="_blank">📅 00:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f939645d.mp4?token=i4C7bDoXiWq-ZkswcFMQfhuwub5y5pVRU7P0pwY9QrnJAlojasm3HZ7dtxq2gLGKNuUWrcLbIsneyETklHFMqBC9VM-FDTlxL5HELuxVW_R9wIPjaBCY3jDIZeujh5o1SIuM1n4kRKrW3VmmN_d8D26ymB4hQQH0b0y0IuiFY7pNIjq2VXGO73rNfSOoS_L0t0yL7Re_Fi5Qcoe5mR_pPZ8DwGe8dwlbs8gYWSRWzvU4-ZSbUrdB0UpH-O2ymyrB0tLpKT1_byPJWSpb3WRRjPHh_xL3w95zMRd7jWxeyL4h2Hng2StGqnuYgD97tz0_p4LOLRxsdq9051UXxE5LYhYGBCypjVode3lceeZqo9WiCNR1LiZKdGZaVtVtUhTzyi24anIt_Mg5Vuoogzmv5lA1CA441JCQOwD5wDmQjzlcwhSN8eg70qyCUiz1wGUFUL2-BcMYoIZOWT9fhTuvLZPx6mcuSH_foelWTwqSc3FOufBVslHoq_dO7vgkEAxQIGkpVAI6dj3aV9Au_oJ2mxz8DqHFc-ovI2RVCXfUy50uSxeVEyyXq7Tt400QsedSVZeFdmCN54nl0-JOuhVip9jCB2hfI2ov0ZxCvDio-R4CkQKAo7nolCELv3a_dOPax5VW5E0p1e2Z9XI1mvSBZRh6oBH0PrZWAaTv6jpJXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f939645d.mp4?token=i4C7bDoXiWq-ZkswcFMQfhuwub5y5pVRU7P0pwY9QrnJAlojasm3HZ7dtxq2gLGKNuUWrcLbIsneyETklHFMqBC9VM-FDTlxL5HELuxVW_R9wIPjaBCY3jDIZeujh5o1SIuM1n4kRKrW3VmmN_d8D26ymB4hQQH0b0y0IuiFY7pNIjq2VXGO73rNfSOoS_L0t0yL7Re_Fi5Qcoe5mR_pPZ8DwGe8dwlbs8gYWSRWzvU4-ZSbUrdB0UpH-O2ymyrB0tLpKT1_byPJWSpb3WRRjPHh_xL3w95zMRd7jWxeyL4h2Hng2StGqnuYgD97tz0_p4LOLRxsdq9051UXxE5LYhYGBCypjVode3lceeZqo9WiCNR1LiZKdGZaVtVtUhTzyi24anIt_Mg5Vuoogzmv5lA1CA441JCQOwD5wDmQjzlcwhSN8eg70qyCUiz1wGUFUL2-BcMYoIZOWT9fhTuvLZPx6mcuSH_foelWTwqSc3FOufBVslHoq_dO7vgkEAxQIGkpVAI6dj3aV9Au_oJ2mxz8DqHFc-ovI2RVCXfUy50uSxeVEyyXq7Tt400QsedSVZeFdmCN54nl0-JOuhVip9jCB2hfI2ov0ZxCvDio-R4CkQKAo7nolCELv3a_dOPax5VW5E0p1e2Z9XI1mvSBZRh6oBH0PrZWAaTv6jpJXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناسان فرانسوی: این دیگر چه اقتداری است که رئیس جمهور آمریکا مجبور می‌شود از ترس ایران بین ساندویچ‌های مرغ و نوشابه پنهان شود؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680984" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
داماد ترامپ هفته آینده به اراضی اشغالی می‌رود
🔹
آکسیوس به نقل از منابع آگاه خود گزارش داد جرد کوشنر، مشاور و داماد رئیس جمهور آمریکا هفته پیش رو برای انجام مذاکرات با محوریت غزه به اراضی اشغالی سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680983" target="_blank">📅 00:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680981">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBcfunMdeeT8gmVo0G0ThPZsArfjR_Z8nCdZ-_r3caaCOpm4Ck-5KmMJpHbVKcc179AkhxPpgugnmER0Tn5lvBsGhQv1FuG1VIyB5WEVw0LVrSaRsfYTb_4iRIIFqh6ostCB3Mlrvb38kJmi_c5kfqtMCfhUyc6P4nRF7vxp8shXiDaIV_p9fOyQNgM2UBbOdUyK9WkM3SI863oTcRFZw4vT3RqaCg5kgZ33vpjsRx96rqa2laxW9Ohc6vvBb1vAo8XpwUL98jaPPljFOkdjKScjIpYM3eqQ3hc-zdpZz8LrtdRcPCwSHBdLGffVgC4SJfU7EL_06_q_JRdBWtiTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/680981" target="_blank">📅 00:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680980">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3320b0f7.mp4?token=QDVe0dZgHumFtZ3e4m6sJpjNyobNShyXckkotNx2fWoma-pFuQOJURic7WYW_C9fuK6EEPXVD_psVhXB3AUpN3sWwrkq5xP1P3s0LJjM19pMUfhp23fs4gEQwpnGzF4Bn5sDtJm989UYfxt-CNXLWe72Enm6GW-ouN5o39oR7vvvTeXA_LSnVolaBUyzJZA_NDHQ4WZTlLozsj3YysgbFoByIKpL-Vl7_jv63TCehS1_84P7TK3KvbOdUapRf_1cPOHJtRGYq1vO3Uc8PhqPNkfvurv-upOincPU6w4uG2SapFFAR69IX-2VRVSUKmrgRMotWS9tLf0Qzuzy7RDrvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3320b0f7.mp4?token=QDVe0dZgHumFtZ3e4m6sJpjNyobNShyXckkotNx2fWoma-pFuQOJURic7WYW_C9fuK6EEPXVD_psVhXB3AUpN3sWwrkq5xP1P3s0LJjM19pMUfhp23fs4gEQwpnGzF4Bn5sDtJm989UYfxt-CNXLWe72Enm6GW-ouN5o39oR7vvvTeXA_LSnVolaBUyzJZA_NDHQ4WZTlLozsj3YysgbFoByIKpL-Vl7_jv63TCehS1_84P7TK3KvbOdUapRf_1cPOHJtRGYq1vO3Uc8PhqPNkfvurv-upOincPU6w4uG2SapFFAR69IX-2VRVSUKmrgRMotWS9tLf0Qzuzy7RDrvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف ۳۶۹ کیلوگرم کوکائین در اکوادور، با عکس ارلینگ هالند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/680980" target="_blank">📅 23:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680979">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای جی دی ونس: ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند
معاون ترامپ مدعی شد:
🔹
من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت.
🔹
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت و گاز را برای مردم آمریکا تضمین خواهد کرد.
🔹
مشکل این است که ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند و توافقاتی می‌کنند که بعداً از انجام آنها سر باز می‌زنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680979" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680976">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVKH1bJIks-rQtVUFLHkNh0xvz8TzAW_ZUx9y3cSEex84WyEBxN7PRd0JjzKTd_MrPZbouxyFKVGEYcyGn3pROYQZgzJrMOc7ZEjmm2Onpv5pHnO1XIXSvWcCE_hXVp8hbEQZnqa-4wltj6i2Cnnb5x3RiAG_sgCigux3wEo6XB579XOfGPGXmPEk4feGi_XFQwZBsmevQz5VUPtym85o0zfGRygtvTCCnkuvNPK56vcnmiUS7C86yFLMYJKeeb5LZyDboncfMpSrWQUKThq_nqHZFDbBC_miIs_iUlMzloIqvIjRIm7MeOiMAdNMQTh4jNhdq9p9OaZR6xofz3bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VknIdkUCA9pSHGwoMnMBrGuUh8ErLs1ml364sjJd-iRCbM7JeDutTqRowzS3lpZPs1YcFfeYxzRwZ2-KvEDBiRXUYMvrvEjIpbOYjfJZJsnOZSbyTU2wgFwRbGCC03X5LbMIOZNgB1KVJBOnj7zWzv3cRlZvDBFRoUm1D5y8DrV52XE5aYLU3pvOHsxGDA8bIWXOD9cUsYRf6EyTNJG5XBrWjsMyoeZjXNRZoI1SwEdr0QILvW-sUr6U2soZ3pvWPcxlKVqDWqTWeEGPLxmiPVlrDefhnL5N67RxaOoZcJInnXzuoxJeTb3YJi6qLv9UlrNG4M-XmDLZqM7q0Fdwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXwEUYR4p7_nPaUQQEyvOwE81x67XgVrrfuqDGasGxMMKYWlkeL5vrwGsxSa1Y8ewnA1KVQUtzNwtMSTHQKUkImaG3xubGAWRstwQvlAdg9szgxn_MYmoc8SB7ZjdF6EnzpPAgFXTfGYo4TEZOe2GLaYIecDrutjaW5yFr-kwKI0I3oXGaAEw-G3kUHHAB5f148SSJe6fJYBjXjhC3JKAYDt6BDw-0XqzEAKV7x_UbzYFutbXxSmcZsNgIH6I62r4okAoamZY1sBwKLvP8DmJdUM0YgOzCJuoN6rUXD551hlPSnP0RJi71K0THRejZWc-2nkSamvt9uuFPtFwAXHSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ارسال تجهیزات و محموله‌های نظامی جدید برای اسرائیل ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/680976" target="_blank">📅 23:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نخست‌وزیر ژاپن: نسبت به بازدید پوتین از جزیره «اتوروفو»، به شدت اعتراض داریم
🔹
سرزمین‌های شمالی از نظر تاریخی و حقوق بین‌الملل، بخشی از قلمرو ما محسوب می‌شوند
🔹
این بازدید، احساسات ضد روسی را در داخل ژاپن بیشتر کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680975" target="_blank">📅 23:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680974">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxA5P0iKzd5tZ3GGhVO-VeCJjeA5ouLdnXLBdhjizLsO4RyNCooVW7V14PQkP-tiOocM52-pNawxuOREE2FOEY2h6E3shQF73LZbDeMCqLmJGXJvRpfMPBtMDfda6Aa_FQTigt2uTJ2Jh9sZcxFuf6NLMgBusgqO5GJM-HYqUAxtInobhNp26sfqIVuWP7HCcoLj9b3fEi0-_mS1fZ4SAi8rljnLtunOXJKqmNtn6J85T1dB8btBVOBOOjNSbU3y5IdE1-edhzMdyarOzmEXCxh8CS_HtWcamHLBTYhl1TyGGLaCtHTMmeLTEIYzBk-VAJiBnKJdY_tl8nbNyoYOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل از بازسازی سریع صنایع دفاعی ایران غافلگیر است
🔹
جروزالم پست به نقل از مقام‌هایی از ارتش و موساد اسرائیل گزارش داده که سرعت بازسازی صنایع دفاعی ایران پس از جنگ مشترک اسرائیل و آمریکا علیه ایران، اسرائیل را غافلگیر کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/680974" target="_blank">📅 23:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atcokEY9hYkSri80a9FEJxYAe5Ef7R_GJJnLuUn6jUYRNJDxxAvZUl4hMkoZtgqEJFJEuEy8_uaMjYIGrqivxhUV-oBmltABfdpQ7ibvz_MaOwALRfUYs2x6EZqw30jKW2itw4dttdB10Dv_gxXPoKhKMQz_rk1w35oWn8TdRGS-3zKMPpkw-AEjRrYnLadgr229cKuYDOK-2246mcf50mKCmZw-LmkEkk6gBFmKvWRYRJvtiayta2NYlG2-BKdYu7AxKflA5e5v0_LuLgt_8MdBKGj2JiEPNWoB13fsYKobUZKvMO8ZY0zyq2d8a273N355gbN7uiQ2d2FSiWNQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23aff7a7df.mp4?token=ORDl9Spkwqc-tFT7Y4_5vgAykfuGujBGzEFIDVKwi8JZn_WtZ7RjXO3P_uDQCJF6LlRBiSe1S4rKLHxuz1-gkZFYvfrdyGIHKRDUCaDU2VqKrW1OcNLSlpBkVHmBihl231UhzA0QE0o7YsjKEfusE96Hk7q8Uz6ebCVU5UZ6-1uemQphIJWi9chDqE9ao5PLOeQbuienVYlvSNL-x6NpBbMlIoWr9-f-KHX313rk764zY9oFlAiI_g4OYsdnnJG4x7qVzzZrvQ-p41eBEo89y3ijiv7nz1QNHGJ8CWpOmVLpz4kdJywT1flWlgzZ5ucgKPGfyJrl0BwaY3nmD02QQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23aff7a7df.mp4?token=ORDl9Spkwqc-tFT7Y4_5vgAykfuGujBGzEFIDVKwi8JZn_WtZ7RjXO3P_uDQCJF6LlRBiSe1S4rKLHxuz1-gkZFYvfrdyGIHKRDUCaDU2VqKrW1OcNLSlpBkVHmBihl231UhzA0QE0o7YsjKEfusE96Hk7q8Uz6ebCVU5UZ6-1uemQphIJWi9chDqE9ao5PLOeQbuienVYlvSNL-x6NpBbMlIoWr9-f-KHX313rk764zY9oFlAiI_g4OYsdnnJG4x7qVzzZrvQ-p41eBEo89y3ijiv7nz1QNHGJ8CWpOmVLpz4kdJywT1flWlgzZ5ucgKPGfyJrl0BwaY3nmD02QQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌رسانی که با سرعت کبوتر نامه‌بر کار می‌کند؛ پیام‌ها در راه گم می‌شوند
🔹
یه مسنجر به سبک کبوتر نامه‌بر امده که فاصله شخص و دوستش رو حساب می‌کنه و هر پیامی که به هم می‌دهند، دقیقاً به اندازه سرعت پرواز یه کبوتر طول می‌کشه تا به دستش برسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680972" target="_blank">📅 23:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb02fc38ef.mp4?token=LTv1CXJy9FOoFpcgrobAREE_lKPTUk8KWQ9-wjnO4UJZhfgk48UXM2fuO8xcWcJKY_xIraBXZ3NgtQt_rDAcaTJmya2wg8xZIaMv1fFKwUzVKWqcBpIyoBwtXLjLACynoJEMAILE9vK2kRhtBbYH5BF0iGLf3bb9ufpdkCacUDcZki3xO8PEcug4hW4wSL1vwWqkc77uP-nBWI1ieowZLRdYVeZWshkFMdsvRkpsFOqzzju77wJwEPMtrcN9c025UJAfjyw3hQOUE3ZaEzBRSuGFThs85Ar3o07aU8nc0ELOLuobV5hIDW0XXyEaO1QmwJaH8JqKZ9Wg_Y2tV6eBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb02fc38ef.mp4?token=LTv1CXJy9FOoFpcgrobAREE_lKPTUk8KWQ9-wjnO4UJZhfgk48UXM2fuO8xcWcJKY_xIraBXZ3NgtQt_rDAcaTJmya2wg8xZIaMv1fFKwUzVKWqcBpIyoBwtXLjLACynoJEMAILE9vK2kRhtBbYH5BF0iGLf3bb9ufpdkCacUDcZki3xO8PEcug4hW4wSL1vwWqkc77uP-nBWI1ieowZLRdYVeZWshkFMdsvRkpsFOqzzju77wJwEPMtrcN9c025UJAfjyw3hQOUE3ZaEzBRSuGFThs85Ar3o07aU8nc0ELOLuobV5hIDW0XXyEaO1QmwJaH8JqKZ9Wg_Y2tV6eBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680971" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFzKgR68L7UCIQ06CvAEB5DqmdHIwDVA9OFGHV3u3-R4OKY6Jph5lt9gMAhJSNqbqDz794i1sORGc2T1y2hd9MPZ_pvHrVw7MS4bGcnJ6ko_IkTA28uy0T0Q2d7EzdK9adxTDjL1SrXVRKGJ-6hrzXnGZ-dEy7WxWA5hgE_w3IDjgKgj2qpckE_8fDPoD97HLoLQXB2nsnujJSn0MgDNFQxo_zyUJemehzgvJy3Nm_R2CLW7CPJ6hMF1J4U6OlgSkcjSZKrzvtYa-mO0LBADoF4G2NoMMiwBbGHDfDNBMdACvGlZD2KA7745SV6ZALtFMeKQ2vgcGmq_WaSdG2eR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrfVxCSYI2V_Q9t6XKME1F2u7ViSCvAYotomiedTRupUr4YrDmXCqUMOrwm8ju8uXqlLhKaidP7jwzCPLzH20yegP7b46r4fkXiJmWU0KN8VLRJIUlkTbbnwoNyoSZQd61ux07xZf1s8PbJGE54Ad46yJJrQ0uCIxi7gaAoE94VRrWw6KnEDxt3se085v2WBddlvZD8sYhAQFIryVJ9kBHjTATnPZqbBMyitwvJLk6l8D8AmqmmkFCY80B6hc1jyPiOHUDtPHTrpyD9wSWgKzyx0Vjft736hICohzC0gWinRjkM8BW9HYXXFbsiPo71jy3EItWEVRb5KUTbJL_cC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzmkWSTbpTuvNPzDvAiI1tXRZ5Nn1oKoAox8BPCeNCVInfNBXfc2VUeEqwS54NxzVu3667NCqhCZ3_agCFxaGyycl-xqAoah_7UryEj_97CqkIJRDbX5fQQ_J1zRFjxI1xldnWers4XbjTEwDenR6Qj5qxpjaN4A15W7LP1r8tSYaKV4zQ7C8kAZkmki3vTFB6Xmozptbn-qbC_Ecsmi5_AHO0G7E_LzF6SJlYCkjsi-ZyG7FMwciFh6ZZNmgHvqFmokfyyObRBxyzAEhpPtnUX2H9pm06SKnwAaaL8dukPj3wjs6r9m3JmaBWV34u99lpsA4_ebCPFmPNOfw3xk_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت کریستیانو رونالدو به تمرینات النصر عربستان با موهای نارنجی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/680968" target="_blank">📅 23:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65ed2a7e1.mp4?token=vzRdfuvaGWi4pGj-GAYOZdPceeWCRegMWqTLsuxgRB9HOa0LpPtamVbYwCLnoYoAIoxjjtld6iGOQ3JztFgV0cPqce0_S9DGvGeZBPJQrcW_j8FrQWQu1qB1d04cTOQC8mVXSUqeuGBP2ReDES4falY3qOovU_r60Xmy1IAYbo3FG46GCy5If-LGHdhFMxSNE7IQbAMo9ZEIiEdDEhNrRmRmHvXQFdc9jq8SymBfkSP8S8_a2Kib21S8JfHN-M8h8sSAd7TpE7l56kmHtD2Uj-C5jr06-6pZUYyKzZNDglhECqJh_eS_OBwtrHDeNpWrMo1IzG0AAx6jjlF1f5s4xStQpA8PQnfYlKFZLskZdner2Mnlua5rLgxEqSFJNe_fby64LTV3-I7HKbOJQ9YYibnxTL73dueovDmU6Tiahohvtu2xmEhXELfP1nhlto14JvL-GdujupSlu7ymYxMPksXn71XyFyMUtLLTHhPV-Va3Zj4m5gWEjqoJvWDMz4kO55K42gkwbcrUQnjww2CkLFlZCf2z-bp6rudZFsxefAIeyenEBUIwiy902nCtiZRSrovB5Fi2QqrM91Adhdw5HAM-kaqeCJ2n4-dRrBdqZzDoStHxuWhG5j_KkRtp4s8rhjMDZ-93jmGciuy3_qe3ZgmmvZvarpHK1eV1OuldljY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65ed2a7e1.mp4?token=vzRdfuvaGWi4pGj-GAYOZdPceeWCRegMWqTLsuxgRB9HOa0LpPtamVbYwCLnoYoAIoxjjtld6iGOQ3JztFgV0cPqce0_S9DGvGeZBPJQrcW_j8FrQWQu1qB1d04cTOQC8mVXSUqeuGBP2ReDES4falY3qOovU_r60Xmy1IAYbo3FG46GCy5If-LGHdhFMxSNE7IQbAMo9ZEIiEdDEhNrRmRmHvXQFdc9jq8SymBfkSP8S8_a2Kib21S8JfHN-M8h8sSAd7TpE7l56kmHtD2Uj-C5jr06-6pZUYyKzZNDglhECqJh_eS_OBwtrHDeNpWrMo1IzG0AAx6jjlF1f5s4xStQpA8PQnfYlKFZLskZdner2Mnlua5rLgxEqSFJNe_fby64LTV3-I7HKbOJQ9YYibnxTL73dueovDmU6Tiahohvtu2xmEhXELfP1nhlto14JvL-GdujupSlu7ymYxMPksXn71XyFyMUtLLTHhPV-Va3Zj4m5gWEjqoJvWDMz4kO55K42gkwbcrUQnjww2CkLFlZCf2z-bp6rudZFsxefAIeyenEBUIwiy902nCtiZRSrovB5Fi2QqrM91Adhdw5HAM-kaqeCJ2n4-dRrBdqZzDoStHxuWhG5j_KkRtp4s8rhjMDZ-93jmGciuy3_qe3ZgmmvZvarpHK1eV1OuldljY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
فرناز، بعد از دست دادن پدر و مادرش، حالا تکیه‌گاه خواهر و برادرهای کوچک‌ترش شده؛ در حالی که خودش هنوز برای ساختن آینده‌اش به حمایت نیاز دارد.
🌿
در ادامه پویش هفته گذشته، این هفته نیز برای
تأمین مواد غذایی خانواده‌های تحت حمایت مهرآفرین
همراه شویم
❤️
.
🏦
شماره کارت:
💳
6037991199529904
💳
5894637000012820
💳
6037991199500038
🔖
شماره شبا:
IR710170000000216780692009
📞
*780*35260#
📌
اگر مایلید کمک شما فقط برای
فرناز و خانواده‌اش
هزینه شود، در واتساپ یا تلگرام به شماره زیر پیام دهید:
📲
+989101785282
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680967" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
پاسخ محکم سپاه به ادعاهای واشنگتن؛ دریادار عظمایی: واقعیت در میدان است نه در اظهارات مقامات آمریکا
👇
khabarfoori.com/fa/tiny/news-3237494
🔹
فرودگاه کره‌جنوبی؛ برنده غیرمنتظره جنگ علیه ایران
👇
khabarfoori.com/fa/tiny/news-3237470
🔹
از «شام لوبیای» معصومه ابتکار تا «عروسی در باغ الهیه»/ روایتی افشاگرانه از عباس عبدی
👇
khabarfoori.com/fa/tiny/news-3237489
🔹
نوشته‌ روی موشک ایرانی خطاب به اعراب/ عکس
👇
khabarfoori.com/fa/tiny/news-3237446
🔹
سناریو دولت برای بنزین چیست؛ با قیمت نجومی مواجه خواهیم شد؟
👇
khabarfoori.com/fa/tiny/news-3237426
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680966" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b408def775.mp4?token=uw2nz0R5WjL6pFpnG4tkv3F4ACTXQz_GlXt0fyYqVKwwzxg6HnaMaPWm3PpVas-wYBQ4A1NFqBJD2zkE6f_Jy-ueD33eWuUJ2m3nW571v7SGMNA6lhjwEX2gIHhO_jeCvJiikmwQcfTLZWjvoUJ2glDVw6RHUkntzMUIymUy7TaXhOBTvI366Cfirml6xF5xgM8EzH8wL1BfcqYQ-1fwVIo0YKk2XaGBg9cXq2V_RkWdq8Z3FS8Wm3VHCuV45JnxyExKk3Zj_-g6tGJMktR-aEr41rq6eJzHhepOD7GVGWL4aFf_umksypODLGIiOrPx1Qn1hqPd2HSuFo8uyvHW6of7MsGNUXQikq19whMpKYugAvxYmm0F4CxOkFEGIgEm6JNXlfppi9TQ4N4UdqVhBPOqOmh9YaPqFAl_lFAc8a31vAgFGSI_4X2IjMPPCSIvaaEa4HTNuQzoYcCiizSwzSmZce3_Y6-KSBpru4dEMUUuWODgafylYLEUzMTrFBsNvPduSxEqNQr8FCHBOtriApsmffsP0W_PkC6-K-2osq5-TL8fSBvJaoS3MLzYl3jdKaGL3eGkk3fn5WX2FiaEuDTIdfct-kXUjAda9hysN0FbZf89WVVNSkesb_M_HclTMi03J0-77S1q4_Y8IRDFY5Bimc2PB9UzV0FllOlrzlU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b408def775.mp4?token=uw2nz0R5WjL6pFpnG4tkv3F4ACTXQz_GlXt0fyYqVKwwzxg6HnaMaPWm3PpVas-wYBQ4A1NFqBJD2zkE6f_Jy-ueD33eWuUJ2m3nW571v7SGMNA6lhjwEX2gIHhO_jeCvJiikmwQcfTLZWjvoUJ2glDVw6RHUkntzMUIymUy7TaXhOBTvI366Cfirml6xF5xgM8EzH8wL1BfcqYQ-1fwVIo0YKk2XaGBg9cXq2V_RkWdq8Z3FS8Wm3VHCuV45JnxyExKk3Zj_-g6tGJMktR-aEr41rq6eJzHhepOD7GVGWL4aFf_umksypODLGIiOrPx1Qn1hqPd2HSuFo8uyvHW6of7MsGNUXQikq19whMpKYugAvxYmm0F4CxOkFEGIgEm6JNXlfppi9TQ4N4UdqVhBPOqOmh9YaPqFAl_lFAc8a31vAgFGSI_4X2IjMPPCSIvaaEa4HTNuQzoYcCiizSwzSmZce3_Y6-KSBpru4dEMUUuWODgafylYLEUzMTrFBsNvPduSxEqNQr8FCHBOtriApsmffsP0W_PkC6-K-2osq5-TL8fSBvJaoS3MLzYl3jdKaGL3eGkk3fn5WX2FiaEuDTIdfct-kXUjAda9hysN0FbZf89WVVNSkesb_M_HclTMi03J0-77S1q4_Y8IRDFY5Bimc2PB9UzV0FllOlrzlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دولت برای بنزین چه برنامه‌ای دارد؟
🔹
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🔹
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با قیمت آزاد فروخته شود؛ درست همان چیزی که قرار بود در کرمان اجرا شود.
🔹
روش سوم: از ۱۲۱ میلیون‌لیتر، ۳۰ میلیون به حمل‌ونقل عمومی تخصیص داده شود و ۹۱ میلیون لیتر باقی‌مانده به‌جای خودروها به همهٔ مردم اختصاص داده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680963" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDU2Ns32Rvv-sZ0tf39UooGL_2HUodxcF0N3Pf9-_Q6x_rx16XM1tUIBniKQHoLoYp1N97KQ85etYcY-8DHV8drkzWo78RWomwDFDFZWgsP0GLc-Yo1VZ8BJWxa9k7XIerfYyHRWVQBYimOhBZhMwyJlJ-dPP_UmdN_G7wVKQr_oq4NqvbIt42nlGCvhSYf2ksBWk3iV2lC-gqKhvcXQPcgBl5hRLUNKOasvJc2YOO9y5yZTaa_fQyX8kVLxxkQgor4vGXUEIiF20aJvmnxNrTnTmHNZ-nZ2jnfv9jvjBMKW3Gw2dJaDm-aApRNp8wKM8YMYcOkqDAQssPZhh4o0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوتبالیستی که در زمین فوتبال مُرد، در سردخانه زنده شد!
🔹
یک اتفاق کم‌سابقه و حیرت‌انگیز در فوتبال نیجریه، نام چینیدو اوزور، مدافع تیم کاتسینا یونایتد، را به صدر خبرهای ورزشی این کشور برده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237312</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680962" target="_blank">📅 23:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b698d3c57e.mp4?token=DsQlRZ3SQmnPC3G0qSq7eJOy2pvVHZmUzpJxHlgrNAlUOSkUo6rnmbmn4nvw7BTqnuROiMRoIZt-TlSSsof_qyaNVJ0ACcUIcIPpAhnOg_gw4rCNERbiVXbNDZOtjcxK_RfJ0v0x8xup6vLbRg2wBt_XdG9IrmShKA1OjT-Q6llzosCRcEt5z4iJxIjAUVwn0mgbkaNNoVzrqFUM6Qw8h8kOI9ryFm_abNiAN5OV2nbsDJjJ-0I-mNILHVo9ur4-pYYinXZiRN5C1vwWUdMZXx6RZjes1zZltS1KxuQq6m0seDXYcHeqIaTv7D4hfV6tcPz2l8BIx1KKKTpgU4URgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b698d3c57e.mp4?token=DsQlRZ3SQmnPC3G0qSq7eJOy2pvVHZmUzpJxHlgrNAlUOSkUo6rnmbmn4nvw7BTqnuROiMRoIZt-TlSSsof_qyaNVJ0ACcUIcIPpAhnOg_gw4rCNERbiVXbNDZOtjcxK_RfJ0v0x8xup6vLbRg2wBt_XdG9IrmShKA1OjT-Q6llzosCRcEt5z4iJxIjAUVwn0mgbkaNNoVzrqFUM6Qw8h8kOI9ryFm_abNiAN5OV2nbsDJjJ-0I-mNILHVo9ur4-pYYinXZiRN5C1vwWUdMZXx6RZjes1zZltS1KxuQq6m0seDXYcHeqIaTv7D4hfV6tcPz2l8BIx1KKKTpgU4URgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخشش رعدوبرق در آسمان اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/680960" target="_blank">📅 23:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بیانیه ایران به مناسبت تصویب معاهدات چهارگانه ژنو درباره حقوق جنگ
🔹
وزارت امور خارجه ایران امشب در بیانیه‌ای اعلام کرد: جنایات جنگی ارتکابی رژیم صهیونیستی در جریان عملیات‌های تجاوزکارانه علیه ایران در سال ۱۴۰۴ و ۱۴۰۵ که با همدستی و مشارکت آمريکا صورت گرفت، در زمره شدیدترین نقض‌های حقوق بشردوستانه بین‌المللی از سال ۱۹۴۹ تاکنون محسوب می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/680958" target="_blank">📅 23:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e48e6fb8.mp4?token=WDWhev34fxKe7vfbkc9T-prK8Lxc5Shoqu5h9VHVEHmFKW5LYAmpY9XtPf1OfiT4aCFyB1grcqk0BF1efvouBLrnXyMKe1ZXPJWmbhGEnJziOVp2s-8qMk-jDDcRP7ftKBC2pccpzbvnoGAxDG77CoOlVMaUIX7mYTnlNOICyiZofHNPhR7D0db1CuKXeaCPpOAkUKTUFtZtjfoPlzEUC71_70wMiR0r2GmhHs2NXnrI1ZWOyIeh7RXUPDHC6oupqPzobhqvcpCPKpXNswW0uwrEYRyNXxK20PCpHvw7Y2vBuipv_Lc5h0R3RYO2Y9nRI5boh-CVVWHPKyxMddMPRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e48e6fb8.mp4?token=WDWhev34fxKe7vfbkc9T-prK8Lxc5Shoqu5h9VHVEHmFKW5LYAmpY9XtPf1OfiT4aCFyB1grcqk0BF1efvouBLrnXyMKe1ZXPJWmbhGEnJziOVp2s-8qMk-jDDcRP7ftKBC2pccpzbvnoGAxDG77CoOlVMaUIX7mYTnlNOICyiZofHNPhR7D0db1CuKXeaCPpOAkUKTUFtZtjfoPlzEUC71_70wMiR0r2GmhHs2NXnrI1ZWOyIeh7RXUPDHC6oupqPzobhqvcpCPKpXNswW0uwrEYRyNXxK20PCpHvw7Y2vBuipv_Lc5h0R3RYO2Y9nRI5boh-CVVWHPKyxMddMPRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه سازی و مدیریت راهبردی انرژی: واردات بنزین آسیب‌های جدی دارد و کالاهای اساسی و دارو اولویت واردات است و نه بنزین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/680957" target="_blank">📅 22:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
فرمانده واحد سنتکام ارتش تروریستی آمریکا: هدف قرار دادن زیرساخت‌ها در ایران قواعد بازی را تغییر می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/680956" target="_blank">📅 22:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsYw3mqUaIRnJZeszDUSPVM30J39hh15m1-9fEJmhd-rkBCqcqy2uIhD303MRG3LDw-TQuZlLWDJirah3QWOfemsWurVdqM7jTMSmw_76IJ0_smUuGczEX1Eh80yZ4uRNtIPGfJFUdfeHjkxwSpXO2B-PaBOV3YxqmYxh2yIBWqIaMNUKC6JiZNcM1WvhlV3CJKN0zbqNTgUztkaW3lqyBfioA1uVtTAsq3w-WhlldlOkUwtu9a0QOH_CoYkK7R98WL71N71sDsLnsGNByeaWsbHSDmY4EkuLc6C95MkzzMbhHXSCoD-6K6-A7tGgIWE_qz2NS39cYygmS1QU2kIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/680955" target="_blank">📅 22:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزیر خارجه مصر: برای پیوستن به توافقنامه مکه ملاحظات قانونی و حقوقی داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/680954" target="_blank">📅 22:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دریادار علی عظمایی: واقعیت در میدان است نه در اظهارات مقامات آمریکا
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
تنگه هرمز بسته است. تسلط ما بر تحرکات کامل و قاطع است. هیچ تحرکی در این تنگه از چشم رزمندگان نیروی دریایی سپاه دور نمی ماند.
🔹
واقعیت را باید در میدان دید نه در اطلاعیه ها و اظهارات مقامات امریکا.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/680952" target="_blank">📅 22:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC3zTSMy2cYA4U1S019MoOVkDn7Fw_KXp7eYPFjEDHicK-Upw_DKj1Ml0Bvyyc4EH7--3c9g2QuLsHA8eYiO4LyxH-8BUmrakHqZ8ayMkq3AH8NmzNeWdysjDBDrvxb2Z5DLGjqiipd14S3Y2BArIfaYjKCpAz0dLyln6ZEqsffZn_iWl1zVSjx-63vMmVCnu85qRbmhZ2qtDcW8DCOwlpxoTqsVIIqG9zMJRlrd02Cr5rDRY9APalaLuXEXdE85nnWXaZ-Nc2YEZ4lwt6nPewSkp8escN3hnQErj9E0hk2p1EAVhjpoPgP677IZCNkGWQ5VtNklis5n5Ml7RChOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: هرگونه بی‌ثباتی منطقه‌ای ناشی از اتکا به نفوذ خارجی با واکنش قاطع ایران روبه‌رو خواهد شد
🔹
تا زمانی که شما در برابر دشمنان اسلام تسلیم می‌شوید، حاکمیت شما در معرض خطر خواهد بود و جایگاه ملی شما تضعیف خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/680951" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fed294f.mp4?token=ayaRfa5ZLPVNvQAnoBZXRzZU-NtUHGlPrvjpfDVaQAVdx_i85lAGzXYsGMfJCHMkB2gIo1IbxQPRxa5qXKH7mUIMzmoj65LC27GcXNQMs1_uPhKqaoUtFqNCzQ4LLBxkMkTYPFfH-hGMj4R7NQy9Gun3f8jFu3QFD4JgzC3OkXrXOZ_wMebxskN1XIaKwisj2U7mq2d9i9U8umC-bBPfliTZ4KVp1plVC1Jc0EOdp2BVYL4lienF5H5waEo4O67WAphhMunoaZjJ1SHAdOAAmBh6uuyNgZRJWK38qCrY89zzQa1PtC4xu_WDVybTNQZ9ZvPM7Pd7VNHd9jAc_C0gXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fed294f.mp4?token=ayaRfa5ZLPVNvQAnoBZXRzZU-NtUHGlPrvjpfDVaQAVdx_i85lAGzXYsGMfJCHMkB2gIo1IbxQPRxa5qXKH7mUIMzmoj65LC27GcXNQMs1_uPhKqaoUtFqNCzQ4LLBxkMkTYPFfH-hGMj4R7NQy9Gun3f8jFu3QFD4JgzC3OkXrXOZ_wMebxskN1XIaKwisj2U7mq2d9i9U8umC-bBPfliTZ4KVp1plVC1Jc0EOdp2BVYL4lienF5H5waEo4O67WAphhMunoaZjJ1SHAdOAAmBh6uuyNgZRJWK38qCrY89zzQa1PtC4xu_WDVybTNQZ9ZvPM7Pd7VNHd9jAc_C0gXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیین شام غریبان شهادت امام رضا(ع) در حرم رضوی برگزار شد
🔹
آیین شام غریبان شهادت امام رضا(ع) با حضور اقشار مختلف مردم، زائران، مجاوران و خدام حرم مطهر رضوی پنجشنبه شب در صحن و سرای این بارگاه نورانی برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/680950" target="_blank">📅 22:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=pd0uUSnXAa-KC5JTb6w_sY3tsUiSPMEgCzQ5Vvzjski5QrC_9aJag-81fDgNEB6PVDYu2mGcQdtKKOu_M7aMIUGz0d-k3Uabi88oOyx33t8zNfOJbQDZHO0tlKODsP_uoPpyulAgjoRJk49Dh-7srkiItMbqWh5xRKCrsGQqMJCruY1amSo1rGbywoTerBlSORg-yuhJWRKO2RsAk0FpRG8hB_ml7j3F2wsrz-yLgxL9BpK39sBHGGs0Bwm8vbnfmCcjPJuF_vQAGYKsDQ4kxFbExKtKMaMyYqFc4HfTMzTtjD-S8gGa3Me_jrucXJyQHD-HQqVTyPLIyhTQ95BoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=pd0uUSnXAa-KC5JTb6w_sY3tsUiSPMEgCzQ5Vvzjski5QrC_9aJag-81fDgNEB6PVDYu2mGcQdtKKOu_M7aMIUGz0d-k3Uabi88oOyx33t8zNfOJbQDZHO0tlKODsP_uoPpyulAgjoRJk49Dh-7srkiItMbqWh5xRKCrsGQqMJCruY1amSo1rGbywoTerBlSORg-yuhJWRKO2RsAk0FpRG8hB_ml7j3F2wsrz-yLgxL9BpK39sBHGGs0Bwm8vbnfmCcjPJuF_vQAGYKsDQ4kxFbExKtKMaMyYqFc4HfTMzTtjD-S8gGa3Me_jrucXJyQHD-HQqVTyPLIyhTQ95BoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است
🔹
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، چند هفته قبل از اجرا آن را به مردم توضیح می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/680949" target="_blank">📅 22:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شوک یک تجربه مشترک؛ عبور مادر و پسر از رودخانه‌ای میان مرگ و زندگی
🔹
00:15:30 وجود جهانی زنده در هر دایره از ذرات آب
🔹
00:20:00 اهمیت خواندن نماز و منع شدن از سبک شمردن آن
🔹
00:40:00 تجربه نزدیک به مرگ مشترک مادر و فرزند در عبور از رودخانه‌ای طغیان‌گر و گل‌آلود
🔹
00:50:00 رؤیت مرگ خانم بیمار دقایقی زودتر از وقوع آن
🔹
01:07:10 رفتن به جایگاه خودکشی‌ کنندگان بخاطر کشیدن سیگار در دنیا
🔹
01:10:10 شادمانی و غرور شیطان، بزرگ‌ترین رنج و عذاب گناهانم بود
🔹
01:15:00 غیرت‌ورزی برای اهل‌بیت(ع) در دنیا، کلید شفاعت‌ام در جهنم شد
🔹
قسمت بیست‌ونهم (فراز و فرود (۲))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/680948" target="_blank">📅 22:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=tIu6nghavSeozDJpn9jZb9Y0Bm3P71uFvQ_qhFQJMiRkL9jhTpqJQX1Ez_vmnjvU0mV1lpqB7qBkWcx_JKuxPOW_WtPUaLF-nfIImWzJITw7LtiCVIY7ZRG04AmXvw6RxI4pi62l90qnw1SqYuMcGrzKE-5qNHqTedAhrULPlXc07Wm_90z9fSlnKuabZepmYK-17I-_hpdOzMscHopOd5-a3MEJrcN0veNOs1UFNZDdQumHxlFTdTV6LypEACl6eJTLg7mtV2Hjmzv68IuWa4fQFk3yG6M9QdyCn_9Ur5pZzpHCmYMlCKqStwXtGI5p-r9FJK6OwhNHqs53zgDhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=tIu6nghavSeozDJpn9jZb9Y0Bm3P71uFvQ_qhFQJMiRkL9jhTpqJQX1Ez_vmnjvU0mV1lpqB7qBkWcx_JKuxPOW_WtPUaLF-nfIImWzJITw7LtiCVIY7ZRG04AmXvw6RxI4pi62l90qnw1SqYuMcGrzKE-5qNHqTedAhrULPlXc07Wm_90z9fSlnKuabZepmYK-17I-_hpdOzMscHopOd5-a3MEJrcN0veNOs1UFNZDdQumHxlFTdTV6LypEACl6eJTLg7mtV2Hjmzv68IuWa4fQFk3yG6M9QdyCn_9Ur5pZzpHCmYMlCKqStwXtGI5p-r9FJK6OwhNHqs53zgDhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: تا الان هیچ تصمیمی در دولت برای تغییر نرخ بنزین و سازوکار تخصیص فعلی بنزین گرفته نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/680947" target="_blank">📅 22:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آی۲۴ نیوز: ترامپ و نتانیاهو از زمان دیدار در واشنگتن که به دو هفته قبل بازمی‌گردد، با یکدیگر صحبت نکرده‌اند
🔹
این قطع ارتباط در شرایطی رخ می‌دهد که ترامپ همچنان در حال بررسی گزینه‌های خود درباره ایران است
🔹
در عوض نتانیاهو تماس‌های مکرری با جرد کوشنر، داماد ترامپ داشته/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/680946" target="_blank">📅 22:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdbecbe41.mp4?token=ChzhLTPsCt-RkYVGEk97fR78_O3oS2YAB-2cU_l7JaBruZ9XyitLhsqxp5vHw_Mci-8rJjafGH3Y4lVW6IcqdcLdb4mg9Qzi3FxSfYk-vIryYx30FHyiYi7dn8xVqWLptHAH9sXGGhNvCGt_Pns_afcNF_hmq3zD_vQQ9qy3QnozphgKdjiYfVfwwVthMchINavQrsKob9nKQIpqMm82DSPdddVXvJxcgLfqQRRKjh_IJ8SPpFateUilJkPe5uCmKVJIy9zQFb_clVu-FVOv4K4ovWJ9zK--jjoyO-aVrDjD9csE_tl1wlcYNayH828VKcD5zghDaQfFUbhCp00FEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdbecbe41.mp4?token=ChzhLTPsCt-RkYVGEk97fR78_O3oS2YAB-2cU_l7JaBruZ9XyitLhsqxp5vHw_Mci-8rJjafGH3Y4lVW6IcqdcLdb4mg9Qzi3FxSfYk-vIryYx30FHyiYi7dn8xVqWLptHAH9sXGGhNvCGt_Pns_afcNF_hmq3zD_vQQ9qy3QnozphgKdjiYfVfwwVthMchINavQrsKob9nKQIpqMm82DSPdddVXvJxcgLfqQRRKjh_IJ8SPpFateUilJkPe5uCmKVJIy9zQFb_clVu-FVOv4K4ovWJ9zK--jjoyO-aVrDjD9csE_tl1wlcYNayH828VKcD5zghDaQfFUbhCp00FEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی:  اجرای تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد
🔹
رئیس‌جمهور تأکید کرد از اقداماتی که مردم را غافلگیر می‌کند پرهیز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/680944" target="_blank">📅 22:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbxsfON0MW8UfK8lDTKnVW_38_XBgVdUPsqOYpMKwUMv_seOk89fv49DAYniSnartFKDZ_CBtzLbx8hmIox9wubdOQ0sx-pqEpWY4X-4721fQvDkweExjqiPqGp2GoKLPZMpv7nUiXXrrigBTcIUj5KeazQ_-RcZ3GI2_62hAE8ZyGG5qRwPVUElJuXgP5YRagHZU6e-9qFU60AG8lQQTG48LExAvlyxSLJ_LpyTQd_XnaApHIrfYmv7SG1eRJfmzuu5WlVf-LdngAHcKehb0ZiIpE3HGP6-uVoH-B_XCEdEbPfe2OHlPTzbQuJSKjO3BysNWxQl2klVkJIfdXa22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردا جمعه ۲۳ مرداد نخستین روز ماه ربیع‌الاول ۱۴۴۸ ﻫ‌‌.ق خواهد بود
🔹
گزارش استهلال ماه ربیع‌الاول ۱۴۴۸ ﻫ‌.ق از سوی ستاد استهلال دفتر مقام معظم رهبری منتشر شد؛ بر این اساس ماه صفر ۲۹ روزه بوده و آغاز ماه ربیع‌الاول ۱۴۴۸ روز جمعه ۲۳ مردادماه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/680943" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رسانه رژیم صهیونیستی مدعی خنثی سازی طرح ترور وزیر جنگ اسرائیل شد
🔹
شبکه ۱۴ تلویزیون رژیم صهیونیستی در گزارشی مدعی شد که یگان نیروهای ویژه ارتش رژیم اسرائیل موسوم به الیمام با متلاشی کردن یک تیم مسلح در جنین، طرح ترور «یسرائیل کاتس» وزیر جنگ این رژیم را خنثی کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/680942" target="_blank">📅 22:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آیت‌الله سیستانی شنبه را نخستین روز ربیع الاول اعلام کرد
🔹
دفتر حضرت آیت‌الله سیستانی در نجف اشرف اعلام کرد فردا، جمعه، پایان ماه صفر است و روز شنبه ۲۴ مرداد ۱۴۰۵ نخستین روز ماه ربیع‌الاول سال ۱۴۴۸ هجری قمری می‌باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/680941" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
شبکه المسیره یمن در خبری از آغاز موج تازه‌ای از حملات مزدوران سعودی به مناطق مرزی یمن در استان صعده خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/680940" target="_blank">📅 21:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عربستان خواهان توسعه همکاری نظامی با عراق است
🔹
وزیر دفاع عربستان سعودی (برادر ولیعهد سعودی)، در دیدار با مقامات عراقی بر اهمیت تقویت روابط نظامی و دفاعی میان دو کشور و همچنین تداوم هماهنگی‌ها برای ثبات منطقه تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680939" target="_blank">📅 21:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سقوط ملوان آمریکایی از ناو «آبراهام لینکلن» در دریای آزاد
🔹
شبکه CBS گزارش داد یکی از ملوانان بال‌هوایی ناو هواپیمابر آمریکایی «یو‌اس‌اس لینکلن» اوایل ماه اوت در دریا سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/680938" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e3638fee.mp4?token=bopA37R-geL_mpDeuBXWNKPw2gPiLIKlhDYrRCJh6cI8CW6oCzylz2rZKR_rLxEae3_avU-xcXZeCgWJ0GYK_Ndxqt32U-Ph8vD7OOhLWAfYUFLFmoZY_fCYinXuvy9QHYPz_1DHEwhSiHGPeseMlaEvdmlJmyZ1dpJNJKniyNyBKe3h9NwKqNJPiWQ5HjA5yhQBBObcfCgufV-FVPRlG8Ba46sk2AQ1qNZ7HSYG0QhSJypV3Odc_kdCNO-E76Zb_0e2RvM0CXLyBDucl8SlmFSjwTBIfwkVrcUD1d_THfYeJFAE2kVd9ximprElunMG-xlgtQUCw4oFYCbSm2gC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e3638fee.mp4?token=bopA37R-geL_mpDeuBXWNKPw2gPiLIKlhDYrRCJh6cI8CW6oCzylz2rZKR_rLxEae3_avU-xcXZeCgWJ0GYK_Ndxqt32U-Ph8vD7OOhLWAfYUFLFmoZY_fCYinXuvy9QHYPz_1DHEwhSiHGPeseMlaEvdmlJmyZ1dpJNJKniyNyBKe3h9NwKqNJPiWQ5HjA5yhQBBObcfCgufV-FVPRlG8Ba46sk2AQ1qNZ7HSYG0QhSJypV3Odc_kdCNO-E76Zb_0e2RvM0CXLyBDucl8SlmFSjwTBIfwkVrcUD1d_THfYeJFAE2kVd9ximprElunMG-xlgtQUCw4oFYCbSm2gC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب کامل یک انبار در بندر المخا در حملات انصارالله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680937" target="_blank">📅 21:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmP6Pa5fpaqNCxqZKKOKpkeCyVOImLFANDfqnItoW9PzibonajfPgQJDclvwhgz7KpURINoXAG1wlzbzOhLhJrZ2bmMntXLlzWjdDjQDpF2ZhmS1mbCN8BVO0vSv4btSIg5mrO0zOIW8xnC9neEPWXXulF-sQC9x_bi9fmfAQm9TSGvs9QCTWReZBmsgH3ab6C3RbxUhDW5W0-jmnfac0OpVhyBsYwW3enJM1lihmTd8GQc9YUJzSduDIpfLthoy5OUh3JHloNpP0S4kF6cJeSf8IocSONS_ug4s-8zNDj-SM8OvbbHvOoJcf1bGXbCHsPmNf1YDgD_ois3zWzmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس جالبی از شالیزارها که شکل خاصی را به خودش گرفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/680936" target="_blank">📅 21:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
برای نخستین بار در تاریخ، دختران وزنه‌برداری ایران نایب قهرمان آسیا شدند و پسران نیز عنوان نایب قهرمانی قاره کهن را کسب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680935" target="_blank">📅 21:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
خروج قطار از ریل در انگلیس
🔹
یک قطار مسافربری در حومه شهر «لویز» انگلیس از ریل خارج و واژگون شد که این حادثه منجر به حبس شدن ده‌ها مسافر در داخل قطار شده است.
🔹
در این حادثه دست‌کم ۴۰ مسافر در میان آهن‌پاره‌های واگن‌های واژگون‌شده گرفتار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/680934" target="_blank">📅 21:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع عربی: نیروهای مسلح یمن با دو فروند موشک بالستیک، یک مرکز حیاتی در الحاریکیه در نزدیکی باب المندب را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/680933" target="_blank">📅 21:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40103108a8.mp4?token=Lr3YtBaaYnH58AQYFPlo8SCcwmH4FcRPjyLPp0f-6rTL_mhqtEVIKi_4pe98J2iACX4m_D9EdfKZgcV96f0AObRhDZdB2cByR4MCUlPl9aMhcgrhb5jn5ddKXNnwkoE_OJxPmiRlPh6lu_1xnWXqALrtDz9st3ynAAVs6vNYhbG9TJI_hzQNlT7qlNZu_aLihFBobyTHwEfA2m85mqXqkoO_zQUzWTZEpBZlea3gDNaocO7i-4YlJFlqwoHWpGWwTyZ5Qp38LjezQ4oxWUZH2uSQ2mvDqRu6taJ3XbAu-_wcc8MCzabxcg3GBScCX6YyOY28OpgQFF7woab55b7Nfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40103108a8.mp4?token=Lr3YtBaaYnH58AQYFPlo8SCcwmH4FcRPjyLPp0f-6rTL_mhqtEVIKi_4pe98J2iACX4m_D9EdfKZgcV96f0AObRhDZdB2cByR4MCUlPl9aMhcgrhb5jn5ddKXNnwkoE_OJxPmiRlPh6lu_1xnWXqALrtDz9st3ynAAVs6vNYhbG9TJI_hzQNlT7qlNZu_aLihFBobyTHwEfA2m85mqXqkoO_zQUzWTZEpBZlea3gDNaocO7i-4YlJFlqwoHWpGWwTyZ5Qp38LjezQ4oxWUZH2uSQ2mvDqRu6taJ3XbAu-_wcc8MCzabxcg3GBScCX6YyOY28OpgQFF7woab55b7Nfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش فایننشال‌تایمز از حق قانونی ایران در تنگۀ هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/680932" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1dcfc4caa.mp4?token=Oh6I33KofQ9SfwKOEbTldWmbfTUwutwYbjmIg4izwGOKfd8QoJyyUG1Wo9FTtQZV-2p7WSIyyRusIDIjaDTdapokLvE1hy6SiwjJqxf4PpuNTwni4RkC5_xSGP6f6MOv8SPwPDV4FYuCQkTSkKXQARdTuwfXYEzD9n1Npr9pgZvRFnZr94TE-8bNvdOJrkyqxGiQZG_0VzHvlPV7UPtkIpq1D1ubI3OiePXocYJX_0ie0z2xEmyzUMA1N6lJrsrrDe1quIBuwjrSjb44z8Zi2-sTe7k-VfW7YbwWUzDCzLc3wjaA1k1RRFvIbcvgM7GwGznz3C5PMbK8nSCj8EUfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1dcfc4caa.mp4?token=Oh6I33KofQ9SfwKOEbTldWmbfTUwutwYbjmIg4izwGOKfd8QoJyyUG1Wo9FTtQZV-2p7WSIyyRusIDIjaDTdapokLvE1hy6SiwjJqxf4PpuNTwni4RkC5_xSGP6f6MOv8SPwPDV4FYuCQkTSkKXQARdTuwfXYEzD9n1Npr9pgZvRFnZr94TE-8bNvdOJrkyqxGiQZG_0VzHvlPV7UPtkIpq1D1ubI3OiePXocYJX_0ie0z2xEmyzUMA1N6lJrsrrDe1quIBuwjrSjb44z8Zi2-sTe7k-VfW7YbwWUzDCzLc3wjaA1k1RRFvIbcvgM7GwGznz3C5PMbK8nSCj8EUfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشیدگرفتی از فضا به شکل عجیب دیده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/680931" target="_blank">📅 21:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde608c1ad.mp4?token=qB5W9uo9LT-bp3dg_cdnrLiF03DDWYggdsad5RN9URB1f5QEUib7ut4AUbseZ1G2Bxsg-ma3NBh3Bkaz8yTcJOUTr_O7y9yEiTxDqnR_OptrsZtprX6XWk24EsaF0FajA_XjN5i9BfybcW84gsSQTRxHBYakkim3G1BX0ejwbnfnL-qxgdQiEdKojPYWMmtQ1dCol1eGuCvxdtswXIljD0dl31h9Xukk5ySpyPeTr_S_OJzeTSXV8LtxiZP_HMBpRBK6oqY9vngfALTRfUjVqYdEykFIVxiSDEWAp_eQYAnknqgmIrDi6LlOcTZo0Hi96Ir2Z6e_I5_kBuiaCUyrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde608c1ad.mp4?token=qB5W9uo9LT-bp3dg_cdnrLiF03DDWYggdsad5RN9URB1f5QEUib7ut4AUbseZ1G2Bxsg-ma3NBh3Bkaz8yTcJOUTr_O7y9yEiTxDqnR_OptrsZtprX6XWk24EsaF0FajA_XjN5i9BfybcW84gsSQTRxHBYakkim3G1BX0ejwbnfnL-qxgdQiEdKojPYWMmtQ1dCol1eGuCvxdtswXIljD0dl31h9Xukk5ySpyPeTr_S_OJzeTSXV8LtxiZP_HMBpRBK6oqY9vngfALTRfUjVqYdEykFIVxiSDEWAp_eQYAnknqgmIrDi6LlOcTZo0Hi96Ir2Z6e_I5_kBuiaCUyrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیوار چیدن راحت بدون احتیاج به مصالح و مواد خاصی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/680930" target="_blank">📅 21:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=A_5_wFRJSxizRN0f4Pzq50GueujyJM-6jHxU0VzF81I9NHvaljvdABzgPF6HTdSXo7EbmaRAzFQyEOS2vF-E_ifpViiUC3qOizU9a5Xx6n3fxhbyMqTUyFIYEwFQUrLYL4FNr0wI17h7bLH_3049R4v5ANrhRec9J1hYUOE2AMOHUZ0Gimztspe_-T_DoBAI6fhtRuxXuNMx9r8KJq3tlZp1XgchZZNY-GVAaZQcR-Vi0XoiCkfodqOiduCiLjAAD-eKuBBsksh_qARBB6u-WHsiOmITS5DQRbPqFpw1j3AIKyQe4-Ea59xbAfY59E2MBdw6D7aaX60ce2C__3qYKz-aTWtubCEtKk-97VqIpGXMljToapWKxarZaPj5Po4zJ2t11XlVS6gRI47X9wKidKhgojPI430UTMZ-tMdkDMQi62dUDssT8XDtsKldoQXJ0rptZsLv9V3iT7__Yane_1YvE2sIsWSRZSZIW0sXkZV0DJ8su-En0YCW2pQDhQFg2BHepGn_DXuM7yS_L7R_h831c9RYD7hXrYFpy7-foX0gALEEL_r0LVhzbvvC_Wo05xp5kD1FFfvfV8xb8XH0RcqefGHLBGBTwwnVUjmGtFyiycKa_95ISF3wnRck6X8tMSpdfSNCSqwjzlFqf8C84bkHmzriuC0zj58aJ-LQfFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=A_5_wFRJSxizRN0f4Pzq50GueujyJM-6jHxU0VzF81I9NHvaljvdABzgPF6HTdSXo7EbmaRAzFQyEOS2vF-E_ifpViiUC3qOizU9a5Xx6n3fxhbyMqTUyFIYEwFQUrLYL4FNr0wI17h7bLH_3049R4v5ANrhRec9J1hYUOE2AMOHUZ0Gimztspe_-T_DoBAI6fhtRuxXuNMx9r8KJq3tlZp1XgchZZNY-GVAaZQcR-Vi0XoiCkfodqOiduCiLjAAD-eKuBBsksh_qARBB6u-WHsiOmITS5DQRbPqFpw1j3AIKyQe4-Ea59xbAfY59E2MBdw6D7aaX60ce2C__3qYKz-aTWtubCEtKk-97VqIpGXMljToapWKxarZaPj5Po4zJ2t11XlVS6gRI47X9wKidKhgojPI430UTMZ-tMdkDMQi62dUDssT8XDtsKldoQXJ0rptZsLv9V3iT7__Yane_1YvE2sIsWSRZSZIW0sXkZV0DJ8su-En0YCW2pQDhQFg2BHepGn_DXuM7yS_L7R_h831c9RYD7hXrYFpy7-foX0gALEEL_r0LVhzbvvC_Wo05xp5kD1FFfvfV8xb8XH0RcqefGHLBGBTwwnVUjmGtFyiycKa_95ISF3wnRck6X8tMSpdfSNCSqwjzlFqf8C84bkHmzriuC0zj58aJ-LQfFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی منتشرنشده از دیدارهای صمیمانۀ خانواده‌های شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/680929" target="_blank">📅 20:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680928">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اوباش صهیونیست قرآن را پاره و به آن اهانت‌ کردند
🔹
شهرک‌نشینان صهیونیست عصر امروز حین حمله و تخریب یکی از خانه‌ها در منطقه «بیر قوزا»، در شهرک «بیتا»، واقع در جنوب نابلس، قرآن کریم را پاره کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/680928" target="_blank">📅 20:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxEdaFlPCDzHspoMSgCnhthnpH_F1_yLTu216gbmF3z8EDRV7OiQ1ElQDz16cMhRq2LS5tDaIRFUE9uVhHrfja5mtMCv7pIfZOKYRDP6QtPMSIH7_EES95mXNN1Ez4bKLLpN8jRFhMjXX0doRyJEwOBaPoOwKirUGhpHNOpAZkIqPJRsFPvGbWCwSSyEoEZj_KsEK0INxlQZj32KJcv-B38SXW56ROhSMXL_gZaTKz90hL2ZmmTSJasFaci5Hf1BcYubxnfCHNqKF5SXeG79agZD7KZ6JyLsibmdHGXo2waMXPBR6YyfjHSezpfFumDF8WukR9PghcNpiseO2rbCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6YUtMZNMJYnlQtm62XjYzRFaXcwfW0qxF25Id3bDBQ1Z2PY5OxbNfu5UoIF1nkrlYBC-clfn1RppLElQ_x7EGY2jx6-WzYKTC6rx0VRvbKg6FSX0WNMjDLJ0yEPq6EctcU5f5pSzsqZyHRjnacQjiOBUmmzpJ486zalMU4pMJwHvSt9qNWJFm-fBMO1WRmhtTXdwc4cc1JDNa-62cvnQm0NHZI0Z0qCEd-1e6YGKfHty1P9DbyceXbI_ghuTlR_rylUDQ8_lsACzCo_v64mqdN7j7xo4ZXlDHGDysQmnw_3mdlYQQZx7cu6BFIwnRhH5mBc778Wsb5LBIpPVS6XAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه به مناسبت سالروز تصویب معاهدات چهارگانه ژنو ۱۹۴۹ درباره حقوق جنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/680926" target="_blank">📅 20:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded454043a.mp4?token=ALkOm8IpPq79JoFHvYVHrdr3SdchdHU5h_xnxXESb9U4D3XgXerGGx6mWGRhOVE076coGr_hcQyaouMZ2xPThxv1pKopwSAFcqUJe4g_q0OfX-9vGRn3nbXoAoPL8b01M_uY4jjtL0wNGRqeTZm4LWriWVFeg4gq1fWI2VEl6ux5YUgn4EbdIz3za74pKZGqKYK7mHenmEN1NE_TUvnr0P0s2on0PxQecMR2rE0Nas73E9qoFXqOHHaNzUOu8GmOmCPL2HIZFu9LyjwNbuoGGCuNC1OrT7vE7yyPmuDrFtTtWXHdzilRruSzZzEZTiMeTAVTOR0uXIOre5nDDCba-2EF2xR7YVkCb2EqBtysVpycr16di-1r_7S-mcp6x2uJivMv6vDPcL2R7YjQ1FEQQEL8nXM4d2BMKfavlUvK2ToT183CCyGTmxF6T0CGQjrHNKBLC2_wgkUyCULL-CJKnRN_YcVNH_8gGXq8tXKXiQNxdaPxy92bvizg11Zs9QOtuTcZYWg9lJF_7ZsJWZ-YXRP3qofR8MLBYXjJ9Q589WGsS8Fgo03451qtqGKJtZh08NNbj7cXc3L_3uACs6mGJVIfJFCLBTQEJO2WAZdwunoMp0yGHS8CDaIrr0_SwDBpS2--9c8brfjqaqsgoePUp3YhzJUMjXmVkQmcIemh8ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded454043a.mp4?token=ALkOm8IpPq79JoFHvYVHrdr3SdchdHU5h_xnxXESb9U4D3XgXerGGx6mWGRhOVE076coGr_hcQyaouMZ2xPThxv1pKopwSAFcqUJe4g_q0OfX-9vGRn3nbXoAoPL8b01M_uY4jjtL0wNGRqeTZm4LWriWVFeg4gq1fWI2VEl6ux5YUgn4EbdIz3za74pKZGqKYK7mHenmEN1NE_TUvnr0P0s2on0PxQecMR2rE0Nas73E9qoFXqOHHaNzUOu8GmOmCPL2HIZFu9LyjwNbuoGGCuNC1OrT7vE7yyPmuDrFtTtWXHdzilRruSzZzEZTiMeTAVTOR0uXIOre5nDDCba-2EF2xR7YVkCb2EqBtysVpycr16di-1r_7S-mcp6x2uJivMv6vDPcL2R7YjQ1FEQQEL8nXM4d2BMKfavlUvK2ToT183CCyGTmxF6T0CGQjrHNKBLC2_wgkUyCULL-CJKnRN_YcVNH_8gGXq8tXKXiQNxdaPxy92bvizg11Zs9QOtuTcZYWg9lJF_7ZsJWZ-YXRP3qofR8MLBYXjJ9Q589WGsS8Fgo03451qtqGKJtZh08NNbj7cXc3L_3uACs6mGJVIfJFCLBTQEJO2WAZdwunoMp0yGHS8CDaIrr0_SwDBpS2--9c8brfjqaqsgoePUp3YhzJUMjXmVkQmcIemh8ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار وحشیانه پلیس آمریکا با دختر ۱۸ ساله‌ای که به دلیل تخلف رانندگی دستگیر شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/680925" target="_blank">📅 20:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgxqR4vgd-cxQMU6vZBkmQyAK1M7A5dBN9k2xx_Kpp7znwAXJgu613JN_mRR6_OM4iYpkOv08F7EaN9vJ2Nfh_uHFCiotPLU0bWVzhFMh_kZDHxOglUHXQCIKiHZewQp8H_SpgwtrJP45g8LHl4DymVQsedyWDZ_deugcqYbJmgLLI0Wab4xo5KnLvD2QZ32BzqvQcsFzbFFcCbC9koIXvgAtGQxYOwCRnvV6CrQjDHxTtboml125gYHxMKTI49M_4-Mfz2CiVj_L1_ndivlGdKumBNduzLoB-982MnI6ZHXIwJndUOp4dpMknT7MNLyqFLVnMKiQCyR4UuQOI4lDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش CNN از وضعیت بحرانی سربازان ارتش آمریکا در ناو آبراهام لینکلن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/680924" target="_blank">📅 20:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlvoIjX5M89bzqulgqx6FmYE5UssUDGga1fmtn83758YDVfyJHUsPwRLf0xr8rGlx3mToyI1CVzRUzWEneS-rlj8CmAkqsejhfxE-tzAsQAhyf0xKXaWhL4Uvgf_tMvR1P4sLzMFrX6nsJNkx452-D6DyS5AudUzHqVidAzoDITZ_9EWlM6krXGr5WMkHcf2BJUHaxTVEt3sf6W3r0_f6XBovqIdbxFplxfyhNqrOVlyRKPKGUlit-FhTiOuwgcKhpLF1KSikC3EoxxQ-tkIIg85rxx9dNGHv9eQ2Ev6ZicUUUh97SO_MXIMKP3emr519L3SpM8EyU1ZaUIFMusNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وحدت و انسجام، مسیر عزت و استقلال ملت ایران است
آیت‌الله مروی در مراسم خطبه‌خوانی شهادت امام رضا(ع):
🔹
وحدت، اتحاد و اعتماد به دست‌اندرکاران کشور، مسیر عزت، عظمت، شکوه و استقلال ملت ایران است.
🔹
ایجاد یأس، بدبینی و شبهه در ذهن مردم، جز خدمت به دشمن هیچ اثری ندارد؛ همان‌گونه که بزک کردن و بی‌خطر نشان دادن دشمن نیز مردود است.
🔹
ملت ایران در برابر سختی‌ها و جنایات دشمن نه‌تنها متزلزل نشدند، بلکه عزم و استقامتش بیشتر شد.
🔹
زائر امام رضا(ع) باید با افزایش معرفت و تبعیت از آموزه‌های حضرت، زیارت را به فرصتی برای اصلاح و تطبیق زندگی خود با سیره امام تبدیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/680923" target="_blank">📅 20:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حملات توپخانه‌ای عربستان به شمال یمن
🔹
خبرگزاری رسمی یمن (سبأ) گزارش داد در این حملات، روستاهای واقع در منطقه مرزی «غمر» در غرب استان «صعده» هدف قرار گرفته است، هنوز خبری از تلفات یا خسارات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/680922" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
چشم‌پوشی نماینده فرانسه بر محاصره ظالمانه یمن و هیاهو برای امنیت کشتی‌های غربی
نماینده فرانسه در نشست شورای امنیت سازمان ملل با موضوع یمن:
🔹
ایران با حمایت در این بحران و نادیده گرفتن تعهدات خود در چارچوب تحریم تسلیحاتی تعیین‌شده در قطعنامه ۲۲۱۶، به تداوم این وضعیت کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/680921" target="_blank">📅 20:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680917">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2cb0d8e4.mp4?token=FIWdnu9GaIG_omq1gajsRSysDkrN1tD6cUEmoq0tKRe5kk7nCLG4CSxSnH-78hlBCZblONzwrCwAFZb-W2gBgsz0FIaAU0_1W3rXyWrvPFyIVCYxQDHWJk-bwT9RBf1q47QUE-1g6d-Jy0KDAhJbVJLb_llIHQ3p8u-IgCJ9EDAU8SJZd84QFCFvxKiRhz_kCWSDxBdGnJUd03_rkoYU5-kMX4-zMYyXpkbJGwNORN8KnsxQ55lLxYE8nffdraTdPpaqHEDQ7wJ3-9wH84r-Ro6EXD3Y52hFVZOdnAV8kPoiaf7RNLmeiY1PTx-n0rFUBBaJnD9mFfhcwA7NAhaCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2cb0d8e4.mp4?token=FIWdnu9GaIG_omq1gajsRSysDkrN1tD6cUEmoq0tKRe5kk7nCLG4CSxSnH-78hlBCZblONzwrCwAFZb-W2gBgsz0FIaAU0_1W3rXyWrvPFyIVCYxQDHWJk-bwT9RBf1q47QUE-1g6d-Jy0KDAhJbVJLb_llIHQ3p8u-IgCJ9EDAU8SJZd84QFCFvxKiRhz_kCWSDxBdGnJUd03_rkoYU5-kMX4-zMYyXpkbJGwNORN8KnsxQ55lLxYE8nffdraTdPpaqHEDQ7wJ3-9wH84r-Ro6EXD3Y52hFVZOdnAV8kPoiaf7RNLmeiY1PTx-n0rFUBBaJnD9mFfhcwA7NAhaCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
🥀
شب جمعه است هوایت نکنم میمیرم..
کلیپ های شب جمعه شب زیارتی امام حسین (ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/680917" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680916">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شهادت ماندگار است
🔹
رهبر شهید انقلاب درباره شهادت اینگونه بیان می کنند که خاصیّت شهادت، خاصیّت فداکاری در راه خدا این است که به طور طبیعی ماندنی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/680916" target="_blank">📅 20:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680915">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
احضار فرماندهان نظامی به پارلمان عراق در ارتباط با حملات به مقرهای حشدشعبی
🔹
کمیسیون تحقیق وابسته به پارلمان عراق شماری از فرماندهان و مسئولان امنیتی و نظامی را برای بررسی علت تخلیه نشدن مقرهای حشد شعبی پیش از حمله به این مقرها، احضار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/680915" target="_blank">📅 20:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680914">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjkERJFNtYS8fif_9uY_SMYN4d4iCDmy8eV73wuIXBl0S4MJA66T5YWSzALUQRwOOGDAshMk_W_b2NhvRumO4yX03cDYdk5I4EQCss-MW1onWRj8VCWgqs9Wz1wLdQ6RygSdzq9ycR5U2TMjxQYQGgcQIos1GmLxFWzyKhCe936SRC-HO8eMjTX97uvGoLQtSnErGK0zsJfw0mXjo5iYHlJ9Y5eRiWd4lK7SKTJuiXR3CYMEP0_Jiore0t4nUveQFHaEE3k7G5vOFqxGrs9j-TvrOTWakRBF8I8Jbl8Dtm2MvLskAhuevNNb89vPYMXjfrIKuEDa7zyxuaWbvAOjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌲
کلینیک دندان پزشکی سرو
🌲
👀
اگه فقط ۲ دقیقه وقت بذاری، شاید نظرت درباره کامپوزیت کاملاً عوض بشه!
🦷
✨
🦷
اینجا جاییه که سال‌هاست لبخندهای زیبا و موندگار ساخته می‌شن…
⁉️
چرا سرو انتخاب هزاران زیباجوست؟
🌟
تخصص و تجربه حرفه‌ای تیم سرو با سال‌ها تجربه و تجهیزات مدرن، بهترین نتایج در لمینت، کامپوزیت و ایمپلنت را ارائه می‌دهد
✔️
🌍
کلینیک سرو به عنوان بزرگ‌ترین مرکز تخصصی کامپوزیت و لمینت و ایمپلنت در خاورمیانه با بیش از  10شعبه فعال در ایران
🤩
🦷
✅
اقساط بلندمدت بدون سود و ضامن
✅
۱۰سال گارانتی بدون قید و شرط
✨
✅
سال پالیش رایگان
✨
💎
اگر به فکر کامپوزیت دندونتون هستید  و به هر دلیلی هنوز شرایطش رو نداشتید ،همین الان میتونید از شرایط ویژه (اقساط بلندمدت)
🌲
سرو
🌲
استفاده بکنید
💯
✅
📞
مشاوره و تعیین وقت:09337830160
📞
ارتباط با ادمین:
@mahya_sarvcip
پیج اینستگرام:sarvcip
برای دیدن نمونه کارهای بیشتروارد
👇🏻
شوید
✨
https://t.me/sarvcip_cllinic</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/680914" target="_blank">📅 20:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680913">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/680913" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ایران: بیانیه حقوق بشری فرانسه و شرکای غربی، فرافکنی منافقانه است
🔹
سرپرست اداره کل حقوق بشر وزارت امور خارجه اقدام فرانسه و تعدادی از کشورهای غربی در صدور بیانیه مشترک علیه جمهوری اسلامی ایران به بهانه حقوق بشر را محکوم کرد و آن را مصداق واضح فرافکنی منافقانه دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/680908" target="_blank">📅 19:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1c3df4c24.mp4?token=BjxoczEG2pApkk7ru9rmqxJjVX76wKvdat5o7ISI5FdkMOrKaO1zOrol7gZljbV77gsQooQ8ne9awMRz5rjQzTEaNbJzcJ-kXZgPg2b9YB-zGAymmUjdkqQDDdPL3jMoy_HKMl8WaNU6PPrxXD_86UZlb4tbK2D8BWsEshWQtZzTMVYJRRlKkY_E2oCDSWp6zssTsZ55kl5ZSx0K1VBe8Agdnmm3-5xBbE1nrZjKY1ItKIAFBe_R84AQCqA8IMrVevD1SSDw-J6EEFPNxzgyOFPUtlTAuwq-k8kMKxGDE4QsMTD23BN3c-wf5-rmSdR0Uyq5oE2K2PJ9yZXquIkAtxVnsQ0nuvnAzan-G_5UdTLnnXW6vYz5AZrmir0xTQ6vk9EbwUZ0Xsw1E0jxkjLxyndA_PbS3CK6YqlR5ZRzSuo8DRcCikdejfoPs8dtCdvXAggmzQen9g3Of1M5bJXBHM-xOM_peVWdsgwtw1TonY67F796iliWrMzXMxPtDcWWWlBULkfBD12g03LnbWI_SEiXDd6Qs0TjZJWRqWHYzSy0m8Ja5KhlA8vV2NZTuNXULApruYKtiw1yK9-wSsN3mjv7qUW4Jeih5ykONpgzcjDS0l1E7EHrzo14VT43N_qyXoyvCY9aIc2g0DzJ1LIjaP1Ft67BnpAP0NGWt5b5fLo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1c3df4c24.mp4?token=BjxoczEG2pApkk7ru9rmqxJjVX76wKvdat5o7ISI5FdkMOrKaO1zOrol7gZljbV77gsQooQ8ne9awMRz5rjQzTEaNbJzcJ-kXZgPg2b9YB-zGAymmUjdkqQDDdPL3jMoy_HKMl8WaNU6PPrxXD_86UZlb4tbK2D8BWsEshWQtZzTMVYJRRlKkY_E2oCDSWp6zssTsZ55kl5ZSx0K1VBe8Agdnmm3-5xBbE1nrZjKY1ItKIAFBe_R84AQCqA8IMrVevD1SSDw-J6EEFPNxzgyOFPUtlTAuwq-k8kMKxGDE4QsMTD23BN3c-wf5-rmSdR0Uyq5oE2K2PJ9yZXquIkAtxVnsQ0nuvnAzan-G_5UdTLnnXW6vYz5AZrmir0xTQ6vk9EbwUZ0Xsw1E0jxkjLxyndA_PbS3CK6YqlR5ZRzSuo8DRcCikdejfoPs8dtCdvXAggmzQen9g3Of1M5bJXBHM-xOM_peVWdsgwtw1TonY67F796iliWrMzXMxPtDcWWWlBULkfBD12g03LnbWI_SEiXDd6Qs0TjZJWRqWHYzSy0m8Ja5KhlA8vV2NZTuNXULApruYKtiw1yK9-wSsN3mjv7qUW4Jeih5ykONpgzcjDS0l1E7EHrzo14VT43N_qyXoyvCY9aIc2g0DzJ1LIjaP1Ft67BnpAP0NGWt5b5fLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد ایران برای کریدور مالی مستقل بریکس
🔹
رئیس‌ کل بانک مرکزی جمهوری اسلامی ایران در دومین روز نشست‌های مالی بریکس در هند بر ضرورت ایجاد کریدور مالی اختصاصی بریکس و اتصال شبکه‌های پرداخت ملی کشورهای عضو تأکید کرد.
🔹
وی گفت توسعه همکاری‌های مالی بریکس باید از گفت‌وگوهای کلی فراتر رفته و به ایجاد زیرساخت‌های عملیاتی، امن و پایدار برای پرداخت‌ها و تسویه‌های فرامرزی منجر شود.
🔹
به گفته عبدالناصر همتی، رئیس‌کل بانک مرکزی، اتصال شبکه‌های پرداخت و گسترش استفاده از ارزهای ملی، ضمن کاهش وابستگی به مسیرهای مالی خارج از بریکس، به افزایش سرعت، کاهش هزینه‌ها و ارتقای امنیت مبادلات تجاری اعضا کمک می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/680907" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">امیدواریم با غروب خورشید ماه صفر، هرآنچه قلب نازنینتان را می‌آزارد غروب کند و شادی ربیع بر شما طلوع کند و هرگز پایانی بر آن نباشد
🌸
🌸
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/680905" target="_blank">📅 19:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ4jlzq1Ps-VSLpYsU2ZQlU7XBaDCQ2FvIErJTcZhluFWj3p7w17UHcnBBxRuoz1Re3xz3uT5GLjti5_qbiK4RpMFE6WZQfMy1LiKARrSH2HkZsx_GOz05K15dPr8W8VmN7myuRwiy_i6ps2TvpDaawpOMjRKBXVL1uHPfG8xxBDqecDFdHgL0kgd0u7Csq3ecbjNg8SRqdZ56HMHVSYu1kZT73kBZwtq3W6t3fqHrENKf1pUQbplKc-UEqles3L4MG4acf2iuDpXzCPGP2ZKaOavkTGHOy-QZHWtxrZNPRF6lqWQJoG9h7sBFLesW8pAZCGij4tesRBuuNxadJjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اجازه مادر سادات رخت عزای پسرش را
نه از جان بلکه از تن در می‌آوریم و می‌گوییم
ای حسین داغ تو تا ابد در سینه ما خواهد ماند...
🔹
حلولِ ماهِ ربیع الاول ماهِ شادی و شادمانیِ اهل بيت(ع) را تبریک عرض می‌نماییم
🌸
🌸
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/680904" target="_blank">📅 19:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj-lHJ_Hz2ADq44wSLH4LYoULScrToAOIIu9SRPiF2_KUnXiC9sMDS63Al3WHnCyQP3LyekOXRi0gkRBCODSGJOd-t_ClCzPmrw8F1js2a99gB_eSDCPq2Cu80brATTRyHbHzU5eZcT58BfEe2WQ17ylQeZLW1ek4hxNfHWN2ahFX3rzh4HsIH9vuQFhtA7PAkEQLFMnT0wXuO19rux6-Adxq4elSRlusFbHSZ6wJ8f1WRCFNL90Q6ABz-Ng3ypved949NSyjEQ9tLtWL-j6s3xMRZ9kxbcNKGXGAvnTHS4HsnezkvwYejVtJTXtCm6MmoXg5aY3k8H2fFG7KRPndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام پس از یک دهه لوگوتایپ خود را تغییر داد
🔹
به گفته «آدام موسری»، مدیر اینستاگرام، این تغییر با هدف مدرن‌تر و ساده‌تر شدن هویت بصری برند و درعین‌حال حفظ ارتباط آن با طراحی اولیه انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/680903" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پولیتیکو: جنگ ایران می‌تواند ضربه‌ای بزرگ به اعتبار آمریکا باشد
پولیتیکو:
🔹
پیامدهای جنگ ایران می‌تواند بسیار فراتر از خاورمیانه باشد، به‌ویژه اگر تنگه هرمز درگیر بحران شود، اقتصاد جهانی با شوکی جدی روبه‌رو خواهد شد.
🔹
در شرایطی که نفوذ جهانی آمریکا کاهش یافته و چین در حال قدرت‌گرفتن است، تردیدهای مداوم دولت ترامپ درباره ایران می‌تواند به اعتبار واشنگتن آسیب بیشتری بزند.
🔹
تیم ترامپ در محاسبات خود درباره ایران دچار یک خطای اساسی شده؛ آنها تصور کرده‌اند فشار بیشتر می‌تواند به فروپاشی حکومت ایران منجر شود، اما آن حکومت فرو نخواهد پاشید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/680902" target="_blank">📅 19:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966d0062d6.mp4?token=B-89VCfQvOOp3V5IAFBM-nW9rWo3QWUc6FQ_2tegRjdRve0uqV3KyzLcvinNP84LrgXeVt4qms5otCBEHuls1tHGSVI_YS-zaYMxgJlEMzyC1p4ioMULdInSlfvcc06QhtoRfXThoUF48EqJfl4ceRVk2shOwPTP3qd32M_sA-u2n6ztmTMrMa4TIyr4FjecvBd63it4wMUtl0r8PHJyp7C08LvlVDa7IaAYgLYXlJ4Z8WyULsdxBEwv7DgV7ej48duZXxTMfBp4vjzae36KS3tvVydZoySU-ubN5C3kLuVHj39-aXmr5kvXo497twR57qcXvZxZ2TT2u9sr7ru86Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966d0062d6.mp4?token=B-89VCfQvOOp3V5IAFBM-nW9rWo3QWUc6FQ_2tegRjdRve0uqV3KyzLcvinNP84LrgXeVt4qms5otCBEHuls1tHGSVI_YS-zaYMxgJlEMzyC1p4ioMULdInSlfvcc06QhtoRfXThoUF48EqJfl4ceRVk2shOwPTP3qd32M_sA-u2n6ztmTMrMa4TIyr4FjecvBd63it4wMUtl0r8PHJyp7C08LvlVDa7IaAYgLYXlJ4Z8WyULsdxBEwv7DgV7ej48duZXxTMfBp4vjzae36KS3tvVydZoySU-ubN5C3kLuVHj39-aXmr5kvXo497twR57qcXvZxZ2TT2u9sr7ru86Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها پادشاه ایران که اجازه نداد به او بگویند قبله‌ عالم یا سلطان!
ادامه‌ی ویدیو
👇
https://youtu.be/IPmkJyaMkF4?si=f58hxCuT9iH8RCT2
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/680901" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سناریو دولت برای بنزین چیست؛ با قیمت نجومی مواجه خواهیم شد؟
🔹
یک اقتصاددان می‌گوید: با توجه به شرایطی که بعد از جنگ ۴۰ روزه ایجاد شده، بنابر اعلام دولت، تغییر در میزان سهمیه و حتی قیمت بنزین امری اجتناب‌ناپذیر است.
مشروح گفتگوی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237426</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/680900" target="_blank">📅 19:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
‏
یونیوز: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه استراتژیک در صورت مداخله در لبنان تهدید کرد
رسانه لبنانی:
🔹
تهران با آگاه‌سازی پایتخت‌های منطقه‌ای (آنکارا، بغداد، دوحه و ریاض) اعلام کرد در صورت انجام هرگونه ماجراجویی نظامی سوریه در لبنان، یک رویارویی منطقه‌ای گسترده در جغرافیای سوریه شکل خواهد گرفت و پاسخ موشکی ایران شامل هدف قرار دادن بیش از ۱٠٠ هدف استراتژیک از جمله کاخ ریاست جمهوری سوریه خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/680899" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اوضاع در ناو آبراهام لینکلن قاراشمیش شد!
🔹
همزمان با حملات هوایی جنگنده‌ها به ایران از ناو هواپیمابر یو اس اس آبراهام لینکلن که اکنون در خاورمیانه فعالیت می‌کند، خانواده‌های نظامی به MS NOW گزارش می‌دهند که ۵۰۰۰ خدمه این ناو از کمبود آذوقه رنج می‌برند.
🔹
این…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/680898" target="_blank">📅 19:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c0f75f54.mp4?token=V0TSC4n5VYGfxpHkYZTKAk_CO-_IH4fhqxH_qkPn9CQgsKqmRsRPRBF1pgnZyDInA4viww8Vo6XPPyQ2bBniDE21hMCTn-L9J6tTSxfn-XBr2Iv423wFRmymOnjpqQPe70yrcsrEtYBU_Dnt8aub5Ql-gdSBudt1cOX3zNlxEjvnnjTshMVi-vPy_PmKciFwxcrbc3lD39j1c9Oi9YlR9UdnM-nCrRFvAPrc7SXlg2R9LNy7j9OkEKfJAalU_P-YGEXbg_S6DS7Bd8UNtkruGdW3MHQN-_m_Y4ea-wwszcTrk8OTTQQTEazQd3RcCcuqVumBlqkitEjgJ-hs5v3elw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c0f75f54.mp4?token=V0TSC4n5VYGfxpHkYZTKAk_CO-_IH4fhqxH_qkPn9CQgsKqmRsRPRBF1pgnZyDInA4viww8Vo6XPPyQ2bBniDE21hMCTn-L9J6tTSxfn-XBr2Iv423wFRmymOnjpqQPe70yrcsrEtYBU_Dnt8aub5Ql-gdSBudt1cOX3zNlxEjvnnjTshMVi-vPy_PmKciFwxcrbc3lD39j1c9Oi9YlR9UdnM-nCrRFvAPrc7SXlg2R9LNy7j9OkEKfJAalU_P-YGEXbg_S6DS7Bd8UNtkruGdW3MHQN-_m_Y4ea-wwszcTrk8OTTQQTEazQd3RcCcuqVumBlqkitEjgJ-hs5v3elw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلکسیونی از خاطرات و نوستالژی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/680897" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اطلاعاتی ناامیدکننده از بارورسازی ابرها در ایران
احد وظیفه، رئیس مرکز ملی اقلیم و مدیریت بحران خشکسالی سازمان هوش‌شناسی، در
#گفت‌وگو
با خبرفوری:
🔹
بارورسازی ابرها یک فناوری قدیمی با دو دیدگاه متضاد است.
🔹
شرکت‌های پیمانکار مدعی تأثیر ۱۰ تا ۲۰ درصدی هستند، اما جامعه علمی و آکادمیک این نتایج را مردود می‌داند.
🔹
بررسی‌های دقیق در آمریکا تأثیر واقعی را تنها حدود ۲ درصد نشان داده که از نظر اقتصادی به‌صرفه نیست.
🔹
اسرائیل نیز پس از دهه‌ها آزمایش، این پروژه‌ها را تعطیل کرد و به سراغ شیرین‌سازی آب رفت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680896" target="_blank">📅 19:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رسانه یمنی: پالایشگاه آرامکو در جیزان هدف حمله پهپادی ارتش یمن قرار گرفت
🔹
خبرگزاری سبأ یمن گزارش داد نیروهای مسلح یمن در تازه‌ترین عملیات نظامی خود، تأسیسات استراتژیک نفتی عربستان سعودی در منطقه جیزان را هدف قرار دادند
🔹
ارتش یمن با استفاده از دو فروند پهپاد، پالایشگاه شرکت آرامکو در منطقه جیزان را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/680895" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd281a894.mp4?token=cN3cR1ul7w0HG_ZGi7vQsutgil1m8or-Z9pyjuranRot6QbZ1okOWJAmUCsmNoXwlrTphZfUiUM-x1y_CW_BJ0y5tZ-FMqfTq9XZipmudrMX8liPBMrYiT04d6tWogEysvok0aJq7jAZjW9-YKqUxDFtUj5Z4kccWLrOu0xMlgHUFtAtqQP3TBUwHbkPVmKdU92dbR9AaLy5w9LqgcDy2Qv4KCjc5ngLmhWrqtDJuZyuaeIgA0zwG6ioqsRH-XWVFAK5PPQ6CxdbIRF7kz4sUcjSlXLeyei2iIdqtkJaVFPwN_oHnv2YJbkH8t-RS9IMieEskvzLq92ol7wkEjb01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd281a894.mp4?token=cN3cR1ul7w0HG_ZGi7vQsutgil1m8or-Z9pyjuranRot6QbZ1okOWJAmUCsmNoXwlrTphZfUiUM-x1y_CW_BJ0y5tZ-FMqfTq9XZipmudrMX8liPBMrYiT04d6tWogEysvok0aJq7jAZjW9-YKqUxDFtUj5Z4kccWLrOu0xMlgHUFtAtqQP3TBUwHbkPVmKdU92dbR9AaLy5w9LqgcDy2Qv4KCjc5ngLmhWrqtDJuZyuaeIgA0zwG6ioqsRH-XWVFAK5PPQ6CxdbIRF7kz4sUcjSlXLeyei2iIdqtkJaVFPwN_oHnv2YJbkH8t-RS9IMieEskvzLq92ol7wkEjb01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب گسترده خانه‌ها و زیرساخت‌های مسکونی در جنوب لبنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/680894" target="_blank">📅 18:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFqKPGjSK7_pRViJIG7r17ETSUQxQHX0FxtMkIwKcN9GgX1btja_AMh_W10mnxrCpfSQmcyAHY2Pf0y1Rip1cPDfsQQ9149L6u-YXJ1KKS2MOP67p7nSk2wmsnQ-53J2y6AP7M93zXcVM2bUrgDNgfRbcJBRi7BDIl5dh4gXmTGALPVB6hHHg2VNdfaQcZugnJnzDVj7Q2ANXC27w7YjsObl1aB_yAXXrwXvlwUDfujeqvOg1jYs-EA1g6Ze4XYQQh3cICMw2keNkrJyW6yF_HghM1V5V5-ZV8OaDyR491TumJaCCkaxf2eyQXJ4IzLUEOc1MHAW8AJIlAIx2KR-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد شرکت‌ها و محصولات نانوفناوری در ایران
🔹
بیشترین تعداد شرکت‌های فعال در حوزه فناوری نانو به بخش‌های عمران و ساختمان با ۶۸ شرکت  و سپس نساجی و پوشاک با ۴۱ شرکت تعلق دارد.
🔹
از طرفی دیگر، حوزه‌هایی مانند «انرژی‌های تجدیدپذیر» و «ورزش و سرگرمی» با وجود پتانسیل بالا، همچنان در ابتدای مسیر توسعه شرکت‌ها و محصولات نانویی قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680893" target="_blank">📅 18:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOsf4tmatH6q1egD_S9i61kGEXXRDIv7pvd834Hg-yFdMV-bYswQthuDieZ8tXfCGPXEMFkOI6HyHCA5puPjrlFzV6kBTvygLNoBGwVwKOsNzs8nPjngdnO987NsyulL2rGkz7u4DbyOqWaUjKcIe3MEzMf4pshTXQC_rU4AVH-mg90jwNuye5J97fSz7uNL417gxjPyfCl86W1fgTZroc0G7HMX3znU6VkopQvc5Lc091PIHKX2GRx6F9bbQ2WLSDjNIAYrXPWPDEQkNgYBM4yZh2MPSkbx5JFf3pCdpcN7CAxOO8C2PSepQAU5ZJ9uZYHD6gqiu1YpN291xtfO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41fc106a5.mp4?token=DRIyPbPDMoWsPHxnqgOV37t0HEIISoowCLw1DTUxzIvgMP-5_ADM9gIK1CjPvqqqdZ_pZQv9Y-bIwhw8aSMaLFGofrtKR2RSh-6DYxUbRszM8PE2KJ48jxz1hFmf6l5MOHDWrq_uHj5e43xKjpz016VKdqCSqg0xCuGW0cbQPzvxE0IJfp4nYgS0pNScZoh_o4PFECmFo4Mc3Cp6E46M40B6geplIDLR6nM5AsqgqXvcGUigU0TrxeNqz4JNIgahw9IRLKkVxluxy6qyWAnO7m_cuW-ZLM0dmHzf-H2NeJOS0L9iULPYQ9AEzcz0ZvoMfN_Eg83CKlSE2VavBEeukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41fc106a5.mp4?token=DRIyPbPDMoWsPHxnqgOV37t0HEIISoowCLw1DTUxzIvgMP-5_ADM9gIK1CjPvqqqdZ_pZQv9Y-bIwhw8aSMaLFGofrtKR2RSh-6DYxUbRszM8PE2KJ48jxz1hFmf6l5MOHDWrq_uHj5e43xKjpz016VKdqCSqg0xCuGW0cbQPzvxE0IJfp4nYgS0pNScZoh_o4PFECmFo4Mc3Cp6E46M40B6geplIDLR6nM5AsqgqXvcGUigU0TrxeNqz4JNIgahw9IRLKkVxluxy6qyWAnO7m_cuW-ZLM0dmHzf-H2NeJOS0L9iULPYQ9AEzcz0ZvoMfN_Eg83CKlSE2VavBEeukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشید گرفتگی زیبای دیروز در اروپا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680891" target="_blank">📅 18:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYP0yJiHChMonrxdLQkZB4uCyqpSD4Jq-8ssGh7C_CkC_RdwrUBXq-J38CzLeI8JmOzH487asgOVwSN4OBVThnzGHhtIteZArg5_G4a13LeJ6vTBsUcewQWA1bPO_LHLzqT4ECDnBFbm1gGCMoIRkxUpH8VnMtaU_QBMl0qTQ389acmsVhcrTNpKjuoYwThRHwNiQljbtUkUvQqWoI9zcTWIlxN9LTtPmhyBZJCCawaA1KTb1iTpJPX_J3AdZ7kt89OaSu2vIdaeXpZbQ9KHd9MJPIu3-ez0QaotV9UYKh5wVKRYg0-Y9uwDrvQIbVr060y1SX2fbbnHnWZ0osdk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوضاع در ناو آبراهام لینکلن قاراشمیش شد!
🔹
همزمان با حملات هوایی جنگنده‌ها به ایران از ناو هواپیمابر یو اس اس آبراهام لینکلن که اکنون در خاورمیانه فعالیت می‌کند، خانواده‌های نظامی به MS NOW گزارش می‌دهند که ۵۰۰۰ خدمه این ناو از کمبود آذوقه رنج می‌برند.
🔹
این کمبودها در حالی رخ می‌دهد که یو اس اس لینکلن رکورد دریایی بیشترین روزهای مداوم در دریا را به نام خود ثبت کرده است.
🔹
طبق گزارش‌ها، اعضای سرویس در شیفت‌های ۱۲ تا ۱۶ ساعته، گاهی بدون هیچ روز مرخصی، کار می‌کنند و استقرار آنها برای دومین بار تمدید شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/680889" target="_blank">📅 18:28 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
