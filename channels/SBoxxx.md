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
<img src="https://cdn4.telesco.pe/file/saS_byGfp5reUzvtezGUiLIjiag-wyM3dtgQRCrOBTgeu_nB2CLFMglZST77btbGtLzRkRb9tFcT-Bveq5KcbiYGQVrmMiYpfyDVSYVgsgHfobQXGVinItapqJMNanNnE6TzRr3PMKieIVEO8LNDs7jUxEH_ksnzDa5a9gqnjsDeYqyDWBqXXiiUUM9Xe2HifLh55PxnbvwLZVC-jhNug1Nq95DVGPxJgEha41ZrxMiTbV4KHiLzEXxY537FcOzJVJ3qy04ZooDLVh_Y7p95b-eW8TNlf-1rVr4kHpmnciv0crSJYLGNH32lk-gS6WR1f3vZtCIyfU72paFBzq-VsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/17405" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نفت بخرید و شیشه ها را چسب بزنید که ناپاکستانی جماعت کثیفترین دروغگویان عالم هستند</div>
<div class="tg-footer">👁️ 62 · <a href="https://t.me/SBoxxx/17404" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=klUHAsrNUHuIdESm3G9Z66EgSom1lDNFC7n4Ouz0vFV5kVS6p5AqJCsWLZwoeAus2rtCj69LbumXk4x4HKnmPGQMR43kEQ93BEBb77ILCfoMrSbCFk08TWLYzoPtUa_Os0Tn0iVueOStdB1CSLslQABogFL2ZchbMaRCF_EQCWoNV98X9uPfX104tzhJ2j1yLOfoBCt0xVd2lEz-6oPA1IbORo79eK_TkP7-NDLEO4BlFK5O3SDo9zrbNTGpWyPChzqONHN-uyio8dIAazkztAC9Bw4Yzpwblb2fQJkoFtLB5YEuvwgITwsjUErtI_aaBVxtF9-pwmVW7He30sq43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=klUHAsrNUHuIdESm3G9Z66EgSom1lDNFC7n4Ouz0vFV5kVS6p5AqJCsWLZwoeAus2rtCj69LbumXk4x4HKnmPGQMR43kEQ93BEBb77ILCfoMrSbCFk08TWLYzoPtUa_Os0Tn0iVueOStdB1CSLslQABogFL2ZchbMaRCF_EQCWoNV98X9uPfX104tzhJ2j1yLOfoBCt0xVd2lEz-6oPA1IbORo79eK_TkP7-NDLEO4BlFK5O3SDo9zrbNTGpWyPChzqONHN-uyio8dIAazkztAC9Bw4Yzpwblb2fQJkoFtLB5YEuvwgITwsjUErtI_aaBVxtF9-pwmVW7He30sq43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اژدهای بندر به شما نگفت ولی دونالد قرمساق گفت که منشا صداهای دیشب چه بوده!
یک کشتی هندی بدبخت حرفهای کله زرد دال بر باز شدن تنگه هرمز|ثابتی را باور کرده بوده و میخواسته از تنگه عبور کند که سپاه پاسداران به آن شلیک کرده و می‌گوید برگردد  و هندی ها با ندای :
Sepah Navy ! Sepah Navy
!
You gave me clearance to go! Let me turn back!
دمشان را روی کولشان گذاشته و برمیگردند
این به قول اژدها یعنی
نظم ایرانی
!</div>
<div class="tg-footer">👁️ 399 · <a href="https://t.me/SBoxxx/17403" target="_blank">📅 17:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شرایطی که ایران به اخبار جعلی نشت داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده است، ندارد. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و حقیرانه‌شان مبنی بر داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. افراد بسیار بی‌آبرویی برای معامله کردن. با آن‌ها هیچ‌گونه…</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SBoxxx/17402" target="_blank">📅 17:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/SBoxxx/17401" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Buy Oil</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/17400" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/17399" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal with. With them, there is no such thing as dealing in good faith. AMAZING! Also, their totally rebuffed Drone attack last night against Indian Ships leaving the Hormuz Strait is TOTALLY UNACCEPTABLE. They better get their act together, and FAST! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SBoxxx/17398" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجری فاکس نیوز در مورد توافق ایران، به نقل از یک مقام کاخ سفید  مواد هسته‌ای نابود و حذف خواهند شد  برنامه هسته‌ای برچیده خواهد شد  هیچ یک از پول‌های آنها تا زمانی که عملکردشان را نشان ندهند، آزاد نمی‌شود  تنگه هرمز باز خواهد بود  ایران هیچ گونه حمایت مالی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/17397" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SBoxxx/17396" target="_blank">📅 17:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SBoxxx/17395" target="_blank">📅 16:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ایران وضعیت تنگه هرمز را به سطح قبل از جنگ بازنمی‌گرداند - ایرنا</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17394" target="_blank">📅 15:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/17393" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/17392" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متن کامل:  خبرگزاری نیمه‌رسمی مهر ایران فهرستی از اصطلاحاتی را منتشر کرده است که گفته می‌شود در پیش‌نویس یادداشت تفاهم با آمریکا وجود دارد. این خبرگزاری به منبعی نزدیک به تیم مذاکره‌کننده ایرانی اشاره می‌کند، اما جزئیات به طور علنی توسط تهران یا واشنگتن تأیید…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/17391" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRY2qTnfKHqiPdlvUXscmDlMejnWhOsZL_4aVKpEg1qi0q0QBKxX6jYceFsRO_dYgaTDP2vsWSFp5SWf4uJrwcXlUlb60LFs7sSWPcUrWFVmXCuLrJ3azYgEgxQ1k4yJnUQzXAhV8sY2eFI0E8ygjs6YxNEKR2_csZKdhJ2oqji9UqvcCjHMxPXVeq9QZ3qI8s1U3rshYpsz45ywslMYDiivuhJpcMTEgUwZRg6-JwsZu-kNUAhLCEh9MsTO2VEHgy55m0E0l786mfo2dQswTYe7XKS2G5fPW2XJZX86UKOJvbiOWjLqtdtaCroEFIMXbZsiLK3uK8uNZ2yj-scJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزودن شدن 1500 میلیارد دلار به ارزش بازار سهام آمریکا با اعلام توافق دیروز توسط ترامپ</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17390" target="_blank">📅 13:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17389" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات سنگین هوایی اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17388" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB6SY76fO6wbSOhbvMIrhSB1zNlgyHyqXRB6DrAr_GgzrmhOXNfWRQqCkW9OtVfPsdkqszjfbuDFPjfMGQRAwBfSHCVvRbURe6uX-0shgCZIYTOnu78YKb8hkXm_UKD4X5dVs6hDksTA68JyU_0gaGwVYvpV9RH5R84aFAHs6Ywiop0EqJKw74RkAOjUqGaUlyLa9ansMi-o3HS4Xpz_wbsbne3zDHKnELt8RxZddOidbDoGC901Kv0ixS_94LfanY4HceG26p5jCOjuGGVA_nNWqsYBzHcdm-7EhSADsjPri0xo3VWU246lM6nA4wH7jQYypQaSKByS_dKmEiRweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/17387" target="_blank">📅 12:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17386" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/17385" target="_blank">📅 12:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سردار نقدی:   انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/17384" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سردار نقدی:
انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17383" target="_blank">📅 12:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">توقف دائمی و فوری جنگ در همه جبهه‌ها، از جمله لبنان</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/17382" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/17381" target="_blank">📅 12:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همچنین ایالات متحده وظیفه دارد غرامت جنگی پرداخت کرده و از کل منطقه غرب آسیا خارج بشود و ایران را به عنوان ابرقدرت چهارم جهان به رسمیت بشناسد.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/17380" target="_blank">📅 12:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17379" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.
خبرگزاری مهر</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17378" target="_blank">📅 11:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الجزیره:
ادامه حملات اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17377" target="_blank">📅 11:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17376" target="_blank">📅 10:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فوری | یدیعوت آحارانوت از منابع خود گزارش می‌دهد:
نتانیاهو گفت به ترامپ اطمینان داده است که تلاش او برای دستیابی به توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17375" target="_blank">📅 10:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17374" target="_blank">📅 09:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آمریکا: دو پهپاد انتحاری شلیک شده به کشتی‌ها در تنگه هرمز را سرنگون کردیم
نیروهای نظامی ایالات متحده دو پهپاد انتحاری که به سمت کشتی‌ها در تنگه هرمز شلیک شده بودند را رهگیری کردند، این در حالی است که گزارش‌هایی از شلیک ایران به کشتی‌ها در این منطقه منتشر شده است.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17373" target="_blank">📅 09:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17372" target="_blank">📅 03:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات در ادامه روندی قرار دارد که از ماه مارس آغاز شده و طی آن دمشق اقدام به تقویت حضور نظامی خود در امتداد مرزهای مشترک با لبنان کرده بود.
مقامات سوری هدف اصلی این استقرارها را افزایش امنیت مرزی، مقابله با قاچاق و جلوگیری از نفوذ عناصر مسلح عنوان کرده‌اند. با این حال، اهمیت این تحرکات در شرایط کنونی منطقه فراتر از مسائل صرفاً امنیتی است. مرز سوریه و لبنان طی سال‌های گذشته یکی از مهم‌ترین مسیرهای انتقال تجهیزات، نیرو و پشتیبانی لجستیکی برای گروه‌های مختلف فعال در منطقه بوده و تحولات جاری می‌تواند بر موازنه‌های میدانی تأثیرگذار باشد.
همزمان با ادامه درگیری‌ها و تنش‌های منطقه‌ای، دمشق تلاش دارد کنترل مؤثرتری بر مناطق مرزی اعمال کند و از تبدیل این نواحی به کانون بی‌ثباتی جلوگیری نماید. هرچند تاکنون نشانه‌ای از آمادگی برای عملیات گسترده نظامی در داخل خاک لبنان مشاهده نشده است، اما استمرار اعزام نیرو و تقویت مواضع مرزی نشان می‌دهد که دولت سوریه تحولات مرزهای غربی خود را با حساسیت ویژه‌ای دنبال می‌کند و آماده واکنش به هرگونه تغییر در وضعیت امنیتی منطقه است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17371" target="_blank">📅 03:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
🇮🇷
- دونالد ترامپ:
ما امروز جنگ با ایران را به پایان رساندیم و آن‌ها توافق کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن اصرار داشتیم. این همان هدف اصلی بود. این ۹۵ درصد از آن بود. و، اوه، آن‌ها این کار را به قدرتمندترین روشی که ممکن است انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17370" target="_blank">📅 03:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فارس:   دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17369" target="_blank">📅 02:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب لغو کرده‌ام. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا نهایی شدن این معامله به طور کامل ادامه خواهد داشت
— زمان و مکان امضا به زودی اعلام خواهد شد.
دونالد ج. ترامپ
رئیس‌جمهور ایالات متحده آمریکا</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17368" target="_blank">📅 02:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99919094c3.mp4?token=DyOvE2RrBF5TKOKoaCFBVWRbH7578wz-azVAv5vcrH-bjewDFFR4UQUIgxZmbv-k01oZrX8sRi3Mf3XJot2Ip9Q62fr9GkEPxUqHkasZUo47W0Qpts5bX50OJUxKIO1A7zihvryBPPWA0cUuoIkasOiHJTx8Q3gor8g52bJ258GdVuN43SwOJ6XuHw_tcP5WZlMxDYR6BKJpAtqeEG-4-QaloqfjrjUEPn8zJwjKQ9jqEYDOkNlfBgb1PW3ljX0jifCrfQgz2jD3Z4J2LjbAtbFfXg4ZYvOQWMMuWgZAaq6ZVnhGwNf-77qCe7cW1g9Bg0xNI7jpAzm_Bh0uD_U7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99919094c3.mp4?token=DyOvE2RrBF5TKOKoaCFBVWRbH7578wz-azVAv5vcrH-bjewDFFR4UQUIgxZmbv-k01oZrX8sRi3Mf3XJot2Ip9Q62fr9GkEPxUqHkasZUo47W0Qpts5bX50OJUxKIO1A7zihvryBPPWA0cUuoIkasOiHJTx8Q3gor8g52bJ258GdVuN43SwOJ6XuHw_tcP5WZlMxDYR6BKJpAtqeEG-4-QaloqfjrjUEPn8zJwjKQ9jqEYDOkNlfBgb1PW3ljX0jifCrfQgz2jD3Z4J2LjbAtbFfXg4ZYvOQWMMuWgZAaq6ZVnhGwNf-77qCe7cW1g9Bg0xNI7jpAzm_Bh0uD_U7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17367" target="_blank">📅 01:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17366" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس:
دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17365" target="_blank">📅 01:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش های تاییدنشده از انفجار در بندرعباس.
گفته می شود ایران به چندین کشتی که حرفهای ترامپ را باور کرده و قصد عبور از تنگه هرمز را داشته اند شلیک کرده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17364" target="_blank">📅 01:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17363" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgQyFZfaUO-CKOgG968qdHw7L3-r-FZLxnhJGqn29UIud-Jgy6xy2TTuHGuXTs6rNNSDscRsTYDeKoqcYj3YNhCwM5WwPO7mKteu6zSfNQXttExmLeyUWIb5yb0Jtb-NSPrTYvVIyPzIg4Vf6BdC5LpYaWtA8p6QbpagdP-yZMnIp_aAqCwRvL1JQA3iPaBJxslDA93Cnphb0x8mGsL3bA6NiufUb37fk1PzXrFzvAthiywYrWKQxr7ZBhDGKjyShpKUY4SJMnegs7gB6XmdWWzcm6b3u0C9Wp098UPBePTmlhrL6bWAjhQ8IZG4yhyBmTS_9QWmgrSAIv5Iz0qfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی (ب) قهرمان | امید هر مسلمان!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17362" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17361" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17360" target="_blank">📅 01:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17359" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار: پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟  ترامپ: چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17358" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار:
پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟
ترامپ:
چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر از من می‌خواهند که توافقی صورت گیرد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17357" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 به نظر شما:</h4>
<ul>
<li>✓ توافق شده طبق آنچه نتانیاهو می‌گوید (تسلیم کامل ایران)</li>
<li>✓ توافق شده طبق آنچه سپاه دیکته کرده (تحقق همه شروط ایران)</li>
<li>✓ توافق نشده</li>
<li>✓ نمیدانم؛ اطلاعی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17356" target="_blank">📅 00:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل نتانیاهو: توافق شامل  محدود کردن تولید موشک و پایان حمایت از نیروهای نیابتی منطقه‌ای   می‌شود</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17355" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فوری | وزارت امور خارجه ایران: ایران ثابت کرده است که آنچه را که به عنوان خطوط قرمز خود تعریف کرده است، تحمل نمی‌کند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17354" target="_blank">📅 00:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17353" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، اسماعیل بقایی:
تا کنون، ایران به نتیجه نهایی در خصوص توافق نرسیده است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17352" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جالب است که ترامپ می‌گوید خودشان تنگه هرمز را پیشتر باز کرده اند و ما خبر نداشتیم اما الان گفت که بعد از امضای توافق با ایران تنگه باز خواهدشد!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17351" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvtx7TkV0uPaBhbgKMHb4PiMaiuJJ_nsHaSvtQOa0atBhpuAKHRGAdmJKVFqfi_XMbmN5jI2Sr2YzwQf4rLA9tMrRpHULkqrlMU7DUZn_6sRfJvSO6CoSGuvyhIz_kccvSmIgAMAFzRrwFYYlS_vpJ5MgPVITE1FMl5jgvhr0pgm4wxe7T-GmXtR7mdMnmNV4USTLb_c_SFGm3tMo9FTjUYdVbg84fZtPxdkE2IdpmBmxGjBDg446nJPC7UAVWNgUyLTY4uOpVAdeaq5Y1I--S6w9l_uB-l7dhnLVPw15v7PDrFfipZaZ5ihkhfjxzNKIeaKw474TJ7pGkChaETUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!
از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17350" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل، نتانیاهو: توافق نهایی شامل خروج مواد غنی شده نیز خواهد بود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17349" target="_blank">📅 23:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:   اخیراً ایران را به‌ شدت بمباران کردیم و رهبرانش حتی بیشتر از من خواهان رسیدن به توافق بودند.  ما از همان ابتدا در جنگ با ایران پیروز شدیم، ایرانی‌ ها فرصت دارند کشورشان را بازسازی کنند، چرا که به‌ شدت ویران شده است</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17348" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!   تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17347" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!
تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17346" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فوری | ترامپ: امضای توافق به زودی انجام خواهد شد و برداشت من این است که رهبر ایران با آن موافقت کرده است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17344" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بالاخره محاصره را برمیدارد یا نه؟!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17343" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فوری | ترامپ: محاصره دریایی تا زمان نهایی شدن توافق پابرجا و معتبر خواهد بود و تاریخ و مکان امضای آن به زودی اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17342" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
ادعای فارس: احتمالا مقامات ایران با توجه به عقب نشینی آمریکا توافق را بپذیرند</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17341" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»   – نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17340" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»
–
نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17339" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— منبعی نزدیک به تیم مذاکره‌کننده ایرانی به خبرگزاری فارس گفت:
«هیچ متنی برای تفاهم‌نامه اولیه با آمریکا تصویب نشده است».</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17338" target="_blank">📅 21:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع اسرائیلی و عرب های خلیج فارس که با کانال ۱۳ اسرائیل صحبت کردند، گفتند که از هرگونه توافق حاصل شده با ایران آگاه نیستند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17337" target="_blank">📅 21:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17336" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری تسنیم:  «ترامپ اخیراً ۳۸ بار ادعا کرده است که توافق قریب‌الوقوع است، بنابراین تا زمانی که ایران رسماً اعلام نکند، ادعاهای او را باید صرفاً در چارچوب دروغ‌های قبلی‌اش بررسی کرد.»</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17335" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">باز کله زرد حرامزاده دروغ می‌گوید  محال است سپاه چنین توافق ذلت باری را بپذیرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17334" target="_blank">📅 21:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فوری | ترامپ: محاصره دریایی تا زمان نهایی شدن توافق پابرجا و معتبر خواهد بود و تاریخ و مکان امضای آن به زودی اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17333" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: «با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و مورد تأیید قرار گرفته است، من به‌عنوان رئیس‌جمهور ایالات متحده آمریکا حملات و بمباران‌هایی را که برای امشب علیه ایران برنامه‌ریزی شده بود لغو کردم. همچنین مباحث و جزئیات…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17332" target="_blank">📅 21:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: «با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و مورد تأیید قرار گرفته است، من به‌عنوان رئیس‌جمهور ایالات متحده آمریکا حملات و بمباران‌هایی را که برای امشب علیه ایران برنامه‌ریزی شده بود لغو کردم. همچنین مباحث و جزئیات نهایی این توافق به تأیید تمامی طرف‌های ذی‌ربط، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران رسیده است. محاصره دریایی تا زمان نهایی شدن این توافق همچنان به‌طور کامل برقرار خواهد ماند و زمان و مکان امضای آن به‌زودی اعلام خواهد شد.»</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17331" target="_blank">📅 21:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زیمنس انرژی:
جنگ ایران به رونق آلومینیوم افزوده است زیرا تقاضا برای توربین‌های گازی بیشتر شده است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17330" target="_blank">📅 20:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو:  امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم که اگر حزب‌الله به حمله به شهرها و شهروندان ما پایان ندهد، اسرائیل به اهداف تروریستی در بیروت حمله خواهد کرد.  این موضع ما بدون تغییر باقی می‌ماند.  در عین حال، ارتش اسرائیل طبق برنامه در جنوب لبنان…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17329" target="_blank">📅 19:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpF5Cxj2_QMxA99yGP4VlUlYgAgEafUhYHPP1b6fZkZyAb-DUbLUxy7ePmqJNSnYvmKmH9lsUrlzo9tDCputhQRhkjAi2S2SRLopwLjNwGMT13QjM8gaoWid7q6AM3khbFrV-pdM52XtSJijH0MivFD7ueOvuNGwyPuv2QItGQ_EjGguoUEQkokKA2N-7pdiP-gV25fiZMhhmJMGZkqU0jh_ep6VfQ_mXxdXgSES7omhYdmBV-wiVtb70B9TrOtB8xSupu0qgPnGlh0nttxjGV3p-S2IbPdnXcuO3AH33dirCCv_yA2JEefK0ldIb3DX4Gzk_svQt_R_nhuShxmp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17328" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODuKPhaRRz-S-9cFFYahRLhi0qbNHMuLWBrmrkUwhvwZgmT2ATnlOc-Zft36VI3HfWF60TuoZ5qtfeh_qXyDhKcW1-1894qFfmnk-AVKMP1z-8fk5sKDGdp6bjL_yE0pu7VOYG9k-fegkmAhqvoU1xJY4DYBEXLa8i_l82hdxIKuZ3eW0I0dsESrbm_65tsHPzmHUrN2wdnij0lCrS0BjPkNIs1iDor1Zv02AgsCXkaXu0QCKrnjNCKGPV7dDJzSNYX59A26wtTnONDj4dU-x2oHyV5f-QeubREF4RvvZxgBwkHSqD45t-W8-Az2lQpoibZk6jBRbe_bTTClR6bucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله ان‌بی‌سی نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17327" target="_blank">📅 19:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSnmPoa_beoEJ9qDRzKJTmY_11OjVVMy8NcvS3vUrAlKSieA-MLTsQiAVe74usXNfD04FURVwXxEYkrmSZSbI6sSuCKuqss5-Cg3bcLG1JYJYwZ_ZxVxejVz4KEj09s63jUfenfJggQMW8MyQDE5o6jvRkP-zFxbc6SoD3PBRHym-Vl_RGJBBZlEzf-bWwPJ0LGnPLbxsfbiYR5rN6sRhdxREfgt3pPP2nHDTHingvP7147YTHLDauULrHA-1voIS9I3YraNXddMiRu6pBvvjNz5cekLl2V0nDJwsGD8B5L85_1r5uZqH0P5RnsSBiNaTrExDnRP7xxhes7NXMMq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17326" target="_blank">📅 19:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز:
انتظار می‌رود که لشکر ۸۲ هوابرد ارتش آمریکا که به «لشکر شیطان» معروف است، به زودی کنترل جزایر نفتی ایران را به دست گیرد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17325" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17324" target="_blank">📅 18:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">▶️
همکاری مایکروسافت و استارلینک؛ اینترنت ماهواره‌ای در اختیار جوامع بیشتری قرار می‌گیرد
🔹
مایکروسافت همکاری جدیدی با سرویس اینترنت ماهواره‌ای استارلینک اعلام کرده تا دسترسی به اینترنت در مناطق مختلف جهان را گسترش دهد.   این همکاری شامل استفاده از اتصال ماهواره‌ای…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17323" target="_blank">📅 18:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls97_xjk0XrMHbGVxRB9mA81t1HITynsWTmBr_Exd4Q4N3oMzhTuMOg2SBfdLZeUkJB94yD9teeYm7_ZN5n2G3M8v1jkusPeno8MuJJlH69Q3RbUJo_Zjyk37h5U0qJKa8eOejw-HNCzMbAOT3UZ5nX3qZJoN6iRvC3gUkwswImIF0u7w7ouD11OknMHegFBpACGYLMq8JB2qKUnQHA2SxCgIqTPiu9g7M4eoSkqiMS5iWchwx1smgDvMlBNZ-tk_Q--MkV8HV6UBZuUQtjWyGb3AzG33jQWEDOK2FeUGJB4SotLxSYAnqiTbf-GDCeqBERO4gZd5eBllC6hEHQKgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17322" target="_blank">📅 18:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ،   «هواپیماهای آمریکایی بر فراز تهران پرواز می‌کنند و خودشان خبر ندارند».</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17321" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ،
«هواپیماهای آمریکایی بر فراز تهران پرواز می‌کنند و خودشان خبر ندارند».</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17320" target="_blank">📅 16:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17319" target="_blank">📅 16:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فوری | ترامپ به شبکه فاکس نیوز: ما هنوز به ایران به اندازه کافی ضربه نزده‌ایم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17318" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17316" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده بسنت:   هر عوارضی که به سازمان مدیریت  تنگه هرمز پرداخت شود، از حساب‌های مسدودشده آن‌ها کسر خواهد شد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17315" target="_blank">📅 16:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17314" target="_blank">📅 16:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17313" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مثلاً ما میگوییم همه اقداماتمان برای ظهور امام زمان است. یا اردوغان میگوید برای اتحاد دنیای اسلام است. روسها میگفتند برای دولت جهانی پرولتاریا!
این قرمساق میگوید نفت تان را می خواهم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17312" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17311" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!
«ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار شدیدی خواهد زد.
در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.»</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17310" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از انفجارها در منطقه دریایی نزدیک به شهر سیریک منتشر شده است.
تا کنون بیانیه رسمی صادر نشده است، اما به نظر می‌رسد صداها مربوط به درگیری‌ها یا تبادل آتش جاری در خلیج فارس و تنگه هرمز باشد.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17309" target="_blank">📅 15:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر امور خارجه ترکیه از ایران و ایالات متحده خواست تا حملات تازه را متوقف کرده و به مذاکرات بازگردند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17308" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17307" target="_blank">📅 14:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17306" target="_blank">📅 13:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حمله آمریکایی ها به 3 کشتی هندی دیگر!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17305" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در این نشست گفته بودم که جنگ بعدی در سوریه میان اسراییل و ترکیه خواهدبود.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17304" target="_blank">📅 13:47 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
