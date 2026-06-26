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
<img src="https://cdn4.telesco.pe/file/BTzqOyjUJdCc5XdnxlQ7zqFf2zaoV5tgStPezha8ou2xCAp3s5f4hss6muFsAW9u5yfdr0mBp-JJQLdFvIOIGviOzHT5W8CvNnM7TpRufMPJxgb8KSLvb13QB9xt8GjNKHc4wj3WVVX8V6OBfA37juzjG9iHyxDfRdGyQT-LU87GrMi1CxR5RIyd9J4Uy1nnUmkxEJ1cE2h7mP_5zzug5hiw67Va5v8mHTv9prEOeOCoQr84_y3Bh382olVZkmacHllkJ4DCDTlnKgqAB2tBLjbjZ5o-rLe7Ajfggbj5OO6N3F6UxyHVRfAVfOTGTgo0yzc9aMIwqpw4kPqahcVKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxqfAWEuU4eao3usK4uLriyDfvGdeNzeggeD-NqPb6CIM07uzJEHE0MgF-sFOPqCDG92mVPf9a9MY9pVABXZPjfILcwkMwY6I4rF2jCbN93ES1UxFUIcC3DalpYW2IpwPwbMipNKcyU2LEnKxzaQY5e4KZUVe_0rxIUYi0ig_8HA4ciK0MRwCpfrDBd_LyhDmjuJheBcTiqEBLUH9aKxj6A_WniYsC6_ngzrgbydG1l3bvHiiV4DIFL347tpptr66cqc62EZxbDxSC-rl5rPNcyXBU5ZyuZkhVdHrzo53wQAy4QOlXV1wAdQEPOlPy4zByUy9uP2_TdCi3_heKvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEQ7fWFlXnEv89sO_tE5uvGgSJqnJiGQKOXImPlI2e4J5eUJRAE6wOB9e0YcE8U-4kW4_0mbqgzRpZ0d63JkE0bkj5YTWmVennzm36O5jB6gZ-EsdZWJpyNUYi1A9IEPSh0sutyWz1__H1bFAYk5VHuQTKUMYjI5bmxpoRnEzG6eIn-v6C9aXLyb3HNKkIwoWXILrwbfDuJHZFZ0C8WebfXDkpUfFYZspui8fXVR-cIDI7P1z2_KiusNrRMzeQJwOWsbfhNxxTxfXPOqxQuUfA3sOztkSq1APJcIxDHeXapSBriUAji0TLQuiRIuBpFZ32WbsK_o40QO13qb_7pQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNN_UQXyCgS9dsGiBd3wXJcc9TasnrobI51xOw7y828jrmeTIIvVTbTFIn8p_C_ZPSarmJqbJi1ByT9WlQGFjtAImL0-ILDwRNGVpOO5kx43kShusoGgQGkoj5EFwgbPIZwhXjVfVSIs61iGLVIzDr2Bwx9pCFFLuTP3Tq0FzwqhFkdL7cAsTSKBs6W7iqtQk7TjqZn8oJdDms4_ajtLYwTH-iNMyEsJcTS6Iwex9eO-NzLCrImaZik461fkSxitvbqeTMX6UsY4-z4Bl2-VFazC8523bDKiwSoY0bW4D1HVl9TxixbgK3N9v_By46KNBAOmRSmiHVlsru-BezAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5c2TC56R9nHRzkvwjJCL6I84MZWWXQqNM4T732JkDj-8UCOK9g9k5SuakxHwCrEyDnJfpvurF-SaMm6k5fDFpQ9O1Y2RLRj_2dXyTTB7a2gWoSKKFNpeehHaxbIc37cOzx4ZS0IJHL4S4SZCIO33eZ5wZzVecq4dh7p8LMNtpzQtEmrb0aXGc57F4-bhL2EMM38fCOVFbDHNDXvLM7SPs4Qh78AmsTCnyFB0nAQP96HNnNXx8miQx6j_4tt2z4aUlcNK1nLlJlpRyJWtMhBB2pevRcF9BvxB3Vd77yIhkm8WWLiuMBznhbFEQMV_HAbXXioHGc8loz3Fqep_eQ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7htThZXDe5psyKVisSdaaZGuyEDnmt4IqSHcQosd9SZaFI0zrFyeWe3dxjQcFiEml2vBnRYJskjBS6ieOtRwsmYcql947onFdCRsNTTNxffT5aATI2sNGq_8jd3xqcFAmUPJAmD0Bmzsytw5429IeisAVSpIO5Lg-wekwXlGihHOmZpDldO2b5m9BoaLOuCJLHfljkQ-NLKgg6026NuAQOJKEutcymViG8svIsA9E7P6rGgkYK84LS30aeRFqFcN-Ho9Krl_v7R77nGXI8Mc0nx7aVFAkUpvWLCvwUz_8vkItn69FoBHNup0TIMydHicnhWq1CDGljpUGwm11TSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EagfVo9qqlk9DmlMoeeFyG4Cfe5iI7vWFKFtsLB6pFeRDDdUCBJCmaZRITbz6xKvumV6WfISsLlvGSER1Ob-k5ybN2-E3bHFgqJRB1Uvhj8JM5xB_qNTdofUATJhU1d4hEvWSYKRHo8Myjrvm4TPXOqJPwAxMn_OUPrj_Jjqzb3dFc6clYCAW-7ExpKchcOZOC-B4mdRJnpT2Z6v7djz8L-L_yho6JMkMx3CDxsLJnEwnz65d9m4nvD-JGID99UfKPJihl0jhXMyrTZTOv6yO6z75lT2ADxzCt8LBz1S02ety30q-VUwmKwJmeEhPRD_qKXCRB_omW6x6LTAvvg4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbbC_TGJdKwNRvN4Cv3fskrRNnsyFiPlHixoBk5Stv0bo51s1_TqziDVAYFTDvvIP99SXh-GRBzZu1FDda5YfTdjyd9opo8YKQGP4YIi3C9W9C59pqISSD11p5AevFT2t_1C8e8N0cUjx8n-6CNjwxWxrFnvwGvbs-X9NBNBu0bs-vvCdgZCJq1a0LqYnU4N1q1PTJNIaV3XQB9A7y1HJD-Sx_lT7l_X6ZEv_0MSGysm5gfv1MnUi7fAgVNwarduoM-SRb-PaOXrATT3UhNXr6VB-ll2oSTJ0vT3xnThFmcgVTHAPhfDtCwWWW93gD0rS4M_Z4AwoucoEWN8kDueug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzzLm9ZnvbB9AhhFMYuU33UhxPRIq552v_mmc6jVcEY45_BO36y1OOtVzip0tHX83M9YCdtDqFBCq7NqUN0QizIWEXLzcgH8ICgGNk4q9NIJzWf6OTIb6CZ399CiJeuBSgDaRaayMxfPX76xTzZr44bQHP7Akq8DBtp9DwQtynjetvWPq5Ql7JG_vaZy2qvq-L1rmIVakMEQhgbIbKH4klywwH4s_JDFHTgX6BRwbnjmeNfX2YyLX4WlxlcdVSTxgyOIt2AkjR495LNgZJpxpxio-BcOPDoRcOko-KniQ6pNbf9m9hBMx37J6eqh82mhYhlOBApBdCTtOz2R4C_laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFlPzzGiwuhJOaU3p0QZ8b0_SuC0pR-aH6wH-7oiv-EXik-5DIGAqunYkYVH3FKZNkVnvEhM9mS5CvM3R0EkabtzIny3RtjvldDyMpwxq4QSDajkhhDdaBfZspiupd4dIRCRM61Ljxet0CQHYTnK_DMVUMdsEzifSrhjFAJ_rDBFtuxzW57WMiI9VSS4blKF2jKeLRM4LIrK5_FwQXUAoD0X_DLTKfKq6tsR_ZpfoZL99Aj4Re_OtO79scgsdxUyMTnqSZK_Efnh3ZEFDSdyuu8ji5yOFddAf9vTH-MKTKRRIhyfZcnitN7WSXzxausocyxM3KgPjk5flioG1ZOKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfOdsDmRmhKaF6jCwS4q9_Z1HdMAKzqCPo1F1d0GvCpSSWY_XUyVnevELbCntJhTp-zrGgzpzIpMF00pATuCSPzdhMln-SRcLoHRfFq7LrsPP1qOa34WbIMNFTThsLkaEoqLAO6CI1TWhjfz0ONJD87ltZ7AJHh6kMJuJs0T1YeO-8EjhpjsJxOyHidIapLBBEHdDlurzeiV91NMZL8b6rNGzYXs1iN3vYzJ8A_oQDWv3WcvtQ6YBGoRcRsQLjatYOKmK0SxuVz8yXeJGecKdFOIwXop1Z2fy96tjVnQAAcT6ZYY5GnYV1FAIyKgaczDy4_CdJcGkbLj8rZay_ca8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz6J_6vAlYCqvIcgiBy3mKrNZwWzHrCB6D-bZUd7sHcR18TjOzrMrNU7w3dSMvinbpXPjygj2xtKi91g_Jz7T5Z-z14M3vlrrjDGc3Y02WY7bjajApzBNGpZepXQUX-yiA7BW7eumfE0WxBCDJ3pfVO6FQsMwTuVmiUqoFHPyRq1lem2-G2AMUwa8AqjXM33Z0kD6UiZmaRmsQMf0kVlOQWXqhtguQn6SfEwahzVlqlIAW8l8Zc9XV7c5eei-WnxcnJ28ZiWe0S0NNlH2WxsLT3U3UOdki107wc5DhQkJFOjwQp1L6hDR13DEEDmNTs6LHX9WccVRgyO838WDflqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcsGw15g6qf-_r8f6fdqwF6ncvF8-4gawkZgcmQiPHWKhoZh6ABdXPyvh3SumXiuAPXGnfFvmLSUMBjH3OW3QmbVg_AWiCS9S5NM7aJHv6rkBrHD6Jj-ZBKEMNYMZCeEqBkelU4m6CRd1xW6eSi1nTfFzuRX0GnbHQKtBIiyk9oyt625tacRfDkLWdxacXL1gtJ5Bh5arhALcgN93204fYo6qmsQ65Jr98JqmWWa25dn4DZt_t6xn1IDmVZkq6wQHG3lF8VcPDMaXTNDrDKN83JmLhSMUYwfpWJC-pYWk6CKKr_qJAKp43eSTDBF0FSxmJzjXgUtDOnSn_RfytZTtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWIujCFNNI3qoCjo9nGWt8U1FQnRqCpXXzKGGx-ex9r2DOzg56uPQ-BW3h2ePD2dcz1oDSVvZlUrTqDuVH9bKxf2atmhw8cFqE45pinEjPB4fZzCTou_O4yb1vWWqY-ec-gDrs2wIMet_0vkuiWnfYJ1oyKw_S1A80WgBOcTbZhWR2OqzgpObnoM_e5lKqXs7t-mvDXe8B78yft3E2y9hMJkknsKFO_AFONNQ8P14JMtmeqAQEqwMS6jNlo9r6Nlka7ufJI5UDOLpJs42Ri0_3Bat-OcfUqtF7Wy4wJodu9o8arsP8Bv5pIGW_ctPaZ4_Cfw2n5I_Rq0Hw_yCs_faQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-n_m7pa6-qTtrMAOVZr4GYffqgEUjAMpnoP1icxD58w0bivEZoGsisa88v4lZgJU9-BNqm1D8QjKhV5JUjVadNvqHyosyNUYl1-je5E6Qtw82xxmVfWWNVBQXJSYfdVd_4xneudehYV-UP5r7jsWQ_D_eWa2lN9oFyZDBE-qMR8sFYBpqPfJ8RunABuIwdgZ9x2A2hOdttGVXYtlGLg2aYDx8rZf4d8sPxs3nzfraWHKPWSMoUo3EGR66LN_Z1zQgvrlz7tKQZlr4CIDHa4WNanlsXCogwR0Zee9775Ufryxjg0gMLY8o_9S1_k9r5Hqy0Rb0_bSbLnr4Vh4gjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSXtlh37cBJdUY4rBftODIBTtUsVEDjNq2W2bY1l-Q_bcZ2m0rcsIQC4x5iP5keMfhTA1do1vDZeebnsMhMhIaBhCIrwN9bI3NPsGpbiywrcH10iF0vOhXWduEDfqOcjLPgHstOvrVjeyPjIQWlfArOEve_k5xVbCfy4xsRQyyFWTs4zyXkyHlCJkHbW4XAjjliJB9nIEhK-uKBQO5FHB9q_Lpxui29HiWU6aWW5Tl44ptO90WdBR0RBKrxMjaSJFOfbU98uzWrnae6D610QlPr_pDTa6QS_zRnP8cb7IMOMLWFst9I-rWm7RHRYs4He_NTD_JXUcx0PaDcM9hwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq5Q4hX3wOzjgdOFkEN0uprHZEScEvG_ke-lf51LmMXOkfSqxv1Qa1CVoz89SL4w3KMzSpqDstOqxWhcWh_nYkfVB8aQ0pP4BThcFLr8ecTd6rNXay_QC3sYk5ze4cPqlSf9tkBOvoG6EvYdlemk59F3UW2t14tKVoyPudUqtcUara68n2QFQdpvYnIMReCg9sbfWvNrlOGq0zgmzcj2JBSXCUsxRGMXPMeRL2aCJl1qo1VGBSlckdSVWO5BQJ7xNDrdmNB03dUatwKqIe1q9IaRdGx6XIa_L0RyylGOb9DRZaxjnLfmaTrMQWEcHNYSBFuTLKrXF59EUl9FDI9cLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2dMDdwIu6EgJcVDzLsjWw02fVd7Yk7LVyWA1Abe9Lo_rP35Iy_C5ZbBoIT0zGxiLHHd5FnuXY2qHiBRHXoy3ifvabl091rIqpE2q1UXUb939xijOD8hMHRPYzMD0iGxn9QNaOF0x6jz4UNEg80xjMJhrevhXZhIqAVRGvBcxeBpwAvDVRCqF-GZMDjqILzx0ipP5gDmCyxwGoc6hWzgGjVn4m1nV3NIIyBBHcEK0MsUj7fP0hIsj82jyb-_4aZ_GNxEgXpZdoboOkr9-Y2eKTQlb3gVJbiRse5cUmYm-YZxVBYurEli-hCgWk3A1y6WT9GB-vKzVltw3OPmud5prQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYepwfvNvH43Q3k6SuCmTQHjV_v949qt5njCMaa3bybX3suewhu4AG1IGZQn4mJ-cYo1TskzTx9nQuuNopC4t1WIazOloLWh_S4h1WWVjpj26zh8xmalnZzVdkgoKtqt90Mi7uAicojSicC5xcci3E0Hsy1wVIbRwDINybzzOuZv2JtDNzw56qF-xRUYo7p3Iw69L7u3VuBQaVjeoLEJanh3OFdH3L004Pm45lk4848mF_ZiJfns-RWLyu0brMEMMY-HXBe_H9HGf3gFrB2UTqQWTp00O2DPd7ly0021wTtig-ZjO-Yi_vPJkJVWxzLHmVS8pZSHGgYYdlMCsOVNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upiFSqODacQdRwNUbIJX0WGDqfz8V_tiiQiJ-e_5gIidr7rZeYZNoqKMUwiw3NB2e5xVHiLg3qVX3p0OpPQ6Qd4ZZqMP0LFuw1Bel2QFk1-mPdeauX6RR7AU4svf4lZnr6gb7TETTcbWA11LCwAB3RmKuAfjkT75yhTCuFgsAZ7P_bvxrwJ1BS91ZzReQro0FwpWlfX3iE3TwJasMrelIzszLcIBwQY0hSSyAdhg-uBVLIiPInNlRB-gBPtXbJ_vGqpigyYbAkR4xSg8AexW4JAnZUpOkyTfA7iGDNkY5ZBHwjFlmkGydYLqA6FTf4d8e37BWVblmEwY9lYAgWQYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBW9jpbEUDjmQl6aS_aWpbBi8dtg2qTWpxoOi-I_yPjn_fgD0gsaeJDa63ixIliM4l6i7AQ3XpbfBG7ppbfPrqSgQPSB1xBAn2jX791ExxoZERFUNYdsyQb_zQMPzxTm1gexNPhKYJHvKW4Pksj3dupWG6u1Gj40kGLiiiQ3JzNavsIL7UQoLw_e7uFG-ZydHpbR8U3dU50zAmobMpEHQllSFxw9MH3df3kYUt16d-MOnCJMv1hK-1npSMwGdGBzTAPJs8aleth0GiwTLRtZD_Y9cKnSixF8vZ9pO3Pf55nri-oHOACYJuLI-IV3DlKE86u3WOznHb_4spIUUA53vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBpYhhjeAwADwu28oAyxFGI-7qnFbGHwD1drEeaZVtoL6l-1rfqvBGXLEvxtCjOOyadWm5pnnvjS56tUowBSOgVqudRxLUEoBioQTCfNfPotgE3xq3GSZJq200m5VUM0hcF78MV8RPrn6HLFFhm5CLY7fyPujpeBNxCvFE6y_QWCWzkP9KJV-jZHbdCRo7hBd15SRrQM66MO61WqxhKPd5mPqZ2oMi4oEKXx5zg1m7pG2jtkLeZOKT6j84RO-3thcjH01SOBMlT6WRdeviCG_NkQ0KHdhXvLipbq0wAATdh_M06AoUOs3F-Oc7nR3t3ukBZzlLUWGS_rvq5S2NogWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6tJ-Jo_OUNj37B9fvhU5LlKrOO20QJidCSx9kFSfsO4E7EzhI6OARyRMe53KiMiu96xyqqMjJCBNBwqAmb8XOb51MqTzFXOkFWglwrZFV-JjsW8S8g6_nOwPqKNJQYAU0_biJvIfXOGZ2522c3KzmeJ_JFwKXH-92r63RiF6Vm2-1alPV5Ov9fR8HrLdTbPa34YCV3imIxfSbYiws1R7qZh44P-FBqqPrCWaTBfeVspvJ_f46HXySqqCKeppQTuJSNKt5_3dSk43T9ekp-v2l_XWwlaXtkrH6Y_OnT6HA_I9EsHnWYaBcbJPNMqP6cRfYqYRClgUej-SBusxd0FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFS0Q0-3RmZKMon64cvhrzhQYqfyvRewe9ga770RD9Ry6Ffo3J68go7yQHN1D3v-3l4ynMDvC-VlynsBYMugbcIi8xQF_JpO0coZG--Mx6TuKff0xnq5zmrs81O-k4kG9Tb_146KBA-3mLsjBX2vfcEemlRf8LNRViVArU1yXRY6IpP4R_wWlEmpMT9jlLKln1mJIRx4h328wYGTLcTVWTAK7ACC2ng_veJHdUNn5buv67FLv3FZj1OLowE5xS0RGy9XxYt81RVsyqbyDBB1I3mChRw4qzQXrqV3C02uRi1rw-B7gEKtpt4qW7bNRa9f-0F77sh_riOOo_2GLoTjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8eiVy6hYsT27ASlDsh7c2GqDd_mKKPJW22DsjlzRN4TzsPGeszrafMIM6jsB2J_wiBe8i1a7sjpvojpvxCUoRjpdWH4ED4McL81QrH6JaJnqV1KkWFIVRoHirAKiuc9Y88qIhnr7i_PZFy9lGFAFPEj8wwj_9_FaqyblLFKi9xM56QuQbC4OVAsJZvJj_W3uhQRg9cPdfElcsTmVD-N8-RfwJvmRCaXQj71tIpMC5kRIF8rZu3axwbrNcizgTu6WgNtVFuzyUn7qB5NPa-pEFFrqsCRKu5xXudGSjQtzWA1IPZn5M9Crx5IIUSsGDz9wyyE1f-TDda_12Guo2ujrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFVixNwE-im0mbX3A4fCLwQI8DGUvHK9Y_ZxP_Pn_juShNaMkZQynWgm_5_qlexZKNXSFJfNx1xuvsIur1N9_qlOzDRrPKJMB6y4q72O2lJNt7ln5P0aYFv7KA1SoCnuBz8fIjy2vxiU0b5k4xaSTkPB6Fqq4Om3rEPg4c2QbbE5SLSZa8ifTvKRCZa6s_Zvg8_1DD9i_pMQoGTcCR8gcdzNW49Fht_KPQ3PWm8el1a4XQHf5WXTO8fh-wCqZBY8DYWk2B3xPNLeJFDCUyz4ZxRU-6hz8OHDBYPCUsjyBiYs2yzsX1yltG4sTjZvJjd8ThpC5dhC1e6bGu11481dGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuXlL90dLiwLBLKCz4pAMtc6tEX7B6anC0dM0JxSOi9zp5FF0Hk4aFHMRUzNtd7qC5nTgmqgly5W6hiZJHFUi-Kp6B3-9263WRY45AIRfiPjKtYDAbakuyFGaVNiklP-p1DgTwBeN0XHwoSpKMrYFmSoLFajcKwSC44VxBystIvmsdd5FBj2htGO7bJzk2O8T33OqgsRdkK9lWGd6fblVemCDi42d8PW4TPhF6pqDpx6LBm2AhBAxo-vBsZQGUpV3oi0gva_m3WQbESX1e5S-6U-_mv76UY9kDdSSQoOxPu36anIlBjj-EYc-9t6tMTXW_wdIFFN1zlClcg_SlcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkO27mitCzqnQWUZx3avSOTS41KjPa8vuzJs4n-eK3t2AwJpHQwhGdOyq_ISO6jb0SVJobTNIBFi64M4NKaFXswABLjowlZN_ylQpaaRROWRJ0JYyGdbIJBI8vMJmqDXn6dxdq9vEtSFMiuh_9CfkP7JVwalL-Tei0g4PnfHyQF1S_4hvUIP2svQgTJaCvG2OfNyrFglQITorrad9s7yKYciei3BjCHy9HrOLl-rCAwffbCae1idSzoALihyF0wmgcdoKtige0CGbpbS6euoOL9QWlDJtety6pjodk8KyR7Anr7_1ZULtrumCf4kj_r0Gisb9VKk9fhyhnZfmuZIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M9OcmhMIT-uLtWcqxtq3FkcNk_WQ-otaJpKYyERefIi4qyc0MWLjaryDkSg6Cqyq-FdcYo4Rep_Gh5sArEnD3mYPBKwoxlb9bKVQxU7qRastQVI0bnfIC3tQXHbywoANGgbssdESs9HiEoJl6PZ01VoT30r-ufE9uae3vALvoF5Q1hEV_TfpgkV7GcUNLyBFbXycYW1odjITXR6hrWycbEf8F2NtF5PyqgtW51B8SnTMhqQM9ADXm7VUU_41kwacj7Vx4xPrzH3b05klx34_lz6nXMdo3U7K68I1fSOkUAtojLrbFcNhd5c1nrCiJWowdBQbMfhfJYGPB9tuxeNNog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M9OcmhMIT-uLtWcqxtq3FkcNk_WQ-otaJpKYyERefIi4qyc0MWLjaryDkSg6Cqyq-FdcYo4Rep_Gh5sArEnD3mYPBKwoxlb9bKVQxU7qRastQVI0bnfIC3tQXHbywoANGgbssdESs9HiEoJl6PZ01VoT30r-ufE9uae3vALvoF5Q1hEV_TfpgkV7GcUNLyBFbXycYW1odjITXR6hrWycbEf8F2NtF5PyqgtW51B8SnTMhqQM9ADXm7VUU_41kwacj7Vx4xPrzH3b05klx34_lz6nXMdo3U7K68I1fSOkUAtojLrbFcNhd5c1nrCiJWowdBQbMfhfJYGPB9tuxeNNog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxxMYSB6_id5dOR_iiBPIhqDqHECPlEHvm61J9lDdk7sVVr5o_AvTLNJNiEp_Gpa_vnVQUnNPLUMccZkRYnoRzUIFTI8kOzKVwZh7ihKonRc88T-CuRZ9w1PhcSyuK9Wzb-yWHwURt2MhVlWx7bF_5kCjH8R7un3dE_fR_ZyVhZFWha3utPVoK9YSnjQ5kOdHTKJgJvFAEBandugP3jAVhcfRv37xNgZYpShRq-5UpmEovaLjFH4_MJKAOzftHjLVjwoJJE-htXvswF-pePWRWRihg9Dr2g3KO-UZm3DnkDvw54FMmLPuRVSlwlCufO1zybBZlT7dV1glfmNFoKpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edESG7dwlVBCDgas8LYzx4v0Tba1XU7cvS9INba38Z1s_2x6BSS19IxEAoxVAL9FeEATzRtILsD8Lm7QhMR6P0X68ee-TPnB2_mi51KyFVTOD7uNrM7xN1X_eMN6_aYjucip57kP0HXnsmXot5Qo6OKeCJ5h960P5_jewiydWdWdIBCrdHPSsof63YblGPVIWkBv6l_m8vIolsMaFWHy8zGA9ErZ2loV5U7qrhm5aS8fuxHW2O8Y9GQe19s52QOPpjM8YgK_DG1UXj8PsZjLb1YcBl0SEk82qOfIx5AnLktZqAnkLFEMM6x0IyajPghvyx1_GU6LkTCQzc5qz_DGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFL9vMU7UJvodxekAXsJhsAOeXX_O5tUsfgMKznvGQYxDlX7CxKbLcoaScRN-jIdYMdhzM54b7u5jQSScO_MiOv5_TTlBqrp96rVdCrMmgdiJ9ex7fhNvK4CHzhvEDGaEbfOCzW0o6oBlIjWN7j88g9pEJpflsHFH5aA70JfFxkfV-dwnB34-Xwlboz9KgvX4JC_K6cNSfb4Ul-JdTcpoBk8WzxMzsKqc46iwtthySZLKWMxyXXDknqeF1LZ3GvLnpzY2NxG-wFXgBekdMdiqXgK_Yrx1uO5DiK99yNyV0q5qVGz57mGVjrBFNCsvvqAam6UJJmzFXRzbdluwD9YCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICvho8ztpR6fKZ9q7pd__i0aqJ7dncwF2HTh8CS5NbfkH2fyYLIZZleCVLYmy0imqf2EIpy5GFjhAdXeDwtGSmK0W5XYACpPrcLl4mvvlQIQBPfprb5ULgTiUt27SEidshezgC1DikprGhqCI3f_3Ej9b__3jjtYYd72MGsQJ_-Fy-A1AA8HXsE4y3Myexl2P_2ttBRcers9CVycMd7GerVPnmLYOFDuQwQ6A1S4YLk52JsrR7alRP05GmjOhwSkIwCUDuOlaWKXkWuiaQ1_GownR3UzC1vE8TrmS0qdqxwidbecnB3SQXHuC12J9Nxxs4uxUYtFZK8L8r8TqyTunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhI5tsGZPWu91yjmmLTpCLf-HiWltXOdWNno69ishDxc7y04SEOUqdGQ9tu420aiUBC-cNxXWy9666ZLt11p5S0tw-5kTt8OGRKjvl-2PBdTze_XEPnuJYYF9POqqmRChNzpjMV5vUWo834IMa6fQ1VO7zSQXUGMMqipdENc44jh6alQ4Rw9mAAxizK-Bg-liCXXsZllbdPN88vG571HKfU5dkygGYVAXAYnP1tXomgkebM05kDdDIj6mz0z_oxjs9MbeQkXfd0fJtotYb6GD5O4j1aINwyZfvksNZAnDklGGSwJ53vBSRZXevnndr2GE2GDRe9Yi0LiHQGOzQKXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOXjmU7lMiUu1O-YMKpY-YF7NwSDnC04m5Fdip9lFuJtWMzz4RTGqd0D_x1AoaLhk975OeGgggo0wTcteAipoDIMuN3spOE3VJmiRWWjieZs9CnAvhBdU9vX27OVQ4sOowzQppTA16OPTXoxeroLKaZ0MgpReKgjGzm7ZTzBrAfuvsaK7zaF7njoFAy9JzjpARtsLXgtfIOpCsvIlSw2ax8Tyi9wr8cX_l7YvhDBSE2S-DOAVdvhgp7mvte2ZBY0xyZ845xlFXsMHn85Qt3EY2JymQXRJyWTnI6ix-d0Fhx2t6Xz8weScTPZtfpl2rXvbwuqlY5Yg-VBmC563VEP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGeKEkSOoCVGrPbDa1ab_pYUzYAAgewjfu32gthlfIVEoxEEXsInd8i9n2cFSoLbK198BpOTCS4o6_wu6c_vX5te3MbSYXimZ44CZJd310gzJsBzwbnbqnpBZW_kQvtp3ElB7P5mbb7ZuQye7QB6e9a1cPoWgosm9WuptZ5dHqVkd6J9TuDpTeDysvu21py6MksVR8FaYqz0Y9U6QW1RZ-nyeyVgxkq1C6J48ibAvktgKyyoF9AtgOGZfaI9-TVnNDAVHv6K42EqVDXwEUBiui2tPR4RFy8XDjYhEH7TKeYoHxE2Eybs4YYljlcEZoYNIl8vjs-PL_N_P4HZ4oAVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePX-a2Z5vS1CkMtB2hEfhsEMnK86UimQ_2-RuT9Y3OUNgORahlAgHrztqTxxIqUICByo5yHYVFtF5AIZr6x2fdksX_cvasp_uMigpml4Dd8aKnzmFMtbH7vYt-o_Z_Y90hnLUy9Cz0sYHoll8eEMTbMAW6PjMpHlGu3mHbZ8rlX9SjpG-BGZhoZuAH3Mq4jNV9igNRgUc1Ty7dS5T0xQLbF_5iSbad30r5jEw2k8jFrOHuvbEwf8pQ12FAsSqK6AShyhr9oXEgXr87Zt_GKUiGa7pYC75DFpO2ti3bV50m2FcaZgqAOJaFdO_qZWxuEE1DDZXuIJMSV5eCQU7xknoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=J3AobAOEBgaAjxKAUM-nlxsp-WfEBW8AYcYp8jEym2o1VOevhWnziC8YfdPqAFFEERrmys84Mx99HThVCzCJNX1FuLEpmjM8nge5W9HBoWNhmkWfHJ8NdAHDXv3stxl4QhQCNJtSVlCWNnzEm0AjBJBhhFjPtdhsXnqUPfOXBhdr288_m2lgcXUVWjDUJBG_G04TfQCzfDtGj2rccBdmKHmRZkGuX0mSSvIvE9waE9b-_aMYoYQzMZ0SXaAq3lue4J5RiwhFIg-ndXoHrYMrEAYhK8g5eo7C41j1Rm9wtEOJmSsGB4xSMBjjuiGIrPjZ8r2L5xB6qARizzXDuNqhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=J3AobAOEBgaAjxKAUM-nlxsp-WfEBW8AYcYp8jEym2o1VOevhWnziC8YfdPqAFFEERrmys84Mx99HThVCzCJNX1FuLEpmjM8nge5W9HBoWNhmkWfHJ8NdAHDXv3stxl4QhQCNJtSVlCWNnzEm0AjBJBhhFjPtdhsXnqUPfOXBhdr288_m2lgcXUVWjDUJBG_G04TfQCzfDtGj2rccBdmKHmRZkGuX0mSSvIvE9waE9b-_aMYoYQzMZ0SXaAq3lue4J5RiwhFIg-ndXoHrYMrEAYhK8g5eo7C41j1Rm9wtEOJmSsGB4xSMBjjuiGIrPjZ8r2L5xB6qARizzXDuNqhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka5ibfxucQfJ9ApsOhjobNc6Awqm7PGTeoM5fPU70m_vbNFqmusJKqvlu0SXxP8lK23iu8NcLObZBHfKwA4IdMmREp9Jf0BRHnxru8iMzVtmZOV_7yhJljpf_Ijv1c5RykR17TNGi3DzFg9-cYrY1H0Y36ZX9PVa3oFDtLTOos0Co1U8M6orWMxRYo0bjW8hQdtvf4q9e5onkurFoFq0u02CgWeDfi0gSHYUg2pQvfUdAa7bExPHQjYBVwIu5ejy7GrOBT25hl63TEq1JvGkGDPFthjsbuWgPv1z_yM4UmUG2mA85B7TyPwEX6dFgKLcD_VhDYkl632IV31MJuzi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3uxrgNc7OnpFkK4yVUqNO5yuB9HYH4m0_uvV5kWJpA8YcG43H9rL8tFi77bC9ZxGumaqYdroeKanwspIsCjRVFO1K1VTCPQxItoXCqFunFBvtrc8CRX8GYGOFmnnEkhNe3lqYMavo-vyRb2hnmB1tPoPmClTs_m6Gzd0k8wDmmswlVL9t4S4ujpyuWd3kP7xKY5EpGbFi1PUyPn1SmnWFLrPlhSUu8-mfdoZBmbxB1Y0SPbeaHX_ZZIPi-Z7wlMKbR_F66kK09RdS26nL-0_8W5mKRIUj3758Jkk7fotsJwmLjnzHvw2AsUuH0BHqLO-9Ailg1QhICmQmbjWaNABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA49yzCkIpdUOQk9_4i2zUWcLGtkJfsGp0eCM0a4892nfh1ioLHnQNuH4NBze5G_1hnx9dDkecQ5lyf9LbdMbxawDFX_dLsL6R7QiNPKaQH7O5mMHf4-h7TcAA4yNWIbbg4LmyKguvI3WWQaJ9X4n6Z0BCSzO3k1XnErwWubN0JK5Uv_pARvsK321ZbEDUkA6Lx4C8YvgOvtHEE_YsQFm8HHdPjCxisoMfvkiKBOEsg76_6S3uWqW0028eWgri2zBJ8ywKoLHtlAo60F9KDBcSKzNL9awGtP_y9s1mYpbWny2Dyy4mCZONlIbBvtdJXSlllxCSV3dv6Y0uxXy99NhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM5e4qyWwHwSgVKD7LNf6AhA7FWz9su57nfdqYA0JNCF_KLl0yyxm25brbYsEbLB4vROixu0CzwYma4UJp8toVJ666-c7HTFIHdh7Uz0HZZ3T7coZQ7jgrQYOlkwQkMa0ea-Fzxn5LuHVfjuD-QCzGVJkHhICQp-8yeX4wf4R_JniA8-4AkoEkM7gma-yQLA9aycLkps8teWdrBfgTl6sUNAdWIMtc45uIhD0ydvNbqUX6VyN9UFu2G_gxTn2QiZTdY-D6gcSx7Cdwvt0jzv2kcRAG3i9ERI0wrH9ycYOQ7bBK2edkV9zU4Q-gfki2XajtdTwQOg3lWtYPuMHRkeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=iafZJbqKlWroFC7X2uAKrxrBlywIUTOI_suz4wGoQgO72Q6CxEdBREPaP_MNvbYC2t3OTHT6SlaPJzlqjiHHxuRgAvChY5BCRDKAYu_zq-5ST6BX72jT4-YIyBreL3VTEpKgBVCpag9l8XoPsBRfM5xhiaDqCeWeXngZBz6XZRHSHi3BG7ZC_oi7KLvwp59_YzMnSnnNR5aFhg06QIk8xImpl5JHdEMwLldO4AC3UzWrcTTAiMf-G72iLJS7Aduivo3LSOtcMoAjkSyaBdBf4VcHkatZjyjCtBP8V_RpYdcLN_H3EVzH8iqj8jrBEME1eN8I_E7PZfI9We18YN_f0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=iafZJbqKlWroFC7X2uAKrxrBlywIUTOI_suz4wGoQgO72Q6CxEdBREPaP_MNvbYC2t3OTHT6SlaPJzlqjiHHxuRgAvChY5BCRDKAYu_zq-5ST6BX72jT4-YIyBreL3VTEpKgBVCpag9l8XoPsBRfM5xhiaDqCeWeXngZBz6XZRHSHi3BG7ZC_oi7KLvwp59_YzMnSnnNR5aFhg06QIk8xImpl5JHdEMwLldO4AC3UzWrcTTAiMf-G72iLJS7Aduivo3LSOtcMoAjkSyaBdBf4VcHkatZjyjCtBP8V_RpYdcLN_H3EVzH8iqj8jrBEME1eN8I_E7PZfI9We18YN_f0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6kOi0mQClehwMPLdChocGH7-qZa026f50QOpvJb_LrkSd7nhGC-PR9Xv84P9hpWOajbaqwZBWYd-rprI5PMbdzQDFUmR8V_WcndAUsmrT4nG8_UXUk8eEw-9zrRZvrOdhHlpDmCwSBm4uBX_C4d23mrJ8qGLCPQUIoO4oUU-D5jZvW-H3JUWzO0mlGEhMYtFuxXZvgqOMMDKBRR0qEs282nLgwzbUrhPbxiZYn_NxrikyQAKB3Hw-fy-NjXm_UCXINvGNRdgOHApYwwAhDUYptN0eQV5CDiDyaDqt3QSnD38iL279wwo09DWIoDLAGpG-sPW1PJHy2peIva6YXOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd1QI6SSJNQ15wChhWnUb0hpU4XCLL3U6tgzQqL8n7Zyk-80AIAxAJcLzoTDBtIi1Vdt97LdI_SKsKN0F49A_BmHKTVt_vQNDeXJPNQlM7LRHwH8ONaQujdNQxHVKh6bQavi8xGJVXgfpp1K76ooMQkp2gApWMMNQ892DFABiPjPGcOj-4kX-XIlN8fmBmG4c0NbIlbc-g1yemrMyVOKksk_VZji4_r0Y4dTXNTGUMZQQYKzkuXGXRXoKjYBKU3t89jA16J7SZQll0V0nOwQRTpkNKnmM1pbjVISBU7nAXx7TBCvVNP_HXN7w84zSQ1vMKL4qr5fPnRbHwLD3pxUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKLh2S7tPWnzJRJHu2VThrO7fuHNP89wdVwM085-y3rv8riHNTYfum_vwWvFUmaXgO0CdwNelUefW4QT4A4r21oyweciKaCOuFKd2SxKG8Mftvl8-fEGnfqIOjFe9O25MR_s4J-vA7bjqGG5B8mKRgIIqWeBwW6-WUcgjH0pMh1C5kfY8pWkmGF1ex1vzU5PCPD2rLKP8eR8lNEmJFHjA-G4C5MzLOpr9mpfjqnMgPVGEQInGki_9_rAVxo9Mt4CYieYBZsTyiXuW80vbnw8u8weC52fUQz42p56dUlksRjw8AJCVkBOOGDwdvd84oCSUd9r1w3pvjcskKksco5Ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYGvvjY7J1rFj8guTpiXR4rtzeH9fxvrfiYwuVrvg0zC88B8B1zkhjY-jX1WngduywTN3ggtG9lK6AsuStNXkAslWdrrbmwkfH8CZKA-SYQE_ca5k34kGSkLOyUnB4PcpmVswk2N1MEz5evhirOgHJWKlJGXs-GpLikKgG7t68Vx3PkZoiYFxUO8lg_uoz5uV8j8d_8PVBz4DYBm1liJ2gjAIwlL6WiNCacSh-hEU3IEgaxD4VGxJ9hIPOaJIZayNgPySm87chlrr1ZOxJsdmy5vGHHTCwWFENLqdSdJR2WfQwPqxw-ve4xwWZUGB2xt7JxwdoPFZhBvtlvuwZg8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramAmwtmfraAqg-M4OuDHvzyCbGyCqacqbGGuUA1hJxa6jBaXgENOmJ0KkhPdhzZLTK0a9uwCTmn0Wfdh_RCJx8MA6BGUrhgJ3j-8AAYP3sjiaKFTMk0IBo8AeF1FmvB2ZClv6Cy4abnGwot4kDPgJpuePBIhAa84_pGr8_1CNs17mZjbYSqFj3LaFfbckTXNRKjdOyfXTCMKAVtFi31lZQy_IdT3J7joBzEcNLwEkfNQaNLCHt_IqFiulNlCSP5C_C2X1_0fOmJxwLcMsY5IBdzwfLRyfx6r1msgAs-zm2pUaPyzMSjotKI6eRQ6RLTDRxWZTSm8M7uGo10kZkV-AqqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramAmwtmfraAqg-M4OuDHvzyCbGyCqacqbGGuUA1hJxa6jBaXgENOmJ0KkhPdhzZLTK0a9uwCTmn0Wfdh_RCJx8MA6BGUrhgJ3j-8AAYP3sjiaKFTMk0IBo8AeF1FmvB2ZClv6Cy4abnGwot4kDPgJpuePBIhAa84_pGr8_1CNs17mZjbYSqFj3LaFfbckTXNRKjdOyfXTCMKAVtFi31lZQy_IdT3J7joBzEcNLwEkfNQaNLCHt_IqFiulNlCSP5C_C2X1_0fOmJxwLcMsY5IBdzwfLRyfx6r1msgAs-zm2pUaPyzMSjotKI6eRQ6RLTDRxWZTSm8M7uGo10kZkV-AqqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=SJYPEbfrrBKIaXwHFdP9UICygb6vGsnrYc1ot0W-raGAN0eQJ4E3eVGovj4ig7A2XuOFu1NrtNxe7v9lTPYE_T9UXjVZkmq9v-VirrzpuLoZBnblqgh2drYkCFfDMP1qfhD_oFFvQ-u1SzmHUnqOL-BpGfXOoyq33i5gbD1ygq4zpbQeeD-joObGh1d0-_8WFM7BOx9ZMxwA_rb8oO38HhbWuPuStCxbPKySJS54Zd-Y1XWwW-MNjNmkiH66UtwQHyFagsiCGcDKfqPJYJHG5OJyRp9doxvv9pB92djtN7NmXcd02tlNGw0nu8lG8_Cqr7PFwawBqr4yqIDIy-AxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=SJYPEbfrrBKIaXwHFdP9UICygb6vGsnrYc1ot0W-raGAN0eQJ4E3eVGovj4ig7A2XuOFu1NrtNxe7v9lTPYE_T9UXjVZkmq9v-VirrzpuLoZBnblqgh2drYkCFfDMP1qfhD_oFFvQ-u1SzmHUnqOL-BpGfXOoyq33i5gbD1ygq4zpbQeeD-joObGh1d0-_8WFM7BOx9ZMxwA_rb8oO38HhbWuPuStCxbPKySJS54Zd-Y1XWwW-MNjNmkiH66UtwQHyFagsiCGcDKfqPJYJHG5OJyRp9doxvv9pB92djtN7NmXcd02tlNGw0nu8lG8_Cqr7PFwawBqr4yqIDIy-AxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbyLJvLn7EklUBJqnVE8MZrCX64vlNK91UqeXxIL5u_WAf5K3UyCEjQzKQcv3zGDqMiP9z2f-C9SN_xi2SD_AOJqKTPRP57v-4Dvh6SPQppaDfG_i0pSjB9JAB9Mkm58-JFTLROPXlK26QSgydvGKxPTT5-12Q34ulzifRGfOSqHkO_q_o65qvwgA0vHRUPasXqHWk7gZpRtu4hfeZSrQe_LQq0H47jXmVa8AkTXcnXJe9lTAIQ7IjL59M31DR0OgBZEFiNVBfGPWwXU8HlDHJdJ-sdEUmW3_wZP4RDPh1rQnidWWQKFF7D7ruXEI2GSCeX40QZbwg8a4vVQS4Kz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIeNQeAsndfGnCvs0ycX8GgxEj0tkxFgiv774PlV79crZDeGW4rhW6nskpeNV7qRFPBqmUedbXlkDPyZcLSteNp6LTYnVUdk9X-_OvctbJebxcw8Wp0UejLvK58T0Rr7l5d6NK82OCoan2XJfYJCASykS5zJtwihVfmGhRpv04v32LYh4XkrVOy_xnUgHsRrULOPib1WQsvJIshSDFpa54EtzLo3itRxieMEPucIEwJH_YU4Vmy9m98jDYM96Wdt0KmkDjRojTLXXqFITtshGSvq97GUVP8JwqUTK24C63VHcNK1zfebgJdeCLI-EKpjVRQGJn9ghUX_rJJ1YyV01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3PUacoLVujy6v5EG1GumEVftzmGSrCg9LGeoXvVwl3y0r6PwY5u-BPzdHIZp5fwftP4L4StOrZ__3RcjmH096DYJaB-etEimUw1pO7YR9xUJkdoANiY9KhENO4cJr4vAG0VPf7DLifeYRnhsiL_v9L4fSj_gvd_oNFy9aH_6oJFi-7o-ul8ktTkvi5T_Ftw7uUL9fCNAOJqDbOWvm6GvKg_7piOkDQH9151Fxkz_CO2r17646H4v6I8vdihfjahYS7zY3bgINa1077flGglG4SA1UCd_PS3fvLK0ckrwzFq-gT_FFUk6yjz50O4CYr8Mk_daUqmbYZO7IHTN1naCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=io6qWHqW0gn9O-HYnGIpPiI8dRoWDisaRQGJw8F9UyU6-5wypcQ80gXyGLf0G5wR0OxktWWorDbq0ESMUrkxXlo-l-Ndeb2rYezs4QtFzVR8gfkCamFusIXe6hkDCGOsvpkuThRrsyuV8CFaUFFxq1W8Ag-AWw8HQo-haeFpiWizmzn6hQ14Ixd2GZMLpmx_rE5JPcR1OV9OweYpvfYPPHOEUWDHmT3tr3YJPEgzJHBdKv0f26smGEtzv0QwB6qWRp1Feq-9WqaFhQN2q_E8laqVb7810SZfk_eJmJnaU3hl1k6IsTI-f6EkhplWb8uoYlB90zQ1AUCs0WLlhtedqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=io6qWHqW0gn9O-HYnGIpPiI8dRoWDisaRQGJw8F9UyU6-5wypcQ80gXyGLf0G5wR0OxktWWorDbq0ESMUrkxXlo-l-Ndeb2rYezs4QtFzVR8gfkCamFusIXe6hkDCGOsvpkuThRrsyuV8CFaUFFxq1W8Ag-AWw8HQo-haeFpiWizmzn6hQ14Ixd2GZMLpmx_rE5JPcR1OV9OweYpvfYPPHOEUWDHmT3tr3YJPEgzJHBdKv0f26smGEtzv0QwB6qWRp1Feq-9WqaFhQN2q_E8laqVb7810SZfk_eJmJnaU3hl1k6IsTI-f6EkhplWb8uoYlB90zQ1AUCs0WLlhtedqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh94Bn5dKxIKQQ8bCLio8xxMXbeJ1N5H9afqW935cbOKO4r3xh-ka2V6qamDklAwzdeDgoWchvdfLoQmnZzY5U19FxiilXGgumha7qr2e_tPpl3R9k23Dreb6Q07rC0pvxfb-EI5UqgA9oXdCpf7CfmIdQhi5BVNdebXEbEZNU7RiwaruGD3y8ZF_smzuaPzaIq3KrTBdVud5dBhEnOnDa0rMaP-YtN2taZdYNgiRfzCIN5kbDPj0GECPBK039c1MZ5Sd_dLHmd4W_X7Y0wwvRYFgZ3-GHQFUNb5getpor4nUd9N9Cd2aaqhb-UOQe4a2WhmA8vPbiF6HLCUIC1hGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqBSOJRMK7NVcNfSPJb5Q5M3yu2EeUxhDxyAJXJtND4XBlBQ0zVU_slY2AdQM9hNcWontVEBW_2XDXvZ_KiP-lfU_zwTCR0KLo60xwMfiPvc2vbsMt26akArMq2uhtZaHqkYv3BMsJtFcpwJWIPRgCo7P7eNq0gRxzlUa8TDBbczka-3a5TKwkapfPB_wf_oVPzGNfswtyrt57JV-e3wqYJ80VaOUs__ld2y7BM8yWo12f3GbExzrVzdElldZDwTvHzLmgfaDpw-aBH6xp5-EsIk3fKVlLeQtinUBq1UHSGh6g4ygRGKWFFrfnfpE76KcmMuY-Cgft23okR7Lf-7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOKhkU6Z6IK_yEDK--SgienYsArK66uoImmfSDwSyFeD3Oz7pUxwCIRQ-ucbF04xowbk9I4nqgNAtfGg3J59iAOpWUPCRk2ZrC259BpsIkyrLKlHbFhc54s8dkPTHbwygFywDdaVdGfiIRXX6E3hLGpI6pOSSZMzh7sejzkR22xmE-xGMWo5jAFstYE0trv6IVzl-sDm0x2kl87RN27V8RBIL7r-sL8jQEPRuwHgAk_96XdAb0pmJpZVXBZjnEVs9LG3gKuPf-UnXe811SLiHE01glEPFBlDI-ZEqiWhTYU1KCbLrfHFyeUQ52Zq6C5hU9mLjtavyOyuyAq9RwhE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsuXLqCUuudgoY-ctjdNKdzLGRYx72P8yP_vJZ29kYEO87cczmnx9HhXnYLJ2wszGJniBAbg1_hdOsj9mX22qO9134IqC8m53P5EGa4eFnfBLVQR0_tgjCQZa6Nl6GH0jEFrBkLIjC0dmp2LgezH7-BRs9cqgp8_UcAermKDQcrttuAZ8iF5ZbcpagrE4fpjLsFS-pVbRjFcR-LlIuUPMgvJyXMo5TsxFpNhCQBCKwCQPS4pFCo0ch4ZjXLMyW17XvpErYdPZPcH5LWLiznuErk-3xeKV7WWBtRjt0ZOXJoNKddo95tlqdgwjJbPUCgyM1TKIpIXMfaBoGqOUvaUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aum0JvCk2vKA-wzA3ck4CA6i-ZUdFssFEyizVnoMf98ZL9ybWXcpG6qi6pY50sQ4AMxZ2V6SlOGm6Bhp3cnsv-c2wi1vovohCljuLGz31juND7r-dvmB2XFkiJhduk-ENgcCrsTKid_91BlBn8PAIagy8Qxbx972tSA8J8gexkUK6VvdgUz_pPmD4Hzh-6cOQ5rX2In1VKejkJ15TlhZwD0yKE2uDizkxqWfcZdwzaN6yUpe-g5pwfd7iH1P2F1BBJFkZcUCbBfPdmZyMsbyFqlvA8Uyw4RmEWPPSMsasqiAaudqqFEEtP4Nk1QZ84VPc5l-arh21Nm-v8O1c5h_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrHZrw5Mr7OvokUhL5Qiq62DGTdXU4LuJ4BVPK1vm_AvpYvKKFCf8gD5plmVQT3i9kwQKDMrf6uKwotjU8WSpVZ5E6enC6pWamKBpZA-8eJJChzsF7pFkFIruJUri-ahSGkBMaBrVgVl6BuKJb60U_QSeP90NikS9_BzTZ2uaTFSOw8k0aeX5SwZn14EvDhyIeMubFmF0Y7jJOuk-mB-lD8kIyKmv5wK7aG06Y0EvuYW3vv1UW6lsThEe4gM3reSwtpEETthcR6VrMbwB-fwQ-5vs5xu1a_kiaZEJoFmNztZ5dxxMc5CcdtTeCxpGYsAnomrokUn_YTfowDcD5ch9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdlzRMkrDHctIb4XFEM68qRFOLsJElqmti34OeYaAfjlAQCXLvNRuhTjO-RXF0e9rP6OTa6FF5xo-01TmOvzYGQaVMKesoehSk5mZ5yWpTKlipzkyIp02hpSBGm-D9BpCHeDYGdmhlK5I8c0MBOYM7DRAIjgg0bi_ug525TovWiriRUpz7XNhoIyiYOgsg_2ccGbhuyGxGKwRDbxHxfNkOYeEPfeOUs4zqNullgBkgRLlzHQ5-nMusfV7UEZOrEYFRNlQGrmIQaBU9mMcOZqlYKM3KnCNK4Bz7pEY6nfhb-vSWpFB72VSSHaLa3H4ClVroSL_J7Hodfu_ue-rLJUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-biGD6ooax4RpUX4KwU53Zw8EzLLP7GiDTP5RzbvqxXhZO5Ztlxcc_55Fvpk1oZkQKADp4I75BUfTBxB7tbiccpTKAm9XPJZ23VchMvkICN-_TFYzjjlfHfO9L_IxBlW6VIrQYvxPnb5DsyqJsfeaihfXAMIQHYobnSdOUoRM9cEsVMyNjI2Jovj36yAfCp2tY0M8_jkzwdO0_xRSA7RepQFYCrfqqJOR0EVSckFhj2dwU5K91cz3G5z94ZHYm-WKKe-z5Hj0bBbvJAa5DZo8IN2Fhi_2Lnm1WiacXhw_3WSgEKk14CmDoQNPZ9NmKeFBEOcx-6lQX-6fapO7Dnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQdUePQzE_NB00R9GiYHshp-5Stgf8_kMHfujURm5387VG_c6M_uI0aJw7hT8TaMXEV5P7gxYJyTMkO4MxYVqsp0y6w71jjZ1Iy_-WqufrCWljeO_MsKfJT2jrkVuFX0leqcNiZe2YVKvjKnaX9ESUs5hV3A-9BI-PJih30llaX5RAHfogZ-5To7gYRRty8r3wDn1nv2FShQwtrBqxQUEudJuZsLkscF6ETqzH44Md1PnoCwbdiS-XgunD1Cuur9WRPYiEea3H1-XnjKRyvnR9pQS9_tz0vamti4UCFj6Cp4ZED11WWLX3w_3g4RE_fpO7RBINJI_YJw2lBPWKxixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=ttHAZV3P121ltG5zstLxWF5LVQ91xLCX3oN4hsgFXbnhHQntEZkBmLG1VaRseaoeGU28lk98edyIQ3v5q-74xM1zI820viRGbSsuLHYvZj8JI0tI6f_ETODN-1xYbGmqMmNk-Kaf8tdUlxs7X7abmFNWxSvx2WEKvU4ybvGtLTcoPkP1ENVFWA8vyjl0cPr76FAdv4_j9pYiRPPmCIZScw_bDtKjISNBUCqFoPlmnn1c8W_HbxuD4e9lFSkYNwbL8SWb9tRxP-2I8YqsHOCY4chPFhWMiK3JfF1AKhXet0aXIQENwoRJJ96drmH9LQESHU0KNjMN0g3WBTuhYXQ0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=ttHAZV3P121ltG5zstLxWF5LVQ91xLCX3oN4hsgFXbnhHQntEZkBmLG1VaRseaoeGU28lk98edyIQ3v5q-74xM1zI820viRGbSsuLHYvZj8JI0tI6f_ETODN-1xYbGmqMmNk-Kaf8tdUlxs7X7abmFNWxSvx2WEKvU4ybvGtLTcoPkP1ENVFWA8vyjl0cPr76FAdv4_j9pYiRPPmCIZScw_bDtKjISNBUCqFoPlmnn1c8W_HbxuD4e9lFSkYNwbL8SWb9tRxP-2I8YqsHOCY4chPFhWMiK3JfF1AKhXet0aXIQENwoRJJ96drmH9LQESHU0KNjMN0g3WBTuhYXQ0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpKnn0q3skOMc_-yZglN3Z-axfxUXT3iJSHEwzM9eL2qr0xD0BG_QUwnQxwsHVqFhhEA9KtxqED8IBrT5ndDmKrU4Za4jzXzdxNw43I3Ewe53XzZ43-nIlxvjqNuX1-BRJHDqEkYkifLUIfHeC8qyN7RXVeqkzfySxdTsTeq-JnH-PkdqLBVVYtcMJvB5fzuV55tq8Is8zmTHVn48F3UVZgAaXaKbLbkGfCD014T8bvJuDVL7_m_s2r7D2O1AOmY1MEAo6wMnZFt-Ur73yR89JDiYvip7G0X61nILkDDVAHiG7khbPqYIz47A_vUmlq79Gieq4sfDQToPVI0Fl3eXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1o2PPs2IXJHCM6RYQh-IwQV2GOEr5hnqfRwo7M3hYUvmZ5ywgInHyGIIFJjFXAdJ2I5qzv_7H3o7JJ_n89rgrgwwtSnGiogBi7JlImB8JLUiyCA7AsB7rwrgQFu7vBki5gXhmWEekMwAqV7dOvP8lIcHkZTEyoI9_iW-JH705FEknV9tZtZeI_gnGK5bWhjmWU3RVrhdO0rQ9eVVsRo8eWrHiobG5LprOVHT7rZryixLdutdpNTfXpNY6y_JNy_j2d42B4VxrO1JRNuxS2zj0D2iPbBP2W0qlxA9WewBxvFHAHVOh74j-JBqdIq7QI8mTuYR-VMksAd9Vew9llcVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWAC-nJDUb6jrAvjDyfJUW_Uh-tG4hg_W316l6aPf1ZaarBcV8hp9R2Rur2mOE2xK4s5smV8N1zZ8EtZI5wvDAmTGbJVI2awzfWWwji-DyXKqar-fvksxq6zqUIYeWdfV9re291IhLbcYYUO1-wNiBbIwl4tkQLp0wC7-n1F-6cVa86cE9YeQ5zEHZN59IlLnxBoV7hqBUNwICqCeFWLhwJjpUboQz5iYr4IxEbPgIp6rSPWSTGnyICexxq3Bdx8ffOdWqYE1XmdhTwpINyExvIZrYAuRfaElExDwPVt5fP83rxdLXKTXLDnir-mmwbTKbMSelIwpksJ2PBSvSzRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=a0dCwpbjJ58lKdXj3d28eBKapAHpc46IWK_m1zkGsPQHJuwyYUFMf00-hZF5Z29uMtoPuWxwRPSKL2nPm1tUwVHNAwMUjAdTasuIy1CsGafhwD-bxkTUmEmiF-6KhNWt5f1GQSDnoWpYR8k8fCFUHORp_6DKlHudhfe8bffH875WE_C5Xq4i1FJyDofDEBNc37V1KohWFg0HgOJElCKcPqM3TkSgmlht-mc2SBww6JEyKu1BoTo_DvpbL7HInVjczrbW-kzvpjbL9OvXSESdM77EeLtvRtqxF8kHPp5sOHLlQC9O6jBm0isEo3pEfljiR6IPiguuxdxU15YZeP9dgLLkEwSbGxPb5BLdDMdR7UI49sgn66uHX9MwF3TnrVWDOR44CX4KTM2Ij0pQ55DkTI5Kz0VdrYFBqCGYJAdbwpU-0mQGxByWDYyhuY7J6gfmJTk9vGKd_d7Qcj_uTvvhXAyuWcD-fJ0gU8TRYsdy6afwwOcmO39ItmQQZbkYW4_5a02KlSSsC3PnyUM2bU4cZYsTL_9AE7UulMb59B04OEfSQNNdfmt6wEnq-muDRKsdr7-XWc-h2_9blKvlP_cQzhQQb0JdmZssC1mvcQTAuv234Vxr-IQxY5c7VIeqJpl19f-5W6MHBXwuZHMORASl51KvQEXTy-yUjhwhLpPtbrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=a0dCwpbjJ58lKdXj3d28eBKapAHpc46IWK_m1zkGsPQHJuwyYUFMf00-hZF5Z29uMtoPuWxwRPSKL2nPm1tUwVHNAwMUjAdTasuIy1CsGafhwD-bxkTUmEmiF-6KhNWt5f1GQSDnoWpYR8k8fCFUHORp_6DKlHudhfe8bffH875WE_C5Xq4i1FJyDofDEBNc37V1KohWFg0HgOJElCKcPqM3TkSgmlht-mc2SBww6JEyKu1BoTo_DvpbL7HInVjczrbW-kzvpjbL9OvXSESdM77EeLtvRtqxF8kHPp5sOHLlQC9O6jBm0isEo3pEfljiR6IPiguuxdxU15YZeP9dgLLkEwSbGxPb5BLdDMdR7UI49sgn66uHX9MwF3TnrVWDOR44CX4KTM2Ij0pQ55DkTI5Kz0VdrYFBqCGYJAdbwpU-0mQGxByWDYyhuY7J6gfmJTk9vGKd_d7Qcj_uTvvhXAyuWcD-fJ0gU8TRYsdy6afwwOcmO39ItmQQZbkYW4_5a02KlSSsC3PnyUM2bU4cZYsTL_9AE7UulMb59B04OEfSQNNdfmt6wEnq-muDRKsdr7-XWc-h2_9blKvlP_cQzhQQb0JdmZssC1mvcQTAuv234Vxr-IQxY5c7VIeqJpl19f-5W6MHBXwuZHMORASl51KvQEXTy-yUjhwhLpPtbrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA6bTWCGjgAZVEajmhCYIX2t59nafCZA7njaHz9cYQ0y58ACaaNMkjwVb0znex06StsFW5IRnY-ZZG0GnlvSf7-yOiA6g-uC5qzPHwm2C5NtAvbjeD-P84ihPBMw1O6iaHPW8hK6ybvVcdrio1pBn2XkMTzpBFvLp48ZapiBAJUj8qxWaOB3sF1OWf_QfGIwKqJ3Kt0MN1RmKLi2r75fkhaM_NbR5i9M9l8Ts01JcsHdGLHIivmqwy6m9EYTbPHbNk8nwtn_QmDfDu8BTj16LsZceYPimAUHSrscoWNgAiQbrH09u1CmzEZzvkmACQrY8Gst3ryh6h4qQaUGqw_rJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSlbLAehZGyspVMn5XrOZjYgSmmCVFYBa9MTcx9qXQpt3QXDf3ZHLFRdN-MPjELXyT-NYcwxH1HfBXOt3AkwrWQBStVAobD8i3Sj1LsAIND5ErYH08km-nPMDhx7BOv7N8YCqIk67Iq5IFmeZtgvgyOWaXTG0aXDPxtN4EL8YNNdrahIBvWSYNadzqCqJfZJoFkq59SV6fP_TzshnyDPSE9Nom2qvkUSsIxJ28k-05m7cYHqQq0PbMJ4G8KIQSkY4QogXEnli-lNt_RpPLSFJEPnsfxREzsHlLgBNv-YMk9Tm66PlTVIx4wOKDWIsNyHWiTaZ23JKtHieuijrjTloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRuETY4__HHT280UV-JK-8ULLt6QB8ptr8wxdcTFP7z4Ttx8IE5lNt4mH60nz7bm5IBz6a2QLNKENZQVE2kM9JsOsHZ9pWV-EJwxIAboLFbvp-iTTG8692C_O2iZe2Nww2r9BWGQbhYW5j_7vNh0NAloRLdOgDCMIW0MPAAZ9LeJwxdbEZbkWVoBs0otpJljq7d4MwbCa98IXC3FqPXbdNVSp2Y_sCrabgu3bKIkuXHGtlftuw-PnRVvY4vcWkndAzN04RxcNMgPmw4wYNpD5zWzkIKljnCc0MqX-xmOlr86ayscGSXP0-1Bac5R5EHUFBWc9Uplk_MvZQYWAEtvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKIAMarnOErtIyVjg-tX3QOUBpdYOUuGGFX7yGjKviV-yv10iUs48jZqi7O2AzUJIKu8WjciHu7FdgrV3ySTLiNbJjCdIUUAD0VI51zLpU-rV0XzU2yU4UD5NeIEn2KKHHXpak3fwNJnXy2Y-1n8qO-E1CdT7mi7hnBvtdBjy_jlaI1aoakSYDQByK2ubeafDYI5mqt2gG4zl0RgenZ01XBj5Sy1tVqtbb3BsvrPAeEm-oegC1uu9M5Xwv7OT_ChOVDWNRg6HCLx29ufN8hwGbVMOuxoCyQxB2jbc4v7KWnt2EC_qWKYPsXlMxpt1hCICyk5KlJgzwGaMbyZCH77CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3fYaPG5aj9bZD_3SqPeZUHeOmKB_515wPy-6v4QzUX9ZmkpGMW2rM4mysC1io-HE0irgypsxEFfB_U29Ul9zN6mAFwhU5ApCk2lORFIRa5RYBBsxuOhospzPYuuyCT4JKS0be6sQTWilh5edXQirBrrAWTHMKVBNzb-8aTY-8w6nvqInDp6miyjOuUU1wyLDoi8KYUZuwJHjxWqzpsXhgiNypJAeGNGPgRgM1gSFNVgCMpfbXL1-XjTCRvwllf4_Dtt-HyAzk5DBaC2v1BaGiGaO2xeY4zMJPe0zRI91bQrlUZXcfvQai-yW1yP5XzOkTe4z2KBibGEV2AynkQtwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cihtp82Ef1BNIp_f5Js-b3ktgtSwH-czfg3zUuQ-tY05uD8PNE6xZvZoPVZHaMoOnip70o6ENjEtDd6I0qCyphmsVHYs6aT0xRfAsBcHP1tiklHAUUd6J0vaKn1h0ZmBkiz8uHh4qsbuH_DxY58SLOIydarcCsLJPDet95zoN7rqYaa_M3Z7aicYJYpjH5yuhGgv3zynIGS8sy1Y382Ngn9YBXbRWOXpuD7rpXkTSLGuPcBLjrbp-J17HMLrAglKAsbxT_Dvjakd6rseupgrMNJMcekzru4_8TQ49rdJ3r5IXzwQ9GEgQ7yriX761ZtBjv70t8RbYh_rGI1R1hYtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9WzfdeVrpWTi88ttSk5ASjjDpo13ThWoBNKmzdF-i5aw_6OOXOM-c7HBOpfocB_adfEsks9ybFHCjqeIpHbgW45how0d7sGdWas-wDtD-ngV-uRkwmb3XTnp1OgOco_sD-tJVBv5U6KNQwEcVilRiAYRSa4jKEspI4X4jRKIXusGtLgch-WYNHrVQpJ8hfmYuobcoMBkBvMTEIKmOZ5MnVxt2RRwgfFJD0WTrdgwHdOR0rS05eMjwC_JBVnCB6rJWMC6E9nGxeGx0aDeMHQ1VTtO959LqXkF5DACskvzIhcO5OAgBmk64YHSa9gRL82Ol_Ldnz9vovIz0gQ738FGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SamRDTCAqzfc1G4XwfdoBI3KKXWo1UMc4L1h5t-yVmxXAyn0eYX0-sZu5w_lUu-DPghK9QgGUx8s82HkoNHHbXGtIW-paPq9O6MnyT5lyvvy2CUMb3zaIxkwBhs2CAle5jHIcuXBu3fHCrZmOjXLCWrt2RF204SH3vfSYnk6eGPCHump8XA_dgM8-A0Akk9km4mPW-olzaRbvQJKB_kLD8SP8Rx_6KkOSBHlQM7iYf64twnuhC5DzBRZ5bVdrQuxiLd8446mCquIH_bdZ_NCHYPM7afiU-WwrIkGOK3dcM4BlK2q29bEu4wL383VYjjkn7BqKSnkJJjPjh0prDyfuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUXX3QTWLp0sWBXpv1tT5b4JETEkHJKRZIa6sQ8UaKZUdZxyXEy8JzyFH62fETEsqeOPF_aJ4NzUuMXM3uRqMFcrq8auHOr44HvAqCGCm53w_jSSwEMeOxzTlUw0O3kEDDW24q1iz-37XGCExvHnietnEwDyKTkhBiFuJMLPN7opJrJgTvuKu7yqijhw-dY0c3JuoGb-a65XjkL-Tny0-B8IjhHRzwqWYQs7efp9oGv-VUTfdNtbLCn9Iw1RnVbKy7iKlf5slXYZS7SF5bd479HqxBcHe5BesjWip0ylzDKa27_p-BEvCk6TW8VG1CgTefC_jBi4gz9-592H-1v_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8Y3VRLWWAUwltYorqON3kGg_Jf5NrpX2i_ndoeVbzQ4SIW4Ny9ynC0mZOktClxDg9PtanFMu8ykN53bf4b6S_kbVivRpYa1TGtjzaYc4pPJHtVHpM0sjeaNhxk40wfbFii3Td3PnCQFJvtBx6MshFVOnIkRY6HB_Fpd6uvNlfZLtxipkV9M23OhIdfgjpcZjUat95DucEd9LQIyyBxhOQrAmawkB1krTWySE967LW5jwjK9pfqBvd6AspclH5n40sdxQvKqpnwRa2HYOQJL9vNE2BfrmhfObPG_97MpipHLfzTR2ATE4sTvC8tOqF42jHdbKPwXRNqZvfCF3Mez9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=a4TqJ-0mHiW5czJltMfOuqJRE-MqbM3u28OMaFtYt3s9234Jykh4ErAo2VBY5sOKGtKSyfXM8zwgLPHG68-isdOSilr3Iz2G2Ps-jMhvyUedH00pools5MNyOZZEglMJRVQYGlfXOHBUGQznTnX_a123qrbBGzKkxhB2IPJeuMOt2_XivEfeCxV85bZ4LYStzkoPS71M8vsXttqYrP6Rcxir_6Y80BdW-9Pxikl6Ynpoli5YkUjJeVrMeuoJHoyOmzdJcZSHdImJRfdbOPqyNPCkCfYz_isOKwN7o4_KoQ2CEC48HmRd-dn74i-JiAKLxXJ3t_mD6oihHEfPUVXzb5-y0F-22Jwo-yRXf-EK69wGdvZRhfosSiubPR73wW3xGKRJhnWgB4Xra99sQuUzl3MQKxMnWXiq4MJWDzbDnjISFwsYI8ogQ3q74XYkDjD1ljOvaU-k4Q-4Xye78vgyUhGx_wkdb8go8WRKgdOBCixNlRARcJTNvXVFhWrpJ-kYlPgsoVD3Yxu8nnXZD_HquugRh6Nm3KPu5k7qqtgFpbHuISex6yKz1wYaF00ubiNyuUuxmhN9eEKDliIxlj8CT9KzsMb50ADOozpL_-3mZGh85hrBuJCyhdVpj3mefnbCLHlzla3I6i_j-CGWJ8n1D9FSX-0d_xA_KKUlfR_RG0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=a4TqJ-0mHiW5czJltMfOuqJRE-MqbM3u28OMaFtYt3s9234Jykh4ErAo2VBY5sOKGtKSyfXM8zwgLPHG68-isdOSilr3Iz2G2Ps-jMhvyUedH00pools5MNyOZZEglMJRVQYGlfXOHBUGQznTnX_a123qrbBGzKkxhB2IPJeuMOt2_XivEfeCxV85bZ4LYStzkoPS71M8vsXttqYrP6Rcxir_6Y80BdW-9Pxikl6Ynpoli5YkUjJeVrMeuoJHoyOmzdJcZSHdImJRfdbOPqyNPCkCfYz_isOKwN7o4_KoQ2CEC48HmRd-dn74i-JiAKLxXJ3t_mD6oihHEfPUVXzb5-y0F-22Jwo-yRXf-EK69wGdvZRhfosSiubPR73wW3xGKRJhnWgB4Xra99sQuUzl3MQKxMnWXiq4MJWDzbDnjISFwsYI8ogQ3q74XYkDjD1ljOvaU-k4Q-4Xye78vgyUhGx_wkdb8go8WRKgdOBCixNlRARcJTNvXVFhWrpJ-kYlPgsoVD3Yxu8nnXZD_HquugRh6Nm3KPu5k7qqtgFpbHuISex6yKz1wYaF00ubiNyuUuxmhN9eEKDliIxlj8CT9KzsMb50ADOozpL_-3mZGh85hrBuJCyhdVpj3mefnbCLHlzla3I6i_j-CGWJ8n1D9FSX-0d_xA_KKUlfR_RG0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5MKsxHU6-gi7-aNTTb7OU7xfcf5IJ12UaEivlsP-7CCJrf_3jH7ErHBoek0rOSOnb2lys1ipeYhsnIhxQ3-trf_2yC3dC2KXoPjNKlgo3ii3VCf8M27nxTCar_YuqrxxAT-7_FbNVK4rnSiMrmi0eWoUCCB7Ky0na1hnxmI_vNOBFCocqxSmz6Tm5sCaxZnDa_qD-_6-irJ4QKUy8xunvMrZMMTRqtGD2mGC2Q3ihcI9ZSZx7yQ6cJkLACoVsX-7jF0hoPW-_h2XQ54OM5sh6pu_ScqFe5MsgSt5bniqqFGY6GUrKIr7s-YDwzOL2-lm4oZfJo3sMZ3hnx_gL63iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=omLAgt3SOEZUuCCXfmMyWQ5XJaeZsOTqcnpEFgepWY6pkKFCkdaz8Zzmqs67N5sSiMCpep8drvpRxj0WFSK-xTmnOSJTlFDgbeCg2vhdokNQayFN9sUsm1AZjT1RcBQkrivFeZUkvK6dE8fbtTaUDAcs3HLnklY1Cwah5loYn-S5LY-zZGnU8cq8Fdj1neJqwz_ihK1CLE2_jYU2C-JhaHhhll54rHiyBTPuNWGQd_vHkCB1Zt2N3t8KSy33SDYoAWg9q5SZaT9Q1TaCbZbSE6kWIJ3PfyyEww05iVEDEfYfSKcyRmmkPARof8mx3crnVd_MB40p3iXl0eR8RV6FanxiToD3qiKc0fH3TveOvar596m-kWe2iwQWm8iiFNuTYywYZ2o3cnCvysTyM0QxLNHKLw_NGfNF1F546SyiO5HO4qXdPN3qs6C8kXexN1nSpluxrhH6R42if9pST3qstLEKcEtEAWf-nd3rbgkSnG3wdVYgi5hr59gIdzkVpiyXE8md6g9uoLejYr1XRON1ZAzEcpxXS2hfaS1sJs3VDHApoZNda-qXp03siVSKXk6sNvEXHLzoM135Z9llYH_Rn5WDOhZ_Weht07i0cknpJFXlqjm9ZgBKJmRo-iwtJTkdUaMU_WnUdP2lUnYmbI_SxMH3-NmNaxX0Vs8R_NbluVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=omLAgt3SOEZUuCCXfmMyWQ5XJaeZsOTqcnpEFgepWY6pkKFCkdaz8Zzmqs67N5sSiMCpep8drvpRxj0WFSK-xTmnOSJTlFDgbeCg2vhdokNQayFN9sUsm1AZjT1RcBQkrivFeZUkvK6dE8fbtTaUDAcs3HLnklY1Cwah5loYn-S5LY-zZGnU8cq8Fdj1neJqwz_ihK1CLE2_jYU2C-JhaHhhll54rHiyBTPuNWGQd_vHkCB1Zt2N3t8KSy33SDYoAWg9q5SZaT9Q1TaCbZbSE6kWIJ3PfyyEww05iVEDEfYfSKcyRmmkPARof8mx3crnVd_MB40p3iXl0eR8RV6FanxiToD3qiKc0fH3TveOvar596m-kWe2iwQWm8iiFNuTYywYZ2o3cnCvysTyM0QxLNHKLw_NGfNF1F546SyiO5HO4qXdPN3qs6C8kXexN1nSpluxrhH6R42if9pST3qstLEKcEtEAWf-nd3rbgkSnG3wdVYgi5hr59gIdzkVpiyXE8md6g9uoLejYr1XRON1ZAzEcpxXS2hfaS1sJs3VDHApoZNda-qXp03siVSKXk6sNvEXHLzoM135Z9llYH_Rn5WDOhZ_Weht07i0cknpJFXlqjm9ZgBKJmRo-iwtJTkdUaMU_WnUdP2lUnYmbI_SxMH3-NmNaxX0Vs8R_NbluVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9TIJZT8jl1ChWL64xsr9hW4RkJCY-MUHLXAkUuy2bxJPZnkVaecx9LIEEXqX265UKvNr5P4Fk8_wgy5OLpBaibLfystaX_IXIkcNCRhFavDX3zf8fDg_yrdBLEq-NvU72ZMrBhsp-KTX_LD7uJkHb3cBpmzn3bykGkjv_a8pc5XfpUWkwCwM7582-L1-G3TTk1ZTDAxQ6_w29ImyMLTLP54sgn5F-aMcYbgzVJe-PPlCNO39b6zjOrxnsqPEwRKfZShQvvprAJd8SaZNxqUTyaCnsc7mGpXz0jcXflgSnYJBB1enFK-388gOH2WZNVhmJ2dbvCMGRJdqLEJeMdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E91dbw5yBaX6UrFvz40a3Pszo-AIKA1VfJ4s8BmjtdeikDGAcaeOZqQZv8MEnMPc_YXqneGyWzh-Bpo007gt5IpU8WvVe81zuscyBQ_EDoKOx9IVwikngUKTMfHJk8shRU-VsQxrrwzEFw7hdZ5KZ103JzhwNp6jfbLHHeLKMliQqmeoxIJhJWnO9j2Ej9lLuriR15UJq3qCIklj4gw1rcAJmwvdA-Bskc_B9QqFFgPSe4UpNGyfvpwVTCzL-eYOXfSP8nlX07AyOLbL6RSQGOx7CB_V0jUsa5uiz-irKZlT6kq14veMnPoidRAbi3o8Jny_YCpan0dr-w9EUpBVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHXzRg1HahOthoWYYwndqeVbbe1R8xx9iyvdlMhqyaH2Pk_EKQZQd-6MQVZX1F1_voerLTZTZfghjvVMFxPRKog7ho4jtgzQv2jz96wM2AnSo8oA8wOj7nLEaQCkooR4zTnuNDQvwELpxg8TIMXB--MY8ZSDAbf_bBQQnCKNhroU0RGAR_eirLit_BtvJD4Na8E0Py3VU3TAQ7ygQ-S_i5Cixk5z5cARv-3SOmMIb2sDj55bX7OcJAgXC6kcnNuSJ5-HtFwEyYBhGUAFQL9uilUZsgTcmu2u3ZC8ykjp2h-FwLJST8g2k854uX37PTTv0WTbSTN_q8f9ZQzKX0DNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3MVyJM3orzRHfL4B7kB7aFMnnOUoWn-6JrmG6xks21NG3XSrgkkvQJ7c4uoBrgRl6Kmvp1yryrtqQTP4RqzhHS-vMGOxiV_aHoPtjVvCngqRSyLmWqvIM-VID9Ca3or8yATChYQ1XMDOKYgk817USArWbBORjdLdfAAZ3O6tEpids1DO2LQ9cqKmkv4t8XRauit20RjlG_OxHucLkT8SFE-9cdEhTqtdmCmBtf2NQlbImVF642y7pCCU4rifUhIw3RnEhFSeRDVeh_vvEJddB4vX4tLrtEX404YirOzZzLP74cX_9ukJTkZ4jR_a4tHGhpWXWSinDpnuTuxmZWUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qloYb_lvSxX9DCuxIFujLdFBmXFDw-BFZI6TvgEJDEZJyuucAUa4J2cIm0od2XdbiNFszUvQRAuLArI1JbZhYF5K2fLDvSbin3atgzH3Y1Y0opbiYSNp-GJTQA91x96Mbg3_PuixM7b-ni6Ik3lxYTf6E61lBkPyZzuKHbh6yUt_XJSABlOA0zaP-l3douMMVY_mcuPq3NGM5stQ530AwDvaxos6F5mKu818DxEkLpVsyYzO0Gh5o5uMiSLbmByld9gLhlDZqREwlFEFnJV1cKdI54vvXyAr8R49bwmgBIMe1F9f6osq8J-2hRn-B58Sl0YV5fWZRcQzZGcly74drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=vuIihH9W3L2tOh6-FlPo8WUuKaz20wmRE64T26dBupdUKE97wWuT30oCKWrQMoXKfjX2iK6gylcIV75Zc1mLk1MkSaHec94Fh9r6n-alPOuEbMT4p9k4Ej5qmeffqKbVWWzpvGXD_9_2kpnWUNoN4RexY7Mr9_iyyh-G213TfdW8BZKNJEZH6gJo3tFytuRJadSOkV6YlqkxNbwu4p0wK3m3KC-uVHvRmpIV1piA0HIJXh-YLFfDNagozGr_G3SMifRPh2_hJ1m7zdajRoZWH1rBdhGgyr4JlSmFdixqEsWnkfK8kfMngYTXZdldWHQTIKNzh0hsevkMrvuZQCBQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=vuIihH9W3L2tOh6-FlPo8WUuKaz20wmRE64T26dBupdUKE97wWuT30oCKWrQMoXKfjX2iK6gylcIV75Zc1mLk1MkSaHec94Fh9r6n-alPOuEbMT4p9k4Ej5qmeffqKbVWWzpvGXD_9_2kpnWUNoN4RexY7Mr9_iyyh-G213TfdW8BZKNJEZH6gJo3tFytuRJadSOkV6YlqkxNbwu4p0wK3m3KC-uVHvRmpIV1piA0HIJXh-YLFfDNagozGr_G3SMifRPh2_hJ1m7zdajRoZWH1rBdhGgyr4JlSmFdixqEsWnkfK8kfMngYTXZdldWHQTIKNzh0hsevkMrvuZQCBQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHeULLy5h4SwuiXBucs6jExRBXlLaungIk7A4xDmjFr0G2QQmRQutrr2aPGP1AqEYvdF4Mm7IGgIekuWc-yovr7eqeAcTTUIzBRnS2TtH1Oo-UtkTbt40WsjByPtIxWQl3oGjrEhATQHAsAUs-9U6uws2VdKW8giD0MiPB8GAUl7ob-w6RCRn63gSShu1geWw-owti9_NfVvmO65Y9SioOQtN8rs7zm_8yr3eZ_8HVLbM5OKXMCk8OttRyGmPj7rM3zzJ-Dd56jJ9d7wQDwixX_zJlCpgDMxQ_d3TJKvBEf7cdvABhI-gA6V-3dLakhFEFC9ull334gb9XtnPB783A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFXQpTvoriGFC__WD5jdxyUGH95KA7MdWfpuzu8ebSnUqmrPjpGK_oYebJe-y5-EBouQhKkF-J8E2Wb80AeVet6_gUDB7czoBJbJCJopWkCdmwJMoHCADDWRHlCG4eirxYRt4gbsh198lm137YMyIVhs54j-52HVvPhMQMTreXQxS8DVsCWxRqDnG9GxC-Wk58NQ4ZzN1Z-cxQjF24znhXRd0_QtZ3_coIZs3Zbpo61w4yy5_WpWv5Gxcpgwbu9ewITDfzTn8cgtd2PextPK8Eat6YQI1-JtTzXBoKgQT4OBneKFW1cNwQqU1Kk8Wrjo6OOK0iIkk4nS-lZ-JFjxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFu4ezynmZ1gntcRBmol3xUfceZQpREfCV74NUF5T1C3ZAYdt68s0ribk3V7gKQCgxnW2YFgE_pZa_AZIRdcaRZ83osgHtS5EQ-qnO7_LJwpOfiDnGL8fPHTofa8iYr8OzfVNwRqoeAsAVoP4EZYDC6crZkAeheEScIVcVPpKSPkbXPuLNm6aKq9Xnaclc--HJ6bjB-mhtUAgxa3Ad4OO3c1bapM4USo_BTG3vGE10aTUy9LydB9VCdBsEznoyzvj3Dfpkz5yZ20XgNisxSjpD8Qa0302nuUwn71cA03lkRqtqxPvOD6Gqf4EJSAbXy9Rpceo3gbXCRRRaTigOpyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=a-qjh4c-Y4eltvfstnGt1av1f4v-bJLtP9wgstsYNlM8-P3tKOLqlOjkVrb6_V0TGpG12m3dFRuXxvDSkaKbaX1V55JkRqXMg2XFvCKJzTMsma05HA0AZYMWc_qDdujlkN3hqFhqmVN3duHgKqaw9tUalccJ0URg_yad_ztGkemID5Rm_l3BUPGM2lqvoOxnXpTeXpCPDoH5Gv2t4isjB8PWQdqT_O6VSuzCuZSvBXUWbT0a9lVumAbUV9ZK3xfOibD4SqYcshPqL9UpAKdsY1fDRWO0Fx0jERbwxEC2LbY29FkPtTHGqI2T0yB4AJ-103F3fOxV849Ap-P8k01Lo1yq3l2Iy-gnssVe5uPUPYIMA3hN8L0tzEVsat6Y6sjbxe-Ar-67xlmE5Ntxr_Zyj_4ZtTQ65JneFGRdePoT5PLTT4iwmIbR_vGQlhBF_Z5a7sMMPm66106cv4P3Yzlru42ZqELeVJDDhtUCN48-FGJMcnruhBlSVg_bk37HQdFntIIzCAAaDjtcYEQQxGTWYJyLonieVuxO6wd9ptFMKpXm99yfkYZGmHtAb9XAD0iMxH3EqysNLygoZ-_wQqv1gljR6TR7qAJQhRm8LcLpmJZcprWEP3OG0YV9XCb3vn1AvNWywQZqfijk6xKg3QHfP7TWfF4vDC4BhzpetJjkhm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=a-qjh4c-Y4eltvfstnGt1av1f4v-bJLtP9wgstsYNlM8-P3tKOLqlOjkVrb6_V0TGpG12m3dFRuXxvDSkaKbaX1V55JkRqXMg2XFvCKJzTMsma05HA0AZYMWc_qDdujlkN3hqFhqmVN3duHgKqaw9tUalccJ0URg_yad_ztGkemID5Rm_l3BUPGM2lqvoOxnXpTeXpCPDoH5Gv2t4isjB8PWQdqT_O6VSuzCuZSvBXUWbT0a9lVumAbUV9ZK3xfOibD4SqYcshPqL9UpAKdsY1fDRWO0Fx0jERbwxEC2LbY29FkPtTHGqI2T0yB4AJ-103F3fOxV849Ap-P8k01Lo1yq3l2Iy-gnssVe5uPUPYIMA3hN8L0tzEVsat6Y6sjbxe-Ar-67xlmE5Ntxr_Zyj_4ZtTQ65JneFGRdePoT5PLTT4iwmIbR_vGQlhBF_Z5a7sMMPm66106cv4P3Yzlru42ZqELeVJDDhtUCN48-FGJMcnruhBlSVg_bk37HQdFntIIzCAAaDjtcYEQQxGTWYJyLonieVuxO6wd9ptFMKpXm99yfkYZGmHtAb9XAD0iMxH3EqysNLygoZ-_wQqv1gljR6TR7qAJQhRm8LcLpmJZcprWEP3OG0YV9XCb3vn1AvNWywQZqfijk6xKg3QHfP7TWfF4vDC4BhzpetJjkhm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUk54K0Q4Qr-EBQgpahH1kJo5jemR7IF8dssQlPOrmTD4AnzvJ1miH2c4oTt0Wgo2-vAdk-37YkXPQMi95X1f07-oBJ9aqjFK-WO4b4ch24F9XWFh4-WxF2dhnaqlCleITz2ZZP6Tas7Q_9jHvjrE21mrSvOAfHnnKCUiSdYkbhxV6Vok_InEYtgj_9CMkBjvsHVglz8lJ2MdiaISCunOnsOlNiR6i8GviIWJS_NPft0yHL13HLnkoS3v-wglSfW84qnqqm9dzzUVYVBXezVuctXsp21WFJtwiogldNOxLOl_Y2ejIyE4SpsiBt-cjYHgQep-E646DTt7kcCpGpBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkB5Ef1TXRZZhSKrF7JVpnx97guMpa7LOPFzYAIvS6d1WB3MDzoVfhzCPuFY2qf82_8b7UNWbIGW_srwmAkQvixqFMf9idWbg7Cu9wJdpY07mbRP1H93gGdGY2-wdmOQwjeHFvr5WRfiI3-4nZuYB4DagO00wx-RUOHU1b7kqkHKNXPIKcXZjGW8HRq2gzUYCHKr_emJYtDb2idcX345FPE8UCPQheLfuWT5wLRMIfBxt7gN8V5mhZgKBRO6ulNYTJUGYET3RzqdeHwnvPXPqyajOXVaKBF6jCrMEHm2oHrs1gGi_9nMKVLFohanGJParo6n7wXioosdBSkOUSzvkroY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkB5Ef1TXRZZhSKrF7JVpnx97guMpa7LOPFzYAIvS6d1WB3MDzoVfhzCPuFY2qf82_8b7UNWbIGW_srwmAkQvixqFMf9idWbg7Cu9wJdpY07mbRP1H93gGdGY2-wdmOQwjeHFvr5WRfiI3-4nZuYB4DagO00wx-RUOHU1b7kqkHKNXPIKcXZjGW8HRq2gzUYCHKr_emJYtDb2idcX345FPE8UCPQheLfuWT5wLRMIfBxt7gN8V5mhZgKBRO6ulNYTJUGYET3RzqdeHwnvPXPqyajOXVaKBF6jCrMEHm2oHrs1gGi_9nMKVLFohanGJParo6n7wXioosdBSkOUSzvkroY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=jYHVYo0WTIEQnPA1cYizaQrVds3BijaDR7uuVAoAJ6RmIPHDPjmyFRSAdChad-_jm8vvr1M26BpCIams6oMVZE1D8jB1N6X1aeXSzF_xquFDXrXhJFdr-XLJAAI-4m9a5F844GbdXz27D3PXHmM5Mf8txzC9DQHSjLF-0ASJQd_AGXD1xDIOmKgBb01KtZ909bakFGM7ptvMpyHWwSOR9fyZTPWBMBI7q4DJQjvDgrrpBmJkVotsmAbIuk2hgqqD8eQME5p7GWV9wAEJO_TUZYC-6fa2usF9SbxEmJlHGNm6cIeoFu2SeX5L4TLdvrhKx97jeaWkG-rngI9LPU8pvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=jYHVYo0WTIEQnPA1cYizaQrVds3BijaDR7uuVAoAJ6RmIPHDPjmyFRSAdChad-_jm8vvr1M26BpCIams6oMVZE1D8jB1N6X1aeXSzF_xquFDXrXhJFdr-XLJAAI-4m9a5F844GbdXz27D3PXHmM5Mf8txzC9DQHSjLF-0ASJQd_AGXD1xDIOmKgBb01KtZ909bakFGM7ptvMpyHWwSOR9fyZTPWBMBI7q4DJQjvDgrrpBmJkVotsmAbIuk2hgqqD8eQME5p7GWV9wAEJO_TUZYC-6fa2usF9SbxEmJlHGNm6cIeoFu2SeX5L4TLdvrhKx97jeaWkG-rngI9LPU8pvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwOfTO1Qse7jspCNJaNSuXkdUrFLsl5uVVjVTrNS78lzan2icdO9E1l9WbZX_NkDPREp6n0_2XkdGQIjA_WeXgp2ZJMasAanx2OIiUVkBG2Q0XRZiVkJcDJem8TkLKaQ4PXxfkAFifEdX-Eb-o_zGEIw92-HvS9TDtxGwCKaimq_CzHLAHfMy3kHYCkhufrLbE9V-u_X5lDuO7j9lB4mmXrE32aEWvDOKv1W6AGZaFAnbUUE5smlDnkJNyDl2ePNTBhqDTGaNoulJYmZGsM2LV5vcd6HDCuI-6sKIbI2yJt3n2Qo6PccJs5fr6S4dpBtBDKhej7NN0NeRUb3EBvM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw-tuP_qiN62H5tmLE6HlZoJ0Nip-0CRu4jiLUVTT_N5zPx0oCJTvdjoXm3Bk1nPCUDyo6wAS0_rWCkzw118qIVkTkDWHgmnWdP9YHNkgGxk2PI45NuyZ7DWLcvLhbjQydbCTV9kvcai2S0RZMDQNy5ZgZqyti7PTpTpDmjVPtHzTNPX9q07Z5aH2Ympqgt21UZUY1vRDfNB5iVZNJLxrL2qxhBaQze1sUF6iQGeFgSLQHgjGxkX49ExkMNh3Ufz2vWbJLg8agnIMEdQ3wKEt5TC_ieWBpSb9LwFD3qsLsmYtJMSLnrpwP3uiChFcVg6gK1NTfwfZSXLuutQqTKQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
