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
<img src="https://cdn1.telesco.pe/file/YteaAchGTUICjWIjKYr7VMAhiz54oUQFoL0S3JT_TcIpbvyfmx_UAAGRkLFAnFGvzFODgbYw7_4RGymzaz1OMDBzgERoFcN4yVBjgMCm8lTUPx5A98uQ45xeq_9dDKRM51s11_POQQZ2sde16Ef5N6iMf6sOZVJg8SquP3x9kjMy-WdWnWSBsySwjPGtxNe2JsQSH-BshO1H28ijlBG7bBsS_v23NNKCcymibSIb0gWaOGnSCXRclfwkbry75MLwSBOFCrDMLFuS2jVeJLXAZYQ3lAHXIApp5T7P0dhtuzWYSP7WqziTUG3djhPjy0s59m3hlrU4J3HKflUFyLPpuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 11:44:08</div>
<hr>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syaTOdCbX9V3a3BGL05An-KQCFqZqMpgmZQDRXOhMo-b7l_B_CFnPmDmJYQnSAAXJdoB8HzjrpMW4bym9-8F23MjfUWmeR549bdLHJ3dSkp58ZaE0X0muk5fBLXn0970qDNy4hgui-t2PPF5Qc47HJo53Z8okXnQkbL7aFgtjEoTXKYeclqR6l7XQXk4638210dY3HKUH-H9z_uuQSfjoP_jb4vzXICUXWg_TJzGtNQjYg2fcLp1W1LIGncUz0gSO0uzIviDM1SdMls_AKljVkZS1bD-YBmkA9uCcbeL5v8iOK4QNdSozna5jvr4mUy2XQUZ0Bv-bmU8QZF5uUwf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sI-SCDey-3unSSPSJ-r3ZAoebRuFU2lfQXLK-KX096CNn0cbFbQ4s01UZwnv7XCaulrraTcP4CISQgmu2EKPWlyAM40IZ7ZLiHc3C7akBHYcOJTTAGWGX_bX02pW6gW_LLy4SA_j5vJ9b8zFwgx1yr1bcYromVI5MgBK00lXhmQvfK0jQM4c_779aU30gz-21KqbeUwdCID8RDQgSUCSHIZq5jMksCubs9ug1L9FiTZ1VB5dwb69OJ_POImDUL1U6zPVPeBQWc_aTF3PazFVvTbl7m1ZjQtT_dA4SjteL0ZL6sCD8XQhlD-OBK3WnJjgo8uZlPCtF0qCMRkBDTaswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dDs1AAwGL6Vyb-5DLjsyhZ2BttyOYD1aVJiTIpuqlEDY0MUJ_B7idEsGbbIbZB8MKlHY1R_FftCa1glRwHeZwTcunMUQj2wFBQbpUL1z3sk9IBOPZzd_8C1Le_Qc_VehzR2eh5k4ITGfw7dBCH6eL0JQwJ1KT097uq-vJ4pUANbRBPNTFl6RHencX69U9DzVlfcY3mIkNYyqh0ihdgNUBSFd-_0u3KuWcg0c4vICvzsmevamcsE2wBFELIiowz3LNfGjpU6SxkuMf9W9wOI0vxiIPmbdDF0m3KUaVcfdHBsRtKVWpx-KwnhWMakWrCwkP1-kF6puT2_rn6u74pI14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B4-9iPlUZCxUbI_Vvxft7m8OmW-mArBlkU25vddBj4xp8ktyp1QJ5GQTwAq9I9ShFcBcSDNz0HehiqYrqdQYEhnLOSMiZ_xd3L1yA0-UCf4Mbpgoz3lRfLKEgkQiKC7sZbp6vk3xYeKHu7K9lq4TFwz4157bgRb1UQO4SXguDrf3YSoPQjnhKMt6R6jQQMoLYkjoMC4hsW9lEv9Kk4St7rmczOxUVH_aFTno7hATqhUV8oYXQmxJy-MujiN--4CuCAJoI3-xuoICbvoV4PbWrKSuBruorlVAy8I6YprWMCKhW71dq76SbsX4cA7dRe3SQrvdNW0q5efFMnqNV3S4Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7kll4cxYjrZCnikxBzZ7kr4LBypkMHZMzxcQdlzyAWDjWHmljINlb4nRPDaPKrGOoXasCHxgIL18YC5cmkW8mInazpZ7ITVGrxPb7SB0endUocxBgfSQAPwLIxTzfyh2aNoc-FZhHCnHt7HIWPunRqifCayvX_9-IxFXZKDUL9Wg6zbmc8idzRH2diQlm1qU8qQz-Nsvdn02SO2cbaDkcXPBZDiH2s2rKhQ4Q6diy2-8bfPNysN10r2vuoz-ZXjtJAGqfeje0H_7E5T8OfqqVYfSx7Muj6DE4eHefcapZ3KB8I8TBtwm12-Raz7EBZ7eHYSem1IfKZzncDUTlBXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=CxJ2B8WHYI7qbhqg7z74xhOLrBIPbFz0W2F6csWKcd56Y4d0RD-h_5C5t01R1HdjLGb0aKmBRgKfSlG-1ac6cYdP5iy59_F23B2OX43VaTyBnTeKZm9UcvJGcNQUUbhLfnFFX4G9DJQh1AI33vaE4LzLgqojhlhK94yiw6adicT6OZAEjX-z-_Wh9EcMaNuP27h-j4yI-Imb6OswB3oMStjPyVNA6kO5DEEmZYVJgmcaBBdl3XbOyxuMSUzQdbiRrfC-uEmwvIMaAu0s6Q5ZtW8EgtFuMIDGgfOk3HnSRsIQGnVoVRrAHy_k2hCeVyPhtsmbnIy9xFs-MowdByt2hLa7QuYY2iV3nvrCQNw09yqxcK_st7qoux6JBgspzCZU5dofA4ofBZeEeQPow9imyBA7SriO61PxjZ7sRM4w-rtRzgjuLyEoQ-z3uQqJmk92kEyqCKJUDm2xbgovE7VC3bdujwjiqQAdyn5SodKg_JlgwBfw3R323JBUPSFlCFDvSkjyoLscEl6kPdcVtbB937s_DnKu0NfbMMwCPkRvtn2ux1PmOjmZQDd9bNjMCIdZYkOjQVBJ_49jxl1GZrFPIrfzb9GfGs5ISJqU4Pb7fpedmTPJI7TWMsZX3QGY7xR5tkghwuNXlud3fh-lGbhtUhtu5CSO7QmRKZP5AyYOedw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=CxJ2B8WHYI7qbhqg7z74xhOLrBIPbFz0W2F6csWKcd56Y4d0RD-h_5C5t01R1HdjLGb0aKmBRgKfSlG-1ac6cYdP5iy59_F23B2OX43VaTyBnTeKZm9UcvJGcNQUUbhLfnFFX4G9DJQh1AI33vaE4LzLgqojhlhK94yiw6adicT6OZAEjX-z-_Wh9EcMaNuP27h-j4yI-Imb6OswB3oMStjPyVNA6kO5DEEmZYVJgmcaBBdl3XbOyxuMSUzQdbiRrfC-uEmwvIMaAu0s6Q5ZtW8EgtFuMIDGgfOk3HnSRsIQGnVoVRrAHy_k2hCeVyPhtsmbnIy9xFs-MowdByt2hLa7QuYY2iV3nvrCQNw09yqxcK_st7qoux6JBgspzCZU5dofA4ofBZeEeQPow9imyBA7SriO61PxjZ7sRM4w-rtRzgjuLyEoQ-z3uQqJmk92kEyqCKJUDm2xbgovE7VC3bdujwjiqQAdyn5SodKg_JlgwBfw3R323JBUPSFlCFDvSkjyoLscEl6kPdcVtbB937s_DnKu0NfbMMwCPkRvtn2ux1PmOjmZQDd9bNjMCIdZYkOjQVBJ_49jxl1GZrFPIrfzb9GfGs5ISJqU4Pb7fpedmTPJI7TWMsZX3QGY7xR5tkghwuNXlud3fh-lGbhtUhtu5CSO7QmRKZP5AyYOedw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ry1XmvwqybXnFpK2cl7JrY1q_F2S-T2gTwSixCG6xJNqnM4jZsADOoZxgXKAozkTjmaalNC8IeMYHfBocmD4TVbgLOwrx8V86k3oddvCKz_fVOtnRQdmRh8hsGE7qYkLeZan2i50aU05KQY9VVWY-iHufQIsItQXkduvq3k0i5d-9h-8ryot-W91IFjDcYwyOMa-NxiqBw-yZ4xIz_A8cjJWRpv8JH2_MxZ0yW5E9Zf-eNYGtZfm7tchmQz1b0MB4FpS8W6MnbbBC_BOpOPVRjRiqHZ3Yz-bJVzBSpV3u7pwa2BrRjYvI5xL63tQGvrG4kdweW6WMg3geKKw1XQJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/daGO0Dek0SnFx0X1cEQRPC62EEoB0hX6gOKOA76iIylSRKGkD4BxWuadnomSGHB_ves_84juMk4gfBvga9CtskvWfZepMXy255xEjgDBbiHm3GGG8BSAW5wHCBkSkOHUeBcchBlqQm1b3MiHdt3LVncoiTSsIDUbdXC5RLlThyY1Em5OWCA_IZKNJVICmKA9VvjShUUd6IXVhEMHwawH4eSNGcRExE7kHfrI86Y0D8sUpy8vF84JxZCcY2dKprj45MeQsLtKuMGIKLnx15hIACi48jRGwTt9kzqY8F7D95W9hONOPs5A239ib0Dm2xx-LPYhmGAhDJF1nNFU8iwrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sJTofWgA3cmGxSxkUxxRzNTWG86y8pbohqeN21lnHm1orEAqdoatyqdz3prd1-XZuesO0CwUh99KFi5Us-MOXhhM7VdDH9sekfatDBQ17qR2ZhNU3GIzGvwSkBOm3yFi-2M01kxF1NZ23G3nmge25jFlNzJy3gqyzN8xZkhjAf3yKtCcH4fJWjM7R2EJQdmC78vCPQZOTgPGPbh8HOPULY7UDdpeLMPAZVnAmqXqWRLVkK5cmlQgw98sKECBOZFYhHPBgAMu_yEYADQB17sU0OWWhV8LCj1ODEmTw2AHu45EHrHF_yBZqoP8aeobWzofT35YvmbnHd1H-LeDh_q-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NUlUqPQ8L4OaABySt2J6gjx4K2PL2pheYZV4HenAw9kyCGPw8YVwVvMWVNSghqXIzUiymbo5TGcuWyhqADNJjzaD-YxswsK_FnskhdxYNpaaP0RSvQna2tb-RNzqTjiki25dDpvTTmE2El_05zDZD2qgjL16pz0ucgG86W9D5l9t3FQPQmT28Kv8X4ttzVBWLJitxP2T93t3AnikOIvy2v3ZoOEUNUIj4QrvShXsPS4R444_c2mto-35Zvhp1-oRy0D5BkzYpg5sIQFOG5IjICuHXyF_V0Utr5s2djd43NX8Tjl0isUcRUIzxb5q-G8v9zH-9k4l5FEU2AIcEwB7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LixqZ2b6HkgDBKGf7mXS6pNJMZZz9OUMYkJRrX3v6EYSviQ7QjNTL_zu-X1zQkOhEkamQsK-be5KDvx7qJ2DNepSoao4WoRGnGFPcorub-CIDYfJXe0pZUobF5vdqRccg7rqcqBe-kmQyn9tGX8PLYdHYxoIvhe-5YV3zJp8bpBiN9GZx4PvKurqX-cfXohQ6nZSgHJgriKQE2Y7ayR-Hhd7QzXL5tyyD7zGmfHzY01-Ye4auZOzTjUeSvpOnJ_wAj50ea73Ae3SauNUc4L0CaL7fJ42ZqSKRu04hvdZ0rZPXqSuWu649yvzKkbT2HTL8kOitphkVCOYHwHwbGFpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BoDWne2By3B-vdaP9bmDGYGNza63Q0C4Fzj4EH8jQEpfj6JbVpSLBGE3_Ore1i-Qp20tuaTS27D9PouXWeYdvy5bLlC-rprntdHHgXEMg06Fb-6hOwaK3Pjvcsx6ktQ3hHgt1qbsSMk5ZluUjJHqxKfltuN_8tgD-e5q8EVgyjmf5fYGB2Cj95JKONW-UXQN-4zvjK6AmfSglWybl_HCN1_5Ru1-EWM0uAXbP6QFT_nf8T0C05vNHM_zSb-al4TBYpqL22d8gqA7w9yjL8rvdDgaJcRbaJJrVycxNwrZyc11NNH_xt9yS3Dw5R6OFvuIXaUeveEa1et-O8ZP5Gn6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KVixhDRzti_c0WUD_tIEpgF3JTn6Z8jNs6TqUIFty7maFiuOobIgjRBq5pU7GiQW3k4tZ2_Gkp_2sh3LVHvHTp5bcsPc84yqtqdWfwLk7-hB3JsnfgBwzNANKSkBgA4QQv8j46CuzOQ6rNJELA61HfslUHNPxbFweK0aLbYaiixsnGbz1ZuDdUoqTPTMV33wHF8NhP98AFdYFRdhVqe-C1G_tuMhSBdBeCi4wiVIhlJVtlIWWz4Jlce-8pmBHdqk17xSfBxdLNsDdWdzUlxT1BycBLXqzUWd_iR4qBFAZMg32pX5E6xFPRUIfWyUUJl-PHtcImsB9mG8yK5xFRTfkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=WQIyDGS2eECLyQlQfWzpPXDhcQdtoogW9aR_Ct0ifaQlJ8GodPHdEEEC1WmKyt9OMpSUIF9V7ROXPuVVhpThs6ah0RE_AMiBXTlYhqsM290L7_rGXa487IaQ9XXvTem2gI2CSxVuaCyKuta6l0nh3xY8CVWU93AJyTPZ1o9TwJPqW_T1ror91j1tKN9PgPsyUL4bF0m3LWh4C29AITxY2FJ6K3V7mcyzo9G0RcsKpZnCjF7t56lKkBRBpdsVC-MSRzk0z3JUbHSxo3bouUvPBKggJU7RFoTncKyeFamnqW-H0gaZXXHnb5s61SYORfzws11qJlsDhUnD_wM9mgItuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=WQIyDGS2eECLyQlQfWzpPXDhcQdtoogW9aR_Ct0ifaQlJ8GodPHdEEEC1WmKyt9OMpSUIF9V7ROXPuVVhpThs6ah0RE_AMiBXTlYhqsM290L7_rGXa487IaQ9XXvTem2gI2CSxVuaCyKuta6l0nh3xY8CVWU93AJyTPZ1o9TwJPqW_T1ror91j1tKN9PgPsyUL4bF0m3LWh4C29AITxY2FJ6K3V7mcyzo9G0RcsKpZnCjF7t56lKkBRBpdsVC-MSRzk0z3JUbHSxo3bouUvPBKggJU7RFoTncKyeFamnqW-H0gaZXXHnb5s61SYORfzws11qJlsDhUnD_wM9mgItuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA4j1qjvNaaC-s2UoeUhFOs4AOsxFEXFrl514gjqzmPIwZhHUWldgWuWZU_RFrseVzzQAiIdBPxZ4lU7M-bye6AtRqyg1XyT4HwJQgpl5L6riPDGlFe435wy61JvZ2YYDNF6v0W5ov2tV6S7ngzn_fq8hCeqlQiUvjB9zLyooHAij9m3PnDNQT8uwIw3wlMRAOR14fw0aLuuqGRAPpgB0av296FPqGQXgCmepTgKCdj99MWBi7q00QwwPuq2LOS3D5bfUKUl91gzadx72077Rv_VnMLU5-LZ5V0CHoMRBGW2JYizTsfbNrZZjRWlYE-x_2z1Kzrg4NQkiGorAiWWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mMW9OO1g1fA67q9h2wzReE19XbWcO1gOLnRoxJ-zXAAQ_3QPj7yFbxtK4sz7MUTeWSdj4US_d39aXU9dxQWdUGQKrb4ac-dN2VpOgn4Gp2zjuQLIcrFUXYRzpBVPB7A_PB20awpHB8FCtWhW26CMJ53UvF4nqtAaZsWqEvw8lQg7gG5MfWSc7g-BJviF5kc0nOUY93aY4FIyBbqg79FaMJWWS3PfLJml5riPNq3i4zbMeYAkka2s7OuS7VTrunCmoXo-nFjevXfedVtpObDZs11zbRb7dEZljdDEjAZW6FB4bZOHSq5rE-zqhXmlgbV-4RNVQHYlXknI1AjT1ZCOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VzGFuslG5pX8Mvq_zgMRK-jzvypMWKoSpg4wEzlM-BvDBmTgk2cwfdi6vgv7kQN4AAJh4O93IPeRpyfq4kEcmkLarKQvJ_ZF3oNKtmw6kS6pXcbOhKblUEoV-9vFT-obv5M0FEOrgHgiEgj-JgvYvxCDsd9ekzIAoiDcclC13oYUQPmrZgdgIVMaxKdJbdQ2L46TpbjrpmKx9wN_nCJbjYo4IEvDGFQcFeyw_AW23r8QuEnROrcp0RVLQ7mS5ltBVRfOUuTtF4lU387k36_x_DwnrujVVNTqUGMFp49FJdKWjqq6ZhdJN4i-sM55DveqdwUlMOcD1GgVNNYTTXzx-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=rGiXb_Hzao_CRwYa_ibpnkTUAjcdy2QehbA9GujSUixzqtwyTxAVm7nWkBnjaks09oLSbUv3vFA6vsuabVu83NEvr6hau1uSSY6CDudtayg-B8xCAhycu70k8E_LZxOl04Ifwql9I1RnBj2YqHvoJdFdEQnbl3KA_CWSp5rPv-Apjum099g4_SJFl0YYkpqaORlHaU9OW2Bem4w0QUog5e7GjPl-azA5lHH4-dOI1xm5XYD9SqT_M-ROz7Z5YqJ0NY7SqoYeTPSGkqnqHH1AZajskypQxFGERVYP3XhHLTZfvyLD89smBw9AJ7pgtabX5Q3mh-Pr6Ze-XIAka8OvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=rGiXb_Hzao_CRwYa_ibpnkTUAjcdy2QehbA9GujSUixzqtwyTxAVm7nWkBnjaks09oLSbUv3vFA6vsuabVu83NEvr6hau1uSSY6CDudtayg-B8xCAhycu70k8E_LZxOl04Ifwql9I1RnBj2YqHvoJdFdEQnbl3KA_CWSp5rPv-Apjum099g4_SJFl0YYkpqaORlHaU9OW2Bem4w0QUog5e7GjPl-azA5lHH4-dOI1xm5XYD9SqT_M-ROz7Z5YqJ0NY7SqoYeTPSGkqnqHH1AZajskypQxFGERVYP3XhHLTZfvyLD89smBw9AJ7pgtabX5Q3mh-Pr6Ze-XIAka8OvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=DTzBCeWj5h7y5z9YLmt4LyMzYvhluFU6yxhZuXbji19qMovZqUEgIFiHNQWG9uUMkeZYImW-H9M-G6Xo-UMFKZY03XJdazgJ6G4LM3u1HcnzTaYTX2nyY2PcK4sy4FRtkA6bRdTwQpbBZeMcpL3JSXVyQoU5UdgJFOSvzoewRbhpSwPQ-LRZlf_mz8i9dZnJOhoXV819x1sOQVPq_A-6xs7arCrlNECqUhHtEvbouvdpC1fyN8qysqwOJ39JZRsy2E4XXmpDsDDzNnMkhDHkJ3svk-M9imZ4Jj_jy_uecFJ39V6eNQaHco_SLJIFL5ZqMZSe9ClmtQ4pWc1OfJzlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=DTzBCeWj5h7y5z9YLmt4LyMzYvhluFU6yxhZuXbji19qMovZqUEgIFiHNQWG9uUMkeZYImW-H9M-G6Xo-UMFKZY03XJdazgJ6G4LM3u1HcnzTaYTX2nyY2PcK4sy4FRtkA6bRdTwQpbBZeMcpL3JSXVyQoU5UdgJFOSvzoewRbhpSwPQ-LRZlf_mz8i9dZnJOhoXV819x1sOQVPq_A-6xs7arCrlNECqUhHtEvbouvdpC1fyN8qysqwOJ39JZRsy2E4XXmpDsDDzNnMkhDHkJ3svk-M9imZ4Jj_jy_uecFJ39V6eNQaHco_SLJIFL5ZqMZSe9ClmtQ4pWc1OfJzlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPocSw__VZ5qPVMqu7WQ_h9so69V0MFwT5X28e6DyoDr0GF4aDMqRMzNLh6NvM-gddtgApHx2N1h5mNepRtnjVkcbCqULhT-KbwTz0ElKb21jWXBN4CWV9YLyrCTKVydd3exP3R8tFKjX3EhQ4RZrnkHlnqLN-0QLCSxjZpjNzMm_HZAZEI-2zoaJO2VU4bocPNSFhFoWYS62APAi4B54R15g1Xj6U_RiKSDw-Q1tedRuvMobcj9o7t-XxB9r3z1qMSBptsLfhXrwyORh6Qs2fDorwbi9IQw9uH3AepxnyQnz6uRLblOCWkdDVT2g8yYKm0H_s4_7JylIDOIU93wEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HQRGuP0y3FHK2TM0dAX-4K1qTSncN0dHO5KAw6-yqT6W9CTDbf5TRkPRJK9uefjgB1mgSLCkXnFNxQh8L8JjvlFVWsR6aYymBM6YwY2oDAFl9TDspW7akqJzsMGTAuqisytWPAOjvvtpudlfA5ixayQRnJYZfKlGQJWFrIsBx_PISC2uEwD5csKMlPPm0uSn02Fa5LfBZemMt7Dv36KRt_4nmn22pLyd1uNAL1wN6NI4Tsm_Yp_XTaZYV6TsLNaVTPMBrzAHuUazmy1JyC_nmztrlhM1kCW3rIaZ0ilMeCjxjMYoL6xjWa7kEifPzXM2mTsCjqz8eS1KYt2-XCryFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/imLFn13gRZvl3m1PCRFeck_-KljOBXuu0QHmnXWNnBbMKKQuMMw8w50CWZY7qhqJcOKNwMM52xfsnhkXQv3_qpw_M-pYErdOXOQew98MKYiPKtov0N5_oR0Q4Z-A39Y-sf1ciJF9pWPavrTlcL6df1q5sT-NnK65umiRuougFsNaR-_lxwZseWhE7SjcW-RS7ptxRnnZ0KfLMeCNj-zi9_i0uzz-DygMCwIhYdCkKb5gbtZB5kjMzdW7SQZApgHKA5BkFqr6tG-hW2SFoSkHcZl9h2fYGy07IITCLh2i_XbajmCTUO9y1G9SOapi_RHKBdQ7Ki5Abm_ZKmSaop_2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKrFbbkUdDaIJsAVZiWqeW5PFvhuV9iBssWhbWYgips7jrVGizVhitG9nGhkDSCzUhLVyryW_nqcRXRHnDCJcMzYe7DepDzeF2DhHOlZ-gjZ4PyydMCtn0oKb5VvKBjXJEKieXnPkDmIt5wpjX3zi7E5Dqej3T3HD8x7Fhk_qt7Hy3rwG7eIagRw7g4kMhwQ0S4lqij5GA6z6Ecyp5wPIBVX0AkwBlNZ4ZQEckmvr1IMQN9OeiKXzmmyQwsOytjU7YM_sPOrdWAEoyFOtttgAjP-cHOODxXTdAKpyfEYnwvuzALvvCePE3zoVOfyTkmtW1OpwzxoUwewr-S_exlY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RtVtyMIPer0VvIj6tAdDHiQ9N-4o5RqAbaCNkmxG0VqfcMmxa2PldGpr6hrUAseeqxzO6PMfoTDsaBy00r-NbGoljpSVEKUm47u2jevvgTffWJYJ3dOIJOhIGhxYJEXffKZYtQ6n35UbKNpkaTEkOZB9vdOGJQWIHtyosTpDShVb0gr5KOn53B5f4roGPfHvhBX-JtPeZ7ReByAzcwHAJpym1L_Wpxv1pIKYu5J0pQbHzk766K0NxacB6ulB7GBPYlIgbXnI3i-OUZW-UqsYQ1mVqmAVSLieDvES5n9_wMQXuqHNPugonHhzzdQMdBOCeLmqThnCFNCN74D15mPWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uOJkP2aAPERQi5oKZgj_mBIylzA2pkOD-tude_ReH7VBXlJPQB-I0D1MHSxzladh_IEriumH99F9OFy1uOmkI9Bx9KExxEbKWRAfVb311uCinmHCvtxOdDENsguu8Q1JjJtU6jJ3jnpUQbCTgLZq935TcUE3T7q9Md1ULr1ae-LEIOKTVqMKCKqPtYF1m8b7vBEGvNGkKjI-EHXANtdBkWnbaKE6vTvbvFYif-2qU2MJvSZOMmh3GqFqOg42JACLmS9JvO9eO_dyKs9qp3Y93JvhJOnMFFE1-60wtDQ8Wz8AuBkVSpGougXkpRAuhKaG7tDO3ljfqf1-wPw3j634nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QJjXsIgZo1Fbe3hGE8_1fIN8atoVNe35qjlB4yaEDlLxeMa-9VMxYgIFGInHi2rAvDVrONj0cPO6SufivH4avxha8q03zWidDmpKp_1-ZI5AoZv--gIiv9JnQjB9-OrXrUR1P7nh0vKhfj9ALJnws2h4WlFt6xA_UTxK7ujWbZBlBZYQt6Rub9W7u7TSLTqQHsjJSq1pYaxdidUI_tMtPYKoaYIVzr21XaiBJ01QJQ_eX_A7Ko1k6ecyn_ZrcmaOp7LP86moDMwJFimtYA5qCGdcMmGvijZmPU8SOchf1RCQEkbY2nYWtLpYKTubR0TG_D2aniup2UTQIVLcjugmGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NCLu_6LTavzeW8KU6rmfDk-NIcl9XiU041PQNekp45ANX1MImyI1mG7_8lTqWx9MJTeRNtWvr3Im2Qi6imVso6GbJkBjihe_rretyH8a8Y1Qtb7tgwLVyBAmfPOkuvuupdGm0xMI8AvFtIOJd3Nqhk0iI-kP_JEkypGHjX5pVGXjAYRkfFFWGMSODLXVokuwKa_d6HAH7BpP8AS6wZJTZ9WCVb9i7iZBJxBH0Vc9CXIl9eVV8duDXb3zybBAwDJuqwHTO20yvActy2-fqnVqvWz3eiKvv5wTSE5sPiE0NFBoL_ZHldWymL2haeNOY1QtOKusNcAjQ6uvbkXomH8lfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=Z6cLTpPLj5QEdmJ_A3cFJ4TP0TZi25ZW9yVbE-1SA-iQZ01Rf68rWS6XwU6gbJfoKljkvig-5lmegxNhYUzU_i5qczXUnjBVfbnsHNyKVxEAIRYw_EmBuiLvDKQkJD_1yIG6uVARaPcBcJxg4ftscwTtkzL6eQ-8qvlWt7Epa9kpDPGIdmYic9bBfH971PTC-W4On2j9GOieWvqVgmbmdv6rI2wxLmLCN8SJbIiSOyTZFdZvEakesuux6a8_7MnwoQ3QLkHOuQAY9Gd61pgsgySS58sgBmLFRe4C99-xi4gtqCePrSYE6ebNn9bkqe9VMlUvY1W3qQAiOWVcCDoClA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=Z6cLTpPLj5QEdmJ_A3cFJ4TP0TZi25ZW9yVbE-1SA-iQZ01Rf68rWS6XwU6gbJfoKljkvig-5lmegxNhYUzU_i5qczXUnjBVfbnsHNyKVxEAIRYw_EmBuiLvDKQkJD_1yIG6uVARaPcBcJxg4ftscwTtkzL6eQ-8qvlWt7Epa9kpDPGIdmYic9bBfH971PTC-W4On2j9GOieWvqVgmbmdv6rI2wxLmLCN8SJbIiSOyTZFdZvEakesuux6a8_7MnwoQ3QLkHOuQAY9Gd61pgsgySS58sgBmLFRe4C99-xi4gtqCePrSYE6ebNn9bkqe9VMlUvY1W3qQAiOWVcCDoClA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vbbs6fXoUTNovGevoQg9DZXylG8GdAvcgFa2oKA69uGDvmSqiZyAgPH8TYlK4h6XvsYkeRrwsk7Kzur3ETX_T69CV-B1V0zawLbaa6KX5MBBjNmFvIz41kRscDI_8mtr2YXl8Zpnq_pq7-Zxa2WVBe_eI-Oo677Y-S1pOpR0CuT3UowSfYkGoxTWJ0NFRm0Gg4TzBVOlk07UXkpWY3-yOKYv-cPTYJE__hcS-9qa1wVFtLKvSlIwUFThQBifztMlpaf4KSKa0Qh_oFQCi8E-FGbGmE0-lA4TWVOfKASD81M9xjTOVaDa3Hnch4US67ycyeltjmoIUNDrlEvVQQQerA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TClx9QU_5GmqHb4zIsvoQyVuO71jkIRosaxGeq1LgqtFzAbQN5R-kU6G5hv4DAmA4O2PjUv0WK5Urc3CZg4W3bwyuts2NIQQIyJ2JtvWG1k6YH8R2VBDZMrnnTuxYGFA04sPVQyUqiNnslRqESaP2Dw5RsWVY3CnJ6SwT8PvtimA3tj3qrifILXaCgSX5kUwEsrqNBdAy07Rr7GiUFb05sCtR9kyCRQXn72utY0MotqgKl5BcyHAd_oKe9eJU7n2SvoKRNxV8cC4ybNM98gAHEOVw2ewkdlxCIAHbRst2qcQ2NOj70LK9WOwwIqX4AJpXf8g_cS9RS0S59UtgW7WhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ufhyhbdge1AzSnX87_0JxgkGnKNRpPOlvXddTX4_upl5hQ-fybmn4SHSQuqYEH1Fxu7sHzu5WdTogkNH3O5iA5eL3lCGeVtoGTmdjqWIBRQ34WrcWCxRdMst4I_MhVzCLT7883tY4aMe2-fEQ-j2-97ATGCy5nqWoC70e8_YU1qVW7t-OKRnnN2jp2g30zTcnWPDRFiTH1bB-aN1s3RDkgnsaFqDQfbX27oDbv0gOesCsYVw7bAYFwAVDMfV-tjcUS_aE_PdarJoV4NqMCaat4HeHgZn7zxBFAFqqUK2n0OGRyFY5I265Sku1mZyQ6hSRiokq0x7ivS-u949cRSoLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=oYFpAq0l2Lt9zYJPkozpxKQkCiJq7rb3l-B7Mr5wg7Y0kQ7gS1jhrY1XbRQJZPGRbevnVGoWvOAJp_H1vPpTtOU59Fw7wQAfSWozHtdzz3ZY3m-e5jvPFTVy6Zd15p9pUNgaui95xCYk857amagt7p9b_Gv6GV83zPxAP13bgLgDF9ZdXvpxgqOfyZwIq5jlo16_nwyuhtmRbtAsk-BehcsIC_pIKxRvK0cH7ESqUyIKku-zytDP41i_1KrJsjkhFCBTjQRSbTqpW7q5iZYUgzSlA-t_gIeyk3kPUo3iPS35jVT5KAsHD8MnwxObQL3gjHyP6WKroiyUvUVIBDfdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=oYFpAq0l2Lt9zYJPkozpxKQkCiJq7rb3l-B7Mr5wg7Y0kQ7gS1jhrY1XbRQJZPGRbevnVGoWvOAJp_H1vPpTtOU59Fw7wQAfSWozHtdzz3ZY3m-e5jvPFTVy6Zd15p9pUNgaui95xCYk857amagt7p9b_Gv6GV83zPxAP13bgLgDF9ZdXvpxgqOfyZwIq5jlo16_nwyuhtmRbtAsk-BehcsIC_pIKxRvK0cH7ESqUyIKku-zytDP41i_1KrJsjkhFCBTjQRSbTqpW7q5iZYUgzSlA-t_gIeyk3kPUo3iPS35jVT5KAsHD8MnwxObQL3gjHyP6WKroiyUvUVIBDfdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7tUNginK_TCIWaKRuyk0KSRacGSlvljRjFWToEScvHxRTL2NeHBHLGjn1BkafSBR2nr9P8b_ZVmbOUq-V7SQe_uTDjoySPtM-ranh2a_oMjhZZ6_Xt8tvQu2KQj7LRl_n2-XHtkeLH-VbE7XV6UNjSTcnmdmzBS7qZjQajT7-cUMsT_K4ooeT5vCFRctblaDm6F2mCOs7JWAFIc4xMKoLWY6DSqyzwR31-jebZ1Z-seNFX766B6N74RwgCuPqC6q9DeKaJcft7c7m9T_ZuUf3NGUWYD9wJOGQk-8nZxIVs5kre5ddo5SHMI6WSLlb879ITHcG7zAKajNMVaafK-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHMq_5gSMrN11uaiWmclMkDxzlIpolYm3LguhSKTDu-zI6iEzj20jo3L4oysFmTHvGTF7bpj6qy4UxHw4GN8UDj3ByiJuT24JQ9CSumol7QkPSWAkXw0oJsoCrgU4G5UnQBo9SbeXT9LKHluBNJjLt-0-YnvnE-NiiffVJEhH4iXKVtEsjr5J2UJWmS-XCdV-gmXJw8xYwtg1iZlRN4xmaL_CBYnwjhk7jsB6CIWbjPtgvtfqUr1lCd7CVec6O1HpmPRwrrdbrlhkB3qHkAOHJ8eRZ1rCpsjQDlq6VeQllHD1doDAT1sErG5YCf9DDho9ftWkdaf5NY4GD8k6xTf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=LrPnbIYv9ww9Ym87aG3ychLeU0yRict0mDqWDc4DrK58Twdu4bAxBcUo1EBCT0f0SxHcVxUOYaFzPoZR_9dMOmXnVVxMDvghAaKGdvtS71ZMPepr9Q7DTiMKNNHvO2eN1grysAaBGVEUynUFRUM6M52TkzaF2mB8hTn2SGqDGtlkWC_n4YrWLIyH2PCTOjmjIOD4Xq9cBPo7j9yhlSuSNyRl8uLk1JW8Unc3dSupvDrlw7y7cyHgVVSVVi62CC_cfYQtzpGFfYh6Z3HG545nTwtLEMcxiShiYseV3BarCzl-oEDG0Cl94LG-yuqTm2nScb6yU0YgXOPOud2X8OZFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=LrPnbIYv9ww9Ym87aG3ychLeU0yRict0mDqWDc4DrK58Twdu4bAxBcUo1EBCT0f0SxHcVxUOYaFzPoZR_9dMOmXnVVxMDvghAaKGdvtS71ZMPepr9Q7DTiMKNNHvO2eN1grysAaBGVEUynUFRUM6M52TkzaF2mB8hTn2SGqDGtlkWC_n4YrWLIyH2PCTOjmjIOD4Xq9cBPo7j9yhlSuSNyRl8uLk1JW8Unc3dSupvDrlw7y7cyHgVVSVVi62CC_cfYQtzpGFfYh6Z3HG545nTwtLEMcxiShiYseV3BarCzl-oEDG0Cl94LG-yuqTm2nScb6yU0YgXOPOud2X8OZFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-bMTXiGQl7Q2RHNVxY3XttRiTLZlcUe8hfbVtuN_y8YCBY-pkt-H-e629_Aep-6JxbNWlSoVUUa8pVJEczjH6QrhEtD8c35sJmyfv5MSJ69TFr-GYLhzc7g4EhMDZe88KEpa_m-I-qESJ-UVA0Vigf_6SYm5SxbXTZf35qI4dASBFygYSZPeJRuEdFOUK8gKfr19WRk74pyWMVPxNit9jJjT_--a2YKY8l5T6O_vqyfgmJYPy0n9PnxtAfBIt-ajwgCRxNI_YAapIek1ZID0gCNV2vNarv_I4OPpiMoy4dA89pU1OjJmb8HHZzUXh6Y5I_adjjo_wxLeCG7pdqEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgdD74dNAcpmypJXleKzkUbh5mGVl9JCSoThGsvHMC6Ptfk3grqwj0mEhS7Yapl1V1dAVMMHbRCEw0paa9ZKgaOJS1sH545Cxiai-a8PiZijaszkZicXwoLV4kIfKAlv-HqLpGXYXFWMAJPLkmNCNyKLcqqZqEZQjuGDUE97TDvGwVQIPRzPMhkXmLWdfF-tSp51gxHK3wSuaKd5yRjZrICnvpj8Tj5RkCPljr9cPo9rMEWAaBbDBk8WuovoI3hn5hjE81X8Gxfue7CpX4VdiH-hmZMr0hqcBMNQCGmggmYwbWieAEz5QQPm3tm3Er5qDvlZz1osq9gvdl7-CnVTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5xoOayuly1aWHbQ05VqgQZEbZ7uY9g3vQpvEVA8_5dU036OBA6-FwRVnPtGKniOUNufphkETsJMWLoSkthxVl0qID5AKsqp33qFlhYtjPNYoXbm7XTFJlK9B_-iSggmKX0l7qHGkIHJPHZR5x4HkrvZYhraF7q7iaVrMdYu3JCXVYLr6an7HfInaD6XrYovWI0-Gb4Ug0q_C7nrS0ElMc6pb-J5q5sNNEf9VDbMbCcuafJIAPlOHtMkPHYgSKMRQg0QKS88lUZIF29cbg31YpWc6dCPThiXwSKefNd3aX66GVlhZUdFGDCr-EjbU72z1o-mg7bz8VSxUArnPZGnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T5o0GABfAjckuy7ix_kARD3ZoGh3Z2Uj3jJdVXR3YuGicOzcVkBtH7a3JxzVgM76H8WlE7ssex9UZo6OyKopOWTvCGDfXnzf_4czSldhEVNZVb8AyKBOdWeBiwqkL0z9Hz66OFMJg_StIpxe1YNTv9_kveNxs2OGR9LIwEIfRnK0y1U4n1FZarmxinlsAPckOii2WFVVS2_eTwrr7NYiej4CCAlDHS_n0WV1yfHZk5hfk00fpvi3QwwRnhgomig8oI1CXV0NcT8KE6gQ5E3tLMYyEZlkSXpgq2Pw45i5p4gedNPHxo51OqTVIGxT_PZU0WS34kImlFKeUFrFoJ_a-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=kyHbV9r2LXZMCWmNkM6zVEsPFKUTZO3MzILN2p6mcLcLc-UOQkegsPtIAKNPnvt33m5YXowMIBoyrBKq4jxUOv8cUbtFPb672_QGuD4Z0jPJcgAlwXm-CLxUuXC2gQ8xUt1EChvYWAFJdFTlfVsFFH1uaLcdhm8oYvPVajnUhCO5n0TqKEX4WCrADBYM-e5LOyGl3Qp0RlZvbC8lXIjG8b2hshgedhTSg8gXk3OfJYNy272sPLXIlbfXa0SeSiQB9V4EbTHfdoeoJhjpiNctsio8KmUxTEx4B5HPVav0fSG-FdowCUq_jghTz8mJ-kep13kf6isoQTdWSOLDL1MWIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=kyHbV9r2LXZMCWmNkM6zVEsPFKUTZO3MzILN2p6mcLcLc-UOQkegsPtIAKNPnvt33m5YXowMIBoyrBKq4jxUOv8cUbtFPb672_QGuD4Z0jPJcgAlwXm-CLxUuXC2gQ8xUt1EChvYWAFJdFTlfVsFFH1uaLcdhm8oYvPVajnUhCO5n0TqKEX4WCrADBYM-e5LOyGl3Qp0RlZvbC8lXIjG8b2hshgedhTSg8gXk3OfJYNy272sPLXIlbfXa0SeSiQB9V4EbTHfdoeoJhjpiNctsio8KmUxTEx4B5HPVav0fSG-FdowCUq_jghTz8mJ-kep13kf6isoQTdWSOLDL1MWIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e19LcStaGmDKrJjuCUWZtaW9bGT1lAH9RSGQjm1wYvBP330Qvo6OwR7y1GEmKEf3SK8cpGZxWwALXwiSNrRDU0pZMI4ObIkP7Wd1j-FcsP1qR3Ejtl3jIdskuu8Vq0SC7aC59QTvC0tXCy65EUMUZVDwIQsL37uACxVkvoBC6_1Ysq7zLDfF1T77tp0Cm92aegGAGJihZ2wl96opIeGGtncI8qEi4QCpo9l8qnXgIuX6q2oyFDjw3kn5gRV9XeDh9fEn5s76t03bycp5O4gaeacrJFxjwUgk7qLRuM3vT9uUGPR-MDJpKHmBCjNQGMN33BmjZEOPH3sTv80wYAH6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQegzgORLA9CJa4vOlwEK0i6eEkn7XZWgHcRkcJ-A5LIscvnEjT6ofKjGq_NCWq8JicKdH7pMg2mXtbKibEcB2oo7lbC0tHBFogVdbty4B5N1W-VQfkcFdh_ZLyLQhQyZABrhYLvAxX-Q4ihDo4t8mJiVC8VY4TdKbmEFPTd23WKeFNdX0LMLoYsbFmc37lSaTkXb-Xewm6bqlvmzSqDS-g4N1suGo21id2-beZDEO5izr5GmSxr7A3oyGOR6J2vmSQAzE0VrBqQo88fnWGacNm3SXeWU4vLhqZrbr67KBzENpNpuBhDowo9cazURze9By6IcWQ7x9DG6CYp68VC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OhK4bd_GV0fFKvkoHv_04MuZpG3J-SwvsRSz6w_SPG5i6HWksay0PM8pep4aEu1U3lsdCBqUQB3skSRzCume8zpqfnMUsZJH-QRV_OON1IDnfqRzBbD5EFYpN6nIglUVRFAOkgw-YdY-iGFQvzbNXxkbCFP0TPwufURRHkcf4Q2coJCjrLmLpcVwxLSOkWsRjwo0LWkGskdrljGPIVzTkhaJN1bE7CPA66LYek9x3CIMptLW6XbKfL8EYXnwD_MAxHWt66vejCVxmZSrLVc1pAx1cLsqzeuCheuz60kPJxli_n25c7vqXJ_AG_1dQpPK7thxTF5kIYOFN1eQX_jZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dYEyboLNAzBOBGJo-RHIhxM7Y4U5OYOJOSaZ13ieVDRWbQLgUQjvIS7RiOwoENwjBhyQnN18Bxsf8BaiqiIS26IeUSX-a24is2KTE_nL8-zhvDQUjVpnANcjOmo2Ik05E8gKbhcNXAxwrzKvMyXCz79tFZlEIw9iHQtW5GRYLsu_LT-xJ6AIHaBOFyDRNiArxVsNoTeoHkLvDjPAgRMkg3aFumFLPVJuOaEfylcJLNp1PW5RCd1sfOoEnp7bwSFvaQeuBeRkq_RxwN5iBO6u3EGUunvUPWIZcTDyvv1RphxLvJu4wuO73_I8A_1KTQVzzEJbPz1Yx37H8vD2CMzBSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gdlg2z8_rO7ibHIIrXyMjIan3O8qJ1LVRyWamIqXq883cMDgwMM-Z6SIe-JcgxmlWUUVY4m3RJeEvj1mnVLIYLo9Ws7ommslDyTwPi6unnhhBo84OhbAA2uILXJzyEobskdnJJN337Lru0AzBbNBL2aJe3Sen7XibXykCBIXX4fkmQR_qPBnQx3GdqUKDQ0GsNnWQrCgyolQxiIe5ipp975bPRAAS9DSVh0BmR5DPANwM_zUV3Ser9BoVdSVOnfqkcj0r_xvCGtSIfLsz323KrIesGEJeyV2uM2N0AfM42qOZF1CUK8ZHIJEQFN8V3_L1T2fcYKJ9pm8KQt84JkCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ3CpYifUIT3gKUQiU1Nh2WeOaM7Z0KRtfWRLErdsXRfPunygH-OR7lpe5GHs2xurOVd8orlzF_LYx_a0PNHrLzy6VK58th8WhFbEguNqROcLsStHnrPQ_mSN63OaXIV4oeT_kB_V0aFJs8oCoXPN36F4XEmu8F74QSL7Rya0rvRq3hWhwgGPkP37th1aFHDv44-qTaymokV1Z63zW8H6_oyEynNFMVzrewAmUCc5trysVcS46-TJ8M-L7tEgNmc-hOgY4Sjc5sTkAA6H_Ph5B6FLWEkv7UaL6RWOBVX-7WQmX5qSxwbCgGdm2sjIxkzJbuXgrIOK_p1Kda0xEvPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNpQGH5G3bc3qCVgy_mkGJxmQYMy1TgQuHCZQ1j0zwrICcn0fVyOjXyy5qgTgyfdSXHx0FWhR_NlWRtLdwXE1bN1X8hFUSWR9CpgtAHdrb8vJljliczL3dGGIE2B2EIQuXJX3Q8n-0zjFdASQ5vJ6AyrUtTI7axRy69Suf8OaJ6PKUerSF7ZWoVR55qHNP6zPnS6KZb0Ey1yhagw_Bby62s-SwbdEhQ3PBT4MZlFkColIHyQVJ89tAwkPb7sqm1ksu3ghGuIOgza7uM3rQxRV78BoNH6pr2NVf72N7EiS4W3vsEQJecIlz3LHMzHsFW0b9J6om7q0UIJAzUsJkVtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری از رسانه‌های حکومتی یکشنبه ۱۸ مرداد از انتصاب محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به‌عنوان نماینده او در شورای عالی امنیت ملی خبر دادند، اما دقایقی بعد این خبر را حذف کردند.
خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از «شنیده‌ها» نوشت که با این انتصاب، محسن رضایی و سعید جلیلی دو نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی خواهند بود. تسنیم پس از چند دقیقه این مطلب را از کانال تلگرامی خود حذف کرد.
رسانه‌های مهر، ایسنا و جماران نیز خبر انتصاب رضایی را منتشر کردند و اندکی بعد مطالب خود را برداشتند.
انتشار و حذف این خبر در شرایطی صورت گرفت که در روزهای اخیر اختلاف‌ها در ساختار جمهوری اسلامی بر سر روند گفت‌وگوها با آمریکا، از جمله پرونده هسته‌ای و چشم‌انداز تنگه هرمز، افزایش یافته است.
@
VahidOOnLine
🔄
آپدیت: خبر شش ساعت بعد از حذف دوباره
منتشر شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=J4K3uRKz4J1d4RvHQzW7U7JF_98-hyWRMMAhCATecNtzC7DdyqcReBo7wC1bUPwuBsEbeNX9a4q2o3EQiAFuSjiCUY5d4Tv-TwlYwYI4MMJYgiNBCq8IkQ56V_O6pHN4VdEAH9-UT1BlTAbSO80Ce6xuWr5S4uZGY8vPnAgslzSw9getjMxM0MdpTtC9mjw6WLH7FAn1nATjDdhi9qKdpOvvzbBIgCY5hb_CdT6NuncGFHMTD2EIXmQsrojP6HU9opM4LoxLZA-hwWX1UzbH26bKiNseJBAVY09cvS9ChcXlJ8NMN1iwdWH-ciBxw_ujuW4_EM523kH7EHisdLwLIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=J4K3uRKz4J1d4RvHQzW7U7JF_98-hyWRMMAhCATecNtzC7DdyqcReBo7wC1bUPwuBsEbeNX9a4q2o3EQiAFuSjiCUY5d4Tv-TwlYwYI4MMJYgiNBCq8IkQ56V_O6pHN4VdEAH9-UT1BlTAbSO80Ce6xuWr5S4uZGY8vPnAgslzSw9getjMxM0MdpTtC9mjw6WLH7FAn1nATjDdhi9qKdpOvvzbBIgCY5hb_CdT6NuncGFHMTD2EIXmQsrojP6HU9opM4LoxLZA-hwWX1UzbH26bKiNseJBAVY09cvS9ChcXlJ8NMN1iwdWH-ciBxw_ujuW4_EM523kH7EHisdLwLIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mjoJh_8o44I5QX48APwVRrfl2qr0EtKWsaR-yrNF6bkz1JVDeKjnZllPA8D7F0MVeaDQCfVaqND78jNQLtbFL78aKNUbI8_M-ctRGZvKMV6rsQnZmEBZGHAt37X_HrapBxXE3nOWwzgkzhqbt9hDxTmsczMJvvcqJRhhx8dvszYCj7bbhhyMGZkFLB7avH1EenFol3Qb2Cfm9oO1Gn1r5lhPb5gETEVVD6dkPXgFxdQXkTSzuGpGXaPIscJa9TsbaRzpJmg0kr4Zs5dJxRhvBdQKEb5zPAAoOt5SL-PFIl-9tx6_r5s98Q6fpd9Dg9byvZxrTZdcsTg7IbjhvaAqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان امروز منابع حکومتی درباره قتل مداحی که ۶ ماه به بهانه "دعوت به حجاب" مزاحم یک "دختر بلاگر" شده بود تا رفت سر قرار باهاش:
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴ روز پیش ویدیویی از پیکر آسیب دیدهٔ این فرد در یک کانال ضدانقلاب منتشر و در فضای مجازی دست به دست شد.
مرد گمشده مدتی قبل در فضای مجازی با خانم بلاگر جوانی آشنا شده و به او امر به معروف و نهی از منکر می‌کرده و می خواست حجابش را در پیج اینستاگرامی حفظ کند و به مسائل سیاسی نپردازد که در روز ناپدید شدن نیز این خانم بلاگر از او درخواست ملاقات حضوری داشته است.
تحقیقات کارآگاهان نشان می‌دهد زن جوان با طراحی قبلی و با دعوت از مرد سرشناس به محله خلوتی زمینه حضور وی را فراهم کرده و پس از رسیدن مداح جوان به محل قرار با تعارف خوردنی مسموم ابتدا مقتول را بی هوش کرده سپس با همدستی 5 مرد او را به قتل رسانده اند.
خانم بلاگر در بازجویی ها گفت : من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و... من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند.
...
تحقیقات همچنین نشان داد این افراد پس از قتل، اقدام به فیلمبرداری از صحنه جنایت و جنایت بر میت کرده و فیلم تهیه‌شده را در ازای دریافت پول برای  شبکه‌ معاند منافقین ارسال کرده‌اند چون تصور می کردند برای این فیلم ها که در آن بسیجی ای کشته می شد پول خوبی می توانند دریافت کنند.
بررسی‌های کارآگاهان در این مرحله نشان داد مقتول با ضربات متعدد چاقو به قتل رسیده و پس از مرگ، با آتش زدن جسد جنایت بر میت رخ داده است. متهمان همچنین درباره نحوه انتقال و سوزاندن جسد در بیابان‌های اطراف پرند توضیحاتی را در اختیار تیم تحقیق قرار داده‌اند.
براساس ادعای افراد بازداشتی، یکی از متهمان که به عنوان عامل اصلی جنایت معرفی شده، ضربات اصلی را به مقتول وارد کرده و پس از آن سایر افراد نیز در این جنایت مشارکت داشته‌اند؛ با این حال، متهم اصلی پرونده پس از ارتکاب قتل متواری شده و تلاش‌های پلیس برای دستگیری او ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfW1Nh4KBNmNsn_MZUueDaqSb2okIRegC0A9Yjc9l3IKztHadt8eW9UaCdDlZ5RJg3LWbpV1zjOaRdIIpILV263m252QLArYxvhAQlXze9oLV9oez2KhI6MYz5t8s-RCk_cSvUOPcb0ntL0omaiLzx2KUXp1_KGdqM8g95TOHIQ1iQheGXKV2C6IF2bkLgyUDqPe6DL23vtp_Sq1PCaaPAYPYvVQ76bl3RL2t0Pk7HOtIX6sPnyr7fH22B8wu1cLQ7CCMZY3BSXKD9Dg9jMmVCPRVQZpzEDKPu5ItgZEyQs4hhlNvbCZQChX7f3rRqTIhu8VAFT_JnZI-yAzl4E3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات حکومت ایران در عین اعلام پیشرفت در مذاکرات ایران و عمان درباره تعیین مسیر کشتی‌ها در تنگه هرمز روز شنبه، ۱۷ مردادماه، شرط‌های تازه و گسترده‌ای را برای باز شدن این آبراه مطرح کردند.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه گفت تا زمانی که آمریکا به گفتۀ او «رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد» و تأکید کرد این شورا «چه در جنگ و چه در مذاکره» از این موضع کوتاه نخواهد آمد.
او شش شرط را برای بازگشایی تنگه مطرح کرد که از جمله شامل پایان جنگ و حملات آمریکا به ایران و متحدان جمهوری اسلامی در لبنان، فلسطین، یمن و عراق، رفع محاصره دریایی، خروج نیروهای نظامی آمریکا از پیرامون ایران، پرداخت کامل خسارت‌های جنگ، لغو تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران است. ذوالقدر همچنین خواستار پایان تهدیدهای آمریکا علیه ایران شد.
ساعاتی پیش از آن نیز سخنگوی سپاه پاسداران اعلام کرده بود که بازگشایی تنگه هرمز اساساً «ارتباطی به مذاکرات ایران و عمان ندارد» و تنها در صورتی انجام خواهد شد که آمریکا «شرایط ایران» را به‌طور کامل بپذیرد.
@
VahidHeadline
شرایط شورای امنیت ملی ایران با یادداشت تفاهم با آمریکا چه تفاوتی دارد؟
انتشار شش شرط ایران برای بازگشایی تنگه هرمز، چشم‌انداز بازگشایی این تنگه در کوتاه‌مدت را در ابهام بیشتری فرو برد.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، گفت که این شورا چه در جنگ و چه در مذاکره «هرگز کوتاه نخواهد آمد.»
شورای عالی امنیت ملی ایران زبان صریح‌تری در مقایسه با تفاهمنامه با آمریکا به کار بسته است.
در یک مقایسه سریع با یادداشت تفاهم، ایران این بار به شکلی صریح خواستار پرداخت «بی‌کم و کاست خسارت‌های دو جنگ» شده است، موضوعی که در نص یادداشت تفاهم‌ دیده نمی‌شد.
پذیرش آمریکا تقریبا ناممکن است چرا که آن کشور را در موضع «متجاوز» قرار می‌دهد و به زبان سیاسی هم به «شکست» تعبیر می‌شود. در عین حال، پرداخت غرامت، تبعات حقوقی دیگری هم به‌عنوان آغازگر جنگ و همچنین اقدامات غیرقانونی بین‌المللی دارد.
این در حالی است که دونالد ترامپ گفته بود که خسارات حملات ایران را از پول‌های بلوکه شده ایران می‌گیرد. این موضع آمریکا عملا نفی ششمین شرط ایران برای آزادسازی تمامی‌ دارایی‌هایی‌هایش است.
شرط دوم ایران هم اگرچه به بند نخست یادداشت تفاهم می‌ماند، با یک تفاوت بنیادین. در تفاهمنامه دو کشور تنها از پایان دائمی تخاصم در ایران و لبنان نام برده شده بود. این بار اما جمهوری اسلامی خواستار پایان دائمی جنگ در «فلسطین، یمن و عراق» هم شده است.
به نظر می‌رسد شش شرط ایران نه موضوع مذاکره که موضع این کشور است.
پیش از این، اگرچه مقام‌های ایران اعلام کرده بودند که توافق با عمان به معنای بازگشایی تنگه هرمز نیست اما رئیس‌جمهور و مقام‌های وزارت خارجه تا حدی این موضوع را به بازگشت آمریکا به تفاهمنامه و تعهد عدم نقض آن مشروط کرده بودند.
حالا به نظر می‌رسد شورای عالی امنیت ملی مطالبات را افزایش داده است، اقدامی که حتی اگر با هدف فشار بر آمریکا و امتیازگیری در مذاکرات باشد، مخاطرات خود را دارد و مشخص نیست که واکنش آمریکا چه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBTve4xXnhs0RaMtm8wwInINSeNb2XLre6GSgmq3kDsH3MX73vv1Wged6OUjiDhkPvsciNODtyGPGsOjmx-eZ1g-qSUnL0wM5uXpi8qZNvgZi9_57dYhHu2UZgGG86AJvV8VXtQoJAZ8LMwhoUxMuKssKNOkuiWVwvl584Ccp8-y16uzWtoZGVk1idQqjNp0WbdpIMnTIqoz-7la113MgULYgN5vGY9O_SNMOU0p5YHvHblK6HOlZ52dOhHSiWTEcMsWEztaVAXs7ApZjwvCCAHLE88m6GQ_gZQOMbFH8AGN2R3d6TinO8UiZZJLlXXqH45uy9PAh3NQqv8bByWwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=TcygaaRBXimK2sN9ZeM4589FGwWxxaFnJl9g5J5fwlCYcKrA2VWgGATiaIOHzmY54PjcetZF-mQfJNxThu2R09DcQ6bD9EMg7ev0MSsRY-qhLM7J0nWLwyxbd00G6ocp7u6AAfWIaB9CKUXPRZfwW8tFnIBsK61fWdhUlZTy74eh9Z76eFNhDl0j-cxVL4IeE_xhiFZ3MCrOYg5PUd03DihJy01sToqNjW8LQ-ITM3cmZnQQO5pMRuIbSlqbKy3TH_wYPWHgXitq_MkQ4r2-Cd-ps1F0s_TNTxdgGQn4FDgn-v8FsX_0Uso2xxfcTOWzpHiClq-8mB4Tc4zRBtvwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=TcygaaRBXimK2sN9ZeM4589FGwWxxaFnJl9g5J5fwlCYcKrA2VWgGATiaIOHzmY54PjcetZF-mQfJNxThu2R09DcQ6bD9EMg7ev0MSsRY-qhLM7J0nWLwyxbd00G6ocp7u6AAfWIaB9CKUXPRZfwW8tFnIBsK61fWdhUlZTy74eh9Z76eFNhDl0j-cxVL4IeE_xhiFZ3MCrOYg5PUd03DihJy01sToqNjW8LQ-ITM3cmZnQQO5pMRuIbSlqbKy3TH_wYPWHgXitq_MkQ4r2-Cd-ps1F0s_TNTxdgGQn4FDgn-v8FsX_0Uso2xxfcTOWzpHiClq-8mB4Tc4zRBtvwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMRsNX-P4iVLNA51WBYNbcon3dvJZUTq1HqynMvO507O_Ke_iVT5dAHKN03VfpSoicVp7vXMxk2we-94PJuxy-XZKXgwph186h_GYlxlYBAmx9a8owg2wrB3_a1UOnnowLv3CLDCY8yPeHg3PqwiULDpn2ZJcggHgALTjFn11JZHvusklvTROUXFymRqwIpq0Ius9L__17_qje5d6sHt1DdGzN4idQwCHqs5-6pUh8w2a7wTLLSpJoM3yx_J7rzZ4gS1Vu_hIisX2aZOEumiGI8bG9Iptixmj63MnzUK-jZLZef_AZlK-zBQMMI6bqtvRMBjm6I6zvpjUSlaLhCvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8sBJbPIuJEDuhQvVi9QIaXXxf_4nnezTteWkveOZjiGVwYRxj6r_GG49nQnOER2gLJphdt8w7pr-jo9Q3kAy_E0nLAZNi1xQ5c9nkil4GVif9_jKn2fmBtRLbCECLMEUmLcf2GgLOUcJfP1xgmYn2EVC7OnTloXyzZI-iUPJhdU0YCu5eE5CYQ7xoTTiXjQPF17EJh4fWmiCOtNbqMC3aVdZHB6h2HMHskkT749cBVEWd0WbPnAeGHZxr66XyhHdd9ZRMVJ-kDVBt-ItXVOKGdzzHMuelll60ijopiYyetIWaSCD0LbL85ssRIoLgS6iul5DCdMJbhUOv5JQ62NVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldZWmEkg1W67optK5CZ5C1Gw3r0SwV8w-zlG_xOgqtJ_HD4Rp3svaYm0CVlsJBXp8zBtdf9w5lUMkcvsBpNyD1Cj-8dd61beEN2sDXRH98fhgUdMmwigUPDXY1GcVWmxkE-HEWidOwfooGZ9wKUw_IZMAKBjrH7dIWGppuGd0Blve3UDilD8L4BEWP2z8KErmMkJBo87s5ASG62p_bsHlXamHSArZaUF3kcMLP9ANYcoeIz4sfErMc-w1HF1IJu3Ox7bDE9unICeocYbKWtTjFPaUWaj7EDgxXWlB9bKqyIH9Rwj9POctEBOkJp1FVawmOqKNlo2zvHQ--fZiv0MFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spg4nsBU4XMCbaTEalVrrbWIgfJm-ZzzKwioQh3Ra4WxAjL0ak6yilj6rkCx0_piOat2xYaWjqGQtGRr3EGmv-2uk220YfM03jHK1iNBAh63qcma6gUKXIPrIwcksXS6sXa2b1sd4SnUj79EtdrXyKrx5DEhI-3Nt6UXKfi1eHAYwXiQj9MBqx8iq44veNoWdzgJSvuESDYBO_zpF8l3aGBtTZgJWIcDpbgReYBbzstapzwhLOlYECCzO0f31UFi0ChdWdW4gpiFVzFQgSxs3D56ECOCw4Gk_i_MB0W5pJX5uxr8kPgAtE3DMWSJ-m80EcgA8BNAK6g7K4KCvfzM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vHxF4OJcddy2ubJ8tWdMIirXfJQaAPbPOWq0q7VzrhrJ3P1mjnUYFzcTx-RYv7fmea6h7-YfYlY24MwL5D66liWF7DCIovkXwRQV1g_rYAKca_ZLCrAhGgf8EqalDZQEH0SM94Fn4LNXhkpPTAsSh-HAaSrmWL5BKBDmOQaLaitmfdcXVKlhXjZ8v2-1nVSBVHsLbzPqKINEUbwEuitxa4hpFHz_XjPm-uhVUlOEQnH0kKDgsvXEEY5ySOf_c6S0fTUwLfslzCeD-RCyddPAivLdWzOcneRD28QPv3ojmachtVRvlStqvC8eiO-kZL1aFHKn2bb8HosAQ7Mc2ZopLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrSU_buobuXISXpXMg6kptIRGyLfywCXqgCDvYtxtabjO_8stju75Q38In33EhE-5nhG1spTTV1A7dPnNXuWlIYnGkbH4fGEHA7asaZBmg4hCN8At6aBaIZsAEKR0hi8uatT9XTS1pArSmDJbN71AgwI6O90iPP4kS8sGxFSCdP327V4c3ITyHq-z-MJEY8E2FHB_TwelhJ5almqIj2jMKcaSdPLsXorE4aCnbIFtRphyV74xiMLAp1hyEtTxRDRDyPdLeltyQCWjj5H7xHhBmKe3PVU-eNyi93zM3yXkFlDaTCyZnDe2HDvzEvMitMcudonRfPZy00qHt8CUQW46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tep61ClHlYsxVROKmEI2M7J8HAzTbzPsgj-T-ZDz2Nx93SNgpHU9Rv4xjqEZUJjxu0MayqW-T2aIModng1DEK5pK4Xttq2KFh3Y4JYHz4F1ZUfN_Pd_Iq_FJhc54lgjzfEPs88hwUo8FSDu9ko3-6wFwgs-td6MT4ZK4xUea6QebsXCQZYtkUBNs8VXcR2PiBwZI-EA61zR9CRtlIvq35-6RxpMuKoNaZ0lqzfsoByTNpC8pBqUKQ7Qw7Mh-nuzLlDEv56FhSG4BpnonZ-QzH9cfdXfWKS47n_f3Coga1JQX2DXo2bFNIPv4eaGEj5l_g6ZNBhM1KmPsKvUj4avqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvJBOBmJM_Ibt_ziyDI_D3Lg3eU0kWKmMni1550Qi17WcYFHwKAlv7_bp28B5YRELnJ9HXlxCTV8AoEobpjOOh9gW_OksYQoyJBQ2lsWo0BofsRpBaeUUVFWp1YmS_cmXoi2qdI0lua7HhNZ3q6k-UnsgtqGzD1a48K4EMiazDkAEUsIczEqp9LiyVdCXCRklxv0CECh08z26eCA9fJQbgeijg1cTtXTtRiWNBUJTTbsTd27nwzd8god9fuDfz0nXOnMxjLh_rZBNOonUjBYAJ54Q11jMmxVekXA3Ydx6eRsZ29M6evlZq6LCqbeuEYojewg-XOJ2BUL0wEnyQXNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYnHKa__Q3LOjjRLTL_WOW-4U_DCvDDQIYovSEOlH5BJkY6DAemC9SXZ7araL9d-v0xxVomHQeIa33Cact0oztEndl7yk158u3tDx60ZnfxJjaA91RY8KsrPzy_K6QDzzcok-pKea959m-sQH5VYNfi86xkzsw1gqXbUeh_YmmQVrchbN821Aur-tCWfiVm7-9q-NdriOH6Rk9aTNWhIDWJCEI0j9hhigqVHp6wZfawUpVlTG0NvuhShq_0scyXdx3UTaa7mh5HJnMnKOKlq-ieIMzqn3A1rhg8kZijF51vdKyMGi1PzjtUAqkj4eQsEJ5qaYo13jNgsnZZLRvs6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1IEBXfWjRniKPMipqb6jGUwZMnnQbzgkXPyyGSmyZMkrwkuTJErxaEDRxPXTzpCTBHa3EgcCo18SjLSjyJlr0lb3rhuLyb8bmT32txBi0coqDX82nmz4jmKA0AY6VCGSwZHfuN2yXq6YRlGV5v7stR6tKpi3ToNAjgDakTOqA3Blk19X6SRB2Wgmi4_vjjNebrGhCIBJXqxGgdbrcRrd78BMkEr6UYR0taVYCQBi704Jlc0AXrlztmktQueBE9krXYxFvG-A6luPIT6BxEbBNl3rLuXAJTFIf_OGFX74NuV1pOFSVCYVDsvF7tJCIHe3QUmiZOzQTIZJ-FcZeE9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-PsaS6vPqR77qSwMqZLJjP2I3znQPF0b2dMc9Xexvt0yGXy1g2GAzog8kUCSCZTSlDYJS3q4z3CrjuFamJfwVnuOVWF_1lNPz5NffetzuzlzNrlAtcP8ANK9m9O2g2NPYVxncKEUjBu5ENLlZgPp5MTo0qc3JK5VljC8rnBtzRvGkMB9wn-iLAVR3wX-bAZK0zWDI7EKeBp9dAdUXCfXF-Eg6bXic-1XVRLy5c8BzdE0xjWQc_eB-W_JsE7_4yywP66JIdl1Tn8sHwd5DhFR3GNmhbQ5ZDo5LFa0VlN0doyIrgfPWbhaGkc9G2Z1wrf4cQB3NBSWj-zjxg4NMzR5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyT62LpG9wVTPhJBc8RdW3UiZ8uN-94EP8uI7cm-qJL4MIoUnUJ6i56CXffdWJYFhZ15hItdirDQov8iccZn6UB1h8WIoDzSq7SaTsINNwpA4Gttehw1jRpajsWKSW6YB40UTRmnS1iFEa8aOV5drkq4ydi-v6s0_uSAdcnI0jciTM4uerDaEVSk2oSADNOIwOc5S56R6xSXXv7BNn5MLPwUTCm74FW2TE9-NTwNx6obNmh_xeSONwvf-fpkV7JPXQpAMAjHQNaBZITGoXU6ga86JeDBl9bND8AVja8eC5dNqlhqTlBWG1UrU_pZA4dRBVTX3vKtBVrlSvFxnXzlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pa6n3f9kHp68txPJUNlBvfalxBVBIkZZEVCC_oSEjdBpqq6uRjD_If3daXRovTWlff9dlnBnpxnshq56tIEyMC-QAlATsXaLvcJQWZ47XV8ndnudsKb6eXGmI6-amdgcUNbNtUcoctBHIYOEZOpaEnt2VXLJQVabtfSOvNcA_a7qEfUQR5vVp6SFdl2GESXiUi_O3-JCRa65w2NRWcVvo3IqqohzlppMO9sz9TtjCDHu0j3KkLPjcJZeI_6uMzg-n5JFCB3QlRQ6ee6B9urU1fyWhlsxn-_8nr5IWyKJar7V1fv-TTuXJA5NlTWaDBlw2YoNF8u0xJJdtX3sLS_tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=NkuvWSl5_GjLQhktNkqo0qopIZlxZS_Mta3jPK_C1UDWDPQbj77gl-ZjuWl2r6Vu_9tGykmO0FH5zsI5YrNBXaFTqmF0oOEJtw-IoQy_-rzbbqbRoS06gJgPL7n_T_LaWFyCrDK4a5L2gy3Sp7jm--TSJX4A9YYNewH7-m0Ay_uyxkUP07gU8fxaXmjbok97o9CQbfboy30ova7xxUTncTM14V_5Tef-AfYtqa9aAtW0pu2IfS0T8a0bLnedvBnUfuhIq3lGbo1tYBdyn-pSB_tCsQEoeCvi5Gb057Ns3W6UV8tqmLal2HuPxazMcxUzM9FFAnRX9Gw_TN-K1kIj5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=NkuvWSl5_GjLQhktNkqo0qopIZlxZS_Mta3jPK_C1UDWDPQbj77gl-ZjuWl2r6Vu_9tGykmO0FH5zsI5YrNBXaFTqmF0oOEJtw-IoQy_-rzbbqbRoS06gJgPL7n_T_LaWFyCrDK4a5L2gy3Sp7jm--TSJX4A9YYNewH7-m0Ay_uyxkUP07gU8fxaXmjbok97o9CQbfboy30ova7xxUTncTM14V_5Tef-AfYtqa9aAtW0pu2IfS0T8a0bLnedvBnUfuhIq3lGbo1tYBdyn-pSB_tCsQEoeCvi5Gb057Ns3W6UV8tqmLal2HuPxazMcxUzM9FFAnRX9Gw_TN-K1kIj5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E0yxfrU5ytbFnAP2tTSemQINZ9coqQyxCf69T6p6drS6lCwniFhNnFAPQVAZdUX62WYCdiZv9GAgbZ4Ki8I2PA8GTvONnusrNRV6w2GzFO1lPTof6DfSh8YsARL0ZEKZkZPRs7Qa3VeO1CBI_aOQAXUQSTsfFG3ExR5CVrewHBMQp4asIDm1A1JKzGZTj3-Pax-tnab41euxO1hY_Z3e0VRJAn5tujZGMF5CtV_yOzdR0aU_sHSEMBm3mIN8nCiKEVIbJd2Aqpn0s2vZbwsi-klwUdQaoJhglVoKcPHR9tVmnaKAxJLnft_WRcODiB8BQjJYV9Eu6Y6hl08PQrWAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 493K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejRc1jihFjY-4RnRSvdsQA04LMdD2XkVCxAloq1N_VltU9651XhcNwnJoF7v4qxBBR7_JObqOmM8-bqURsFl90RpPcTUJt5YK-7fui5neOOqOLqaBzRIq0djn0ks9FVrpSNcd1EqVwLZPjs_qxPKDLUJ8QgGIchy223LJOXzktmZqbZpggrU7z38PvolXOn45MkQ1MkRVIBdP3zJUUyzF0j_EMIZRxmYwyfY7VJirYs_F3ROEQIoYRIWTEkCsSK-snsqEiY87y_3LJbaPJQJNquqHO__TR_0iV2vjY2SAJjlkZKvlDT2MeaYcMWDrZG6nKvpQ1O1xTK0xGH7OSMtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
همین الان دو صدای بد انفجار شنیده شد قشم
سلام ساعت ۲۱ و ۴۳
قشم دو انفجار نزدیک شهر
سلام وحید جان الان قشم صدای دو انفجار بد اومد
صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن
وحید قشم رو زدنننننننن [لطفا صداها رو تفسیر نکنید]
۴ تا انفجاررررر
قشم هم اکننون سه انفجار
ساعت ۲۱:۴۱ قشم
دوتا انفجار یکیش خیلی قوی تر بود، اسکله بهمن بود یا کشتی‌های نزدیک اسکله
بندرعباس ۲۱:۴۳ دو سه تا صدای انفجار [که لابد همون قشم بوده.]
همین الان صدای ۴ تا انفجار اومد قشم
دوتاش خیلی شدیدو نزدیک بود
دوتاش خیلی دور بود
سلام وحید جان ساعت ۹ و ۴۲ دقیقه قشم دوبار صدای انفجار اومد ،نمی‌دونم چی بود ،خونه لرزید
ساعت ۲۱:۴۰ صدای ۲ انفجار شدید شهر قشم درب و پنجره ها لرزید
سلام وحید جان صدا سه تا انفجار تو قشم اومد دوتا شدید بود یکی انگاری دور بود
🔄
منابع حکومتی:
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UY1O8qwIcoGpIU5sgoLYCoNZP-o7GXsOtlSODJq_pXsXw8BgJ-CWabBSY6dRqLOtnOTx1OFR6S2JKFLLTV4-hoZuXLJ2Lva-R_N9Pol7V5DqNbcnR5JCm_Zu865D2XOcsyrYOOT1IfzOaI2Sz2ruhuXRre3wiXTVp1Xa6mRdleFJcfrbnytxwrlk0vypN9VbL43znof4XJr2bwwek4wim1_3AM1HU_bH_Bk6pkhNLjjXpZ1H6g-r8e3OQkYJib59A7f2LqY4ZSxsKiBgvNsMRlJEjUSLX2GlFvDzEuPa_ELGFjF5c7kc4EzApV0CCz6pQVduKSmg1jKYmiOLQtDuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hdjeAlFFJs7pnP5W2Ubr4acXCyz9rz-mmNYjzRR67mzmjVB_5uxwZBRhkCkQrt_Z8RZPkJ_vdhBeEpgp3QfaIwS3B3QCl2CkElwRAqDB_EAAqqN7yUP3NclJXvbOAEvIO-a_3iSFIFCmBhZpVzM8YW3oHYy1modKhc-Yx8s8ubaxGl13l2U1bpQ1qW_d0tMRpeIcl8wKTlH8MtmNS3rI0kiOMW0ceaxvHSojywYq75_wgIxXyWNtQURVqZExzexCH9FpNNmVUypP0DKAaYVWr0yPZ4-F5PRyMB74RLKp9boMsVeuZRzGO8F0U1NKaHywukmYAgMGWyelfUsSJG7C0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
ایالات متحده مقادیر عظیمی «مهمات»، به‌ویژه از برخی انواع خاص، در اختیار دارد.
افزون بر این، هر مقدار که نیاز باشد، حجم زیادی مهمات تولید و به ایالات متحده ارسال می‌شود.
شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات تولیدی در تاریخ کشور ما هستند.
کسانی که این اظهارات خیانت‌بار را درز داده‌اند، تحت تعقیب قرار دارند.
برای آن‌ها درخواست محکومیت‌های طولانی‌مدت زندان خواهد شد!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PCFNNrJXRO_DUcA2xjRhMfUvhn4wgBQYY10iIG6VIGODv_AVyTGqf77Clgo2aZrh02VcrPWwFKzKc57QJfQBd3kA4TeAlm-Dil8zJ5qz1tw3lyZUT-VmJUjQJoggjOc_cCie3iw4vkPASmXPGluvcF9Z3GJxVvcZHg0v7S14Ezbf1kkpwphXSx7IwoDd3lSeeXP5tL813TvlkJeV7si0zW0nZ8V-MYPIfzsKRSrnjiv61vWYnWdwRcAElK9IW7UbZp_wcoN1G8Rmggf261kTGKEl_2qiQrVaVd4G2hzZhi-aztYhI7O8pBZcTkdaHzAkiu8yS50vt0KQnnnyygpu9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن پست
:
درگیری ترامپ و هگست در کمپ دیوید بر سر نگرانی‌ها از کاهش ذخایر موشکی در جنگ ایران
ترجمه ماشین:
در نشست این آخر هفته در کمپ دیوید، رئیس‌جمهور ترامپ از پیت هگست، وزیر دفاع، درباره کمبود شدید مهمات توضیح خواست.
به گفته دو فرد آگاه از این گفت‌وگو به روزنامه واشنگتن‌پست، سرخوردگی دونالد ترامپ، رئیس‌جمهور آمریکا، از جنگ ایران هفته گذشته در کمپ دیوید فوران کرد؛ جایی که او از پیت هگست، وزیر دفاع، خواست توضیح دهد چرا ظاهراً درباره کمبود شدید مهمات ــ که اکنون گزینه‌های نظامی در برابر ایران را محدود می‌کند ــ گمراه شده است.
این رویارویی روز جمعه و در حاشیه نشست کابینه ترامپ در کمپ دیوید رخ داد. به گفته هر دو فرد آگاه از گفت‌وگو، ترامپ با عصبانیت به هگست گفت تصور می‌کرده مشکل مهمات «حل شده است». این افراد نیز مانند دیگران، به‌دلیل ترس از تلافی‌جویی، به شرط ناشناس‌ماندن صحبت کردند.
به گفته یکی از منابع، کمبودها، به‌ویژه در زمینه موشک‌های هدایت‌شونده دوربرد و موشک‌های رهگیر پدافند هوایی، از دلایلی بوده است که ترامپ در روزهای اخیر از اجرای حملات گسترده‌تر علیه ایران عقب‌نشینی کرده است.
کارولین لیویت، سخنگوی کاخ سفید، در پاسخ به پرسش‌های واشنگتن‌پست گفت: «این خبر صددرصد جعلی است. واقعاً هرگز چنین اتفاقی نیفتاده است. رئیس‌جمهور ترامپ نیز نهایت اعتماد را به وزیر هگست دارد.»
متن کامل فارسی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 487K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=D5uc7wwGm5s3CrIM8omovCOFtGzmQDYw0vdEjbERFvgKiKltL8GsXt7xCCCV15Ez_oUFhNvefCVTs9TydnUOlfnrc50RPZzOHNvXpNLy-4lsVokAhgtWhg21wyAiXi2b8apu_yRIDZ6CAb5eKck1b-OKWHIhGM7Hgm20Wa-5nZ0X0fwO9DcGA5fPk_BvbL2qYdPl-DC8J9hvnVl-8K-U_E-ZIUkzrE48QgyQtvi8SnTx93qra-YK6M9W5vv-yN5NuHtv3eJpkkMUSQPT-2Ej0mEBOX76dwtRsgX2m_9QjoNXFmJ2uk6u-7nVUikAQScQ9CFRvv66Sl4EI3HOVDHZ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=D5uc7wwGm5s3CrIM8omovCOFtGzmQDYw0vdEjbERFvgKiKltL8GsXt7xCCCV15Ez_oUFhNvefCVTs9TydnUOlfnrc50RPZzOHNvXpNLy-4lsVokAhgtWhg21wyAiXi2b8apu_yRIDZ6CAb5eKck1b-OKWHIhGM7Hgm20Wa-5nZ0X0fwO9DcGA5fPk_BvbL2qYdPl-DC8J9hvnVl-8K-U_E-ZIUkzrE48QgyQtvi8SnTx93qra-YK6M9W5vv-yN5NuHtv3eJpkkMUSQPT-2Ej0mEBOX76dwtRsgX2m_9QjoNXFmJ2uk6u-7nVUikAQScQ9CFRvv66Sl4EI3HOVDHZ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESqRNfx8uImSaEi5lG0n4FXtMH8XIGUt46K-bWS9BZ8NB0QznJXLsFOcYR7Z3u7IneBE9H7UKyYT67F_hZMOVHihBnzvMeI0gBVwd6QJHf6wuFmnU8thAB2uO3HX1A0p6GSsCtxSeQHdha7MIOn6TwQtw_iUb-4_H2emNDM1Dgv3mLbS4P9_I_KRPAS69Y3tMtasH3G_c9y2DzAoJdALWngMiTG-FzzRNbcSc3-RH78T5DahSbM9HhKlOXVLNkJAWGoGxZCoCL_O2dCGROcPstVUo3q2IgvW9Xis4hCMpn9AHe4N6KbGG1dtTksoSBfV14Hb0e32amgXqOCQC8uDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2Fzw5xYBbwHR8vt6pyM9hF8He07HsJb4sWWt9YKnh_2tNwaKxYO6IKwpQF4OULwaBlx_Pp4eSW6yBzKQgZxlKMy9jh5VFRynOxbXOIm4LZNXmFzsh2xZIkKscOF1Px8NpD9PMEYx8KFt7oi88JeF-u9QLMwJZopsnszXc5w9Omj5cT5OuH9Slukr5XewKl7Oh_BDG_srJ0skobu3dARKhSW_MbZ4SS6Spnvab1NSqYBi-J-h2aSqUBVdD36JP3wafzd6WsquZLdSczTwyIIN31XWq26aWx8TkdQoJv8mMJix0cv67EkrYKYefG4g7fru9dck-RWSJ-A-gM6iGpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=UN8WzcmCZz7QkIH3kL1O4aZZe2mx1oSqzjtcFzyDJ_VbGripa0XvgWvh36u93bL9r3b5uMrgm6Boe8dTk_Ii7qBDCVO5vQ1apFoF9eQw2yzZcWdXv1VG4UOWwUQOUoBJB1EF241ZiyGYhzZbIHhMGX-U7xSqhkfa05Dzcb1XpNJI4ecVHo1PuJTaC9CpORdYqkKpwvNS_wfisPiXEev9UmAi3DFjgkEuFj6j_MSrGouffCEQ28IcWSF0lF47O8PpXftNygUYiQqfzOknusYT6InzJfRJPchy3uidZHH1i-VcLCR_PMbS2geBaThtygIp8beCd7-Nc5CX3vMNqd2wRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=UN8WzcmCZz7QkIH3kL1O4aZZe2mx1oSqzjtcFzyDJ_VbGripa0XvgWvh36u93bL9r3b5uMrgm6Boe8dTk_Ii7qBDCVO5vQ1apFoF9eQw2yzZcWdXv1VG4UOWwUQOUoBJB1EF241ZiyGYhzZbIHhMGX-U7xSqhkfa05Dzcb1XpNJI4ecVHo1PuJTaC9CpORdYqkKpwvNS_wfisPiXEev9UmAi3DFjgkEuFj6j_MSrGouffCEQ28IcWSF0lF47O8PpXftNygUYiQqfzOknusYT6InzJfRJPchy3uidZHH1i-VcLCR_PMbS2geBaThtygIp8beCd7-Nc5CX3vMNqd2wRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXhZvmzvVsnQZr0zp9ODPKAYYWBunaN1Lhe9XWA1QDeQ-uROKnrJZjUySWwf2VHIQV4y9tpEFQosAX36E9lHo-kqm2WeI2aJiyNoHUE1Xh0Bl_g81uCLcxPasYPbrC4NOKnNFw_CHinpx08OqIGyD3GZTVSmFjdYhchS-qtVWhOTKqq6tLRRvNlJnPdUwWM5hMaGtMmQxqNLXNnoWnbrAwoCAAFfBNkYGiLER5rJd-b6Hyt5-fqAcE-e6xwH0nTB1zmX71iW8Lcw9sY9Icwdp-WFAXRhGR7akZfaOijcGvwussCmvSQSxvcBUfZObXuCE4VrZW19w42pCKP9BzwaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NROqpvabcw6NipczvNRcottsUZmYud09IJIxPY-Egvx6SAF7RK5kAwrmjq_lstjdyfBbX8jNr1XW4urPnfHedEiATHJ4AiRYkbgUNs7wYgujIb5L_LkBwArCkP_EAYlonDWvSzqprKSnJMXSipldGfrMZG6w1DIjBkN0PSd6aLDEEYebOuO75uFJuOpzMu-fiytbjy5Bd7qDvKT4rJzghcwYbut1ILg9cHdC8hETtfYl_SDfzuzp9Y85MkJRbRRJRNtziswnuPdSkaN9R9EU8zcaBkvise18Uq0SySmHa66w5ANYtcuoFDaOXJLQMSURjbxgvWvICNW0VgzQxwBeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9Q5k1muycWb-VaTuCpzE5dgBlEMzf3ao1pi_j5Ck68vfzJyomTKiJPGIQqxEIbH61cDYekT-RhZvxzjBzQev99136OpV6ICgmMz570O9kYEHS3l2pDeetkgwzAYBhT26uMdet5a5dqvaTsaZzWawJUlVyWdguzF0H5Y9yCxKZZVqmZ3MoB4-E8SgIWlKdl065uQ9ajILLQ_OdKcUrowbTxdlNOgh7_MhhckAL2dL3l_NcQc1e-m9nzfRGe2go98IXn5XkM3mga8Sz0nze7bIUtSGI2H1i4qphw4XqLvAaY3PljAfa7r8zHkaSkjEyXRIa1sbwjBFOs-06X4GVdCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcvn98pZ0g-QLrVr1Iab-ZwJO73HHLVl7my7raoOrg6D-GumqKrhfr_C_i55dkUwKO8QPPnyv-k9egPC3XNQ5Q2yf-tQCn42tGWN4h2ENOij9F3V8yPkTMzDmN1xfJPR4yXfQcRX4AwoDgeA_C6UiPuSfstd2oq6MOtf3LEwd6brUViGUKe0OPtndm3ec6N_Wflfvy0J8-fxCREEu3bnJgPKfThI58xcvpwhlfM70zjlR_iQLpY9fnGaTgTGPxRjuJfVhaFJbWpc0YhMuVfolfy7IlcCahnP9M7NneKxCq0ulsy8Q0NYUyW26je0PQzyErrxY20XstN5afXvN1SIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=nk-nyutoqeVqvXB9RQ3bUTXpPbNgzRoGDACHJXskBWsMXohuOIwfZYm0_qxA67wBzH1cgOjXW2R7tqMkkasNNiACkyzBC84xODZw_t6ZRAuqhOUVlLAioH5d4ROISiv2QPwNgC-UmdxP9actKF0_OP8dlhrHHLiU-ul5AJGecxNY-OooRR4cls6mQ9L6F5K3SpJ-thz0L2e3nYRv3QCdtfDd3elWBoeeUE9JGtmEjkD3m7O1SE7n1y-fZh2HZevimFsgoC92irAV8om8ofQwJeKYSrNy-Ky2kRl6hqrfNpU-WrXlVf_iUwzmWTa118xPlxZr6z7-ynrXSzEjMtRwIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=nk-nyutoqeVqvXB9RQ3bUTXpPbNgzRoGDACHJXskBWsMXohuOIwfZYm0_qxA67wBzH1cgOjXW2R7tqMkkasNNiACkyzBC84xODZw_t6ZRAuqhOUVlLAioH5d4ROISiv2QPwNgC-UmdxP9actKF0_OP8dlhrHHLiU-ul5AJGecxNY-OooRR4cls6mQ9L6F5K3SpJ-thz0L2e3nYRv3QCdtfDd3elWBoeeUE9JGtmEjkD3m7O1SE7n1y-fZh2HZevimFsgoC92irAV8om8ofQwJeKYSrNy-Ky2kRl6hqrfNpU-WrXlVf_iUwzmWTa118xPlxZr6z7-ynrXSzEjMtRwIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
▪️
تنگه هرمز به‌زودی باز خواهد شد
▪️
مذاکرات با ایران به‌خوبی پیش می‌رود، اما تهران تمایلی به تایید آن ندارد
▪️
اگر بار دیگر عقب بکشند، ضربه سختی خواهند خورد
ترامپ:
اگر به اقتصاد نگاه کنید، اگر به اتفاقاتی که در حال رخ‌دادن است نگاه کنید... برای نمونه، ایران هرگز سلاح هسته‌ای نخواهد داشت. همین حالا هم دیگر نمی‌تواند داشته باشد، اما قرار است این موضوع رسمی شود.
تنگه [هرمز] خیلی زود باز خواهد شد؛ وگرنه ضربه بسیار سختی خواهند خورد و پس از آن، تنگه باز خواهد شد.
ما آماده انجام حمله‌ای عظیم بودیم؛ بزرگ‌ترین حمله از زمان جنگ جهانی دوم. بعد آنها با من تماس گرفتند و بسیار مؤدبانه گفتند: «لطفاً، می‌توانیم صحبت کنیم؟ می‌توانیم گفت‌وگو کنیم؟» آنها نمی‌خواستند... [جمله ناتمام است].
من هم گفتم: «بله، می‌توانیم صحبت کنیم. بیایید بالاخره این کار را تمام کنیم. بیایید انجامش دهیم.»
این کاری است که رؤسای‌جمهور دیگر باید طی ۵۰ سال گذشته انجام می‌دادند. می‌دانید، مدام عدد ۴۷ سال را می‌شنوید، اما سه سال است که همین عدد گفته می‌شود؛ حالا دیگر بیش از ۵۰ سال شده است.
رؤسای‌جمهور دیگر یا کشورهای دیگر باید می‌توانستند این کار را انجام دهند.
من کاری را انجام دادم که مجبور بودم انجام دهم؛ چون اگر آنها سلاح هسته‌ای داشتند، تمام این جهان جای متفاوتی می‌شد.
خبرنگار فاکس‌نیوز:
اگر دوباره عقب‌نشینی کنند و زیر توافق بزنند، کارشان تمام است؟
ترامپ:
اگر دوباره زیر توافق بزنند، ضربه واقعاً سختی خواهند خورد. خودشان این را می‌دانند و درک می‌کنند. من انتخاب دیگری ندارم. آنها نمی‌توانند سلاح هسته‌ای داشته باشند. موضوع بسیار ساده است.
این‌طور نیست که بگوییم: «خب، بیایید درباره چیز دیگری فکر کنیم.» نه؛ رؤسای‌جمهور بسیاری باید طی سال‌های طولانی این کار را انجام می‌دادند، اما انجام ندادند. حالا من دارم انجامش می‌دهم.
اوباما را کاملاً سرکیسه کردند. او فکر می‌کرد می‌تواند با پرداخت پول خودش را از این وضعیت خلاص کند. میلیاردها، ده‌ها میلیارد دلار به آنها داد؛ آن‌هم به‌شکلی بسیار احمقانه.
۱٫۷ میلیارد دلار پول نقد، اسکناس‌های سبز، در یک هواپیمای بوئینگ ۷۵۷؛ هواپیمایی پر از پول نقد. احتمالاً وقتی آن را دیدند، گفتند: «حتماً شوخی می‌کنید!»
نه، نمی‌توانید با پول‌دادن خودتان را از چنین وضعیتی خلاص کنید؛ تنها راه این است که با جنگیدن راه خروجتان را باز کنید.
اگر ما این کارها را انجام نداده بودیم، آنها مذاکره نمی‌کردند. ما ضربه بسیار بسیار سختی به آنها زدیم. اما ضربه سخت‌تر هنوز در راه است و امیدوارم مجبور نشویم از آن استفاده کنیم. امیدوارم مجبور نشویم.
گفت‌وگوهای بسیار خوبی داریم. آنها دوست ندارند به این موضوع اعتراف کنند، اما این کمی آزاردهنده است. به افرادی مثل شما می‌گوییم که گفت‌وگوهای فوق‌العاده‌ای داریم، بعد یک نفر از ایران می‌آید و می‌گوید: «ما دیدار نکرده‌ایم، ما...» [جمله در زیرنویس ناتمام است].
تمام روز چنین دروغ‌هایی می‌گویند. متوجه هستید؟ باورنکردنی است. می‌گویند: «ما این کار را نکردیم.» می‌گویند درباره موضوع هسته‌ای صحبت نکرده‌ایم.
خب، پس درباره چه چیزی صحبت می‌کنیم؟ آنجا نشسته‌ایم و بی‌کار انگشت‌هایمان را به هم می‌زنیم؟
اما اهمیتی ندارد. اینها فقط حرف است. تنها چیزی که اهمیت دارد، عمل است. آنها می‌خواهند توافق کنند. خواهیم دید چه اتفاقی می‌افتد. اگر توافق نکنند، برایشان خیلی بد خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f1EOBVZx7DGIJ_Xr1x5g3XHqpZSPQo1g_32xCiRX45MkXZVCoVNS9cLwBxYsLekIjQDFslrwlNPQbhYNZ5kxb2nInV_1S8vtE5MmicUlc8bT8gOlJaQQnQp5PX56DwJt6tuuaQ9VxsIpPUa_hGi5VoUtV7wWtmoqVRMvyiKtnc8qXzwib6Z5gj3gutTc_1nZKCdOtEGASIO0LmWwpNCEmrNjzFdW07vLz7ANbcgHILLKNN93c4ncsUAqd6v6m9MdQFkyUeBsTruzAV7SunMkdObO9jTsALvQPK0e_BpIl1foIomvP2Cnf_DYU4naLsDtS3wfdZZyKG7uL4wG8YnURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"آمریکا به توافق درباره هرمز نزدیک شده و به‌دنبال اعلام آن در روز چهارشنبه است"
اکسیوس، ترجمه ماشین:
به گفته دو منبع منطقه‌ای و یک مقام آمریکایی، آمریکا، ایران و عمان به دستیابی به یک توافق موقت برای بازگشایی تنگه هرمز نزدیک شده‌اند و آمریکا قصد دارد این توافق روز چهارشنبه اعلام شود.
🔻
چرا اهمیت دارد:
هدف از این توافق که چند هفته است درباره آن مذاکره می‌شود، ازسرگیری آتش‌بس میان آمریکا و ایران و آغاز دوباره مذاکرات بر سر یک توافق هسته‌ای است.
▪️
رئیس‌جمهوری ترامپ روز شنبه تصمیم گرفت تهدیدهای خود برای آغاز یک کارزار بمباران گسترده را عملی نکند تا فرصت بیشتری برای دیپلماسی فراهم شود. با این حال، اگر به‌زودی توافقی حاصل نشود، ترامپ ممکن است با حملات بزرگ موافقت کند.
▪️
توافق در حال شکل‌گیری برخی از خواسته‌های ایران برای کنترل بیشتر بر رفت‌وآمد در تنگه هرمز را تأمین خواهد کرد؛ کنترلی که ایران پیش از جنگ در اختیار نداشت.
🔻
اصل خبر:
به گفته دو منبع منطقه‌ای، توافق مورد بحث یک سازوکار موقت ۶۰روزه میان عمان و ایران در تنگه هرمز ایجاد می‌کند که امکان تمدید آن نیز وجود دارد.
▪️
همه کشتی‌هایی که از طریق تنگه وارد خلیج فارس می‌شوند، از یک مسیر شمالی در آب‌های ایران عبور خواهند کرد.
▪️
همه کشتی‌هایی که از تنگه خارج می‌شوند و به دریای عرب می‌روند، با هماهنگی ایران از یک مسیر جنوبی در آب‌های عمان عبور خواهند کرد.
▪️
در دوره ۶۰روزه هیچ‌گونه عوارض یا هزینه‌ای دریافت نخواهد شد.
▪️
طرف‌ها تلاش خواهند کرد ظرف ۳۰ روز مین‌های دریایی را از مسیر میانی تنگه پاک‌سازی کنند.
▪️
پس از پاک‌سازی مسیر میانی، این مسیر بر اساس مفاد یک سازوکار دائمی که قرار است میان عمان و ایران درباره آن مذاکره شود، برای رفت‌وآمد کشتی‌ها در هر دو جهت مورد استفاده قرار خواهد گرفت.
🔻
بله، اما:
کاخ سفید، عمان و میانجی‌های منطقه‌ای سه هفته پیش تصور می‌کردند با ایران به توافق رسیده‌اند، اما ایران حملات به کشتی‌ها را از سر گرفت. این موضوع به دو هفته درگیری و وضعیتی نزدیک به جنگی تمام‌عیار منجر شد.
🔻
پشت‌پرده:
به گفته منابع منطقه‌ای، علاوه بر مذاکرات میان عمان و ایران، مقام‌هایی از قطر، پاکستان و عربستان سعودی نیز در تلاش‌های میانجی‌گرانه مشارکت داشتند.
▪️
منابع منطقه‌ای گفتند کاخ سفید به‌طور فعال در مذاکرات حضور داشت. در روزهای اخیر چندین تماس میان استیو ویتکاف، فرستاده ترامپ، عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، انجام شد.
▪️
دو منبع منطقه‌ای گفتند عراقچی در پایان هفته گذشته در اصل با توافق موافقت کرد، اما همچنان به تأیید مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، و شورای عالی امنیت ملی نیاز داشت.
▪️
یک مقام آمریکایی و یک منبع منطقه‌ای گفتند رهبری ایران روز سه‌شنبه روند تأیید توافق را تکمیل کرد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQFsAjjZ-RPZ_bY8cvdHlFKKtmmJIauEWCLxi_DnnhPf4QAFcCjh7Gz9GJOEOCWA1AUvbl4qarGSUboHMvLxuNXzeiL53vMHvnc7zC24mEMJheH4HHCUbFIGzT7Q9a_iHc7wDmE6P52P0yOgNQEwJzO3UrQTrP8OMmX2cqIWONUratbTnApeHCUuh9VF6ktT2eFOsHcHd64XdeH1whBaMKFabluCdmORHwTOwekI7FcujS4zrO7UijHVsd0jLlXyzhbUNV0nh2PrezFLc5Tclp2QuKP1M0_yQjCxAnm7ICBre-Cle9e7VdGI35EKbsZBEbZWql2DVDdceh1h_V2djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=AhTHWi1kKp0USDiWOKR8UrjqSMvav_lQa0Qhh4BSwH88fMtwr7ammQ1ctoEpPwxHMos_-Pc2MnhpdVZsenXfCDdlE6x-nmKguG3G43sSKd29xkfuqyG2xsvc9YCfiJ6o_zuh38AxD1lErMx8bPvKfkYVq_oEY82GvS2Otw0N-XSYBkIST5WAzyAjVssPIZyJQTMJ0gfMvRmPKPdRGCl8Kw09q2vc_dagO4cUAEtWKfua_7Z1nSjungt2MIiSEfCLfhAURzXH0fp3F6AzYNMasPo0-nEupcbQlpmiHdNS40NNvQqj0BIR9Cy0iuWdANvhi1Z7SHvtVyC1ZMmYArGP0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=AhTHWi1kKp0USDiWOKR8UrjqSMvav_lQa0Qhh4BSwH88fMtwr7ammQ1ctoEpPwxHMos_-Pc2MnhpdVZsenXfCDdlE6x-nmKguG3G43sSKd29xkfuqyG2xsvc9YCfiJ6o_zuh38AxD1lErMx8bPvKfkYVq_oEY82GvS2Otw0N-XSYBkIST5WAzyAjVssPIZyJQTMJ0gfMvRmPKPdRGCl8Kw09q2vc_dagO4cUAEtWKfua_7Z1nSjungt2MIiSEfCLfhAURzXH0fp3F6AzYNMasPo0-nEupcbQlpmiHdNS40NNvQqj0BIR9Cy0iuWdANvhi1Z7SHvtVyC1ZMmYArGP0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=QAvGrrtN2RkDBe-77scYXLHOcUl33WvoSFrmlzUCPPifSMiyEUY0cKdLxqZ61vzi4sjgy_MGZEDYuynndPoAPo8BypuOUysNAKCa1i-1XBdJwwH3W_dsXMJga3VMA7w3-5Z0Qzn_owPNltX8jNzJkajnTSUDVi96HDCt9nHe8UJARzpIWqCmYE4r80QhGLPjgz5awULXjV6zX1CP_lbIBSLFnpwZclXcei2DzQD2u65ez0IxIatx2ZOsaqmLjBuf30YbYSi5G6hgPnxhvjA-7fewCEq0ys6dS_Fqxuz_v54ibAWFkD6r74DeWEoc8N89WQVvE_oiGkLuac6qAKYVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=QAvGrrtN2RkDBe-77scYXLHOcUl33WvoSFrmlzUCPPifSMiyEUY0cKdLxqZ61vzi4sjgy_MGZEDYuynndPoAPo8BypuOUysNAKCa1i-1XBdJwwH3W_dsXMJga3VMA7w3-5Z0Qzn_owPNltX8jNzJkajnTSUDVi96HDCt9nHe8UJARzpIWqCmYE4r80QhGLPjgz5awULXjV6zX1CP_lbIBSLFnpwZclXcei2DzQD2u65ez0IxIatx2ZOsaqmLjBuf30YbYSi5G6hgPnxhvjA-7fewCEq0ys6dS_Fqxuz_v54ibAWFkD6r74DeWEoc8N89WQVvE_oiGkLuac6qAKYVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmOMA29RpBTyAOGqkNWhRGDOtHE1IbayiBaBKQEjGUb-dDH9SBO9qBSFhgeEJRHiCCtnfPVgFs7siWbM9d9758NvzOFVpEzoVwWGihKuooxTOpEBfpbV--h86CSX7vlbpW8XlwLKXAP5k1-dQqlCRdGuWe4LbshyoFYwaIM8QTzwynbqnjq1OVcHq73d0rQOIYZV9lTDzhvSWmiwi0aYXkI3iMkGCFIZ5HqJYHavgTcEqGqRmwmtXTILVdLAYVkqUlqXgf2nVZ44mdSr9c1Vd7cUg2yrfXetqcSDfNJlg-U1IE4rNfVCEccvrnIaRizu2qfgOBYfyHNa9FRQ8w65Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCvIuBdhJ2jAr5SLWLrfJGS2WGMeW6yMIXx5h8eBpnTvLHoyR-QlnTMljXCiNMYQI4UYAHFgtel-eMRveAOC8KnVksUM8FI_ZN8V7Oz2lkrGRVJdeRaiRnIzYquHlJdktZOtnOZT0rmGwS5wNQyIutsEjIqot389Y4VDPgaYCcLcR19OyqoTureITQA5ZWzWkKE9LEqgAckBsI7iP6yMIgtM7I1IsQaxMZDNM--qRdrts0uJKNsvNGkaquTVDqHUlTf0azm2xIfgB-nRQfFpNTibCLar46Ro0TZa8x_IYSx6_oGU82xpspBaikrajdprSEXOz387JCEMnlM7g9apEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/khxwB1dHvsh0C0-pQoRxdploUkVwbTN9CH2AlN-2ulFPku4VKNcdimBxtAZGxjBj6qnJPRZshpXXTXp_NERgHEb95WnLA6ECjuoevnPmRZWmus7jVecoDjs9KY8xW822MtpnRsXJ6dk24rP6Kufz9C8N9TyYO6YbcpDkVlREAyrGzGxm3IeCD2dcVyKiP9hhFOrCyzFPAzzqB3Yc_6HfpB1IKdKxnJ3LSGr6e216hrfmhHd7puDRxS5xoyy5QJ1ADCHZwyQw6RRUk-uvl6y2IIAqX1okDyxYDTcAK51B5QdVkOI_VSeJl6Qu700VQN4T288mK_JwQpWM_ix4rCjMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qNmTeQ6Y7bOgEU7Ht73d0JNSqB9iJbk4l9K5vzo48w24ypl9Toio5lAoVgfYoVsAF8yXpA7WC7KJcJxbPpyNRTuA7YN7Kad8Gyn31SCUO3RSFGCGr9paIuGVO_S3ET7xm5mnAzkrjY3S8BdnP5AUEmV2GYuL-29Wv23eD47Z47qQSdsafLjryHGtMbjqBR0x6Nv1HsGlkj2wdm173QmKVEy9is4cH1GRg7-z41NHHokqX9DJl0yNvI7ErZe0pJKWHSMDgBfQ6a8WUcrACHd0Wvm7eWZI_6Rcnl0w-eszmpVLHrkIc7l1_LI22azHlxOFHxDr3YSbbkAWEkNH3SADnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EM3OvWfvgslcFzmTPaLOVyXaEJIwBGzGbgC8sH5dnF3VBIB1-TOuMx6JQi2zfW6rjb5l_UGAkT6NNxs5b8xDKwx_UA2xzFepADxBjqRZUrr7ixgYdTiKgaA2vmUv0iGS3AWjO6PVu7KiN-22ivvi1wfWPCEYNbzKPwJqHGW6AkOfunNZsa7JfE4jyevjiggnimZv_dpNg46Rl5Nlk1HWXBhQjpY_Nl3oXWQM2tgHK-IKo3VL-Hd2OdH9z3yT-8NswCPmpTIDO_jDIrVvc2hAab5HefFXuwyc8UXlC_dyvnDs-xhhPhOt8D9n0E7riCpF7C-frrS7KvPHkqD7pCammA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F-wphlna5Ql1RviQt-jCdUPNNaSOXSRgsVHljl74C3Hg_m219x5S4EHWuittmm_dAHzZZ2ickT0PYkPqHTjzAo6pl7TD8G6xJlR3sOUT-ydpkXmMAOAMSULyhVrDhsJt6y7B17ViUTvYhudXI-lecC304l8xpp3nwmtF6U_rCc1Y_xTex4pCVaitLWe2WCqDtwFYNR6oBfJsUjE6DZZLKOj1lZ_LLfzGuIaXTM8rYWknc0fiWQ1K1uF0qhBwJI07GtLSaVVihBDHm1-bO_JBmf7_RUGnUvIiYduCDNqHQv65f-KoJA34nLg_lMULq8dcJe71ozPTul20SQPTeChDXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=WHwdS2u2_Iuzkz613RxMkWnlemWb42U0kR48KE6sM5ZBvI8NA-91KI7cRK_ZVrtMwA7ZrHOQZ6kHi4AJaqOlP35qbsPZCOBcqqNzywuDqm5jVatRqxA1_b_YxgPZQOZaJSkhATGAzTLFIOidTjDg224QbmlQW_KASKF00t1ahyenoCYnWVzA-KM0IzYO27ExIX9noKG_P5Mi3pQzz4yTWtJqD6mkbomQK5C4Qu7OSsQffoSHG53QBVC49L06NPLotyYB4iLti6QzQgXbzV83MtrZDwTsVWAPL-INRoE4Qt3HoKF9SiS3iKwqsKfPXAnynSkPtdIyGZGjhF9EVe-PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=WHwdS2u2_Iuzkz613RxMkWnlemWb42U0kR48KE6sM5ZBvI8NA-91KI7cRK_ZVrtMwA7ZrHOQZ6kHi4AJaqOlP35qbsPZCOBcqqNzywuDqm5jVatRqxA1_b_YxgPZQOZaJSkhATGAzTLFIOidTjDg224QbmlQW_KASKF00t1ahyenoCYnWVzA-KM0IzYO27ExIX9noKG_P5Mi3pQzz4yTWtJqD6mkbomQK5C4Qu7OSsQffoSHG53QBVC49L06NPLotyYB4iLti6QzQgXbzV83MtrZDwTsVWAPL-INRoE4Qt3HoKF9SiS3iKwqsKfPXAnynSkPtdIyGZGjhF9EVe-PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت ایالات متحده ممکن است تا روز چهارشنبه برای بازگشایی تنگه هرمز با ایران به توافق برسد؛ توافقی که به گفته او می‌تواند قیمت انرژی را تثبیت کند.
او روز سه‌شنبه در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «ما با ایرانی‌ها در حال مذاکره هستیم و فکر می‌کنم این احتمال وجود دارد که امروز یا فردا برای بازگشایی تنگه و حرکت به سوی وضعیتی عادی‌تر در این درگیری به توافق برسیم.»
بسنت در پاسخ به این پرسش که آیا چنین توافقی به ایران اجازه خواهد داد از کشتی‌های عبوری عوارض دریافت کند، گفت: «فکر می‌کنم منظور، آزادی رفت‌وآمد خواهد بود.»
@
VahidHeadline
مارکو روبیو، وزیر امور خارجه آمریکا، روز سه‌شنبه ۱۳ مردادماه اعلام کرد هدف نهایی مذاکرات با ایران، دستیابی به توافقی برای خلع سلاح هسته‌ای این کشور است و گفت توافق کنونی که تمرکز اصلی بر آن قرار دارد، به تضمین عبور امن کشتی‌ها از تنگه مربوط می‌شود.
روبیو با اشاره به ادامه تردد کشتی‌ها و انتقال نفت از تنگه گفت: «همین حالا کشتی‌ها از تنگه عبور می‌کنند و صادرات نفت ادامه دارد. تنگه باز است.»
او افزود: «خلع سلاح هسته‌ای ایران توافق نهایی است. توافق فوری، که اکنون بیشترین تمرکز بر آن قرار دارد، مربوط به تنگه است.»
روبیو همچنین گفت مذاکراتی میان عمان و ایران درباره فراهم کردن امکان عبور امن کشتی‌های بیشتر از تنگه در کوتاه‌مدت در جریان است که آمریکا نیز در آن دخیل است. به گفته او، این مذاکرات پیشرفت کرده، اما هنوز به نتیجه نهایی نرسیده و واشنگتن امیدوار است به‌زودی به جمع‌بندی برسد.
@
VahidOOnLine
قطر اعلام کرد تلاش‌ها برای دستیابی به راه‌حلی دیپلماتیک میان ایران و ایالات متحده ادامه دارد، اما هنوز توافقی حاصل نشده و هیچ مذاکره مستقیمی میان دو طرف برنامه‌ریزی نشده است.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، روز سه‌شنبه ۱۳ مرداد ۱۴۰۵ به خبرنگاران گفت رایزنی‌های دوحه با ایران و آمریکا همچنان ادامه دارد. به گفته او، این رایزنی‌ها بر دستیابی به «راه‌حلی کوتاه‌مدت» متمرکز است تا زمینه ازسرگیری گفت‌وگوها و احیای کامل روند میانجی‌گری فراهم شود.
اظهارات سخنگوی وزارت خارجه قطر یک روز پس از آن مطرح شد که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود مذاکرات با تهران در جریان است و ایران با «آخرین فرصت» برای دستیابی به توافق روبه‌روست.
ترامپ گفته بود این مذاکرات به درخواست ایران، عربستان سعودی، امارات متحده عربی و قطر انجام می‌شود و افزوده بود: «این آخرین فرصت آن‌ها برای امضای یک توافق خوب است.»
در مقابل، مقام‌های جمهوری اسلامی تأکید کرده‌اند که هیچ مذاکره‌ای با آمریکا در جریان نیست و گفت‌وگوهای کنونی ایران تنها با عمان و درباره تنگه هرمز انجام می‌شود. تهران همچنین اعلام کرده است که این هفته هیچ نشست مهمی برنامه‌ریزی نشده است.
@
VahidHeadline
قیمت نفت روز سه‌شنبه ۱۳ مرداد پس از اظهارات مقامات قطر و وزیر خزانه‌داری آمریکا که امیدها را برای حل دیپلماتیک مناقشه خاورمیانه و بهبود عبور نفتکش‌ها از تنگه هرمز افزایش داد، حدود ۴ درصد کاهش یافت و به پایین‌ترین سطح خود در سه هفته اخیر رسید.
@
VahidOOnLine
—-
ترامپ هم دوباره چندین پست پشت هم منتشر کرد که یکیش لینکی است مربوط به مطلب ۲ روز پیش
breitbart
با تیتر:
ترامپ: «توافق قریب‌الوقوع است»؛ مذاکرات با ایران درباره خلع سلاح هسته‌ای و هرمز دوشنبه از سر گرفته می‌شود
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ROKSUbUbUItSjhGSPhTbfwPZk9rgXXk78UEfjLbEA6R2CqW7sNOrBP6LKQDlIFp2CWbNPgSMxqK5NOKS45PC2qGrovI45u0_zrD_l5MvIG2t2CzvxNyZYE-3JDkzbtwJ5OeYpIcpLLYh5KwCHL4tsstNtzGKCTzrsZIXaHkVXzIYEUMG2kUaKtP_6ryvFsckJStLvsTFFH3wRdA-nvKMGvpN7yd8wNxExUmyxzlr7umR0o0dJ2mpfiU2t33MDq_92Vr8c11NyNrLSL6VoYHcTk27ah5fJ89r7NrvUDK9M_590wdbmEruLlERfLybXcdlK0DsOSbXQV_SU0maFTzafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=ovGS92w1c0UHlYZy2ftQNGSJt1ftw2F3Pjd3-jvum4e_44uVwbWaTky6dP_wtzQNa20WL2vPSGWvtV36mKwatnfAsNOmI7820VTiR39KVPAvp8-pbcVcQtYKKMzSjQa4jB4Vi7kMmOCWZLpJRjQPQsMRwQmJT-AD0qVyJvUDL9IJ55Mqf5t0luLMqwcrHVfhmTcvuuQWhL1Lu1uBKT5z6NNExyc-eoKAhKahvVN5WbpFvmUFcIPQ3ocEiyE29Qe7qb71ez_g5iewV91a23T6QZoOVTQghT2m7LqFsXMXcgaLw5wVaVMORy--t5CyTPeXS8avCwV2f1u-ksz_SnF23g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=ovGS92w1c0UHlYZy2ftQNGSJt1ftw2F3Pjd3-jvum4e_44uVwbWaTky6dP_wtzQNa20WL2vPSGWvtV36mKwatnfAsNOmI7820VTiR39KVPAvp8-pbcVcQtYKKMzSjQa4jB4Vi7kMmOCWZLpJRjQPQsMRwQmJT-AD0qVyJvUDL9IJ55Mqf5t0luLMqwcrHVfhmTcvuuQWhL1Lu1uBKT5z6NNExyc-eoKAhKahvVN5WbpFvmUFcIPQ3ocEiyE29Qe7qb71ez_g5iewV91a23T6QZoOVTQghT2m7LqFsXMXcgaLw5wVaVMORy--t5CyTPeXS8avCwV2f1u-ksz_SnF23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوها از کانال‌های غیررسمی حکومتی
درگیری میان حامیان جمهوری اسلامی و مقلدان صادق شیرازی، از مراجع تقلید منتقد جمهوری اسلامی، در جریان مراسم اربعین در کربلا به بازداشت ۱۴۰ نفر و مجروح شدن ۵۴ نفر انجامید.
شبکه تلویزیونی «اشعائر» عراق، رسانه نزدیک به "آیت‌الله صادق شیرازی"، صبح دوشنبه ۱۲ مرداد ویدیویی از این درگیری منتشر کرد.
بر اساس گزارش این رسانه، گروهی با در دست داشتن تصاویر علی و مجتبی خامنه‌ای و پرچم‌های «یا لثارات الحسین» و «یا لثارات الخامنه‌ای» مقابل دفتر آیت‌الله صادق شیرازی در کربلا تجمع کردند و علیه او شعار سر دادند.
این رسانه می‌گوید حامیان علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، و فرزندش مجتبی خامنه‌ای هنگام عبور از مقابل دفتر صادق شیرازی این شعارها را سر دادند که با واکنش هواداران و مقلدان این مرجع تقلید روبه‌رو شد.
به گفته کاربران شبکه‌های اجتماعی، این درگیری ابتدا با مداخله پلیس عراق متوقف شد، اما در ادامه میان حامیان جمهوری اسلامی و نیروهای امنیتی عراق نیز تنش و درگیری رخ داد و پلیس عراق در نهایت با استفاده از قوه قهریه به آن پایان داد.
بر اساس گزارش‌های منتشر شده، در جریان درگیری مقابل موکب منتسب به آیت‌الله صادق شیرازی، ۱۴۰ نفر بازداشت و ۵۴ نفر مجروح شدند. این آمار تاکنون به‌طور مستقل تأیید نشده است.
همچنین در برخی گزارش‌ها ادعا شده است که حسین ستوده، مداح حکومتی، از چهره‌های حاضر در این تجمع بوده و تلاش داشته این مراسم را به موضوعات سیاسی پیوند بزند.
"آیت‌الله صادق شیرازی" از منتقدان نظریه ولایت فقیه است و رسانه‌های جمهوری اسلامی او و جریان منتسب به وی را با عنوان «شیعه انگلیسی» معرفی می‌کنند. او ولایت فقیه را محدود به امر قضاوت می‌داند و با تفسیرهای جدید از اسلام و مذهب تشیع مخالفت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DLeKGFXS7MUDvD3sYgNL4cLQk9Ys7jfHFkVo7_yFiQ9NiYVeUJugZBJ1p5zpLzT69Q5TaL4U-Vl-Rsal0Hzo6fFWjoHtExJxGyvuHKhq0AOZaOpCkaPSltBQf6yN0HU7RgR0sfsap9gjdDNFE_EwhfEXE7utM7NhHSwXEjBkvdHWNJiK6zw07tXwhQZDwXGKYcePRIFkhTvupiAig1cGadiuDj6TT6hSClrmYUtt33H03RzmsroqmObWc_B9B8s_s7so3PyBsMGw4SrFJodFZE5W73Jf-RbBIvacb1tn7EpHPf7Wf0AwUDDsLeOyVjqiRkMNTGIyUCGWt0Tr4dBptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CaTfwZx-v2YNWEWeJN75qr2x6nLzHmcclLvXhrcVjSqL9pHrzUlBdfVdMFY2IimYxdTwnLgDoZfapxBmOvQjC_TB45WEdZ-INDOCcAs1dHzGuIL6D1GrOd3ywabxAkt-sDeFyFJm4Xm2yWBDSW4mQegsSFJwZHChgRbtdEW9bfVJ4i-x4c_J7a_KZSLhbrpv2A0hChEycolUOCEjCJbuU2QegCCyMQ2QVXdKhmqMJ0lE9q3jYqyJnE52E_dm_2vWXfauJfDs_Ip-P0uEvMMBrBmP1Q33RYAedHAq7HwD8YVXVFvZAJagVaVgtpUtnglwAu_ilcgNC6ssY8pJbFlujA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شرکت نفتی آرامکوی عربستان سعودی روز سه‌شنبه اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال جاری، هم‌زمان با افزایش قیمت انرژی بر اثر جنگ خاورمیانه، ۴۴ درصد رشد کرده است.
بر اساس گزارش مالی آرامکو، سود خالص این شرکت از آوریل تا ژوئن به ۱۲۲ میلیارد و ۶۰۰ میلیون ریال سعودی، معادل ۳۲ میلیارد و ۷۰۰ میلیون دلار، رسید؛ در حالی که این رقم در دوره مشابه سال گذشته ۸۵ میلیارد ریال بود.
امین ناصر، مدیرعامل آرامکو، گفت این شرکت با وجود اختلال بی‌سابقه در عرضه نفت از مسیر تنگه هرمز، توانسته است با استفاده از خط لوله شرق به غرب، ظرفیت‌های ذخیره‌سازی و پایانه‌های صادراتی، فعالیت خود را ادامه دهد.
اعلام افزایش سود آرامکو هم‌زمان با انتقاد دونالد ترامپ، رئیس‌جمهور آمریکا، از سود بالای شرکت‌های نفتی صورت گرفت. او گفت این شرکت‌ها به‌دلیل کمبود نفت ناشی از جنگ «بیش از حد پول درمی‌آورند».
@
VahidHeadline
شرکت بزرگ انرژی بریتانیا، بی‌پی (از بزرگ‌ترین شرکت‌های نفت و گاز جهان)، اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال ۲۰۲۶، هم‌زمان با افزایش قیمت انرژی در پی جنگ آمریکا و جمهوری اسلامی، بیش از دو برابر شده و به سه میلیارد و ۹۱۰ میلیون دلار رسیده است.
سی‌بی‌اس به نقل از خبرگزاری فرانسه نوشت پنج شرکت بزرگ انرژی غربی، شامل بی‌پی، شورون، اکسون‌موبیل، شل و توتال‌انرژیز، در مجموع نزدیک به ۴۷ میلیارد دلار سود خالص در سه‌ماهه دوم سال ثبت کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g5HF9wWViXTSLVXRUALtbuoxtAwdXk-CHl2oGt0ZWBBdX-F4ug98bl4sInRmLtNn5k1uDFvClILoeQypwEX374LrqFd1fZkjqfzhg7WLD4oZZmgXPSiirkDrRJx7FoivQCsGvJo_Ap8xloaqRV0LJM_pdJcZM99kNRtfIMuz9U8cRpBVpliJXfHeCHSzfBnaC--biQJxXur6YH0fZ4zRNhLDi4n-QZrtSv-SqiQHXu0CjCXLG8SDHezyI-G_AfNH6gXvJBvu-p2cg_RFEbAbkNL6hkwNzc1Ppx3PZ9_VFcvc-D9jkg65XJRcC0ibP1A9vYmtHqKgTTlYqLVS-b1ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i36NDmq_ySqURcl4rPX6xhyzrmUvuJdkI6Fyng_Hjp2OWBnXzleTyL7-bpmVanOuKWuA69Os4UGJEGKxU2MCOdFb9Yh5Wjjj3qKgiMKAdOIclIq1da0uyT6xrnPf5DVFg4VpydjYN9PLftw2DmCOi2iQxCzRSSAYWKVcL2KrCGn82V4aux4jp7r_y2hy1fokwxdMCVdnpYpM_0-g3jnKgIdBMbdaiqDd6J1EiBgWOmdVfhPImlWEnM_ASQOz8vGEf3k2-DxV9f1kaBcaN35TzUcxBBZZnaUlYpr6pYFC0qtErGhvcbff1TSL1Kygarb0lpuSqXwIBtIHVZTOlBa5rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=YOBMArVLvbuz_1wXUsHXptW3RpQcAJt9CjgWwLvVhK6y64VrTzRQKhdA_FTh-FWX50YulLYlMm5k9HmIBREy2JeuHZHNiscUJ19oQr67UybtcCV5icLrrgGwRhBR-HXAz5avZ_CLU2iVyl5Acvj7xUNRimZ8Mu-J5tEDBvbCbwEMBbuioYhPnsqAyn1miE8CzCmsOB3upUrY7U_JEjItjI27lGmuNc_B-8Ky_cWoYfR-r8PaZV16y8mCKXlpA2NcTbpsq-GlDXYXUQkXPwKKxTI9aW1i63pIPRp4oQOJPErlGjCYptV3QG1A7P4upIKQBzH7bCVc0SOakcyOC9yHag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=YOBMArVLvbuz_1wXUsHXptW3RpQcAJt9CjgWwLvVhK6y64VrTzRQKhdA_FTh-FWX50YulLYlMm5k9HmIBREy2JeuHZHNiscUJ19oQr67UybtcCV5icLrrgGwRhBR-HXAz5avZ_CLU2iVyl5Acvj7xUNRimZ8Mu-J5tEDBvbCbwEMBbuioYhPnsqAyn1miE8CzCmsOB3upUrY7U_JEjItjI27lGmuNc_B-8Ky_cWoYfR-r8PaZV16y8mCKXlpA2NcTbpsq-GlDXYXUQkXPwKKxTI9aW1i63pIPRp4oQOJPErlGjCYptV3QG1A7P4upIKQBzH7bCVc0SOakcyOC9yHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در تیزر تبلیغاتی حاوی بخشی از سخنانش که قرار است در چند قسمت و از امشب به وقت محلی از تلویزیون ایران پخش شود، ضمن رد گزارش‌ها درباره استعفایش گفت: «استعفا نخواهم داد و خواهم ایستاد. اینها می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و اینها یک چیزی می‌گویند.»
این سخنان یک روز پس از انتشار کلیپی پربازدید از سخنان محمدباقر خرازی، دبیرکل تشکلی موسوم به «حزب‌الله ایران» که برادر همسر مسعود، برادر مجتبی خامنه‌ای، رهبر سوم جمهوری اسلامی ایران منتشر می‌شود که او درباره «۲۸ بار استعفای پزشکیان» و «تهدید مجتبی خامنه‌ای به پذیرش استعفای بعدی» سخن گفته بود.
این سخنان واکنش‌های چهره‌ها، جریان‌ها و رسانه‌های حامی و منتقد دولت را برانگیخته است؛ از جمله حمید رسایی که از آقای پزشکیان خواسته بود برای راستی‌ازمایی سخنان محمدباقر خرازی استعفا کند.
مجتبی زارعی، نماینده عضو کمیسیون امنیت ملی مجلس ایران در واکنش به طعنه آقای رسایی نوشت: «از ۹۰ میلیون ایرانی فقط یک شاهد برای تهمت خرازی به امام سید مجتبی شهادت داد ؛ سرکرده شریان!»
@
VahidHeadline
حمید رسایی نیم‌ساعت پیش، یعنی پس از انتشار ویدیوی پزشکیان هم تاکید کرد که هنوز تکذیب نشده:
بعد از اینکه سیدمحمدباقر خرازی درباره نحوه برخورد رهبری با استعفای پزشکیان - که تاکنون تکذیب نشده - ادعایی کرد، اطرافیان رئیس جمهور برخوردهای متفاوتی و گاه توهین آمیزی داشتند.
تصور کنید اگر وی ادعایی برخلاف آنچه نقل کرده به زبان آورده بود (مثلا رهبری به پزشکیان گفته شما باید محکم ادامه بدی) چه اتفاقی می افتاد:
rasaee
👈
بعدش، یعنی دقایقی پیش، این خبر منتشر شد:
دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با انتشار بیانیه‌ای، گزارش‌ها درباره هشدار به مسعود پزشکیان در خصوص استعفا را تکذیب کرد. این بیانیه یک روز پس از انتشار ویدیویی از سخنان خرازی منتشر شد که در آن مدعی شده بود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده و مجتبی خامنه‌ای اعلام کرده در صورت تکرار این اقدام، استعفای او پذیرفته خواهد شد.
@
VahidHeadline
نسخه منابع حکومتی:
دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77730" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQdAax92h2dl8I1izhoSLdtKfS8L8U8J-65kk1cwfc-I6-iInmzPvfjgjPkyi6RF9XEVWl0geLsVfWK4Q0R-VoAhVHS7ujJgwN3DbP24r2y01N0crFTgFHEAsPtDZySWkwj4834K0S9JyUTAyAqrCzj8Um6t_2k7A6lUiNh34E_2pNV7vKg69XfWWgLNRFr1EDGqbFtZvPgtiEu7rEOnyyoPDZRxBpVs1xbvbSYUGaDa6lXLXjKq-mc8nI6wdQPxWYGYy2I4FzE2HMK_pTw4Yx7CHTrDZjZfkaPzLoPfqdVjuaD6UZ14qkFgi70ORS_MTPaO5glmfJoo0oUdDhreeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکنان شماری از روستاهای جزیره قشم حدود چهار ماه است به آب لوله‌کشی دسترسی ندارند و برای تامین آب مورد نیاز خود ناچار به خرید تانکرهای چندمیلیون‌تومانی یا استفاده از منابع نامطمئن شده‌اند.
براساس گزارش میدانی آوش، یکی از ساکنان روستای طبل گفته است: «چهار ماه است شیر آب خانه‌مان باز نشده. حالا فقط با تانکر زندگی می‌کنیم. من توانستم سه میلیون تومان بدهم و آب بخرم، اما خیلی از روستایی‌ها حتی همین پول را هم ندارند.»
پس از آسیب‌دیدن یکی از تاسیسات آب‌شیرین‌کن در جریان حملات ماه‌های گذشته آمریکا به نوار جنوبی ایران، وضعیت تامین آب در بخش‌هایی از جزیره به‌شدت بحرانی شده است. او گفته آب لوله‌کشی تقریبا قطع شده و مقدار آبی که با تانکر توزیع می‌شود نیز پاسخ‌گوی نیاز ساکنان نیست.
این اظهارات در حالی مطرح شده‌اند که عباس علی‌آبادی، وزیر نیرو، ۲۹تیر۱۴۰۵ و در جریان سفر به هرمزگان گفته بود همه آب‌شیرین‌کن‌های منطقه در مدار بهره‌برداری قرار دارند وهیچ‌یک از جزایر کشور با کمبود آب مواجه نیست.
او همچنین گفته بود با وجود آسیب‌دیدن زیرساخت‌ها در حملات اخیر، خدمات آب و برق پایدار مانده و شرایط مدیریت شده است.
عبدالرحیم رضوانی، نایب‌رییس شورای اسلامی بخش مرکزی قشم  گفته است ساکنان برخی روستاها بیش از سه ماه برای وصل‌شدن آب انتظار می‌کشند و پس از آن نیز تنها چند روز به آب شبکه دسترسی دارند. به گفته رضوانی، قیمت یک تانکر چهار هزار لیتری آب به حدود یک میلیون و ۴۰۰ هزار تومان رسیده است.
در همین حال، یکی از ساکنان قشم گفته است برخی خانواده‌ها که توانایی خرید آب ندارند، برای مصارف روزمره از چاه‌هایی استفاده می‌کنند که از سالم‌بودن آب آن‌ها اطمینان ندارند. او به نقل از یکی از اهالی گفته است: «آب تمیزی نیست؛ حتی حیوان داخل آن می‌میرد، اما به‌هرحال آب شیرین است. برای خوردن استفاده نمی‌کنیم، اما برای کارهای روزمره مجبوریم همین آب را به خانه ببریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77729" target="_blank">📅 18:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBV8k4UALAM_DrVjyqj_oDsn9YEAigirURQtWNpLzAZnIbCpISknRKjx1d0siG9Qw9xhys3JhlTAoHZWRrTJGNxEQmaKhy009Kw8jlZ8I2FK7PR3y0GkZdi2tRZVic9aYkECmOKTGYYZAL3dWniQ_eia5IeJ66nCtim81gREgvI9huGcrQmqGNbjSSD3YIXLI9dJdFh4tj1J4bL4jBYA7IEZK21rujENc-3XHG0wnbqsvibHSh_DFQ-5V_cenSJWV1OqRoqacKRtFj7xhA054EROg4S0fx7LwoTve3TeFE6-zpMy3DVVN3JLIKZw8JJwZC_fBcm0COAO8QaZoYimsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه موج پلمپ واحدهای صنفی و مراکز فرهنگی در ایران، در روزهای اخیر، دست‌کم سه مجموعه فرهنگی و صنفی در بابل، مشهد و تهران با دستور مقام‌های قضایی یا نهادهای ناظر پلمب شده‌اند.
هرانا خبر داد مجموعه «شهر کتاب» در شهرستان بابل، با دستور قضایی و به‌دست اداره نظارت بر اماکن عمومی پلمب شده است.
هم‌زمان، گزارش‌ها از پلمپ «کافه معماری سکنج» در مشهد حکایت دارند؛ فضایی تخصصی و فرهنگی که محل فعالیت معماران، هنرمندان و دانشجویان بود. تاکنون درباره علت پلمپ این کافه اطلاعاتی منتشر نشده است.
مجموعه «خانه ارغوان» نیز اعلام کرده است که به‌دلیل «پلمب موقت از سوی مراجع ذی‌ربط»، فعالیت خود را تا رفع محدودیت‌ها متوقف می‌کند. این مجموعه در خیابان فرشته تهران فعالیت داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77728" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQ4KEtnl_A2i-zUBrClLcuLuFne6Yu4aDBADI1YXf85Z3RpfTCCD2XT7j1zPpa9hUdVg4LRh5Vc0WCZkmamNQIHOVQVUPB7vpdYH4OkW8YaquOEjHcZ9b_fSHxkfeOv9A7bUtfpRpzqq5NeTN8seRqvmBNT6VMOWPBry3zLGM4dOyptsxzXKb9eMBsMbBjlNQeoRJ5jtRmcg8o9x1Z6spiuLbAQ96S8I1uurZTq8o5jNmpF76Ir9OZrDBNofwGY0DaDH19-2h7QvEP9A0AwnXnJx-O5rBpW66Xos5grhFeKsylTR-3n2pGLDJuZ5PqDcrWnEUWs6kGEAxZMNaE5N7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سازمان حقوق بشر ایران» اعلام کرد «مهدی روشنی»، معترض بازداشت‌شده در ارتباط با اعتراضات ۱۶دی‌۱۴۰۴ در شهرستان ملکشاهی، با اتهام‌های امنیتی به اعدام محکوم شده است.
این سازمان روز دوشنبه ۱۲مرداد۱۴۰۵ گزارش داد مهدی روشنی روز یکم بهمن‌ماه در منزل خود بازداشت و به تهران منتقل شد. به نوشته سازمان حقوق بشر ایران، او پس از بازداشت، دو ماه در بی‌خبری مطلق نگهداری شد و برای گرفتن اعترافات اجباری تحت شکنجه‌های شدید قرار گرفت؛ اعترافاتی که به گفته این سازمان، مبنای صدور حکم اعدام قرار گرفته است.
سازمان حقوق بشر ایران به نقل از یک منبع مطلع مدعی شده که یکی از افرادی که مهدی روشنی را پس از بازگشت از تهران دیده، آثار گسترده شکنجه را بر بدن او مشاهده کرده بود.
این فرد گفته است: «اگر بدنش را می‌دیدید وحشت می‌کردید. جای سالمی روی آن نبود. پر بود از آثار شوک الکتریکی و شلاق، اما حاضر نشده بود اعتراف کند.»
بر اساس این گزارش، مهدی روشنی اواخر اردیبهشت‌ماه ۱۴۰۵ با تودیع وثیقه آزاد شده بود، اما حدود دو هفته بعد بار دیگر نیروهای امنیتی او را بازداشت کردند و از آن زمان تاکنون در بی‌خبری مطلق به سر می‌برد.
این منبع همچنین گفته است خانواده مهدی روشنی تحت فشار قرار گرفته‌اند و به آنها هشدار داده شده درباره پرونده او سکوت کنند. به گفته این منبع، حدود یک ماه پیش به خانواده او اطلاع داده شده که وی با اتهام‌هایی از جمله قتل «احسان آقاجانی»، مامور پلیس، به اعدام محکوم شده است.
بر اساس گزارش‌های منتشر شده، احسان آقاجانی در جریان اعتراضات ۱۶دی‌ماه در شهرستان ملکشاهی کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77727" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9wZroGIvjzWEbYDTUEW2IgpV0nk8dmKPxIRVp3q7L6YVomrMqEXQsicYVr24TYlH2SAK-wSC30444R6VEmlLNMJWEnEAwG0Pvd1DZANVYKoAuJyu_LgFyvYvMI0_-wBst69BPj2gTDB4kWr5H_63jre_B1ioUOL2OOenB9Ca1wAAfcPxQI77XY18Yr0R5hUsz10_jdVjpfCjZdM1dzCRkGBa9TpjSWTF0ksel7qpt1iEf6zDe5xLGiJcdnmLIOLa9gA2_U8KdAW0Y-sD8ITZd2VmQ7lJNAykzGF2NyYCmaL_j4F9DhwJIGOoK1X7hmUjn0U7O_oCzqEsa5z_dlOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
🔄
و آپدیت چند ساعت بعد:
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
@
VahidOOnLine
🔄
پست پاول دورف، مدیرعامل تلگرام درباره این موضوع، ترجمه ماشین:
🍎
دیشب، اپل برای مدت کوتاهی تلگرام را از اپ استور حذف کرد، زیرا یک کاربر به‌تنهایی محتوای پورنوگرافیک غیرقانونی را در یک گفت‌وگوی گروهی عمومی جاسازی کرده بود.
⬅️
تلگرام ظرف چند ساعت دوباره در دسترس قرار گرفت. اما می‌خواهم توضیح بدهم چه اتفاقی افتاد؛ هم برای هشدار دادن به دیگر توسعه‌دهندگان اپلیکیشن‌ها و هم برای کمک به محافظت از جوامع آنلاین در برابر حملات مشابه.
🧹
از آنجا که تلگرام با استفاده از گزارش‌های کاربران، فیلترهای هوش مصنوعی، هش‌های محتوا و دیگر ابزارهای نظارتی، محتوای غیرقانونی را به‌سرعت از گروه‌های عمومی حذف می‌کند، مهاجم ناچار شد به یک ترفند فنی متوسل شود. او با ویرایش یک پیام قدیمی در یک گروه فعال، محتوای غیرقانونیِ تغییریافته با هوش مصنوعی را در آن قرار داد. در نتیجه، این محتوا عملاً از دید اعضای گروه پنهان ماند و آن‌ها نتوانستند آن را ببینند و فوراً گزارش کنند.
💰
مهاجم یک «باج‌گیرِ حذف محتوا» بود؛ کسی که از صاحبان گروه‌ها باج می‌خواهد و در ازای آن، جوامعشان را هدف قرار نمی‌دهد. این باج‌گیران با استفاده از حساب‌های خودکار، محتوای غیرقانونی را در گروه‌های عمومی قرار می‌دهند و سپس مستقیماً آن را به اپل گزارش می‌کنند تا باعث حذف جوامع مشروعی شوند که صاحبانشان از پرداخت باج خودداری کرده‌اند.
🤝
از نظر عملی، محتوای پورنوگرافیک غیرقانونی در گروه‌های عمومی تلگرام یک مشکل نظام‌مند نیست. نظارت ما مؤثر است (
https://telegram.org/safety
). همین که مهاجمان ناچارند به محتوای دارای تاریخ گذشته و عملاً نامرئی و دیگر ترفندهای فنی متوسل شوند، این موضوع را ثابت می‌کند.
⚠️
با این حال، دو درس مهم برای توسعه‌دهندگان اپلیکیشن‌ها و جوامع آنلاین وجود دارد:
— باج‌گیران راهی پیدا کرده‌اند تا اپل را وادار به واکنش افراطی کنند. اپل پیش از تماس با ما، تلگرام را از اپ استور حذف کرد. این موضوع برای هر اپلیکیشن موبایلی که میزبان محتوای تولیدشده توسط کاربران است، یک خطر بالقوه و نظام‌مند ایجاد می‌کند. اگر اپلیکیشنی که بیش از یک میلیارد نفر از آن استفاده می‌کنند بتواند بدون هشدار قبلی از اپ استور حذف شود، هر اپلیکیشنی ممکن است حذف شود.
— تاکتیک‌های مورد استفاده باج‌گیرانِ حذف محتوا در حال تکامل است و جوامع در سراسر پلتفرم‌های اجتماعی را در معرض خطر قرار می‌دهد. تلگرام تجربه گسترده‌ای در شناسایی ترفندهای باندهای هماهنگِ گزارش‌دهی و محافظت از جوامع مشروع دارد؛ حتی وقتی این کار خطر حذف موقت خود اپلیکیشن ما از اپ استور را به همراه داشته باشد. ممکن است دیگر پلتفرم‌ها به همین اندازه آماده نباشند.
هوشیار بمانید!
☝️
durov
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/txiuK36CFsh8AOnzfeSth9pH7H6rXbssQNNweKtnDKjBhEfMO3xhWD20QTpKgmAebiwu8622F3TeYFDBSn9t584-62sOE4YQOjMt9witQXmffFLGa2wZErjTQBzvc85Uan2uhZsVlvQ8QuO1vznPTwP_hxrJ68swshIFNuqH9GpoPDrs7FMotI_93_--waejw_MVMxrBRMzSmE95WGRCeKBMKn2UNRAOzELm7LcURinrYKfUFjMln51S9uLxQOJ_SlenSgR0DdNrtyrDCPO1XeHkyBVxTUozKzJoBqYVFcUZL72tkrcFZ70PKXKxXRISKCBgp3xXFG7X6ij_Pbyyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu6Wukiteh1PML7VC_L_doKkp264P4r7tv2jgi9TgezjgiFzIaIBKMjx3ociFz23hU6ipo0kNEknlGydghbSouOSEtjLcU3JCJF7gkfcrH_nf5N-QGYMBiP4wY9TJxGZo8tSMFz3KhIhDMUA6i-nBsKTP3uk-Pu3KsL5mpDpK6tiGUM1kHEtsd9Z4jMBjZwN3mRl6ggpTUe8U5wrOYdhTUA9NTpwtiI_XabH3XOBItbhOJaBm3t1KwJRhM9PKTtnyYnCe0TjvPjUouuCSapD3KaLIcudwYvv5529dJFk-8z1b2BGF7UCDG1f68XxGVPbKJIF3Xk3muFIBcnK5S51gG2I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu6Wukiteh1PML7VC_L_doKkp264P4r7tv2jgi9TgezjgiFzIaIBKMjx3ociFz23hU6ipo0kNEknlGydghbSouOSEtjLcU3JCJF7gkfcrH_nf5N-QGYMBiP4wY9TJxGZo8tSMFz3KhIhDMUA6i-nBsKTP3uk-Pu3KsL5mpDpK6tiGUM1kHEtsd9Z4jMBjZwN3mRl6ggpTUe8U5wrOYdhTUA9NTpwtiI_XabH3XOBItbhOJaBm3t1KwJRhM9PKTtnyYnCe0TjvPjUouuCSapD3KaLIcudwYvv5529dJFk-8z1b2BGF7UCDG1f68XxGVPbKJIF3Xk3muFIBcnK5S51gG2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/njMj_ZYbfNwg7NL6qesjGdKL2ZGAsQIW78rhPB_0UO0-s9P6j5vCL7G2Y9fiX1xjRhRoste-41e_B6tkna3-gV1w1JHPshEj_XL9484r46gU79V41u4r0_gNABM2tbyII4rTOB-pTdnRff7L23Jaq9coMkLl5o3Q_0TbfJNmakKiirFMvf0EqYAyLcgwPYmEaey_ukFsEpTV5HJ9Hl_mRQ190IeMzvDYhCd89KJKdJm0Zcvqw8F3z0iPlhgJR_zCZgHeREZSEgtN5JyNjPumnmnS1eBsQCV4INZmF5UGGGHSOa20365rOchI0dntxZsE-8NPr2V4NlhMQaN84sGoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U-uWtkp5UwfKxJtlq1YoSlD8ttjk6yhAZPuBpIGOwOJtuAKg7YX9HJTSStZvp5co9iwDUOKPdQv3-K7atIrJakKipgVTq3tSGtIDlF_nySHDWZMLJyW6oSoiplwZhjDKfSb_fhVD5ZNoVbcbRoLJ5saf50Y9K42OzX1GYvjsm5IwUTz3h_UMIpIXcyw2egPlTqXqxIi_T39MjAYICJys4wh0Pg7zaM3ktzw96kxJvKalXofLGE6ddlkYANGl1Alt_wE6lIhcTxbscfm1tvtVdFNmms830VmIfzUsW8mBSgHBozzEVU3cNKlMj_ShArgy04SjwfpmG42wGZ9_PoADvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEbenDLyL4au2DzCFbvBi4Mld0igtuC1eUw5apSH_hib2gLAr_S7d3R_5uhKgY6Lgb92sf4G1wrxCQbbd0VS7daKG1BfKGIJqpMKhNnOA0EfKRZNEmZpai8CxgAXITPi039m8kzth_-re5RFy5CKKZpC7f0aVt8Vaq6JpS4670T3wRsQ5cs9MTFNzavSyXNYUvHgrqgD9dxl86jqyZaYnjolZGjLThvT4opNI52sh_CUxAbw4gr0oD1Na7roADx6I4cRKV3XVD-Ja0_73-PvpDWzviTMW6LaQBVlCi0uksPfKHFEHaYM8vQ1OZArc8KiPtLAsdM7H4XDCD-3TlezJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsiJOqI2zCyZaNoUXYZDudtrOHxlBoLdYqwLQNd5coSmeyrlWWl9PYW61d57I3BWdCOhO0vobFrU-AXDTB2tVs05g4uX2MPwalWO8rjItdeWwi3xu9ZPPtONIkuoHYCPZYjBmLLbhUJrWZPdUBuSDRqsL7-gTN99Z-6hChMxPw5HJdghSrvjNQDOrQknAvaXIkjqwannjHztd8FtknKWQC_OAwogVdMSLR1s8js_4Y3lCYb97wgfTaLpdmDcfQTYDv56VjQtM2_3CQxNNU3_zgxiLgeZe01Fbe-16_ApFeAJwLk7mQReKKiACdBLzEDGhIsekXVUpSqu2MKolPWgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKlB9KUSDHJqBFJnEWhOzClvYB764M5oWGr4rCM20u5sJex0yvl6D4HLnM2bsW4a9YX_0FS0mdPGcNlPMIHTT0hdYzKRqXB7AtaeNAd-L7k4L5kIQbh4nXUW_ygu1mo9O288-aTBmJAir_khRMUK08OmnmvHoShnnQ0SUVDgJGu6YZj6nvU6rPDJEtn82hlxrpWNDcTo87EjI2mci6-GShc9T5Rdk9jVqTlrMrGE9fvLvnVi0Gwi1R5B7Uvm-uYkgNkryzzZUgDH4S4CTdP4FUuLKpHjhczzaXECMjreTRqOfSGXU1ukVhzRtLRVu3EuYgyGlN7x_N2pj5fxprEIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌رغم افزایش امیدها برای دستیابی به پایان درگیری‌ها میان اسرائیل و گروه‌های فلسطینی، مقامات امدادی غزه اعلام کردند حملات هوایی اسرائیل برای دومین روز پیاپی به مناطق مختلف این منطقه در روز یکشنبه یازدهم مرداد، جان دست‌کم ۱۸ فلسطینی را گرفت.
به گفته مقام‌های بهداشتی فلسطینی، از بامداد یکشنبه، جنگنده‌های اسرائیلی شهر غزه در شمال، شهر دیرالبلح در مرکز و منطقه خان‌یونس در جنوب نوار غزه را هدف قرار دادند که بیشترین شمار تلفات روزانه در چند هفته اخیر را بر جا گذاشت.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از دستیابی به یک پیشرفت در تلاش‌ها برای اجرای توافق آتش‌بس سال گذشته خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77719" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbMkALZHoa86vRT6O9Pt77k4oCceR1O8Fhg65WzVrsGLAI5h1YuJc9JAmPdMavs1GHNihlE8dane8mv1pP1RRr_4i_Xi6HK4OkPwdQ9uwdl66DG9Krtg0NiJNS5SJYzjAHBooJgoVENJVf1_-S9CraR0f0Ouprg1kq7d32I2I2tzr7ZKeWGnz_wDnNAvyUs-wzQ1R0-OEWvVp7jEdxiBUtS3Nf5Vwj-WhQqk8tAfwDdQ65375mIy96Yl_9Le-xKUJpYs3qhHFdE58-ebnkzALhIkk_EY92E-59RIlKnIkgljsoMkksTymWLhI0ouSIg3ABN3Kws163r25ZDdwT_M2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۱۲ مردادماه گزارش کرد که «سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه» یک پهپاد ام‌کیو۹ را در آسمان تنگه هرمز رهگیری کرده و «مورد اصابت» قرار داده است.
این خبر در حالی اعلام می‌شود که دونالد ترامپ، رئیس جمهوری آمریکا از توقف طرح یک حمله بزرگ به ایران به شرط توافق برای بازگشایی تنگه هرمز و اطمینان از دست نیافتن ایران به سلاح هسته‌ای خبر داده بود.
مرکز فرماندهی ایالات متحده (سنتکام) هنوز واکنشی به این خبر نشان نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77718" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdA8-V_l47g59bD2xLhqj6DLQlsp9UjYmoFi017YjrhgRWX27i-E-DWsVqcT59SeNRM3yvF6MmIsb08kT5WhDg_r6O5PG8T_Gn6puPWEirMQGQe43zmoI8j0ypqLK1WgvquJdIEay56EwK9ZeWKtx1THbAV0iDedtAzHoHnwhsZw7m644Kmu8Pkh-TJYU7TQNP4MI5wKaMEU_zu9O62dT36znpuLX9wkw86pMD8D150dn_Cz-TOWsYna3FIzXlW23xVmK27XfXVG1TrMzgTosQHlVYvhYDHb13febRXHJ6YhV1-aKIiWyXoRlvWu7reaUWXF-nA7EqswaA_8GpgTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=RpNif4d9wZSV0tsVjUCZ8UKXBELtGJLZyNqSMDRafH_WM1-4xldgvJeeo60gxzslwfT_G-tXxLdyo7TFugtLDOFzqRN7nv3UvR6IiRPEiiplzUwaHb0h8Eey-kPLo_pshVXTnBj87GpWG4EjVm8ciu9FcV5fS2butrxuNaZUZYni5I4QwZBEYG5Jn0NnbcUciZG-JIn7MjDuS09gYUu7Q-MxM2d7xP0ZViot_IrNq1BF-NzBGQdFlXQVeNd_3SG1UqEJin-jQe1a4rEeqrTunnGOvAdQ5_uXMd1jC--LCuunTiI_z0A5aCv0QQJxRppqsqL4YRvnbEDPjPteX4pHLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=RpNif4d9wZSV0tsVjUCZ8UKXBELtGJLZyNqSMDRafH_WM1-4xldgvJeeo60gxzslwfT_G-tXxLdyo7TFugtLDOFzqRN7nv3UvR6IiRPEiiplzUwaHb0h8Eey-kPLo_pshVXTnBj87GpWG4EjVm8ciu9FcV5fS2butrxuNaZUZYni5I4QwZBEYG5Jn0NnbcUciZG-JIn7MjDuS09gYUu7Q-MxM2d7xP0ZViot_IrNq1BF-NzBGQdFlXQVeNd_3SG1UqEJin-jQe1a4rEeqrTunnGOvAdQ5_uXMd1jC--LCuunTiI_z0A5aCv0QQJxRppqsqL4YRvnbEDPjPteX4pHLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی، می‌گوید در حال حاضر مذاکره‌ای بین ایران و آمریکا در جریان نیست.
اسماعیل بقائی در نشست هفتگی خود با خبرنگاران در روز دوشنبه ۱۲ مرداد، افزود آنچه در حال حاضر در جریان است، مذاکرات دو جانبه و بین دو دولت ساحلی ایران و عمان است.
او  می‌گوید که «حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.»
اظهارات او در شرایطی بیان می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرده که مذاکرات با ایران بعدازظهر دوشنبه ۱۲ مرداد آغاز خواهد شد.
با این حال او روز یکشنبه، هنگام بازگشت از تعطیلات آخر هفته در نیوجرسی به واشینگتن، به خبرنگاران توضیح نداد این مذاکرات در کجا برگزار می‌شود یا چه کسانی در آن شرکت خواهند کرد.
@
VahidHeadline
سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس می‌گوید در حال حاضر «هیچ بحثی» برای مذاکره با آمریکا در دستور کار قرار ندارد.
حسن قشقاوی در گفت‌و‌گویی که خبرگزاری دانشجو منتشر کرده، افزوده که حکومت ایران به‌ویژه در پرونده هسته‌ای، با واشینگتن مذاکره نمی‌کند.
او بدون اشاره به جزئیات افزود: «حتی در مسیر‌های احتمالی دیگر نیز بحث هسته‌ای مطرح نبوده و آینده این پرونده در متون مربوطه کاملاً روشن است».
این نماینده مجلس، اولویت فعلی جمهوری اسلامی را «لغو تحریم‌های اولیه و ثانویه در کنگره و بازگرداندن اموال بلوکه‌شده ایران» عنوان کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77716" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIV4Ae1esXJEJDOha0zhEWyecijxtVmT_xHzHOUUz3V3nij9iF1J1eOQSK3WZMehDRQONvjhCV6SvCfnbedyLPlE1Cbz8bujYritzVdbGv3aAz3JRv4I_4B1V-ueTQUKskUfsyAkbBjSA98Vng921ndDilhGUhK_UiF_6ifrdSvQzmOk_76LHY4jxl4te1E2T0XOvbxfgnULdtHQTIDFIUBCsrSiIHQUGRFJa9GoMODWYiJ2oRzDhDu6JAFFuGFI3eQhrgiGsfoJRlTylMaElviinAFaDm8W-i-lx_OhCnoUciZw4FJT3SzolMA4bF-kUojXAb_I6WJoM5WBhrLnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا، روز یکشنبه ۱۲ مردا گفت نیروهای این کشور همچنان در آماده‌باش هستند و آمادگی اقدام دارند؛ اظهاراتی که نشان می‌دهد تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به‌تعویق انداختن حمله به ایران، تأثیری بر آمادگی نظامی نگذاشته است.
پیت هگست در شبکه اجتماعی ایکس و در کنار انتشار ویدئویی از رئیس‌جمهوری آمریکا نوشت: «وزارت جنگ آماده اقدام بود و همچنان در سطحی که از زمان جنگ جهانی دوم دیده نشده، آماده است.» هگست سپس گفت ارتش «کاملاً مسلح و آماده شلیک» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77715" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig9M6pdvUiddVLCuPsIZ8F5SkqHmXRpzGP5Z2nMclJjBcZltmNNLBB6pIlGa9wA7tE5qP52PpWGR4RM-ZKZsgODH6u6lKpiC9Syis1NXXyZAA6ur6p9qFBT5V4bdVy-v5SFwMtN_SJ5caqVpk5i52em-BxU_RFHyxPjrLJLzrsO-uDJ8jvvNk-PxFpoYIIJcLDQTA87s5Mp0xCi8ygSpoVjOZle2IK7boqUXpN5d7BkVjQHaBxYwNx_lhPhVFWjZNDrfo9uhirDlLiMJmikGxEBytYpORRZyRUEVS9GnOl1HBzhHz-SnEoBGSsscwE2HQFp_GssTkWFp4SUB0lBEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
خبرگزاری فارس از کشف یک خط لوله ۹۰۰ متری غیرمجاز انتقال نفت در استان بوشهر خبر داده و نوشته این لوله نفت سرقت شده را به مخزنی زیرزمینی منتقل می‌کرده است.
به گزارش فارس، فرماندۀ انتظامی استان بوشهر گفته است: «انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی» شده است.
این مقام محلی به فارس گفت که «تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات» مرتبط با این خط لوله غیرمجاز توقیف شده است.
در این گزارش به مشخصات فرد یا گروهی که در احداث و بهره‌برداری از این خط لوله غیرمجاز نقش داشته‌اند اشاره‌ای نشده است و معلوم نیست آیا آنها شناسایی و تحت تعقیب قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77714" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZbEwKMul9eAXPcZ7hpxVsrOqDD2raZECJj3rsbY3_r9TcIolxN7d8RyxQyTfvnE2hqfX0Csgq9mCy0lKW9AqGxHhFfso8lx8hjeYF4BL5ZfYoRGu3KtbU9nF1bkPrqpYCLoY-nzYGBAqrl_L_PtRqfjct2XOYjNcW1_TO41XOXsudR0QnxyA29jI1GK4ZWncG-hDWWhHfqt5dU0_88LV39mVxNQETupy_Ec4eNebn_V5iXJUeWSfrsQvxIo8zk09TqoCuvsmSwWHE3xN4OpX7JpC1a3h4dPUyC3uzJVrP0YHxagzRMEMvVE2pxboy5tOdrqsC2Ndk4lMRj_-EvB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی نفت دوشنبه ۱۲مرداد۱۴۰۵ پس از اعلام «دونالد ترامپ» مبنی بر توقف حمله نظامی آمریکا به ایران و آغاز دور تازه مذاکرات میان دو کشور، بیش از پنج درصد کاهش یافت.
خبرگزاری «رویترز» گزارش داده که بازارهای جهانی، کاهش احتمال درگیری نظامی در خاورمیانه و افزایش امید به دستیابی به توافق میان تهران و واشنگتن را مهم‌ترین عامل افت قیمت نفت می‌دانند. به نوشته این خبرگزاری، نگرانی معامله گران از اختلال در عرضه نفت و بسته شدن احتمالی تنگه هرمز، پس از اظهارات ترامپ کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77713" target="_blank">📅 17:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SmfY7HO6ELEjX0zy5Jt5N_efdBayhfwtTI8ANKUPBxt8j7E--nPRIEHfKNoyLg5Uya7AmU8hI3wcLiTejPjcEOJHbbGFfnhSbTCbaB9hZWUzZkthn1xSVt_ZrswoO1sFNlg8HR2rtJjhBPcQyhwmG7LtyDKu_AN7M3IBEAZCqX1RXPj6jANdmKaH2FIlwZSsfdHukMuvmkuBVmRctjnUZZT4Mg5bgQkt00FsKEvUqLYXanb7XVRjDSN3EgThUzOyOZQNw41LxH2mDTV0g-TEK3MmpJ0A3QersbWk3Ga3cazfNFGgo-kN6r0amghsktis_lPsrz0R5ABkr6N0PeM9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه وابسته به قوه قضاییه جمهوری اسلامی از اعدام دو زندانی به نام‌های «امید بهزاد» و «پوریا صفوت» به اتهام «جاسوسی» و «همکاری اطلاعاتی» با اسراییل از طریق «ارسال تصاویر مراکز امنیتی و نظامی» جمهوری اسلامی خبر داد.
خبرگزاری میزان، ارگان رسمی قوه قضاییه، اعلام کرد این دو زندانی بامداد دوشنبه ۱۲مرداد اعدام شدند.
به ادعای این نهاد، «بررسی‌های فنی» انجام‌شده روی تلفن همراه امید بهزاد این موارد را تایید کرده و او نیز «در جریان تحقیقات» به آنها اعتراف کرده بود. با این حال، مشخص نیست این اعترافات در چه شرایطی از او گرفته شده است. جمهوری اسلامی طی بیش از ۴ دهه حکومت خود، بارها اقدام به اخذ اعترافات اجباری کرده است.
در گزارش میزان، پوریا صفوت نیز بدون ارائه هیچ‌گونه سند یا جزییاتی، به همکاری «مستقیم با موساد» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77712" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=SL_gQuDm8u6QllaTTbf0UIGurlYsWYA5agzskaGh9kvrEs5mVMR-DTL9epK2cN7XlgngzCppKpccAntNn9OSNcCdwtatmSst0oAyOAl-BJZClh4by58eY846HTt12AnOsONUSXDPBLduIXRNjU0tnphaEp0rCddIRsDmxO1Xc9_fEy6UN_P9wbQLsqr6qnz27lbjlN4aZMyGEaDUF8ephZ3QrrXaqgrfI5jvdamEQNj6fYRxvRcBOReahM_RyqF7BLrOjSkOAiXAKIkLkk607D80P-Jk-AgnsjHSLIMekg2-NANNO24lkS1aBvHs17I0XXvLbHIkdsbtLOOE8E_4ZaI97tDGaRvTTf7P-1DWTrB5mZ_ipCBh0ndeQ5wQy5GJHXjrl6x1V9wEDQ_zQ-67SfFm3Oz1tbW16g4QCX4oB1OtNVVRN_PHmkbEQ2tvbWKogSWc2r7U6mvxkFiHTI2LZdSGLbItoerH_zgVx9HjGPSsbFoGyok8kS8IusFY1VDiDKg06j8FfSJx2dopK4sJ3Z32elDPwm3q9jmgE7dCgQlEEpHTS1EP0VzlR0cdi-GEIGubKb61wlM13PLUPLzlgPIc7_pias34YJlqVFYIT36HryxLUNMihaxq1nGLiQ_tPS6Me9NsfImChZZNlzmHrwrhVlES89ylRUJ5Msj29g4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=SL_gQuDm8u6QllaTTbf0UIGurlYsWYA5agzskaGh9kvrEs5mVMR-DTL9epK2cN7XlgngzCppKpccAntNn9OSNcCdwtatmSst0oAyOAl-BJZClh4by58eY846HTt12AnOsONUSXDPBLduIXRNjU0tnphaEp0rCddIRsDmxO1Xc9_fEy6UN_P9wbQLsqr6qnz27lbjlN4aZMyGEaDUF8ephZ3QrrXaqgrfI5jvdamEQNj6fYRxvRcBOReahM_RyqF7BLrOjSkOAiXAKIkLkk607D80P-Jk-AgnsjHSLIMekg2-NANNO24lkS1aBvHs17I0XXvLbHIkdsbtLOOE8E_4ZaI97tDGaRvTTf7P-1DWTrB5mZ_ipCBh0ndeQ5wQy5GJHXjrl6x1V9wEDQ_zQ-67SfFm3Oz1tbW16g4QCX4oB1OtNVVRN_PHmkbEQ2tvbWKogSWc2r7U6mvxkFiHTI2LZdSGLbItoerH_zgVx9HjGPSsbFoGyok8kS8IusFY1VDiDKg06j8FfSJx2dopK4sJ3Z32elDPwm3q9jmgE7dCgQlEEpHTS1EP0VzlR0cdi-GEIGubKb61wlM13PLUPLzlgPIc7_pias34YJlqVFYIT36HryxLUNMihaxq1nGLiQ_tPS6Me9NsfImChZZNlzmHrwrhVlES89ylRUJ5Msj29g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، می‌گوید که «مذاکرات جدید» با ایران روز دوشنبه آغاز می‌شود.
آقای ترامپ گفت که در حال حاضر توافقی درباره تنگه هرمز وجود دارد و توافقی هم درباره هسته‌ای زدایی ایران حاصل خواهد شد.
@
VahidHeadline
گفت‌وگوی ترامپ با خبرنگاران در هواپیما
تشخیص و ترجمه ماشین:
🔺
خبرنگار:
چه چیزی باعث شد حملات دیشب را لغو کنید؟
🔻
ترامپ:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند این کار را انجام دهم.
ما تقریباً همین موقع کاملاً آماده اجرای عملیات بودیم و قرار بود حمله‌ای عظیم باشد. همه‌چیز برای اجرا آماده بود. اما وقتی متحدان می‌خواهند حمله را لغو کنید، ناچارید بگویید: «خب، ببینیم چه می‌شود.»
دلیل درخواستشان این است که فکر می‌کنند توافقی وجود دارد. توافقی دربارهٔ [واژه نامفهوم] وجود دارد و بعد هم توافقی درباره موضوع هسته‌ای حاصل خواهد شد؛ یا می‌توانید آن را «هسته‌ای‌زدایی از ایران» بنامید. من آن را هسته‌ای‌زدایی از ایران می‌نامم.
فعلاً آن را متوقف نگه داشته‌ایم. فقط باید ببینیم چه می‌شود. هر زمان بخواهیم می‌توانیم آن را انجام دهیم.
اما سه طرف اصلی از ما درخواست کردند. ایران هم با تأکید زیادی از ما درخواست کرد. گفتند: «مایلیم توافق کنیم.»
حالا نمی‌دانم بیرون چه می‌گویند، چون خیلی وقت‌ها این را به من می‌گویند و بعد بیرون می‌روند و می‌گویند: «نمی‌دانیم او درباره چه حرف می‌زند.»
بدیهی است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها از وسعت حمله خبر داشتند، چون [عبارت پایانی نامفهوم است].
🔺
خبرنگار:
حالا چه اتفاقی می‌افتد؟
🔻
ترامپ:
کاری که اکنون انجام می‌دهیم این است که در قالب مذاکره با آن‌ها گفت‌وگو می‌کنیم. مذاکرات فردا بعدازظهر آغاز می‌شود و خواهیم دید آیا واقعیت دارد یا نه.
خیلی دوست دارم این اتفاق بیفتد. جان‌های زیادی نجات پیدا می‌کند و [ادامه جمله نامفهوم است].
سال‌های بسیار زیادی طول می‌کشید تا بتوانند آن را دوباره بسازند؛ البته اگر اصلاً امکان بازسازی‌اش وجود داشت. فکر نمی‌کنم حتی قابل بازسازی می‌بود.
حمله‌ای آماده کرده بودیم که اگر انجام می‌شد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
برای آن‌ها فاجعه‌بار می‌شد و نمی‌خواستند ما آن را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم آن را نمی‌خواست. آن‌ها فکر می‌کردند توافقی قریب‌الوقوع است.
🔺
خبرنگار:
آیا ضرب‌الاجلی وجود دارد، قربان؟
🔻
ترامپ:
توافقی قریب‌الوقوع است که به [واژه نامفهوم] و در نهایت به هسته‌ای‌زدایی از ایران مربوط می‌شود.
وقتی این را می‌شنوم، می‌گویم: «آیا می‌خواهیم تا این اندازه شدید عمل کنیم؟»
گروهی از مردم هستند که می‌خواهند من فوراً این کار را انجام دهم و گروه دیگری از مردم هم هستند که نمی‌خواهند من این کار را انجام دهم.
🔺
خبرنگار:
آقای رئیس‌جمهور، آیا ایران برای رسیدن به توافق ضرب‌الاجلی دارد؟
🔻
ترامپ:
باید ببینیم. ببینیم اوضاع چگونه پیش می‌رود. هر زمان بخواهیم آماده‌ایم وارد عمل شویم.
آیا ترجیح می‌دهم توافق کنم؟ من در پی کشتن مردم نیستم، چون مردم کشته می‌شوند؛ تعداد زیادی از مردم کشته می‌شوند و ما این را نمی‌خواهیم.
بنابراین آن‌ها از ما درخواست کردند؛ مشخصاً ایران. اما آن سه طرف دیگر هم گفتند که واقعاً...
از آن‌ها پرسیدم. [اشاره نامشخصی به پادشاه و سپس ولیعهد.] گفتم: «ترجیح می‌دهید چه کار کنیم؟ ترجیح می‌دهید ما این کار را انجام دهیم یا نه؟»
گفتند: «ما توافق را بسیار بیشتر از حمله ترجیح می‌دهیم، چون نمی‌دانید این [واژه نامفهوم؛ احتمالاً اشاره به حملات یا اقدامات] به کجا منتهی می‌شود.»
آیا کشورشان با ورود سیل‌آسای مردم و فاجعه روبه‌رو خواهد شد؟ اتفاق‌های بد زیادی ممکن است رخ دهد.
🔺
خبرنگار:
قربان، گزارشی منتشر شده است که می‌گوید نیروهای آمریکایی را از بحرین و کویت خارج می‌کنید. آیا نیروها از خاورمیانه خارج می‌شوند؟
[در ترنسکریپت هیچ پاسخی از ترامپ به این پرسش ثبت نشده است.]
....
🔺
خبرنگار:
بازگردیم به ایران؛ آیا آماده بودید اهداف انرژی را هدف حمله قرار دهید؟
🔻
ترامپ:
نمی‌خواهم این را بگویم. نمی‌توانم این را بگویم.
قرار بود حمله‌ای عظیم باشد. قرار بود حمله‌ای باشد که با فاصله بسیار زیاد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
اما از ما خواستند آن را انجام ندهیم. گفتند: «لطفاً این کار را نکنید.»
همسایگانشان هم همین را گفتند.
بنابراین فقط می‌خواهیم ببینیم آیا می‌توانیم درباره هسته‌ای‌زدایی به توافق برسیم یا نه.
🔺
خبرنگار:
[پرسش ناقص درباره اینکه مذاکرات فردا انجام می‌شود.]
🔻
ترامپ:
بله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/77711" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpzZSFuP1XB5sqiFTt_FZeN9JhxayiHQRqc2aBoTAngWf4EXsriQDzXyb7w1FuihTNG7B6z7Vq4tw0DR82yNGxD4cLN256zLbygxzjg1XYjD9GUOvtBYj0wCKKHw9EAhup4ir6KB82g8ah2NVDrON4I3esp99hyd3VqiqzUkfSv7zNsrExVHqkNIFGetxrse3A7zZ_8B--D1bCeixStiG8W8mJuZf1MaZ8yqcXZm7B8dy4YY6dwTCFtxrxYG9fi-LvY8s-YPj--1Nq1SuAaiPgf87F2v9gvAvDn8tYtKov69t2OMourFXn34uqt_hZNFrYXIOvpx9jun6KjDKbYx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رییس‌جمهوری ایران، در پیامی یادداشت تفاهم امضا شده میان تهران و واشنگتن را «حاصل خرد جمعی اعضای شعام» توصیف کرد و نوشت: «باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند.»
پزشکیان روز یکشنبه ۱۱ مرداد در شبکه اجتماعی ایکس نوشت: «تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود. باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.»
همزمان، کانال ۱۲ اسراییل به نقل از منابع آگاه گزارش داد کشورهای منطقه در حال میانجیگری برای بازگرداندن آمریکا و ایران به یادداشت تفاهمی هستند که ماه گذشته میان دو طرف امضا شد.
بر اساس این گزارش، توافق پیشنهادی شامل باز ماندن تنگه هرمز به مدت ۶۰ روز بدون دریافت عوارض و تمدید آتش‌بس میان تهران و واشینگتن است. کانال ۱۲ گزارش داد یادداشت تفاهم پیشین به دلیل اختلاف بر سر نحوه مدیریت تنگه هرمز از هم پاشید؛ به گونه‌ای که دونالد ترامپ بر باز بودن کامل این آبراه تاکید داشت، در حالی که تهران معتقد بود این توافق به جمهوری اسلامی اجازه می‌دهد مسیر عبور کشتی‌ها را تعیین کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77710" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
