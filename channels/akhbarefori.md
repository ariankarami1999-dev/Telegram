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
<img src="https://cdn4.telesco.pe/file/Fv4DFSyCIVvujP-oiP82KWpiD-TnvMTQg_sCXaK1hwbRgoLS0l-xgyvBCJtUP1g7Ur5yq_k6KnXdkrjLgAsPMSJWevtP_69m1mb58_zMCRwpx-_-iL5ERwyQf_x2XnYofltQHTcHkimHDgmG9kFGpi2d7o29cBr7ODKYw9qmW6Zdbx3YTDubo6OriJW6tA6-QzUat4URLlEtcWtVLl3lKAV_AcIzpj6J3n2PoNP1MieArFJS5gVVRjCpiAv2Swg1P3ZmYknPj5xbesmzpSWI8sLy_a8yqRYnQvfa1B-OAwlt293mTDeiVJcc74nMRHaPKKm9CYw1JpYbLQgRUXrN_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.91M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 02:09:20</div>
<hr>

<div class="tg-post" id="msg-652040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
اقامۀ نماز آیات برای تهرانی‌ها درپی وقوع زلزله واجب است
🔹
به دنبال وقوع زمین‌لرزه در مرز استان‌های تهران و مازندران بر اساس موازین فقهی، با وقوع زلزله، اقامۀ نماز آیات بر افرادی که در محدودۀ لرزش حضور داشته‌اند، واجب فوری است.
🔹
طبق رسالۀ عملیه و فتوای مراجع عظام تقلید، رعایت نکات زیر حائز اهمیت است:
🔹
محدودۀ جغرافیایی وجوب: اقامۀ این نماز تنها بر کسانی واجب است که در شهر یا منطقه‌ای حضور دارند که زلزله در آن رخ داده و یا لرزش آن را احساس کرده‌اند.
🔹
زمان اقامه: نماز آیاتِ زلزله باید در اولین فرصت ممکن و بدون تاخیر (پس از رفع دلهرۀ اولیه و پیدا کردن شرایط ایمن) خوانده شود.
🔹
اطلاع دیرهنگام: اگر فردی در زمان وقوع زلزله خواب باشد یا به هر دلیلی متوجه آن نشود و بعداً از طریق اخبار یا اطرافیان مطلع شود، همچنان خواندن نماز آیات بر او واجب است.
🔹
تعدد زلزله‌ها (پس‌لرزه‌ها): با توجه به وقوع پس‌لرزه در ساعات گذشته، اگر فردی هر زمین‌لرزه را به صورت مجزا احساس کرده باشد، برای هر کدام یک نماز آیات جداگانه بر او واجب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/akhbarefori/652040" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران به اکثر تأسیسات موشکی‌اش دسترسی دارد
🔹
روزنامه «نیویورک تایمز» بامداد چهارشنبه نوشت که بر خلاف ادعاهای ترامپ، ایران به اکثر سایت‌های موشکی خود دسترسی دارد و ۹۰ درصد آنها عملیاتی هستند.
🔹
در این گزارش آمده است: «ایران دسترسی عملیاتی به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده است، که می‌تواند کشتی‌های جنگی و نفتکش‌های آمریکایی را که از این آبراه باریک عبور می‌کنند، تهدید کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/akhbarefori/652039" target="_blank">📅 01:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS7el8gs70WFvERz1o0U1s5YKl2Cys3PPA9XrjvpTMDaICYS-kiCYzCWoj6B05VWoiHrUfpi6BlrKvUKj4BB03-jppLTJveLl5zD_QrgIk8DF6Q4gOr2gUWKRwZBNjOBbjqB60hVon2Y9Q2l1vynxuEq0O2w6orQDQcDfiMJHYZWC_-zDG0916KrWNswS_rPNVH_Pg1xhbEFIO2Bw-LQO_Td89l7g-ZUL0efiBWyYrLPuUBNeST0xkUFerKD5rasij63dGRBnUEAPoa9DDrck4q0oMBA-diIfn8LomPrVOkQ3UTOwYipsCj2xkWyqhs4Tkq_PtZ3Ge2yte8FXa4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف صریح مقام صهیونیستی: خوشحال می‌شویم اگر توافقی میان ایران و آمریکا در کار نباشد!
🔹
منابع اسرائیلی گفتند توافقی که برنامه هسته‌ای ایران را تا حدی دست‌نخورده باقی بگذارد و همزمان از موضوعاتی مانند موشک‌های بالستیک و حمایت از گروه‌های نیابتی منطقه عبور کند، باعث می‌شود اسرائیل جنگ را ناتمام تلقی کند.
🔹
یک مقام ارشد نظامی اسرائیل نیز ماه گذشته به خبرنگاران گفت که اگر جنگ بدون خارج شدن اورانیوم غنی‌شده ایران از این کشور پایان یابد، آن را یک شکست تلقی خواهد کرد.
🔹
این منبع ادامه داد ما خوشحال می‌شویم اگر توافقی در کار نباشد، خوشحال می‌شویم اگر محاصره هرمز ادامه یابد، و خوشحال می‌شویم اگر ایران چند حمله دیگر نیز دریافت کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/akhbarefori/652038" target="_blank">📅 01:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مصرف ۱۳۰۰ فروند موشک پاتریوت از سوی آمریکا در جنگ ۴۰ روزه با ایران
🔹
رسانه‌های عبری اعلام کردند که آمریکا در جریان جنگ ۴۰ روزه با ایران، ۱۳۰۰ فروند موشک پاتریوت مصرف کرده است. هر موشک پاتریوت بین ۴ تا ۴.۵ میلیون دلار هزینه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/akhbarefori/652037" target="_blank">📅 01:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فعالیت‌های ماگمایی قله دماوند با ایجاد تغییر در فشارهای منفذی، باعث تحریک گسل‌های اطراف می شود
🔹
اینکه باید منتظر زلزله بزرگی در شرق تهران باشیم از منظر علم میان‌مدت و بلندمدت زمین‌شناسی دارای دو جنبه است، از نظر پتانسیل لرزه‌زایی که از نظر علمی، گسل مشا توانایی تولید زلزله‌ای با بزرگای بیش از ۷ را دارد.
🔹
با توجه به اینکه از آخرین زلزله بزرگ این گسل (۱۸۳۰ میلادی) حدود ۱۹۶ سال می‌گذرد، این گسل در مرحله تنش بحرانی قرار دارد ولی هنوز در حال حاضر هیچ ابزاری برای تعیین زمان دقیق وقوع زلزله (ساعت، روز یا ماه) وجود ندارد.
🔹
وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی: وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل دارد، ولی این لرزه‌ها نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر نیز می تواند، باشد که مقدمه رویداد بزرگتری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/akhbarefori/652036" target="_blank">📅 01:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مبادی سفارش‌ها تغییر کرده تا بتوانیم کالاها را از مرزهای زمینی و بنادر شمالی وارد کنیم
🔹
گفت‌وگوهای جدی نیز با کشورهای همسایه و کشورهایی که با آن‌ها در تعامل هستیم، اتفاق افتاده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/652035" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApqBSqaXtxuyp7H_Q1BwVsTFanlSQ7N9P3kdEU3bQ8i0lG8R_e6WOXntoIqJzcDpK-Ub1Blsh0_RUy2QMKnMvrtax9AOl8SaMrTkmuqUWi9PvADrWiAHbr6z_JoxY_7AI84Ncqbvw1hbf9srNpfulovACZ4P_S7TzuBKpl-FrMoF4MiVCWmxRakuHE8kYbIktukFUxcOQ1zqfm_cqD85WfMB1udEj0ojiLOH8c2g_p2n03XOkHR4LDfWivVeVb5Ya1GhY-qxSacYdRIm9rLmLhyOeCedad_PwMNrZd8uZUHFXkiKw_r8PzpgLrIVGIAjUPtnftdT7lajWaeX-NRgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: آنچه بر ملت صلح‌دوست ایران تحمیل شده جنگ متعارف نیست
🔹
سخنگوی وزارت امور خارجه در پیامی با بیان اینکه آنچه بر ملت صلح‌دوست ایران تحمیل شده، یک جنگ متعارف نیست، نوشت: این جنگ میان دروغگویان حرفه‌ای است که برای خشونت‌شان توجیه جعل می‌کنند، و مردمی شریف که فقط با تکیه بر توان و اراده خود، از وطن و کرامت انسانی‌شان دفاع می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/652034" target="_blank">📅 01:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز و امشب، جانمانید
🔹
🔹
زلزله‌های پی‌درپی در تهران
👇
khabarfoori.com/fa/tiny/news-3214578
🔹
دیدار مهمی که سرنوشت جنگ به آن وابسته است
👇
khabarfoori.com/fa/tiny/news-3214551
🔹
ترامپ به جنگ ایران بازمی‌گردد؟
👇
khabarfoori.com/fa/tiny/news-3214321
🔹
چین بین تهران و واشنگتن میانجی‌گری می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3214364
🔹
سیدنی سوئینی به سوی آثار مستهجن می‌رود | ماگا علیه عزیزِ ترامپ!
👇
khabarfoori.com/fa/tiny/news-3214209
🔹
تصاویر و ویدئوی املاک توقیف‌شده خبرنگار ایران اینترنشنال
👇
khabarfoori.com/fa/tiny/news-3214399
🔹
ویدئوهای جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/652033" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
زلزله دوباره در تهران
اخبار لحظه به لحظه
👇
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/652032" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qc1sxyukmacHGjhSydTofEaGT2to7fBOA7BSxv03M1jW9tBGfQt1sJWYSYMA8WXIDs_qo8eIxX4On_yc8tM4JuAvvZ0cdc-zqOO8BXyizE3ip-fDy3fsm45iB1SFATbBcvG3Kn2O02TmJ-szZLwX37asA99_U7uYZOSdIIVvkLKt8wLjYzL2NVEsdZ_1wusXa3wJ1URr3th-uuqKt_Hovl0XXqOAKin9C0KtfqS-as83OeRWUaRjC-4mRJ4mc2B3FE9geK33ccAhkkYRVoHMBl7Icl_J_MYBQln85ZPUXfiE_-qmXbbJd8JsYbhuTI2ERoDk_awv5nv_zm9KKCGGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekfJrgtXFL3YA8ONEIaGCVXvUkcFqoJvRRIJM3XrKzQw4wPeI3tdQHCJhajVRg3todHbL2WNOWXSgkLnC-AQTxM27xn81LSWS1cnDXpBAURm73wB2X3RS9TSsrIgx5b4QQolRZdTOWnOVpsfZIFRjQ2dZwjcQyws8-ytNGz3Gfea_rN5GJ6TQ9PXFvaho2mcXt4wCPkfhm1Z5_ftpDgPSYMeLnOtcdovr6UX66oEYuKKe091lxgamD04Opk9zhi8e9wMBmm16oLZTz6vlJkHEwUx9D5VqWvb4_qnjUTjmqYVMDwZ9k2LA94vJDbjfC28HnBtOwppc4bmV3smNXL5zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم اکنون؛
🔹
پایش لحظه‌ای وضعیت تهران پس از زمین‌لرزه در مرکز عملیات اضطراری سازمان امداد و نجات
🔹
در پی وقوع زمین‌لرزه در تهران، نشست پایش و رصد وضعیت با حضور مسئولان و نمایندگان استان‌های معین، هم‌اکنون در مرکز عملیات اضطراری (EOC) سازمان امداد و نجات جمعیت هلال‌احمر در حال برگزاری است.
🔹
در این نشست، آخرین وضعیت مناطق تحت تأثیر، آمادگی و همچنین هماهنگی‌های لازم برای تسریع در روند امدادرسانی و پاسخ به حوادث احتمالی انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/akhbarefori/652030" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdQRDG5Y2r7ujlFXZnddogDPZ8iKjlRnMSGAipcNMgQtxTs-eVLXv8id45qUVyHyX_qN2yUVQVzIWfliPueZi_Y9A0ryDfa-cYwBxUvvEK-CNd63nLiwKQZ8GeOcMhjVs8FVR2-DHQ2ks9fUkdiIKuuWbfRfc6v1hJn6hIZ2ZwjWPDJtVUDZ8n-T3pgxS6oggWFHyUZ8yQCNnsPPIfe30JeqdHywE_e7V4zb5L2ObTv9zn2hOHr_2FojeWFiL9lBKgWO0Krf6MOl2H6lUxZH6yBTtCtPizpRHWB7JS_lkP7AEwLZXaVlDgAss_duzojHsIlGLVQXu-DDqU1NncqlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ:
🔹
وقتی اخبار جعلی می‌گویند که دشمن ایرانی از نظر نظامی علیه ما خوب عمل می‌کند، این عملاً خیانت است، چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آنها در حال کمک و دلگرمی دادن به دشمن هستند! تمام کاری که می‌کند این است که به ایران امیدواریِ دروغین می‌دهد در حالی که نباید هیچ امیدی وجود داشته باشد.
🔹
این افراد، ترسوهای آمریکایی‌ای هستند که علیه کشور خود ریشه می‌زنند. ایران ۱۵۹ فروند کشتی در نیروی دریایی خود داشت — اکنون هر یک از آن کشتی‌ها در کف دریا آرام گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/652029" target="_blank">📅 00:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
جزئیات کامل زلزله شدید دقایقی پیش در تهران
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/652028" target="_blank">📅 00:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پس از زلزله اخیر در تهران، پایگاه‌ها و امدادگران هلال احمر در حالت آماده‌باش کامل قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/652027" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
دنی، سیترینوویچ، رئیس پیشین میز ایران در اطلاعات نظامی اسرائیل: هر توافقی تنها بر دو موضوع اصلی تمرکز خواهد داشت؛ کنترل تنگه هرمز و حق غنی‌سازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/652026" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX1cVCHwlDFy2f8WkSQNAeHcNdir4ePgrLW0eKIkVxew1sqfFM2DawloK4DEaziL2tqir-4hdCw_z2vw95ie9IdX8eqS6IAEPTFMbc3sUEnz-JlPiHG7qmVfUpTuhyxRNLgLRszJ91vDYuTV6-ZB_Sj7kT6G9Zs5_eRBvKiCKkw4I390FceNnxCYeYwDBIVhZODSMdChAyr4xJg8TNiB4IXO-XOKXIpQ-0fYuN3cybH6UbfSk9_lDKvSEMLe1yHq9UnIg-iygNc6Ri2WUGm0Zg3eU6ZO1dlOilOkQGw-CQmoIxFKj_NyfEIYKC_fkJT6s4Y0-RTARTQ_HFXTlWbhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: زیاده‌خواهی و عدم صداقت آمریکا مانع حصول توافق است
🔹
وزیر امور خارجه امروز در دیدار معاون وزیر خارجه نروژ رویکرد زیاده‌خواهانه و لفاظی‌های تهدید و تحریک‌آمیز طرف آمریکایی و فقدان حسن‌نیت و عدم صداقت آمریکا را مهمترین مانع برای پایان قطعی جنگ و دستیابی به توافق احتمالی خواند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652025" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
زلزله شدید در تهران
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652024" target="_blank">📅 23:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تنگه هرمز معادلات جهان را برهم زد؛ همراهی با آمریکا دیگر صرف نمی‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/652023" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Lg2qy5a9q6QH0p22CmLgzC90nkJwcehlq7QEQKKHFUY-2HFM2rVDKQJ54OvleTNzJx5DQI5Ip-TvNY2evyDM_U_SW7134GPoTCg-8mnFGv-kdpc5LDD6GJkJYnPxPoggVaq-t7EOH9rZ5H0tOCLP9EeYT9Frt8gvveVdE_jzUNK3VSk5ELSV2HxiIKA5t41EIkYDOC4RCVVf98dhgH6fZaX8QghctkwrFuJuAHrVKcmVOgxg3js0CmtNf_EqifOYdoGqQpxdIMRaFbytOFnP2Al7HNDuOsid1ce_tYj2T0nRS2QPljtIV8DStP8K_sbCJdq3aMzE2mOfgtQpIllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار مهمی که سرنوشت جنگ به آن وابسته است/ نقشه ترامپ برای ایران چیست؟/ چین صلح می آورد یا به زودی جنگ «تنگه هرمز» آغاز می شود؟
🔹
واشنگتن تلاش خواهد کرد تا از طریق چین، تهران را مجبور به لغو محاصره و باز کردن تنگه هرمز کند و امنیت انرژی را به یک برگ برنده مهم در مذاکرات با پکن تبدیل کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214551</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/652022" target="_blank">📅 23:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2170f2149.mp4?token=smvnaNoYCKiifnF6EkKLIU1f0ZN5n8VajYba5tpXtSCf-M-oUWD3fsKHD17K3eXbx7gwfwR7k5wYHf3I4ZhAXo6ScF3Bh5YRlG7jYQkxh6gFxAfzTiqwsULkvlIqN6SNjQpouL5Uoi81lq8aE6IoDFH825IvUDELXj8dT_iUIfmzwrsvnmhR-7CfOmNR3ATw7Vgev1kPg5_MTvWGywEFF0KHUX61lq3-EMyvTL0-alpMLzApk-4SH24wgZubQ4XW3AqoF33xUzCKZ-KaQE3Dow6ol5kYF56yWHzSiW4w84EDBXzag9r0CjxsySEEgRddcDnXldCc86mcJoeP4nyslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2170f2149.mp4?token=smvnaNoYCKiifnF6EkKLIU1f0ZN5n8VajYba5tpXtSCf-M-oUWD3fsKHD17K3eXbx7gwfwR7k5wYHf3I4ZhAXo6ScF3Bh5YRlG7jYQkxh6gFxAfzTiqwsULkvlIqN6SNjQpouL5Uoi81lq8aE6IoDFH825IvUDELXj8dT_iUIfmzwrsvnmhR-7CfOmNR3ATw7Vgev1kPg5_MTvWGywEFF0KHUX61lq3-EMyvTL0-alpMLzApk-4SH24wgZubQ4XW3AqoF33xUzCKZ-KaQE3Dow6ol5kYF56yWHzSiW4w84EDBXzag9r0CjxsySEEgRddcDnXldCc86mcJoeP4nyslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: برای واردات دارو و تجهیزات پزشکی، کارگروه ویژه‌ای در دولت تشکیل شده است
🔹
مسائل و موانع مربوط به واردات، از جمله موضوع ارز، با همکاری بانک مرکزی پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/652021" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CViyES94f3p9VO27kxL_00bSs_wCvkAqt_ZD3GssNxB_Y5v1KwSIyS9u3uQp94V4JXeXFB2JyLyMXaVKW6wAMuYzQzDH_5whsUrdjQU2GA0h7j0ewqyihlCpLdPJyKyUtvY9LXnHii6Zo7oHvzQOyx5cJttFjF8YzaIY59H9jO_Ia_zaxPJ28GRAS0RMlbSyhr7ihXq05jXGdlbu-AXsxqp_Pb7KDmiuYlgDYVSxTYbS2xHHcxXns4_I29xDrHMHh6uefJEWO8mcJMijlLa73gRcc-Oay0NC090iApFoY9dVtLPJig17dnCJH5cNlavqdjMac_yThHmzOj3W5FMgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزار‌ش‌ها درباره حمله عربستان به ایران در طول جنگ
🔹
خبرگزاری رویترز روز سه‌شنبه گزارش داد که عربستان سعودی همزمان با تجاوز نظامی آمریکا و رژیم صهیونیستی، حملاتی را علیه ایران انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/652020" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پنتاگون در حال بررسی تغییر نام جنگ علیه ایران است
🔹
شبکه ان‌بی‌سی مدعی شده پنتاگون قصد دارد در صورت شکست آتش‌بس و از سرگیری عملیات جنگی‌ نام جنگ علیه ایران را به «عملیات پتک» تغییر دهد.
🔹
دونالد ترامپ نام عملیاتی که در اسفندماه علیه ایران آغاز کرده بود را «خشم حماسی» گذاشته بود اما بسیاری از منتقدان به این عملیات لقب «خشم اپستین» دادند.
🔹
این منتقدان معتقدند یکی از انگیزه‌های ترامپ برای آغاز این جنگ منحرف کردن اذهان عموم از فساد ترامپ در پرونده مجرم بدنام جنسی، جفری اپستین بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/652019" target="_blank">📅 23:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbQcwxk3qGrxa6FUDGYjZP2eIqpxgb_EyJ4RBpQkGwSk-nj_iLI2SkxMMHau6rEhAWRUsDhoZyX-gUE9AkEf5jTOAArLR1WH3nZGv1Rp79p1h6WOE2Dqjz0Va6KzG3a4zhQFwuUd-j2ODT3fN4aFIdz-6KSrkMprXUBaQdI5gNcKbi4UphwI3hqTMoiJ7bEYmFrvbsvHXhQK-yjNncVro3bZuPioxxzdheGqdBENAFcb7Zpxug7KLI3n3PA_P015Y9hf9XJQmJ1AFM1di8TEl_HSuqPcVdimBVLM7PxX-K-MUEgayguTUyR6tWQfe_ncmKAv812s7R22xj2z8kjUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌خون
🔹
مردم نجیب ایران، حتی در روزهای سخت جنگ، رسم همدلی را پاس داشتند. در جریان جنگ اخیر، بیش از ۴۰۰۰ کودک از مراکز شبانه‌روزی بهزیستی به خانواده‌ها پیوستند و ۱۲ شیرخوارگاه به‌کلی خالی شد. در هفتهٔ اول جنگ رمضان، شمار مراجعه‌کنندگان برای اهدای خون ۴۹ درصد و خود اهدای خون ۴۰ درصد افزایش یافت. در مجموع روزهای جنگ نیز آمار اهدای خون ۱۲ درصد رشد داشت. این آمارها، تصویری از همبستگی عمیق و بی‌ادعای ایرانیان است.
🔹
هفتصدوچهل‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/652018" target="_blank">📅 22:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb2d80e06.mp4?token=CFv7S2J63J2gOtA5-Ln30X6SjRFVtH_8uB7qmwkDpnbhKH7C3wQ_wQV34m7ZpJN_F75HjKXAtBuztIOiEPvR0l72QsAhlevteqcNbpjmUtU6sPlNjMVLIXidDxUn47u7OMddABELVVNZTb6YfsysSkJazyhu2Vvodp16maSDs8iUOLGxuP1okD3TDFG5BuVTZXC_Ozio1UOlJha_pUTTDJWmk1H0O0ikl4Pxgu1R3nIjQTgTMK39wHXHwsLYIU_FiqgPSuouMTcUFkej5nsw2uuOyn1cs92LTsL3izNaAve9PWKnntXAo-X5LW4lGuW2aZ9sXEPfZIgNgmGagtlRQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb2d80e06.mp4?token=CFv7S2J63J2gOtA5-Ln30X6SjRFVtH_8uB7qmwkDpnbhKH7C3wQ_wQV34m7ZpJN_F75HjKXAtBuztIOiEPvR0l72QsAhlevteqcNbpjmUtU6sPlNjMVLIXidDxUn47u7OMddABELVVNZTb6YfsysSkJazyhu2Vvodp16maSDs8iUOLGxuP1okD3TDFG5BuVTZXC_Ozio1UOlJha_pUTTDJWmk1H0O0ikl4Pxgu1R3nIjQTgTMK39wHXHwsLYIU_FiqgPSuouMTcUFkej5nsw2uuOyn1cs92LTsL3izNaAve9PWKnntXAo-X5LW4lGuW2aZ9sXEPfZIgNgmGagtlRQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون اصل نود مجلس: وزارت تعاون و دولت به سرعت مبلغ مابه‌التفاوت کالابرگ و قیمت اصلی کالاها را به روز کنند تا مردم بتوانند با آن مبلغی که دریافت می‌کنند براساس قیمت مصوب کالای خود را خریداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/652017" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
جزئیات جدید از پایگاه مخفی اسرائیل در صحرای عراق
🔹
روزنامه عبری‌زبان «معاریو»: این پایگاه علاوه بر آنکه شامل یگان‌های کماندویی برای انجام عملیات ضد ایران بود با تجهیزات پزشکی و گروه های پزشکی نیز تجهیز شده بود تا چنانچه به خلبان‌هایی که در حملات هوایی ایران آسیب می‌بینند خدمات فوری ارائه دهد.
🔹
چند روز پیش روزنامه وال‌استریت ژورنال در گزارشی از تاسیس یک پایگاه مخفی با همکاری نیروهای آمریکایی در عمق خاک عراق در صحرای نجف خبر داد.
🔹
این خبر با موجی از واکنش‌ها به ویژه در عراق مواجه شده و دو تن از وزرا و فرماندهان ارشد عراقی برای ارائه توضیح به مجلس فراخوانده شدند.
🔹
یک مقام امنیتی عراق هم اعلام کرد: نیروهای "صهیونیستی ـ آمریکایی" برای مخفی نگه داشتن موقعیت این پایگاه سامانه موقعیت یاب (GPS) را در مناطق صحرایی غرب عراق مختل و تجهیزات پارازیت‌انداز در آنجا مستقر کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/652016" target="_blank">📅 22:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a60e4070.mp4?token=hAmyCf_g7QKVboJnjtdHLobBBGl1LsTxeZGUvPRoHen7QDl1Dbws5JmQ0yQmr_MOy-q79eIB4fbNSzrL0XuXVxKGZno613bZJVEuL97o37Y1GTc3HaXU3aTo6y4kyLT4X8V_njmTklynV4XmXvzERunDCozUYetlqPI7bkm1vIoFMdAmOPZMVgtZLJpwgWCFHIaWkBMAZ5kBegKAfzouXjOzbluCpuuO-qa7DvyaD_E5XkbsiuGXLB2cSw09JcB5Ygz2rPwkN_8CDV4up1n6_rUzmU57msIcfOYFmn_rbF6nP3qJHpfYjF_K5bJKIv6ueFp59eRmv9I2q2sua1f4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a60e4070.mp4?token=hAmyCf_g7QKVboJnjtdHLobBBGl1LsTxeZGUvPRoHen7QDl1Dbws5JmQ0yQmr_MOy-q79eIB4fbNSzrL0XuXVxKGZno613bZJVEuL97o37Y1GTc3HaXU3aTo6y4kyLT4X8V_njmTklynV4XmXvzERunDCozUYetlqPI7bkm1vIoFMdAmOPZMVgtZLJpwgWCFHIaWkBMAZ5kBegKAfzouXjOzbluCpuuO-qa7DvyaD_E5XkbsiuGXLB2cSw09JcB5Ygz2rPwkN_8CDV4up1n6_rUzmU57msIcfOYFmn_rbF6nP3qJHpfYjF_K5bJKIv6ueFp59eRmv9I2q2sua1f4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستاورد ترامپ از جنگ با ایران: تقریبا هیچ!
🔹
سناتور آمریکایی: هیچ‌یک از اهداف جنگی ترامپ علیه ایران محقق نشده است
🔹
سناتور دموکرات آمریکا اعلام کرد اهداف اعلام‌شده دونالد ترامپ در جنگ با ایران محقق نشده و این جنگ نتیجه‌ای معکوس داشته است.
🔹
کریس مورفی، سناتور دموکرات، گفت: هیچ‌یک از اهداف جنگی ترامپ علیه ایران محقق نشده است.
🔹
او افزود ایران همچنان بخش عمده‌ای از موشک‌ها و پهپادهای خود را در اختیار دارد.
🔹
مورفی تأکید کرد برنامه هسته‌ای ایران همچنان پابرجاست.
🔹
این سناتور آمریکایی گفت ایران پس از جنگ از نظر نفوذ جهانی حتی قدرتمندتر از قبل شده است.
🔹
او در پایان این وضعیت را «یک فاجعه کامل» توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/652015" target="_blank">📅 22:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0348a6d7.mp4?token=XJcD4_2v8LwTCmuqATUwbAj1i1M8xDBef1BOPG102PyhBJQF9LXYdx-9Oh6un6r7jpEy1uV08kiUBSAYhsvuHdzO3G-lNkXL9NB8twUC53Mn2PNBPXlFDSM609bGZe5rxYqyGBeCRpLAZsTs0o0jN-fLJV77n8nE4PZLamwJGvT1h9CjpZwp1BJDClMsn2f5NRVv0ZUcj5s4PU3W3DX7AtO4hcIGad9uNdlOrzkrLXGjcXdtRtO-fhcrA8AdSrqnVGq8Y9EM0U9bq2-6BgIh-Apz64zesnZLYT4XiSyAE1BLiCOHP7oOdE12Ojm_SUKPaWaLEQMTz5nxPZjEC1KhqKhKKPVvApsN3AiVubBrG4wVNaAo1rjZxHs6I7Cxv0ZfykKQr1EvbrOI6ogBNYhzueQUWWa5lFEUiECWi_T1oQhFrl8oRjFCydpMV9PKELMr8wpNFVko-tJfgPXSbHj1g1BJeBNCuI3zFsbARwLBCa0YxBmf270XtnE1KwPzmG5NTxsoy_rpkxIu3I6S_kbRO6UDp0QRMrMIDvBJvy_0eONKD8MfgVt-YQuvYAGRdZwxoFUNOa8zjBmSCoD_q5XSJpDwBFZ7FU_KyZZJyBy1zeSK8XiCjcrko7uHQs6jT4NNQcVWyQmJS4LqW_eGG1vw6wGlglU_HJ_597UKQWZz-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0348a6d7.mp4?token=XJcD4_2v8LwTCmuqATUwbAj1i1M8xDBef1BOPG102PyhBJQF9LXYdx-9Oh6un6r7jpEy1uV08kiUBSAYhsvuHdzO3G-lNkXL9NB8twUC53Mn2PNBPXlFDSM609bGZe5rxYqyGBeCRpLAZsTs0o0jN-fLJV77n8nE4PZLamwJGvT1h9CjpZwp1BJDClMsn2f5NRVv0ZUcj5s4PU3W3DX7AtO4hcIGad9uNdlOrzkrLXGjcXdtRtO-fhcrA8AdSrqnVGq8Y9EM0U9bq2-6BgIh-Apz64zesnZLYT4XiSyAE1BLiCOHP7oOdE12Ojm_SUKPaWaLEQMTz5nxPZjEC1KhqKhKKPVvApsN3AiVubBrG4wVNaAo1rjZxHs6I7Cxv0ZfykKQr1EvbrOI6ogBNYhzueQUWWa5lFEUiECWi_T1oQhFrl8oRjFCydpMV9PKELMr8wpNFVko-tJfgPXSbHj1g1BJeBNCuI3zFsbARwLBCa0YxBmf270XtnE1KwPzmG5NTxsoy_rpkxIu3I6S_kbRO6UDp0QRMrMIDvBJvy_0eONKD8MfgVt-YQuvYAGRdZwxoFUNOa8zjBmSCoD_q5XSJpDwBFZ7FU_KyZZJyBy1zeSK8XiCjcrko7uHQs6jT4NNQcVWyQmJS4LqW_eGG1vw6wGlglU_HJ_597UKQWZz-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ بسته حمایتی برای صنایع و کسب‌وکارهای آسیب‌دیده
🔹
وزیر اقتصاد: ۶ بسته حمایتی برای صنایع بزرگ صنایع کوچک و واحدهای تولیدی کوچک و متوسط و کسب و کارهایی که به صورت غیر مستقیم آسیب دیدند در نظر گرفته شده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/652014" target="_blank">📅 22:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
یک منبع آگاه
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز» می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/652013" target="_blank">📅 22:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حامیان ایران در برلین: کودکان چه می‌فهمند از جنگ و موشک؟
حامیان ایران در برلین:
🔹
کمترین کاری بود که می‌تونستیم انجام بدیم...
وقتی مدرسه‌ها هدف قرار می‌گیرن و بچه‌ها کشته میشن، دیگه نمی‌شه سکوت کرد. این بچه کوچیک چه فهمی از جنگ و بمب داره؟
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652012" target="_blank">📅 22:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02512faff.mp4?token=bO2Q43iswqxLqmzE2eLnnCFFGa4dEcUpiIf5LjwrjOzrhG-H0oaWzIul3NZr-QScu7b39J-90_Dtylg9Ds6OLX9am7DJ81fMPCSsKLarcUhhJ6sGuM83strh3Ce1dMvwnZ8N6GQza_zEjYeHF2GDp5rejoRlUzLtdYRCsU4wrVgHsGBaLbqbfRs4hCz4Gy3ohabNZVwAR-_gFDo_nW-Fk-sMy2FyFz6fWPvdI83q1Zm2kZbW6SBonYKGsSseQtx0w51RBseHzQ8zdkwg-cRwqcuy5p753PJ4pA05qslyw6A1rf1zTVO-c7V6SIVJIIzCxZ_LKIMMwqdGTs1dCh_OLhE5XZK3YZ4v61m91AW_1Hal1SSOHsNEcuX7zkov1M3RJ3h1rJnGa-s1sDNblKpbOj0F06_E0WjL2M_-uWrPOa-lCZ0sUHbJb9Waia2APObu7EATzwK9XP7zYK0B8bI9zlihMKJzRLKJupkyimGv2FFJpYFfYDG1pMhoXCeGksKZnXoWwNc0_hLdKyjXvoAVwbSKv_NQBieYt6jdyAnFlauokPu0LITqMU7QL02JBzGA67Bhyvgx64nxnhW1XbJdu1Z1XYRD_7zKiY_S10K1DX37hIV23Khili8s_5WfnbMGHYSNgb_RPrA_9ksoc-ds5mwEtF-37E9v1b9lvzq3aKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02512faff.mp4?token=bO2Q43iswqxLqmzE2eLnnCFFGa4dEcUpiIf5LjwrjOzrhG-H0oaWzIul3NZr-QScu7b39J-90_Dtylg9Ds6OLX9am7DJ81fMPCSsKLarcUhhJ6sGuM83strh3Ce1dMvwnZ8N6GQza_zEjYeHF2GDp5rejoRlUzLtdYRCsU4wrVgHsGBaLbqbfRs4hCz4Gy3ohabNZVwAR-_gFDo_nW-Fk-sMy2FyFz6fWPvdI83q1Zm2kZbW6SBonYKGsSseQtx0w51RBseHzQ8zdkwg-cRwqcuy5p753PJ4pA05qslyw6A1rf1zTVO-c7V6SIVJIIzCxZ_LKIMMwqdGTs1dCh_OLhE5XZK3YZ4v61m91AW_1Hal1SSOHsNEcuX7zkov1M3RJ3h1rJnGa-s1sDNblKpbOj0F06_E0WjL2M_-uWrPOa-lCZ0sUHbJb9Waia2APObu7EATzwK9XP7zYK0B8bI9zlihMKJzRLKJupkyimGv2FFJpYFfYDG1pMhoXCeGksKZnXoWwNc0_hLdKyjXvoAVwbSKv_NQBieYt6jdyAnFlauokPu0LITqMU7QL02JBzGA67Bhyvgx64nxnhW1XbJdu1Z1XYRD_7zKiY_S10K1DX37hIV23Khili8s_5WfnbMGHYSNgb_RPrA_9ksoc-ds5mwEtF-37E9v1b9lvzq3aKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
🔹
دولت از این واحدهای تولیدی حمایت ۱۰۰ درصدی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/652011" target="_blank">📅 22:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZkGFP-jeW-s5O0Ll1K9SMCLhrGFSJlrgYO4z-P-LspSdz7lh7OXUzCEEDEMvXPRnElHwqlMnkQCWixoPo-8jeumVNIXNCXYB3rHP8Le8hsElzeQlBITL6fX4GpT77hSXHcaBuR4sSO2YdiVSbSRDrVmS_dgry1r-uBUzaoz57ihEY-tWWgdUMTrdMt3jhBoosRCPfZ1APIOz1XAq5HmrZdwSUa8wWik8zKLZHyyyAbiQO34iLY8cUb4Idkfu6jcmmSJFntyKh5D3JzFIDxuo2lzQXB7ojsL9BAz7VU1u1cjD84mYkiKyqN4VgRHfXbIwkmYvZyaiGFyh0opUEvwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین خطاب به پاکستان: به میانجی‌گری ادامه بده!
🔹
وانگ یی، وزیر امور خارجه چین، روز سه‌شنبه از پاکستان خواست تا تلاش‌های میانجیگری را افزایش دهد و در حل صحیح مسائل مربوط به بازگشایی تنگه هرمز مشارکت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/652010" target="_blank">📅 22:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiGeh2bVp99pTEKrNDFTE7Mt0OECulME-kXnk6tT0YhYpRMy8svaecjdah1zb2AT1YJ1N2Arut1O6ymN93Sx_QFIu-wdEobkOKNxkERMc8dk7pDrpK4aRTIwY3kdFiBadf6e0MTzV8NijbOZ0OdZYxCjfqVbiVqJNkewLSJPGJ3BidS35a6HLmib_LC7ds67Hy2SHMb2pTDMSYn4NTiUmh0vWbbvF3YfHroN_0T47sSBETKyefhSF4YAd87SZUN8F3HtfuKpdu3n4Y9xTJcbTQKGp8MiGg-cwqTogaDuIcgKppXjF-BK-A5CuqGCAT0f8yEeXKoKdKDYXr2zl7ttyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌بی‌سی: جنگ ایران، قیمت زعفران را در لندن دوبرابر کرد!
🔹
جنگ در ایران و بسته بودن تنگه هرمز باعث افزایش شدید قیمت جهانی زعفران، یکی از گران‌ترین ادویه‌های جهان، شده است. حدود ۹۰ درصد زعفران جهان در ایران تولید می‌شود؛ به همین دلیل، اختلال در صادرات زعفران، بازارهای بین‌المللی را به‌سرعت تحت تأثیر قرار داده است.
🔹
مغازه‌داران در لندن می‌گویند عرضه زعفران در حال کاهش است و قیمت‌ها به‌شدت افزایش پیدا کرده است. صاحب یک رستوران ایرانی گفت زعفرانی که قبلاً حدود ۱,۲۰۰ پوند برای یک کیلوگرم قیمت داشت، اکنون حدود ۲,۰۰۰ تا ۲,۱۰۰ پوند برای هر کیلوگرم است و تقریباً از زمان آغاز جنگ ایران در اواخر فوریه دو برابر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/652009" target="_blank">📅 22:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa26b96f7d.mp4?token=U45ZNCM6_AEJvAGU8dE_ROh5wbfoKDrOjRju3PuCLbGo7_R2ka1JM4QT5ENDatvH2NrbBdFwQGWnfpu3L5bFApwKMdfvH1LX-Ez30xOYCAnhrbhfDYZexh2VsyOc-bmM0oKuBQKGiI9LIEv05KzZOfJW3VqeO6L-wPoYiDyLnGScHCbJcDOARXNUUqKEBfEhVE9jpAOovTQ8YisMKzysuJNIieTEh1D7xbg7maC6qatUCfaNfkVLWYdGLTjGCHEoMIeMqyEzI4NBPTmqYVNs-408CUoDZwqX4Hj4vZrwfSfwM1nYTeeTFEVqkYN_zFxLEGnhVrJYUS0Zo7jb0C_YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa26b96f7d.mp4?token=U45ZNCM6_AEJvAGU8dE_ROh5wbfoKDrOjRju3PuCLbGo7_R2ka1JM4QT5ENDatvH2NrbBdFwQGWnfpu3L5bFApwKMdfvH1LX-Ez30xOYCAnhrbhfDYZexh2VsyOc-bmM0oKuBQKGiI9LIEv05KzZOfJW3VqeO6L-wPoYiDyLnGScHCbJcDOARXNUUqKEBfEhVE9jpAOovTQ8YisMKzysuJNIieTEh1D7xbg7maC6qatUCfaNfkVLWYdGLTjGCHEoMIeMqyEzI4NBPTmqYVNs-408CUoDZwqX4Hj4vZrwfSfwM1nYTeeTFEVqkYN_zFxLEGnhVrJYUS0Zo7jb0C_YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کار: امیدواریم هرچه زودتر مبلغ کالابرگ افزایش یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/akhbarefori/652008" target="_blank">📅 22:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اکسیوس: حقوق کارگران آمریکایی به خاطر جنگ ایران از تورم عقب ماند
اکسیوس:
🔹
برای اولین بار در سه سال گذشته، حقوق کارگران آمریکایی از تورم عقب مانده است، که یکی از تلفات شوک انرژی جنگ ایران است.
🔹
جنگ به از بین رفتن پشتوانه مالی که مصرف‌کنندگان را در برابر آن محافظت می‌کرد، کمک کرده است.
🔹
کارگران اکنون درآمد واقعی کمتری دارند، تهدیدی برای هزینه‌هایی که اقتصاد را فعال نگه داشته است/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/652007" target="_blank">📅 22:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
حملات ترامپ به ناتو بعد از عدم مشارکت در جنگ علیه ایران ادامه دارد: ناتو من را ناامید کرده است و ما به کمک آن‌ها نیازی نداریم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/652006" target="_blank">📅 22:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc-aHD0lmRYx1Pu6tga3_YSbQHyMhgxltftkPWh_Xn4Sj2hdTkMPgtV08taCE18R7_tZZrmnC9_cxTGOMLnzx7cWq0jeGeZ0qcKLxa2WVnaR42hWqAbKditLckrmqT9eor75QdG314IeTY5F1BSGLL-dYiIljkctoAvKYy40L-hqnZOsdc6MYF5ug-wrf3QaP9tENeCKRh7Hl7CbeCKRe2faAjKlFOimUZqOxWeWW7e9N0VCpYJz6ZfWPyA0P8IK9ukmavMIB1IqDFI_ZSahkIHBJMXwW5VrSRf0W6o72s4SIYjuOB0Ea5KoX0aNVOhX3z3xPj61KKj6n_xBzW1E4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فولاد مبارکه مامور واردات ورق فولادی شد
🔹
وزارت صمت اختیار واردات ورق مورد نیاز بازار داخل به فولاد مبارکه سپرد.
🔹
براساس اطلاع، ارز مورد نیاز برای واردات ورق نیز تامین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/akhbarefori/652005" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b2315c5d.mp4?token=Nes9S5SUJr-JQyONrLDxU6J35eRX1SCh6DjEefQEJdAsFvZYhIvQaXfJhDpp-b5-nDyuYUV-vghsd8yCv5_K7lSF6syUq91pzU_T0U0WXTHWsBEGd-HQXrpf5lje0Fs3_Loqe6cVkcJ35pDDnrXgXnMdRCAZxN4E7T9qEalZU81Uwose_N2qR0hbY0rnQ63TJJAlpcrPArmA0hxDXK8L74cCLLE_EJSxHXZ7V6ytC3IKT7jG7DjDEgn-roPEY9pnKpXZGRYwNNzUPaTYCUHzdKapEWyjmDuVQiFunmbbHhuIsdbJZFyx-Qd_U1qyh16pu25FMVSNdiA_3ZmUYHwZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b2315c5d.mp4?token=Nes9S5SUJr-JQyONrLDxU6J35eRX1SCh6DjEefQEJdAsFvZYhIvQaXfJhDpp-b5-nDyuYUV-vghsd8yCv5_K7lSF6syUq91pzU_T0U0WXTHWsBEGd-HQXrpf5lje0Fs3_Loqe6cVkcJ35pDDnrXgXnMdRCAZxN4E7T9qEalZU81Uwose_N2qR0hbY0rnQ63TJJAlpcrPArmA0hxDXK8L74cCLLE_EJSxHXZ7V6ytC3IKT7jG7DjDEgn-roPEY9pnKpXZGRYwNNzUPaTYCUHzdKapEWyjmDuVQiFunmbbHhuIsdbJZFyx-Qd_U1qyh16pu25FMVSNdiA_3ZmUYHwZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صبر زینبی در خانواده قرآنی با ۷ شهید
🔹
جمعی از قاریان و فعالان قرآنی کشور میهمان بازمانده خانواده شهیدان مقیمی و ساداتی شدند که در حملات ددمنشانه رژیم صهیونیستی هفت شهید را یکجا تقدیم ایران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/akhbarefori/652004" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جلسه 47_مراسم دعای ندبه_سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">@masaf</div>
</div>
<a href="https://t.me/akhbarefori/652003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وهفتم
رائفی‌پور:
🔹
0:10:00 چگونگی مؤمن واقعی در قبال ائمه (ع)
🔹
0:26:15 فرمایش پیامبر در رابطه با تربیت فرزندان با ۳ خصلت اصلی
🔹
0:36:30 ملعون بودن فردی که موارد شرعی را برمبنای شهوت انجام می دهد
🔹
0:38:00 روزه هوش و حافظه را تقویت می کند
🔹
0:44:45 علت اصلی منع از غیبت، نابود شدن مغز است
🔹
0:48:00 حسرت در قیامت برای همه انسان ها
🔹
0:59:00 ضریب گرفتن اعمال در محاسبات قیامت
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/652003" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شهروند آلمانی: آلمان را وارد جنگ نکنید
یک شهروند آلمانی در مصاحبه‌ای با انتقاد از سیاست‌های برلین گفت:
🔹
ما خودمان مشکل داریم؛ دولت باید اول به فکر مردم آلمان باشد، نه دخالت در جنگ‌های دیگر
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/652002" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhLKACz6_nBddFJ42RMGUjIYv53ZxHv54PaDx4WaJC_p4-ue1TpmGL3yRXLdkgoDHdILEhEcxHis_3gNA8FekamxUY8QTlIjZWMo4PP0gThEJ46GHq9RmtOO5M-nCx-TLPoWf1GJKDxMkyaDJ0SOtLHhdAz4tOEbMOP-fpybksAHVc075L29cygutV5BwLXlaX682LF5_ZyBfPUaFs4UIvOAVIfTn0tg6ws-_xgfY2uSCWqlJJw9kFHxhxWLrCvB2ZMt4lLSdAaGdZTTda_Oj6sWODv03MBWZVRan9fb_k2Y5qn5dNhKI5kMQfrGwEdnaqoAHVCA0dwMtilns5Je4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: بسته بودن تنگه هرمز میلیون‌ها دلار هزینه روی دست آمریکا گذاشته است
بلومبرگ:
🔹
نیروی دریایی آمریکا با افزایش هزینه‌های بسته شدن تنگه هرمز مواجه است.
🔹
تا زمانی که تنگه هرمز همچنان ناآرام باشد، نیروی دریایی ایالات متحده هر بار که ناوشکنی را از طریق این آبراه اعزام می‌کند، با میلیون‌ها دلار هزینه اضافی مواجه می‌شود.
🔹
بعید است که چنین گذرگاه‌هایی به خودی خود آن را بازگشایی کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/652001" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12960aa4f3.mp4?token=gJOgEGadYwa1p1B29lR4zpiqa11eBvnPkhgSVZjQDkyosapzpONPUrd95i-7vDkgEd5VELt45_En057VQyDP50RyF5GGwcutVs9fgTwiDHYulTLtYgWJeCWTLAIcZlpRxB0YfAgFG6o6_j2T4k28heU7p5U2_u_L2_9eIibb1pgHZc3bfKUdSfodltaolpmL8PJhFb4W9w_1ep8hXK7I_7QprIHYTNLp-mFFNjEfXzbjRDDVOXPCEoQiAlDNukowa3Ovz3i65A4pSuWDk1n8C_n3ZI3BXnBcnsHgJJ78p2foZtVt_iSSzysgr_BpGAbZY8USHo6Qdo96dpJnwU1ob7c76oO51LjjLBmj0bTJR6QK7AP-7hSS3_L_LwApyqPMUwPeQOgG705d1b0Nr0se0tUTFJz006ncDm418ThdJLeeZYG8VPGDCdo9JFgDOcXr0xczW2KMY1qNqB4P9xmjNnUtk0oTr5K1AEKk74HrOJIRLkdtDixlp1hPKGLmR0lI7vIgi6HanSifnAmTqDRSy8NInHNW7n_kkNcir8KoBMydhvdmri4x9GPuSXTNvpS199ojnSLxBehst1808LC7VIzb7KBfa1nZUB9U1rFB053JrI6UwTz6pelX4UdjQuchEQgHaz8sL1H4MS2w0-ZURH3vGNzG6Gv8QZBHOZQV4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12960aa4f3.mp4?token=gJOgEGadYwa1p1B29lR4zpiqa11eBvnPkhgSVZjQDkyosapzpONPUrd95i-7vDkgEd5VELt45_En057VQyDP50RyF5GGwcutVs9fgTwiDHYulTLtYgWJeCWTLAIcZlpRxB0YfAgFG6o6_j2T4k28heU7p5U2_u_L2_9eIibb1pgHZc3bfKUdSfodltaolpmL8PJhFb4W9w_1ep8hXK7I_7QprIHYTNLp-mFFNjEfXzbjRDDVOXPCEoQiAlDNukowa3Ovz3i65A4pSuWDk1n8C_n3ZI3BXnBcnsHgJJ78p2foZtVt_iSSzysgr_BpGAbZY8USHo6Qdo96dpJnwU1ob7c76oO51LjjLBmj0bTJR6QK7AP-7hSS3_L_LwApyqPMUwPeQOgG705d1b0Nr0se0tUTFJz006ncDm418ThdJLeeZYG8VPGDCdo9JFgDOcXr0xczW2KMY1qNqB4P9xmjNnUtk0oTr5K1AEKk74HrOJIRLkdtDixlp1hPKGLmR0lI7vIgi6HanSifnAmTqDRSy8NInHNW7n_kkNcir8KoBMydhvdmri4x9GPuSXTNvpS199ojnSLxBehst1808LC7VIzb7KBfa1nZUB9U1rFB053JrI6UwTz6pelX4UdjQuchEQgHaz8sL1H4MS2w0-ZURH3vGNzG6Gv8QZBHOZQV4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزادی بیان به سبک پلیس آلمان
دستگیری فقط به علت پوشیدن تی شرت فلسطین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/akhbarefori/652000" target="_blank">📅 21:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf4175079.mp4?token=vytzHakEgF5VppyLPqCeAZBBgeHQwA5UGHUo2G7R9xhezKHUXrUQ5Uh_ycW3BJzw7mgXKOhDabwwSt4XdfNv30Rtk2Bb_ZHbRJ7WJ81T0saK3txmpA2-xUAz479uegEdHjhMrfD538iPF4EknOJXtPWZvv4zseqoum40kReDTasVYSC9kJA9ycHNuFQ0-iV-tfqTycuPyhTN_id1ff8YM7w0SH3h_pADOBzXaNWTw5N6K6H9IT41_r9QBOCvp-2hAmMRNht38alTNPSX6QR_sYlDoFU5JgJYaQN6tFzOpiLAqGzYhO4kzK6nUMgsTqlJN_6Dbofp9LCrKK37H-G5QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf4175079.mp4?token=vytzHakEgF5VppyLPqCeAZBBgeHQwA5UGHUo2G7R9xhezKHUXrUQ5Uh_ycW3BJzw7mgXKOhDabwwSt4XdfNv30Rtk2Bb_ZHbRJ7WJ81T0saK3txmpA2-xUAz479uegEdHjhMrfD538iPF4EknOJXtPWZvv4zseqoum40kReDTasVYSC9kJA9ycHNuFQ0-iV-tfqTycuPyhTN_id1ff8YM7w0SH3h_pADOBzXaNWTw5N6K6H9IT41_r9QBOCvp-2hAmMRNht38alTNPSX6QR_sYlDoFU5JgJYaQN6tFzOpiLAqGzYhO4kzK6nUMgsTqlJN_6Dbofp9LCrKK37H-G5QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: من نه به وضعیت مالی آمریکایی‌ها فکر می‌کنم و‌ نه هیچ‌کس دیگر. من فقط به یک چیز فکر می‌کنم؛ نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/akhbarefori/651999" target="_blank">📅 21:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
طغیانی، نایب‌رئیس کمیسیون اقتصادی: در حال حاضر حدود ۱۸ درصد از خریدهای خوراکی از طریق کالابرگ انجام می‌شود
🔹
نزدیک به ۲۷۰ همت از طریق خریدها در مسیر کالابرگ جبران شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/651998" target="_blank">📅 21:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ایران یا کار درست را انجام می‌دهد یا ماموریت را به پایان می‌رسانیم و ما کنترل کامل بر اوضاع در ایران داریم
🔹
اگر ایران به سلاح هسته‌ای دست یابد تمام جهان در خطر خواهد بود.
🔹
همین الان می‌توانم (از جنگ با ایران) عقب‌نشینی کنم اما این را نمی‌خواهم و خواستار آن هستم که کار را تمام کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/akhbarefori/651997" target="_blank">📅 21:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz9ARr7axu6cETVBX9qKWUmkiA8gdWG2c3Me0ngHhrFtLeUpRaJdQYLoaxnFTPUyORhTkRNr1AaI6O-TOwZXhDB-qGFuoVbNAoN2AUMCHPflh70hxcsJh-XIGrl84RhAMb9JoSqr67rigCSPLmSNnw1DCOFsfEVCyxYvpxD_N1lGr3NROW8zhOWC_pgSQHvky-piuPwhzM4zNCI0y7Fi91L2QBE5BEBC5YHgp9tot0mp6lXdcbCp1XmsW6F58MVrLtfpS6aCmTbStuX00M6ylU9nfxygGUV2w8B_tNhDszRoz6EutDlKLNV6qF6GptTZ1Fa3Qo5CB3xyAAR5FVxT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت واشینگتن پست از فراگیر شدن حمایت از ترور ترامپ بین آمریکایی‌ها: «یک نفر باید این کار را انجام دهد»
🔹
افراد مستقیماً نمی‌گویند ترامپ باید کشته شود، اما برای آن یک عبارت غیرمستقیم ساخته‌اند. عبارت «یک نفر باید این کار را انجام دهد» و مشتقات آن، به میم‌های اینترنتی به‌شدت محبوبی تبدیل شده‌اند.
🔹
طبق داده‌های مؤسسات پایش شبکه‌های اجتماعی، استفاده از عبارات کنایه‌آمیز مرتبط با «حذف فیزیکی» ترامپ در سکوهایی مثل ایکس و تیک‌تاک نسبت به سه ماهه اول سال جاری، ۳۰۰ درصد رشد داشته است.
🔹
عبارت «یک نفر باید این کار را انجام دهد» به یک ترجیع‌بند در زیر پست‌های خبری مربوط به بحران ایران، قیمت بنزین و تنش‌های خاورمیانه تبدیل شده است. کاربران بدون نام بردن مستقیم از ترور، از این عبارت برای القای ضرورت حذف ترامپ استفاده می‌کنند.
🔹
بسیاری از کاربران، این شوخی‌ها را با استناد به بحران‌های جهانی مانند خطر جنگ هسته‌ای با ایران یا فروپاشی اقتصادی توجیه می‌کنند و آن را یک «آرزوی نجات‌بخش» جلوه می‌دهند.
🔹
این نوع میم‌‌ها، فضا را برای افرادی که ممکن است شوخی را جدی بگیرند، آماده می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/651996" target="_blank">📅 21:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnW9-wZwkCv6moZq_EXNHaaWf6S5q_CXiSbzyx2Xa0xrAEplkHki_zEjiThaibcXMz86sWqe10AE7MNJiaQi-U6BUoKnwqbpY7b-Jf9h0RBESAWvi5ci2NlTvfaerq1v17wr13vTJpeVL3pKsGPc-bNU_XUazAdzQ6mIKOcW4O2COWNcWmLJUzkS3Pc3fdWDl_wp__Jh6NHEsKlmB6rvnGeu13kqjxaKhsWFWp0qRzA7rTJmbp6fFi1IycGcusKTbV7wcpaPMdxbVC4YBibZEMPTCqZ-GnMYmvd6ZNNaJaY0Fluzg30HFNLRiBb4Ab4AwYkQhnxVEucKk6gdDkTO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید علی موسوی فعال رسانه:آقای وزیر بالاخره شما مقصرید یا اپراتورها؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/651995" target="_blank">📅 21:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هرکسی که می‌خواهد به دیوانه‌ها در ایران اجازه دهد تا به سلاح هسته‌ای دست یابند احمق است
🔹
پیام من ساده بوده و این است که ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز به آن دست پیدا نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/651994" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ترامپ: از کسی در جنگ با ایران کمک نمی‌خواهم
🔹
هرگز توافقی را با ایران نخواهیم داشت مگر آنکه توافق خوبی باشد.
🔹
مذاکره طولانی با رئیس‌جمهور چین درباره جنگ علیه ایران خواهم داشت.
🔹
هیچ کمکی از کسی درباره ایران نمی‌خواهم و ما پیروز می‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/651993" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفویض اختیار به استانداران استان‌های مرزی جهت واردات اقلام اساسی
هادی تیزهوش تابان، رییس اتاق بازرگانی مشترک ایران و روسیه در
#گفتگو
با خبرفوری:
🔹
با توجه به تحولات اخیر، تغییر رویکرد از بنادر جنوبی به سمت بنادر شمالی و دیگر مناطق مرزی اجتناب‌ناپذیر شده است. به همین منظور اختیار واردات برخی اقلام اساسی به استانداران استان‌های مرزی واگذار شده است.
🔹
پیش‌بینی می‌شود واردات کالاهایی مانند غلات، روغن، حبوبات، دام زنده، کود، نهاده‌های تولید در حوزه فولاد و پتروشیمی و حتی دارو از مسیر کریدورهای تجاری شمال کشور، به‌ویژه کریدور شمال–جنوب، افزایش یابد. همچنین با توجه به ظرفیت کشورهای چین و روسیه، امکان تأمین این اقلام از طریق بنادر شمالی فراهم است.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/651992" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROZm5KGidT0UjitskaOvOC-Ue_AHqdFLQrj-eMO2-jPFVqMHeaYpKpDXp8kiLgEPFFj3uejOYdU4VxgHpiYdVeGZcmggeIqOXBOD_fv3NkT9qX4Y9eqNCUyxtZe5Na-HyctQjHNp9H5wSgGl-aBOGYRKkuLy3wsmEs7UUxNT3dIXjr2vCjLGqkodCnqbt2zOm4w5vNQOFsavZl1jEsVS83o5zrzodzNBZLWiYoTW68B0rma85Ph8fiBNuN-5NwEoSCZHlIf20PidKcPKlVQAjyHIZqX6MyHbpn6pBzOkISVs0TiGSf1tehU0SgiozdQJ3XOHznXr_8kWOioiZmrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلومبرگ: امارات با هماهنگی اسرائیل دوبار به ایران حمله کرده است
🔹
بلومبرگ شامگاه سه‌شنبه گزارش داد که امارات دوبار با هماهنگی رژیم اسرائیل به ایران حمله کرده که یکی از این حملات پیش از آتش‌بس و دیگری پس از آتش‌بس روی داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/651991" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا و پیت هگست، وزیر دفاع آمریکا، هر دو از اظهارنظر درباره گزارش‌هایی که ادعا می‌کنند تنها ۳۰ درصد از توان موشکی ایران نابود شده است، خودداری کردند
🔹
هگست گفت: من اطلاعات درز یافته‌ای را که ممکن است درست یا نادرست باشد، تایید نمی‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/651990" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQlH-5E3JPw7feUvVzOvFfeDJSPIlULiHSXl6AB43C0VSm7tVyeNfzwcwZw0WdgWgPXNbBjh72XtuNZpG_najdy3-plFiq3yRI2HRRiSfMbcz35deNXpkOAUXA2CrnlYzL3ofoV4_uIj6P-IkItq6ljNg23u6v4kpBXOUb6TlQst0OsmL_DmniUcvBBtghd1jOXpzwaiJIB6wV90jO3eSsvWb5J28D8Jp6088HpiyVhPT9uax2qZUX42kCGknTfQFC7PB_4pmDlNwPhkwHywdVRHj3stF3pxt6Ujjdfkv505nlE7NAEsqDE2BUvyK2-ZEklv59_KxXpgsMHv9DD7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جدید مجلس: میانگین پرداختی کل دوره شغلی مبنای حقوق بازنشستگی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/651989" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
لارنس ویگر سون، افسر بازنشسته ارتش آمریکا: در حال ورود به مرحله‌ای از این درگیری هستیم که دیگر راهی برای خروج‌از آن بدون تحمل تلفات انبوه وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/651988" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64A1YNkAIT2spwUHIUgyvQl4_S9vnzcxP4u7dapl4qiO7cIbWlH4vp8ZplMUInF_6rGi44MPejhTYh17IrJ4GB2a_RPgaCDydOaVQoTGXyu1emmxcAnqIGuuUH-nFFeezzEs-tI2gbQAZEXzUaD6dx1fDOU6ar8kqpotCJ4y3KFOYOSPfzv2QZ13SK846iyS1P50EyCwxUHojJZ4f5RgNoA2FqSb4lekyyVSB9at9vBbwzoPnGm4487N37GGi5zHnxkk66yzXtta6AttV0HYo7T0JPLf2pS9z7dalN-FhCHQ5CbM5dPm3fj7tOwHyc3xZd6KdSV1UtkATOZwwSJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: تاکید ایران بر اصولی روشن است: «توقف دائمی جنگ و عدم تکرار آن»، «جبران خسارات»، «رفع محاصره»، «رفع تحریم‌های غیرقانونی» و «احترام به حقوق ایران»
🔹
معاون وزیر امور خارجه: نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد. چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/651987" target="_blank">📅 21:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225fbab644.mp4?token=M0iOg7TzXr5Kbi91eLLDGxyyaD-CULLiV7pwr6NC3ZrkLVGMxVSKnilN2ayq6vobNTAU2Otjs2NOXIMjWZTDVaVai6v6lsh4M_dIm22mpQyhHgRy6ad10gMAZhZeA4x0YhfOlA4GYplLrgESJPcof60nOVn6cBRwDWBYRSZNMXAv6yue4WaCZrrBaYow2CXiS4ypm2S0yHsUXKyy10LJWxTmNi_SfgfE5aa6u779G_Kfm56TfDNwz-U7gtu1XrEYW0MWpg8oVbKQHU-S83g4KZF4LYkJzzy_Q6iJ-hNKtF2Zlcanxyztu9GLmKSRnDCap8N1HKTjXWQtOr20zNhvZx32hT17gJ2cQuB5wpfHmOAffAIHUlZV672AQhsSxZbzyRGo-mv2UvvhKHlTjSgjHxiMOFa__VaT9EApGld8byL88uy8hFtHxR8tcXTThUzSqPyxhVbT0HH6C8_1wAyA21fTVbsxRpF0Qx6jtUp4OsW_LdtB1jpPR8hywd3T-2f8sPyJSwONWiBPBVgcfKlgpyxe4A82ljqL5C2ofDnAbK7ENcsPzJ1dCvbW29gd0SzfT0aZBWWIFJC11eYd-RRFM7vtttRRwrWU2htETjzuvFbzFG86-m3guELDuG_v7KM6S6GaWMm0-SJxpq_iuxltCy5p-TqCYmj0eH70Sf0a-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225fbab644.mp4?token=M0iOg7TzXr5Kbi91eLLDGxyyaD-CULLiV7pwr6NC3ZrkLVGMxVSKnilN2ayq6vobNTAU2Otjs2NOXIMjWZTDVaVai6v6lsh4M_dIm22mpQyhHgRy6ad10gMAZhZeA4x0YhfOlA4GYplLrgESJPcof60nOVn6cBRwDWBYRSZNMXAv6yue4WaCZrrBaYow2CXiS4ypm2S0yHsUXKyy10LJWxTmNi_SfgfE5aa6u779G_Kfm56TfDNwz-U7gtu1XrEYW0MWpg8oVbKQHU-S83g4KZF4LYkJzzy_Q6iJ-hNKtF2Zlcanxyztu9GLmKSRnDCap8N1HKTjXWQtOr20zNhvZx32hT17gJ2cQuB5wpfHmOAffAIHUlZV672AQhsSxZbzyRGo-mv2UvvhKHlTjSgjHxiMOFa__VaT9EApGld8byL88uy8hFtHxR8tcXTThUzSqPyxhVbT0HH6C8_1wAyA21fTVbsxRpF0Qx6jtUp4OsW_LdtB1jpPR8hywd3T-2f8sPyJSwONWiBPBVgcfKlgpyxe4A82ljqL5C2ofDnAbK7ENcsPzJ1dCvbW29gd0SzfT0aZBWWIFJC11eYd-RRFM7vtttRRwrWU2htETjzuvFbzFG86-m3guELDuG_v7KM6S6GaWMm0-SJxpq_iuxltCy5p-TqCYmj0eH70Sf0a-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید جالب شهید حاج محمد نظری به سربازان آمریکایی!
🔹
خاطره یکی از نیروهای نظامی از دستگیری نیروی دریایی متجاوز آمریکایی در خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/akhbarefori/651986" target="_blank">📅 20:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
انگلیس از حضور خود در تنگه هرمز خبر داد
🔹
دولت بریتانیا اعلام کرد که با پهپاد جنگنده و ناو برای تامین امنیت تنگه هرمز مشارکت خواهد کرد.
🔹
لندن خاطر نشان کرد با تجهیزات خودکار برای شناسایی مین و جنگنده های تایفون و ناو جنگی در تنگه هرمز حضور خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/651985" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jevQdKXm2i8SHETHh-kc4KUGIZbLb-joJtLivNfmwdqQUONDX938RsY8UgznXr23DcZnYefkPWnjEa67C2_Bq-wR2fMfjOHmUrnbOv1-R8Jcm0derhXYbymJQwssybKWfdq-Rs-USFBJxKELW_Diib_86VO-UQKjtuYbx1Hfiaey2_K-QU9MCwn69yEarzE_SOUrgIkJs7VXLAaizWwFIVKR5d37moTYfCXVxoko7TwlKS1aD04jpjqzVOMaprQCz7GdRl4RNU4TLEyF6WxVmSI9JQv0iGmpN3r8Gtka7XYtNGktnZ6gRRGq5OdcAHGgYEsE9hB6bbA_qzRFvCC-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمک نظامی اسرائیل به امارات در جنگ ایران علنی شد
سایت رادیو ملی آمریکا:
🔹
اسرائیل در جریان جنگ ایران، برای کمک به دفاع از امارات، سامانه‌های ضدموشکی گنبد آهنین و نیروهای عملیاتی به این کشور اعزام کرده است.
🔹
هاکبی با اشاره به روابط دفاعی رو‌به‌ گسترش اسرائیل و امارات: «اسرائیل باتری‌های گنبد آهنین و پرسنلی برای راه‌اندازی آن‌ها به امارات فرستاده است.»
🔹
همچنین از امارات به‌عنوان نخستین عضو پیمان ابراهیم یاد کرد و این همکاری را از نتایج این توافق دانست. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/651984" target="_blank">📅 20:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d58e4bba9.mp4?token=sJXglPxuiChWf8gZxQGLMmhrkJGoZP7Znj5NuKFUI1GddcixNUj56uN3waDpZ7dP3xOXK4OnPoYUSzdTJoy8YAIoX1Wpne8sQNgWvJn9t2dgI3Fsjp75erIfpgZnYTf6KcCjBIDIm-siuyqce75ZsmDkRZDqoKLHdxTjaBKRahSgDQzbdo6FodhFWrhbg-a-8xBYWPEu_-6ZSRSmQATk0XjNtJ-tiWH4LRah6JTAprMnUSKOdOnBAC2WZX2TRAlHAuxrnff4Fm_ZIDaBIZP4j4uRZnBY_kfObA6ZDMBjG72VaObXp1GCl106ABLun4VyxaOMKt6PknI3pe1-p_NICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d58e4bba9.mp4?token=sJXglPxuiChWf8gZxQGLMmhrkJGoZP7Znj5NuKFUI1GddcixNUj56uN3waDpZ7dP3xOXK4OnPoYUSzdTJoy8YAIoX1Wpne8sQNgWvJn9t2dgI3Fsjp75erIfpgZnYTf6KcCjBIDIm-siuyqce75ZsmDkRZDqoKLHdxTjaBKRahSgDQzbdo6FodhFWrhbg-a-8xBYWPEu_-6ZSRSmQATk0XjNtJ-tiWH4LRah6JTAprMnUSKOdOnBAC2WZX2TRAlHAuxrnff4Fm_ZIDaBIZP4j4uRZnBY_kfObA6ZDMBjG72VaObXp1GCl106ABLun4VyxaOMKt6PknI3pe1-p_NICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس کونز، سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما در جنگ با ایران موفقیت‌های «تاکتیکی» دست یافته‌اید اما در آستانهٔ یک شکست «استراتژیک» هستید، چون ما اکنون درحال مذاکره هستیم تا فقط [تنگه باز شود]
🔹
وزیر جنگ آمریکا: این حرف خیلی احمقانه است!
🔹
کریس کونز: شما دارید به من حمله می‌کنید، من دشمن شما نیستم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/akhbarefori/651982" target="_blank">📅 20:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664ca9f2de.mp4?token=WbV9ff0OWunkuJ5f8Pc7JUQeuTRJs8-u-vzPtdbutOh_oXsPKAgoSbTfSiLL1W6ebq7F1zl_BiuNp8DJqDhxSFLw578ejoyaCR294BEnBrD3J6egbqJylt1BdcQwJJVVY4fE7-BsSDy8CWNBEbUa2bxHO0scg7Ifg3PgJdZBvdguh0Ayf0-T0r46HiTA6Z8g61_4Uuf1EJ3LJE8FvNKmGaMO8h2seqw9N59X-k9LJL2l1oIds7pf8xb_d82KIQdSlIqlGMpqbZkHuzbeafPQT637u7-11_CgX9xrRIAHml5fuy70EkCNnUu0gKUd_Na8wGWb1RhHODiv9iVF7GLJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664ca9f2de.mp4?token=WbV9ff0OWunkuJ5f8Pc7JUQeuTRJs8-u-vzPtdbutOh_oXsPKAgoSbTfSiLL1W6ebq7F1zl_BiuNp8DJqDhxSFLw578ejoyaCR294BEnBrD3J6egbqJylt1BdcQwJJVVY4fE7-BsSDy8CWNBEbUa2bxHO0scg7Ifg3PgJdZBvdguh0Ayf0-T0r46HiTA6Z8g61_4Uuf1EJ3LJE8FvNKmGaMO8h2seqw9N59X-k9LJL2l1oIds7pf8xb_d82KIQdSlIqlGMpqbZkHuzbeafPQT637u7-11_CgX9xrRIAHml5fuy70EkCNnUu0gKUd_Na8wGWb1RhHODiv9iVF7GLJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: خطاب به وزیر جنگ آمریکا: شما ادعا کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای تردد تجاری همچنان از دسترس ما خارج است؛ و دلیل عمده‌اش این است که ایران ذخیره قابل‌توجهی از پهپادهای ارزان و مرگبار «شاهد» را حفظ کرده و رقبای ما نیز در حال کمک به آن‌ها برای بازسازی این ذخایر هستند. آقای وزیر، برنامه شما برای بازگشایی تنگه هرمز چیست؟
🔹
وزیر جنگ آمریکا: بخش عمده‌ای از سوال شما بسیار غیرمنصفانه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/651981" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شکست «عملیات پروژه آزادی»
🔹
باز هم شکست خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/651980" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESIboz7DVYbUxT45ZKfkd6nyvaGRxt2Wif_2OI5rL-qDzqU4uRmBXEGkPallarUPFqWQKPYQd2mkAM6eKU2pugJGmTgnyWKhrKZ5EVJ-Xh3Fj9bSfD6VFL6zFvkXxN_c6mMmZ6kteejw_jHRCtZ8ct7wpXJaAyEOpWri_Ux_uVQqGUtZnO2XDd7QUjuymTl-6zv_Ren0cRriIbWMRl8PPHG0Y5G6alRBU5k5Jez1CfGzvaWtX1h5cZJAivlYgfIYYPu82ajoHSRWsbXulNCDfxExcs-RTdOXiu-EjD9wbmdQM2liQmt5qjuPuuwFOeL6MnxDaRPUWtRoPRuNcj1Oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشینگتن پست: جنگ ایران رؤیای کشورهای خلیج [فارس] برای اقتصاد بدون نفت را با تهدید مواجه کرده است
🔹
این درگیری نه تنها درآمد نفتی کشورهای خلیج [فارس] را کاهش داده، بلکه تلاش‌های آنها برای گسترش اقتصاد پسانفتی را نیز تضعیف می‌کند.
🔹
جنگ ایران به آزمونی استرس‌زا برای آینده‌ اقتصادی کشورهای خلیج [فارس] فارس تبدیل شده؛ کشورهایی که برای خود شهرتی به‌عنوان مراکز مالی جهانی و قطب‌های گردشگری و فناوری ساخته بودند.
🔹
این احتمال که ایران بتواند تنگه هرمز را تا هر زمان که بخواهد مسدود نگه دارد، اعتماد سرمایه‌گذاران خارجی را متزلزل کرده و اعتبار کشورهای حاشیه خلیج [فارس] را به‌عنوان پناهگاهی امن برای کسب‌وکار از بین می‌برد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/akhbarefori/651979" target="_blank">📅 20:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d264a2ad4b.mp4?token=jtTE_yQMukKxT6IEeAx9UtAmxHxSv7eRklIS9JfUJyNL_u0WNvDfPVYeTJSRLWRuisImd2IHkb2zkLCUR_B-Ae0b0yo60PcVX8nttpWnGVuuHyjTILdniChPx3N1QxyM9X_m1ZMnDwLkChQHuE00RayY5J6alOp88OJo-NH5SsDYM4ZfON4oyS2nthoH-H2Am6yI03KskKogZH7hLU4oV6cpX-dBXqlGMubGVV-CPZhWUguaedgdGaXNWL6nnyQL9yIeIlsJA9Gq_22xsU6ShFsnVRwoUYB2hDi8hhgQFqMTkaz0ZodMj1_owCjB9X-TLrPzByCjfVOhddcL_d-20g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d264a2ad4b.mp4?token=jtTE_yQMukKxT6IEeAx9UtAmxHxSv7eRklIS9JfUJyNL_u0WNvDfPVYeTJSRLWRuisImd2IHkb2zkLCUR_B-Ae0b0yo60PcVX8nttpWnGVuuHyjTILdniChPx3N1QxyM9X_m1ZMnDwLkChQHuE00RayY5J6alOp88OJo-NH5SsDYM4ZfON4oyS2nthoH-H2Am6yI03KskKogZH7hLU4oV6cpX-dBXqlGMubGVV-CPZhWUguaedgdGaXNWL6nnyQL9yIeIlsJA9Gq_22xsU6ShFsnVRwoUYB2hDi8hhgQFqMTkaz0ZodMj1_owCjB9X-TLrPzByCjfVOhddcL_d-20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید محمد ناظری، بنیانگذار نیروی ویژه‌ دریایی سپاه بود، یک تیپ‌خیلی ویژه و جوان که مخصوص متوقف کردن کشتی‌های متجاوز در خلیج فارس هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/akhbarefori/651978" target="_blank">📅 20:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58948247ba.mp4?token=fGtZC_mMZhpvJF2SOMR4JCVF3dEvxSL4YUFrdkpCsT9AXZEfFUZkD03jfmFhu8ri_qWvd-uiP_ODrMfSHx_ZNAlx4wIUO0wYyC5QhO7ppSUpmpzDtL4HgbFfnyCAOztKkdfUrIgH7Sc3dxSWQNV6m2OUbEZgh0WWMCbH_4-S-8qNJL1ZZ1C-6Oi_r3TftgsgM7qajbbYB5Npsih3RIcUFClHySp_OehCJ8POK8IXLnGI7bx31u5yrSxLgZiWdPcsytTUAy7WDmZ0XHzqxCyI_KZ9XxyPx09fqDyZhhgKPJv9_mcpXNA0R0u2WZ3ymKrDk4JOn4Yg5WOaPfGQrG0ALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58948247ba.mp4?token=fGtZC_mMZhpvJF2SOMR4JCVF3dEvxSL4YUFrdkpCsT9AXZEfFUZkD03jfmFhu8ri_qWvd-uiP_ODrMfSHx_ZNAlx4wIUO0wYyC5QhO7ppSUpmpzDtL4HgbFfnyCAOztKkdfUrIgH7Sc3dxSWQNV6m2OUbEZgh0WWMCbH_4-S-8qNJL1ZZ1C-6Oi_r3TftgsgM7qajbbYB5Npsih3RIcUFClHySp_OehCJ8POK8IXLnGI7bx31u5yrSxLgZiWdPcsytTUAy7WDmZ0XHzqxCyI_KZ9XxyPx09fqDyZhhgKPJv9_mcpXNA0R0u2WZ3ymKrDk4JOn4Yg5WOaPfGQrG0ALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلجی، رئیس شورای اطلاع‌رسانی دولت سیزدهم: شهید امیرعبداللهیان یک‌تنه جریانی برای حمایت از غزه در جهان به وجود آورد که شاید دلیل شهادت ایشان هم همین باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/akhbarefori/651977" target="_blank">📅 20:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
روایت علی هاشم خبرنگار الجزیره از پنج شرط تیم مذاکره‌کننده ایرانی
🔹
به گفته یک منبع مطلع از روند مذاکرات میان ایران و ایالات متحده، دستورالعمل‌های سطح بالایی که به تیم مذاکره‌کننده ایرانی ابلاغ شده، شامل پنج شرط است که باید پیش از ورود به گفت‌وگو درباره پرونده هسته‌ای رعایت شود:
🔹
۱. پایان جنگ در همه جبهه‌ها
🔹
۲. لغو تمامی تحریم‌ها
🔹
۳. آزادسازی دارایی‌های مسدودشده
🔹
۴. جبران خسارت‌ها و زیان‌های ناشی از جنگ
🔹
۵. به رسمیت شناخته شدن حق حاکمیت ایران بر تنگه هرمز/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/akhbarefori/651976" target="_blank">📅 20:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d18d73e58.mp4?token=s8bwT5-0By2C8Y6NMmVNkLfXUJGwPUBgWW6W2eb3AP-1t3-ekeZOMTMzdkB65EpW1_wsoKpNLKqfZotAL35WZMZuZbVfDyMDJ0VcwF7OkCe2vf6myydBGGInp3-3UCvQd3tpLcaKeDK69ygQXG495KrlGrWc_fKMnBf9CiUHLiqZHv1GSXK_-m6lisZfQ0araakfLkYvASIbLMyFofqqGtE2RC4ihQwXteRSgVSWX4R-hyhs4zpvxoLihS_4mZjm2iqs5T584jF6Dmugy2xg8gcFr-JJRueiJIAcZgivAGjl3KPjelcKmMXUKvwX2t5f1bdIBatZeX062VmrT8RdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d18d73e58.mp4?token=s8bwT5-0By2C8Y6NMmVNkLfXUJGwPUBgWW6W2eb3AP-1t3-ekeZOMTMzdkB65EpW1_wsoKpNLKqfZotAL35WZMZuZbVfDyMDJ0VcwF7OkCe2vf6myydBGGInp3-3UCvQd3tpLcaKeDK69ygQXG495KrlGrWc_fKMnBf9CiUHLiqZHv1GSXK_-m6lisZfQ0araakfLkYvASIbLMyFofqqGtE2RC4ihQwXteRSgVSWX4R-hyhs4zpvxoLihS_4mZjm2iqs5T584jF6Dmugy2xg8gcFr-JJRueiJIAcZgivAGjl3KPjelcKmMXUKvwX2t5f1bdIBatZeX062VmrT8RdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنتاگون: خسارات وارد شده به پایگاه‌های آمریکایی را برآورد نکرده‌ایم
🔹
پتی موری، سناتور آمریکایی: طبق گزارش‌ها ایران به حداقل ۲۲۸ ساختمان یا تجهیزات در پایگاه‌های نظامی آمریکا ضربه زده است. آیا می‌توانید بگویید هزینۀ خسارات وارد شده چقدر است؟
🔹
وزیر جنگ آمریکا: خب، فکر می‌کنم قبلا به وضوح توضیح داده‌شده که ما چه مواردی را نمی‌توانیم بگوییم.
🔹
پتی موری: هیچ برآورد هزینه‌ای ندارید؟
🔹
نماینده پنتاگون: در ر مورد آرایش نظامی آینده در خاورمیانه، ما هنوز نمی‌دانیم که وضعیت چگونه خواهد بود. در مورد ساخت‌وسازهای نظامی، فعلاً برآورد هزینه‌ای نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/akhbarefori/651975" target="_blank">📅 20:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تخمین وزارت انرژی آمریکا درباره زمان بسته بودن تنگه هرمز
🔹
وزارت انرژی آمریکا گفته تصور می‌کند که تنگه هرمز تا اواخر ماه مه میلادی بسته خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/651974" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH_nwoLqDAmvxRoZvQAoJ_M0TQRVP09iL5H-4Jobq_ojNJw9o3c0ckLIepAonzC0BDAqVImg3z4nc6FjEnYOkS4Pp0T26QsLbcqkrSwVLEw6SaUXq2D0O4-1AJGV51zYHgDIVLX3bqltYCMXbr07R1Ue_5GDJOXun56-Pnk1y_zUbKGWEHqgx8peAJNfhllUwaDuPEht1du3ihTcHPsMtYv4sRs9X4e5GAUmRL_jdK6yJxrYPQA0wbFCOSbUPsp-eUNV6bABg8ad0qbVqQwudjQGAru_pKgn-7L9rwrZYdllzPNy8pL-Poj3cXMoMjalDDZYUylJDHq3DgXIYbb-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افرادی که وسط جنگ هم دست از افزایش قیمت خودرو برنمی‌دارند!
🔹
طاهری، عضو کمیسیون صنایع مجلس: ایران‌خودرو با مدیریت جدید نباید هر اقدامی را بدون توجه به سیاست‌های کلان انجام دهد.
🔹
پیش از این بارها هشدار داده بودیم که واگذاری‌ شرکت‌های خودروسازی از نظر ما با تعارض منافع همراه خواهد بود.
🔹
انتظار می‌رود قوه قضائیه به‌صورت جدی به این موضوع ورود کند زیرا تصمیمات مدیریتی در حوزه خودرو مستقیماً بر زندگی مردم اثر می‌گذارد.
🔹
الان کشور گرفتار افرادی است که وسط جنگ خودرو را گران می‌کنند.
🔹
حتی در دوره‌ای که مدیریت خودروسازان دولتی بود، اگرچه مردم از وضعیت خودرو رضایت کامل نداشتند، اما سیاست‌های کلان حاکمیت در حوزه قیمت‌گذاری رعایت می‌شد و کم‌تر شاهد تصمیماتی بودیم که در شرایط حساس کشور موجب افزایش قیمت‌ها شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/akhbarefori/651973" target="_blank">📅 19:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsYk0BieLVPHMIDxDr2XIDa9PhWqtjj9q1ArsZuL5MUkoUufNeP2-nDgaAzpBNG-QHdI-7_5y_tiQgZaAXL_I7RtbhrqlUunhaE7PfJkPu5aHmC9AxdvGi2oV-gv-V9RUMzm_0RauJ0nu56ISR8k2CUUQqu0Hprna9Yk_TLh_mGkfQRY42C6ZV7JtGfquO_DEnXyWoHjlNRQwdh-oBLn9rWmuEwLjbX1TQE2a8MUj2lfy-eHB1gWRWq6mDp9_uBH77NffX7Dqvi2T1j7qHLxTcaVXNjA-D1KaFRwyB2SdNNPu7AmfAtENy-rYWEIWTdk_EUywr0URjoQmshbbo-b8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام زدایی رییس دستگاه قضا از اپراتور ها با احضار مسئولین ذی ربط
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/651972" target="_blank">📅 19:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8549a7b4e.mp4?token=JZhRI_FBQXbIaBUBL9zLWh6H4YM7S0D813mII-DVi_sKWAUZb8IDk3xvohvsLIhC5EMbGL68hi-XNOVynnt7_MHMAI_wTwcxLHdLqCE6_T-cN4PVRh3OcIODchCuZSsq1vg6CApc-cuUthF0Bc69V4HyMKXhPbRd3T_d0yX34o--0aRlbUbGBKepnZJ82ebTnWC15J27Q5jVXTvDtiv-96Oq8BWSUmo84UE3NDg2JlWbvnuFgWIi9YN9JtdmArINwR03v13i17J5Dl1o_OV7_y5D8XnAmmWNRui_GivyGsH3bnXHYvL8WmiVjZ28DWsY9EPZ4G6VrQ-f6B6luNV6Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8549a7b4e.mp4?token=JZhRI_FBQXbIaBUBL9zLWh6H4YM7S0D813mII-DVi_sKWAUZb8IDk3xvohvsLIhC5EMbGL68hi-XNOVynnt7_MHMAI_wTwcxLHdLqCE6_T-cN4PVRh3OcIODchCuZSsq1vg6CApc-cuUthF0Bc69V4HyMKXhPbRd3T_d0yX34o--0aRlbUbGBKepnZJ82ebTnWC15J27Q5jVXTvDtiv-96Oq8BWSUmo84UE3NDg2JlWbvnuFgWIi9YN9JtdmArINwR03v13i17J5Dl1o_OV7_y5D8XnAmmWNRui_GivyGsH3bnXHYvL8WmiVjZ28DWsY9EPZ4G6VrQ-f6B6luNV6Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ جلسه هگست در کنگره را مختل کردند
🔹
جلسه استماع سنای آمریکا درباره بودجه نظامی مرتبط با جنگ علیه ایران با اعتراض فعالان ضدجنگ مختل شد.
🔹
یک زن معترض پیش از انتقال از صحن سنا، مخالفت خود را با ادامه جنگ علیه ایران را فریاد زد.
🔹
معترضان خواستار توقف بودجه‌ریزی برای جنگ و مخالفت با افزایش هزینه‌های نظامی آمریکا شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/651971" target="_blank">📅 19:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70bd3f20.mp4?token=rP3Om2p1EMiqxZYbkAKSUSo5W2-9bfJNOVVvIyAHsPwydz7fdx5UjrPI-sMtrnJrCtKVe-h55MxLqBniRzDSfhQjtMx02tgaEBwI4XcUxF3RvHT-VUlD8Lq7YwxVtExRXMdhPgzoYZA_Ggw6EmLNSFBt-FAT4ruE-p9Z9mMKkfKupwDbNcVP5R3otq6SjqwLRFT2Pfpffu3-Sl-MvrmEEYAe2btO7NJpsW58Idi98glXkBtqgBbg0Gsg579utggvg7U9lEkSzG2_Kcxw0vS-RKGZ9YFhvVH66vt4ALIwFuhyykJDWV2zRTOHWGY0VolBsCV5rUFhhRijdCs-APx9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70bd3f20.mp4?token=rP3Om2p1EMiqxZYbkAKSUSo5W2-9bfJNOVVvIyAHsPwydz7fdx5UjrPI-sMtrnJrCtKVe-h55MxLqBniRzDSfhQjtMx02tgaEBwI4XcUxF3RvHT-VUlD8Lq7YwxVtExRXMdhPgzoYZA_Ggw6EmLNSFBt-FAT4ruE-p9Z9mMKkfKupwDbNcVP5R3otq6SjqwLRFT2Pfpffu3-Sl-MvrmEEYAe2btO7NJpsW58Idi98glXkBtqgBbg0Gsg579utggvg7U9lEkSzG2_Kcxw0vS-RKGZ9YFhvVH66vt4ALIwFuhyykJDWV2zRTOHWGY0VolBsCV5rUFhhRijdCs-APx9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق به تقریباً یک ماه پیش است. آیا هزینۀ جایگزینی تمام آن هواگردها را می‌دانید؟ با این فرض که برخی از آن هواپیماها قابل جایگزینی نیستند، اما قاعدتاً باید آن‌ها را با نوعی ظرفیت و توانمندی جایگزین کنید.
🔹
نماینده پنتاگون: هزینه‌هایی در این مورد وجود دارد، اما می‌خواهم جزئیات دقیق آن‌ها را به صورت مکتوب به شما ارائه دهم. چون همان‌طور که می‌توانید تصور کنید، محاسبه هزینهٔ تعمیرات هواپیما کار بسیار دشواری است. ما می‌خواهیم پیش از برآورد هزینه، یک عیب‌یابی کامل از هواپیماها انجام دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/651970" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae403d377e.mp4?token=WLppBUj-GiKts0KYVtwTAprhMDi79EhngQdyOSv0_HY49RYzTBkrcDgPMP69Wj-2KXkbekuvqYCd141fF_7M-kZqlYHUoN8Wnc5oDYdZuB-NOE-F3S1RTNtPdlY89iV6ZJacwkB7k9YmhuV9YHC8F5JYN0doNUcWKvfZ9UL2FrvkhVLO7ATFeEBfiBC301sPhtxlgI57rCHJ7RGjs7BLLbb88ZwM3Lb6oYX0aYp5ReSmi6hOh7U4S68-j7PZCc7-dGtPVI8TplpLLe_4uWJXLMBAeKEaERzBsC1MpsxvybSv4Vsl3IcJddu-XxY3zRf8_8X80mNa0loucC0q-8VHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae403d377e.mp4?token=WLppBUj-GiKts0KYVtwTAprhMDi79EhngQdyOSv0_HY49RYzTBkrcDgPMP69Wj-2KXkbekuvqYCd141fF_7M-kZqlYHUoN8Wnc5oDYdZuB-NOE-F3S1RTNtPdlY89iV6ZJacwkB7k9YmhuV9YHC8F5JYN0doNUcWKvfZ9UL2FrvkhVLO7ATFeEBfiBC301sPhtxlgI57rCHJ7RGjs7BLLbb88ZwM3Lb6oYX0aYp5ReSmi6hOh7U4S68-j7PZCc7-dGtPVI8TplpLLe_4uWJXLMBAeKEaERzBsC1MpsxvybSv4Vsl3IcJddu-XxY3zRf8_8X80mNa0loucC0q-8VHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: اینترنت پرو مصوبه شورای عالی امنیت ملی برای کسب‌وکارها است که پزشکیان رئیس این شورای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/651968" target="_blank">📅 19:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مینو محرز: هانتا ویروس جهش پیدا نمی‌کند مگر اینکه آن را دستکاری کنند
مینو محرز،  استاد دانشگاه علوم پزشکی تهران در
#گفتگو
با خبرفوری:
🔹
ویروس هانتا سالهاست کشف شده و جهش پیدا نکرده است و از جوندگان به انسان منتقل می شود، نه انسان به انسان.
در آن کشتی کروز همه جمعیت حاضر در کشتی مبتلا نشدند و تنها عده کمی درگیر شدند.
🔹
این ویروس تاکنون جهش نیافته و  با علم امروز از انسان به انسان منتقل نمی شود.
🔹
بنابراین ویروس هانتا جهش پیدا نمی کند چون سالهاست که وجود دارد مگر اینکه آن را دستکاری کنند که البته بعید است چون خیلی از ویروس های دیگر نسبت به ویروس هانتا قابلیت بیشتری را برای این مسئله دارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/akhbarefori/651967" target="_blank">📅 19:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU0nOqiCWEaHvjD8wV90AOWDM_VlPi1vNwFP-JD3RGDIDGawgFA-YllQ0mPCHGPN9J5xFLmVn4cIYZ9W84CnyCu8e3Xz30jmLsdgT2nyFPLgE4cJqG5pZpVukl9cVz2J9dEOMFsg5Z5BcFmgpXDb0ZHMirk0z0KRByiEGYLg08jALzF9tR86HbPPVmKCRvM31wKb3LTbZOjWlGdg2V1kro8wSUpdu7CMy_j_JYkJQFFYPi87-di-gNZg3grS2VpfpK2Gu655sCCiqAEFhPOqOwZXhO-BWkEPMrLI2kVqXDJKZItH0MSBWyn5PC1u7c1T9fYQ708KhHsjgLxibq2mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایش فیلم در دالان تاریک قطع اینترنت/ جنگ چه محدودیت‌هایی برای وی او دی‌ها به وجود آورد؟
🔹
وی او دی‌ها که قرار بود تحول ریشه‌ای عرضه محتوای آنلاین را بر عهده بگیرند این روزها در دالان تاریک قطعی اینترنت به دنبال حفظ کورسوی حیات خود هستند.
گزارش خبرفوری را ابنجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3212579</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/akhbarefori/651966" target="_blank">📅 19:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d499d05e5.mp4?token=GgV_FLf7dGgSaCxSzn6UcwWdWG5pggyA4OJv16EPU5jHdqrGU5LTso8HFuGXZyWFGEV0clDLIu3OFiNoBBf7mUselb2yhNz8zSxSwVZsVhVYvi071UOYOZ--ba-TeZzGO63gDi42BKWgQFGjq_WF64PbOzIk2RrnpC8jqdDxvNE5W-oxb3tsAf5uv-aJRVYN0RnkNgGIHT4NRuBXskqrFtCirzeRQ-zOSU1VB2YV8DSIV5CEEkuzlmCBgDJUCMHJ9aJVYkxeCSPKhxPh-6ZM698kLMogFY9pGXh-CCi4HecDQzlRjb8Yz06IRjOoQ_SvTS1c0MfBVTEb8tD7mfEY3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d499d05e5.mp4?token=GgV_FLf7dGgSaCxSzn6UcwWdWG5pggyA4OJv16EPU5jHdqrGU5LTso8HFuGXZyWFGEV0clDLIu3OFiNoBBf7mUselb2yhNz8zSxSwVZsVhVYvi071UOYOZ--ba-TeZzGO63gDi42BKWgQFGjq_WF64PbOzIk2RrnpC8jqdDxvNE5W-oxb3tsAf5uv-aJRVYN0RnkNgGIHT4NRuBXskqrFtCirzeRQ-zOSU1VB2YV8DSIV5CEEkuzlmCBgDJUCMHJ9aJVYkxeCSPKhxPh-6ZM698kLMogFY9pGXh-CCi4HecDQzlRjb8Yz06IRjOoQ_SvTS1c0MfBVTEb8tD7mfEY3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در پایگاه نظامی اسرائیل در شمال فلسطین اشغالی
🔹
منابع اسرائیلی گزارش داد این مقر در نزدیکی شهرک «مرگالیوت» قرار دارد و دچار آتش‌سوزی شده است.
🔹
این مسئله ناشی از حملات حزب‌الله به این شهرک اعلام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/651965" target="_blank">📅 18:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIe3jHXt26xSHRFYVa9JZ8nkm43K2XskmP2WVOShkg4K2-yv9ovHMGX2d8LjJVKsJFtxlvqw3Bft8w2B8P3zJ9SmL77ps6jCnL95N7HOlIQc65YTD06tePKW8SPefUPHk8Kw1XbtFZ268lxvsZQHe3sIBWmMCscmWYIRNpjXUUWgwzYuuz8bU33afqC3NOzvpf0TN_k-Ww7FLOV4IFQRhEJGeNo0AUFKMM8D78g4E3JLCX6wtU_9t3fIfccJhapn8K5VL9Nk9JbzBHKYSmbE_o8nx2yWrX0Cwz4OjQBbT-gxSuC6_fB0th5lV40tB1ZBWC9xnZ_s_vfL0I3L7G5s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات پیام تهران به پکن درباره تنگه هرمز
🔹
رحمانی فضلی، سفیر جمهوری اسلامی ایران در چین با اشاره به تلاش چین برای کاهش تنش در منطقه غرب آسیا در نتیجه جنگ تحمیل شده به ایران گفت: «پکن کوشید از طریق رایزنی با بازیگران مؤثر، ارایه ابتکار صلحی مشترک با پاکستان که زمینه ساز گفتگوهای اسلام آباد شد و نیز طح چهار ماده ای اقای شی جین پینگ مسیر بازگشت به گفت‌وگو را باز نگه دارد و تقویت کند.»
🔹
مسئله اصلی برای تهران این است که آیا طرف مقابل آماده شنیدن پیام واقعی ایران هست یا نه. پیام ایران روشن است: توقف دایمی جنگ، تثبیت آتش‌بس پایدار، رفع محاصره و احترام به حقوق مشروع ایران. چین می‌تواند این پیام را در سطح قدرت‌های بزرگ بازتاب دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/651964" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b4c0212b.mp4?token=FipgJtzp61IgNXrfka3WpEQrxamS6q12gU_TF-loft8vuPU_Kn1OaSy9mpFTJT3uPhtLDdAQj2dxoTwtYwNpLOe6CyPiztFC3D-sItFqPpKXavAY2OTXZWmlhVyRAZd8Ke3G9DUbtjbL1UO64mWODhLN1AIOzExjincMPJIlfXmbvFCl5MF6tOQGM3nunKxLCnSO4Z9vH1VFex_qo63-sjaQIiRGCfm5kIn-K3Dd67D7SaGKv64tl96zs56wsJtKP3V0nfsQonunh1yvKj6R35H0oFQ273Mgzz5u4zHdcCtoaOlYoQ57Wvpvyv5aklGv39jwJqwqb1YWlmw3ck_IqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b4c0212b.mp4?token=FipgJtzp61IgNXrfka3WpEQrxamS6q12gU_TF-loft8vuPU_Kn1OaSy9mpFTJT3uPhtLDdAQj2dxoTwtYwNpLOe6CyPiztFC3D-sItFqPpKXavAY2OTXZWmlhVyRAZd8Ke3G9DUbtjbL1UO64mWODhLN1AIOzExjincMPJIlfXmbvFCl5MF6tOQGM3nunKxLCnSO4Z9vH1VFex_qo63-sjaQIiRGCfm5kIn-K3Dd67D7SaGKv64tl96zs56wsJtKP3V0nfsQonunh1yvKj6R35H0oFQ273Mgzz5u4zHdcCtoaOlYoQ57Wvpvyv5aklGv39jwJqwqb1YWlmw3ck_IqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین اتاق فرار دنیا کجاست؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/651963" target="_blank">📅 18:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOES2igykMhdwqX1oKq6G4WOPCeqWWGnmeT7grfvGaLjDAl-aEm-YG6o0JM6CEr3S2a5RM9Z9c477H8b0FyIEGJpkthes5Gp-yp4cGbyaWo_DWuMC4Mk8GVwEg9l7cEBo1sE1KgMYCr8bc74ZX1OgZ0VS6klx7xeknAERFiEEIy2R1TrCQMFNbn1A4LYO_HmF43no4lVoZV2sAQEtbhoGijspkBRBTo5_fGMmtQQ7PVFH7sviNzWFgoCrNUph4bStguxQHOFf7W6SxpFLd1dpoBHworIZT9oRT-5Xv_TpldHkrEYWswAF30WwWI1mSS87pAiBZ7TreQpPqiFvOvZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت در بند پلاستیک
🔹
هر بطری، هر کیسه، هر انتخاب کوچک، می‌تواند حیوانی را آزاد کند. آینده‌ سبز از تصمیم‌های امروز ما شروع می‌شود.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/akhbarefori/651962" target="_blank">📅 18:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
کویت سفیر ایران را احضار کرد
🔹
وزارت خارجه کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/651961" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68eac19863.mp4?token=DZonB4Zj1R-Mv6JQ7iRtJvQMHOo0gRgbZM7KtwLl5RoOZusXKfdVr8zrnQAnpTpB5RCuug7EiX_rJBACI05dkYnGhVm38jtsLq6RcRkrNjmHPuLglR_NmAHT0fuBiFNrZtIYgMv_vz49tDMz0WAUipT6p1vlACMPlfSKrA4B2P_qVYfuhKsxOXRfimsshSaR1qE0Swz43L6y0uWA7KO5-Ui9boiAXi6LWfiMkM5OQfRj8Ec28xDu6fUpiG34fz4rguO4pWDU959UAdZvVd5nxs2_goYk13Ls04kiDmUuOqbWjWUZEV0gQOiP0OOch7VyzGfvnrfNlb9OXBVxiVCgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68eac19863.mp4?token=DZonB4Zj1R-Mv6JQ7iRtJvQMHOo0gRgbZM7KtwLl5RoOZusXKfdVr8zrnQAnpTpB5RCuug7EiX_rJBACI05dkYnGhVm38jtsLq6RcRkrNjmHPuLglR_NmAHT0fuBiFNrZtIYgMv_vz49tDMz0WAUipT6p1vlACMPlfSKrA4B2P_qVYfuhKsxOXRfimsshSaR1qE0Swz43L6y0uWA7KO5-Ui9boiAXi6LWfiMkM5OQfRj8Ec28xDu6fUpiG34fz4rguO4pWDU959UAdZvVd5nxs2_goYk13Ls04kiDmUuOqbWjWUZEV0gQOiP0OOch7VyzGfvnrfNlb9OXBVxiVCgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: وزیر جنگ ترامپ گفته جایگزینی مهمات استفاده‌شده در جنگ ایران سال‌ها زمان می‌برد
🔹
دولت ترامپ حجم عظیمی از مهمات را در جنگ با ایران مصرف کرده است. بعد از ۱۵ هزار حمله، تنها چیزی که نصیبمان شد، ۱۳ کشتۀ آمریکایی، بسته‌شدن تنگۀ هرمز، بنزین ۴.۸ دلاری بود.
🔹
آن‌ها بدون هدف استراتژیک، بدون برنامه و بدون جدول زمانی وارد این ماجرا شدند. حالا هیچ راهبردی برای خروج ندارند و به دست‌وپازدن افتاده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/651960" target="_blank">📅 18:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea6055463.mp4?token=UXS6gpL7EYPm4pIq9B4bP_fA5qJs_dhXWSAbbkzFnKol7E1uShyjSpi8o8Udo0efuiTy2S53BO9E2Fp8LE8J-n-r6bz3C7RMhbGoec7sAvqc_bzK3LWHJcqfzDQ_kH3e371iNeY5Wu3t7LYEMsPHWVLLuXbTP094Dy_I1nMFsB1YSB5ezq5gmSGaiLrCKZbyCyTLefDLOu_h6ktESmrlzch2tJ1d8jp-_yknDCIwNGyNVFHb_6wPPINRXupYdU2YBwHpmNsgMqKf7L_s6ftfqYk9r7aRv3N_ZRfAprUiRiM4TLeYRWoV97UM9CViiGychzBdWaGn4sFZTT6rTB3AYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea6055463.mp4?token=UXS6gpL7EYPm4pIq9B4bP_fA5qJs_dhXWSAbbkzFnKol7E1uShyjSpi8o8Udo0efuiTy2S53BO9E2Fp8LE8J-n-r6bz3C7RMhbGoec7sAvqc_bzK3LWHJcqfzDQ_kH3e371iNeY5Wu3t7LYEMsPHWVLLuXbTP094Dy_I1nMFsB1YSB5ezq5gmSGaiLrCKZbyCyTLefDLOu_h6ktESmrlzch2tJ1d8jp-_yknDCIwNGyNVFHb_6wPPINRXupYdU2YBwHpmNsgMqKf7L_s6ftfqYk9r7aRv3N_ZRfAprUiRiM4TLeYRWoV97UM9CViiGychzBdWaGn4sFZTT6rTB3AYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف جنگ از زبان روبیو: بازگشت به زمان قبل از جنگ
🔹
مارکو روبیو گفت: «ترجیح ما این است که تنگه هرمز باز باشد، به همان شکلی که قرار است باز باشد و به همان شکلی برگردد که قبلاً بود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/651959" target="_blank">📅 17:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz73ruePXJX2knM7W0yiQ--hrNcLyAtBxXCh6azCyQQYQpvBiDKaUc95KyQBIXNhwJA2HKzjVp8t15nEPHujZWiJjZHdEN98dIJJwpqgep8HILK7LkkFWpOQrlLiGr55Mw6V5QaYm38B_RD99HCk1TRh-hDMfA9CecQsXPpMh_EI72QNWbtXENlhf56I2zO80lNytqLZSHeIibVFUmYBb3xfJcMMXsO-xeWRGz6vAQOVswmjlHyb2JNPx25O3xtXmPfXHPvbrn6Z7akmgzJ9zXYZs9WBjWfW_m5qkJJOGu2PCGZCfc3SN7ajONhTbKDuh3cTF_PRVxT2xKzcsqTU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و آمریکا دورتر از همیشه | مرحله اول جنگ؛ بازگشایی تنگه هرمز
🔹
آمریکا و ایران همچنان بر سر چارچوب یک توافق برای پایان دادن به جنگ و بازگشایی تنگه راهبردی هرمز اختلافات عمیقی دارند؛ موضوعی که به یکی از حساس‌ترین پرونده‌های دیپلماتیک سال تبدیل شده است.
در این‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3214220</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/651958" target="_blank">📅 17:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdp2D6Rq9T73CUJ_P69z7Fwwd2XObWLZDcjOC2-zSSCyF4ETEqI5zVrdX2is24GD0wW5CfZk7ekI-emiGamE385zAmckZOmU5gMM4POz8E6KjVHaJJo-8Ny43qiJVfDShUdCfugL5uteRpYR8xnWYIM_9ijgxR9LRQ-3w2Ak5KmBBMo_rlOFp5HVFZkvBL7REf9yl8ZlBwIcdbj1uQrCgSXe2Rk_Mgy54HPWIZ0aMmYSK8ayMPK85TWuyWTTiiEaqMTaX8LvDgN8vqoD1B7SZr2jMJxm08hbxH6iFJKH7DqaEf1b5d3w-Y_Sq4cruQLDOpDbysPE2euRh_u_88Xpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: «ما ۱۰۰٪ گرد و غبار هسته‌ای و کل ماجرا را از ایران خواهیم گرفت»
🔹
یک بار در عملیات شهرضا سرنوشت ماجرا جویی نیروهایش را دیده اگر هوس رقم زدن طبس ۳ را دارد در خدمتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/651957" target="_blank">📅 17:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIuj6KQvZSOTnxzMiPijBxA7dBN99zZ02yr5jYA1pAe3VjsrtRKaWy89oGbgPJJ8cafWg7Nw5rycccJ4WqIeDbu-hHBrFQ7Ju2sFXPFosgN9qDuOIebG3jwTFxneKcfLVgiCESRv7KcgqSHP-k0rZzB5smZuU8RdVCVPTFJ9hUmYRK2kQFCRQHaD3yacoHUV73MU8yznLJUIEhpRY_QLpv2v1NJnersx0wTIvlO6aScI8C4klevt8k5uKuRMCF338TSRoeyU6el0075baJdzV-I122mEhkA08_CUxVUZ6llw-CoJDZoh4Pmz6rmOOn3HmSvRTSHFADQ2jibE0ccIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا
🔹
نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/651956" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbf8f3249.mov?token=Z1m7dfRERLG9LYOzOEfziDrCJ_whzdOsiVkHamC1Uv65m5_jRRyLQBsSjLxMMEbXhhRp-yHz2ZJvAFqkNPZSJ36V9okSfELNz1ZrvakJu_YnPYBNqvmKe9eJz13uHWh70hPBUbJV7oyCDGzbNnNAUc2VP_2bu84pavdKDfVf-dGFUMVe91-x5t5tt_zenAhvZXfpRhFB5OFNKHCPblU7_bVfUm4RoEKROkhmtZg2PPsEu8_Y2yo4r0NyVSGC-FiytuwMU3GaZNjNtBoeAxQBhIG-YATATCRwv-xjdSPVbmSus_1RcsJy654aj0shfumnldW2rXEaXSRahZiBUM4fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbf8f3249.mov?token=Z1m7dfRERLG9LYOzOEfziDrCJ_whzdOsiVkHamC1Uv65m5_jRRyLQBsSjLxMMEbXhhRp-yHz2ZJvAFqkNPZSJ36V9okSfELNz1ZrvakJu_YnPYBNqvmKe9eJz13uHWh70hPBUbJV7oyCDGzbNnNAUc2VP_2bu84pavdKDfVf-dGFUMVe91-x5t5tt_zenAhvZXfpRhFB5OFNKHCPblU7_bVfUm4RoEKROkhmtZg2PPsEu8_Y2yo4r0NyVSGC-FiytuwMU3GaZNjNtBoeAxQBhIG-YATATCRwv-xjdSPVbmSus_1RcsJy654aj0shfumnldW2rXEaXSRahZiBUM4fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات و آمار آسیب به اورژانس و آمبولانس ها در جنگ رمضان
🔹
توکلی رئیس اورژانس استان تهران: در طول جنگ رمضان ۲۷ دستگاه آمبولانس، ۱۰ خودروی پشتیبان عملیات و یک فروند بالگرد به صورت کامل و ۲۷ پایگاه ما آسیب دیدند.
🔹
بعد از آغاز آتش بس تا به امروز همکاران ما ۲۴ ساعته آماده به خدمت هستند و هیچگونه تغییری ندادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/651955" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651953">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9524ecb154.mp4?token=o-qrdmqejbLlz7woiPbYiON1OWXSJ4790AT6ZCmvIhUrryQ1EUGoTSfxvxUbxQyyvMsdXdZ9JeLKbX0c6A2dUwdSiDd7oW8vlSowlmgI_518i31kcBczBbCN0qx4I-7nzVau3GAJZQrGfkhHfJ22WFWSBP2D4hS-VMOeLBIiJHHhaToEeYrXnPagifTcK2RmpgFE_rQftqVWP-FqhtvTkTyMTHvUlv8t0-LSrTiJKXzM34HEpFUAFj3ip933L4XL14CrUzkzG_strIKpHWzB2k8zmzUiUB1g56gZmC4IE9AkNJ021xa8CYygybwi_B_lNf6eyOM11TaNQZZAr5xxFkdgQfjBJoKka4_JYfciSkb8Rh1fIBoybJkamD-CeAQXxlQZFkTYHS3VfRUBLt5nQfmJDJBzMQwibhabI0ZlsLi8qGGz9HlXzpVzZpnRaQDJpH1q3ydcZgQyAoQ4zoWYn178Wq4kGbkpRxjHyCrxUj71PKGPUsX1z_cdE8oFkUB2BCmRpz-iOGifPREstKPkbBtT5yr4A8zvYAsJtE1n6KKYcT5g9FUxW5YHr-husIGRlqpawRiEP2T2ur8LMnsoSK_BUJ5QbjvxAqjqp2Q-sGraxMpZHRA9f2hz4tep0oZZQCPEcDnNLEkp2k-dL9GNhP0ARW0kw8mpDSWbDxrPPEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9524ecb154.mp4?token=o-qrdmqejbLlz7woiPbYiON1OWXSJ4790AT6ZCmvIhUrryQ1EUGoTSfxvxUbxQyyvMsdXdZ9JeLKbX0c6A2dUwdSiDd7oW8vlSowlmgI_518i31kcBczBbCN0qx4I-7nzVau3GAJZQrGfkhHfJ22WFWSBP2D4hS-VMOeLBIiJHHhaToEeYrXnPagifTcK2RmpgFE_rQftqVWP-FqhtvTkTyMTHvUlv8t0-LSrTiJKXzM34HEpFUAFj3ip933L4XL14CrUzkzG_strIKpHWzB2k8zmzUiUB1g56gZmC4IE9AkNJ021xa8CYygybwi_B_lNf6eyOM11TaNQZZAr5xxFkdgQfjBJoKka4_JYfciSkb8Rh1fIBoybJkamD-CeAQXxlQZFkTYHS3VfRUBLt5nQfmJDJBzMQwibhabI0ZlsLi8qGGz9HlXzpVzZpnRaQDJpH1q3ydcZgQyAoQ4zoWYn178Wq4kGbkpRxjHyCrxUj71PKGPUsX1z_cdE8oFkUB2BCmRpz-iOGifPREstKPkbBtT5yr4A8zvYAsJtE1n6KKYcT5g9FUxW5YHr-husIGRlqpawRiEP2T2ur8LMnsoSK_BUJ5QbjvxAqjqp2Q-sGraxMpZHRA9f2hz4tep0oZZQCPEcDnNLEkp2k-dL9GNhP0ARW0kw8mpDSWbDxrPPEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه از یک موشک عجیب و قدرتمند رونمایی می‌کند
🔹
روسیه می‌گوید که موشک جدید «Sarmat» با قابلیت حمل کلاهک هسته‌ای را با موفقیت آزمایش کرده و قصد دارد آن را تا پایان سال جاری در حالت آماده‌باش رزمی قرار دهد.
🔹
پوتین می‌گوید برد این موشک می‌تواند از ۳۵,۰۰۰ کیلومتر فراتر رود.
🔹
پوتین: «قدرت کل موشک سارمات بیش از چهار برابر هر نمونهٔ معادل غربی است.»
📲
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/akhbarefori/651953" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651952">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b4b75817.mov?token=o2tnb4pp6Y0TLikAZ0yTlhgg3P1a6XftX4G0J58ZJzaO9Rk5g8HWN45WN2Yl7sVufxIpuRoBzdmDJd9BxSJP-74YhgkGoMsDjOSLLdeW7OqyxYB0mhOnDUO85qRjJbD3zlWD6eZ8Jsk0okxf1_nAPvinT9cI9KO1Izbq62EIAy7Md1TzKJJFbF8h2BXxcNI2KiHoKUpZOMLGc3lsFHpPXOeh3BHtsAyxwggUIyvsPTiwyDkrUidWJEjuQYxW5GZMHHwYurKw-f7wAVf9gCoPgQOv6dew1Z9bUbOGpB-85bqYw2Z33ATLRQ-vTmJxDqBCRZ6knJrCfG-hggevHZfCeDJZ4Y1-yAvLqAN6xpA39WghNvTB-hxQFill_NKGJzROeEFgkJpgD1k1XMoU10nCSfiqWey6sHdvBsAL7nfotyfQvThOsMno_MeQVe1j8rL7EZl32zEi-rd3ED6JEuTXPkicDGz2jesoGc_oOuBIUiVaAV6R_7pO5fjFwSL5dbPe6eM9kGRqfA3GvLsiOZ41d1oMkKQuc3LLcGQCs-cglPWj9v0Q-Voxsw3swvuOgDtfUU15YbAosn4zLCoc4-Bsmxkw7K0QqW0n_dzB0Zl7sLWuOL3ARun6HYc_bWiwakrdsTIgOw0KKW0hRBXJ0r9vrrbrvNeEsWX0zbytVPqWOXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b4b75817.mov?token=o2tnb4pp6Y0TLikAZ0yTlhgg3P1a6XftX4G0J58ZJzaO9Rk5g8HWN45WN2Yl7sVufxIpuRoBzdmDJd9BxSJP-74YhgkGoMsDjOSLLdeW7OqyxYB0mhOnDUO85qRjJbD3zlWD6eZ8Jsk0okxf1_nAPvinT9cI9KO1Izbq62EIAy7Md1TzKJJFbF8h2BXxcNI2KiHoKUpZOMLGc3lsFHpPXOeh3BHtsAyxwggUIyvsPTiwyDkrUidWJEjuQYxW5GZMHHwYurKw-f7wAVf9gCoPgQOv6dew1Z9bUbOGpB-85bqYw2Z33ATLRQ-vTmJxDqBCRZ6knJrCfG-hggevHZfCeDJZ4Y1-yAvLqAN6xpA39WghNvTB-hxQFill_NKGJzROeEFgkJpgD1k1XMoU10nCSfiqWey6sHdvBsAL7nfotyfQvThOsMno_MeQVe1j8rL7EZl32zEi-rd3ED6JEuTXPkicDGz2jesoGc_oOuBIUiVaAV6R_7pO5fjFwSL5dbPe6eM9kGRqfA3GvLsiOZ41d1oMkKQuc3LLcGQCs-cglPWj9v0Q-Voxsw3swvuOgDtfUU15YbAosn4zLCoc4-Bsmxkw7K0QqW0n_dzB0Zl7sLWuOL3ARun6HYc_bWiwakrdsTIgOw0KKW0hRBXJ0r9vrrbrvNeEsWX0zbytVPqWOXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک سخنگوی وزارت دفاع: ایران در هردو حوزه دیپلماسی و میدان ظرفیت های دفاع از ملتش را نشان داده است؛ هرگونه تهدید و تعرض از سمت دشمن قطعا بی درنگ با واکنش پشیمان کننده از ما مواجه خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/651952" target="_blank">📅 17:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTxonsZYUBK548AY2Z1Bcwg870KHqWXEiBmAFYop5g0s-0EwBUUDWllfI90cI8O413kW0xYllIB7Ykp6n8rNUk_ghQCaPOQx90sgSaIqd724jWKUdJt0VOBWjpG7sQQguJBxtZM9XT3SvPXD9T8pVcqovFgPdmYjDKfVYXgQx8FbUTnngAgUPEA3i2GSUHFatRBLpUcm_wA5TFVNAQJgi52ZGh4UU8oduCA1Tr9Nw7zAnegnri3gd-ZqVPy8-lctSfQPvgwmiz_Np0qwWZO9qQyzmWS33gEvr2O5Tbw1ztCpd8W7L14JbjTAav--9h3yU_9ujoN-_Iyw66Dw7OezXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بازهم مدعی پیروزه شده است؛ آره  ۲ بار
🔹
ترامپ طبق معمول بعد از یک جنگ پر هزینه و بی‌نتیجه بازهم ادعای پیروزی کرده و گفته است:«ما در حال پیروزی هستیم؛ ما در هر جزئی از آنچه در این درگیری جنگیدیم، پیروز شده‌ایم.»
🔹
برای نابودی نیروی دریایی جنگیدند تنگه هرمز چند قفله شد.
🔹
برای اورانیوم جنگیدند شهرضا طبس شد
🔹
برای نابودی ایران جنگیدند همه ایران تبدیل به میدان انقلاب شد.
🔹
برای نفت جنگیدند جریان جهانی نفت متوقف شد.
🔹
ترامپ در ادامه هم باز تهدید کرده و گفته است:«نحوه حل این مسئله به شرایط ما، به شرایط رئیس‌جمهور ترامپ، بستگی خواهد داشت»
🔹
تا الان که ترامپ هر آتش روشن کرده ایران آن را مدیریت کرده از الان به بعد هم رئیس جمهور آمریکا اگر پیروزی می‌خواهد بیاید تا دوباره در خدمتش باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/akhbarefori/651951" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a68529b33.mp4?token=uT79w0ouPXGN3Q6o5Z44ulhjK6OW1y62x_0-pNQT-R10O5p7CPtfP7BpTOH7Y_9OpWB7j3XPZ6aSaAMdEddk5dF2CGrGn_Xy_j9JqYoBDInsb8NFTBJKXmLbQx-31ooQ3jS5tOLXAD4AJh5Xogi3TFX6zcDPIWp6HK7fIKn71JKJuEovWKFIwGg47lju-6hYP_rOe0Wiwa48jTBix0xmrUeB5DiKtc88IS7X-1Z0GAZkkzAzoV7o__ZhpJBiziaL6rrZhs1tq4qfakVNsiFScQH6cmnnW09amZ_XfD-GmtEqtrdquIhnmXkiRs_XCIb0-oGOH5eb9vO6FYq8Yqw3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a68529b33.mp4?token=uT79w0ouPXGN3Q6o5Z44ulhjK6OW1y62x_0-pNQT-R10O5p7CPtfP7BpTOH7Y_9OpWB7j3XPZ6aSaAMdEddk5dF2CGrGn_Xy_j9JqYoBDInsb8NFTBJKXmLbQx-31ooQ3jS5tOLXAD4AJh5Xogi3TFX6zcDPIWp6HK7fIKn71JKJuEovWKFIwGg47lju-6hYP_rOe0Wiwa48jTBix0xmrUeB5DiKtc88IS7X-1Z0GAZkkzAzoV7o__ZhpJBiziaL6rrZhs1tq4qfakVNsiFScQH6cmnnW09amZ_XfD-GmtEqtrdquIhnmXkiRs_XCIb0-oGOH5eb9vO6FYq8Yqw3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس گلرو، عضو کمیسیون امنیت ملی مجلس: آمریکا ۲ خواسته دارد که برای ایران حیثیتی شده است و نمی‌تواند بپذیرد، اول توقف دائمی غنی‌سازی و دوم تحویل دادن اورانیوم غنی‌شده به آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/651950" target="_blank">📅 17:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1645c3c85e.mp4?token=TjMjywt1hotS7AAxfOavCxZbtTgJG3y9E-r5UA6wHbLMWtxQBGRAmXcQ0gdCwZdDalMhUVHE770_vNefZKFZn1O7R5PfRyu6PBfb-_8ttbU1FVJGRXe1YR_H9GUKybUShqnDDkLbI5RV2JVoQRnZ9t-c_mFrUNFhT0m8M8ackDw1ssCUdjuuC3V0E0bwTEuXcpXEymdyoDWGR3vYTwRADcsSdMqx6qbhsX3Qch7Tgkspg7ESPExA6INBLeAJCZGwKALPtuwv0D-X0tp5EVuaAjLBNNV9Fz1LmLduMaAlPS8c5QEWwwZD4pI9ZRaNwLVhBBhoHMGuFCS2OzCd5UDoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1645c3c85e.mp4?token=TjMjywt1hotS7AAxfOavCxZbtTgJG3y9E-r5UA6wHbLMWtxQBGRAmXcQ0gdCwZdDalMhUVHE770_vNefZKFZn1O7R5PfRyu6PBfb-_8ttbU1FVJGRXe1YR_H9GUKybUShqnDDkLbI5RV2JVoQRnZ9t-c_mFrUNFhT0m8M8ackDw1ssCUdjuuC3V0E0bwTEuXcpXEymdyoDWGR3vYTwRADcsSdMqx6qbhsX3Qch7Tgkspg7ESPExA6INBLeAJCZGwKALPtuwv0D-X0tp5EVuaAjLBNNV9Fz1LmLduMaAlPS8c5QEWwwZD4pI9ZRaNwLVhBBhoHMGuFCS2OzCd5UDoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بخشی از محموله‌های کشف شده سلاح از شبکه‌های قاچاق وابسته به رژیم صهیونی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/akhbarefori/651949" target="_blank">📅 17:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
جایزه ۱۵ میلیون دلاری آمریکا برای مختل کردن سیستم مالی ایران
🔹
وزارت خارجهٔ آمریکا از برنامهٔ «پاداش برای عدالت» خود برای پرداخت تا سقف ۱۵ میلیون دلار به افراد همکار با این کشور، با هدف اختلال در سازوکارهای مالی سپاه پاسداران خبر داد.
🔹
این اقدامات در ادامه کمپین موسوم به «خشم اقتصادی» دولت ترامپ علیه ایران انجام می‌شود در حالی که آمریکایی‌ها خود اذعان دارند چنین اقداماتی تاکنون نتوانسته اقتصاد ایران را از مسیر توسعه و تعامل با شرکای بین‌المللی خارج کند و بیشتر جنبه روانی و رسانه‌ای دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/651948" target="_blank">📅 17:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0858d26d7.mp4?token=hP1tkWnWinhQ8-cgoEaUGsDf7MhDhikXLII6k57Dmxw7SdW-vebAvhDqd2feIR4WgZ-pRbMSBvRU3S92Z5FezxsPsDAse_ZjvuS0YYNwZ4uaSHwlIly03pI31v62CrB9hdBvYeYftMEtYcCh2XSKsCBGMXTgebsdSm4WaIdIfFV9A0kU9xp6AKypaTnmdXlv16ifzxizuBHlXzE7jmWRWDYHlvGE8wP66G2r_e2DO-yd9nZpfBfRpyGbDMRCJN0a6HEn3dTOB_2xpE8UAUXNbKeQrgV9e_W0Dr1P1LsPpz0HtykpoL_VJ06jFBKfZZyZd8_PAaQBrxD9lfCSeVEdDnStXcq9KhhBkvRwlr7arxNOpBTwlmIu35vD1hRSpXmUb3guMZ_0T6uJLgJpyZINAZ6t3g7DgVHH1tZRgVI4eBzBSgFXDyFAk5B_XllV53iZAMQrQK1zVC2-pXqiUYG1Qt6-WcJTn9YZ8YYkEmkzXIbxPke7xaYfdwBC371MQPb3H_4akqW5eOGIocH4EbqdpTvlDNxAKxA1lqnCT6Mi3fDi9UrTBzyYybf7Av3etd5GbuUSicDG4XR9NVEIpbb2VmkA7EdVmQhXH8avvyQ3ZteyTnqgN1_MjThzdueQMjfFdoUfagwIxcQSM0JxnkGl-M66UacwpdDdzAYXf7Gfc6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0858d26d7.mp4?token=hP1tkWnWinhQ8-cgoEaUGsDf7MhDhikXLII6k57Dmxw7SdW-vebAvhDqd2feIR4WgZ-pRbMSBvRU3S92Z5FezxsPsDAse_ZjvuS0YYNwZ4uaSHwlIly03pI31v62CrB9hdBvYeYftMEtYcCh2XSKsCBGMXTgebsdSm4WaIdIfFV9A0kU9xp6AKypaTnmdXlv16ifzxizuBHlXzE7jmWRWDYHlvGE8wP66G2r_e2DO-yd9nZpfBfRpyGbDMRCJN0a6HEn3dTOB_2xpE8UAUXNbKeQrgV9e_W0Dr1P1LsPpz0HtykpoL_VJ06jFBKfZZyZd8_PAaQBrxD9lfCSeVEdDnStXcq9KhhBkvRwlr7arxNOpBTwlmIu35vD1hRSpXmUb3guMZ_0T6uJLgJpyZINAZ6t3g7DgVHH1tZRgVI4eBzBSgFXDyFAk5B_XllV53iZAMQrQK1zVC2-pXqiUYG1Qt6-WcJTn9YZ8YYkEmkzXIbxPke7xaYfdwBC371MQPb3H_4akqW5eOGIocH4EbqdpTvlDNxAKxA1lqnCT6Mi3fDi9UrTBzyYybf7Av3etd5GbuUSicDG4XR9NVEIpbb2VmkA7EdVmQhXH8avvyQ3ZteyTnqgN1_MjThzdueQMjfFdoUfagwIxcQSM0JxnkGl-M66UacwpdDdzAYXf7Gfc6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش لحظه شکار سامانه چند ده میلیون دلاری گنبد آهنین به وسیله پهپاد ۲ هزار دلاری حزب‌الله از شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/651947" target="_blank">📅 16:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrfBliaH5gfuXHtsg21CcJUwUnJMxmAG5mEb1Z5YN78jCUzfDDBPC0HGFEQ_rhldjn_dRQkxoPGFV7FU1r-trULa75hfbAWucZxtI3rd7K3wQkIQcmDXYUj4kidKbXKTuaBCkMuRjDgy3hwB4kg3f2pXk1jvLQ4k6vzDW1f0P5daHLhIfi-QAiHkpcDiMi12igh0uw4d1zqgRmFhgMSqktw3hAv1oD8E7Gyl9HzrtZgx4sOEVg8oZBUnbGyxR7RyK_n_F3fzIAxVNKJV5xYsVbyoLBun2hhUcivuJtYf7RucBY6htmzYHRwRReT5R-jp6oqb6kkO4w7X7cZgN9s52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه عبری: زندگی در شمال اسرائیل به جهنم تبدیل شده است
🔹
رسانه‌های اسرائیلی گزارش می‌دهند با ادامه حملات و تهدیدها از جنوب لبنان، «زندگی شهرک‌نشینان شمال به جهنم تبدیل شده است» و هیچ چشم‌اندازی برای خروج از این «کمین استراتژیک» وجود ندارد.
🔹
تصریح کرد: «ترکش‌هایی از موشک‌های رهگیر که از داخل اسرائیل به سمت لبنان شلیک شدند، به خانه‌ای در کریات شمونه برخورد کرد. این بخش خانه تقریباً به‌طور کامل ویران شد و این تنها چند دقیقه پیش از آن بود که سه کودکِ همین محله در راه مدرسه‌شان از آنجا عبور کنند».
🔹
وی سپس با طعنه پرسید: «آیا درباره این رخداد شنیدیم؟ اما تصور کنید اگر این اتفاق در کریات شمونه نمی‌افتاد و مثلاً در تل‌آویو رخ می‌داد؛ قطعاً تیتر اصلی در دستورکار تمام اسرائیل می‌ماند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/651946" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8195f830.mp4?token=dMrAJuQp9hplmAOEqhIKddVdpXi-au1ggxxA4bbtmjxA45OmyA1shmO4IGlXHwEqQC30DD9oJK6ABOUyO_U-5J8LycwreX6zkixVFSFOHiv4UWJohULZ6QWHfmDh3c8CpmdHaZYlg9ASDJZP42Qlg6jJN0ZGCrcOjHWGsdeDkPeUO1xy3_9jKuPsMDXCjW8tE2BTA8xP1xAKTMmoDMg1uoQjDtw3PHN4PriC_Fnqg7vJAENoP16fiyI_oZUl23K_JJvOKB-clgElft1yds-qvBPMg8wLQeMaEwjAfxU8HSdB7VVzDgdP-aJJZEGZdLLYcEI7jqq7lkSXJDLl2sfYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8195f830.mp4?token=dMrAJuQp9hplmAOEqhIKddVdpXi-au1ggxxA4bbtmjxA45OmyA1shmO4IGlXHwEqQC30DD9oJK6ABOUyO_U-5J8LycwreX6zkixVFSFOHiv4UWJohULZ6QWHfmDh3c8CpmdHaZYlg9ASDJZP42Qlg6jJN0ZGCrcOjHWGsdeDkPeUO1xy3_9jKuPsMDXCjW8tE2BTA8xP1xAKTMmoDMg1uoQjDtw3PHN4PriC_Fnqg7vJAENoP16fiyI_oZUl23K_JJvOKB-clgElft1yds-qvBPMg8wLQeMaEwjAfxU8HSdB7VVzDgdP-aJJZEGZdLLYcEI7jqq7lkSXJDLl2sfYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: اگر لازم شد برای تشدید تنش با ایران طرح داریم
🔹
پیت هگزث در نشستی درباره بودجه دفاعی آمریکا در کنگره این کشور درباره جنگ علیه ایران گفت، ما در صورت لزوم، همانطور که طرحی برای کاهش تنش داریم، طرحی برای تشدید تنش علیه ایران نیز داریم که اگر لازم شد آن را اجرا می‌کنیم.
🔹
وی افزود، به دلیل جدیت ماموریتی که رئیس جمهور ترامپ بر عهده گرفته است و در راستای عدم دستیابی ایران به سلاح هسته‌ای، گام بعدی علیه ایران را فاش نخواهیم کرد.
🔹
اظهارات وزیر جنگ آمریکا در این باره درحالیست که بسیاری از ناظران سیاسی و تحلیلگران غربی استراتژی واشنگتن در جنگ ایران را یک شکست تمام عیار خوانده‌اند و می‌گویند که پنتاگون به هیچ یک از اهداف خود در جنگ دست نیافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/651945" target="_blank">📅 16:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دستگیری عضو گروهک تروریستی منافقین در ازنا توسط سربازان گمنام امام زمان(عج)
🔹
سربازان گمنام امام زمان(عج) در اداره اطلاعات، یکی از عناصر عملیاتی گروهک تروریستی منافقین را در شهرستان ازنا شناسایی و دستگیر کردند.
🔹
این فرد به اتهام انجام اقدامات خرابکارانه در چند استان، ارتباط و همکاری با گروهک تروریستی منافقین و ارسال اخبار و اطلاعات برای مرتبطین خارج از کشور، تحت رصد و اشراف اطلاعاتی قرار داشت.
🔹
ماموران اداره اطلاعات با هماهنگی دستگاه قضایی و طی یک عملیات دقیق اطلاعاتی، متهم را در مخفیگاهش در شهرستان ازنا بازداشت کردند.
🔹
مجددا از مردم عزیز درخواست می شود هر گونه گزارش و اخبار ضد‌ امنیتی خود را از طریق شماره ۱۱۳ ستاد خبری وزارت اطلاعات اطلاع‌رسانی نمایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/akhbarefori/651944" target="_blank">📅 16:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gejIWj7VO7_Oct2CKS2QmdRybEOkC6zYCloruIIeatu1xw9Mi7j9c3AO63LWp9aLPC88K4S81hlCMM9tb-DccET3jfo7CL1yPD257ETcWrSjthfSNiUIste_2bG_2b3WkP2e1x6Qx85sAlMI5i1PyH7_o2FrWPMYVgbv84MKsO3rsujjQQvHtxQMRGuge95hcLmEbLOdm58rk2_3Ss-nDbaZCeDrWsKTsPAD50q-GZDbxfOfrBTSLjNRv7SFXAwNgmEfnojqJaKrnqPOqxTuY83NjphFu6-Nj_qMub_5AFCdqeqW88IWgqIFh_A6ZHqwxXlJVontevpSF8je1LCYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضربه سازمان اطلاعات سپاه به ۵ شبکه قاچاق سلاح و مهمات وابسته به رژیم صهیونی
🔹
سازمان اطلاعات سپاه استان تهران:
🔹
در ادامه اقدامات هدفمند اطلاعاتی و عملیاتی و اشراف نسبت به مسیرهای انتقال و جابجایی محموله‌های غیرمجاز سلاح و مهمات تعداد ۲۰ عنصر در قالب ۵ شبکه سازمان‌یافته ناامن‌ساز، وابسته به گروهک‌های تروریستی و قاچاقچیان سلاح و مهمات، شناسایی و منهدم شد.
🔹
از این افراد بیش از ۵۰ قبضه انواع سلاح گرم، ۷۰ کیلوگرم مواد منفجره، ۲۰۰۰ فشنگ و مهمات مرتبط کشف و ضبط شد.
🔹
امنیت و آرامش مردم خط قرمز دستگاه‌های امنیتی بوده و هرگونه تهدید علیه ثبات و امنیت کشور با پاسخ فوری و مقتدرانه مواجهه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/651943" target="_blank">📅 16:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmAGpjhOAebSP_UBC4O-Os5LROFr4BljraWk-es-V4mgtUZRpEApP7GPij13ZvGovtbXEBziCe25uZ6gN76lDxOzGyFtyV53bAHh-j89iSax0vUKBI49HcEoc2biTNUfCLpd1YwZp7HLbhF4NDLErGQkbtDY61CfTvAZocutPD3-rz0sDVHaJwz8v0s8uMgLSqJfeDlJGfMNr7UArBZlmfFKVVRQ6tvQtsUMsYSv3IqDb2XtG6SkHDjm8X1ktpliCF6Gd0RWVrx186nnAmLRRDAidh_9qB-qe9j6l9gAVurAF8TTI1eVfELJwP5vM4AUspQSsrcx1oNbiyNc06_USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: یکی از گزینه‌های ایران در صورت حملهٔ مجدد می‌تواند غنی‌سازی ۹۰ درصد باشد. در مجلس بررسی می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/651942" target="_blank">📅 16:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjEzVxNSB7WAFQA3e_ew1aqZo_CZ1zI8arsL7qrWpxVIcfUBekjy7OSXDvYstbKOvJKx9CgaisL_zEJ39gYnlux2anJZ9djkW0xzdOB8-NAEi9dz1fA_i7GM6gtPtVurtfdyDCJMdyW3KuE7qC7sEAqN64lr6dXg--0XpqWQGCSiJPDkUXx8RSjBabqxUbwpUMGDAwKMMl28zpgWJWkXleIRktaCZiINcJMp9ieP2gTVlDHWRQZ50huG8qnbdaF8X9KcliRPrKizrSV74Hc2Ytbexcu6T4fZ1XbES-mHUrWYlP2XD_YgcM9zd30nXckbVcYSDA0UKIjTaMlW3hLqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام ارشد عراق: ایران در برابر دو ابرقدرت نظامی ایستاد
🔹
معاون نخست‌وزیر منطقه کردستان عراق قباد طالبانی به یک چهره رسانه‌ای انگلیس پیرز مورگان گفت: «ایران، بیشتر از هر زمان دیگری یکپارچه است و مردم، پشت سر حکومتشان هستند.»
🔹
طالبانی در این مصاحبه گفت: «واقعیت این است که ایران در برابر ضربات شدید دو تا از قوی‌ترین ارتش‌ها روی پای خودش ایستاده است. ایران کشوری است که دارای نهادهای مختلف است، نهادهای سیاسی، نهادهای حکومتی، نهادهای مذهبی و البته نهادهای نظامی و شبه نظامی. این نهادها قادر بوده‌اند که در برابر ضربات (و حملات) شدید حدودا دو ماهه (آمریکا و اسرائیل) مقاومت کنند. ما الان با تحول یک دوره آتش‌بس در جنگ مواجه هستیم که جهان می‌خواهد بازگشایی شود تا اقتصاد جهانی امکان بهبود یافتن داشته باشد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/651941" target="_blank">📅 16:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc97e3f7b.mp4?token=rh-Qa6Nmt3z_Haa6U-fuJALeB-jd0Yr3tMI0KpSC2YRgqEC2g-uEk8DvIER9rMMztTTmkqvf-05pDAXGHd_EBe0jHyZNlMAweAzvvFtVKErm0KqfKzAVUOUMwpE35SvGPLPrj4D_v3aVntC6HsaievCJQY4ZCYdW9e0FJ9f93uj0bby7ySQ6UfhOyC9n8gRxFKGhdmOaRzWtH25MEG7Fl1vxBrC2MdOD_1NC3hoz9YjDzp_xd2gnkrvarCdUuB3ea_GgbpHcfC9B3ARm0WJia8jByaOj2vCuQ13fQOx2DatCHKhrfoz3tJuFJ0t3-8idMwearXjkjxh9lFGsJ8ZO0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc97e3f7b.mp4?token=rh-Qa6Nmt3z_Haa6U-fuJALeB-jd0Yr3tMI0KpSC2YRgqEC2g-uEk8DvIER9rMMztTTmkqvf-05pDAXGHd_EBe0jHyZNlMAweAzvvFtVKErm0KqfKzAVUOUMwpE35SvGPLPrj4D_v3aVntC6HsaievCJQY4ZCYdW9e0FJ9f93uj0bby7ySQ6UfhOyC9n8gRxFKGhdmOaRzWtH25MEG7Fl1vxBrC2MdOD_1NC3hoz9YjDzp_xd2gnkrvarCdUuB3ea_GgbpHcfC9B3ARm0WJia8jByaOj2vCuQ13fQOx2DatCHKhrfoz3tJuFJ0t3-8idMwearXjkjxh9lFGsJ8ZO0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۰۰ هزار میلیارد تومان خسارت وارده دشمن به قسمت هایی از خط تولیدها
🔹
مهدی طغیانی، عضو کمیسیون اقتصادی مجلس شورای اسلامی: در دو شهر اصفهان و تهران به جز دو واحد بزرگ تولیدی، بخشی از خسارت های وارد شده به واحدهای تولیدی شامل ۲۰۰ هزار میلیارد تومان می شود. البته این میزان خوداظهاری خود واحدهای تولیدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/651940" target="_blank">📅 16:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGcDlmOzgb8ypZT1ZT9zKStiYJl-grweK3gL95VNLExIZ0XEy_cyTXAYsyaGdsqsgTorGq0_DGlXs9_Y-L_QogXRRow-bUwCnM8NROEs7f5ruwgmI_jmLXtiNypoIxI0I1u3gQoxN67kHsBlzqwz8JXNM9TQ_QbnZQ1TjhXObE22hdoe5z3P4CYjlybgjZ7II0sjgnTxkz5tk7st_dZ7gbWZr52fI4gB_TY3KTarA1l0r1wa11RcuWWtj7uhN5qCARo10aJUzDF3I0trDxf5InOmlndnSeNiTVQDe69yJ4U9pFoPCqpRylXf2NnVmJ-z4Q5ZsFerSreuWB5EIOgl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش خرقانی فعال فضای مجازی به اظهارات افشین: اینترنت رو به خاطر ترور قطع نکردن، به مردم آدرس غلط ندهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/akhbarefori/651939" target="_blank">📅 15:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651937">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF8aLUsPO4_QcargRSXyVmujm8G3dcGl8RNk2yB3R2UvDtNOlKMRA_qRVhgGrNTpSwP5-FmGpw8tUgnLDqkGeF2GbjOM3s6NFgV66ejumnYBMvy-B0jhfIoMuuK4K8XKwqzc4CAx-fXelSx2VG4cr7lQuMEW_F99_wGZkP27ml0PRzdPEgFn1ys0CgystxQDww0gtaOmrX0f2VKv5r4zGYYeBvIrKBU_tWfrOFu_cLQju2rbdAEr84aDAdn_lEAe4L-IJiuDvu8EN6moeVGKr2h5tlHMcQ82sCFqkTPt-c648gXCC_W8vODoa-Nx-jaos_msIZFVz0hIcushGl_6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودروهای ایرانی در ۸۰ روز گذشته چند درصد گران شدند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/651937" target="_blank">📅 15:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651936">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42278bbb3.mp4?token=UkbotoXdIexRzJ80nIEdt-N2ctZBzb49TRCwMuNiI0lWGJEr3fZsbTFbWIg9Sv0InAhsRu18VOMb3UWTH9-UxDji_H_FoGUXbFweujpaJMtKdCivauhfcrSAR3p_WKhMUyxnd7de2k4PeDuWoYd6etDcObnFbNzv3cbS03TNitz_nTGLo2bPjCCaf5HJfWXyx-DbR1KooEya5qc8WmhH9_egsU_veI6nqojPfb4sJC4hrN_wqc1bYOdYyScL_3h85_pbEoSy3bBNQ6kmwdue5sLozjUfwr0LuH4MvVSDQdsp7PVHUD0V3n_myph-7dJgZV9U9yRzKK0uULxQjttTFXH6nyMp6glUc9GiAlrBbAmiVfU4oFEHOR-fwvNQAn3HvXfjSShtK-HONtXm11McMWOoKbzmpp_Qsv3_euqadsSOBu0RHFpkwHbtt2ZRrrrJji6BcklbBdag40EvyHwQvZT7lhobQpibN8J7V1dCZ_7IB9PMKAS9anciapWJBOskuT4PoSDBZ9SDaI6gBz5mTfgNo905E_DtqR2doJpxoxjsZvL1HjW1lxT-e339LbdLy0ghoIHgQqV0uCFmbhqStax9xD3lNvvy1V-0YOhu5aL-LY3bm7lcAU1C6GMdBBaOuOvWrz3-uj64YZ9OgJhlnDjCvh7NL-UgrYcv_jTJ2rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42278bbb3.mp4?token=UkbotoXdIexRzJ80nIEdt-N2ctZBzb49TRCwMuNiI0lWGJEr3fZsbTFbWIg9Sv0InAhsRu18VOMb3UWTH9-UxDji_H_FoGUXbFweujpaJMtKdCivauhfcrSAR3p_WKhMUyxnd7de2k4PeDuWoYd6etDcObnFbNzv3cbS03TNitz_nTGLo2bPjCCaf5HJfWXyx-DbR1KooEya5qc8WmhH9_egsU_veI6nqojPfb4sJC4hrN_wqc1bYOdYyScL_3h85_pbEoSy3bBNQ6kmwdue5sLozjUfwr0LuH4MvVSDQdsp7PVHUD0V3n_myph-7dJgZV9U9yRzKK0uULxQjttTFXH6nyMp6glUc9GiAlrBbAmiVfU4oFEHOR-fwvNQAn3HvXfjSShtK-HONtXm11McMWOoKbzmpp_Qsv3_euqadsSOBu0RHFpkwHbtt2ZRrrrJji6BcklbBdag40EvyHwQvZT7lhobQpibN8J7V1dCZ_7IB9PMKAS9anciapWJBOskuT4PoSDBZ9SDaI6gBz5mTfgNo905E_DtqR2doJpxoxjsZvL1HjW1lxT-e339LbdLy0ghoIHgQqV0uCFmbhqStax9xD3lNvvy1V-0YOhu5aL-LY3bm7lcAU1C6GMdBBaOuOvWrz3-uj64YZ9OgJhlnDjCvh7NL-UgrYcv_jTJ2rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد واحدهای صنعتی آسیب دیده از حملات دشمن چقدر است؟
🔹
مهدی طغیانی، عضو کمیسیون اقتصادی مجلس شورای اسلامی: نزدیک به ۵۰۰ واحد صنعتی به صورت مستقیم مورد اصابت حملات دشمن قرار گرفته اند که دچار تخریب حدود ۸۰ درصدی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/651936" target="_blank">📅 15:40 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
