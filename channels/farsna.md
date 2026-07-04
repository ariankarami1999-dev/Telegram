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
<img src="https://cdn4.telesco.pe/file/Sd_fsjzUosmXMZvdJJhhA8gUobCRP5iRKyBH-L1od2wbnx20LYYwe_OuSCGVtx9pE_fbfa675sIsHnpu4DTy1iPIT3g1p_PEg3Dg0mpGW_RZ7rf0nDz7PRO33ydNNjD9M8EomfZYjz1XNdnDEG-ihCiVBGCpwt-vpFQNj4_ljAQXkTBTXyEes5CjGbTrq9vohY8E8XYmMBY2Rlk4eUA8mUZJ0RkRnBWRPamghgNSCth1QKe4B2MBeI2C6DBf2e6oYvKHvb7veoqJeh3HOGz2xePNpz6NHXSMBnQwAHvIebj23bYalqvPOHtiMtKa03LExxX8b7bCpXOS01AQ0dtwNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-446618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cb95837e.mp4?token=cXUihTZuCjJsUhppPtxxMT7yrGzghoKQuic19EjVVYZ616CL-flnsj3EGYvzQxZxR4-bJt2qyTcm-0U-oP_cCErKn6za55s-JrCVvaEE7VQW5TxhEUeMJLuOyLNhshsU7k-suYhnB3iubsasa0IMsX2qqFiaCXPvhb1iJnDsULY3rgctCdAVsxk_LNjB_VQ-TWISAX1qkrEOUA527MuK3PAatIw4mCEbAGy_9ZdsmjrXVxgYO3pc_cI3Lr2_6oh5YM_LepogyDkcblAuyrMqO0y0G2UoVm-A8rRfewOg5wc4fzlg3o8wGHCzlGVfShhTn8osilJ21G8lXKAf55iFvCXmBCi1V_TQ2dKl-i0O1x3taymbLBMgOOj14WOLjta76oCQ7mfv4N_AB6RM1oKBMMx-s7MauSBwjpgUhJcap6-8LgIq8pwf5X6jGxhwgcN5yFpV9p_81XWW6q8kcm-_r64VhlTyzPamrWYSp2Td0F2QOgx0hZk9ItnxXVfOZe80dDh0mbokFugxuLkM4xDR9WiYofn0WwtDASDvepa3X3mAOpR23SGkrTo_AJmPqLVryR0ByPgz9ACuqTEOe13-7IjIdowp_Iu6t8IyxWjM0p3A9EeztVYywe5wljqhvvqNNwua0t6pdrGCtAw6K1AoWhbYqvGzAshWac1jJk7zckM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cb95837e.mp4?token=cXUihTZuCjJsUhppPtxxMT7yrGzghoKQuic19EjVVYZ616CL-flnsj3EGYvzQxZxR4-bJt2qyTcm-0U-oP_cCErKn6za55s-JrCVvaEE7VQW5TxhEUeMJLuOyLNhshsU7k-suYhnB3iubsasa0IMsX2qqFiaCXPvhb1iJnDsULY3rgctCdAVsxk_LNjB_VQ-TWISAX1qkrEOUA527MuK3PAatIw4mCEbAGy_9ZdsmjrXVxgYO3pc_cI3Lr2_6oh5YM_LepogyDkcblAuyrMqO0y0G2UoVm-A8rRfewOg5wc4fzlg3o8wGHCzlGVfShhTn8osilJ21G8lXKAf55iFvCXmBCi1V_TQ2dKl-i0O1x3taymbLBMgOOj14WOLjta76oCQ7mfv4N_AB6RM1oKBMMx-s7MauSBwjpgUhJcap6-8LgIq8pwf5X6jGxhwgcN5yFpV9p_81XWW6q8kcm-_r64VhlTyzPamrWYSp2Td0F2QOgx0hZk9ItnxXVfOZe80dDh0mbokFugxuLkM4xDR9WiYofn0WwtDASDvepa3X3mAOpR23SGkrTo_AJmPqLVryR0ByPgz9ACuqTEOe13-7IjIdowp_Iu6t8IyxWjM0p3A9EeztVYywe5wljqhvvqNNwua0t6pdrGCtAw6K1AoWhbYqvGzAshWac1jJk7zckM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزومه همیشه یاور تو باشم، میون لشکر تو باشم
🔹
مداحی امیر عباسی در اجتماع باشکوه مردم در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/446618" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اهدای شال عزای قائد شهید از سوی وزیر صمت به موکب‌داران چادرملو
⚫️
وزیر صمت صبح امروز در جریان بازدید از موکب شهدای وزارت صنعت، معدن و تجارت با حضور در غرفه چادرملو، شال عزای قائد شهید و عظیم‌الشأن را به موکب‌داران چادرملو اهدا کرد.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/446617" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکربلایی وحید یوسفی</strong></div>
<div class="tg-text">﷽
📽
نماهنگ |
#خداحافظ_رهبر_شهیدم
🏷
- از سوگنامه
#بدرقه_آقا
🎙
بانوای: کربلایی
#وحید_یوسفی
🏴
ویژه مراسم تشییع
#رهبر_شهید_انقلاب
صفحه ی کربلایی وحید یوسفی
https://t.me/vahidyosefy_karballai</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/446616" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/446615" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8B4F2KlgwKrRuNLvTmKiV1HVSAO3obKwhUmgxonWnX0chtbfnY7ow-YHud5cf6fESSKjtiauC4s1hy0Ap8IfNS0CuCgWqzs3O0_LeB2A2cGC5ugSZ4bM16AajuokiIuF4XhSzRMsQ7CSa4ZaXSyIX0CRReGxOh1zcX-_1nzFOR6r7c2SIintEBDi-FYEnvz9fOhKlnxaZGwYwRV8CVBy6lvJyAYUzxzcxI5rquhcBI5MVzBX8FvRmO8kqn38i_aGBQ26ELfy8rIl3MOnZD1rNrcLOQixMKaaZ4r8D-p6hS6HZYRZS4ifKU_KPvxOIeyb_otIeAtL_xYmq-1aHWyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران مقتدر در سوگ مقتدای خویش
🔹
بیانیۀ وزارت اطلاعات: ملت مقاوم و نستوه ایران اسلامی، بیش از ۴ ماه است که در تداوم مصاف تاریخی و مبارزۀ عاشورایی خویش با جبهۀ کفر و استکبار جهانی، داغدار و سیاه‌پوش شهادت مظلومانۀ عبدصالح خدا، ولی امر مسلمین و بزرگ آموزگارِ عزت، استقلال، استغنا، اعتماد به نفس، ذلت ناپذیری و ظلم‌ستیزی است.
🔹
دشمن سفاک آمریکایی صهیونی بزرگ‌ترین جنایت و توطئه تروریستی تاریخ معاصر را در این فاجعۀ بزرگ رقم زد و قلوب بیشماری را تا ابد جریحه‌دار و محزون نمود.
🔹
دل‌های آزردۀ مردم غیور ایران و آزادی‌خواهان عالم جز با خون‌خواهی از مجرمان این جنایت التیام و تسکین نخواهد یافت؛ که طبق وعدۀ الهی این انتقام و مجازات محقق خواهد گردید «انا من المجرمین منتقمون».
🔹
اینک در امتداد پیمان استوار و میثاق ناگسستنی ملت با رهبر معظم انقلاب و اعجاز مبعوث شدن بی‌نظیر ملت سرافراز و ولایتمدار ایران پس از این شهادت عظمی، سربازان گمنام امام زمان در پایگاه مبارزه و جهاد وزارت اطلاعات برای تکریم و تعظیم نسبت به مقام شامخ و روح بلند و طیبۀ قائد عظیم‌الشأن شهید (قدس الله نفسه الزکیه) و دیگر شهدای بیت شریف آن حضرت ضمن دعوت مردم شهیدپرور، استوار و مبعوث شده ایران اسلامی به بدرقهٔ حماسی امام شهید خود، بار دیگر با بیعت حماسی بر عهد و پیمان خویش با رهبر معظم انقلاب اسلامی حضرت آیت الله سید مجتبی حسینی خامنه ای(مد ظله العالی) و مردم همیشه در صحنه برای گرفتن انتقام خون قائد شهید و شهدای مظلوم جنگهای تحمیلی دوم و سوم از جنایتکاران آمریکائی صهیونی، مزدوران و سر سپردگان کفر جهانی و دفع همیشگی شرّ آنها از منطقه تأکید می‌نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/446614" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
ابالفضل علمدار خامنه‌ای نگه‌دار
🔹
انبوه جمعیت در مراسم وداع با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/446613" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNBTWRf5Gzd2TGZerKHpFkxaazCTOTJsORXBRARuZFyMQnsfRO6tI5nHIYNSQ399yw8BTbd5_SaYiYdTQqegpmomIBG3Ko7s2xm0gTOjMn9jG53NCJCQQIwS-X0JDJw1tka5-Go-LLEPcXZLs_rO1B2PjzBglNxfyRzS8Sq6-eTlaSIfPxPBMTEpDccx1cxTA8-R32nPxMHot02bYs3abvyFbUzoBamDkmLU__sqEMqNV0yD_fwFTCGuci0Na4gx5mZa-LqCgM12-Lls9kQaWQqk6G93GZnUfEfw-xlDg7RIcba1mAAi6ymjYVLY8gtAj-mn-OzSPJc5E7W4zFBkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم اقامهٔ نماز بر پیکر امام مجاهد شهید و شهدای خانوادهٔ ایشان، فردا ساعت ۶ صبح در مصلای امام خمینی(ره) تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/446612" target="_blank">📅 10:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
بعداز تو کشوردوست هم تا صبح باران بود
🔹
سیل خروشان مردم در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/446611" target="_blank">📅 10:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b766132058.mp4?token=Qms9lZDJKG9p_cll3mjqnMADy-QNXkWYFPFDTL4hh3-ZhxIq5I4-JKxv4yonFG8jyra-TKyts5HibHTB5IeY-2_tkQEi3CALrSfpGw9tlpR_dxweDZj_RS_CQsDOQ79CZhLVIu6a65iaRnTiOj1gaATr8G342uJm7y7agCfgKVuezkWDaEmTxwPfaRRHEzSmt7OlNZG5uXCb8RMuTiwlzLXRL382mv9ip-JvfrDo3dAYIY_0g4ZN49T1eVzQyTq_PQ-yoneYqSZCSNt0dNWGXtwZpR8r6QedA60I43ysuzqc2g2-pLNSpZ4VNkze_5aNkzlSOVXZhGFhvfPnt7ZFmZLQ3mMNBZ8KZGgxcSh4leNybHc4QOdAb6UQ_VrcRa84coNO8MBBuNPvQunA11FPcfHda-c0eLGGKQ9rFsV_1jufPa1yM7lab84eFkoCFFx61puXwHT4hQeDywF52j5dLu-i_ejgthfV2LONzCOiJLAPSsqRZ19dwtZ7_QruZxE3gqS_RE4M3WMwb2fOjtIx8Rv_2PeWIHKQKe9_4V4G7B125-qhEkV4dnCXmNK_MXumhtEXml7wxIiev-bGDxS-3osNwVjmAbO9tP7ZISFbz_e43ke4Ejp59Phmz2iKHm5eugo0lccORuCqp4l3PZe3LSQKTveWajWjFdoeJ_0sWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b766132058.mp4?token=Qms9lZDJKG9p_cll3mjqnMADy-QNXkWYFPFDTL4hh3-ZhxIq5I4-JKxv4yonFG8jyra-TKyts5HibHTB5IeY-2_tkQEi3CALrSfpGw9tlpR_dxweDZj_RS_CQsDOQ79CZhLVIu6a65iaRnTiOj1gaATr8G342uJm7y7agCfgKVuezkWDaEmTxwPfaRRHEzSmt7OlNZG5uXCb8RMuTiwlzLXRL382mv9ip-JvfrDo3dAYIY_0g4ZN49T1eVzQyTq_PQ-yoneYqSZCSNt0dNWGXtwZpR8r6QedA60I43ysuzqc2g2-pLNSpZ4VNkze_5aNkzlSOVXZhGFhvfPnt7ZFmZLQ3mMNBZ8KZGgxcSh4leNybHc4QOdAb6UQ_VrcRa84coNO8MBBuNPvQunA11FPcfHda-c0eLGGKQ9rFsV_1jufPa1yM7lab84eFkoCFFx61puXwHT4hQeDywF52j5dLu-i_ejgthfV2LONzCOiJLAPSsqRZ19dwtZ7_QruZxE3gqS_RE4M3WMwb2fOjtIx8Rv_2PeWIHKQKe9_4V4G7B125-qhEkV4dnCXmNK_MXumhtEXml7wxIiev-bGDxS-3osNwVjmAbO9tP7ZISFbz_e43ke4Ejp59Phmz2iKHm5eugo0lccORuCqp4l3PZe3LSQKTveWajWjFdoeJ_0sWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک سیدمجتبی
🔹
شعار مردم در مراسم پرشکوه وداع با رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/446610" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BANQxvLDKgTzA-svMFaAQHAoBiYM_7uVKliudxqdQdMO3yiRpTlIAGLoyicEN0MEv0psj9Dfe0040GCPkIhTx0kaTnIcOAcmPmePgw-0Jj8ZNQZ0eV6BaMC3AR-AWalkuTG6ua9HddB4JepnmIxAc16TdHHa3I2CDWE75PqAazRhkuCgk0bhtR4DTa2RxVRnwvPPSA5gimv6gyZ4TFjWIKHBqBmGjjgh01BrP8pBQu_mkUOlHwFvKVjc-USYIs7RsSw44-o6FoCnnEwqpPBwygJbzPVfiHuAMEXaPGW1qnyHCvWKA6eN8b4xKK4JOCcMXzXRVmF1abICoP-zyXG70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ صهیونیستی: میلیون‌ها ایرانی با شعار «مرگ بر اسرائیل» با رهبرشان وداع کردند
🔹
روزنامهٔ صهیونیستی یدیعوت آحارونوت نوشت: مشارکت میلیون‌ها نفر در مراسم وداع با پیکر رهبر ایران، نمایشی از قدرت و «خاری در چشم آمریکا» است.
🔹
همچنین رسانهٔ صهیونیستی وای‌نت هم نوشت: جمعیت عزاداران در تهران پرچم سرخ انتقام حمل می‌کنند و شعارهای «مرگ بر آمریکا! مرگ بر اسرائیل!» سر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/446609" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5110c90444.mp4?token=U34tCnftT3cseSlqufUgwrKlY3ZPoUX6vpr1aAWPacfuulaGxIul8ezRGPxLgBSXzYEkLpFt-F-t2V-xz7UB8N__Y9faPTl_xeYWmB88vznzNvI2ArrE2t7Um99WlCxgCMP3Ot32Ec4e7CO2JLmLsceAkXtoWrLIAbb2jRK0YzVys4g1Ip8LmWkmtqc6Ojoxp3-qwwR5Gv81OH5x7m9PeGfMAxuKRdFke8ZJkLA6HZ9-Q5v345q-MIwv2-3FFTQp-7ZowrIfwIMnG_7qOrzIZZD3rU0VFzDdhZg0Iud3zcdwRg2lWDBjiuottiECK-yh_4t_S1mnyASE4V4IAM9q1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5110c90444.mp4?token=U34tCnftT3cseSlqufUgwrKlY3ZPoUX6vpr1aAWPacfuulaGxIul8ezRGPxLgBSXzYEkLpFt-F-t2V-xz7UB8N__Y9faPTl_xeYWmB88vznzNvI2ArrE2t7Um99WlCxgCMP3Ot32Ec4e7CO2JLmLsceAkXtoWrLIAbb2jRK0YzVys4g1Ip8LmWkmtqc6Ojoxp3-qwwR5Gv81OH5x7m9PeGfMAxuKRdFke8ZJkLA6HZ9-Q5v345q-MIwv2-3FFTQp-7ZowrIfwIMnG_7qOrzIZZD3rU0VFzDdhZg0Iud3zcdwRg2lWDBjiuottiECK-yh_4t_S1mnyASE4V4IAM9q1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک سیدمجتبی
🔹
شعار مردم در مراسم پرشکوه وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446608" target="_blank">📅 10:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=UihG2Go85g56g1xyjj8x2-jwjOK8uXofOtXeEQXiJRZp8Pw38lCuB4qlvNf2yc7CfFrlloamUdov0Oy0sqUaGqJCevK0ELuk858YI7-1Ax0NriOj8id62FK59g94fKqEq0MuxS_6S5uFzs461htjgPlkFbDcjSp_trMpe3ONJ6hOkU67ZA5XeIXildtWXEC0trFOQ5azvPDYTHZIidQyUwIzxlteHVY_0e1bGzvUY339V2GS7uILMMyKjpb9JH2_iPEsyvYlEJmKMGrvYNX8CVv07gO94-lZKmHmmxNbvUXObFwtUd9vAJCPn_lZbaz32dsfteAXSjtMMx2Tj0iw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=UihG2Go85g56g1xyjj8x2-jwjOK8uXofOtXeEQXiJRZp8Pw38lCuB4qlvNf2yc7CfFrlloamUdov0Oy0sqUaGqJCevK0ELuk858YI7-1Ax0NriOj8id62FK59g94fKqEq0MuxS_6S5uFzs461htjgPlkFbDcjSp_trMpe3ONJ6hOkU67ZA5XeIXildtWXEC0trFOQ5azvPDYTHZIidQyUwIzxlteHVY_0e1bGzvUY339V2GS7uILMMyKjpb9JH2_iPEsyvYlEJmKMGrvYNX8CVv07gO94-lZKmHmmxNbvUXObFwtUd9vAJCPn_lZbaz32dsfteAXSjtMMx2Tj0iw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: مصلای تهران غرق در اشک و فریاد «انتقام» شد
🔹
رسانهٔ آمریکایی سی‌ان‌ان در گزارشی از مراسم وداع با رهبر شهید ایران، مصلای تهران را غرق در اشک و فریاد «انتقام» توصیف کرد و نوشت: هزاران عزادار با سینه‌زنی و شعار، پیکر آیت‌الله خامنه‌ای را بدرقه کردند.
🔹
این شبکه آمریکایی به‌نقل از آسوشیتدپرس نوشت: جمعیت یکصدا فریاد می‌زدند «حرف ما یکی‌ست؛ انتقام! انتقام!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/446607" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWzYFfSNDvUWgbaCFPCr3Ef1L0BWnQ5Tz1vuFWtvZ5d9f_8FiOD4SiIazlXLU8w4PP-HvsYyy8MqqwqnCy5je20LYfcgAeID7ksvLXGSagNEV1ifNKbZJbRtIVR3qNbKJR2SN0DDTljUcGMpGuGB7L8MyWq5AnJpZ7-1gg3xFD2485s_KuSE7i6qWkMBPJ5Cpzpc-QtpCT4sTGVvgDGr6Yl_TKI0YH8_B7e1KSs_imDmywLCcLg06QQOS-g2-YdP9vLEbF40zYa323ZBxEeJIs9zTdr782O3VV9zAGtfsbBNtIqBpceIjUwd0pmgRQjwNM2HNG4t8MudwxIfHKO9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایستگاه مترو مصلی باز شد
🔹
از دیروز به‌دلیل محدودیت‌های ایجادشده، ایستگاه‌های شهید بهشتی و مصلی امام‌خمینی مسافرگیری نمی‌کردند.
🔹
اما دقایقی پیش مدیران شهری اعلام کردند که در این ایستگاه‌ها، تا اطلاع ثانوی، خدمات‌رسانی از سر گرفته شده و مسافرگیری انجام می‌شود.
🔹
همچنین مترو تهران تمامی واگن‌های خود را وارد خطوط کرده و سرفاصله حرکت قطارها را به کمتر از ۵ دقیقه رسانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/446606" target="_blank">📅 09:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">◾️
خون‌خواه رهبریم، خون‌خواه رهبریم
◾️
از حق انتقام محال است بگذریم
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/446605" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fceH0SgqBv3V9klfHUSn5owhU6d25nwdxWlB6q0vAiBzd_debpNf1IHDq3SlQhEw8x3ItdJiWEUk22psPLeP63oQ6F-ZVn_TlF2NpEBkNMvh3gm_yK_-3AE6ilw8VpkFYuAn_JkN5l2G1l07gQpoMMNCjpWJmTUiUYc0phArRE2u4KdsZ_-z2gCuaoPsxebxdQNvj5Vt1de4YLrgjPXgTUb8KbviFjXxL5ZJ5l7k7HUNiVtL34G-c3_1ByfHP8HMizWXecPaQt9__pc-mQSNkIgXZkIiXbE92iKxKgnw75VHNPl06puoxB-3pYktpUMstl5bJs-9nDxNN3M5ght7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHmJBBxBLSsxKPYba7omWIh9xPvwgwUS7lLVSDegq0iglUcGCioPMlqad0gs_HRs-WGwqg_Io-FT7awoxSr68fCAfg9MuBKLEmEochfdjuxKRdrjLaZbKx3HkQWDxQ5Xogi0HgqZuzoNVvQkHJyT4jHElzLd3njdCDDmvrIskIoA_aGGLpyU08eCQ2U9RSBKAAL_AaUTOTvVX_dFSEKQgoU07JUNXYAt-lUJJXVK5qkD4aagaRNt3TcskDONXsouGSsZwCAyfnPZMNpluC488NuHbjj2ho4yztYhCUndALW3NdRdm9GRlnT4CAizTmZTHah6smVetY9F-vcxryxCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbQdZ4khCjpr4CVGw6LLpu6ssrf7oBT083ZdMhgGI-Iy1QttKBSC6vbpGJKemUChwBL4dYfmpfTn24SpuvowgCdyYC8nqvmG5v4K4QtXzDtMXihX7IjtNRVdmqE5jGx1mCYYFIExjg-ZgsI15TafnHqv5jm4KUJBmYqY0N18FgF116YmcJZfCQaqPrug8fxKzOQ5KIyCSBSVkDpwgPFLnpOP4cRyjrn7Io0xCn_rogpTivSbgmWm_ftPzSBl4B4ICBVUF2ZNbCITTt-_ycJQX7_EmU4ETtF8wVdhIlfrj2J5qi6XZQsKJKt1X2v4ENQeIJhu3-DW9OFtBy_GMyiDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2fgF5wbTa5zCO-Nxm8FIDdzh1hPOZJSVc25zBa9roJRmydCWDDCRal18lpEcXNBhkSJrJAkS24eU4Kl5zj4NOlLFD4jafXA_3jASXT0D8weSEeStb--UtI2-f4ForOA40WcMB_SKlAfCKgsQlgaRcKZTN68m424O_iSz7GooKiUqcJRsF5QcGFN2vWn-NSpNWWqxIsqefunAdOYsnpfRfP8QGRptbRZRpsLFDaKkgoROS7FR9MolU0ZOCCwLbucj5yHb0-A_S0eiJ6iPYWx8i5frhdu83jvJayMBlzaewi8vKv88lQtnkYNDWmUdJp6LuYmPFJOmempeMMSJ7aVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMHeuyfUvKBFxMEkV_qLU8yYGU56kXDZ0ryrn1tKzbKDxXWS2VHf7jTdoq6X6xaf83LY-duo1bt4afUof7whvtazKCEwIxnWaNWZYXXGLKO3VC3_qLcuqJZ9J13ZbEMa856_5Pwjmzg0c9gLWZz0Ff4Id1Dh2KKUsthB23zE-dQHO5ZWkSPJuOLWybNPUIv9c_rq8y3WATvbHdY33soPhNCpip-SyhtmU7Ysvq6NKavdY55Kz-QupkOvo5pyJ6eZ5UX9vI8gxjwPlzOkoB6tgLM7SEfnO1dITVqGYe1WqG-Fq1DSbW1ssmRpTf3VI12qlgsRFCsMvbSmD7Xqzvhu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wver0uOxHLQidrW-F0IujEVt5d4I-TYn3P2gw7U8Md7X7ebajtJv5OW7FTIoWWbqdRIRYuzQ5Fw-BjsjgN3INZ01peqsnPfyidC44mFqbAGM_WYoOva7Fdy9dRpsam7YbSKLSS_NGWwjZI8aYXs4zvjEFfNfkmVmMu4LlbW4Wdmin9if4jBfO9STbTerpoM5v8uUcluQcxtE25Sl_0ZQsYY_BCyvwy0TE45n5aI2FiVd3lpO9_pBXadFit9nmqQz7js3ExgtGf4CHE-cgm73AoovpJ15qsGptR_NcQWNjWzg6GSn7_RrDL6aBXZSksfyTZUH0x0jTJrxrTcrOvpjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEkcRt-eNExCMsgJd49rD-eKdpErFBDIpbQ2o5X2ReGex1mmHVJDFQn259Ho-CsdFahY_K98-p7mTdK25cHjxzA22inpMhvEtysGYzbu7d0wzh2jaErTYj7UatfqbcSYtkdjI1L6K_PGV5nYDRwB-6dHy1RoQKesyRr3jJBp-orkTS2acSdt7mT7wLd4htLvQj-tf7yLxl-61WgWl-fEQH9pX43ftecG64Tc8O4op68LOlaw9OPbd4LXEbcixXfPYp-fMCz_xs8fXo_MU81C98asZYRSDjZBuAFArPKIxL1kmwMv7sJ1K6jU4LfU_dPU8ivbxbZ-4zhgyZgKetq7yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین وداع مردم با پیکر مطهر رهبر شهید انقلاب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446598" target="_blank">📅 09:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675844bc07.mp4?token=SSZWfN138PUxDjwccbdUKiZqdckYc82Rm3JaC0FDHPF7bIqdfoAdCgfHo7yqEP287kyie0b2CyjeukBFhb6a1ctFikm8l3ea6UqLdlYvu2ZIfvg8xNR5Te_g2ypoaWBqrgkRh7fhMbEGvuMLqH8lXTxiSAS3EjmLUSK8_sh34a3tmJpj7VgEPMCfJ568sKmgEPzF5zO56rsDmrHIRyYxIFyGveWjgP5mf2ZWG1F353D2A34UQF87lEvUAQDuN_5rgo1I-QiwTWxd_E6hNAT5CESd3A87uRT_rYqwcrDPQw1XHEqiGX4qpDXmCPOahuDwvemJ18bRIfTsmj9zMspmkQX8iHnavyLqjLTe1bR-f65l5YmKDFv_Vb6kC1UlaF__kr_zGpPUn0tS2NpkUL786un-pYgZM_J2Dw86i7v56LA68iwLZMvkBbyXXgws3Bo0sfxB4gaTo_3T-CA6DJLt2fpHpBvxyC1Pd3IZn-_5MDcfnY5IoqxYuLCmlW7xI_cXjWqdFzKEpDJeFXS8mp_OnpNaluh5IKZ6ZRdpg7_DgrNV9rE8YUrLNJKrVmXOZvDgJPsdvNDtvIU-sr4Fp2A0Jnyitn-I105IjgmTdIDozTCIx8md5wmtdVjQGmpBOMRr3gga65kkXoxwKPbE75LgCYTuiMa_tNrLLR8Sq_bjjWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675844bc07.mp4?token=SSZWfN138PUxDjwccbdUKiZqdckYc82Rm3JaC0FDHPF7bIqdfoAdCgfHo7yqEP287kyie0b2CyjeukBFhb6a1ctFikm8l3ea6UqLdlYvu2ZIfvg8xNR5Te_g2ypoaWBqrgkRh7fhMbEGvuMLqH8lXTxiSAS3EjmLUSK8_sh34a3tmJpj7VgEPMCfJ568sKmgEPzF5zO56rsDmrHIRyYxIFyGveWjgP5mf2ZWG1F353D2A34UQF87lEvUAQDuN_5rgo1I-QiwTWxd_E6hNAT5CESd3A87uRT_rYqwcrDPQw1XHEqiGX4qpDXmCPOahuDwvemJ18bRIfTsmj9zMspmkQX8iHnavyLqjLTe1bR-f65l5YmKDFv_Vb6kC1UlaF__kr_zGpPUn0tS2NpkUL786un-pYgZM_J2Dw86i7v56LA68iwLZMvkBbyXXgws3Bo0sfxB4gaTo_3T-CA6DJLt2fpHpBvxyC1Pd3IZn-_5MDcfnY5IoqxYuLCmlW7xI_cXjWqdFzKEpDJeFXS8mp_OnpNaluh5IKZ6ZRdpg7_DgrNV9rE8YUrLNJKrVmXOZvDgJPsdvNDtvIU-sr4Fp2A0Jnyitn-I105IjgmTdIDozTCIx8md5wmtdVjQGmpBOMRr3gga65kkXoxwKPbE75LgCYTuiMa_tNrLLR8Sq_bjjWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باید برخاست، دنیا با آنها و مولا با ماست
🔹
لحظاتی از شعرخوانی محسن محمدی‌پناه در مصلای امام خمینی(ره) تهران. @Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/446597" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446596">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpQoYbU0yiRc7Bi6cLCuNTBBG1-LOburSVALSCukkDr4sT3Wnf6ACmWrxSr99LsE4_lF_4nZOZ04wOfkNI1zn1C9-lVyJh7r6N3tJR9530IYjI1GmVcPlRhD-8N83TyubFt_7Mr4gxKapVx2ilg_QSwFEp-SliUAakum9n4IZscYuimZz_dwo1_w6p4auErymYn9GszYkcsv3dAWGZk9GmEfiTu1eRauod-dI7ddjp5LMuKQEwecihukPDeYJeftCe8rBHWUrblYD5qIFimzXJVVO9GebLj9mbu8uoqzAK7ywi_saWy8rrcF_-bktEnEjPNAKa4htEdCy8X9eoh5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قدردان همراهی ملت پاکستان در دوران سختی هستیم
🔹
رئیس‌مجلس سنای پاکستان در حاشیهٔ مراسم وداع و ادای احترام به رهبر شهید انقلاب و تشییع پیکرهای مطهر، با قالیباف دیدار کرد.
🔹
رئیس‌مجلس در این دیدار گفت: ما قدردان مردم و مقامات پاکستان هستیم؛ مردم پاکستان، دوستان دوران خوشی و سختی هستند.
🔹
رئیس‌مجلس سنای پاکستان هم گفت: من چشم‌انداز روشنی برای ایران می‌بینم و با پیشرفت ایران، صلح و ثبات در منطقه نیز رو به جلو حرکت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/446596" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446595">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
باید برخاست، دنیا با آنها و مولا با ماست
🔹
لحظاتی از شعرخوانی محسن محمدی‌پناه در مصلای امام خمینی(ره) تهران.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/446595" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lm90PJdYeyXmSnzOXLemFC6YqUGmbTZq3_j52kMtJe7Qry0UbERC5kWe68UdYArQ295-9gOit4gIvqC-rvGo9r2kzIDEpQhzVlhoDZ8rET9MwFOi9yu78pRXC-hT1RElv2kePHN0tm8U7cFGD5rjk7WOsPKvVfj-RHnr08YBK3xtjWAHMpicudDA34HFP73MNZbGKC-7WvtIR6nKl_-CHORxTuD9mU1LsYqfal4FNo2qHuI4-JqZinthQfmsod6efsO8q8GIIAfK_4f71BKcXtmpdTIY_lC44uQtkXtpK770h6TXQ7rMvEdD3o71Qfh85pzdezEm6Wir9XJWJJqksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gP_Q2utfHoHW-SUv98VTp-0zUjDCuK0V2OQ0xpfWdAG_so3fDxIRxt3rcZkzkVrYJ-ou0aTNHAn4EXhnKVTbUpK205Y2V2MJaWCNOp4ZJUQVZgnO7dNE9SxleydVKY7wIK0hrlPysjmOmi5RmCflTR__HroNHdtib-nJvg-ooErXmLoF8o_jY7v1NP2GGUm0Yyfw4pKnqUBgZ62N2tOx_z-THuUFUQ7u8pbKLR14_Yzndwtc-Jegg5S7NelmxuAt1QHMumWP4Y4jAUTJh0yrPqHgKomSIJgEQxgkyZ5tKT9BfyoTkFS4mpwtF9SiXc3zVv98stAUWTmHzjchd4gd1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور پاکستانی‌ها در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/446593" target="_blank">📅 09:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa20970f7b.mp4?token=krRv6GFWFCgATPiXX1PYzo_1o-wcFpnZsbDPuLIb0c5748vwsanERawO4_r7Sfa_5OdtXXSSlIgqEzPQ9wkRNYN6jSG78631sL7L47n8QV_TKLbsB8vfKIxkW1yc3CMXht0Nhbw_XB-2JAPpqxeVDqzBvFX66WfxSCMk6MOty7fiFlzQ_ozDciyCHiUYhh6L_XqzpzVyZbuk2mO2Ztqm917PnozhthMG-smtd1JvzaxDGcS9E6QZ8Xai55ehaJbB9r4_LvYvV7G-qM1IgU3werQur_mN0TONkXNhga--u2_67OwRTpQ4Z-AbuQeSyVoQHG_tTzTQVQQ3L0W2l36VH50hHCoMjMvXXfraPJ_pZXlEQsrIysesvA2rW3VlBQ7yrAAmfF0XqvYdhBHvlZEeDe2Z-n5PhhtvEWiFi7ZNIPsvHq_ZcdFuYrNLptLSlt7C_K64CmDG_n2CTw8j8FW5z3OvSJFxqzp83N4x38yBOFSC9aWE0gS72heROu0xHA_dkTOySgWUj6ZOEmIrtziiwJRVgofG0jZPYLp9GWE5z_ybaDK5YomDXG9fFooV-lQs6pJBpRzZ6u-FXO0xmFgL8a_o4Yqy76Iy5056cxoR6nlYl2jQhSLyfWDV7ds7ap5yHpMus9ur_3kBouEIiWvK90i48xM9CTeNF0XcUOVCFwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa20970f7b.mp4?token=krRv6GFWFCgATPiXX1PYzo_1o-wcFpnZsbDPuLIb0c5748vwsanERawO4_r7Sfa_5OdtXXSSlIgqEzPQ9wkRNYN6jSG78631sL7L47n8QV_TKLbsB8vfKIxkW1yc3CMXht0Nhbw_XB-2JAPpqxeVDqzBvFX66WfxSCMk6MOty7fiFlzQ_ozDciyCHiUYhh6L_XqzpzVyZbuk2mO2Ztqm917PnozhthMG-smtd1JvzaxDGcS9E6QZ8Xai55ehaJbB9r4_LvYvV7G-qM1IgU3werQur_mN0TONkXNhga--u2_67OwRTpQ4Z-AbuQeSyVoQHG_tTzTQVQQ3L0W2l36VH50hHCoMjMvXXfraPJ_pZXlEQsrIysesvA2rW3VlBQ7yrAAmfF0XqvYdhBHvlZEeDe2Z-n5PhhtvEWiFi7ZNIPsvHq_ZcdFuYrNLptLSlt7C_K64CmDG_n2CTw8j8FW5z3OvSJFxqzp83N4x38yBOFSC9aWE0gS72heROu0xHA_dkTOySgWUj6ZOEmIrtziiwJRVgofG0jZPYLp9GWE5z_ybaDK5YomDXG9fFooV-lQs6pJBpRzZ6u-FXO0xmFgL8a_o4Yqy76Iy5056cxoR6nlYl2jQhSLyfWDV7ds7ap5yHpMus9ur_3kBouEIiWvK90i48xM9CTeNF0XcUOVCFwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یا فاطمه (س) ما بعداز این خون‌خواه فرزند تو هستیم
🔹
شعرخوانی احمد بابایی در مراسم وداع با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/446592" target="_blank">📅 08:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD96Gdun1AeTIZE0vM5XwuPTo56Zt3uOVA472jRzXSbQCtAXgK2mf2A2lih51mqr4nLRaTGoa1fAu9KNcYd7D1YI8WxsX9OVHfo62y9vwtV2QKvFNQnown6Dn7x-lPBklgReczrq2LgJ9Pvo0dA6WdnbNqK5MxzUPeJ8w99WuNtAyj6sa_K0qRuww-7o33MV8IWmbejiv6Q1Nnn3o6n5kYbzCjp2PNnxVf-cwH1x8GRXYxI21apAc05oATRfvb1ouVL2SsRPulaNUl11uDMuBDhlk9y0jThInGPlIdnKGysn9vLHYtBrqtaUwH9R6nXn2y-LgfVWG1CJaCjDzkYe50pcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD96Gdun1AeTIZE0vM5XwuPTo56Zt3uOVA472jRzXSbQCtAXgK2mf2A2lih51mqr4nLRaTGoa1fAu9KNcYd7D1YI8WxsX9OVHfo62y9vwtV2QKvFNQnown6Dn7x-lPBklgReczrq2LgJ9Pvo0dA6WdnbNqK5MxzUPeJ8w99WuNtAyj6sa_K0qRuww-7o33MV8IWmbejiv6Q1Nnn3o6n5kYbzCjp2PNnxVf-cwH1x8GRXYxI21apAc05oATRfvb1ouVL2SsRPulaNUl11uDMuBDhlk9y0jThInGPlIdnKGysn9vLHYtBrqtaUwH9R6nXn2y-LgfVWG1CJaCjDzkYe50pcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای ایران قوی، ما همه ممنونیم ازت...  لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446591" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
اصلا نمیشه باورم...  لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446590" target="_blank">📅 08:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446589">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متروی تهران از امروز ۲۴ ساعته شد
🔹
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446589" target="_blank">📅 07:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589f19bd5f.mp4?token=mskCEnBOhqTqpvI2YdUZKcPTOiSmLuyIrFGaBGUm4Rd3tRqq566FSEJsT6gJviSnKDkFrOX945RRpUCkcs3w_CpJ31M6d0AOzsNNRUZF8lUOYXfLwxbluBaUdV-lW6HFZJK3Rnf7S_vgQo89wx06qFikzk5l1n7ktUG2vk7htATM5xR1K3z1jmR4yBWLub-GStfE0U8ME22wMxDAslRQcikchOsaCSZ5roRVLagx_yuZSCukEgVU7t4FgWSkVa-vJqJO-eZD1W858OE4S-b7VJUH9eALtv8OYTahf-5LgoemUsDYQKcA6jNt3HSq1x0571ZRvWtpGjxLpcuQwySbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589f19bd5f.mp4?token=mskCEnBOhqTqpvI2YdUZKcPTOiSmLuyIrFGaBGUm4Rd3tRqq566FSEJsT6gJviSnKDkFrOX945RRpUCkcs3w_CpJ31M6d0AOzsNNRUZF8lUOYXfLwxbluBaUdV-lW6HFZJK3Rnf7S_vgQo89wx06qFikzk5l1n7ktUG2vk7htATM5xR1K3z1jmR4yBWLub-GStfE0U8ME22wMxDAslRQcikchOsaCSZ5roRVLagx_yuZSCukEgVU7t4FgWSkVa-vJqJO-eZD1W858OE4S-b7VJUH9eALtv8OYTahf-5LgoemUsDYQKcA6jNt3HSq1x0571ZRvWtpGjxLpcuQwySbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مردم در مصلی: «انتقام، انتقام»
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446588" target="_blank">📅 07:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446587">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=NH_A7Q0PM5o_EBFTnmRNHfatJ_Nk-bVcYv6VllVUTrAfRWAZV0fgiQY-Yl-oXFZlnkjy-gtAZ4sjqXIamy1BVjs4fXKvw2ukhO8jRgui2MioADd8vQzYk2VRB0gisDt4RoYnzdt3d-tLdF9AAnLvyz_FbeEKlzkEjBfY1fSdv-JoVsd2Aj-AzlVpnvb-QwfrqFbKcesKr4dBqqvmYwvqtVSK4U_HtCpr0BzmysLQKvFCMiCJr5Xm0rwIE2MD04g_FS6QQqZG6Mqm_e-fULxZfHAbn0enABlcgj7V7gKIt2gJOkZaawYoBQzZBherc-CIsM7hB2Qf-c9dcWPZIWk8t6Dqe55OocOL-zqAhfxvJaEIiWAQS1n-UM4zCq7Nh5ui4scSmNMT56_Q0waLh4XHLqcLil1RpT12xdzUdekGqjmC1NHGfYfSOiXLmMbdl1iRMGUQMgyeZT_Gale_6DXOJTya9WAnHI9WKn26VZuxlu1EF9qFOr1kSY65Gp_hn9pkkPbPq7g_YdFSbGC2VInRkTD6bGcuGkL9vArrGtWeSVEMsyj-3eJsv4A6UA2Lg3u_lu9qneR1QVAWXIwJYic2qf8COCL6UmtwqB4ODZ6aEIXsdt6eVJwITuBiQYTSL9NLyAWgq3eg-egiptDy6Mt6ePOTH92cq6SuhQkzfCRm6NI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=NH_A7Q0PM5o_EBFTnmRNHfatJ_Nk-bVcYv6VllVUTrAfRWAZV0fgiQY-Yl-oXFZlnkjy-gtAZ4sjqXIamy1BVjs4fXKvw2ukhO8jRgui2MioADd8vQzYk2VRB0gisDt4RoYnzdt3d-tLdF9AAnLvyz_FbeEKlzkEjBfY1fSdv-JoVsd2Aj-AzlVpnvb-QwfrqFbKcesKr4dBqqvmYwvqtVSK4U_HtCpr0BzmysLQKvFCMiCJr5Xm0rwIE2MD04g_FS6QQqZG6Mqm_e-fULxZfHAbn0enABlcgj7V7gKIt2gJOkZaawYoBQzZBherc-CIsM7hB2Qf-c9dcWPZIWk8t6Dqe55OocOL-zqAhfxvJaEIiWAQS1n-UM4zCq7Nh5ui4scSmNMT56_Q0waLh4XHLqcLil1RpT12xdzUdekGqjmC1NHGfYfSOiXLmMbdl1iRMGUQMgyeZT_Gale_6DXOJTya9WAnHI9WKn26VZuxlu1EF9qFOr1kSY65Gp_hn9pkkPbPq7g_YdFSbGC2VInRkTD6bGcuGkL9vArrGtWeSVEMsyj-3eJsv4A6UA2Lg3u_lu9qneR1QVAWXIwJYic2qf8COCL6UmtwqB4ODZ6aEIXsdt6eVJwITuBiQYTSL9NLyAWgq3eg-egiptDy6Mt6ePOTH92cq6SuhQkzfCRm6NI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصلا نمیشه باورم...
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446587" target="_blank">📅 07:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446586">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efeb113d0c.mp4?token=CIKd5d5HEokzljV9lzgQhuP7WQ_2mnBnh8rdKw5aVzMW4FePEedo927n-XrPgtanAsOcwL1F0on7AoQqVA9txgMmS7SK9zddo7lCI5lDCWRDncQ7Z_HMFgMXTwOYyWbCFftRvL79Kv6nEFHNCPnqxpygOFCdHDqUbwqdxyjwBQkdMSWj8ypgfK0zem9ibHYdH9pwm33Aw3b_tjDxr-unW2idP2bGl9xYTjiZsw-Nb0dipTj_K0Jwnb1x8lhjoiLbPlkC4y3cYaxP0m5WRsLvXivaeazAdb48YPiNjxVjoDKegVPitFa2ylV-cf35y1t3e3b8Yp8-iQc-Tend63KgZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efeb113d0c.mp4?token=CIKd5d5HEokzljV9lzgQhuP7WQ_2mnBnh8rdKw5aVzMW4FePEedo927n-XrPgtanAsOcwL1F0on7AoQqVA9txgMmS7SK9zddo7lCI5lDCWRDncQ7Z_HMFgMXTwOYyWbCFftRvL79Kv6nEFHNCPnqxpygOFCdHDqUbwqdxyjwBQkdMSWj8ypgfK0zem9ibHYdH9pwm33Aw3b_tjDxr-unW2idP2bGl9xYTjiZsw-Nb0dipTj_K0Jwnb1x8lhjoiLbPlkC4y3cYaxP0m5WRsLvXivaeazAdb48YPiNjxVjoDKegVPitFa2ylV-cf35y1t3e3b8Yp8-iQc-Tend63KgZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار خیل عشاق در خیابان منتهی به مصلای تهران: ابالفضل علمدار، خامنه‌ای نگهدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446586" target="_blank">📅 07:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446584">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=LFI5iXv0gxvDheIad-YgbIm8tnf1DAMHj_iKrZHwu4cOy0bLX7quLyniytjQ5LkebwF-TzyePzAuJbUvPsOBD_DLz7ju8XwLu-dLDIBxuYW9gVG6ilekdNDms9dhGT6OHTQTlx4vWxBSeartXUgoHyp5Gp0p_ZyxC5XJv0Jp8r8EQMVR5laQQJmZgGNi-pXGlhKIIPJLD5E8bHPvheOqDU3R1QzSkY-O6pK8Ntn9vVjMn2LZ-MoqnHyrLq5h8Wp8BotPkiQoCaeWjpdJN-oK6DK8_HwcA9j2HUN3F5plkoN4tcIi6bW5XJGhoIG0o863FLX8EwEMwCZe8ldkIvsvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=LFI5iXv0gxvDheIad-YgbIm8tnf1DAMHj_iKrZHwu4cOy0bLX7quLyniytjQ5LkebwF-TzyePzAuJbUvPsOBD_DLz7ju8XwLu-dLDIBxuYW9gVG6ilekdNDms9dhGT6OHTQTlx4vWxBSeartXUgoHyp5Gp0p_ZyxC5XJv0Jp8r8EQMVR5laQQJmZgGNi-pXGlhKIIPJLD5E8bHPvheOqDU3R1QzSkY-O6pK8Ntn9vVjMn2LZ-MoqnHyrLq5h8Wp8BotPkiQoCaeWjpdJN-oK6DK8_HwcA9j2HUN3F5plkoN4tcIi6bW5XJGhoIG0o863FLX8EwEMwCZe8ldkIvsvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
ای ناگهان عزم سفر کرده، خداحافظ...
🎥
قابی از پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446584" target="_blank">📅 07:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446583">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdOuSx43CWN7lULFyV9MDJdqwUVHCoghybXzDZSZWMroHAaJZgQM11OImzovsyX2UfuJTj6zLWpgOg3j62CIQgCKhX1OT4rGtxWTmv_lgiHz-IQRbmfKncsvZBmUmglZcPTeI2UPponOg5ISBm4rswTrsETj9UuA7xwQu1TIbMaoBxA3EJ1tNej-HiyYXr4of8ecZlotSVgwe7QM60FyGKFXJhWIh1FdHxZ2kVNlR_ugOdEEwGIMA-b9sdmGDtn4_bg7LBhhAm74GR9Wm8Bw_rVk0sEoe8e0kEk9uLBRctG68uySmz2TSPfAJIV73ntxbQr3Kw5UE64rDXBm_HQQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
پیکرهای مطهر رهبر شهید انقلاب و خانواده گرامی ایشان در جایگاه برای وداع مردم در مصلی تهران قرار گرفت
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446583" target="_blank">📅 07:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446582">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542913cea4.mp4?token=rhaIuSYQwkMgOVIlPMw7Z1M1rV3DwJnMbBMB7-2isQgwNTts7DXOGa8paYzZeIKYLe74Zra0IxuySC42SnVC2vb8dnqApz-ggbm6WFJXsoXBS-rCGfqJ0_6h_F1O5tWBG1xCQXsTlh45nshysA3HpRAwKG4zNT2kgPY_O59Dbo_g1KJ9xkgaWu4JwBCnCJPZTIasKsA6nImVCoNH3sWDvUENpFmjVC9mR2gG17zKwQzbYgLOU2foi4ktFdfLpSDf6P1ZQrLTO5cepys3zWhEUdMBf5-ZHf3JxDCvhbVqdInYbJGTGCFzyWLOLdYMv5XyvLrWLpqAyh67nWxE08zAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542913cea4.mp4?token=rhaIuSYQwkMgOVIlPMw7Z1M1rV3DwJnMbBMB7-2isQgwNTts7DXOGa8paYzZeIKYLe74Zra0IxuySC42SnVC2vb8dnqApz-ggbm6WFJXsoXBS-rCGfqJ0_6h_F1O5tWBG1xCQXsTlh45nshysA3HpRAwKG4zNT2kgPY_O59Dbo_g1KJ9xkgaWu4JwBCnCJPZTIasKsA6nImVCoNH3sWDvUENpFmjVC9mR2gG17zKwQzbYgLOU2foi4ktFdfLpSDf6P1ZQrLTO5cepys3zWhEUdMBf5-ZHf3JxDCvhbVqdInYbJGTGCFzyWLOLdYMv5XyvLrWLpqAyh67nWxE08zAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزا عزاست امروز...
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446582" target="_blank">📅 07:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446581">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf5d2e7c.mp4?token=u5O-kofjR-PvyYPjM-IpEF3ETSQ1Q9BojDPqjwUx0FXTBb4gKwzdyAAUUym1xHsUO5TNzw_IxdAKrk3xuiIxiJrEI3r-2jZiztnRzOWeNg2RMUvFgRCV87fbe9y-0tpSEMOdG8-6Dxt_am52Nas0cRHjH2Uf8vswC-8ZkokPICqXMu5FbiO9h2GJEv8SlsGcOfzFjsLO-Ghf6G9BK_lymjS1_wsPztEUprGY6Y9bOTzA0Zk9L3iRnqKvvPzQt7Lp1Q8qpfX-a6Sg7Jk5Ab6YVLIi66kYBGG-kzqGKlJ9i0hF2hwTNz1oGA74Y7bDeRn7xYkOncZ3MoUPzB_PoeROnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf5d2e7c.mp4?token=u5O-kofjR-PvyYPjM-IpEF3ETSQ1Q9BojDPqjwUx0FXTBb4gKwzdyAAUUym1xHsUO5TNzw_IxdAKrk3xuiIxiJrEI3r-2jZiztnRzOWeNg2RMUvFgRCV87fbe9y-0tpSEMOdG8-6Dxt_am52Nas0cRHjH2Uf8vswC-8ZkokPICqXMu5FbiO9h2GJEv8SlsGcOfzFjsLO-Ghf6G9BK_lymjS1_wsPztEUprGY6Y9bOTzA0Zk9L3iRnqKvvPzQt7Lp1Q8qpfX-a6Sg7Jk5Ab6YVLIi66kYBGG-kzqGKlJ9i0hF2hwTNz1oGA74Y7bDeRn7xYkOncZ3MoUPzB_PoeROnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم سرود ملی ایران را در مصلی زمزمه کردند
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446581" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446580">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=gny2WN6Ydgzg4EQVunRLuMzCfgOQOyHYc090nux3-LAeeRcOn-DfgKUY0gAjqu9JgQhPILb9EM1-bE0-r_xfSCENF-7rPP2Yd3agUvuvx8wG1rixOIbT9uwvnmcXTGQQUETXVTFiRwi0maoIJP24FaCniJEWFdV_-krEwEYeFzUgifDh5Q0ztpDCMBy-MZ1g4dJETphSrhkXrkRhXFi9WsQRbBp5-4GCImgC7jsWe2aP2iUG1aPqZJ6sWVjDWubj_0kqDkMXLp2s1sxdvMKdnCxoGTpc9tZgPUw8Hp1KGug07TKRdb64QcksuPVXv9IPfMfcPYlYXKgLDXaBy8aPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=gny2WN6Ydgzg4EQVunRLuMzCfgOQOyHYc090nux3-LAeeRcOn-DfgKUY0gAjqu9JgQhPILb9EM1-bE0-r_xfSCENF-7rPP2Yd3agUvuvx8wG1rixOIbT9uwvnmcXTGQQUETXVTFiRwi0maoIJP24FaCniJEWFdV_-krEwEYeFzUgifDh5Q0ztpDCMBy-MZ1g4dJETphSrhkXrkRhXFi9WsQRbBp5-4GCImgC7jsWe2aP2iUG1aPqZJ6sWVjDWubj_0kqDkMXLp2s1sxdvMKdnCxoGTpc9tZgPUw8Hp1KGug07TKRdb64QcksuPVXv9IPfMfcPYlYXKgLDXaBy8aPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در خیابان‌های منتهی به مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446580" target="_blank">📅 07:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d25574b.mp4?token=Dq47UCEQbQ5JnqgVA6HNAUlKbz-IJWg6QbiDJ3QVRLY7zzBWqSoIImIuos5nmz8uW4-6sxtl57zpBfJfnueazewnfaknaAfMs2SFANAHm5zeO_OjEHGA9cAC4QRLFu_a5vyE1hyGTS7LD6C4Xs1s7rf2LvE5M9l3tVPpcDaFr0skV46Ne_XLVX6OpyLm5OxOxWUY1p5Gz3Mm7dvtgcsxzARUvR17LiDPJVsf40I4v8TTJtowFPmF5YPJBAHNqSGCJFvaA_t_8blyquEI9mX5YoxTyepryWzRY2H6rHAOLB5ORu0aZPnO-tRR384xlkjvjs1DlqKWLwQYFyMoDxGdBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d25574b.mp4?token=Dq47UCEQbQ5JnqgVA6HNAUlKbz-IJWg6QbiDJ3QVRLY7zzBWqSoIImIuos5nmz8uW4-6sxtl57zpBfJfnueazewnfaknaAfMs2SFANAHm5zeO_OjEHGA9cAC4QRLFu_a5vyE1hyGTS7LD6C4Xs1s7rf2LvE5M9l3tVPpcDaFr0skV46Ne_XLVX6OpyLm5OxOxWUY1p5Gz3Mm7dvtgcsxzARUvR17LiDPJVsf40I4v8TTJtowFPmF5YPJBAHNqSGCJFvaA_t_8blyquEI9mX5YoxTyepryWzRY2H6rHAOLB5ORu0aZPnO-tRR384xlkjvjs1DlqKWLwQYFyMoDxGdBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این تلاطم تمام‌شدنی نیست
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446579" target="_blank">📅 07:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446578">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJOnp4QRcYq4-PYYsDSZkydQEj7NG2souH4silaDewiDWoBy4JzAhtfYH6-43vucOFjPbxU1CfSR9t8q4DINZ_u9xgr5i7b7z2jDOR4wGzJ3sarq2vJxfdgowbrzssKgs7Cp4sIp89etKHhF1lpNgWWXL4yUYuBq7VxfsIQwtZIIDK9bnNYD-VgEp6fpaOtVRkNSYeG32dpakUFC_2i91SAGrnWSRGl1cHbicQnzmrHEIfIPlBbDLN7HmqcXfKmnskWZ9pBpS4Ys3gVMVf4tMRaJgH1SabSt3mLHcxj63y2uRxNwvMIgfG_igFp1c0ujEkCFN4MIjkwZZjv_vvpaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وداع شاگردان کی‌روش با جام
غنا حرفی برای گفتن نداشت
کلمبیا حریف سوئیس شد
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446578" target="_blank">📅 07:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446577">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-G3LDmEOc8cgF41WiN2uRUhGhrkLUulGrNb3T_Y0iYX9fYtsqbsa4qJfokaunQrPLIRdp-KbKz4ZQXihx9VKYIH71a42rkxxYvlWbZaH8p-e6w7rRzJBZ56ZyrDlYLpCUQCrXzyppW9gHWpXdeuuBivhHlFdZPbPL7rKLUkkNrFG2DH-6av_rakzNWffeARMCwGdEL8DE58GqtdKzXlZBsRDjl0D-CdJfRBNDZqt2yEElDc7rXBOjGG7FsMFf2GnVEN7OmRIImGLSHcIqlVLVGU5tfxmSKz4eyqA9Ub1pXzq-6d8hNkRWdTMDQgw4UgidVkFXOeDVlJ4LyscJz-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مهمان گرجستانی اولین روز وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446577" target="_blank">📅 07:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446576">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3438c87d.mp4?token=mgdYlkF2WcYAc1vxG88iA6dIFzZayusLmIGm9N2DLzbo54Ks7jM_UVxOvGEuOjYd2toun40mVPBzAqAyYtEop4G1FiJrDuOlupBrCmT0u6ApJbO-aD7e65NZ3urzulgGNsafiHgsGbcb4LeK-HMHWWoT2vePtV_yU6fYYeen4fb1b4f0xjI-Xcm5_tnvlF-avybj-99GXt_zwijnZw6IX-SX7kQfqv_mM1xo4Q7el6YJhvkEXw8p-Npyfk-w9HrpmSY6yFtAjIWbb4U9-5vQMhTpWbDkVL1x2CDNpw3eR-NRIPSHqFj6u1MUKVagXt7mGwUUEz4jmLVBLQ6MmVYuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3438c87d.mp4?token=mgdYlkF2WcYAc1vxG88iA6dIFzZayusLmIGm9N2DLzbo54Ks7jM_UVxOvGEuOjYd2toun40mVPBzAqAyYtEop4G1FiJrDuOlupBrCmT0u6ApJbO-aD7e65NZ3urzulgGNsafiHgsGbcb4LeK-HMHWWoT2vePtV_yU6fYYeen4fb1b4f0xjI-Xcm5_tnvlF-avybj-99GXt_zwijnZw6IX-SX7kQfqv_mM1xo4Q7el6YJhvkEXw8p-Npyfk-w9HrpmSY6yFtAjIWbb4U9-5vQMhTpWbDkVL1x2CDNpw3eR-NRIPSHqFj6u1MUKVagXt7mGwUUEz4jmLVBLQ6MmVYuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی مغناطیس امروز پایتخت شد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446576" target="_blank">📅 07:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446575">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f042e46d24.mp4?token=UX-i5lP0HcPED1XNEErI_wLDoOcGdyxCBurhAGzZo_svXnxClpx2YNQccmOMhMN2Wj01bGiuchGtPbA2-CH1yDnxCZdgZ-gDwgWgN-BmUJ9uIIiqcCw9x4E-5jkgL-WTwBzdFIMMxof_EYQ3wNWwkq2JZbyRvOdRO2qXbomtwELCjCJw3dExEGb9qOh-FhstDz-jqsoi_1EgE0T_RRqXlS2sqQFcUfpmet-N_Oitx5t1TIC5uGczK4T3ixsjmK6fzDBfOkD1XJn5iDpGMnGfBYSYd_LNZ00OxqjQ13eTSU--O0CT0YAGpPxMVhrhjdIM8U_k_HU5O1K_ODQp0cXhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f042e46d24.mp4?token=UX-i5lP0HcPED1XNEErI_wLDoOcGdyxCBurhAGzZo_svXnxClpx2YNQccmOMhMN2Wj01bGiuchGtPbA2-CH1yDnxCZdgZ-gDwgWgN-BmUJ9uIIiqcCw9x4E-5jkgL-WTwBzdFIMMxof_EYQ3wNWwkq2JZbyRvOdRO2qXbomtwELCjCJw3dExEGb9qOh-FhstDz-jqsoi_1EgE0T_RRqXlS2sqQFcUfpmet-N_Oitx5t1TIC5uGczK4T3ixsjmK6fzDBfOkD1XJn5iDpGMnGfBYSYd_LNZ00OxqjQ13eTSU--O0CT0YAGpPxMVhrhjdIM8U_k_HU5O1K_ODQp0cXhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از سیل خروشان دلدادگی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446575" target="_blank">📅 06:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446574">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a947bd8001.mp4?token=pIRF04q8EXcFqBFa_KUAVeiDJIhpIqYImwPd4QuAogPR4i7PNBjLSDXrtwnzT6tYUApJvvoFS_3PGDPQr7EpU3aEsxyVLHKfv3b1fd3ici7e2tljk1KX7OJyPfu924pG4LKzryDPGK2_5OWMC1jTdYso3XkySOoM-7pxOAHe6m0KyuVlCSktFPC0rRSURDCmcYBfx5gC_C_3UJbVzHXmZW1WXw1o9GdzQsZV4tgjaizEQCcbMxpCbyq6rncomp03mFX5npVC2CiszLgdJdSyOPZ14xSp7qPXnLT6KH7NpRIZh9xh9Depo-_ilERsWtwJAR4AdWLhJPnvahZzlbpJ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a947bd8001.mp4?token=pIRF04q8EXcFqBFa_KUAVeiDJIhpIqYImwPd4QuAogPR4i7PNBjLSDXrtwnzT6tYUApJvvoFS_3PGDPQr7EpU3aEsxyVLHKfv3b1fd3ici7e2tljk1KX7OJyPfu924pG4LKzryDPGK2_5OWMC1jTdYso3XkySOoM-7pxOAHe6m0KyuVlCSktFPC0rRSURDCmcYBfx5gC_C_3UJbVzHXmZW1WXw1o9GdzQsZV4tgjaizEQCcbMxpCbyq6rncomp03mFX5npVC2CiszLgdJdSyOPZ14xSp7qPXnLT6KH7NpRIZh9xh9Depo-_ilERsWtwJAR4AdWLhJPnvahZzlbpJ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم یالثارات‌ الحسین بر فراز گنبد مصلی تهران
🔹
همزمان با برگزاری مراسم وداع با پیکر رهبر شهید، پرچم سرخ «یا لثارات الحسین (ع)» بر فراز گنبد مصلی امام خمینی (ره) به اهتزاز درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446574" target="_blank">📅 06:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446573">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553be7ddd5.mp4?token=qdYPG_ln3WhGVerAbclSemkGrWG95GxY_l0wpc_ijsBQNsZ0A39UqPs3tj1xJjaUzSudHBZ1m4Htb07ww9vqfIGyCW9REyOMLzzKoUX6iIoEb-awppQ3LYT344mO7C2RnXyo434ADFDxNAr8KF5a6wDMAUzvZHKdyDZ2AydasqZzHIFrEfe3erqh9yJ6rwaYLDHcnRI3RhyDMpPoCP9XvmPEoqtHMBCZ4bRaZaAlhGu-80wUZp60shWMV8cylnTSQWCQIAd7o0rMVsS8mDVfXKx3VMSoekuyNConyDmmxE98Oihwd5Kch3MEsHoEgeBSakLR3Al6mWjgzJBHwK9fVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553be7ddd5.mp4?token=qdYPG_ln3WhGVerAbclSemkGrWG95GxY_l0wpc_ijsBQNsZ0A39UqPs3tj1xJjaUzSudHBZ1m4Htb07ww9vqfIGyCW9REyOMLzzKoUX6iIoEb-awppQ3LYT344mO7C2RnXyo434ADFDxNAr8KF5a6wDMAUzvZHKdyDZ2AydasqZzHIFrEfe3erqh9yJ6rwaYLDHcnRI3RhyDMpPoCP9XvmPEoqtHMBCZ4bRaZaAlhGu-80wUZp60shWMV8cylnTSQWCQIAd7o0rMVsS8mDVfXKx3VMSoekuyNConyDmmxE98Oihwd5Kch3MEsHoEgeBSakLR3Al6mWjgzJBHwK9fVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر لحظه بر سیل عاشقان رهبر شهید در مصلی افزوده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446573" target="_blank">📅 06:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446572">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a292515d66.mp4?token=RRuatViStVeKpzlrjr-qwfyWOBmCUiSseI--bLr20wN5N5d80aafJCbN_2XTQVq9cwuElWcWZ-eZSfejwlde7PgKcgHihYEcyUQt5pKD3do_v7NwZcVWShvkIL5lFoQFXOLyxkU03ATdclm7hxo-F-Wg3nUw_6W2aJN7bB4XoO-3LQgOlKOrrnv67kqWJ9j2PlY1xBgHlZTRDxrREGtvtNOqr7-k0OPVB2nUdUkfKBAtHrHsdpH4mrdQzC6-KbuBfYAkpXBHvviy7N5WW8E4I8Kh5FXYwxeZE2aHYealP8UqpGhlZh_w5i6IaFINVz3aUVWFzUbevn7Lm_4GPHWXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a292515d66.mp4?token=RRuatViStVeKpzlrjr-qwfyWOBmCUiSseI--bLr20wN5N5d80aafJCbN_2XTQVq9cwuElWcWZ-eZSfejwlde7PgKcgHihYEcyUQt5pKD3do_v7NwZcVWShvkIL5lFoQFXOLyxkU03ATdclm7hxo-F-Wg3nUw_6W2aJN7bB4XoO-3LQgOlKOrrnv67kqWJ9j2PlY1xBgHlZTRDxrREGtvtNOqr7-k0OPVB2nUdUkfKBAtHrHsdpH4mrdQzC6-KbuBfYAkpXBHvviy7N5WW8E4I8Kh5FXYwxeZE2aHYealP8UqpGhlZh_w5i6IaFINVz3aUVWFzUbevn7Lm_4GPHWXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل مشتاقان درحال رفتن به‌سوی مصلی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/446572" target="_blank">📅 06:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401e987e60.mp4?token=mz3srbxE0IUSxeNZ8Tj0VPGwpv55X9RzbDQY96d7KXnw0IL-d-RAXAKjKZNtQFwySbfLmn-kHTPHtgt2wQpJSvi7hKDbd6jUBU91nKU_yFHbjnzwjj2Nm2CTMWw_gT8aadJLRTLZL4tQ9dzE5IenWWAuj-UbdaHtb15q58GULxlrIRpa-I9KaqVGPq2Hryjy2pDMKZKsauBIIfcY3oT1QCluEWSOLl8uHy8AYJaLPOEUHLKuZDT2qJuJ2ZhQz7Pew3JnO44KUYURP4kpaSt-L683IQV_FBb9m7753N15a8ExP3JNuHqT3B2wVu6RnrrIMatyqFmvqhoUf_JqwJ7sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401e987e60.mp4?token=mz3srbxE0IUSxeNZ8Tj0VPGwpv55X9RzbDQY96d7KXnw0IL-d-RAXAKjKZNtQFwySbfLmn-kHTPHtgt2wQpJSvi7hKDbd6jUBU91nKU_yFHbjnzwjj2Nm2CTMWw_gT8aadJLRTLZL4tQ9dzE5IenWWAuj-UbdaHtb15q58GULxlrIRpa-I9KaqVGPq2Hryjy2pDMKZKsauBIIfcY3oT1QCluEWSOLl8uHy8AYJaLPOEUHLKuZDT2qJuJ2ZhQz7Pew3JnO44KUYURP4kpaSt-L683IQV_FBb9m7753N15a8ExP3JNuHqT3B2wVu6RnrrIMatyqFmvqhoUf_JqwJ7sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مرگ بر آمریکای انبوه زائران در مترو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/446571" target="_blank">📅 06:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446570">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36339aa371.mp4?token=mgiWanhiTkuWfe7v0o-8W_tthw13xgLNkLSnR07dnAiMI47WmYP74W_heyjyPlenYvi2bN1QyGi6Cs7naam6UpCfEjo51J4f0KETN1dm_rNawvsZWF34k5_PKIhP03PB-sWn3ehWRgTT0f_EViZ3KXe_L3qKOQyZWM7S0w4bPe2xck70HWO_04R7rv5BPzbfvxmU4pIES-Z9Im5fScxFvDje6ixT2-R2aUGS03kOnuwM2HnisLsc0xmM9Jn3uSQN1esDSWEdDWgBmK0yoG7xWispY7cFQqQegy7zM5ytoAOx9Je0_t1dSSH-xD5bh41tydVo66vFZq1fXxO6lquukmD1yXzdkGS_WRdp0QX2rbxzWvCD-Ndrf_WRGqvUNjL-kzBHf6qKPjvp7K5zJM3jA6BfQ2aIZ89IojtvA-5yix1cS8BfpwXWapK1IyhhgS3_w7Q_C-DH6KNnw53S5wQYHcoW8-e_8Xe-OkPFwrrlcgd50LMJQNruj44aIiYGTCUX6HTwwGPjQQUsIanSJC8CBtCvopKjuoSZig8tLi8oL2XPFUtBDpZnHsoOTJJsyr84X4TLpKe6SL4cDkxCOrBXbBmfnqtW-5XlpDkERqdegepqeYqRFSlEGZxXEiZkJ_5eTKk5Eo49hIVSWGv9WK7GmLH39OMpg_hvee9e-Lm7axg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36339aa371.mp4?token=mgiWanhiTkuWfe7v0o-8W_tthw13xgLNkLSnR07dnAiMI47WmYP74W_heyjyPlenYvi2bN1QyGi6Cs7naam6UpCfEjo51J4f0KETN1dm_rNawvsZWF34k5_PKIhP03PB-sWn3ehWRgTT0f_EViZ3KXe_L3qKOQyZWM7S0w4bPe2xck70HWO_04R7rv5BPzbfvxmU4pIES-Z9Im5fScxFvDje6ixT2-R2aUGS03kOnuwM2HnisLsc0xmM9Jn3uSQN1esDSWEdDWgBmK0yoG7xWispY7cFQqQegy7zM5ytoAOx9Je0_t1dSSH-xD5bh41tydVo66vFZq1fXxO6lquukmD1yXzdkGS_WRdp0QX2rbxzWvCD-Ndrf_WRGqvUNjL-kzBHf6qKPjvp7K5zJM3jA6BfQ2aIZ89IojtvA-5yix1cS8BfpwXWapK1IyhhgS3_w7Q_C-DH6KNnw53S5wQYHcoW8-e_8Xe-OkPFwrrlcgd50LMJQNruj44aIiYGTCUX6HTwwGPjQQUsIanSJC8CBtCvopKjuoSZig8tLi8oL2XPFUtBDpZnHsoOTJJsyr84X4TLpKe6SL4cDkxCOrBXbBmfnqtW-5XlpDkERqdegepqeYqRFSlEGZxXEiZkJ_5eTKk5Eo49hIVSWGv9WK7GmLH39OMpg_hvee9e-Lm7axg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمده‌ایم برای بدرقه پیکر مطهر امام شهیدمان
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/446570" target="_blank">📅 06:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9d38515.mp4?token=Wvb8UpOiJWP24TgC6xrEC6s5zw5pnJVIdMobDC3k9qwadVZ20V6e_JNWTWyhPL8ClxOZ-DJH-FiX2zuaW9imP2kapBEwoU4hKNE7K7hXkmBzWNdLxeid3OxJPdYJccwu5PzNneGPnDCMb-hA4d3DUVwdin_6hqfrsof9KC0P9_2tlfgRvqt-EQAljaVyxqDbU4ocIZCatiixbFBIWlHAbzDY4PRcTXjIuBm8EAWsXO8ZA6KYt_6Z3TWrTl_czqJkpIV44XctMkqQTKwJU-O_0YYtLjcL-sB56FAkpfyO-Jb0n97h-ox8d36DdC4-oJyck4a96jZgcXf7LxJzWaZk6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9d38515.mp4?token=Wvb8UpOiJWP24TgC6xrEC6s5zw5pnJVIdMobDC3k9qwadVZ20V6e_JNWTWyhPL8ClxOZ-DJH-FiX2zuaW9imP2kapBEwoU4hKNE7K7hXkmBzWNdLxeid3OxJPdYJccwu5PzNneGPnDCMb-hA4d3DUVwdin_6hqfrsof9KC0P9_2tlfgRvqt-EQAljaVyxqDbU4ocIZCatiixbFBIWlHAbzDY4PRcTXjIuBm8EAWsXO8ZA6KYt_6Z3TWrTl_czqJkpIV44XctMkqQTKwJU-O_0YYtLjcL-sB56FAkpfyO-Jb0n97h-ox8d36DdC4-oJyck4a96jZgcXf7LxJzWaZk6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
جایگاه پیکر مطهر رهبر شهید انقلاب در مصلی تهران  عکس: صادق نیک‌گستر  @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/446569" target="_blank">📅 06:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh6eyhRJ92FQSBeEy2a7FvmBID2J-cxf-0ujnB739bNzclOT0dl9wkiKIeI6Xa-jf4iAqssxd1SsgmPviad2D4qe833vm9sDzBJo6wpcgG84EFOiOOMzkzF2u9qqzvfA_r9bYSqnT4KEXacbpJD3WyGEdMIeWg9QV9AZjZflLMH-96AbQxjFokWw1tTMwFXxyiUotysffJ6C0AUVfWemnq07XWeL_qbkJAxWitjSuiBywtfZ0AK8RStXeFYuYS__CzSmLfudLptPbPV8W7Now4eYcZ9i1eDJdfhYmudaDnyr88omA27Q_CR0Fswbend3Sguh-0yqmGRQ2NY5EeQKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آماده‌سازی جایگاه استقرار پیکر مطهر رهبر شهید  عکس: صادق نیک‌گستر  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/446568" target="_blank">📅 06:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446567">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f1e09ff6.mp4?token=hoPys8_Xtz3eBaXv87OjZI_qoDKlNhUROB2jpEMkNLeOFG4RJDTXoF3zj8rlAUnr1GTlcdaap9rgbAzwoFX0N1Ov23aw92BrDYj-pZnHcXL3ax4hpVqH0wWCHr0wFTjIygRqLg-0RLHhi3ec5IBmQOgtXGHBtgMZSleq6Lm__GZPEtVL-DoUPpoNp5ztCpqYpvTEpL4k5GlyUBB-eDTkBX-Q_w0tfQdXfWA8-rPhAfaRga2B_2neF_UYn9XsCXjRr5zjXNYvcqhzApcn894q-Ek25CdUhUufml6QW7Oyc0_9HdgvIlmkmdKDNbBG09Eu_lWGkti6IFBDv6MRcHaHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f1e09ff6.mp4?token=hoPys8_Xtz3eBaXv87OjZI_qoDKlNhUROB2jpEMkNLeOFG4RJDTXoF3zj8rlAUnr1GTlcdaap9rgbAzwoFX0N1Ov23aw92BrDYj-pZnHcXL3ax4hpVqH0wWCHr0wFTjIygRqLg-0RLHhi3ec5IBmQOgtXGHBtgMZSleq6Lm__GZPEtVL-DoUPpoNp5ztCpqYpvTEpL4k5GlyUBB-eDTkBX-Q_w0tfQdXfWA8-rPhAfaRga2B_2neF_UYn9XsCXjRr5zjXNYvcqhzApcn894q-Ek25CdUhUufml6QW7Oyc0_9HdgvIlmkmdKDNbBG09Eu_lWGkti6IFBDv6MRcHaHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت لرهای بختیاری با امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/446567" target="_blank">📅 06:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34406c17e.mp4?token=HSr2Yod9ShkTOhmoD_shhSg73BTbSST2izckSCCwhHwBYupILgX70nnpzSaobCQDxCDgfEU2Q7_-MVZ_Ns5Loumf38YfWeWwPOyTtgcFtOQjCMBU9868MF74H_dR5fP4uUTj_Xbpmv9YSXRmROl392MeynHTZb1rkyHM8HzMNialzazcR4ZFpdY__0aeA3wFr86O6xX8L5XVP3V2LeaQArJ7BYzV1SxmwSmciJrIKVYNa-wo_1ays4RdE4cF08dNo3QPBIWk5vChStrmM7UAXX5g5m8nlWfu3kKq3pl_6vcc-VqnueUr8zWvv1ykuOE8wdBn4iJaZVzuym-MAM8vjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34406c17e.mp4?token=HSr2Yod9ShkTOhmoD_shhSg73BTbSST2izckSCCwhHwBYupILgX70nnpzSaobCQDxCDgfEU2Q7_-MVZ_Ns5Loumf38YfWeWwPOyTtgcFtOQjCMBU9868MF74H_dR5fP4uUTj_Xbpmv9YSXRmROl392MeynHTZb1rkyHM8HzMNialzazcR4ZFpdY__0aeA3wFr86O6xX8L5XVP3V2LeaQArJ7BYzV1SxmwSmciJrIKVYNa-wo_1ays4RdE4cF08dNo3QPBIWk5vChStrmM7UAXX5g5m8nlWfu3kKq3pl_6vcc-VqnueUr8zWvv1ykuOE8wdBn4iJaZVzuym-MAM8vjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری دستۀ لرها در مصلی تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/446566" target="_blank">📅 06:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446565">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e02c94e76.mp4?token=QTEBrbZ0zmd0fiiEjf0QaejDX0k0KkDU99BkQri6ChR691NOQTKtt5pK3YXLq--mZIUGwXm43n94wZ-GPRB1d124OoSeuJbK1kg7xxTaO8I-28V8Fi31KbMuUJrfRtYQKuVmvTeRZ7BdVHjg91NG4JAKQtuOp9Us3UX8FX1ubB3YnN6I9yL9hgh4ulr3EBDHhvLX0IOCNew3TdD-IERSiQf4m6tEIWLdm1DAPQ0abLeySvNT2Mz9_5EFMhQgYEnK4Fs5fju7LYaL5N__Ua0Jebi1Hp0oWgQkv9EhbD5-18-JSGxYdOrDuXxt0EA199U_1S0MAKoLZ7sz1ZeR90FJ9kJdaOmVXT_g2ZP4Bhb9m8SCgeFA-oIh2xBcVAo_Wdt8ieWdtPJS_oikCGlWoRH8KjwT_99ajOumnn3BjftF-Hi98fXqpDyaH7rAjcJoosbBWvPQG5ZBEmoE2WVODR1bahDw5vCUjiFXcnzmJzz-1BmT3mi__6nq0PxT3hbqn6KCiijH2HHdaQ4liPSqJalOxP5BBXjio-EfqVZomUnhhgs4LAAtPBkyVDjfIBJciAME1Em5fy_Oo7YdXPCGn_O4HO0izP_cPKcz18kq03e4sTe0zQ20FyW5DyIRBZFBrVL036gHmFj_kKeIVBLwMo8o3YkblGpy1-s8_J3QnhTbPW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e02c94e76.mp4?token=QTEBrbZ0zmd0fiiEjf0QaejDX0k0KkDU99BkQri6ChR691NOQTKtt5pK3YXLq--mZIUGwXm43n94wZ-GPRB1d124OoSeuJbK1kg7xxTaO8I-28V8Fi31KbMuUJrfRtYQKuVmvTeRZ7BdVHjg91NG4JAKQtuOp9Us3UX8FX1ubB3YnN6I9yL9hgh4ulr3EBDHhvLX0IOCNew3TdD-IERSiQf4m6tEIWLdm1DAPQ0abLeySvNT2Mz9_5EFMhQgYEnK4Fs5fju7LYaL5N__Ua0Jebi1Hp0oWgQkv9EhbD5-18-JSGxYdOrDuXxt0EA199U_1S0MAKoLZ7sz1ZeR90FJ9kJdaOmVXT_g2ZP4Bhb9m8SCgeFA-oIh2xBcVAo_Wdt8ieWdtPJS_oikCGlWoRH8KjwT_99ajOumnn3BjftF-Hi98fXqpDyaH7rAjcJoosbBWvPQG5ZBEmoE2WVODR1bahDw5vCUjiFXcnzmJzz-1BmT3mi__6nq0PxT3hbqn6KCiijH2HHdaQ4liPSqJalOxP5BBXjio-EfqVZomUnhhgs4LAAtPBkyVDjfIBJciAME1Em5fy_Oo7YdXPCGn_O4HO0izP_cPKcz18kq03e4sTe0zQ20FyW5DyIRBZFBrVL036gHmFj_kKeIVBLwMo8o3YkblGpy1-s8_J3QnhTbPW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علمدار ولایت، لرستان به فدایت
شعار لرستانی‌ها هنگام ورود به مصلی
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/446565" target="_blank">📅 06:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446564">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94777c2b96.mp4?token=noG_KUAN-hX9CgYKx8quQJi7_qHshkw2-EyH2-X_k5Q1Oit8ZD9e0rW3VNrNQMXLdSNxkN41N9aZ3bVlsG7IkbGkiLGKYgcYxfNem1PB_pcxKnGZjShvtD9Lg6Fophc46JfrXOrqrXnCiH92QOYUiKsAJlJl3aQes25_LiR38N1SiokJiII83bBoAcBWUS6CyladpmfSht2U6ivDv_ksNQzFMD6sAhc0DLFzG7mu32XbfInwsQ1XXkULa8PS6Q4cI1Q4ZoqLAk8LNejafg9_PY3H4teykasiZKLnbBcabFf2F6bWeARyKpH94J5cremk6MjqyU_I7oJOyetErp-L6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94777c2b96.mp4?token=noG_KUAN-hX9CgYKx8quQJi7_qHshkw2-EyH2-X_k5Q1Oit8ZD9e0rW3VNrNQMXLdSNxkN41N9aZ3bVlsG7IkbGkiLGKYgcYxfNem1PB_pcxKnGZjShvtD9Lg6Fophc46JfrXOrqrXnCiH92QOYUiKsAJlJl3aQes25_LiR38N1SiokJiII83bBoAcBWUS6CyladpmfSht2U6ivDv_ksNQzFMD6sAhc0DLFzG7mu32XbfInwsQ1XXkULa8PS6Q4cI1Q4ZoqLAk8LNejafg9_PY3H4teykasiZKLnbBcabFf2F6bWeARyKpH94J5cremk6MjqyU_I7oJOyetErp-L6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلای تهران و حضور مردم برای وداع با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/446564" target="_blank">📅 06:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446558">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCV1euX2ueAmkWHrBAcV_mVQVpZPbBIx-UsHLeAN6ut57qdHBch8ktJEE6e8ibeYWRFQ_baNdB9HLbJ4tB4B6j5YK9ZDcJjD6cacNUSzdcjUDlsUD_4fqng9W4vX8kcFV2J-YHC1mQpSOSI69adei2spvTQwpzD-0MJGJhseMeHgpxBWWH6bRK76Ix67jCRTDIAvu94ZJBBANzxfYqTkO7aRITo92OUTd46Twib7StrwMwTYtdAkvxXQS6S4FbBX4NEQrtQOTRmKkOOh_x3Q9El2RNobIuio3UHBgiRulIMmq-_OndsIjMhdS8fE7wW1YXn-xdZ5rlUcD96Afr1ENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCECuXdIar8lWzUvzUCTf_aGgbkaFHIeA7w-zXvkyQLQYYFxlL3kbeBByJ8niUKJZqWWGxzduAYSUskvpmG9w2b1r8MdTbTuZZLl49X_bj-eklv4ulJRSKJ4cbbTcncjc1yLAAxRL3VpwvtTtc1YWJszDqLsuEuMYpRKEmaBNyaPaNKVlgErB1szjZP6GFzzIANG0WRUyNW_MqjwPE82A49I3jB2Xj5MtcxSF965Enf6Afw7WUb39OlqPs3ZkDZnNKIg6tfXStQwZF78xSVYdkGL0JsUGEkZQaFUG5zKxpUjCIgQ9dvyiGw4KR6W2Z9UhwDGb4Q-R3XTMSwYzk7JTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDjHJhEn_bFW8KOEMud9wgCtMGMJ6rGEuxcS-NaP3_QhSEJuDwCU3DSpoPAT3uxNZ56639tclDJrtdixN4KzFgCpmm9Aa5V1G0X2yvA7yf5FJ5IK-F7CscP430ZQWgfKhUZpTazuOLmMgscTsEbRAfTggA0fstedUx25Yn87gueDL2VnJUP-N_nS3EvfMzeXm5504v0QyGePWhakRRLhDFtBTYWQpzfzz_rw787nlRqtUOuoGifL-xgaKs5K3Htnb8tdjFWEDSh3RU7c49TswyErIgToTpvKsA_4SV17_Q9iTclcJbH6dJ-6XbSWUK1lOrW2d1p6_R9QO7HFvf04Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آماده‌سازی جایگاه استقرار پیکر مطهر رهبر شهید
عکس: صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/446558" target="_blank">📅 05:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446557">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎥
لحظه‌شماری دوربین‌ها برای بدرقۀ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/446557" target="_blank">📅 05:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7861e5f68c.mp4?token=viWiPzYFzliL95e04z_Gs2sVNUDQ4ZXTHWO9RCUEjr_jTwW-P9OARwrJlun0X295NqejMkj9ivBY-PsBZIT-UfEaZ8xAImuX15DoJhZ3zYAKFX6LNBQQQrLcljgXZCS1EFTWv78Q42lrn3d6BcJcBD5R1LixLvm5KiR2COGFS5PiMGB13V5yA0AU9neTfMghqR5RjqKby9R9jPROnsupJUdFWXDfF_VcyT2y_Boao2LS2WfwCkue5PipmvKQ0XhsrKesJmUy21sf1G3UVzR4A4-TnSKRSNHy8vrD3hXfK27xCpAW0w9RRNlgFPlK4koMODwiJDeX6UTCWJAfAUX9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7861e5f68c.mp4?token=viWiPzYFzliL95e04z_Gs2sVNUDQ4ZXTHWO9RCUEjr_jTwW-P9OARwrJlun0X295NqejMkj9ivBY-PsBZIT-UfEaZ8xAImuX15DoJhZ3zYAKFX6LNBQQQrLcljgXZCS1EFTWv78Q42lrn3d6BcJcBD5R1LixLvm5KiR2COGFS5PiMGB13V5yA0AU9neTfMghqR5RjqKby9R9jPROnsupJUdFWXDfF_VcyT2y_Boao2LS2WfwCkue5PipmvKQ0XhsrKesJmUy21sf1G3UVzR4A4-TnSKRSNHy8vrD3hXfK27xCpAW0w9RRNlgFPlK4koMODwiJDeX6UTCWJAfAUX9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری پاکستانی‌ها در مصلی امام خمینی(ره)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/446556" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d096f553.mp4?token=ZL-nlG5N6hzkH3_S4346waOw56JDmUGTo5l72O4OVWNBbIUh_t54t53a10WApL0XQhYAfKatj2wKUtabMyV4wEuCFIcQQ9Y0MzDynvCRtXcaY42U2d7MJ_s_KdxJ7G_UvBQHbw3_GWgcClCW21ojRou6kNsg21I2zmpA1uqA9PFaKhGSeyzovm846-vE1KruOC-7htFRUVmPdvioLM3O0HiZLofwIUqMaKvDobnNZatcYlOFtmZwi7weRUrxpa-E8Zw7EgJRJGmGMqSclZSbDjbKuhYg04atSIhkNX6rKW8eytW1M6YUTeYoy1yiJVqpXs3MlgZGBeKpMq1tTb3eRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d096f553.mp4?token=ZL-nlG5N6hzkH3_S4346waOw56JDmUGTo5l72O4OVWNBbIUh_t54t53a10WApL0XQhYAfKatj2wKUtabMyV4wEuCFIcQQ9Y0MzDynvCRtXcaY42U2d7MJ_s_KdxJ7G_UvBQHbw3_GWgcClCW21ojRou6kNsg21I2zmpA1uqA9PFaKhGSeyzovm846-vE1KruOC-7htFRUVmPdvioLM3O0HiZLofwIUqMaKvDobnNZatcYlOFtmZwi7weRUrxpa-E8Zw7EgJRJGmGMqSclZSbDjbKuhYg04atSIhkNX6rKW8eytW1M6YUTeYoy1yiJVqpXs3MlgZGBeKpMq1tTb3eRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات مسیرهای ورود و خروج زائران در مصلی تهران
🔹
درهای شرقی و شمالی مصلی برای ورود هستند.
🔹
خروجی خانم‌ها از در خیابان شهید بهشتی، و آقایان از در خیابان پاکستان می‌باشد.
🔹
اگر خانوادگی به مراسم می‌آیید، بهتر است از ابتدا محل ملاقات با یکدیگر در پایان وداع را هماهنگ کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/446555" target="_blank">📅 05:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92a96e1b7.mp4?token=TYhWjWx7-YiMEZgMAyiaSckxAFyBRle0q6on8SbWQANugHewYIL83_iB2KtSPmjQQiVtVI93OrV3ne72xAvfhmnlca1OEQ72ErRrquXm9Yq0LQiHlGDrAQSdHqFuXtTaHiC9vISTdc11B3hpLKVzODvB5_cY9vsNFVULp0jX5yNCZmMTZ_Nt5bYcyEzPYKwHfVmmwIVMUJ1QmvYpZr-CNKeb9Ty1-ei3cJJ58Y_HSldWXHj5SYVnWRXRzZJPJZUDI8LJNqd1chGotIJ844xhY_7X63h-FpIsiF4gecNqi8SafvC0CvmWDPhEI9vT-uAHUv6T6JLQgu6O5hVflUogWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92a96e1b7.mp4?token=TYhWjWx7-YiMEZgMAyiaSckxAFyBRle0q6on8SbWQANugHewYIL83_iB2KtSPmjQQiVtVI93OrV3ne72xAvfhmnlca1OEQ72ErRrquXm9Yq0LQiHlGDrAQSdHqFuXtTaHiC9vISTdc11B3hpLKVzODvB5_cY9vsNFVULp0jX5yNCZmMTZ_Nt5bYcyEzPYKwHfVmmwIVMUJ1QmvYpZr-CNKeb9Ty1-ei3cJJ58Y_HSldWXHj5SYVnWRXRzZJPJZUDI8LJNqd1chGotIJ844xhY_7X63h-FpIsiF4gecNqi8SafvC0CvmWDPhEI9vT-uAHUv6T6JLQgu6O5hVflUogWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دودمه‌خوانی لرهای غیور قبل از آغاز مراسم وداع
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/446554" target="_blank">📅 05:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446553">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c7e2db8e.mp4?token=nDCVKqIeiJnCN5nMVUkA5Cg1uBjXxDMbdaBqLBXDLU37nd0jd7naWSeJapPBzlSeFogJ8CiWlB5s5tET4dWACADVjmLS4jpxbsvglAci-Qa4i71HNV0tNyRF6odqHAL2U_qnoc--4nVGXJQfDd2ah23tgb9ycz_0x9N4gwBaHWH3vAUIJ5Aq9cdifluMXKUAGWP5rm0sokCChEjLCnO_tnkqQAu_m8qZ5eS9T3msyN22foboo-YCM6Ki70bPAmzGM_9zqR6mIce0qBEJpyhJcHxduLH88S7kpALx9bCyVweomGxSmDryoXnkiCNrYrtZwxo4Ti_Gp_MpBOP3nbWxoyRt7Qq-mzufbixs3X5OkIKjyK00xsll_KCc9q8lOLUHY1DCFmooplKqdNn5Fcm5g7FN2ZQkotI_hPNYvdjUCXj3sUmoeTeU4al5MFWSA-1Ql7Dw-7qCfD0Gg1B8Ys-ohs2cIGfrZ7QLkBPGrqWP4R665dnWhn5cGZPUeeGxLhoEJziJuPq8YsEkY1IJBLunKy2QkafKU-1RIpBl6B8vi55tIblU1AvCFnZWUYcCzsAz4xOfgkPIR5awaNVAktoWz7YumZdyKBLBopv6y-0N3Md7boA3WitX79gYDdzBBwFrFpSYhJbfUQ3iTcvdfqnD3ZAs2W_WMdl5OPwtEniB2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c7e2db8e.mp4?token=nDCVKqIeiJnCN5nMVUkA5Cg1uBjXxDMbdaBqLBXDLU37nd0jd7naWSeJapPBzlSeFogJ8CiWlB5s5tET4dWACADVjmLS4jpxbsvglAci-Qa4i71HNV0tNyRF6odqHAL2U_qnoc--4nVGXJQfDd2ah23tgb9ycz_0x9N4gwBaHWH3vAUIJ5Aq9cdifluMXKUAGWP5rm0sokCChEjLCnO_tnkqQAu_m8qZ5eS9T3msyN22foboo-YCM6Ki70bPAmzGM_9zqR6mIce0qBEJpyhJcHxduLH88S7kpALx9bCyVweomGxSmDryoXnkiCNrYrtZwxo4Ti_Gp_MpBOP3nbWxoyRt7Qq-mzufbixs3X5OkIKjyK00xsll_KCc9q8lOLUHY1DCFmooplKqdNn5Fcm5g7FN2ZQkotI_hPNYvdjUCXj3sUmoeTeU4al5MFWSA-1Ql7Dw-7qCfD0Gg1B8Ys-ohs2cIGfrZ7QLkBPGrqWP4R665dnWhn5cGZPUeeGxLhoEJziJuPq8YsEkY1IJBLunKy2QkafKU-1RIpBl6B8vi55tIblU1AvCFnZWUYcCzsAz4xOfgkPIR5awaNVAktoWz7YumZdyKBLBopv6y-0N3Md7boA3WitX79gYDdzBBwFrFpSYhJbfUQ3iTcvdfqnD3ZAs2W_WMdl5OPwtEniB2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای موکب‌های آقای شهید ایران در ساعات اولیۀ صبح روز اول وداع
🔹
نزدیک به ۱۰۰ موکب، بی‌وقفه خود را آماده کرده‌اند تا با تمام توان، میزبان قدم‌های عاشقانه زائران رهبر شهید باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/446553" target="_blank">📅 05:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446552">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ad1d11e0.mp4?token=Y_ASxYWbxpYxknFSgbZl1_KnEOhfJeEF9AaGgG9cSEwpjdTDVmC3r3W6JTbCFP-XGy3mM098PffJHmVTS5AZZezajNwfuVtVBWH-08dUg89uB7iCaa4DJJYVtpov3DB0NEnWAd6vg3QhP_C0-q6FnthZKI1kszBIQzCV5JSf1sSyz_wm0TJxQySROS5N9fSDVwtIwX_h4QzuDjfmlf3fmpmK3HAGMd_3M2qw3Kokz7KVyAXVRisCl6khU5Nh0XSnTxshHIB5EUa0IkGAzVmbySjwCJ6vuUFdJiVR5GzvGjeeDHCSPzHlmIHnyWbk09aAdc9LRP4KnTab5TuW3NdQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ad1d11e0.mp4?token=Y_ASxYWbxpYxknFSgbZl1_KnEOhfJeEF9AaGgG9cSEwpjdTDVmC3r3W6JTbCFP-XGy3mM098PffJHmVTS5AZZezajNwfuVtVBWH-08dUg89uB7iCaa4DJJYVtpov3DB0NEnWAd6vg3QhP_C0-q6FnthZKI1kszBIQzCV5JSf1sSyz_wm0TJxQySROS5N9fSDVwtIwX_h4QzuDjfmlf3fmpmK3HAGMd_3M2qw3Kokz7KVyAXVRisCl6khU5Nh0XSnTxshHIB5EUa0IkGAzVmbySjwCJ6vuUFdJiVR5GzvGjeeDHCSPzHlmIHnyWbk09aAdc9LRP4KnTab5TuW3NdQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید، ساعتی پیش از آغاز رسمی مراسم، خود را به صحن مصلای تهران رساندند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/446552" target="_blank">📅 05:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g119zrocWqdO5EQkl8-BBA5qeWNW3nx8G2e2Z6Zqcr33ZNJKlXGCJZ0vxVOjzYJxW2QO2zlw7WzqlkqbVVacpuz3t2vPCcxRmNLxwfvE_pFvnETVQQWp4wpt1qG0WVTEDi3Sr7y9RXVMT6hHi5SYkP1Y5z5XU1AWKBA7soNezdXjGxwol-bthJoqxi-aDRMj7Y2lNO5-70xaVI2Bq6ge1vRj3cI-0HlUa6Hupdh-iXprKZS2QfIyFvykyvPlt-5DLfgo4jGgXmK3__wF5BR1V0-UCnqyY9piRk7DDiLXOoUf6kpIqTgRKc4XFlpp81GMay9Lyy-u9Q_wlY80F8Un1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
طلوع آفتاب به افق مصلای تهران
در روز وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/446551" target="_blank">📅 05:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446542">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcdb4cRxyACukdMQ6qSjIrjOnkVDIb8vyh_ZqpnhSd25iGvkjjzt7crQAfCMlV8Xy_M0jZgbMWL9iVXXdhThMw5buYg61r1JVSiDkeOR0kdPuNYq9YhiVC6AMEcv0pIw3Ou8LXROIjNQhN7TPde9RD5QA4CoYWrHUkB6JyPbOM0Qc3RWgnYFZW-0Du8hIqo20ist8KJQqoypxjVUEsl8cWSOD7Np0IYQoOJTtZER0kxknfXD1EQdao8N9UVe6_j_WmxFSBB2-sJHoCBrgb5YHN2sSCvJzTj3Y2hH2fGWlyFxATfVhKFO3L2yox9nhCBs3uFdrX-zoq5_edU8Z5Vy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPSykQP3fsMNVVoUh4zey6K0ma6t-ZClqDYzl3Q-hgmaK4MJNXnSpTTRu54c53JbvNF030ojnZvXZIg3zaZuYw47LtHqg2hZMX0ZPITQt2yTcFL6hP3tQ63GObX7-EeSLpTeyq54Q5Yldr-FoLG8R3A4sBJpqGQmZw-T1WX_PUIMSJIHDADn4Tum98_n3JSz6Y17CJYyc57sr3RpGo-z7HnSIzjinZozh4OKyJZc0LunyeMAnxST2XHJ8RZkR0x3GEEjNJwKA8KQDQdeBALjDaQsx0mmZ512PIYgO9Bg0LponlLIfIyEn358jbifWnLctP45YKSGcyKSS-oPlgWlMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8d0zgs1GkMEJS3EbJqCSqnuTaYTD_a9Qio8AG78xnuHWRdXWg_4-dMf2ctYPoUOHhkMmLuhynZYI9TtiMhweF5dIsbY7MCnBrG5KXMDyafyv7UfrLApyEPdLCtjlgXoITWWez7okrB3s35mNvU6V4_wo6qUITYaO2IoafopBJw-JSIQNSHl28mPlvLK_zFHX4c99NGEnZ4kTXwbAU26IjARzKn_sJyGB5ecSMeZW9kKizJzmrqV-UfnaUycuCpFK7pcDmO6_menBI9j3-18VkIK-iI084n5uLrqcq6J41uy8ymROm3MLRSafn6-fYYPo73t8Qi6KAqVCn_Xk81L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikWVcmQOVJXyZhZY6w3pMcGa9mYTXC8G4zkJc160lfrJYi6NGPF6zFKKddmpUiXAGnYoOvlV-IizJ18-gIYhaBwIlbAPrB6OtaDyoZIyQo-xSgJ_UMr_P0xX0A-AWFBA3qFPbDv7onaj039VCjlIMV_AE0Xmlo57X01ur1Pfa6TYyU5U9bKxziBmb8-cMIk1k4r2oqaTd3ZrXIwCtmTstJGwtFZ5Do64BIVivHpqlwmVTdLKpUY1ZdQPAYuFlEHnGRZeaN6HoENEY-lIvq_RZeWvLKHFicPuNOC8cbr3VAPok9r4HoJCga0fRz3Zi_ski4Qn1L3qjoMwZI7KLKvu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9aRmTAQTIBkaJ-qBxh8er6s1IVCKfdTvBKNASsfdrCEuR7FaCvC72VfKnVXVtDvPQX_S7A8H4eKXEWQ_eTEctH1R1ivyqWU5TE23ORfTowxedBR3nWhWxwUckbGtvcku-mD6Vz3Fx0QTOqQfhvGEzafz9jA6-CDGyXGqB9gWNsGLdmtKan8-6Hww1nhtPijyb_OLYh6XiHTSz0mg9PBfKzrBT4TqFXP2JtU9v0RrQmvboZufm3Lu_w1jo2cmx-TN9XNmhBRwaKSjVEBd5xn0R1szBG6xrQ9500_k5Td0BF_-bK39qPsJHGtysEabNJIORupleuomEghw_HSAQVtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LozmVqe93NCQCDfcABiE65PaHeeSFe7hIDmbGWooroG5QVC9leuTcfkFl7qdKjoV_j8SBVTx2Spwap00kHN2c9ExFKDJ1qR0p4bbz-8Lz77p8q3jRipk3Znai8qdXtx22-qTyjvj8tTN-gmMwUYORMxC8BYQqk7dR2vGPrLyq6BQ5LcHEvKOrL00ARLUNTe18xxgDFRjXMVfYUxBBUijM1i49zpWPLTcycMbvlbKHgKdlR4d3cNNe7ZaBelv0ODAIbuk8KQovHlp_U2IgtF2ed1JRE-rcw_hLVawv9uwhNJrN8eubh35smA61B-dVioq1fGJIvVzkAZEsDmP7WgAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGf73aDiZm9JPYtaa6swNzzNjOdYG6GzG28yS3vqFie4APae2kbETX4Gk07Yj2WGv9hugT75gm71K2K0bbn9MmKLaadOiz-O934Qo23BdWdIk80K0x4iv5nB6BmrvIGRNiZRVROqKdxR-cW8iKiuTrbB7VzSrWrbwbJ6NtfD3JzOzLb9WVziI3DBoNIL8OjKpwe_PlHSoiwq5a4hq8szOWEvIqp33wxQsRnmn3nfsyJWJxzNNpzu1aQq0xFUAIZXh2v9g5TT1z5qUiWZdJdERsoCxj44YZ3m2DjF1gz-q6h7bpPSvOgvEBs30wqyQCSP6QOh4Kn6Kf1vpgWkOCouFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1z7cJpD6ky7fPWWugsSX0TvCvrN_GqRfHPaoUa9eoXgem7vPIleFZoRE0p8mNppQ1LkGWrV6P5cZkIQTUlxhKOTzWD7o8FMXTIq2IBfb7VsUq8mlvTlWJU5DFqAr5tBQRsDegu7PkzUgcgDU4uXdC12Ir9-dbAViY72fBkc8c3uQJjdHN-YsZTSAQXoYP0Jo6xU7-2V924MJwwLlU0oMAomnovGu9g217RnR_TLxwEp3w5xlO2iHbTePJuGsRWvvPb0DHo7S5vRXEj_cUawNFyl82ClZ_JoWaq58Ij7Xjx3jRfSYGM0_-WVFr6O2JY0fzg25D9gv6Kub8XDdkJr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVp83NnyTC2mU8FAsANjkBUsoINd7FzjsmJMSx6UFripdaAYbL2HVWTQhmTYYNpDxAGPnu7EmDXAFPzABIXw29tpL3kI3n5-sOd-ttJXRevNJUSUrzclqF11tXeefu7QlJ0RcWbQiI0QOX_WlO3j0ufNQ_1jOp1oo0SCyXdkq5dd_XIC67SFxqcCNg3XrGIqAsiv_ZAyGFCQWYretbh2DPBbapouVy4znOHK6zLfwoxItizXfXOZhNSnjRyi4DQnNmfbInj00kSXUha6Ofete1rXZWlNvUnhwnIQG8giTwBOO8niHrtnE17gasNGXdekNPf1-5ecWg1oDwe5uGvCag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تهرانی‌ها آمادۀ پذیرایی از میهمانان رهبر شهید هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/446542" target="_blank">📅 05:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446541">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUJTSSxx_vLwZFZskCC8crzVrJY6wOtaI-kM9n9d4AtxHXNX2MuLe_lA6TgYLnzV7ffaJqk4R1i5ISD_MPJM5BDhU4o1qi3xSWTpK48xqreKKal_-E40HEszoiH1mvSPgYV_65kyjQ9hxM1gaTtTYUkBR0Fgb08gHc0_zWeLn-toZQnU2loATpcL5HQaylL8D9XPu5uQJ3u3n--mwm6v-jKsmJC69YWTqg5YQoYbCrgEMiBJ-DzhiKknnQXePAjwBmW7z0KW5_ROTqAGN3yKrndYK5TCqHZS9JmztPKOcKsbzC1ZU4Jl3QEFI9hEi7iTuzvtIQZYdSwzj967nghfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر جدید
KHAMENEI.IR
در آستانۀ مراسم وداع مردم ایران عزیز با پیکر مطهر رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/446541" target="_blank">📅 05:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzCrDo-NB54Py8mR29BlABDUtNDTsZq6Lpy1hXQhOeqjEwCP79KpcKgI4_wwHAK-UfZ15Qo5y5qEZH0HEOtQEjIf6eRrmtK6WH6x-gsCG8DoGefS7PIXW6QCY6P83bV9mO35Ed8zh0Ku8EjV5LdqD_P1u23_e2Q7w2P2kkVrDXK7tZqhsnHU0XdAwjwrmA6-Z3fyMifndn9HC__5YTy2h3lm_aZzkR6U9pXgr6d8AJBI5EBf5GUcb_cBWKcXyMD6KeLCXqoxb3AjUufoLB7M3JJz2x8yYi9zr3MPmctQYYo4vJfxJmujk8CNRGuvYl4UsrUz30f5hgP-iVlIkr21Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط یک جای‌ خالی مانده
📊
نمودار حذفی جام جهانی
@Sportfars</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/446539" target="_blank">📅 04:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fe59c080.mp4?token=vimZi26fSMby7b3giGjkRcrWJopEN-s0PNY3JiLyqVf3UdIERSs3_xf7ikTyNKfR0G_ndScgc0-ZoD42A31WW3LDlODYoyfa2P_VXwAEfSFOOF9AJokgZJnUP0pDYU0UADs3jizWcs5cFSlRwsz_927YWxLK_3QVkK1X734VSrwxlnuWfi-izWMagVjfzc582RDtGtg7ZBRJGbz5bLSzBeflMzOYK87nqLs_aIP39qMUrDl5S1duJOpHN0kZ8y_nvEKrVXUb0R8a7D4X4JmPT7onymm8Q_31nzImV2eb-2gFbG7814b7fumWMwSCubBTlCy0pbQ93Ez-rtXddlZ9GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fe59c080.mp4?token=vimZi26fSMby7b3giGjkRcrWJopEN-s0PNY3JiLyqVf3UdIERSs3_xf7ikTyNKfR0G_ndScgc0-ZoD42A31WW3LDlODYoyfa2P_VXwAEfSFOOF9AJokgZJnUP0pDYU0UADs3jizWcs5cFSlRwsz_927YWxLK_3QVkK1X734VSrwxlnuWfi-izWMagVjfzc582RDtGtg7ZBRJGbz5bLSzBeflMzOYK87nqLs_aIP39qMUrDl5S1duJOpHN0kZ8y_nvEKrVXUb0R8a7D4X4JmPT7onymm8Q_31nzImV2eb-2gFbG7814b7fumWMwSCubBTlCy0pbQ93Ez-rtXddlZ9GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یا ایهالمجتبی، تسلیت
🔹
فریاد مرگ‌بر آمریکا و مرگ‌بر اسرائیل در مصلی تهران طنین‌انداز شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/446538" target="_blank">📅 04:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d94ea47e.mp4?token=Cy3vGvFwOel71bs0Lu6yQSnGz-tErV1uej_GXqgA6RIUV6zjmGPl3grt9qCZcePDtYRF4LBxgJCW4eLCDXCbN3AjQ9ribtvCkC0o62tYEzQt2syjuYRVwTUX31x-Umw8-Ue261ALzNI7jNnUXp9kajesjQiOU5q--tot4YY8DjTiFV2ubjIWwXALgq_7AAWZkTD59XTQBC2hMIzy1-t6vK1i63goyX_2xmg6s2YEf5MTpkSSPH2S2LeH-7g8vltwAaSZYG6kR9v_zW2vQP7aGOqc68wkYH41EDPVJ1d_gXMSoUkakeNwWRZ9T9nIphNF3XmxZ74yOBEqN_tCtECa2zCy0e2MZMpaKIu9GbImsR78QUF5vJjQpyt-OTdNZ34l6U2cX84QyQoC7ddghiQOL4zqEu4IBpuk16dKwZhAPkOw-cM3l4IStXZ3mMVMc-x6bS5BMznM2E9Dt953rwQm1kW9ZpSCOAU7aO5ZUNzCbUJMVMj6wArTqqeRISESdbOLhKjNLinXY9qtLVq_wghm20bv06G-T2jiJnAprYsRbJMJmCA7zDqH2MmckPqz53tJD8XNBJo5MwfCnX1a7Q72r0IrymbEc7_kwnTHWoK6rQfdwYAKcVn8zmtN4Tat5-A3g8Gu38jrq5EwsxldaZL3IK4QqytJ4cZpMu7k7m263uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d94ea47e.mp4?token=Cy3vGvFwOel71bs0Lu6yQSnGz-tErV1uej_GXqgA6RIUV6zjmGPl3grt9qCZcePDtYRF4LBxgJCW4eLCDXCbN3AjQ9ribtvCkC0o62tYEzQt2syjuYRVwTUX31x-Umw8-Ue261ALzNI7jNnUXp9kajesjQiOU5q--tot4YY8DjTiFV2ubjIWwXALgq_7AAWZkTD59XTQBC2hMIzy1-t6vK1i63goyX_2xmg6s2YEf5MTpkSSPH2S2LeH-7g8vltwAaSZYG6kR9v_zW2vQP7aGOqc68wkYH41EDPVJ1d_gXMSoUkakeNwWRZ9T9nIphNF3XmxZ74yOBEqN_tCtECa2zCy0e2MZMpaKIu9GbImsR78QUF5vJjQpyt-OTdNZ34l6U2cX84QyQoC7ddghiQOL4zqEu4IBpuk16dKwZhAPkOw-cM3l4IStXZ3mMVMc-x6bS5BMznM2E9Dt953rwQm1kW9ZpSCOAU7aO5ZUNzCbUJMVMj6wArTqqeRISESdbOLhKjNLinXY9qtLVq_wghm20bv06G-T2jiJnAprYsRbJMJmCA7zDqH2MmckPqz53tJD8XNBJo5MwfCnX1a7Q72r0IrymbEc7_kwnTHWoK6rQfdwYAKcVn8zmtN4Tat5-A3g8Gu38jrq5EwsxldaZL3IK4QqytJ4cZpMu7k7m263uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود زائران به مصلای تهران
🔹
دل‌ها‌ بی‌تاب و چشم‌ها گریان از فراق رهبر شهیدی که تا ساعاتی دیگر به جایگاه آخرین وداع در سحرگاه شنبه می‌آیند.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/446537" target="_blank">📅 04:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8c363281.mp4?token=HywHtQOBQdGFlS640Ve4LO7HnJBfnHSbaX10LmcT_ZT_4qNWX1U23laOxZ9upJqwa3NeR7UwPJQx9NeOc6vzmrsWmdb_pke7ogPhG54zkqOX3MYQaG90Te9TUvkZjRJJtNhxWbVi3s5ETu8b5wMDa-AASxscxK5kJa27BGvVu1GQnUg58qO1KKRgX4RhrGPm6Dc-csDtxcf2jMytYHADrDuaWx7EUO8bbxwosRnkzrCtIt77eW_a7LIbNTs2R5KzIAIpvKuU6gvSW4d39pZuDyvZkZPq3a3LwXfAB9tqZLe06jn0jeu7clVN0VrRMtr_40rDXwOrQ05GEkWPP0osBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8c363281.mp4?token=HywHtQOBQdGFlS640Ve4LO7HnJBfnHSbaX10LmcT_ZT_4qNWX1U23laOxZ9upJqwa3NeR7UwPJQx9NeOc6vzmrsWmdb_pke7ogPhG54zkqOX3MYQaG90Te9TUvkZjRJJtNhxWbVi3s5ETu8b5wMDa-AASxscxK5kJa27BGvVu1GQnUg58qO1KKRgX4RhrGPm6Dc-csDtxcf2jMytYHADrDuaWx7EUO8bbxwosRnkzrCtIt77eW_a7LIbNTs2R5KzIAIpvKuU6gvSW4d39pZuDyvZkZPq3a3LwXfAB9tqZLe06jn0jeu7clVN0VrRMtr_40rDXwOrQ05GEkWPP0osBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنج و دمام‌زنی زائران در مراسم وداع با پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/446536" target="_blank">📅 04:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b870b3546.mp4?token=skprluC82P2OzfjYrwqEaJq12T9hiPCTmZKfByUga-kkVyKNwTj9nYUp2nvDcfDkSMK_vd7Bpf8G4aVqv4nGrvbQEfiVBTCZS2UzoQWtvdLzQcxIw9Q1DuqWnNhY3Sjbc30AytyBqbkHC98Wu6JHkZ38RGqhivr0w7_8UR3gcT5hTipjKZfJsmuokK1CC0iauxz4VvNsmpkkk2z8BF5QsCto4oO_F_WoI3fxUCZRgYAkv9jDMWieA1tKSupX2_PZ-Xcmx0fwLPufjqZAETLfU7qEfKGWhNk27dlJMVARjpoKaA-3ocSmGDVcLE3rLhBFUTZ2AmwU1mQQ8ekUFZ7Snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b870b3546.mp4?token=skprluC82P2OzfjYrwqEaJq12T9hiPCTmZKfByUga-kkVyKNwTj9nYUp2nvDcfDkSMK_vd7Bpf8G4aVqv4nGrvbQEfiVBTCZS2UzoQWtvdLzQcxIw9Q1DuqWnNhY3Sjbc30AytyBqbkHC98Wu6JHkZ38RGqhivr0w7_8UR3gcT5hTipjKZfJsmuokK1CC0iauxz4VvNsmpkkk2z8BF5QsCto4oO_F_WoI3fxUCZRgYAkv9jDMWieA1tKSupX2_PZ-Xcmx0fwLPufjqZAETLfU7qEfKGWhNk27dlJMVARjpoKaA-3ocSmGDVcLE3rLhBFUTZ2AmwU1mQQ8ekUFZ7Snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلی با ورود خیل عاشقان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/446535" target="_blank">📅 04:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/446534" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای دعای عهد در مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/446533" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/446532" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای اولین‌بار و آخرین‌بار آمدیم دیدار؛ آمدیم تا حسرت دیدار به دلمان نماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/446531" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت عاشورای آخرین دیدار با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/446530" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای سحرگاهی مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/446529" target="_blank">📅 03:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/446527" target="_blank">📅 03:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/446526" target="_blank">📅 03:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Pw5Ea_aAlu8pzJrLcqYWo4Tl9eiHIb2_HScoX2Zlkq_PiYg2hObktwWi_fSyrlmH_G0pQrui5HXoxXuXej1ABj7p_OF6tVJ7NejOGVichZe6mERRISi4SCk2wxc7UQx4-zpVpq-LuoPLD2YENXf1WCw80o5bJpYRbuZg-vkGxzVsBdqZT2MwyZdfkP7aucvgMFdiVJr4JpO-JcCc6Ee1arupepVDcmlPDDeFLr-QtN_b00fHLmktfaI-wVMbU1Iegd-HNJvOjvlYZtV-usFBWsaNX2lwjvTf9Ts9QaykRBJVqNwoSj4jpRXp9pAz3fofPLhVuSg4FOsXWXq1Rz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آماده‌سازی محل قرارگرفتن پیکر آقای شهید در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/446525" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی نریمان پناهی در حیاط مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/446524" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاهی که اشک همه را در میاورد...
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/446523" target="_blank">📅 03:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/446522" target="_blank">📅 03:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین ساعات انتظار این شکلی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/446521" target="_blank">📅 03:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446519">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
«عشق دل‌افروز» پرواز همای، برای رهبر شهید
🔹
نماهنگ «عشق دل‌افروز» ساعاتی مانده به آغاز برگزاری مراسم وداع با رهبر شهید ایران، با صدای پرواز همای و شعری از قائد شهید امت منتشر شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446519" target="_blank">📅 03:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446518">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اندک اندک جمع مستان می‌رسد...
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/446518" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌انتظاری مردم پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/446517" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی عبدالرضا هلالی درکنار پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/446516" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌تاب آخرین دیدار
◾️
بغض و حسرت مردم در مصلای تهران، ساعاتی پیش از آغاز آیین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/446515" target="_blank">📅 02:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446514">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
۱۴۰۰ خودرو‌ی آتش‌نشانی در خدمت زوار امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/446514" target="_blank">📅 02:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446513">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ادامۀ حملات اسرائیل به غزه
🔹
منابع خبری از حملات هوایی و توپخانه‌ای ارتش رژیم صهیونیستی به مناطقی در شرق و جنوب غزه خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/446513" target="_blank">📅 02:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
الا ای بزرگان، بزرگ جهان رفت
◾️
سران را بگو، سرور سروران رفت
🎥
قابی از پیکر مطهر رهبر شهید انقلاب در مصلای تهران، در مراسم ادای احترام نمایندگان کشورهای خارجی
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/446512" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSQR7L7B5jjrHxYDdhxzqONWMZoVLBiCzO6wy0e5EZ3DyXGioFvCoNJRhAgLVi_TG_wRdsYH59bC1SJMqLIC5mjGcnDWE2c2t44BKBfGIda28Nb3WrWqU1DklUonr5POW8h5gwuA9YHkzhSneIsA_ON8K6LvitP0gzyC3SnIaljyhveg2uqIX21HcBLqTz_Wzz9u8JcOgob14x6L63U3NN58aSVVcQhhPGJIHxH8VPJdsBU_MHf2DVT_RgKbqRzmj9v5tfjNRNsQJbptio0DPauLPTq_FqYf-TU-TC4_NnYStkhcLjgqOPBGaYt2kcDmunWdwfBQ7RiYiKH6PSSgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB-EzK5qGSI4hRDCnu4XO8NuFd7tExuQ7sy7wbx489pOMGYWZGilHr6TAPSAxKtFn0Zn8Gw5osoE59JZMkMR779bwJEBkuaawOjrAn3NXVibggbyOx7-XXFDyS3lbCh3u-HUAwf_xl8FyHyuKJF7C-iZ055t-bsRTpgabLhn8QxB2khDWgORYm6veLue1Uk8GnBKyaWO4a_UqWpnbAqdY6OzSuwBHb1URC3hufxSpiC-OHCZ_hb1k5sDSuIfLY6Nr9MU21unwt4U3357M8xhL8FVD9hjkAZNF-QsTqQSJQ4HlU5VYRPWkXsAOpvjc1YguX-ralHnUedtCSWjdg3Q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuYzbTXNTxZulWSR7ElPpE_tA1bubyjDrn1a9CAFAhd_YD4uY9Q63FgiUV7AhH1rsPczx_22I76ODJSyyZ2XW6nkwU8w8bQV43LZdpEo8pktnBxwDcaSG70_IGYw829jAcnjWnY1p_Po_bFBlpGHFTG3N4dWCsy30ZFqHvYWgx0aI95d8lBj5N9co7oRJKaEiqFHmBDNeMIDrParuOKsoC5lNxQZTfZ0PO3ux_KEKL9m5ay4zpaoznXYSOkjlhSKC2bLxnF0m556-1UVDpxi-50SHlL_cdYobv5j60h12XK_hlOn7oBP_WpZndzC0v2ti05BufVDXykIyiX2njx0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زاگرس‌نشینان با سیاه‌چادر به بدرقۀ رهبر شهید آمدند
🔹
هنوز سیاه‌چادر برافراشته نشده، اما چکش‌ها بی‌وقفه بر میخ‌ها فرود می‌آیند و مردانی از دامنه‌های زاگرس، در گرمای تهران، مشغول ساختن سقفی هستند که قرار است مأمن عزاداران مراسم تشییع رهبر شهید باشد.
🔹
از بچه‌های مسجد و بسیج تا کسانی که روزگاری اینترنشنال‌بین بودند، امروز در یک صف ایستاده‌اند تا به گفته خودشان، وحدت و ولایت‌مداری مردم بختیاری و زاگرس‌نشین را به نمایش بگذارند.
🔗
روایت شنیدنی بختیاری‌ها و حضورشان در تهران برای بدرقۀ رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/446509" target="_blank">📅 02:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
سردار معروفی: دشمن نمی‌تواند محاسبه ملت ایران را تغییر دهد
🔹
معاون فرهنگی سپاه: ملت ایران با حضور در آیین‌های وداع، نماز و تشییع، هوشمندانه پای ولایت و ایران اسلامی خواهد ایستاد و به دنیا استمرار انقلاب اسلامی، استمرار ولایت، بیعت با ولایت و یکپارچگی ایران اسلامی را نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/446508" target="_blank">📅 02:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت  @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/446507" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی در دقیقۀ ۲۹ دروازۀ حریف را باز کرد
⚽️
آرژانتین ۱ - ۰ کیپ‌ورد
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/446505" target="_blank">📅 02:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات محدودیت‌های ترافیکی در محدودۀ مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/446504" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم منتظر در خیابان، از بدرقۀ آقا می‌گویند؛ نمی‌توانم با آقا خداحافظی کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/446503" target="_blank">📅 01:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای نزدیک از جایگاه پیکر رهبر شهید در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/446502" target="_blank">📅 01:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میهمانان خارجی حاضر در مراسم وداع، از رهبر شهید می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/446501" target="_blank">📅 01:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG4mAErDJNmpnPDtY_xOVIVVRjZk2HtgHuKucJoRnG1vafDmB61Wh1794iY9pgF12Pu60Cj2WQjoAuT4Z6z75F1QsCP39RDpCuM0-hwhw8Y8rHr_GDiJildPCBRUhcHQ-RjeDkaH-y0GoL28okqvtOnMllwNeXrwEMllN8XbAJJuVgts5vP5acXACsLtNCex9398P7HjaNVaUYJKCJP5h8aB2j41F-9Z3_KkdztYTBt0UvcYfeg_nOlqzklqRmQP3L5AkFG4nHMGWQP6r8PMj2jQgCu7o2An48_rDBP0JAHk1XsBAO9gmAiWlgtVDgIvv-TTLByetZo7A963TgTZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخت‌ترین شب زندگی حسین طاهری
🔹
«سخت‌تر از امشب توی زندگیم ندیدم!» همین جمله‌اش کافی بود تا بغض‌ چنبره زده بیخ گلویِ بیشتر آدم‌هایی که ساعت‌ها روی پا ایستاده بودند، دیگر طاقت نیاورد و بشکند.
🔹
«امشب وقتی وارد بیت شدم یک پرچم بزرگ دیدم که نوشته بود اتحاد مقدس؛ کلمه‌ای که آقای ما برای آن خیلی زحمت کشیدند و بعد از شهادت آقا، ما باید حواسمان به این اتحاد مقدس باشد. آقای ما فرمودند به مسئولان جمهوری اسلامی اعتماد کنید. اما از آنها مطالبهٔ مؤدبانه کنید که خطای محاسباتی برای آنها اتفاق نیفتد.»
🔗
صحبت های حسین طاهری از حال‌وهوای اولین شب وداع با رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/446500" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/446499" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446498">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه‌چیز دربارۀ مراسم و محل وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/446498" target="_blank">📅 01:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446497">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنج و دمام‌زنی زائران وداع با آقای شهید ایران، در خیابان‌های اطراف مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/446497" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446496">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌  یک استان دیگر عراق هم برای تشییع رهبر انقلاب تعطیل شد
🔹
استاندار استان واسط عراق نیز برای حضور عزادارن در تشییع رهبر شهید انقلاب، چهارشنبه آینده را تعطیل اعلام کرد.
🔸
کوت و العزیزیه مهم‌ترین شهرهای استان واسط در نزدیکی نجف اشرف قرار دارند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446496" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446495">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiamunR03TZJ1Tb9L2dpYRccFhibuLrYHVFAfkM_8pkyeO7YCgJby2XPqZdikJmLKcBf77KKQ2vsm-oUXRi4sSdcSVo3PHTAucfzb_LRdc-jhsYOQuRof0GMUe887wpazJnl0tpPtyw0-mZWBTm4sN0M2FtzSZOhPe8WqvOGNJRFWFqFs5W_JlN1_584_BnOdIn1Spa1h4G6RMskOMmyjgLQ94Dl1zh_N710Xkb7WwfwEU8bxzEdi95njWM2Jy6QHoB4kfvUqH3onykGTaHxYcCSq1m8azegmq87r9VdMh5wFgWu2ptDtuTvuyFGrUtfuCo69p_w9of13Ys7oXbbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجباء عراق: ارزش شرکت در مراسم تشییع رهبر شهید، کمتر از مبارزه با صهیونیست‌ها نیست
🔹
دبیرکل نجباء: میلیون‌ها شرکت‌کننده، خاری در چشم دشمن ظالم خواهد بود و فریاد مرگ‌بر آمریکا و مرگ‌بر اسرائیل تیرهایی هستند که توطئه‌ها، دروغ‌ها و جنایات آن‌ها را نشانه می‌گیرند؛ پس کوتاهی نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446495" target="_blank">📅 01:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446494">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMVavkjyoTSiEhNdudPPuU9JknkuX3i4tVX_jK4eTtKcZvZPGqBc6RQdt6rWmhY95FVIckVMWp82rPztjtgNhcaGF5p6wf54twidmbrAiv7ZGjfr3zv6XGZelPvAnNHb9l6akbWU9gSpNutR_bpNJo_NUFaRC1ROibrbOG0-QfLDUmq7mdRisRY-V9cLW-dGDcgLbZRqa8A8VXWi4CczebrNmzEDuNLRK8uoTT6fHBcZRx2tjam9eK2wVM4Ey9jOEXF6ahkTVcmNk73-cFKdnQrToa4eCgl3vLqAsfns13rRMOdqORFuVRlxPMMN6EOzzreag_zBGI9pHUeyug9MsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی مصر: این برد را به مردم مصر و فلسطین تقدیم می‌کنم
.
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446494" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446493">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lopExvGw7Wzii-Sk0ipaAeXh2ZzO1dnpXi33U7AKWMHk_2yIttBe42KgCNxYHd5F0pYvhxhSBzKa3HZzmAyaVSo7HrkhRvBI_6L9xGZ268auklPtYGhlM1AXx1YXW50GIGJy_A39lUEFFFuryZ8sumA8dsQVP7EFvNqvN4e-b4eAFrLb4zLygcDykztBXk04v-jp-3a70p3-HLW46708B1NA5eJ1OvLQKdolb_XV9xkcub3pJynVvKvF2ELDPc2MTsP-r0CPwYtNcfJqA-N3tM5sHylCpwTKof04y0yLFQITIpQu2nHOMz-nG--hDrfzAjHLckIVICLC0XV9abdUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ مسدودی خیابان‌های منتهی به مصلای تهران   @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446493" target="_blank">📅 00:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn7FOv1klRj7fSfBfC5ReYLQpQnlJab2MB5qOcfrVxNInXgLSKqJu-j7cwkWQRss7i7EQ5-pQhZisTMxvFp8dBcgd0tYRaRRmOrifGfCiG_9WWM45BsQjTzGh00XfqNg1NlpxBklKIdCQ_Pf7hnNqx1EVQWUrLkRQAsxOGcjj3G-MtQ8aX1AvpA5KlEvLXmVDyK-2Ai5WI7V45o3JmyG8u7M7VZHkV-6O6E6VRjkdC8OB0L1Rck6BY69tFFwJTgMEsMAOG4fc92E-D5lilq1SCP-8kO2PXP79KYH05ieBtwyACBmy_m910q7HjTxRcSPw2cyQeD-Yoa2imiLWhS_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وداعی به وسعت کل عراق
🔹
طرح حشدالشعبی جهت فراخوان مردم عراق برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446492" target="_blank">📅 00:55 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
