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
<img src="https://cdn4.telesco.pe/file/vVIXrgJFeMi6eb0LnMzBxNjGM24XjofyA3_4f3C96VH4I2DpJxaRkAKNWVmt1GgcW5PHEJTtoX3YvSd6IGmwTc7XkDX19dFdc0J6zdnn4gu2Zx9COCeJfGQ_KoBV4dqv3qjZ0uxra3SzVdcQWK7_u-cBp8CNOzF89gf8ASXCtnE1Se9etS24G1Swa_VI7UdvwR383NiAT9rB_D1XHSwv_f8qHY6Ea-vyKR7SraXMY2kvdvQ0H7h06ZdTS7_iftVJWz3ix3gpcxtZLND6qnwR1Doom5dMQlMXukk7KmWEb7Cxe5kt7eWmt1DCQRoj3qcWBar6Ivi2kHQPbqUMXlrlnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-463860">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_5kaMH8us8O4Mi2SaSfhp9vHC65LMhrmPt6dM63_WmBxauIczDWpN3k5yXA8GGn8yKN0Qumw-MqK5HAkqEfR3ZsTpUjsKUK0HZUjjh8Z0jVHSDhJlOgrX1CleJXD5PbrhFdv__Ojx7GeZTNPMis49a9IGFrchSRjlnJxohX4Xf_QqL8-fhpA8l_GLpQ81inHShbYMddxA0POHPEjAjcUjXPZGskEyQhdiq4YJK6cW1c0XmKfjakwwuPRQyhLYYTHyWy7VDGLCkkBMPkqy80C4d00zGScCNiJ-Tii0McBenz4O6BSXZjmE_4GRmEMoI9XQz45KYF4DYiI1Ma4LzSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دهه هشتادی‌ها، نودی‌ها و دهۀ آینده ایران را تضمین خواهند کرد
🔹
رئیس‌مجلس در دبستان پسرانۀ شهید آیت: شما دانش‌آموزان وارثان نسلی هستید که بیشترین شهید دانش‌آموز را در دوران دفاع مقدس داده بود.
🔹
امروز در شرایطی فعالیت مدارس آغاز شده که تعداد زیادی…</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/farsna/463860" target="_blank">📅 13:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyLzl-Y6NUFXt8BRYzIUSUEL4qkhZoFb1rs0VIrDpV7Hd43axrR4oM326RNjNGFwp4IM-n-W6Kx3WPWXQhsAuVgfcQIU-Zq415iPdWQolM3Mf6Scc4fS111CozkxKIoSmOU-hJtsnAG3ID4VJgxMxxPqRFKrYd86Bh5GY-haX4rVvr1d6yZ2wUWgY11Acpo3iPYe7mZEhLV37mjNRZOyniXzTRzOglbzSy7_J_v6H_M31UFOd6zTgDjziQvEO7_YwhJTJQyidCbNu0hjqqFscUUKtx9rV8fdSXOvYQy91eOzgYsEZohtyyUmMouGL3BfCEhlUaX0QqdO3qY8vBVfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
امیدها دوباره همه را ناامید کردند
🔹
تیم ملی امید کشورمان با شکست سنگین مقابل کرۀشمالی و با توجه به نتیجۀ دیگر دیدار این گروه بین تیم‌های امارات و چین در رتبۀ سوم قرار گرفت و از گردونۀ مسابقات کنار رفت.
⚽️
ایران ۱ - ۴ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/463859" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlHLQYpMeTfEQFF3iznDmcSfWg10ninF-GWovuCXAv5OktBt6zOjFejz0DG4YKC2zptP_u4B-Y5m4moxVGPU36aLaqS5uK3FvTtIDpWaUjM-qW5jRAbquAJi_Kv3JqP4H6QcXWfdM4UbIOLJhWx5Zct_aY4QO7GYLYkY_7bbMLOR06ke3KjBqNP7RBVw0z54vHNUITej-9N-2QomnjjIjpTX7Patnd36wwS--Kje6JNy92-2XnF0p_OqES81UDqiOz4d2OURwPeviIqvocQaeb9ZpUtc_j_9DgPoG16NFOhwEdsUZwc5DhBQCUvzUgEtcR2sgagLOSafP82NxZ3hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دهه هشتادی‌ها، نودی‌ها و دهۀ آینده ایران را تضمین خواهند کرد
🔹
رئیس‌مجلس در دبستان پسرانۀ شهید آیت: شما دانش‌آموزان وارثان نسلی هستید که بیشترین شهید دانش‌آموز را در دوران دفاع مقدس داده بود.
🔹
امروز در شرایطی فعالیت مدارس آغاز شده که تعداد زیادی از هم‌کلاسی ها و هم‌سالان شما در مدرسۀ میناب و چند مدرسۀ دیگر مورد هجمۀ دشمن قرار گرفته و به شهادت رسیدند؛ آنها در حقیقت رفتند تا ایران عزیز ما بماند.
🔹
پرچم زیبایی که به‌دست شماست، نشانه و شناسنامۀ این ملت و نماد عزت و اقتدار آن است که به آسانی به‌دست نیامده و جانفشانی‌ها و تلاش‌ها در این مسیر اتفاق افتاده است.
🔹
بدانید آنها به شهادت رسیدند تا به من و شما بگویند آینده این کشور از آن شماست و ما چشم انتظار این هستیم که دست‌های توانمند شما دهه نودی‌ها و دهه هشتادی‌ها، آیندۀ ایران را تضمین کرده و با دل‌های بزرگ و خالص و خلاقیت خود آن را بسازید.
@Farsna</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farsna/463858" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPU0z5PlzlVaWll_zftse0gYOcJ8whbAOFdKHuG00K_XqE9Ire6UD9BCHFkl5-N4MdxEhIrFW-0GylXuz5RmtKOS9jf9sXE06DMeOEkrK4bsRW-sie47jG5v71bDgmmaHYa20g8KFtbWYrSER_OWs6vbKHMkAIHOqpF4i8lxv58eMzHDTDL9RRBoEZyNQFCWD_fx2gZiCLW67z78ez3bbH6kS3sHMuVvdNs3WCATyEd-d8f_H4L7WbwlLkDoLQKp4-DS4hkgyJ_T6Xod5y4cOAKG9ybmc6dpb_oQJBK-1FullMjpyy9TCso42ToFmJHM7FJiSu2eACprqy4W1H95jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔹
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔸
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/farsna/463857" target="_blank">📅 13:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI7fqral5McC26NCLwM0ZfAZOlhkyi6OGOCIBDzwLKTTPilkH7sH3ZprSDQnmnDm9Eqzw6oTsed_oy3T--PtGX1wALi7itJx9vwuWvYZvb6AZntdHHvHrTWfFEXn8s_fdZtCY28QWJK4g1sYszljBKjrFJ5IGXaOTsYpSqmY-EiCiCYV5Fi4l35YCqQZlemluactyNpeRCBXGCGLb3mjBjkqCGKy1SVHdpmkwb0OIaIGsSTSyviKIRlc4V9sC8SgReH60lULyJF_Z5TuaLa9sc7tC1Sjw0C4he2hNKPO9d-P4qpqvFH8nYBznuGsaNLjuZKM-127iWaa_D8b-_pPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ پرسش از عراقچی درباره علت دیدار با ویتکاف
🔹
به گفته سخنگوی وزارت خارجه، دیدار تیم ایرانی با ویتکاف در سازمان ملل، با هدف ابلاغ شروط تهران به طرف آمریکایی انجام شد. این درحالی است که طبق تصریح محسن رضایی و بقایی، هفته گذشته شروط ایران از طرق میانجی به آمریکا ابلاغ شده بود. بنابراین، سوال‌هایی در خصوص این دیدار مطرح می‌شود.
🔸
۱. همان‌گونه که دبیر شعام و سخنگوی وزارت خارجه تایید کردند، هفته گذشته شروط ایران به‌طور رسمی به آمریکا ابلاغ شده بود. درنتیجه، واشنگتن از شروط ایران برای هرگونه مذاکره و پایان جنگ، مطلع بود. طبق اظهارات بقایی، دیدار روز گذشته عراقچی و ویتکاف، موضوع جدیدی نبود و در این دیدار، شروط ایران ابلاغ شد. بنابراین، سؤال این است که برگزاری چنین نشستی، چه لزوم یا دستاورد یا ضرورتی برای ایران داشت؟
🔹
۲. بر کسی پوشیده نیست که یکی از اصلی‌ترین فشارهای داخلی و خارجی بر دولت آمریکا، افزایش قیمت نفت است. همچنین پرواضح است که برگزاری ملاقات با طرف آمریکایی آن‌هم در سازمان ملل، بر قیمت نفت موثر بوده و فشار آن را کاهش می‌دهد. اگر آمریکا هنوز پاسخی رسمی از طریق میانجی مبنی بر پذیرش تمام شروط ایران ارسال نکرده، چه لزومی دارد که چنین نشستی برگزار شود و از عوارض جانبی آن، کاهش قیمت نفت و درنتیجه کاهش فشار بر آمریکا باشد؟
🔸
۳. بر اساس بیانیه اخیر قرارگاه خاتم‌الانبیا، آمریکا با هماهنگی متحدین خود، در حال برنامه‌ریزی برای اقدام علیه ایران است. هرگونه اقدام نظامی جدید و سطح بالا، شوک بزرگی به بازار نفت در سطح جهانی وارد خواهد کرد. بنابراین، آمریکا نیاز دارد پیش از اقدام، قیمت نفت را تا حدودی، هر چند کم، کاهش بدهد تا بعد از اقدام، با وجود شوک نفتی، قیمت نهایی آن عددی دور از انتظار نشود. بنابراین، هر اقدامی که منجر به کاهش قیمت نفت در زمان فعلی باشد، ناخواسته نیازهای پیش از حمله آمریکا را تسهیل می‌کند. سوال از وزیر امور خارجه این است که چرا دیدار با ویتکاف، در چنین زمان تعیین کننده‌ای، انجام شد؟
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/463854" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f719d6b1.mp4?token=aNGVQZbzZ-MdmY6aqrSy7z4rGgKk3zJuVYApR1TRxZkLL-bZWBFvwiTQCFSKEYT4locmzOI9Y0em3tFEyVunW967toFouTws7XfseTvT4lRGQqXLHAWfJgJGusqgYbF2lQsb7V6svL4H_BujiENR3iCULI8X3JVWQ3J1YfRLKS5E4FRsD-lC_GXJUodvDgbI1jUxTB1ZZ-WzpYsLTu3ngPv_5BHmAWQjSVodDlbAVnmzDZ7cmXz7MvZtdCFWuiD0gLFvW_UgTB3iMvLusC9hlfHy6s_zZFGVIuSku6cpfIh8qSeytMApbkL6reSeMJ57xf-3UORekk3QThgVUX8jF08QqTTmM-BV8QS07YqFaNBB86CfOUoPbIhzAbGh9XCgQGRNLhuhGdPRupU8WfNRpQp2xjUhEiviFhHobINBct8ITWelCk5QgOYh_ZFo--7nqmFLmiulsMBcZf5E4abqNymiMYILchJtcR4C7--VXd5fOSwt9WAgwhcDr1r4KLxZa3jbIEaYKK5UbNGEmj96o85PhGGQsd3p31EIlUCbZEvATQ6tNHpZ0iz-hPbisZrV2plSr3p0ciww4_uzlCO_UHb43z3T4TXJkVx4HFF_YtiN4OFLEEMQWhjZxaHlIvN3xr0z1foC2ZJGZLmJY8E-vZGhkAY8BkoR155XFW5O1ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f719d6b1.mp4?token=aNGVQZbzZ-MdmY6aqrSy7z4rGgKk3zJuVYApR1TRxZkLL-bZWBFvwiTQCFSKEYT4locmzOI9Y0em3tFEyVunW967toFouTws7XfseTvT4lRGQqXLHAWfJgJGusqgYbF2lQsb7V6svL4H_BujiENR3iCULI8X3JVWQ3J1YfRLKS5E4FRsD-lC_GXJUodvDgbI1jUxTB1ZZ-WzpYsLTu3ngPv_5BHmAWQjSVodDlbAVnmzDZ7cmXz7MvZtdCFWuiD0gLFvW_UgTB3iMvLusC9hlfHy6s_zZFGVIuSku6cpfIh8qSeytMApbkL6reSeMJ57xf-3UORekk3QThgVUX8jF08QqTTmM-BV8QS07YqFaNBB86CfOUoPbIhzAbGh9XCgQGRNLhuhGdPRupU8WfNRpQp2xjUhEiviFhHobINBct8ITWelCk5QgOYh_ZFo--7nqmFLmiulsMBcZf5E4abqNymiMYILchJtcR4C7--VXd5fOSwt9WAgwhcDr1r4KLxZa3jbIEaYKK5UbNGEmj96o85PhGGQsd3p31EIlUCbZEvATQ6tNHpZ0iz-hPbisZrV2plSr3p0ciww4_uzlCO_UHb43z3T4TXJkVx4HFF_YtiN4OFLEEMQWhjZxaHlIvN3xr0z1foC2ZJGZLmJY8E-vZGhkAY8BkoR155XFW5O1ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان اصفهانی روز اول مدرسه را با یاد شهدا آغاز کردند
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/463853" target="_blank">📅 13:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بیش از ۲ هزار استاد دانشگاه: راه علاج مشکلات کشور، شکوفاسازی ظرفیت‌های ملی است
🔹
بیانیۀ ۲۲۹۲ استاد برجستۀ دانشگاه‌های کشور به‌مناسبت آغاز سال تحصیلی: آنچه برای دشمن و نظام سلطه جهانی غیرقابل تحمل است، پیشرفت ایران و الهام‌بخشی آن برای کشورهای عقب‌نگهداشته‌شده جهان است.
🔹
آیندۀ ایران با شکوفاسازی ظرفیت‌های وسیع ملی روشن است؛ باید از توان علمی، انسانی و فناورانه کشور برای ساختن ایرانی پیشرفته‌تر بهره گرفت.
🔹
راه علاج مشکلات کشور، شکوفاسازی ظرفیت‌های وسیع ملی، توسعه علم و فناوری و تبدیل توان علمی ایران به قدرت و توانایی در عرصه‌های مختلف است.
🔹
رمز موفقیت ملت ایران در برابر تهدیدها، نقش‌آفرینی به هنگام، وسیع، آگاهانه و منسجم آحاد مردم با گرایش‌های مختلف است.
🔹
حفظ انسجام و وحدت اجتماعی و پرهیز از شکاف‌های اختلاف‌برانگیز، می‌تواند زمینه‌ساز نقش‌آفرینی مؤثرتر مردم در مسیر پیشرفت ایران باشد.
🔗
متن کامل بیانیه و اسامی امضاکنندگان را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/463852" target="_blank">📅 13:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463850">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzfxcXrX6Rh3jExyf1Xnsh-joUn1sd-_MrtoMpTZzj-KT3WtidDLgb4nudDNv5S0k37sxSjHputG07CFsciMc3Hd2qDhZ5fnmO8I16LHIEAxcCh2163Xq8k5S2ie7OlYNiyRFsRo46fc1PontQhEKU2-Wp6BlYjqsps3izZV0CWfN8CNV6YBroEldlHnOm1N2vTWklee4PrLhhneytUn_ovt69AHuyjuT-hz3i2W4A8oliu24t2hUm9P8_J4dJITcO_leeF4dVF-INy8lIL6BacnrI3yHB0dqsefwXcagdlrTKQIf0NP_V7rehMjT7LYtFHjqch2Z5JHml4kUbY_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را سبز تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۹ هزار واحدی به ۷ میلیون و ۲۵۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/463850" target="_blank">📅 12:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQllPuXkXtAIEBAkBdtA4WS9EsShxAB_prNG_vPs5I87TmXh_fc4et_AUUfEp963X6xN-UXGKFGb48EezH0mpfrnHAeYHG7oIeehG-HWmHCXR0wJN8pq3RQ8l_S9VeFF2tIiWRUYRPu_D5JJDlwKbWVaVTHDs1BNCUjJ0IFqovvm4zufcTHsx34Jz9hXroIPs5-YJ1zcAD8ehm7b2gEteCHkQja7HyE4E2uhDWyKSL7AShLB69FPqAXhycIqiNnli0mtjUxEonWgjm1_uF8gavs9qiMviBrIdvrG5WZhmgWuqnwEnC3uEnhMYJR6jtzWe9LGTXnWO5xybTsHz1VSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تأثیر قطعی پایهٔ یازدهم در کنکور ۱۴۰۶ پابرجاست
🔹
دبیر ستاد علم‌وفناوری شورای‌عالی انقلاب فرهنگی: درحال‌حاضر، تأثیر پایهٔ یازدهم برای کنکور سال ۱۴۰۶ قطعی است و شورا مصمم است مصوبهٔ موجود را تغییر ندهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/463848" target="_blank">📅 12:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97bdd86324.mp4?token=JdufpnIRT7ik5KKqusDQVh2qGeSbDJ3z_tyvo1VCd2Pg8HJ5cgZ9JhsFgO7fIh6-rdYbfzzIp2rpUApBfygJCipiRynm0OfYwaf7KiKEyN5y-ngL8J8k2rMVQkw5CrErG-JiaYdSa6mcf-rcHJTkYCfmTQrxzACRuV8pEkAPUmvKtpXlE4MxacHt3k1W3l-7hpTv4q4_zt6TdnGG_GmL5j2bh47iscJHIq6uO4Sf9jpr08elxmtcOq94bcTbQhwAEjRD8kAXGCh1yRXsyoCh_xrB9c64YJQjRmjQGsRCfo938Eu90aD-9OhVFcaKVwziiPXKRRWc22wAaOAXaosXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97bdd86324.mp4?token=JdufpnIRT7ik5KKqusDQVh2qGeSbDJ3z_tyvo1VCd2Pg8HJ5cgZ9JhsFgO7fIh6-rdYbfzzIp2rpUApBfygJCipiRynm0OfYwaf7KiKEyN5y-ngL8J8k2rMVQkw5CrErG-JiaYdSa6mcf-rcHJTkYCfmTQrxzACRuV8pEkAPUmvKtpXlE4MxacHt3k1W3l-7hpTv4q4_zt6TdnGG_GmL5j2bh47iscJHIq6uO4Sf9jpr08elxmtcOq94bcTbQhwAEjRD8kAXGCh1yRXsyoCh_xrB9c64YJQjRmjQGsRCfo938Eu90aD-9OhVFcaKVwziiPXKRRWc22wAaOAXaosXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربستان در پلی‌استیشن هم حریف ایران نشد
🔹
در رقابت‌های بازی‌های آسیایی ورزش‌های الکترونیک، ابوالفضل آقایی‌نسب از ایران در رشتۀ eFootball Mobile امجد عثمان از عربستان سعودی را ۳ بر صفر شکست داد.
🔹
حسن پاجانی هم در رشتۀ eFootball PC عبدالعزیز فلاح از عربستان…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/463847" target="_blank">📅 12:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9BUUHsNXF0sTIJ3JTuxhGrwhC7K7l0vQAU2rf5KQBRtfoogvQKFZawKlja07TxnNmGBx2KSZZMW1yEjzrfzajdl0o6gMOZSImfB12JMIV5gKhbHkHaYaMeHzJf1jK9CRhbYi6NcdaS-vGejYrR2rn8g2buL8ujUrsVjfOx68SgxeRXW3XEeCVl9SIPJe46FLLw_oDMvV5feYMaEjXbkunKWD40VArLXAAIkpAtIq5GHQYE1GQ9ZkIhBASpv6SvVso2pz6784MQuZb-lQwqFu_PZZgcB8EH6RFF82grBDHVE_DLv5Ck0-S5EdxziIgw-i0XRBa7U9SAwJ0fNcMM-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
‌پزشکیان وارد نیویورک شد
🔹
رئیس‌جمهور دقایقی پیش به‌منظور شرکت در نشست مجمع عمومی سازمان ملل متحد، وارد نیویورک شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463846" target="_blank">📅 12:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb61ac5a3.mp4?token=P0tP7euwursbr6F_1eblAvMcsksLDKSuTJbGB3Ab8yEYryvUB_H7HUmf-O3-lLZ6M0zheaeo8OHQq_2WC8vbdgUM5upRlLBBVZ_NxcCDYcR_bw264zKSobvIfGAWGbDfOfRrI1amslYQVgDq2OSDJVcGUOtW9H6YATvpHhESXxPU8C0cQmRxfI2PHz4MoAN_wL3e5izXkCTT2716VWGZ8kLEinvniwXukliGmAvqmirWEUCDe8-SBTSxFFnNlozBXrpvaDPFirdt-fip_HYWSp4F5cViDyiATihMnjXF_IHhZLvsHKYqarrHUgKq0G7YJPFbJ4-hBdUZSJ8cWWwkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb61ac5a3.mp4?token=P0tP7euwursbr6F_1eblAvMcsksLDKSuTJbGB3Ab8yEYryvUB_H7HUmf-O3-lLZ6M0zheaeo8OHQq_2WC8vbdgUM5upRlLBBVZ_NxcCDYcR_bw264zKSobvIfGAWGbDfOfRrI1amslYQVgDq2OSDJVcGUOtW9H6YATvpHhESXxPU8C0cQmRxfI2PHz4MoAN_wL3e5izXkCTT2716VWGZ8kLEinvniwXukliGmAvqmirWEUCDe8-SBTSxFFnNlozBXrpvaDPFirdt-fip_HYWSp4F5cViDyiATihMnjXF_IHhZLvsHKYqarrHUgKq0G7YJPFbJ4-hBdUZSJ8cWWwkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم قم در مراسم تشییع پیکر آیت‌الله شبیری زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/463844" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSiX4_7sHFlxgFvTvXMo5ZUpPzkG6kPtcIXVjPLxuc-CvXYm9zC9p6bNDkbbLcOb2zoV1KUsnj2Bd_49UGfZuHMekhB_VNFoO-LdUFILsLXrhMQLXzvJ775eBdtzsOfbBqVQASxC6wTwJvwE7zYMjyTT5Gz0SQdx2yCib40s7LQpCiUoEKVP8RkMj0SkUANBfY0uhJ2n1Lbp68hpayMwL2Wc47w9yvOQaXeSt-Ui9InnajjB4a3VkjkemD8x4BpYdDyG8v9DAPE1ekYJwi2TmHJcB3wgzoMUHW92EyDd-YlhZgsKFOsdnGo-kMs1OzdBgpO-hmWgSqjdslNT7pQQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایه شرمساری و تحقیر ملی»؛ توصیف مقام سابق آمریکا از ترامپ
🔹
«بیل کریستول»، رئیس دفتر معاون رئیس‌جمهور در دولت جورج بوش پدر، در واکنش به سخنرانی دونالد ترامپ در مجمع عمومی سازمان ملل، در شبکه اجتماعی ایکس نوشت: «تماشای سخنرانی امروز ترامپ در سازمان ملل برای من عمیقاً افسرده‌کننده بود. اینکه او رئیس‌جمهور ماست، مایه شرمساری و تحقیر ملی است.»
🔹
کریستول در ادامه گفت: «هر کشوری در جهان، چه دوست و چه دشمن، می‌بیند که ما زیر سلطهٔ یک خودشیفتهٔ ابله هستیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/463843" target="_blank">📅 11:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69749884d3.mp4?token=fzGHLSpbXXn2WuB8bYlzL_-uWRog8wDMlaUGZpedCpFZTAdp4FaXQh_mK0f0Y7rG5pCoZvnO0xce7hHf5ithIOnF1Hl35IhP1OWZNJn-SUIeSysLqSeYIytt1HmBSMX7oWout58Abfgk8zEXO2AL3-RLcd5ay_RfyduUFpXYr5DF-_WomjbXI-ptGi-eaRX5Hyq1UmpgF3LrGaUZMVzl1m7PcRJv9fu6GeCLyuqogKoZ1cnSSVM_D58D_1oNqXElcUEAjdTAaV-olmufqsVlcy_Mv8JIBBqxz6ETeCj86OfMol6Rb9UCZh-YeV3rMh1nujCQxxL7mnV306Lw_ynZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69749884d3.mp4?token=fzGHLSpbXXn2WuB8bYlzL_-uWRog8wDMlaUGZpedCpFZTAdp4FaXQh_mK0f0Y7rG5pCoZvnO0xce7hHf5ithIOnF1Hl35IhP1OWZNJn-SUIeSysLqSeYIytt1HmBSMX7oWout58Abfgk8zEXO2AL3-RLcd5ay_RfyduUFpXYr5DF-_WomjbXI-ptGi-eaRX5Hyq1UmpgF3LrGaUZMVzl1m7PcRJv9fu6GeCLyuqogKoZ1cnSSVM_D58D_1oNqXElcUEAjdTAaV-olmufqsVlcy_Mv8JIBBqxz6ETeCj86OfMol6Rb9UCZh-YeV3rMh1nujCQxxL7mnV306Lw_ynZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون کاراته: به مردم بدهکار بودیم
🔹
رهنما: ما می‌توانستیم مدال‌های بیشتری کسب کنیم. به بچه‌ها گفتم که به مردم بدهکار هستیم و باید در این شرایط دل مردم را شاد کنیم.
🔹
مدال کاتای تیمی خیلی خوب بود و مشخص کرد که ما در کار تیمی نیز موفق هستیم. فکر می‌کنم…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/463841" target="_blank">📅 11:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3QCojSHuEGq2qWvoCZYuqvSra5Wy1a_qeYKifdrxFs33oK8227u6topUyFr3PunLoKKWGl0ohiM176IJ_ZEamDCOxbuBGW-xvLsWQXLMvBYFQU1Ort6cDBk1NauGRU4o9aYfUu9alUoNy8julmDc7zBM0dkWc0IGvMX4gIiMB9Vd7Fnjpvi-O1dsR5vdWY86f05OqIHTwIN-Lbof6f3e_dO7qYjUZ4pdmmC9hUpa4-ch4b77x-QDIZ7302COTBFIMcLlWLhL1y1DZya31q4Lxo_nAVLWX3PpYilyooiKV8zS3Vs6OLVZ_qQndByBY6QQ0U3KwT1oiSIYfPt_oh_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-rdPW4ccLoJ2s1n-oml01ka_j6QOO15hF2HQdja_j01O-zZkBkl39O6oFj8z8xzoxmx0RfpAdcVYktMeE_YYktOXLuHhtYZjRtkqHJSWaG3HqySwzR-OUyy01Lx-wzGDQuUNBUbnmGhB3x5T6tktZpmnxPK4XoJw2_14Fze2iIKt71GYlHjsN5vTy9F5yCdbuL5A6kANt27GQs6BUAlBreih5_2NkPM6fl5EiX_8f1KiXovGdvTPOKSUvqQzejVeSxukchqB72RZNYPU7nO1Fup3dFBOVQCFIfy4WSzQUwdWANC6AKmsQSG9B74Lwmkgj7IpfD1rL4tAuOOq5qQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVC2TsCD1k1oQu2iVa_2AcX209jSAAoMul1xK8r16yqoBbtvjxTxGTGjKU1Pn3Tw8HFfqWP7MDnY2-B9UtgsB9zhO15ASASwNplcURz5XusCahwIpe0ebnciqiYOzMYjUI-HXrm_eBXAdcQpcaQOmptCXQBvI-O4aoG8wLsi7lcOTvHSFNPyjS2ZUAOZpFu2Ahgrku-SLOT1eFqNqIxoU-7-ts47xd5LGc_egqeLRdEEfl6GKxio-_MmclhLN9q9944dWi0TSbWhhOfechBQIuxbGnRSz_0YlTPmpOA3spfh1phv-9wesWleXsWvMvm0BXyzRzngAPfYvY83zKJLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kc5jKZRZ32E7QcZO7AURPR2HFBo2V6K1ijNhZIBUEKBEejdWd6sGtE5qQshG8gBy5uNSJYKvSZh6-u8mIpBq3rl0c7NhhW8u9dpIJWIZxvaaqdC-xC0xGdWR5daYvGoCBiKgFQu_BeQNMD2GhzuRjebEIWwba85bJpIVD0OG2tl0Shr25LrmUnl4Z3jQTFW7qcMIxo0s6_CGedUsu3JsjyNvvnki5horkXHLOLD3ZbGk4mvPQaea1qmzTnypU2hEsnKfaflaICmcO_ii5K4dGo8hQfGeYvh6V5nPy600XQ4s_NdrY-MLkd5XBn1kHzTAxC8qnnyhJD2i2i8bvGYzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSnArEutFdGp8_2jk7mxxEqW-Kry_1DlGHmxPR9xESnQBVnpaCwHEmHjvy8nkrzN43MmXIVJ2wKcO0mqw7p_EvL_jOh_08WjKzlq8noa3Znhne_uWBb3pHadig-919Iax-BuVE_VqNkkDARnMeu6qoV3LcR3iGq03hE3k4hNoYHjGUBI7TRtsnL2UL8EMZ02S_plAK3QaShFfiMthFmrgh8myjVAcmJtIf0eOFTcyW_XjRefFjgxrlZWqPAnb3IyQfW9jyNX1kpANUwa4yEAWAO6S4NKX9AODSXvXSjUx9e_HpZ5wbK04aPxr_TdZMNIIMBrj8ohWeNUXW6PiK9CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcK_eO2oJl9XRmrz7EIQLVimzzFBaGD5KLBYHe257aW5VK3URZ67uguarn_mYJels20pd4n9M0PEQJ_hZbov9FGpr_cql0fGdTi4tSMO7a_vbjxE6vJogWBn4ao0QFMg8CjzZ-O-j09K9MkUfbNzozb2_3F7XAAey2x9tNP_RHoexiKIaRqT4j2cHozLnZjRFaDmOdjsjQDi06gaEq4zlqb1jn_2CKO9989Fn4N8ikn88lpxNl0XbbQ4vvjfHcL4w5biAVvFWayCIv_0kOx0kUqW7E-OsbMEaAEUG03n42MAKc06z4s_oD582g0F2-iezqEqZFgclSo4r-sC4WsazQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5iixbpT6cB6IdkiphSUbBBghTHYuNXel-Y4slAiMo37zoYsfiC-05ejhcdLxHBIWowJw7njt1OviIsPVw0mVDye3lvSt1S_agwcF12jQWdreA8_s-e23HieCmV9-cHe7GpU7QaOrLSUueXeEx85XK6ALTKPt2dlgVmdqswE8bCtLMdCmiPn2sSA8SEERiasNhmsVkJ9BjZ4DPLW7_enxZ3SGTLBrqEha-U3nYiuNqtwS95uLwGYMBN_DWpHHKURLa6fS5FYTFglLG7VflmbtCSGdcPZmry2oq2Z-NEBEdbaTJaG5258Etg51EBvT-R5iMS89YQp5F36tt-cAPQKRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باز آمد بوی ماه مدرسه
🔹
مراسم نواختن زنگ آغاز سال تحصیلی ۱ مهر با حضور معاون اول رئیس‌جمهور در دبستان دخترانه شهید بهزادی برگزار شد.
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/463834" target="_blank">📅 11:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa88be9b77.mp4?token=oybHSl3GKFtrBS4OzNOkGLZ_ruNisnezZ1OUbwCkDzRA15kYV2ZZ9edAAGQOVXykDfuaKefcg4nxRvyVCEdGnIusng2lq0vabN6C8uPDLmvSrcCdLo5Pt7FEM-C5LgmNREM0lEsJ5zroD7MspoVYpaYe0_T35A9aNpvuE1B25h8JRxD0KthWohDgCklm6rwKMUKTqQ6wwMZcF3DBQvop8rw1Xw0kv5enHabOyXQmLMVobnQeRmtKkxtDSx2x4xFabyiZ0VzuFUVxFlNRDm_OItk1Xtg5SlxrDknStRp7wIDgeBiTdZNsA8w1XggjfIy9pvDBna6udH3OpNibLxx1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa88be9b77.mp4?token=oybHSl3GKFtrBS4OzNOkGLZ_ruNisnezZ1OUbwCkDzRA15kYV2ZZ9edAAGQOVXykDfuaKefcg4nxRvyVCEdGnIusng2lq0vabN6C8uPDLmvSrcCdLo5Pt7FEM-C5LgmNREM0lEsJ5zroD7MspoVYpaYe0_T35A9aNpvuE1B25h8JRxD0KthWohDgCklm6rwKMUKTqQ6wwMZcF3DBQvop8rw1Xw0kv5enHabOyXQmLMVobnQeRmtKkxtDSx2x4xFabyiZ0VzuFUVxFlNRDm_OItk1Xtg5SlxrDknStRp7wIDgeBiTdZNsA8w1XggjfIy9pvDBna6udH3OpNibLxx1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم کرۀشمالی به ایران
⚽️
ایران ۱ - ۴ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/463833" target="_blank">📅 10:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463832">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7452c31cae.mp4?token=X91NCwhxclIDbnOf3B9aFVlapHWv4te9sQKEgyyxVg_rsSmUd_UqjyfwS0IXZHPNbRRpsg5A_J3yqxxA6QjOBoL0Oml0OylNTa9PY96q7X3c43a0tg4kM8QPFPFIGlorefewjvCeqAqmzRrdBZESH7LZCRwZBrL9Q2jL_4Yc-S5dhKBktb66gCxZAVylM9JZzieoAjrLH85veYgH5QpY81SsZm3KVLCcOHeeYbTvJ4uc5SdgbnWOaIpT08R2jzT-A6_7GzQLSqaiD-mJTznOqvNB6E2JJrkOnwc-z8DyI3NLwDGSJJmwpjw0leH5qq-73L3LR6WakThyBHPxlllXnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7452c31cae.mp4?token=X91NCwhxclIDbnOf3B9aFVlapHWv4te9sQKEgyyxVg_rsSmUd_UqjyfwS0IXZHPNbRRpsg5A_J3yqxxA6QjOBoL0Oml0OylNTa9PY96q7X3c43a0tg4kM8QPFPFIGlorefewjvCeqAqmzRrdBZESH7LZCRwZBrL9Q2jL_4Yc-S5dhKBktb66gCxZAVylM9JZzieoAjrLH85veYgH5QpY81SsZm3KVLCcOHeeYbTvJ4uc5SdgbnWOaIpT08R2jzT-A6_7GzQLSqaiD-mJTznOqvNB6E2JJrkOnwc-z8DyI3NLwDGSJJmwpjw0leH5qq-73L3LR6WakThyBHPxlllXnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم قم در مراسم تشییع پیکر آیت‌الله شبیری زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/463832" target="_blank">📅 10:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76403b064e.mp4?token=Tw7d21EEWvw1j5kYOqL9BkfDPkUvcwZ2dho-AVAtYX6f7MXNRQNZetcS1qNRNoRnlHx8Hn7g7TCQdVSVq1lxbPkXbZPf5Pt1o4hf61EEB59NAkay2Xy1tSCUf_1GPhcUlJ4BSLwxdDDIbltUBZ-WXn9o_vnMz0YjO63FI2IF0zGadRDOC_g2ukD1MtcL3XEAjmYU1CGpV5EaFg3vp9elSAUn5aNFcSQb3PYHbAT1ExE99X3kDr6PUL11o9RZ42MnzuDZJZMpZuBEi4EUhZTcWU3uBj0QFrZDyK3axhZS07zr_HD1XiNE922YpEV38epcyG3AJFemrzkWCjnb4jsWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76403b064e.mp4?token=Tw7d21EEWvw1j5kYOqL9BkfDPkUvcwZ2dho-AVAtYX6f7MXNRQNZetcS1qNRNoRnlHx8Hn7g7TCQdVSVq1lxbPkXbZPf5Pt1o4hf61EEB59NAkay2Xy1tSCUf_1GPhcUlJ4BSLwxdDDIbltUBZ-WXn9o_vnMz0YjO63FI2IF0zGadRDOC_g2ukD1MtcL3XEAjmYU1CGpV5EaFg3vp9elSAUn5aNFcSQb3PYHbAT1ExE99X3kDr6PUL11o9RZ42MnzuDZJZMpZuBEi4EUhZTcWU3uBj0QFrZDyK3axhZS07zr_HD1XiNE922YpEV38epcyG3AJFemrzkWCjnb4jsWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ برادر و ۲ طلا برای ایران
🔹
محمود نعمتی در فینال وزن ۸۴+ کیلو کاراته، برابر صوفیانی از عربستان ۶-۳ به برتری رسید و مدال طلا را از آن خود کرد.
🔸
دیروز هم اولین مدال طلای کاروان ایران را مرتضی نعمتی، برادر بزرگ‌تر محمود کسب کرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463831" target="_blank">📅 10:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5hGeJByN84WcmSWOfc04BkuQ2hEmgHcMLK_yKXUc6dziBuxOWDagG2LtrtMwOoXDHtDd4IerMubVJXr6p8t21jUkkdbGtMqCScKLsmgCR680pXy7vJFQboRDbbLm2ZCSdkKFL6xDv1WZibU3m9MmqYwJ2Hmc6iVinUnElpjOy371BCUKnFZv6WzHUXcTutcPPItRMtosCcmFFTGQYdlqGoxAJksesGKDSgq8E3p8DRXmIgPaJVvjOVGZAS_1FTpYAZZbmmsy8UnybSh5DZ78xRvZypIrMpS5qitsDVbGd99ho4obOuaWnQJoo2i5DjosqqWjGk73E5-yBDo4Ie6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMJ5YEUx_h5Y3AGAFTwDhjOqCBXKsIgwLoBBETeQaynMmKRG4rMpIdsDpJ36GB5TTJ7EHuB7rGXwl6HxMgZTBu_Q8gZ7wi5Ggi9dwGu7cxcx1XI1MXuyDcgh4lJYwZQfu32iU1wYvmQU18hdKhbO7H55b-qIzvukqpZSRWswV5vd3zlMw3WPgJ8uBQsFf0q_Ml04gJyqUocF3JHExFm7KTYtjbZUULJvUKTbpRrLRJ0VFezq6oxl17DaW18Hv8nL5IEq4ubafKKeko6mPD6iUXHnBRNR-RXUjbq-tLqRkUr5CTHeanrgthDRIDJeFCTHPVWBIY1NQYYIgx7uYQdNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl4lT2dSUJlgIF3FLaihmgGoDHBESu0vmJ9c2thevzJugIh8Uk9W7jK3rctv063Dhf4SOVMCR91EoFOKyNd1FYTJNLvW-LKwlLZ-ZGrLgRCOIx_ylICYumcuIwnzTHKxqrUCIjDrsLYh54iGjrPaB9NwQNhI6h3QQzkpXlCSyZ_gJ0j0iurSg3c5tiGYeEPzAnNKOJxNEZ1Zcz7aHiLebseM_ubkRKZgICwtO8XPvLHUUCeNIBc9I6BbJnw0yF5KqCRf_qsa4atLEtlqPCqDDD_1Y3wa9TEnJ4rwBhMwPrjiDiY1KahbgFbCMubVARvzTB-Adwt4yyp6SFeUJbq5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ud7_r-0S4SuhR6pNkHAZWsR4dcf6tqB3zNtw79YlXPHXWawfmU13ulflziM5IWg6h_axQ1ncX1e3bF7-704flTygWoBhSMhhjtWAYQ9FLxD3Awx3BdWGI1po-4Ho7c7DY_r4vjMB2Pdcreot34KV5J388fka9cR9-5J_8-8OlCern9AVNjcTEPoz6mBeqsS4cCcp6mgwdcAflkh697FE6PjPRmpHgc6vA7Z76J86Zx1jNbKxU5zbeKe7YQUvSA__-RPc4ruqNKcTM_REb7YqQUABevAAtpc2kh01QBv9bE1ShaAtpS04pTWu7Ihq9RToavAMjBHNZBbBQA_UDD0g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q606KNr0GEDENM86Pr6n0FfGyYAE8wnE5EXOQF4G9ltb1OGiQke5NrAxHtH-diaWCCksXYGU0Zy65caPQ0xljRifE3w7LrmbXOHT5mxLpZ3V4PaquX1LqBWDXmGnYUd9ncg2xQ4vchUQjezRRkfK-2D_67XCOHCf6jpyzUq1JVDnUtqen283V6BPnvIizkPYYwliyO81kJFJ8WGtaovKbyQq5E7e4Y-1tv0J7g03WEpKRZa1RCwH-0A1FxBWvFzCZTFxdNp-XuUM47sv8CpOcQ47MZgO395nIHyA4KwxIOqqAIV9EuCZ1maR4AtMmxJPwZzNrIolWm2ZNpDbGIAOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz79ZWjEq0sGdTKPT1TC4ykyd07swxk2jXtvo3toqSZbhdUSArL31ZfebtnBSX_VJ_pnrFIk8jLQTQ1muNwEY0FPiPEGlYcZ1Qc8qLPHXWkwaRZpHNPN7fxwpwEF8kVV8bgRdweO2iXwVM0xfqa8wVnmPX5EMaQ5k_jXEGByClw0f1rr-McnHnLlplaKp-iLNpGFHBcC8xApo7lcQzVJsLEILTf5MUZtdldRNQYHm4PMXKlNEye52Xh9GzNBGvy_NvbL9utGFk0OgjreRuh_qsgdsY7tUer_WRwws7LpZo85IxH0RnKH5y55kUA2BjXWkzq2gyb9swhidJcvEjBkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5FW3_8FJkeNwBKfddUPHqclf0M4W595F4oxSVaLZCbdEUftUORRZICbfxDTaFS6p6g0rAAX7cK2jvr4V1X7_AGUk1FV1-b4SqnHMht0Uc0LoC17R8-rLCvh-YQkh0xDLB2mcfpQwg0t1P2TA5tdVYrbWF8ASt6G3tFGTrLv3pYQz8pUFfZQNWn8qtAaqF3bXvzibVDrDpAHELgP4p_NXkXG-_UEYG3hAKqHuj0R_VXWyE0BrEnF--igduROVNHwJcwvhDmCjH9xpKg-OcSJAZbqhnDgfCRy9IDuB83R6xPU3BpE2on5q8hyoz2eSqWAmyRD_tfbNOhMVlukJzBteg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اول مهر و ۱۶۸ نیمکت خالی
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/463824" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9E1U23QtODOl6H8k4-7EwgXJ3rC6_UCEYY0cVtQ_2SQ69fbG3oyag21J5CvLtVTm_T61-t2B1_OE8KvOs9-Dm3HqQJaDPF-i2mPwv6TPhWj_j492WjPcORs_XonvmJGXoboLlVwbnkBKXEgJ5AZZQUI4BSlHuMSoi30FwxFYQSH15O1QISF6gw336GbpD_zEhm2KMJHvsouN15P10ZhGZN5q9iqA_O4MFeez5kah_CVu8522HOy8h2mOxp3PjEcbMLC_sNWqws3JE1uVDWpoPlmDcdxYof-BR9QuqCAe93nPP-SS_BvE_Rx6UHbkLkdO7xAYtXbrNJFefW2es9Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuHlCr67oGsgGEZE2pDtkBt_RZDDfoXnJUsxFbiB528iWAN-R0TJ9zovHFiH2niOH0fV7RYUb6ZIiseN2Ljo9glqhhF1vKPDmk7ogaDCcHxJTuhlyQMUEj3EUNYfIA33W55t-U22t3Yq6u3o_T6hFFB6eaB9ctXRK3VJ9nTswLxopzJxkUrBha6mhcIv3_Ce0_b1NFKE8cHkwbuH6H9IwbUYD7Yn5vAUFEsGE-73rZC_A1Jik-UxycKDtypLPuGcY9bR1HFeTpFe7gt1DAlaH1Z3_ZMrQFXZmcvj6Q1U0Ufh1-1H6QIkCVilSjQ80h4X8TjNigQgHYhnO3P2sNryXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9Udv9C9n2J8TNI6jrUCIWQTxlrskqQLSzj3hUUb_4BLVUWi80ppzR9H9kNNwnMWvyxN98dr2AZTU20WUGsLen6ekFoJsYyYP5IHyuPzgdiSaJlEqJKbOj-K3Hi3y2d9X3JEqfXZsOI_nrN6V38aGoVLFZ7Bko3nIDdmF1qKZtw9SgTdcBVY2DCrMZL3u2Wm6fNHJ88hBVlcjgSSJPf0-8vraz1FR-ihI9ULFAFkbtqeoDzMdDLU1kiJzQx2gf6_sT01Qelo6SFakvCstOiV5oqF_047o64ic7QaqbRw4klbdINmPK-j30ahspt9ZgCO61K_013VhJY5_pfe1MCIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShvvfrP8j5g-NT8iMGJpfrVfrsmUTM2AMAkoO0IRhiBrZpseBZAzssz0ivd0o2t24Vp1kF1o3-pE1dXVa1Xt07en4VqGss_BWAPG9TPameM7L6nGtT5HXlJg9sKx1SlXN1jCJwpVOjszjn-bDxKHhRhrFUCxvrxdtYDq5rD47qpbPMBLwLmGGAD5XHBskzwQBE1KfUB6zsCAFbg3HzFmpT8jFQdfr8Uo__LlWv6kqr0_QfYMIppS2MRuGgJN2f-M7lQihCcOlyzzR7dM8BerH1kvwDq7KNTqb-0pCX_clXS52ByRofpvQEtavA7r0uJUrhZIx3bgYtpxdRPdOtcnYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید فرمانده نیروی زمینی سپاه از پایگاه‌های عملیاتی مناطق شمال‌غرب
🔹
سردار کرمی: همچون دوران دفاع مقدس در مقابل دشمن ذره‌ای کوتاه نخواهیم آمد. آینده از آن اسلام عزیز و ملت قهرمان ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/463820" target="_blank">📅 10:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dbac331d.mp4?token=MUuJ4ewqi6-btxsqdluCsV5KSdy0pVXrpAbU6myMCne8JUJW3e-MoSm-Gb_ImQou2CEKBh7m9IDFsIUgE3irPWOYQgmk_xglwkKITqlwHUCoX-6OHiD355LMg4VUKrXIeGjJ6IEyNLOJRjLjWxyVQBuEKGTaP1keylOf35_prkepLOLlfgR8FD59Gpd89Kas_bWlEnPSLoJkRElr8izU4TGu7jdJ2HDXHgBavO7nVu4mqtiqoVRE39dz_TAd1HD0Ii6C4fVK_eZDtXBMvnpUELSPKumIjs8RziQ0wUyf8q6izkiAk6JooXf2M9MuNqdANHaY6ZTVc4pl0soqvufE-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dbac331d.mp4?token=MUuJ4ewqi6-btxsqdluCsV5KSdy0pVXrpAbU6myMCne8JUJW3e-MoSm-Gb_ImQou2CEKBh7m9IDFsIUgE3irPWOYQgmk_xglwkKITqlwHUCoX-6OHiD355LMg4VUKrXIeGjJ6IEyNLOJRjLjWxyVQBuEKGTaP1keylOf35_prkepLOLlfgR8FD59Gpd89Kas_bWlEnPSLoJkRElr8izU4TGu7jdJ2HDXHgBavO7nVu4mqtiqoVRE39dz_TAd1HD0Ii6C4fVK_eZDtXBMvnpUELSPKumIjs8RziQ0wUyf8q6izkiAk6JooXf2M9MuNqdANHaY6ZTVc4pl0soqvufE-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم کرۀشمالی به ایران
⚽️
ایران ۱ - ۳ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/463819" target="_blank">📅 10:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77a05b238.mp4?token=c9xMn42CcO2PF_FTZUCXh3UOwBO29IILEMnmsVExWeGoHZSUqXfzHLp6ssZ-fsufzoG5Lqlzz902n2g7jaO9AIV0qZxg9t-7yYJ4nUPG_sQpB1ilo2SL-f1STOEm2WM2n1vq6BzKB_PoIvFW7J03qD0Y_xsVb0s1wRNa28_65h_XVAosDiQbG_mtRqpMr9N-1fmvKjGiUAYOm5E-QkACJ4z76dN3KNc8Tv15lUaVnfmVFjFIa6LVMM3fi54Z4DBI208YZno6qgBF5zx7UKQJWiPsQFc9jjcOnbgc9lJrRz796qSbyI0OsRf54ik1k6aGJ9A8o9YnhqjMGE84rEaxXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77a05b238.mp4?token=c9xMn42CcO2PF_FTZUCXh3UOwBO29IILEMnmsVExWeGoHZSUqXfzHLp6ssZ-fsufzoG5Lqlzz902n2g7jaO9AIV0qZxg9t-7yYJ4nUPG_sQpB1ilo2SL-f1STOEm2WM2n1vq6BzKB_PoIvFW7J03qD0Y_xsVb0s1wRNa28_65h_XVAosDiQbG_mtRqpMr9N-1fmvKjGiUAYOm5E-QkACJ4z76dN3KNc8Tv15lUaVnfmVFjFIa6LVMM3fi54Z4DBI208YZno6qgBF5zx7UKQJWiPsQFc9jjcOnbgc9lJrRz796qSbyI0OsRf54ik1k6aGJ9A8o9YnhqjMGE84rEaxXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم تشییع پیکر آیت‌الله شبیری‌ زنجانی در قم آغاز شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/463817" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30ef874f2.mp4?token=tQC033dJljzcnnkfmNMQtCFDXp3ysWRA7iSpKDEgb3VVco15oqLZbixZ6Z7M75YAW3f4U5kPd5BeHqh98EwBgP2eYexu7_jy--4atKgVxoThUgl2mcdSM4xJQnJww5Ufmg_vizfSv0mkKlMf2gI2GYS5gLE3-lF24uhnVOnCd40I83AWk7RaW8t-CISH7lS7phzLyxTkGg4NdTtSHdz4N7dChj9sP5nXt-KmxKsDbQobxlnzRa8vmehFM0xpo_70pV6zAADP2s8VpsaF1HgKt7WtxRlxfW0zPiNC5guDG49qE1RIYAjqRabio3TteGHRaFg5mCdY3tS_CKfN3-fRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30ef874f2.mp4?token=tQC033dJljzcnnkfmNMQtCFDXp3ysWRA7iSpKDEgb3VVco15oqLZbixZ6Z7M75YAW3f4U5kPd5BeHqh98EwBgP2eYexu7_jy--4atKgVxoThUgl2mcdSM4xJQnJww5Ufmg_vizfSv0mkKlMf2gI2GYS5gLE3-lF24uhnVOnCd40I83AWk7RaW8t-CISH7lS7phzLyxTkGg4NdTtSHdz4N7dChj9sP5nXt-KmxKsDbQobxlnzRa8vmehFM0xpo_70pV6zAADP2s8VpsaF1HgKt7WtxRlxfW0zPiNC5guDG49qE1RIYAjqRabio3TteGHRaFg5mCdY3tS_CKfN3-fRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم کرۀشمالی به ایران
⚽️
ایران ۱ - ۲ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/463816" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2079f800d.mp4?token=I1cS8c57e4cXv8OHhWDATjWrxlvgo6jkoekpE3I7fCsuz5KWQlceZft6uVvl9NEglEUZZRspDhD8C1JnDPFl_EVpDnT70pceETE0I2la1hLT99eJ4nMEf_zzSqFvBdJMIv0Mi4wSiR1dk3Th6ouYNuDhnnjRSl1LAVWqN9sf9KErrtSKdTT9QE9BdDS31ErhYofgVtDrAaHBvMDNXelwE4FD1MFXk1VzQQEZ29H1kCTp_ndFGLUCihcHB89SWZ0OXcDx6yb07oOmbVwDZint_6teyYEQ3dB61eDhWlGrpuG68MuPc4ay25z3pJm_8zLY-CglGUfzbOAze1vLzQtHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2079f800d.mp4?token=I1cS8c57e4cXv8OHhWDATjWrxlvgo6jkoekpE3I7fCsuz5KWQlceZft6uVvl9NEglEUZZRspDhD8C1JnDPFl_EVpDnT70pceETE0I2la1hLT99eJ4nMEf_zzSqFvBdJMIv0Mi4wSiR1dk3Th6ouYNuDhnnjRSl1LAVWqN9sf9KErrtSKdTT9QE9BdDS31ErhYofgVtDrAaHBvMDNXelwE4FD1MFXk1VzQQEZ29H1kCTp_ndFGLUCihcHB89SWZ0OXcDx6yb07oOmbVwDZint_6teyYEQ3dB61eDhWlGrpuG68MuPc4ay25z3pJm_8zLY-CglGUfzbOAze1vLzQtHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگزاری مجلس ترحیم آیت‌الله شبیری از سوی رهبر انقلاب در قم
◾️
مراسم ترحیم آیت‌الله شبیری زنجانی از سوی رهبر معظم انقلاب فردا پس از نماز مغرب و عشاء در حرم حضرت فاطمه معصومه(س) برگزار می‌شود.
◾️
پیکر این مرجع تقلید فردا صبح از میدان جهاد قم به سوی حرم حضرت…</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/463815" target="_blank">📅 09:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d13ec09f5.mp4?token=dcykVxxAfNcrMi5k8GgE3jiNwMpzXd7jtWR2ZD3OZrvE8RR7klu0No3ygL39YampT1bhZ-vZ2qik2p4g6faZhIeY9SrgZDlMZxUzw96wchajdj0emyDtnnKUBi8I70llUWxANRiSRiLgA3cQmyswS_p3HDrX12yzuOQILXTrHj4U754YjxDEfZ8QEyWVjq0D6mKT4ijV8ifs3zfDR3AjywwmIMksIYfICA8bT2427agszmr_mNRLa0oVsTFxw3YEyIoegNzy7x87IHB68rm_yDJynk2b5q2_d6uoY2LNft5FJcV3cnGym8oQ-wYWv1ePevzyKnEGCJ_CqUSZxaTpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d13ec09f5.mp4?token=dcykVxxAfNcrMi5k8GgE3jiNwMpzXd7jtWR2ZD3OZrvE8RR7klu0No3ygL39YampT1bhZ-vZ2qik2p4g6faZhIeY9SrgZDlMZxUzw96wchajdj0emyDtnnKUBi8I70llUWxANRiSRiLgA3cQmyswS_p3HDrX12yzuOQILXTrHj4U754YjxDEfZ8QEyWVjq0D6mKT4ijV8ifs3zfDR3AjywwmIMksIYfICA8bT2427agszmr_mNRLa0oVsTFxw3YEyIoegNzy7x87IHB68rm_yDJynk2b5q2_d6uoY2LNft5FJcV3cnGym8oQ-wYWv1ePevzyKnEGCJ_CqUSZxaTpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/463814" target="_blank">📅 09:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463813">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144d3e014f.mp4?token=eCstM7Q4bQO_WucTGGpkNJHymhCOQUGtMY4r5qXO9PXWQVHi-omVAY7lemXXVFnXt9wsKBp451LbxooM0GH_jJVQJF9tNMI3DEj6xbylYjBYgZ_FDVEKFlCwBZpwHTRnlY_Tq4kJpK1bZaKc2XV_Go3LkRBj_BdeyecbPJXq2z2Tf4tEDkA9TJxZ6IW0xMhTGa-v82vftdmD29ZbvIvw90PqW0j83OFli6ntSw-7mEUZbYkyn6-rAhT8Q9EVM_y6yoWEh0A2AgR-Ua0NETiiJUddLg2fWep8DGMcuiW1BwGS_wnrLgu4JAPCyYcHZnbSLGhqTPBMcj5BTy5KP_d_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144d3e014f.mp4?token=eCstM7Q4bQO_WucTGGpkNJHymhCOQUGtMY4r5qXO9PXWQVHi-omVAY7lemXXVFnXt9wsKBp451LbxooM0GH_jJVQJF9tNMI3DEj6xbylYjBYgZ_FDVEKFlCwBZpwHTRnlY_Tq4kJpK1bZaKc2XV_Go3LkRBj_BdeyecbPJXq2z2Tf4tEDkA9TJxZ6IW0xMhTGa-v82vftdmD29ZbvIvw90PqW0j83OFli6ntSw-7mEUZbYkyn6-rAhT8Q9EVM_y6yoWEh0A2AgR-Ua0NETiiJUddLg2fWep8DGMcuiW1BwGS_wnrLgu4JAPCyYcHZnbSLGhqTPBMcj5BTy5KP_d_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول کرۀشمالی به ایران
⚽️
ایران ۱ - ۱ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/463813" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463812">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMgo3fpdtBjQSkl2J4zwTBmZQc9NS7tOAqygsFPRUzY2FpAVIow0xUYPIESYJaaKHUaJTrAJDEaXWAYaO99zeLuMdGQVUd6iEUeGzuPWPMOaoqJ02y5rXDXHRWT--HKN-BLnmMJkoIlVLOFP-QCX4BxAbvPv1HPypsUnyL5qSjqrjVyH0rWgRlSJkx6WZVq5l4oXpGdxpU2URZ3FQuPkq6_uw8XwMFGuPIEgfCJq05CUka7_jtfuHGOdemAzSLg1h_aLbcqtjM6VoLZ2LPdfA7lZMqak4Z5Advs9h6XbdLcwvsk0q5fQN8Cr-I0IbVWj_W2FVlFrFOX2jFgtzkPRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دانش‌آموزان مشهدی سال تحصیلی را در جوار رهبر شهید آغاز کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/463812" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463811">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e623abd6.mp4?token=eUuiItrA8lUY2y18RCcAY2cQOibo2v3lekzLVyDmFmgOBWCUeYlXsjEDVw2SAyg_WdT0Vh1-pdBT0RGfyBON58Fb4wW6J2B-wlskEEBXcQrZ-iQ1sXXb2XeAQ-SCgDKKYcg6RKalk_jjWEs5yNTLukOnHG0V0YwQ_rBuflKDQ-8UtnPFsSIF2vVAIjY1_aAQ-dKbp_Gui_-5HG4LsXH1NvII7O-MuHf2BfbMNH-jzNSz_33WWemL7xdnKOetBawpzcNjDpOvNi2cQGF6ckyOO3WDjYz5ZY8cJtluBG-t1qGDXXlkpoZdZTcT2WhOlbYVrswtpGwnHdoS6H2M5PdBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e623abd6.mp4?token=eUuiItrA8lUY2y18RCcAY2cQOibo2v3lekzLVyDmFmgOBWCUeYlXsjEDVw2SAyg_WdT0Vh1-pdBT0RGfyBON58Fb4wW6J2B-wlskEEBXcQrZ-iQ1sXXb2XeAQ-SCgDKKYcg6RKalk_jjWEs5yNTLukOnHG0V0YwQ_rBuflKDQ-8UtnPFsSIF2vVAIjY1_aAQ-dKbp_Gui_-5HG4LsXH1NvII7O-MuHf2BfbMNH-jzNSz_33WWemL7xdnKOetBawpzcNjDpOvNi2cQGF6ckyOO3WDjYz5ZY8cJtluBG-t1qGDXXlkpoZdZTcT2WhOlbYVrswtpGwnHdoS6H2M5PdBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران به کرۀشمالی توسط حسین‌زاده
⚽️
ایران ۱ - ۰ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463811" target="_blank">📅 09:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463810">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-qGnUtGuY3_CNROsqGEEqRJSZ2RrFPqqT7FvtK_muNwrW71rg0sVfLbprN6QuiEnlunsm0eSlKurhvg32mNAP4qAnJp8tOIm0nYHFjaXYzBT6D8JypvOZiY_cU5xBumvUEjhpKn2-AWzqwBM6oOHoFaHVkBFoEvN-Xnme7O6VWhHG91Z4i-AZalwjLgcDWkVjezoS1RiPtVQAwkBGbDLvUgowos09-b8s1GOhLg0hCzA8obByxPSZCBSHmKuWkGVTfp3AkWyY6ZJ9vzU_UzGynUEgwVVgxgRP3V7BCZD18JFeQi-T-WZIUwvam07Z5n9EfZ9c4McmgOtnGP7qn4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/463810" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjSAqDELf2b6tL-P_t03xP8m-XFZQ_1ABFtOuhgGJrMQXieIHR-3GMXxchzQo8f_DFUwixptd53f_HCpWBmJoxxrjd_C7_s15GN7SwCKOPQbnKTaLDRHpjYFC2WozbelG4Q52AKtGs9Y-ccQTir00jbCA1rFHqhsEC2V6XwsByU77HK3JeFGgtI8_8eBb0z7Ar1wPUJQaI-TiTOat01J7pmNCohQGVW_0LhRuLDpCOVtL0K9rpNnhXSF9yYz2SMZRO6ccnUQ3Jw_6t3MhToUUZBRhRNrL9yPYbPVSMEtBPsfgab0OZgfHCQMoDQTxqPue5zmfSq4A8J3C0yw4x55xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد ۱۲۳ مگاواتی آسیب‌دیده از جنگ به مدار بازگشت  مدیرعامل شرکت تعمیرات نیروگاهی ایران: واحد گازی ۱۲۳ مگاواتی G15 نیروگاه مبین انرژی در منطقهٔ پارس جنوبی که در جنگ تحمیلی دوم دچار آسیب‌های شدید شده بود، به‌چرخهٔ تولید بازگشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/463808" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463807">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a51315c2.mp4?token=icYkzxa195NQ5duuaNy6LTwpJOtTLOqmhzhgDU4TyQSFQmtfolHy-OfDBXI3vHUZWHCiyRlXTUqAUERIoqln0zLPDkksQDNz3XTUeQifKy_iY8Vaq-h3vIpAB6-Mmmof8DZPN1kd6NeqtPxQk1j19s2uNR7d4MEn6drpQQjW6WWJ1XuDPrpQGHiTyuG6ArJGOuDfpYRryRLeJAilKo3XRK4YJNh-ai_Z7NTaEpCJwboKkYzM73Ta0b2Ovy09GU2fRToBfmDhVaCfbl2CCChmV6qwYEK_FMIjW9HjovZHdV1AnXS1fyokbemrTO98vVPBL78YXj8Nye-wrSfYyueVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a51315c2.mp4?token=icYkzxa195NQ5duuaNy6LTwpJOtTLOqmhzhgDU4TyQSFQmtfolHy-OfDBXI3vHUZWHCiyRlXTUqAUERIoqln0zLPDkksQDNz3XTUeQifKy_iY8Vaq-h3vIpAB6-Mmmof8DZPN1kd6NeqtPxQk1j19s2uNR7d4MEn6drpQQjW6WWJ1XuDPrpQGHiTyuG6ArJGOuDfpYRryRLeJAilKo3XRK4YJNh-ai_Z7NTaEpCJwboKkYzM73Ta0b2Ovy09GU2fRToBfmDhVaCfbl2CCChmV6qwYEK_FMIjW9HjovZHdV1AnXS1fyokbemrTO98vVPBL78YXj8Nye-wrSfYyueVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود کاروان تیم ملی امید به ورزشگاه محل برگزاری بازی با کرۀشمالی
🔹
تیم ملی امید کشورمان با ترکیب محمد خلیفه، امین حزباوی، دانیال ایری، فرزین معامله‌گری، ابوالفضل کوهی، مبین دهقان، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، یوسف مزرعه، سعید سحرخیزان و کسری طاهری،…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/463807" target="_blank">📅 09:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463806">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulXvs9PqeRplIkhR2Skl0Kxed7aCEyOD7kTM6KM5a9ad_njLO-dZBrxhBjt7KqVANAK-7zprgk2L9A1TQML2-eQCqvhkrzfvYzyv6ajwhtYx7RCdaB-7tUfrHSVU9vMe-DnzuXfWrtUGr2aZ6gXDEkl7udN9iIGKG5MoYL73cvL57l7adljwvq9glqr3YbXtbVEhJj_UVChyQre-2z9XN6_0-PdhP0hRHZDQ4XDZeBI0KwJx-HcqDgtSzdFXyPCBq8QPBRCi1cf9ca1a8Up5jZx3zDFtKLP0TSgtBSJ3largHlZrlIHgPp3ajwGGasM0AUXBbImBhg4SYQ_PFE3anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجریۀ طیبۀ میناب در روز اول مهر
🔹
پس از برگزاری مراسم ملی زنگ بازگشایی مدارس، ۲۴۰ دانش‌آموز دبستان شجریۀ طیبۀ میناب در فضای آموزشی جدید وارد کلاس درس می‌شوند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463806" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463805">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74bda766b5.mp4?token=dWSHtbH6-hVBqJ4J6oeSfdBvUlg1xwNXpqlDCPBCgdWMCD6nab7HTRk-FztmUv6i79r_7yqIQTmNKv3fG4HVCKpp3eUNiZWZnHwoBVt-bBnRHi79VOSSCNgqo2WNoVPH0Srnc3neSilmLnoMvZkUlWFywN1Phfi7oasA5Aca0N-tHyFUKaiGksGE_bZKfYMXM6cjJcWyTYVklffOCbmXaZ7FVRDjHkPoTCr8jBm11hnbJqG_ewoRaMhHjHWv1VMgizkmPoPghD0V8vjix2-iwjDtS6UMC1oBN9DIU122o45WhG5TusNITd8jSZAMcOYT2VevzxlKY2uhbXJE6BVheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74bda766b5.mp4?token=dWSHtbH6-hVBqJ4J6oeSfdBvUlg1xwNXpqlDCPBCgdWMCD6nab7HTRk-FztmUv6i79r_7yqIQTmNKv3fG4HVCKpp3eUNiZWZnHwoBVt-bBnRHi79VOSSCNgqo2WNoVPH0Srnc3neSilmLnoMvZkUlWFywN1Phfi7oasA5Aca0N-tHyFUKaiGksGE_bZKfYMXM6cjJcWyTYVklffOCbmXaZ7FVRDjHkPoTCr8jBm11hnbJqG_ewoRaMhHjHWv1VMgizkmPoPghD0V8vjix2-iwjDtS6UMC1oBN9DIU122o45WhG5TusNITd8jSZAMcOYT2VevzxlKY2uhbXJE6BVheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: تا روز جمعه روند افزایش دما در بیشتر مناطق کشور داریم
🔹
از روز جمعه کاهش نسبی دما اتفاق می‌افتد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463805" target="_blank">📅 08:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463804">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f430bde39.mp4?token=dzGaR2KOkXqsx_UM6NiCPjo6LdXgwvsrz7lDvmZITElGzMd1FPS2HYeMCIT9m4msgpigRYUrdof_udFw4Tmh5JDhJiUkF2dfuh11GI_CLd7zdBblLafJiLLsZbkO_4GzhZpsnvYmXI41dUlKLnNimInoX5Xh4L-ZTIdmUq_U3HMAxK8n987-IIkCx2ktQpzf0mYaor84lsMf5uXrRSPrvH70z9x5LyXrgicRY92qeDLa6ZrlNeQ9rpaNpIxzgtYc_Ff2B_FSb-HuGyYOhgnUqN5lB-Fghbt8r9NBhMgB2hKVZm7hm9rbg2HZayKC9wNqNjwP5TV_Oz2-v4LCyeon7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f430bde39.mp4?token=dzGaR2KOkXqsx_UM6NiCPjo6LdXgwvsrz7lDvmZITElGzMd1FPS2HYeMCIT9m4msgpigRYUrdof_udFw4Tmh5JDhJiUkF2dfuh11GI_CLd7zdBblLafJiLLsZbkO_4GzhZpsnvYmXI41dUlKLnNimInoX5Xh4L-ZTIdmUq_U3HMAxK8n987-IIkCx2ktQpzf0mYaor84lsMf5uXrRSPrvH70z9x5LyXrgicRY92qeDLa6ZrlNeQ9rpaNpIxzgtYc_Ff2B_FSb-HuGyYOhgnUqN5lB-Fghbt8r9NBhMgB2hKVZm7hm9rbg2HZayKC9wNqNjwP5TV_Oz2-v4LCyeon7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجرۀ طیبۀ میناب در اول مهر @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463804" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463803">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318fa54bad.mp4?token=BW4SREg8Vhity3AuDCjFKBIAoOYnRTQIikjhhr45VvAyQtvol8xejvaUcZlkKg7Yj30FjZYXUH5jMWUvwWy4ksFcb6e0MGrX3XFNzLAOnV1dVMB67-lNXx0A4Ugd3pE1kOK7ATHDzApujIz0n00ygxbiKvXLw4tSyhmsydu1PaNAuLoQy0HPsd3miDL1oQrLAANfe-41HatRzvrKyhsBrdnN45YdX1sc-qPAG7Uap4cmVflQFHMXvHwyn7lm0Q83PbMPN2LmLyiv1GvZJ0_lTHTOe-IiSru-FZfGxADepd4eN4L0_yXL3QLbd9bezFK1jyeATmD-e0Fjscxv24-aig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318fa54bad.mp4?token=BW4SREg8Vhity3AuDCjFKBIAoOYnRTQIikjhhr45VvAyQtvol8xejvaUcZlkKg7Yj30FjZYXUH5jMWUvwWy4ksFcb6e0MGrX3XFNzLAOnV1dVMB67-lNXx0A4Ugd3pE1kOK7ATHDzApujIz0n00ygxbiKvXLw4tSyhmsydu1PaNAuLoQy0HPsd3miDL1oQrLAANfe-41HatRzvrKyhsBrdnN45YdX1sc-qPAG7Uap4cmVflQFHMXvHwyn7lm0Q83PbMPN2LmLyiv1GvZJ0_lTHTOe-IiSru-FZfGxADepd4eN4L0_yXL3QLbd9bezFK1jyeATmD-e0Fjscxv24-aig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیفت کاری نامنظم چه عوارضی دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463803" target="_blank">📅 08:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463802">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97cb710862.mp4?token=DQQ9dp-yv3h1nQ26YOjBMv_lMdIfXGcMwdAKKhPW5leAE01Ac8dCs9C6p_sF9d3nHO9i464i0KyhLItlt-gEuq4hN1R9UGniAmbZABIY0oNFg1pPlK5k175vGvSTKa1gYTLEWgWqId5L9tCPnUMMuiPJdgK_dMZ1_hh671ku8mq7sZS-WiuEx8czD29YasR5tJGKbh0bBb5RJ0dinOtW08nkJCtRGvVjYHcIntVSzI368CJsOo31SA8Dcw91AxdOGJaWr1HmQqOeC0PAEw3sO7nczCMCeKKnrrFGbmKIHMrzGYAdxli5E-fbV9_MNCh1YpfLkuA8hxIaaI96SIly0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97cb710862.mp4?token=DQQ9dp-yv3h1nQ26YOjBMv_lMdIfXGcMwdAKKhPW5leAE01Ac8dCs9C6p_sF9d3nHO9i464i0KyhLItlt-gEuq4hN1R9UGniAmbZABIY0oNFg1pPlK5k175vGvSTKa1gYTLEWgWqId5L9tCPnUMMuiPJdgK_dMZ1_hh671ku8mq7sZS-WiuEx8czD29YasR5tJGKbh0bBb5RJ0dinOtW08nkJCtRGvVjYHcIntVSzI368CJsOo31SA8Dcw91AxdOGJaWr1HmQqOeC0PAEw3sO7nczCMCeKKnrrFGbmKIHMrzGYAdxli5E-fbV9_MNCh1YpfLkuA8hxIaaI96SIly0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود کاروان تیم ملی امید به ورزشگاه محل برگزاری بازی با کرۀشمالی
🔹
تیم ملی امید کشورمان با ترکیب محمد خلیفه، امین حزباوی، دانیال ایری، فرزین معامله‌گری، ابوالفضل کوهی، مبین دهقان، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، یوسف مزرعه، سعید سحرخیزان و کسری طاهری، ساعت ۹ امروز بازی را آغاز خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463802" target="_blank">📅 07:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463801">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafc0ac85a.mp4?token=tH671h3rBKxZMVWYIYqd8i5PoEUmsfB8yhZVE5I7Y7Ia6bR-Ykykqtp3J_QqnOio4yl_zScVWFRnDYs5fcNT19P565uNH3Oi-JOvdel0NzzTqIHvT7ehV_FE0NMhJyKcJmMau5vvmqQOTEDOo0SkwGOOiILi3AA_rrBSABa1f4votqX_ZVqpEq8oA2WEI6RXhiO0ZMrDmEgwGhZn8384T13me9anBvOYgf8yRBYtizh2FH2U2IZc88WOwXmeRiN3NiujS3y6C78BcHB3S7139ugD6Lv_vGW6d_FBQvmJ8j7tclpuvDhKLncPxZS1fzAi83evhjnlbnMJq3_NJyMCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafc0ac85a.mp4?token=tH671h3rBKxZMVWYIYqd8i5PoEUmsfB8yhZVE5I7Y7Ia6bR-Ykykqtp3J_QqnOio4yl_zScVWFRnDYs5fcNT19P565uNH3Oi-JOvdel0NzzTqIHvT7ehV_FE0NMhJyKcJmMau5vvmqQOTEDOo0SkwGOOiILi3AA_rrBSABa1f4votqX_ZVqpEq8oA2WEI6RXhiO0ZMrDmEgwGhZn8384T13me9anBvOYgf8yRBYtizh2FH2U2IZc88WOwXmeRiN3NiujS3y6C78BcHB3S7139ugD6Lv_vGW6d_FBQvmJ8j7tclpuvDhKLncPxZS1fzAi83evhjnlbnMJq3_NJyMCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمۀ اول دیدار تیم ملی هندبال ایران و قزاقستان با برتری ۱۶ بر ۱۳ تیم ملی کشورمان به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/463801" target="_blank">📅 07:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463800">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUL4OG2oUUyGuVuZ87sS_zRom69VzoMIs0conAm1htL14DoiUFN1pc1A1NIs4wUWzt-kQ3NLbYd2Y57dscczSL0P4WCi99qlJ269xyzs6XsL8Rc6rM-Swk0BQwxxO2t66h9KG0gXXaRGQc-nEJk7gILbCwNx3f9XRCOV3Ot4LzcVGxVzEQ_3-qP9VGVZmBM7jKxqKvo18CNWoc0MD32sBY4B-KVhGWNtQfqEENKAXMP0xZTXhmyTmcJqsDEUxdD5r25q2v2rm50Huh1XEeKMoVLb4zYO9JX4eVSSboEs3XKlU4vBDJw1x8fq_woLq5hzgF0NqTqN-8RARXB5Qhzuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ مهر به صدا درآمد؛ ۱۶ میلیون و ۷۰۰ هزار دانش‌آموز به مدرسه رفتند
🔹
سال تحصیلی ۱۴۰۶-۱۴۰۵ با نواخته شدن زنگ مدرسه در سراسر کشور آغاز شد و دانش‌آموزان تحصیل را آغاز کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/463800" target="_blank">📅 07:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463799">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی خطاب به وزیر خارجۀ فرانسه: نمی‌توانید مدعی دلسوزی برای حقوق بشر باشید، اما در برابر جنایت آمریکا و رژیم صهیونیستی سکوت، و همکاری کنید
🔸
سیدعباس عراقچی که برای شرکت در اجلاس مجمع عمومی سازمان ملل متحد در نیویورک به‌سر می‌برد، با وزیر امور خارجۀ فرانسه دیدار و گفت‌وگو کرد.
🔹
عراقچی با انتقاد از مواضع مداخله‌جویانۀ فرانسه در قبال ایران، بر ضرورت احترام سفارت فرانسه به قوانین و مقررات داخلی ایران تأکید کرد.
🔹
وزیر امور خارجه گفت فرانسه نمی‌تواند مدعی دلسوزی برای حقوق بشر باشد، درحالی‌که در قبال جنایات ضدبشری آمریکا و رژیم صهیونیستی علیه ملت ایران و کشتار زنان و کودکان ایرانی سکوت کرد و در اجرای تحریم‌های غیرقانونی آمریکا علیه مردم ایران نیز همکاری کرده هست.
🔹
عراقچی تاکید کرد جمهوری اسلامی ایران قائل به روابط مبتنی بر احترام و منافع متقابل با همه کشورها از جمله فرانسه است اما در دفاع از منافع و مصالح خود جدی و قاطع عمل خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/463799" target="_blank">📅 07:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463798">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8aaff579f.mp4?token=kvT3nbprU4HCzPpacPLSbmulI03jSN5DI8IJ5QYw8jcdRfxoxf1gm99CYP2PgmWdHrhyrYPiApIHCIOEmV04Ju1LH8iapNpraG_jnq2BlL8YVfpYf8G656tQ4YYY66w5nZ_m20TohRJpmNN14GsFB3zML5I5YtK4CmcLbsTaY_UpVybkTUZunLdLc6JwDQAYXXiScwuN3CnP3QjTuXO2Q0ot0THF-PGUF1JKcf7vMB02UL-9hb39sy5tb4zcJvjiWT9WxhM27JkC7nlfe1YxKPYiL4qkbaJlCZT25b9lBrCaWziMA45zZ_JVWpGMLzlbDg_2EVsZ3_veR5Dn1uJFaHoT2BhW_S4fIplQkVz1Xl2WDFRm8Jt-MgAIPaQUZ60s9DQu68zAzfJd0xmnL_8kEyqSnsTpIZ7lalngxfo7-U0UKt4xdv1we_x8rIAF55uNenB1-wePUKCrbvaJAWt43KNIfSpiuAHat-G-9fgn4rLMYL0X8y5CdJCtTAsl7s6d8YVJTDTD_T4iTKOnfYWh7c5YNzlVNOfiQx_aM4WJ4BrIyy69zecx5WG1754NIbHT-i6nT-beXFZl6XFTU_ADmYyWLPEigTHxEEi1SyxKEHKyGKD7-eDtol7z5ugLVLMg7uwGR1d39pFWRAMRtqqxz8SqpQ43TmB-iQNYwudu_So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8aaff579f.mp4?token=kvT3nbprU4HCzPpacPLSbmulI03jSN5DI8IJ5QYw8jcdRfxoxf1gm99CYP2PgmWdHrhyrYPiApIHCIOEmV04Ju1LH8iapNpraG_jnq2BlL8YVfpYf8G656tQ4YYY66w5nZ_m20TohRJpmNN14GsFB3zML5I5YtK4CmcLbsTaY_UpVybkTUZunLdLc6JwDQAYXXiScwuN3CnP3QjTuXO2Q0ot0THF-PGUF1JKcf7vMB02UL-9hb39sy5tb4zcJvjiWT9WxhM27JkC7nlfe1YxKPYiL4qkbaJlCZT25b9lBrCaWziMA45zZ_JVWpGMLzlbDg_2EVsZ3_veR5Dn1uJFaHoT2BhW_S4fIplQkVz1Xl2WDFRm8Jt-MgAIPaQUZ60s9DQu68zAzfJd0xmnL_8kEyqSnsTpIZ7lalngxfo7-U0UKt4xdv1we_x8rIAF55uNenB1-wePUKCrbvaJAWt43KNIfSpiuAHat-G-9fgn4rLMYL0X8y5CdJCtTAsl7s6d8YVJTDTD_T4iTKOnfYWh7c5YNzlVNOfiQx_aM4WJ4BrIyy69zecx5WG1754NIbHT-i6nT-beXFZl6XFTU_ADmYyWLPEigTHxEEi1SyxKEHKyGKD7-eDtol7z5ugLVLMg7uwGR1d39pFWRAMRtqqxz8SqpQ43TmB-iQNYwudu_So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجرۀ طیبۀ میناب در اول مهر @Farsna - Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/463798" target="_blank">📅 07:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463797">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ebd9a8611.mp4?token=H0stl_JNTG2R8JxZnvAz8A4uCE-qttGhkY21jJTxyfXpEkDICWksChHh9Qw7wJwNWBwVkr9X0DNFxj7nPsTvI8wvoY9o9wHif58HShO37ej1c-fJXQagDPN7reMq-KcSxfQPEczeLwcBYF75yi4ITfR32ZzZ1M0geN0tOU5rXlfg3AR04L2447lWxFkj0BHJvOR3FRSIkImB-8W_nvwfS6touiGxnXTakQ6ISAVzT8evP2wMpKtm1rflssoXPPnzchKSR6rqQcCJMvTZX393e7Mc-1QeiNbJPZCZ_HlXgodMrSHaLezFJi9YcrHozpZi-BefVuoBivTAjE4BCA5QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ebd9a8611.mp4?token=H0stl_JNTG2R8JxZnvAz8A4uCE-qttGhkY21jJTxyfXpEkDICWksChHh9Qw7wJwNWBwVkr9X0DNFxj7nPsTvI8wvoY9o9wHif58HShO37ej1c-fJXQagDPN7reMq-KcSxfQPEczeLwcBYF75yi4ITfR32ZzZ1M0geN0tOU5rXlfg3AR04L2447lWxFkj0BHJvOR3FRSIkImB-8W_nvwfS6touiGxnXTakQ6ISAVzT8evP2wMpKtm1rflssoXPPnzchKSR6rqQcCJMvTZX393e7Mc-1QeiNbJPZCZ_HlXgodMrSHaLezFJi9YcrHozpZi-BefVuoBivTAjE4BCA5QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صعود ۲ شمشیر باز ایران به مرحلۀ حذفی
🔹
علی پاکدامن و محمد فتوحی، نمایندگان شمشیربازی ایران در بخش انفرادی مردان در بازیهای آسیایی ناگویا، امروز چهارشنبه روی پیست رفتند و کار خودشان را آغاز کردند.
🔹
هر دو سابریست کشورمان در گروه‌های شش‌نفره حضور داشتند و باید پنج بازی انجام می‌دادند که پاکدامن و فتوحی هر دو با ۴ پیروزی و یک شکست موفق شدند به مرحلۀ حذفی راه پیدا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/463797" target="_blank">📅 07:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463796">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799d70cf31.mp4?token=rCQNyEwhqxUs86f5797x_PO1qzpEat7RFRPDb5YX9oHxtSwKQAVUi-Y6DJEiZx0Fei5MyYuX4B04AVmMjrBDoFFPjs_diCcnJMtYmjtSnABOQ75gWUgaQ3_qU8iaQZ8hsjlL7TtWOLAj2i7GW2-r8Y-WjnyQxtQl10U2mKWsFm8n56Ym6J7u5HSLbdu9Kq7cKHpqxmcshPgKVSfCMSpUHR0MY9MAPaxczSiemtgPqDc58r5Y9-dwrLAt0Pk12byZhGyvifgg9o5PHqPZkDhQPunPq0OcLFN51JxNH9VcajRsqccfEoPLOUo4YzOQ4lBFoost6lMY5aSLuluNFmt9-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799d70cf31.mp4?token=rCQNyEwhqxUs86f5797x_PO1qzpEat7RFRPDb5YX9oHxtSwKQAVUi-Y6DJEiZx0Fei5MyYuX4B04AVmMjrBDoFFPjs_diCcnJMtYmjtSnABOQ75gWUgaQ3_qU8iaQZ8hsjlL7TtWOLAj2i7GW2-r8Y-WjnyQxtQl10U2mKWsFm8n56Ym6J7u5HSLbdu9Kq7cKHpqxmcshPgKVSfCMSpUHR0MY9MAPaxczSiemtgPqDc58r5Y9-dwrLAt0Pk12byZhGyvifgg9o5PHqPZkDhQPunPq0OcLFN51JxNH9VcajRsqccfEoPLOUo4YzOQ4lBFoost6lMY5aSLuluNFmt9-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجرۀ طیبۀ میناب در اول مهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/463796" target="_blank">📅 07:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463795">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76e1f53f2.mp4?token=flbszeLIXf2KVTSXvIgbeo7teDDgezdQ-HoQOTH49ga9k2EDoHKoCDhUuZ_cPm6vNEvy3MibDbMBKXtPsrEeqwmigWNv9PAOKeAj49RJlCsrisSGlHZQHu6gIG5EPDBpbG1tnW9xz2vTfXyRyZKDLa712x8MtyXOd3KjvVNi5bVsxSa97OZE2CKZMZPdm8RxPnyWlje51NRMvkuXkrbRC_ILfYK-SPspSAtqTLIIRDg6oHJl3ZSl1POsi_1smpszaJ94S-cJrb5FXY2sKEU1HObGfDCxPPPR8bvzLttjzk5PLTVAdSFacFL1PXs4E8WFaB4LSzyCUjmqbxVb4YXlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76e1f53f2.mp4?token=flbszeLIXf2KVTSXvIgbeo7teDDgezdQ-HoQOTH49ga9k2EDoHKoCDhUuZ_cPm6vNEvy3MibDbMBKXtPsrEeqwmigWNv9PAOKeAj49RJlCsrisSGlHZQHu6gIG5EPDBpbG1tnW9xz2vTfXyRyZKDLa712x8MtyXOd3KjvVNi5bVsxSa97OZE2CKZMZPdm8RxPnyWlje51NRMvkuXkrbRC_ILfYK-SPspSAtqTLIIRDg6oHJl3ZSl1POsi_1smpszaJ94S-cJrb5FXY2sKEU1HObGfDCxPPPR8bvzLttjzk5PLTVAdSFacFL1PXs4E8WFaB4LSzyCUjmqbxVb4YXlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمک ۱۰۰ میلیون دلاری کانادا برای فلسطینی‌ها
🔹
نخست‌وزیر کانادا با اشاره به بحران انسانی در نوار غزه، گفت که بیمارستان‌ها، مدارس و درمانگاه‌های آن همگی ویران شده‌ و هیچ‌کدام بازسازی نشده‌اند.
🔹
او گفت من ۱۰۰ میلیون دلار کانادا کمک بین‌المللی به فلسطین را اعلام می‌کنم که ۸۰ میلیون دلار آن برای کمک‌های بشردوستانه و ۲۰ میلیون دلار آن برای حمایت از ایجاد ظرفیت‌های صلح و امنیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/463795" target="_blank">📅 07:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ0H6hOPeeqqvvt5qJwUWCGSv0VGUtQGU3FikCdGeSOau1su_YheFeOg4C0nTmTNCnnQhcMnQTm3OXYqhBrkJscCASLiUS2h1u5lDCo61Qr697Y5epIuSnRDslGz68fu9WKWjFhGSz5eAMGEEwyhwL6F0kcN1KShAYj68enKioExn_UTWTz9TBOneRn6w5l9606QAuFE1BqtcXrZCEDOAaMMcHvQxZJLwBmIt0YX1azcJIOF_XFPoGz8o9KODcXQzhNKJCLQeucgRHAitw5Rivofhj5c3CtndX9onrUVK3f18S5hQB3UPPt_j4ayLmMXjX1NK8fhYSoggKEFdRa01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این زخم‌ها فقط «درد» ندارند
🔹
تصادف، بیماری یا یک حادثۀ ناگهانی می‌تواند زندگی یک انسان را در چند لحظه تغییر دهد؛ اتفاقی که شاید برای اطرافیان با چند روز بستری، عمل جراحی و دورۀ درمان معنا پیدا کند، اما برای فردی که با ضایعۀ نخاعی از بیمارستان به خانه برمی‌گردد، تازه آغاز یک زندگی متفاوت است.
🔹
زندگی‌ای که در آن بسیاری از کارهای سادۀ روزمرۀ دیگر ساده نیستند و هزینه‌هایی که پیش از حادثه شاید حتی به چشم نمی‌آمدند، به بخشی ثابت از زندگی تبدیل می‌شوند.
🔹
زندگی روی ویلچر فقط به نشستن و جابه‌جایی محدود نمی‌شود؛ پشت این زندگی، دردها، محدودیت‌ها و هزینه‌هایی قرار دارد که هر روز تکرار می‌شوند. از مراقبت‌های پزشکی و وسایل ضروری گرفته تا توانبخشی، رفت‌وآمد و هزینه‌های روزمره؛ مخارجی که برای بسیاری از افراد دارای ضایعۀ نخاعی، بخشی جدایی‌ناپذیر از ادامۀ زندگی است.
🔹
در این گزارش، روایت افرادی را می‌خوانیم که می‌گویند هزینه‌های ضروری زندگی با ضایعۀ نخاعی گاهی به چند‌ده میلیون تومان در ماه می‌رسد؛ هزینه‌هایی که با پایان درمان تمام نمی‌شوند و برای ادامۀ یک زندگی عادی باید هر روز پرداخت شوند.
🔗
روایت‌هایی از دشواری‌های پنهان زندگی بیماران نخاعی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/463794" target="_blank">📅 06:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440cb06b59.mp4?token=rjxvQTDVsX_B9fsgx7BhHWWzBLn36iRUJcNGpN3rtF-1pUDpFm2t7TeXPFjNUGmaRxkRX_1S7D1LRQg-PpIA2FNB_SMhFwXLf3eXuO_t-bNbLAWFJxLUvNCnGmv9YlUFs_4YktLVgils1fiLvXqOKkBmDmJzMM8WjjJwS5qkzIu_s2Dj8YUa-_qZmMY-gWm6UMrJmKzNvlgnon64Zm4hZM_EErl3EHHepr2xLg-7Q6ndV7K0cjqCM9g9_dAaPRAM5kFviGyVFSu_NQkegvmOEdxecfpB__m4oy719Kh0Fgxu7o-0dwDBwV1VGUFi8Ijwlk9RH0SMvxyKCnsnAdYLAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440cb06b59.mp4?token=rjxvQTDVsX_B9fsgx7BhHWWzBLn36iRUJcNGpN3rtF-1pUDpFm2t7TeXPFjNUGmaRxkRX_1S7D1LRQg-PpIA2FNB_SMhFwXLf3eXuO_t-bNbLAWFJxLUvNCnGmv9YlUFs_4YktLVgils1fiLvXqOKkBmDmJzMM8WjjJwS5qkzIu_s2Dj8YUa-_qZmMY-gWm6UMrJmKzNvlgnon64Zm4hZM_EErl3EHHepr2xLg-7Q6ndV7K0cjqCM9g9_dAaPRAM5kFviGyVFSu_NQkegvmOEdxecfpB__m4oy719Kh0Fgxu7o-0dwDBwV1VGUFi8Ijwlk9RH0SMvxyKCnsnAdYLAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | صعود الکترونیکی‌های ایران با رد شدن از عربستان
تیم فوتبال الکترونیک ایران در مرحله یک چهارم نهایی بازی‌های آسیایی در برابر عربستان به پیروزی رسید و به نیمه‌نهایی صعود کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/463793" target="_blank">📅 06:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شروع خوب روئینگ‌سواران ایرانی و صعود به فینال
🔹
بهمن نصیری در مادۀ تک‌نفرۀ سنگین وزن روئینگ در رتبه سوم گروه قرار گرفت و به فینال A صعود کرد.
🔹
فاطمه مجلل در مادۀ تک‌نفرۀ سبک وزن زنان نیز در رتبۀ نخست قرار گرفت و مستقیما به فینال صعود کرد.
🔹
در مادۀ دو نفرۀ سبک وزن زنان ایران با ترکیب زینب نوروزی و کیمیا زارعی، این تیم در رتبۀ نخست گروه خود قرار گرفت و راهی فینال شد.
🔹
در مادۀ ۴ نفره زنان ایران با ترکیب مهسا جاور، سها فخری، ساقی ملکی و هنگامه کامیاب رتبه دوم از آن ایران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463792" target="_blank">📅 06:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کایاک ۲نفره بانوان راهی فینال شد
🔹
الناز شفیعیان و تانیا کارگرپور در گروه دوم مرحله مقدماتی کایاک دونفره ۵۰۰ متر زنان با زمان یک دقیقه و ۵۲.۹۳۹ ثانیه در جایگاه سوم قرار گرفتند و راهی فینال شدند.
🔹
هیوا افضلی در گروه اول مرحله مقدماتی کانوی تک‌نفره ۲۰۰ متر زنان با ثبت زمان ۴۹.۳۰۸ در جایگاه چهارم قرار گرفت و به شانس مجدد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/463791" target="_blank">📅 06:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انهدام پهپاد ارتش سعودی بر فراز یمن
🔹
یحیی سریع، سخنگوی نیروهای مسلح یمن: یک فروند پهپاد شناسایی مسلح وینگ‌لونگ ۲ متعلق به دشمن سعودی، حین انجام مأموریت‌های خصمانه در حریم هوایی المخاء رهگیری و منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463790" target="_blank">📅 06:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8I4qmHYNeTDfyrP140J0PCU6FdDoqZxDgcameeRDpuf0jFTsWN7xuqEpvk_a1-l8KSngLgdP0yO5mDT2_Luc79kEqzPGp5Uw3EoJIfr1C-rr6Vbrw5nLwoJNXRovIuto5C4deBFpwGyTu1Zj4-PM0zg2hnf7P2OL4fcNeekklfChWlnFKBcExu8cUwwwjfCRawypdNmTGjBemdOdl5-nkjekqj_j1jUdv91exCIbh_DUwUC7liRHVgOQZjARRFVdYs0kGll5MbbTZm8oK7q0iIhtbYUi4nN0y7UH-IO1WzHtZ9538Ew0JIr2-VD7sDo_2wUmpkfx2-BN5gnA9UQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین «راهیان نور پایتخت» برگزار می‌شود
🔹
سازمان بسیج شهرداری تهران: نقاطی که در جریان جنگ ۱۲ روزه و جنگ رمضان آسیب دیده‌اند، برای بازدید به نقاط یادمانی تبدیل می‌شوند.
🔹
این برنامه با هدف روایتگری میدانی، تبیین جلوه‌های مقاومت و آشنایی شهروندان با ابعاد رخدادهای جنگ ۱۲ روزه و جنگ رمضان در پایتخت اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463789" target="_blank">📅 05:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058897298a.mp4?token=CxwcZEij7M8QLdM9p4WfyBHY7kIHPFv9iVMVpjITZOPcx71hnfogEcJA6ET6TkEQGxrZc_9rH-eBWzYMYKK4Va80TIReFgGHs5KRZtekbPzae1pqK-IdPeZVhS-tpPDHSbgrIYO2I-szeMSZGfqXDSQQR3lolswZKO5J8tDtjRKwh0QmPVx7tDqOPkhu9MBT6-FNXMYEkKT9n0zyGbbYbAdZx14MtmB0QV8JmlJimJDTNwaU5aGPVyHwndfQ2M7UUYHV0fisWOyI25WAgoIWhBm-QCqI0deeQG_fUCmucB3nrRfqh-BxlwgkyBIBge7Y0V8wigFGLOdv40GBayWdYmvoI6rORDb3ymFyfP-yZOMiUDTDKVVDm-wybb1cN2A3DpChBShMCGEbArcTkIwq3ADpznV5hUSJ5FnpfZefidAn1NodovB5Z471go2R06e_L5aqi1Ga_kiV9iSQE2lHLKCt4eV3zjXIIFlyT3_aMIgeUYxxGeekbamPDLonj7vIak0ZJ3Ca11wQS9v8SQrbvvEBPCg_qynnq3K6uSu9Urvfa2mo4-cCMHCiNd9eteFlJsIdjAbf6Qbf1gwFqEO7ljTK4x3h-1Nza6dlSmSf2TeHZ3BzDrMNXgH--6aYyzXtDC8TL79E9PZpdhHLc6SQ7FU_XyEOjYnrnH2qrru38FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058897298a.mp4?token=CxwcZEij7M8QLdM9p4WfyBHY7kIHPFv9iVMVpjITZOPcx71hnfogEcJA6ET6TkEQGxrZc_9rH-eBWzYMYKK4Va80TIReFgGHs5KRZtekbPzae1pqK-IdPeZVhS-tpPDHSbgrIYO2I-szeMSZGfqXDSQQR3lolswZKO5J8tDtjRKwh0QmPVx7tDqOPkhu9MBT6-FNXMYEkKT9n0zyGbbYbAdZx14MtmB0QV8JmlJimJDTNwaU5aGPVyHwndfQ2M7UUYHV0fisWOyI25WAgoIWhBm-QCqI0deeQG_fUCmucB3nrRfqh-BxlwgkyBIBge7Y0V8wigFGLOdv40GBayWdYmvoI6rORDb3ymFyfP-yZOMiUDTDKVVDm-wybb1cN2A3DpChBShMCGEbArcTkIwq3ADpznV5hUSJ5FnpfZefidAn1NodovB5Z471go2R06e_L5aqi1Ga_kiV9iSQE2lHLKCt4eV3zjXIIFlyT3_aMIgeUYxxGeekbamPDLonj7vIak0ZJ3Ca11wQS9v8SQrbvvEBPCg_qynnq3K6uSu9Urvfa2mo4-cCMHCiNd9eteFlJsIdjAbf6Qbf1gwFqEO7ljTK4x3h-1Nza6dlSmSf2TeHZ3BzDrMNXgH--6aYyzXtDC8TL79E9PZpdhHLc6SQ7FU_XyEOjYnrnH2qrru38FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل نوجوانت را به‌دست بیار تا دلش را کسی نبرد
🎙
هادی زینالی
#تربیت_فرزند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463788" target="_blank">📅 05:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c0ce36f5.mp4?token=jwCulC6mCPmAF3IJ-WYuLxJzatvZ4FcbwnyGx22ZEFY_j50nclw6OX9p9Aw7xiTeBPEfmkkN-2WhdLiWBLlOZLk-FgHwbbUpqWRBZe9RfIF9RrCqTcNsQHL8QBlGtXK2E0Pg0XVNdoeyPAPIGiBsK0rj80nVNme95TjESzyFbGyaBTQNAtOGtIQIaibGbq2whafpZoPRVxfLAH2FPl81zS5VaRYEnm8WEfxCqEYKQA8MeiFpZviG_Sh-g3m8l-Cp1lElticb-b6YFllBrYvMZQHLTfW9UjXGyjJMfHT0e5hX1fxYH-AEflbuNDCUhtEYX7NHGr9mxYrIC_gGQP0Pkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c0ce36f5.mp4?token=jwCulC6mCPmAF3IJ-WYuLxJzatvZ4FcbwnyGx22ZEFY_j50nclw6OX9p9Aw7xiTeBPEfmkkN-2WhdLiWBLlOZLk-FgHwbbUpqWRBZe9RfIF9RrCqTcNsQHL8QBlGtXK2E0Pg0XVNdoeyPAPIGiBsK0rj80nVNme95TjESzyFbGyaBTQNAtOGtIQIaibGbq2whafpZoPRVxfLAH2FPl81zS5VaRYEnm8WEfxCqEYKQA8MeiFpZviG_Sh-g3m8l-Cp1lElticb-b6YFllBrYvMZQHLTfW9UjXGyjJMfHT0e5hX1fxYH-AEflbuNDCUhtEYX7NHGr9mxYrIC_gGQP0Pkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت انگلیس از رژیم صهیونیستی در سازمان ملل
🔹
نخست‌وزیر انگلیس در مجمع عمومی سازمان ملل گفت که لندن در کنار رژیم صهیونیستی در برابر تهدیدات مداوم ایران و محور مقاومت ایستاده است.
🔹
همچنین او از تداوم حمایت نظامی از اوکراین، برای ادامۀ جنگ با روسیه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463787" target="_blank">📅 04:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMDhE4jYPr3VfH1ENBo3EKdnLMwTaOLax4XT6x0SYAGb61NiDfkUJbgWQeYwA03RylM3JFzEZRBbowI-xs_ZVJtp-wHooWESLr4HwZ0q8-BqkyzNS7CoiHwspvPdlHcWgudwVymzacGdKUIwlCRNRYTgY765V6zjOCz09AkOGAXRZnQIRINGNpUeNvMPvNw4Odsu8P3wUztq1gWjxm5ul0u7_90jwlphVX6Qz3ZpnpWqq6i5wwYcIPuJ6JNbeVJIEjyBvQOkZMablUKtYSXzcq3e0c5pOvcfPrwKuTPTRYaO-yWfz5j6siCrQB5F_z37_f2uODcfG5Y0uzwr6JKkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سید مجتبی خامنه‌ای، شبیه‌ترین فرد به آقای شهید هستند
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان رهبر معظم انقلاب: ما آقای شهید را جز یک‌بار از نزدیک ندیده بودیم و شناختی از ویژگی‌های اخلاقی و شخصیتی جزئی‌شان نداشتیم.
🔹
اما در همان حدی که ایشان و استادمان…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463786" target="_blank">📅 03:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463785" target="_blank">📅 03:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfCizr_OP8jeKfFvc6dVJ3E_bRgIqO1kSuL8iYKDhT_AtNaERECo_XxAJArKRez35oGTqNar2XS1UTVEIAuX0njdLk77zMIywkDY7i98mTv15oHddg8_hWdt_wdQolmIyGIvKyjA0a1AD0_JzedP6ZgarhfbmoyXw_mYKvvjUli82ru4BnFj7MeFpkdn-5V6QxhdqumVI5Ks737850zSAXHcbdHx7iJDRqhusqduqTzifTByyOHvG4PbdkOpxJA9mvdmNVapY33T6HZRZjMtONVhssCmgt2ybxFbn2ZYu8sNTMPf1DAaNT9BGso5awY7koM163zvN8lucNUVSkb2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات اسرائیل به لبنان و غزه
🔹
همزمان با انتقادها و اعتراض‌های سران کشورهای مختلف به تجاوزات مکرر رژیم صهیونیستی به لبنان و نوار غزه در مجمع عمومی سازمان ملل، رسانه‌های عربی از تکرار حملات تجاوزکارانه و ددمنشانه صهیونیست‌ها به مناطقی در جنوب لبنان و جنوب نوار غزه خبر دادند.
🔹
براساس گزارش‌ها، توپخانۀ اسرائیل شهرک المنصوری در جنوب لبنان را هدف قرار داد. نظامیان صهیونیست همچنین ساختمان‌هایی را در شهر الخیام منفجر کردند.
🔹
از سوی دیگر تانک‌های رژیم صهیونیستی در حال شلیک به مناطق مسکونی در شرق شهر خان یونس واقع در جنوب نوار غزه هستند.
🔹
همزمان گفته می‌شود که نظامیان اشغالگر به شهرک‌های «سلوا» و «عقابا» در کرانۀ باختری یورش برده و منازل فلسطینیان را تخریب می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463784" target="_blank">📅 03:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463782">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAqgEum8sH4ro2oQ_XH19Wr9UH61trUzqnONH-fcAQ-yUBoay2bZ0UoX0qwkuB8zKzuATyK1IjFm0tO4RsxBJubKQOtfc1vcuLYOaIiELBIbEEbRM6JgrbYF2otwimnXSrsPpXv2mmSOaGwNe0VRYrgRUkIExPqC3oyMAg-hQ38vfBaOQ_3WgJaVQRgjeUJYRPokR421FMofUZymxf56NOarqwhNOewRkezV1jRr6NErom6jbD26Gs2nBtb8se6o6szs0Je0KKvAYbcX-_xOAFoOPc3fk-T0kqDiBSp3p0HVt0JJ-1Mcpdlxk_JRh3LAhSXDQ_f9-t5jCfHpHJ0nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFR11JpcI_bAd0YJ2kEXA2JZyqA32f5CZ7X1EOx4PN5jYSNYWeDhQw8vFsjeP21TK-tCaz4UZ3dxdsnteWyLfdbR2hQsMqKYaeAB_eAtIwAqAlIUSYxVnfzetUYr32mIdhvBjunwiPex9wpfOaUBGZJv7cX6GENog-aGrIpsv70Fb3atreAfk6E7ScLLc3V7cTm_-ihTO3nJJ9iR_S2RoB4rYCmyhYb0Jg-C79GkVFGZa_9nPgftIXc60U5UFRxaoYFGp1pigXeiPR7z8DBecj_YmhU6LsCtXLomAD1UVCWVv0JyeCxUpkiXbGqIHIyxj-5rwfw4fhjLKbn9dkXrvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عراقچی خطاب به وزیر خارجۀ ایتالیا: میزبانی از پایگاه‌های آمریکا به معنی همدستی در تجاوز است
🔹
اقدام برخی کشورهای اروپایی ازجمله ایتالیا در میزبانی پایگاه‌های نظامی آمریکایی و هرگونه همکاری در تدارک اقدامات تجاوزکارانه علیه ایران به معنی همدستی در تجاوز است.…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463782" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463781">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1EguhIBVhDe3cr-plLaYTYlFEI4HRFFpbhokGQo3HJ_C5CsZVj6D3BIPf_MAaet5cyUnKRvGEs1NT76vepre068WFrIlgh4dAmywBye7FPWVbLR4bBXpn2QIbfGaE_u4Llq2W2gLHlbg5BSejj2bNBkopOYTJSmDMqdLOeDgiHMZMIGrBS-eQU4bhRed8DP-El-Yh-eHQ-GW48nbYCpocyWjCaXremW-BRBa4-7EqZ6sD9LadXrncvjhv7Vgr0OQfyEhLBmu_h2zjcVhwdcDFq-9yPtcOEmZLRdMvhY2vEOiro__YNxgVN6qH2B927E9K1PfYlGfinR4ca0B0wwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پرتعداد رسانه‌های ضدایرانی در نیویورک برای حاشیه‌سازی علیه هیأت ایرانی
🔹
در حالی که آمریکا از صدور ویزا برای اعضای تیم رسانه‌ای همراه مسعود پزشکیان، خودداری کرده است، ۶ خبرنگار ایران اینترنشنال و ۴ خبرنگار بی‌بی‌سی در نیویورک، محل برگزاری نشست مجمع عمومی سازمان ملل حضور دارند.
🔸
البته حضور خبرنگاران این دو رسانه در نیویورک همزمان با سفر رؤسای جمهور ایران، موضوع تازه‌ای نیست و در سال‌های گذشته نیز تیم‌هایی از این رسانه‌ها به محل برگزاری مراسم اعزام شده‌اند و به جای تمرکز بر برنامه‌های رسمی، به دنبال حاشیه‌سازی برای هیات ایرانی بوده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463781" target="_blank">📅 02:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463780">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حملات موشکی عربستان به شمال یمن
🔹
منابع یمنی گزارش دادند عربستان مناطق «مران وحیدان» و «الظاهر» در غرب استان صعده را هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/463780" target="_blank">📅 02:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463779">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ac6906c6.mp4?token=sNAfqmWneFMGFpLzYtKkEyHmc35tmXYPaE3xpurOdYaeOQeEWACUiAKPCmzhsC8LUTbM7SjQKYajIHAPpr1XBvCSkw-aYXTUjUq8HMISJZSnW7qljDQnPuJ8FEDkHNzMFvShsX0dbRGMeNxrKbYJ3e6LeIHSkjIE3Z5Y8f3_L7eB8PH25kzGHZgH7P84fKQd_4g947sfP_bjHEMyUJU89XpgD_PLZgLsi05C1UameUSqEhbICGFuTDzwb0RpSi-sonExIEzkVuJMhXXZQlthO09x9gS-U9Evk8EQr-SZDZZE9FBcHQ8oaMpoPNP4ksKZDXSOLkTjUeShCa35zFP0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ac6906c6.mp4?token=sNAfqmWneFMGFpLzYtKkEyHmc35tmXYPaE3xpurOdYaeOQeEWACUiAKPCmzhsC8LUTbM7SjQKYajIHAPpr1XBvCSkw-aYXTUjUq8HMISJZSnW7qljDQnPuJ8FEDkHNzMFvShsX0dbRGMeNxrKbYJ3e6LeIHSkjIE3Z5Y8f3_L7eB8PH25kzGHZgH7P84fKQd_4g947sfP_bjHEMyUJU89XpgD_PLZgLsi05C1UameUSqEhbICGFuTDzwb0RpSi-sonExIEzkVuJMhXXZQlthO09x9gS-U9Evk8EQr-SZDZZE9FBcHQ8oaMpoPNP4ksKZDXSOLkTjUeShCa35zFP0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای توقف هواپیمای پزشکیان در الجزایر
🔹
دیروز هواپیمای رئیس‌جمهور در مسیر نیویورک، جایی میان تهران و مقصد نهایی، در فرودگاه الجزیره نشست و وزیر کشور الجزایر از پزشکیان استقبال کرد.
🔹
برخی رسانه‌ها شایعه کردند که این توقف به‌دلیل نقص فنی در هواپیمای رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/463779" target="_blank">📅 02:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463778">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIS2lkSESOnutze9CxJTV8d5lx1jlmBFAH-h_oroJdTeE2rGb0TzuW1_gOPUfuevtubwU3t1j7CAorcZI2h8pvhioISE2kzOGvj-GV-yWcF7EwSFMGd92i_KEI_oQtRMq0He6DfNrKuAsVNXZQj1d7Twp6A7jId-jleTe3ySOpDfFwxDSI-ECiVMiaaw1ebRm2ranPmvCXo7jcFsFtC74fTXxOGMsvDfHSFFyvn6pxXYS8oRMPGv4udR6X2hiJvmvX8oVJU43Tmw8b_jzB1ks5h9EuQmcvX_5PGr5CVu7vss2ObWx4PLnbZ10PJSKHhgY_xbj5jF7oJRjFlhg7II0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولیمۀ لاکچری رهبر انقلاب به صرف استانبولی‌پلو و سالاد شیرازی!
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی خامنه‌ای: وقتی حضرت آقا تازه از حج تمتع برگشته بودند، همراه گروهی از هم‌درس‌هایمان در جلسات حاج آقا و همکاران مدارس فقهی، برای زیارت…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/463778" target="_blank">📅 01:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4kn9lKX8QG__f6mvkEOWfXKARTgFQGSrKccf4WMZCywFLoMscOqiJnp_SqHiEDioHeCppU6oSVEX2ty730JL31sk4mZ7VWG3pcd6KyTStgj4Efol19nGO3_ezG8uhWTR1fg_m9i1goHoxsk_XzKjdBp8XIIGH08HjR61kBBYDoshRkHkpahHXqLQJIL0mXjE71SLlzRlaX3Ml_miK6di-Xqyi8FW01gmHWF6dzP2WhwzEB5JsvyALJ4v1f_lH7BBTbWXB-xmELu7AoeSRXYv1AwNwdhDsDkbch0A3A7GyKvxjlF5Onn0KhlAMWV3qVb1QALEMARj2hxXpQZ8BfarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbMOlRGRId2p6OTbUIOat2cuirmN-amX4BiwVkk_lHSif72_b3mu0PaIUB6jQEq-hKX0Cmf_RJC4GLb2W3IgJq6UJfTWXkeJx9p-QYErMVxt5lkQTNSAQiV2H6L4lVJXW-stZxBWVbIcxW5Y4aHeVJoxndJj5bBndh9wWM8KqpyWpCqerbwAuyMSib8mWzjVl1WhaZDyYqW6xhjLdn9RBUCUv4k8fcNq6JbNgGC3a0z6UOkmh8ZoDHaapCRtef2es34L8ujzpMmRDAx1JPyCrt7pv5yoWwVfjJ6yjJIsKmDAPkIoF79pRZrhRXMSfehBvbrXnCca7ZMeV_5AUz3oLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7HpgdzX2Sfmn5aJcauVvhDhoXMbr00w6CGXrjqnngNCE6DhZrSklhpGpxNm3EW_sFdn_iktHe2oMbUKa4orbMqQ8mWpzZxgLJlU1ijwL0JW-Jv92DTmwHb8QlZhPr58mWM8ZfElmeiV7kZ2-iC43Dsj1TKy38g6GGjISD6TZcw4FC9VlocWGMiHoZqNMgwal7DCumMV4wYmk9sz_fZae_4GF0Lipq2SEjhq1H0YiVM_tSi6Rr7pagtMy8hyrAephOJQcm3JLzJGpkIHopY4KtKF0EYwXiV-GS9Y9Ket-iPDLM8AYg6znDzdy27sWUwNrLutI81DT8v2rqiedhzEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6CxhWHEu-htLXBUYCCYoSknF6MMxOXFNmrBW6QfUKoPusTfcHST7YY0NMWYiSgy69rIhrWhWP3M_-yxwLGK3YyUaYFC3I_DSUC_PR3IEaer2xxgI8hsdNwfIHTVl2Y7UMuhU_p8Ecu1wMa7BySecVGy4gAq1dWaELv8ji54UWy4mGRKNzVLAU8q1Aqy7-_55c6vUKxIzP5nD4eXF8njJ3mSW8_lkUs85y4_P21Lo_KNfDqmlP0-1ar_7iOVz4NLFb2073emNJN4W4-FSU9UwhAyfxqEsynYuWUMv9lqq8dBKHCnvnj8xqSsxAYxXMdVF963QcFZ2UtUjSOtsc-xrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRGsNTvOJtUTn2OQKaZT08qooP9fYMbDN7gVPVRLt4pBgRl6aIj2_dYl9n47fdUCr_OlpjLcm4ektqFcmEnZB6V93yWjF_NeTVEhMpEyjbDPfycSdcxhibaClotKyKUhnKTWDmB61IUVlHrz-8EYXd3c2G4GyJf14cL7YJcvGIJFf8Bd8-bxuvEvd7wnzIYicQDxp2fEEANe-waIbgF_9ouYxuhS426VzYYQ0fHmHU2ABkGbeEu4KntxIUMYb2TMVBT6E0wFp1nnH95shhqb8b1x3JdeLeMjwyQIdHI2BlrJ5ZJR7DTO4a5qaLiEg4mlNS9u3yyTReHSkR6fEvqf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akyVOGaw2yj9Su5ZWCyTovw6lADWDys4FWyahlMZrZ_X1BdCPEHYu6cqGcn6uWLro6C52x5cuFTnb-_dHvCNM9e8VSVJULrHOWtnGZvWLZJ7Ip7487u_rm5Pc5cYQq95SsMYlX3dDUCi6EHsi-0OClM4yU4C2zbdFmqHhFIa9FLVLjfwqUmIB2enCbWQnMeuRBluWnoSKI326hM3YlooRNDcSfDWRF1TxqOsyMn-gYFM1ZzPAlOGG4_RyuuNx1zpb0v9OC1eMrPwOt_QYEQ2j3nJ1qTj5xIiseLupP5IM56NGJYYzflCKd4zyKgft-MxYqbGkWwoOf5f34xN3fKBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iz4E6RPwK5Jt9sjj1Q2RqRtwFR0Zp8291si0IogpHoxFR7ALOU0hhQHzV7PgUMWqE-zuSPwZchDikRv2vRLDTrAEm-w-HNUfcblzCDgyyORAh-l28FfjE3FMlq0TZWOij_k0Q7BzX5_Z9a-xtvJP0rw31OBxCdV2VyPwEtZbvftwMn7EYMqp9flAQdXks0ylE_cAj9stoXfI1jO3dBjUOoJuJ2pJrTxchYTREgDQja_hxxICfttAaGKrletXKC-xVL2D7oDP4HqJUMltuBaWx2DDEnGaZoK9iS8LfZPL0yVVCaDOyfTI8riLC3vh1itNRwww3ldIjkPixtcwHkqMLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری سخنگوی قوه قضائیه در میناب
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/463771" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463770">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkgIYSEPLE0a83iFlmqvjop_zWs3eFXZrxCXqsuH9j7oHQDi5UX0IV6hiMfr6pgjDJi8fyA0ynjmwmbNqDvzKKydkSGhBXyCHxDYsnCDOaXEb_jxGhRnPE1ss6DKS9AzDiaIbFmae20F7kirX1gKoIq--R-Q7cfawFTJ8GuOGzqwDt4Y58OqqD-IODZXkWcAaBXaFJ_LKWqYYTHIA2tHpEQUQt7satEPbM4ibGNNQ2GXS--vCCRdNSYoI9E9Wj36rXQ2n3FNNVVVgfUDyVpU8C1R4FNBSioax91dfIcwT-V14cekShodW_hSNFTHyDcYylFZ92ymy5DPvM1Ou8RDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
در نخستین روز هفتۀ دفاع مقدس، برج آزادی به قاب پرچم ایران درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/463770" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463769">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دو پرواز دیگر از مقصدهای ایران حذف شدند
🔹
سخنگوی سازمان هواپیمایی کشوری اعلام کرد فرودگاه بغداد و مسقط پذیرش پروازهای ایرانی را از آغاز امروز انجام نمی‌دهند، و در حال رایزنی برای تغییر پروازهای بغداد به فرودگاه نجف هستیم.
🔹
اخوان تأکید کرد که لغو پروازها نشان‌دهندۀ عزم کشورها برای لغو پروازها نیست و صرفا تصمیم شرکت‌های بهره‌بردار فرودگاهی است.
🔹
چند ساعت پیش نیز جمهوری آذربایجان رسماً پروازها به ایران را متوقف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/463769" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCn6Cwpq0An3bAr1zdI97D1ukuTQ-TVWm9Q1z7x4SqiEgMR-LyqTecp3tFdfCbDVL3RIXh6YxA7o_tR4N-HtsR1TXQe5Fb4YOubriyceneSRbg0uKccwhty4wPh3t_Uo-OffFNbIJH-uNZ4KmdX6RFaL-6JOvbHhzru6aIm06O4dwsZyBOX2bW5CTb82JGiYacisXPqVl-DbQ_YoaYVRCnO0mWGAV7P0doS1ChWFgHVrxsH9j7pfw2SuXblN5w00ue-YEB6zC_wuaLbSf6i5LU8h3t8u8QuCEYRXY1Pizrj5EQ0PHOIaAcztx_4CY1D2WVAThhNkzO0p0oKRSqQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان در سفر به نیویورک، در توقفی کوتاه با وزیر کشور الجزایر دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/463768" target="_blank">📅 00:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMNYBarhq7l3xgwAGL_0TGOZ4h1HVHvZlkT1y_20HFJJ4zYGtXvG1AKEXaIa0SPMzn5xZizXYBQtHCekfH4PArQz7u76leZ2RfgAXZa06V385oyYrY9FKmpG_sTorf4oUSVERsrk838U67rLKmbOMRgQcPrhLDBdQw40u45kTzkeidKgIAQHhjHd0Xn0PXg1JVhl3-m2_ryGLH4jz5kaBWJN9Ggi7FxmD5Uop3MDIUJ6o2-x3j5uZH3udCDG_yZMfdGVOAthTqJcQTOGSIfc1H2yWdr8h2oP8Y5lEB1oh_RiVKy4YulOIZtL-1FbaoK8dYgIYoB-j-jSsvlw91VHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسانی پزشکیان را در سفر به نیویورک همراهی می‌کنند؟
🔹
۶ نفر به‌عنوان تیم سیاسی و تشریفات، رئیس‌جمهور را در سفر به نیویورک همراهی می‌کنند. اعضای تیم حفاظت و کادر پرواز نیز به این تعداد اضافه می‌شوند.
🔹
محسن حاجی‌میرزایی، رئیس‌دفتر رئیس‌جمهور، و سیدعباس موسوی، مسئول تشریفات دفتر رئیس‌جمهور، از جمله همراهان پزشکیان هستند.
🔹
عباس عراقچی وزیر امور خارجه، کاظم غریب‌آبادی معاون حقوقی و بین‌الملل، اسماعیل بقایی سخنگو و علیرضا میریوسفی مدیرکل رسانه‌های خارجی وزارت‌خارجه نیز در نیویورک حضور دارند.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/463767" target="_blank">📅 00:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات موشکی عربستان به شمال یمن
🔹
منابع یمنی گزارش دادند عربستان مناطق «مران وحیدان» و «الظاهر» در غرب استان صعده را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/463766" target="_blank">📅 00:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197e752b37.mp4?token=THAJ3tzZDYpDqKwrmiIm1ROSSfrpyQhLcXHa8MMiR5JOYNd_6KoYwjjNT1oBoUa9NpF_zi9OT4D5siJNAcsIeabfF5OofmiHg769S2U9K9_nSy-ZcjXHezBihMzPuBkqIMmzg5GtnuSiUig0F74bGKx9yLGPKealH8gjhdBrmaxn1sr93SJaGe0mqrTv0CSTRRIWEA3Nojkb65xw3DDKRvwbrkVsqIxLajClhwYmIBHcUJmvcz_db7OsR6pLeY7n8XCRiFfv3sTiMTzvtDU6KijOegs2cysd181Bo1iuB-0YiFCFfR3UpFIXxcWJQzvk5DQT3T2EOMsn7lGxi1u4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197e752b37.mp4?token=THAJ3tzZDYpDqKwrmiIm1ROSSfrpyQhLcXHa8MMiR5JOYNd_6KoYwjjNT1oBoUa9NpF_zi9OT4D5siJNAcsIeabfF5OofmiHg769S2U9K9_nSy-ZcjXHezBihMzPuBkqIMmzg5GtnuSiUig0F74bGKx9yLGPKealH8gjhdBrmaxn1sr93SJaGe0mqrTv0CSTRRIWEA3Nojkb65xw3DDKRvwbrkVsqIxLajClhwYmIBHcUJmvcz_db7OsR6pLeY7n8XCRiFfv3sTiMTzvtDU6KijOegs2cysd181Bo1iuB-0YiFCFfR3UpFIXxcWJQzvk5DQT3T2EOMsn7lGxi1u4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل ترور شهید کاک درویشی چگونه عملیات تروریستی را اجرا کرد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/463765" target="_blank">📅 23:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=KIDOSn4-4UvMhkWV58kSTu_Akr3kSKES2xvXOW2b25XaHGhaBf5GM7eM7Akp71NONfHUDrue5VFwkRlMrx11SyD-MMl7RLgjhDjdoTpiGL01rzUM96wlF12Ef-WBiIQ_LKoPLU3SQv23HOKK5uUmY3TGVUNvpacjVr4pPxLWjwTNaVUOUPmJe8xXF7pDIF-OG2UqF7IgqoWPlC9JW4bfE0VO-RNrRhaOmnth8fmznkyKBcrRuZxuM6JMuMsv5E80kVBkXILswrzj7ohOCMDcpCL_ns_dvfDSWmglWeCndFQl64uz-VW1eDDY6KL6n4WVp-5Kk3n5LKJL2kImXpdLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=KIDOSn4-4UvMhkWV58kSTu_Akr3kSKES2xvXOW2b25XaHGhaBf5GM7eM7Akp71NONfHUDrue5VFwkRlMrx11SyD-MMl7RLgjhDjdoTpiGL01rzUM96wlF12Ef-WBiIQ_LKoPLU3SQv23HOKK5uUmY3TGVUNvpacjVr4pPxLWjwTNaVUOUPmJe8xXF7pDIF-OG2UqF7IgqoWPlC9JW4bfE0VO-RNrRhaOmnth8fmznkyKBcrRuZxuM6JMuMsv5E80kVBkXILswrzj7ohOCMDcpCL_ns_dvfDSWmglWeCndFQl64uz-VW1eDDY6KL6n4WVp-5Kk3n5LKJL2kImXpdLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه ۳ از وضعیت مردم غزه
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/463764" target="_blank">📅 23:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
امروز
برای ثبت‌نام فرزندم در مدرسه دولتی
شهید مصطفی طاهرخانی در شهرستان تاکستان استان قزوین مراجعه کردم، اما ا
ز من درخواست پرداخت پول برای ثبت‌نام شد
. حتی اخبار و اطلاعیه‌های منتشرشده درباره ممنوعیت دریافت وجه را به مدیر مدرسه نشان دادم. ایشان نیز
تأیید کردند که از این موضوع اطلاع دارند اما گفتند مدرسه باید از خانواده‌ها پول دریافت کند
.
🔹
صدای ما
زنان خانه‌دار
را به گوش دولت برسانید. من زنی بی‌سواد، خانه‌دار و دارای دو فرزند هستم و در دهک یک قرار دارم. همسرم کارگر است و با حقوق کارگری،
تأمین هزینه‌های زندگی و تحصیل بچه‌ها بسیار سخت شده است
. ما زنان خانه‌دار که مهارت و تحصیلات کافی برای ورود به بازار کار نداریم، چه حمایتی می‌شویم؟ تنها یک یارانه به حسابمان واریز می‌شود و حتی برگزاری یک تولد ساده برای بچه‌هایمان به آرزو تبدیل شده است.
🔹
خواهشمندیم
شهرداری منطقه ۱۵ تهران
به موضوع استفاده شخصی و
هدررفت آب فضای سبز در کیانشهر و شهرک شاهد
رسیدگی کند. گفته می‌شود این آب به برخی منازل لوله‌کشی شده و به ‌دلیل رایگان بودن، برای شست‌وشوی فرش و خودرو مصرف می‌شود. همچنین اطراف میدان امام رضا(ع) کیانشهر، لوله آب مورد استفاده تانکرها به‌صورت مداوم باز است و حجم زیادی آب با فشار بالا هدر می‌رود. خواهشمندیم شهرداری منطقه ۱۵ موضوع را بررسی و با هدررفت و استفاده شخصی از آب فضای سبز برخورد کند. در شرایط کم‌آبی ادامه این وضعیت قابل قبول نیست.
🔹
تعداد زیادی از
مردم
شهرستان بدره استان ایلام
که پارسال
به علت نوسانات برق کولرهایشان سوخته بود
، برای این افراد در سایت وزارت نیرو پرونده تشکیل شده، کارشناسی و تأیید خسارت نیز انجام شده و هزینه بیمه هم در قبض برق از مردم دریافت شده است، اما با وجود گذشت یک سال
هنوز خسارتی پرداخت نشده
و کسی پاسخگو نیست. لطفا این مشکل را هم منعکس بفرمایید.
🔹
بنده
فرهنگی با ۲۰ سال سابقه نیروی آموزشی آموزش و پرورش ناحیه یک اهواز
م هستم که تمام این
سال‌ها در مناطق محروم و روستایی خدمت کردم
و همیشه به‌جای گلایه، سعی کرده‌ام مشکلات مدارسی را که در آن‌ها خدمت می‌کردم در حد توان خودم برطرف کنم. هر روز با خودروی شخصی حدود ۱۰۰ کیلومتر مسیر رفت‌وبرگشت تا محل کارم را طی می‌کنم، اما در تمام این سال‌ها هیچ کمک، یارانه یا سوبسیدی از هیچ ارگانی دریافت نکرده‌ام و حتی اداره آموزش و پرورش برای ما سرویس ایاب‌وذهاب نیز در نظر نگرفته است. با توجه به شرایط اقتصادی و مشکلات معیشتی فرهنگیان، خواهشمندیم لااقل برای
تأمین بنزین رفت‌وبرگشت
همکارانی که با خودروی شخصی به مدرسه می‌روند چاره‌ای اندیشیده شود.
سهمیه فعلی حتی برای یک هفته هم کفاف نمی‌دهد
و پس از آن مجبوریم بنزین را با نرخ ۱۰ هزار تومان بخریم. تا امروز هیچ‌وقت گلایه نکردم اما واقعاً شرایط روزبه‌روز سخت‌تر می‌شود.
🔹
من ۲۵ سال است
کارگر ساختمانی هستم
و حدود ۵ سال سابقه بیمه دارم. ۹ سال پیش در تهران بیمه بودم اما به ‌دلیل مهاجرت به شهرستان،
بیمه‌ام قطع شد
. از آن زمان تاکنون منتظرم در شهر خودم بیمه شوم اما هر بار می‌گویند سهمیه نداریم.
🔹
مربیان پیش‌دبستانی
که سال‌ها در مدارس دولتی با امید استخدام در آموزش و پرورش کار کرده‌اند و کلاس‌های ۳۰ تا ۳۵ نفره را با حقوق ناچیز اداره می‌کنند؛
حقوق امسال ما فقط ۷ میلیون و ۹۰۰ هزار تومان است
. این در حالی است که شهریه دریافتی از هر نوآموز سال گذشته ۱۸ تا ۲۲ میلیون و امسال حدود ۴۰ میلیون تومان بوده اما با وجود افزایش شهریه، ما مربیان
به‌تدریج در حال بیکار شدن هستیم
.
🔹
خواهش می‌کنیم مسئولان برای
قاچاق سوخت و تردد خطرناک خودروهای سوخت‌بر
چاره‌ای جدی بیندیشند. چند روز پیش در محدوده
حاجی‌خادمی شهرستان میناب
یک خودروی سوخت‌بر با سرعت بسیار زیاد با پسری حدود ۱۵ ساله برخورد کرد و این حادثه جان آن نوجوان را گرفت؛ راننده نیز متواری شد. تا کی باید شاهد پرپر شدن جوانان و داغدار شدن مادران باشیم؟ قاچاق سوخت نباید به قیمت جان مردم تمام شود.
🔹
می‌خواستیم صدای
کادر درمان
باشید. در شرایط سخت و اضطراری، ما
به‌صورت دائمی در شیفت هستیم و با کمبود نیرو، اضافه‌کاری اجباری داریم
در حالی که هر ساعت اضافه‌کاری حتی نصف هزینه رفت‌وبرگشت با اسنپ را هم پوشش نمی‌دهد. حقوق ماهانه حدود ۲۵ میلیون تومان با این حجم کار و هزینه‌های زندگی واقعاً باورکردنی نیست. قرار بود از ابتدای سال ماهانه ۴ میلیون تومان کمک‌هزینه به پرسنل پرداخت شود، اما تاکنون فقط دو ماه آن پرداخت شده است.
🔹
روستای جهان از توابع شهرستان بام و صفی‌آباد خراسان شمالی
چند سالی است با
کمبود آب آشامیدنی
مواجهه شده است هر چند مسئولان آمدند و رفتند اما مشکلی حل نشد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/463763" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
جلسۀ ترامپ با سران کشورهای خاورمیانه  @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/463762" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">واکنش مقام ایرانی به ادعای ترامپ: در صورت تجاوز دشمن برای توسعهٔ جنگ آماده‌ایم
🔹
یک منبع ارشد امنیتی در تماس با فارس در واکنش به صحبت‌های غروب سه‌شنبهٔ ترامپ در سازمان ملل اعلام کرد: آمریکا خط قرمزی در منطقه باقی نگذاشته و ایران برای تمامی سناریوهای موجود…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/463761" target="_blank">📅 23:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef896db23d.mp4?token=mZhe9xo-C88OAqexBpbk4-_C1oMOCujD8WUJuOcBqpxfUaixkqMtCI8LzHK9WTkfmJyYB0xybGkeH5vwu-I5P-CKbPWTOkDfh_AmQKFH3G6cbSU6d6yId8cX81IOEQDbRVBUxmu8oQ24029gDji4SB0DywQkVBqOnEfFI3VFQPwQRBtIjwO8J_lQCoV6oUHiQnliIuoX0oGh33oQDxF55iRE5jsC-9ESUYpZTyJrZ6982a3p_BSu43i2y6H93Su_0OL2xFwk4kN3hsR-tT8xstZUuiJoloNc6CKmUg2kymWlxBtkq3hEHegofnbi-vUy2ysX3ShnpfI2f2aHkO4tcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef896db23d.mp4?token=mZhe9xo-C88OAqexBpbk4-_C1oMOCujD8WUJuOcBqpxfUaixkqMtCI8LzHK9WTkfmJyYB0xybGkeH5vwu-I5P-CKbPWTOkDfh_AmQKFH3G6cbSU6d6yId8cX81IOEQDbRVBUxmu8oQ24029gDji4SB0DywQkVBqOnEfFI3VFQPwQRBtIjwO8J_lQCoV6oUHiQnliIuoX0oGh33oQDxF55iRE5jsC-9ESUYpZTyJrZ6982a3p_BSu43i2y6H93Su_0OL2xFwk4kN3hsR-tT8xstZUuiJoloNc6CKmUg2kymWlxBtkq3hEHegofnbi-vUy2ysX3ShnpfI2f2aHkO4tcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلسۀ ترامپ با سران کشورهای خاورمیانه
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/463760" target="_blank">📅 23:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📷
پزشکیان در سفر به نیویورک، در توقفی کوتاه با وزیر کشور الجزایر دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/463759" target="_blank">📅 23:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صداوسیما خبر دیدار عراقچی با ویتکاف در حاشیۀ مجمع عمومی سازمان ملل را تأیید کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/463751" target="_blank">📅 22:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcQSNwOk93hPObxAvzbGuVhT0RBIWCHIIjoPjunDAzQcVFh2ncGchke4-v_auZgoVz8VkKYQP7-6z0eAPoRitGkeGurjBBWSHzknnERpUJw2iCjdftjytBgZgKD9URMOCqi_gxOMiPeJxh9wBV9HYLrdV-y7SPE5O_loC7IV2-BZI2XHMDPZvLSb3IunweZc9G4ZDQAmU-Wo8I55JXdNsuFeoew6KyuwVR37zYdIq8V43rybss74DApY2XQr83592olm06Cki8dDVQUJMYkH95hKapafEjftvmiKGG7lfh-FWw16Yen40mS3v0oy5mCYrPuSsNhG20lkl4eN-djCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عددبازی پنتاگون با جان نظامیان آمریکایی: ۶۰ نفر دیگر به زخمی‌ها اضافه شدند
🔹
ارتش آمریکا نام ۶۰ نظامی دیگر را به فهرست نفراتی که در جنگ با ایران زخمی شده‌اند اضافه کرده است.
🔹
با این آمار ایالات متحده تاکنون کشته و زخمی شدن ۷۷۶ نفر از نظامیان خود در نتیجه…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/463750" target="_blank">📅 22:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REasGnzGR9cBx8MVs6-s6IOwUtBue4x01KvsCIYcFJxStfMKxVm9kLO6qLhygLoxMQca_nWZs3rqQ5P-pJzg3WtSdf0r4f_0l0h5ZUX0JPX6mgiQvgcJiX9jL7tivdmevGxu7ps4KqyMYffQsbpiXr80M7sZg03SJNHmXqvcDbuST4cgmjBprVWaS-n3ikbE4NSJv5hv9wO15JQgNVBBcUwX26-o5t2nPcliX9AW-YV8n1d1Q1QgCR29iF7va5B0oTAYnYkByCG-mjmoD9BuyhLLYrJ2E7u4v7vEOmPmuXQVeMcCkQeMs_-kSGVDmOpXt9y1i4EEa9J4AT34J8g3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کشورهای عربی خلیج‌فارس به ترامپ: درگیری با ایران را تشدید نکن!
🔹
یک رسانه آمریکایی به نقل از چندین منبع آگاه نوشته مقامات ارشد کشورهای عربی حوزۀ خلیج فارس قرار است در دیداری با ترامپ که ساعاتی دیگر برگزار می‌شود، از او می‌خواهند از هرگونه تشدید درگیری‌ها با ایران خودداری کند.
🔹
طبق این گزارش، کشورهای عضو شورای همکاری خلیج فارس که میزبان پایگاه‌های آمریکایی هستند، خواهان پایان درگیری‌ای هستند که در جریان آن، سرزمین‌ها و کشتی‌های آنها هدف هزاران موشک و پهپاد ایرانی قرار گرفته و اقتصادهایشان نیز، عمدتاً به دلیل اختلال مداوم در تردد کشتی‌ها از تنگه هرمز، با رکود یا کاهش شدید رشد مواجه شده است.
🔸
با این حال، میان دولت‌های عربی خلیج فارس دربارۀ نحوه تعامل با ایران و اصرار تهران بر اینکه حق کنترل کشتیرانی در این آبراه حیاتی برای انتقال انرژی را دارد، همچنان اختلاف‌نظر وجود دارد. با وجود این، آنها امیدوارند دیدار با ترامپ به پیشرفت در مسیر پایان دادن به جنگی منجر شود که آمریکا و اسرائیل در اواخر فوریه آغاز کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/463749" target="_blank">📅 22:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07e321a04.mp4?token=VgP_jDbBLCR5H_I79V_nogse3wbmB7CgOxi_f6wsMWPh6ZY3XhUsnAuopahhgD7BSZ7eXMnlOHhdJZP-XPQwACWZcFGFhwxGwRXXT0YVFA_RysUcTFEcxKCAyKIIHb7Fx8jazZr98HftCb6t01LrtjOwJ4Em4kewi7axlJZmT3cw-2QgMR_uBi9LeTrGxrSrKj2oNvH2g1zzVXhRQaGCGX8EeJD7TPAinKsP83QLb4q-XQwuXaoXac4c7npqYfmLYpDivps0SzMl-XFWvlinpARrQZGEieDmkmm-fXLZI7GFm0NvDEMKEuhKdxalRvncxmgUdqmqUX0e-niHl-MYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07e321a04.mp4?token=VgP_jDbBLCR5H_I79V_nogse3wbmB7CgOxi_f6wsMWPh6ZY3XhUsnAuopahhgD7BSZ7eXMnlOHhdJZP-XPQwACWZcFGFhwxGwRXXT0YVFA_RysUcTFEcxKCAyKIIHb7Fx8jazZr98HftCb6t01LrtjOwJ4Em4kewi7axlJZmT3cw-2QgMR_uBi9LeTrGxrSrKj2oNvH2g1zzVXhRQaGCGX8EeJD7TPAinKsP83QLb4q-XQwuXaoXac4c7npqYfmLYpDivps0SzMl-XFWvlinpARrQZGEieDmkmm-fXLZI7GFm0NvDEMKEuhKdxalRvncxmgUdqmqUX0e-niHl-MYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: آمریکا سرانجام از منطقه خارج می‌شود؛ ما می‌مانیم و کشورهای عربی!
🔹
هدف ما این است که تهدید را برای همیشه از سر ملت ایران برداریم و امنیت پایدار را برای منطقه بدون حضور آمریکا تامین کنیم.
🔹
ما براساس مبانی خود قصد کشورگشایی و براندازی در کشورهای…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463748" target="_blank">📅 22:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f4cb5e80.mp4?token=vaq3ljvtjB6D7ypLtXxB0y9esOkJlHS9wqNv3tssZfwSxE9j5OkTa8mDAo-TOxwGl_7B2SieopILx4cMn74EBtAZAY051qiafyl2Yfm8dB_nccaO3R9bAUxgiVDp8Wv9BdERB7AtmoVahFF05zPGCNORPSVmsjYJA_oFG5YYwepqmsm9ob4BshbwuTtfRoELs5BAe0aSd0aIEVC_FH-H70huZUz1_fctc9KG5k39in85aXQ9if27FPlS7IlXZ3CqtKgTxIDkhzkMsWhwzdHTEncKoaXstwqXzUJuXElKbupL_qDDF7HI9S1asBBzf0xF19N8vr4KB3SU8xR6ewKt0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f4cb5e80.mp4?token=vaq3ljvtjB6D7ypLtXxB0y9esOkJlHS9wqNv3tssZfwSxE9j5OkTa8mDAo-TOxwGl_7B2SieopILx4cMn74EBtAZAY051qiafyl2Yfm8dB_nccaO3R9bAUxgiVDp8Wv9BdERB7AtmoVahFF05zPGCNORPSVmsjYJA_oFG5YYwepqmsm9ob4BshbwuTtfRoELs5BAe0aSd0aIEVC_FH-H70huZUz1_fctc9KG5k39in85aXQ9if27FPlS7IlXZ3CqtKgTxIDkhzkMsWhwzdHTEncKoaXstwqXzUJuXElKbupL_qDDF7HI9S1asBBzf0xF19N8vr4KB3SU8xR6ewKt0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: یکی از اهداف آمریکا تسلط بر نفت ایران بود اما ایران حالا جریان نفت دنیا را کنترل می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463747" target="_blank">📅 22:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXWI0hO4_atsbugCbk7INkGvFZN4Z--0dti2AkHMoQdTtZHctlVEgl1F61jjcPqfrbcTCETD4Rp1tGFyCNaox_-IScloAJ58saJI7zQpt7V1DfKEEQoF-yM9E9ZisVYr7EoX658DcI141w5bHFbJrLL99XBUkYBaG_aUsAlHplajSIptcxXXHTR2FZ5rdr-c1iZwEp2lSvVy198sfc732uBpQLR0z4Z0P040DjNsLfFB9sRRkFboH2gWy5XK3JjMIHFnOAUrl8NohTgHJSslpcC4NMYItrHVq5gSXpKmSKHKrWOdFIqRQtWiTOS3TILFaxYzL8vLwPaiUXQikhQcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: واحد یک نیروگاه بوشهر با ۱۰۰ درصد ظرفیت فعالیت می‌کند
🔹
مدیرعامل شرکت روس‌اتم الکسی: در حال حاضر ۶۳ متخصص روس در نیروگاه اتمی بوشهر حضور دارند.
🔹
لیخاچف در بیانیه‌ای با اشاره به روند ساخت‌و‌ساز در این نیروگاه گفت: در حال حاضر، تلاش‌های ساخت‌وساز بر احداث ساختمان‌های راکتور و تالارهای توربین برای دو واحد نیروگاهی متمرکز است. واحد اول عملیاتی با ظرفیت ۱۰۰ درصد کار می‌کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463746" target="_blank">📅 22:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986e451529.mp4?token=vqZ5E0mtN9AOhpvypjpXuevHSURvpQLLo5S_dKUnYvLGj_IHX_iVgKtfEF60ioX_Rhr_whzoAKRhYCuwVCHjJOD9ji2n3mfOAnQCLQAKGE--WMfBKk0qWPQ2pkYk0AxuWfxMobLwKdDUdQ-fC1mJEWqXouX_Cz3QDMUZgtddfydxWx_ZzQVhWQLGj7TpcrtYjIzjaTyP7aKQmvoXs_vA943LTLahXZXzqCijCyFvkw2N7gUt5DlrJPBQfIndwarQ9q6YWw-YUDl_dae-bFuFSNzsPb38Tv3FOqeSVeY-gLfBm_xnmqGxh1hTpWkP1auoq5KaIGaYhamEsjWxzoumYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986e451529.mp4?token=vqZ5E0mtN9AOhpvypjpXuevHSURvpQLLo5S_dKUnYvLGj_IHX_iVgKtfEF60ioX_Rhr_whzoAKRhYCuwVCHjJOD9ji2n3mfOAnQCLQAKGE--WMfBKk0qWPQ2pkYk0AxuWfxMobLwKdDUdQ-fC1mJEWqXouX_Cz3QDMUZgtddfydxWx_ZzQVhWQLGj7TpcrtYjIzjaTyP7aKQmvoXs_vA943LTLahXZXzqCijCyFvkw2N7gUt5DlrJPBQfIndwarQ9q6YWw-YUDl_dae-bFuFSNzsPb38Tv3FOqeSVeY-gLfBm_xnmqGxh1hTpWkP1auoq5KaIGaYhamEsjWxzoumYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: آمریکا می‌خواست تنگۀ هرمز را باز کند اما تنگۀ باب‌المندب هم دچار مشکل شد  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463745" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/463744" target="_blank">📅 22:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416a1505f7.mp4?token=T8yzXFcwIu9po2f4yu90okJONU7PfMgLXtIzk7rhFGW1gdvsOjjGegEnIBsiftGUWatOgVkRXOjkKKL9-29_aaRk9RQizjTPUgcmkiPwO1WVXvvQLhz9mW7qkeNFC7AJHTCvGqQ3QWeLxTjDLrwZEf_J8SckNL3WK5AAlCII_Zc1ewMCm27EcHiDsdoVWsdQXTSc5WzmNAS-IFFw72Bc4CNNrIiiqj208GWr_Rw8aAV-FZoeUX8YoJ2nJaFI7_BVnpdlMuHElcMM2SXpUCBi-4VnDCk9IcFnQOhy_DEEqJBl-_6CKkt1RjV4bD6U73RNnuLpqbVXQJqen98Pbc_IKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416a1505f7.mp4?token=T8yzXFcwIu9po2f4yu90okJONU7PfMgLXtIzk7rhFGW1gdvsOjjGegEnIBsiftGUWatOgVkRXOjkKKL9-29_aaRk9RQizjTPUgcmkiPwO1WVXvvQLhz9mW7qkeNFC7AJHTCvGqQ3QWeLxTjDLrwZEf_J8SckNL3WK5AAlCII_Zc1ewMCm27EcHiDsdoVWsdQXTSc5WzmNAS-IFFw72Bc4CNNrIiiqj208GWr_Rw8aAV-FZoeUX8YoJ2nJaFI7_BVnpdlMuHElcMM2SXpUCBi-4VnDCk9IcFnQOhy_DEEqJBl-_6CKkt1RjV4bD6U73RNnuLpqbVXQJqen98Pbc_IKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویر شکار مزدوران سعودی را منتشر کرد  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/463743" target="_blank">📅 22:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d3d62672.mp4?token=BDbhcuBAX-_uS8YpyY1c6QN2lKD2anJ2nxzjx0iQVRKeRfuafJjkNWXN3QLuZ65wF2EkXi34c8dhLKF0RKvwdDQ9vSCHDsCf1DoLqPES2uZTGAEgZtU-nHUGUKUD70KLGAch4QkTwBu80b4xjAU7YtIzkHbKyW38zZD2vVJPepZ487tRq5IdEKQLgiDPJJRuV9iQAIC41XdqBOeMhvf3KTjvogdOScaZF8GXNhG5ik7_fSumHLuii73bjLl9ruJeNOdrR-XxYyUkuopMXvMBKUum_1z4XH6JXRxazmyeHl5DfaPwlv1GJarux252kDOvAnybdbALJTZa9UOfMdd7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d3d62672.mp4?token=BDbhcuBAX-_uS8YpyY1c6QN2lKD2anJ2nxzjx0iQVRKeRfuafJjkNWXN3QLuZ65wF2EkXi34c8dhLKF0RKvwdDQ9vSCHDsCf1DoLqPES2uZTGAEgZtU-nHUGUKUD70KLGAch4QkTwBu80b4xjAU7YtIzkHbKyW38zZD2vVJPepZ487tRq5IdEKQLgiDPJJRuV9iQAIC41XdqBOeMhvf3KTjvogdOScaZF8GXNhG5ik7_fSumHLuii73bjLl9ruJeNOdrR-XxYyUkuopMXvMBKUum_1z4XH6JXRxazmyeHl5DfaPwlv1GJarux252kDOvAnybdbALJTZa9UOfMdd7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: آمریکا می‌خواست تنگۀ هرمز را باز کند اما تنگۀ باب‌المندب هم دچار مشکل شد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463742" target="_blank">📅 22:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واکنش مقام ایرانی به ادعای ترامپ: در صورت تجاوز دشمن برای توسعهٔ جنگ آماده‌ایم
🔹
یک منبع ارشد امنیتی در تماس با فارس در واکنش به صحبت‌های غروب سه‌شنبهٔ ترامپ در سازمان ملل اعلام کرد: آمریکا خط قرمزی در منطقه باقی نگذاشته و ایران برای تمامی سناریوهای موجود آماده است.
🔹
به‌گفتهٔ این منبع ارشد، در صورت آغاز جنگ جدید، ایران از «توسعه جنگ» هراسی ندارد و آماده است پیروزی بزرگتری از پیروزی قبلی در جنگ پیشین را به دشمن تحمیل کند.
🔹
این منبع امنیتی با تشریح اینکه ایران از آغاز جنگ جدید چند مدل مختلف از انواع موشک‌های ضدناو و زمین‌به‌زمین را با موفقیت آزمایش کرده، تأکید کرد تحقیق و توسعه و ساخت سلاح‌ در ایران به‌طور کامل به زیر زمین منتقل شده و به صورت ۲۴ ساعته ادامه دارد.
🔸
ترامپ ساعتی قبل در سخنرانی سالانه خود در مقر سازمان ملل در سخنانی گزافه‌گویانه مجددا «ایران را تهدید به نابودی» کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/463741" target="_blank">📅 22:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqzUAkiLDcnYF1kbLHxrRPpcUa1sta4CxtFdeV487C9SukS-e0NjWTHeDNcib0is0ATyPFmKWkPtyMxoLy2l8ajBu-kvk4tWJqX8LsuYppxlzlTKCIIHEsbO9f0ePmx9TmnRZOS9-PH1dIoVFjnHr8_huDGEipXsw7AdIVp32adU_kaPa618RaHETklkm2ASqFBXCjO8gwRfmjIyyTyLfPCyUy0n-uGdSw7CelEbX36SAdh6WPqjKPe7t2SEy0TlAVTUn_d14mh9p-igHo746ZKMns6wWJGWD6v5iglPlMIWy6Ryz-ZsfHqerm55PX-jju6rTC3r68Ol2kWdAxvFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اروپا مسیر مماشات با قلدری آمریکا را برگزیده است
🔹
وزیر خارجه در گفتگو با مسئول سیاست خارجی اتحادیۀ اروپا: پیمان‌شکنی مکرر آمریکا تنها عامل اخلال در روندهای دیپلماتیک بوده و اتحادیۀ اروپا نیز متاسفانه در موارد متعدد به جای پایبندی به اصول مورد ادعای…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/463740" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6ZgrkYLiC3DWt0H2WuiHdE-ZfCbssvSn9lHF7wmvfoUXhz_DN1fMhElGdlQQwGUVRw3fjs7Dk4LrItbtqyD5EUxuAga1L-GApj7_oqN9IBwx3b_52H0XEDgStstZ6jac3CIYFcl88vrE1-ujO4XxCsIwRZrH3_Jf7j6VRKCrV89YeeCUchwa-x7i95TCT6w2B3wjQ3cs3UgKU2ItKYpq-Rv715Y6qYa4ZUHNkRGle8c0f5l-QGMti0nQY18BDZ07D15I9AXD_7AfPySW7kQMy-Z9WSlp5CMsY7oYk9TknUwEb9YwJzUzyBRHTMUCRcWDmhBGUPA91FOsAeF4-LWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی با مسئول سیاست خارجی اتحادیۀ اروپا در حاشیۀ مجمع عمومی سازمان ملل متحد دیدار و گفتگو کرد @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463739" target="_blank">📅 22:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfde8fd33.mp4?token=oH9pvQf4X9AxR3tHS94I-19TOgC0_4d-H7GloCbcJWIubymg6smL6IXr7K7l4bOWOqWNTpQBMVDori4h1nsBfaquoEgdKrEP2m3TPE0sPVY8E8sG4jMznHqWSqDNH6XXtlvs4ZwJoymgUGnf6gLF2Syrh6YOvmioPJXZEGelPoTkR1-kiFmw18a2aMkA_4anzASdsmVWlQ8IbjM_rshau08kfEKXhoPqO4AHsI0AmNu2p0JA16cL06tE5cu9P4xkFkzT06sPzf6fvvn_zlABwNaiiyQIA11ZmffPmjVzvGsw5BmtwxehzczVbdDKdEIlayj6Sl5UlViB79WZ1EKd9Vq4KKaMrkHaMkz605VEqf4aJamB2EudXKpGxtNHsoFNYInOha_gXo0TYFSPx1GIlVQDPdJuw32dZsWcJyEofI4MOGZBThAF30NPHP43F-frR1hQ0WLDeTT6VhvMxiRSmcRXxa1Shd0E3pZ0LjGql1Cyf8HOX3GRhQM-GzndQOG83oM6n3k22vdRRFAsgy6EuE_unhKsrejJNHVRFwmXmQagOlzST-1kzYm8-cbx8bZhMHlJx8uipC50qrywsf51bNDHwEyAn4E7i3AZ4f-CRaZhFs8Y9Dav-l2P4ygqlyG3OM-jWnJGT22QOcsKZiCmak7Xl8OXWTXd8o5FRz0BHCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfde8fd33.mp4?token=oH9pvQf4X9AxR3tHS94I-19TOgC0_4d-H7GloCbcJWIubymg6smL6IXr7K7l4bOWOqWNTpQBMVDori4h1nsBfaquoEgdKrEP2m3TPE0sPVY8E8sG4jMznHqWSqDNH6XXtlvs4ZwJoymgUGnf6gLF2Syrh6YOvmioPJXZEGelPoTkR1-kiFmw18a2aMkA_4anzASdsmVWlQ8IbjM_rshau08kfEKXhoPqO4AHsI0AmNu2p0JA16cL06tE5cu9P4xkFkzT06sPzf6fvvn_zlABwNaiiyQIA11ZmffPmjVzvGsw5BmtwxehzczVbdDKdEIlayj6Sl5UlViB79WZ1EKd9Vq4KKaMrkHaMkz605VEqf4aJamB2EudXKpGxtNHsoFNYInOha_gXo0TYFSPx1GIlVQDPdJuw32dZsWcJyEofI4MOGZBThAF30NPHP43F-frR1hQ0WLDeTT6VhvMxiRSmcRXxa1Shd0E3pZ0LjGql1Cyf8HOX3GRhQM-GzndQOG83oM6n3k22vdRRFAsgy6EuE_unhKsrejJNHVRFwmXmQagOlzST-1kzYm8-cbx8bZhMHlJx8uipC50qrywsf51bNDHwEyAn4E7i3AZ4f-CRaZhFs8Y9Dav-l2P4ygqlyG3OM-jWnJGT22QOcsKZiCmak7Xl8OXWTXd8o5FRz0BHCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ۲۰۶ شب را ساختند؛ خیابان هنوز شاهد حضورشان است
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463738" target="_blank">📅 22:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6504102bd7.mp4?token=BKQ7jRSwQF8w52wsExzZmp9lwJqlVcUujzdBHy1-QYox2jkgWwumV-As88sGAS3tUuj37ETQ9dawW2fHvxurZqDD2_IeWYcK4PjBUAL65IA8gY6--sei1mNSHD5MkwQMKSYsgHcEP670tEIf31NAl3wgJb08h0JAWMe6NNsDlwwpwYMRBX9V3TigjWvTIGuCacqMCmmv2hFD8QGC3FyCp4XYOiR8OMGlBKEBZAal1ZCbfs2E6sndjlnZNzPPU1wzmZPdsYbt2bE7sMoQDwSJlnLADciRi8wA-mJyLkPYuNM2mUdXpELqi1J9359bgVd_j5BqbsBy3FXHw1wYb8LoZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6504102bd7.mp4?token=BKQ7jRSwQF8w52wsExzZmp9lwJqlVcUujzdBHy1-QYox2jkgWwumV-As88sGAS3tUuj37ETQ9dawW2fHvxurZqDD2_IeWYcK4PjBUAL65IA8gY6--sei1mNSHD5MkwQMKSYsgHcEP670tEIf31NAl3wgJb08h0JAWMe6NNsDlwwpwYMRBX9V3TigjWvTIGuCacqMCmmv2hFD8QGC3FyCp4XYOiR8OMGlBKEBZAal1ZCbfs2E6sndjlnZNzPPU1wzmZPdsYbt2bE7sMoQDwSJlnLADciRi8wA-mJyLkPYuNM2mUdXpELqi1J9359bgVd_j5BqbsBy3FXHw1wYb8LoZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
🔹
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
🔹
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/463737" target="_blank">📅 22:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBo0hFuyJHSMuj0DcPV9GbuEVv8fGpdMwhiZocP4ziNEvVV0QiMsBqRvomgXWtg-Yaux2edTcFXutTodumV5FpH58zVzHclDcbUAxA6U6OlL08JcjjwcNIJjX9TVF0PkxAQbR_3zPjvCDmSfZBHzLMBSQbETPAHPx61g7XcLna_MrFleTY5jJBKK8eyHSFlCkJwR_xXn_7FiyOrwAyw-Vv5cx8iHh2I-q4gYtOYZduMtB6MTwdc6gxh8LEGM5c51xZcN3Ek2HTbejOuXEvwDOsuxoYNffG7giQibYp7Vfi8oZeqW8bc4l8CCehgSRppcucplHrLKqbcm6mYCHJIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش متفاوت رهبر انقلاب برای تدریس درس خارج
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی خامنه‌ای: حضرت آقا به‌عنوان استاد ما، این را نمی‌خواستند و اجازه نمی‌دادند که طلبه در درس خارج فقه تبدیل به یک تماشاگر شود.
🔹
یکی از شیوه‌های ایشان این بود…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/463736" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463735">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6XKUnWyTBTDBuRrAm_QNklHGknyzX2UpN7ADu7rr4TeMeZ9BiGrwgU88y40D4dmLjW-Om1oBNVerxvxZf4woyCK7c7eMblhICyeIzyz5GfnBocmlaz1xGtnSGIjCw2fCiOlZBHt4ckmnbp1dqlZTsS-LhxvwY1eAcVJj7P7yzDN59ak1Ns8Zir7DuJK-bD1Z3cVwdc6rT8cTmXAXQQEDsrFHZ2IqJOVhkuws49KK-NySqK7Isn5EHh-gtGCEI3or9AgmBWQDW7Z_Wuig66M9eJgZuF4VEMpcj09wGM_TooKuCYNS2xsdRy7LYtY_5SOeKmlbYXTTokkeuacpgO7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز پرداخت بخشی از مطالبات پمپ‌بنزین‌ها از فردا
🔹
سخنگوی صنف جایگاه‌های سوخت کشور: با تأخیر ۶ماهه در تصویب و اجرای حق‌العمل ۱۴۰۵، تسویه علی‌الحساب ۴۰ درصد از مطالبات جایگاه‌‌ها از فردا آغاز می‌شود تا مصوبه نهایی ابلاغ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/463735" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463734">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f86f57de1.mp4?token=jDG1R-V9PXdmdpncKuH1e-5BCvudpi-kI5d386nyS1javthWMgXHCS4mdF-5R19YJMFZXPtIgi51DADBtGPZhW4N0tSGqV5AjKP_0W0DKFbXQBWnylkXNAjY4Zwq-pgq58P6X_lwdqJ209rv_QMx-CbbMLOqL2aqTSweoYG47GTAQ7kEAaFy88E5O82fi8GjRqfjSbUpLNOraH24xfm-2CvGH9EIOvtnmZT-29HLMtSSP-5DzDArWrkbnS9AxkFohrKsllNXpGYMhAuKeqCnXUzzwmnX_bQ2XR_GdhCZ0GibkvyBWh_3bfAz5T93kXCKA8e-utQWJ2yfTv7S7hgBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f86f57de1.mp4?token=jDG1R-V9PXdmdpncKuH1e-5BCvudpi-kI5d386nyS1javthWMgXHCS4mdF-5R19YJMFZXPtIgi51DADBtGPZhW4N0tSGqV5AjKP_0W0DKFbXQBWnylkXNAjY4Zwq-pgq58P6X_lwdqJ209rv_QMx-CbbMLOqL2aqTSweoYG47GTAQ7kEAaFy88E5O82fi8GjRqfjSbUpLNOraH24xfm-2CvGH9EIOvtnmZT-29HLMtSSP-5DzDArWrkbnS9AxkFohrKsllNXpGYMhAuKeqCnXUzzwmnX_bQ2XR_GdhCZ0GibkvyBWh_3bfAz5T93kXCKA8e-utQWJ2yfTv7S7hgBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: از نظر ما بازدارندگی یعنی هر متجاوزی باید هزینۀ تجاوز را طوری بپردازد که دیگر آن را تکرار نکند  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/463734" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a57e6ffd6.mp4?token=isdjZebcTRD3m8QGTuqnD7Y4XjXPMgKVGrn5L7zDsKrqivzClWPLcn65_DUfPcmKTM8KtSgrPOLhliWurk9G_0wtQw7dpOCW3VCKQXm5cv9blPNPvGDVj0OZZYY_OrteVq6Cel5bx2yKrBmXVb9bYQe3D2aHPAMI9QzmhIy8xkVcbjEQi3zH7d8ObWhHHhsmv4_CUBLx_f2QLuma1zRbbwFp_2YqnwhJmVYaooVD_F-fkg9WbbaOGT_HQoVcc42c_sUeJbmpHmjvEY5xO_xQlPBa2fjjj11ktMcs38PoFudh1JuQrLuTUGhD1jwqAjFX-eXjjggm6VgfRbGtFiWDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a57e6ffd6.mp4?token=isdjZebcTRD3m8QGTuqnD7Y4XjXPMgKVGrn5L7zDsKrqivzClWPLcn65_DUfPcmKTM8KtSgrPOLhliWurk9G_0wtQw7dpOCW3VCKQXm5cv9blPNPvGDVj0OZZYY_OrteVq6Cel5bx2yKrBmXVb9bYQe3D2aHPAMI9QzmhIy8xkVcbjEQi3zH7d8ObWhHHhsmv4_CUBLx_f2QLuma1zRbbwFp_2YqnwhJmVYaooVD_F-fkg9WbbaOGT_HQoVcc42c_sUeJbmpHmjvEY5xO_xQlPBa2fjjj11ktMcs38PoFudh1JuQrLuTUGhD1jwqAjFX-eXjjggm6VgfRbGtFiWDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: از نظر ما بازدارندگی یعنی هر متجاوزی باید هزینۀ تجاوز را طوری بپردازد که دیگر آن را تکرار نکند
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/463732" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عملیات فریب آمریکا با اسم رمز «تفاهم کوتاه‌مدت»
🔹
در شرایطی که تنگهٔ هرمز بسته شده و همین موضوع، بازار انرژی را تحت فشار شدید گذاشته است، ذخایر نفت خام آمریکا به کمترین میزان ۴۴ سال اخیر رسیده است.
🔹
قیمت گازوئیل رکورد تاریخی زده و جهش نرخ بهره اوراق قرضه، واشنگتن را وادار کرده از وعدهٔ انتخاباتی ترامپ عقب‌نشینی کند و نرخ بهره را بالا ببرد.
🔹
در چنین وضعیتی، به نظر می‌رسد آمریکا دنبال یک تنش‌زدایی کوتاه‌مدت تا پیش از انتخابات میان‌دوره‌ای است؛ همان چیزی که کارشناسان امنیتی و اقتصادی آمریکا هم در فضای ایکس بارها به آن اشاره کرده‌اند.
🔹
نشانه‌های این تلاش حالا دارد جمع می‌شود: کاروان سوپرنفتکش‌های سعودی حامل میلیون‌ها بشکهٔ نفت در خلیج فارس پشت تنگهٔ هرمز تجمع کرده‌اند.
🔹
قطر انرژی هم نفت خام میادین الشاهین و قطر مارین را برای ۲ ماه آینده با تحویل قطعی پیش‌فروش کرده است.
🔹
دیروز سخنگوی وزارت خارجهٔ قطر از دستیابی به یک توافق کوتاه‌مدت میان ایران و آمریکا برای شروع مذاکرات خبر داده بود.
🔹
جمع این نشانه‌ها این برداشت را تقویت می‌کند که واشنگتن می‌خواهد با یک تخلیه تنش کوتاه‌مدت، قیمت‌های انرژی را تا قبل از انتخابات میان‌دوره‌ای کنترل کند.
🔹
به نظر می‌رسد این طراحی آمریکا برای گذر از ۲ ماه حساس پیش از انتخابات است تا آنچنان که برخی کارشناسان می‌گویند، تشدید تنش را پس از انتخابات میان‌دوره‌ای از سر بگیرد.
🔹
مجید شاکری، اقتصاددان، هم می‌گوید اگر ایران تنش را تا پیش از انتخابات میان‌دوره‌ای آمریکا تشدید نکند، آمریکا پس از انتخابات تنش را تشدید خواهد کرد.
🔹
در مقابل، جعفر قائم‌پناه، معاون رئیس‌جمهور، معتقد است ایران پیروزی خود را در عمل به اثبات رسانده است و اکنون نوبت پیروزی بر دشمن با رفع تحریم‌ها و فراهم شدن امکان صادرات آزاد نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/463731" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a801167fbd.mp4?token=YmkcXDFGK8PWzJmlzgHdLuCWgC9ihlmsR0TjHMuvXVc8UusnjUybSYJQnR5bBgfo4NLab-r_djy_6dB7oMU5wHniqOnt7qHnb98QeRsb_mch81_QI5JqKTHa529l_4fUUHLEDydDjcsX5shPkwm6-7OGo-xR8kLW7iVtAoyoVohtiMl0fL5jbK5bk4PBejdSOT7ouTyQsYfZa_reUGy1WpRkXvtplMvPEgzD70lOqkVXZC4LjMwgyCwipxNZ1nQa0ORQOhcnjpp7Dpn_-ZUf_-SiI9goUXHqevdGPlK4Zs7AJNxo71ouC-QdIgFWNtYL3Mol_ESrWsD-aePR0WaXwZXrDzGA6dcPHbl_SmeupeJzjsqEHfm0Da2Jbb-aHIImzOGR4wcKC8np84WaJ6H9GtMN6SCES_o4eWNND58hDFIsjuSrn0efEybXp63vVQmvxkiE8mKpknuLZ0Ux2zFWXBmfGw0EqkptxuufZyGyqvJOw7oCdRiTF86GbwprbSWpAwuHQJo4qnWetp_qDk4YBQAa2wcVzlYLe0AK4dAJmtmfKXwmRNQGmME1X8M1IhOQOHOMROcUknDS2MTTaR5xJum_0sxlzPjm0gmChVcnbd3pMUUr-JpcG3LoZQ5d0goqzsT1a4TvL69ZLAyehB6dPB3jFezd3rvrEtSChz5DnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a801167fbd.mp4?token=YmkcXDFGK8PWzJmlzgHdLuCWgC9ihlmsR0TjHMuvXVc8UusnjUybSYJQnR5bBgfo4NLab-r_djy_6dB7oMU5wHniqOnt7qHnb98QeRsb_mch81_QI5JqKTHa529l_4fUUHLEDydDjcsX5shPkwm6-7OGo-xR8kLW7iVtAoyoVohtiMl0fL5jbK5bk4PBejdSOT7ouTyQsYfZa_reUGy1WpRkXvtplMvPEgzD70lOqkVXZC4LjMwgyCwipxNZ1nQa0ORQOhcnjpp7Dpn_-ZUf_-SiI9goUXHqevdGPlK4Zs7AJNxo71ouC-QdIgFWNtYL3Mol_ESrWsD-aePR0WaXwZXrDzGA6dcPHbl_SmeupeJzjsqEHfm0Da2Jbb-aHIImzOGR4wcKC8np84WaJ6H9GtMN6SCES_o4eWNND58hDFIsjuSrn0efEybXp63vVQmvxkiE8mKpknuLZ0Ux2zFWXBmfGw0EqkptxuufZyGyqvJOw7oCdRiTF86GbwprbSWpAwuHQJo4qnWetp_qDk4YBQAa2wcVzlYLe0AK4dAJmtmfKXwmRNQGmME1X8M1IhOQOHOMROcUknDS2MTTaR5xJum_0sxlzPjm0gmChVcnbd3pMUUr-JpcG3LoZQ5d0goqzsT1a4TvL69ZLAyehB6dPB3jFezd3rvrEtSChz5DnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مبعوث در شب ۲۰۵ هم میدان را خالی نکردند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463730" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b504b9fd0.mp4?token=tm2WE4PQfOuT3MwaJv7qlEduHS6-B9kEVgqlTHt3COvHCd-1FXiP40S-spKHIuVvPJjIBTWxpqsGzpLXb6xndcSnPz8BMFNwu-y_sk4jPCjuiMZvyFY3HOfekyazPLenO0lNHuKEOL1ft1Q5DSr2VsxVVsR3pR6LdU5gg1ZZ-EzG2X1cl1LEpWSaXLCcQ5CJD3TEAzXDPKgGdOyyvaYZW28d87cvJKlrAXS8_XEKR-ib0YbiCKIQxn1KK6XR00-ackNU0-4Rk_mEvyr70-xfL5NkE-EHexOnVWZ2O0auqcaY1Qj4Rp3UKTzakb2ihMUhBr2KNCvaS0ksRfp0mqhqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b504b9fd0.mp4?token=tm2WE4PQfOuT3MwaJv7qlEduHS6-B9kEVgqlTHt3COvHCd-1FXiP40S-spKHIuVvPJjIBTWxpqsGzpLXb6xndcSnPz8BMFNwu-y_sk4jPCjuiMZvyFY3HOfekyazPLenO0lNHuKEOL1ft1Q5DSr2VsxVVsR3pR6LdU5gg1ZZ-EzG2X1cl1LEpWSaXLCcQ5CJD3TEAzXDPKgGdOyyvaYZW28d87cvJKlrAXS8_XEKR-ib0YbiCKIQxn1KK6XR00-ackNU0-4Rk_mEvyr70-xfL5NkE-EHexOnVWZ2O0auqcaY1Qj4Rp3UKTzakb2ihMUhBr2KNCvaS0ksRfp0mqhqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلایهٔ‌ وزیر صمت از خودروسازان: مردم از کیفیت خودروهای ساخت داخل راضی نیستند
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/463729" target="_blank">📅 20:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbe171e06.mp4?token=Rc429BVSGorPy_D-clZqu9jwAwLFYRakkTDwl4DsT9vpxcdlqGr-g9EyYr5Zsp9c3PThreA0_Iqs702qhxHiOqxqVIcL71dOF6rSBaa4Ke2yyGFyX9rdx4Y5W4LnywR2MVID42C-PV8gZUSljrTLSIQwW-w8dYhsHFCxn2DyYcIPBiXnHTUWAqtgQWZo8uqcxvu1Oms726scSS15QjOrMExnPua9HbNeASek0J8ZEh5P2yvUPQ5IIbApr2v7hWFzJAUJR7QKsp6TR38Kl_i0s0WxW7uKybYBqchNZMCKlfyi_wRIoIK9PxTj2AYj95CejXIzPdIMo94SNx2qeuj6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbe171e06.mp4?token=Rc429BVSGorPy_D-clZqu9jwAwLFYRakkTDwl4DsT9vpxcdlqGr-g9EyYr5Zsp9c3PThreA0_Iqs702qhxHiOqxqVIcL71dOF6rSBaa4Ke2yyGFyX9rdx4Y5W4LnywR2MVID42C-PV8gZUSljrTLSIQwW-w8dYhsHFCxn2DyYcIPBiXnHTUWAqtgQWZo8uqcxvu1Oms726scSS15QjOrMExnPua9HbNeASek0J8ZEh5P2yvUPQ5IIbApr2v7hWFzJAUJR7QKsp6TR38Kl_i0s0WxW7uKybYBqchNZMCKlfyi_wRIoIK9PxTj2AYj95CejXIzPdIMo94SNx2qeuj6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای دانش‌آموزان در آخرین روز تابستان
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/463728" target="_blank">📅 20:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=RC-3qqOLoO_qUgh182MlK2wjOJkajNfGUDrWm-Rp1QlN38wLPYh2AFqYIDdiGdl5-v2KRwkMg-WIoFhSCW6EvF9EIX4f2OJ-2UX_SuLcrGA6EiAdY1I0OiyUbySFePDUj9ei8v9CdlwyxaGVVicgiM4ltXhc2xgo7dmmVZPqTI5G4hVimDzd1cAQ7SMQcWjQv0pubzSCinfdMxMTz_mH4RtCOTD9SDCvbiFtidf3nAX9368w3ayoRBvP3jbALdFT4xeWsVmyYrN5NMuo5FR9JM9ySrMwFR0s-mFXkoZpC5nJAj9EQwNZ59zHILXNJ69uwYbqn7vII6KKozDjJXfHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=RC-3qqOLoO_qUgh182MlK2wjOJkajNfGUDrWm-Rp1QlN38wLPYh2AFqYIDdiGdl5-v2KRwkMg-WIoFhSCW6EvF9EIX4f2OJ-2UX_SuLcrGA6EiAdY1I0OiyUbySFePDUj9ei8v9CdlwyxaGVVicgiM4ltXhc2xgo7dmmVZPqTI5G4hVimDzd1cAQ7SMQcWjQv0pubzSCinfdMxMTz_mH4RtCOTD9SDCvbiFtidf3nAX9368w3ayoRBvP3jbALdFT4xeWsVmyYrN5NMuo5FR9JM9ySrMwFR0s-mFXkoZpC5nJAj9EQwNZ59zHILXNJ69uwYbqn7vII6KKozDjJXfHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینستاگردی جولانی حین سخنرانی اردوغان در سازمان ملل متحد
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/463727" target="_blank">📅 20:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUtHdFG0tAoSDvoA_Hn97lbp5ywD95K2qiFJcBuwrWsBRxxffDYiHec3EIqnhm2g8xg8jJnEs5JPFOx6FiZDzmd0y6oyZ3TS4bLt6M6lGV5Jd6eKXaWEnIh_1Hg8eU_Nf2o4tpbNWZi31c-19pT8vgnjwmjCYOYhPTQqQYn5pEwHUdexuiVr1zLEZWsZRn433iODl69SEaIQKtR8-xbs2sURUciBUChsL8jA6WVpRqQZ6VNuIGlKz8RbYd598V08frFZrNQB8pkZzqPfzTKy4aj3jdtqsOnZalk9BzI_28lzumsRe60NNXuNqZg1sHE4u9TXAZVKfAm1yULA2jF52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leXQQZObcbcWRo0CAZgZFNDnMLfNzTcTKdHo15YPznN6dTXPsZUC9BykYc6m129CNjpAPJXQdISZb2spl6Im-SM3K5WgSI0uZGx7UyWS31c81YPW9AGBIvpgzAKhski62hgmnhOFOWm-qhDgocmva6QCQcB65SDzKRUFa2y1x8T_FZ6fSWIxWrwapzOIVSMDQhS42ujXCtsQqZeaaG65hqIyErQBZwb2tcUYVcI1TPUnUbZ4_Qgu4LWdKYx2iEzVxytjcCWbFD19Y9mnnxwP6fLOx_qH38eORU7xZqOX9ba7NNFBlyQqdKCydb-r9lCUsZ6pcIznjVEvk2pCwb3nnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3HgM65MSyZB66jdpLF4FSraYLIlkddnC5tLArB5zUluRr4Z_upsRQb4Ec8bZCNpinb-P_IGJ07dbrGOQ3nPAqwRWT4FTPy766BjR7lJzt9WrQxNnc9ehtOa9trpWHmbnvgkLDGZhvNUiyf09X1RML_NRhOoeop18sJwY_nAUxLWQDg0X9V-J7-0sRXf8iJMso9_-_-d1qR0xir32fKed8VgHiLKhZChMxc2XfxnyftpV-5fhQfN6OvnKcqk6n-ksdkR90kcT59xRgKo0BQr4U4jqT_B3LRxzP12UV-5k3xCZT2iIXomPWDZ6axEsHQnfo79aONQs0XeSrJWE4ZQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISsQW0Ip9q4GprUkHaIQfaXMmRYjSRXH8ClwmxBDNoVAM6eWhS84Q15MVRzDdWp0DAJb2R0F8-kl3rMxGc8eXqHkoR4I40fjU46QaoWSN0iwyFoFRGMgiszdADtegE4fOKY1fKkDirdayJfaCItmYOX0vhqWD7BFqOImHtppjQCaQpoz_7CfsQcrbc1EpN8Lep3qx4apmxRvFiB7yE0aQO45vyT8M_9SW75fwxNs3VBwlgWpS10Vq_miExRX0sIERoORanD6ije58r5iS5PyC5F-mY6iL52pI8MAkW_VT9GfbgpygAdqa4R3B9ZLTWyej-WDDpKHU95HS5TqnpzJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-p8SrHj5fxu1xwIMWYmh_vEZ3Ez_BQpU27HBx-okGhE0vdfCuJsyzixFfUg26Hd97FwzJGcNh6SHxbLLWIwXqdWsDDooiCBNE9ULemyvK56gjHK6NdJKGPZWX6JDz5nhsgGAVjOhS-4CdUVqx9ZnOWkgi5kvMyTJL2AP57bAcLgPFY279tlf_JxWcIlHmJfZH1eiq7qDXSsKcNr2ir9WPaO9E2oVkUAE3-34eukheuLGJzHgfsGM-J74QZqgdpN27YT4mfoGUd2xc2uSloRc33JM92l7toelSnrzJqPMQPKBuJdsJSrF5-CntrN1eQskegSK_-a4W60mSjNxdPecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhzW324hnmWakj_wmpD7YP1M84am5IKDCVVWl6nz8vqndzbtHutTM58OmliM3jX7N4sw3JfdQEaWc-mKlXR_IllopUhJd-Waus_ugzgizksOrXcpiGavuPP_rK9HVekbalyWYe4NEt6VmXdbIs9WyYH-03eFBQ32F4rU62lWySl3lLozWRf605QQka39p9Jbc2JsnvQeiF2c2O3IJiPxezUzDwBctRJZq70DaY8ruQkxD2nzw26P1AU47fj96-wg4TLxEeCcCcGSFwGXfCjWgmMy4X3i7mIeRsMKAvkMDVqk_QnWUO-1qFK9gGMz04CpC00EGrTHlJ5LZH-XNhNy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K95ZY9ANvIdt6bl63oNtX0e3ayIZWhnzl5-JvoPpYGLiOJk1bGkNJN6jTjAnRQpoz7TCZ2-cuDLZVx5GdpXD6fH4gsMyUXH9Xs1YfIP2l9K0auaGqnadoTvwSYw92zFrIfYdEhdJB6aa4pg5eCBQSFpXwFd59ASALcHrZmuQe9UekY5GXACLW-a1nLznW_9S9c6t1buiGsqvulruCQQdeOt9MRQPIitNh-J8A58AWi73B5lAbqL6SIKhnXcEifz1uwU42T8tWk_wjI1JPBKewf3aFAz6vWxstBRtH1FejYLzrAaNlDx_4uCOGCNv3IV4TzS7FVcizQa8UQGN87Oagg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رژۀ موتوری و خودرویی نیروهای مسلح در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463720" target="_blank">📅 20:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLfisVFsZIBvxpfjoFV80eBLcGStjCXWRNjw3nFS21n5O_aPFdrSjmeV9um-ttoLhPXGxcZqORTx1NUoJkpLPsg45b6hIDPHA_kJYg-5aD6B0IeRuOQiJkQsHU_C6TEWeex74tQ0XVaEh2T6VE9NYGGvyxkee91IygT1JAEqfHv6khZH7qtpFjiel4N3TJiaoZinoWt_jZBaBd1Ofj01zxfDyR8C5DQcy5NTG_vmoCB97vWMYlNfZGgj-DTuf2HCSynNEw8s3LV5dGmFeaoU-FZXG8OYNJGt2EXEalMHUW4uQx4SeNoHq6F6d23rWuwzvDGBO12saPBmHXpmHSO5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنایات وحشیانه‌ای که دشمن سعودی مرتکب شده، عواقب وخیمی را برای آنان به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463719" target="_blank">📅 20:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLDotHKC9WSdLH9LqNPh_7F_xyHcJ5DnwJnakjxp0nErSi03mHF4s93su_lNeCshbEyluz_R1sGDAhvumhHKWWxx_Eclgv2bBnHSMPkHypIqIQk_4ekud4lzu1R17xBOrvhktx4KjiWYlc9wZ0OfOjUQEYZk1cHLpQytG948w3QZ2JCs72SlXM4k3536LZiULW5eIg_PykLbOdqIwNNm9qUEThQqTNh2amC9ajcpizLb-oih3KoIr5S60X1DDHw1uwMgVOsoQPjvaVnbjxUkP6GsDMsKfHEpUEGEuDjHEiUGx5ppAH0y6h9hlVm_X7JDLjcNeJvdi9a7qLZbn3n6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور زاکانی در گلزار شهدای دانش‌آموز میناب
🔹
زنگ آغاز سال نو تحصیلی مدارس فردا با حضور شهردار تهران و از جوار مزار شهدای جنایت آمریکا در مدرسه شجره طیبه میناب نواخته می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463718" target="_blank">📅 20:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463715">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnF9ySwvjgQ3rbHV2Y0n3mUKdkoSHHfv1XZKI60aa7RpBKdd9d0SXdsut0bTdX9VpvPG8CihR0ub-kOk_qldMUueLG6LTYit5O7zaqo5_fTTkEsQPcGgodtA2HnpKdg_gRD8rgqprvBBy-ZFUgdgWFdg3PtrKVk63focxvg-j4tdb5su9E5GdQb0AaWCmYynLIAVICTdUz5r67eHTePdJR9zQzTo_vnBFFWDHt1QwPsGmRz32LpF3rk7P4WOFphFRYjsTOkaSvE9k5dsXzqrwawhk8LqKTR22hknaS_pSv61NDxKhHBLVhtUojI_T7LseGVBJEocwrSZgPNaSepZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwWNsOVbFp2oSt23vkvEEJLsXqY2RTYioevI98rXSUnWYnXx5G6_wKxvIUseEdHL2mA3W2Jns22q2dS9NXA5GT4Mw_tW6lbKsL4j_d7Bkg5D7driXckWBTZOlqEYtQGrn_Rs6D2HlnXDXXnJQ_CDRgVQKkuxXUYzfHJtuH8H_Hx3scb6-EL3EQ6HLAhvY7NIn_9n5XnENCsC5BHlXRXsb5xWKEitZ5Q7dbR9kRqtc0G77CNrNjbDoNiJa4xnbqsZEcsrX1Itb2rCDjJ4SFjfA8LnBODxw1FnmeLTEmDzug9kKF3su3oH-NUOIAvGId0tXnlpA1PHMmYF4NcuEv3ejg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de3dbf71c.mp4?token=fYbODYJNeDSVPE4OIJrzIqoBRzrUuMAfnsziGDs6985RNvLRetjemuKaJ7s711MrTaSM17hlPZjWgpkohut6q5nmHTtygRfn6E2x_yxlfRB5gsJ3WsAGUAd2qYG9h5xmapDSpc98fOQijxxiPigCsK5uqHjbDenBYPUBfuImpmUGtbBkXbV1_jPyK8EGqSDJ1tmEG2cWFYX3DsXgwrknQAyP8zFO2vFSS1GUuQa7fIvf1M1fMw0KHzHVKAWeHwGbzn8WtuOx35fLY2ZrZ-nYa3l6kdde7rFIn9Wr3L4KnynQY3r13KuOfPNHH4jbo0DkQ36N_Q4HEyPFkQHp2CNejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de3dbf71c.mp4?token=fYbODYJNeDSVPE4OIJrzIqoBRzrUuMAfnsziGDs6985RNvLRetjemuKaJ7s711MrTaSM17hlPZjWgpkohut6q5nmHTtygRfn6E2x_yxlfRB5gsJ3WsAGUAd2qYG9h5xmapDSpc98fOQijxxiPigCsK5uqHjbDenBYPUBfuImpmUGtbBkXbV1_jPyK8EGqSDJ1tmEG2cWFYX3DsXgwrknQAyP8zFO2vFSS1GUuQa7fIvf1M1fMw0KHzHVKAWeHwGbzn8WtuOx35fLY2ZrZ-nYa3l6kdde7rFIn9Wr3L4KnynQY3r13KuOfPNHH4jbo0DkQ36N_Q4HEyPFkQHp2CNejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عراقچی با مسئول سیاست خارجی اتحادیۀ اروپا در حاشیۀ مجمع عمومی سازمان ملل متحد دیدار و گفتگو کرد @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463715" target="_blank">📅 20:22 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
