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
<img src="https://cdn4.telesco.pe/file/DxqfTBgkKDjJ63JJNlOkRgusDfIqIblkGO0He0JeRi3VV0bv8yMPGCMJ2feTY94TkekjSZXyDkaOTaaQQ2vOnQqMzc6UjYf_4J_B1bpW_8RlCVV02cRWN8cLJWOGXJFDrJb7h2me-9B0QZC4LiNZonCMGGBZ-75sp1PeQeWMgGP9EgRe_7v7goTnopnD0Tiw9HKVHf4CJ_FSle0a8fQWuw6FnqzbAABi3udivxhvG1pytW5Pr1rBbuEo9AJAnhcyl3tBFd3Ngjsjgeb6imfeJtCUcwkS5XOtG8yve5ikz8-Vr9OAPezkj2ehT_Q1vefFpzYWAhbqGTFRHBiEyqtNnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 272K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 03:23:07</div>
<hr>

<div class="tg-post" id="msg-12385">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شبکه خبری سی‌بی‌اس به نقل از مقام‌های آمریکایی آگاه گزارش داد اطلاعات ایالات متحده نشان می‌دهد علی خامنه‌ای، رهبر جمهوری اسلامی، عملا در مکانی نامعلوم پنهان شده و دسترسی بسیار محدودی به دنیای خارج دارد.
بر اساس این گزارش، مقام‌های حکومت ایران تنها از طریق شبکه‌ای پیچیده از پیک‌ها با او ارتباط می‌گیرند و حتی مقام‌های ارشد نیز از محل دقیق او اطلاع ندارند یا راهی برای تماس مستقیم با او ندارند.
@withyashar
سی‌بی‌اس نوشت این اختلال ارتباطی یکی از دلایل کندی در اعلام جزئیات توافق احتمالی تهران و واشینگتن است؛ زیرا پس از ارسال پیشنهادهای آمریکا، دسترسی دشوار به خامنه‌ای می‌تواند پاسخ تهران را با تأخیر قابل‌توجه روبه‌رو کند.
این شبکه همچنین به نقل از مقام‌های آمریکایی نوشت بسیاری از مقام‌های جمهوری اسلامی هفته‌ها را در پناهگاه‌های مستحکم می‌گذرانند و جز در موارد ضروری با یکدیگر گفت‌وگو نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/withyashar/12385" target="_blank">📅 02:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12384">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جنگ مارکت ها با ترامپ : نفت اومد زیر صد ! هم اکنون ۹۹$
@withyashar</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/withyashar/12384" target="_blank">📅 01:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12383">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Marde Tanha Remix (t.me/withyashar)</div>
  <div class="tg-doc-extra">Farhad (IG @yashar)</div>
