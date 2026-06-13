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
<img src="https://cdn4.telesco.pe/file/BxOi_Y9fXowRbKTNVNM4D4TSn25-XWr7OX70x8Rm7QCd1d2EcvjcdhJJZglA3AdsLrS8Hz_PPQziL4tx0T5Ze7Ge7It9ow6qiR82B0GCI-7JihvOALkhN0qm8n6thlrImvnK8o72aUznhVM_sSDCDoKbLoO-HyakctJwk9lWv0_KYef2H-JrtipZmombXuUE_chlg_oIWiq-aEQ2lBRDTF6LGh2-HB2gmugoqO9NdrrmFaCKx3Wuu49_7WLbcL6LGDprrcknkh-f2pXcW9ft5qdLpO6ViDKHDTcEVYnQMxAVed1zyQzXe5bLPXtaE0c-zVqLkTstk--f_DnhzfqfWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-441817">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa3186d71.mp4?token=X9frTFpUxO_aqHJ4mbChNv83QzSQJz2LFf8y9QEDbncEEzbfds0nbb2CXZe3rQT5yXhBn4tE6gldZJqYKFwZm3XftDw_AOQQWDdHBA7Pa8-_-SCMRXML7srTo1JtEfU1YD6dQnjK0kekZ6RcaHlB2PIlDZq1Sjw9GX6noWX2WvIpc7chVp5NGbVxNWRKOk7Ika1v_57MFiSXDF75gabuIwhqE1Z7FxRxjq8BMTMeQvLgqQ5boPVA8JI9HmH1iUrFuMFOgZ_O2cOudALFt-kSDgXYUpsbrWtHXCo9gw-EeiuBdOHYOx1kMtC_Choc4tUZu0k_3pPzpEodQP6HhivCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa3186d71.mp4?token=X9frTFpUxO_aqHJ4mbChNv83QzSQJz2LFf8y9QEDbncEEzbfds0nbb2CXZe3rQT5yXhBn4tE6gldZJqYKFwZm3XftDw_AOQQWDdHBA7Pa8-_-SCMRXML7srTo1JtEfU1YD6dQnjK0kekZ6RcaHlB2PIlDZq1Sjw9GX6noWX2WvIpc7chVp5NGbVxNWRKOk7Ika1v_57MFiSXDF75gabuIwhqE1Z7FxRxjq8BMTMeQvLgqQ5boPVA8JI9HmH1iUrFuMFOgZ_O2cOudALFt-kSDgXYUpsbrWtHXCo9gw-EeiuBdOHYOx1kMtC_Choc4tUZu0k_3pPzpEodQP6HhivCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲ ماه از این ۱۲ روز گذشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/441817" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441816">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام فرمانده قرارگاه خاتم‌ به مناسبت نخستین سالگرد شهادت سپهبد پاسدار علی شادمانی و شهدای اقتدار ایران اسلامی
بسم الله الرحمن الرحیم.
🔹
۲۳ خرداد، یادآور آغاز دفاع مقدس ملت ایران در برابر جنگ، تجاوز و جنایت تروریستی ۱۲روزه صهیونی آمریکایی و نماد ایستادگی ملتی است که بار دیگر نشان داد امنیت، استقلال و عزت خود را با هیچ قدرتی معامله نخواهد کرد.
🔹
در نخستین سالگرد این حماسه ماندگار، یاد و خاطره شهدای والامقام اقتدار ایران اسلامی، به‌ویژه «سپهبد پاسدار شهید علی شادمانی، فرمانده شهید قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص)»، را گرامی می‌داریم؛ فرماندهی مؤمن، بصیر، مجاهد و راهبرداندیش که عمر خویش را در مسیر دفاع از اسلام، انقلاب و میهن اسلامی سپری کرد.
🔹
شهید شادمانی از فرماندهان برجسته مکتب دفاع مقدس بود که از مسئولیت‌های میدانی در فرماندهی لشکرهای ۳۲ انصارالحسین(ع)، ۳ نیروی مخصوص حمزه سیدالشهدا(ع) و ۴ بعثت تا فرماندهی قرارگاه نجف اشرف، دانشکده علوم و فنون پیاده و در نهایت نقش آفرینی راهبردی در قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص)، همواره منشأ اثر، ابتکار و اقتدار بود.
🔹
ویژگی ممتاز شهید شادمانی، پیوند کم‌نظیر میان ایمان، اخلاق، تجربه میدانی و تفکر راهبردی بود. اخلاص، صداقت، شجاعت، ولایت مداری، انقلابی‌گری، مردم‌داری و روحیه تعامل و هدایتگری، او را به الگویی ماندگار برای نسل‌های آینده نیروهای مسلح و بلکه جوانان غیور و مدافعان دلاور وطن تبدیل کرد.
🔹
امروز، در فضای ناشی از جنگ تحمیلی سوم امریکایی صهیونی موسوم به «جنگ رمضان» که ملت مبعوث و برانگیخته‌شدۀ ایران اسلامی، خلق یک رستاخیز معجزه‌گون در حمایت از نیروهای مسلح بیعت با ولایت و خونخواهی قائد شهید امت آیت‌الله العظمی امام شهید سیدعلی خامنه‌ای (اعلی الله مقامه الشریف ) را رقم زده است پیام خون شهیدان اقتدار برای ملت ایران و دشمنان این مرز و بوم روشن و آشکار است؛ جمهوری اسلامی ایران با اتکاء به ایمان الهی، سرمایه انسانی مؤمن، توان دفاعی بومی و وحدت ملی، تحت زعامت قام معظم رهبری و فرماندهی کل قوا حضرت آیت الله سید مجتبی حسینی خامنه‌ای (مد ظله العالی ) مسیر عزت، امنیت، اقتدار و پیشرفت خود را مصمم و باشکوه‌تر از گذشته ادامه خواهد داد.
🔹
اینجانب ضمن گرامیداشت یاد و نام «سپهبد پاسدار شهید علی شادمانی» و دیگر اقتدار ایران اسلامی به ویژه فرماندهان عالی نیروهای مسلح، بر تداوم راه پرافتخار آنان در صیانت از امنیت ملی، تقویت بازدارندگی و پاسداری از آرمان‌های انقلاب اسلامی تأکید نموده و از خداوند متعال علو درجات آن شهیدان والامقام را مسئلت دارم.
@Farsna</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/441816" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441815">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e089dd3f60.mp4?token=pTxdkusclLt-xH7QKH8kW8godkOcBzUdNzxOvSTdC_kihidifMqa7cCqTuoP5w4c3jdCZL0nqPs8lhmQ1DZSSMFdRpA3jjM2EwZsAAVfIDl7bZ6_4PLp5Ft-hWPod8ALC1iuCmaQf3_dpXJGOx-Mzj3Z8dh2a1Ix0s-vexUwxr1QhwNyCJFf7tSRuFmEPCXYAmC658s05BOcGk_1MR0aLmBYfS1byaiGmOEUIRtXptBLrGmkyBeyFZoL0DFLQpTvCqySNHOg3JymUHXzXqWKMLZSq9OO05CKRjLSbvzC2DXeJP0m7rEIGEtZhUjniuJstW_nEKiLPqqJQ10dMls3Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e089dd3f60.mp4?token=pTxdkusclLt-xH7QKH8kW8godkOcBzUdNzxOvSTdC_kihidifMqa7cCqTuoP5w4c3jdCZL0nqPs8lhmQ1DZSSMFdRpA3jjM2EwZsAAVfIDl7bZ6_4PLp5Ft-hWPod8ALC1iuCmaQf3_dpXJGOx-Mzj3Z8dh2a1Ix0s-vexUwxr1QhwNyCJFf7tSRuFmEPCXYAmC658s05BOcGk_1MR0aLmBYfS1byaiGmOEUIRtXptBLrGmkyBeyFZoL0DFLQpTvCqySNHOg3JymUHXzXqWKMLZSq9OO05CKRjLSbvzC2DXeJP0m7rEIGEtZhUjniuJstW_nEKiLPqqJQ10dMls3Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه با جانبازان کوچک جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/441815" target="_blank">📅 17:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441814">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqAtxfv95dpr4JrA9_8_8tWEtP_uoZIS1sYLgCqiUC7V12yxq4xrj14JU5xQmdABRcFMGKsKkJxRbZEvgJHOwG3f9PDUxJTBD8R6h9pwJh-N9XrrU8BOff0tsgPAoL-b4JjAdnRncjtROAzFszkRpELdKWx-QZyM-bzrPscw7F5_ZfWaToVCkswJvua2q0jMy_DwJCdmuRpsuCmQdTcgB1DkJM_Uy3tXUx9VW1nKZgQCzZi1jTjy-3q66RTc_x1GpoJ2BNZE6BywofNj7avRvB6TYjc40E-n7AkDNTMAp1Y8t3qA47l_RoKnSg5oLWvDchy-jnqgyI1nXCsAI4Ep0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار وزارت بهداشت: مکمل‌ها و ویتامین‌ها را خودسرانه مصرف نکنید
🔹
دفتر بهبود تغذیۀ وزارت بهداشت: مصرف روزانه و خودسرانۀ مکمل‌ها و ویتامین‌ها نه‌تنها ضروری نیست، بلکه در برخی موارد می‌تواند به سلامت آسیب بزند.
🔹
مکمل‌ها جایگزین غذا نیستند و فقط در شرایط خاص مانند بارداری، شیردهی، سالمندی، دوران رشد یا برخی بیماری‌ها و با نظر متخصص باید مصرف شوند.
🔹
مکمل‌هایی مانند ویتامین D، کلسیم، امگا ۳، آهن، روی و حتی مکمل‌های ورزشی نظیر کراتین و گلوتامین، تنها در صورت نیاز واقعی و با تجویز متخصص توصیه می‌شوند.
🔹
بهترین راه تأمین نیازهای بدن، داشتن رژیم غذایی متنوع و متعادل است و مصرف بی‌رویۀ مکمل‌ها می‌تواند عوارض جدی و گاه جبران‌ناپذیر به همراه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/441814" target="_blank">📅 17:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441811">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985b9f9324.mov?token=J2VcKZ6wmL1c7JoEiGGw0wbdUGYKu5CEyWkgJLlH0axVqUxKQjGfQ8XiTJcdHE2Bc37_0j7QX66JccGyejV4NHd1wWQdjF14fLnSdsSTyYAu3bkZNULrCQshB7rjcdwHwCDS7HnNcNdD_ax7YUjSqNPf24u_WpJZKWFeHZ1uerQTcD-94l4_8Z3dLEcnylV1-s0tTblPx8ww2a1ktsuoJpKrtvnHsuWqURJ9eJs633JWy_37ZTlj2GxXLGk9vwWr3NIX0hLet3JVJMH4Q50t75PZIcqLsjrhJPiGmHHfQZ-xRzRGbOWeu5JfS2a0T4uRZZwy8gski3GXt5aA9oK1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985b9f9324.mov?token=J2VcKZ6wmL1c7JoEiGGw0wbdUGYKu5CEyWkgJLlH0axVqUxKQjGfQ8XiTJcdHE2Bc37_0j7QX66JccGyejV4NHd1wWQdjF14fLnSdsSTyYAu3bkZNULrCQshB7rjcdwHwCDS7HnNcNdD_ax7YUjSqNPf24u_WpJZKWFeHZ1uerQTcD-94l4_8Z3dLEcnylV1-s0tTblPx8ww2a1ktsuoJpKrtvnHsuWqURJ9eJs633JWy_37ZTlj2GxXLGk9vwWr3NIX0hLet3JVJMH4Q50t75PZIcqLsjrhJPiGmHHfQZ-xRzRGbOWeu5JfS2a0T4uRZZwy8gski3GXt5aA9oK1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهروند برزیلی که اینتترنشنال را سر کار گذاشت!
❌
«دود ناشی از انفجار در شاهین‌شهر» عنوان فیلمی بود که اینترنشنال از درگیری‌های چند روز پیش منتشر کرد.
✅
اما مدتی بعد کاربری که این فیلم را برای اینترنشنال فرستاده بود، نسخه اصلی آن را  به خبرگزاری فارس ارسال کرد.
✅
این فرد ساکن برزیل، بعد از دیدن اتفاقی رد دودی در آسمان که به محل یک آتش‌سوزی ختم شده، تصمیم می‌گیرد فیلمی ضبط کند و آن را اصابت موشک و انفجار در شاهین‌شهر اصفهان معرفی کند.
⚠️
چند ماهی است که شبکه اسرائیلی اینترنشنال با کمبود سوژه مواجه شده است و برای اثرگذاری بر جامعه مخاطبانش هر خبر و مطلب غیرمستندی را به خورد آنها می‌دهد.
🔎
این نخستین باری نیست که اینترنشنال بی‌پروا بر سر اعتبار رسانه‌ایش قمار می‌کند. پیش از این نیز وقتی از سوی مردم ایران بایکوت شد برای بازیابی اعتبار از دست رفته‌اش اقدام به استفاده از هوش مصنوعی صوتی برای بازخوانی پیام‌های مخاطبانش موسوم به «روایت شما» کرده است.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/441811" target="_blank">📅 17:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441810">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
سیاه‌پوشی حرم حضرت معصومه(س) در آستانهٔ ماه محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/441810" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441809">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLVVt-eabM3gfxO8KDiQC8yvemIb3KysrBJtRujo6g5bRO0jM4bsQIDVLJuTBt-wYnCbNpbReo7Jkgc031UdcpQXjoh-EDyOSW5pIWDzeH5QDOj5_hNTb2oSRV50k5Z_gR6JIJbvUUVe8-liQME9lpJw-yHdm9nUizzpC36lCTCfYU1kfS0b_PYyZEPXdLsH7JAXgYqU1_HPoFUKMegrfdZT7yJu1gVFoyCrljZmzb4qJgje5b-NVbHzWycUf87B-CcMf0t3IUcpAJAgykS25JKzGiqohTFkho1RJarVFM7rJGJBBs0IAOIm9MZX9jvdPW7zvr-L69qUn581fU5iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب بوشهر ‌سه‌شنبه قطع می‌شود
🔹
آبفای بوشهر: به‌دلیل بهسازی خطوط اصلی انتقال آب و همچنین انجام تعمیرات اضطراری در بخش برق تأسیسات آب‌شیرین‌کن، قطع یا افت فشار آب در روز ۲۶ خرداد و به‌مدت حداقل ۱۲ ساعت رخ خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/441809" target="_blank">📅 17:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441808">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaaTf7DjEt6bvLUXHYXtr7pezw_a1oDWUEaOp7jRJV0ifPvRiXtJPUSVKDFvpyUwD6xl-6agFyRR_B47FrlMXvn__OdUU0llEx3ITXKF1K6SWrl6hNyFgimFWTc5ULq-xc9iuA2ttaYBjhzqZTgfwKXZGLYOrlms7XnsUGh72itkQ3vYaebykNdwGWq0hr8olljUgio8v36SipefLcWekakDvyLDq1rooPskLeEfHbRcRMxIAH7_ocHRc0izceRJYodpJEF2-DDWJqlmXMyGIRnnu0p9Wy5hCYRxItFLX3ANDi3SzTJTLe1TTvfpEZYpJZKu0-72op9aHIrFs9Od2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار همیشگی تلویزیون از دوشنبه برمی‌گردد
🔹
سریال مختارنامه قرار است دوشنبه از ساعت ۲۳ در قالب ۴۰ قسمت ۶۰ دقیقه‌ای از شبکهٔ آی‌فیلم پخش شود.
🔹
این سریال با وجود بیش از یک دهه بازپخش مداوم و تبدیل شدن به سوژه‌ای ثابت در فضای مجازی، همچنان یکی از مهم‌ترین آثار مناسبتی رسانهٔ ملی محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/441808" target="_blank">📅 17:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOo0Huax9E1-PxYE4fKWFSv8AW6ISn5Wz0YtTnPE7qWy3m9r26W-pVSmCkST1QnysNPf3zO0Seo1uitCYyo7Bgdvo4RQ2-FG8ACFqEmFphUfhYbX67NEV4fbFH5YNYH55PTeDXi5OFPrdWZvjFvHM4YEl-HXUEzkHYGKw0apDsoseJ0g_56Dii0-W3uUJJYnSa6l_yhFsTAGO_iSLUgj4Ru_o_8YQp6owBRRvY6BHpbFFJUDsoWduyJoUS1KflD3WiuGt_SLHk7MDvEaUtaJzkHbWXS9yb4dixM6UbyfIiM1Gx0xiO69ZZcvBOgUexVSVoj6b7tet72CPlFDgg1TNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰۰۰ مگاوات برق با نوسازی کولرهای تهران آزاد می‌شود
🔹
استاندار تهران:  در شهر تهران حدود ۳ میلیون کولر آبی وجود دارد که بخش قابل توجهی از آن‌ها از موتورهای قدیمی و پرمصرف استفاده می‌کنند.
🔹
در صورت جایگزینی این موتورها با نمونه‌های کم‌مصرف، امکان مدیریت مصرف نزدیک به ۱۰۰۰ مگاوات برق فراهم می‌شود که معادل ظرفیت تولید برق نیروگاه بوشهر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/441807" target="_blank">📅 16:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درهای دانشگاه قضایی دوباره به روی زنان باز شد
🔹
رئیس دانشگاه علوم قضایی اعلام کرد روند جذب بانوان در مقاطع مختلف تحصیلی این دانشگاه، پس از سال‌ها وقفه، دوباره آغاز شده است.
🔹
این اقدام در راستای اجرای سند تحول و تعالی قضائی و استفاده بیشتر از ظرفیت‌های علمی و تخصصی بانوان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/441806" target="_blank">📅 16:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1OJmMUmFPrikCukPVwDgXZ4SohbO9YQzY0iZfkBy4ozK70Tgzj4glEtzY26ykjzohbbEffkr5tveaa1ZuEdG9TwTi_a-aXGgnT6eb_JFvhgk6hGpOTxTlpl8oFzUoWEUTFibIDl6Qg78Zrpu_EuxKE-PxdG_YQ42tDYjuq9yrCowDDRby6CxdEOmnTbtr5kyXejp0DDxoukojCZu-oWNoAGanJ3svTcEXu0AmkDg-ov_Lv0EhWCQENlE9wUilbh_0kYn54HMgjdS6IaQrTfcbMJ2zA7SLaPkkExEErjwJz9TDPi3KB2YBWHD5PC_JWJTI-qvKHisH8tmrbpGvr2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjUx3Ah0Yb3llLbl6wTlpoV4DR_T9HG5oalRUhQEBe_ofzSSGk7OtfHr99gPO_suSNiVS6IaHFXf4SzpmLd-uVbrKvNbQBF2KT__eZ7lzyfX708AJNourMtJpSxaj-73kpuD2v25br4wipAD3QwDRMHpOT0LHhhnHjJoabcUOWlJv6NFuF7SKIaHFZWYGZooIKjJ3t6LK9rU1Gv3-6s071PrFQpF6i78N3tU2IUTSBko-0-KPq_GvturAzGDDOBm5u4py0NRvLQR_qQgWHp7CaT5J7Hi7eZfEcCV9aQaPx08zlwAWPZoQtv4YJ73mJAPmSleL-mRCeyPxzPEa99xYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2DEUzdLCmGYYoGQ-rzw2tNgMxw-P2oMw4bScQ_u5ohQ5ZpDnfUuZPtgJ5p1ecYSJNF1_r-a418f3QlDRBl01cyhOkUeP2wZ06zavj4Cow-gRlAJ91GRiFk-vp0i1_VdW2YP376KE5qnAQ5KL5fZXg7F3W5JkwA8VUIDJ3orb2J-RlI6nLPtJYOcXp_cOiO-WIGF-6FFXMoyDbDOvvZlNQai660D_0CE-OD5LL0PfC614UdAtFuugL7YQ20K1Qm0so1UjqcDJZf1CGIp0HOMKXWJl_SyuW-DlEM4Ch4qmqR_PzhE5Y_wmkhoVXUWLk7YSduYCT-rt2kNGlIARVs90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpgJ5HsS4aiWBSD78qUoatXqSCJiYUHF1kBS7O8H8aVEqUoyEy708Mh7m11yW8Tlw2CCjXAEGiuhcxtkhMo-IXrEeekptBOLYKb-tH4tm21028CIfA6SdVuKkxBObmURgCvNoYIEIvfnMUzKdHceQ_nJ3tZdvzssic5LoCAp8tDM-oql9YTA-yIco_uupVTUn4zMkMDnCM8ttYuqHTF7PkE62o-buyo5YJZzcm4XfA27I5Knghdhns3yv7NZYC0GwfLubfKeJqrhuILdheDX7i8QS_ttOAPTuYCvXW0sDl_615rHG_NcaeRG2DyYdtAMCQ2ffZaO61V2eBa_nq-grA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlBPYZeGLTiAMiy_cMfD1zUYbpNK-2Q0EXMfVxnFZ-GVOmC6HayDfgQcOsgG9RidepPMHTrmkjO2Sr4ziod104If5QbHy6gWw6JRSmsUcPCl-BU6FgWgUp0_ihDeRzr5N40mOZTZsjzoFmy9KErcoKJymkS8gvFraFHwxF7xDYxVNvETdPLFeFWREWNjXSwiWF6OgaSQL2GMDBHk3NUnEVG0hGTySStuy3hCG4qCYwSSovDTmIUez2QMs5m7O_wOHnqfLYUiPf-RJwWuDwWYu-bKKc91SjByTycplr41o-R0SR1ypOfqAGreUYb9cH2o-zFcobRoAiSiPtNBRyyO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22310abe25.mp4?token=tiNxziMULcwNzhiz9geNtXVqUPRICj3_Y9zJFouYwVG2xh9QYsVT4Gb6H5fSD1Na3HAC76O-R3WoLbARm4kRNjQ4-zgAJdPmU_GCs3qA7SbToonpsY8h-cVyGU7hEjQGAB3PdVtbO_MYfTt9gQCkjEypBS-CMMWI1BIDjyxsd0PX1oKGXwzlFxT8lAKOa5LbXv3-xmnD22oIRxJAnmHhS8go4eHdax6q3iVqg32Cj2s-v5Vlyx3czMR59JA83kcZj2iHyDndcIBZVcpRUa5hP_KQ3HMevm0Asy8HGl0Ak9Ayf4fR3w1oNQ0AtYQhiwAxJdEE44izJ9zsYnT0UhhqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22310abe25.mp4?token=tiNxziMULcwNzhiz9geNtXVqUPRICj3_Y9zJFouYwVG2xh9QYsVT4Gb6H5fSD1Na3HAC76O-R3WoLbARm4kRNjQ4-zgAJdPmU_GCs3qA7SbToonpsY8h-cVyGU7hEjQGAB3PdVtbO_MYfTt9gQCkjEypBS-CMMWI1BIDjyxsd0PX1oKGXwzlFxT8lAKOa5LbXv3-xmnD22oIRxJAnmHhS8go4eHdax6q3iVqg32Cj2s-v5Vlyx3czMR59JA83kcZj2iHyDndcIBZVcpRUa5hP_KQ3HMevm0Asy8HGl0Ak9Ayf4fR3w1oNQ0AtYQhiwAxJdEE44izJ9zsYnT0UhhqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید انقلاب در لاهور پاکستان
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/441800" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cfdf36f2.mp4?token=ejR40-MEKzOddyoWJoA-ScYGo7Uhkd9F_uArfGN7kH7Op4fG9H01PtGd_cV-wtLvTp1d75Sw8GUAodHy0ACg58FoKHsKaDgt2I4GF4aj3LhRpYSdC6muNlruk1_LAbpBJGZ2FG6UvFsoaoYZjIrH_HT-OoqTdK_RXW7MezQLpgTAUVoQ1mzp8QMg0iJSbNPNynCgA2CH0aKtvIZkxi3FO5GV3P5Ib7JjNCSq78za0lH_yO4FF7kRINiwyvOFHTqAijlyOXTKmZh6rb5UB2lY3cDf77G2rObQ0-tXYMhsAugn5I2OMTBAbL5EkDmmXUfxKxTpEMty6kcBIb_ytAmr2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cfdf36f2.mp4?token=ejR40-MEKzOddyoWJoA-ScYGo7Uhkd9F_uArfGN7kH7Op4fG9H01PtGd_cV-wtLvTp1d75Sw8GUAodHy0ACg58FoKHsKaDgt2I4GF4aj3LhRpYSdC6muNlruk1_LAbpBJGZ2FG6UvFsoaoYZjIrH_HT-OoqTdK_RXW7MezQLpgTAUVoQ1mzp8QMg0iJSbNPNynCgA2CH0aKtvIZkxi3FO5GV3P5Ib7JjNCSq78za0lH_yO4FF7kRINiwyvOFHTqAijlyOXTKmZh6rb5UB2lY3cDf77G2rObQ0-tXYMhsAugn5I2OMTBAbL5EkDmmXUfxKxTpEMty6kcBIb_ytAmr2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس هلال‌احمر از نخستین دقایق پس از حملۀ دشمن به بیت رهبری  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/441799" target="_blank">📅 16:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDrsC8542NDxvwHHGC79HTR5Kik4wK1Pq5fZEMKn6u_OMvSoMeuWde4l_lbv1oIbZAQuAi7hrrfPzp4aF7jjdOxonkej9OstVmf8npi7i7BiQVk2UO7n08wMQGJ58OzWrfAzYyTEVtY_gss36RnK-u5MVY2tHv2WQ4L2r09cUAs-plr5_2XUOdYGJ_A8VFIS3A0mGsjJqFllMRtDkWgINwtx822f6aLHr802kPsiPSGHnvOAiTOhANmbGYFW5TQmQXXfK2xR9g3D2KXK9EcFVowloSJOAAzeo3GHnUYASGEufeiThEL6_0NkXJM7Sm1vQjmE4TZVPL_GeJtyVpMUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت تخم‌مرغ شانه‌ای ۱۰۰ هزار تومان کاهش یافت
🔹
گزارش‌های میدانی نشان می‌دهد قیمت هر شانه تخم‌مرغ (۲ کیلوگرمی) در روزهای اخیر با افت ۱۰۰ هزار تومانی، از حدود ۴۹۰ هزار تومان به ۳۹۰ هزار تومان رسیده است.
🔹
به‌گفتۀ مدیرعامل اتحادیۀ سراسری دامداران، ازسرگیری توزیع نهاده با نرخ دولتی و راه‌اندازی سامانه اعتباری برای خرید نهاده، به آرام‌تر شدن بازار کمک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/441798" target="_blank">📅 16:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA53bbP0Jovayc2Ih2gyRBfASAcVwI9K_4VVbNFPuYSBTEw2objAcig2nUHgTar33bJDL0i-2zSW_AAE1NR73576uRsqblmcYdJI1_RU7WmDZpPinh6db6I3u-IOYHgHjH9FEzbtU3CL9M0oyQN6vex32XMQInPT5-WdnvzYN7CyE-oexqj2K2Wdj5KoVhW5EO0klrjcglzqEbLKw1oIEB3gUQzq3yBPF7Q-UyWIxmFm1p7Z-LVdx4pqQxiSG4MFmYFaC7OksCeGBNuK49Dh1h2uDqIuhvEluclNJRFblJH4A-CUDmPLo3YWR47OilkGM8v08kKgRiWW-Qphw2G5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ پهپادی اوکراین به ترمینال گازی روسیه
🔹
درپی حملۀ شبانۀ پهپادی اوکراین، یک ترمینال دریایی گاز در سواحل دریای سیاه دچار آتش‌سوزی شد.
🔹
این مجموعه از بزرگ‌ترین پایانه‌های مدیریت و صادرات گاز مایع روسیه در دریای سیاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/441796" target="_blank">📅 16:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9761f96324.mp4?token=RmdtfxuoDUxrXtvBZpt7aVckEk-p9JBjWUOCUJtaz3f6GfFQBdoHmErLJKHu4qUBk6JN3SltnM-kyoPCrUPG4RcDbSSgploHSGYqJ7ZNEViTv__WzXZ72o8TQSasxMI21jjRdmf3_J7Cl4ie6-8M5bB-toLTRNtRi6k-rijBO4cVh0tDJ7uLeSwHa_nMFzy65DFsuVw_kZ6PcyQdqe8UDhbfTERMVM1FkhuUuG1-f6qUleIVTyhgPHRcVq_rrmqoJfEqzMQYwYOnQWtgyASYG_WStBt9A6ZQMeaBPboKfKeF1MfyRiCA__MW0SOPZlEgy8ndYV8MSSDZNNERZd8Y-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9761f96324.mp4?token=RmdtfxuoDUxrXtvBZpt7aVckEk-p9JBjWUOCUJtaz3f6GfFQBdoHmErLJKHu4qUBk6JN3SltnM-kyoPCrUPG4RcDbSSgploHSGYqJ7ZNEViTv__WzXZ72o8TQSasxMI21jjRdmf3_J7Cl4ie6-8M5bB-toLTRNtRi6k-rijBO4cVh0tDJ7uLeSwHa_nMFzy65DFsuVw_kZ6PcyQdqe8UDhbfTERMVM1FkhuUuG1-f6qUleIVTyhgPHRcVq_rrmqoJfEqzMQYwYOnQWtgyASYG_WStBt9A6ZQMeaBPboKfKeF1MfyRiCA__MW0SOPZlEgy8ndYV8MSSDZNNERZd8Y-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس هلال‌احمر از نخستین دقایق پس از حملۀ دشمن به بیت رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/441795" target="_blank">📅 16:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8322c0cb.mp4?token=XC_NydNpH3GSOC8rMKVE5b2uZAMwulQgAF4ifcYcpDhQ16-Id0HJ9mrgndH3IGiV62Qo9-Lj2jQ7gVgoA8p0NMB0NJd7jaGhFQYg4QVmVP3-uh30CKU1Z9Pv6ZPlCQSKJwrE7jCw6naCLj9wgWd_MevWk0iccKyg7xLXquWf90u94uy2-R3a_YZpuUtH5N3ET2tOVjg8dGBqavhwqqLBqP0eseuGkT-bF7NrqNed407Fml9aFFCM_2uwvoBVqjPGK3j52oG6aB98d1Q8zworrZX_SReSsQ5KEqHdYvv9XYasnM72OQ2f_nXzesW7h_9eSTulemBOwwK4VmzJkZ_AiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8322c0cb.mp4?token=XC_NydNpH3GSOC8rMKVE5b2uZAMwulQgAF4ifcYcpDhQ16-Id0HJ9mrgndH3IGiV62Qo9-Lj2jQ7gVgoA8p0NMB0NJd7jaGhFQYg4QVmVP3-uh30CKU1Z9Pv6ZPlCQSKJwrE7jCw6naCLj9wgWd_MevWk0iccKyg7xLXquWf90u94uy2-R3a_YZpuUtH5N3ET2tOVjg8dGBqavhwqqLBqP0eseuGkT-bF7NrqNed407Fml9aFFCM_2uwvoBVqjPGK3j52oG6aB98d1Q8zworrZX_SReSsQ5KEqHdYvv9XYasnM72OQ2f_nXzesW7h_9eSTulemBOwwK4VmzJkZ_AiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم از حال خوب دریاچهٔ ارومیه می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/441794" target="_blank">📅 15:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sglvb_29G0SgBoSTR60VGv3lsbrXmZwl9GjWD6UA8fz-fKc12n3oCeaIGTx-hso3mKjbj0cDHcX0GAtMntZMG6oWH-BAtukuOXovQi-90FWn7aWMPPox7ZFoXxIyUQOlft-ixzELyeVVtMqIpai7VWlFkwfnxUZsZOfWltu1eoWoVmwSJbwfHsFscwZuFE4Z4fY8GK9C5svFVUt5VBtugLYzve_h4Ws5ZF4Z9OMKXuwP2JOMPMOiU_fvMQcO4UIlQM_aFu77H_w4jDHq-PvVs7WOmkaGeseIgbrSccXUjQbDT2mDk6BZMOj6A3CQl08i8MHODJeCIgedMQj3Ezv5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه پرسپولیس لژیونر شد
✔️
یحیی گل‌محمدی، سرمربی اسبق تیم‌های پرسپولیس و فولاد خوزستان، پس از توافق با مسئولان باشگاه دهوک عراق، قرارداد خود را با این باشگاه امضا خواهد کرد تا در فصل جدید رقابت‌های لیگ برتر عراق هدایت این تیم را بر عهده بگیرد.
⏺
باشگاه دهوک که فصل گذشته عملکرد قابل قبولی در فوتبال عراق داشت، امیدوار است با حضور این مربی ایرانی بتواند در فصل جدید برای کسب عنوان قهرمانی و حضور موفق در رقابت‌های آسیایی رقابت کند.
⏺
گل‌محمدی طی روزهای آینده برنامه‌های خود برای نقل‌وانتقالات و آماده‌سازی تیم دهوک را به مدیران این باشگاه ارائه خواهد کرد تا تمرینات پیش‌فصل زیر نظر او آغاز شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/441793" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1c90fee8.mp4?token=iPpjuQcuEtiWJ4eojllz1eX5-pRqSb8XBtCBNdqevWy1HspepRIrr6vBwSo66snXA7sh6Fwq1jjwMGrvvwK696F6Lx7kipDa1Cf2hsJ0Z-ianEb4GA0o4xDYgiUWPHvPPGyYBCEiKG87T-VdjbQIqU-UdNnV9JlGviAWc0V4iZAkTn56zmmdSYg7Wy2bshshHH9n3AvRqLZ2JUxGDXrjKjyNzETU5WrLfooXBDZ8MUmYkp5PENZZ-iSKX0dmlmxNhzINvM0mn7KsBYSRjU2i49trYQBSw3JhlabMEEyFFwvk64H5sWv925vGpunVb4h2ynjYFIli1ptQlz9H0m9z1JGBY0S5mES4WObFviFJDcHxQYUFr7AnPGlIXqpK9vHRtXBGA_ms7eTmjyAT1jvoZdWKqiVbL-PedV4BSNRfeLrHPOkHxEIOiQ1Gb4cY4DwGpip5yFPx3BBoJC4CFBiDWrO-UPONuv2tAvLjcmLWy35Jr_i61zwk9UyCMTqsWsqFQXLgzogW1sd0r_LqFo9GfhB8trjJ-YsTunmzNoGSTtw8nZ0OJPzkt14vUGsKzLe3ScwrQqaufHpa02ge7lAI4bVfIF1Zi1PVRyOm3AS12rP6eGOXcxep4pFM7NA1uevHpHe7gPgsLmyluqn3C0ksBftHUD-KESWFbqV_zypbZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1c90fee8.mp4?token=iPpjuQcuEtiWJ4eojllz1eX5-pRqSb8XBtCBNdqevWy1HspepRIrr6vBwSo66snXA7sh6Fwq1jjwMGrvvwK696F6Lx7kipDa1Cf2hsJ0Z-ianEb4GA0o4xDYgiUWPHvPPGyYBCEiKG87T-VdjbQIqU-UdNnV9JlGviAWc0V4iZAkTn56zmmdSYg7Wy2bshshHH9n3AvRqLZ2JUxGDXrjKjyNzETU5WrLfooXBDZ8MUmYkp5PENZZ-iSKX0dmlmxNhzINvM0mn7KsBYSRjU2i49trYQBSw3JhlabMEEyFFwvk64H5sWv925vGpunVb4h2ynjYFIli1ptQlz9H0m9z1JGBY0S5mES4WObFviFJDcHxQYUFr7AnPGlIXqpK9vHRtXBGA_ms7eTmjyAT1jvoZdWKqiVbL-PedV4BSNRfeLrHPOkHxEIOiQ1Gb4cY4DwGpip5yFPx3BBoJC4CFBiDWrO-UPONuv2tAvLjcmLWy35Jr_i61zwk9UyCMTqsWsqFQXLgzogW1sd0r_LqFo9GfhB8trjJ-YsTunmzNoGSTtw8nZ0OJPzkt14vUGsKzLe3ScwrQqaufHpa02ge7lAI4bVfIF1Zi1PVRyOm3AS12rP6eGOXcxep4pFM7NA1uevHpHe7gPgsLmyluqn3C0ksBftHUD-KESWFbqV_zypbZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گروهی که عکس شهدا را به خیابان‌ها آوردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/441792" target="_blank">📅 15:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نظامیان و خودروهای ارتش رژیم صهیونی هدف حملات حزب‌الله شدند
🔹
حزب‌الله: تجمع‌های وسایل نقلیه و سربازان ارتش دشمن اسرائیلی را در موقعیت بلاط مستحدث و شهر مجدل زون با حملات موشکی و پهپادی هدف قرار دادیم.
🔹
همچنین ۳ خودرو و بولدزر نظامی در جنوب لبنان هدف پهپادهای حزب‌الله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/441791" target="_blank">📅 15:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJbBNpKT-aqXqHeM1uVxXK3abAdamVTQexDyxSv3rbjLIgMxZxXHPzCdMMO5RYbgbh2cPCq8uHh1Y4fQgpi3c9U3hZYnVNnGGnmdr-YGq2ga-cw0gG90YLL3uYsurT1NX6mnv1323HWle_7TPVFJMCIVme1jw7oNYs0e3bZFBBaF4lAHDC9wipWZNUHWoiHQCSXWav9_2ablWvORuY1UfYiwzxaMiZNKTOzLl29pg9y3VbESwEK62Yz1RuXqQGVEHtJ6OwFmUWPTpFEjJrulycYFIt3yg2xi4t-1xBHQZG_DZ1NtKAj3MNXmTNP7iySX0sEKeuQhdVKgppqDuvTs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به آهوهای ایرانی هم رحم نکرد
🔹
درپی حملات آمریکا به جزیرهٔ خارگ، تاکنون تلف‌شدن ۲۵ آهو تأیید شده است.
🔹
معاون دفتر حفاظت حیات‌وحش سازمان حفاظت محیط‌زیست می‌گوید که آمار تلفات حیات وحش مربوط به مناطق خارج از محدوده‌های نظامی است و تلفات واقعی بیشتر از این میزان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441790" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baeb39f02c.mp4?token=NLbj67GPgEvcCGHW6v9TZY7m8nkhiqhxFXzNmGmdEGedgEjI7_QSvJXXiv92XLVhxLiFXL1lQH8I5Ib635ho5uC1XZ6QPW6GqbPjLKjn35brpdhMN8bDJNHBye1ZxCrwm5nkVLN1HyQdPL3_tj_M9FjRdhvZ28Q94FVNuhZdclzCP1UfZEUUALTZDZu2AkVHQvN9jeg3SOmgPFh7T7B-4pd_jnCWHF7Iuf4AAVeQPAQkzSLryNv7F968L85_Vj5qwCpjpPUfTCI5e9uSzwJDEjGvgz8dPxVq1BKwi6W1Rp-0xi8MASkDwZiJeA2u6LwzwWsm32PyND1nV7O2Uyd1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baeb39f02c.mp4?token=NLbj67GPgEvcCGHW6v9TZY7m8nkhiqhxFXzNmGmdEGedgEjI7_QSvJXXiv92XLVhxLiFXL1lQH8I5Ib635ho5uC1XZ6QPW6GqbPjLKjn35brpdhMN8bDJNHBye1ZxCrwm5nkVLN1HyQdPL3_tj_M9FjRdhvZ28Q94FVNuhZdclzCP1UfZEUUALTZDZu2AkVHQvN9jeg3SOmgPFh7T7B-4pd_jnCWHF7Iuf4AAVeQPAQkzSLryNv7F968L85_Vj5qwCpjpPUfTCI5e9uSzwJDEjGvgz8dPxVq1BKwi6W1Rp-0xi8MASkDwZiJeA2u6LwzwWsm32PyND1nV7O2Uyd1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح آزادراه شهید شوشتری تا ساعاتی دیگر
🔹
آزادراه شهید شوشتری، یکی از مهم‌ترین پروژه‌های عمرانی شرق پایتخت، تا ساعاتی دیگر به‌طور رسمی افتتاح و وارد مدار بهره‌برداری می‌شود.
🔹
مدیرعامل سازمان املاک و مستغلات شهرداری تهران: پروژۀ آزادراه شهید شوشتری که از اواخر دهۀ ۸۰ آغاز شده، نقش مؤثری در کاهش ترافیک سه‌راه افسریه و بزرگراه بسیج خواهد داشت.
🔹
قطعۀ نخست این پروژه به طول ۹.۳ کیلومتر، از بزرگراه امام رضا(ع) تا بلوار هجرت، تا ساعاتی دیگر به بهره‌برداری می‌رسد.
🔹
سپهبد شهید موسوی فرماندۀ وقت ارتش، در آزادسازی بستر اجرای پروژه و پیشبرد کمربند شرقی تهران همکاری مؤثری با شهرداری داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441789" target="_blank">📅 15:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9ZCmNNd8LHVlP4Yohrdasn6A8KqxzfrJjfUSkTTfJpMpTMoA6pe8nfbM96YOXgv-MgebdJhYM9MluDA_r1lqMjeQsR0wbYkuqOxzAp5eHL1oGV1DWLzZF5IyUXfHzYIPmVSRaWQ2VvC7rD3IEoxz7_zlvlnM3DuGb7j1l1_Ad31-PsP3T7-emo2iKoaqt04ufzJ5LJFrm8ai8V-nDoOebrRhc2lxlen_zUHLFANKUNpEoys0tiLXJZBYTXy09VBaEJeM-T2-8ADJJ4SS0t916Bg88DB68oRjt8XeeXmLZ9uJgHeQJCGi6Cecy9_xyUjiOnqqertKbY1Y843iqelag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به یک کشتی در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در ۶ مایلی شرق عمان هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441788" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc596f18b1.mp4?token=bVCtlB513hE1ZywxRMjwPg3reSr7ZR3M8U48eDEkwHAniZxvpLETC_1JgsvbgGwiVllgjMFrwfgWX4ZPL8v3RpQnsp2TTYmanhxctg0VTfSTWpo7XKJjDJ85OWQjj2NOXNzdNNRgEf4iqIm5tfqr1MgCgyNWMLLHUg25a3NF27UqMNU__ajYVLQP5IwIVaMBrbQQEV-SzH9Zge3BjPDD2GoDlmUvQVelo0yTf29knsoleiupTt0JQJuZJ6ord1jGRJ9_5mpLD8cyaXq-Cf72TgjVjxrXOtEFP9ICbiCWd2jXSbnGYlNX1Iy-0hxbzQ0m6OyiBU0Sen4Q8MUgZM-pMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc596f18b1.mp4?token=bVCtlB513hE1ZywxRMjwPg3reSr7ZR3M8U48eDEkwHAniZxvpLETC_1JgsvbgGwiVllgjMFrwfgWX4ZPL8v3RpQnsp2TTYmanhxctg0VTfSTWpo7XKJjDJ85OWQjj2NOXNzdNNRgEf4iqIm5tfqr1MgCgyNWMLLHUg25a3NF27UqMNU__ajYVLQP5IwIVaMBrbQQEV-SzH9Zge3BjPDD2GoDlmUvQVelo0yTf29knsoleiupTt0JQJuZJ6ord1jGRJ9_5mpLD8cyaXq-Cf72TgjVjxrXOtEFP9ICbiCWd2jXSbnGYlNX1Iy-0hxbzQ0m6OyiBU0Sen4Q8MUgZM-pMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختلال در خدمات ۴ بانک کشور/ تلاش برای فعال‌سازی سامانه‌های پشتیبان
🔹
از صبح امروز خدمات الکترونیکی برخی بانک‌های کشور از جمله ملی، تجارت، صادرات و توسعه صادرات با اختلال مواجه شده.
🔹
این اختلال در بخش‌های مختلفی از جمله موبایل‌بانک، اینترنت‌بانک، خودپردازها،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441787" target="_blank">📅 14:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c58291e3d.mp4?token=tNH6DrrfYbgRFarlXyLHjGcZKOCL2McBiKN-Tj0xAsvCzlVQgZ_6n9IHtqSzDcl9C0lDWLJ3yObmOy3XcsP5-Lqp73QpNa-p13Azp-Nij6RY3I6HehSxq8E2a9KAxd-DQNO_qH-2GWo78nrag6JhMZxc_2KoePcZar8Xqnr8J9lIxgBKHf0oQbCc3Win07AYp8upNTG_uagyWO1miNFeCb1UG1-rAOUTaaNZ1O2T-fqsLIT2tiH5F1EjeoEM6tEVbsO-iKmyzH4XFCKwWY4paFvwa75pVZVP1jZA8chRD1BJpB-almsjk0A4qYJz2a1UGs7LSN6AZr0-YUWcLgd4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c58291e3d.mp4?token=tNH6DrrfYbgRFarlXyLHjGcZKOCL2McBiKN-Tj0xAsvCzlVQgZ_6n9IHtqSzDcl9C0lDWLJ3yObmOy3XcsP5-Lqp73QpNa-p13Azp-Nij6RY3I6HehSxq8E2a9KAxd-DQNO_qH-2GWo78nrag6JhMZxc_2KoePcZar8Xqnr8J9lIxgBKHf0oQbCc3Win07AYp8upNTG_uagyWO1miNFeCb1UG1-rAOUTaaNZ1O2T-fqsLIT2tiH5F1EjeoEM6tEVbsO-iKmyzH4XFCKwWY4paFvwa75pVZVP1jZA8chRD1BJpB-almsjk0A4qYJz2a1UGs7LSN6AZr0-YUWcLgd4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام خود را روی همه چیز گذاشته است
🔹
ترامپ که پیش از ورود به سیاست، به عنوان تاجر نیویورکی نام خود را بر ساختمان‌های تجاری، زمین‌های گلف، استیک، آب معدنی و حتی دانشگاه خود زده بود، اکنون این رویکرد را به سطح نهادهای ملی و دولتی رسانده است.
🔹
ساختمان‌های…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441786" target="_blank">📅 14:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a04b797.mp4?token=NOEufgLtWUJbxvS-a46_dPqo2IwwoEvkevEYMWYRAMOoP5VDFtx468XWa1cKoKCcZ-pQwzfAkNyxECp8Pg2lZvu7gJkTWO9MGkKJdexUaqqMuqJoEi7tZm8kHWDDNz9-2Dds_NR9R1_T03NU2NtNd1ukbA7ddjcslIA8nciSaxX7q2tQfz1eM-7cFlqiLAMiJ6LxXDYLK3yyS_aGmSQHkF-EJOkpSuTSaY5N2zsMlSd1LcWOGeSSPUbglk4525Rsbj0bG7iRA0tdQ5xW8xr8tvRv6PNHtIPLSq77xDtvXYke6ail5QVO3x6oiEVYD8FR_nBKwmZpoNKIxlCKb27aqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a04b797.mp4?token=NOEufgLtWUJbxvS-a46_dPqo2IwwoEvkevEYMWYRAMOoP5VDFtx468XWa1cKoKCcZ-pQwzfAkNyxECp8Pg2lZvu7gJkTWO9MGkKJdexUaqqMuqJoEi7tZm8kHWDDNz9-2Dds_NR9R1_T03NU2NtNd1ukbA7ddjcslIA8nciSaxX7q2tQfz1eM-7cFlqiLAMiJ6LxXDYLK3yyS_aGmSQHkF-EJOkpSuTSaY5N2zsMlSd1LcWOGeSSPUbglk4525Rsbj0bG7iRA0tdQ5xW8xr8tvRv6PNHtIPLSq77xDtvXYke6ail5QVO3x6oiEVYD8FR_nBKwmZpoNKIxlCKb27aqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آبروریزی گستردۀ سلطنت‌طلبان در خارج از کشور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441785" target="_blank">📅 14:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d5fc3535.mp4?token=VKrZ62DRXQpUHyoPjLB1gvoIwiSg0WcsxvY-UvZEc5kEWcHrTDGcigeae4ivHLrR6noxkIyumRFXCtjmjkDLfWi2b7OA_LBx7SopKQWLfZE7HTgiMJpCvI5YyQ_emyyIsFqXGoW-kpzb0sS7LCUs_l4qY3UNZWm2q7IiZQY5UMU73ePC79xHHCj-HuZH9szTSoDEH-bHqVtF5qKlkCjxdcmD93tonhRA5NCGE3J1SxDC_vhmWfpbrDyip3xia2P0x0gzcnLgxlKI9109QxNl9So_WXGeZnFKM9kS9qUokZT0D8-XRwoN-qcS-Eps94nWKpDN0zXxdAPfsWrkLWnTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d5fc3535.mp4?token=VKrZ62DRXQpUHyoPjLB1gvoIwiSg0WcsxvY-UvZEc5kEWcHrTDGcigeae4ivHLrR6noxkIyumRFXCtjmjkDLfWi2b7OA_LBx7SopKQWLfZE7HTgiMJpCvI5YyQ_emyyIsFqXGoW-kpzb0sS7LCUs_l4qY3UNZWm2q7IiZQY5UMU73ePC79xHHCj-HuZH9szTSoDEH-bHqVtF5qKlkCjxdcmD93tonhRA5NCGE3J1SxDC_vhmWfpbrDyip3xia2P0x0gzcnLgxlKI9109QxNl9So_WXGeZnFKM9kS9qUokZT0D8-XRwoN-qcS-Eps94nWKpDN0zXxdAPfsWrkLWnTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیش از ۱۰۰۰ نفتکش منتظر اجازۀ ایران برای عبور از تنگۀ هرمز
🔹
صیادی در تنگۀ هرمز ممنوع است و مذاکرات بین ایران و عمان براساس قوانین بین‌المللی برای عبور کشتی‌ها در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441784" target="_blank">📅 14:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxrNMZP-o1da_HR-GM7ugUJJJMY5Olc56JWCxK50-Tt7Ubl32RlSS0Mdlso33seiEjHc-uhNlXLnZ0pCwMI9TEF6E8ntaNnhHQ3GmEP1jTBoWOxoyVN9l8RKvLsmsiGmrkShTZsnMPuQ_Ch9nJQpDJ9tTbDiXnFK7VG9lFj9abFf89iaFQP2dgDLku8GNiDb3lpavH4oRLIqZxhXQiuRjQY15zxp4Wi5gM64CoWn5LgjZq5NXASk38sByGNghauDOdDwxwVxqPW1yqIet2dMewKP64qu5HEZzwcPdbZ7bobQZlQB6U9oXB7oyUtQSjpM7qdC0ghBxxT7o8N57gjvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جزئیات مراسم وداع، تشییع و تدفین رهبر شهید انقلاب اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم «مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441783" target="_blank">📅 14:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🖼
تا دقایقی دیگر، جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله العظمی خامنه‌ای قدس‌الله نفسه‌الزکیه با صدور اطلاعیه دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441781" target="_blank">📅 13:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvRBL3vZyJ6vGwoLBUH5Ck8tV-eFtZDLsps4j7CuNCEO0bJPASci2CfE2LqEQU-yBFm_ZRypjtHwHh34jkBb9tFZhA06itoFM5LGC692YC-PzvPKhd_rSohP-MCRnS5rn3tLsikzQSarM8DkTMerVRsewvoafRfjPmJCDP1JqtV45gohTQ3xyb7NLLaZA8nrh09hN-92SJJl3qWD3GyhvxkiM-weALINH-5VrLRV85L2Etl_W3SzqqxK0hgjmb-X257nl3qFlsF86k0KbUQpwUbN9bw1RnOt5Nf-Ah6bRNqUBtgUZ30Z76rSQ84ztPSEdQcgcUPdIWgq9HO0y80VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ‏به تأسی از شهدای جنگ ۱۲ روزه، تا پای جان برای  پیروزی نهایی ایران عزیز ایستاده‌ایم
🔹
یک سال از آغاز اولین دور از حملات جنایتکارانهٔ رژیم اسراییل و آمریکا به خانهٔ ابدی ما ایران می‌گذرد؛ کودکان بی‌گناه را به قتل رساندند و از هیچ جنایت و قساوتی پرهیز نکردند.
🔹
‏به تأسی از شهدای قهرمان و مظلوم جنگ ۱۲ روزه، تا پای جان برای سربلندی و پیروزی نهایی ایران عزیز ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441780" target="_blank">📅 13:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3J_1kChvQx4Muz2rx9LkZ_NdDmhZbyidu9PJoAP3DojvA1tKmxSMRG4PqC3DdrTU20vWybGUmPIyAkLcdM1dhIoCnr-bBDoiwLLXXIVn_VAb-LQp9pLQduTv5zLSA5AOAoCBE1SWJDlp4rg9MB61BHfNl3AbrM3RosqfTOt6tVhMJ9DTsMLZmp0lAfzJ7lsbjC0u51Z6lQT67kGCVc8yNCNt5ePsc-NnlvJq1p5c3cBv5biQyMAel3y0VY3lArH5UNVrprMeYUMiMToAllLJhBpzU2EIXtZcd7OXCJlRoddar3e7OUfqUqNkPYLUIE_PiV4d0lWVNTgBSLP5FymTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌: مراسم تشییع امام شهید انقلاب پس‌از دههٔ اول محرم برگزار خواهد شد و زمان دقیق آن مشخص نیست
🔹
ستاد بزرگداشت عروج خونین امام شهید انقلاب در اطلاعیهٔ شمارهٔ ۲ اعلام کرد: با توجه به برنامه‌ریزی‌های…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441779" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14284d44cc.mp4?token=aD70iCmR_sAF2yVnm5LGhwmYjt3KhItweoKUBUBUfHdW-HZY6egZKIvQJs4-1cheIHIcq5blj4FElsOFg0l3Og_AWCQ-MeI4kuStPtMnzSwP3IQHbXpgJD0R_MJvupkOFWuvMSNXeqww14KneTkgBmXjsHFeoOlLTfuQxKXIjb_iHFJiK0FN4ec40k2QXKBRO7vB7o_Fs2qiFk4SFqzX5SVCGNDPTNEcKto4DWwfwZFTlq7ediwwk6coFp6VFOlupckXHXK8kQeNUyVYFfMUCPgWTXMwim9eq2k1m1gMm21hl0AJ2zxyV8Q_U4G5FZL9mRLEcAeaOQCX7IXGYP8UIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14284d44cc.mp4?token=aD70iCmR_sAF2yVnm5LGhwmYjt3KhItweoKUBUBUfHdW-HZY6egZKIvQJs4-1cheIHIcq5blj4FElsOFg0l3Og_AWCQ-MeI4kuStPtMnzSwP3IQHbXpgJD0R_MJvupkOFWuvMSNXeqww14KneTkgBmXjsHFeoOlLTfuQxKXIjb_iHFJiK0FN4ec40k2QXKBRO7vB7o_Fs2qiFk4SFqzX5SVCGNDPTNEcKto4DWwfwZFTlq7ediwwk6coFp6VFOlupckXHXK8kQeNUyVYFfMUCPgWTXMwim9eq2k1m1gMm21hl0AJ2zxyV8Q_U4G5FZL9mRLEcAeaOQCX7IXGYP8UIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کالابرگ یک میلیونی دیگر کفاف نمی‌دهد
🔹
دی ماه سال گذشته در زمان حذف افزایش قیمت کالاهای متاثر از ارز ترجیحی محرز بود و دولت جهت پوشش افزایش هزینه‌های خانواده کالابرگ در نظر گرفت.
🔹
خبرگزاری فارس در تاریخ ۱۶ دی ماه سال گذشته با توجه به نرخ کالاها در ۱۶ دی یعنی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441778" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
روایت دختر شهید تنگسیری از پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441777" target="_blank">📅 13:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2SupNmqzJ8Yh7nhGqg53_9hjSyC9EBjD4OYGce-43cE83Gaw1pCKVP5vxvOHhtNSpK-_4-y5iYaBuKljhEZXowDafzGrBKfjX53hTIujIWf9dzt0zXvRFRDt8cOTa2yuiVoorD9U0Psig0O8zEs6a4ufl5dqI2krYyQvb9uUQCX-k7_WIOby93Tg9mEaMoYS3ulQchHTutfKPkX2BmPQCS71VdEGH9zHKYxgbq-JvxX28apqSM23Z-Lim0sst9n9Ki7r2VaENZPJp2NpmFtGtyWtPXWQ3mhE_wzmcwU1XvrH5PF5NSPY1GgotbcXBT5Jb1cejxT_FExryfUPI_eAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیل‌کاری در خط مقدم اقتصاد جنگی؛ استراتژی پارس خودرو برای حفظ سرمایه مشتری
روزهایی که کشور با شرایط ویژه، محدودیت‌های ناشی از جنگ و فشارهای اقتصادی و لجستیکی مواجه بود، بسیاری از صنایع با چالش‌های جدی در حوزه تأمین، حمل و نقل، نقدینگی و برنامه‌ریزی تولید روبه‌رو شدند. در چنین فضایی، حفظ جریان تولید و ایفای تعهدات به مشتریان به یکی از مهم‌ترین شاخص‌های ارزیابی عملکرد بنگاه‌های صنعتی تبدیل شد.
بر همین اساس، پارس‌خودرو در دوره اخیر تمرکز ویژه‌ای بر فرآیند تکمیل‌کاری به منظور ایفای تعهدات و حفظ سرمایه مشتریان داشت. بررسی‌های میدانی نشان می‌دهد که هزاران دستگاه خودروی دارای کسری قطعه به صورت شبانه‌روزی در این شرکت تکمیل و آماده تجاری‌سازی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441776" target="_blank">📅 13:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFlwZ83S3gmNoZMrLuvZFmpB7n9d5IeGAt6siChBBrTIeGH1ZTzmv6TT2Bpa79ygtS8J0pPFrd-SLxutpWA3mFfOxd536mWt8ID34lT0Th3Wy8z9PW6rupgXgGsRjggseL2jT7X9s90oakP8_6yAxMiwietpf4ckCp9F-dxsKWci2_VPX1wSNfF65JllhXOc_3XZXbpHq1PtHlqi71GTYaLju5QFchfpeTp18HbzB2hQezbo1Y3LePxO2prc_ZlBTF4l_dq-CTY9JFFOniM0SFldZA-2sjRBY7Xh_ka3oYlarySAmbx0DYLoReKrmkTHH5tEDQLUTeK2aL-f9Qt5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5UXJb_yPOfQVN3iN8pKeT7W2yUNMEOQQ2-hwsapfxPsCJgjDryeGVqS9RQny_5c2453IQEZE_9oeloXbkWyZuSmOzuKyivTs5KVuFdvs0PtVbS0LQgjtwYtpk1TLKRdBFQpEcvvX9KCU7IJKlJEhvrHhVjCZ2naD3AQF9cIS8M4ogEaKWJaV3Ws8YPBttpM4bBTPd5NwephmjTRvHZ8edDfOjBSah9xs0vWBjMqiHDLu1LgzQHVka0_5dfmt-2S2oz0pd_phBF19pGi2j3YHXi8D7CBNEMaHFq97lMAmscFjPmKvQtPZ78WlmP7JZpK90hPB311Ri6_oStzbrbsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg9hr8dA6yxNypRwQLDTfyMXQH8klud-og6Z_i1Ftepz3017KA3bQe2Qm4N4OctPwNhcfQ5T9AIJNo-yRmua336L_6Qy9tS9-vfyNPWMLPmTDK1kUiusyZgjfESXcoHNSQmC1FJXSdM7v8-VyJu4rD5i3JloqT7akmSL9dNfZ1uNUfUjoVkUElKbrau9wKZqDKtOSp5gXdSiGOTMogGi8GDUd9n2DJ5_itlx-4DuSu39llQKbxNoILEklpeleZwCkTxBHW2MA-mst4AcWbQ2KoZoOTtg2xIf0g5en1krXGlcQAWkUydVtwu-bIbiELmqsj01alelYzkJHNS4iQEpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFUym6Qn-qRYLC2-dedenRJYdwLeDXP_yC5JeSM6ax_DQO3XVZXER8bz8DmP34RkWCkYRPFloKx-57oVJuqZI6uvR2TAl8adOKIWwApSn69cqchOavU6CuMgUm5UxqJXnIerdmB4eBfTadd8qpMtlG64Qma2bB9xj5lye2V9SUQGKnMbhLj_d7aTl07hINqay_qMBRW8aDx3VczhuR49tS0CCXJdzUr04JlsjyK42yIlvTpHEqiP-oUexFcc34RKc6loEzvpuBPFba-V8H5f8H0bTrxUPpwSJrWhtw120VxCMMMJV3RTMCG6uzAjJNFb0vHYC_TzjFa4ngMwS21V_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bs1tV12tjaNa2maeYiwHuk1j_KhA5qQnKuSmoJyM0Bh0-l7uYr1lxBYUQW2N2FIfrKHA9JWYm-J89UcX_MUUz23tXLjeHi9lr7nx4Y8TsEqRAfjDFLeT3Bs80iKcBusDjNQ0HQ-IgiXAT9YoIgDuRn9g8PSe4FDuVkTaHs4epxSUZtkjz0sXZJjfbXtgzjbOcp0xh1a5dOtNXlGzGPzhAXVKAAzLLZIHuPiWs7r5fOk0Pjw3G-EzfGOYdfKBsU6Tit-h3mjsE7acPSNck-K-OP6CMxUrN2OW6UmpUkULYFfMvgjzYM7JNduzBMfIV_YBVvcGlSdkWZmxkd-n6XwvgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مدیرعامل بانک سرمایه در نشست ارزیابی عملکرد شعب منطقه پنج:
مشارکت و خرد جمعی دو بال شعب برای جذب و تجهیز منابع است
🔵
در این نشست دکتر موسی اسلامیان، مدیرعامل بانک سرمایه، به تشریح اقدامات انجام شده از آغاز دوره مدیریتی جدید بانک تاکنون پرداخت و تصویب برنامه مدون احیا و بازسازی ساختارهای مالی و عملیاتی بانک را نویدبخش آینده ای روشن برای بانک دانست. وی توسعه خدمات غیرحضوری و دیجیتال، تسهیل دسترسی مشتریان به خدمات بانکی، بازطراحی برخی محصولات متناسب با نیاز اقشار مختلف، به‌ویژه فرهنگیان معزز و تقویت ارتباط مؤثر با مشتریان و سهامداران را از اهم چشم‌اندازها و اقدامات انجام شده در این راستا برشمرد.
🖥
متن کامل خبر را اینجا بخوانید...
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441771" target="_blank">📅 13:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/441770" target="_blank">📅 13:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2bLXHmh00Lb634wLRhw06uhTiW_U2nMqfVEjKIe13hwUkm8ywChFhd9YwVAA3ceVC_0kSOgsWZZmZtcHk4psv-ES4K2vI8uqMj0U_4HGG9w9HotA1N0HK7ZWp4SAgEcmLJQ6V6oRdYfNJEhwdnaH-2hFLdJUL0i8AT7Bt1gF2q3RPGzBLDdtEL2J2Z51P3FXeLzrpxOdS-8FiWhCuIWhVCBrUmln2egMrIxXbYLgXH2O3PMeyGC5mG0Pb8HHfk_LT7Vyo5otPEaD0YIkc1Yvn6Hd4f_9_JrVqEcQCJ3fQHOIBqqupgtTqejSAsQiqrCWifmFyRrqnjJJ5wYyEY-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ ۲ توله‌یوز «هلیا» در تصادف جاده‌ای تکذیب شد
🔹
مدیرکل حفاظت محیط‌زیست استان سمنان با تأیید ورود یوزپلنگ ماده معروف به «هلیا» به استان سمنان به همراه سه توله خود، اخبار منتشرشده درباره تلف شدن ۲ توله‌ آن را در تصادف جاده‌ای تکذیب کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441769" target="_blank">📅 13:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اختلال در خدمات ۴ بانک کشور/ تلاش برای فعال‌سازی سامانه‌های پشتیبان
🔹
از صبح امروز خدمات الکترونیکی برخی بانک‌های کشور از جمله ملی، تجارت، صادرات و توسعه صادرات با اختلال مواجه شده.
🔹
این اختلال در بخش‌های مختلفی از جمله موبایل‌بانک، اینترنت‌بانک، خودپردازها، پایانه‌های فروش (کارتخوان) و برخی خدمات کارتی مشاهده شده است.
🔹
برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده و اطلاعات کافی برای اظهار نظر قطعی در این زمینه وجود ندارد.
🔹
تیم‌های فنی بانک‌های درگیر در حال تلاش برای فعال‌سازی سامانه‌های پشتیبان و بازگرداندن خدمات به وضعیت عادی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441768" target="_blank">📅 12:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inn0kBiIpduRiQPdGo7UsLVJuywVzcrajr3mxKnPwItYNv0j6vjSnmsKSX5nuwumTwU8u9sHeVSfRzzbfJ1M8psXXekfjkRcBPWgjnhgTcs0EjcnZ2pdxgmCt_TCfQDT5QhgQJJA4RlKs3nRI_spZkQGXlS-a01Hw0cQicF5RqILc4Od2N33kBswgM5gjeqQFSVxfxlpX4CQPzvSXAs0C_jtkglaFNJmCM0VF1KLRzSa7ci7mDTTaFPQG_IQyrAN9BW11mfk8GXb3NRAuUE5uuL0VJ6TSvBI-khc0v9le_QDVSpHNJ1ohb024JRcuFd4s0shvgl8owWZ5eXsCMi4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با یک جهش سه‌رقمی دیگر رکورد تاریخی جدیدی ثبت کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۳ هزار واحدی به ۴ میلیون و ۶۹۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441767" target="_blank">📅 12:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8RmBj2Ggm03xSTIvOnVNNQjEwr8r5tdzkBJfFxDqrSV6-OOFOOmalV1gojDLemG_l0zFF4h-30Pn29wBLIoTHpBIsrzqzBghm2__z-FRbSrPUSV8-szrMQH4yDF193ZcV6iArAFPQ11KV7LyZCmBloQKFhzXy9x1b-6M2goMibyg5tIhSe8PNcimXycPJEOuRbK9QyeCWwbTVvFsLkiItYqcIje60tSY0dK_eTVe4MYT9hDitUqCDr94T1-u9svj8aG-LSOsNBw0xJ5epQS8IdG3h_PsTP8PaM0FLoBCCDS-t6sKXXTVH8hSr6dspAeGfRdl_yghJXA6YlAxANDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب، صفحهٔ خبرگزاری فارس را به بهانهٔ تحریم مسدود کرد
🔹
گوگل اعلام کرد که پس از بررسی فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای ایرانی تحت تحریم آمریکا، دسترسی به ۷۵ کانال را مسدود کرده است.
🔹
در فهرست کانال‌های حذف‌شده، نام‌هایی مانند مسعود پزشکیان، وزارت میراث فرهنگی، علی‌اکبر ولایتی، دانشگاه المصطفی، خبرگزاری فارس و برخی نهادهای دیگر دیده می‌شود.
🔹
همچنین کانال‌های چند صرافی رمزارزی ایرانی از جمله نوبیتکس، والکس، رمزینکس و بیت‌پین نیز از دسترس خارج شده‌اند.
🔸
این اقدام درحالی صورت می‌گیرد که آمریکا پیش‌تر نیز به بهانهٔ تحریم‌ها، دسترسی ایرانیان به یک‌پنجم از خدمات و زیرساخت‌های اینترنتی را محدود کرده؛ محدودیت‌هایی که از سرویس‌های هوش مصنوعی و رایانش ابری تا ابزارهای برنامه‌نویسی، آموزشی و ارتباطی را دربر می‌گیرد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441766" target="_blank">📅 12:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیده‌شدن صدای ناشی از این انفجارها در محدودهٔ مبارکه و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441764" target="_blank">📅 12:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7afc5d86d9.mp4?token=pSAPG4u6pUPfWGm9PRbD3wqF9KbMDW-cR8QmnDDgNCdN6FhzldMsD63TfS6NQ2y95azU9CoFmVOpfMD8qAQIOFhmOYMcbCXBve27WQT3eJKVOShC_fGFDeU_9AFsWDQUng4j2V4OlcoXGgUvv706F-SZxfV7MnlZ0xF1mOzEal7Y7NimrfKoQkaOTKIjGhMr2pxd2bx1iPsKuLnPnyBjIF4yNElkbevGis7jzfaYSajaRYlyaut-Jk2sviYEJiBFJ6Q0YY8OPaDwztuDLXMgRi1jROKko1V4wZf4t0mjMh0CneyzSebR83kFl_WSz5_RleW6dkcF53TIqAH3l_eA_BXeOR_8wnLR8EqZj60o3IDAELCfrp1sMExxYGwq98Aq8CsrbA0Od_iZAmcA55HHrahwpFydBjWxZ80Q5KvBjvOUvm9s2Qj9RsyL_6Fw2fsHUkWyD1o38zL6IJ2X0zkWIaWqqcCUniY6uMobC1-Z44K3jdKCqTwl0YrxMKLPr5cYMO9NQdc_jYDPtXdhV0GZhQOmDkP9POLms-blPT6U4JRD_rQLLMrdNYP3eN1lqVkEa06p34f_cvrXM7L4ZSDxF9La7YvV2DNO-hAfSNryirysYtfN4bcAZ_c0L6fKUy4aYcup5mxU-XeEKOrRoHxNo-NjlhNBHGq5iP_i1dj1xRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7afc5d86d9.mp4?token=pSAPG4u6pUPfWGm9PRbD3wqF9KbMDW-cR8QmnDDgNCdN6FhzldMsD63TfS6NQ2y95azU9CoFmVOpfMD8qAQIOFhmOYMcbCXBve27WQT3eJKVOShC_fGFDeU_9AFsWDQUng4j2V4OlcoXGgUvv706F-SZxfV7MnlZ0xF1mOzEal7Y7NimrfKoQkaOTKIjGhMr2pxd2bx1iPsKuLnPnyBjIF4yNElkbevGis7jzfaYSajaRYlyaut-Jk2sviYEJiBFJ6Q0YY8OPaDwztuDLXMgRi1jROKko1V4wZf4t0mjMh0CneyzSebR83kFl_WSz5_RleW6dkcF53TIqAH3l_eA_BXeOR_8wnLR8EqZj60o3IDAELCfrp1sMExxYGwq98Aq8CsrbA0Od_iZAmcA55HHrahwpFydBjWxZ80Q5KvBjvOUvm9s2Qj9RsyL_6Fw2fsHUkWyD1o38zL6IJ2X0zkWIaWqqcCUniY6uMobC1-Z44K3jdKCqTwl0YrxMKLPr5cYMO9NQdc_jYDPtXdhV0GZhQOmDkP9POLms-blPT6U4JRD_rQLLMrdNYP3eN1lqVkEa06p34f_cvrXM7L4ZSDxF9La7YvV2DNO-hAfSNryirysYtfN4bcAZ_c0L6fKUy4aYcup5mxU-XeEKOrRoHxNo-NjlhNBHGq5iP_i1dj1xRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شش‌تایی‌شدن آمریکا جلوی ایران از زبان مینیون‌ها
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441763" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441762">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdd218be0.mp4?token=MoEuiiNKwKEce-qR2IKGiMrE8nAu1vLQnaFoJIv6Q4JnLzul6Gi8O-762Wdr_uif7Kb_RNOr_V1r7bYmvpoYaP66k6xXJoeDx00Yy9STnbCF1RukosCzxGO6XpaPRRkKHQMDm9fiioHyar88LvHdwNXRjrumBDUAt2zwv2lDDY2rHdLw7KOJOoaNbpCp0gmpmsh1eGRPA-fIESkZuqBNyxEoVOU-QalhU4XL1k0i6scXGc-UVKo9IZ4UguJch-vGego6ekVC2v_sRgecIYRZNaJQmFdkSVASoe8_HA95nld2LuWEXmijt0j-wqP0E92CTZhkBJAP51aQLd6q88FPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdd218be0.mp4?token=MoEuiiNKwKEce-qR2IKGiMrE8nAu1vLQnaFoJIv6Q4JnLzul6Gi8O-762Wdr_uif7Kb_RNOr_V1r7bYmvpoYaP66k6xXJoeDx00Yy9STnbCF1RukosCzxGO6XpaPRRkKHQMDm9fiioHyar88LvHdwNXRjrumBDUAt2zwv2lDDY2rHdLw7KOJOoaNbpCp0gmpmsh1eGRPA-fIESkZuqBNyxEoVOU-QalhU4XL1k0i6scXGc-UVKo9IZ4UguJch-vGego6ekVC2v_sRgecIYRZNaJQmFdkSVASoe8_HA95nld2LuWEXmijt0j-wqP0E92CTZhkBJAP51aQLd6q88FPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای‌شهر تهران: ۲ رام قطار چینی آمادهٔ ورود به کشور است
🔹
طبق قانون دولت باید ۱۵ درصد پیش‌پرداخت قرارداد خرید واگن از چین را می‌داد، اما ۵.۵ درصد را پرداخت کرد و شهرداری ۹.۵ درصد باقی‌مانده را پرداخت کرد.
🔹
معاون شهردار تهران برای تامین منابع، شخصاً از بانک شهر پول قرض کرد و حقوق خود را گروی بانک گذاشت؛ با این شرایط نمی‌تواند حقوق بگیرد و به او کارت هدیه داده می‌شود.
🔹
تهران ۱۰۰۰ واگن مترو کم دارد و شهرداری قرارداد خرید ۷۹۱ دستگاه واگن را با چین بسته است.
🔹
۲ رام قطار چینی آماده شده است که به‌دلیل شرایط موجود هنوز وارد کشور نشده‌اند و قرار است از طریق مسیر دریایی یا ریلی به ایران منتقل شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441762" target="_blank">📅 11:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3xY7_KSRA0VS6gJQZ5mtPzs67nw33LdPxqwXkoNnb8dEThf_ZA1qvVgCn1X7OCrurCdILOimMWqa6jXovUa_56UPUZQsxI31CjcKIn2AdHW7zWlCmCcJX9HnDEN1IcT74mNph31B7JC88bSzDCecAoGrPuZhOHGrEUahcRoNCZEPj_S8dX1_dAnJYlVTQInbY8-0af3zf5ybPoNd3x-GaoA3eturOYkMInY_7BZvLPMw9Sxe1nuupgSwonm886nAdp5fYP-TREdZYB3eSQJ9hHnpFGYAT-j6sKroHsSCKmGD_M3NgaQI41UR8fDtLfbsjOwTGyMaS8VULvSLbeaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام رئیس مجمع تشخیص مصلحت نظام به‌مناسبت سالگرد شهادت شهدای جنگ ۱۲ روزه: خون شهدا موجب تقویت وحدت و ایستادگی ملت ایران شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441761" target="_blank">📅 11:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufLcdAJhSzfSQPW1dzcfagpdF6BImm11_vupOBvBfcmi-P7CJmCPhKip-YSGhEQ_8hanjwFepVB2MjtKSV9OWdxw-_ttn1dNKYtWq3UDBEIoFZjz_dF9FC98a7Q0Oiq9VfJKd2VjwmmiO8OLaavM4-zrjju_VqPFMWFi6k6dzpwrAsR6kWxCmT3AMJibVR9TG0VZWqNTJ-VKul9fA54a4lw_tO8L6zDJCwR2d_uN-Ybaq_caf7Ul2hlyi4U_dSLXL6-u8wpUQCQSZ4m8TvgFDZ74-MqrDK7aERyQ-eKrfza1JHZNugisaDiF5mEc9mAd8ZGoygXTD3eJeeFqlXfzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلبریتی آمریکایی پرچم ایران را به اهتزار درآورد
🔹
جکسون هینکل، اینفلوئنسر معروف آمریکایی امروز در تمرین تیم ملی فوتبال ایران در تیخوانا، مکزیک حضور پیدا کرد و حمایت خود را از شاگردان قلعه‌نویی در جام جهانی اعلام کرد.
🔹
هینکل با حضور در محل اردوی تیم ملی کشورمان با پوشیدن پیراهن ایران، گفت: «اینجا در تیخوانای مکزیک هستیم. پرچم ایران را همراه دارم؛ اینجا محل اقامت تیم ملی ایران است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441760" target="_blank">📅 11:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSNcDWuVOImzTpVT2669ZB_3kgUQ6xK0gZ-S3kKsZESTcjEy2kv_MVXqAlismPbFqgI7-Y-L9mwTNVUQA-Q3kGo2MDqSJjU5TTwb0_JTonfC9zIrrjM6jzr220k0I7eA065i5yzlMcU2x77_Ks2JyBx0RbCJ8neddUv1lpCgvVdh9LAusshm5q7wY1aCM2gfNphx-4J6Bzh0BfsWZQSfsIASQalHm9myhwLipUHVXVmr83i4-OzbBfElbfuOGzBmwOhs0Ylx23-mY1DhJ--S4tX4T-7oMxvtVuZLW789YuWqtzqegWJCW9FLuPM8tSZ2yM2ooLdxnC1MTmqSuHrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات عفو و تخفیف مجازات ۲ هزار نفر از محکومان به‌مناسبت اعیاد قربان و غدیر
🔹
معاون قضایی قوه‌قضاییه: افرادی که فاقد شاکی خصوصی و سابقه کیفری مؤثر باشند، بخشی از دوران محکومیت خود را سپری کرده و نشانه‌های اصلاح و تنبه در آن‌ها مشاهده شده باشد، در اولویت بررسی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441758" target="_blank">📅 11:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruF97N6DqzIL6-yKDPrcEUqqpky9-t1PKboWtw9Za-pRMmRO24nQiNUb41wvdtrGiAJacJpMfMyP_-I55IoXtb8cw5rklMkJZWJmwqCHmhXMbfjS-D0sr6vxDp8MEL-mEH-lX-ySRny3YBJ5wQywBME4rr2v23_a-uI9tMjJA-UnhyKRHvUtBerJ05f_ez8YGtOun2sxjU81Lgx4rhMWIGmrKQAJyuL1159tzcFDdnBeLrsNibJvnKTRi5A36ieXa_hEMc1UQ4BN5qeTK1PKABjd33iBxNOG6RKIs0Fm6FQbioxWcklYaPkQ_u2REyP7FYds1FliRKkgt4W8WPiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLn6ESRz0OCmfvz8mNtHyr9lpliI6eVsHfvmrm9M_ovoszIzuAUiepjd5MV8jct-vt2zkh4dr8vu6BBPBX9zLPvQ5xZGuq2jD36VEnF2by4631ZVhIVrQGgO9R_7-YvYRFno8BqFPXuOjzDjnZlSTyKEg-XAcxLODmFoMkfdUdV9EtXfQGdxPyEIzyH8pyBm67XENspzFeqxmL43lj1nnKQqfGqwOlkxuMH-vok_LI6Jxh5xUx5hbcbcJvTBshR2UYQ4tumarefGSDv1XzVfUfzMvn1dly_DonhLTdClO6djoqKqODuX5V1FXOpZ6A54pdjCVVSCVG8mygOOVUJ5qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8a0cc480.mp4?token=hd2yd7vaYpLAdqxZC3WczLbTs9Dz3qiQlweSam2qIAY9f9c4ZeYWkQ7wBTVkkBleqvbVTzh5NuGAA4IZdKNHJuJp1GwbwPZEggA__ua5fyi82LBApWO1qTm8_Lzvxw4ctkY_cSwMSohlMsFQehWU78hEQQQY-CkjUk-vlhmUXGoPAGufPafUuogZQNOQ8D02kv9GbX3Ty2wXj_7QwvHDWu4V9qqwrCcuBHJDRob9z7nE1v4iCUVXU5V37CxiBr21li14-44xHr8q_2Ur0PcNj-iRXShYJVoM7or-6W97KfL7DR2TucFoLOIGQDxi-CACUNOb8Ha__CBEO4Lv-FeFmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8a0cc480.mp4?token=hd2yd7vaYpLAdqxZC3WczLbTs9Dz3qiQlweSam2qIAY9f9c4ZeYWkQ7wBTVkkBleqvbVTzh5NuGAA4IZdKNHJuJp1GwbwPZEggA__ua5fyi82LBApWO1qTm8_Lzvxw4ctkY_cSwMSohlMsFQehWU78hEQQQY-CkjUk-vlhmUXGoPAGufPafUuogZQNOQ8D02kv9GbX3Ty2wXj_7QwvHDWu4V9qqwrCcuBHJDRob9z7nE1v4iCUVXU5V37CxiBr21li14-44xHr8q_2Ur0PcNj-iRXShYJVoM7or-6W97KfL7DR2TucFoLOIGQDxi-CACUNOb8Ha__CBEO4Lv-FeFmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواپیمای روسیِ ارتش هند سقوط کرد
🔹
هواپیمای ترابری نظامی «آنتونوف ای‌ان-۳۲» نیروی هوایی هند، حین فرود در ایالت آسام این کشور سقوط کرد.
🔹
طبق برخی گزارش‌ها، این هواپیمای ساخت روسیه در حدود ۱۰۰ کیلومتری مرز مورد مناقشه هند با چین، هنگام تلاش برای فرود در پایگاه هوایی جورهات ایالت آسام، سقوط کرد.
🔹
افسر ارشد وزارت دفاع هند سرهنگ دوم ام. راوات، سقوط این هواپیمای ترابری نظامی را تأیید کرد و گفت: «تلفات (این حادثه) در حال بررسی است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441755" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alRG1wJLxRkOmgk38JVt2_h_E_B4I6t3v4xmxE75by9efmD5_n_Ce4h61yBCbIHw2i-92OQpLaPagCFFL0BK8I4JHOSYM1-SzKL27ULw5QXlonx9TuHFfAXKZMzY2gmFWCMtBiR7hgqX_m7lIwLr7ajFi9BKBn4TkbdsSJhpj3oCXIepliHa6Fl1B_dPWBmNZUif6Jq7jjBpWriLWtJbewhh51vslThGmdDn0pQKetWi47exoPsgmw2OXC2syGBZJ9BXIKdOqRXw8QVuQVEhZNuFKznUgQAkeqq0bQgt6eOaxOIhZEFPe7O1uLdLVr6lvxAj3KoQGQPUxfmoe5zaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: دنیا به‌زودی طنین پیروزی ایران را خواهد شنید
🔹
پیام فرمانده قرارگاه خاتم الانبیا به آیین بزرگداشت نخستین سالگرد شهادت سپهبد شهید رشید: شهید رشید نه فقط یک فرمانده میدانی که یک مکتب در عرصه دفاع و امنیت ملی بود؛ او که در دوران دفاع مقدس به عنوان یکی از معماران اصلی عملیات‌های غرور آفرینی نظیر فتح المبین، بیت المقدس و کربلای پنج در قرارگاه مرکزی خاتم الانبیا ایفای نقش کرد با هوشمندی ژئوپلتیک و تحلیل‌های عمیق معادلات نبرد حق علیه باطل را دگرگون ساخت.
🔹
دشمن زبون و درنده خیال می‌کرد با ترور فیزیکی مغز‌های متفکر نظامی ایران می‌تواند خللی در اراده دفاعی ایران ایجاد کند، اما غافل از اینکه شهید رشید میراثی از دانش، تجربه و تفکر راهبردی را برای هدایت نسل‌های آینده به یادگار نهاد و امروز فرماندهان غیور نیرو‌های مسلح با تکیه بر همان نقشه راه مقابله با جنگ ترکیبی و شناختی پیچیده دشمن در دفاع مقدس سوم را هوشمندانه مدیریت می‌کنند.
🔹
بی‌تردید ملت وفادار و قدرشناس ایران اسلامی با تاسی به سیره و منش شهدای اقتدار ایران اسلامی به ویژه شهید رشید تحت تدابیر و منویات خلف صالح امام شهید و فرماندهی معظم کل قوا آیت الله سیدمجتبی حسینی خامنه‌ای همانند همیشه استوار و پا برجا در میدان، پشتوانه مستحکم نیرو‌های مسلح در برابر تهدیدات دشمنان به خصوص در شرایط خطیر جنگ سوم تحمیلی آمریکایی صهوینی بوده و به فضل الهی جهانیان به‌زودی طنین پیروزی ایران و ایرانی و غلبه مقاومت بر دشمن متجاوز و تروریست در پهنه گیتی را خواهد شنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441754" target="_blank">📅 10:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
سرگذشت عجیب داور برنامه سرآشپز شبکه سه: از ظرفشویی شروع کردم و به رستوران‌داری رسیدم
.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441753" target="_blank">📅 10:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUBRQeJyFo8BmUrZhrrmrFL2PhsqO6iEmjkMh1cnq1NAVVuSS-nqJHMjSSDmoNZp4RKDogOZ1aB2G11MnC0EXbgI8T--xCpnbt4zAnGm_QmP-qcfVUjUb72wBSwxJJxLcKsK-Yu249np8yeUVmHghYbOHRuU-lbItnfG9tcQrS9le4KpwJ7EteifYWVkdD9Bwhl0IcS2wnry1KEZhFFw7OW-RFv-8WOEjmqAfjAuipMzBEBfdxAAZQsO3r0QlA8Bq-GMlhjaihJoItI3zWifXdutQJTdV3HRObcfYEcaYiuJ3XduhGudKSIxjkrpVWelxEUGaZUdWLG20N73vD4lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441752" target="_blank">📅 10:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441751" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5443f02782.mp4?token=gI8sw3Har6JZ4GvooDITIagJ9f2KO5sHU_QCL1sHX81wUi4_XelxJl3vpu_Rku2XR83kf664bGhTiS1MsIotEC2bbQ3CTDjPA7j1M8Fwx43B32-76mPdVX6dGhri2bAU6zOVOjUJcLB1g3WEbs03kNSN-l93wi6_krReAi8M5j4vJPbBPE1PEsaCf_Q1DjZHRznXQw3R1DWHeVrrEcrCEy3Y8sf8r3-x3wWKKNf3HEi_ifHVnWO6l3uTXs5llcsz3iXYwVpPT1xir1xRO7Fmrimfa4TSD9PqFhtI2ypiymee3tQX_ozVPeq8Ttgw0MrxLvT3fBxu6voCRXIUPR1HIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5443f02782.mp4?token=gI8sw3Har6JZ4GvooDITIagJ9f2KO5sHU_QCL1sHX81wUi4_XelxJl3vpu_Rku2XR83kf664bGhTiS1MsIotEC2bbQ3CTDjPA7j1M8Fwx43B32-76mPdVX6dGhri2bAU6zOVOjUJcLB1g3WEbs03kNSN-l93wi6_krReAi8M5j4vJPbBPE1PEsaCf_Q1DjZHRznXQw3R1DWHeVrrEcrCEy3Y8sf8r3-x3wWKKNf3HEi_ifHVnWO6l3uTXs5llcsz3iXYwVpPT1xir1xRO7Fmrimfa4TSD9PqFhtI2ypiymee3tQX_ozVPeq8Ttgw0MrxLvT3fBxu6voCRXIUPR1HIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم حضرت عباس(ع) مهیای ماه محرم می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441750" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
رژیم صهیونیستی برای ۲۰ شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد
🔹
سخنگوی عربی ارتش صهیونیستی از ساکنان ۲۰ منطقهٔ جنوب لبنان خواست فوراً محل سکونت خود را ترک و به شمال رودخانه الزهرانی نقل مکان کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441749" target="_blank">📅 10:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در دزفول
🔹
فرمانداری دزفول: از ساعت ۱۰ تا ۱۲ امروز، انفجارهای کنترل‌شدهٔ ناشی از امحای مهمات در برخی از نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441748" target="_blank">📅 09:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
اهدای تجهیزات تنفسی به بیماران سی اف، زیر سايهٔ امام رئوف
🔹
با دستور تولیت آستان قدس رضوی، ۹۰ دستگاه نبولایزر به بیماران سی اف در بیمارستان اکبر مشهد اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441747" target="_blank">📅 09:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس دادگستری اصفهان: دستور شناسایی و توقیف اموال ۱۰۰ نفر از خائنین وطن صادر شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441746" target="_blank">📅 08:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce6d0fe70.mp4?token=W7lC6rGSmy-yUE2iMGhKh5K3hiF8NS1gI-uzz8e3jNMUa0J9Ft2EJQyXcdcHMjVACak96OcioCojUxDfy7YCA21IsJSaHR9OUbg7LI10IW27yL1ZbUa_eVvzfxUpeLPlM6JHydI0k2wxlutXlFwtykGNbSfPI0bj5d1Ujk4sMhJuQIjTNFdxZ62CiaKGi-G6H3TGyQuk4SoNpGtr6GgZuoNzfv2HRfGw2kX_FxhatqH2UECgyMdNKWmH30stOC-H67rgiRHZKnBLHWi-O9qbPWtAulZ-j4HUHVfrR94VJa4cFJkYQ9jbxdijOl8UfWuIMrDKu2jodp2YzlNj2_ajyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce6d0fe70.mp4?token=W7lC6rGSmy-yUE2iMGhKh5K3hiF8NS1gI-uzz8e3jNMUa0J9Ft2EJQyXcdcHMjVACak96OcioCojUxDfy7YCA21IsJSaHR9OUbg7LI10IW27yL1ZbUa_eVvzfxUpeLPlM6JHydI0k2wxlutXlFwtykGNbSfPI0bj5d1Ujk4sMhJuQIjTNFdxZ62CiaKGi-G6H3TGyQuk4SoNpGtr6GgZuoNzfv2HRfGw2kX_FxhatqH2UECgyMdNKWmH30stOC-H67rgiRHZKnBLHWi-O9qbPWtAulZ-j4HUHVfrR94VJa4cFJkYQ9jbxdijOl8UfWuIMrDKu2jodp2YzlNj2_ajyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
عراقچی: تفاهم در صورت نهایی‌شدن به‌صورت دیجیتالی و از راه دور امضا خواهد شد و سپس اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441745" target="_blank">📅 08:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMisPDaUA53dIoApMqvEBJyxHfIKEuxFa2EwDKwAQoJb0JyNmAb5SDTAgNKsKDINRa1AyveoZJGI4TDj0ttJTv-9d_ptfUgvqq6MCE4kwWma-Ct4sucG1zDF2w289TTN_bnNpbqcJTp-E_LGPCMF2QrCg6cTOwXhm9UHYSP3paAIs3DlfjWe9_9VYfiiBBckYaUbuQygCz9SmRNS6rZJ-b-HkTLhrrnU2XDZyhNmu7M2NmnyHt2fPsFWXZmXj2PgNx2Vb3UQS2jwb_uQOtciLRiQyRKbuQoVrdR5Ew9-VyWgEGPw2ZKMqtjv_enONWkNiGVrgJBy1Myiawv-wWbZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگل‌های هیرکانی زیر رصد چشمان هوشمند
🔹
مدیرکل منابع طبیعی مازندران از آغاز مرحلۀ جدید پایش هوشمند جنگل‌های هیرکانی خبر داد و گفت: با استفاده از پهپادها، تصاویر ماهواره‌ای و دوربین‌های تله‌ای، نظارت بر عرصه‌های جنگلی به‌صورت دقیق انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441744" target="_blank">📅 07:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjENhcEs64vrNzZlS8nf_3D1zfDLX7wHxPuCIKqokFKcBqYVfc5_AEs0yxBjewDUs4GwhchycX-lerVq9m0E9m4ZUp8-3LzvDl-GOphOtAb3VHYKwtiC1w-wDuFP1n5pshfDIcrgT_UG5ePxyGWrfhf-m62KVsiNi0Ols2LO7PUDY3nshCy4wP_gkhC2nL3TCzhFPPL14pSJKSCM2GBJVFlh_SDWX18EsFgOKvWTDGvwGY7aitCRpzC7J6YpA54mO-PzbM6NnPRO6eT9q_tPTqMxnRMsSIBcBXjlxgLXnskwVXNXAjHd2S-QCatQFtzt0CrkEN8BA_V-Mgk0VQvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام سرویس مدارس آغاز شد
🔹
والدین یک‌ماه فرصت دارند تا درخواست ثبت‌نام سرویس را در سامانۀ سپند به نشانی
irtusepand.ir
ثبت نمایند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441743" target="_blank">📅 07:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcb57Xjd3PNgVOcQ2WTBigPEtcYYJ3UXv5cEGwj_Wche2FORB8gIS-KH5JQaFynrosIScTIgc5owsC8QzQnaI1yXzfViCi61YelL51KGPADTM7z7_C_wrLuNtqxxqkxz-Onxeu4BOxufjhdqeU38L03jF0IZs3OR7MP56zaegTNUBDsmd_wkun0FxZbnccHqowBZgsxl34k_him_rNR_PVXpDF293VzrTjJ19g9X76e5qF-tvZdM4gGCZW-gl9mFsCJL4FSfEcpi4Sw1taMcjsux3KYmGOTthJf1gDzdAX3dzxWTlTCEsqOgeaNUBgOZoBuKNAF5_bGHqZ5jxjbOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پایان بازی آمریکا و پاراگوئه، با نتیجۀ ۴ بر یک @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441742" target="_blank">📅 06:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODRpXAl3MoRdYOvKbm5vynrbnHEBnfx1J5B0HUBjVele6Opust0Y9BaCyXJedJjqEcv2U87Tc6IAiNfsKnyg5CjW-PYpQfZr8mKK-p_TtzyIldgAeRB3gBYEwl-e30EVJIVz4mbp-cVyBduuRpIZpPxvQEt5JWPenlBo7geUNmTwEjaQeLQYeNnol-VyiGQ33YeVXYYEBaP-nknF-8l_VDlXuwuMgIBSmAMa-oy9jbnr5VJDeCjvgsdPK2bZRTK2Usoe1e-J8Wo9DvmSNMIB4N_wPRpv8XmcNiIer01vRQSCdZIahA2FXomSxIyqyRszBMgvLgQCy2i5eNHuyx24IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پایان بازی آمریکا و پاراگوئه، با نتیجۀ ۴ بر یک
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441741" target="_blank">📅 06:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOFJ4YVPOVXKQ0guuYy5gHZ3Ok1qI5c6kg9PcK1Mv_h2pmXHWKbnBpAa-lDa6A5I7BJfsfp9bpf05fCM8mao0K4eBgEb21L7firtxEYQmVBjgpziGe1O9Gqkskw1e-45sBboyYF9btjoQEZDgCyjDFmrAOE5hQM_Ea9_trVjhklyuNufed438s__0-XtD6tlysvr-bt1a8GFAR-GDrPKlQXqEocXJUAmapVEhjF_9d12g59HN-k84YRcJ04QrjUcvEGrZkwllym0DOYFTv9IlEPpM1J3MtWFl2hKScHtQ0f-ArFmah4uKLLahSx_bMYbzEGWeoU4uY9Iz4FUsy7Gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taGz5A0fr4RVYh63x6Bmypxd5HzmOd5x2jeJ0x2A3cdn9uIi4RuISdkicq7vmdNb-SLQ4Hh8j1FVNt9vDhPkOQlD8fzBSR-Jbly5LIsua4TejAd9jI67O0McIianmYwPBtQtv6Lp3o5hXTlbwS4MzQBEVnp0LHcE-VcF4wDEAuuj4NLIk4Vbqy2Uo2ht3XxxGE_pNST0FpluqdUZDuI5SHl0HsYQmCswlaVd6dggBJe3sDNTEEIJOc6lA28mUE6arVJM_QodDFD_FgWOQa2hBxSRKzeE6sD-hwDIUutUe1OZzM6FhaIREaY6ZdXVa6_xGTDld_3bFHoGmbf0UB_hQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLHFRIwnJZXC7wlwK4AtJQImEW40jLzj4LOviIKMhLkCYPCq4euVtKe38iQFKBiG69rlaW02pDg73l-RDQg2QaWz6xClO8W4_xScjGerKKUbYJJvqcqDzUwdjnNo9tytoU31ENvnCAyQPh-Zm_K3X9Z4nQ_u8K2Ouy3sC8foWDi_B7rCQwgTHrSFXVu_IqmNo9OPEoVrHu0IRA92EEQuArvbz8LCtEbfD5NLCZU8zn-zv5ksL0QA_0ZCIeZqfXmhyqWGxrI9n6tipc1lZ5uZHk9ls5gpCn2FHAHpFJNP8SSeWQydfTMb9bdC6ubSCy7NBMVtSRDlsMU2bhhJE3YRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nABmJjsSWeXZ9MpJnSAyUrYv51jy3vzEsasyQLssRETURGdmrJxCNRVTUFFktVos61nd2-2QKIeRoojCZ14FMYeQvLC5EGbK8YT1drVl0_6G2UpIXwuPZOLmi8mVx5zOdQ4B0JYI20RX84CCA3IbB_-Kh4_SJtCnAhFwSTNsPwDMivzIA3M5-6CGc4TOYNQY77qOHdT41O24ADWdWb81mOhNwCMaApJAAbbuVvPT8AZfijsLj5JQ7qmsAPhLUhYYI9YpyoG9nMgDWeeIr4UsRxUZi5-wbTkiFuYsJ8BgxW042Jjvdk1zJTch2JSwVYnmywvdc4P0QBA563y6z71shg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zq9E1jLX2cKQ6ewY-Pl_wT5gPqO3r89rcLP3UOPm6LnnH_jLz6EVcq6KKjQL4_2wjV8z3H4cWGiqLyCPbNARt36TtryEF7aX3Wr-Pyg21lHTbrHcjJb3V5rkKtRjiViYKVHL9jgZOzX5HCIjncqFeIZnY_UTylbvjxLPjBsjYGQESSdcxAALiZy9a0d1WWxCPE1YxLmfzVZKbZXS0UAgH4PfV6jWUO1QMoizZshNsCKQWMxDBHz0eyogGCteZJ_7LlUEs3Isvl7HTdeTQL27M5eTM9NDYQ7DeGKB1Paeq0Gbf4TEYA7I8DA_n3YxT9oY3RvPwnN3vxznC5SPYaTc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLPUt2rw3LCwD4eyQ0Eaez1wM6bgql1leMvzkIICbfgx81wMw9wqyFzLy9MRhW5yKEFmXieq6wzyi_oTYRU09YQ187S9GXDCJadQMxMCcdT20atx6hNAxEFKFVJwRwqDIH_5FGzptrJsHhY63ahob0dJoykNGPILhFz4ca6oEe1NfJR_4O-nzKL99LrcJxoC0e5tu_RDjk3tbpEmpt3C7r_ZVK3Jt_mE225YCoMlLXR-Ja-HMRMSoCnJc6qH2rJi_VYNNSQ61SDvkMMhMYbphPi-yTpANYKtGw8Of0U009vz5Lj2KBFYV97eHz0Jr1XHGUDGJfk7au_JaYiHowmxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_ciNAD6qDTSWB9Aof_jEMT-N67egeSA6ZKNCvIy-fsdvkucRs-oe6tULK5S0OmgYgii7_P0fNDBpa1kXj4-o66k99tK_lMShN_Ryp3mq-3IvnS2Vm0kwGWlAAEfZZNNDUuwMDNg50RHoAwDLEMnSZyGbhLIRDM9r5MmvVomZW7KYgtl3arlnHtuknlhNrH8xF58h6TUb2Cpa9y48E5PBVSL3-o7KSBnaQ2Tdb5utiSc9OfFbYPYw-JfctFFfjONbzLBumTQ0k1s2mBzzY08ZajGjhU426cpYN-mhtuBUBVbQUY-pmt8Le5H8GVzdemqW7Hw9Nkszx6tiEE1xssedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN9PKWvh0m13ua3Kugxdp6zD1w40lazxi_K0v__824fsmF7OE2C73H0DK1pUlNn-hSsHP2qvv44GcjUYyq2CeT5abMH27Vujd12926c8mPOI4Hz3uyCY1SV3DN1Fwf3WbepgQnlhmHObLDLbz79d3_xGFyTeT94ZLVDOhKI7nC_NkYr3Txanf685WP1jTpPFUWQAez3TyVQG8_sN9yiUrVl__eaMSsNPCgaTer1o-u3Fm-LnAuVfwhKPPD2qf021ZDZmUYO_BT7aOkjyL6Td1btOQpoebmRdW1svor-gzgnPaZ73-jJpoX7HmBJP8vbka6OvBj8_wmsdCEED7rghmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dc9Lpbwb_LpFa41vw4PnRNbWzmM1HFAGgCcoKWy7EDHlwxa8ohZO2skkiqWTdMLAfiXm2W--QIE1OFTxY6S9S2Z5EjEA6SCeTD9KXmdLlnokt9RLCXRS6LNodueBW_QGkmkfSrToljZeJqVYunu-9GrA1tC3bB97N1aV6DDTgIPNRHbf5iu1IZQp4VYoXYqkJDoT4nwY2KRP0HbolsU4SsXRbGfEB45jH2YcwuvfCJLFml5cXqK0XGiZLio4CeSy-nZ4IRLtHXt0kCLFEHKhLfG4fYPXTRaxEJUL7BWhgtsYid7hafxY1ZkVppyQcv8DF7AQqNiMAe_Ru5-KYCT4GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طبیعت زیبای تالاب آغوزبن بابل، میزبان سنبل‌های آبی
عکس:
هدا کاشی‌پور
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441732" target="_blank">📅 06:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f8492ee8.mp4?token=rkZxRNVBTLKRZujdfl8HPjP1C_x1JH4fIQWZCAm-l2dlXC0g4I7qVU3FaJgJ7rnAzOwsIAgega5II0O_jhHaUfN0-F_Q1vYa-V3Tn5VOQJq2IkW_TvbzYL3BabjzFQ2FcUke10r5nNSmuVve2kvdyAF9WHbTjKtBN2izbHbyy81yI2CDo-wXOjMopV4rdny7If7BcjVMomhbrfesHk03BsdCnDa_1T0S3hV5X80Nu0EAId6aEuSUAcSwW1SG9nKAsqOaogVKjRzuKlEJiNP_uAUAupFxuQRjDtVhgL-Nz2Ajm13Y4dLEy4D2mFFLPLqyxGlaklxaSH9LTnH-tm_NZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f8492ee8.mp4?token=rkZxRNVBTLKRZujdfl8HPjP1C_x1JH4fIQWZCAm-l2dlXC0g4I7qVU3FaJgJ7rnAzOwsIAgega5II0O_jhHaUfN0-F_Q1vYa-V3Tn5VOQJq2IkW_TvbzYL3BabjzFQ2FcUke10r5nNSmuVve2kvdyAF9WHbTjKtBN2izbHbyy81yI2CDo-wXOjMopV4rdny7If7BcjVMomhbrfesHk03BsdCnDa_1T0S3hV5X80Nu0EAId6aEuSUAcSwW1SG9nKAsqOaogVKjRzuKlEJiNP_uAUAupFxuQRjDtVhgL-Nz2Ajm13Y4dLEy4D2mFFLPLqyxGlaklxaSH9LTnH-tm_NZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخالت VAR برای کارت زرد
🟡
داور پس از بازبینی صحنه، کارت زرد تیم ریم را پس گرفت و به آلمیرون داد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441731" target="_blank">📅 06:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شوک در ساختار اطلاعاتی آمریکا
🔹
کنگرۀ آمریکا در پی اختلافات سیاسی و بن‌بست بر سر انتصاب ریاست نهادهای اطلاعاتی، نتوانست قانون کلیدی «بخش ۷۰۲» از قانون نظارت اطلاعات خارجی را تمدید کند.
🔹
قانون موسوم به «بخش ۷۰۲ قانون نظارت اطلاعات خارجی» که از سال ۲۰۰۸ به نهادهای امنیتی آمریکا اجازه می‌داد بدون حکم قضایی، ارتباطات افراد غیرآمریکایی در خارج از کشور را هدف شنود قرار دهند، برای نخستین‌بار از زمان تصویب، در پی عدم تمدید در کنگره منقضی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441729" target="_blank">📅 05:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4aa0b04d2.mp4?token=v7s_UxmR-YV7LHAmi5i2LXd2yF7Y2OZUU43FsOEqrU97mja3TxoFeTJjPYklWs_7t6tKCYaYaARqmMbliQkzJXQky-D5yy6CPxGL5QxRfl8vBM5IzT6yFHLlGuwyZLCIYwHUc0i-lEBLWNMnJZyPFOWl353OHlOK5xQm2koDCeUiu6huAcyDqS-zuNuaLFu022jKnXyDxbHshtFLkGGckEawlDpMbmeUTwm8--pc8oWp6loj5avujUbaujGXsFSdnVyedDPoagKXZtmSMbE9BCFIuusln1sNXAreIgQrByBwlLuYB6LKvY461jpiuNOsNo2TMANHV7qrstSkQGHL3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4aa0b04d2.mp4?token=v7s_UxmR-YV7LHAmi5i2LXd2yF7Y2OZUU43FsOEqrU97mja3TxoFeTJjPYklWs_7t6tKCYaYaARqmMbliQkzJXQky-D5yy6CPxGL5QxRfl8vBM5IzT6yFHLlGuwyZLCIYwHUc0i-lEBLWNMnJZyPFOWl353OHlOK5xQm2koDCeUiu6huAcyDqS-zuNuaLFu022jKnXyDxbHshtFLkGGckEawlDpMbmeUTwm8--pc8oWp6loj5avujUbaujGXsFSdnVyedDPoagKXZtmSMbE9BCFIuusln1sNXAreIgQrByBwlLuYB6LKvY461jpiuNOsNo2TMANHV7qrstSkQGHL3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید طهرانی مقدم: جمهوری اسلامی تسلیم هیچ گردن کلفتی نخواهد شد
@Fars_plus</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441728" target="_blank">📅 05:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d88936d2f.mp4?token=fBH0akH70s3Uou5YyZ5rZ151cC7qrj_LgkrJzR5Dr5HKxbl3n1hpClIR2zrsvo9mqYNKjOwGa3PbHHOzmjgveJ4UZB29JbGuQOhjOcnVxbAALxh_ZOgTDfuyu2VtCBE2MD7_qIRekyu5ndIBDaPD05UbXl6cFBappBKVU2m7AoH7NDf2QIUAEIA5V0EwYohSyL2K7yHKRkWzMv2_HAOCV04dCo6tXXiSnoAKZGpFi9HcZuFnEAYElKwJX4bEiMKTAxdKZxYxnmS96bL4In7G6gleLfgq5ohwiKHHVlozRaNigVz1Hs0wXlzL_pKz-eIjLCicjj54uQGKyAL_qymXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d88936d2f.mp4?token=fBH0akH70s3Uou5YyZ5rZ151cC7qrj_LgkrJzR5Dr5HKxbl3n1hpClIR2zrsvo9mqYNKjOwGa3PbHHOzmjgveJ4UZB29JbGuQOhjOcnVxbAALxh_ZOgTDfuyu2VtCBE2MD7_qIRekyu5ndIBDaPD05UbXl6cFBappBKVU2m7AoH7NDf2QIUAEIA5V0EwYohSyL2K7yHKRkWzMv2_HAOCV04dCo6tXXiSnoAKZGpFi9HcZuFnEAYElKwJX4bEiMKTAxdKZxYxnmS96bL4In7G6gleLfgq5ohwiKHHVlozRaNigVz1Hs0wXlzL_pKz-eIjLCicjj54uQGKyAL_qymXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل دوم آمریکا به‌دلیل آفساید رد شد  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441727" target="_blank">📅 05:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6090ffd634.mp4?token=b3eNpaloetCo1TYay-hJZdcxpS2DV8BGmjj_eQnOGEvjjrPt6uMaIhrwjfbPhhOt3TYB5yjZIvuNDkO0UprhVOimPL03nKxEJ0wqLpl78oDHWJ6IotzUv_QvnCY5K2tW3skXd0ehLJ57ppouSy2Fckqxn3isRdI-oeVVuFway0igZtc0WLKcmKCzDXUQAml9ZOObQJ9hgjx3kpJvaKrK-RdVJZJvocbdGB9czwS4W4ZhGKrHffrdq_jXqRgvVSdEqVj7q95727aCr5k8Tk1YNnz4mga1Pzqlm9mkb4ViDWW-5V0opsafUpuzIhCwPCLhglQEGOJwOxwLGxBqbgCw-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6090ffd634.mp4?token=b3eNpaloetCo1TYay-hJZdcxpS2DV8BGmjj_eQnOGEvjjrPt6uMaIhrwjfbPhhOt3TYB5yjZIvuNDkO0UprhVOimPL03nKxEJ0wqLpl78oDHWJ6IotzUv_QvnCY5K2tW3skXd0ehLJ57ppouSy2Fckqxn3isRdI-oeVVuFway0igZtc0WLKcmKCzDXUQAml9ZOObQJ9hgjx3kpJvaKrK-RdVJZJvocbdGB9czwS4W4ZhGKrHffrdq_jXqRgvVSdEqVj7q95727aCr5k8Tk1YNnz4mga1Pzqlm9mkb4ViDWW-5V0opsafUpuzIhCwPCLhglQEGOJwOxwLGxBqbgCw-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا ۱ - ۰ پاراگوئه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441726" target="_blank">📅 05:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
منابع خبری از حملۀ هوایی و توپخانه‌ای رژیم صهیونیستی به حومۀ منطقۀ کفررمان، شهرک ديرالزهرانی و چندین شهرک دیگر در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441725" target="_blank">📅 04:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884af75b92.mp4?token=pj6Mn6uHsjb3lrbP53ki7-cVR78TvIxIhXYrIKZeuJkwSMnvcUHy1bla_FAN_K5L_qzDfzo58mgwDRB1v-E0FQsPMxoTLc-CpXmRK1bBL2k-a-JOgiu_mKg2BgUWA6IrePpV3YBJovRhWURtBqqpnC3QmCeXwnAMOaOwLttq5miXZXf6_YpHgyt2leX-rIT1ikg12zCDqA7YwsyosGZ6LczhYNnLhzEfAzKHenBQT-rbTcCeQZXMYY7wpjc0r3jG9KbSyQqkUeadK8irNbI_r89YStoS_lhUmUfOGOuVpiUMQwYZ4d_ynGrbg40S1AjDtyJW_ttOfI-H6IIA3Qw7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884af75b92.mp4?token=pj6Mn6uHsjb3lrbP53ki7-cVR78TvIxIhXYrIKZeuJkwSMnvcUHy1bla_FAN_K5L_qzDfzo58mgwDRB1v-E0FQsPMxoTLc-CpXmRK1bBL2k-a-JOgiu_mKg2BgUWA6IrePpV3YBJovRhWURtBqqpnC3QmCeXwnAMOaOwLttq5miXZXf6_YpHgyt2leX-rIT1ikg12zCDqA7YwsyosGZ6LczhYNnLhzEfAzKHenBQT-rbTcCeQZXMYY7wpjc0r3jG9KbSyQqkUeadK8irNbI_r89YStoS_lhUmUfOGOuVpiUMQwYZ4d_ynGrbg40S1AjDtyJW_ttOfI-H6IIA3Qw7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اولین گل‌به‌خودی جام‌جهانی
⚽️
بوبادیا در دقیقه ۸
آمریکا ۱ - ۰ پاراگوئه
@Sportfars</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/441724" target="_blank">📅 04:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441722">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43ea1b1a2c.mp4?token=cwckYv8UDl9Y1xnZLV1jvd1jEG2XEoLzDQoDxy4XQnUi1k4FkpfF8F7ENKwKaAcbGdOmSTLVgf-X89k-ePwdwAFZiqkILs3d24tKU3_q_rorfQIuIYF25oIHwxkZBQ6RO78AF4cnHk8EYn_bZFIweSNzrJePiUm8iF5Sq01DUVaUuxx1UvNUNWV5pZeipFwhbUK7wQ1RpxuO7xsWcZHB_4dvp2zSsUhEDfqfCCEet_D7ElBf3mkKgFRhvpbSCKiD0H05XA_pjYFNafdlj0ZaQqikjgY0t982qzk0L1WXlls6sBte4IlI7pJzRxYX5REbGYdMcmjhlQ-JCWqqi65yvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43ea1b1a2c.mp4?token=cwckYv8UDl9Y1xnZLV1jvd1jEG2XEoLzDQoDxy4XQnUi1k4FkpfF8F7ENKwKaAcbGdOmSTLVgf-X89k-ePwdwAFZiqkILs3d24tKU3_q_rorfQIuIYF25oIHwxkZBQ6RO78AF4cnHk8EYn_bZFIweSNzrJePiUm8iF5Sq01DUVaUuxx1UvNUNWV5pZeipFwhbUK7wQ1RpxuO7xsWcZHB_4dvp2zSsUhEDfqfCCEet_D7ElBf3mkKgFRhvpbSCKiD0H05XA_pjYFNafdlj0ZaQqikjgY0t982qzk0L1WXlls6sBte4IlI7pJzRxYX5REbGYdMcmjhlQ-JCWqqi65yvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخت نان برای رزمندگان توسط جمعی از خانوادۀ شهدای قم
🔹
جمعی از خانواده شهدای مدافع حرم، اغتشاشات دی‌ماه ۱۴۰۴، جنگ تحمیلی ۱۲ روزه و جنگ تحمیلی ۴۰ روزه برای رزمندگان جبهۀ نبرد نان پختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441722" target="_blank">📅 04:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcapmB3TYmWfuIt5lumj2Y8YDU3Zi3BuiV22otX9w-waeCU1xdIxQRos3LMw5m6xR0rij7_2bU3h7Q3oZCYMCFqL3AQWUAYx8lPvcQS5E1kqzncE7QVWDkiUyp86IygT0B0rBgXX-1jJyfM6mUhtPDva_zLFQf-WVm3aRCmJAwJ6uAsK-agkLM5CZm-xHKKvXY-JLkdNr9bZLNCnmkX1n4y4j4NlkSIVQacipqsBuiiCfh0WqeLJgJMzHBgpj7M9cWvwo3W52i8ovI_zSox1r-06-t0jrEnsbQRkNisju3ZkpKS3IhUamWUFuX3RMCa1t7AmgBw7dxCB_860QXcMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصحاب آخرالزمانی سیدالشهداء
📝
انتشار به‌مناسبت ساعت شهادت جمعی از فرماندهان شهید در سحرگاه ۲۳ خردادماه ۱۴۰۴
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441721" target="_blank">📅 04:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELdDxt8-jH5QYhZHC9EI2sNVcKghLuvXGVC-8bUPdy77-C4_E8URvAzr71tG044r1a4yBRvd7-PLqOhPAUFd95WhjS32_eAEgjUxRsbP28K-7aDQ6IPNrhLlEYST5y8NHQkgMA3ii_cuElKrct7kjX63qIIm63LZTMDAyzxddTkmii3ENMpWzVA9OrtLhnQKSFIVUgRACnrbEuKkKdG7Sk6EHsGyu-T4OzDmCvK3iPV7QDyryDL5245LLRhu43bZ-GNRpjZzQOEdJYPMkbOk_J_5HO7zpvWQfdTPhfhvLejTZO25noqPBFv0Tvc4Vy_OwhfmBe1Owd2-XxVvQvYuJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین پیروزی سروقامتان ایران در لیگ ملت‌های والیبال
🔸
ایران ۳ - ۰ آرژانتین
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441720" target="_blank">📅 04:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441719">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUHJS1biHpsos8Im0Hp8uF44XP5n_MHMfD8LQe4l2uBzpY2DTHXVfrWHD-1ZDJEE_Xt89gqKD62rG_WMMKQUkrcrF8fAGC1cGkmDK_8NO8y_HUZuTs43BA4fw36zvxDZ0LnAKnBlEr4DVr6bO_b9ZxcT460WmgjfVrVOdqjoYhIcfqfkSHT0RAkGRSH-nwWdszysxF2GBAVRW8LMeT3syC3KfgzUk-8EeYW_3A_wg4HcvspppPTpxzwODDH_O6tTa7CpOooOiIAHZWhb5ay1-ilirvOPOjuoLWzOlJv0Q2Nwq73LKSDbCIngnw_vG5r8YbkOzMHtqjW12X72RaNnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصیحت جولانی به لبنان: اشتباه ما در مذاکره با اسرائیل را تکرار نکنید
🔹
روزنامۀ لبنانی الاخبار نوشت: جولانی رئیس‌جمهور خودخواندۀ سوریه، در دیدار اخیر خود با نخست‌وزیر لبنان به او هشدار داده در مذاکره با اسرائیل «اشتباه سوریه» در دادن امتیاز بدون دریافت تضمین و مابه‌ازای متقابل را تکرار نکند.
🔹
جولانی گفته، اسرائیل شما را به‌سمت دادن امتیازهای تدریجی بدون ارائه تضمین‌های متقابل سوق می‌دهد و هم‌زمان حاشیه‌هایی باز نگه می‌دارد که به آن اجازه می‌دهد دامنۀ تحرکات خود را در آینده گسترش دهد.
@Farsna
ـ
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441719" target="_blank">📅 03:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441718">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m74tcCl4UJBEDddfjnnF9Zq2GtDIPYeZqqnb_eWqsN-umTjvc39I6SUwsbrMKjmdgFoB4VfJsDQPTBqbeQA6SEV-R5YrJNTKGNbgqbCMWk9pIlGbg-THQrnePuwC3t0JRocNTv7EqIl9L2FnOL1Bo0Tl40kpjMwnjK2ze0LJS9BzIAr_r-XjUMt-587GJ1FwXsYUxo_LI8kNpSG4DYb_8hDPhg_bv4J3uEkZiVEVd7YFGeOQCEHYh3HtpAjQ8BMYkPlBqOFnDnfOMnUkq7NUSxd7IbMwSKLNyBWUH_dw2frV3jLIJlQvTanUXhoicoJMJURiFjIwhCO4cXr0nFAceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سینِ بدون پاسخ سروش رفیعی به پیام پرسپولیس
🔹
سروش رفیعی، که از ابتدای جنگ تحمیلی سوم راهی کانادا شد، هنوز وضعیت مشخصی برای ادامۀ همکاری با پرسپولیس ندارد. این در حالی است که رفیعی همچنان با باشگاه پرسپولیس قرارداد معتبر دارد و تا پایان فصل بازیکن این تیم محسوب می‌شود.
🔹
رفیعی در گروه مجازی اعضای تیم حضور دارد و پیام مربوط به آغاز تمرینات را نیز مشاهده یا اصطلاحاً سین کرده، اما تاکنون هیچ واکنشی نسبت به آن نشان نداده است. تماس‌ها و پیام‌های مسئولان باشگاه نیز بی‌پاسخ مانده است.
🔹
پرسپولیس به دلیل برخی بی‌انضباطی‌های اخیر از جمله غیبت در تمرینات بعد از آتش بس این بازیکن را ۲۰درصد از مبلغ قراردادش جریمه کرده، اما بازهم تغییری در شرایط به‌وجود نیامده و رفیعی همچنان پاسخگوی مسئولان باشگاه نیست.
🔹
بر همین اساس، مدیران پرسپولیس در انتظار روشن شدن وضعیت این بازیکن هستند تا مشخص شود رفیعی در نهایت به تمرینات سرخ‌پوشان بازخواهد گشت یا اینکه ماجرای او وارد مرحلۀ تازه‌ای خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441718" target="_blank">📅 02:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441717">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
منابع عربی: ارتش رژیم صهیونیستی هم‌زمان با آتش توپخانه‌ای، عملیات تخریب و انفجار ساختمان‌ها در شرق شهر غزه را به اجرا درآورده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441717" target="_blank">📅 02:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441716">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQpWG9Eg-4SDkJi6PP4lWaHNM9GYCN3kxa9r57MjSWZrfXOMec1GQIo3m1cnHjdc_3wjWtembofyOJzD4C5ef07idmhpeOvMvvOZsIarsMXO-hG9r692-iawvz1DDpMPgG0CebRrpyGkB3UX2KLkLsqubnfXOj5rQ2BWJT7UZorpDQeLG70xjJHVumBGbX6kQa9g_23UrooGJiW3F67KhR4tnml2cxNXV_AWOVhuAx8XWchQRb2FCJVG05CNeIEhRxUAwif8av8M1cWm7hq-EVL8FdlpA_XAgzLmXeyCxMzSLG-MjGPRfNjVTRDnn8M9I6_fhAuuA4xkwWNbKOXc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: ترامپ موافقتش با آزادسازی پول بلوکه‌شدۀ ایران را صراحتا اعلام نمی‌کند
🔹
عضو مجمع تشخیص مصلحت نظام: ترامپ با آزادسازی ۲۴ میلیارد دلار از دارایی‌های بلوکه‌شدۀ ایران موافقت کرده اما با صراحت این موضوع را اعلام نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441716" target="_blank">📅 02:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441715">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic9RC6WPYhm8EIuyHa1vgsBXNKACP72CleOCgFBRZyxef3OrKgZnwjuVZ3j6pEt1lHo0RX2AIMku5FTZbJPzrNVb2OvFC_Q0MtD_618ehCoQvEfSQpY23JHJW-HcUn57pB3G6gfuXC0FGdZnanrjnr2JJuGyHBMt35zRsBF1PSGbjA3BZIeyfa9qNR3ILHCedrhn6ZEbw7iUwTHjMNqNs-tpzMJ5ugqOsr5n4DNSKeks80tJe1uriMfYVh3wZJPj-aR_6av_Q_r8IImZKL_DcEEk4FOGxf0H1uOTCRz7N8xM5nc2nGTF_xaTQMKezMUR0v0YsWBk8CZRAVkJbQg3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک ترامپ برای کتمان اشتیاق به توافق با ایران
🔹
آدام شیف، سناتور دموکرات کالیفرنیا اظهارات ترامپ دربارۀ اشتیاق ایران برای توافق را تاکتیک وارونۀ او برای کتمان اشتیاق خودش دانسته است.
🔹
او گفت، هربار که رئیس‌جمهور دربارۀ اشتیاق شدید ایران برای توافق صحبت می‌کند، در واقع دارد اشتیاق شدید خودش برای رسیدن به توافق را لو می‌دهد.
🔹
مشکل اینجاست که وقتی رئیس‌جمهور اعتبار خود را با گفتن دروغ‌های پشت سر هم در طول این دوره و دورۀ قبلی ریاست‌جمهوری‌اش هدر می‌دهد، مردم آمریکا دیگر واقعاً نمی‌دانند چه زمانی باید حرف‌های او را باور کنند.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441715" target="_blank">📅 01:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز: امارات با آزادسازی میلیاردها دلار از دارایی‌های ایران موافقت کرده
🔹
خبرگزاری انگلیسی رویترز در گزارشی نوشته: گفت‌وگوها می‌تواند به آزادسازی ده‌ها میلیارد دلار از درآمدهای نفتی بلوکه‌شده ایران در بانک‌های خارجی تحت تحریم‌های آمریکا منجر شود.
🔹
این رسانه…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441714" target="_blank">📅 01:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0Shg1_jThkEsyeUpIZtmKWiECzRatPMiC7OCfy_yVKoZQydtq0lyV3m8j3ZIt4DvLcQnqUG5bluo6AgPqLg9LBX4QghkmUUFcRBXZhJN1kYr4lp-VHUmqTuPbW2f5ojglrQ8K8bHAand6SZ9HPpF_NRb-e_6JCG3DYhM0YmDoqSuS8VoBGFphUa9hw0QNoMtP-xpIipyLcZSMW247hx0rpf1MeLGiQMozvVdNN848Q9RZKoBvDOd5ofQbAAUPq3sDTIjGMrTHacxyBmFnpZIApw26ZjeKMSJB2U_5RnWQtNQCMWyNGAqD8ZwHGoiLEhWfP5qnT4NZPASPo5qzBZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گروه B جام‌جهانی ۲۰۲۶ پس از پایان اولین بازی این گروه @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441713" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahkm8yXfNSftaYIR3uUxOBhH7YRUrOhy-wpHHOkNWqt4KqSAg61aICFv1e7w3KTNSN1rcSDgXthTuhlQhVKbR1hMTaMKAgpenSS9DdTpntR5DaJR3GHn-AMZWzYU8Jc-hzLWnEztXf7-0V8b9qK0FSQysUCcrBwol6tI7xjzViRInnVvjGqBIVOVslr6pNPH0-snxWDdaJjD9a3Yf44Ds7RPBNR2g4t7B5BPnscAEIRfPV6Hnd9Uoiy0FnsVLvEwz1RNyBHgP2CMEZ4xfE3g1iJfCgU5NiSL4vDt-fI0BQRQh5YEJnBIzbQHDO_qeZOvMSz0D-tVNrNey7SB3a8YwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWOtZosUFWXdBxs-0RTNGUOvyQD0KlWvX7eSbQx36MMO-MXqiqi4XL4lELibMDuqq9gytjUOPdQ9JowoDzpkcEX6CoGcNChkc8Z0-XywATVzUtcaz3miSarhlrSYl1PZi0QYJz1Q3VpMnmhz8CiUZOY8AIimhQvds5r_eLlnFuxLpVAobFI-3oWZPxZT8-NzPvaQZ8muY1wsBTzC50qQBzLmmTPRa62pV23Qzzdb11yU29E5W3C3tyTq0vreTVNQN3x-lt5jx8CFUUbOEyMu9yu8lfP4u-Zbs76q0Va_506wNfD8WZgkWfoWduiOs4VpKC6RW7Vjrjbb_ryAFawqlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJGoY-Yo0ymfKSWr5ujTpB5WtmlUSHiWcJXgD2nwHGCkJtlixT7NAG57HsY-o5Ng-_DD-LaY9ohxk4_Ag2QufgPUYBYnRFHD0hX6MtnsMNn06PNPUGLkcw_QsXVZpFhekRc8PlFxhFFOCqBxAU5S4UszgwFzjYQldiwp7AdPswmfkiIGCCZTd_mR7zE_Jr7tjZkXt7NdfMvGGZ9ySkLAPdS2XlbI7tGBrz7D_hqYnFZZ4R6bpDH-gvhYqFku9Vjiiu0xvR-mALoIiMuxpiNExuV56w81HsdXOvnSAtemJxB7VtpwWHMHBcOuTPx_fcvC_VsptLLOUoWZBiuUePBIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGK6my7IBWGhxu4ChIptesHoi6fK9hDo2GA4RJhSsUwp-umCb2t7SJKvqzsQFHKKpBVhtDNqIG1FT8ulan5zr-RDnFIJnwXA_HUoXByqJfSnv-z7kyT8cMAHigzho6ylo765_hEu-CPf2O0IpLMXs5aNHFVzgaB51LPkwnSlzE0aTO6hF8_pMPVi67nh6iZJd_ckEVotyOY9JzL40LVlWsngYWD1oL8KNP3pferCxE_OTRVOnMT357aeNoCNcvdhiGrhIRNTJDF5zIYbf4jgmqjSaSKgnJ5HylkBtBokqZoJlOnteqWKvk2Shq_c5Cu-1crASNdc2DA8q97dAQq_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSMxPr-udhCCB2a3uAFSYHjB6cr09fFh0t5wi_lZo--4MFFQuth3ojxyh_kXpx-QeWNIvoKUsoX6NTPH-mHhgmmRoxoFcZmibWmylvwdYqsAXyzItpO9U1sEAUg0wfaBXc7cJsFZH_SpwrBI0omrDLVgQ7em9E5G1TX1fW3tCqqxB_lwXTIBjE2ssTaa5QG5g1Zu8a5yYG4fN4KCfHMxSc2q8bFR0y47YJjK2dLzYvtBOt7p4wVpiHhJCkN0WzYdS3YB21EDdk9RAbJVqmuXmZhz0u9L_lt1ych4tNUbWusoLE_GsoXuP9sQUwSuapGhKyG0qy7nU8EUi_ynVXqDsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۳ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441708" target="_blank">📅 01:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDhjMdadhz6yYSZTXYNy8tiByC-ubNmg6w1nJsYnxzU07TwKi6FWX2AN9RwXc1u31NfWMAaXagi7pO3AL9_lVqfKA7Wl7AZ76gCHMzc7St82CdcGacokwP8dJzmg8M30N-DwGSQWd1YEz8WHjhiMzrxiqDp1I2r01rP38wKjPvdoXXzilKVYprNIvkSoTNhhVEpDeiZEFI_9v61OYdg1DinWq2lLX1pkcrMETa5h3tvdMroBfiJcMPBaSoRPXYKvHDRNMUnmwGEAQM5UfAYdBH1kiaWCo4paza6Q2WdPRfj2_6bWo-u0DWa-q6Mq8cAR1ZViJoqytdBczrnJAPuZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ8HqSjqNT79GHBeiu21XjeLTzykwDPP7f7s0jE757SMkqKLSzyWYXEQBJwAwf8nnCvFvrN56oPKiM5Q4MwayG-aIfJGpa2IzClmk313uLx5cuvfLQIVUkNFD2XLBqF11jXbmFCIQDdaub__VDz9aisd1Kne05hYoO_DtwILnbNzYehFQi1pW-SN5BTDQqjGZ2HpSag15RdDrl1xyBp9kunFYzfZklK7EkpMYLAoovwPUUADn_Rv3yai3H3gYyzinMnpad28jJXQX0KjjdzxLordD1_BGs2PUskR0XZFlQDxZHQ9Bfe-2CWb9wsGGQgBrz-O20sHHCCrJTXKlcXMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKP3mUNkrnWiAc0027d0xZotO7AmXZ97E6NwP461Rvm9T7wYReSs68WlQYQOn7HOx8uPaI59L-dhv_mia7mH_JICqshuFh4s2G9xejTlZUHl245UzthCNJY-reluI_hS9O6s8WsXJcnj7s7USfBN7W-B3us_sbbd2q9rfq9-2VWh61EYgA-In8B2mKdzKqeyrbJxJHbLFVgfPGyobyCgee9jGv0mYeP69GZu2NYiu88HI3RdC1HRnQpCdEo_q9s8-VnbIUf3xKI8SlhRsQ0Ija63QJDXpQZe0o6hUs3EklTdvAAq2xdku-oyF1f_Rc3uDzf-so_yqEm_5n8ebZAhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6-j6_aM1enpf6u43tZSSPpkaX6_K8apYRdLqpB2ssPQKgpN1f76lGOBGsUBAPUvLPJusqTvqBPVMGFD6RUcGZlbRgZFzpZvxMGTNLSt3e6K7ruOO16OCT6nHmTYt1yMaTTWc6wIHKrlBxN85Cxes_AomEbwgQ0hXCmN28ECEJeItfqKqeLlDV6w96hGXDrsmR1i9aIPCylaevmDQyFlmTuDgZ-BMrcn5xUUHiH3S7pPQbFGzyljt4eU7GE-HQmkVAzneTyArS7zn_S64JieBadGTpOUR0447cv5bzNrIXgri4fI68Js9ki5zU3XpN93KMyjI9s30jb8jPiFuy4npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-O10BD2-UeEdfN3BGjdUgcT6ckROBVD82RDSktZaZfjjItG-Ae5OiUPxwm3unehsn_wRACbFBP_hZ1hC1wN4vGyT8SyejQUJKS0brOvzjlt5Ebu7WsOvXxSuTAEoNnC582nQZ0NFV9cBQZirQZ2f5Ja4u_SgWIDCe-70LnHiaZwrI-eioW1KwRrZjHO28-_fBe5haYwXsNqZarBaV5CP5WK6weNherwRbifWzVGlOk5tc4juHDvjKc510zjekHtjFH1HmD04Yw5_vlgP5TEtNFo3EZiq_09ALdBaGvWN0BUs-ZA5jqptvLmotQQra4QPuuvV2JkmEIp6w-sqeEi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGa2ut9aBf4IqMODMx5ipI2w9Va0k4PSKJlAPVszgI0R0p1c27HGj-yordESMGZjEvKhJ0IhEdnVN0M-O4jCyBcntS6G693qEVvvC-4As2Njj_MeEQREnBNxtEaL8eZM2JUFYD_tXZueEsxLQ64uGowgkxy0SNt-bM2kjtUzwNlR-QrduoNLzrr08abjWpZI1PmwCsBe-URkacbe4y5NsJrpqR0KhWnGj6EdXlRyYNcD7HTvmUMeB5HNrkYRoTgBTKOIe26Ut4iGGxQze3Gnj5VGd2R0WVWcnZ8lvKXIo29wIuOMCRadFqegQdGRnFlD1YAReKwmEn4ev2rgFEkeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNKqAKfFm1evdFR1Ldy74ptrntqgps6mxgEIu4OyewPiwhL5T0UaEzxA2PAtIfOKAksP2msP0C6L59J2mklCoCI4xJTwaxF_0gDebx_5CNURsR4t-4hZRpk-hnu8Gyv3azI3kbiG-N4VFfpOFN0rWBpN1GcbDYI5R9iHvkUjGsGTDaroBwIY7LYS-3xoeG9LVFOsyy-6ixqCpaXBapadr9T_ew3QrwB8RCBB8GWWV0ktAWwCwUL5G80hdq62YLm22Q872XBkKmEJJa94d6j9PLFFWivR_8gBSvexLGzW4Sg4WAQycYzFWX4Ea9CwA8sd74vaKK-H7_ZLhUpoQRYPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HsOSc85xoXMWRUKyAzPXifg-jHoSewEBtbf8TxE79nvzoudYRf6VLMBpgc1SOeNGGW4ZkEeugwJQ9ARYg83gJh5HYC8HfolYeW-HdMLqGkfrueDD4MmLdlLJZcHpRHMgI90-8eucCCvs1ZDLo_75utMTT4jK8LojFX6AY7xIR5NdISHoGXC6HbhqVewUPdSCVDrNgv5MwI-gTrP9T_ukuyZW0fXUR7_guUcdQRzP0rNihrGHc1aDFUdD7HVqjyJ6iAimvap0GadtlFxjrEDPeLtmQQY2dYvaL5Nde-ybTNtfKYnG9JUuqMYtXFHp4jML34kfDurPo-ra69Is5vuAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnaJvVHZJk4nZTWqU7jv7a36MjWT_mrGJJ-X5tziypuGeemOs_Aw-A9HKjzfDtdi5BHwBYuxioFWyheuimhOogdcGf0Shuj24-wxkuhIPKr_PKfBBgz_aSQpS_aLO41CoA8emArRSFqPop_a5S7FB4f7jifMGhULN--TlDaSlpOIZBGcthP9wFwGFvPGnjQYWL40mUP92ynjUtcLCHjQKBoZPbplDqprtFPJSY1xoln5LXVvQLHE7sBND4-4CCwRJm6IpKfE6wL78Jl3UCPjEvJddPBwSTbYWb_QDg4YfaoTJ9WXbZo5yZLbOKOwtap7LOoJpGhycNMnF0miQ-MFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RB7liQjZ25CbpdsJbcte0kS87tdVIqJaFgzu43cLMoscVctdNtPFGaXiYqFReEWcic8D1CkBVeT8i9MsR8TTXod0jTbkDfPGm6SY-dKDYD5RE6t8i3ARQJjR-bAkwEBestWYe6z8qNOFfQadiOMA-8uIf7A2kb33IY1NwiQglGvETCCGrFDEcKV4DEVhzBS4wKLiZBOZcv9xV6zga8pjfk1hl8LjMYceoPqNV3wPcMe3MKhO_nNzjiD9YtaQkDeyGUhMQ2FoqkholWlajIl2w7dOdtDh1HsQqQtOZ-6P-PTxJZgsew-G7yFaSsR9FiVwNqy3OAvG55hmXjq5cqppqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441698" target="_blank">📅 01:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLD8klQ0uNbXtRE5yfrIK5e2SWxARVoMqLs0zpj0zoddFcPLB-s4PIuORytLjxXtfc2jO-AeiOldtxl5ce_sv7KtHV53tLdvYYE-pK0KcpV2pv0VgGz8C1LogIMtfDXJeOxfKRpwuMu6xrhNLDd4igzTxghFrMO4bJUBMvezdw1cke0GDtMSLXrG3hRFhhK4rUg8gW79B_MV_MMLwfMiCEnxmhcASFA6tWWQPYF52QX9zug5Q-ph1EAc-Lcpy_tbwAe1m-XAxIwstO6rBkJd0i9_g3RCbWpB5fvzbl-ZUlLWN34Cg6PMAHEUv8mvezP8Me7K8V3i2ur4Kv6j43KSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا و بوسنی به تساوی رضایت دادند  کانادا ۱ - ۱ بوسنی  @Sportfars</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/441697" target="_blank">📅 01:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
شلیک هشدار به کشتی‌های متخلف در تنگۀ هرمز
🔹
از دقایقی پیش اهالی مسن قشم، مناطقی از سیریک و همینطور جاسک از شنیده شدن صدای انفجارهایی خبر می‌دهند.
🔹
بررسی‌های خبرنگار فارس از منابع آگاه حاکی است صداهای شنیده شده مربوط به انجام شلیک هشدار به کشتی‌های متخلف در محدودۀ تنگۀ هرمز است.
🔹
منابع استانی نیز وقوع انفجار بر اثر اصابت در این ۳ نقطه را رد می‌کنند.
🔸
در پی تعرض دو روز پیش آمریکا به بخش‌هایی از خاک ایران، قرارگاه حضرت خاتم‌الانبیا اعلام کرد هرگونه تردد از تنگۀ هرمز ممنوع و کشتی‌های متخلف مورد هدف قرار خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441696" target="_blank">📅 00:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
منابع عربی: ارتش رژیم صهیونیستی با استفاده از گلوله‌های توپخانه و بمب‌های آتش‌زا، حومۀ شهر نبطیه در جنوب لبنان را هدف حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441695" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWf9N8708OU3pZ9KZU0viTVv5ew9qp5FUu1A7mdcnmvuJN92ZpM8jfHoTAsuLGXET4LU7VXk2Eg7BgmF7vGlTSxbliWkppDlK4TL-8C_0Q-7muiUavX-GNpW1frfiFIGym4Y5WU8nQkWMwtRRROUo8ZPcZRq2Jt_pyf-N9koIFPHVO4nE_6WBHMdsLG7YhfCTvTqgQ9QvIQVIM9q-HXQRlTmP1-lKrpvc91CZuG0zktro6Q8rwuDEhkEGtnhzEvfiCfwOJQrARF3KYhvUgWy7tMoFnX_3k1XwyVtR_uWDtyosXIBd95x3oeV0YueTKf7xoBE9Cl223HSYi2FtuhtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا و بوسنی به تساوی رضایت دادند
کانادا ۱ - ۱ بوسنی
@Sportfars</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441694" target="_blank">📅 00:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تغییر شرایط ثبت‌نام حج ۱۴۰۶
🔹
نمایندۀ ولی‌فقیه در امور حج‌وزیارت: طی جلسات برگزار شده، مقرر شد ثبت‌نام حج سال آینده زودتر آغاز شود.
🔹
تأیید استطاعت جسمی و معاینات پزشکی زائران پیش از واریز وجه و ثبت‌نام نهایی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441693" target="_blank">📅 00:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/741bda4987.mp4?token=Qe6wfamvSvWrFtcloaD2UxAkSwkN9nteyH3xT_wHAid6aG1V3orL-6ZPVWGJhuL_2FNqmTAtcY9fyC_I_-s4Is5KXtUNzJGwcT3DejlaPsiuwUI1uFhDM-hNfhEaqsXaDPN1vfTxvn2REcNrWqw1-OkRccJptG4-su1MHAvA0HvGpPuhJpa2j_lADSEAeklJmq1Ao-R3sNfqHHoQvnWKj0UMApfeJpTTsCaVWk4p70ICtIQu6uGGOVqb6BcqCLE_2V4OfF0vpfQnFq-eYtQIJqWjWORgX5oUwM8GzvibL8owFOKctyHQ78xkgd-R98OHNvXew2rNGOZrURv8MD09_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/741bda4987.mp4?token=Qe6wfamvSvWrFtcloaD2UxAkSwkN9nteyH3xT_wHAid6aG1V3orL-6ZPVWGJhuL_2FNqmTAtcY9fyC_I_-s4Is5KXtUNzJGwcT3DejlaPsiuwUI1uFhDM-hNfhEaqsXaDPN1vfTxvn2REcNrWqw1-OkRccJptG4-su1MHAvA0HvGpPuhJpa2j_lADSEAeklJmq1Ao-R3sNfqHHoQvnWKj0UMApfeJpTTsCaVWk4p70ICtIQu6uGGOVqb6BcqCLE_2V4OfF0vpfQnFq-eYtQIJqWjWORgX5oUwM8GzvibL8owFOKctyHQ78xkgd-R98OHNvXew2rNGOZrURv8MD09_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای این روزهای گلزار شهدای میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441692" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhwCBqlrqd7pKxE5DavsjFArwmoW4o0Qid5KnpKMV7-R_y8srJkd-eMNcZM0-komtJttLF9eS7lwZ5EREayMbNN0HbSZllBDLt5AddPzOAdVpYGLsvuuQPLLtSyc8EbWTxVM6wZAzuVtZ3i4KRjHvv5G_3RL1C_6kl9SENOqP0452AlLbtCxcs42C6bIN_4E3vfWj3nQOG3-WAbuCTd6V7cWoHpod6VWaVS2yL_gUrzz1RYobgvdqptYubPsBtWIgMb0AYyho0MEuPb4IASi6Etxi6Q8pMQDX27x2lTkhykxNHCrIb-QqncD3Yu1KP45KR5bRQhuIrDDC70XTyc-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
امروز به‌صورت همزمان گروه‌های سرود جان‌فدای ایران، به‌طور نمادین سپر انسانی در اطراف زیرساخت‌ها تشکیل دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441691" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598f106c.mp4?token=ch326iqrLP1kwEQT_en5JLVK9fsdUNt16wB_aAafKabT4FNg9_nJ-QIy0gsBaf6Q-xKpYV2jyZRJUF8Rv_IuJ10CHmFG8FPoGreQNdHyTBgKmOknPfGoc5uDHiv1zB1n9IhEsWEH0hYWCntlZsO9xcM07kD-otGbtyZCi4NpLqLQq1fG4TnPc7sDmG_pnlAkU4O_6cCKevdbkyvWeSA7aFWbMeX2WQS2BKn2SbUYJoT-D_MpLxk0BHmrbG-9-3277lfITKF4Dnw8uzNK19sa3ndMzTc-J1a48s9DgBShyO86sR2iuR0cJ-W4v1vLMmSfJsuQts9InvyUPtyVAEhBnrNVRbEXr-WaMmeu3jcaoxSq0S0_28eC4a7Q-iT7keXFY4EtoBT8xDW-ewgTsExNUEV0d0iU5dcN1Z_V6Pr2BBoSJrjGEadNAUKeUoPeaPBY4Vw2bRNg9XwIuZDCeaqcU7W0IIJTv81sdVO4A24hM8J4he-V8KdUaXUrEqCeTDUlMXSklBIhP1iUipzuWrS86DcO5EwnzNQgdAA_FyxkMrHJARHqVz8JpY5O580sn2hPwUnkTMbT0pthsGVFIQulbYY7s9g1lNWajMR4dRbxrLxoOJcfjYxTXDsdApM2K--i2Qc5RAOGkjR5yN18yt4M9IPc8jMZ1ZMR1AWpUzSl25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598f106c.mp4?token=ch326iqrLP1kwEQT_en5JLVK9fsdUNt16wB_aAafKabT4FNg9_nJ-QIy0gsBaf6Q-xKpYV2jyZRJUF8Rv_IuJ10CHmFG8FPoGreQNdHyTBgKmOknPfGoc5uDHiv1zB1n9IhEsWEH0hYWCntlZsO9xcM07kD-otGbtyZCi4NpLqLQq1fG4TnPc7sDmG_pnlAkU4O_6cCKevdbkyvWeSA7aFWbMeX2WQS2BKn2SbUYJoT-D_MpLxk0BHmrbG-9-3277lfITKF4Dnw8uzNK19sa3ndMzTc-J1a48s9DgBShyO86sR2iuR0cJ-W4v1vLMmSfJsuQts9InvyUPtyVAEhBnrNVRbEXr-WaMmeu3jcaoxSq0S0_28eC4a7Q-iT7keXFY4EtoBT8xDW-ewgTsExNUEV0d0iU5dcN1Z_V6Pr2BBoSJrjGEadNAUKeUoPeaPBY4Vw2bRNg9XwIuZDCeaqcU7W0IIJTv81sdVO4A24hM8J4he-V8KdUaXUrEqCeTDUlMXSklBIhP1iUipzuWrS86DcO5EwnzNQgdAA_FyxkMrHJARHqVz8JpY5O580sn2hPwUnkTMbT0pthsGVFIQulbYY7s9g1lNWajMR4dRbxrLxoOJcfjYxTXDsdApM2K--i2Qc5RAOGkjR5yN18yt4M9IPc8jMZ1ZMR1AWpUzSl25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: دست به ماشه آماده دفاع از ملت ایران هستیم
🔹
سردار طلایی‌نیک در گفت‌وگو با فارس: نیروهای مسلح همانند گذشته برای ناکامی دشمن و شکست‌های پیاپی آمادگی بسیار بالایی دارند.
🔹
نیروهای مسلح تا تحقق مطالبات به حق ملت ایران و خون‌خواهی شهیدان، پرتوان‌تر از گذشته برای پیشبرد اهداف و آرمان‌های دفاعی مهیا و دست به ماشه هستند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441690" target="_blank">📅 23:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
ارتش اسرائیل: پهپاد انتحاری حزب‌الله به مقر نظامی ما در مرز لبنان برخورد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441689" target="_blank">📅 23:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6b06f1f8.mp4?token=JzX2EggXdEUv6y0IOg2bYLxUPvqHcMHnHKE6PhaoVO3DYLD-t9VyDoxTvB0Na6ghQzoWWYa4BE193Nvi78bsTS4-RKRFvk7P3Pp5PD0tb5Hjff0CFiOxm19Up-HfOZiu13NZS6PW92hCNxt8IPbmKQCNUqBkNePOBfEBs5P6KoOvCzi1JgKB-EybxdH0ty6KRA9sEVhP_Yf1nmcSbPf3ZIrGZ4aIuGsqGLqtAeK8i4xENv8lKHGufzm-vaXGZrC9HAZP4XQ7Idrwhxql5HcYfkxaPsNf7MCiN9FqdL0nGaLQuHWb3ykAVmMNju3qal_5IT-417NcQzS9yX357lP-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6b06f1f8.mp4?token=JzX2EggXdEUv6y0IOg2bYLxUPvqHcMHnHKE6PhaoVO3DYLD-t9VyDoxTvB0Na6ghQzoWWYa4BE193Nvi78bsTS4-RKRFvk7P3Pp5PD0tb5Hjff0CFiOxm19Up-HfOZiu13NZS6PW92hCNxt8IPbmKQCNUqBkNePOBfEBs5P6KoOvCzi1JgKB-EybxdH0ty6KRA9sEVhP_Yf1nmcSbPf3ZIrGZ4aIuGsqGLqtAeK8i4xENv8lKHGufzm-vaXGZrC9HAZP4XQ7Idrwhxql5HcYfkxaPsNf7MCiN9FqdL0nGaLQuHWb3ykAVmMNju3qal_5IT-417NcQzS9yX357lP-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین الله اکبر در قرار امشب مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441688" target="_blank">📅 23:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KpLcBUc5ka9az3_wAqXoUGY-SYQFrzebBNYFC8nbr92WyjvS1Vg10GerOCsfRsrmTBbOv0kB9Jm2WBfBDjHkxA0JfZxX1rn2dTO0Luidvk0vqwopT5o8dk4iJVa6-CofptvOQrzwI8JwP7rihSMaTa_tEhW8qcLWE0Xykn61AKfIx_TcGS2XXnEQRwfn8tGXfQsATZIdiGd_xwULX4a5s2ki5uz6jFpa4fSPvBGZZ_YiYsnTcGFuc_cmlibv2dq7OCHO82vxarn4eKcg1xS2DKDBUMoUK_CC4IXUqi4dvPdB2XOPALO9lRo1tfUBTz3XFNmYlikLFAo15AfWlUKRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfK2cC9pIWVThKgLK9GqXRbZwTphen-q2vHFfhjBqFvsI_GazqVHADfKK9psUGHLC4Iut2aORHOa2srPabt_Zy5vBNhnV-8s-m-feUhDq_Gx2lcfodqCm-hQZB2bU-JBXWUi2P282p_dw1l9p6fZQlZUjF9v1l12jUQXhq6DDIbw_otPN-an5fQ5wxN251Ptrn9Jj37gBK1a2HCS08qsYXzc8MaX8ah19dLVpT2kCYDotI_txPnND5muwHf9ECUpxvEXtwg40GEgbLm0_v9fYZ_kMdGFjFJ9Mh7hI46Tjlmk4yyxUxZ3Bqv7J93R81fYWHsGZxOWtZ1ZKzhNjSb1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoDvQGBnc1pHy7qLUVCf78I1FK0F-NzPPbgvZNS7OHrsh8ZbCmPpaswU8VheXw1lMSBAn_1Mb3o5_cDm5gtpvXadhKxx3lsXl2MUTHpEN-vPSQANpuYcMH4jor5mYLumKDGhxqE-4TY2rw50Ua8dHZcseN-mcgPEG3bgrTvpjwsqJr6EoAEjkSDTrGuzTmXYa0rexoaumqaUyzYeKKUZt9kaEaNtvXI9sT8QIfxPtxxwvnlJZsu6uKonwffIvfd2nbz7eY6Xiq-7vWI--GVq8EkXdFEvlO5-ddyKAxtzxYff4rZfB8YxAwPqpTvaA1ZAPgD8xz86u2x0YNn9zGTQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G25JcnN_3TVcC_5k2Gd8OHxYUzkBrVuwzA-qneH8rP8EfMWN5E8_547yTQT3cPkG8NXKAnmIhRsBUqCUA2lY5-DhRfwQxKWzw5U-6IyCzyV1D9RIjkClDeHcAXm0OZVVUWG0wX3RCpcmHb9EF9YIGWS0f5AkZvGyUMXw3XPeiBeoDhZ11FwR56Uq01xgV8M5uWNCzV6TTQsoVbNwFNZI8rw9JbK0T3bahaVhJSa2t_tOJy7iKHYR3ApaX6c8V-Rl-Y3-MqMRp14k9sGJRK0HZwnISZ_C_31woi5S483gfJEs9Fm2Ra2OqxJ0Qeb2Qheo8v8KHDhdIUAhio0_TiB1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eaGXBQn5P5K8VAZzk_afQ6A5enJTYhnrpGESPcxes2YjP-dpOjyOwihqarVUZhVzSkgIvXEQmaeSQpyJOxCjiXbFGq7cq6sXSzNrzwA1G4OTOTud_gJ8l62-E8Z52YvVFq3MUY9QcJ1NTxqYkmH6hSqBh4ZeW0TfvSQfRzFT21zFr90YeN80ESo7HwYaHJ7-SBvvrCTLJzgWSKnvSlqOV2erkcrnw26iIXvAw17u0PLOZ_oPOlLyTXN5fIwHOcCaHBlEOO5PxVX6kiQ5WoNjJ7D5dzNeOgFUmiTJR7ZEWiBctOPtYYDYPxxMXbQoE6NRVgcngDbDr5J0JKuJ2eRbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N30Rz2kJjcpPK3qLLTrJrCOiF_5hxyCYE1Y8SB-6sYMPsBQh70fFgBla-RP2UiiFhFjNDPM926V0hNa6dwdbwoKqG6SfsMS0veP_ioGTympEEit-2fjIEAxrMExqax-zE8Y86zY84XHGWptC_HLq3T-AzGS1ExsdevXcjS4coRDJ2nBM4RYSemVS_ia7d5BXxd4yI2Xn5WWjNBF4qYD3EIoU3jHkkXFYbzr-4u-fPhQ_TZxd9vzF9ekeeZ9wlrTP4efMmRICz16FYxFwyvuOQ94hYYcVj8WOhliwY5hyv-U1xwqdkYjtLKUg9q6snoVPajRVmME0lTh1Sn0zLctMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp2vrHZ35wc7A201QjtprNqIn9z4gAzTUGUgsA1zv9Ad_Ers3FAdI3v1o-Deq-_SEsK2Vu4aYMF5rkK4zTIb-fzL83GQH_qRT3L-nGLTHKEYiXAhCTGQTn2SRG_cueCGQVqY6YQrm3YvoVUuGoNLgyP3Xjp9LtVeJarqtOZjmFv81KDQ2Rqk38qjdmZpSf9sCa27c4npe9pclbz5HybG8fuDBGWQoauCBe7mUmvkGa4zXPOyHDhuLP-hMiUYYcizMwPFm5wngqP13JYfG7BkeOzprJlrsu8Lt4muvHuZGuvIjJ-2skezCLTiJUy-_HMakS89S4CiSPiYwutU3FX7gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ برگزاری مجلس ترحیم آیت‌الله فیاض، امشب از طرف رهبر انقلاب در قم
🔹
مجلس ترحیم مرجع عالی‌قدر آیت‌الله حاج شیخ اسحاق فیاض، جمعه ۲۲ خرداد بعد از نماز مغرب و عشاء از طرف رهبر معظم انقلاب در شبستان امام خمینی(ره) حرم حضرت معصومه سلام‎الله‌علیها برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441681" target="_blank">📅 23:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
عراقچی: یکی از مقامات آمریکایی به‌تازگی گفته که ما تازه فهمیده‌ایم که ایرانی‌ها با بقیه فرق دارند. @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441680" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
عراقچی: علت جنگ این بود که ما در مذاکرات از منافع‌ ملی‌مان کوتاه نیامدیم و مقاومت کردیم
🔹
دشمن آنچه که در جنگ به‌دست نیاورده را در مذاکره به‌دست نخواهد آورد. @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441679" target="_blank">📅 23:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌ ‌
🔴
عراقچی: فکر می‌کنم نتیجهٔ تفاهم برای منافع ملی ایران خوب باشد و دستاوردهای میدانی را تثبیت کند. @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441678" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمهٔ آن بارها بالاوپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را اجرا کرده است. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441677" target="_blank">📅 23:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
عراقچی: شورای‌عالی امنیت ملی اشراف کامل بر مذاکرات دارد و در مورد بندبند آن بحث می‌کند و تصمیم نهایی را می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441676" target="_blank">📅 23:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
عراقچی: در مذاکرات ۶۰ روزه چند حالت رخ می‌دهد
🔸
۱. تمدید مهلت مذاکرات در صورت خوب‌پیش‌رفتن مذاکرات.
🔸
۲. نرسیدن به توافق، به‌علت بی‌فایده‌بودن مذاکره‌.
🔹
بستگی به شرایط آن موقع تصمیم می‌گیریم که اگر نتیجه نگیریم چه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441675" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
عراقچی: در مرحلهٔ دوم مذاکرات، بحث رفع تحریم‌ها، غنی‌سازی و تعیین‌تکلیف ذخایر مواد غنی‌شده و سازوکار صندوق بازسازی ایران بحث خواهد شد
🔹
از نظر ما تنها شیوهٔ بررسی مواد غنی‌شده، رقیق‌سازی آن در داخل ایران است. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441674" target="_blank">📅 23:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
عراقچی: محاصره به‌طور کامل رفع و دارایی‌های بلوکه‌شدهٔ ما آزاد خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441673" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
عراقچی: اگر دشمن بخواهد ادعای دریافت غرامتش را عملی کند ما برخورد خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441672" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
