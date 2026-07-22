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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h41pbYvhb9e0DKRwl4nmkMylfjR-L_tw-Q_u1kgjrIAa-zqEKnIpLdrsXeEsv4NaKUUyLpzbZUnogyAG8nrPyUxHWEjTejJBgChTLoF26tDq62oMlN9rggeq-HnNLHq1xbsdgLGAQd1Uz23i0J0pCAAL_U8wmX0_ARuoNMvHyQv-DDyU8JrYXMyfBPprca8m0c1Jv8g3xWdzEWntvrDOMsWvDi4IA1_VnsilREud0LNmu96zrOoNtpPS4rzBz9zjVlBqEuVwK5VVzueshEg-U4zst7Zrdb99BALFund44B6QeO6SNd-fvUSw0ZCegQaC_xZxyRK5UiCPR07rRHVDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHSV551QYiaa7lNxeZyZHdoqMT5rVTZ2Mp_QqLo7WTBaFO3W3E1VFTfTT3j0P53qHoyERa1sirBfEfeYaYiB15LtHussL6SMdUEloOrh0KhkK8Thn14Bw-eGzIjDW1WbWK0BPNtSHB4eGsCjKSB0XyF-35NKkFlQy2X_ixysDWAN1KVjjWjRiLztEmR-2v5pJL4g-mnNWeUg6Dyrabb6dwT3qInXbxspQmbmhdYiTnFWj71lwwgRwRbHTru1IO3i_exbTlJBLDKBk47k8niROmoK0mvgDwG3brHc8CUnDotlSe0y86SCFbjuYT41KlrMKjmac5UjCvjabQJgq3tWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwia238aa4jtjgpwphxxdxOofx8yCqM494SeCF9gezarIaXY24YO-Z_gvdeT8j_P8nWI95Hty8ZESwACWdIGx-_hbvFMG-R-FfVMWpGHujFpjNTikQIDhjq_fJmIsMqnj-SSyDNSMIEtoySBtyLDMv2hY1zS58MVf_GylbWWNSf2erursHIpUxI8BIYQjLeIZoJG8lnTKgqdHA3BRCJBu68HhysftgiUhMCid-6sGsuqxNaJDujOnSq05tQJIq0pahUccHgdkCXl6Sea736ZlMBcqykxjjJ3AGDWlnaw1NGPz85rX4uSPuwjVivPFVvC2OrPr0HF3vMbf0j_2PdLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfbTxnVOObZtKHadnNtxCtZtdBr67DUZynwZBbegv863QHo7DJRrN4GT1-KpPcUqcbcuP9iAFKUW5HdocjXct_GJouLM6IE11LJnpaqE1LCiCiubLYpF_z8KSWaJwr28LZxjsJyQAnnV3IThy2ELUUCroidbFVji9lFQUrTJmP5W72mnuVGxdtupRThGoZSSNkL7gmI1mlgGRH59_ZOxE1KtcWsXHmVvRzCAlDQIuCV4kGoVvA1NqdASSzwaUOszNx02vbsm4Z9Mgp-iWXAgKGEfiRVVF46hxfVMKkKb8eme1Khveo7yB6yYYw_so6mx7C5yhtDUrThh3OUWIO9LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxAjgqSl2SB1YeWhbuLTig2G-bw7zrV_xlUArawlnZ6fRv0SdEEHxp0A9z9q28hck0olb0ty8F4SyEHlh2t30blDhCu9uIZHWbC2qWugYc1zpuMlDLMKwVZZrs4ZwHuxrExRmYMhQ68PV-S164IVg-HrQyYxxUSP5IHVKA0BpI0nKdpMuIQfsHg4sTk6hp4xtkxJjH2lOm_RlTyMhITMXWrMfNeMya9nNToe04o1rnvOdSq81fF7EsZoevY920xS1RyS4Scuk5MT2D_RduxWbpPZ4V2cgh4ibuylMgES-D6N3a6ug1zAHR86NO-vNoPVf2dzjpg6nWtxhq7kjRIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r31
📩
@winro_io</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-96ktIoxM9JGuoKECL_hoGqK_q95f3DJgVzGu0fwZnRzImfyu7IAYLYTW7atqFdtz3orRoCa3Nr3aSZrgjM9JU_ElVqRxAMhrwqnOuo-aSBYK2BngShbtpmH9QtiW2HxzT8Jw3oWFjrkka_f-vC5TCmKJh39Nc5Vy6Dr5uAh6Z_qEQFLlvCVwS9mW1pzG8H_bePJKrK6IarMIo4yUgkjvbS2k7DKo3K5Ud0jRyFmCW3kQ7x269FcMqePqbS61VHWMWzsGJm1EcRXFcJGJhuNc_zZ_-tentXYTRrxzWm2ZufrmUmjPZ_JInZ0sig-QBX5p5aNi1322s3iu09zN9ghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGgMpjT1WlmePFKXhHUWCNDabILWNpPYo9W9uXRzLdkc9qZt3LuQNHfiJt1mH_txhUg7m78K5sGEUupg8XVS1ZPJlzJTVsx61cxh1-EWQwgGUsDt_q6hy22UF7URl-t6whxcotGFATEae0ejteVgnegn7o2Hvem5Oy4fkJvzctPWUVwCsMfnU8XujpkSvZtScC-8NW_FBAk1CLLLeHnhD576hYTQCCyM2gk7cY_0hJXIItv1Ki_w2NYNceJutoSJZZI0FbMpoUPg-Qi_sndf2ogvKLg4-C5On0dHk4YZSTNMlYDp9XlsH0JpJh7vIuRrSaOd7fIbtFNMYVxmiX_GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpKImnDXEbYxcK8fR4QFYhY3M1XScePpCNmwZ6cdHbGhC1MPgDPjQ_s0udGbeTncuHl85hmRGwtaVg5Vzw1Oefpze2N4cdOQE9djkkm74bh82dOgmOZaTsLPLosf02TI-kbT9Y0q6zwk3WbOnoBTBTe4cY9oSFFWOZQHN5ZHToxgUqgEboTadi-03-zzdELDr_v0yOPGKym5EySGrup7Y_jrSUlPYmvlujqRkfsuQvzbm9PUtIEBN1rXXkH60AA5ZN04tHBgU5_NctAQhOpR_7Z37CNqMlTxWIGrc_wtDvnWxA_SHp9XTL5c7i1AcFLiPEQNJ3tYuO_b0aVTVYhMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQCmA1ZIljxhPY9k_dJojGRjQw4EH3csPf4WD5PbiEdeEnpveCRbIU58TsYqAjDjTUSCFZwjAoFLTj2aDIX61GL6_IL-MQixoj4ZDA4qKSLAK5090kVT9KKdUfbLoBAfnCsF9D8xZKb8kZ-sBgAx_uam_Q7kO2sMeYQPWtIlBOOpMEeNV2uGh3SmPt7mNZLFHuQn4TJSBfhh9PnwGQojz6qHJPZH0N_fOAVWY8oAutJl17x6OLumj3sNalvQ8M1ejsdT6AHQUmP0eApyrrZNLnfAvJSuKV0KlGUjjK6eJMU5UZgAY-TNXuSsv-5wrzE5nEb7ayoNeQexcOKg7Cn7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLyb5v1dcs2zs6JILMMQOGt3D85e0BlyCGhLkxM8KQZo3aX3iH1Zcv0ppm-VTtyTo8zPNDf1YzhrdQpXlZRyvt_Ml-oEo8qfBsNH8qphTsB3vblKYAc-2IUp-_stnXFjjGlHVmh7T-TDK0SLzE7ywT7UGT2xJsPZqWbtXest39owBylQwsiAPjmlLuyVxo5lbYxHwfcD3uCCM97ONLBXwLX2i1nAJL2OUiFV1UGH74PsbRNkmtjPgj1bHnmcPUH_j1_WHN3Fpm8zZNgk4p80L41fmY8Q2FYP-1u6g5ThMjp4yiykWkHKKzWqLJhgFxRf-lgZskqZ4Meu0-xLJdhF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFf_q6_Xz0KWW8pQucChXGGEDqRkZRo8INcxKiCNKexZKFvay-v3VPGyvd8kb4KTbV1WY5Rz2jdxwsDC0dPuvuJcORBKXkf_r3SjO0JxOC4ATdRow69LsaMxcNGSXx_qvrZBrkcNcVtYQFMbIBfPXYjpzDa2M27-tIrKXWhLZctLG6cjzQTz7h-QIEDbOX6XHp0VWojl1zSkoHbuvMb4zfKVK58_98Fw52E9m8goBHZxq9fxeCYVaxaXPAUGI6mSbtG8mtmj2XKKZnDs7GOoE1mSt0S7d-pNfc6WXVn8dCoVkPXrtyC255QIAzWCepwW5vmPOv9a-znvl_l5mdmuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs5K6FBVOz_p8kMRhsqhhcjsGlCrPelI12y3FotDVD2PPKiTHGqF2cBRDVL9MtcnnQjQBvhI1-nHHR8oNv6nLrfOXMidtvajiJl5Vr6eo1BMxk10DRjgqa5AVby6_L2nqTH4Kl-L4txlzwH0494sm8Nmt3XgaOxgN-AuD20xdMUc663TiiNQcjdKMmHIk7E5QdB2y10eJimH_R_bupifNllkTSBC8Kv5bA1rc5ndcij3UaDkC3y91kakIzUdUw15xt2Hztvz47TgF8CXBqkGsHaFbz6Hedz5vSI0B7LhRkdPQ8s13SdrJOpgr4Zg6RsYMhh0w3etfQFS4xBa_-5sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuSVMnzg5V_MCgdRLhno_LdN3F1nTZMnTHbT1G2I6p1WzboKEuhwBsUyUJ63T-Lss5446o5zNq1mBL8b5JJOla9AKjETSxoF80o5SMN197cio2sEkwAa890O-seQ-E2-1S3vBXKxmO7SwsSqVpNiTZSAERwsoESFATqafeU7nZPpM9D8zj-HzSvyNPMXpxmkiA1LVrgJUM5uOT8xjA2keXuwMWDXVwbvmRKnqnj329wI-AbeOZjSvJnSUGDyvpaQyaKmZdFA6r0ZfGsFUO6u30sV5QtfHCZ4hW_kNorFjTOFlJHc5R-wQgjmfO_HJVNB90eTDKRrUjkjYONWkz1Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIrgJDezyXVDd6ps9UghDn2U8rEwOCzXZdsEcyVofccc_f583zVtLxM-AlATVbJFD1jRZ1ZL21EQHbF2fWOsIafShISiwK4jRId2RjAhh1-E_gJBCe6rRHXKKzvTj2BkdTNNK2Rs-yxKscjjmC2GhSBeG2Q_-C_INFZLqjWVsxdlgUazN9WAxtgHbUd5suUdEI0u_Iq8it9S1C0_DPiZ4EB9nEF8uno8At7HlOVfiOKVNJQKDvcG8Bs6mGxiwuVQIEzBOfYdyVeARkQZmjzaK8QiK_QIKSohlTMUghB0AOhjQHZoOz6WOB6zP-8nDo6FTHDv4RkEH-lgiapcACJ57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCEUwBpelyJiO7UjmALKc-_-v522PeUCWqPtqIOiHJbNXbOPVbH5mGI2GSsZpWaa_4gZMeqUC7K-8stgqfDW6-UtCumBapvJnsGMit2Nnfeah66oox_PTSUmGs5n3tPKnRPYvk1X63IGK3l_GQI2gZU2gB1ocYe40h_Md0xLLfHChf1eJFr7oHhrnPJEhrwoeknwiIKF5lsOH6D3Oo-TqFSOPyKhFGfD3OyP59ZF7lpdkMa2t3GoQOPoB_P-AkfwJ7sKONfaWPadp6PLalrPeJvCkAGt81s_2K__h-aw30lbx7_3Xc0e1R6SQ_UlnRMzkFdxFu0Izn-DOe6_4EzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bulvij45AcTGXTZ1FnkEMOuMIF7ma_P8m55cLBBxqRKU2mnMiO8qQ5CXJLuqKrXRQxUpa8djzCFmJbPwcOUEjLHn-7FX1Guout6fzxCHaK_ylCYtqVFXdE07LyFRy5WXThv87Z1X0G3tqlPbIt8oyLE0T2IqjxXD6nQB1Fu-ekQJDLuxjlGt1w0fOWiCev48fwDyvYUqt3KvS-XtcocXN_Vp1QMHhDWQ3f2x-Z_C2vWaFybtC8okrzpi3VlaZ7ZBBUXRuJTq1SesswQmLvToYpkEnFY--sUk80SW7nxajL32G_A4iQ5kuB6pGrRH78XmdpAzAmUdphk5wnPyEOtybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0qqAUVq9t-gp55nS357rSmx49bWa-SoJybV-Jl7uL0LKh08tl8BXQ4UbhRAzLUbEgVp6t8ooV2u4XDnL0og-gqn327StuJYZFpRsUqiCg8yryRxudtu6eX_AGrYCzpR1mG2PgJYdS-DeXTZ4H-Z3F1poR6Q6roa2FNj-5YRimGXrE6EV7vH184sN0DMqC7R44lIun3L5hvoxZ6_dvxwGxk-8Gcbr_PFQoENctY6nktC6-VPGzfnh4ZeooFWKIZIQjp_OoCgInmbaOPFwqyao0usEuKw-cz7dzdinu9bBCgYTtBHYxStbkj9FH2QZIcseoHOubowAPjUtDy0lg7KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey56noqRzdOHPf0rGC-n3KPaCuuCJ0ju6VWu52kjDvtW4w3fjxYLJTukvF-mxxNZf7abWh2sDnFWnMDBLopxGBwNXIWiupUAdE7R_3Oy0OjQmVu9PIeP7ONVJqd65rd1EgDl9zWNe82CtZcRGu0NsPpOjVEGchAUz1CbR7vE5PaKYkXEwKysszqjRQd9Ab6t2r_G4TLaxMDa1lsmrt9OMgiUKNrfsShf_5rhc6Pfb8Q6y8fYTLaFEVhuKiH7nQgPW2B4iQmfiKzMJARbrqwRXTEXx_Tu-TGRrjWnSXZY52XUZvVsePlnUPHWiDY4m2Xf_qwF1qKqs3ADioky2pr20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCaCdgzPrPTckBLiGH4ogIocAO4xKzddaNiwWTpTT46VyZmOkgLrLg5DbyVswGH4W0J8Od_vy8eXHNZNZLbiBHb-RryVSnPiDODoXiC_x-X4HsFonVBvVGsZpfFm6-HX_EvRplDlWYgCwVOf-ylR-yW9DXCx7MqogsVF6pEUCbIl_iyzdlIi_y8aBhIBpvZlX8g8z6reZDsY1ppbhBKuUzRxhs44oCW9S7vbA0IDB_92b7Rm5BOQSeTP55WDAEiq4BUpWytiRMgMAM0bpj0lipxRxGkRz3m2iMgxVL1GFyN63VynltZ2NCzFmiSEJEHsON6wO2tmkX_Au-5VBUEeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewi-UxTLZ-rI0IOPHEENlRRqCG7bUmHi7gQvRdM2lEEdrNLkevJ5BvaY7aCWrvqbKX2_pXhmTdFzK8PO8-X82BEztrVIV5XpyRAFxHbAdDp-xuq_786uyhJ7Frr3cls0fGE_HadtNn-cSTzxaWxJHc3KqctLAoftIO1jAPdo9SqSc1P-eoGDBTGh7qaLaexiISR41is1uwohn6XBL4TwDp4a9sDDLRF3JkMB_83fl9aMvabebVZV2FpSvdLOprgp1M_HFVcQBe8poqfQKsTO6O5Apddat4MvW9ZSgkYvl-2Vo8XfZLJ25VmZTvU1NNL-ipyku_JmN-Eu0aaavVnRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RYf0SkAqdghInfnCo6ZxiiMTn0kE-GfsWS3nbTKuNCQTIc83cTn8_NfqF9so727gRZZm9hQ61Ljr5_G8tt6V5p-MiVPikl1Oj93REYahZF5LwXZUsHb9J_7Fk629vMzBIfMfIkbKRnx_bY5CqVmbtCB18HeB2JrJWY-svOkB2hKOSipEslfYXhu3lycdtND5aEcOTvj84P9iSw7L-jXIXHY4sMT3tuR4AGrZaJ-11Quf5fMt_AeXyi-4D483dA6bcgl5GH4ix8YcHHSHzJg9gcwehl2jIP5hHXNxTGbrdsdhza8nJG4H0m6mQMp9f_uMhDlEHdzc_clq3uIbs3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnpWzRn20eP4rNOZw2XlOkA9evRYa2jrtLrnfvcBXP8-GauLXX-ZgLuHxAUzczcE1W1VijQDsaOTgQkXYyEp1mQ0tg-aOMThKa1CkVsUjgegZExjXxFIfL5GpYRWVBmjMwio848ZYecUc2T59GFRrSRg8yruXcBS5qYIPPkjEVZYEK7irhnvta_cZq_k2VJI9LWM-OFc2ewgI3XhKTRPGwbyVPDUGUgENoTh8de7qOGNZmFbEeBwkzu0DNxKm4e8OKbv5cvp31p35POAI2VaPT3Fq82eG5HtdBe_llivTUaJKR4CGE9V8buIBVn4Q8RwMOAqDnGR_B0qMXz-j2_zMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VZuXcmKu84T8fKUAZNMaYIILchmEl3eap-eLnMKo23ytbqSlDTSFwbhT4m6OGTScXtjYbXVO_CSttxSGi4frtFJjR357GkuqSepjzGViKbpAGKp9xMMB_QGzZRghwsixpjnDvI94MOD8Gj0Rz6GcXUScReb5JqfD0HjTf20gKpt8D2IsFIDNvh2eq4si7JUO2LJQOYgPg8ey4zslGjqFEgvx9lrhvkQFxko-3__iDnVKjvdDiolLe71Cz7zSXOmlp3gEeKizOU3tMasjkaV-QKA0-64vu05jNbil3t07NbHXgkk6W8fedf0lagg7X8inETau4fSD2HQJ0FDc2xAf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VZuXcmKu84T8fKUAZNMaYIILchmEl3eap-eLnMKo23ytbqSlDTSFwbhT4m6OGTScXtjYbXVO_CSttxSGi4frtFJjR357GkuqSepjzGViKbpAGKp9xMMB_QGzZRghwsixpjnDvI94MOD8Gj0Rz6GcXUScReb5JqfD0HjTf20gKpt8D2IsFIDNvh2eq4si7JUO2LJQOYgPg8ey4zslGjqFEgvx9lrhvkQFxko-3__iDnVKjvdDiolLe71Cz7zSXOmlp3gEeKizOU3tMasjkaV-QKA0-64vu05jNbil3t07NbHXgkk6W8fedf0lagg7X8inETau4fSD2HQJ0FDc2xAf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Y-AiGHcXwFnHHH-Z10navIHhzhMCSbx_xvLmeC9upGmVkT56LQZ22vW5cyUvq6YIuCO5jUexmF_iW39JXedlgvj9UpXvzEkgAmXpMQxdqgTIMlRlDBF0tUCY8qkfnqwyBr1mRWOkadVaUydlj0GiXFuooKT3Wdcrnk23vNEd-qL4LhSm40j0fC82LR8kT1r4iAIfeG7TUdLCfCFz7oA804eh-DlR2Bo5FnvM426foUC6YAx5h-FQhoW_owHKHJj8z-VMefTd2bST2vRP2eFwW8hqeZKjyJUis_nJ3ArkoyBDAHeSRgWfsWLWVN7jkqO4NP7N_wk1_DYglc-PNFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6CKRAET_vMMOPC4JwyTIEA15YUevjD1XFiCJcpH6XnI5ZmTLmUjjw5tfqF8_2knAJAX6wMKFK8Mn42F9YQIZIVVuG0RRNAzRVAMLR4GLRrgWVnSkaFMWSr26hVAszJ441Ptpq4xedaQdyhuyZ7YFp80B-zOKtaOgwdJRHVAODBA9trVJrtOSnSco1-HWAbv9cCffXXMdbbRJ1FzukvwZLS2G6zJEFM_SJcNaIE4-i7hc6gSGVpE1tTjSWmgC2KfvUwp3VV6XZHLiPjfUJl4jRdz55C9PWql7j7a-cwW4WvYDZRx1l_OY12Cx-tGSRHUN22vt869wpkEzbooNo7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7mKsBkuQWcXH8h1mGbDhiknWPOGUoILKFdldNBNWWebfHho7tnG6RJIZZ7k3tO4TNOM_ouhK2nE-a3m4kfpsppO7-zmk9Im788JBdQGgJNgZJofI25AOgulrGwhtEWraHrxzXQ3bquCm-iPWae47Pjf_7GvGulWPq6KP49WElcNLYYk1A0OFAyNw8dco1LIMeISffuvVvncfP2ohHs75mrl_3Ygin5xUitiuvSAkxrfXOBBFRiXx0Hgn-z6XubMsnG7OsFG-uT7qaDvoXNydP2UUplAGBOZPSGmynKKJ2y1Tf5TSdZL4iyRjj9kSC-Bn1Jkh0rE0-L8nXZFGjnjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-8xRJclFWl-wKv_7MUchXEDpik8TOkcL2zlbzGibPyDrS-JbldX_9u7S_SLMdtefLcPjQG48ItihYcUB1ravfAlQjWIFIYRCO397KQh6Tc0qn2bGAOuPC-gHYTOL8UvRXpDH2jzTZ8Y89s8J2CJJmTP8giUWiYGCBybnmJTYae9UCKU8KG-UdFFdXi3yOv2sEzXnHtKQ7EWUC2T6NPtHZeD3Gsa2PpeXW6FPcS5nDZR7MXiqeknJuiB3IT7ioX7x4IUvsk7gaoxhAbftuflwGMpf3HVbCuCep4CRjJxYi7VjkgXOosOE_-UhPGqlH-ETYZhypXN1vxiu1ALqD6ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgqoPoUd_jH0DBv9TI6DDTzT5NhKHzW11v0Ppp8kcLxfk4Fzu8vAjIaZBPv0CX3He_S_xrAqFNlhBeeJoSTrMO8lpWUrSz_0ykU_nurTXNGZRKOVMQZzxWSc158QBsKT4AFmwnjElW8QkXbetN5TjCkpqGItSQHnIxaUkI1sWwW9BDgJqONQquZ1fVBNi1JaomX6_Umbxhcp2a49BWL6mimfo4GwQUE_0JZWNCUPI8eoqYkEmh2c-nSBaAiG8krU588AuQX7qz84zQcrjw6oU2OPAJrKN0tC-15ChQgb0gRcg_YqvkZU_dOBTkzhbWy4ydLpcAJfweRbMzzX0VLWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYQ2mMamyL_EkNwjsA_Qug4O9aWATcz0z0rHaLjwK4cA2KxklSRy5YoaTcm2lTXes_KwvvjWOegXoY7KUIZormWV_oy07avyaiy4guTSjsI4lrS7EaklGz8_C2WbrVXSAdJX4s9ePFmULRa1o1glXm0l8rdTcy8a3uMADO4UoJ6Y2xIKiWpXD5u807kla38bDzRizsxy2PdC8y4MmCAqKzFr7iucV2Vn7BbaG5WGqB8QBRoIto_s3zM4pcmvztRWZj85QbAOMUvrMngw242HTgjQ2b9vgRQMBhGyWIi2qeF61VAVoWAlbhM5vocYaJbxtJsKasts45LdKZqIMdakPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ8C3NpoCUMBIs0AfFnVS8P8Swb-1fsaPw7rdA92kI-l0Zn28Zi_4wOs8VRyc8seaK7kAKZvm_Fpd4cXkBxNsdTs9Rw1qE4doF3YWxdcesahEATTEkhLB73KnYKqukh1UEcff1LmM2TgTbsMfaN-kl-JZjHHfOyJINCyBVVojC6X9lNgXUDQifN2QEiX5uiGMgeNVQ7hMSilfQCN9wZfW1xZfuyJpHMaTdVlzYph4g40ym08d2LwrZcx7HVCcYQx-qEii6swPxsfxSHUMrq2fUJWdVEzMM9kuc_M_gPfEfBVDhJ97ZnlY8T2Jc9xvmdRIVBPqsNk_DQ2K6DgkSAjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI8VUmYkp3MOqCHmpT5WufSZQj-kH7dYZCk_8LS3WWv_ZDEt45asdkXvNurEwmPlBCj2pun_43plZvee_0PI7GroVPGXugXp7RhmZbCw6irv8kRIbvuwyK3t-UkAttiiRDCxkeHFBkThbKhifsIyS3YnY03VeMbi1A-qDSE4eN-194Yx2dtT610trSAp9BBFeki9CQxU3cFXZQpISQ7hwcwRZCG94Wa0FX-VmvIp_1n8KX2EETATD2UIslEd_cDdOE2VY5QpZUC6LpOS8EjDzXgWNE_U1etHZo5MPpWf6ianihM6LC-22Cd-YqG1Pzzx4nHMzhYACj5WeWfDETZ8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=bF0xfMWKlUpLXlReRTnEPBM11Xyw5X87ZnzLRBpkHlao5O9IIQX6z00ccJItUDUIP9-Km5cElHC-uwMoMvP0RThQAbHjdrNYQLrSziWAEQWwjT2ls8mTcP_2oMjOsv2ut5WwIGzsXtFj-p5SYhMtv9kxttV053WapqP9OueGOqOLXiLe6gh9lts-yfxU-hRZCkdFcQGl_rUAChN3wMr8YLjkOmPbbWOOQZIf0D59DDqsaQo0PFKIisWbOpgG3QOE54G_Crvz2Ik3sufMhyCw-SDkbUrgei4awjt7boL3ffZFlprTiqquc3I8NgovxXGMNPiagJAkAeY9yCthxgjx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=bF0xfMWKlUpLXlReRTnEPBM11Xyw5X87ZnzLRBpkHlao5O9IIQX6z00ccJItUDUIP9-Km5cElHC-uwMoMvP0RThQAbHjdrNYQLrSziWAEQWwjT2ls8mTcP_2oMjOsv2ut5WwIGzsXtFj-p5SYhMtv9kxttV053WapqP9OueGOqOLXiLe6gh9lts-yfxU-hRZCkdFcQGl_rUAChN3wMr8YLjkOmPbbWOOQZIf0D59DDqsaQo0PFKIisWbOpgG3QOE54G_Crvz2Ik3sufMhyCw-SDkbUrgei4awjt7boL3ffZFlprTiqquc3I8NgovxXGMNPiagJAkAeY9yCthxgjx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEMLYlt2A_O-4b6tUrPNhqf9kTBxF5vBCyo-c7L55odN1bWEz_aWlZQWDBiandwBf4hG3CqEStcjua6bYwgsgSOWYaw-7OdlV90PkF7LcoSvVwOy5mL1m49XcLz0AgabxOpl5f437ZndqxHJ3P74cjScTn8XE8t12mbyh1qCh4rJoChC81LmZB8MiKWWdiKZNJ1Pzqin-Y0pZ39rbeN2u-gi_S5YVYJ2az-lqIh41QM2NuPQEBNPUUbAznoFnEbMnJB4xrbeOqLRa9WvecSjC6pOvLiMxfUlr5VDCsz_HwtpBcUfaMKbOtLwuOj2dh7KElAnnRBfxvrZpefQ5h8r_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcww9IMUmJPIh4l1fir19KtcrR4_eklvFjhagaL_792qiUZf1nb6BP7QSCW0yv18WTtFPQLu_Qv3QPOf1BiLxJ2uLUjvIMd7EZs4-tHSd7NJptBPmsk7Vi-U1yaR9MfXPP12-R3RKKIZoW0BYO4mTZMPt8V_f30v4uSFb1IaTDSl0Q6fumI9kxP1Us9_l5F5RLrz1H6zKTbwmUeI_F3iBOvbwkFwY4CYzT4IoSehwLgt64t8603-RteAr-t5k5Swx_LLxO8b3MifMwiuknnhfavHkialj9vmSMLffPwFlYt9CPF8t3CJeU76M1rbwp5-R1ETpcC1r2QTkQJfLisa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlFTcRC5VypZBFkrpo1Ypkbu3nEadTNdyNHhLtAf-qW5rIRgqci0Jdh6iI8MVJie3GYroVVgzlg8Ej2A1vjiRvYFGr-eOWhCqbybTDDfjiPf2fWtaOf3RGiFQDoGov-Z5EzuXf3PM5mie1BYIVUWp3LCAY63ZbOykZjDOdzjMNCuhp1FkPdJMSyhcq17Qhq-Q6R_RTZEpRBoV307_O_UqXAfsvfqWNoUKqqI9TrHetPCGO7flj4z1af_9jC9tR-6uMJwJPIdOkalqZXJ92pb3DcnHq3QMD2oL_TF45jorHN6cXleR1ddIBOAT3W5t4Lf1aG8yRJCteQOjdKUGczGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=quTbrdco_IFtc0S8t3N7dm2mQX2kLGjjNQmb1e2uy71Frpx6NkaBBGG7WhZsSuV7W0O53wZSIAh2bQfzv50rkTkC266RKBPfx982zz0DJscJw8dYRcyDRgEuiLw50G_Bsu_gCUd6_9k7HkqJaks65RSnvynAjpTiY-MErgFKojILnXChVXWGOhK_apaGdNXKM1F1WvjN3XN8r-PjGiRU0Q71uhuKfLp0vg9yT9u3EQfuKTh9UqiBlT8dkbg5QowLRUJ_OMR1o9fhafcCz8mSueNIYox4gyhzOJoHhKrRbjSLqasEipHfr7a3_9nhjRDDNIA4R6sGuvEK_bJkZrIesA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=quTbrdco_IFtc0S8t3N7dm2mQX2kLGjjNQmb1e2uy71Frpx6NkaBBGG7WhZsSuV7W0O53wZSIAh2bQfzv50rkTkC266RKBPfx982zz0DJscJw8dYRcyDRgEuiLw50G_Bsu_gCUd6_9k7HkqJaks65RSnvynAjpTiY-MErgFKojILnXChVXWGOhK_apaGdNXKM1F1WvjN3XN8r-PjGiRU0Q71uhuKfLp0vg9yT9u3EQfuKTh9UqiBlT8dkbg5QowLRUJ_OMR1o9fhafcCz8mSueNIYox4gyhzOJoHhKrRbjSLqasEipHfr7a3_9nhjRDDNIA4R6sGuvEK_bJkZrIesA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUvYhyygbZoJFxY8MyUJQkLy5Fo4ajZSiySm0lhuBlhOzfv_Bn2tl8X2RGtIjbB4oSC_shyes92oK65iZsd9eeteqkYX_ERYeixSfW0NGXYeJSZWAJ01D3TeW2LB4oiXx1nEwjkRXGYOPW5ehxxCn2I3117-SVHwIjiFhF22pu0OzLF9OjCTl8OHQt6tlWzOfEgmb7BBQMmR7Acmy-beC7WJg_CBi1knxDzDtQAkEF52lveg5FuH6NyG_802lvGBK3gz3-UdktwQiZUTQXbrjYRD5lALaPzGPyKWw1HS-mJuAsZfGOFB_qs7B748UWjzFRsz186BBuBWD8ZrmAYHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjqHIarjOuk-s_X2tlI_862NEVFyUDlzw8euaCNBsvtlOKbQvzFU6mUtipimdKmTBH2cegTHigunK5L5mmaPRS3azbzfowd5sdYhmOeuCdubzY4dvFtQHpQJyLutZdKA-vv-Zh7Wrtg7h9xU9CEh4S-peHdLb83tn4khcxesg8KduplL0eKr_-YPSeDJAzrKjw7vGNL-4sjsrHCZaLcxjGdwg25snEa_zC7wzAdLqBdfF5Bl6TCqnEWmY8lOQIB4cHrW9O-uY8pInuAZmmFTUlih1tJe3vTz7wqC7Uv1iOPh5-bXp2Nv0ougtoFKS_g9RiteCoIK2pxlCnFNRzl-3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYtXa-dyOX_YkxBgJeYj7kO8uEYX7PhRFSvR_OBd7SZvqwMQeTNDNboCo6qiOPSu25I4iUSpzlLDVemvXudgb6pFIq5TdnK3hrPFCaDv5QfthOZD67vF5Jyk2pzqKfEV4LCVHPF5sXssBjoRfcmgmifeGNvqXUBTmlL3txNDpYdB8cDuSreKAufV6P210GK5LIJh5vMpbvTcUyHxy8W7ky_ELP29Z7M9viku_EpbRIfaD7gtyt1vhUmKY_FVAFEEr2TuyOwSAseqlidkiCIvBUi71_O2NigEr-uap-usdWS6U533-s9ZUIChBa_QQoXEMJCx9Fcq7LPnP56u0DF11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3evc0o2XR56T2U4xM8yCeW1MEST57xPYmNtR2YErWaz7a0MD1rG94202Dl28C5Nc2dvX_nc4Qr8glyHQXg0QChnU55FkvJOgOz_OD-OqHlAn43HBtgtuXU7Q6gFWc9t0lnySbiph_fgIC6QJTaIOl96HtRhNIPG8wGFjlFHwTuJrEbU_TtL2744bVlXEjLLidOZDOB2wZAkW_ZdUNZ62rddhdEQ6ILjBhFN-szk9cbqTcqJvK_J9L25uCmtHq_1nufVfK2YQ2gaOTB8G-Ss5dS9VM4zx4SMQd8GxcEVTruZW930KgEoyNfMM8xe_vTQTaFSRvSfXu-B4XeCnNEWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOyP5BvgAw_DFv72VMBfJ09hHV1G1QSdCX2u2-coAKPyjgz69mTSzYvXur7rVqYdP2Srp54rZw20LK2q0XF_tu6PU-9ZXi7b6uDmrUhgRlqW4hscKI3QWAaMQB0M-3Rp1cZBeXE2ENctybGSnKl71hucUflSo5uzI11jTKZlZdsZ54ENjmchl37ugWguyGJsC_bSsaarGrHUvH5AXpR0EIBEG10jUQ1pYuqyVNvL6mYU1_HRzjlItzC10fyd7Jb68ktP0tRxEEIFwwgfEhDdjB5o9l0cdM3MieIIs1a9rbUHHTYT1AOSewKUiC1ZPtZNUZJu2EDvfuxIBT57e6vLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=u4CJDpiJxGHze12tEBasgOHuK6AVIuW7IwsiDZddUMJoK1lDcruRZ7kLybHXlkv_PZE2oUpSe3gkDaxoCK8CA-EF5tfhkcoWfBLn5qQZHIfrL_mSSGhLl2H9ZRhRaeYCcCQq_DmhayWRimbPkfuhOLv7IOvj3Gqhuucsv7X8oqEW2-GFI32LOgY993HGN-gaWeuLEIp9-iExMj7PITYSCP1NIrq7wsueFDq3ILRRoqag51FvXNmWW12rDMPUaMwrgoiQgAGzSPWivvz3B6mWlVm2rVvUZ0v-rBba6dl8dskLYKHFSPd769AxvhteAjHfRmBbSnjgbojnadK6DX6KgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=u4CJDpiJxGHze12tEBasgOHuK6AVIuW7IwsiDZddUMJoK1lDcruRZ7kLybHXlkv_PZE2oUpSe3gkDaxoCK8CA-EF5tfhkcoWfBLn5qQZHIfrL_mSSGhLl2H9ZRhRaeYCcCQq_DmhayWRimbPkfuhOLv7IOvj3Gqhuucsv7X8oqEW2-GFI32LOgY993HGN-gaWeuLEIp9-iExMj7PITYSCP1NIrq7wsueFDq3ILRRoqag51FvXNmWW12rDMPUaMwrgoiQgAGzSPWivvz3B6mWlVm2rVvUZ0v-rBba6dl8dskLYKHFSPd769AxvhteAjHfRmBbSnjgbojnadK6DX6KgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Setu4OeeFWGT0dTonOwhQeDS8O88VyLsUtCIk4xVqukOqRY19iMSJCd78OUp4E-2TpouoMXUCfzO5UB8oggtIPbQFV1Ht9FF85-zQ0fr8u9bz5ApsxrjMzf0XKx8BajXWkZ-2WfHQLcMBILUzvxVrJ1uXbOyIAnsOhpA8tgbgp9GylERRNhsCJETrj3T_U3Le1R4VEo3aP3DHDFcHh4tHW971yDtfvI8hs1qOy3oOYWWtHb4poFL0Fcr4PN7WVRjse-SQH473XMHlDzG2EcA0mHzmzB3kkB2-ub5VnGc7yevq-F-nHl05BL6yt58qMmwR71fqavK-7oOGHKuOClbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Setu4OeeFWGT0dTonOwhQeDS8O88VyLsUtCIk4xVqukOqRY19iMSJCd78OUp4E-2TpouoMXUCfzO5UB8oggtIPbQFV1Ht9FF85-zQ0fr8u9bz5ApsxrjMzf0XKx8BajXWkZ-2WfHQLcMBILUzvxVrJ1uXbOyIAnsOhpA8tgbgp9GylERRNhsCJETrj3T_U3Le1R4VEo3aP3DHDFcHh4tHW971yDtfvI8hs1qOy3oOYWWtHb4poFL0Fcr4PN7WVRjse-SQH473XMHlDzG2EcA0mHzmzB3kkB2-ub5VnGc7yevq-F-nHl05BL6yt58qMmwR71fqavK-7oOGHKuOClbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=HVHOTGmuonTQpB5z-z0-KuLw8gZwnnkjZ4c4L6ecdJ6keEBWOqiMZDCpe47Q_GRtIUWBqLadgtpberbAwYSQlmpaXpWHo_-DzE0YYYwk_1pS6ZoyKp7Gv8Y3ESu875_Q9eJR8gpNDgKKzH5KUC6R3L0on8Lv5lvkcT4pgXdQjSivnozQLq2QK_K-k12xE3t6fy8cMe_cVYirls0MB6JdI_Dnzp8VXWwAlaeT7asBwTzEViAmQbdBcKXIUL6bvoA3vjVfMaC7Pk8zlpP6Rp5tEzOS6Qrxrjq--1z6rBuqcfRSwIYsWvQebzlGWygXRAzid7cAOrw9QSZ8-R315WKvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=HVHOTGmuonTQpB5z-z0-KuLw8gZwnnkjZ4c4L6ecdJ6keEBWOqiMZDCpe47Q_GRtIUWBqLadgtpberbAwYSQlmpaXpWHo_-DzE0YYYwk_1pS6ZoyKp7Gv8Y3ESu875_Q9eJR8gpNDgKKzH5KUC6R3L0on8Lv5lvkcT4pgXdQjSivnozQLq2QK_K-k12xE3t6fy8cMe_cVYirls0MB6JdI_Dnzp8VXWwAlaeT7asBwTzEViAmQbdBcKXIUL6bvoA3vjVfMaC7Pk8zlpP6Rp5tEzOS6Qrxrjq--1z6rBuqcfRSwIYsWvQebzlGWygXRAzid7cAOrw9QSZ8-R315WKvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqVQjPhkikCPPG0JWDOgw0gCQTonCXsWiqqvMVMtWf5z_XPBv0Hbxme2O3LaIMJiaoI5CEauF7XNc95-b6Qt4GJL90kdLGRiN8QYZ4QSNInd_HPgkJCGeT_ryiP2NrkHiQNdvM_blyRfWL8ew0QGSUJy00SZ5SMF4SqBz8rMAOlAbEKdUOpT7harCleIY6HDLlVNTb0g2S8748AKHI7KDKp532mSDDuYXCvkNwAOUz85PvyhCDntUHupswMruJmkTW24tp0ssbvyehU3oBbXKjPVhk3mQIgR73T9vDY2IDFsdJd_Mru9uaFJrzlJUv5-e-PzZFWEPbLJJfk8-PqAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B13xFCnXEGc_XDJsHtVm9ce4q0O3u99SsCYK1m4O2ESMRDl6lTEe_rRdbWFEYkjZ50Gp96UcfzwWssm1GKqlyBI3leffFXjaqDmh9icUWLIt1ibBLFbTYf_I12U8D7lfZDs48A_DI4E3SprTd8wgXaD1S9etBOknqVIx5okQYekRsJLULjxn3E2YrRcdlcirNB_8KJwVAkT0_DI3khjyHmSwIdIzaVDBFwngCXEgmy5OxVgf_pN3-yWpT43HbfYtC5UamtpwvOQ0i4l_LffybU5oxjTBtfkew31M3Wu5pDRPv78KNU8XEzxSLQO6-OZo0Tbw0MoHxQLsZYRv_89DQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYZC5xTM3Zq1KkaaxyOJ9hxCWSWy3UUNu-NYdy3QOWq6QgCNyuxgilzhqIbKyHz9hKz6wmFfuTfsyBhjO6jr5DH96CNNtsIxgeVoYJkSpP5kz8d8CR7w6EaxkQhzYK5borRjIDV3p3jxt7BrOz0OmK9RjQ_sQN6m48qgfq0Dn1I7o9c4r_M28U59ewaHFKlyVCCloqBmja1i4qg2lco3HYiI2DAvWn7mcAfNUdayBWz8KmtL1EM4CmZWSFkv0-pzGUqdYKrRywMlZKv0F3CFzn8Sz2u1weOlVXYEEaZjIOdTc6BlEOaRc6e5z7stR2Cz5rQ75bDsuAEvQ2UGODOD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2x5hlY4lyjAzduCCZl5XqXi9hKyhtfadWDJP410eXH8kzGwfE25eGY0-pOY9X9JK8d-C_PLFWaFVxNFGDGoiK6BMtcDzs8JHoglBd0gca3pniMJo0aQOOOCUSI7aNUQktIXX3QYy6n4mToBGzzmtkfSajP6ZGt_lwlPA8z-p4lufLQhdQamnnfvLbW8ed7xcJO4VpYqV5iO4pO-Mt49y3D5r7T1soRao3WPsjas9oIGUw98bTeNHjsYlLgJ0G8PMehofeUP0jsrENh0OgDD8YHy3_oVLQc13qJPHF7k4woF2CR9EBUXuMERWpnm95qjz9TNAtpR_wNBQTKuirZ8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2kacAd6WPI0zWmtvRp65mImvbDiAsSwigDz5aztzZzYdMcmHVU6ducQZUSpqNhI796yg41XsxTiqVn6Uq3EhGk7S7_aNib-6ZRoSfh0M8F46XdzFVYzyvT4hLk_9ekgXo50OHzm-coGGheGYusVfrNeSo6xs6uRkOKKidSG-FoTdyUuwEpWRSF4N8cRhG9eXbkANO3uQKsoGwyahMolq0HVTahuDMcnREmv8VpB0FkxJG9fi_SAOJ5A3ItlSAR0FGNHbBHaP8DHVIU8havQSnr4URvS4xNU3k-JPK16pDgX6S4xt1RjUZLBk2gxysbTSauG8Ng6D1b9Ry-wMet6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdSubJK54raqvk7BNxEtFj3J5cByUoSjt9k-8LIRkhe26gxhyLtIGCas1fu7EQeClvL1cQ2AjXhAg02zNAjUECpOkgR8caFf7L_okNE23QK24LSO1C3zefdSFzejMyyfmleL-7p8DPZAjQ96HUkVD6HZA-IIIcfbxjQFLz9l1J61d5zAQyICclta8bD9QgAfhU8_FOagU9AnMV9sR0r7d8eBkOg7NGAp5qsiDXNCsIf7B9DiEGFy2N7UiDfr-M9Uc71STmz12AZY4FeajFvk4INHIcMrz_dJ5Ao60Nq160-tAGkiNUV3AiOy0Yy2RMJddKxS7KMvV-sRVqPj8PbTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1_7IQtXDA3pSXlaI0AOYxxWWlgwUzl1yVOA5cZ0G7X_Bhr1mT5d5V7uycgFZsniVMy-22NVeqCw6s9GeqhfRqACxyJ9mitfNGa10NBskK5SACvfRoN47jlFL7uvVgfNEV7P1hWkU6UM642531u1i9AlIdm5tMDvW32uhHwI6zpt2zHS9ZBEQWHVgxW1ottT3FcCfo1mJuNwflcGxCRpk82eFJXZ7oiu6spSgnqXRmAZg5POSCVNwiJ8nMgS6BlqPG8NxtQPKTvOy337yAWqVDjZhGZsT-hBgf0JSaMmQdZG5S3aWzzbvcm5pp74Z5iRM_xWdfrSGQO1ptpDE_yg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Agrsedscvxwnzvn5YnRnnT5LhxrmesuvUPj8G7Wyh33YEeJkvGq23TxNgXeMr0B3EmArylpLGHNkEvuh884dTIas2Ywuiz8EB01n3Fj7MoRPXKLLOPbmNOiK-9e03-pGqcMepSqEyn1EicwP43Hkx_xlXJ0yN9khk9aAuncqmiA-8whaSh-IQU2mY3ddZ7UQ3SoWWZEozXBWNAESgaf1UAQ5C3oei5LQLoQgQKr7AqaAXFw83xeV_4H1iBJuidk5f4pgJUNpO-c85sQ5LicbwgddNA85R55mkX8WeStRT1CgDFVu0R-cynS6AZnuw4i15Ko_xVBFKfUeJ9ZUhDRceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb4PVf7r0sVmZorpb9Cs1LNrHFwTNdvV2T4VsfDHmtKG-mDQXAz8psqOpNclfmDg2DK_mMq7O1Q14sMb2Coy-0AHWITyCJI_m-DOiCN5tC6sDroovVBgZd8jc5SN00R2veFlibLLrUV8LuVSECxemO9vBu0ea5eLQBDACP95s5CYPvx3NDqzWmh_teafc5YXFnAy2liDES06KySCbg4ZA2duxUDN4a3kwcglCMkd0QyafDK6h-c666DjBHseSKshe1KulkHwtM6dknXuDPDeQbSEqC8VfXcgIQq6TuSJMTNUnhb9g02sBi38eQLvcBWg6f7YPpfPemfANELKa80blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA5a_DiFPq3R7dKLLaxyEnRz0zhm8m9yf8sCnR0f_pdjs3c8GnJIzQyzHv2QiFB1dghSpcT4gvXxlfHlElymYVi6C_EqCGNRs7Cumh1cuBcbB_53HpzriUjjIp6Jz5A4_BK2yPYTXheoyKF0A7drfP3Sia0eHb5__00NTgOyqt5481JfDc_xj_O7SL4c2Gcj2_kN6mButd2n1oJ-LONA5CW6HthROPLJ5ZRQc0GvYjob3ngs5C5lRz2co-9o1-AYt8ySyH_DJO4_6xZjpoui8MMqcCWoeqMAt05EFlpGw_-NiRC8jZpVvb2AvBVtmayoQxl2lrrY4Nj-IuHjzqrmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtLTiO_kn-rXQ1c9G36trXJOgOVi08LsUVswv3LV8eU4AsbVP20H_QMiLOmAxw2l4qX458jrpZq4LfoXrFQOLp6AxmE3lZ6fLQTV87CBuF2WhayaBIFEgrNymq9nNGpoMcZZ_hfnmR9bZ3dmqKbvRkji8aLjsrbG1tYbUrf_W3iW1q9qNeaaJNj1-Up070pXLhR0bTK06sP2oWdmjxdl3noc49Gtxh02rvYySGYXQWp1ZsGDkH3gncmgbDTc6bFQn08tukl4WFERJB9kfTbAk7jMHTVRlJ-lLdKxHR35byAm48KqW-AS48oCCxGSz9HrP53GwLhp1FBN8oY2Cif8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSGLKel5FfXVLuihgage6NH4IF4KWVDQChTrs9HhSmD0Abw3dhks_M8VBYSUg0OLdZoXSXZNXmd6u5rjma2MH2QDfJ3fxk2UnESryR5Bw5pWOwoX0xwbTMu6XkLhWPxB_OL-AGaplThmkSvWj0rVPZbskpYQibiTCDZKdguH9FnW1yI-r9xyeLEAkIYsF4Z2L9CNgChx2K0Xg1AVDs71-WQ7oDoXklB25qwEUUQ90128G1MS1zFoDpItmp9CymAwl1bg_v9AdAEHzYYnwGlKSyjKhZH4hgQplIFx1KR4vDogPxQADtxn28XQGmmF8wwT_aKBifGQ4tiyIT-vqrcibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKXsKF98GlRX02R0NVUN3-MjHtrxoYyfhbKb1-MZbSXxL4wh3hupbOBliV-gDYUoPzlzPE13rmwx_qXhfxmaYOtjjWfH77vVY5MvjdXa98JKMruJnJ0mGjelgJ-WumPTl77fB1NkXJqOnx_n_miCJxlqvQxu19-Yf-EkpsL5eGnU1dYCntoGJwoA08l2smh5yYfzqqNsO47Td8e4ETe0vsmNegSDqCPNpUPIvWS0dMl2Vrv6yfmmhNgRna7ijBm-WFgLn7futSjxwK2VqYgOFnQH5ds4k1ZHwTEsz5cGMFzk3av_HPBUIY5AF0BiITgtCkK8ia4auoL1tdJZI-dq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8_E4R6QLjRID537EkWp7HnEBlbjvt8dfLcXytOIEJ62yxoIeB4nlh5Fr_vc5AJq4JKxXJE69Oa75IqwphEk7H493GAZ6MteWZK09U2I0zuk3VziLumsDsc1pdX42JfjcxEf4bMePr98LcdL0fppaqkfFAiYZWKd24BjUPrSYeC74FNYNBHYwRA_7W97Xm8kvdyldmmC-1SE3gKNiPo-kGKS91116SbMzQOJT6g7xl_L7c6PPXrpndSLHcGxnenPeehqGP0vX6ta2IzNYHrado0wgmfndpjUxnAIccd3BqH66l8VJm0sGWHtTf-QsMDiTpZgIKSQPVsU-XzjeV0k1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUAz8fUgebS5Md0WBbWaODzS7N2MOshE1-0HGe509GalEiAzfz3mtMQ7YXRoLyk4B7ZS6Wn_PqL6INrdqLCSGj8vPI8wx-3SSnvsPpPceYn-Y_kZXqzC4GMnPY9CYCAS86pQLxk2aAJCyBa0UcLhFtXlzWoL5MjdzE8qYoNLsV4GNwJMoCBO_Gu5LfwbvcuXuDTi4TpeNgBrjzyKZYDfibIuefb3ICyrw2tl4KpTDDkXGqUvfo8YB2UtbSPrOBBhh9dEJltbvWm_hLXaznjhAvkyD5daHCrZZN6LCD-CmIrhezlSnR4KSnzTBMy1m5IfgbQ4Nq54zpSumqJnElrSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGUvsLwcBSToku6tO6OcVEV2SYMzdYem-tQZcSDr9EB8_P-dcHOVU2efI7SZFswQ4j34PdGBu_ks8soK2VhzZ0LGXnCfaVP_VbM7T4IFClewQx6nPQz0RjqdFDXUDzQcKWtAFySpmWUIi05q8VzwwdzngkHQMDSN45FfnzRVInVi6IzmIHNFzLafYT0BecM2Tm7oS5UWJ_y7yYzr1kL0vIgK59dRTyQ7j-5uylu8IvpzkGIFhh2hh_Cuk87PWD1GPJCFmc5aYqILDVLZtDGdsu5yc9CNruixKUpIUIFAeAmIG9bK0IWED8ytt9R04tPotibrGBLBgfTHZToJdKlOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbHAOT5PjgPH5PWVmPufg2M77hSxAT0kAVT7EMnPGWdnC2HR3XNnQY4rJ2iajmdQ2wjJ2LUow_DJFpgznmfvMCtwkdfDCt907fYv2ixLWM4MDepmCIjp6m6rxlJyKBoncxkZ3fL9MCVS3-PzB2633YronDqgRfopIltd_FmRc50oyMV40uQ2ypyDbQnj5YXW7z7nxoYa1-is77n3VLp8rN3wpSYAdxVPY4N8Tg4T7-MOIS2SUmctwwwDMxv59XMHGJYVe2WgVEd72bhngkMxptBYm42E5zqm_wwBmthequKEJs0_A9UNCyGXyGxoUuXoLJeH58RKxY37mkcA26vrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=XchBs1l-jQZAl4-eBnTEsgH54LSqyFbwlVTUNcM5elKd-N4IddyBanyem3J_ntlHUX-KHixpYcUL2eFaLX9QV3XtiI23kvC5zobg-S0ZQSoUFlRASRGDzfYi28cjJDJEfauSqQtc8egLMAVWw51-UgMGyLMCm1f0907nsqBYMbQJh4S0HzF25fmL6unD0YrVtg8PRrkUNzbVXPPGxstQcfxwvjkYbiTwA0f91lSzw05OvRvxMma1_8xV3pOzUvMapNC21IRNY6uiMzKi5SENJCWZ5LI1VeMrZqT1ANifl1FZYLXLeDZn8YKNADR6Y1oRBoGRO7NwXfM6m2IyeQ2i4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=XchBs1l-jQZAl4-eBnTEsgH54LSqyFbwlVTUNcM5elKd-N4IddyBanyem3J_ntlHUX-KHixpYcUL2eFaLX9QV3XtiI23kvC5zobg-S0ZQSoUFlRASRGDzfYi28cjJDJEfauSqQtc8egLMAVWw51-UgMGyLMCm1f0907nsqBYMbQJh4S0HzF25fmL6unD0YrVtg8PRrkUNzbVXPPGxstQcfxwvjkYbiTwA0f91lSzw05OvRvxMma1_8xV3pOzUvMapNC21IRNY6uiMzKi5SENJCWZ5LI1VeMrZqT1ANifl1FZYLXLeDZn8YKNADR6Y1oRBoGRO7NwXfM6m2IyeQ2i4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DubECk51m-AQcd5QOVYOHQBuULoD3UyC72bq9v8BSuRHUbnWznVVgeCi9zSwnlfZXZGNqiL2-oh48tFWIlCBol1G2E-ymO6unQAbGeWYTuxTSC42mRmi3_z-F4s5TnbRsi4dJwS3Mv-TfNrtgWkfHd8Dzv9wdimkkcbw269rEl2wUVSLfyDWRgE6CMwoBlBvV8-87-It_gnz5sJz4DRk8RMBElmu41AbFlIJsgJHocY0rq4FZyEN7KkwTsE-FPV6ThwdTCYq9jWpLgqw9b2aOOzmoDFimTZJmi750nMu6fZbRG3Okkm2Li-KaF15gwl1vvPAm5PWT0aoAHg6kindVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca7yz91cr0xzvXOeGBN9eiP4IHL5-TDM6jWA0eYKweBjZG6671mrJqgFhbbGMCh45exgXJrA-seuOBBKBUFbAYCNrN7MJSLwu_OAvzkqwE48JzslHqBR6AsEbtN40Jv2u3O-VAW-vgWYOzBRh8aO1cBbFU6PwszHaKCFlOecAThKhiA5nsC6iUK2Me6vt4HG6tS1ZlhOyzqssLcr4lykRnj7DQ_QmE9tWyW4Cub3PNZbsZ2XFlItj30_fNqjw57FuJ2RvQZK229WB9OI5JJbLmPVUTzQa0UF_QaVMcr37XJ4ZwrrWftM1IWB-MB9LB0aNpYMaKFrsJP6egvrLpzSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWaXbpov9XNmTS4Zqb-ggT6c9jbLsBqFgeQ6Ykd_wrk4FU0QKe1RMIbTz77DCic03nJAPniB6qS0PcWAgY2gI5UjymAdVx8JDPylumSgerhD5fmN_TS3R4uo2wpNsMf37hsyMDI8Z16lughQk8gncXSvlp305kn0POzlQVWdXtU_ETTrf-GCqw7hYczEwA515wjXIkpDknKMro9YEW-Mo-WENXrBrOtnFfA5Y2rxugfe2jKQWVW85dJ2yT3xLAuApECgwnb2RB0ja4T7M_vEfBNk058u4vcWcu3lT_HFOTwXn5zYeujsr6YscTevHX2qcOKTiJPU7u7VnvbNoDZJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8aghHekxvKC0nmToiQ1MFGU74gMRTauVbpfpTkCTn5Q5sGFM4QkGuscLS692Uh6EN4Eno3Ew1X2oQ8oFxFKAiSTqgoFb18KRQLm3JyJCGrXoueeHeHBgyT9gsv_mRdq01NS2y7zcxRvxmf71JS1zNr_hapKp79gctvomYyI6MiQvjCCSmtEnqq2Nqk1WzeFFbsd258CEIlO9Vewdit3JkL4Su0FLG-w5N6KeIwlv7HxPW4wIb7Ih7EIuFLBBPPwNPTbLXWA3j2DHLasPC70fJLxwUQrwhe8S7D13g4dELq8sYRq4zRnUd85a-1uf0ASxLgwjayo_d1h36BF1K4CTGRetY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8aghHekxvKC0nmToiQ1MFGU74gMRTauVbpfpTkCTn5Q5sGFM4QkGuscLS692Uh6EN4Eno3Ew1X2oQ8oFxFKAiSTqgoFb18KRQLm3JyJCGrXoueeHeHBgyT9gsv_mRdq01NS2y7zcxRvxmf71JS1zNr_hapKp79gctvomYyI6MiQvjCCSmtEnqq2Nqk1WzeFFbsd258CEIlO9Vewdit3JkL4Su0FLG-w5N6KeIwlv7HxPW4wIb7Ih7EIuFLBBPPwNPTbLXWA3j2DHLasPC70fJLxwUQrwhe8S7D13g4dELq8sYRq4zRnUd85a-1uf0ASxLgwjayo_d1h36BF1K4CTGRetY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svCCBZ-hAoRnOS-R-gve2-Ofeb7g4zsaG09j2cQO5KXy3ZsR0UW1ClpR33paBl0kDsvTECE0-5aHXtOCdP16VDPA2RS2HP2R1vWCUDsch4JSPqk8sxiZdN37MvrJthExIIBdB4mA6MrU7s-JdhXKTfQgfVovk_rsZHYbwjV5SQAvsgEdU2Tz7MP77VhcOvvTBoTKCJnKOeIt6jBsJyi2EGp5qSb-urqjkf3AVTvnbLNOKNPlrK3NOsa78BNnnT7_BQdxhQ_R7WGcZ9qfUBjdLi5OtHqcbyZIS3kGL-IFgXz6OkwVMMMZaOkDhIYmbbvQ9IycXSxggxxBjjaeyCJQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbZVk_8W3eLtdTmwG2HeJFhFd9qvM__x86kacUDSFwGe7HeqpP5C8eKXwWwUd9ygjQdnh7f-OexkcGz86Mw5Eyrr7zH48-vcwf2Oh-Y7HkZP18qoacD-h2kIpwaCIL-Rj_7QRsq2A2qqP16jOdSThLSWnbp5lLLcxw_mRs3i4mEfrgf9tiiQbP5uPq5dzgzQM5ZmLlFJM5QAJOwRYSzyqPRweTM3wI3x7sijqZqNid3rFEXoAj2MEh5pliibSwFIN4gEnEeKm7V7k5h85fcKGUotOfr8DBUgPIsDiW7HVWaOmYMxjyTaIuA-gLJAOntQl2LV8aifcv8_pADN_QocTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=mzqiqEKo4YkU6h6oQGisMHhCt-vSBqlrNCgcQrwSbFu6DbUeqyMStO4w-tas7qss20ize7bndcDhotZgIlJUU9i9rByrNtNnImNeGb10E2KZbnxc1x5FFVZ6pirH4s1E5osnR1Ca5H3RFqDrFrIHhBD1QG8cc6PE56sjeOhHtxQl5Pg2UfeYqhCZ8-dbc2cO3h6b6-fjDMcdCWojVHpVcbdDvYddcnN3QfktZIAILQ0Hw1-fAGm9Aykm01-bO5cXJzGVHdH34pYsFuTnalibTa2ksPg7kNu-Ku1WHTM9ubvak7D4lOCyInPeVL_E_LlHz1LTOAagSxMpe7fyuiIUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=mzqiqEKo4YkU6h6oQGisMHhCt-vSBqlrNCgcQrwSbFu6DbUeqyMStO4w-tas7qss20ize7bndcDhotZgIlJUU9i9rByrNtNnImNeGb10E2KZbnxc1x5FFVZ6pirH4s1E5osnR1Ca5H3RFqDrFrIHhBD1QG8cc6PE56sjeOhHtxQl5Pg2UfeYqhCZ8-dbc2cO3h6b6-fjDMcdCWojVHpVcbdDvYddcnN3QfktZIAILQ0Hw1-fAGm9Aykm01-bO5cXJzGVHdH34pYsFuTnalibTa2ksPg7kNu-Ku1WHTM9ubvak7D4lOCyInPeVL_E_LlHz1LTOAagSxMpe7fyuiIUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=Ynvc2r2Gbeyx8cr8oyX7BVPr2ZqG42Fsk_zbLDJG_SKMmXitvw-7pHYdwh3_ZNVZBwL8BLWBqkZ6zX4oPZOxZiNzYzIDtcV_XTx2rRge4jkqkdxPxRudUCvkv_cbWk-uI8zvjlFBOpinHZKaduMKQEn4b03PMv2lxlYUchAATt1cdq-7JaxPp2mSsw0U9eWdpEw5fw-EYm5BF4qKEvc30vFXwQd1hKJrR1J3zkZmWk4kWQz_gvynvaHdSTwdiKyhIA4h6_DuA49X6XtbA-1Nj0UXM_Px0Ur-4JKRX1B29lcdbdFMXYJ4eSGD-wCWw6U6f7yowQCRqPskBd8dZNUi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=Ynvc2r2Gbeyx8cr8oyX7BVPr2ZqG42Fsk_zbLDJG_SKMmXitvw-7pHYdwh3_ZNVZBwL8BLWBqkZ6zX4oPZOxZiNzYzIDtcV_XTx2rRge4jkqkdxPxRudUCvkv_cbWk-uI8zvjlFBOpinHZKaduMKQEn4b03PMv2lxlYUchAATt1cdq-7JaxPp2mSsw0U9eWdpEw5fw-EYm5BF4qKEvc30vFXwQd1hKJrR1J3zkZmWk4kWQz_gvynvaHdSTwdiKyhIA4h6_DuA49X6XtbA-1Nj0UXM_Px0Ur-4JKRX1B29lcdbdFMXYJ4eSGD-wCWw6U6f7yowQCRqPskBd8dZNUi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=rPoZASA8W4OqSH8YeV8_0SYAd_RMFbpPd-azqzpog8I7L1AgbI6I8_zyp5TNxRtSL6-gC_WHxAIzGXti1MQFIzpEKNj09odoUm-TazHm5SaqJ5po_9AXe0dOuLrLQHZQsoaCd2tgl3Cnoc4ZSwv2TgWVzjyp0E5uKp4oA8eveyJquaJmqupgPtKUB_P9GK0ZKPKMiwV-aP3HrsJEZjtL_vl9EuGXYqf8JRjMgA7D131LYBIi7AkXdekUXcaWATR9-xli2HiOb88ts6Oy2MSa_x5HdCyDNBtHAfIemh_1psudXTPY3gBw0H2AsSZraBOer5bFd1Pe_586R_UX2Ti2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=rPoZASA8W4OqSH8YeV8_0SYAd_RMFbpPd-azqzpog8I7L1AgbI6I8_zyp5TNxRtSL6-gC_WHxAIzGXti1MQFIzpEKNj09odoUm-TazHm5SaqJ5po_9AXe0dOuLrLQHZQsoaCd2tgl3Cnoc4ZSwv2TgWVzjyp0E5uKp4oA8eveyJquaJmqupgPtKUB_P9GK0ZKPKMiwV-aP3HrsJEZjtL_vl9EuGXYqf8JRjMgA7D131LYBIi7AkXdekUXcaWATR9-xli2HiOb88ts6Oy2MSa_x5HdCyDNBtHAfIemh_1psudXTPY3gBw0H2AsSZraBOer5bFd1Pe_586R_UX2Ti2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9w7imhLC0t998WVpkSZG4dOn5_JwQrlZP3ByYRQYXFDqPY4TaLy7j131-U5C6Id-G695ARSIAmpSZm7C6CJwybOArlFlCkv5qtyDxzoDO7e4Y2Ulom0ZHTchxxfo5uAPFAVZmqAJVEtFXTdD3hWWOjVw9xcQC87ixc2K0fmjIV0bD_HkUIky7fM6LXfvJz4zMI5hX-QzSWyFagQP6c13rPAAXQINBRzO5Pce2zBDy0_ZladXqd2vpNE4RPByOP5oP_oyDAH881SQYG3eCjngaM8jLuAFBk5gv7QPlQusYhXHDKA05WRalrE9_Y3KzxXgGgDm4Tt9TnFjb7iNewBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biLI8jbbNJsANQRBE7_fqAlrFqj_dDAHZTvzNHV7LlDWCYcNPH5GmJANmerFCeUybBWEQ7rcD1_gAZ_DDQslssS_9-hPtYA8a7ynL3Yqzk7t__cd-eEmiHpSl07D2DS30Fo0g39A3q0NwKievZqGSpYc46W37hgEhsL3GoqOkd5fGDeTeLFAbTmqIGugJxZT0s1XDOobAWgKQ0aMfQvBSpEsmSWH7GZrN2Z-9hNnmPg_ia9jVJPRkaWYiIAg__VHObb-1f02A0xZsQcTRcZHn5yY_1a7FM_fi-A_LCTIn61uBFdVJlwNlycPus7PVsDWUJaHHVfsUXwcko3GoXWl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=sacngiEUvtgJB7L1NE00Nd9F6JASfTcLrx-DkpXhjWSini1C4SbLbKPxqy6YjVHzJD6VS3aeZpe6gPrOexOPhFkhRwVcnIOrtYAg8NC4Q-nOBU71HZuj6B_ZhUgswqwp3nNBSl8VyBUrzxpkrt0ZNq31-CVQPWR9PPsfjp--0CSnuEqP-wHPbGSa_pMkCJ5z3huQ7jj5qcc1szrn6J05GyFp-hNO3ulgnh1J77eN80L9_ScXQIraqxxT2-k0st89fNzx2ULAmJw4IDBrqVIk4e1lkimxbxQwcuddpNf7gNqxruIEgmkqtpGpS4vld_KetlWwOQdIVr1MlBbum98whg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=sacngiEUvtgJB7L1NE00Nd9F6JASfTcLrx-DkpXhjWSini1C4SbLbKPxqy6YjVHzJD6VS3aeZpe6gPrOexOPhFkhRwVcnIOrtYAg8NC4Q-nOBU71HZuj6B_ZhUgswqwp3nNBSl8VyBUrzxpkrt0ZNq31-CVQPWR9PPsfjp--0CSnuEqP-wHPbGSa_pMkCJ5z3huQ7jj5qcc1szrn6J05GyFp-hNO3ulgnh1J77eN80L9_ScXQIraqxxT2-k0st89fNzx2ULAmJw4IDBrqVIk4e1lkimxbxQwcuddpNf7gNqxruIEgmkqtpGpS4vld_KetlWwOQdIVr1MlBbum98whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=fiN_XlTomIbpRiYY4_UTdDpRx7GetFZEIeLwOIojeGmIIvOkxd3lVullc6XYsCAQYEbWu4NMipEQcYftNBIPUKTY1aSUyNXMKdhIqIYFDCcEq05HhH--EAhbGtUdeKL9KboUXIohbOCZ6i0e5V9ayuqboaYEFQk6VB5y8Tp56Rj-uwK8pdO6_9FhYDFSf3zGtgrtAB_ii3nxrDQq3KtPUpLcSo2yls3MLBXy0J2TSG9AKIrIcCNb8L_-XsUA45z1ym6tGuqO8EeNZ1mZVcZmtzWT-gELOmGZOuFT2a0CS9otWrb4kB2p8sU39yPOdnanSHV93HtycKeiTTK6aJ3uWHzngvVUZYSSeaRLrzNTt6b8kc16LT0TlB1A0pMNhAz4V_xW-VImv37qPKr0dwY8ERfdX2CcF5D2dem1CC7SArEx9f011ESAR_yWiHGVkA99Dw3CnW12WBZI3_sP2VKAjE1UnOc8DxisYABUFhmaRBSJIPsLXV4AhamnuPFhL9XFCJFihC28e7REy0tnpbkEg8-iW4A_JPAjmkAfkZyQVC15nfvqH_jrmO1HrfQ4qEFhKfYbFRNe7gpRuOSN8_A8N4KywbfoUzEqxBITUdnsMP-RHlYAvlSDuEO93qKEDZgPKt1oXNVw34dXk_JCB77by3ZybPRGGmL2qKPqb0_eCOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=fiN_XlTomIbpRiYY4_UTdDpRx7GetFZEIeLwOIojeGmIIvOkxd3lVullc6XYsCAQYEbWu4NMipEQcYftNBIPUKTY1aSUyNXMKdhIqIYFDCcEq05HhH--EAhbGtUdeKL9KboUXIohbOCZ6i0e5V9ayuqboaYEFQk6VB5y8Tp56Rj-uwK8pdO6_9FhYDFSf3zGtgrtAB_ii3nxrDQq3KtPUpLcSo2yls3MLBXy0J2TSG9AKIrIcCNb8L_-XsUA45z1ym6tGuqO8EeNZ1mZVcZmtzWT-gELOmGZOuFT2a0CS9otWrb4kB2p8sU39yPOdnanSHV93HtycKeiTTK6aJ3uWHzngvVUZYSSeaRLrzNTt6b8kc16LT0TlB1A0pMNhAz4V_xW-VImv37qPKr0dwY8ERfdX2CcF5D2dem1CC7SArEx9f011ESAR_yWiHGVkA99Dw3CnW12WBZI3_sP2VKAjE1UnOc8DxisYABUFhmaRBSJIPsLXV4AhamnuPFhL9XFCJFihC28e7REy0tnpbkEg8-iW4A_JPAjmkAfkZyQVC15nfvqH_jrmO1HrfQ4qEFhKfYbFRNe7gpRuOSN8_A8N4KywbfoUzEqxBITUdnsMP-RHlYAvlSDuEO93qKEDZgPKt1oXNVw34dXk_JCB77by3ZybPRGGmL2qKPqb0_eCOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pybQL73tJA5Fy1rmSyKQuchTT1gytowbRa7zu9fuhSpLlAm-bEEviiNWNfqJcFVOfek43tJOaICciJyMcwoaw5uuox58mU_j9Q_Mj4tmYs0QZutuEydiq_SgtGGj9BQ38uEMdrvRFDFqbduiiwAbDF4v6wbO7S_XUv4EXEe_orroTfeVfEQ_xlbYrue73qdqDLlQ9cowlPUnW7DEG_jllqxWgSyb5f_PvBFMf3rSF821Vkfr2kk2dhRfOdDLiGz-e53uRMz-jWAIk3RC7Asl8DYGfOdD1BXjSFZ_6UBkcw7TEtNwfbOapvf53taDnCP7VQo_0g4Q_74FRvULjrAcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=qZvDSVp1jVYHbHqhvsSySOALGyhUXpwE2CQVQ4W3Jjvsi9Kpn3kSGhqfYIal05SOFacjOS4S1tAyVf8dsSYXcQd7BFHIPd9e4xulH2SLjPwp5wyqd1OhLEQaUGgzgwM2LEaHecbUGrpZl2V5YpZVpWgOIU3aAGqJNT9eN-GlffAJWmv3SBhFioEgaCwavmhhtpgtTdBuC9LuJtg8QjMK4pTKJtaRg2L0Fr6bmmMuuF25cLSaj3Q7uRJU97OWMmG-Y1ymZwWOiBQEYjU7AU9yCZPTXHgjo5G7NF4A6qk56kw2it23-HWrFUJ0Sx68nB7kkauyTqXLWYxf-bvaCawASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=qZvDSVp1jVYHbHqhvsSySOALGyhUXpwE2CQVQ4W3Jjvsi9Kpn3kSGhqfYIal05SOFacjOS4S1tAyVf8dsSYXcQd7BFHIPd9e4xulH2SLjPwp5wyqd1OhLEQaUGgzgwM2LEaHecbUGrpZl2V5YpZVpWgOIU3aAGqJNT9eN-GlffAJWmv3SBhFioEgaCwavmhhtpgtTdBuC9LuJtg8QjMK4pTKJtaRg2L0Fr6bmmMuuF25cLSaj3Q7uRJU97OWMmG-Y1ymZwWOiBQEYjU7AU9yCZPTXHgjo5G7NF4A6qk56kw2it23-HWrFUJ0Sx68nB7kkauyTqXLWYxf-bvaCawASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=sa49VPpMOI04T5iaWG0fB791-RimSEX73Uovu_7Qcj3MlfAFmSwCEB6yyiRrLNZD2G6ceTOQ3QOVA-M4wZn-qFmwxGP2329poduzXqFVTy4ynIRMjf6fqKm944dHe7DgGGjAyvUtAlMEyTflpVsrgt2evYl-e_3jvYma9hpU27xh1UYXdNzHZmlE_aSGVkAzF4osV0MPnQbmgWOi4GGvpM3q_Qqh64syyggknevBqXbvMFXmGQzLN2h22T5LMFBPk0SldwfNF49yggOqX6Db0JkrWJaSXmiSZFRF1zGyXV-sQrUh6haA9JsdpScFrRs-aTETUFxk5NAdLRLgLlioUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=sa49VPpMOI04T5iaWG0fB791-RimSEX73Uovu_7Qcj3MlfAFmSwCEB6yyiRrLNZD2G6ceTOQ3QOVA-M4wZn-qFmwxGP2329poduzXqFVTy4ynIRMjf6fqKm944dHe7DgGGjAyvUtAlMEyTflpVsrgt2evYl-e_3jvYma9hpU27xh1UYXdNzHZmlE_aSGVkAzF4osV0MPnQbmgWOi4GGvpM3q_Qqh64syyggknevBqXbvMFXmGQzLN2h22T5LMFBPk0SldwfNF49yggOqX6Db0JkrWJaSXmiSZFRF1zGyXV-sQrUh6haA9JsdpScFrRs-aTETUFxk5NAdLRLgLlioUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa90oHzGF2SCIK73nEWtUe7IwGmFLPJ2_NOavNj3exYNl-M1xhEpkIsIZa1zWhleROWaYCa7vL8KYmK-zkMaFMquPRR-7F1kxKZz0hKA8omg2kOytRIuz_c081A44DoQ62zgt-GgrwS0Ib-8WwpzXPH1meb1btRh698fP2FksN5pLKk02W7ddUpO6-P9Y3w0ZQV5yjp-8kSQvVK8upabtUirL2PAIgcZ88JusXiIpNCznRvlkTpJif0Btgav-6dQRhkzf1b3unCUl7QXnJA4wye3J3gBlcXb0pLeRU4DZU9I7WGzoxJ8ihkDLspx_rUsRxMFHfLOYDzeiToAQzMRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7yYOpR_xoWpGSAXvHrc8O6PauO_lIb-KonMRkBO5KeUpjWFceGOKfQkSvgdicA-reG3qSsGPTfUthEafcQWtAmH5C5vdVs2ptupIPXWGCuzPktHUdMKYdwPdBiwMmhdkbTjvLk4rS6nY93SShqsa1b6UH4XbmCs2kJ3noHkycyCaCUJeMWlyJYEGGTeOxBXwRa7nODOAzEiDXQoDJtTPbZ0MD0uiGovP4VdT6rLQR2OIU_W39i-Jpt-nFHYE_AW93794DQEVSobqFBcUm_1weUOogQI1t7-UEAa6Z3GMmj9y-82jVMKV7u5kz3Pklded41gd4KZwFW7KhmsOp-AyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=aDU2gFg9zZlkPkzLdsSzUvPlKJZPdRuGsJ6ILzjNWUaffTrhkY2Sdh4jv-dkMKjMl9-iyCkM1j6ZjfZkAVcYMJGzsrEZh60A0vF-MG_0SJZ8fZrRwL4ibq1z3AUcOmQZ00kBHNfZjB-YN5Gl-EwWbOhCBoPUzkRlYR1AxQHD_kBdraIDdxn1Djbv55I8LV2Zr7GSwzfKL5yOdzl1p4YN3xvpuh3qyfjpt3N2Lo9crXvuuG7QKBExi1YqkWp2623FA0777Esuotxu46ZeKvkjAn0S32MrL5is6r4YHwNxStlRpK7T_cOa-QDmZKXzeLqPLVgogoUL-0j8j0oCGpJh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=aDU2gFg9zZlkPkzLdsSzUvPlKJZPdRuGsJ6ILzjNWUaffTrhkY2Sdh4jv-dkMKjMl9-iyCkM1j6ZjfZkAVcYMJGzsrEZh60A0vF-MG_0SJZ8fZrRwL4ibq1z3AUcOmQZ00kBHNfZjB-YN5Gl-EwWbOhCBoPUzkRlYR1AxQHD_kBdraIDdxn1Djbv55I8LV2Zr7GSwzfKL5yOdzl1p4YN3xvpuh3qyfjpt3N2Lo9crXvuuG7QKBExi1YqkWp2623FA0777Esuotxu46ZeKvkjAn0S32MrL5is6r4YHwNxStlRpK7T_cOa-QDmZKXzeLqPLVgogoUL-0j8j0oCGpJh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=ay8eGeNTf46p-xTvlqi4zbr4AF8QLPt_5hkic0STugpPp5_RR_wgg37P2hMmARpskm0dIH43bvDUxU6sbBtVa38s4PXDYXAX_Fx7lj-aVfVG7E8rvpJqDysz0kLUDey6fxXC9ahayauYVzQfKclWrKrjUuHh4bPUSGkXko4HoeilyDblO4ZKyBbz0MVZqphsYU1apsd4JjmvhbCnn9L3wDxvbZvaOGgEE44nkdj2Q3g7HSlwKuV2gYsZo4Hw_9XAD0JGv8e4XEdRUeco5KGnaeGlZbHnMF-RmU4bB54KIC3MEHQqKWQ4ZANuCt4GwrDyKayDX3CSXtTVJ_NOpfUkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=ay8eGeNTf46p-xTvlqi4zbr4AF8QLPt_5hkic0STugpPp5_RR_wgg37P2hMmARpskm0dIH43bvDUxU6sbBtVa38s4PXDYXAX_Fx7lj-aVfVG7E8rvpJqDysz0kLUDey6fxXC9ahayauYVzQfKclWrKrjUuHh4bPUSGkXko4HoeilyDblO4ZKyBbz0MVZqphsYU1apsd4JjmvhbCnn9L3wDxvbZvaOGgEE44nkdj2Q3g7HSlwKuV2gYsZo4Hw_9XAD0JGv8e4XEdRUeco5KGnaeGlZbHnMF-RmU4bB54KIC3MEHQqKWQ4ZANuCt4GwrDyKayDX3CSXtTVJ_NOpfUkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTEP_pCa15XHmMB2nVcVDNZR4abIbvL_4BM9sVrHe3gc6rleEiQuwnb24eYg0hmRbWMkm6gv0bZvy75nkEJXjDHHpn9GpAxoYZ9Y0ehtaQjEH-ln_WX0scFfMA8IdG87t_k3nwjepzF7s5NbyntfifCUCT7wUZykjU3rBkCobLK6ib2LiqzoD28j_FNGgDXtQynf3hN_RhwgAnyavzZe__F0s62fdSxtPMV_ZAwZo1rHpa-sfB92e0EK944KaPO-wMsfkJXoNTeoFajcIB5mOsBo_UEQBoWHVRQBO-v8dXY-wyxVzkfrif0FDlzt1ph-kI-ecS4yWqByVyFrM3_Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqT06tdfaYOotH5YYpo-1J_gQBn-3ubyAra6Dt5IXPhBvjVGDKWvhn3tnICT86fo7lDt59Ux8tQSvubwutPAVi59rfIXvp9S4Xxfgs8hkM5S4JnrQKJXDb0vHGzZPUw6FmkkiHCYw5VRzf27yFUBTbbA6Ts8isLEX6CtvjZ3JfO6utKFqs9c_FXjqW5wTjeid9HajcnyoLb_KMpPNrEnjgHFdH2nfIVk2Jo_VIZqh0hT92vMEaInTVY-biW4OE1Xezs1qeECY5-5XYSfqae1NIvrh9FSuxAJOccbZtABI3W6keY86KDRT_QeiMVjM8NbWqmJcnIjiE0pEujKSY0uTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5TpZFCq2Vkp0npJBM4CzrszG0eqj0IwA9Ks_oL9pQqRuvQGLCoy-kyhiXH2FTF88FfP-1-kaAhqb9r8eduZFV9-SNsxjXR_GvhPg7DL-P2jtedZJaRDuRECSl6g0puzt1wy88KrykOJnTGn30b-_Sel9LQomkRa0LtsJFKlgJcmEjJg1tBwfU23IbPGUEMn2JRXQ_kh2UsOYg6r0Oop7OXUWvSFZRoKSktTCv1qvvfRdhaW4pGwaVVHCkOfQue0MUj26lZNeezpjZyrf63zTyeP3V-wUrYCnSYE1AswN_-WxK1T6D2a4Z_fNRab5DNnGbIB31AqFr0FEwgdmQO4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDhYuLSXHkEsGMISfzqp2TiK8z6lPWEiYImHvOSQhJgw3Oge688r8TmSosmLyluxAIHFa2FzBg64vKURVW-LYF87FntFWlMqMrAjMHE47KQz03AaLrITcXqU0ufsaWzT9TWE3OK-9Qyv9m14qhw_ez0PgVJ-Ultej4eCCQOpokvTAYdejYv_K4V8JaoRhdmnf5Bo4O4FCotlDdGXFFXxjBH9LWZl-HxbYLLiXuj8KN7AO9D6tXiXC83F1nvf_2zOMJt2S3WcI4R0C_LkPt0UW3bup9XN343tYJWVBSVHS8PmSI0qbjCqniwuL2iHcTjcmhZh6V5iI8rR4ZLg_ls4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