</div>
<a href="https://t.me/withyashar/12383" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/withyashar/12383" target="_blank">📅 01:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12382">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
۷ روز دیگه دوشنبه شب ۱۱:۱۱ دقیقه تهران به شاهزاده پیغام میدیم تا من با ایشون صحبت کنم ! و حرف های شما رو برسونم ! این یک فراخان اینترنتی هست ، هر شرایطی که میتوانید فراهم کنید که افراد بیشتری به ما ملحق بشوند ! حتی شما دوست عزیز که فیلترشکن میفروشی ! خواهش…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12382" target="_blank">📅 01:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12381">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۷ روز دیگه دوشنبه شب ۱۱:۱۱ دقیقه تهران به شاهزاده پیغام میدیم تا من با ایشون صحبت کنم ! و حرف های شما رو برسونم ! این یک فراخان اینترنتی هست ، هر شرایطی که میتوانید فراهم کنید که افراد بیشتری به ما ملحق بشوند ! حتی شما دوست عزیز که فیلترشکن میفروشی ! خواهش میکنم اکانت تست بده تا همه باشند حتی اندک تا صدای ما شنیده بشود ! همین ! انقدر این کار را انجام میدیم تا هر شخص دیگری هم پیج ایشون دستشه مجبور بشه این ارتباط رو برقرار کنه ! خیلی واضح میگم من عقب نمیکشم !</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/12381" target="_blank">📅 01:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12380">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به خاطر ایران به خاطر تمام جاوید نام های میهن از روز اول این رژیم و اولین جاوید نام محمد رضاشاه پهلوی و تمام ژنرال ها به خاطر او سرباز وظیفه که اینجا خدا حافظی کرد ، اون خواهرم که پدر مادرش ۸۰ سالشونه و مریضن و تو ماشین گریه میکرد به خاطر تمام جونهایی که پیغام دادن و آرزوشون او موتور بود که هر هفته گرون میشد به خاطر حتی اون بچه هیئتی که گفت من اتاق جنگیم ! دوشنبه شب به همه بگین هر جور شده بیان ! و پیغام رو برسونیم !</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/12380" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12379">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حق گرفتنیه دادنی نیست
💪🏾</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/12379" target="_blank">📅 00:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12378">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12378" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12377">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگه تا دوشنبه دیگه  زدن زدن ، نزد به بچه های ایرانم بگین تو پلتفرم های داخلی هرجور شده خودشونو برسونن ! فقط یک لحظه همه باهم یه پیفام میفرستیم برای شاهزاده رضا پهلوی ! و هر جور شده ارتباط میگیرم با شخص ایشون هر جور شده و هر کسی بیاد جلومون زمین میزنیم فقط برای ایران و شده ۲۰۰۰۰۰۰۰ پیغام بدم شبانه روز این کار رو میکنیم شده اعتصاب غذا میکنم ! محترمانه به عنوان یه جون ایرانی تبعید اجباری شده ! و نماینده همین خونوادمون !
میدونین که من شده انقدر بیدار میمونم و نیمخوابم تا جواب بگیرم ! هر پیغام هم اسکرین میزام !
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/withyashar/12377" target="_blank">📅 00:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12376">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیغام های زیاد اینچنینی گرفتم چرا با شاهزاده صحبت نمیکنی … ولی امروز شخصی نوشت تو نمیدونی ایران چجوری پشتت هستند ما با هزار بدبختی پیغام ها و صحبت هاتو میفرستیم تو پلتفرم های داخلی !! اگه میدونستی انقدر خودت رو سر حرف بعضی ها عذاب نمیدادی!!!  در نتیجه این تصمیم رو گرفتم ! امروز ما نباید مانند دیروز باشد !!!</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12376" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12375">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توییتِ سخنگوی فارسی زبان ارتش اسرائیل و طعنه به ترامپ : کس نخارد پشت من جز ناخن انگشت من !
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/12375" target="_blank">📅 00:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12374">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : حجاج امسال دو بار حاجی میشن
😃</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12374" target="_blank">📅 00:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12373">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقام آمریکایی به سی‌ان‌ان:
آزادسازی منابع مالی ایران منوط به گشایش کامل هرمز و اجرای تعهدات هسته‌ای خود است!
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12373" target="_blank">📅 23:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12372">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک مقام آمریکایی به شبکه «فاکس‌نیوز» گفت دونالد ترامپ، رئیس‌جمهوری آمریکا ممکن است به ایران هفت روز مهلت دهد تا به یک توافق «قابل‌قبول» برسند
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12372" target="_blank">📅 23:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12371">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL7YGzUObfOUtRWux8MZUypcEyUaKaTAb49uQs8y8odFH30Z4q41N0Rj9VFoVvSuWPFOH7ZjzKYmJb_UhRE6x_g_zTY4nIiw7G_DtT37zUSTicUZKsQYiRBudRnrRtsSHUQ0X88O5Dfd_BwDqWMsZovDIES_AeUxA2KAZWmagevKYVTQXWyBKiavO_pM2n7qjbcMD4nb2rUiQA-ui9zThBA7xRpwt2rfntLWnNVLGc5YjTWhgwo0aF362PPz4oeaeY8l9LRQz0E0wHC1QzarMaaUDIMe99W5O4LtKUJC1SYQRX47LcYprvenI0OkADBv3KDzgF_za8LWSQiSvuut7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث: از شما بابت توجهتون به این موضوع متشکرم.
@withyashar
😂
🤯</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/12371" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12370">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حوصلم سر رفت</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/12370" target="_blank">📅 23:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12369">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رسانه وزارت خارجه ایران: در موضوع آزادسازی دارایی‌ها که مورد اختلاف است در حال حاضر راه‌حلی برای آن وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/12369" target="_blank">📅 22:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12368">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرچیله زمانه را بشناس…
😃</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12368" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12367">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12367" target="_blank">📅 22:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12366">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر امور خارجه ایالات متحده مارکو روبیو گفت که توافق احتمالی با ایران حمایت منطقه‌ای دریافت کرده است، اما هشدار داد که یک توافق هسته‌ای نمی‌تواند «در ۷۲ ساعت روی پشت یک دستمال کاغذی» به دست آید.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/12366" target="_blank">📅 22:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12365">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/12365" target="_blank">📅 22:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12364">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaeENVNr-iY3GCVhGF3ZCAjlgDAFjs5jLs0gUx5qXQDJcBAFaWLt5JFWAGxgEmsr355YXoKUsGyvY_VV_Q-yWF1vUtKff8RPWz9XWjtY2TRxWlu2r_SUyY53MO86tVdMBnunVQ6-TeLAK2zl3XMHz7NuTI46RBiNzvpXdsAhfhYLhZtx92FVkDxzui6UVhQVJkhZk1CUZcYGyIz07Kd2GO3mwuRecs1I5srvUfTnONVMa4-r6gkQGWoRRo7-l5WJCyx64ijgYndSTxCFOHA4ITRBPAoes-5hzbh_ynsoxa8REO0qK_ctlRPIgky1UWucjgauvq3hcf_-newC0eqgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در شبکه Truth Social:
اگر من با ایران به توافق برسم، آن یک توافق خوب و اصولی خواهد بود؛ نه مثل توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد داد و یک مسیر کاملاً باز برای دستیابی به سلاح هسته‌ای فراهم کرد.
توافق ما دقیقاً برعکس آن است، اما هنوز کسی آن را ندیده و نمی‌داند دقیقاً چیست. حتی به طور کامل هم نهایی نشده است. پس به افراد شکست‌خورده‌ای که درباره چیزی که از آن هیچ اطلاعی ندارند انتقاد می‌کنند، گوش ندهید.
برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد امضا نمی‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12364" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12363">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:محاصره دریایی علیه ایران به صورت کامل ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12363" target="_blank">📅 21:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12362">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/12362" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/12361" target="_blank">📅 21:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12360">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیویورک تایمز: یک مقام آمریکایی می‌گوید ایالات متحده و ایران در اصول برای بازگشایی تنگه هرمز توافق کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/12360" target="_blank">📅 21:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12359">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12359" target="_blank">📅 21:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12358">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مقام آمریکایی به CNN:
تحریم‌ها علیه ایران نمی‌تواند قبل از مهار برنامه هسته‌ای آن کاهش یابد
وی گفت: ما در مورد آزادسازی وجوه ایران به عنوان بخشی از توافق مذاکره نکرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/12358" target="_blank">📅 21:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12357">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو توافق وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/12357" target="_blank">📅 21:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12356">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به قول مانوک اگه الان آشمز شدید این رو هم ببینید…
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12356" target="_blank">📅 21:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12355">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طبق گزارش فاکس نیوز، ترامپ می‌خواهد توافق پیشنهادی توسط مذاکره‌کنندگان او، از جمله استیو ویتکوف و جرد کوشنر، اجرا شود؛ اگر این شرایط برآورده نشوند، هیچ توافقی صورت نخواهد گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/12355" target="_blank">📅 21:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12354">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الجزیره: یه منبع ایرانی به ما گفته؛ آمریکا داره از چند تا توافق قبلی خودش عقب می‌کشه، مخصوصاً سر آزاد کردن پول‌های بلوکه‌شده ایران و مدل آتش‌بس لبنان؛
تو متن تفاهم‌نامه، اسرائیل میخواد دستش باز بمونه که هر وقت گفت «تهدید حس کردیم» دوباره تو لبنان عملیات بزنه و بهشون حمله کنه، ولی ایران مخالفه و میگه آتش‌بس باید واقعی، کامل و دائمی باشه.
پاکستان پیشنهاد داده فعلاً بخش‌هایی که توافق شده امضا بشه و بقیه اختلافات بعداً حل شه، ولی ایران گفته نه؛ یا همه بندها کامل و تضمینی حل میشه یا کلاً امضایی در کار نیست.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12354" target="_blank">📅 20:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12353">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فاکس نیوز نقاط اختلاف در توافق ایران و آمریکا را اعلام کرد:
1. اسرائیل خواستار تضمین «آزادی عمل نظامی» علیه تهدیدها در لبنان است و ایران این را رد می‌کند.
2. تهران خواستار آزادسازی فوری دارایی‌های خود است و واشنگتن امتناع می‌کند و اصرار دارد که این موضوع به فرمول نهایی توافق مرتبط شود.»
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/12353" target="_blank">📅 20:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12352">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/12352" target="_blank">📅 20:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12351">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نعیم قاسم رهبر گروه تروریستی حزب الله:
ایران با رهبری مجتبی خامنه ای آمریکا و اسرائیل را ذلیل کرد
@withyashar
🤣</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12351" target="_blank">📅 20:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12350">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تسنیم: علیرغم برخی گفتگوهای امروز، کارشکنی‌ های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12350" target="_blank">📅 20:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12349">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علی هاشم خبرنگار الجزیره: کمتر از ۲۴ ساعت پس از ظهور خوش‌بینی در مورد امکان توافق‌نامه ایران و آمریکا، حال‌وهوای منفی دوباره سر برآورده است.
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12349" target="_blank">📅 20:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12348">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صداسیما : ترامپ چاره‌ای جز تسلیم شدن ندارد
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/12348" target="_blank">📅 20:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12347">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل:
ما آماده‌ایم که فوراً به نبرد با ایران بازگردیم
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12347" target="_blank">📅 20:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12346">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دبیرکل حزب‌الله: خلع سلاح را نمی پذیریم
تحریم‌های آمریکا هرگز ما را تضعیف نخواهد کرد؛ اگر آمریکا بیش از این خوی وحشی‌گری به خود بگیرد، دیگر چیزی برایش در لبنان باقی نخواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/12346" target="_blank">📅 19:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12345">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک مقام آمریکایی به سی‌بی‌اس: ایران قبول کرده اورانیوم غنی شده‌ش رو به‌عنوان بخشی از توافق، دفن کنه
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/12345" target="_blank">📅 19:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12344">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جروزالم پست
:
جنگ، ایران را فرو نپاشید. کنترل آن بر هرمز را تثبیت کرد، اتحادهایش را از نو ساخت و همان نهادهایی را که ایالات متحده هدف قرار داده بود، تقویت کرد
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/12344" target="_blank">📅 19:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12343">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی: مسائلی مانند ذخایر موشکی ایران و غنی سازی اورانیوم در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/12343" target="_blank">📅 19:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12342">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حسین یکتا: علی خامنه ای توی دوران جنگ شبانه با حاج علی مالکی رفتن حموم، حضرت آقا گفت فقط به شرطی میذارم منو لیف بکشی که منم تورو لیف بزنم و کیسه بکشم. @withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/12342" target="_blank">📅 19:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12341">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/12341" target="_blank">📅 18:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12340">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک مقام ارشد دولت ترامپ در گفتگو با آکسیوس ادعا کرد که
انتظار نمی‌رود توافق با ایران امروز امضا شود، زیرا هنوز جزئیات متعددی باید نهایی شوند.
این مقام مدعی شد که مذاکرات درباره عبارت‌بندی‌های مشخص در متن توافق ادامه دارد و آن را
«برخی کلماتی که برای ما مهم است و برخی کلماتی که برای آن‌ها مهم است
» توصیف کرد.
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/12340" target="_blank">📅 18:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12339">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD4Ud4tV5fDb0oIpConsCoAPL9aCgUWxKJylMlt43tC-NQ5v9qzRZU3QacIFK61dDQPNvh8_jwZo-NWquOe_yBWZAoweODPqf4HNdo4XMC9cWHizl_Qpd_rGPCXVoDHDn3OgPrTFKbbjHWsDSz0diuk2XVIzmhpnehdTVMk-kQY2Kc2H9eYrUL0n1ckHTaXTc4G-T4CKD6yAOXY-R333Kw4lch08S7SauZUByTzmkZ81CPbbQX87Q2yPtg98Wnr5LaQuAhNkU2lM_ORWSSQ3sOHzc4I80OwsKrsCS4UpSKDWnWTgWdBPp3ytPWNqY-qEfRS-M_O1a2RzdtgfZbRhqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پست تری یینگست را منتشر کرد که از قول مسعود پزشکیان است که گفته : «ما آماده‌ایم به جهان اطمینان بدهیم که به دنبال سلاح هسته‌ای نیستیم. همچنین به دنبال ایجاد بی‌ثباتی در منطقه نیستیم.
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/12339" target="_blank">📅 18:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12338">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaciDWFbQlCc6JoImH_Gmy742FhklbX6y2jYbfdiIz_IE40IF-4Us-V4-w88sauWu3jtkjvKgScq6oY4GH6jvgLYLeZNzZymV_j3LiMWJCEmCMDIpD4Z-vxDt5C8L8uiOiKgPX_3hVAa_9qlQQm87uiEHeOBySYf_hFifQKAWzMOBzewEYkJQTZ0ups27UKXDoqcI6TgJkpWNFPiVjNocA85qhIM0pkQucrR2h1xGEKXB3NheZETvBBCR23HAzjUGyaF_tYKSLTPj1TgomGaKEonXuDgby_fPUOJqTBX6nwxIMV6sOGz2z9oZUTKwUzuv5rrc39iNEQZRLVS7vM84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : یکی از بدترین توافق‌هایی که کشور ما تا به حال انجام داده، «توافق هسته‌ای ایران» بود که توسط باراک حسین اوباما و افراد کاملاً غیرحرفه‌ای دولت اوباما طراحی و امضا شد. این توافق، یک مسیر مستقیم برای ایران جهت دستیابی به سلاح هسته‌ای ایجاد می‌کرد.
اما وضعیتی که اکنون در حال مذاکره با ایران توسط دولت ترامپ است، کاملاً برعکس آن می‌باشد — دقیقاً نقطه مقابل!
این مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگان خود گفته‌ام که در رسیدن به توافق عجله نکنند، چون زمان به نفع ماست.
محاصره و فشارها تا زمانی که یک توافق نهایی حاصل، تأیید و امضا شود، به‌طور کامل ادامه خواهد داشت. هر دو طرف باید با دقت و بدون شتاب عمل کنند. هیچ اشتباهی نباید رخ دهد.
روابط ما با ایران در حال تبدیل شدن به رابطه‌ای حرفه‌ای‌تر و سازنده‌تر است. با این حال، آن‌ها باید درک کنند که نباید اجازه ساخت یا به‌دست‌آوردن هیچ‌گونه سلاح یا بمب هسته‌ای را داشته باشند.
در پایان، از تمام کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر می‌کنم؛ همکاری‌ای که با پیوستن آن‌ها به «توافق‌های تاریخی ابراهیم» بیشتر و قوی‌تر خواهد شد. و چه بسا شاید جمهوری اسلامی ایران هم در آینده مایل به پیوستن به این توافق‌ها باشد.
از توجه شما به این موضوع سپاسگزارم.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/12338" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12337">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://www.instagram.com/p/DYuUYVWMTTa/?igsh=eXI0enRnYjU0aTlq
کامنتم رک و مستقیمم برای بی بی
کارای ادایشو انجام بدید
ترجمه :
بی بی‌ جون، کار را یکسره کن.
اگر این توافق امضا شود، مردم ایران بازنده خواهند بود و اسرائیل هم به‌سمت افول می‌رود.
خیلی صریح و روشن می‌گویم: ما دوست نداریم دوران سیاسی شما هم زود به پایان برسد.
شما باید روزی در ایران میهمان ما باشید تا با هم جشن بگیریم
❤️‍🩹</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/12337" target="_blank">📅 17:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با ABC News:
من نمی‌توانم دربارهٔ توافق صحبت کنم؛ این کاملاً به خودم بستگی دارد، و اگر خبری وجود داشته باشد، فقط خبر خوب خواهد بود.
من توافق بد انجام نمی‌دهم.
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12336" target="_blank">📅 17:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یدیعوت آحارانوت به نقل از یک منبع ارشد امنیتی: اگر این توافق به شکل فعلی امضا شود، برای اسرائیل فاجعه بار خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12335" target="_blank">📅 16:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رادیو ارتش اسرائیل: نتانیاهو امشب ساعت 18:00 جلسه‌ای برگزار میکنه.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/12334" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس
:
کاخ سفید امیدوار است که اختلافات نهایی در ساعات آینده حل شود و توافقی روز یکشنبه اعلام شود
ممکن است این توافق حتی 60 روز کامل هم دوام نیاورد اگر آمریکا معتقد باشد ایران در مذاکرات هسته‌ ای جدی نیست
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/12333" target="_blank">📅 16:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رشیدی کوچی، نماینده مجلس: اینترنت بین‌المللی تا هفته آینده به روال عادی برمیگرده.
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/12332" target="_blank">📅 16:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال 14 اسرائیل:
اسرائیل رهبر 86 ساله که از سرطان مرحله 4 در حال مرگ بود رو از بین نبرد تا آمریکا با پسر 56 ساله سالم‌تر و تندروتر او صلح کنه.
با آمریکا یا بدون آمریکا، اسرائیل این رژیم رو به پایان خواهد رسوند.
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/12331" target="_blank">📅 16:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ea0c04a7.mp4?token=HDUCJ8CtiEU-su_YjFzq4gvjC6FdrkL813FlmvAymti6PGBoRiGbYetmAa-wCQUm_i6NYERPU_iN4qcOc99X-3afkrovEWypryqG7e9HYIqFZaMqNfeZnu7mgFoznnFTzoLp0Iiu2AqYkCdhjxXkBViCYcX8ma7RKE4whKa3f7FWiZ56dlsmz05OCaDKSw8etvP5bp1sX8w_xOxYPuyJfqFaic420XlkxKExdgEz7TmJYzpWYqZZCE2YNMQMCdDQiMIKDw-gkbadanaLyiMDNJ5D4pUPXQZUpPMKh3D3uySy6zf6Q5TDcELId0nplVM_V0FI1lE71Q3UxSmIqtLnhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ea0c04a7.mp4?token=HDUCJ8CtiEU-su_YjFzq4gvjC6FdrkL813FlmvAymti6PGBoRiGbYetmAa-wCQUm_i6NYERPU_iN4qcOc99X-3afkrovEWypryqG7e9HYIqFZaMqNfeZnu7mgFoznnFTzoLp0Iiu2AqYkCdhjxXkBViCYcX8ma7RKE4whKa3f7FWiZ56dlsmz05OCaDKSw8etvP5bp1sX8w_xOxYPuyJfqFaic420XlkxKExdgEz7TmJYzpWYqZZCE2YNMQMCdDQiMIKDw-gkbadanaLyiMDNJ5D4pUPXQZUpPMKh3D3uySy6zf6Q5TDcELId0nplVM_V0FI1lE71Q3UxSmIqtLnhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
ما توانستیم وارد ونزوئلا شویم و اورانیوم بسیار غنی‌شده را خارج کنیم.
نظام ایران حتی از بحث درباره آن خودداری کرده است. این باید تغییر کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/12330" target="_blank">📅 16:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روزنامه پاکستانی«داون»: فضای مذاکرات همچنان محتاطانه است؛ تهران حاضر به مصالحه بر حقوق خود نیست
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/12329" target="_blank">📅 15:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9zAslTVFT1e5RKkj4l93RatsogUWs7x1NwoskdcKb6FVUb7YCCc1Vqpd79b2WbGm5yqbMWTPTxlpi1dmMXu8O7aqIP7qY6JJYFes4WaoAi6Ldt9AI5pl7gr_VTndfqgkGLSqt-dez0kn6yO52V-Eyr0e2hxY45SxAcCFxpjyJmo4Ji2L43xKeRi_g3k2RAtjHd48CLgYoCUXg8O-Iv95IPZztc6x9E1ZUQiKztX2YtpsSUBjtuOzWGT2jb2-Ux_JaW0aQ9jQa084QGUvkchulcje1gTFL--mVbtIH_fD4i6-omY7tiUQmGEb-omeCJSJlNOFVWhdVh5ELISV9STVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به اسپانیایی واژه خداحافظ را نوشته که بسیار طعنه آمیز است و معنیه «بری دیگه برنگردی» را میدهد.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/12328" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تسنیم : بر اساس شنیده‌ها از متن تفاهم احتمالی، برخلاف گزارش یک رسانه آمریکایی که می‌گوید طبق تفاهم نامه «آتش بس میان ایران و آمریکا به مدت 60 روز تمدید می‌شود»، این عبارت در متن وجود ندارد و تعبیری که به کار گرفته شده است، اعلام پایان جنگ در همه جبهه‌ها از جمله لبنان است.
بر اساس متنی که هنوز نهایی نشده، در بازه 30 روزه موضوع تنگه هرمز و محاصره دریایی پیش برده می‌شود و زمان 60 روزه‌ای برای مذاکرات در مسئله هسته‌ای در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/12327" target="_blank">📅 14:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روبیو: اهداف تعیین شده عملیات نظامی بدست آمده
@withyashar
😈</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/12326" target="_blank">📅 14:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2b229eeb.mp4?token=WaRelDGkSXSFWOe_hM0GrPgDHRswm4uBycj-wBglOBcC0TSp62PYr8Q-Wg8B_MW0TAHALBUmTuT-IpNNMlGRcsryDYCN66PMRbenfm1zfXRdQ5aphflFNQAQdDfODRKp0tRtGisp9dYumrUznKdYK4XKAYZu0I6HiWqg3o8yr13xWVT_SyrBydYelatuW4Daz5nfkRHBgW4vJ6h3liqWU3eyeNdEHTV0bimXde06WXpdEkZEJFehiCOk4Xg5bDH2p_b_oH8MDoko5c9Pt3Z51SezRdttk9s2VR-kPZBcly5bZM8cCVJxY0JpVMOMKApWGmsQfjv0dGQuaUusMDVaxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2b229eeb.mp4?token=WaRelDGkSXSFWOe_hM0GrPgDHRswm4uBycj-wBglOBcC0TSp62PYr8Q-Wg8B_MW0TAHALBUmTuT-IpNNMlGRcsryDYCN66PMRbenfm1zfXRdQ5aphflFNQAQdDfODRKp0tRtGisp9dYumrUznKdYK4XKAYZu0I6HiWqg3o8yr13xWVT_SyrBydYelatuW4Daz5nfkRHBgW4vJ6h3liqWU3eyeNdEHTV0bimXde06WXpdEkZEJFehiCOk4Xg5bDH2p_b_oH8MDoko5c9Pt3Z51SezRdttk9s2VR-kPZBcly5bZM8cCVJxY0JpVMOMKApWGmsQfjv0dGQuaUusMDVaxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرحسین ثابتی نماینده تهران در تجمعات شبانه :
ممکنه جنگ یک ساعت دیگه باشه، ممکنه یک روز یا یک سال دیگه، اما قطعاً قطعی جنگ.
حتی اگه آمریکا تمام شرایط ما رو بپذیره و امضا کنه و تسلیم بشه، باز هم جنگ خواهیم داشت.
حتی اگر تیتر همه رسانه‌های غربی درباره نزدیک بودن مذاکره و توافق درست باشه ، من بازگشت جنگ رو تضمین می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/12325" target="_blank">📅 14:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیانیه منتشر از دفتر نخست‌وزیر اسرائیل به نقل از یک منبع سیاسی (وای‌نت):
در مکالمه دیروز با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عملش رو در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، حفظ میکنه و ترامپ هم حمایتش از این اصل رو دوباره تأکید کرد.
ترامپ روشن کرد که خواسته‌اش برای خراب کردن برنامه هسته‌ای ایران و حذف تمام اورانیوم غنی‌شده از خاک این کشور ثابت میمونه و بدون این شرایط، توافق نهایی رو امضا نمیکنه.
نخست‌وزیر یه بار دیگه از تعهد طولانی‌مدت و خاص ترامپ به امنیت اسرائیل تشکر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/12324" target="_blank">📅 14:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تروریست
سردار قربانی: اسرائیلی‌ها بدانند قاآنی تا زیر سنگرهایشان می‌رود
سردار «مرتضی قربانی» مشاور فرمانده سپاه تروریست پاسداران: هیچ‌وقت از قاآنی ترس و واهمه ندیدم، اسرائیلی‌ها بدانند قاآنی تا زیر سنگرهایشان می‌رود!
@withyashar
🥴</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12323" target="_blank">📅 14:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002092c0.mp4?token=YM9vSBEo4zD_AFdoMU0G5d9wQE1q0GcKIHAtlmmlNxybvLgFpE3Qcs135uZxZsJ6pY11JOD0OZtnyBHatotCapVXU4Qwa5l3CL9l-h6qsH6mc1SOFLCVWYEr5XoItBOYnG8BbtvmAK2b-OjPMILwMbBFNMjQ6_zpWji5MeFLYTSvsVwR7u97hzuEYICP4vUZQWv1-ffNtWLAG5pBQpSFS0SVJsroPLmDRWjIiqQwuhg14CCjrrax4KSCSxreA6mSEAH9boSMI-8XT4vEdiux4KJ0ihYNNikEoFjUFnhVcUAXRzXasylVADJWWx0_vu0gAEx8sI7ymfKtok0EISZfvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002092c0.mp4?token=YM9vSBEo4zD_AFdoMU0G5d9wQE1q0GcKIHAtlmmlNxybvLgFpE3Qcs135uZxZsJ6pY11JOD0OZtnyBHatotCapVXU4Qwa5l3CL9l-h6qsH6mc1SOFLCVWYEr5XoItBOYnG8BbtvmAK2b-OjPMILwMbBFNMjQ6_zpWji5MeFLYTSvsVwR7u97hzuEYICP4vUZQWv1-ffNtWLAG5pBQpSFS0SVJsroPLmDRWjIiqQwuhg14CCjrrax4KSCSxreA6mSEAH9boSMI-8XT4vEdiux4KJ0ihYNNikEoFjUFnhVcUAXRzXasylVADJWWx0_vu0gAEx8sI7ymfKtok0EISZfvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بالاخره توافق رسمی‌شد
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/12322" target="_blank">📅 14:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مهر: یک پهپاد اسرائیلی بر فراز هرمزگان سرنگون شد
این پهپاد که کاربری جاسوسی و شناسایی داشت، با شلیک پدافند ارتش سرنگون شد.
لاشه پهپاد متلاشی شده اربیتر با همکاری ناوگروه دریابانی فراجای هرمزگان کشف شد.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12321" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/12320" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/12319" target="_blank">📅 14:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احمد وحیدی فرمانده کل سپاه:
فتح خرمشهر یک الگوی خوب برای نابودی کامل اسرائیل است.
@withyashar
یاشار : همین فرمون برین
🤣</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12318" target="_blank">📅 14:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش کانال 14 : ممکن است ظرف چند روز توافقی بین آمریکا و ایران حاصل شود که انتظار می‌رود لبنان را نیز شامل شود و احتمالاً به پایان درگیری‌های اسرائیل با حزب‌الله منجر شود.
بر اساس جزئیات منتشر شده، ایران تنگه هرمز را بدون دریافت هزینه باز خواهد کرد در حالی که آمریکا پولی به تهران منتقل نخواهد کرد و به هر دو طرف مهلت ۶۰ روزه داده می‌شود تا مذاکرات هسته‌ای را ادامه دهند.
تحریم‌ها علیه ایران باقی خواهد ماند به جز تسهیلات محدودی در محدودیت‌های مرتبط با نفت
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12317" target="_blank">📅 14:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/12316" target="_blank">📅 13:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ما عمر نوح نداریم انقدر صبر کنیم !
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12315" target="_blank">📅 13:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Pishro (instagram.com/yashar) – Sonnat Shekan (t.me/withyashar)</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/12314" target="_blank">📅 13:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو:
خوشحالم که رئیس‌جمهور دونالد ترامپ، بهترین دوستی که اسرائیل تا حالا در کاخ سفید داشته، در امانه و مهاجم قبل از اینکه بتونه آسیب بیشتری بزنه خنثی شده.
خشونت سیاسی، از جمله تلاش‌های مکرر برای ترور ترامپ، باید بدون هیچ ابهامی و با قاطعیت کامل از طرف همه محکوم بشه
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12313" target="_blank">📅 13:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12312" target="_blank">📅 13:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عجب سکوتی …</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/12311" target="_blank">📅 13:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29d543059.mp4?token=G_A0Xb4QrHHQ7TslLVmWP2IIZcCzQT1I9-M3obrS-pKxqbSwFajRlmkg1QGCWxILhhPfyQmAVt5Ivql4iKW1kQXPgNVTU6RvPlmBQZJ7mmt94d3ixAbzgFPd0aUD0PyBf6THCFj4JlZcWLMT7OPiSyoyu9hAoIwU-xvmCP8WYK3g8BqGA9HWQdNX65Z4o9QGW7-q6oTe7ktr4W50h2EkM6Jszk6Qf0zKAMI5vkQxb5mA4nk5AWx48bhy_dJX6bA0bkfVz5TXX5xESwsUwDDtu7LdiBOLWO58ocNZHAG8HdikTcVLyEFLh1Xhm96uZyPomE6K2ro803ZlmJuWD6AG8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29d543059.mp4?token=G_A0Xb4QrHHQ7TslLVmWP2IIZcCzQT1I9-M3obrS-pKxqbSwFajRlmkg1QGCWxILhhPfyQmAVt5Ivql4iKW1kQXPgNVTU6RvPlmBQZJ7mmt94d3ixAbzgFPd0aUD0PyBf6THCFj4JlZcWLMT7OPiSyoyu9hAoIwU-xvmCP8WYK3g8BqGA9HWQdNX65Z4o9QGW7-q6oTe7ktr4W50h2EkM6Jszk6Qf0zKAMI5vkQxb5mA4nk5AWx48bhy_dJX6bA0bkfVz5TXX5xESwsUwDDtu7LdiBOLWO58ocNZHAG8HdikTcVLyEFLh1Xhm96uZyPomE6K2ro803ZlmJuWD6AG8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
🤣
بی بی عشقه</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/12310" target="_blank">📅 12:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۴ اسرائیل: نتانیاهو به وزرا دستور داده است از بحث در مورد توافق قریب الوقوع بین تهران و واشنگتن خودداری کنند
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/12309" target="_blank">📅 12:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/12308" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تسنیم: اختلاف بر سر یک یا دو بند در یادداشت تفاهم ادامه دارد. اگر آمریکا به ایجاد موانع ادامه دهد، امکان رسیدن به تفاهم وجود نخواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12307" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز به‌نقل از یک منبع ارشد ایرانی: ایران تحویل ذخایر اورانیوم خود را نپذیرفته و موضوع هسته‌ای بخشی از توافق اولیه نیست
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12306" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فارس : ‌
احتمال دبۀ آمریکا در یکی از بندهای توافق اولیه؛ ایران بر مواضع خود ایستاده است
درحالی که مذاکرات به‌سمت توافق اولیه پیش می‌رود، منابع آگاه از احتمال بازگشت آمریکا به رویۀ قبلی و تخطی از یکی از بندهای مورد توافق اولیه خبر می‌دهند. این چندمین‌بار است که واشنگتن برخلاف توافق اولیه عمل می‌کند.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/12305" target="_blank">📅 12:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای العربیه: دور بعدی مذاکرات بین آمریکا و ایران ممکن است در ۵ ژوئن برگزار شود.
واشنگتن و تهران هنگام آغاز مذاکره برای توافق نهایی، روسای هیئت‌های خود را اعزام خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/12304" target="_blank">📅 12:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الحدث به نقل از منابع: توافق اولیه احتمالی بین ایران و ایالات متحده «اعلامیه اسلام‌آباد» نام خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12303" target="_blank">📅 12:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بازنشری دوباره از صحبت های بسیار مهم از صحبت های مانوک درباره مذاکره و آینده ایران
مجری  :  آیا به توافقی میرسند؟
آیا مذاکره می‌کنند؟ یا ایران رد خواهد کرد؟
مانوک خدابخشیان : ایران رد نخواهد کرد، اگر بپذیرند خلع سلاح کامل می‌شوند، و مجبور به پذیرش بقیه شرط ها حقوق بشر دیگر برگ کوبنده ای نیست زیرا صدها برگ دیگر وجود دارد
مجری: ترامپ میگه پیشرفت زیادی در ارتباط با ایران به دست آمده! از این پیشرفت منظورش چیه؟
مانوک خدابخشیان : دونالد زبل بزرگترین خواسته اش اینه با یکی از این ها سلفی بگیره! ایمان داشته باشید«اینها با یک جماعتی در تهران ساخت و پاخت کردن!»نه این که رژیم بمونه!
یادتون نره!
همه ترسشون اینه امروز آمدن مذاکره کردن کار تموم شد ، استمرار پیدا کرد این رژیم ،نه اینچنین نیست.
«این تحلیل های آبکی رو بعد بذارید و بعد بگید »
آمریکا جایی که رفت مذاکره کنه مذاکره نمیکنه ، باز تکرار میکنم « حکم میکنه »
ببینید آیا رژیم جمهوری اسلامی حاضره مثل صدام حسین تحقیر بشه ؟ اینا به نوکر صدام گفتن برید بهش بگید تمام سلاح های اتمی و شیمیایش بده به ما و بعدش میشینیم مذاکره میکنیم و دیدید صدام حسین تو سری رو خورد چرا ؟ چون «بازی تموم شده رژیم کارش تمومه »
اگر یک آلترناتیو الان بود و اطمینان خاطر داشتن اینها در ایران بحران به وجود نمیاد قطعا عمل میکردن و الانم قول هایی گرفتن!
دلیل خوشحالی ترامپ هم همینه
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12302" target="_blank">📅 12:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/12301" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کیر استارمر، نخست وزیر بریتانیا:
پیشرفت به سمت توافق بین ایران و آمریکا رو تبریک میگیم. باید به توافقی برسیم که منجر به پایان درگیری بشه. حیاتیه که ایران هرگز نتونه سلاح هسته‌ای داشته باشه. با شرکای خود در جهان پیش میریم تا از این فرصت استفاده کنیم و به یک توافق سیاسی بلندمدت دست پیدا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/12300" target="_blank">📅 11:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12299" target="_blank">📅 11:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBFah_zdhDXNMY2SP1bvkxIzXyz0bi58rTHY8xY2qYLRVmIMbHWTmcSWc4E2zkYqjjGqVECweeUjOXy5T7rAYSjVLPwl02BHkAEQ0rke8hd8RRjii0uR-pqqWoIJSjRVBP9Rd56MSomhoBw3hhVBsLSna_rqiXC0cI5mpAUs06dkSsnVQXQKOd6ZChr5BE0imMoroGN94seqr1uVIn957OqUt1tPhLmd2AEWdRMFAKKkcoGkXaSwUxWkRwbHe9itueYMYFewrMKSkmCIVIaDgaJE2oPwFXwYV1uNxiNMCI3WPGbMuL5FaElHDvQLudJQ06PdEUOGGNOkiaNfa2HbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">B2 رسید
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/12298" target="_blank">📅 11:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/12297" target="_blank">📅 11:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/12296" target="_blank">📅 11:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انتقاد تند تد کروز، سناتور مطرح جمهوری‌خواه از اخبار توافق آمریکا و ایران :
به‌شدت نگران چیزهایی هستم که درباره توافق احتمالی با ایران می‌شنویم؛ توافقی که بعضی صداها داخل دولت آمریکا دارن برایش فشار میارن.
تصمیم ترامپ برای حمله به ایران، مهم‌ترین تصمیم دوره دوم ریاست‌جمهوریش بود. او کار درستی انجام داد و ما به نتایج نظامی فوق‌العاده‌ای رسیدیم؛ از جمله نابودی تمام موشک‌ها و پهپادهای ایران و غرق کردن کل نیروی دریایی‌شان.
اگر نتیجه همه این‌ها این باشد که حکومت ایران — که هنوز توسط اسلام‌گراهایی اداره می‌شود که شعار «مرگ بر آمریکا» می‌دهند — حالا میلیاردها دلار دریافت کند، بتواند اورانیوم غنی‌سازی کند و سلاح هسته‌ای توسعه دهد و کنترل مؤثری روی تنگه هرمز داشته باشد، آن وقت این یک اشتباه فاجعه‌بار خواهد بود.
جزئیات هنوز کامل منتشر نشده و امیدوارم گزارش‌های اولیه اشتباه باشند؛ اما اینکه راب مالیِ دولت بایدن از این توافق تعریف کرده، اصلاً امیدوارکننده نیست.
ترامپ به «صلح از طریق قدرت» اعتقاد دارد و رهبری قدرتمند او همین حالا آمریکا را امن‌تر کرده. او باید همچنان محکم بایستد، از آمریکا دفاع کند و خطوط قرمزی را که بارها اعلام کرده، اجرا کند.
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/12295" target="_blank">📅 11:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دلم میخواد یه ویس بی‌پروا بدم ولی افسوس ….</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/12294" target="_blank">📅 11:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خامنه ای کپک زد
ترامپ به ما کلک زد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12293" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال 12 اسرائیل به نقل از یک مقام ارشد اسرائیلی:
توافق احتمالی اصلاً خوب نیست؛ چون به ایرانی‌ها این پیام رو میده که سلاحشون به اندازه بمب هسته‌ای خطرناکه و اونم تنگه هرمزه؛ ترامپ هم فکر میکنه این توافق فقط اقتصادی هست و شامل باز شدن متقابل تنگه هرمز میشه، ولی هر قدمی برای حل مسئله هسته‌ای وابسته به خروج اورانیوم ها هست. و اصلا معلوم نیست بعد از مرحله اول اصلاً چی پیش میاد.
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/12292" target="_blank">📅 11:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور خارجه آمریکا :
«ترامپ اجازه نمیده ایران به سلاح هسته ای دسترسی پیدا کنه احتمالاً جهان در ساعات آینده، به ویژه در مورد تنگه هرمز، اخبار خوبی خواهد شنید
»
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/12291" target="_blank">📅 11:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تسنیم : پیش‌نویس توافق با واشنگتن تصریح می‌کند که وضعیت حاکمیتی تنگه هرمز به شرایط قبل از جنگ برنمی‌گردد و تنها تعداد کشتی‌های عبوری ظرف ۳۰ روز، همزمان با لغو کامل محاصره دریایی و اجرای تعهدات ایالات متحده، به حالت عادی باز می‌گردند. تهران بر حفظ حق حاکمیتی خود بر این تنگه اصرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/12290" target="_blank">📅 11:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر امور خارجه آمریکا :
«هیچ کشوری نباید از گذرگاه‌های دریایی یا حریم هوایی سوءاستفاده کند و آزادی کشتیرانی باید تضمین شود
»
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12289" target="_blank">📅 10:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال 14 اسرائیل : ایران تنگه رو بدون هیچ عوارضی باز می‌کنه و آمریکا هم هیچ پولی نمی‌ده و تحریمی رو برنمیداره فقط اجازه میده به ایران بتونه یکم نفت بفروشه ، احتمالأ اسرائیل هم حملاتش به لبنان رو قطع میکنه ، خلاصه اگه پذیرفته بشه یه آتش بس 30 الی 60 روزس که برای مذاکره داده شده بدون هیچ امتیازی اجازه نفس کشیدن میده به جهان
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12288" target="_blank">📅 10:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اکسیوس؛شرایط پیشنهادی تفاهم‌نامه آمریکا و ایران:
🚨
🚨
🚨
🚨
🚨
🚨
🚨
آتش‌بس ۶۰ روزه بین دو طرف.
بازگشایی تنگه هرمز بدون عوارض.
پاکسازی مین‌های دریایی در تنگه توسط ایران.
رفع محاصره بنادر ایران توسط آمریکا.
معافیت‌های تحریمی که به ایران اجازه صادرات نفت رو میده.
تعهد ایران به مذاکرات درباره تعلیق غنی‌سازی اورانیوم.
مذاکره ایران درباره حذف ذخایر اورانیوم بسیار غنی‌شده.
مذاکره آمریکا درباره رفع تحریم‌ها و آزادسازی دارایی‌های ایران در دوره ۶۰ روزه.
باقی‌موندن نیروهای آمریکایی در منطقه طول مذاکرات.
پایان گزارش‌شده جنگ اسرائیل و حزب‌الله در چارچوب این توافق.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12287" target="_blank">📅 10:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب تشکیل خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/12286" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
