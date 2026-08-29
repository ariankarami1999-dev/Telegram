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
<img src="https://cdn4.telesco.pe/file/gIvpIJSgRxlr4ykGs00TtXAsW1GhjgP6xMHa4fJtbnqSsp56i5Et-UUtdU_d_3qSvRNazznWT58l2E1ruXm39NuqbJH0nGB6iMsS8gDnABBsYi8JyabwAfYvL4sDAU-_QuHYo8Yzu3w0MZcAAqK8QYq7qRGwJqU1N8W9B4PZUnzor99k25OBzNtLVxFNdNm54esQmFgNNy3Cm6vHBO18V1c8UINDmgOzKI1IuJ4qBWX4IE9rRSmCtO1RNYqC8QbcVf4CTMGtM2tlg1EZeyg5IEdDu-Kcih6svojlkpoE_SEuTzLuZ1IXCEn_WepAB7gf1Qh9JTQrAtEe3bukyMC_hQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5yo6Gbyf8-MReQhfOqf1SqxZooGBnKsHcWBCcPTjMZCm3PzscBwT4TMEOc1xa6RsJg6hrDGLOYIDyvyY0SpOXzP__kxnBlthWiCOV3weMPlUGEEaYc97AVWUkFB8cMPGsHRp8CU7VaQtoLphVxRVZPY4KHZZeQ5HMy3DgpNp3uR8F9DH0Xdf7aPVtlHVDUAOO6LREF7OO-Ti7Bze36Pz6qK8Y6z7l8odCIiGsswBwRSoB_bwThhJ5rPfIkGhO__lwBaSH08umQz-r8tCK1meNoafxdsGE3YgKuZ7SZ-qXy9_UomnmrH4-1orcC2B_1sXK82kE7JDj94xT0EA-EGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=PslfkAlgsaU1yylZbgrUef1sDNQo1yT1artlZkBE6vh24mVKYvHhkM516U_QWiY36kVwJ0aD3Nedt7hoGF-H91kuu7ZKRqVMS8K5WMLvN89Bxlk77viHNb-ph38p07JqEtAGCzfJJVABuMq2wecvCTZA3d0vm2bi1Hmxm3afNXSBsynFjfL8vgrYmjMfFJDoNhMOILzZOcA8oiJS1KV01Ujhynn-RF5Cm80rqHXCTfcPjCx2QzckzLOSEeETnxw4zDdxOb7pNLWV_uy3bpZmBHcr90I1awa5ms8BEG3Tv2Rj6DX40kpEPQHN9QbFO6onWmpTZiJoBMeUHF1ftgdHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=PslfkAlgsaU1yylZbgrUef1sDNQo1yT1artlZkBE6vh24mVKYvHhkM516U_QWiY36kVwJ0aD3Nedt7hoGF-H91kuu7ZKRqVMS8K5WMLvN89Bxlk77viHNb-ph38p07JqEtAGCzfJJVABuMq2wecvCTZA3d0vm2bi1Hmxm3afNXSBsynFjfL8vgrYmjMfFJDoNhMOILzZOcA8oiJS1KV01Ujhynn-RF5Cm80rqHXCTfcPjCx2QzckzLOSEeETnxw4zDdxOb7pNLWV_uy3bpZmBHcr90I1awa5ms8BEG3Tv2Rj6DX40kpEPQHN9QbFO6onWmpTZiJoBMeUHF1ftgdHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9Vv1KrzWCOkI35rpBPhZzXnASzNOVVPOim4cryMnh0x5wSwDOaHxxHteyE2x-F0If1Ifxx9Y0fbW6-qGSHtUQ_RwLiz-aXxpADXvRc56Lytty-_YwDQ53I6OhmtQd4gDgSCS53MbRAqJtgQASPv09F8cKG6PetYn4jREUHCpHFtPqub8IMhrTUGU4uYfgq5mCofmOtyui-w5s1SD8iDVxFOHNbESWASq5PtYvhT1aPv1JFZOpUG2dJ4MwgEVu2pzt90iL624G833_PVel8Mh0CEXxOrPd5hyTIg31UomRPuR_nsBhm5YfY9GseZ0E6YXdapRNu1QfikFjjmNSRp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
مواضع هاوکیش کوین وارش در نشست جکسون هول
مواضع هاوکیش کوین وارش در جکسون هول نشان داد اگر تورم با سرعت کافی به هدف ۲٪ نرسد، افزایش نرخ بهره همچنان روی میز است و فدرال رزرو لزوماً مسیر کاهش نرخ را ادامه نمی‌دهد.
بازار نیز این پیام را جدی گرفت؛ احتمال افزایش نرخ در سپتامبر از ۳۵٪ به ۵۶٪ رسید که می‌تواند به رشد بازده اوراق و دلار و افزایش فشار بر طلا و دارایی‌های پرریسک منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpytBOGdSrNVW8kZ1WRo1KivSekL1ztsuhJkHC25i1y1qC8a5g6UY06gWdr319E5uik2bst3zRtPmXDWY2ntnndbS7Z9Dtj4w7A9T7VYRQm7_-gqJ85ASOihO_RKLyZMZNOEJVjqXlYXiVXMLz306p7_g2Cp8u_ZOT2aAgs8BPwnDbPpEpyEcQ1ZXZW-wYnt-bo_cQtLU1S5jrG0dIVcr4AISI6oD2cjJ7wnr7S5eNpufV0O6PGX-M7w5lNAAvRuarrQEcCAD0oNsur6SWBV5mOcyp1_3051W_PbyMCYhoJraQYYCPggGkWuTNFdH_Afg9Qa0cbafg8lf0vHgzmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlRyhQ8qPlAhpsXnfh32TYNl9mqRVtrnTxTJloSU1ABv672ErjBxgB3sDdAtDvXl4w3KifEewOWDuKjWW-_X3qaNs6MIGyEIENGcu5W-tWt7Q4_O5QzUKp-0vQi1pQUHXFVmJOAhkEIJACQm8VWCd7RZC28ZdA_jvUPZxJ-5R2m8tngCPIdTNDW2At1EUQGVPK2speANTns2h2-9bXHrVLRhYUZV3cZ3xg6vDj1KyEqPrAxl-GPu2aL1zyo1RmInsFLnkWb2TIBvW_EEU54EIhfHo3XWvXdGkeurgPYlROU77B56YpxbNtDPX0l7u04pFnncC37prZFlZV1RESZT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWyp71lCl3uvKu2U4b4rMZ_8JAmb__Z6SeUHvBpooiczxMqQ2nmT40ueJPpZSJKe_O_8sQ6_0vih_E9PigJmAy4RwlVOpTf_NRJhpRXVxbMZ1UqhKYHtoMbZ66xv1FAdXmoqfoj1ZhJs_mML_JTNh2PI8FNR4h15zUNZJ5Bsn-1Qr3c6MF7vFffAwm1ZmFTVxCtuEieigT4Smrp8j_z_yCqxBt7QMqahAE5Ia2bPYbSz5d20OlO-6587ebuu9QGARFI-TDZQpZbE2l2njgwAEC2DTi7XfESc0EBQn_E3Q6_v0AoTXf9_WZ1UqF3SYbVD9xV8sgxB80HV5BK-XG_FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az_OeWrNOdKo852y4dOjiMApgd3SHbplc1gbIjVxP4AaRRBI58j47WKZ7idKXiE_EneC95SQA0H_osdZyE48WZExr0PHr3O8flvDz-iVoC6HnTfIEzrfl4XpTAJjwdyXGo5gC4T32mEkM5NzLfUpm1Ngs5sFWFdnZZWUJithkgtLf-yZKUbt01MoTua5rciOxyb01S75KTGrAjgiksDQHQ3oj68fy_pXPyU3uEyvE9VIeRrN92mAGhAuAFWXbpwAMtOWwCEyAWXjk40YmmiMM0odGnnzhZGMfbwm7d8GUFc-xPJ3PK6-1YRNswiqyxF-R56W5-dXcr2LcnsrAZ6aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3IQLYddEj3TiPEXZuQrcLc7MwPpTqhfw_RN46ywDrq43nUj-8ZyrAlAOFdCFytBHU6w3pMH0PFjmsku1irxaCvJ7woPTVb755fmMQxykgfDpf7GkJ1y0U898guCvPOgTixs5iVhaOxjzRs7CtKMAQ0ZU9lTfiFGpmT1TjGp7aIv8Ch_xet9iR-khLPOUsy5-CqJTDFzuIM4fn_M6HI3UEVALrm41rs3rB9hK75jNUpXekFEtqCzv5jTV3XNlxFy0Dhz1vvSBay2mkxeeobzyaShdwMPinUKc6EODF7z4Liht_CF0-sk7VgnVtcC9X7a-eHjVFcG9WvlQ1SsYGpRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNZq8gS4WFa6bwww7XpEqlSS8wvO_0i5SgjFDDjUYtQH43zuhkvUDxpvLN0S2zaHqILFWg91606tEAkHUSxdKerciFB-Iielqp3t30R7G8-udE8k4p6rG-Cjy_YyltM2aT9PqftVICJdxQEHCEP8-dEhmvduvAu9jTRNpLlKFNR2GaNR1k_l6LeKqvH9jlfJcM2YacPnxfgi2plNvQHWsbfEn-rG83aINmKFHvrtOpW49-EplurFVJx9FCkMk7vZqmfX_5qumR-ov6ooWUUyS2XTEU1RKHupgL1PXhkmR_UxQISZvB5YXnJPCLA1gyvPS_pmug6CNq0boiNR-GUMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM6kBoJIxQjaYDqF-ewMGcXY2i9Lw5MYH-0qefu0esXK1cqy0W0HnJU0ZN22WM92v79honeCAH-2Hhqcvr0xu3UW72WfNT6LGZCxXvLfbXVOdm8mCeTrKYo-9vKlOSrU0SiqR2zjwuxyou8Y2OFQRmZKMQSqR3UVI_Sg0Os-BGYmds2OlW3G0XVg_KRi8S-D7zHywMidVQAb4yO7t3gdYReqlXNgWwl9WJeta2yEjWPCmy-9XE6-aHPVmB-IyCpsXdtfLczaayJ6J-SMgOQF5Q97gUlYk8KCxrtxJhnxNY6zJilg_jQYzXJtr1oPXCWHPSa_b96x1C69QAfKf9CLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWr0SDFGiVYuDW3ub0_5k_M8hPrrTbIvzik8DufqDWpfPRgzJvJUgYSdaCKuyYdmGAtypRiQXv4Mubxd6ufqDVmiQuW1PT7edkZParylQsCqub9OU7byW6RhPP4qSh_07vOp2F1taIpP3-cSYiLEy20txvIGCwAxFkyOT8TxWuNRtW-LUnaxQZOApcKa4zZHFoj9rzSNHTka5cYD4ExLVG-gWgq4hwW5XHIcvZJh3Y7TgL-apB3_GNHpP6egd-kiPUTrGNX91PwYtPL3t4_6BXfu4-CWX288hyVr1KRIZFtVjdABjPA02CjRaq0bm5DrArPbuspffXQDG2JdKdf_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7OIlozkM7kFUzZ4A_rXhBa1e4tmEpMfSTAjOQUgBifgNSIjqQdGqDHwKqrYUleUUvqIycNTg8dY8GIUkrWEKS2bcvipANTRY-bT3U31kYbZe5mUqB-7082cvXCYCQbslqKF_4UB9tPYFsK-VqG5a-69KOJGldAXKRjOGnCh-MuNclMXcm4J5dv7nVLrjZihAr40tz2c-DnXEZvYZAmKoKocoRgjBmanVHgA6UJDtqkvTng2zpExzGtkLC_l-i_btfBVOApVYhHslOn0wtYwRL-p3AFN6kxnQP7A6s57oeYdrsNdX08wVY-UwgHqZq7DuCsYI1OlaLt5lIwKaup0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOKFLEcX_aJCKhKVc8ttnP0wEpOKheExGa_Wr8oM65qFZAk-ZQ5WNcYKWRCPWkS9mL54j8MpKt9_bafLxDm3FEMUp08YB0LCkK11COwBpJXO1g-CndmCqP5OhOnXu6X2dZW22guXgPPTgXqJiG8suJSbrSDVNJM4tvJEhXyvudGpyR6tdmFZUDjl36s_M3eDCIRDjlUNWb94-b2p9XTVB_LwlTiVhZppNM3lis_SWWUICGrTRr7w9Ek1h73BCVprd-xnyAOsmC6mc_W1wBc6OfCP95FMRQO4JV2C9oGDELcWAGPAYv2ISYnVHt1L5saM9O-EhMlNjlngfvAl_BIdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6sasYb_a_THhJ1jtV3kIhhE0nbOosXBL0bxTGPtKtMzz6qii5JfSaRXq_yHyXiaMLc7T97LPAoBH60b3zc1MSggJZtbYrvxRSib4o3FM9WFk3wsoF6vqAfy09-ykzbXIeo8mjz-Dtqbk6rjlYCZx0emmtMwlvpTSS4r-8eznI00-heqXMxSToMCmib2To2nvy8YcE-gDzKiYnHTSqmO7NLS5W3S3gMGbQXSwgXHiyWVpE7-YJ7ZeBiKQZiSp5kcExcDjiqa7M2a3hP3M9I1DltZk9z403epFbmFFCQx6blJSM2cQJTJVzQ7KKXqapZgGK4GCB0HmBLeziGghhaqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayM7uYPEoQh8RbEIl4H6wON3SCnnbLNR_czeV_GzMDqLkx219encIyalicsOTvq0qQK-XlgwXVRHQJxghjkO52Cobd7XiBATX-x0DZLkpJNYHaT09hazlZDMayYTUtz_Ejm7M20ptiGbypLPl1Z3KEfSG-I5JoR22WbhDyXGcUYKcL_R8KMr53jPqtda5HJNVI25t0Xfr7vOz1GIkGg_BFcS3gKqbq7B2zkjIc8Df1Gl0YcLRoI52SLQqGQg3x-yMNOg-zjTRN7S9JNfgKSADAaO8B0wp3ONYFpAAKbbey8GEx36GmS_5w1WTu7CQZczNldBpKmKddbc9AwzycKPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaBYOj78ipyg3dBv-u9cqdGG6t8Ud8D1PlUtVxpJrm0yVb5H9XhuLkQK8WgVPG7IdBWhkCOCKA7aU7IJkjPEm1nh68izGxnq5q4mxO4yhaIHjqOOyFK_NZanovf549EPRxmc1hMF83c2THcCXXbFTNjlmHqszIDOs8zEYkdRzAjNozPSi4iQJkzTtx6W8cpIJPnbYYW71dNnNpvgS-8c_ShYF_m1O7GQSbV-ggQ_m9vUpc9JK2koircSAk7QyLOpkd5DtS0fu4ptDrLN8g7VB1QGYeSaLhgRfV7DTlDdCZ_sJc-f9KCYw4vPDukUYG7qLlB5hdchthuW8b5SiCYT6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaPqNCYHApJkRixtdPWR1FLHqPC1MN6Qc9yj0o687eF3pyW1LqVQlBshA7CHaE4LO11mPGBmXTGEmAPOcu8rnbrsKFY6vE1D8_z2y77uIc4CqI85DQ8iD0LQIbkvax-CYoTXrGfcaNrXLkDQXXimJkIZNlJlkvn2skCZQkhXlRWjiW43XwjdHbURoZP3jlkVYvIDKIg8lF-uwwLBJUJTf7zMmNSs_Os8I5oQMetFLH_U4biAQpHtZ236Gve8eDjiSg_tZUAxxNPa96kKeHYChfK2DF3LDNm0b7KuNfV1z4MEFGT1zeWwBRYvcnN9gwQsHZZshINksgliL44PF29EEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKEfXXYkPS-7o7aCI9Mm-OLTp8iDOcoLRKNclMAnKNh5BeEJz4-Ov6iRNa3QntFGFd0iqb_Hg8huOJFbxX8RvXOSVmXgl1ywqUiWD1sECRXDUT6aQ_ct3SBBZtQrAuUHDY3DXKUTCa5dER7fyYYIu5stidbWbyJ8qf5TXsrNg0pR-QMV4x77NIb4SoDJ1dIMCgETvQjpSZ_3xiIxu3BUybb0pZmiTj1bwOhd0aT9hwB9_V3ofnbXaIydQiFJQ0Sr9mzKPxo32_4hfJzs8ZWztWP4NcaNm3oMb1rxmRAhvhQxGTyk8pLFwcQL3PhP5KFG1KqtKAI4adEbVmqsnaQ16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEzURlOVij6qNZWKXI9rNRrwSMjU0PWj0mA0J5-rJw_mlZx6eYoL4txrGxHZdtKi1VwJNhTS34qFqUufWPJ-uDj0HXxLs2WYBLYWIcOSkRU8myRk-Sf7Pe_jPVSE-fngRaLdDiNpq49NhDJULpJM3XClJMbBow2y5k7nIE828oi7KSLSDZLMlyBg_l8Xvw8vrYQ0bR6IWYnsNaSB6_pm-SvW58WWK9qbbm-HxYJktn6V_zJF4Nk3mOrFfIkrKPYLDiZCkd6KRycY53yqqxNvbeBvCrjsV2tGSd05qaJ4mGfsLJCZoOu2uQkFy6GZCOhckClX__t8gSGRDPu3gAzTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=K6WXDTAcPCQ-4XCqNvvyHNnedQJ9ovfOauB3pb3YxD6FFj6xI-jyH7TJC1mr4PZMJXEYYnN-5MAC2X6BcWFqlDNMJZbrfbhzqWVtbaedXHNALuGMdbm6wOY77WaRkcHzJC8S53SeTF3D470YkBFnT-GI_MfjSP6buzsXN8NJ2EVClYU5ZbguN98Gzf30yazKhzSbQGr_3qjjBzb4cHwN5Ng0YH4gKfh3w4iFxHKKOd6tSBLbwHvU2jC90veSz7h3OFihrOayyAt53MzUxc9w4iNYQHmp0-VL7xWo-cs94DiLCxi50RgaOf78Cy20BcetCJ8wByZZNJ7N0UEmTuJVqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=K6WXDTAcPCQ-4XCqNvvyHNnedQJ9ovfOauB3pb3YxD6FFj6xI-jyH7TJC1mr4PZMJXEYYnN-5MAC2X6BcWFqlDNMJZbrfbhzqWVtbaedXHNALuGMdbm6wOY77WaRkcHzJC8S53SeTF3D470YkBFnT-GI_MfjSP6buzsXN8NJ2EVClYU5ZbguN98Gzf30yazKhzSbQGr_3qjjBzb4cHwN5Ng0YH4gKfh3w4iFxHKKOd6tSBLbwHvU2jC90veSz7h3OFihrOayyAt53MzUxc9w4iNYQHmp0-VL7xWo-cs94DiLCxi50RgaOf78Cy20BcetCJ8wByZZNJ7N0UEmTuJVqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZZybawsD974LBJ55UO5Ve-Kb-R2zn3QafYhaIQU7B2qutfC7a8VbMUtuup-LLouo4HIYfF6mL4eNJPP10l8YzyMm5gR8It_OadXIWcXGYupsJBz8smnITqihhGrZ24-dcWNSfYaUbpC3J3QnIGxFM21yiD08V1sglHXcNnaGi4Zao3Xat0QRI0Jc-vvdYekzIZMfx22EKHolOIjYyiZmjqJCBKYIpF2QqwZjRayWJnk1_v7355daFSMGewnc7_Sm5cXZQCK0f2qgPa3ZBYLGlhYLf4DFy7FKeXsEtZuQj0bEF9_epCkm-gVbiQhyIrkoH0kosnHSKlcdScxkzNXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmwOTFppOxz3AGoF_k7S8VkmQf1076eGVHIl1I4TlC76r_ZAtFxBQ8lG82pqGvxKkKjwv3FIjjLLn7FDvKP30WmGTj10cnLIs7iMzhTSO6se5pfGYSFfYn6292NhhdBOJ96i6Zt_RqV5KrpzQOi6btOdTpfUreHd_XVyFoC2U1VkhaUTgMXsNP-6YBMWCL_wtpPhYCSj6sDS7M3tCHF_O4mI3hgWYfX_P8vvOzZi1bDGDcRuHmP9Tl4Z1DZyUEbwizeuU8bb2lewPF6KfUCWGI5Ull5uGesUSuee-wFoKsNLlMuVIBvXx2JVqfexUy3lKpK-SNgnYvvSxmhQ-Kvg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1OODQ8LfYjQZBmQzl9sm5kTMa0Jn37ItzFfwHLYpaRUQgGauisLaGsecOCYxyM57NKk54HsJR1SedTpfb8Hu9H2LnDmwCOzYHns4tcITc3bfvBOTNaneatwLEqbC2Hz1I8wZgzXfaja3sCOX_Kk9HwyM4ZvTfxwko3lkp3ZEAbaqwpZwFvXVO_0A_8vOPfmMHPuITlI1pwlpaTE_b3fPn0dwvZlBrJycr4muXcfviz-003sMemzziJKaaSKqFDkSTJH5Y-e79VF2tOPZZEaqOteaQwmfR1A4zH-OYb5lAKwGnMTcK_rtY-1vd_Z3YdhorrQG7jCkcZKY378Ac90Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJcBSdZW2bNCjdQp1rXc5lv9r7uYVOBWjoD6O5QRFC0Z07e_yUcHaK0tnhp5qzbUkq8NS6TDjU2NQ9uuTCXmn64xVGdirCjOoS99UfoAGndlKX4r0x1wS0TBH5I5L7INzsM2LiBboRHrO2hyX97JOk2cIfI0TKuP4Wyvx8FAAoqJEHMt6f1TfNmM4En2GZTqGAGHyEB84HebEE4X6g4Vt7INC3F2GpsgBC4hxGOyThH32uxWdWnL0MhMaVvk6uZU6vZhrKE0Ij-ARGwMUyhneKoCO3IlAzr0CGwckb-7lzrXKs35B6ZwWsbQNupd6Qo3Vbf1x8uML0NaMJ1Pexdlmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJJIg4ykcP-ZqZazUQD67PRgS1WAyWzSYAmY4fmuE7Gq3xPqvbYfoOnZg0Xm5nU03g24Trg5UIvy-SmIQ9BLFlJr-dXm2CTlz8LjhyXwobjmGJNEEKDXW3PoLDv02T3jQVZrIzh8KyHInn-GfUgWV7ND1XdoRKumiaC06sIrnjWZDv8vFGKMY4gEV_QuCeshWD6U6Y3LNtlbAyMWb2WFNw4beTlJHJTslzcmJMguuYGO1HdPBHlmGl0757BIMBPODKXMS5VL47ML57pXpcALQ7tbpWY7mDmYJveY1AQRIraUZpt_rIlVFrJEXUQPZDNPJF5ksxHUeiqz_XeuasedCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AltWHgvlSuV8s_GrhlJW6npNZivsjX_cq9L3_FujKY0QHMwY_4TMvWJjNt02QVEwp7Bv6m_mVaBdj4OX66StFFOCr0CqU4IC9J-OpEkGfCANfqDc58c_wAMubTNCUnFfe5dmX4C6Ivo2dru3OHfAhQKG85o29-Q_Fs0g2be311cGv6C1CNTJO3Jj-5vbgNX8b4ELDR1gZa5pk2dYLs_hQC5kZFtEPc35awv8CYqTLRLWqZbIVJ10s9yM-gFAzgghBWftv_1gEOA3Bi0TOcRNM8er1DOV-hraLnaoaKgqIlA6hgiZjTq8EEiATPD-5Ilhn7H_FdipPpzTAHK8U6sYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_qITXoWhVxhKzSKnjj0_citN5pABFPjab6j7XUqEDvYy5iwuPyQ3owZb4VPuLsAAydBM2ha6Q_A0G02HnH85taN8QYXnRIhXCkSPT4RZ5nAW9OZkzKUMQG3M2dAeFmMtXaMEWYqG1KAuplCkq8P6DWlCPs4CN-B3wO4mxZoY_Nt66oSqDj4odlnenBUN4ia1si4kAK3Dkpfw-V-1BzSX5RJSTN7zi9KF8StQKlO-Vcrn6bA7FpS9czcmormSnR_jO1UGU1pZzSUu_1I6484-Fm8ZyXVFAO28QPY0_eWNVefSe8JaNrYc9N98o3-qKHFXqDHHTSVllYvy4DxrrwVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=mOrYoJmlyz-_b6Fip5KBXbCa5D7KYwkTbRUb1wyRYfVFaZTKZHCfqTk7B5wXHK8F0W0p4xi078GosHALxM59gN2wFZSzL8FWliUngqvllUBIhrmCgSklTRB3uMSLpCnx55jkVxrCqhzQYFPg8JT7UFUIrUeSIXzBzPlL9qKjRZzvU5AG618y5OAir5snAttdsiZtavUKL-UrSlMDHBGg4_SLAsvqeUdcu1tbZziMTA3_izGdKZ4JCMbwKQT1gOn77rSTVc8A00FE9f2drxStQJzasdOws06qpOCYaQ0PWI1kM5yWvcHwrPCnBz-igubSy0wBQAtguWchYESeuuNM2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=mOrYoJmlyz-_b6Fip5KBXbCa5D7KYwkTbRUb1wyRYfVFaZTKZHCfqTk7B5wXHK8F0W0p4xi078GosHALxM59gN2wFZSzL8FWliUngqvllUBIhrmCgSklTRB3uMSLpCnx55jkVxrCqhzQYFPg8JT7UFUIrUeSIXzBzPlL9qKjRZzvU5AG618y5OAir5snAttdsiZtavUKL-UrSlMDHBGg4_SLAsvqeUdcu1tbZziMTA3_izGdKZ4JCMbwKQT1gOn77rSTVc8A00FE9f2drxStQJzasdOws06qpOCYaQ0PWI1kM5yWvcHwrPCnBz-igubSy0wBQAtguWchYESeuuNM2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=cyMEp2i7dGJic-N0zOoAFx5vsEqrlThJ4J9J6rdlVMLsWAzujsfmZVnJCSCDtplA6Xn8mMUnPmHmOMgRfK0XA_d4DL9sCetphfPusX7e-LqdDivYH47TUC_GRoPseDlKl0dVHCzvakxFrY9vUV-nif7UviG50lw0YOyxsUvx_IK7kW_UJJIHlwLQBSB01nqcdfPodphRmgCagM4UQn1fzDB8XBy0bi6JChfr9GIj7sVUa8GWbg8PENSpq_af5Km40NODEea1u6uzwW2J98ovmj_NaQqLoSXwjdO3EVTks8ASose9jZtdgeKmSHAhkmJHde7D4AHpmNXZrTwFLjkJ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=cyMEp2i7dGJic-N0zOoAFx5vsEqrlThJ4J9J6rdlVMLsWAzujsfmZVnJCSCDtplA6Xn8mMUnPmHmOMgRfK0XA_d4DL9sCetphfPusX7e-LqdDivYH47TUC_GRoPseDlKl0dVHCzvakxFrY9vUV-nif7UviG50lw0YOyxsUvx_IK7kW_UJJIHlwLQBSB01nqcdfPodphRmgCagM4UQn1fzDB8XBy0bi6JChfr9GIj7sVUa8GWbg8PENSpq_af5Km40NODEea1u6uzwW2J98ovmj_NaQqLoSXwjdO3EVTks8ASose9jZtdgeKmSHAhkmJHde7D4AHpmNXZrTwFLjkJ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbDg9XDBnEpo4BfHGnEMXwZ5beOgxVmOjM4Jrgip0nuIr-uLz01sBAj3vn1y9h0p61BUgQfmrmSmIV9QaUGzggGAsK03xBMWsskdkORtKE2YSqghQpxbbCWzTx2KyxP1EUiaWzrdL8rSUTXAVRwLb_p1vt3gYTa9wCcNmkZ0mLQg9jpGhR66d70Y-nE_DnBd3y24uT9TaL8fWiPGERQOh7fcuNG5t47FST9-AQ1NeoP6K_H2bh0DJF05Ih-2yBVQtMsHBlxZZRjCxxICxDERlRxFTTzLsHdCU8jyGzIyKLB8b1XCegUNO4BHvJBCDWDmyY-mB6mlxCoNYDlaOKKsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epOUKHtdzBQ-wl5ndRdQwJm8DIwS15xdkcZfYI9VbPOksKqgNc84AWGdBh7Qu9L61W9brMdOLnDCQGOSimtrMgPKeTVyHRPvXKKhWZ2yLeZkRa_1hdjnMnOB1D-i7P80PulfXSHyWEO3Qbl_DGs33qCTkMvcIX5p8WOHBIynr6JFMejt3KbTPuy9YdDzehWo6PbMH_0GYM_LcIlvwFQIzwjxd91GoI0PE6Btjx5EORtuWqgfo-9T1enHA-ZtJhLUUdHPm4ZtFqjCwjrp5OYaqTl8-5Ws-oJ-XDya1xuOSCvFSfwbBaHN7Lc_gzSfHJxMu6ctygyiTfxCWWPom8sZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMGtbSYETjqYTijS7JeVD_RmX0bFq6LCFSsYWZeN_OTPKvuWmEm4zBKoUznZiZUykP9NBLj2YPTm8-EX31f9NyQiDW8s14Bxt_rz7oX3oY9R5yxg3FmR0PtfVUWNJt3rOfpWbFTKvWeaVmZVlqYXNXM30a5GAsV9opCyeaXbLrKoktuNQcmtvniFUZG5yQ0x_3k-Gfre7WErww03aMUVhynlPkZKpSuybVCxn3xFHlFFE-NwT286XziS5aGUgvxLGRKes5cZL_YlsZ9ODmFjVK5SwN-ItpSYgwjMEHHgWazQeaDgvxdOWIbbV-Zb0Dhx6hN67fcbZ8H-ZZ5pPX-OKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiG37fhvtnzQnmRYoDKfkuZ2o360fNLY6Zth2pP0fH5q1vCNbqCIvoCloRpcsOzZ7jlFu9jin2Y032RhiSnePfqP17gzw1KoOTOlbQ2pngz9o9HISIPTFgii2JSRKnm0_Cm0jm1uy03zg0fqFCurl6a4pdKJ5zTPbpPBe50Xm_0WEOQ-9lv7393bhNJdraf7zbcyPDD7v6-u6y4VKR12Z9ndGBJVYJVXMcewu5h4K5SsK9qGw8M_8Y7MMpXLMElzLEvGyc8WmKsM2Ny6ell91Y0Ko0b_ROGfB2s9mhxygrTblEsjOiW24zCY0FxbT3A7-1JSqLU-gSkEDMd_IhVLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeC7ioUn88m3mxBgGk3ao5vLapzY6MxCelcsIKatg457glQc2GR6rxlU5f4Cy0a3n0bkShDfaL3tyxUVpGOfv45DBp_Cy42lm78vAwWwSsunf79GJViqg0wqd6ZgHxHA4eWXg_k6ZUqSbph6RAd0y-WHm8RiPc18F2qsTtic0tIYA_WY2a9ACe8liH_jtp_-ug1PuHt6aY8EDIyBoDoAP0CNZwxMRZtLzEnJnSyggFLDc2zm7dYg16QuaJcL-7UJ9twc4oPwDAfzOySlIeX9VGJeWFjMZFwM_SwEcH7ooY2NHFtD0ZppVgoaf31qKWXhTU2ZrH9qf8BI-v4kvGpvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz396K-n1uL0K7m4YuGur1kLy-NtFHszG35siFUN7bK7fW6-sI5GHi7ru2aQY1QaL6lUyyiC2qx8FNH7Cadyp_Cyd6X9pWi0T0z_a3HxQxEGYIve5f6C26T3ZduBGBTfPlVxhdv8gEA4jHeQ6utjj6QbINquUivdtOgkYrblZqnHUsXmb1ekdmZJzKcZch0Dnp9x6dFYzS-hbyZob105D1kPySLj5AfaMjbM-AfpwFzikvKwuj_RgUbHMbrCA4qqjmnoDvLuwus-Ddl6PXt0-JuDweGDXYqQQWR45nk2180egTSU8TzOI6VOwZUQs0vQ5zkB40QLTfLYnLGGmFCr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPOr8HyweMAeBUtHsTyX_QcfhIZNIuW-DPKD_eR8nPrpLw9eZsCoSzRfKhNTTPNWmtRRdE05lIjVJJcU8Vxh9gxleF2ef7i3_1uFH0SeNOhmHFZnMl1gETT1howTnCyzSit3y8zcWZWLXjYpkrPIJKjfKPKT11fnGilUn1tew6aLogpSaz7WLGUyf7ECUy8r4kxOgH9_q2zWfhMNmsOZG1k3iVAB0QqVqPewilFYrBrhdbpuYmlGIr479kikO7PngTcnNBjjhJ4DvZQnIJqyXtpkUL0XNQRCVvZfgidFi4BpcQ17VbfWIwJwPd__O1xc4LniUCaj51O-A3hPG1kq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpYHOAmVMHnTAWcFtxbVUYzSO_jgm24qcsmwt7YYjoydULbjNsp91oZT21v8bl6assZzf0gFVy8aM6u6_CbrSo6k_eCnNVeYz1nMQgaG9sYtgLbh3yYFltxQ6krzAth22Hz38LuebwoZA9KJ9HYFUkti2VTPeKG_HUvSka5TtIlsCh31Q_lfsXy19AVxo9nvFuLNbBXbROR4owOwzzvwbM5NyZhhl03OpdKyGUwEQE7OsNKdh9r8SVHIbwiM0IEctTFUrJikTAMH-284Iz7Bd0edqh_Y5Hj6NcnwpkvcQVSHl71ZMwFLLQU_ftkiezxb-8n8szMfDW0FGY8faEJXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
