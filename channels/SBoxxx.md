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
<img src="https://cdn4.telesco.pe/file/db90F712AeJFnLnDt7gj4x6UmXMQz3gRumlwCruerUqlCD9Vo6T8aefjLWYGzaAqX3LfaoLAxqsX0r2Lzei26p7rWzje6M_sel4MriJUYyrsMT2OKdTSCoSF9hhrqb2h6c2B0B4Mmy9pzPf6UAWUhUPVFdMlUtaIeL1lfVpKqfRm8viffPCMk0gZ3-wa9s0UO91TzSZhRGsIu3fWJDmia0600pl36vxbr8d3HY3T0bzYr3gxOc0PVKoBd8-or1tTEkMPndKx5Tvze58jfbD8yNfzRDsew_NbSP7FtyRixE4G-JtAvKah_zU-Zq8WYrVNq59o2TYKGXcM-ABIf0AAvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بقایی:   مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/20626" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بقایی:
مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/20625" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/20624" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Avnq3B2CfWWiDjpNv4_lQv-9CSouO2RNeHLMWHHzHhmi2rXkZTd8CEWVrSno6lS6hjyQ-EYyE_hJf5ahZaDIgIOHaOb2A478K1uxkxA30U26TA79x7eAn-NOmMYLbCCwBCFPSB7EZEym_B70z3_RJNRafXX-U7ZWF6SRr3KcozPKBLsiQFiGooB1clh78HO5TXEfac_jGZ4Zowr-KSsnSBKgLanMTX51BUPgwORUA44wYeTHLkRwYgMa27PqN0U4yRN7Nx5qPMAdvyZVD2Mu1bXu7WgaASmYfKFFwvC64zjh_EhDFwPLlTsYEKzDmLEthbN3gfkjFgx-QvntWfB5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Avnq3B2CfWWiDjpNv4_lQv-9CSouO2RNeHLMWHHzHhmi2rXkZTd8CEWVrSno6lS6hjyQ-EYyE_hJf5ahZaDIgIOHaOb2A478K1uxkxA30U26TA79x7eAn-NOmMYLbCCwBCFPSB7EZEym_B70z3_RJNRafXX-U7ZWF6SRr3KcozPKBLsiQFiGooB1clh78HO5TXEfac_jGZ4Zowr-KSsnSBKgLanMTX51BUPgwORUA44wYeTHLkRwYgMa27PqN0U4yRN7Nx5qPMAdvyZVD2Mu1bXu7WgaASmYfKFFwvC64zjh_EhDFwPLlTsYEKzDmLEthbN3gfkjFgx-QvntWfB5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/20623" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در استرالیا استفاده از مواد روانگردان برای مصارف خاص درمانی قانونی اعلام شد.  پس از قانونی شدن ماریجوانا در بسیاری ایالت های آمریکا، قانونی شدن استفاده از مواد روانگردان طبیعی در موارد خاص در استرالیا پیشرفت مهم دیگری محسوب می شود.  شخصا باور دارم که بزودی…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/20622" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/20621" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFv2Ciz28CyHCzt84EHWxFz4HGEac5iG1Vz_tJDAmUlUwa-xCR28yyEXod_eMIYvvnfsDk8B9LwQokpuCuWdRaaY_9wG1q15W-kFadskFVU1K7iXuPVu91XXHcjGIEXAWkfRQDfzYmHCNuLWAlgdn8W83R1039phMIRY8Cu1UGF2piO_eb0fhDBmCiPg4vINeaV1JDApEthJQ63Q-8PZ9jW-B7ALmTjTswmG_4qqFHkhFk9zy04owhqqyiumvab9ZtvFrLyvStg4fNbyI3oWHwuUrbYSBnRdmDwrjBiEJ6uxPWiyNgiG1RLvVRikgCpGFe9T4umBcJSHCzZb_HnRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/20620" target="_blank">📅 11:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2_2AbHS2eg_zzTeAScPbU3la3gDtW9ppzHRubOsI9ytJkRZOA-YvJxv0s88Mx9Lnzwn6FNd9Gtm2TEWrL4IoZiZmpZqwDeGpiD1LUUBKrCfhTmP5Z1rncrOupb3dS9RqJAl_YVf7gknLWJ_qZUoV6xlJtshvwnIVvUPpae__cC9-qRTQmlb469ioP8wU-haU0ZK5WFN6Xpcfjqp37SWTrydYh-ZODbOkwg3LunrFT6cyrvFukVI3t0fjcwqt5PzDBN-fV3dPx4QoyCOeab5Zki1dnlbQrZJG5G4Q5AtDB9sPMz9SUBSzu6ze2gDefYRj92v46DLi47VsVgcZ7QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/20619" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/20618" target="_blank">📅 09:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">— به گزارش رويترز، پس از حملات اخیر ایالات متحده و ایران به تانکرها، حجم حمل‌ونقل از تنگه هرمز به‌شدت کاهش یافته است.  داده‌های شرکت کپلر نشان می‌دهد که میانگین روزانه کشتی‌های کالایی در ۱۰ روز گذشته ۱۰ کشتی بوده است که کمترین سطح از ماه مه به این طرف است.…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20617" target="_blank">📅 08:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIhHfOVlNpuOHrb2CRgQmc7kowTt6VfjYCeP4EDzOrYu-XcDcfZLyF7Arg9aOPmmopOW0p7oyPcoF-H9GCVwVuFnCdm4CuWwKrGbc2XE7cy7Fbmta8Ryhl9Xf0w3xXgswWTendR2Vl5Uqg8IA345TY4ixI_XWLYczkKLf---SdUoDVVue4wdvO65X-3f0-9WnKY1tSn6eNGjm1iejPQgqliQ7KvsdCo-i5NFaEGenG5SBK4gy-LbEh22aSlnlhcQN3gNg0HurNOIsYbpohJzEZqV3B_2WKb8yYmhMyzz7tzBx31Hstk41B53Y7TqY6JfOCPtdqoHiq_r5GyGAsEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!  به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/20616" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20615" target="_blank">📅 02:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhzIpv0RuHb4F1TlC9qZh9iuRG0HVn2M1vr9aBGHx5uExejVgUsxvkj-3sgC14mmMhv0JL5K_P5tvOWMaroNdvjmPebFDeNjtGdz-eGjUxj_K4-lPm4W8qlFdbZ7ZHVU-voj3TfBX2gaAl2mooEL1GBFkGS6q8dN5CbI3NogI_2fUeI5yKWL_qm4qcrObtWhUGwE1ECW1duFd8vtzilX9llrDGc-v5ISuxEaMiiiyxSEDmFlPj5P9ehR_n43TQDWivITvG2VfkQLeDDuYFvIzZ-yLP4NNU9zG-H8RqBRbmcaUjLzx-YVgIWbYHBmxB5ZAH_URrwLhtnHDnJv-aCqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه میان‌مدت ترکیه برای سال‌های 2027 تا 2029، افزایش 229 درصدی در هزینه‌های دفاعی را پیش‌بینی می‌کند، که از بین تمام دسته‌های سرمایه‌گذاری استراتژیک، بیشترین میزان افزایش را داراست.
این رقم، هدف کلی برای سه سال است، نه افزایش در یک سال معین.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20614" target="_blank">📅 01:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آیا ارمنستان در حال تبدیل شدن به هاب هوش مصنوعی آمریکا در قفقاز است؟
ارمنستان در حال ورود به مرحله‌ای جدید از توسعه اقتصادی و ژئوپلیتیکی خود است؛ مرحله‌ای که در آن زیرساخت محاسباتی هوش مصنوعی می‌تواند به اندازه فناوری نرم‌افزاری و استارتاپ‌ها اهمیت پیدا کند. راه‌اندازی کارخانه هوش مصنوعی شرکت آمریکایی Firebird در نزدیکی هرازدان در اوت ۲۰۲۶، این پرسش را مطرح کرده است که آیا ارمنستان در حال تبدیل‌شدن به یک پایگاه راهبردی آمریکا برای زیرساخت هوش مصنوعی در قفقاز جنوبی است.
پاسخ کوتاه این است که هنوز برای نامیدن ارمنستان به‌عنوان «هاب هوش مصنوعی آمریکا» زود است، اما شواهد موجود نشان می‌دهد که این کشور در حال ایجاد زیرساختی است که از نظر مالکیت فناوری، تأمین تراشه، نرم‌افزار، سرمایه و مجوزهای صادراتی، به‌شدت به اکوسیستم آمریکایی وابسته است.
ورود
Firebird؛ نقطه آغاز یک تحول بزرگ
مرکز ثقل این تحول،
پروژه Firebird
در هرازدان است. این شرکت آمریکایی در ۸ اوت کارخانه هوش مصنوعی خود را به‌طور رسمی افتتاح کرد و اعلام کرد که برنامه دارد تا پایان ۲۰۲۷ بیش از ۷۰ هزار GPU شرکت NVIDIA از نسل‌های Blackwell و Vera Rubin را در ارمنستان مستقر کند و ظرفیت زیرساختی آن را به حدود ۳۰۰ مگاوات برساند.
این ارقام در مقیاس اقتصاد ارمنستان بسیار بزرگ هستند. پروژه فقط یک دیتاسنتر معمولی نیست؛ بلکه بخشی از مدل جدید AI Factory  است که در آن برق، سرمایش، شبکه، سرورهای پرقدرت، GPU و دسترسی به مدل‌های هوش مصنوعی در قالب یک زیرساخت یکپارچه ارائه می‌شوند.
دولت ارمنستان حتی ارقام بلندپروازانه‌تری را مطرح کرده است. بر اساس اعلام دفتر نخست‌وزیری، در مرحله دوم سرمایه‌گذاری کل پروژه به بیش از ۴ میلیارد دلار خواهد رسید و حدود ۵۰ هزار GPU جدید NVIDIA Vera Rubin به زیرساخت اضافه خواهد شد. مرحله سوم نیز قرار است ظرفیت کلی را به بیش از ۱۰۰ هزار GPU و بیش از ۴۰۰ مگاوات برساند.
البته باید میان ظرفیت فعلی و اهداف اعلام‌شده تفاوت گذاشت. تحلیل‌های مستقل تأکید می‌کنند که رقم ۷۰ هزار GPU و ظرفیت ۳۰۰ مگاوات عمدتاً یک نقشه راه توسعه تا ۲۰۲۷ است و تحقق آن به تأمین برق، سرمایه‌گذاری، تحویل تراشه‌ها و وجود مشتری کافی بستگی دارد.
نقش تعیین‌کننده آمریکا
وجه مهم‌تر پروژه، صرفاً اندازه آن نیست؛ بلکه منشأ فناوری و نحوه دسترسی ارمنستان به آن است.
شرکت Firebirdیک شرکت آمریکایی است و پروژه هرازدان بر پایه فناوری NVIDIA و زیرساخت Dell شکل گرفته است. علاوه بر این، توسعه مرحله دوم پس از دریافت مجوز صادراتی آمریکا برای انتقال هزاران تراشه پیشرفته NVIDIA به ارمنستان امکان‌پذیر شد. دولت ارمنستان می‌گوید مجوز اضافی برای ۴۱ هزار تراشه NVIDIA GB300 صادر شده است .
این نکته از نظر ژئوپلیتیکی بسیار مهم است. در عصر هوش مصنوعی، کنترل دسترسی به GPUهای پیشرفته عملاً بخشی از قدرت ژئوپلیتیکی محسوب می‌شود. واشنگتن نه‌تنها بر تولید بخش بزرگی از تراشه‌ها و طراحی آنها از طریق شرکت‌هایی مانند NVIDIA تسلط دارد، بلکه می‌تواند تعیین کند چه کشوری به پیشرفته‌ترین نسل‌های محاسباتی دسترسی پیدا کند. از این منظر، ارمنستان صرفاً یک مصرف‌کننده فناوری آمریکایی نیست؛ بلکه در حال تبدیل‌شدن به محل استقرار بخشی از زیرساخت محاسباتی وابسته به اکوسیستم آمریکا است.
«دیپلماسی تراشه» و قفقاز جنوبی
اهمیت این موضوع پس از گزارش اخیر
Wall Street Journal
حتی بیشتر شده است. این روزنامه گزارش داده که دولت آمریکا در مذاکرات مربوط به توافق صلح ارمنستان و آذربایجان، از دسترسی ارمنستان به تراشه‌های پیشرفته NVIDIA و پروژه Firebird به‌عنوان بخشی از بسته اقتصادی و تکنولوژیک استفاده کرده است. WSJ این رویکرد را نمونه‌ای از Chip Diplomacy توصیف می‌کند.
اگر این گزارش را در کنار پروژه Firebird قرار دهیم، تصویر بزرگ‌تری شکل می‌گیرد: آمریکا در قفقاز جنوبی فقط به دنبال روابط دیپلماتیک سنتی نیست؛ بلکه می‌تواند از فناوری پیشرفته، سرمایه و زیرساخت محاسباتی برای ایجاد پیوندهای بلندمدت اقتصادی استفاده کند. این تحول از نظر ژئوپلیتیکی قابل توجه است، زیرا ارمنستان در نقطه‌ای قرار گرفته که میان روسیه، ایران، ترکیه و آذربایجان واقع شده است. ایجاد یک مرکز بزرگ AI وابسته به فناوری آمریکایی در چنین موقعیتی، می‌تواند حضور اقتصادی و تکنولوژیک واشنگتن را در منطقه افزایش دهد.
چرا ارمنستان؟
مزیت ارمنستان فقط موقعیت جغرافیایی نیست. دولت این کشور طی سال‌های اخیر تلاش کرده است خود را به‌عنوان یک اقتصاد فناوری‌محور معرفی کند و از سرمایه و نیروی انسانی دیاسپورای ارمنی نیز استفاده کند.
اما مهم‌تر از آن، دولت در حال ایجاد تقاضای داخلی برای Compute نیز هست. در آوریل ۲۰۲۶، وزارت صنعت فناوری‌های پیشرفته ارمنستان قراردادی پنج‌ساله به ارزش ۲۵ میلیون دلار با Firebird امضا کرد تا منابع High-Performance Computing را برای استارتاپ‌ها، پژوهشگران، دانشگاه‌ها و فعالان حوزه AI خریداری کند.
این اقدام بسیار مهم است، زیرا مدل توسعه صرفاً بر صادرات خدمات دیتاسنتری متکی نیست. دولت می‌خواهد یک اکوسیستم کامل ایجاد کند. همکاری دولت با شرکت‌هایی مانند AWS و Mistral AI و ایجاد «Artificial Intelligence Virtual Institute» نیز بخشی از همین تلاش برای ساختن اکوسیستم داخلی است.
اما آیا ارمنستان واقعاً «هاب آمریکا» خواهد شد؟
در اینجا باید محتاط بود. یک دیتاسنتر بزرگ الزاماً به معنای تبدیل‌شدن یک کشور به مرکز نوآوری AI نیست. برای ایجاد یک هاب واقعی، ارمنستان به نیروی انسانی متخصص، دانشگاه‌های قدرتمند، شرکت‌های نرم‌افزاری، سرمایه خطرپذیر، مشتریان بین‌المللی و مهم‌تر از همه برق ارزان و پایدار نیاز دارد.
مصرف انرژی نیز یک چالش اساسی است. صدها مگاوات ظرفیت AI برای کشوری با اندازه اقتصادی ارمنستان عدد بسیار بزرگی محسوب می‌شود. بنابراین توسعه Firebird به همان اندازه که پروژه‌ای تکنولوژیک است، یک پروژه انرژی و زیرساختی نیز محسوب می‌شود.
از سوی دیگر، رقابت منطقه‌ای نیز در حال شکل‌گیری است. Firebird همزمان در حال توسعه پروژه‌های زیرساختی در قزاقستان است و برنامه جهانی آن تا پایان ۲۰۲۸ به حدود ۲ گیگاوات ظرفیت می‌رسد. بنابراین ارمنستان لزوماً تنها مرکز منطقه‌ای این شرکت نخواهد بود.
نتیجه‌گیری
با این حال، اهمیت پروژه را نباید دست‌کم گرفت. ارمنستان در حال حرکت از مدل سنتی «کشور کوچک با صنعت نرم‌افزار و استارتاپ» به سمت مدل جدید «کشور کوچک با زیرساخت محاسباتی استراتژیک» است.
اگر برنامه Firebird طبق نقشه راه پیش برود، ارمنستان می‌تواند در چند سال آینده به یکی از مهم‌ترین مراکز GPU Compute در اوراسیا تبدیل شود. نکته ژئوپلیتیکی مهم این است که این ظرفیت بر ستون‌های فناوری آمریکایی بنا شده است: NVIDIA برای تراشه، Dell برای زیرساخت، Firebird برای پلتفرم و سرمایه‌گذاری آمریکایی و مجوزهای صادراتی واشنگتن برای دسترسی به سخت‌افزار پیشرفته.
از این منظر، شاید عبارت دقیق‌تر این نباشد که «ارمنستان در حال تبدیل‌شدن به هاب هوش مصنوعی آمریکا است»، بلکه این است که ارمنستان در حال تبدیل‌شدن به یکی از شرکای زیرساختی آمریکا در جغرافیای جدید هوش مصنوعی است. و این تحول می‌تواند پیامدهایی فراتر از اقتصاد دیجیتال داشته باشد. همان‌طور که خطوط لوله نفت و گاز، بنادر، راه‌آهن و کریدورهای تجاری در قرن بیستم ابزارهای قدرت ژئوپلیتیکی بودند، در قرن بیست‌ویکم GPU، برق، دیتاسنتر و Compute نیز می‌توانند به بخشی از معماری قدرت جهانی تبدیل شوند.
اگر پروژه هرازدان به ظرفیت‌های اعلام‌شده برسد، ارمنستان دیگر صرفاً در حاشیه اقتصاد دیجیتال قفقاز نخواهد بود؛ بلکه می‌تواند به یکی از گره‌های محاسباتی شبکه AI تحت رهبری آمریکا در منطقه تبدیل شود—درست در نقطه‌ای میان روسیه، ایران، ترکیه و آسیای مرکزی.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20613" target="_blank">📅 00:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20612" target="_blank">📅 00:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaun1exgxcr5o6BgqTwxpjp8U2FAxq1Tl5QcY8Wfrg9PZbH7RGQiHZZwx3MnWOyEthIpmcqF0NNFntzkgtePxx3HGFsow_ORAuufL8-Xgu2it2O0WqhMlolrcxupTOhv22TL02W9fPGakG8j1PGK-UXAdrd9zOxpQInbokZny9tC9WNGVq_cEKCjigUKFkRmwHwcvdA14ujEnqYF9fmnXBIp78dzQHOvra2mcfvSIwzknWhvDmxaAPRIvfzzhZtDHnI9peP2prz9UVQCCoKCe01a3t-wqstY10e1ZrWnBoQsCZ7ZRfhPEdgCqRRre7v5y0fT2Qfnqy0exZSerqIWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!
ولی همین که نام Persian Gulf را می نویسد باز خوب است</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20611" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIhjeQQTk5_lWggEA94_h59HCAHS9ckn5pIqskvsnhO5aohZPk_B3_yGapFbZ9BJNpmxCERMLoU4PrjeRVeht_y01oM1s7opjvvXJZ6m23kN8JX4dOKGvp2FWh8y03tQ03CPKUeCI7bM7b25LwTsYS3nQnIRp7Vo2AljtapKG3Pztlp0tmxemxyvFbybpd28igILDzUrDZoN3sKZ_2vjTMtSj5t5hhkOm79a2sexT3IAbFuORtfnMmwLTM7tT5nX6SN5zHWf_M8aGCBPXCefPA21oBtudPqLgPUuf209U7tdA_AdfXMqrVKdvobGCZZBQZNB2K8SWq_v5WyC_Y0g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20610" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سرلشکر رضایی:
برای داشتن وحدت باید به رهبری نگاه کرد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20608" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDwxTf-DrfFrb3nnp-2AmyED1O2z1b_oxj-b900p_bm6AsPK_kPtfygNNidiVomosCDV12Gh0Y6imt1lXfQTiP_akVd_MorlEfQtmgfrtiNxfpqim9pghirZtipHehJ-D7W-9oAtbCW4rNNuxojFBVPaREAlaVr_kVT1OH-_z04XV_746eJwnoVIuU97_2t0Kfq-BFHvwt-Z25y5fQZwhkGMoPYxm1AVzZq350v0vC13LXp6Xf7r9W_IlSuq8tV09Vq135dPH-HNe21MkvUOQ941U3s2SIlXPXVSu2L-1zerXRLaSe5jngraFNe1PVudCtWaXnYCFMbwaS_Jhbzzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20607" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTFRqtJqr7HGSDE_gWrwHsLaYY5AcH2OG418MZKx8xpPvi_6TJd4_BuHRo4deJ8dRAoYOLZPTHnlQWlskneo_mnDiWiEeTUhwVWJi8nC6jRMv1qLhf2wfFZROx1vGF0qX1ijVZ-Knqg6ugjsCKZEasQq77Ro3neA_jQzqWZWclwJahlSPoHoIAhdDxMs9EeSbR2a4ravVxB-TJjGLpPW6RmF2nQ2vzmMb5AZTpa5ok9GqHMx9l9mnQUmhVzeT6JeY_b15parafngr6o_ysZDu3eHPgx-xzRIrPRduNgbVNDQMafHZGXvHlznzl6elS5gi0zbnf49bJM-ngaId5YCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه ما خیلی سلاح های دیگرمان را تست نکرده ایم   مثلا شاید طبق مورد ۷ بخواهیم کوههای البرز را ببریم تنگه هرمز تا این‌‌ تنگه برای همیشه بسته بشود و اسمش هم بگذاریم تنگه ترمز!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20606" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سردار رضایی:   ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20605" target="_blank">📅 23:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سردار رضایی:
ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20604" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH92k0wLuKtujwtZZWabGhRiiLtAO54fzR6O3lTLkhWxgBXq_DXa5AmHQ2Yx6FuskNp58k1Q_6HyrBnwRDygxUJ33O20KSiJwWGQwnUkPgNBrn98eWTD1VjSMf_DJ4HhnD-I41SN_0aKYgpfkh2D1ToQc7DQ5_yAvVYypvpYQdB3f0O5BKcjQ5XGnLOlAjJ3HctPntr11rF08b8Ug6THLpClaMD1sGxmkKmAxB9RR2fhrJhgB-ZYZ5d9fH5oS95S8qOc9YRSFJY8nQHYy5zaK-Mplnyde_yPym7ERR4Y_cYY0qR2yKH7097tUMhuCBiGvloY_zc7w7GRELb9U-x3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20603" target="_blank">📅 22:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G009UnlJ6--dlFs62G08PWYSAFlkQiywpBjdaF_tGkjlFGRU_IKZkIzSYekzbHbBBMVyis9D4uuUroDDxet2UBkP8pdZ6qGXtrKa7iIVk5vxc7fcgK_wYKKpRASupRmeT8hsnOJnmrLpxzt4r5p8U8PZOZXal6IoUGWPiHd7yTRTf-RV5teziCeSrSjQEk5SIul4Jxucoaspf6NtFPrzJ4HGSEIOoA2n2cBjxU1blLaLeP7vQSwKsRNtf_KRylVX0n7CvYdYnnmnzabz6agHuKFS6-sgHyRABDKo8tMF7AgmV34bfzhlURhGKk8uV0bNLLswvWE7Dg1ExuZBiE372Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!
به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20602" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20601" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ52NCDFwpbMbcVNkLrO98cnQgub7rqTzcmrtpCChMj6W5hk65a-sRRo0oPXeB1dI7LwMRB8X6_1cieQelGrWot39kIPWHU8LN4I0BkWUB9xB7TGrEyHOeej9tlbQTIZjKZ9PBLVMDkSPjR8BuQE9bJG1osUijw7kfa4CMwzRCuirdL-9emyICWUC7xsrrTnJTz2WOiox4r9WxXDeuj19me-aFtEA80K9p71TACQcrlXwKtTtWjvV63hkSHnt-j_HTFwxX0-UuEWqwTgnNerKhydiaSuH2drPBll9eiN9tOR60l5dyOfPDWWuoUbDR0MvvqMiD0DTeZDHS47Vvoa568c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ52NCDFwpbMbcVNkLrO98cnQgub7rqTzcmrtpCChMj6W5hk65a-sRRo0oPXeB1dI7LwMRB8X6_1cieQelGrWot39kIPWHU8LN4I0BkWUB9xB7TGrEyHOeej9tlbQTIZjKZ9PBLVMDkSPjR8BuQE9bJG1osUijw7kfa4CMwzRCuirdL-9emyICWUC7xsrrTnJTz2WOiox4r9WxXDeuj19me-aFtEA80K9p71TACQcrlXwKtTtWjvV63hkSHnt-j_HTFwxX0-UuEWqwTgnNerKhydiaSuH2drPBll9eiN9tOR60l5dyOfPDWWuoUbDR0MvvqMiD0DTeZDHS47Vvoa568c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20600" target="_blank">📅 22:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محسن رضایی:  ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20599" target="_blank">📅 22:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محسن رضایی:
ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20598" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ایران از خط قرمز ما عبور کرد.
در یک حمله غافلگیرانه، آنها پنج موشک با سرعت ۸۵۰۰ مایل در ساعت به سمت نیروهای آمریکایی شلیک کردند که هیچ اصابتی نداشت و هر پنج موشک سرنگون شدند.
اوضاع درست می‌شود!
در همین حال، ما واقعاً به آنها ضربه خواهیم زد؛
اکنون نوبت ماست که حمله کنیم.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20597" target="_blank">📅 21:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS1vKMLGBjimYvoQ5oc-8Vq-Pw8D33ejtwhPjOHuM2Yp6QYPReUo8aK6Bkibae8yhNwhAB4jQPvgzTlasG4Ex721QYbhmIByS96aMzm4EHvRog34mJEAnvZTZeKS6TlO4DPj7N8rc-p1iHHzNBFm14ZlW53qqsnJbdb_yiLViXNm-inv2Ow3KZsTKEZ2DZfEtDuHRDkPEXmeyWZ3rDNCQaOvtVrCrtdwIYpEmilGP8FGzgotYORbnXtCYbEJTKujp-syyS8n9kaGE0rTRxaN7CTbIGEWyS7r95YDnoLd_ViaP2qeSSFg7wk9xqCbHZuVtbsbgHY7MbwcPTncNmMZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20596" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20595" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سنتکام:
نیروهای ما تا دیروز ۹۲ شناور تجاری تغییر مسیر داده، ۳ شناور از کار انداخته و ۲ شناور نیز توسط نیروهای آمریکایی مورد بازرسی و توقیف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20594" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ospF0_cD8Qf5iTUWiy3Pte8QZ-aGpIB2ujf0ys5yy3U7U17o5IxFmJdgpfi2myxd7NpjQ1MdjcUBZ27OSqjHZKuW0mLCeNvNDoBUsdLiBCz1DCi0-gFNB6vKsL2mk_BWtb8aYa1R9ZBmyDt9TLGw4CrUkrP9GRxhd-fteF0S-W-KdQJorcF4ad3xhX-HmymdETWqS1yov0asmIYF-wauroccAEhVSJZCNrOXANPC0uR9jKwiR3Lt2kYel_1UpnN3e99VIVXxi6PyN1SoQHgTUioRPgLdQMF01w8uOSYPKtuLx61bRlxqNjRTaWNYdK7D8Z3iBI1zEgsjrKJl8Ez_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار سوخت گازوییل در آمریکا وارد تنش‌آورین دوره سال شده است. موجودی جهانی گازوییل در یک سال گذشته ۲۸.۵ میلیون بشکه کاهش یافته و به ۵۴۲ میلیون بشکه رسیده است. در ایالات متحده، موجودی‌ها از میانگین ۵ ‌ساله نیز پایین‌تر آمده است.
دلیل اصلی، کاهش عرضه از روسیه و خاورمیانه است. ممنوعیت صادرات روسیه تا ۳۰ سپتامبر تمدید شده است.
وضعیت در خاورمیانه به دلیل اختلالات در تنگه هرمز پیچیده‌تر شده است. محدودیت‌ها بر ۳ تا ۴ میلیون بشکه فرآورده‌های نفتی در روز تأثیر گذاشته است. در نتیجه، نرخ بهره‌برداری پالایشگاه‌های ایالات متحده به ۹۸ درصد رسیده است که بالاترین سطح در ۸ سال گذشته است.
بازار از قبل با کمبود مواجه است: بر اساس تخمین‌های CERA، کسری ۲ تا ۳ میلیون بشکه فرآورده‌های نفتی در روز وجود دارد. در ۱ سپتامبر، گازوییل در نیویورک تقریباً ۲۰۰ دلار در هر بشکه، یا حدود ۱۴۸۰ دلار در هر تن قیمت داشت.
اکنون، خود ایالات متحده در معرض خطر مواجهه با کمبود سوخت قرار دارد. تا ۲۸ اوت، موجودی ULSD (گازوییل با گوگرد بسیار پایین) در ایالات متحده ۹۴.۱۸ میلیون بشکه، یا تقریباً ۱۲.۷ میلیون تن بود. در یک سال گذشته، این میزان ۱۲.۲ میلیون بشکه (۱.۶ میلیون تن) کاهش یافته و ۷.۴ میلیون بشکه کمتر از کمترین سطح پنج‌ساله قبلی (۱۰۱.۶۲ میلیون بشکه) است.
تا ماه اکتبر، موجودی‌ها ممکن است به ۱۰۰ میلیون بشکه، یا ۱۳.۵ میلیون تن برسد. این اتفاق در بستر اوج تقاضای فصلی رخ خواهد داد.
اکتبر و نوامبر احتمالاً ماه‌های دشوارتری خواهند بود، زمانی که تقاضا برای سوخت برداشت و نیادز به گرمایش همزمان افزایش می‌یابد و برخی پالایشگاه‌ها برای تعمیرات برنامه‌ریزی‌شده تعطیل می‌شوند.
در آمریکای جنوبی، موجودی گازوییل در پایین‌ترین سطح فصلی خود قرار دارد یعنی حدود ۲۱,۵۰۰ تا ۲۲,۸۰۰ هزار بشکه، یا ۲.۹ تا ۳.۱ میلیون تن.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20592" target="_blank">📅 13:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….
به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/20591" target="_blank">📅 12:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خشم روسیه از تغییر الفبای قزاقستان به لاتین!
این دقیقاً در راستای تحقق رویای توران بزرگ ترکیه می باشد که من آن را به عنوان حوزه بعدی تنش میان غرب و روسیه (و احتمالاً چین با توجه به جدایی خواهی اویغورها) تخمین می زنم.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20590" target="_blank">📅 11:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:   سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/20589" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F66SyRvkXGJsae6NfB0rGnmw2C4JJx-HBuikkYaLgquDfhoDt2GxrmxTGmk52j4s9YD08uG3pHpCnciFlWpRbKLf7FZgM4QiiQMJS9W5k4iqGEWx8GaFUGrRYJZc92exMWWmXw64YHcbVd5iMQpD6K5OXvOv14uJNSQzlywOJ8eKbmS622BuR96elN5arGtFu0mSMHLEyK6h1GkeuX9mViQr6_LnS3M6oOFx7cMEyMYqv2zwwWVu11c3RxZbgWb52L8yOq5OQsjfIFU9l61cGerm89gCgR4ZWgkIVwvlQIt1gRkuBL8Qdf5kW_u6lIBi0r44E7rDEtEr9VmnoqYJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروش تسلیحات آمریکایی به متحدین نظامی اش از سرگرفته بشود واقعا؛ یعنی گزارشها درباره فرسایش ذخایر تسلیحاتی ارتش این کشور تا حد زیادی اغراق آمیز بوده است.  نتیجه بعدی هم این است که روابط ترامپ با روسیه و چین دارد تنش آلوده تر می شود</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20588" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20587" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20586" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری ریانووستی (RIA):
پوتین وضعیت پیش‌آمده در مذاکرات کرملین با ویتوف (Withoff) و کوشنر (Kushner) را دشوار خواند</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20585" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20584" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دو ایستگاه برق دیگر در آلمان هدف قرار گرفتند و مواد منفجره کشف شد</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20583" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادامه انفجارها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20582" target="_blank">📅 19:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ گفت پس از آنکه بایدن ذخایر راهبردی نفتی آمریکا را خالی کرد و از پر کردن مجدد آن خودداری کرد با نفت ونزوئلا دوباره پر خواهد شد!  این توافق مهم شامل بیش از ۶۵ میلیارد بشکه نفت است. این امر آمریکا را در مسیر سریع بازسازی ذخایر خود قرار می‌دهد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/20581" target="_blank">📅 18:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نقشه جدید کشورهای جهان بر اساس ابعاد واقعی شان!  طبق این نقشه که ابعاد کشورها را مطابق با اندازه دقیق شان نشان می‌دهد، سایز کشورهای غیرغربی افزایش قابل ملاحظه ای داشته است.  رنگ آبی: نقشه کنونی رنگ صورتی: نقشه جدید</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20580" target="_blank">📅 18:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usaeuxzXKSZetVU0hNiTjF77fsLaM8uX6CcGAIrNqh18sCU3XUM3l4c6jCED-OEFDmXzHQNUNQy2DKdPxf2-gJhr07I3xSus1UJ70rOhgryEAD1KgaKsPkPuR5CcoW9zKkjDgk8kdDExNnODnWVDoyo9zCqCbIie14AAFeN4qHAdkQRZCCW6680cDkHPKBcn_X3SHPBEu4tBq48z2a786VUpVYDipZM4rioa5orcP21BLc1-EhGoPyIhPULtYNS9uRZ6FjWXvERTfEDqvQc3Rwxw_zKaNYLQ8tYFLKyKBGiIUI5cHA20Kmq73q_uhE7ij0L9GbELDy0eLwC1EyDgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZyXTBHadu24jeaji3oQGF8SA-LVcENS6J4kD0GwzRUp6iuIaXmOPJH5w8o__9mnrsf6eFUB6qs3YsCXHSmvuS_Z9jxvx25iGTbIRpU3xDAjeGqD-RF1FdDFxRL1BmwJUXvxgBAKyUBEA8KCEkrsr6pYzQ3H7oviASUpv2o8fit_mR8uu49GpsSUJebcnqHohMTaRmJcyuc0vkEfOwHPyhxICNUI20KZ9634iR8GYfzYZqJrb-NioTO9EGqaO028Swf30Pkta-oYCcVswvrV59wKB0r8YE24i3NhbHwOSeSlnDPiv9M3l3-0OQ3Ss4O9R0JwxhJBvG2nTLRWEqSCmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه دیروز حداقل 3-5 بالستیک ضدکشتی به سمت دریای عمان یا تنگه پرتاب کرد تا شناورهای آمریکایی را برای پر هزینه کردن محاصره برای آمریکا بزند که به نظر اصابتی رخ نداده است. شناورهای غیرنظامی بزرگ در فاصله کوتاه عموما حرکت ممتد در خط مستقیم و قابل پیش بینی دارند، مگر مسیر خاص باشد. اما شناور نظامی میتواند پرتاب موشک را متوجه شود و مانور خاص انجام دهد. شاید یکی از عللی که حوثیها در هدف قرار دادن شناروهای تجاری حتی در فواصل دور موفقیت نسبی داشته اند همین مورد است (اما حتی هدف قرار دادن چنین هدفی هم با بالستیک بسی پیچیده و مشکل است).
اما مانور شناور شناورهای نظامی کارایی مطلق در برابر هر موشکی ندارد. یک موشک پیشرفته میتواند بخشی از این مانورها را ناکارآمد کند. در هر صورت موفقیت یک موشک بالستیک ضد کشتی بسیار وابسته به اطلاعات دقیق از انواع سنسورها میدانی است. وگرنه شانس اصابت جدا از طراحی موشک کاهش خواهد یافت.
🚀
🚢
(
بحث آماری پیشین در رابطه با بالستیکهای ضد کشتی حوثیها
)
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20578" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام:
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20577" target="_blank">📅 17:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5S4tDlQJOdhajQgMH8U-clcOd_6J_HJc1SvDC1Bd5z01nr5h-tfkcQh_jACWV5XX_fwCp2FxT_3VbR9B8jaR6JALIoRf3gkUioSraLATnYyLBeJGRkxtxhVLo6BLKcbzjtTk1RM1G_UqHHnFEhv-LGre-wdVQTTdGOiImPD068IkuGNECKxmP6hCf_tFpWrCCpPdcMla5VZHjHidWIOhbv6BF20-lMiBq8APXo9Y6w4zBLd-jutB8FlmeA8NUK3eCrkfkljeBPuLEOBzHK98eMaGU1UM-TcDfvz3UYQHUZu2uEeJXqxWEUM5QfHFIvI9FR7FjS2WqlYUg9UupGJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان  بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20576" target="_blank">📅 17:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انتخابات اسرائیل</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20575" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تمایل شدید نفتالی بنت به سرنگون کردن حکومت ایران را باید دقیقاً در راستای صحبت آخرش — از دست دادن آمریکا و حمایت جهانی — ارزیابی کرد.   یعنی اسرائیلی ها چون فهمیده اند حمایت جهانی را از دست داده اند میخواهند خاورمیانه را بازمهندسی کنند تا دیگر تهدیدی برایشان…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20575" target="_blank">📅 14:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20573" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihslYFqI0l2gwA8tOyxwKpahrZMFWRpc6-XOlI7FU0ZQGKtZh_YIQlAa1cM1xEUGzdDoaMzgLNixu0BUDpXZ0nF7Z9MGUsX98MnJi7AAoSGCVqRL3gW9gcvpqIRY-U7Wbl2KTcCXNOn8o6C9PKEFC7GTrhQlp_qPc4DIvyDAYg1KifvacDBNsKfm9WLUh5dwC2rzIL8H8kG4V4XzfQEsCmWBX6ac9_gwmEiaM8i4IS7ekJeF4UzXAcchRkLK0tvbEmjJNMfSbdzMT8nESG1M9DtoAvom_RynOQJY2_3Vr0YIh4tRE1IiuKcbmWTp7OSJoBvjOcl8BoX5Weh3IXUvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد تهاجمی جدید ژاپن؛ به اندازه یک چراغ‌قوه!
ژاپن برای نخستین‌بار تصاویری از یک پهپاد رزمی بسیار کوچک را منتشر کرده که ابعادی تقریباً در حد یک چراغ‌قوه دارد.
تصاویر منتشرشده توسط NHK WORLD-JAPAN، پهپاد را درون یک محفظه لوله‌ای و با آرایش چندروتوره نشان می‌دهد.
با وجود ابعاد بسیار کوچک، این پهپاد برای انجام مأموریت‌های شناسایی و حمله در برد نزدیک طراحی شده است و می‌تواند به دوربین‌های شناسایی یا مهمات مجهز شود.
از جمله اهداف احتمالی آن، خودروها و تجهیزات زمینی عنوان شده است.
ابعاد بسیار کوچک
قابلیت حمل در محفظه لوله‌ای
آرایش چندروتوره
امکان استفاده برای شناسایی و حمله
مناسب برای عملیات نزدیک نیروهای زمینی
این پروژه نشان می‌دهد ژاپن نیز مانند بسیاری از ارتش‌های جهان به سمت پهپادهای بسیار کوچک، ارزان و قابل‌حمل برای مأموریت‌های تاکتیکی حرکت می‌کند.
#ژاپن
#پهپاد
#پهپاد_رزمی
#پهپاد_تهاجمی
#نیروی_هوایی
#فناوری_نظامی
#دفاعی
#Drone
#Japan</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20572" target="_blank">📅 14:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زاکانی:   به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20571" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زاکانی
:
به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20570" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسکات بسنت:  چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:  ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SBoxxx/20569" target="_blank">📅 12:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20568" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYkF9Ol6i0UUn_PeWaoQ32gPf0sQRDB44EgdcUQghw_0yXTpaDD_ztfaM4wvcNrHh3nOxNxJZbsboPEfxK1TJzhnUcOSKH8wQrFLoGHcX2HkAqQZl3nRlVDAmhkDeMd1_LTfmSfyOGLrphwuKiVg8306yaJCaJ0JnrtXdeEVR-tsg2_5WJ5CVVDUq6No7QJwfgTH4TVycIWKnsyAQaRwN2tHDjSE0EO-NXzeJch8EuHmJqvCtab5Qp_M2zuFHMko2TctbwMTwzqFmMzwZfVQZTDqPPX3AYZSaowk5UPBFIPKgxRnQIEaQHyCTQiFj0f1TamjJaiVaSPAQ4jOnqILwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/20567" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS2XXzg-oB8b4k1OZrjKMtCjz--XSxET3EHW0DOsunsuG-piQmS6iYb8iWA9dQcOINygHKhILbxCFSUeqUgUtg7S3C2-1qLPLUkv1PrJFUDaNxukSk6PwgPercsv1YZZpJobnPZaPkNFWLeIPBJLcYAGtKi3kX9VAaspVHd_O39rp14Bf9ykLol37zxPiBV7ctXycE9mdyEgw7li9twuWH7h6K2jzanM0sztk9xNll8OC4Rp9Hc01ZlyZ2PYqqWC6_n7bBlgd2SatjN3Xlhyby0QPrkC3LhwwqpiQqvIq3mIuHez87Aik5YpIjsvO0txIwNO-JBKK6-RAVZAKBzKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دوباره هما خان سعادت در آسمان کشور مشاهده شده....</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20566" target="_blank">📅 00:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">— شلیک موشک‌های کروز ضدکشتی از سیریک به سمت تنگه هرمز.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/20565" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEu1DDalORvf-WCdZBNMefPafJJq9lrgIqVoN_-prji8Ljl9NM9K90nDaTlhpnh7NEJyAfWdxkMf_Lmrk8uNuwqFTkg5ls9fb2aebbRdMMkW1yLIs32s3Ziw8NtaH5FpjA0RQXgTu9P9sU2MgnWiPOmYPR0d5S2TLTZxRKk--_t6rpQk4Y6nq762spzhcDLHMzUq1PNjxoGb4w299uBXv0R-fvlF7iz4OYuK1az1wgAZVUerqe1C6dWgas6WmAe_s7KjPAaHopul0aLQzXdU2D01zPZhaDxSuwPJz8Sf_vzEVzw-zkdBVgszlJsJk4E1l1i5uLyY1xfoYK0TRp1TZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تکذیب کرد!</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20564" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم.   |</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/20563" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ
:
ممکن است خیلی زود کوه کلنگ را هدف قرار بدهیم ، چون حس می‌کنیم آنجا اتفاقی در حال رخ دادن است</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20562" target="_blank">📅 22:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib4hJwzBM2kAMs4yUqc7QSjnzCo5jVQL-6heMGoM_MsofttOd9aJnQgM56VWUlVYN28iLzahlLMTE9-5Mc0Icljw_SSswxozW6jQD4D_fpBPokTShsPprjHWLJAgr_nex0RqebnFX56qXBjPpDHvxmmQZk3X0YTigyW1fo5KfQL43ut0M12HalqrJHXcxb9VM8kcOtSb-CgoVHeIIR75DD6c5j6yhxNoLirngk2OmDgYW_x9Y0uQ7aOBqphsy7R9pDgNgoz51Qg3itU1xo806AKHg9ZyGaJYT-KoNIphC47ksy_Jq6IuJUHly1rhIqAaHhR5sPj_3M3WsroYkYoV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SBoxxx/20561" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برخی سایتها و منابع خبری از حمله موشکی ایران به پایگاه‌های آمریکا در اردن خبر می‌دهند</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/20560" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسکات بسنت:
چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:
ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20559" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از نبطیه چه خبر
نتانیاهو راست گفت که مسئولیت نخست دولتش‌، تامین امنیت کشور و ملتش است و در این باره منتظر کسی نخواهد ماند(به خصوص امریکا). شاهد، رخدادی است که از ۱۰ شهریور تا امروز همه خاورمیانه عربی بدان چشم دوخته اند. خبری وایرال شده.
ارتش اسرائیل کنترل عملیاتی ارتفاعات علی‌الطاهر نزدیک نبطیه را به دست گرفته و زیرساخت‌های زیرزمینی گسترده حزب‌الله را پاکسازی و در حال خنثی‌سازی است. این مجموعه که طی دو دهه با هزینه مالی کلان ساخته شده بود، شامل اتاق‌های فرماندهی، انبار سلاح، ژنراتور و امکانات ماندگاری چندین ماهه می‌شد و به عنوان مرکز عصبی واحد بدر عمل می‌کرد. در واقع هتل-قرارگاهی چند ستاره.
موقعیت مرتفع آن امکان پرتاب موشک‌های کوتاه‌برد و پهپاد به شمال اسرائیل را فراهم می‌آورد؛ و مساحت و تیپ ساختش ماندگاری طولانی را برای نظامیان فراهم می ساخت. ولی از مدت ها پیش، با شناسایی دقیق ماهواره ای، هوایی و تجسس زمینی‌، بستر برای تصرفش مهیا شد.
این عملیات ترکیبی از محاصره طولانی، شناسایی دقیق با پهپادهای حرارتی و ورود مهندسی بود. برخی نیروهای حزب‌الله کشته یا مجبور به عقب‌نشینی شدند و تجهیزات مهمی به دست اسرائیل افتاد. از دست رفتن این گره راهبردی، توان فرماندهی محلی، ذخیره‌سازی امن و پرتاب محافظت‌شده در محور شرقی جنوب لبنان را به طور محسوسی کاهش داده است.
البته این  ضربه به معنای فلج کامل یا جمود نظامی حزب‌الله نیست، ولی موجبات شگفتی کارشناسان خبره نطامی را فراهم اورده است.
حزب‌الله سازمانی غیرمتمرکز با ذخایر پراکنده موشکی و پهپادی در عمق خاک لبنان، تجربه جنگ نامتقارن و پشتوانه ایران است. نابودی یک مجتمع، هرچند بزرگ و مستحکم، توانایی بازدارندگی کلی، عملیات چریکی یا بازسازی تدریجی را از بین نمی‌برد. نمونه‌های جنگ ۲۰۰۶ و درگیری‌های اخیر نشان می‌دهد این گروه پس از ضربات سنگین زیرساختی همچنان توان پاسخ‌گویی نسبی خود را حفظ کرده است.
اثر واقعی این عملیات در تضعیف الگوی «جنگ پایدار از زیرزمین» در جنوب لبنان، افزایش هزینه بازسازی و تقویت فشار سیاسی برای خلع سلاح یا عقب‌نشینی بیشتر نهفته است. اسرائیل خود اذعان کرده شبکه‌های مشابه دیگری هنوز باقی مانده‌اند. بنابراین، آنچه رخ داده پیشرفتی واقعی در خنثی‌سازی نقاط کلیدی است، هرچند حزب‌الله همچنان بازیگر نظامی فعالی باقی می‌ماند و سرنوشت نهایی به واکنش‌های آتی، وضعیت آتش‌بس و توانایی بازسازی بستگی دارد. ولی حزب الله دیر یا زود ناگزیر به مذاکره و توافق است. دقیقا شبیه حماس.
#یدالله_کریمی_پور
#Karimipour_K</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20558" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارشات تایید نشده    از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20557" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqonM0zkmkdqlxE3o_V2el5zuRH-qwkQBrhHM-XE9E1AIaRWz1BaU27RDdDLyp8dBQ5fMGFvgOQXPZruA7zC6tL8hDOLqZv4umjOtqlTGoSBbLwVzcyeABolrFAdj8SxfwfTMOHfn0N04bMOdIYsnFk-fw-fPDMeAeW_CTbaSv9N80eD5bJJeYjezsPtVlPnZh0OlAWwcTfid976gvjfgN-VjrojJ-p8q2X67lcqdOxvFg6WRaq2m7MtWfrZF2UClcg3Eegz1kQQjAfWGDl7zoeeyawtRVBLqMfap-kOfwMi8_xAHBO-j-o-OBCa3-0e79a54MoCjKdVCrvd8rPbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20556" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEKKU7VwDLFCrBuxirrduEc3ZqUMS3_uXth9y4Ft45DWbP0yX-5dLeH0oTBd-OZYLM44aKNI0BA-T_juAAqHZFAzpgbVx7hgFvbAhxL_b34Z0vYU4TvUHpjkQbdux3dm8QV2aZqEWnRH1pa80DFJAsWe6yEEB0vysu_5QUXrJEQ0tdrfr-PlZ7IJi-WLGVjcfAfMT92fmGbfrMRmARGuntruwlGutTfg0ERBRie5_96sJw2QrMqEfOTuyQqkn7YX8u7aq_hHDfNrMhL93mqXID0RFO823qG8SKwF8Wcc_iC-kimvPjEl8HsM2eLYd-1B4AyG1DPsyZ6PRhb3pmeHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20555" target="_blank">📅 20:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارشات تایید نشده
از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20554" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از اپوزیسیون هم شانس نیاوردیم !
این قاضی زاده تا دیروز فعال سیاسی بود از امروز شده فعال بازار شت کوین !</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20553" target="_blank">📅 19:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایالات متحده تحریم‌های جدید مرتبط با ایران را علیه بانک ترکیه‌ای گلدن گلوبال (Golden Global Bank) اعمال کرد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20552" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20551" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20550" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این ترامپ رسما دیوانه است!
رفته خودش این کوین وارش را به جای جرومی پاول آورده بعد امروز وارش را تهدید کرده که یا نرخ بهره را پایین می آوری یا تجارت با کشورهای دارای مازاد تراز تجاری با آمریکا را متوقف می کنم!
همین هفته پیش وارش گفته بود تورم بالاست و تمرکز ما روی مبارزه با تورم است و شاید نرخ بهره را بالا ببریم!
جالب اینکه همان پاول فلک زده را هم خود ترامپ در دوره اولش آورده بود و بعد هر روز به او فحش میداد که چرا نرخ بهره را پایین‌ نمی آوری!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20549" target="_blank">📅 18:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش مشابه</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20548" target="_blank">📅 18:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20547" target="_blank">📅 18:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حالا اینقدر بچه ها نگران این تپه نباشند؛
ماشالله اینقدر تپه هست برای فتح کردن !
مثلا یک تپه ای هست به نام امین الطاهر که کنار علی الطاهر است و هر کس به آن نگاه می‌کند طلسم می‌شود و فیلم «تپه ها چشم دارند» بر اساس داستان این تپه ساخته شده.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20546" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=TIFeXm_a196tx5Th8R3CCAtIN0oVI4BbiW9duZ829uJwZxUz1qv09SnrPG2LQUU9QdEQqEFSHr2w9wuK2pwJp8TEOwsrVz_h9shqZZD3yVgL-zZ0VUo-onsRvVSzlI1Rz6Qpk_-qQkCDPZJh8slj7K9Hp1ifY2dJpiLNk9SQ0ZvivhEAiwjEfUvY1Zw0wJ4CYVxi7x61Uf7QyZj8JAdXrDxjYZH9p7fpj8NZ7ZOaj0HG4R4J5n9w2rYKXezo6GkXW_2HjzOuF-5u4G_-Am3-WDTfoANJPWojhgOSYnZcUFzrRHh06NbtdG7QruWczxYm-_-MpwPV_c67lmblwAEH8IgvqlWG-7fCDZtawIgbiMVyxqohRdpiavpPrSBwSaIlpXIhsUxuWUP1SECSscU8lxoLV3K56BBfKCHNvdJFqF-2EWcLz0ErfuVz0czNoFU7YTD286BEPdPJHYXtTE32J2GFlqTeveq0MgG9CYUZGBHyTnKK-NczaRk0-qIgUyStVI_W-HShRIq4a2aH_25IWNnwGuXl0et-uNBHKCfvO-MmG8Y93oxM97naLCsAwKDjt8YGY2cFFZRncLa0R-n39UIUocQoQyx__V7f6fZN6eJIUToEwTFtLqxcaWJLSy3pUFBwsuz4u9DOGfJRHEMEIpxwoHS0RfrPdCE41lpA9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=TIFeXm_a196tx5Th8R3CCAtIN0oVI4BbiW9duZ829uJwZxUz1qv09SnrPG2LQUU9QdEQqEFSHr2w9wuK2pwJp8TEOwsrVz_h9shqZZD3yVgL-zZ0VUo-onsRvVSzlI1Rz6Qpk_-qQkCDPZJh8slj7K9Hp1ifY2dJpiLNk9SQ0ZvivhEAiwjEfUvY1Zw0wJ4CYVxi7x61Uf7QyZj8JAdXrDxjYZH9p7fpj8NZ7ZOaj0HG4R4J5n9w2rYKXezo6GkXW_2HjzOuF-5u4G_-Am3-WDTfoANJPWojhgOSYnZcUFzrRHh06NbtdG7QruWczxYm-_-MpwPV_c67lmblwAEH8IgvqlWG-7fCDZtawIgbiMVyxqohRdpiavpPrSBwSaIlpXIhsUxuWUP1SECSscU8lxoLV3K56BBfKCHNvdJFqF-2EWcLz0ErfuVz0czNoFU7YTD286BEPdPJHYXtTE32J2GFlqTeveq0MgG9CYUZGBHyTnKK-NczaRk0-qIgUyStVI_W-HShRIq4a2aH_25IWNnwGuXl0et-uNBHKCfvO-MmG8Y93oxM97naLCsAwKDjt8YGY2cFFZRncLa0R-n39UIUocQoQyx__V7f6fZN6eJIUToEwTFtLqxcaWJLSy3pUFBwsuz4u9DOGfJRHEMEIpxwoHS0RfrPdCE41lpA9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما:   ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید شورای نگهبان نرسیده است</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20545" target="_blank">📅 17:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20544" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq9acQiRPwACvSDIXmovAQ0coBA3Wimw8Sjcjui8rToaydQnxMhQHUzQTibmnDjsfcfT6qNsVSrfjpXJG8vjzIUEsMQWl7OH-C4IKx742zQYuit0RudjY7meqsZ03nbhNe6_r9l3prNxLgI37q9lN44vAb0F1BON_FU2hdrhobQntZbh1br58PwVma4zXeXhhj5L6kfEzB_9MmJDDI0Wuo04EMtTjWEtyN3CnXaGtmGwk_jP-e-Z09-peO8qcN9KK2A8vHqiiElgpYNdvgk-hT-f3uBaN4Kx9CunjO1aYomrcc6AJcAs7hTEhkA-dF4LpEVKgdKPY19T9MiB0BS2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20543" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در‌ روزهای اخیر باز اسم عاصم منیر مطرح شده بود!  سبحان الله !</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20542" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20541" target="_blank">📅 09:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ظاهرا آرژانتین با حمایت ضمنی ترامپ به دنبال حمله دوباره به جزایر مالویناس (فالکلند) است.  جالب است که به محض انتشار این شایعه، استارمر بحث تروریستی اعلام کردن سپاه پاسداران را به جریان انداخت تا شاید از امتداد شعله خشم ترامپ جلوگیری کند.  اخیرا بریتانیا تصمیم…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20540" target="_blank">📅 09:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2lWzMTplU7DAnimafL5tqKuct-UvuLlDWU4WH2bK67Kwl4eBz3B84dmn7RBb_LxWJLzOa9CkypLrupfN5KQgcF9THNPCeSpP4W-8-qlmqwSCzVQ2jfq7eMU5aHWq7AqhY4L-6Y_TVRViATtZl0-Xr8tmP_DyA8bhqyEUwNh4wizCaAWz0g0l3LL5nkXeEU4DaoyVm0V5iRJ4s9wytuNjaaeHPnunLJO57kI5MQdkEL_jI_H6VeaiXzu0JR-Lcyp1pC5OLawU8hSsUHa02ZQ3e2ehNwxBrOfCcaWlqaVK3HVahFRkmzwZQ1TktoC3lhJPhxu5EQAOJPatSOBagcNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش خنثی سازی مین ها از راه دور
این روش عمدتا توسط نیروی دریایی بریتانیا به کار می رود که تخصص ویژه ای در مین روبی دارد</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20539" target="_blank">📅 01:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyDpM7BVm572IU8gbLuh-AAfvPcMrYP8iXF8UIytE08o7FIJrcxYClZ4JjaSSOY-4ghECM9df2qtY9uGtsd7-mVxL48rhiU9DN-cMYlIJGgp3iYG3E75z9uuUNmg03lTHITQaHFOXg-xiCISrj5VAK4taGfeQcuLS9vmdzzAQqo5zm7zTuSCRqzUaQrIWLKPX-kuMkgtVZu9Tz0-hrJHDv8GcH6ix_4lTkFkGlmPj5LE1SrUd06ZIgX8PnKyDyL7wM5iJxoWLBjWVmViv7br6jB7SK_Dprmkm1F_RxmowbrUpQ9NAJY6TLU_fMoTqunnMkvyLMXpzE5eyLnMNO5N4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.  مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20538" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20537" target="_blank">📅 01:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=eSXIHM_UNet0fjNa99nPMjv9XV5LeuP2Xpbu3RiX3g-jExbxgCVhGRdQ8DOQxGEW0nmlXytorJRpRmLwyKV5aVJT0gWr0SjR85zDT4COzxuxDsq9OPQri44foS5IJwP5I6XufTyaLnvLoRGBfLN9gjlDYNmqEoBb34duzqYz4jS9FAvDqMECJ3Wnh8v_r_iXRKPKs9-ofHP-P8DHgff3ihJvZRJqTlD-JkjgVj0qjQJJCE8WCGwwB7PmtGE_Ehgb7SGqP6BykCkKeq1lZ8jEdEOg-6JXDRS3WqiAUQOP377ZJrx9aGbgTRah4PBRAkt2N6eUWCbW_maZj1tA5QFoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=eSXIHM_UNet0fjNa99nPMjv9XV5LeuP2Xpbu3RiX3g-jExbxgCVhGRdQ8DOQxGEW0nmlXytorJRpRmLwyKV5aVJT0gWr0SjR85zDT4COzxuxDsq9OPQri44foS5IJwP5I6XufTyaLnvLoRGBfLN9gjlDYNmqEoBb34duzqYz4jS9FAvDqMECJ3Wnh8v_r_iXRKPKs9-ofHP-P8DHgff3ihJvZRJqTlD-JkjgVj0qjQJJCE8WCGwwB7PmtGE_Ehgb7SGqP6BykCkKeq1lZ8jEdEOg-6JXDRS3WqiAUQOP377ZJrx9aGbgTRah4PBRAkt2N6eUWCbW_maZj1tA5QFoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20536" target="_blank">📅 01:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سوریه به فارسی 𓂆</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=fvLC5xA8FXXQwMD50o13dJvhgNZ4tTnePIqNrq7mNJlkFBN1e99bOeI7h0t8SRHaXpC3J8aXvaejJNmQ_thECa5U_YqfAC4o7z309Ex9omz_dlFU3Db5GmJGf9sk9C-Yn6KGg_0_Xry2znnv57cbekyVZi-keu_BDSo3Hn886-NSc5KX4jFQ-XbcS9lpm1EoCQdi4vVP6Xbdk3WGnZ6uBWAP30FIcyWMKmDRXqWPrDps4vNZMjK1MaUB1Lys6qdFu-d105_TZoxP0-FPrLoVIJ_Pux9bkGF7EbkOXWRevfJaHAE9e9rO4o1NpH30dRTjFf7CQ7Utzn45WcZpFegb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=fvLC5xA8FXXQwMD50o13dJvhgNZ4tTnePIqNrq7mNJlkFBN1e99bOeI7h0t8SRHaXpC3J8aXvaejJNmQ_thECa5U_YqfAC4o7z309Ex9omz_dlFU3Db5GmJGf9sk9C-Yn6KGg_0_Xry2znnv57cbekyVZi-keu_BDSo3Hn886-NSc5KX4jFQ-XbcS9lpm1EoCQdi4vVP6Xbdk3WGnZ6uBWAP30FIcyWMKmDRXqWPrDps4vNZMjK1MaUB1Lys6qdFu-d105_TZoxP0-FPrLoVIJ_Pux9bkGF7EbkOXWRevfJaHAE9e9rO4o1NpH30dRTjFf7CQ7Utzn45WcZpFegb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا درسته اسرائیل علی طاهر رو اشغال کرده ولی اینکه ترامپ پای یه کاغذ پاره رو امضا کرده به شما حس خوبی نمیده؟
@SyrianToPersian</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20535" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فشار اقتصادی آمریکا بر ایران در حال تشدید است
رویترز
کارزار آمریکا برای محدود کردن صادرات نفت ایران و بستن مسیرهای دور زدن تحریم‌ها، فشار قابل‌توجهی بر اقتصاد تهران وارد کرده است. کاهش دسترسی ایران به ارز خارجی، محدود شدن کانال‌های مالی و افزایش هزینه شبکه‌های غیررسمی انتقال پول و کالا، توان تهران برای مقابله با تحریم‌ها را کاهش داده است.
مهم‌ترین ضربه، افت شدید صادرات نفت ایران است. بر اساس داده‌های Kpler، بارگیری نفت خام ایران از حدود ۱.۷ میلیون بشکه در روز در سال گذشته به حدود ۲۶۰ هزار بشکه در روز کاهش یافته است. این کاهش، درآمد ارزی ایران را به‌شدت محدود کرده و همزمان با سقوط ریال، تورم نزدیک به ۷۰ درصد و افزایش هزینه واردات همراه شده است.
ایران همچنین با محدودیت ذخایر بنزین مواجه است و یکی از مقامات ایرانی ذخایر فعلی را حدود دو ماه برآورد کرده است. اختلال در کانال تجاری امارات نیز فشار بر واردات و تأمین کالاهای ضروری را افزایش داده است.
از منظر سیاسی، واشنگتن امیدوار است فشار اقتصادی تهران را به مذاکره وادار کند، در حالی که ایران تلاش دارد هزینه‌های اقتصادی و تورمی جنگ را به مسئله‌ای برای سیاست داخلی آمریکا تبدیل کند.
برای بازارها، پیام اصلی این است: اگر محاصره نفتی ادامه پیدا کند، ریسک کاهش بیشتر صادرات ایران و فشار صعودی بر قیمت نفت افزایش می‌یابد. در مقابل، تشدید فشار اقتصادی می‌تواند احتمال واکنش نظامی ایران در خلیج فارس و تنگه هرمز را نیز بالا ببرد؛ بنابراین بازار نفت با یک ریسک دوطرفه مواجه است: کاهش عرضه ایران از یک سو و احتمال اختلال گسترده‌تر در مسیر هرمز از سوی دیگر.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20534" target="_blank">📅 00:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20533" target="_blank">📅 00:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpNWxhAafS6lkpcYH3T0YP1uJtINTe5Ar9pMNGOPpmLjG_fm4TH9UICfSVGCEY4NV7p_e4XyUbooVRIzr3-MVAbwZG3urQ1kIjDolpCMJp4xPJ2zBUhhWyZqNHkFRgyk_4u6IepqZCWBHsJnqlJg-e9I3f6BjQhQ7lRefSw0q8JMK_FMX7MdlpdRQSbZo1RRZ60Um_DA0IVTTVwnFH2zc-i025v3wkG6boTgK_N5WKzDcny5gaR68i1CNzBFyaAcTnNZ4qkG2grW0F0wAWLHG7FvOqPKZTYNZAxkVzjWZXNS_-YeTGEKSm1HF05HfPYYdQyPzeaz4mzTy9WiBDCh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20530" target="_blank">📅 00:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20529" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDsPoYs28HN4f_gqNmFMNJo_vW4GRwRMdamyK6xn7qenFmgDmMnahc5wwMKdKflG79GWG9vwCrXU2T83lkaFrtX-l0nQwy7xh7muPRudpMQJwoss2tEHX_0cURSbHApvIXqengWYulPwEU_3Bg4S6xm7BrjSQsqHPm-FLDCYc0hxi7xKv8mBiAzG_Hmn8sEdToLP3MKSD_hnIvMH8YtiYbmzG-OCMThR5vYy87JEf9ipwshAl0IMcxoSRtnVmHbemGb1kV4ntxqXbwb89i_nspu5Z3dCzRncN-quXPCpJiWB59fYffGa3C34ByDaRyjCuqv0T4OO2oQLP8qmK-IC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۸ سال بعد از حمله هوایی ، اسرائیل اعتراف می‌کند که مشاور اتمی ارشد اسد را در یک حمله شبیه به سبک مافیا به قتل رسانده است
در ۱ اوت ۲۰۰۸، غواصان اسرائیلی به ساحل سوریه در نزدیکی طرطوس نفوذ کردند، به ویلای تعطیلات سرهنگ‌کل محمد سلیمان، مشاور ویژه رئیس‌جمهور، حمله کردند، او و مهمانانش را در حال شام خوردن یافتند و سه گلوله به پشت سر و گردن او شلیک کردند. این موضوع را اهود اولمرت فاش کرده است.
«در روزی که سلیمان حذف شد، جنگجویان ما از آب بیرون آمدند – تیراندازان چابک ماهر،» نخست‌وزیر سابق در یک خاطره‌نویسی جدید نوشت.
«او را با قطعیت شناسایی کردند. با وجود اینکه تعداد زیادی از افراد روی ساحل حضور داشتند، هیچ‌کس متوجه آن‌ها نشد،» او  مدعی شد و توضیح داد که چگونه کماندوها به‌صورت بی‌صدا به خانه سلیمان نزدیک شدند در حالی که او و مهمانانش روی یک تراس باز نشسته بودند و از فاصله‌ای حدود ۱۵۰ متر به او شلیک کردند.
«سر او به عقب افتاد. بلافاصله پس از آن، جنگجویان به سمت آب عقب‌نشینی کردند و راه خود را به سمت قایقی که آن‌ها را برداشت، باز کردند،» .</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20528" target="_blank">📅 22:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز چند بار تتر تا ۲۰۰ تومان ریزش داشت!  به نظر عده ای دارند نقد می‌کنند   تارگت کماکان ۲۴۰</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20527" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliooMWxFa05d9dA6IZVybiFuLjyZuFpWSq68u-KIJGjXJi2SfKUxyFwQWMo_rZXEFTOydmJZbPI-2n7vtptQQlbw4438wq1QSBVfD0p0YZBwoOcVcrKRI-jWzIaCaTM0quWq2wQwQJUXsxYZU7vJeL3LqEC35PWgIiP4JGYy6pq7DFahieDK3lMsYeQe8yylcY3MZhL7Q-29iGDnhUL9LpQ86CKEnptpjec4L9oJfFtUPJGkcZJZDOSwBl87tyPj6yvTeUilwvCSbbF4N-uU3b_pF15Ea2XIUb43JhudZRuQOtMFFcp2U6iXY6zbleRCCW3c1xkqmKO5DHJgLnPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه  وقتی روی مواد هست  گوشی دست نگیره  مرسی  @PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20526" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20525" target="_blank">📅 20:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سبحان الله این محمدسامسینگ ما چه انگلیسی اش خوب شده!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20524" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20523" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2vMWXodDAOUU21yVMFrwWVyX503m8IsKMA_eIgHTrSRoS1Pb2IU-FYMNveuTZwuz6pXE70s2yERaXHnqEXsg3cv6gOu_FwQ3LMFTBmNcJsXW8fEYegWTpSityZvf2loklest6EUA3d5YbSx52pWdPhAQ0amAmz1ghbiPXN44fFdFMZlDwVu2QX1c1pkOq9_VXbnMk-f2eqvHFECjW-SNH3W9DyAYRTErTh-5B8_kBmepbY1zn0aZwCPvKOwaM_bmBRHADvDrO8SXMIk21d2Rdp-F7anMOGDDYQJRB7UmHheskdRZoWU0GWnmcKPzXpR1l9DVmEHObZZn2bAcQTN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20522" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">موشک‌های ایرانی به سمت کشتی‌هایی که مقررات تنگه هرمز را نقض کرده بودند، شلیک شدند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20521" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
