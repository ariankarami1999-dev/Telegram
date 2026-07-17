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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-672095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: ایرانی میراث پرافتخار خود را به آسانی واگذار نمی‌‌کند
🔹
مدیرکل روابط عمومی وزارت نیرو: خبر افزایش صادرات برق به پاکستان جعلی و مغرضانه است
🔹
وب‌سایت کپلر: دیروز تنها ۸ کشتی عبور کردند که کمترین میزان در ۳ هفته اخیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/672095" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تیزر قسمت چهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین حاتمیان که به دلیل سقوط از بالای تریلی و شدت ضربه به سر، روح از جسم جدا شده و قدم به دنیایی بسیار زیبا و دلنشین می گذارد؛ منزل و باغ بزرگی که متعلق به ایشان است را رؤیت می‌کند ولی عذاب دردناکی از دوستان و نزدیکان گناهکار را نیز درک و احساس کرده و در نهایت به دلیل سلام دادن همه روزه به اهل بیت در دنیا، از آنها پاسخ سلام را در برزخ دریافت و توسط نوازش دست مبارک امام جعفر صادق(ع) به دنیا باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین حاتمیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/672094" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عملیات ترکیبی موشکی و پهپادی با تاکتیک های ویژه و غافلگیر کننده علیه مواضع آمریکایی در موج‌های ۱۰ تا ۱۶ عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/672093" target="_blank">📅 13:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/672092" target="_blank">📅 13:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمله به یک کشتی در سواحل یمن
خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/672091" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8Fns_c0BffMaB6dyWZMIfLW-VuSxeEZKde8F32cMnw5bzg06dyrb4MwC1qbisgdi0UlNsE-Y6Ke6nxntCs466KGp_2AOWUJ5OoT9ePo96sFs8qUX42zPiafnHp9tq62RyGOeMqf8DTuWBQIinYJ3WtX3Wk3PwnZrGESqsWWRDTIGXwDe_sJvCd2Rlb8uiyCFvKCdH6dnANYwTb0G1EJe91XAw14DNo6WZPMrmoDTlfLvqWLzwofivgzzW4He3nJlNrSiHcGnus3gT74SfWSv4jTUftq_GxGCDr-1NLkwU9trkPt9VNuCDclYeCsSuAbrpT2EqhWib7ff1PJQvyfHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه‌های آمریکایی‌ها در منطقه باید تعطیل شوند
🔹
ما با پانزده کشور همسایگی خاکی یا آبی داریم و همیشه مایل به ارتباط گرم و سازنده با همه‌ی آنان بوده‌ایم و هستیم، لکن دشمن پایگاه‌هایی در بعضی از این کشورها احداث کرده تا تسلّط خود بر منطقه را تأمین نماید... من توصیه میکنم هر چه زودتر آن پایگاه‌ها را تعطیل کنند
🔹
بخشی از اولین پیام رهبر معظّم انقلاب | ۲۱/اسفند/۱۴۰۴
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672083" target="_blank">📅 13:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مسئولان امنیتی با پرونده‌سازی برای افراد تلاش می‌کنند انتخابات را مهندسی کنند/ گاهی مسئولان شورای نگهبان فریب می‌خورند و به نوعی رأی می‌دهند که منجر به رد صلاحیت برخی افراد می‌شود
علی مطهری، نایب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
گاهی مواردی را که جرم محسوب نمی‌شوند، به عنوان جرم جلوه می‌دهند. دلایل رد صلاحیت آقای لاریجانی خیلی سست و سخیف بود و در دوره دوم که ایشان کاندید شدند دوباره ردصلاحیت شدند که این‌ها ناشی از مهندسی انتخابات است.
🔹
گفتند شما در نطق خود گفته‌اید نهم دی اگر باعث تفرقه شود دیگر یوم‌الله نیست، بلکه یوم‌الشیطان است.
🔹
رهبر انقلاب گفتند که اگر امام بودند (درباره موضوع حصر) خیلی سخت‌تر برخورد می‌کردند. به یکی از  اعضای شورای نگهبان گفتم متاسفم که شما با این افکار عضو شورای نگهبان هستید.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672082" target="_blank">📅 13:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۴| روابط عمومی سپاه پاسداران انقلاب اسلامی: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672081" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7D8s4m-BiR5gKF23Iye0rGVzqjk5Mk7ogWUqzd4r7EzgyGsGvC8BWSazM_tcClOHAFq_aSBF45K9DtaJOm0cXgc3e5ioElxP7p9bJ-bBidGT5wmXmywIibAcst8xvnf6tlXhdRdp066JgispIQ8tS06uKnBwdNa2iD2VE0bQftsTWs3SyPC0QcKU8t1LgAfaGURN9BYLRlfnr-nxA-RwWFO6_HtiVgAlDCnqLdSmtE24ZHMnkmzlbCARpVsbxX6ru25VTqrFv4G29PhRDI8hmzQGxz2zLjNEJu1C9XseWZ0THJtPgZiz7v100UC3lbT1qiXgJ7h3drFj0UsG-OSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴ خاصیت سیب که سلامتی شما را بیمه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672080" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت دعای سلامتی امام زمان(عج) توسط رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672079" target="_blank">📅 13:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSS4IkDqKDFdnOw_SE-Vx5jV_3S0ZhZwD7vYATOrMWFPPJ0oPZ6Zzpg0RRY6gE4w4V7vaGXSDsiaEsiGWNt7VTz6f9_TJbqINQU0P7Sz56WCPe6YeoQa_YtowEaDLBWGVzkw7xgIJIdOHhstAIMmgilv1nwg3z4NaiQbtprXRo6HyHjw3QMMcUA3KUbhp1hqlXCBYILL7lmXJxUUe0kxqUHiZMztc_REnAOOmv1JxIz0wKxaZbs__RbQuEnDKboN-2R_tNRIDx7wUlamueWKnNjaYxJjv4x8fT0JE77Nm8UlwdmyKrV249F_uXOd6091zEFljecfeGNqChP0hYX_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشاره عراقچی به جریان نفوذ اسرائیلی در امریکا؛ همه این‌ها به‌زودی برملا خواهد شد
🔹
به آمریکایی‌ها مرتبا درباره «نفوذ خارجی» هشدار داده می‌شود؛ پس در مورد کارزار گسترده اسرائیل برای فریب دادن دولت آمریکا و کشاندن آن به یک جنگ انتخابیٍِ بی‌فرجامی که حتما پیروزی در آن نخواهد بود، چه می‌توان گفت؟
🔹
بدتر از آن، اسرائیل از پول مالیات‌دهندگان آمریکایی استفاده می‌کند تا هر صدای منتقدی را در داخل ایالات متحده خاموش کند.
🔹
اما همه این‌ها به‌زودی برملا خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672078" target="_blank">📅 13:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اختلال ارتباطی در ویسیان و معمولان پس از حمله آمریکا
شرکت مخابرات لرستان:
🔹
به‌دلیل اختلال فنی گسترده در زیرساخت‌های ارتباطی، تلفن ثابت و همراه در بخش ویسیان و شهرستان معمولان با قطعی مواجه شده است.
🔹
تیم‌های فنی در حال بازسازی شبکه هستند و طبق برنامه، ارتباطات ویسیان تا عصر امروز و معمولان حداکثر تا بعدازظهر فردا برقرار خواهد شد.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/672077" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندان خود؛ به عراق سفر نکنید
🔹
سفارت ايالات متحده در عراق با صدور بیانیه‌ای سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/672076" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672075" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تعویض گل‌های مزار مطهر رهبر‌ شهید ایران و خانواده ایشان در رواق دارالذکر در جوار حرم امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672074" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شهید لاریجانی ساعاتی قبل از شهادت با پزشکیان جلسه داشت/ پیکر شهید لاریجانی چندان سالم نبود
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
ایشان جای خود را در خانه آشنایان و اقوام به طور دائم عوض می‌کردند. افطار همان شب پیش آقای رئیس جمهور بودند. عوض کردن مکان‌ها به صلاحدید دکتر لاریجانی، فرزندشان و تیم حفاظت بود.
🔹
این اتفاق کار اسرائیل بود چون ترس داشتند به وسیله علی لاریجانی توافق و نزدیکی بین ایران و آمریکا اتفاق بیافتد. هروقت احساس کنند قرار است با آمریکا توافقی شکل بگیرد، کارشکنی می‌کنند. دلیل اصلی شکست خوردن برجام نتانیاهو بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672073" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672072">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی والیبال نشسته ایران برای نهمین بار قهرمان جهان شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672072" target="_blank">📅 12:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672071">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaQg__fJmj-1Pv-uLDWThEcx0m3K-N6JYllJhd3pLK_MBrICxwPF50k5LhCmEfkkTSzJu_o5uwie20NrtzOUmgmRG-ym6xTx3AZxRBIucuBUhg9DumGchQNewnkmiS7QRpKdZaRvCBe8pGlo4ZpV9mw2biAIDQTzs4KwlwB1JTrSXCr0BVp-n-Lc0yjL2nPC498p8rIBvgmcEP4FvSAunzqQvAPi1f0scyJDZpQ0f7QjHbp9CddSM5aoh586MtNEs8M5iGyM4EFh6-3tG5XfPs4Q7kLy3YkgMj4y_GiE_YWgMFFByzAwu3yN6NcxcFmgnNINevKQ_VOj670beEe87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام لانچرهای موشکی مستقر در اردوگاه سازمان ملل توسط ایران
🔹
ایران در یک حمله پیش‌دستانه، لانچرهای هایمارسِ مستقر در اردوگاه سازمان ملل در کویت را منهدم کرد؛ این رویداد بار دیگر نقش پوششی این نهاد در عملیات‌های نظامی (مشابه عملکرد آن در غزه و یمن) و فریب افکار عمومی درباره ماهیت سازمان ملل را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672071" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/672070" target="_blank">📅 12:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672069">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گزارش وقوع حادثه نظامی برای یک نفتکش در خلیج‌فارس
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه میان یک نفتکش و نیروهای نظامی در آب‌های خلیج‌فارس خبر داد.
🔹
تحقیقات برای روشن شدن ابعاد این رویداد آغاز شده و به شناورهای عبوری هشدار امنیتی صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/672069" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF48efWsOLelUaWj4QWQZUql0q6TNDWtbzaA9r_wqrEj-W3-VhT4aZAOig0Z9BJrOe3VazUIRF4ZkdWcVYGSw1yJtnNahO2xBNIZ2-FxbpIN93SwJ_E1D5YLZ3scb_UJ7HEOIMZlL0Lymq7pAaHtpqaS3jWK2Rj1WMsESgheTekdjpmZ9V0pzJk8yIqy2A-WGpMRU2QRs_IcvChlHvlidUCJevO_78UssHE_7G_c4KknVNm5IfWTT7E8co38F2_syAqCLkDEJcWt2Hn0z8YJD682h9uhtBWIqmhrOZt3F23SbtBpQwXNKm0C46vXk1MIW0SKSJpXAoqa8PXayY5f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد
🔹
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/672068" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وقوع حادثه دریایی برای یک کشتی در جنوب یمن
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه دریایی در فاصله ۶۵ مایل دریایی جنوب شهر المکلا در یمن دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/672067" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1DRes35gqWz5Lo81xponQv1iqmDtl_ZIULBHg3PDWlALDDtMxca4Hi1-bGeKpP6AsDKnTAzeJlepOUdkRaSBUxEvsQDlNGpWl7isTycq_SBlp2_cwGqYaaIJiN3jlwaRTuwvbpw0Js1CFM3taxK98La53HgsGdnnbDojc26GTfVmPy3uA6AzOWVCbMTmqIyILzlqOCaptNjSlpILIWwWJqQ-ffnNT85Dpbq0WVx9QYeSHqO9jTecXmUs3mC_qEviPOoAvpr5lTbEnhan--PRl0_2egaSPdHYVDrHif7xDh2FoOLNmR2lqb9-AnuQ9M49k4bUZWi5Rbmbkv_wrUphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBxFyh31G-IXcoUa0MgVxkrO6FZmlL-Ejz398Uz6jXnwEc_T4rqmJVNr8QF-aTn16AG0kVjCREuvdsn8LHhJfzsKSZ0oUh1UyEUZl8Bgaqtt25qH_Qsc4ISC7AujY6NDCejDyvY4HEO66S5gsySURKIbe7pztyTy8IhmUCk85QjhbdLV3-ad6XPTpy5bZ1pFOmimoS8rfru5QML4Inpgw4djFmHgUAKmGe9w_YfBFK7ClmGmoJT7Z64hrGVAZdALK2h-kOnwGkJ9eNWskXPhDoizH1h3vxTQcD3U0NXRPPeOHAxeiftriqARGbegvWUqbSr5AWY3SYnu3TfMBqlANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4cQjdWi-ZFv9CcgNX_a4N6Utc_0Q_gQqNATFfU3DkZLeZSzLl1bGP28fCH7Iptt3xC5Hgep5BnR4Pc0OCoPat2BoGhl3JKP_gdLLtWrz02rp4noZX1dZBB1PKwyMcUIgQ1nVe4zWLym0F24lAvGFtRdGgsigkrBiZnbTeAFtYHjtg3o8wl0LieOev4iu0VA4X-UsFFtrGe9Qx0APSlAOEMqObJQL6Tu8fjF8RXq8hpfNuuYBJsasMOKyZhxptTgWgEBn1vrcnI_xfWG4DpeKxLuGnn4mVF6xAC-tnD4ZL_OtDIf9O-5KCOdUXEu30xIXAFbQuIEU-_15B59EP2R9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8cUuZWg3AM9YUOY5FTv_MI1nEyX-zGQzKP-kTv3xRS_MVq1I4ndT6N5rSeRNnV2NqjyLZVsWQqpO2EqgYq1jD2LY-IcvTUoQgra2NZGJet6sKWgacMaiBBRNj6NBD-f6NIjAGhjqmjELMePpcxknFH6ZeoivBpkKErTqpSnc4Vfbl35bwuAwXlK3ctjQs-kfAB3u92fey46l1OPIxQ1d-nJEmjzteKKPILCzRI8bIHMAZXA0MDaqpIa6GsOiocZfpQJVN44qI1sThq8-XjAsA_UbSW3J5t2ClmoQE1j5fMtWXm0yqP1-Y5lgOErp8gbgwTzvCDjwV6UIaWhKJ__ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlX-KvBf-k9vD3QvcldF5q6zLQkEmffFgk1Mc4J7Kb02R317Q8rkdQYFvjPH7920pPwBouyQG_E5uuURe4bDkxoIzOxoozpxKA2pPg_SJT2NkhX8qI3tFnpNrDSqaz9GbPZ-QCarTM6KGgYMh_SR_89bjpf_KwoTfkPLbb_W32Bmv1_xngJS3KBp-edTlTmrbmouUXrbnimNesT9IB9uRtLx1aqWu2ZOdQC2rsxsYEbakl1jAiE2MAovxt0Vt_zeDJbIVofCMj1Oa0JdUkKww-D8Y3dTvX1gAa4vqpV3Itl7c6IWZT68wlYTZmyGqz5r17ojrzPUjJ9Gc857Xod4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV2tFHKkbYQQA-ymqmXwipAlT4n0Nu87-ILWGRjQG9epIjBb0qiSYVh6iRTr6FtnB0OQNaYUh9cTB2TtWhEsf5IsDhIikhl_AXThHWokmW3gyMKBcL2F84hJIUmPJQdBLR017z8FByIlOBaLRW5f56SCBLg1PI945exe9aPzBENln4JvTxCMTpTJ9-rCGtmE4k2rTiXqZNz8kRlDtX1wvjRNok8ZCx-p1k4PLn_s4tX-wNGHxuJKtaTICFSJbIpe55UvQBxASBSm3NPmTo7XT0L3N6Kf82fe3T1vwYlDvO_QQTsZfLQVG9Ki69kcsx3p1Wtyn5IPb-q3RvGwyBN32g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/672061" target="_blank">📅 12:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: در ماه‌های اخیر که نظارتی بر موضوع حجاب نیست با موارد ناهنجار مواجه شده‌ایم و دولت باید به این موضوع ورود پیدا کند/ ایران قرار نیست اروپا شود و نمی‌توانیم به برهنگی و بدن‌نمایی بی‌تفاوت باشیم/ قبل از سال ۱۴۰۱ حجاب در کشور وضعیت خوبی داشت
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
حجاب یک اصل اسلامی است و نمی‌توان گفت هیچ نظارتی در این زمینه نباید وجود داشته باشد.
🔹
نمی‌توان اجازه داد خانم‌ها و آقایان، هرطور که دوست دارند، لباس بپوشند.
🔹
اینکه مسئله پوشش در خانم‌ها و آقایان به تدریج به برهنگی و بد‌ن‌نمایی تبدیل شود، چیزی نیست که نسبت به آن بی‌تفاوت باشیم.
🔹
برخی اقدامات ستاد امر به معروف مانند مقایسه تصاویر افراد با کارت ملی، ارسال جریمه به در منزل و محدودیت‌هایی که برای تاکسی‌های اینترنتی ایجاد شد، ضرورتی نداشت و جامعه را تحریک کرد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/672060" target="_blank">📅 12:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIe5H-fG9msX32QafKFeS_hU6XqtPR6WtJqgeA6SeykKwDjdUrqIF_RMhRoEKdDy750fWY3aYDemT67RQWCaIl3yN_9JOUj4qyhnAledj_Mb_QpyaKxrGb-m5bXVq4RJ0eFSMQyxAlNF8mriwp8K3-OZD9h2hWI-j6YlgbGygTDNrYYyhHefvgFjpbGNuQMaO8un9gKuOnxnEohJFQhAfFwrBHQAqqFhM8Xj9KQA3EqCj-vDNAVGx18uuEOR3jzOVUANeENaRpNos8XN77UbnIcDA8ST6-z9odadh6DNUxdMyuJv4lVnsD1YB3MkYcSqMnEo_CDpOcsR1xVvcmhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مطالبه‌ی جدی و قطعی مردم است! خونخواهی قائد شهید امت و مجازات عاملین جنایاتی که علیه مردم ایران به وقوع پیوست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672059" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd3kbcTztlDH0i3YCn2D8OiNy_Nlzbowz5qgZunoqKjG12IKEzJA-wx2KlmsTTPXFnlgHRR2xgdzQwA6GxGScXEbX7uTjaPqrAvn3oVfk8pBuat_esJklfJ1hcprs4oe4_c8uSpeZAbTOj9s2x3xdgkHb0U7Lm6yyfutcZhRM3buCB9BDEuOBc39rVUvGkQnNZrbIMbdOUCNB6C5HOGxLDfXgHPwMAdi2CGB4dvQVUtih0nJlihzcmil3Se0yxvG3hmYNL5XjLA5zfsqIkjwbsGB--X8Mi02---425Jwns3-GdwRoaXorS3w9KcXRk6tS48bJlaAgMP-GGdOrrkg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا مدعی تصرف یک نفتکش ایرانی شد  نهاد تروریستی «ستاد فرماندهی مرکزی آمریکا» (سنتکام):
🔹
این نهاد مدعی شده که نیروهایش در دریای عمان بر عرشه نفتکش ایرانی «ون یائو» فرود آمده و آن را بازرسی کرده‌اند.
🔹
به گفته سنتکام، این اقدام در چارچوب «محاصره دریایی»…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/672057" target="_blank">📅 12:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
هلاکت ۸ تروریست کومله در حمله موشکی به سلیمانیه
🔹
حمله به مقر گروهک کومله در روستای «زرگویزله» منجر به کشته‌شدن ۸ نفر و محبوس شدن تعدادی دیگر زیر آوار در مناطق کوهستانی شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672055" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تشدید عملیات سپاه در اقلیم کردستان؛ هدف‌گیری مواضع تجزیه‌طلبان و تأسیسات گازی
المیادین:
🔹
عملیات پهپادی و موشکی سپاه علیه گروهک‌های تروریستی تجزیه‌طلب در اقلیم کردستان عراق برای سومین روز متوالی ادامه دارد.
🔹
این حملات علاوه بر مواضع تروریستی، تأسیسات گازی مهم منطقه که با پیمانکاران آمریکایی همکاری داشتند را نیز هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672054" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcF6-lYdCN415gJfRJ_Yfxofte75fIFPJOEZ2fr8lHDun4dvHA7leYRB1pkVBJAtKouAWRPczYI44W8EJHEYtOGljOVhpYe1xIBr7detyP4g5wPxOb8VEh9ZMkR-IHtNn4W7IFtRf_DXLsBA6AcQd12UyCts7LZzwONbqhvI7gAzeBeLkUJNe2ZYHX1jvSOWfBOnzvQuiCTrYR5M8kcVk_4YIYddH8C7RsWni-_Q6BnKAURHEH9hVbNDZSzlTagZ_QG4ODg5rehj4dklA9fzpm2wNl2c3VotPwj0tC0QFDXBHG480ZlTD6Z-NxQT2RYIspwQYpoZK2m6dmlxU6p77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فصل پایانی امپراتوری آمریکا؛ ترامپ و کابوس جنگ زمینی
تحلیلگر آمریکایی:
🔹
ورود به یک جنگ زمینی فرسایشی، تیشه به ریشه هژمونی آمریکا خواهد زد و فروپاشی آن را تسریع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672053" target="_blank">📅 12:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672052" target="_blank">📅 12:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr7R3WM4XGK-kq40X6KuJgy4WFISQmMck9zRp9YaOrKW1omY1TUd-ZIJG5AWCeA8gtQBCLZcMp7v2rzU9KxIjcmmWN3am_9Pnb7RbNock2Z1Gy8V3t71XQotE-LQKZiXZAjfXj3OU0TceDN22AQgMXRNi5ZEf--owQ9aU3WBi02y-km-_sHrggZdyF5KC86mBCaoYpSUtjujOypLvuOZCH7nXNxB2CQ_DuAvLB5-e08NbUb9R-bVw3RhrmCYjt6OYv9s3nC6riZmBJcjj7Nlxt_PgIuQF0UEoOyVXntg1Jb_mUcr52ww9geS0ZgpQPJukPLyxI7SgmqJL5L47RWm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYM04zD5XPSIUZGr_ZjwfzoH37bXt4ZfIksjvLYd6kTQRJ9K8A93o3N_IUhyEYwtW2kyYd9UL9ZNP5JXRzkmluj7n5npKgrHC50GbA0dNn_lrDA9bG7lp8L94z7G_1NgmoKbDMfAuKTwOHIlJ1iP701suMtRDQcSBzcO2gVChtFx3WEeeB21ESgU7gGcAVY8xvo8XBj6iDv0FsyQHPJQgI5wyg4Kf7wy1hOm7tHkNlX6EZrpUWEWI20Xt8l1bLdxqQSSdnX-B0u_5CTGALDerJ00K7imrjo6YuigxMm7TQWZuMoLFO3jYEII4omwswlMWHjXVCE7pjCvbhApzYRjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vtZrQIkzZa9ahfCOm6_w8srsqw4LhqFdPxcJrBUxSEggAu9VK0l7a9AzzhRMOQpFiyi9oBbnCGxhq0rjSEVGqEMJWScVVS_-lZzKhZzFv1Uv13nQU1ti5QNjh7N491XUliRMHftdoUC5hdWGtpLGEcM3a4PDphKpXDQLcYvQvdfOiEX7DHv_lzx6UHl7HmPvAJFLKjUa90Cv8e0tl4-peL4H2TH8fnJHfJQS1CqJW7-2lVJU2hEKpoV7WVvRkY1qjrmYlu8NLpuxG_YkqfSvF5CUZd62GRprYjuEbd4pPECrr2y4ns4TqSEaMx1-DXSqAmjiNzLGevwOGmF8n2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjjS71GHEWN_QtI-UmE2ap_AoFtzPUYp5Aj3_w88WGRCb682T1phRVdReSbQJjfQdDP_fF3k2I55AmdQexOd8cwVqjpANCFQms7UsvzD0qBFKAy5B3gxcmi6aWVvcseX_9PMVPyWTEUNGqUSdEq3LDK6Vu1wz2CGf7v5yqaT995wC0xzf4yiPFmZ22oQ2T9WiuQFeVpeNPqCzWDuZz62pa9m7I4_fyRjsbvZRWyZr3Q-V9CH9aEvHweY07C5occOyEFjGn3u-C6HpLPDtULftjWdayQhW3KDWSWPvl8cLthe9RaCNg1PxJGEL6id723N4fR-i02yWSchfe6eXosUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کوههای مریخيِ چابهارِ ایران
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672048" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛ یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672047" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
♦️
سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام سکو و موشک‌های هی‌مارس در کویت، طی یک عملیات ضربتی پهپادی و موشکی چندین محل استقرار نیروهای آمریکایی و ضدانقلاب مزدور آمریکا و اسرائیل را درهم کوبیدند و تعداد زیادی از ضد انقلابیون و نیروهای ویژه آمریکایی را به درک واصل کردند. عملیات مقابله به مثل ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672046" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6Ks5DTIG3ibACpHCoertmTSyaJJj7hm_Dx0dXki9KqzBr_dxVhYycAtZXNy9HLjRZzmcFVXKgNYIAZWmZv0isr20q4MJHlXwZZD6DCvMufkOy8sTLJHQOz46P6pXt_7t5M8kwnPZjgtIoTBoyf94SCgj9lZfHcsuIwAAK_-qkBNOmycZk4UObYp956nswmGKOZ7s4_ORvR08jftAe5qv7JvWDFTYEUNsFGmlQWjjFdQKxOoJSS9Sxq8H60Weyd2ecDBSLo7XdMG1EB-0l_g6zcDzl1I_OpIWJOO0eO_FTJaghRb3J399_sprL-0ggELR9QgAvzbWWW0NZiJPfQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: آمریکا شب گذشته وقت خود را صرف بمباران پل‌ها، بیمارستان‌ها و نیروگاه‌های برق در ایران کرد
🔹
در تهران باید این پرسش مطرح شود که چرا این پل هنوز پابرجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672045" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgfqhw1qyNVnB7_eRwJ6CqKUZ6u64-QOakqUM2FcY4BxWSpOvkzrZAHp1yDALMsBGvTVRpP74IMJywEToVyq_9kNhIxA8JkDgpWRVd0kk1HpFXnAAU58VAhz4jCJ0B5wDhVW-WhAXkPEHkkOeI9KRIM3rn7__EBh0sBuhfhNatcANKt27MhOmJWI59IV8K4WArRW6x3YOpAb_rBhjHpRPB_Trup17gGKJSKM1HjbQViGmbuJC9-SrfwKsF_gw4FETImMQy-RGqHQzwnFwW5fx9JQfpHRM705btdvuQrPt7pYlQym-mzEuNzx2eIcCefH0bWLsadqO5tnVi8k7k8p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: تخریب سه ساختمان در شهر نظامی زاید ابوظبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/672044" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت به سامانه پاتریوت آمریکا در نزدیکی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672043" target="_blank">📅 11:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم  روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672042" target="_blank">📅 11:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم
روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده و چندین جنگنده و سوخت‌رسان آمریکایی را منهدم کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672041" target="_blank">📅 11:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
قیمت بلیت اتوبوس‌های اربعین اعلام شد
مسیر تهران ـ مهران
🔹
اتوبوس ۴۴ نفره؛ ۱۲۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۷۰۰هزارتومان
🔹
۲۵ تا ۲۷ نفره؛ ۲۲۰۰ هزارتومان
مسیر تهران ـ شلمچه
🔹
اتوبوس ۴۴ نفره؛ ۱۳۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۸۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۲۳۵۰ هزارتومان
مسیر تهران ـ خسروی
🔹
اتوبوس ۴۴ نفره؛ ۱۱۰۰ هزارتومان
🔹
۳۲ نفره؛ ۱۵۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۱۹۵۰ هزارتومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672038" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه فیک را از اصل تشخیص دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672037" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU66h9au4Dmq5VGpMjuqfTEzWJjj91Q9FH-s85cHAuPC5JeOFkG7sm9p0ZJksBkEW1xwGKykhU2CcsmNzRFFPs5VnXwX3CETPCG022Xtsy1u8GewmdkeWVqCAbSML13JjKZsvWmPVNGsy_de11Sl8W37wfYnK-DUpi15UWjeRvPzpZoV5ffNk4iP2Nb8IjPkxTuSzwz8Z2p29yAafN6uqhtEzhoCun8oVnK9siviu6NS-wz5WKWQE18gmkU28ax7IpHNz4iVhDA3_YWamsv4Jy_u1IuQ9r4fnV5SdIpxiJr_QUYgi40bTfAS5FpG7mdZGvFZ4_b-Q6uifyh8_I-FtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYdnfLLa9LtwFVxDMm-c5GWuEPF8oeEwKNcimv6kSXwDYlRse2hwCST0nsTHlYV4k8xVYPUZbO8rEi5fXemf2dZl_dTLgoh3lUDXxG_JyWvXMOnFGv9-f9-KWSR5X_5tt1q1EIu12fjqaMd7drKe6CFbKDfl7rFTjstTkZ-exiwW5m_W9gtkD2fMaGVKxxG8ER17b6MaLAsrD8wvptJAY3sKOP_A9_8hx0BTJIUg4Xp6pY2DsUiK0t5HZbvOe_f6xnNbMBVZ36E630EorWbqeD7vbuSftOx-fC7t_RRcFrWpfkc7vBGCda1X-xr_XcyNdnDilib_vA0-thYCh-YrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Uvtu1E5WL-r7uUyw0G7r3WhwEw7q8Sik_Ls-7B6GstkY6J_FW_65ojy2rXWH1KfjHjlDy6O6o4HbJg67o94ROZu7qQOJKPZu1CwVvCpk5TdBfix97-KIagov2qUSVJs3CgwQbUmauJC81ZSMCY2SrEmYQfhJ6z1ChKhfo3PkYf84w8s8j80sK_tRJcFJVxSPsLPgvMoysevA92g449YSVxzD0WMFy8EYxOHXQ9iMt8t4P8aPVV5aKPlW5zidbLTaXCOjx291licDZFgSsNdwMaCbyzaawbCebX-ISDntj-D7bFoGxtZ8m8R_xMsr0jAa8fo58HvhHxiHsQF2VF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4e6qTOoDBmegQGgYZPK9OnCIlonXdG-04xvdWshIYKODla7UIkPbEjq91VA7QnEdI23Ls8NtCfm_S7nxN9OdPWgRVNEUN2ACMmSghUbucTD_H4XCtUtw60N1mAHij03nfef-k3Gl4yn_pWiVVQIm2XCnqe54BAJIdNQzixidQuZw_hqKDKJqJpCNGaJJMbCcBPmSYeb_0RUGnOoe-3ajKCO9eVXmhqDooHHcvH_hZrBcve64ayVnKhZWieNMDMIfAb2CfgUMwjiRoXQ2kh4h-fCxEaxgs_4kmdbcfmiLzTWGH2vPhiltpjqSfIahtmPQLvDI_1ZCxJm7eOUZ1tIGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش پروازهای نظامی آمریکا به
غرب آسیا
🔹
داده‌های منابع باز (OSINT) از اعزام دست‌کم ۱۰ هواپیمای ترابری C-17A از آلمان به پایگاه‌های آمریکا در خاورمیانه خبر می‌دهند؛ هواپیماهای اطلاعاتی و سوخت‌رسان نیز در حال حرکت به این منطقه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672033" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7GAZInypPYfZXkkC95iZVJG7GQqhjucVOuTeoCIzPA3yFvvs_O9SLwgKzYCcHOnd1cT6KvN7w_Q_MffWnsgcban-SE2I3IuJTl42Dj89oTdmfR0XYLS8qwoophgtIEHThF4FIqKPOlthDRbzIHcGLpnvAcwavObNqk_8M-21sbmgfIm6DVa3fbC4Ae9UvNIEIAhZEJhlVnIf3glcUMofgpdaGrq3cdC2aBY9u2kea-jHVPGYnqvqcL7LslMnZtfmJUIX20GgFU3YkuSGEmKN9Mr_FbiYLElK6PHH0-nTLqa6zQUMs10CbImWcMbtPKyKqco7wWX9MX36PEDCSg1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن شهید شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672030" target="_blank">📅 10:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمله به نفتکش در شرق خصب؛ خسارت ساختاری به بدنه و سلامت خدمه
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از حمله به یک نفتکش در شرق بندر خصب عمان خبر داد که منجر به آسیب ساختاری شد؛ تمامی خدمه در سلامت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/672025" target="_blank">📅 10:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672022">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaDm_XFydquA72RPeLIjzH8IlkQ-1DJ6-x_GzMr8A2g9kok-wRej0QPxH-T01oviP7C4Pw59I0tgYnIhW88UYakk1bAqPYsXpbN_-Y8t9JPhmhAv9tSvKuO-vhZSR0nKpXUp4E5iKjxB_oecpzBxxz1gac8qwoV48J5jCvfATEh55hKax-IdY4rUwLfF1f5Ft5bzLjqXZjeKcrIGMWXpGHYUnZiw6gJ2V_swKw6PTIubcCbdpbK13A-xQMEAQuZm0uTnW0GVRUQKaoVwoEH77dpEXEj4JezwZ-1RUaFCEcKP7PbrrkXocZcNvaDOG62acsLE4vWs8s6C9y_NY5nnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شب‌نشینی ماه و زهره در آسمان امشب ایران
🔹
ماه از غروب امشب در کنار پرنورترین سیارۀ آسمان یعنی زهره، مقارنه‌ای را با یکدیگر خواهند داشت که در آن تقریباً ۲.۶ درجه از هم فاصله دارند.
🔹
این مقارنه از حدود ۱۵ تا ۲۰ دقیقه پس‌ از غروب خورشید تا ساعت ۲۱ در قابل دیدن است و ستاره قلب‌الاسد را نیز می‌توان درست کمی پایین‌تر از ماه و زهره دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/672022" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufITZQWwVuQq1uTsW6dLDEB9Qya9Twm0l2VMQVWeQq-JwBV8vM2AXfAe1zvoXY2ygo2ZDD8d8gmXV7hcZNJ5YryV6YSEy-PTZC0FdzH_fREi1jkQo9LTFRlfTWCnqjLtRV_5uns6fx7UXhprm4i3iBl-w_eaIjfkoYsovus7qTKMLMESRUbw9TyW5EzYHwpRYecN3A_bm8oKbS83zhP_s-l2tyTxg0jC4XqG0wltuvWJYKj0MPsUnAFW_RwLEXLj552_RiwXvf8FgkW5uICo6VEIUpvNZnEepLxqpOuOWAZ7m_oZJtk6k7BpBrtYGpVO6BMgW0vPlLGw7X9EbuoRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما نفت کش تصرف کنید
ما جزایر قبلی مونُ رو ان شاالله</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/672020" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672019">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hll5YJhHLfeRHaB3G-bW7CYp_TdGhEPKpipy8Y0kpo_vK_say0VkkfEoV0kbG8haOTjvBZRmKhqlIgkn1zkO8hqeTFDAy1JYclJ8aWr6IlObT8d4JR1YsQPm0jxTIQRnNYSkijI_4MwPD0qH8zy8S6rEihLoSIRtB2h-59-XFuHRP6oe4leFY3sxNkcn01nYyQayw8GCPkcQdUih60-ESJ8yo5w72x0p7Egse323Bg_vNObOmyjZy9eWjqBfgOKreGZmQ6GKfwBStMQd6APgtSDWF5bP0_98bixW8qKcdzIiBiQ8ADDsnZb1SdbcnMzeOsf6h_CxLGTcMHRMy66aQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور: روزگارتان را سیاه می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/672019" target="_blank">📅 10:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672018">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaQdHXeZfB8Q6OOI2-QSha_5TfFe0J-vOMjiIBSoilLoL3ugnbdEPYWyL8Mf6MGoSi86TuZr_UR-f28afzMTNeAgQMieudTT-H0ApvcXGfP8OhSAbmO3g4CWHIN80f9AY4zGscS7tIbn6D2gE4qhp63ompZ3J5MHF8MNAhXFoLFVw5gf_KTDxe64P-_4yjf3zAZV8fmaY11Jznx6bSYOs1zSaDWMBfXsGSJJdJ32aA28G4syRcRD8bSiusNKcd6nuNFWh5gj2eNWb2pAaxNlw68iEgnbE8SlSX0KlgHFwNAE_DIlwHkQcOSxodPjHbv61KTlxLHnavbodt0WKcsp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیه ویژه فیفا به قهرمان جام جهانی
🔹
برای نخستین‌بار در تاریخ، قهرمان جام جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود و انگشترهایی با تعداد محدود هم برای هواداران در سراسر جهان عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/672018" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672017">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک هدف قرار دادند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/672017" target="_blank">📅 09:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672016">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv7sQSJgi24bFbSzaaJahTBOHef1mDBD_Hk0o78Dj7BLFontpUohlBL_iMBCnsHj7Tb4DFoTYYGL552qfPUXnmtrJ0qYGg4yJzHvtcYth88McsUzFAxmY4nXhsdugiXMYJRk8ouqyNRt7FmzH3EycoASpiKIXgd4etRuCRqNhWx-md1z7T88B9xa265pNZwZZbDkbOclbJRTCzTAZM_JVa1wSv5Pj5WUeb2WPoamsuOEa6WVGlKHCpUSvsnWinBV_pFCcbFLcZA8kNu0W-z52v6ItsDFNgfDWrTNfCICpNWgc5yP5SOD8us8ZvWN_WKqXoYu_Mxl9i4zsWLNslgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط قیمت طلا به زیر ۴۰۰۰ دلار
🔹
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/672016" target="_blank">📅 09:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6lFLE4ThOL2uolHdoVCVbaCL0E3cwdIWTPhCkOsQ5W_aBRhVIqGvGF3erLDa1YNJJ6UJwQ3_yFRwtqyu-Nip5Tkc-WFoT9A5DyyHx9i75CJlGRcjvinohOnFBM_fd6TML4k7LkoCm68fLZ7_q8oGSDETYNUtSSXWd6wrgIE8yELKlPlZTLPIAXhdcpfhzPypQIjWp5sTbsR5UHrxkDUCC2RaS__bRRGLGLK7fbk3ZidEKDdVsCiZpXladBOy_ApevYcCcnFURyeA_P0VBCbzzBIJh-m4E9gxL68YIzFW_BWN7jto90SWp8PtF6FAvwqBv6O3LWPAFJhf8b4ujmr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHYxEShxjQUeumfPSh3TVSi2pMZPnLql2oAliCvLrYPCfas4qs38abf1KZL1-LVhulohfqISVmAQHLNd5EyJrtXV12htdQnOiUUajMVcK0s3_-hWvc3cpn1YTsGoH1TQs-JPhrPljPPzomRb936aTZh5gZa7SsNOuSi8WrU3YOSstOK5-XILuzl2KruoEIebSxzTyCIIwWOlRc_KweR_Z4JaY2O1mRFE4wR3TPbbga3mFpTACD3z4eW9Zh-WAcpzzt70E6Rab9-sDPGgsuT9F8JDs4U4AfCvG_Og-4L6HhK5PMYJF7D-tbn3bIcE_Ve3t2F4lCuXrpa7__4GSvrMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPIofuAMUqU2pFYZHHovNZv6kjlrXZ-3Px6jc6FXCWpl1gEuBZo6JqPrBK98z6vF_39tlKXLcEtEjxHiduXT46vUCNxyseqc_HXUwo1l2Zww2O42Y0O7GFjlNrMdDLW9kNB36QAEl03nQWhlJ2ibKPcagIM1HaiSgzMYOYwETTmLs6d2ota3VjXog2O4vClJ2bAXqpN3fAUqSZlk-1150ItIMesmf4iBIDJ2vJSFIQ_7eQNNlb6hLmAVyxB-wevMiO7HsAVbx4ZeFeIce1P94mA771-lO4sebkxeB0iG0i2xH7lbIdF4VfMSuVxGti5vUd3f2F7BI_4jTUYB1-l3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOoAGLF2F-tloruCVl_QH37Vpf0bvmmvjdVQp_NuQZn2ZG0jRw5vG1WU99ONL3tgmHNC8ute8DytHeKNDqukhpJyewH3uqC_vK2WrNulLd97FLsmShlAPSyStjWyXOFmXyJfzfdN9NaF4ck5fbpR0KdVUYqRTU0kU-0pQFdgahD9qzrh1uZEJZ9SIhc9s3kXLmirLPzBI2AQICeLelmCgxQqy4BfEQcvc0vFQBXz79X6BNyapUL7UCJ-5eBQqFjpPaC1urvb6zhIlUvbH66foxZ1OQdShHaaRm1Z3WZ_PqmoWEdqRkifQKGsf8kwi8Im6mFj7xvw8prDvgPDje6gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcfEwaH_eurUs33M67jt9yMZEKxOc7RLrs0gWk21qWs-f53I5XRjDLGGnKs1NJPpsJHVsuhmReauY4c89TTcA2FzZyDcdQPaXa8GJaUQFjW_xMb7zdxK8qx-kJIo_S4t_3R9D4zzUcVqEJYNm99TL0pfkcmvvS7pAZFneHWhNedsX90G4jn_K-rQxzwloLQHUjAEBpjECfgleZOHY3xSjMLG56nC3nKLyvhKJrHeh94aF2kh63vbIUU5yapYY26jfIa4zPgTMaO0gohoOoQCf8ovJsTxoY1zePN4eKyhRPG-OKNAVGm9etYKHxi1LxJllPQIbTvVWvQ3EXEIkIThhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/husns5CDeT0exdyrpbmFECj7YysYmev2p5jr8pc0onv_lm4pWkCZ9Zdb-A4OJygnMeGbkPRoQgpyh3KyTybmLVQecisJYZfCrHVk8nqPzLRXBIfBgp6rfpFVhwsSKYPwWfkYRM-SdOKRTMadqqAmm8qbk7V5NfQzmJJTPXWJDvQp8DIztXSlNQCtqAuopH_yN05iVxZVocaXU0P_JltiW6URT0js7ctYMuDbBPSiYcmbGRzJRn7ujf3S84-_fDY2hy19LLR5uEtXeDpb6C3fCuRkUqRfMh5JG3erUMMhDJqMIpSGkY_JJ_f93Fqxuu1qBhYlfzVNabzCcnMHS5RK4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰۰ ایده خوشمزه آشپزی که شما را از تکرار غذاهای همیشگی نجات می‌دهد
🍽
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/672010" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پایگاه دشمن در کویت در پاسخ به جنایت ارتش آمریکا، در به شهادت رساندن مردم غیرنظامی به آتش کشیده شد  سپاه پاسداران:
🔹
شیطان بزرگ، شب گذشته باز هم به جنایت جنگی روی آورد و با حمله به مراکز غیرنظامی، خدمتگزاران مردم در مخابرات و راه‌آهن و خودروهای عبوری، تعدادی…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/672009" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به وال استریت ژورنال: حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند
/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/672008" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ارتش اردن حمله سه فروند موشک ایران به خاک این کشور را مورد تایید قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/672007" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت موفق موشک‌های سپاه به امارات
🔹
در تصاویر ماهواره‌ای منتشر شده از پایگاه الظفره در ابوظبی امارات انهدام چهار سوله نیروهای تروریست آمریکایی به‌ خوبی قابل مشاهده است.
🔹
این خسارات در نتیجه عملیات موفق‌ موشکی روز گذشته سپاه پاسداران انقلاب اسلامی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/672005" target="_blank">📅 08:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672004">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ستون دود برخاسته از مقر تروریست‌های تجزیه‌طلب در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/672004" target="_blank">📅 08:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672001">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر  روابط عمومی سپاه پاسداران: بسم الله قاصم الجبارین و قاتلوهم حتی لاتکون فتنه مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/672001" target="_blank">📅 08:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
روابط عمومی سپاه پاسداران:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات نصر ۲، با رمز مبارک یا اباعبدالحسین (ع) و تقدیم به سربازان مظلوم شهید بمپور ایرانشهر، با حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه تنف سوریه، علاوه بر انهدام یک سامانه راداری، چند فروند بالگرد خاص عملیات ویژه، در قصاص خون سربازان شهید شب قبل در ایرانشهر، تعداد زیادی از نیروهای جنایتکار آمریکایی را به درک واصل کردند.
🔹
کنترل کامل تنگه هرمز کماکان در اختیار رزمندگان شجاع ماست و تا زمانی که شرارت‌های آمریکا ادامه داشته باشد، یک قطره نفت و گاز از این منطقه صادر نخواهد شد.
و ماالنصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/671995" target="_blank">📅 07:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsN1btqSXzNzAZJJ0u0Vpqanqsylyv_FXiYmb_TPnx9-HNnjlldwFDuuJIpXk7zathuSlw_bROzR20gqjT0E_PABDHb4o8YBFQOANUIBzvBGcqa4IKYDhjwtCU4H_3Sm5x3hsq9swBbFld3UjPbDM_uH4GyHuoNgRgXRmN1z1qPTK8DSp9c2OKuQX2-biei6zFyB9t51txIJBN9KHgy6KZEUBpeVoWhaNagZEDGZWrc-k_Rg89XYjfckVtqiEVeJu8UttJsalDcqtBD7TPnc1WuWeX4Ukhh8cwWDt8HrsPaKiiF6gWLrM1SOdozWao75lWLZBQ0FcS7VjLwiqdFVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۶ تیر ماه
۲ صفر ۱۴۴۸
۱۷ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/671994" target="_blank">📅 07:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔹
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔹
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
🔹
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/671992" target="_blank">📅 06:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjM_UkNgB8bntpHKLcnsYdABqFdGHztTspHVigHSW69-zxyuwhn7DRz7gr1pU54CKLHKwc32IU24UV9ybz_Rh_sAmJOT7_B2jJehwySmQhGDyN2JjCmyuT5z9_2JRZaUnKEPReEGUdCVEuG8_LF_nuP-zQk2geH0kVAOb2tNIjf9UwTWg-d-RiOCwZ2Jt7Dq_cZRulfSN5-nh3_xz-jMyHspyiv48iH9awuWumrvEWWUoKIHMkV7qrRbpTglmkYLOjwN21qwtaBt_3RJaIJHOGrGU9wZXOxLK5rtNLZ6ejJwb8HPM3V8Q01Djd5fIWAgmbU_gu2Xmk4OAQZVRNqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/671989" target="_blank">📅 06:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحلۀ دوازدهم عملیات صاعقۀ ارتش؛ حملات پهپادی به مراکز پشتیبانی ارتش جنایتکار آمریکا در کویت
روابط عمومی ارتش:
🔹
در پاسخ به جنایت‌های دشمن مستکبر و انتقام خون پاک شهیدان این مرزوبوم، ساعاتی قبل و در مرحلۀ دوازدهم عملیات صاعقه، پهپادهای انهدامی آرش ارتش جمهوری اسلامی ایران، محل استقرار نیروها و مراکز پشتیبانی لجستیکی ارتش تروریستی و کودک‌کش آمریکا در کویت را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/671987" target="_blank">📅 06:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفته گذشته مورد حمله موشکی خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/671986" target="_blank">📅 05:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671984">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: "روسیه، چین، ایران، کره شمالی و همچنین گروه‌های غیردولتی، توانایی آسیب رساندن به زیرساخت‌های انتخاباتی ایالات متحده را دارند."
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/671984" target="_blank">📅 05:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/671981" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه موشک‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/671978" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌ها در اسمان قطر
🔹
تا الان ۱۱ انفجار در قطر شنیده شده
است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/671977" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/671975" target="_blank">📅 04:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/671973" target="_blank">📅 04:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شمار شهدای حمله به پل‌های بندرخمیر به ۳ نفر رسید؛ ۹ نفر مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671971" target="_blank">📅 04:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حادثه در پل بحرین-عربستان
رسانه‌های عربی:
🔹
صدای آژیر آمبولانس‌ها و ماشین‌های آتش‌نشانی که به‌سوی پل متصل‌کنندۀ بحرین و عربستان سعودی در حرکت هستند، به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/671969" target="_blank">📅 03:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری ساده بر آنچه گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/671968" target="_blank">📅 03:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Lh2JsJRCo7uID8a8T7BJHcaJNsVfFx0b2MEQYxZi_yBpShUJwBcuORd785yfBdpRTBbh6UcjrMLdbRDxNKRFm2FvllOZcEqTGTUwoYiMLPCdBe3slryfQHuskg9Flcxy8LoieVRu4WGurRSEPGVDyJKslljia8wB2cMjorCqgyyCDqePOzkMBaoQOrE8cd_FhaUmTxUJA_tnKtPK4SZf1fNs3hZmJgwNKckqZMZw_0DonWSR8q-W5Iqgu4vmU-mhWJYlHn39tw96kF1iVMwOjN9x_Vwmu7AvK1szpsq0UjWdWSEJG7UsvC253rly_bM9lteT7il17T8RVM7yVd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
اکنون که رئیس جمهور آمریکا با صراحت و وقاحت تمام، پایان‌ تفاهم‌نامه را اعلام کرده و جنگ را آغاز نموده است، وجهی برای پایبندی به تفاهم‌نامه و ادامه مذاکرات باقی نمی‌ماند.
🔹
رئیس جمهور و سایر اعضای شعام و فرماندهان و مسئولین دیپلماسی کشور باید تفاهم‌نامه با اطاعت تام از رهبر معظم انقلاب به همان مسیری که ایشان تشخیص داده‌اند، بازگردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/671967" target="_blank">📅 03:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد در مصاحبه با فاکس نیوز: اگر ایران به بازدارندگی اتمی برسد، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/671966" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671965" target="_blank">📅 03:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmWyhlE68M0dKEGX1B6MukcgmjHXOndN8hhpp7WmfJhmvPf7pt5BhUsUvVmXyTTCpj_8WlmDXawVXeycEyERwO2QKkAFXk9iMRkj_GosLGaaIYmN6xmWZFO5XWxyAARB5pUjX5qr8fCGCVzNTHxoYsZ1A1XILzcTVCYqWei4ToqjlU09RI5X_RHPIgcCOTsZaB0RRVRuR7IefoDiGSNMAFC90nKzgW-7fSFfQuSOzEHbO4QnLyAAeSfnkfixPRJY8rvQot0F9Ftd7HvgE0EIiYIqze-mJ5vilHxqhy7JmVOeNZtRtsKVJ8tGZkGowW_zD5xFMTI2qWo6-Wm6ESD_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkj_w7Ux8qTVMruNjrbpDc8Q3HtY9ViiSrj6sFLDjhD7B9XtYCuJ2ZKskQxprD4MS8DKq4LDkpDQV48LDO_lFSRg2Vq2Rk42en_NmI41sXMiWpOXxOCTkyDfj9LDGoPNViHypo6VFqotEDMMLhVCEmBaPLZ6gBPNOwAfyMKE6rRHxcaV3m9e814azrerl-xt6K8KBlzsU7tdsTuIpxFQP2nvhoXF50ndYO0SAeAnMbjjZ-oiUJF-nBDxixAsDOAgSdjX2vpPQXq_VpwEFsHaqAQKusWvNAcH-JWVE_wzQrUpMEezYubbtKPP0miuXswqqWGxgz0vtvCFUVH0Tu2FyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
داور فینال و رده‌بندی جام جهانی ۲۰۲۶
🔹
با اعلام فیفا؛ اسلاوکو وینچیچ از کشور اسلوونی دیدار فینال جام جهانی ۲۰۲۶ که یکشنبه ۲۸ تیر ساعت ۲۲:۳۰ در استادیوم مت‌لایف نیوجرسی بین اسپانیا و آرژانتین برگزار می‌شود را قضاوت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/671962" target="_blank">📅 03:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج جدید حمله موشکی از ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/671961" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ادعایی از فعالیت پدافند در بحرین
🔹
فیلمی که برخی از کاربران منتشر کرده‌اند فعال شدن پدافند هوایی بحرین را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671960" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی درباره هدف از حمله به پل‌ها در ایران
🔹
یک مقام آمریکایی در گفت‌وگو با روزنامه وال‌استریت‌ژورنال گفته حمله به پل ها با هدف قطع تدارکات به بندرعباس انجام شده است که ایران از آن برای حمله به کشتی‌ها استفاده می کند.
🔹
بسیاری از کاربران در فضای مجازی اقدام آمریکا در حمله به زیرساخت‌های ایران را مصداق جنایت جنگی توصیف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/671957" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/671955" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/671954" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی دیگر از آتش‌سوزی گسترده در زیرساخت‌های شلیک موشک در خاک کویت
🔹
برخی منابع می‌گویند جاده‌ای که تروریست‌های آمریکایی از آن برای انتقال سامانه‌های موشکی خود به نزدیک مرز عراق و از آنجا شلیک به داخل کشورمان استفاده می‌کردند، به شدت مورد حمله ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/671949" target="_blank">📅 02:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله یازدهم عملیات صاعقه ارتش؛ مراکز و پایگاه آمریکا در بحرین آماج حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در پاسخ به اقدام خصمانه دشمن در هدف قرار دادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحله یازدهم عملیات صاعقه، محل استقرار بالگردها و هواپیماهای شناسایی P8 ارتش تروریستی آمریکا در پایگاه الصخیر بحرین را هدف حملات پهپادهای انهدامی آرش قرار داد.
🔹
امنیت و استقلال این میهن خدایی خط قرمز ماست و متناسب با شرارت‌های دشمن خبیث، سریع و قاطع پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/671948" target="_blank">📅 02:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور خودروهای اتش نشان و امدادی در مناطق نظامی پایگاه امریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/671946" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671944">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
یک نقطه در شهرستان دشتی بوشهر مورد حمله دشمن قرار گرفت
معاون سیاسی و امنیتی استاندار بوشهر
:
🔹
بامداد امروز یک نقطه در شهرستان دشتی مورد اصابت حملات دشمن قرار گرفت./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/671944" target="_blank">📅 02:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671943">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/671943" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671942">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671942" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671941">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادارهای آمریکایی در کویت، دوباره مورد حمله قرار گرفت./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/671941" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فعال رسانه‌ای آمریکایی به تهدیدات ایلان ماسک: من در بزرگ‌ترین مراسم تشییع تاریخ شرکت کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/671940" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/671938" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قطع برق نقاطی از کیش ناشی از مشکل پست برق است  استانداری هرمزگان:
🔹
در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/671937" target="_blank">📅 01:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون استاندار: بوشهر مجدد مورد حمله دشمن قرار گرفت  استانداری بوشهر:
🔹
دقایقی پیش برای دومین بار متوالی در چند ساعت گذشته، شهر بوشهر مورد هجوم دشمن آمریکایی قرار گرفت.
🔹
ابعاد و جزئیات بیشتر این حادثه همچنان در دست بررسی بوده و در صورت نیاز به طور مجدد اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/671936" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1VeUIk3GBuF1XTELcpZKMV-Qmae7AtjCJhR5uKIngSd0UXkItT3wnlJTnFz_8ecW3Wxg9HcOgWy_jbiu9vah8gStZsSaA_zeVWSqcG10XmV0bIIsjj7rMo-bVqEsK0yIOGBGK5cl-OeCXo7yp8Z9U-dv5UPa7Xe13qulMPn4pvqwVFwWnXt9yXZshsnJFB2mVAf6lDMvPaGBdpzQeY0f9PlYGvmwSUk25yJNgUPY2q0OlX0k8f3mbnWabL5sf1r_2Wrb6dsElXEGazxjVyzY27tAbjrL4PilgAn2eQIhHjApIDYNBsa0lBXhwFAe5xFiMY36C6PFPIrdFYrVs2IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/671933" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/671932" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671930">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی آخر را به دشمن بزنید
شهید حاج قاسم سلیمانی:
🔹
چه غیرتی می‌تواند کنار زن و بچه‌اش بنشیند و بگوید به من چه! اهواز را بمباران می‌کنند که بکنند؟ نه این مرام ما نیست. این دشمن سیلی می‌خواهد؛ امام(ره) فرمودند سیلی آخر را به دشمن بزنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/671930" target="_blank">📅 01:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فارس: حملۀ هوایی دشمن آمریکایی به بوشهر
🔹
حوالی ساعت ۱ بامداد، بوشهر هدف حملات هوایی دشمن قرار گرفت. @AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/671929" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671928">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تکذیب حمله امشب آمریکا به کیش  حسین احمدنژاد، مدیر روابط عمومی و امور بین‌الملل سازمان منطقه آزاد کیش:
🔹
امشب تا این لحظه هیچ‌گونه حمله‌ای از سوی آمریکا به جزیره کیش صورت نگرفته است.
🔹
وضعیت شبکه برق کیش کاملاً پایدار است و تمامی خدمات زیرساختی بدون اختلال…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/671928" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/671927" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671926">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
حملۀ دشمن آمریکایی به یکی از مناطق ویسیان در لرستان
معاون استانداری لرستان:
🔹
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/671926" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxV58mFURiH4ETvVm9AqrzqhLPRjckZIxEzWnv3Ir6lnWJAZw5ayPsWqqFc_1Q546Nlrm_KmIL-nEEy8aS_3qUZ5n8NL4k-HH2Vxhmap7264VfSyJBivSgElNeYnEcjI9Re-R8YVWuat2WBDOLamrGImoAwfMiXRdaP4jXCGtk_9-HsA24Z-Az4PuBICGrCNAEBeHDXlipnPrcncIFh1A9otgb0ZAHWq4v5lFwEnNpEqraKkQKEOUGQYTDRGmFasvu2qiWWEgmsaYhpoe0VNs-9WnuGwauqija2GmbGalu5L2-6Ysoeoct55dfLCKNjm8w0Mwg6I7t5p8KqPIYGY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب_ماندگار از شهیدان حاج قاسم سلیمانی، سیدحسن نصرالله و رهبر شهید انقلاب اسلامی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/671925" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس: حملۀ هوایی دشمن آمریکایی به بوشهر
🔹
حوالی ساعت ۱ بامداد، بوشهر هدف حملات هوایی دشمن قرار گرفت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/671924" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
