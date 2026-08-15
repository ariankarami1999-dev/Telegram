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
<img src="https://cdn1.telesco.pe/file/KX0vzHgzK93zAOZQFHggn1j83XIK3-YbSRYOr9_3Kg--LFAlvQiu0pozo1IUJ_zbiwLrJLwSODycToMuyQT8knprX3Gy2bvx3BN_rU_h5-ApJw98ZntarTFQbOv_7oITlR35l7XWDGEUeXTPbG6je19im_fDAMWOgK1L8FnrflhKWn2VFtgOK2xLviYwGxARR-kgDK6LLnCkDrujZ9IYS9OzieXU8MeIBhJMVMyTbNCeECYAXGS3W2--uz7zeyJHi_L-Y-mDE3TTDLvQS5vBj6quZl8FDZj6-O6SthkZg6Kh_GjSFqVMJ8u8i5whRGENtnH02vOjP3JDOjik98cA-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 09:17:54</div>
<hr>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=Gb5mGW52MA4xxvlM6ePzEL0NqezHFhZhVoVa5NEuccsV3y-iFPTI8_HsEuJug6i15ssjpRTlIBDNsZ2QG6hMuDG0JH3v6IyANvXDBGjh4-Iy_1kbEroi_0CGsO8RJBvVujpRJA_x2uMCxBOvabz6steNxZKLRMkFv3MlI-86p3QN2YTbf2k4a2THgjhmeuuEebWWbGaiv0QdBEO84ZK2aq-DSDAfLtYcrn6npgDJ4q3I6BKQz3iSRiTBOaNaQTX-lvcWUg3mlD36Lt2D0p7IbefVy014KFTEmNMY_IQtoRjstXy0A3zMmW-vbnGKur5ojkRMZuDGtmRxxOkdpgAjDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=Gb5mGW52MA4xxvlM6ePzEL0NqezHFhZhVoVa5NEuccsV3y-iFPTI8_HsEuJug6i15ssjpRTlIBDNsZ2QG6hMuDG0JH3v6IyANvXDBGjh4-Iy_1kbEroi_0CGsO8RJBvVujpRJA_x2uMCxBOvabz6steNxZKLRMkFv3MlI-86p3QN2YTbf2k4a2THgjhmeuuEebWWbGaiv0QdBEO84ZK2aq-DSDAfLtYcrn6npgDJ4q3I6BKQz3iSRiTBOaNaQTX-lvcWUg3mlD36Lt2D0p7IbefVy014KFTEmNMY_IQtoRjstXy0A3zMmW-vbnGKur5ojkRMZuDGtmRxxOkdpgAjDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=bWwyzPv8-DTrKcT33_-wHZYbDo9hN0OwtFP0RLBruZ_fzM8szIaO11nbFK-q_ygcr-rH7fDEixUBfSSnXnE0XQCYw5JlUaBXgKYZrQwCWb95vK0mCanSTalzjW3CR6RHVp5KpgdlHLuZNsa79Epyr73fOmRebeRrXU2m3RUK4ugPISReuZ93pIgT_XLyMMxaXcVtwcsebK5Yg7e-mupqxnRud1wpMprAY3Tc4kGWs4KUf95dJdg3ZzX7kShp1mg3np01eed8yl3-Xw9VXMkSn2R07gz82ac6TWpTa9FPTtvl-WiSlLfOlkwadkGmDvWEw7pj1jOeBeJv8kevE8AfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=bWwyzPv8-DTrKcT33_-wHZYbDo9hN0OwtFP0RLBruZ_fzM8szIaO11nbFK-q_ygcr-rH7fDEixUBfSSnXnE0XQCYw5JlUaBXgKYZrQwCWb95vK0mCanSTalzjW3CR6RHVp5KpgdlHLuZNsa79Epyr73fOmRebeRrXU2m3RUK4ugPISReuZ93pIgT_XLyMMxaXcVtwcsebK5Yg7e-mupqxnRud1wpMprAY3Tc4kGWs4KUf95dJdg3ZzX7kShp1mg3np01eed8yl3-Xw9VXMkSn2R07gz82ac6TWpTa9FPTtvl-WiSlLfOlkwadkGmDvWEw7pj1jOeBeJv8kevE8AfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=L5hLS0CAzS11U5hQjat0M3TwdgP1Oe8UZfxnRL__JB0wzPLXp4FoDOLqK083PZYEH0EPOCeIrGVOgqG2-TCRSkDP4qjdQvJiOqHbDlevf6pP3PgRFQz0oBxBiyV4xV6Dc3JceXQNGi3YFB4kOJC_7SBNH2j1daxXELFHztDg7-npFlY6T3CsR6sTww693YNLkvo8XSqgSBJ-0O2N9ssMEVnDHWVwxw44cv-HLDPcWdHrfBdA-UZm82T2BBZOceisQMvzXq6DKCwXP9fXEJE5WVZCn5H1hLqFomo4GDnablBqhTk2KhW-0kyk15USDEDyXq-gRUdze4ziAk83igqtQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=L5hLS0CAzS11U5hQjat0M3TwdgP1Oe8UZfxnRL__JB0wzPLXp4FoDOLqK083PZYEH0EPOCeIrGVOgqG2-TCRSkDP4qjdQvJiOqHbDlevf6pP3PgRFQz0oBxBiyV4xV6Dc3JceXQNGi3YFB4kOJC_7SBNH2j1daxXELFHztDg7-npFlY6T3CsR6sTww693YNLkvo8XSqgSBJ-0O2N9ssMEVnDHWVwxw44cv-HLDPcWdHrfBdA-UZm82T2BBZOceisQMvzXq6DKCwXP9fXEJE5WVZCn5H1hLqFomo4GDnablBqhTk2KhW-0kyk15USDEDyXq-gRUdze4ziAk83igqtQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m13rwHChHndWPvbsTBeODKRKdXzhWScfcz7lsSVPA_-D_Ws1FZVXqbMVKOkjzkb5P9NHKKLsmkaGzPFjudzCMmevKyJGjCpFT9UB_nC90VLdXZweeh7fd1VAqhpvJE67iI6J99M6srYYdtbUWPsFlIMwk8A0uKk7JY0y-5FhRSPegrsySbYX1zOLHxt_ufvG00upiBE0pu6lMvyewvfv6ncFPuu2fJtkSqYTGkOqwoCZQMRQfbjcfapqY-KQETjj_zqBqvcqSt5sgQovP5hs5YKMP0PRdSd-U6TW7c1602nqvILFOo5KVxgvRGKrtMAbNe4I6endLI1b8ldP03lYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PV_snfaqvZkhTVU-OvqV4QU3YFWmKAHHLziNukLvQF-EcXx-c3o4D4I5mcBq3EdvXRWh2ghVwPUWRuOvEWkVIxLl0MEjOE9vsRMmSFmmMD6-n7bFZrwQw4ePF9kw7CPZ2C_DDxi-q-z3j39GJf_TYMN9Z-_-2sp3_fALTquUrA9RV52WwGXUdT8W-5XFCBMP7jNmO4ofUb0_bmOPaLihDM7470CVHP5djGkGpa1vUBVisK3NmDp2hjMnuISphGhyEcTNF-ikeirkvDHRvpkCrbpuVvvL7fc7frLPElK-ek3Yv-jPW_SVea_thcs6qDUbUcYOB-IkgTpbXdnLzsWUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=K_tNqpHdGh5y0qfRTda9afklWbB7vgiQjFY4wKzcK6j0kffDSZ9ZD9JxQ25y2RMX_y9CNuNwbtnCvgIWpDs0VycquJ2HXE3LZtCWnIgs5iHjcAP16kQYpqqAJsbOu3kvDOCOj1YY_02-or6VkUr5d357rDjsbEsHX6gfIQC_EFfw9Ztw45gz2RMv-uyCDzehriwVEjmmVuULaVHF0563Dn3WFWUH4L-UtBjH0UNvQS-FUiNNKf0xrduiakjf0C9Adsga-UucLVHw7JI5_AQRtfa2kvLHFlVxynjNwY0dHTE0610CeNmNgr2HkLfotv2OiqVHRCucOJmYx9_AY08U6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=K_tNqpHdGh5y0qfRTda9afklWbB7vgiQjFY4wKzcK6j0kffDSZ9ZD9JxQ25y2RMX_y9CNuNwbtnCvgIWpDs0VycquJ2HXE3LZtCWnIgs5iHjcAP16kQYpqqAJsbOu3kvDOCOj1YY_02-or6VkUr5d357rDjsbEsHX6gfIQC_EFfw9Ztw45gz2RMv-uyCDzehriwVEjmmVuULaVHF0563Dn3WFWUH4L-UtBjH0UNvQS-FUiNNKf0xrduiakjf0C9Adsga-UucLVHw7JI5_AQRtfa2kvLHFlVxynjNwY0dHTE0610CeNmNgr2HkLfotv2OiqVHRCucOJmYx9_AY08U6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YKLVIHMyBjCn350dFTBLR1zhy5lukzN1VM6IXRtKOYc-0fCYXZRt0bX1x-BK7m90LvPyAgbxAD8mAMxx_zz8c3FmsKZLTS-gjcnCos1MFSc4dmoUJO8ZFww-DdkQEDdfSC-Z5XGxphubIixltn5Sz_vmuTGZP8lDv4v-VjjWiNv6kq-9bweENx16OzC3FL_NYMqlAHhjq_TllAOb4D6-X-UKppNlA_jfbCPGpzfvDdzo-pYzBCKrFiwNueA7dfa13hqZhaMF3qxkgGNXheVFy-Z7ipelWuWRhOnrvbDuQfNNpi1DlMjayHYjLQUR2iHsr_Hk0ev84WVO16Ef10rGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RmYi4w6WfSOp1WS1g9oYrQtAHDymO4DEgRZZnYckc0lRgdg6Ce_ef71fBeuW7a_RZ2zQc-Y5wrEIBywPnX2IQ5FfKlSk8ysTsYa2lWDD-tff38-bNqsj4Xpl0UGT6s57S6YkRTj1LpooQ8BP1PbClIzV8A5RlXdyFm7ZEYCW1gjeBk4MBaD-zRjymZuGbvw7Qb0_mS9KB9S3Vj7WY5TM1n541Ti4FVLX523OchA4NykQKrhYt244O82-ylLE4F5ocGAX9quaMOEK8YvD-u8t4o0qDf46unrT45GuTjARS3QNcrDfTc8bXiTAHLaeFeUUfpvUz_0aUDQ4lnYjl5ubkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TekeoN2T7SA1jQCfdo7qMutiUSZ0ergc40vR23XRmNb3oG0jp-9WsJcjj1FUbFadLCAWZzfFmZ3kKKYdWwg3KC-0hygmIOHxHRjW2x1Gj_jtVqsoYFMx3hi2jg_4iD14J7pJfp4p_STz32HNaiuL8OlugeDLxveVqecnHwriKuzdcC63ZwynLHwSGtth4ZFAAHkF1Pk_K4xoUwFpUffLJTo48kr_CraQ57PkFX7GYTDqb9NJKrSLbl45SD_8yx-k3ZPKwMnmhi-kDU11of4ODpU9uJ2Vy2p0t4wsDEZPKnoMbGGQ6VR2bQx_ZoW_ROZuqyJ0D48pixmhS-YawwQXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYimo9sX7Py2Mpd2kb0VUSX6d1BkxAbi-u1qijSVBX5YfaZ-r0ye7p9TtKbdnwg8yVQef-C4ZgJtxP_0DvfMqR8Cr3V6rEskKaguXxNlzokriSejtN30_FZvdlCb9y16TPh21kN1FOPif33gdDeIM1Z_HtoeA5VSCI1Akc34RX6sRKXaBIq0aR0HuvKQrO3E6r6rUN55jT5EqxS507XQXTSuKGerULIyPPM0n577gu1EBaMx2lAkQwsYLaSlhBb8Kq3homvk2nIpLGZgX8kSCW1YVr2jAmoETX4W99KW1B1Xg84pMRtP53tn0wC8ODmS0dTQHkQGvBFjtWNKxBwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibL_UKHDnP-QE57nWA3Q2ghdHvAqd9fvsJ7UzYX6Fi9L3cHVcgIDo5mTEa35nMPEpZ0Ji4Sz4-kcrG_ucw7bgazkY4J_y_pNCWNvRz8TUgoEzmECuKP5Ozstd7P1wfVac97i_4BveSocR07LawKmWL1KqtvdRkcBtBBTm50ksRXkPaHC9RwoTjrriNrNXdm2I3PAzv-uzogOOO2f3JhEZNffOpQNP68PdwsGThUUEeIzfY5y3_mXCkzubSXh8gHWWo4gWwXXyYwcQbRyaItT3w1YcXlYtnMwSK26QyOuQYXlHMTv5TVhyJtaXn5xy0iBZngfvfOWj6NYDd9ugHdwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P0gpC3jrZI7gAChTB-B4R5CN5bLoo039O1n2_I-ylm2fzQsOp_VRaGGjtnBjBX2Rg5hV5yztI0Y6DUsCG_Ywxf1O0tSDRJsTBy2hxUYDk_gTps8MigKCw4ILAlJ792OYf_JwaSdgbiB08bRiJbXz5BAfoQnp7chyQU3cIUIeoj1pFEpI55tqU5aedkPLWRz1owgqtZ6YseI-P1Y-jnGRB9mN212SE9hrxnoLo44yTeDlfgKbBnXmnLFnhEbUQ4WDVMFzUDmIprc1YrbXqUsW89S5qX6HdsZa9kO0CTnXBsjDK6AeMuaC31S1hFCaIHK3RvmEu76gaP8kww4KdfoQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jr2uGoye05-ELsWrFy3GVSL5VCqHkd7mgej0-CRchNvm7thyWiCFRbmz98KKkkwBXk3KP8L3l8z1JToMj-5JQ6nwbCdfWF-UQWCGZfRrqIURD7bRtZv2aE3MLH3Rm3dpy09t58NAmTpTEHc-fYX9VYLAWdIQT0aKCjjTIucJPvWON5k-r9aBhQvfiQIQ_8QIU0kVmv3sD0pBDDlj1r1XJEukyfznC0mif2hR9J0HjmmTPYyTw9ueRMTgFiwbcbDDyMGJagVEDsy4llRhi7ARlXkbnzTV__8nNyg0M42c_pdragZPBamVizw_D9aT2rsn6F3-35aF7gRit5VYPxTP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/trF-HncNgZsFDBL0fjwjQ_hx7KgSVWPNmt-vw_EYnXzybS0LTabznE3sQLffS7VDmKQKit1e3zt19U-AtysKJy607YWhqCxZh8au99-_L2wes26FV5QgMU9YFS4mrln5FH3LFp82PF7vV_MK9mqm4LAUXzJvffd-5-CNuvwWm3DhPwx5Qvg8hQQ21XTLdFRk9r93Plxr18u4Gxya74NCMQC8nHlBan2OXJ1eyZSYf9OZMwzgi0LGCPAfBhEEvthalNKhczw3S8IqVqk7W0AZWmUMyxc-5nLihQiyVrGYgEjdIAdFCPFWwN54hG3mE59iYeGIG3B1f3Ew75I1506QTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/khZp3cM3lZXS0GyJQTibgBVNHAsE32Bo0SKcckAuM8c3Cx9AN_Uh3mcvyJpPRGWnfmo5Z9U4iviqbpK-M6Bny3LjuiX7tF36XaPW9y5li7mn9j-svYc_DAWrHdsZSkdb-3-sXrcOX4bKSqEidzMd63JQTmLtuGRWGXOzQvRUASGWnb4GMGoC7u3frB70D1b13OPcxgviRZBgetfSyG_3DXYzZS7OXsFeGEIfbB5R_OekZ1CYb_2a8oc59yu91R6A0Z91K3pCHm4OrWnOCsGrCZa0N2f-ZZdzH0zHhGT-AvzpbwaIWudfAmBwfkXloFyQ4ylGeE6QWar4dLUmhIBNAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TSuMFtJC2Ss4uFivLoO4yo7WHdyxVtcTwqCuoS4WArFiHakmMcxp8QTfy7lOiqi2bpCUTLinBAu3bzRJNd3t-1MVV_0FlVJK1BSGEKjoQ3PTODN51YrOjcQ8zzp4ZyrqkEYS895IzaZIO5jn939G0YUe0HUJ8WUnoEVWeUhpICCrtuEEF8vQcioyAqd-ERaFL537TypNqGE-dMgN1U7VGdoKmiyr5KF8hPea9xXw4QY6PRwHVoNyAUWN4Ma9wtwViVYc-6Ohm5Qx4TDc1jMaewmMfEFwLI-HU6pkVADFeBpavs2QwvjgP3k-J94ST50Jygm0vmGka9uLRdq7bKdvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=WVC97LPbe4JhSlTxxF-EymKIT8IAiIMYbuMu5R5XD61dZA7rigrO1nbf8ak2WKO7N-toc-V5Vr_UEVeQQ73YxBAkjxC6pmiL-pAVAVN76HKjpt6TRRpua43A17OLc6uQo5ZENYF5dAQwylCWzS3CELlGzR4ZsRZWC8mQ0FWdY874Pc5dM6uPVXuYQkCvcV0Dq_U46vjq4Wz2fpOWJLVkhfzVs7NhuEpqvdnIuBAN9eoIvESXFPgWfL7bLgMrQ4ioWHFe7EGQJHXJUiCGra0FAe0EAvMe1H_c5ebIYbcFHthJ5QiBcfPQih1czSEsFWL4fW1tgnTJqMpE2QMHU4GTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=WVC97LPbe4JhSlTxxF-EymKIT8IAiIMYbuMu5R5XD61dZA7rigrO1nbf8ak2WKO7N-toc-V5Vr_UEVeQQ73YxBAkjxC6pmiL-pAVAVN76HKjpt6TRRpua43A17OLc6uQo5ZENYF5dAQwylCWzS3CELlGzR4ZsRZWC8mQ0FWdY874Pc5dM6uPVXuYQkCvcV0Dq_U46vjq4Wz2fpOWJLVkhfzVs7NhuEpqvdnIuBAN9eoIvESXFPgWfL7bLgMrQ4ioWHFe7EGQJHXJUiCGra0FAe0EAvMe1H_c5ebIYbcFHthJ5QiBcfPQih1czSEsFWL4fW1tgnTJqMpE2QMHU4GTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAXaO4UCYnbh5uQFg8UIBP4FdBlQ8BS45jxUoCffapgfo_p94QysTLVEwst5QgywSRwDfY6J3-T9892_SU1c3VcFFyImYg0u2TXYtmPPMmlyRVDI_3q-iHHNMLg15nxIAgVbCW2Uxmfj8E2i-ID2IuxvJhg0TRFc5sv-u98Gi-H82l9-fOK2AnzikW5B6zitawXa-ce-Nxm461OthExLfE8gKpA9XtedMFlHr517xzJt52TuS2OWycrbqD1ZAq23ZZiUKtX6WIWDQxZgsGRpod85aeZV0pINwTCHDP0-gS6uSfEfJ0Rf4e3lqpPGyvOwgeT6q-bYL0vJ35QeX_ugyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PmxL9JdbI-Cgt2qa820lFUb7yqcOxKPq4zuUNegYHqCRKYc3cxeqA7vXaFNT5WpFlwSKqUscoGuUm8CUUEeRzfXDJ0pUwmjKWYeMPXrGuouIh0u_d5Fsy-MOe67Vo8gjWmRCniJrjHIcqj2m4xD1WyoucN8IRqg5tl2TpMQ3h5bUj82JDyeUSFBYsjTTcfIuG8CQlLxiw5EbPNhokgkBAYezZadaJLlC19qwpOVTgAn1S8CM5VCTbu0nX0BIJqHUH7Ysa7HCWrUOHst2DDynHeuulTYemG7hzL8RdMOf7C4dG2VA_1_hXefNe2OvC9KuFAeDMJ1a7pMLCeRWNVKzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQyy2gnVIlhsJqNdEyqeMIhORFMMED9brAkCtQE7oF3in4FFm1H7vpx9rBtW5JsqLH3BaxhLxSR8wJu8wIr6VYv1UAgmkNIV0pu1yqdJnabrIQPaPTghYp25uca-O2HCd-zCUtNGiX7l1k0T24t_ZmunQWgx0Cvp0GzrvnCrc5QSwIU0YBrjYcLO8eewPBVC0jKiaoEo7l6GW8JueAK2fjV5Qh0vLX1Lg3anDsTVM6gASUR-IFD7QjgsRVWpk92r3HmvMiiM6zu_ZyLovWBSQRYwqYspsRMDViDdrk9wNFiGp4IwY8-ePootEK5J5tJBR8OtAWceAU7ey53It-rzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N9E8kXo27yCBah_bDE_81rgCkV0R9aexm9beNGnqB2ioM_hUHl_YO0I4PosKPpRWVu3edSsJHISeWpZc0FEHZgObJpRpSLJB80LnpVHfgpi5sB70G8JsW53se1w9tCS50asv867bhVKvJAegzvO214Zf2EMhkBbAFeNVDAHrxOzX-fmeZuYvuQFU38qAUqYSQU-8VFHbYZbcu-udEcR5U5dGNXMVxGdWnd-0JnA9eUNkn0gwIBVSRZpE_STFSKkz6iq-NpNJt17spzUupEn4c5-0gWzXHS3akM0IFahum0cZkqTwdwk6bYOreQO_jbdPyQufuavAYp1mZ4Yk13NUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ETfAPjdPXfCGH2hoNGdJLPgTI_FCt6Yc_vgJEkkhghzx89EpqrGy-bVyyHJbKbZfMlogbXO8IpvsMLFgZOj9II1i8OiNZo9AkpbN9vCkpWoS-nKXPnPMnl8vPY4ie9QlbJF3-bSG_2c9KThnX335AevMuWHJjE49EUyhyKv7w3S9wIE-qyaYxWNrqUF4u3osDtQI3JRRYD5jftESC4qVi-e-9R4VUKmaU6k6ug7Iv7KAc1qkVAoQw07Oxtr9ta-MLc-dU9_oVNv-LRlZSyJR2m8WJmjBQqlVCBIY4ZCNAWfVv11zMHYJbuXk-xe0AxYarhmqQ8SeuSRbKuAsZB9_CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2e409gbADkr9CCaQ1dn_c92h4nrdrp_uyX6boWoAI9c-ijveAnCl8VeMW5_PYV3JkY0M2qiU04IfTqLqiBges1XOkEqyFjtdgdV4yH5qLTWa-dq0uHFKPGCAZXCFAtF8gzdyw7Gg7AZccxk4_iczK-3GI5zen-onu3ET-SQBNmm-eIkLdYJfEgkIsoR0Qtumv5ga5sXS3kLKgFth3g2CnmIcMb1cVPvGX_OP_lzM4QjBMWXy7oNXt3fptYva-wewQoR2ku0B6P_zpQtqsLHnbOOAuxUntumjZTu6km9FIWE2AfRP0IPMvdwW4ghSAlAc4DaTbimqnfrTUjsL_Se9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqfxyqhQsHgwxhiwXU1rvigGkQ-TUWXKocq6UfjU0fHKOMgxYbjVGNvyU89NYbS0MvqMB0Hi1X9v8Vwxb2uNjzKSvAq7Xyi_aFcx36TyKmxVK-cre1pA5zAmkRVMtT7iNrf3ZfvAKlqdCoDXW7HtAIBtQQEPM07RrruDgdXGghas7mZ-6jb-ILvDlEyKzvtsExjJmWh8Mlo_AAiRSqud2VTpg3GpLr2IG8EWidjJmEPrWpiptWXO5L6GZvHuUs6UuNEn8FgQt1a4gqiQqUq7-m_098vSwmmWUCVZwB_eBi8zOjPuK9gQ3aTxax50lAI6PnRftGijnApD3_yyTuVe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyHUHotYKZjNJtJAj_AS-lku66uql0MC6dlP3ueelAWxh4NTRnBuqGBLalnNLTsrk_4CWpMF7SYXijyOxFHQ3AYEQKMnRZD1_napNJ-VjHISIokVKWjnr6UQX5GHp_xfYCkIYysUhxiz3kVJftbe-bOfDRXfKIrd9gPZD0drA09feK7EJTX34GuSGNAbo438XZvarIJzC3zLbebfeBA9bVyIarGbzPgr36vClrfElgEvyc2OlEph3NREK-7kCmHxE-J6hVAXgrwe7fDp-SvaJdK1MvzpncqXomUrRkyh8T4PMmRyt7_FAAPVu-UXtlQVp9tgDzxvtx6za5PqlyIzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7u0oZHhOAM9oAUdgMN7ZHJCzufQgut-uAWtpSwNvr7dw9YF6EFurTOvo5ndixN_8PNR0SLT0_2afa7P9TxsqllvpEmwxwK4UUnupvTi9zaYZpijhgoZ6DreWoIZUWPEh8f9mz5FdbH_N4_bDf0cXHuc8Nr6ZoTfx4xgGXzpmN2D2yFKvnXKjQ8utKETSglXKYEgL3BRoMLKZKC89uYjoBNBQ2WTdXiR7800Wgk9xMss4yECKkCE3spEj5MhVJoT-LUnSTsRWCzaMVlMPSxhms_g3fd9D8RCNjfoluV0OPZCnOBdkdI1SL62WWXqq5brFKYv1siQJaIWPErIL2aTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GT7A55zjkjY8xpJGqRMOlTaJDZpYCRmB0TvyNQR4gUae2YI94dctDvyEk7-NxI2Fz-xMwi9UVkeW9zBR8JtTYbqGXzlVM6mIpGVB_66iefJIKFKB0VfGT_J4lOxw1_Z3WZDWUI_ytTrA-ANX26XYFosSCnVjCt91EzYEKcU9Uu56c-rsjcvQUxVQGyAgQhQ9LYzW-xWWOAXVXiH2ZugNQef-8MuySUrWYklL-ce0-UqwLI0ILE4xAlZxkKwBeoZu4e5p5DIKBMMFFfLLqq8BnomQ_0EXcdN8qgcHbN-1vJFITYbRnplcGs70Q06trqGteDbx9ChVKfk9ciN2t4ZV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7OisA-WvzXaNK3jt5_G7ofiHVz0d35delaCbR4oMXkMBrAszaJOfDJ_Tj2Rvt1ImFVQpvkp7-ZL-3811CUQGH-6cAtzYZuyq4uqlo1sfsOPb335zYODROGEA4soTqAG15pHXvLjHegJ_ZzovtiXT_TBJ4b3WNXivzF8xBqLm-r7lRt_RVHs8tLxplR241L9Kn6ZZjm56kzKmAPz0ZaQrWt4YdTgtum_mRRaGcilGvgegWqvuupNDe9eBZVyPZGSHJcyvEsMQCLgx_bEhM01ciZXeLKMiNffjfktcj7CoU3oBFU3rhP42Cw-_q5XZSREOFqtjPecMEoe7zVm9YG1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcbT36tbJJPZujMxJ4EgCsXqbmnl8sx2byLoQB7AU1HN6Q_NRFPtkiYzPhyaVn77UKPFlOcsdx3GJxHrUFMbZYTOUZ3noWHm76zZCaPACAbgJCuUS5ZUy7qgrKhB7OhldCOp_17X6pWJBIbyg7bpeKLI_SU77Hj1LDVIzroX_CGIDUHAhZhLAy2mQO6Hxp11lqggCKmvj94jOU3-58WKnV-62Y6SOzdH70gUCMnFNeNc6hfSxwWQA6TAG1CJyoB5-ISivy2vwYemgyI82azwSMtXX-EalVmou_e98lyeqSozd-pmBaralUt7v7jdOGwkHa6XfXl2fc-CBQmbCGBbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ounO0JPhKD4VifoDYUrQY38VxHx_wZ4vv9Svs4q_xoGT2nnPBSR8ttrR28oRJ73cmI1C76264q1IW3fydCar1_2jXEJe3ijAHkK6QDS4teEODJ326S4a43T-o7JHqBcRUXOiaDDVY0UoVWV724UEmQHqVs8TEf_2JszpG6u3x-U0YJ2FjN7h0Nqb_v6foeNExTBNG6sL3vdkmZw8e7F4IzgEeqnweUNNWnT86TYJU2_MMMYEBnyI8Bl0l79JvJSb1gC46dKxk4tdM8Regov2ZRsum26scfxeqAJEVY5Lb6d6fnE4X9rsFNf3tHfMZ_j422CEH7mb5wZHdxhDPYSTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7DRbo8bFhKomLoh0-gBpsa7xxEjCxo9vGJ50n6P1bLLnTkARhx3f6DdYuM08tMpLaMZZSTv-yc9HW4AFAychI-VWiNzCyU0j-mxOxRbCVIAgnILT_ZoYdoCigxDVnIpOc1yMuegSDCV2tRVbKptQDlvZGeAFYORG_Ut2cKqM1YSfRZiZt88-1nAw2w3UWeOkCPTyUzYa9qCAdBbwDF6N-mMBZLNbOXK5vv-Hyn7qxCSSkE23bcK9ClQCgVFwdwGmel7YUo0myGW_H51b_KcBACipXLlO0J0rwk0riTyALBk8mSQwbMaq771_18cCcqkM6h1yU3NmCZhPVIZ5sVZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pv0rCqB7mNYnmmmI-b6bmgmnKT9mZSVbTr6Foc_lx-d8BUUNURkVeVMIK5nnnW4Jk9P2hf8q2TVEYm0ezTgOli4yABOf0LniJ9mM7HrjYImTh4W2Ks92Xu0UgW3607NtB9ijDu7-BOcEnXJNfsHsMpLTncAu08ZNtDnAKnL1eDamXLV9BsDLFhU875bEc2VpiDyoiMkzEu6mj8eNnJMLgVodPlN_6bNKa_gnQFkHYMXtfhOvFovEEZ8JX9x5nPwsw6FITbLqpjrROJLLHZtYr1RwfMUzRGt0xmCazzak124Db5V9Pw6nPPmO0W_hi0ia090EALn8LXBiU4TeBA_4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/od2pp5VRdUECUom-wc3-HncXjZJxhXgesmLisarU3IGB24v7c1tcK1nXfwGvTQQjmBHv6OocxNDQhAvd8p7APM63hU5LvpFXPPsNnMHgcsxqipn2N-R7sVMHZGFpEpb5AG2tvZ4hIz56JZw-QCUuioln9l_auSbqqoMna7ilTmgZRgVBMC46lF_w0cXnV5ZzVq0Ra93aB7id6zYsy1QgnTCVxzzwFv5SAuHGtI3ChtPIw6jOFFnazalKpDmKrTNw0hXUU8M1oCHULswi5fTcSyAgFUTOZNaSDzVsAIQeB_NPrVW0wnjqBlgPlhq9geA8PZRb5hMG_O8KZvq2C_uFxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B_nHSUWfw95_mshPpZvemD4Ze1olQFE-w_LHSH4psUKI71jhnASfP5bzgdA_wyV4nK7rqWDJQhGTKLUVvWgNJBzpAI65T1DyAUWVZYGGVaNTyxXnZH9CfhQknt81KRBNdoAsauH317CVl_3jPh7CqT9qskd1nrJvluyVSXEoc7bBj3T_Sc0aZQQ5xhucaZ8qTYVHbmiYCzRW0KCt5la5fc6uYtjPjW89gLPk_Ve-EWg1EA32Db1xyWqgEV7_aB45CdwTU9ZshrhF49Iyl9gw5iuYaY1qrQ0DE2r4i9MCbLhM0-kT7Y33q38tiyY4AaBCyh7HXwi_CuG4jAtM08nREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JivlVInDPV_5GtvaplewByRLw2oBI-WEBWt7wHwubVuQjxYbIhmnxFcsX2KywbXiykRmW-IHmdUm88mKruSQnLXDOtGrE4lBzLXSsiz9VCd0OnvfJT4NyTledVLll9uTNpmmvh2JvJ4LuwvyzjAA5TkWQ6Yiu61QSbZXpDKFbtQF93pv7MnAVAgRabrUEB5Qog6JJtE7sMdbesnUXF5CEy7J7icun_G6mJJDeX70VLMvMDOiRHgqxafY0CK09R1BqAAzCU58qsYzLoy0sKT_TTJrXlYb5y90_KyFbUL8yNno77QhLyU-GZyhKzDpFIkwizXg5XwfO1D4w3gXdsWOwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYmZ5VpNSFcr74f4343LC0o6zbt5VsOHs2y3Yu-yTCCWQBF5O2kuWt8MK0bjIQv5cE8ewckyRo4LiSW2HozEI9rpJ2e0N11k0hxItvB_wGWIyE5siL-QeUyrrff5KXFqZ0pSuRqncnnv6onVC-S92jQIsflxzsMW-UA8YmZUo3jVKsgUBLj2Y-J772LUvpn-0Bn2Zf51bTZVXfnkbgirBIhzYyXgSe07uodrD-R64yYHq83Wp9e1DBkMPD2TyQTf-pkIPcaGYcdfxaSB9TtQ3SAoFdArb5HJpvaAT3-jilDcZhAXmM7j_eIs23R1KqvekgaXakKXEIruj_yBME0QHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=PmGmQ_kaxR8m_s6WveS__cYuv5jL-y8mBFD4D8GqfoS0elTTEAoFEeRq9O1umP6i4qcsL-adDkgxK8a9Xi81RLwqUljAcsXIWL1EsSmeOijOWMQiEkM-YjulD2R28aHgYZRruc-c6_kTYIYgZ5H8fOyd8A-QqClTg6xNXnEJ1gmsegoWKWxQcb1Je4q9jtuk0LpaSQZBkOqg9-UO69ynG-f67InizMdaizxdvQ2k8HXgqnyNf0I8QX3FBaeKNzwMsrGFsc1JdsJnOEcg2gHawTV9D8xhUC2ckg6a16FSAfSpX87tdhGtGo0h3EMNr9OiVLXx0XcBr6yvpqujdFILcAclACXgYlfeHhxcKExpZdr5ZNxuNVy21TKocFIR_py6MejJKF1jky9nR6VkJzMqjHna-364oiHZLhYC1sc7tXC3U4Xsw_Yvw35g385Z8jQu6DEDX4HqgAHCvaxtRAecWOQbfIxFuwaeXCJKTh5201GWfeVP3_lj5pPweg63fbZ4HP52SNbA9jSLs3XHYzUqvu6ptEajyU_SXhUDrw-DhOWRJXXo7dzHKTDQQAoeW0EyBbIi54isKn8pAju__km7r3dDqLFIIPawKWgaZV_kyhF7re2OxeSPuSO0F22AMB2WEcK2-4b_7-Q01Xc0mgf148p5tm8FHJIgzqc2cY-tg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=PmGmQ_kaxR8m_s6WveS__cYuv5jL-y8mBFD4D8GqfoS0elTTEAoFEeRq9O1umP6i4qcsL-adDkgxK8a9Xi81RLwqUljAcsXIWL1EsSmeOijOWMQiEkM-YjulD2R28aHgYZRruc-c6_kTYIYgZ5H8fOyd8A-QqClTg6xNXnEJ1gmsegoWKWxQcb1Je4q9jtuk0LpaSQZBkOqg9-UO69ynG-f67InizMdaizxdvQ2k8HXgqnyNf0I8QX3FBaeKNzwMsrGFsc1JdsJnOEcg2gHawTV9D8xhUC2ckg6a16FSAfSpX87tdhGtGo0h3EMNr9OiVLXx0XcBr6yvpqujdFILcAclACXgYlfeHhxcKExpZdr5ZNxuNVy21TKocFIR_py6MejJKF1jky9nR6VkJzMqjHna-364oiHZLhYC1sc7tXC3U4Xsw_Yvw35g385Z8jQu6DEDX4HqgAHCvaxtRAecWOQbfIxFuwaeXCJKTh5201GWfeVP3_lj5pPweg63fbZ4HP52SNbA9jSLs3XHYzUqvu6ptEajyU_SXhUDrw-DhOWRJXXo7dzHKTDQQAoeW0EyBbIi54isKn8pAju__km7r3dDqLFIIPawKWgaZV_kyhF7re2OxeSPuSO0F22AMB2WEcK2-4b_7-Q01Xc0mgf148p5tm8FHJIgzqc2cY-tg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rBdhSE84vLymFtDBa-VPcq92A9-sffB3qGZJ56ABXW2nGIzvJ5KR6TYchA5g5VtDgpf8gQAIkI4NNViHgDek5zFan8Ee78A7UlZi491OSP5AJC40kJ1L5e1bHXUGsIDes_ZTokYNzu2qDnblG9bhQ2-FWqHzPrqHsL6Il3f9yYP3imT9ylnHOvGHVgPWMwZ1mKhey2C6pOcyF86ze2m7z8Ef_xtyZs2lKJTR7iR1KMuSxmEdM5hTGF1wTRiMF0eoWzESmjnyTxgz_3i7DM-rC5wcoH1v_wkpqb0SjTUMvGvPyrf8euqnxTKIKyc_5EkaTjtd48-PG0ULGl5cFgxCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JRAjgtwAkdgS3q2HEyvJHNygIy8S-7uHUBvzHrFvGHEd_IG96aNCzxLd89gXXTB43BdHckCYybM2pRyK6dNuWlLbL2a0ZqAshRo9h_b0d-us7QI_9P_97C9LjPXPWPMkIaNDRAO6YIIJ5Rm3RpwRWD8xHZr1_gt3JB4tbM59V8SZFmdr0e2Y-QwDRglsiLPnziNLrfXD9Cc-T8TypMcCzOwBoIkpCDfIoKIsFohn0F6rX0YTOV55d6tezPP9gp3Wrf9scp9em6UQwNRPfR7bC-HewQwuKZFfI5o3IThfBEH6dC4PzlU3dP5JKuWNbhYYbDghtXsn4SDp0C5BvO15ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qWGRz6csEjHTRhbTSIHr6kgJOkQjQhSZqIPCRSAlZizSuZUIC0B55GsbIIwxzoviKZ_Ljytv7RB10xdRmSCLxJ7qpiu2dpP7yRTL4535s-RxbglMN7Aoo7NDQ-_Cy5RYSKiv0q8fOnOASJhbaNHeYv8FA2Vc4bQukt0qXkmaPwh66FVIaIOwL4Wc5sX6usJEvirCmipEU0vj9I3YW8Loo6Gcqnzo9vKZzKuEMZUrDQyuBWul-EUfGE_NlrlZ8ImXSyVKnDn5M1UB7X2I9uZE6gihMwJ4Ecov8lP2GUUuX1PFIgwa-0t7iyfmhEjhw3yWioxJps9jGaV3koo06AWk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fir9I3nMT42sYi1s0rEOsCxmnFQQfnytfV4WoNrA8Uxh4qqFsLVoVeponDDvHUvy6PxKYlj_7IpuKun0pcSQZxzs2XXPHhP-yDVAeiIny6qRmn6zvs-QUbK8AwqPCfNddhMh1xuIKF_Bc3UAbqqby7n5TJwYbDEhCeQdb9ZPKBiCzceBF8esNL69Vxxv1eDEm6Yz0KN-gYhUS_WZyEchfmcuRFi3DR17vH902mBjbOb1AW-hCW54BgPfy2hc2WrygSYkvkKb2rG7NcrtdgRxjuKwsQTzGH4YhookPNi-X9jkIZY3o5Jk27jXUtXGiYJQCcPmEi9H7uwtgORYj7RkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fY_hsGReKFRihGNONpY7yXcIkMNysw2c4bZk2gDI1dgf0HT87BJ2_pevQhLzaSmrLEIEq71x38HGTc2KOEly8eCr_6NhtdPQkhGazA0IDF77nxMoezrC4yZ-M-_F9WP1bNK5lgJ7AkcYZReSqlni3484xvixFFErOo8BukPn60fn7wM6ItZ29Q_ERLDMxTBtN28ef6A8rYf54loQg0C7NtY0rHHekNaU49qaZ89DAAnkPNz7T69ZJqpewQRpx0V05EaTgXJrTUYbsPmUac-6XKYCWN3W26WwtG7uZAGpYJbL59suhqLpjMauKijTvQxKxZ2TTgqJRNBvX_cpKQcV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zr-XYVc8bZuGtDh4o8_9s9TntoT68Q4h_zbM36Th1oePFhb8qg-IScvNyfUnQn2uBqMNcXo86jRkxLMjtw4tY3slJdpktTMGuPquLpqLMuMJ66vYRMMkcslrZpshcSMjCIgiCzmyXRSn06RHKkZoEoGu0-nlIDOSiven9RcBQ8MO3pAoYQfLKd8K3vA3qoZ15lzlI0QIZTt7T4YGHWtRzF9lw43hZQbK4YCjK5BCWxCiEWENt3QZaDhtx8eY2WVHOd1ZcSnmrb6lSd1-M7sx84F5LVRzE_AsMnVBvXUf2iPzNTYNSH337s8xVDVGhHb7FT4cuI3G5tHzeoYJFY4qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lsG9IRPa77KbnUb-Mm_Q8JK5bmujTYr_xt8zjdL00UXjHS1cU3-lEIpD-10KWocikcJjXE-2YMjIjOboeg3feuItz5e9tXeJOLdJaTrWe3CjMyqran1zY4p9D9wemd9MXn4fAQ1bnR8p4yiv1j2cNuvzoG0YRCg4RLpQJnVvNOxq7yIKzLEu5g5gI2jmB3-q6MLnJOtEWbDd97WDhtLlhvO5XEWs51jRZUVXJ6Ms7vwfdsq1lmIWqKHWDIB6WTAgxYj1vOdz3p_QZnsUiAPcPof7aqBTR1nADJwzSHft-CxbbDPSFlgfpYj5Y5DoPveCXtJsJ0GYM2PvUcGWPimv-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=Li1WOJm8YODW8lqOGOX9GtvkirmYSnMqWZ4VWA4nhOfmP8DuPQ_ZhaMIzxkIedXn56vS38UrJwYHP55rDOlKhKVAtNJB2DhXV2WSeKT1kRS1KkGlCKMkomBm-fjNu0bJi-z6lDvtrCZerc0bdYQfAcpfUX75UbQtkuEpW80XnAcs7JtCUm6ZU_fXU6BejxNBNnNidGcKsLZGiD1UWRyKQqLyoN60Zs1VgEla5F9guipOKT-Wl8xki9uP2skr8spbquVd2CUhCq6Az4UMTXGsm-z5i507JVGndMVz2IdO28e65QiQc9fWqiggONVkMbgx3aHBe8Xo3v8x-TsjWeExFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=Li1WOJm8YODW8lqOGOX9GtvkirmYSnMqWZ4VWA4nhOfmP8DuPQ_ZhaMIzxkIedXn56vS38UrJwYHP55rDOlKhKVAtNJB2DhXV2WSeKT1kRS1KkGlCKMkomBm-fjNu0bJi-z6lDvtrCZerc0bdYQfAcpfUX75UbQtkuEpW80XnAcs7JtCUm6ZU_fXU6BejxNBNnNidGcKsLZGiD1UWRyKQqLyoN60Zs1VgEla5F9guipOKT-Wl8xki9uP2skr8spbquVd2CUhCq6Az4UMTXGsm-z5i507JVGndMVz2IdO28e65QiQc9fWqiggONVkMbgx3aHBe8Xo3v8x-TsjWeExFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFIsn8i6LMLc5o-WhQHsZt2aQPkpau9pYHX50Jemme4eOmkLC1gNQdPibmNmbLmsuFiUGgWG-bDdDFBjD1UKZoGX7364Nhrlz4Yo3e9dKSF6-7CZxGyy2JB9tZp04P7RpdvZ5Krtjh3rYa3leZ0okPZM7H8wl_sRLAYvyuaYg1Y7s1pUnECrUsE9P1W3wkCFIL8eLOL_KSRd6TLKwI45f29oEJewekrqJfXV3qFuvfWsd-Y-JKHP5EN1XPaC3uj_Vz7p-S9nUDsTwz6K6m-xmFm3DxKIMTY816-9Xb5OQn4Uyv88zmAUMQ1DH1W9DX7wd6asnUfD77bRQ0jeyvhznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJ2d9jJ8UxFe2ny8kcOOvyjnjryKFgS4oYrtH5oTGnj4f3DpHMdQW9muDK_nnsg2YCNiIwBMdry-bBJz9eXx4NQFWzLUoSlvBYFTxRMDoT6yiRwxn4XEA9EZTOnYR2Y9mb8sEQ3zHk4fN-aIKAwfIymyg1koKEm79VbVHwimr3EyzvmZBQCouQidLQ1vHJGFTjFEMtyJR9AEpeLWcnARX5yWClyEoEWRQrtyRR5m7Hg8HBmAFSFk40jYMTDkYzSJiKXrOQ_oTkStBtRuNZDOvXIdJWXGCNtfeNVzrfU8-EbcuftoJTlr6HvwZChyNu3L7Kp4Dcvqmd23DZUzAoMZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P1SAG9-SykriHTyIWopLcQMpO3A8kPg_LYfVOr5zlvdGRioS7c1ErLAFIZY8LmxcVuqwjtP8mtsDbz54Irt4fM5pnLHWqssPf3y8lbQ5dJ0dQP0rUHsTBWrhhMQsz7wobs7dsmIjSD3nUD5HOpa0__DY3OZ6wSUB2kHImlwTfibVI1CxrSllN86781vRfjofPlOQVTe5Ke5gZPEnzz-Mwkm4VuAUG0OCZqsNByH3ExNh3JQ4N_qCqv0xufske9agNEoolHrs8qhlY6fJfq-0q6XY3qefXVzXax6c41oSPvKygV0Ydf_SDx1wvko0MaGL6FHc4jXHmiOCDzPT4xPDeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=HLNenneVq0Ks_kSxsgUJQSl2ESJWCK1uzGehiptztw7504zNHrVsmI06Y4NJHjVN97YJrnpXujtKAUF1Ak7onydaAjtLLKMjDNsZBt6Ip4SAG3kW6ttWcIBwXVq-5g9s5FeV5ORYvfhjAuIz9ZPwYdDzVBYcs-24b8L9lyiRQnD3jCFCBr4Mfr0rPXc23JV5w0z4gPfXFKhF5IIINgyZa6yMlSen0JX1-98ctUT_6_vUN-eYUArzp4ndqXhzgCkKOvf_boHoOdWTOvB4yTrEbZBGxWW_zrnHprR2BjxPk7HJPfm95sCYJjmbB_x4ZEUmapWl1gsuqmS_-RcekwFPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=HLNenneVq0Ks_kSxsgUJQSl2ESJWCK1uzGehiptztw7504zNHrVsmI06Y4NJHjVN97YJrnpXujtKAUF1Ak7onydaAjtLLKMjDNsZBt6Ip4SAG3kW6ttWcIBwXVq-5g9s5FeV5ORYvfhjAuIz9ZPwYdDzVBYcs-24b8L9lyiRQnD3jCFCBr4Mfr0rPXc23JV5w0z4gPfXFKhF5IIINgyZa6yMlSen0JX1-98ctUT_6_vUN-eYUArzp4ndqXhzgCkKOvf_boHoOdWTOvB4yTrEbZBGxWW_zrnHprR2BjxPk7HJPfm95sCYJjmbB_x4ZEUmapWl1gsuqmS_-RcekwFPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=kEPwQSYZLShL8YjxAiTgg_ZKUdHBIEdTMhy1YaElpCvVZGZMPzfb4oy0L9A0h-TWvvzOoSy3TibdsBOb4dbqHx8B0H-KNZGOKJDpcCowrodykp6AlB9pqB1riLZAQ7SciDdm0mMAeGhKrioYQgKa8Uqvb5o8kIUUC2jSKgkgT80jWBBPhy3Zvlr24lAPibhP6Kllbk7TpZC2RJpW3YeceF37J_K2bj4pk3B8CCnMkonO3jjfmoomMTW85G54qkiPDKAxauYVHeKYwIGK7-2v7tWmEulDzMIOFIpZF687T0NfQUuWJuflV1EIQ19c-miJiTEC-5fFSxBL265OefoJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=kEPwQSYZLShL8YjxAiTgg_ZKUdHBIEdTMhy1YaElpCvVZGZMPzfb4oy0L9A0h-TWvvzOoSy3TibdsBOb4dbqHx8B0H-KNZGOKJDpcCowrodykp6AlB9pqB1riLZAQ7SciDdm0mMAeGhKrioYQgKa8Uqvb5o8kIUUC2jSKgkgT80jWBBPhy3Zvlr24lAPibhP6Kllbk7TpZC2RJpW3YeceF37J_K2bj4pk3B8CCnMkonO3jjfmoomMTW85G54qkiPDKAxauYVHeKYwIGK7-2v7tWmEulDzMIOFIpZF687T0NfQUuWJuflV1EIQ19c-miJiTEC-5fFSxBL265OefoJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CM37F5W5EFI5XPnEuIBwzrcbVJOjDjxHsyCbtxejPkfPGb6Xchks51mrOSWIlXLrZEg2NpGhv_Ot_doai002tLOwgA7vA2MVjv3Li2Ep0i4tKc5VxUWZNCFmoY7N0PnsAmx1tCnJJ4tGhapeOsOUc6Z7RdDYuIbEoxt3mUC3wesFE2BFrkv4LagCGADTHADLM0xK2_1k8CtgsDLoznioQVi30hyhrSGQ54mvS8aTXJtTA4b8svz3x69gNkyavNU9FTegMJpzHIuuODYz0dR3-VahZ-TciXKFQKFJQ9FartWtDdSSwGh3v6HPOX0HWVTIeq-WTDyJdTexmNm8UeJkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NW5_ENLSMUf7eFoCaJ-U_TbK4Gm5dbT27TSBC-hoiXK3W5NJSmZuEbDzeeFqaBpnRNLU_oIHJ0SnOcKFALtE0igfYev3ZTKFJnCOLLeZl0LETOrrtYah7Cyn9bcJbuknKTpoWvT6DOc4G-khz6Ne1RWK76CGJonSgd5yZJvB3bC9jcoH-pBXw39zRFYlLRMmEFuDr4o5X0ivuuzTuf8QjZhpxQj6Tkdtph6mXuvYUc21AF27iyL2LLSkqbtiM4Roh48ZYjeWDjgAlk6JP8j89ve3TCzCVn0i1ikXrroGGwCUGo80ZYp3dxors85wybq2JZzqnuu-MqyEJ6USzhM5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PauEoZEVmiTtLeeYPetzY6-eAz6UNEIbKZoUhjBG1rPHo1rULcYUzc8brYM2Lf1DvXv4X07bseF3UOsODjs5z4Hps9uMj0zn_OHPhfouFx90NBM89nrFFnFu2JQRSZEtC5stc73GYpz5vLcO8qVxE8M1uZVXbRb09_YRly7JAiCxYggu-oImCYUXjcWxYBGhQNtgNm8rdTiWsGeFzzk-agUmiykxG1ZigoRmjdDo5WZfQjrYFXjhiuGB2tAAGuAQ9JSCpKHykBGoxy0E8MBl2GTWb0DpNE8NEhbDcwYW-vHJQSJJ9bW6GiJ6HSsSdAnbTX2as7VRBEaIKieeoR-DCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u-GI3yhrxYki_yfVgE0wS2ndZKP1b9r8DokklKuI6rZFlaEbeUOyZ_O-5WxAcNSEuzOUlyMp3HOMyvHBUe-CxgPRvPPciNzfF9SEe_uHSefLni7ElViyKoxaQ_vKvZ6_qFoytlYJJ2vB9y1UTxO3P-g8HvmMzNvkdvQ5FBMcyXcDqrcNbBW7EXtfTObBcaun637Fn518ylnzT2eOl9etxL_7jSAVt52jZ7N7Jo4jb4RuJnlPekgk6xS1QeM3BusyO-JML79PfkMqkMwDi72SNYFCVVTkAaLdTq8TUhFGvWcYyYUc0CBchsxDlNNTAny3MlPhAZy6xj4SoWxufBO-dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PeVoWep9a1nLmwoQOQeobu8DELIyws3ioykzCe8Q6qr2DMeSPt-5OlYEF7vv1Bf3-Xx_aznxt7bluOfM1R4-OM_53nwAd4vE-pMOBxbBV4VWv-6_s63KKHGhSeHpaSKOo9tY1ufywnrm19ymr6vaQNtoRiPeV7HkL4gjhqQe2VG_cOdSGnFgXvF0mcJcG4P_Z22-ux304a0teu2vdX82lSroA6ZMV1K_ylPV4eSacVIxO_gd5IX9GXFPkYeJIETYHRaFLUUMoHszq8ky5xAq3cXIUb8zK1RwnaS47giVz5AJOkiqZJIZ12nN17PYOp-PBi7KgUzdSo2eICF9ZbFAoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3RVZTqFkcmSN66b52u9MFM_TJxtok-xbgZQRMZuS7ycYYuyMZWPndWjjPxEyWO7WMhPFIohPeorNdS-Mqj8vG_vF6FNtwVzmJmbbljbnpwfGy5yUnyO7Rkbr9AtawokamWQyF88d_sZmjG7ZuKcZyV0g3bVoEKSZlcfdN6N-sKTfc_z68NoPTa50JUpK_-jw2zC55IRhRejZ57k7Q1nMHFP3UtCS8Z46fGmGKoY3_kHVpWjHZtO-YwGTjvLvtwkw1GehDerRGAnsVg2j_KRaDvEclmMgLyiJKPnMefCpyXeLDzHk4mAqmKxnU65l35INS7kD7cdX85yeHFg_5p2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WHXfVO04i8fVBgnUTX3sJDTG0WGJzpjw06E-38QSKR8tH-PMT4E5GRpUUcvSI5m5DCusnwiJu7FjvC1nA0MhnRYYQeWetC-oDT_7YZbn6rzL7QV3M7z9ouYdKbIZVozf14aohYa79vSgQGIGfpuNbp0OeZ90hIKpN59dNwIFs2jlVMM5qsH9JxpV6laAOE6rAUCHc7zXxtoRkAIDo12fILT4VVDa5VpbddnDQ3M5iUv1RUEEJByjTALOsEhtGU9Jhu6Bq3lAIWpibBZ_8tg5zNXQuD6IItt-Agyc0f-ao91skB5i5DO8J6dE06MkGtQ4NPF8JdPrOEj4L62VncUYOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1I_Yesuvh4JKrpBqEh0Kaew2V__ZID2IFue6VSFkItkXxkE-RFdktdnK44N4yWZwCEgX-8ZjwaZOBu9X0RBbR6Krv9GWPO6hGcKdm9HaQZdvhZpIioOeB-nICrK2z8ID1TN_TfvpfARh-5cb76oIP3EaHBi1wmFqQrRDOIywKmv0EvpJQCy1sOMDUnIJRPyRGDXqMrSiRLCvKGHLmUNQRtfnl64b2BtFVaJVtss1SazycWEOsusnoT5imDbm8Nol92Ua9C7dPWNGlkml3KFQn2NgethgXLzxLwPysnB7KOIY5gYUXppsHGdXRBdQvisRoKlMB-_T8zn2inSReLCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=u10xbFyk0kTB_xXhonATJjlmEmHRuAMVT3OrbMZQhK55OdZaW--J5xPrR00Vz7k6GHz2Qqgy_WhENbxDkau8eCTf-KZAoKgN2hc0ysS9YoEosZlm7TZ53tCudwaqYSi3IIJ-rd36nk4Wn1bKRfQHE6wq_ukXOganHjAzQhRtbQE29lcIvuni5SV_C_xex7AaXz5thzmiGqUd7s3vx4Geil-b2Tf9DpR6lpublrxTakyO6qMHd4Z3V8ckrJMwXrsmf7tqbMfAWZGOy8uzP6rDZv81fi3Ut4iVcAElUIAyIjHiwjMP2if4-_DCJJ6SyHqxnHR-rYg5eaDyZB147cbIYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=u10xbFyk0kTB_xXhonATJjlmEmHRuAMVT3OrbMZQhK55OdZaW--J5xPrR00Vz7k6GHz2Qqgy_WhENbxDkau8eCTf-KZAoKgN2hc0ysS9YoEosZlm7TZ53tCudwaqYSi3IIJ-rd36nk4Wn1bKRfQHE6wq_ukXOganHjAzQhRtbQE29lcIvuni5SV_C_xex7AaXz5thzmiGqUd7s3vx4Geil-b2Tf9DpR6lpublrxTakyO6qMHd4Z3V8ckrJMwXrsmf7tqbMfAWZGOy8uzP6rDZv81fi3Ut4iVcAElUIAyIjHiwjMP2if4-_DCJJ6SyHqxnHR-rYg5eaDyZB147cbIYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g99xe32JvQ3hsL_xF-Phow4WyryQ11HNIJ8LLDIBRC16Oi594dcembVg-VL2M2Swzvj5XeMZpR6pLKRl_Nqu3WIIHS0_dfRDI8FDZErvZXY1KCxdeTjbREKBmNONLhjweTq7eAZtyMlFyQgPqF_f2FkNvHXn8YOBnMCnXKB-QBxjOm1NfixVtyL4Lw9IJoOfHW3uTW8K8KQ_Vl90kUhTUc24bPqXdevHI1XvXaQGAs-R_gPre-Z4sLaWs04ic5izuDnYepLr57SQ-EY13CcJLR-Lf4DWvRAzTr8JYkg0XqABE-DtEdvsA9-jRg0Q93pOspV-EiGISKf58uiS6Pgx8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5Ht3M7wB8dz2UsaCRFQwf14kQeoWwTRpEAWR4_J2lhLnptXYHqcpWUY33dtcSCq7t3lkXRyAoplJL3QdXA7BS3Df-qcA4wK6aufoWWklkS0AchQ1tx28BLZ-0GKiPSjA3hvHba_lXOJb5Qxs4wCdWG7FBLPXUOCOCWrZVHrVkcwbbIoxKJnBtS3M7XHfJa121ZjPLXD6B2FyXbg93HE0bDF5fM3vxV6qYzDkga1fXHOJp4IOA5eqk_eEDnmWLjw2CeM04Z86Dww_hO4Rm-YGQU_bWsLrkCch468Oq3h0WWhwYQXApZWpyh-ev2tGKIGbFOM-p2RblBLe95t21ckLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWd7vcJDzBkq4vmY6oZFLWiqTfj3vZ6nNitSDS22xWTyXRMQvJ6-XFqokuBgdGxblIhALXPjrS4Y4xdTk29jlE2TMLhO_IYEjoNfTwbhmblg1zead_YK4pO2g6A62vMTLo3Lg26ohf8iPj3lHAAfM_vs5DaAsrTL9zkeOyyWwcj7knGy9_MjyCpK6jroGHiS4IsXkCQodup7MQz941XCp4ZznrqVcXAhwhcWTUkbTGXOlK6iXaG5fdzqIfLGzPuZzB53lRYbqzBwRFVqahmz33pNJ--w-WPDsM6K9djOu8MzQfkwbqjCzgOgozLbPM974zzm1Sav-nRQrcbuAkVGsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=TkOTSaK382NUcomNjT40wmOeNTdqbdgn2eOEw6POdo4jWvEND4hpXrt2Oj8KiGmix6wOktKubydJ5Fxm0ih3l6Q3_yuIdj9KfYb2gKDxbrn09obvFX4i8f3iuSqmGy09bliE1j-nthaoKT66DTK-RuHJZtt-ydPoccePoDKSKVf8M019g6O8vV1E9XEfU57DP6uYCT1P_nn2qg4le64CBnoQInBt_myCPNbTx5T--bnzyFcpahUTWQ0TaFA-gvOvJ2WJ6FrO4Ky-qM6dEIPrBWwPwHU1dtFcXmkDcohx7Aws-Vn9CCsYlN3nOSbXePUQr9mZBEB1gtachlgKdczh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=TkOTSaK382NUcomNjT40wmOeNTdqbdgn2eOEw6POdo4jWvEND4hpXrt2Oj8KiGmix6wOktKubydJ5Fxm0ih3l6Q3_yuIdj9KfYb2gKDxbrn09obvFX4i8f3iuSqmGy09bliE1j-nthaoKT66DTK-RuHJZtt-ydPoccePoDKSKVf8M019g6O8vV1E9XEfU57DP6uYCT1P_nn2qg4le64CBnoQInBt_myCPNbTx5T--bnzyFcpahUTWQ0TaFA-gvOvJ2WJ6FrO4Ky-qM6dEIPrBWwPwHU1dtFcXmkDcohx7Aws-Vn9CCsYlN3nOSbXePUQr9mZBEB1gtachlgKdczh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucK7pppwV7s-zgrl7wr2Ddt3OuNBPcMbOfnGvgb2wyhTAJPZOFVv15Uk0bH1Hk84fOCsvjhl122gxReHJouzP90G5oTLWj9YRsG4wAoLfQjMD77BMqF1uYjD6azD0ZLubZ9Ws7DQYXAKh5PqdURpKqvGGyIS96BIWGcJw9FnQmp46t1uJUlPOg97Pfn8wuPjTzE92qqugFTzabxjR5rJFYe85AkC9SmBAtKSOyg6ZrA82BuK58LZO2uzz9K8zhAh4AbZ-cpfOeUhS1hWfzx-bWsSLS-AYZeqX3uxz-y2ntaiR-7IxKWEJEJWLG8JhlagkBG7AU3cZ6-ZvcxXC-Vl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDpUCI3stDV7fkzn1bq_FiB9wXo0apRGEoOXivxcbwzpfcxAzCY256qVh8UqBKZzNT_-LQnM8J7LXlUhYK333w6LxtMWMR6krvEWOojVpYgerJendMv95V-MmyJnkgfqbJ05akyFj4_gs3SI4OuN4rB-dPJut6Me23EcyqVgc4-6__fYd_I5TwPelxorvJBVEawPAf8wg9xcdZloPuUxlZQUuCaIEJYvZwRExr6UNfdq0gkVUrGzZ8EvochLF2EOTgQekttoEoTQayTIv222pmMBsnW5N97HC1LmlX5fobpkc018nGDdUHgvTvYLN1Gvh5xRic_qKnY0E9MZGfD3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=dpkLv8obmzTD_-mwKVIIkWXjjA7IWzJUCo8EXlMlEidCMghukjOtqgFzt04rry188XKkHp3I2VXLzFDvpD4EoWe3jHofSoKvlccB9O0pnxQNXlpRQabPhcPZL1PxkzKBvCaq2AEJzwJtLJfSfK09QgcqcQztgXYwiIZKIrCIZWJcLnZzOckvFR6rgKaafvb8CXQGkMZSxofCpv-LeEswF-Ot8Z8eA3cwr1yLJP7mUFqhIVV_mIlZMLhjCCmuc0WnAqms763QPpv5KK3WDOqWshAEqOLo9x1R8z8iT1gbr1LINZ7YnWe4xVJEa1BOd4VwuITgfeeWKVM_Cvsk6T28Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=dpkLv8obmzTD_-mwKVIIkWXjjA7IWzJUCo8EXlMlEidCMghukjOtqgFzt04rry188XKkHp3I2VXLzFDvpD4EoWe3jHofSoKvlccB9O0pnxQNXlpRQabPhcPZL1PxkzKBvCaq2AEJzwJtLJfSfK09QgcqcQztgXYwiIZKIrCIZWJcLnZzOckvFR6rgKaafvb8CXQGkMZSxofCpv-LeEswF-Ot8Z8eA3cwr1yLJP7mUFqhIVV_mIlZMLhjCCmuc0WnAqms763QPpv5KK3WDOqWshAEqOLo9x1R8z8iT1gbr1LINZ7YnWe4xVJEa1BOd4VwuITgfeeWKVM_Cvsk6T28Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNh96eVlyFPfyE1RB1MU5zTJQuYa7GE-B-5CWqNSgD-JWZWV2kRPqCNvkqGO5SZpX6JGOCR5uWFBYlY-_Yrf1eQl714LXCb_QP1dYkcnXMwneSNmp06xzx3Fnx0KMLW1EjXY2HXhVQc0HphzDx8Lq0jk1XopDdq0RMFktBP-2goYIbZL1ZlNhdlxWTemJJq_LUMKdZ1a-76-s6JosETtT8rML0eOvP7mnefeXFZGnSSArxX_YhhOCu62ENxvGyzLwYA3lq4vKp0WwKwZVnMJ0vSFN2nL2utnVq3lYhVLy8-GGslkHeoju09Zw4svPTSMZyDFKDtAZOXSi-RFERvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZMpe9mUqWsDWdlBrqwOL8oHhgZbN6immAv2-afYsj17bp1yiPDykZ__ZLb1jfApMuMCInr8cgJOrkXm4Yad0oaO219NLFrUTB-W9XlI3L6TO9dZX3GwAAYplXPEwA8kagmMfYKa9s_y6CTwCMbGYdx0cKgEWVm0GH1IrdohiP2L2ejLEXIoqNyySSRAW4BoeYBjXg06692_NgPADdpPQYoudv1NfxGACAfXQeoX7a1VgDX9h3M_8pP_92r72Cttps1hDNF0EQa14vOgVl00ew00l1jIvFlaWPWzXmKsJGlT4D0GH91-HvxT2CxF_pNtG_gA0w2aK7KCHa4MfYSqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-gSozdpG3AmGN_iWryCk5He4IQysqY3MDAQ8yg6xU2Kv-y7Z_FRa27KUy9dhD6empyS9jXxUuT6hMzT8Gr7CxfzidKpfNzSMJrPxXZZU0_aSahdMMGpO8DvutlJsCU_Mzq7bbU3ZYPJlbI6e5zCT5pp1EHxI8dZQwgFS0w_QJYIbL1hLCMT6fLFrzggax8S3zOZt0ruhPtwz9jYngyCMY2xV97f1ywAR4utlqMd0_MAChBo4qkiAhUvHyqiPmN1vx1kmkLyGDotoOJvvxGe-FQOOcrXhW3IIHCDC_aXrmNtvXHxuhVMDM4E5pj2Ts9pYYKHzV__8fUyeZhmo8tbag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LanPKL7TNma4dtVh1A663k0o5keF6C1AZ16VHIReToDQZ6aQOxNWAH9y6wyvtUL7zF3GJXwVQWZiJP-xMkIbpxPTlZxUxLrGmgmItin6hzQhXY41juW64i6hbGf-9pHNuR6aMP9jjE5M5oIUHblVphwe3okjSb4rePkWMVD8WYkKI1SCKGpJHnvWw7pdHvi9sLbn3muVqQbJTeW5ZW5OQC5Yl0lZlABiXDn3FS2KrejH3ABKV29ZiDgkn9HvTn92MKkNYNWgTZ1YQKlpQe73tH3EZzx2xWxf-9Nl_j-A11xDGfK87tsNvY9JzaIJrCbQpXq13dC993cVxjzQ1yOr7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=pwJ_HOUWQzw993TLLt5Qtmq54hHEKpuTd-A04LPTyJbmWaF3KtQVe7FJghlClySV5fyJVkBRCGP7831DKwrVqGFwPNGtbFaSahf_HGHjxQi6jqfpIsX-XsZCUcUp58g8DYp7JOYfsv6_9iZkN4lNGYQTtso-KI8PwsAbTdNYmpWs5U4bACVKf5w5X4uuqRjFdJB0UQ38as4ZAprAKSl-HaAzNcYj3DGPBNM2oxP2UyRhBhXB34DgYVoFSdR5V88LwBIneffRtpl09gOHjOcHgnBDIN_AB9GaRc5SoKCNk-vL1mTh1N4qEVNvX9aa06lj6oAnLTW85wS_eUE7J2i4NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=pwJ_HOUWQzw993TLLt5Qtmq54hHEKpuTd-A04LPTyJbmWaF3KtQVe7FJghlClySV5fyJVkBRCGP7831DKwrVqGFwPNGtbFaSahf_HGHjxQi6jqfpIsX-XsZCUcUp58g8DYp7JOYfsv6_9iZkN4lNGYQTtso-KI8PwsAbTdNYmpWs5U4bACVKf5w5X4uuqRjFdJB0UQ38as4ZAprAKSl-HaAzNcYj3DGPBNM2oxP2UyRhBhXB34DgYVoFSdR5V88LwBIneffRtpl09gOHjOcHgnBDIN_AB9GaRc5SoKCNk-vL1mTh1N4qEVNvX9aa06lj6oAnLTW85wS_eUE7J2i4NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If7MWs7laivaxWEvRYmjSdzAncHw9WNN9MO2thR6P4Qmd-gYEke9MbMnkgm4WvV8Os6GZqyfD_HmECWQgu7p-b8d_UdIJnlVbhVeLmlmQFjvvRk5BQ1RG_ispsEXp5i8wbv2lM4i4JKJeRN0cA8KihbmUhf1qt8yyywZCglHwn2SGZnUMgCYzIpIBHUVAkPzRWuIG8PYYSImL8_dmtqDFcmpTmLtAHM0gdW0iKibiWtFxRjsIERZX-60JtH5BlntBVEz4HymYL-_FGfyxwBvRUjS6REAFCYPXdq4-QpfB3Hwo4kjNneAm6Zax97gcw5dfBJTNwiAmF_1Qz9-V3vhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KGMM3UiRotE53bdW3aas1eWze5wNGoZygg4btEBbSGMC5VbQsVvxOXhhS8afyc6ElhnFymWejDQAuehX-U9mDDRy5_sBnp4UY9cbaufOMn7i1jmpi81MH9NrOnUqwV8WtCIl-kFbz0vsGVt40JmzDTeA3itsQsf8hnmVycAGZrXZ4ZFug1bknHucyVtrFsV3ZNgDJyHn19uelcOvn6Rer-5D3Vez2h2B6hipxQN-bSYCB6lliVALgFuDphqSiJuoOQXIeGh69vkbqaPmamstd7ZrxlqOV0PGNLKrwjPXL-7V4Rh_AI2giDAzIQ4AAEtYF3lgN25nlmiPKhj_H_q8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZQNW4iNG-g1Fb1WzclCLftgoa89uRTVG88BzEZCRnlzSvB1DoEgYJUH_iQHUVVWJ35WMqYUv6dLUHrsIjNHwByLmtT1Lz0gTjOYiRfXs-poJ7RKMTVjB_YrPvDpFvQJALJPLzA9zIJ64Bj0qpKBjP21HL55xCv1S3PxaOXYC43K6nBrGR9ezPQ3ujUQJZAdFClu8EL26m0F5GhljL8XgnKxDgDmAtwUKCjR2hHOMSgEBzA_b4-5dXHFqNqAUTIOXswxpbn4C05CwNbPWAW0GF3jveCceTmks2xq2oVgtxJ3BCymkG8pC5sLb04QDQZfbKsCMSwlhYBuiUv0a2tPgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qLdK58rtIGbGHGerDLqavgs0E-66NRBMjYJNUtuULH1XT7xQYwItZXF4Z05KNLvzqJv8EljPQNy2aiF5Hc3dy-3gv1p6AuCLgXLlTF4sXWFIg1tsnFEvFhcCDnUVi5PpYZFsfxsbraWAaL1EtrWv8pnlrjIVFdJfV12LFf4YYWuFMtyyqCYV6nMJvUFgoZ6JtwSw9IDDXNGyAoXEFsQfsl4rxKzLmvjOQHokDHpKVIWLFF15dlUfbzKafjf_f3_LCvUTLKO5EMfmAFzDrQO-WUEhT_57TzDot7wPp6lkC4UyrXtP3vjSrPEP_nFfjsHSYYiStcuCfGXR2zkrpPBGmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JoCJytVlkyaNWhhjmyxzbEwqEB49pDRWF0qF3t5R9kGI71UBw1zbIN7usWomBvdtoX5YmfWdh_Mw6M5ezlFAnzPVA0WBu2JU9mWgJZMDA-TJZ97cylUtzDEFL6G0ETVa7osyz7F2c6EE3BAIuBHol5tLu8ef8pdoKEIcBvpJL4pyoMc2FUB9h5gg7PjeZTcQP6euM4croE55shWsHMqjomkoILCIvDSBSdqcs-9lFI7uM8RO7Yp8yxd2Ac__k30XIPsE_fMcB_Zz7TxiMEIkU9ehzS2XhPH0tNTf9lISGxMLtZoqGmlm2qiD10AubsuFB-kybuIWgDbMM0Rf_SP57g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz4qSXb1gmDDvrJV_bbgtMtUx8Tp4LqQq13OSLbw9NeqMVU8CmTV6OhFz7jk3RJ-IdG1CnI-1K7tqqmFYrV78k8WtYtPl4BaZrtIaZW-dDTRWnKt43i-of6jnLi3sxAH5QtFGmPMKfjLSzZk3C7YPUV_q4Pqh4svowLUWClGk9fLpQ-CSc52AJg9I_4m5KFLQDNebQnqoBEmpXTnWfiGBE3pJks5VB7HbuCKmTtEL1UU33czyF4XC0MtFRanz_H2m9DuAn3HNfl_UFhq7s08ShMan8xXqRi_ImsaejWyeIvE5yl05iKW-oAbpukxwbZDcC_Zbto2TEh9mFe2yclIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwvtGJfIax3TUY-wxg69-2LygZ0mps3-bff-LAm1iR2jdZFsvpaKVsTMXi0HRR1xAta9nLzgLO0zXNTpzvqUSz6br5lX-g1-HUGuiBGqFHRd-APsiNO_3ElQAAO_JOlDpG3W2vzHxTUZ78mYSYFX8XxMNqCwUvzLwmExU70Vy5NKjCUW-6TieC7oXIPbuqj2D6did7AjyZX4SajVE0vRMyucCfAEQ7nTbTDpwFMphdnhgZ7vEO_izagHSAPhNIv4Hw6cINzMe0d_N2ClbNGhAFK6kkjhMtuNCU7RteIEOyptg9aSE9wfpIjr8bTZTX8lSfRlycb_BK8nyYqULqil-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=uwr15gFrk740YiHJQQXHjYq3JRZ-2UmraIwuSW-D-8xqlVIzPh2TkkOaWMl7nuxLiIomDTBJUfkqWNIDLATGXDHy3keRUKxGyArxV9imD6SOz3zNLfNKo0qSYn-v5vZEZaY7P6sL6cPB_zndKjPQk5cpp_QKnpIT3Fc_u62tHX3q1WGzi5bCIL_lLPeRLiZ-U5RoZYhWtUCFx8xiW83Rx7eC8d1FZSxHNiGwQ5wkY0cfUXTRGDuRLmoH7cz1c61UCy9a9mFc3gvPapYyigXS3HAZERQcDoblVKbDiE7UXzmBj_m0Q6w2QuznZmg9MZFnwueE3wS4UjZgmHNOnKMONA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=uwr15gFrk740YiHJQQXHjYq3JRZ-2UmraIwuSW-D-8xqlVIzPh2TkkOaWMl7nuxLiIomDTBJUfkqWNIDLATGXDHy3keRUKxGyArxV9imD6SOz3zNLfNKo0qSYn-v5vZEZaY7P6sL6cPB_zndKjPQk5cpp_QKnpIT3Fc_u62tHX3q1WGzi5bCIL_lLPeRLiZ-U5RoZYhWtUCFx8xiW83Rx7eC8d1FZSxHNiGwQ5wkY0cfUXTRGDuRLmoH7cz1c61UCy9a9mFc3gvPapYyigXS3HAZERQcDoblVKbDiE7UXzmBj_m0Q6w2QuznZmg9MZFnwueE3wS4UjZgmHNOnKMONA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3KHT43Zn-NZMsLJJ0xlZM8BVZZNAah-6DhR-SMCM-F22dw91_gAZy8krld_3JzpScBrBgpRvmYX6Ctz1fU0NIzoPgcdI3argXlXd5c0u36UvorX6Oru6HL2nP03VKhHqPP86BMXRFB2I_uX_kk-SXlCPNWDBXTKQ7xnLiQ7SEJTVSzO8g-IH99pNb0cHSk12pKw6dbkt0o-NaTQAI8usCPJPJPX-vl-BAvgPHgNd0LMQzNAKkWhma5XiX3hNWDRyaINbpTYx7K-ru7FR57OTV5VQAyKl9t58G6q7E7F2yLVrngjFw6eTTRXkBwAS59Wn3PrvUobDViNkQ5G6uJRFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpU3jDewVm1gq6q1I4t-cQecM_NbYbFcHA3ZyDrmB2HF5ro9GyA3maxonUw__U3kaPyb66A7_1Z2qgG4OTiLNtEJWEkjeknB0cNR8oMh_77Ms4XII4-X0vXfYWoEtHxLgdHKxeDWJNm24dMXYHvT5FNcEOtSRxIKGROxruvB1-FIWRvXRVlerVmvJyukGIEohJYUVRjjuAJnBqeigNnzv73YLjhzHILcAGTGoNBUZClRbMgo0octmwRONB6d9iELGSNdyN-prFMS7uhmeqLRZp9nAs2AmjmeLf8QG4agpiNAKBhamdZCmU3zsRvLswQ7o6KZ6hKLWoTH25ozI9mO-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKvVYge8ZSNWExnoK2JTiUURHwdheUHtw5Ycv8DKylBz7dS8U4jZNwAW9diw1g6AbCTualOrOPMkiOKbiqxxKJ1q6di28-fhPJusxtjcy4HIEbruVKuWiUu_Vcaz8sESvcL0E5tRUamC-_SY0spoN0SCTfPVZfXhPV8YpkNh7HI6T4_1FNwp5fmGUrknFrwThVmUciy1wZYxDMA-TlRaLlHzShROAvEWPo6K5l0uAYmxRZ8_wE6v-3MtYZUlwlhIr1F0DwwOuukXr1ddL4Yys4jRY49sADKcGCHooS-9xvNk7Y3aUJX3HxlwNQtdYXYzBcLT5BHq0q7x3rb2DOUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=syI0dFfBkWvzDH8HkE066s1FEm-ExR2MuIJggK8Qd_9SeJiDv9uyQdBZj2TBYZE3mVycoYOHS_E3VBa3FIyuVJ7wFj01j2Z68EUpipcwcjSfxSvBfeVrRZxQT94Hd0TMWBjLiBURnGE22O9NRxnT_KuzqFUwP8rKwlwHJ5RmtaIzJudXsGuNl1vke5iFaL_DJj1ja6C0v6m8v7icptfQAnmvfulXi84e0AbeMGXt3roGBhQMJ3iP2M0AjlTKeTcLslOPXOon5k8ob-4TsEJBYLxr2Dlwzw8do9YhIgL4jO48ZUxDgtG00ao0uRkbFk9NGs1qsLGDI9ml2rQBqvP5AA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=syI0dFfBkWvzDH8HkE066s1FEm-ExR2MuIJggK8Qd_9SeJiDv9uyQdBZj2TBYZE3mVycoYOHS_E3VBa3FIyuVJ7wFj01j2Z68EUpipcwcjSfxSvBfeVrRZxQT94Hd0TMWBjLiBURnGE22O9NRxnT_KuzqFUwP8rKwlwHJ5RmtaIzJudXsGuNl1vke5iFaL_DJj1ja6C0v6m8v7icptfQAnmvfulXi84e0AbeMGXt3roGBhQMJ3iP2M0AjlTKeTcLslOPXOon5k8ob-4TsEJBYLxr2Dlwzw8do9YhIgL4jO48ZUxDgtG00ao0uRkbFk9NGs1qsLGDI9ml2rQBqvP5AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRgQ2dBp6m004_hM5jXqNhSX5slZe0ve7svmwKfXzlyOMZZtl3JIoioG0f1UHHeR3O6pXRuG-1qTooq30SPmCJSNpeCc5ZCSXl4oLze50l4qleoB2K1k8l1Mq3SQc7WHHT-eLeW8qx5mr8iPVNODn2JixO-U8TYV3oHPiQWB0vmtGW5DUkTinYk6QrSrhyutbPRkcdwazFMRIvxf-MbPzZgFnlmc6AiZU9PPiNE0-1SZK6PrDrsvmHcp1GFtW4n97-BucXodahee7uRLueMuZkKzWk4ZXxXfZlrfSFAslzoSKIoI9IG2tr52gajBBCDx7Hl9WmgLgZaXQxk2uuMw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSVK0pE670T1INV7DyLCPKUMSkF4r1Sbrf1ZZ4exz2JGWFQyzwpVt0o_zznYw9oAIvH9WDT-mWX4PCMkCz_DyYMxzBj2NXnqCGOh1fblGCOLRyNqqV-Z6vRWJaVuadzk4Ue30VAYFQFcYNj566RiBYUs-wh7c-K5lQTbpbHv1dC3pi8IMDi8TEJTM95tlOmmZRVanM-PCqLruGFh53AehUB5XCEnPp8D_TxFJ6eRBDCLLNpdbglB-sL5NW1v1HL0bD5uArqrL5RUrY0nHpMkJuG6NIZaVhW8TUVQnWuRqaG0XTncPyK0bH9gW7QzvSfUaYSngmG0jkxSj37D8OU5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czEAK4ZkIuI93ejJJYLCz5_kWVoWkf5Dghi9DW6Xs0nlcZkwaJenXEHUQYymhWvxl9SFAnpu85ro-iC2nFWNEFxhPLyKgvj6tYWUHdp3DuiEAjEcpAtYuMwRb7TGb5GlW2NJXD58kSUs1cGCZoY_ZPXq9ks8oUR45VU2reJFPWVq-ySZcA2xORQ4rjGWLjXag83V0lKijYiWKyqnbgLVtAKmRpvmi_QSPThgYmfcxFyPlpGH9jmXr5IagvmYyTfEU2HtzJ_YkZx7tdNvI7f8l5Q8hz1HDm8xsT8jkyRhB59OV_yj55IKhZhtM7wndCXtvcHGabaFw5yLpLGHRrnEqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1kjQLmthQOji45X9mTjAS9Cl2SK1aCE7tfhWcNjnrVOsMkKZpS1z-BDGoWxqwghgGYWGasQtri5vkOfTg2m-5OxY_PQjSTSM-B9kXzCkAeuPzvATQA7acoFzgSFchkQE_bem78x8Pd21F99l5wRTULzyN8u2Yv-5ILDgOoHull3Px8np4mlsbbR9Ao1zH9NuEK7tdHDcm3ZzXo9KxjOirEl55GjzVOigpjL4TsnMUuqwmEFm_hdhlLnNkJjMz3mI8l3U2s0oAS8E9t3WLSxqtld1tE4KiN-LhwKojb58RtUYZHgCv2UCxcgbMUgrhN9q4CIfQdPOPVnzOQ9rnkJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GY_uFQYAAvgaLGAukV_i-IaeeGOJkiS_NedtUOVeNANRh8rjSQjIM0cWyHxajHNg6P5bOuYkHqKqQ_1v9OWf5Rd34VPH3fpGPmsTgm1nElCJA6nMKPsy_V-RNxAN9Yt9UJhbHK_6F_wg9NxNt20wAzL1XCD1C-mCLmH3jT1QbVxFBzWDoBpAcq72NBiXOXmMnMLHrmFJRMrhM9ZpffXeGnQLftMnSsUv5JpgL075w5j17YMT-DIc5Nftjqu8Ky_RiTqqlVapc6duWxH1zlgbMJWaw5TZR7NUUwTwxhU1394qElYnxA8pP6qTdYQK5UUH475BksgvscJqpVrlAIIWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcaPZDjVgTP4R8JaXDP21awR0ZnCOEcJzPWQLf_wWq8paNPbEUi-2ZhsBDV13mYUsX92mtnBVfasZ5NOtMjduk3cdPxRDgTm4jIacVyqN71DvGt_J0H-IKGOpp9UMfiVgydHnSoim5BeHot7whd2qQdQ7UtJ8LXbF8zk9i0E6SnfiW2216Hl2nm5_WWwtvoQpy0pb9fJtlfq9m1xKuo-8wU21ylUf4tKPs8edAk4od8-hdIjm_0na8vxKupTDqCfDwgMJzMTBeOx5e-1s1sC8quZFJ-xyZmpt2oBn6wA7q3cFbghnOtmq37iE6zwxV92_YwarUpMmmhGPLTK5Pwl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoEVPENIfLTZe24qZyJACZ4u0nUulBXMQ72ZZkBn5duz2LEVr59Ii8Tg5qWk7-fA7nzg4C-HD21qEEROOC_zPugvv5hNOjW8pPIGDNCtvsMu-A9OgQLL0PGUjJfeVD-MqpGHchEjURXFPTIAiP8b7G2CYakrfXTBGTP0Iou7SEH_W13BAsk3k094viIfAE3w-jh3-XRlQDgR97obyDkPcdRLh-QBcagSXWbnGSHy2oJ5EtLYSwGxrS3ZtJxcYuorWWEAazhgy8uafGXl2dwZsPzyzHd2J4gq6Kikdq-7pVoj6q1fucs2vn26_aynARLLhwryf3o15B4Ige9aWMMvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKAjTWV77VSNK5699jbxF-_h7aLq609xwRz1rQwIbmT1zcNEq-Lv-9UZSiKj0YiyUtxvbAOoNIi8TQzER53NEAgs9OMPzf0sH6GT5bsDgTE1gNAiWfs3EWHjYcHBz06iNLWhX1636FACmJThSgylMd_xpwUYAjju66l-6OnzhL-o_H2iJz7GR6hdto9pI23K6F-yutVtK79pX-YchpunPLjlgla2Myuh28EX_I-rOC4C509HR6iFe2E6V1aC-6eHSxz4WcSmlDrhQnz81S_ayFxQrxPTXrivRSP3cHePW1_g6bG46gcmr_BUWBrcnew3IAvD2Owrv0JSC3wjJYIhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCJpxNymOys4gmbGUfx4HnSe5JDJDB5kcbieaspQ7LJLFo1vI0k7ch3nYolLhscxM39Kmq2ph-TT8oyZgdxGx-OOjcJmy1TvgScnmZ-GqmcwElq9l4JBdAJPCQfWRJI2KfQqdr6lPJp54l9OaTf4ZllXvmR7eoDXl-kU4GUNIbH5rawQUvXg9XCVZ2ARdMg4cX4uiMZOVKv1kahanavgPYiwmsBCFdBWtE1jhm5CwhC72C7ng69YCp4v0Ssaxbi_L-7C2FZrgZuXrsh7MJguXTLgFQbI-8bMU86wJgVR_XCR-91-dv5iN7-kswV0fh6BN_BbjTDF_7fEFXkEFYP9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW7pKmvK93okiEnNsMlawi0ZFlCuSpc4FTNylptsdPQPCGDfe8AD7w_4cqwq3lVe6xwqIWpv4cJbZOypX_4Y2zpi8jwdI87ZKpI4XdaA_ePqT-8ckKgI78lu6byJPu2mhwNbNrvUU6SulHbSMDP1MVU6HgJIfpqcq2fKYB26UtTgaHZjmcu4HTHud6Giyq1EXySsfQUDv4dn0k-rZ0kM1BvDt0AdUysMBN6RBBZdfSy6zBk1d1Z4cLOQa0E3LVUUfCQOJY5Qb81NU-V21ljjMpwiXN-ixAYZ7_Ps3rq1zbqdr3YMGm2K939bbQP9Of6FHT2kJM41VkyU4AadpBQg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvwVJtBzE7U3Tc88K9hiaf0mVtkj_Dj_ZPDm3oyd1HQ_4NMRvVVGpfRWosDLNDQT99G6NSzeCr6G3fdmEgSfuMkyxmPRrnzFYkIcZT-mMXYKvNS25H_0tt-RPVn7bFY7HHgrDqbkFBIWWtIzE1lMfBalhZJYxb4MAF05AnwZfGEkYeMA8g3epPA4mloT8iGLPGti6uZimhyYO7u5ZnZFk8QY_dZz_Vky56-bh0pBhVhgC_FbNAgwkQyuzulOz-cb5B7qHGk7xRb-qG4-qHrK3u-4wF5qkeIivoDE4FIqURtNO6jhA-f2UIpeQ6rViciN2mZrMG-4-iiP4C69qWh17Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFvl9Jh8zoExkC5xMlnLgW04DYYJ2Z-yRXdMz4lATXn-Q8MOSbso7b2_oXJ1DFto6HOdFSZmKgEGVxnp-bNmrL8EHMV-fbSSmS7OsymUcl9oROt8ipVGxR2RU3rbMS5q9C7sI5BvpdGTMhCzdzBX5cbyPKyvRhAAFg-yYwBw2_v77PBTuDDa64o3Iiy01MWU4F0Ea7czmOVLWP49kM9YEuFWjiPaYgWtP4lgi6od_Qbi0V7PpOU42hU8rsf3_L_Ob1a4F72DuNiJD998xJle9oIZNoZrn2IdYZx3tf1R31ZNfmbkT-dR2s4dnZDNk5TkiLiHKM737go5jKowRP6fBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PE2b6XM0RSZYL0uQb8dg5J2Bl4Mxe6wzK2Ru4UGVNAE_MH364KPUE5TQZ3B2mLdMacTtNgaJWRe3nmjBjkZmGr9A8T6_AsacH4lwGdyawlaXrGs-JLpKGMi-cPYlxBj185qHbr0qlfNk9VvDf17CXdWrIotPwYpSInp2dEmM-bZ3NRh4uu8YB-XoGqwlm7Jq95BAUpj9RDwPp7vw2SbcGAD1giY7E7ytIaZAxZ5Q9nuSau_RXC2SwhWR3qQGLzqhN2DYJnOJYGqaJ6Dy8dS5kkiblvm3rP-6FpC54H2mjLv5ww45LRsE6ABGVx9yA4eLSpf9DbhIPDw5NenJ_qrQpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=Tw8Tz5pBFNVaQ9-fq_WhYiyllY73RB92s3RhVz7V1JVa4RxMv7ldDS46V1vhsGw6p7QrfDz-Wroe_CwqLR5VRjgjInDLbOhNk6j1gIlPyqJKArPx6IDx2mgJTqtXVUhrqpgF8bRVfwLTZPK17yxXiz8VV75PK1wUUWzO6xX205f6saD6-nMSDW4fbspOgaJ6DAmL9jsX7HFN88xdXwYsyV-RIv3YvNjjjSkwZd8YSrMKOYk3Et_bxWnHHTVQjyYEnIIHblWYKQRJpS_m6nM3CTBpgGVTpt8udxPusrUkxuAxMRb1EM3APN3hNwEyPUR_PPWWF4GWwFQ5hXw91HHWjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=Tw8Tz5pBFNVaQ9-fq_WhYiyllY73RB92s3RhVz7V1JVa4RxMv7ldDS46V1vhsGw6p7QrfDz-Wroe_CwqLR5VRjgjInDLbOhNk6j1gIlPyqJKArPx6IDx2mgJTqtXVUhrqpgF8bRVfwLTZPK17yxXiz8VV75PK1wUUWzO6xX205f6saD6-nMSDW4fbspOgaJ6DAmL9jsX7HFN88xdXwYsyV-RIv3YvNjjjSkwZd8YSrMKOYk3Et_bxWnHHTVQjyYEnIIHblWYKQRJpS_m6nM3CTBpgGVTpt8udxPusrUkxuAxMRb1EM3APN3hNwEyPUR_PPWWF4GWwFQ5hXw91HHWjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFGnhsd0kThblLDoke5HS_hdLuvskez42EUODbq3eQmVRMvRIEozF95sJyLU254HJjrm92sZxW22cB2VrgRuNuGzJNIUDx35m69D0MwitP_fevge-lULex6Oja9b9dAYHOYLhYQPtKySlk1pOzKCOefFgsFDMhB3yrTQsskLg2oNp4pLp0L3LTnDSHj8FB8SMCzmAGcQXWsuRZYGvueRZB1z09VQ_oYzV5nlnnHnoBqFPWBV2lnJW7bJ-Sf_4G-FWQTxW0u6ep-A4f0F9uxbrDSiYXAClNYVM50E3qdX0yt0O-qxlAMki540xrk1-h4eg9w3yNXfAfcZdep6DHxJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 496K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lehmy3EpRQ_ZP6KXaffcowxFXimtolkdlh3DKvjAI-0jnFga2Q8V70BTW-918au7J5U7ZQI0wl5dCWS-K_oI46Q71FICgnEZRCvVTA9b6Ug9-UpuJp_TbrXVn8GyHX1FdUX07OdTrImQES40GYSswgkhpfl8TsVLco7n2_j3kGclKXBwnfMYh9ANiNeQlpglwuEoyEkkTdL1HTK-7SErsjo94wbgxeUbSe3Z9kIATDCyDsV2vKh7ILpBxUTBalkUM69hEtsaJvCam0kRR0rcMIw308-3Vc1xVcrIWCRGYIKaGMF1Cde4VbGR3_jJX7WQT_ciMA09kkh6OsKJtUJt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 481K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiHmuhkaLFQzXP14JI4UC0snoeYnrWzu_9MDgjnWK7MODYje5owdSxaHaCE7-k-5EES0hpvWa46ZZxdOT3Ojr_P7s6seI9S8xHacrtlNpFXvsPhpz-yvYIrVdbfvSjnO5n5dC6TmpX5_927WAu83qMZALH8eoI16mYWCDa7Hl10IchJcOK3dCTCnc5bnTtffTZ3wXmTdXcoL2lJ0ZrIpF0Uf502xmNwimscEGQUU_ln-79ISdH6NCbDDme3g9hrHlHpWZvm6Qgrotyird8MP-HiO51nebZO7y4zt4-9a4lg9MEYP6FrlUjbqFPkqinpDJ-zKMXXysYGgDFt5cXH8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cd91vAorVTt5S2Du4wNkg3mSVo-S-bH11cJZfIat9zKIrBarVAG9Qr5X11i_9nI5T5mEjC_htYB4k78aDjUTfqKb44WCyI3Ts4CNp5MJXpEtPnG2ErtTP92tC0WoOmzPMh6SjNXaTUp02m3nV4pF0EDEjKmktVed8e2a075XdDvWvU9VQdPYuXz3BjP61sJE2fMCoBylnDh28FYqc8rr7YsqV5OffMrTTN5ebF7u-aDCTOl8ajJVIr_rCFX8qBGg_EhT6cKk7fZ_JfDNJ6aGQVtE_aefKqmS2aWzZ3-wiXA3S49GWsQHUy1plsqIl6yptXkTq2KhYWfgwFfAW5jONA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XALFAXVlcGnjSBUaTa9P4crozbbMtwR_gOLYbe0IucE3_m3zmxlvZF3sD7k8M731lODHOmvuUapf7S7s4Um_80RfBnOHVWXWIOQjWqnJ6LuTtfIYYKAHa9FmsjRfwHxEe08W5jzxhtU2MkCTWqokxjVjdQJcNqKVXOU4vVVc_3rAMyVWYZs7tv6FaHnTL_y_ohfFcev4qTPQLwFZdLd39Md7m4rv257dfK6U4_0Hlya8gXfSCAJNF_5mqMvaOZ4YeQc2nXXohnFQahpBCgJPySjaBdCglpwYKnWFK-I_Uq-c7lMCQJqmE5aEqClgBrJ_QY0Qrpn6qaWe6nOV7ZXb8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 490K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=WiCNcLHqgH47Nv-wWpKIfGEaaVmleXXTwGHNY8C-8EWjOP19QOCPLfTIT71LxeUJImT2_jGTDd5B3M2Zz40nG9Mn73CG6c5aYopaBowukeRJJ-6gsOUupTm9AS4wQx8QKuF_-lP59Oxs-N0drq43fAflFg01mNSSBtcuXYZGgrLECYSNyS8JrDkHMiceC_b5l51e9iQcH1fmCGMBasPFyc2OD5BgP50eKOgPsjJ_lnLf1rqZpnD3Fcy4EOw5Pu_Zd8_Be0l000PWj07SmrArzuW6aVnVx7VLmTHfST-pTCTvpj_iwcLZ7o8LVGMrmDuWy2bcFFOrDCG85NLksLDKtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=WiCNcLHqgH47Nv-wWpKIfGEaaVmleXXTwGHNY8C-8EWjOP19QOCPLfTIT71LxeUJImT2_jGTDd5B3M2Zz40nG9Mn73CG6c5aYopaBowukeRJJ-6gsOUupTm9AS4wQx8QKuF_-lP59Oxs-N0drq43fAflFg01mNSSBtcuXYZGgrLECYSNyS8JrDkHMiceC_b5l51e9iQcH1fmCGMBasPFyc2OD5BgP50eKOgPsjJ_lnLf1rqZpnD3Fcy4EOw5Pu_Zd8_Be0l000PWj07SmrArzuW6aVnVx7VLmTHfST-pTCTvpj_iwcLZ7o8LVGMrmDuWy2bcFFOrDCG85NLksLDKtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaeMPfb_yjwRe0Ky3kPweq0yz0eaANoTSKYV6VW8mjAxcGnyniwBlXGhuxRQOdDugtv1a0aPTE2lJ-UJDerk6YRWR-rJt09wXz1_Pa2FQkwm1ViLtWQ4YPkqtpEfyxGtqoNkKFPI8RYut_roX9ff7MzYvaLp4OGOooP71BWFWbN6GqERpjVwT6J1l0n7vQR-IaO-ja9ktBfWAAaAQhSN5Jkl1VaQM8DJ9_JdzLsbVeA5mapiPbXG4F9uS2ZaQaNycI-mTdPBgQHpa5zAsssKnbNKYslmYkW5N-ri8J3ExC7duz8LuLVdXohWzDghUpUkdtgiQGThmm0IFHldfczZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFm6AK_jiupKLkQ7ljhgWrEFrt0i1_ad2fx4U-wA80JPsMMIYQidRoKRusub-xY1PDxXKm35IGJwCUxJQuM1rzsqswkcMMN9J3Bxp9IefW3loHXGdFpG5n1rWqGRPeBLRNg53-8iDm1gEtEntjhWTU36jaLvLG8K0_EUFWx8ZXB2ZQQ9JxAeQ_uMjjCH6a7jFKKyI7dyyhcMQH9zTGM56Hrc20pXJCwzTYkPnEcD5lxyXzpcRRYkWUVZkPWntg-KdNNcJAlURfuHcwgEFcRS_MNhDSp9fVY_yYPWmdO7KklH-R89xwbYk6W8OnaXs_deXIXSe4JsigrPJ9y-i2aD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=Uetgte9L0evzvmoLXOBAz--yrZknj02XVRY4nXNf50KR-DZvgD8gDfIfUcCcoiK3ihlZBRo8s0CC79rIDdF3Z0wyBILYool3pNzglQLKFaieM_7UR5NoEn0CJFuTevKo1BnO9FXfcV98A1s_RW17fMtvBctUu2k68FkjCpKlnNPWx4aX_0qzOJ5jhkwXnAQoMXDoQjtcUMW9-xgGH1udNqNdXby8rFt6K1qiRNKju2p0YrgzrTWJ0rdXw0wdZMxYYOxv7lvc41JdIpTb5HfTIuRiVpsPFQKW8EVTPwhVM6f-N64rwqsLf1FKaC4RdmsPfrcJwXnlVv332y80HHyTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=Uetgte9L0evzvmoLXOBAz--yrZknj02XVRY4nXNf50KR-DZvgD8gDfIfUcCcoiK3ihlZBRo8s0CC79rIDdF3Z0wyBILYool3pNzglQLKFaieM_7UR5NoEn0CJFuTevKo1BnO9FXfcV98A1s_RW17fMtvBctUu2k68FkjCpKlnNPWx4aX_0qzOJ5jhkwXnAQoMXDoQjtcUMW9-xgGH1udNqNdXby8rFt6K1qiRNKju2p0YrgzrTWJ0rdXw0wdZMxYYOxv7lvc41JdIpTb5HfTIuRiVpsPFQKW8EVTPwhVM6f-N64rwqsLf1FKaC4RdmsPfrcJwXnlVv332y80HHyTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDUTu_fOA7qzi8fdDCwRjuXUcvsMKBs931p0TQ-o_6-KwFVpGcfYzY3xeJZlQ1A5Abfcd02mZe4OSUkJJ1g3710r-oO2S9hHSU6crGI9v3c8Y7lsU00jTtd8loKjV5rI3-t_zQABsFDI1MAyJgydy0vg6UVVMysQ-jrgBOPsYtdH4IjBdx59KrVKIs0uKV4Ln_oVsi3wkL-y1UIIO93QbiaabEM-Ufv1PoAKG3Ks_Cj9lzHIiqDR9Wzyb1_dMGNhzcnv3_Mb2x07rmyFiKHcmnnoZkXiGSVjaZp3XLBX-NjD4pCCo_GkKHmYB920mtCpHit2rbEZZ_6iBLKog6b29Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvO5-pxWOVlI02Cgo3aWbTB8Q3IpZJH9V4O5p_cB87webchccwSJ9o66bKolABQUUdFAHgRlFf91Kths0MG-Li5r_MJFKcDG120gmR7XwcXlfhzKqbx0hiqc6v8rt7ecMJc3sM1YCdto726lqjZeRqhjV4K_Z1b8BtvvwNAb8M-eF2_EEaE9fGW1dZxPCzlp_iFjVpZU3zIZ6ceK1MxVr1OzaMUPfBZJj0Njaue1EZ6BhgIY1AX6Rq2-Uzq2_UoOH-uNaKFqniHAv4rpzsmFVto9GIunKzPKQtRQqVYrhhqML7xHTlywc5WqW8HrTmYiLGES2pB1h-EM6aUhKZaDGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_tMH6604WnPe9lfHYp_8unbEXUx3JtjiLTHC6kK5t3GRVnZdndQYz22ZwHwl2JRV2jOzUFnTJTdZ7fDgiFNENIVU1nT-wTdqBIGXYbBF0L_jpDAUES3druJomeie-gxRz083OBDXn0zjmOv6iOPjToeSfdmHbWUGo8zUxIl4NJ0RoMgQ4nO3u9cSr99NXt0qZVZCYJKWo8tL62ZcROUJYL0waaqkNarx5PwS6b5papZvybMRkubmRQNiZDhUgM8caNj7J2WJkI5aBVnDP8M2Peiz7DuCNj1L14meOgMiUEOeo9-HSg6J2orTU9tI5XB1gOVY7ocFJbj7n01WXe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTPswffrdJW4GUuPBVNc-qN5HXXYl33WaXNAF3rGR1PndGUAlQzN2t3-sESlT_RhX0b8DUWEwMKX010Vf9Up1o_XL18LKaNDwZztsxmO5JC1UqFleFr0oCtS4VtI-5NnmsvMStlnez-G5BgpJx6YmZX07SgcEI9jY6c2HNta-nlkBdyi3z4gifREX0G3CvDMIRlSYSLOkXWhzebOjdJJibfrsvC5UPcTk5rpLkiYXCYJcDE8EHnAnJMUPDYtjs1uT5UVieUTAzqy8jO3hsASl9tzZoCJ8RhLWwTS8UqcG8ylYc_XS-b3qp_D82UYiVN205UHm7zgkVPguAcs6hqabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=o-H0TNL2LtLKNOORpu05EqQcGtypRwC42xZKpz3_i-oTMDom8YPPLdH-HFwpew2iDFZhHnz5bPYKgjVw34Qaxg6ZQa0MHTW0K1TCd15k6LujHsm9lpIGmNLTn7W69K_LRLePYXVY7YNIe_BUU2jCFQbwiq-kI5x-hFnMCVSaEshMbFZ8IHLDW5irB0ZR7pUDKrNB-UY9KPhi0QU6zUjzyyZYUfgMVP8ReBBxQbFEtcZ4vtAPDBcIsVfrscapD5OCjKeJpCUHJn5vHzJZTMK-vPUikJfe6rswM7j3OJKsH6HnDkWaUx0fvwN47PFsYQaSWasxRKV1R2B6DfKtP4dLtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=o-H0TNL2LtLKNOORpu05EqQcGtypRwC42xZKpz3_i-oTMDom8YPPLdH-HFwpew2iDFZhHnz5bPYKgjVw34Qaxg6ZQa0MHTW0K1TCd15k6LujHsm9lpIGmNLTn7W69K_LRLePYXVY7YNIe_BUU2jCFQbwiq-kI5x-hFnMCVSaEshMbFZ8IHLDW5irB0ZR7pUDKrNB-UY9KPhi0QU6zUjzyyZYUfgMVP8ReBBxQbFEtcZ4vtAPDBcIsVfrscapD5OCjKeJpCUHJn5vHzJZTMK-vPUikJfe6rswM7j3OJKsH6HnDkWaUx0fvwN47PFsYQaSWasxRKV1R2B6DfKtP4dLtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C612CtQRCSs9aSKP1R1CGB8g9a3gMR_5xjk5HeJpwF_Enu2WP8xGCeXZ8Bi5ULQoeLmZReTsR1hvJ_Zj38ak17p7HB-jxnpKZayZC0GhpVa04853kKnxwxJuYDFB_xYbxj8T0zT-3hn2k_sCxT0Ii3JdHtHLfBM0jXd2CXYrNSQ4AIZtVvVENbbkFAtDHUDCeMCfcB6t86dHPVRqWJCAj8dmY6smJ6QKztVkHni263M6UtmWbmRBsV5ghVpP8Wbg_LxhRT1Ord1uUY4hVLeuVKcs2xjWndHuwfSLxrCRqi13TmgL24hguR70NsTbKsns5JRiq2j3R9I7nfAdt6AOsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idw7UMzt1MiMUzX1ykP4fCMdJPc9szWyRHWbGTG44Fu9ZReAvdwhHh_ZnDtqn8bw2fbI626pjxBMbuFfhmXt2j7WYQYUR5OlNsMfB4-eYE1KQgGDOwHyOUFcu3RdA1IsA4llVJPKTRX_SytjT2jc62YERFqowoPOiKZQwt5n_2bkiOIVc5DXrZ_4AS57eS7ivmn7Q5BwT-Tl4kCaozbibFmowhvME-pTAzQSxKPKq14Q1ZDX3Uj5dSHGyLZMR71GXEmtMnHna9-g5WIzHNjCk3kMWw4bK4o7ibQYXl0fy1mk39menoqqyQa_3weSMUgRrKo_tMUWmxu1i3k7CdMsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=IkgSS9pHj8rdjcdnZ5icIT_Skqq_3l-KOVc8ybLMX7GVoVIAoIIRH1nd-xY76Isn3qYJ1XEZ2gspztAnA-WqdvRYJvVuRzfjsF7huglP-njWFCu3Da8UcMvkSJPFgaP2eg7r7ovcwAHLBQGIwpr2jb0V7U8tUsP1A4WEH_HjP4tNNOhGu4kd3YXaO2duVRs-b729XpNI-mhTZ1PEIYxNbCEjoaPS7jIHuejhszetnwOVCSgY7Tvi9OnZ94NsFg7shkN5UMar2x8GwrYM9eeOOf3QblRyfqPFVa_mbrkTM4VTBWp6dC8mCD5lErV8UxMtSMBnmp1Wh6KxOBOPLpQGz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=IkgSS9pHj8rdjcdnZ5icIT_Skqq_3l-KOVc8ybLMX7GVoVIAoIIRH1nd-xY76Isn3qYJ1XEZ2gspztAnA-WqdvRYJvVuRzfjsF7huglP-njWFCu3Da8UcMvkSJPFgaP2eg7r7ovcwAHLBQGIwpr2jb0V7U8tUsP1A4WEH_HjP4tNNOhGu4kd3YXaO2duVRs-b729XpNI-mhTZ1PEIYxNbCEjoaPS7jIHuejhszetnwOVCSgY7Tvi9OnZ94NsFg7shkN5UMar2x8GwrYM9eeOOf3QblRyfqPFVa_mbrkTM4VTBWp6dC8mCD5lErV8UxMtSMBnmp1Wh6KxOBOPLpQGz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=aUi-nqgmwV4mJ72xxIRShTHZUdyrZrVQmeQ-0V6cLXQAY3_eU0R5PtmMU9ke3YfR0RyXoLg9o2ffHOH8CemVRAj8ihDPGeGionBg-PGpdM8gir5hCQHV3Fe-MbexPbDP5fYa0QfXdK3cbTk2HoQiJ_Vnjjb3C0TAHUpfkmL27HRH6nVBgJ8TQP8AuAoj6b8bIvKVDfZ5AzXCIDtH-xGFc50mtUM_TNnzBxCIGthzo0IN87djIRj4Ey_KgTIF9Jem0MUAPTPNA6J94x-wZCmTWlJBjwzSSCTXY78UP7-gH6xjia13AcKvfJ-_KdIr3jY8_OB3wvD4uXo1SAvLjcEO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=aUi-nqgmwV4mJ72xxIRShTHZUdyrZrVQmeQ-0V6cLXQAY3_eU0R5PtmMU9ke3YfR0RyXoLg9o2ffHOH8CemVRAj8ihDPGeGionBg-PGpdM8gir5hCQHV3Fe-MbexPbDP5fYa0QfXdK3cbTk2HoQiJ_Vnjjb3C0TAHUpfkmL27HRH6nVBgJ8TQP8AuAoj6b8bIvKVDfZ5AzXCIDtH-xGFc50mtUM_TNnzBxCIGthzo0IN87djIRj4Ey_KgTIF9Jem0MUAPTPNA6J94x-wZCmTWlJBjwzSSCTXY78UP7-gH6xjia13AcKvfJ-_KdIr3jY8_OB3wvD4uXo1SAvLjcEO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntQN_xUSC7hL3Y9tnLAbRCPWOMxceHlMs88ETg6PzuWFDUsFe4WIqoxXlTcy7d2TWgL2J5xTAqS544449_zscxLg9MFISyyCqQxQN11S2eoUpzPwVfEJOFb4kuEPoqrp3IgjaTs1g19YoWUOQl-IGovpEwoz2P36NDH61mzAaBXgt3gwq3gE3eCpoaAze_N0_wyVZxR-OpGN-wC4zxcTrUdlf66lfZZlcux_hd2nGwB6Dza1LD01CuD8ru40mTFyCjOmWNMIQo7d0nVmZ91K01jCw941vFevGSajgblTK3kanvB7kRDPNSobMkMnPXfe2at8KkWxOjkTmIWyK1rShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc7xFS8OYgX3PZu3_ecZ3r-pVMAYWxqjfG8X2iO4d8s7l5MPRr2lQDnbPp4aFeA--ALAycU8AkKuYcidvvYSsl_OMKT-d6YNRN2JzmkvzpNJ-ZSW3HdZi3UEJVPVupwB_5xmWRbIgJhSBByecuQT_yZcZB1e8dengybqicW8gCfg1zBINxZ0HctF0B9ieZHptHVEPz3b2IdyOC82dolNK4G7AiZIGvWIxvUFkLyvFxKg6o9f73p5-Mp0jwDcQotcf3giKZUs3XWUoHy1omi2y7A9UMe6rLXwpDrSgrlNrpZS9o0ssbdVPJxguSd-ZJuQ-xJre8z87T8AiRzFvqRhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bhWzLBc_rpE4Pgc9MGlRcGYPpiJwG0eQ4-9IMfUieb8CvZ1Ok5nxhyxhJ3zf8z0_VHRpJ9Hez3NKpkPB5BkDPeKehKQBnkiuqdEOvVpSwZ25o8hL6pNmd1DjNqnY0BFMOu_1vxDOeFXMKXGHZYUUnVx9wSOfZ2mILIoGJ5WY2bLKCGDUGVUOsKksNr1jmie2nB_wUrZDCLObQQ_rGIt_3uaYKRXgwNOKXfV01hU8TEDvn3HKxQjdP5iXHtMZ2Ir4djto0Gwl_LkYOjmRtQ120h_gpMZqVU6F1KTaj7m4wWwXucm8X1DOXElhjMYpVIRkLwwq22qz-gfOEbKNudL0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LfdPJq4Dc7pfrf0tLGbzF4q42Qa-c3_vNsjJu25BjaiU9c5vQwah0fIPB_Utl3bBliEbJMwmuo_WoPzZcj3Mkcxo83AqUN6HPptN0SZlZp9UHJ1m-YCskCkvUDyCEGVphjooAWf1-n6EAxiz5GvS14HL4AdJQex_rRpPqsM0KOQ1mJZdcbQ_4qxqdn2OkCVCDxNao90wfWsa4xGtvZINQ_zxjrMKjXyRHWTx-DH8OzDsInjNlCYrJ-mC3eEFZJbIYuOOwQzeRyczKrH6t8uZVXf6AiyuMXBU5jila4RxvuGd26YS5wExPMQ3TYZzVuz6dxmkcsBROXYWSrckRT-WzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pl4RTTJpwubL8sVdItc__s-6IxesBY1ZAqnmhSwEGtUCB4tNNhrrMpT1Slc_5QpLadBfaWWTJNBJ_Mj6hO7Tf0Bw204zBspfb8JwvHX79iUtmtydw2arGD1-Sb_y80hRpkpqW7hm3oASWuSeHNHb_cnfF0dSXgHy0fxX69qrmxAS8xAzeW94aEj4F0wvt8wM9htSr6OEYD78CosON_49ANvqrPqF30cRN9QDfLSggKJ6iQOC2S4SLLONGtmGD4twL_N6HynaYdCQjbxno78MshkkbQIGs_TXf7XdfF04E1d1-YdLy1vbfE0Kof-0oUgUjMWMaieeyPWGPfIdxuPIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YqCtXTsSrtYncMLaUJZoJE_azAQn2Y4ar-ycplTUw06ovJZiLcHqd9GehTkVE3lq7NH0eSdZGuldPbokvf2JQ0I-6wvCHNEWqiObfM1ppIwlTq5ZYF7CWTckRjZXWluyGZNaJ0b4pc_yfbpHOnN2M9QsizSqD6EoKtuQYnlmypXaQS7biXX2UX95yT4Ski3DLx9je_ja6S7Pr1d1uOCWKvAiaOh261qlwoQwuEJCxRifz9Mcj6iLv9LyMzoJKSJEEoYxyHJzgh0bYwbkYRIp_tJ1o1lK9bwU6aVgJHSrWn-tHeW2Xisll1h_E3KO9RbUCc_IeRcJuRlafdDKci0Klg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=XpJ2jQJFB5QMHNlMGEJJ4E_c_W7zQe4o_nevgmmFk88W8AMVgd96_2YkkfZxuwVTlH9s-_3GMnBXrMqTq9yg4TawA6RajioVP_2ykRG8JEaeh2FG__PoKs1XJ1nPtY-Zydhc1gsydRxn7lAESbl1SqoVUdzHMCrXSee9Per1IUwmGSU-LK1QttCqXaL1yM2IQ4HTW0uohWsBsg3k1UY4uBl-jSLDyi-2BnsOfvCPLL3zRybNLamRqoGrhMJbrqwY9HzmrOZ6uFgfzUS8xrHbHxmqWfNKvdHi5VulWP9F6DQ2_NEI4N_ei6vgrMKg9Bk75TSQg81FxsaydHNM73wLjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=XpJ2jQJFB5QMHNlMGEJJ4E_c_W7zQe4o_nevgmmFk88W8AMVgd96_2YkkfZxuwVTlH9s-_3GMnBXrMqTq9yg4TawA6RajioVP_2ykRG8JEaeh2FG__PoKs1XJ1nPtY-Zydhc1gsydRxn7lAESbl1SqoVUdzHMCrXSee9Per1IUwmGSU-LK1QttCqXaL1yM2IQ4HTW0uohWsBsg3k1UY4uBl-jSLDyi-2BnsOfvCPLL3zRybNLamRqoGrhMJbrqwY9HzmrOZ6uFgfzUS8xrHbHxmqWfNKvdHi5VulWP9F6DQ2_NEI4N_ei6vgrMKg9Bk75TSQg81FxsaydHNM73wLjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-Z0KdtZVmROwF9MMjREYD5j8ln_ot4xs4_NeHIQYq8U1ALIb2G-_MAZRXmMqnNtSBbSju_3KoPzkBfw1YPK3_BXZStLnZM2u89DEOUoBlW0CMhpqd9HT4LxWTGpofjYbdIovKsUwECKSghDLzt9L3WzQYRc2Oe_6QoW832I2TMB_Ms_Wxyw-UUEjZWsbnQeoFpQdDQgykKPIFPD5AcgdiUcGx-uiCEhKdCpOBjJWVFGE5f2kb0cQNVkLRnCdUOwfY396EqXNJXiBv0Qip0bYeo3Ld6Txrb90XCZFpcrdqhbc8B-qwC3HadZqwwIRDmoJli6pF0PkbqrV9IY8bjqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=jiIKfdLk8i-_1vVt_YR2slymU5kzcslRzkHXmuJR8yNzi85Akfq-13MkpgpOvMZWZyZTSfS5npulVrKa_mqPpr6zSgLwSEuGD9WXb_e6FaZqzAi-xEXIr7CbVBCLdGwn5DlVK7e-snDYliX9aFo-YTp2dZ7opcpf8H6d8fU9yHeXj2uWn5em8idvMZ-zmy4buxMimP8YKVhJA7dw6tINkLa_woc5WdnaVCg7gF_lsr1MZtcX0zJmJDrdaZgeisG9PZc8XoyShbCH2h2cbRrQI_Blgfcvgl2ydKSyQP3scOtSXXxQJ-viHmnfW1ICiUwrb5smA-26ybAdMe1z288Lcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=jiIKfdLk8i-_1vVt_YR2slymU5kzcslRzkHXmuJR8yNzi85Akfq-13MkpgpOvMZWZyZTSfS5npulVrKa_mqPpr6zSgLwSEuGD9WXb_e6FaZqzAi-xEXIr7CbVBCLdGwn5DlVK7e-snDYliX9aFo-YTp2dZ7opcpf8H6d8fU9yHeXj2uWn5em8idvMZ-zmy4buxMimP8YKVhJA7dw6tINkLa_woc5WdnaVCg7gF_lsr1MZtcX0zJmJDrdaZgeisG9PZc8XoyShbCH2h2cbRrQI_Blgfcvgl2ydKSyQP3scOtSXXxQJ-viHmnfW1ICiUwrb5smA-26ybAdMe1z288Lcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CaNPpjfWqi9AL_usU-T7vr1G4vuPatmpxOBoHFLdgBSCZvpCL_66z8DWc9DF_kcEBQX0NvXPJgyqJ9YqgKCM6RDKUvUTjDlbHRy5tKX-tBm4ldpU-lsmD5JW2Je0d_weeMxrx6VsUFX8e_JLAPjGST2sX_fBBojIO0RyLYMEauTVxPJGJAIo1bvEnnMoXzGqzSPu_ikOyc_QJCtSvg16YPT10cchzY8BuFEE-mutzuA_AWYFCj4NwtmaHA8sANFTSg_t1TKJks-izale5IOWMdTdi9KvNbfopwrvMl2EpA1nJ2EK0LBbQC36QiXvZ3mzNkfrW-I7ZDvZz0ctj5qLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aqO-fOwdvdPKlqzn1ccrbTzL3z6alpyCKNC829LBxOxyZ3rKWSbATE-Nvv9UbzSPXQf2AVbxJQ6lyzsGN26XjBmnK2oIcMqnwgHWRMydDRMKcYAioRUl4ndPMMWMjXCWOcTL6CC-YB797tFc5MJ3rtYxllJuUV9ZyCflH_dzsfNqnqdI3OSrb_fcw55mju8BDkrUbbTs4-aXfSQsY3_pBimvDjSFz3tg2hiKb2VlsUbtODzuCUTRejipcgJAfM83eo65n3_Pi-SemlNoqV4Z9gW0ITDJUiKpAO3OJBNKX2pO_wFV2odpMEnMNMPDXoyZlyO2_MQWuicWv881V3yVeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
