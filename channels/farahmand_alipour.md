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
<img src="https://cdn4.telesco.pe/file/rwRXE1YMoSXfC3MCErMvgNjK2GwHN0_EXer3tsTz3_mxciHhyoE8kfc-KZA3-h3z1P3H3FdaFH4DJJnU_8DAfDFKQ6ZZ8sqzm41S_URoeYDOKH_dlgqo1R0R3X3nBlGHaM3VMvYB94R59THqH9_dpVY8EGFjMM66JF9xpkbW2NNH_sKSAMrninP45rSflDU0UL4tbc4OsQGs88TfuPUJanoHK0Cy0x4TOe1vOoL-OlCWSjQzt0SgH_wjUuUpLXLpnXTKCG1ogteTACxxo-qn6Y3SWHuj5ei3o48Sr3sI2WXPBBvaHKBk1kZUP74gp8oj0M2vKZPCKoREWKqDfyC8aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA5T_yyIkebjp6zSipKKrT8OrtsARS3Y5P5UQqsXqZQdiUYxeR5CtUu4thRTL4RJ-PpZUXPH3oi8t6WGaL-o__k5KAk239Sr0cRS6N_A67wz6CQ5QLuiAjyPYhVquaCpI0jScD77iIHFbv9B_f19iIke7L69Av_aIm146MFGdq52s_q_efk0ScjO2Zk2xwj3DNqbtKKta8irIdWWL6M4hCSOhQU-zAjFdJs3BBXbdqqxV9bEAQREoyv1L_ivy_3mXJnTz5pIuw1ToIt6VGyo9tb16ruMYyJGFeginwdJO4UumNet8L70YdScmwGYToczalz-bJBTIWKZtGIlXg1H7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVI-IOdvEAZx6-9-CopNdi5IZCOxhXNsw9SnoT5dEYcsf9LtT8Qg0FWn8moSQL__-sE2n0qhox37_dHUgn1F_IfWlunkm3PG4FYSvEMuF7XxdUof_lNIYqxkCDGHcLmnmKgPWmcEbjmz5i3FTWHacDdbnwFFGhqTmVOzbxKuYy7fy5lAQsXGQ6UE6oWFMZjzxUI3RIqZSvY3y_1IKMvtq-eRuEUJ7cmtY-TdqbvA-u4fsj8-q4qFKl3nRLLQEYfQrKKeB4rh3vvcrntoXfSsAbcd3tSj68IvWLIM55HLMm2AjaAZ60w_qR0XT88G3iZJkU2W7rAyx97I1X6YvIQrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b23JA1V-CUObD6TwsH0RRZ5uUMT3GPFPlu8-Ear75DGj3Dify3JlWq8Pl8-QxvZXuUgcw0tQb-3Hjt8QDWru6E6a-YCBxcDtcSptuUZWy8I5yHtbAWx5m6cRcP2WXFd35rF3YAZ2jw1fIwR11r8q_iZ1FbVInjo3zu12LOhg6uQqFHka6XRpBEB2BNC86F7q-1MCzjuqTeBHf94Ui8gTdFXCzs9R4KUBPeV4fQU0FnYyv1JQheOE4zzsFokjQ3_-rWVB4UagcPau8qToGGQ1SOKEfDbnAm_kZ6huOR424klAvZAD5pN2yjmCbJu2AshOo03ovnPRIKhYmCehAAI32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6alEDuUUbJz17nkLFUcBSB48Jc1tOY6w3djLD52dQzg5xxKQ-Vz53s4HwfDjDhhdabkTGDhuy_QDRYywW6jboRpVGRJW9GMrfl-8Jc8ci0Jk3WisWmfReFJyOfn42pVcnbF1S93QYGDgB4amNMqhIj3tOT2-USTdll5O31szKwMkYHK6QRwDUCwE0pvkZxGx5Z5U9K6sU8sVMMnx_OrS24lRngkByX1xCRgapHIGNbwrOYDq9kCCpSMUO9mM7YIboptDtG5niAYdtBmXA1r2kE9ur6sEOW6FeLSLUqEc5VAVX5unKCRjuDLkB_-sTd20KbeowMCv3ROCZKtUKvBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=gDNc7_F5-n6hADoNcveppUsm6ENhSN15Tp6PyRWMQuC4e5Anh9nBUQRaaZkirZogXPLCKxMMSFbwCx-3vv4-jgWRhqM5J5y_OtvQVn7iri14KCMC1eBURHoXM4WZRzgnphlSnExYkAqBWk11_ybrZF8IghpCGZcZG0zusU7aMJTPdLqtw5wUux3_sSi_EGcEiByznAmTGEwp15TD5l7K-q8nCWEL7OXYpGsgGXcI9IlA4tztpXHz0_AnLXW0LDpNY_bqvtCTj6KC6_P-Y5KHZz9IxzVKovxf0RypsRIMsfx8yobKSQh78F5qN7p6XJDCSUoQFfAKgMNMtuH9MtPHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=gDNc7_F5-n6hADoNcveppUsm6ENhSN15Tp6PyRWMQuC4e5Anh9nBUQRaaZkirZogXPLCKxMMSFbwCx-3vv4-jgWRhqM5J5y_OtvQVn7iri14KCMC1eBURHoXM4WZRzgnphlSnExYkAqBWk11_ybrZF8IghpCGZcZG0zusU7aMJTPdLqtw5wUux3_sSi_EGcEiByznAmTGEwp15TD5l7K-q8nCWEL7OXYpGsgGXcI9IlA4tztpXHz0_AnLXW0LDpNY_bqvtCTj6KC6_P-Y5KHZz9IxzVKovxf0RypsRIMsfx8yobKSQh78F5qN7p6XJDCSUoQFfAKgMNMtuH9MtPHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqcbaT3oLtfoTtA-ossrFzlswUQWFSuyWLjoUbmycqkrCFNBbV1-UCIg4Z9MBnexn0JezGXyvQCGoXpv7OSgI8F5-s0X3GLEEY0_z0xQeyeX5_eqh3gj4D43Lro14OSqCXu_xxv9Q30ixLjjp4J1oZIdvTDgH0kTepNtBgcwIYVKTcwwlTrQWsW58Fo6d2jZlaSACs1hUp_ID0VxPIyzGy_nB8Nc8JQy_EFQhAdWQJsc4nWgW5Br941HBqdc6dyR_c5QjspyTvHH4c4rySCYWnF8EkX8JTiZioAuBOOAvIUM3EI8ym5kHzSw38jvzHBRaY39Iq7ISBSCbnabpVUd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sDYq-guyRSP6Lt4S1FsZ7_nt9rRZMUuzjvo2SvyEcR8hAXUL8MHCINtkycC4erJ-hRK_0sqfl2uDop_6Aoi5BTVMS1wfm2xmWkpTADWHD3kuuWQylDoC3bUngVHLSk87hPY35tgMFKKLFKgOAD7S8RzCk_adtcUgPDE0a4EFBnhCXaESoNlBa-UetENeTdVFxO3idNMWZ7aPbJJosJK1rcXb9erI8Pnc7DFaQEcC_PsGV33HmgDXJILyvu7CuFsVHAXs7aLqZ5VLn5zvhE3He9nE5j4jdmi6DowjrPqRw-Z2dhPMPc7nmLLk-04yvnJzjfMtWM6KlSOuBVKTd9N3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sDYq-guyRSP6Lt4S1FsZ7_nt9rRZMUuzjvo2SvyEcR8hAXUL8MHCINtkycC4erJ-hRK_0sqfl2uDop_6Aoi5BTVMS1wfm2xmWkpTADWHD3kuuWQylDoC3bUngVHLSk87hPY35tgMFKKLFKgOAD7S8RzCk_adtcUgPDE0a4EFBnhCXaESoNlBa-UetENeTdVFxO3idNMWZ7aPbJJosJK1rcXb9erI8Pnc7DFaQEcC_PsGV33HmgDXJILyvu7CuFsVHAXs7aLqZ5VLn5zvhE3He9nE5j4jdmi6DowjrPqRw-Z2dhPMPc7nmLLk-04yvnJzjfMtWM6KlSOuBVKTd9N3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJpgCcFWlJbvdkNstpN5iA99PNUT-RTQ-vMn57aVuyIjYC0QLyf2o-hL3UOSbqZJFuKY0yxud85o9UhOZ_U4DTs2M-axss4-EtjYqkth9imkYdG_tWaMlIM8x-mSxvQJhkEYJenOfu7yCr8wEJJhQnrjFcqUxO8455PzNCtPvB2zIw7nQGmrzHy3pbz06Q8-CQGimYKeaTO9Kup2Uf8EgkODm_kNw_ataKvWTqX6cTa6ZjitcWlVJcNLjQWLcJt30rtCXQFlBfZsJ5myCdp3dRtDlZusWvVRHWDpvwPk_LgeJB-cofaZ1VSeWgTvhEyfmCQQA485ErNXjZWthQ1ntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtgvM_6s4RvbTyBgrWiaoeJq08HVp9a2ZBNKCt7SA11EOB_7NlOsg4-Wz-4I_88WzPmcNyyVFj9SEvHgxNbgsV1nberPPN15PK6EnQ8FncZyXVc-FbA-GiPtOxObfr38ORvLFtS8qT5mMn7bVbPaEX9WE-ORASO9yOf-gslfVFNhz3bn4r8nadm33V76iL2-rfbGGNlG9H6ERpVMp3lnCCN9iKbepYUOAlQ5pX8Uz6teNRJsDVByUcWGbxDLmcD7moOoJcttGpMRir6k1eB2bJT6J5Ep8WxTI1FwsPtT_1Gb9AYvMYOwlqVlP1_44IT-hlpXmeN7yitniutbU1b2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=vEhXxpqLeyoZQyNwpT01cHwMT9fDdXbpv1rSR-StQPh6W_fxhWGKsVcvnmmvDYJMDDkW7FcpM370yRDueaL7hQ2krrEaKIA-a148lwgCjVkpkZFxuYoQ_4BwzQPoCbFbhRQsNLcXtDkuIAwiHxnK0AqMjcgvZWJkqMxM3RL3v5J7fRwG7iXwVs58kpaxeGcHzbytw3HLnislsYEnWgphJgh7_2d6dDTGDYau4KcXSNaraii0bea-Lgt6ZUtZylOaS5bq9StU3nNFo2_X7znfbAEqwsR2qooNarkl7T18XO68ffCTssFPgL8I9Svo7rrinXBukyopFD5CztcvxpZouyFTZROevgOAGKXB10BfrvSDIjEic4TYlyNVzLJ_GSFRhqxMxSjJIinUi4u-_KE-3E56n2SX4l59lG7iiSCPLB6rpEH8MDsICfzMLho8T2QLAwP9R3ppy2EpGpS_lLs8YztKcRsvCfAUHh-FisozkPyG9fTqPBD9peNgahfzFpI3ItuYtiEPcH65MtQOUSQKsIeyFYSQ-Aqwa8wDXv8myMGHpuFcMNKSxRark30xlQwOqVbYPPOKfbQdvGCpopzN5u0LqsDVa-82mpinScEhU4jXc9eaV4MJ0wpYHPBv9GSVQMOKcwLLTnFKZUROCeXERgK5uWmG0uefgTv7Q1rabEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=vEhXxpqLeyoZQyNwpT01cHwMT9fDdXbpv1rSR-StQPh6W_fxhWGKsVcvnmmvDYJMDDkW7FcpM370yRDueaL7hQ2krrEaKIA-a148lwgCjVkpkZFxuYoQ_4BwzQPoCbFbhRQsNLcXtDkuIAwiHxnK0AqMjcgvZWJkqMxM3RL3v5J7fRwG7iXwVs58kpaxeGcHzbytw3HLnislsYEnWgphJgh7_2d6dDTGDYau4KcXSNaraii0bea-Lgt6ZUtZylOaS5bq9StU3nNFo2_X7znfbAEqwsR2qooNarkl7T18XO68ffCTssFPgL8I9Svo7rrinXBukyopFD5CztcvxpZouyFTZROevgOAGKXB10BfrvSDIjEic4TYlyNVzLJ_GSFRhqxMxSjJIinUi4u-_KE-3E56n2SX4l59lG7iiSCPLB6rpEH8MDsICfzMLho8T2QLAwP9R3ppy2EpGpS_lLs8YztKcRsvCfAUHh-FisozkPyG9fTqPBD9peNgahfzFpI3ItuYtiEPcH65MtQOUSQKsIeyFYSQ-Aqwa8wDXv8myMGHpuFcMNKSxRark30xlQwOqVbYPPOKfbQdvGCpopzN5u0LqsDVa-82mpinScEhU4jXc9eaV4MJ0wpYHPBv9GSVQMOKcwLLTnFKZUROCeXERgK5uWmG0uefgTv7Q1rabEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdTfg5Eb9Dy1et9Pp7fvrywbLQ-qn_7algk7E_0gB9Rb2Ymwa0ZhMkTov-U6Sv7EsAqC9opYf3FYN-8cqj7y3xuS-ilD-R1AO4gblFo5X4hPAGxBBX3pd7ONPfwcyqKfwrvBHOZvTIbFUfx5vkQx-J89VlXS5GNVYA0PK5Dmxk7MWDUksykSeTb53n886OCPtifxAaARRvaVAOMtaD-hJV6Cg5sICVLBA9yT3BN8FsBG8ZLZaHAqLT7eeQTkgPLHvfpTzyFlKfrTpExpvKQBlb1xJitQddvBL6FFDtOLc7V1ZLeV4YIuCvfuNHe3xjr9biwHunj0q-r97jU6bTem6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm1DkW6OS4XedHbczr4Vewu7Z4PYVVoSVbhCoxNNdhVnJvo_XYFxdpLu9fbEm_gF-TROgg6KIwvnwC_SJ4BP6Gj-SzUEYvOM17fEw26wsSVvomKIGbUV1WA1zHLqUDR5G2_7lMqy1OWqua7oAWHaQeJ2gM_O3xmd41g7g9j7IWR9_yNK6E2v6TR1UcVw5GWZvlpsMcO6CRVnV2oZFMHaDdvF8HMGoTMZ-4HxaKFTr4HCHU6KgnyXAtDpJJsgUBIWvQ6zi8JLxhQqc-ePKdGh4HkhjcQs21vyGEuK1_4HqIHuvmuaAGkJ56yZ687Q6a4XXkgatrpF3P4ebkS63H3_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=jr8NV_qI741KZOtmjDfG6vlJE7ik7AEVbkBnivi32BU4egqf2rh03AMv-4162gxzjojKkLAUAfheIH8gZagc6Gf2-TrU0TsafYz8Wm5MfRTFb0gS4z2di5DfVhUqv0b6_UfPP3hM3vyusRlct1rg8MhsRYEfBr5ucpRvJNqgKIYYnOSxadEQBCQg_snTytO-P8YkCb0A5KV8NWsmCsggVHRMLMh2_SfZOlfqh6Fl2Kkfu617fwGV22kNtOIcLzFtWrHXw3qXWQgxu7crZVfkn0U--sTOdw8H2CwRgkNwmJjZNmk3ig-gKmK0tE0QNSXVCeeg3DM1reM1gIOZSj0QDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=jr8NV_qI741KZOtmjDfG6vlJE7ik7AEVbkBnivi32BU4egqf2rh03AMv-4162gxzjojKkLAUAfheIH8gZagc6Gf2-TrU0TsafYz8Wm5MfRTFb0gS4z2di5DfVhUqv0b6_UfPP3hM3vyusRlct1rg8MhsRYEfBr5ucpRvJNqgKIYYnOSxadEQBCQg_snTytO-P8YkCb0A5KV8NWsmCsggVHRMLMh2_SfZOlfqh6Fl2Kkfu617fwGV22kNtOIcLzFtWrHXw3qXWQgxu7crZVfkn0U--sTOdw8H2CwRgkNwmJjZNmk3ig-gKmK0tE0QNSXVCeeg3DM1reM1gIOZSj0QDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6g13iRLpAiDjPj_wChLK3NyPiuZ3kOVq1rkcXV3FQQa74nq2jSET8MKs2n87Q-pJHKyBEgComSyOInB49i-HL6CCY2hRM3na72kRF6-2CVUwjXwH0eZE7tKOrlWhwER0Uy5jAnATQrJ6n5NvT22cGCpTgKzXHcFPCTIKvDf0rqyTdkVU79Kg7FIXP1CMpUDITvfpc_flk0u73MDA9fZ6QQkKmUn40SUzSvOFRKMKYl_iy4Y7zf-PH-awVyZ2KLKhZy1XN5JxafLSqnKEE1yECFxnxXesipQnLJKZ8wEaC15hyuxSyG86YBVX-Ram2ZFep75Kqc4HC8vVtrv9cz9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqrvgLhUpC1YWUWXdsZoFLrv1RV-_mHZTho7mB9OmtTByllbBLS-zSJCxsM5hOD41AkoBPTwOk3l8eRYajAhyZzAu254jzHoFfKao4ZCpRHJNGVM-7piBYSGfHb9Mx1YIoGi9nr0iGEigKKUsHYtPim_9166n5o27iKDk62T7RGFo0oy2BjBjrJAEU0f0Jw8bVVZlVaQw-JmWuobVI8TBZeXXGm9BA7666GmuydY_w7-Sc6hJMSInVS9iuz5N5pQG29IlF1b_mRTn2igKcgrVX9wcTpkx-LpF9ObBJByVFmJGxEBnQ698liFdOuvmbssVMXx0AKDFdYCxsJSzFi6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKQjmqf4KJwpLR3Te0x6GUKInbe4n1p-t4ovDXuGWomf_X_kR1-PvbkBNyv-SkJmc7NZL26a9BhcCa7HDJTYfeZ0v58DldssRLaXvw4zlXBSlrCh13V8-SS2-H-OnmxbtIG_9V1VwND0HD57Rb323KvKORzjeZ0k2rXCDSYIEfJ_kFm_8sMbOpuoaWQVuAqbWwzLJwGoSJKFLc7t3CUBM0gp5Z64ftxrrbjtsjl18TwbOXZ5xGdM4PeU_tXWnV7o348-Tw-8vjjKGJeQD9-WIDP1XEXfRmWOnEW7ihnFi2ogSX69_1Gz7vS-FyewFReipQjLAQZf3hqoDz6UnMuA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7bDm-JKjLxaVL3ss14JgtkxeTd_dDQcbn744mTWbRSMzr4rurpccC8bLgLR-DMF8olOBh-oomsNHwgdQB26NlLQUw8WZxSVqihxkADv9TJ_Evq7XiPWDgpS11pdnMB_3LUHwTbAib8P2Tb_MKUelnVpEhyXnxhSge7BfSSHPHZ32mIsoM62Y7T9vWOWUeuOKjgIgmlfiPTUS99DhQyNOooXEwEN43aeIHykNgSKTUTJJD6U6hp-VJT04x8HxGlf24tKuBFCuUn0JvX2Fk8agbTVgUkRyPJsD8pa6U1JHWthhaDvRUSuMWX_6eUxnGOUrGK9EHX-r1rt1EaYBST9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwlPkHq6I0wrZ_MiGsc5cgcb34gXjqSgkc9vPnOXHcJl9PXqTJX1OXgRh47G8RTu7wEvsXabmEI4II07D4EMUH1yspTX4khlQyRr1ZSPpRuzh0UkUCxNZFS68_sX-gt2E-k3NbQXNI_1LVn0GORv6fms1iMX-dEuAmgYPAE7orVtYx4d87cpSVkcfvxknzt8PWYKBzuzth09-RbDOhRF13wIWiqSxmo8T19gZQmUyhVa8Q4uuI-PFhNW1WDjYtKTEtvacMK5v8HtKkO4xzF-lOI-Z2cn_hKM8hbE_ayN2FwDLxPsAQwkWAi7ybdFTdceGgRMlQ3PyEPzU-ZhViKVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObvlLhFGVpIjKzR0if1LuQrniWHh0bETudVCCpdxhhRTOcGAbhWPAnVsZi2qtu9dJZgQe-H4LMuz-3L9XboOsJpsHcqvHFelerFQYVNymLdlP65rdtEQMDooJEx4YPTDNVR0YiFumMcJVhc4Fcb3QD03iHkIkQbsD3rB0xysrpmBftyAvJmX8nEbltSWEraBvEkYGkkN57hurWgT-dQEKCFk30x1IxV3D21j2HofthhRnN6l5QveDd9Mo2lked6NuUhjG7AWlir0LN6utr3XbMRDnPXZEsr8I-WQLrajijY8jWUYMNAhKoFN9ytG2q2fbv25ug3s5381PIpTnfOarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpB2OnBr8Z-tcVDwIimUNtalsuhRwONPvnejdicLbZgCF3cZ7jvn7hoWeDklawDZUQPyoE8GdWChI3NPk2jys-uVDW17NQn7GcvGy7MUgyG7Xg4YTXKE15QxnpgWhsOlIg84XD2Dhtjkt2nYQRzd5rsGvVzBK-MJ99BaI6woNn03pdoyMoB7BDTW-A-iWY1REMFAW6fLh9-By9v_W9sStaCPjd6cvq7NN7SZzF_cnHpv0eooM0iQ9KdVTS2dTtUvQMi4dzdwK9-zDgbhCYyrGU8JuQeYCmsPY3hvy9ThD8GKiAkOuyy_QNFegxrtvw1H90pBe1ZWzDXBatXFSAeGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDYq1AB2MacJ5EhtQmE6R7Q6ypS9feRPpxbtmL2mIBUn33iaAJJF38bE363jCnyzaAeGkpCNb5w31aHjNSCDqgUANN3GeempDKPkkJsB4jGkIVtZqVbq4RlX0Oq9tzZbRLl0WUVfzUtu9ARRU-fgd6eyJKXmIjt2WL8naTK0GlmkC-i9yV8h_DWEh26fpyFx27nDxe19HY9MgGwuxSVPJmK9ubK9G_ezSSKS6hv32b_TLvkR7wcAp3uXsWTAkK14Le0axQogOCjqV5TSn_085FUw0nAks2-wb5ei7GOtY84svU1ADcH8-ykphacocR2DUZS6z_EMgk-L0fw9x7iySA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=rHcHTW4VJpxycgAisyKveWD1ER4ipv3erVUE_LB2xSukOv6sWH2AB5_yMJVPUJFE8g8b0vp2J1Xm30CzkU6HOQFpxosVEb8gBc1_xgaMkadCcB5w7DclOp7TpUggNhR_3eLKF9KjQYzuHfdzsjRKuvayABn2227ZvCbcIrw6KREkIBHzKcfM_Hz-XhF5gesRl433HzFBhOUNZxOUOb0VqKRY5RoQCCgjUZhmeouwRln98OIruZTbYumVRMRF3JKSTCfB7ybPu14c-8KLaVqwVL69hZOY2pyyHhMVOvOa5ff7bTA_MpAPs8WNio8CgK8nDR6zfXp3u4lja-RFzHDRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=rHcHTW4VJpxycgAisyKveWD1ER4ipv3erVUE_LB2xSukOv6sWH2AB5_yMJVPUJFE8g8b0vp2J1Xm30CzkU6HOQFpxosVEb8gBc1_xgaMkadCcB5w7DclOp7TpUggNhR_3eLKF9KjQYzuHfdzsjRKuvayABn2227ZvCbcIrw6KREkIBHzKcfM_Hz-XhF5gesRl433HzFBhOUNZxOUOb0VqKRY5RoQCCgjUZhmeouwRln98OIruZTbYumVRMRF3JKSTCfB7ybPu14c-8KLaVqwVL69hZOY2pyyHhMVOvOa5ff7bTA_MpAPs8WNio8CgK8nDR6zfXp3u4lja-RFzHDRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=e6oAfD_xWcaYnSBqB6agqhFD_5ae562Rtc_Yef1lF1s4WRJ8th5eoW_NPtNXYut79iY_snft62cyTcXg4C6BVfkjuL51_Ozu8Ob-Q7FQYJNjPjRRu2X979Ewf43sz9nF8YzkDaA_PNBX8BzcZv2jMpDhsi7GVlAcvUU9hoxZv9B1SO9sH0zgWi7a4II3U1qoz9eDei_kjroOws-BxSvCIO3T3YvnOCS_CIUNC1DTWK_XUfg3nep3OSl4xOsNGoqMVFqS8VCWJxoGpnG62nAZGA4v4Ef2N1lmK9DUPNqemlJGiWXgcQ7ws6Bqzjo57eQncIGf55xc056Of968fqgke4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=e6oAfD_xWcaYnSBqB6agqhFD_5ae562Rtc_Yef1lF1s4WRJ8th5eoW_NPtNXYut79iY_snft62cyTcXg4C6BVfkjuL51_Ozu8Ob-Q7FQYJNjPjRRu2X979Ewf43sz9nF8YzkDaA_PNBX8BzcZv2jMpDhsi7GVlAcvUU9hoxZv9B1SO9sH0zgWi7a4II3U1qoz9eDei_kjroOws-BxSvCIO3T3YvnOCS_CIUNC1DTWK_XUfg3nep3OSl4xOsNGoqMVFqS8VCWJxoGpnG62nAZGA4v4Ef2N1lmK9DUPNqemlJGiWXgcQ7ws6Bqzjo57eQncIGf55xc056Of968fqgke4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr5pJoivve0l8SxZN0y8bLd9k565Ejox9EfebLf-cP6Q2wDuKknsXAHWr2g9_uI2meWCd_XTfA_5gtKAeGTRhw-7uOjuTt0_Q66nyzpDdXd275rcgTri_lxZoekT3enj-SKAZLaaYz0srFaXIlyQX1-hS7z19J9_EMFp9TadklEErh6AWX18DRC6rOG-J_9tcFr_gtgXOPChQAa5NcUf4I6Nf834zwvwdTgMctISLZh4HS4oSCswrzFtVUsBVhmhX2grXEmH3qqnuY_-r2TRrkktKh0MIfLu51Tl5LDDyLBXKNUTI_1W9ZngodxTkyC7ZOHtUQwbS4Ahmt0Rz71ZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S01zp3si0a1fM9wTH-Ko6SJaYVNkiEOcriaUnHZbWzwjkZdgTOq9FD-MhfVV7lOewvdM0mQf1ylz23iLJLpr_RRTSwsQwvQmfyzxAOEYHYZkbFBVyfIfCfdnZoyuR4bo37B0nAGnBVV-mMVPK7_2xfJuLXGn8-SFbcvZQB-eY9lIBo3kQalWeadmJ7P7h3CdjxHt-N4cn9XA5vMl28TQRuVEvjoDHZrGJ0qSfV1YtlaFOTCKHguWd-SDG00Qy5fd0UfuQ2kMwfLmg6DGcS1-0t1r-JSKzyunMf8OQVEOS9teNh3q9j6T2VG8SvktqzC73lmPFz9Qvoi-OjuH_QSlZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-ito4rR8oVizISz5sHadvBdKe-Pd5xlUtpLAipfoSJvmgZFvamw6G-RPWIgGUTzSOrG0w0pUp328siTRbJuuUKEspVZEFsQiehfyHxuI6I-LF25CmcxANW54KlbABHXIhRK3GysBOBDXTrxb6d3xmsznL-0m6XRV30WCKRCqr2X4OEK0SqJkPw5BV9sAR4JXzvz4FSaYOt_Hujw8QnzDznW5OM4xaBnOkgTkgKjbZ1GwjcAKY2yl2saKda-NNbIUOlJ1UNrqFjm-d-WoR_uaQMXfsS4Es7kiKR1QVkxbvcSPXj9nBg-1vllvUKFs2TXGvFHcszRX1UzxUZ1baofZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqlpnlu36xIquyE13Y0RJyBLTCr6taupy2xX7bA5uLQIreo5V1cBNg6F6RE4ThKvGNHu2B0UfnkdNLfmNP5uv02Sd_J4xA5NgIflhD2-j1CaBOEkcjyDVNFpefQBkfZW66DSyXn8lwQRSJhDMUdwxrOJakGfA2MIfzaWl7_NqB2nNp-ON7g-M80Om6r7logEtWdNmFJWiOgbtFzwUWEpbqMUH9vSjpDHr38q1RIgo9SrVlbVDOoqVrHP3dRoqs0cqZPtuTavXIN6bnd0Jik9q2db2xwKgu25TarYA02Bw6vrU_s6NpKNsqCeWbOf1sIQrPl5G2aSnmvOLFjsncBYTcjbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqlpnlu36xIquyE13Y0RJyBLTCr6taupy2xX7bA5uLQIreo5V1cBNg6F6RE4ThKvGNHu2B0UfnkdNLfmNP5uv02Sd_J4xA5NgIflhD2-j1CaBOEkcjyDVNFpefQBkfZW66DSyXn8lwQRSJhDMUdwxrOJakGfA2MIfzaWl7_NqB2nNp-ON7g-M80Om6r7logEtWdNmFJWiOgbtFzwUWEpbqMUH9vSjpDHr38q1RIgo9SrVlbVDOoqVrHP3dRoqs0cqZPtuTavXIN6bnd0Jik9q2db2xwKgu25TarYA02Bw6vrU_s6NpKNsqCeWbOf1sIQrPl5G2aSnmvOLFjsncBYTcjbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Tz5fmcuAbeRZZy7pTu6caBrKzlbTTWhdoNOYCYyjSdEevgE6yF_p6Nw6eyQsO-0Svs2Rt326PGYEyvGaTlJZlz6kY_7jEYIgntlXQupHsssUXEu8ZR-1v4W3JFrdUlcXLOUc7AzLVqMw0txFdtfzwxep1x3SX78DOqJ8vTsCyfJJhQKRH0MbHFY6Wb6yXDzFqOkOXasKPG25araCDbmCDhD7bvM4aWlK5I_vnYin65DN3LCTDytcK-eSfGNzvBt6zPW-nh_WRZUr_J2kOQl7zRAJYoPexyExPiOzQflVdxnvubE8SrxH5gAygYCtyMPnHfOgSYxS-Tx-mI1Wr0PLPJvxcAFP35T2a-VPCxhrNCGoNj2RhuxqU1_EroI2LZTNWJdVmQKk4Wdj48ot7j-LBv76DtcCxyHOpVHXVBuqEUHE_rmXtvvwNfeqWL9122wswdlMKQ5a8lYf4gwp31Om01FbDSfZxdQRUpPk49mt8FOUqcpUNm79Vy_TxAneYdprUoWtwGyGUqiuFQZPDCYu9vfKXl1yDtSqowxqVwNyhkW6nYtuwpBs_5iyYb72krOg22GiOpwbPwUkqecCIyLcawShSrHJtIDeOxddLFh5FBtWMHj0OZyv-XxHC9-tL2pHVRJYICLfpkqUAPXmAJAaYnKgWAuYepHUsdEY5Zm-rLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Tz5fmcuAbeRZZy7pTu6caBrKzlbTTWhdoNOYCYyjSdEevgE6yF_p6Nw6eyQsO-0Svs2Rt326PGYEyvGaTlJZlz6kY_7jEYIgntlXQupHsssUXEu8ZR-1v4W3JFrdUlcXLOUc7AzLVqMw0txFdtfzwxep1x3SX78DOqJ8vTsCyfJJhQKRH0MbHFY6Wb6yXDzFqOkOXasKPG25araCDbmCDhD7bvM4aWlK5I_vnYin65DN3LCTDytcK-eSfGNzvBt6zPW-nh_WRZUr_J2kOQl7zRAJYoPexyExPiOzQflVdxnvubE8SrxH5gAygYCtyMPnHfOgSYxS-Tx-mI1Wr0PLPJvxcAFP35T2a-VPCxhrNCGoNj2RhuxqU1_EroI2LZTNWJdVmQKk4Wdj48ot7j-LBv76DtcCxyHOpVHXVBuqEUHE_rmXtvvwNfeqWL9122wswdlMKQ5a8lYf4gwp31Om01FbDSfZxdQRUpPk49mt8FOUqcpUNm79Vy_TxAneYdprUoWtwGyGUqiuFQZPDCYu9vfKXl1yDtSqowxqVwNyhkW6nYtuwpBs_5iyYb72krOg22GiOpwbPwUkqecCIyLcawShSrHJtIDeOxddLFh5FBtWMHj0OZyv-XxHC9-tL2pHVRJYICLfpkqUAPXmAJAaYnKgWAuYepHUsdEY5Zm-rLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chFO3O8_5oGKLAEgwG87a2_KScma4VRLbfWKE80hFohygERBrg9sDzbWpIhLWy1xIpf9lO23Dj9f1cYjOfC2p4FvllxsTvuEG7C4UFMo1nQeaXoRaQcnKZyup3wAelYPJNxDvY3U0hvBPVt_X5djSr3CSQwXpVLqP5i5ZOpt76TG5RE-EZbI1LPk7wkSau8xN5qQ05zkdJdzhzVEVlvAF4hA907WvSIkIKgJ9onECRjJidoOu1G95BJgyA9QEtUD9P9t2baxtdyKF3RuFnKJKuFAFQpf9mYjzS4MGJd-0oXI5GMzZ3sAm0ctvcV-JAq29AflbCC0Cb1Sx7eAuvefkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwk8BZjuJkVQrxOoWdkeUUpaNqCUgtbbe5S5aJ9_z1aBbodsyNRyvXMsmZZxRMIqSuB9AnLnrcamSEDLve4nq8mBCYGUmjyPDDHja6mOWBEHMuguTTGMIwl-ghokkxcW8ga51aaXgK2IqnuoZSD5bkKxm0u4u-r6oPoWSEqvS6tOEyx-PUHJHD727gxic2CLLnM9EeWrpLs0T6yb8-oFlJauJrMLZ904JwtJ7XABfzgX5_IV8r2lpINg4d4sxPllZ-SNGYFI0RlMcI-bKYWTJ46yrZSdi1-7ima4Z2T_CykRkU6si4Buq1DCvV1v6N5K6QIq80jLVCHFBLLsFHVx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYzjHSoDfC11L2NUaXM8w59vILa_IOEglidlZ72qcKNE8WanYDS5-XnT8m0vz3LIwtjYJ6UJTwaJdCIaKTQ-br80lC0exLquKTqzqRuiVknz919qMjQJAqmBIBkqPIRmdnns16MSdMLtBxSJvZstoqkacAULXwDZi1Z_xxo4pAPSvEeFdbbP2HeIpJ3tlMKJgtECWxKFcbnwnhbDmYXJqsr05XllAtucX8YTXF1xvrwrOTEEAFeOaZTjDQTUMMzO3U0aWGKRqTHV293iwyW-96ToTQVlkqdigIHYeFZkhUMCo8lHaeeGLxNqmy6LsEHCH2i_Fw5qHNw_t3sjK96F1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=Rblh0Psw018tLywUcigQIVZ9rXPGnvTJ5pOmnJPQ1wb1gNGRXC-gyz7aw-4lKftzm65vfV-WK_w3P-cSlLwPBH_nItCGuWkcWbYDtkrzYQS8pG40-ThjxvZzQtz0xi_3ob9-3MW2AEQHP-0PNWmPgxDMMuyJypAJkDT2kBJECWWH2sXrj2cdHIlzac74jGm5TakwhwY5o5t0Cuwwbn0IIzWDt29swP3eLeMbGas_GbXSZ9LbNjd1nREnHgVsRbAeP-9n0ffZ3Th30yO0ytnQadC3sH5fGkWTuoaTdePtXBe4OM0fFBptqL-j5Bjp2ZHbtUz7AkAnoMMnRCZic0pamQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=Rblh0Psw018tLywUcigQIVZ9rXPGnvTJ5pOmnJPQ1wb1gNGRXC-gyz7aw-4lKftzm65vfV-WK_w3P-cSlLwPBH_nItCGuWkcWbYDtkrzYQS8pG40-ThjxvZzQtz0xi_3ob9-3MW2AEQHP-0PNWmPgxDMMuyJypAJkDT2kBJECWWH2sXrj2cdHIlzac74jGm5TakwhwY5o5t0Cuwwbn0IIzWDt29swP3eLeMbGas_GbXSZ9LbNjd1nREnHgVsRbAeP-9n0ffZ3Th30yO0ytnQadC3sH5fGkWTuoaTdePtXBe4OM0fFBptqL-j5Bjp2ZHbtUz7AkAnoMMnRCZic0pamQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL6E0soerTPxg73t6NBjvJ-q8Nb4McFDITxqVvMnEJ2eVrmiSOxiAe2h9R7mVt7aGG4wJAAm6DG8RdlyqgWQVXZH9Ooc9Xe2fGEkMtbHCoLWuUcWKAqP6viYpez7R7cQRUdefdiSw4AVuMnqDG3MnQ8A6ZAAhtjfhdKPVLdN3RqZUdimUSxBxukbPdPOzvet1eqDkxQm1simL-gWSAF5qnAPbsvctkwzbeKbFtXELStrVTZ6VUjI2hNSDujodR6YC2alM1Rv6MHKiT27d50OpWcFTghAlBPWbzqEB-9cO7HXsTW4ECRh5AkRJgYwuisNNGrz51lJbWReb-OXZW7lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=ZSfJ5WCem_tCTr4pgtn74zk9FJIZ7jlwHmlxV4UBEG9aEki9-fLZrdHFkqmM4NX4fLu6CcOjS4zpqKKdeJAguU8CCFuW8NT-IQcaV4Z5CS6mnMVcYxisnm22gg8pL5u01VIxq58Z1VNvwnmxXtyVisAUoiDC2eSUkAjLfqkcFhVKt_xpN1s4UtDpMvpD2vy9Xs_k6UjLjtFwIdE2YiA19dHDIbo45QQlTxX6sEayJDga6FiTyPy5E3dw6kKeQ0Jwdjndpgl--sY7FMCOEncxARW0p2kPpIXCr1N19f9BH-WON0erF814kkS4An_eqQc2UflO-J9M-CQqQ2f9mcwwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=ZSfJ5WCem_tCTr4pgtn74zk9FJIZ7jlwHmlxV4UBEG9aEki9-fLZrdHFkqmM4NX4fLu6CcOjS4zpqKKdeJAguU8CCFuW8NT-IQcaV4Z5CS6mnMVcYxisnm22gg8pL5u01VIxq58Z1VNvwnmxXtyVisAUoiDC2eSUkAjLfqkcFhVKt_xpN1s4UtDpMvpD2vy9Xs_k6UjLjtFwIdE2YiA19dHDIbo45QQlTxX6sEayJDga6FiTyPy5E3dw6kKeQ0Jwdjndpgl--sY7FMCOEncxARW0p2kPpIXCr1N19f9BH-WON0erF814kkS4An_eqQc2UflO-J9M-CQqQ2f9mcwwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYdofGBzExgt1j8c1aQLjruwddg9C1qVdFGoIGgI8bHgx659-1WD91O1C8ECb5AsHng42KeTUoWimydzf5qA9Cjy1YyEtEb2_hc_gq4rxiqvSeRIjCRLBJ48gQvIj3YejDwC0x4OZOBDe4jsy3nmxdsZzKSOL4HhZ_hlBuv1V4maBYyozPV8GT419Jw6u-KYfi3Fiuy7g5gKnRj2YOIVfZ2RHnwFfN2A8RHf8NpU_7cfv2cnFZ5MN7KtSfE509Qjnh0flnMKFVtzgoTGzzqNlwV3U0ofczhsGc0nT1ss-BWmnObTr9bp4awp8B0QiR5n8kTTE-yIlTOQjs8UN970pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzIqoQCmhKc-Y_yiraZKo87Wz4BhYRwdPeAjMvovEkcfTdJPmyOV10Id292YBP13q9WD6sFRFHVojXiydFiK4HMOO3FJSN9V8Yqq_yx_5E96NyHh62SSaiHHBfxJXG2m16MzzomdaIoMYcbe44TqPERfzUCti_kWYyMf5YUrbsevmT4B1R7Y7TYc6JwaoOpWj03fQ-9qFvD5yLtAr82rwoOlV4lrC7AbXE9KOV_o7yXhpGhUYHyMrI4cl-AJUoY0rZm5Sq3n50VmAZeERHs8k9NTStD-0b6-Doe9iWNVsK-vSuh_XpG942kHw1Y_RYyy8ebDaHmN_LUBoqhYYuPBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=H7zbn2ac2eDttaz3xm1F4bHRa1tzmcraNIK-d2dMkfjEcvMNey9EEfWUSqTvS821rFR5AwBHJc_ACcffwQOyKq7Z3Syaux1wBRbcQwGjNCFOdfCJmybcLYOoO-53OoLXCSXS8gquFRpMe2MKbcWmfpNjIBuSqDKmuuTTQS2oyl99eixAHfbMZCBhqjPZUzoZ5_leFCx9ViY12eGLMttl44DNRVyyy6OwE3vje3O-AcHOrOBbs5f_s3Kibzh5IPhuNu8uVT2FRoXk0hJjulFQCGGdoGL_URlN_986GHIc04mO6hjpQasIp31XFlhiqlK4LkAIMBMGrTIaRFW0ZkrJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=H7zbn2ac2eDttaz3xm1F4bHRa1tzmcraNIK-d2dMkfjEcvMNey9EEfWUSqTvS821rFR5AwBHJc_ACcffwQOyKq7Z3Syaux1wBRbcQwGjNCFOdfCJmybcLYOoO-53OoLXCSXS8gquFRpMe2MKbcWmfpNjIBuSqDKmuuTTQS2oyl99eixAHfbMZCBhqjPZUzoZ5_leFCx9ViY12eGLMttl44DNRVyyy6OwE3vje3O-AcHOrOBbs5f_s3Kibzh5IPhuNu8uVT2FRoXk0hJjulFQCGGdoGL_URlN_986GHIc04mO6hjpQasIp31XFlhiqlK4LkAIMBMGrTIaRFW0ZkrJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UK2qRFE4gospuqBdBqe8NGyuRnHUshpJ7We8efYs8GQ5wbwcct6GtXuuKVhCfjoDqllUG5w_oLB6XkPIr5DikFelLRMKspIEpGZ3tqvOulker_1Yhw5sBzgdA77hBhypVcdswRZj2djXc9oxvgSC0-Wu_577vDcDu8LL6NwVhaYXwY0FbxHlcgwe3fKKNI0Dwn_C-wMU6VY198sxjVeXpmbKZKnwnTb13utbGLgkwUQCa-fRT8jLaCWntxutBq1fFOE81_E9nQ2W9_LWr9DqAEOaU0dGPe21pMrRrohnoxwtJXsdFdeOtytpNdRlcak_lV1eauZ0uasze-BNhKlj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UK2qRFE4gospuqBdBqe8NGyuRnHUshpJ7We8efYs8GQ5wbwcct6GtXuuKVhCfjoDqllUG5w_oLB6XkPIr5DikFelLRMKspIEpGZ3tqvOulker_1Yhw5sBzgdA77hBhypVcdswRZj2djXc9oxvgSC0-Wu_577vDcDu8LL6NwVhaYXwY0FbxHlcgwe3fKKNI0Dwn_C-wMU6VY198sxjVeXpmbKZKnwnTb13utbGLgkwUQCa-fRT8jLaCWntxutBq1fFOE81_E9nQ2W9_LWr9DqAEOaU0dGPe21pMrRrohnoxwtJXsdFdeOtytpNdRlcak_lV1eauZ0uasze-BNhKlj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=FymYB3NSyQn43GB5Re8kEiDIUaTcUbgQgk9TIN-vmuzbyjMtbVmTNGp_wSV1auIPeaiFZoumuCGBIl0WabCb6rN9fv2hcZq25wiL9oH6U-ureYfsJwWwaQv76rrY6cwMAwc1HpHGaHYM9Kk3Bu5upGTsSkc8IGfhpx9A_vSpxWTUcorLn-fVLubew8qJW5CYl-12qrt0TtF5m6sZbQ3LAHJNuYM4pTGb71MyxSkCayNImaxyJtYm_LgdP1I5O7vj3omV_USu301jiaJ-oaQ4uqIVXaISB8B9ULskXPwdpJzVj5hb1cG0XKhfZ8YrI6O_kMbQwkriNa37oAAp7oFUNguw7YoWdiXcdzGRMRwHzxGp-W3Xy8YfNYX4D9Cg2iFmTbOdbTyGJFgz9Mp-mY1FiOHNMn2p9-8jQngI2lY07talQ0lJrs9MK0d49ysuqZdXgtQBVJh-WFRhtoMaV8NN7GsoRH2io0DBsbIHVY-mT3_T6HA9HsvhTrdU8n4eyORhNmXK7SE9eMCA0DppDvMuzdgPU0Zpea-3dtvIYlaebnirACtXFzmbx6aFu2GeD74GGJoKlGwY_ZsMXv4wz7qByEQG_IOvx3IEbFsbwvjj34xQ42QUTvvCA_whq5PsKPt61yr69tv7GDMMoEZz5AGtVWifvoeO6Y7vpwxQZ1PzJ3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=FymYB3NSyQn43GB5Re8kEiDIUaTcUbgQgk9TIN-vmuzbyjMtbVmTNGp_wSV1auIPeaiFZoumuCGBIl0WabCb6rN9fv2hcZq25wiL9oH6U-ureYfsJwWwaQv76rrY6cwMAwc1HpHGaHYM9Kk3Bu5upGTsSkc8IGfhpx9A_vSpxWTUcorLn-fVLubew8qJW5CYl-12qrt0TtF5m6sZbQ3LAHJNuYM4pTGb71MyxSkCayNImaxyJtYm_LgdP1I5O7vj3omV_USu301jiaJ-oaQ4uqIVXaISB8B9ULskXPwdpJzVj5hb1cG0XKhfZ8YrI6O_kMbQwkriNa37oAAp7oFUNguw7YoWdiXcdzGRMRwHzxGp-W3Xy8YfNYX4D9Cg2iFmTbOdbTyGJFgz9Mp-mY1FiOHNMn2p9-8jQngI2lY07talQ0lJrs9MK0d49ysuqZdXgtQBVJh-WFRhtoMaV8NN7GsoRH2io0DBsbIHVY-mT3_T6HA9HsvhTrdU8n4eyORhNmXK7SE9eMCA0DppDvMuzdgPU0Zpea-3dtvIYlaebnirACtXFzmbx6aFu2GeD74GGJoKlGwY_ZsMXv4wz7qByEQG_IOvx3IEbFsbwvjj34xQ42QUTvvCA_whq5PsKPt61yr69tv7GDMMoEZz5AGtVWifvoeO6Y7vpwxQZ1PzJ3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkql5Hl548VEmXQDdKqLeT-Am9UjHs7xQSE_uiipNhOHHAdhr988yNBlqm2Q82aOSQpqx6H0UDcXnq1_W2jLkZBUmQIdQTSVTF6Ktk9s0jrSFbcW5WIuA8oge6gaZ_9MBJqb8hnercsDHk1zVX4HVmTf7TELl5n3DF93KIfrNgkfn_skvO7lOEFm6vCCqgD1d0VhHk6oHTdsTw2YzfsPtAvwxs4VFTXRNe8qApgs5QHR1vAhhQUMyEvolmh6hJCU4tQMZpz0cIkesIjLwefAprBgujhvS8Rrd44dZQvOT8f7-zALdYn895bXVjB2x1fDmvMxjZMX2YBpi4G-IQC2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyU9xaoE7M1jvmK32zU_vWCild4AIhSQojnOIBpkn6nbLBHvKPnHzDOmTZ7BTxL5Mlcg5tHeb2qxRlokQgNW0AGzQzfPJVauM__ErERNe6FDlnqotRYedQTn-IbmLA-F6Eka14PefRrIr_FWUOJXuYQR28ghih7UxA0Uu2o_t7joy4jB4Stw9wXH437y2S_qLV9tMIeMmkOmcfEfM6kaUAljMhqvUgHGUHUkbXkD3fithEWKsHIQaUab62f32ibV4uePQ8GSd_c0StyCl0E3tp6GWWQWAwi5q6g7IB422VKqbOyMFcIwT6Syqb1xqhemyr--e-M2pHjbuLPnaCgpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVYLUe5nZfh0lDiTeyF52QC93ohTlmBW0uLtnDlrq53HtiHNFXJJQpD4XHrzRPpJNbLBvd2D9kj_H_tiHjMvqh24nhqr_czP4_vLMBlCewmk_nKZX75IidWSWdlen6hmXXR9uQFrQPlqqP9C6ibSeFHBB-pagNaSjA2d7izC3GPjsiEkMxmTtKBo5yS_A_jIy9zZrxF0hnVPY7B3dJ8EDl9d377AZr0BeK2bJaoYpKhiN4ON_U51JYhsi3jSsjWkeRajIWiuc6xhG8GJGgPGjyAL5NOf6XK9oeobvwcIYrepD5SWDsgOJqGNQP2LvoZktdNS4FdI2CN2nseu9UiJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Ovf0-gJmGkpX1EGxuVkhKYwuE3zMIDxC71zBPsieu8c3sCFRTYnRJrwgjLh6jkvHLgNZxCx-rNhSQGrBZ47JVPc8IFE6CyFRg6wLeQt5cAwl2fNtSqvR3yQbW5zSYDqQC6OtE95WnU51BlRpecRh6LUGIi9P1-1Tn36Mzp4UIw_ojO_16U6SEQiBQ_hkWKzS_fgoM8eZrSI8qDy1IbWWnDd7fu1ndy38J9ngH_-9K09hvyT64uVmVj9XnbJT5pBy6HCk1mvs7Bc5eqt6JuLwR9YILLjgjPM4UgE5F2lh6w6WUK9PVE3vnZa1xiC1kNymNF13nQPpx-SKRZHVZAI7voWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Ovf0-gJmGkpX1EGxuVkhKYwuE3zMIDxC71zBPsieu8c3sCFRTYnRJrwgjLh6jkvHLgNZxCx-rNhSQGrBZ47JVPc8IFE6CyFRg6wLeQt5cAwl2fNtSqvR3yQbW5zSYDqQC6OtE95WnU51BlRpecRh6LUGIi9P1-1Tn36Mzp4UIw_ojO_16U6SEQiBQ_hkWKzS_fgoM8eZrSI8qDy1IbWWnDd7fu1ndy38J9ngH_-9K09hvyT64uVmVj9XnbJT5pBy6HCk1mvs7Bc5eqt6JuLwR9YILLjgjPM4UgE5F2lh6w6WUK9PVE3vnZa1xiC1kNymNF13nQPpx-SKRZHVZAI7voWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=OINKICfKsBd9WfIA1Zpq5RiDKIN6zQU-09OoskO0258fZic3OMXbmTEv929CIpdq9EuaVRhruDJZxT2DutFDPz7STKNgg0b7E_dnptyNrUjFzlQW1j01M0ELvrSCZzyb1issGKfC7A42ICY9PKwOCWXRBSpiSApGCWSqD8T1bO_g5u34x45wfFiJgoqTB4NF1Lf9--_Co3vGVYhd_CeAHtQenMFYHSD7-o7swYLpFZkIFfRxhlKhbGbbnv_frlxPuztD452WqIZTscHU2qqM2ijAYN3jJdBfQHhgxJArYQU_9K8FSTByPXZi9LWw6jrU9HYap9XWkUrzK_3l56lEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=OINKICfKsBd9WfIA1Zpq5RiDKIN6zQU-09OoskO0258fZic3OMXbmTEv929CIpdq9EuaVRhruDJZxT2DutFDPz7STKNgg0b7E_dnptyNrUjFzlQW1j01M0ELvrSCZzyb1issGKfC7A42ICY9PKwOCWXRBSpiSApGCWSqD8T1bO_g5u34x45wfFiJgoqTB4NF1Lf9--_Co3vGVYhd_CeAHtQenMFYHSD7-o7swYLpFZkIFfRxhlKhbGbbnv_frlxPuztD452WqIZTscHU2qqM2ijAYN3jJdBfQHhgxJArYQU_9K8FSTByPXZi9LWw6jrU9HYap9XWkUrzK_3l56lEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=o_os3_xPilUXFUCEZZQH4FwzfFznsOKruo_FnQ9NhmQEa1kBatFBbv7NjXQoD0uvNv09OF1apvFJQ9pDKNDv87G611iopZkL_svNK_yB8hs7f_LqlXVBGCiLoQBvRmDU3Hb7Kzx_L_sk8TgklnK9yK3S6BXZ_h_YV3S86j5ddQU6ltirxa3jZBNZnBg-p2vIzXOgOn6-998-7pgu8rsZLQi-uZpR1pSl0mnBa3afyrdaLlV7uDRpQV4AswoYr5qMhq6rWtwfmCMlkuynamY5yDswYenXpAKeo6U0S5Dtvkq7jQJBd_i4LKWX7SqGvyJLK-SOxW2K-JYMo5uML713_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=o_os3_xPilUXFUCEZZQH4FwzfFznsOKruo_FnQ9NhmQEa1kBatFBbv7NjXQoD0uvNv09OF1apvFJQ9pDKNDv87G611iopZkL_svNK_yB8hs7f_LqlXVBGCiLoQBvRmDU3Hb7Kzx_L_sk8TgklnK9yK3S6BXZ_h_YV3S86j5ddQU6ltirxa3jZBNZnBg-p2vIzXOgOn6-998-7pgu8rsZLQi-uZpR1pSl0mnBa3afyrdaLlV7uDRpQV4AswoYr5qMhq6rWtwfmCMlkuynamY5yDswYenXpAKeo6U0S5Dtvkq7jQJBd_i4LKWX7SqGvyJLK-SOxW2K-JYMo5uML713_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=FVptgkLSmWG_LUJbmHpTRqSYBEmUpk6wsSwDsG20xFcQL0QwPZSl951iwAB7mSb8dCt3JuMofQLSTI7bGiWI49SkESfALEVLqoqgpFaNoJH_xBh9kGy9iw43_QqjlRGchVV3eEjRj0P_gcNz-fIROJnac-Fs7LVafXCc3Jvr4pxmTKJmtskhJP_InxbrMEOVTlEzSHdKXPqFjSrVZo4wEZW4-xbxzMy1TO37ErQN_W9I-5CjKkBt3mCArbWRQ-8JsZ6J1JXGJmV_fxWu7MGSDUqeWZ05F9QiUIp4pnT7jFRZXCGVVxqYIVoAtdF0F-0sXm2HQ6SA3OYJbZrmKDlWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=FVptgkLSmWG_LUJbmHpTRqSYBEmUpk6wsSwDsG20xFcQL0QwPZSl951iwAB7mSb8dCt3JuMofQLSTI7bGiWI49SkESfALEVLqoqgpFaNoJH_xBh9kGy9iw43_QqjlRGchVV3eEjRj0P_gcNz-fIROJnac-Fs7LVafXCc3Jvr4pxmTKJmtskhJP_InxbrMEOVTlEzSHdKXPqFjSrVZo4wEZW4-xbxzMy1TO37ErQN_W9I-5CjKkBt3mCArbWRQ-8JsZ6J1JXGJmV_fxWu7MGSDUqeWZ05F9QiUIp4pnT7jFRZXCGVVxqYIVoAtdF0F-0sXm2HQ6SA3OYJbZrmKDlWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP5VzgGBQB1frmEIW1J1LAfTiBld3NXzvxbgahDGD8bxhoNiQcFLj0s6moLySqn5cEJzZlVqxvzFPdBeJQV1a5X9o_l5VQwpcym3H5nGIorUyOWjx5JNfo0a1eToOszmcJmrXj7NgRM6Z6NvCe91cAtJVEHOqfKAOoX-3V7R581J4u11oPVKWEbfbAsh_V7Y5hsqfOT9XEeW3g-I8SDCeAZrpkltBWgE5zOPBOGdct_tagMJDSbLBW4R3O-6pgufvi_WgXDZGnzlyBp69Y5sbEXE_dOPPu98AcX7_qI2FBzHRgqNWXVId_gj5zj-e0pAIsbyEZCGPCL8M-MQPo2QWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=asn-L0nCF_TOxI4ZHdWIei4zPEUwdXqPsIEg1SuXdM1EDjq0T54h92cRdi47rN630BjnkgGOUKHltl2Txve25Dc0MqfWqao4IekQPPV3MwLvpzU8xG2atd8uRQSaTXjTVzG4hc_5-7nxpnp8X5tmCjtZgYcog0fuJNpzL61g3phtNu2Re6bZMXJMVTG98bcSvueU-YQE1RtyEw4F_fPqIHpUIYcRNtIB7rRDqlVlhl9B-LVO7knP4VQXI31MJqDHiv77aiVPYf3g3_KzIz_wWsrTIGjcNHE-QrgThZV5Cor4JyfO0fAS7NmUMgnTCY7gSFWauqjWsFXvo4MFtRXU87pHZtCLR-ZFcASC5jzDwv7ES9qrQSK3YpYa_JDcjkdDNPqTdaTPqrsU2HurlbjMZFXtlkBTSblVTHiZuiyCy0-_QG8tpnliVJYAOc5tIWyvTxfwfJqLvb6Ave9ZEwZ5wOSHcivTbxYQh4gz9_O6urnY9YMZSqSaIyRP9Pk_ba8soewQ1gOaO2xe6OpQWgRDZT_P054nMcAVD4N6ekWgB0mJsgYDX_iXt-Vv9-uu1OA1DXpvOtTysDg_3LvlIdISfSssgmV-w7OhwfQcd-M1nRg9ZtsWFXYD-E5dO8FdOCvGMSqt_AMUG81DbKQX9cWxOXqaAlQ0qa2WWM7QAmNj1PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=asn-L0nCF_TOxI4ZHdWIei4zPEUwdXqPsIEg1SuXdM1EDjq0T54h92cRdi47rN630BjnkgGOUKHltl2Txve25Dc0MqfWqao4IekQPPV3MwLvpzU8xG2atd8uRQSaTXjTVzG4hc_5-7nxpnp8X5tmCjtZgYcog0fuJNpzL61g3phtNu2Re6bZMXJMVTG98bcSvueU-YQE1RtyEw4F_fPqIHpUIYcRNtIB7rRDqlVlhl9B-LVO7knP4VQXI31MJqDHiv77aiVPYf3g3_KzIz_wWsrTIGjcNHE-QrgThZV5Cor4JyfO0fAS7NmUMgnTCY7gSFWauqjWsFXvo4MFtRXU87pHZtCLR-ZFcASC5jzDwv7ES9qrQSK3YpYa_JDcjkdDNPqTdaTPqrsU2HurlbjMZFXtlkBTSblVTHiZuiyCy0-_QG8tpnliVJYAOc5tIWyvTxfwfJqLvb6Ave9ZEwZ5wOSHcivTbxYQh4gz9_O6urnY9YMZSqSaIyRP9Pk_ba8soewQ1gOaO2xe6OpQWgRDZT_P054nMcAVD4N6ekWgB0mJsgYDX_iXt-Vv9-uu1OA1DXpvOtTysDg_3LvlIdISfSssgmV-w7OhwfQcd-M1nRg9ZtsWFXYD-E5dO8FdOCvGMSqt_AMUG81DbKQX9cWxOXqaAlQ0qa2WWM7QAmNj1PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=TQYN3vXAJ4B3kIEvfECWiGm4FBLqenE0FKbUZPROqG8UiICxCg88Os44U6pQzJnY8uhrZr_8MLPM8udMs566NLzAMedOeEJaUD9JTQBnrwM4L0JuHQOW5vb9ccChlAX2b1z6bHohtOJTBhtMi74VvHtt7cNrpvYGFwptqg5qaKLxH-GSdI0XjITPeOM3slvh8O9JrIiwXbTqe7HEZFj_8XYe2SaF-j-io2fQvSi4KMKu8LmcBUVCrrToAjtC_R5r9bIVyjrPdva1UJ0w5bFq7IHYgsTjXjL8QAiJwC1azTCbDqCL5P-qyNG7KkAuGkPdlXATYeK8nSPLQmb3uw3JTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=TQYN3vXAJ4B3kIEvfECWiGm4FBLqenE0FKbUZPROqG8UiICxCg88Os44U6pQzJnY8uhrZr_8MLPM8udMs566NLzAMedOeEJaUD9JTQBnrwM4L0JuHQOW5vb9ccChlAX2b1z6bHohtOJTBhtMi74VvHtt7cNrpvYGFwptqg5qaKLxH-GSdI0XjITPeOM3slvh8O9JrIiwXbTqe7HEZFj_8XYe2SaF-j-io2fQvSi4KMKu8LmcBUVCrrToAjtC_R5r9bIVyjrPdva1UJ0w5bFq7IHYgsTjXjL8QAiJwC1azTCbDqCL5P-qyNG7KkAuGkPdlXATYeK8nSPLQmb3uw3JTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_11fWunht2_-WWXS5SYh30bn-jczMRFSVARABOmZC6knEeLrIMJ-BGMd_LQrN7rcK9pH4cy4_l3RtgkgtV84PxFtvQcx_STRJpBlLgmOrDsBNAtppj6-2Iw66zDxejifVey8fPWchuSjGYSmReZoJp8dhs1LZrn0bb7KnP_MW_dvdExEB2buxOOMjTJS9DKZXaLfXGkqJZ7U5wXGD_aD4qnMVkF1RDMJinmRK2GqfNL5XpjSf6_YAyn9b5D-rIs7eweR5pqYLJe0oQCuEIlD_ZXMENGgI13-dvLwUgnT28pIJjKEcS8nr4I9Utm-k66qQt17lCaR2P99TF9mbL5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=WasCBsKIrOfnJUyOnsBIV2tJHXLQZUOAG_4LtacL-WvxvmyUOYIO8WrjAwk_ltWte6LcGe1BPraLq3PEwww5SX4xj0xu_astjj2YQLpDuoMJZcWP8vccvT6C6JFi9tpUDlOrvZM04hAZ0Pykxp0yunh5ewzz6mFMbD7dFZlyokfqWfjOxfjaY0cvl6Ro8TxbHkxQUAcH7X0agfnfAA4my527LRc3M66h69muKL0z1TIqr2UnpQ7WI61mWMIGSpnWk5lnc2EmMpNS-oZN9LRnRzw7mCD_HSFunq_6K2eMQ5sk87GYKo3j0PqHWhgxhXclFF0cU3pZx-135QSSt8KWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=WasCBsKIrOfnJUyOnsBIV2tJHXLQZUOAG_4LtacL-WvxvmyUOYIO8WrjAwk_ltWte6LcGe1BPraLq3PEwww5SX4xj0xu_astjj2YQLpDuoMJZcWP8vccvT6C6JFi9tpUDlOrvZM04hAZ0Pykxp0yunh5ewzz6mFMbD7dFZlyokfqWfjOxfjaY0cvl6Ro8TxbHkxQUAcH7X0agfnfAA4my527LRc3M66h69muKL0z1TIqr2UnpQ7WI61mWMIGSpnWk5lnc2EmMpNS-oZN9LRnRzw7mCD_HSFunq_6K2eMQ5sk87GYKo3j0PqHWhgxhXclFF0cU3pZx-135QSSt8KWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=gXr-49TnY8HTAAO0fKAj3Efg2g96-CETax_C9EqDVG3VQ6uiFKNkALYwd4LkpBud7G-9JAtHcAvSLrvO52RhaYC99iU5FyJl1rKyb5Lvu0GUXz8ZVO-DfgvWkID0RPGE8eX_fldDaGig8D0HI1nzqPOwj_3kxQ6PbrlNz4ZlFd9B2q8ehimFFH3Vn05f9MldF8qXKdR3BOamm1BEk-ISuOFUKe1HRQ5aLYfPT8Z7pjbIMqeF6s3IfiC-7NJNWEoYUkNHSfgXL55UBocpLLQ06INN0F2l6gABCFQ2m59zFPjKyV75FFduB13KUUhwwwn-J-rRNzq7tFPtiPL7MpTiAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=gXr-49TnY8HTAAO0fKAj3Efg2g96-CETax_C9EqDVG3VQ6uiFKNkALYwd4LkpBud7G-9JAtHcAvSLrvO52RhaYC99iU5FyJl1rKyb5Lvu0GUXz8ZVO-DfgvWkID0RPGE8eX_fldDaGig8D0HI1nzqPOwj_3kxQ6PbrlNz4ZlFd9B2q8ehimFFH3Vn05f9MldF8qXKdR3BOamm1BEk-ISuOFUKe1HRQ5aLYfPT8Z7pjbIMqeF6s3IfiC-7NJNWEoYUkNHSfgXL55UBocpLLQ06INN0F2l6gABCFQ2m59zFPjKyV75FFduB13KUUhwwwn-J-rRNzq7tFPtiPL7MpTiAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRCF4UQpidA7PPFi-IfYH_7s1vSsE9xCgr-5spo0EXZOyn4rltFyOHqDbazj-i2JEBbvIQtDV3N2SgcKqiVidawOGhvVfFeHyQtVlyE20NA2Ef1xn5QL0hAyWbGgOAlwI6M4_WrJBoDWph1YgmtUtrbx24EddpUc_zNu4m4YjzMJVohAvDLdEPMLcT7ePZ0A0WaxHghFItsrpRPx--_CQ7s0Z56J6BarzrcJWi0fW4zT1ivNH8KxorzFhWr2-YuIduYJIkIyycMOCnCCVi0Lx4wu6il-uwU4pUar4xjJP-weI_W3T2-cF0dwTlCBwAkkyBiZsm5FXTYljjpINKRpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=lnGdhYSV1wkO-xjBnMJd2pcQFZ64dBLZqa8h-keXHw92p-RUnsj6e8FCMAaEkchAvjqqFUI0YfMM6A0m-De0sACp4Xd6sOeTUmBpkZqck_caJA0YYEFHd8qWL4sGpRq3OZCUiTCJ09AjLq8VirhX7HXIXhhB8PEh357Q1pRphNtBREcXHpBdy0Fhyxw8SidtZw9kSPMwCHsVGajOGZ8Pq3q0CYlY3b5TDJeKQ_KhBrbiV42rsigNecmtWJMjXDUVL8LxgCuvT3Rv50lA_3jdsG36SEepla2Del9B7GTZ04XLfNqvdc_2SNYaQHxoPOEuBJFwc0pSzQUyHdwBnMhR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=lnGdhYSV1wkO-xjBnMJd2pcQFZ64dBLZqa8h-keXHw92p-RUnsj6e8FCMAaEkchAvjqqFUI0YfMM6A0m-De0sACp4Xd6sOeTUmBpkZqck_caJA0YYEFHd8qWL4sGpRq3OZCUiTCJ09AjLq8VirhX7HXIXhhB8PEh357Q1pRphNtBREcXHpBdy0Fhyxw8SidtZw9kSPMwCHsVGajOGZ8Pq3q0CYlY3b5TDJeKQ_KhBrbiV42rsigNecmtWJMjXDUVL8LxgCuvT3Rv50lA_3jdsG36SEepla2Del9B7GTZ04XLfNqvdc_2SNYaQHxoPOEuBJFwc0pSzQUyHdwBnMhR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfO1FEw9Ir3a-mt88k7igmfVX91sYyaFWdNCWXRFnp7UMsmQlfOYypJSDCP94l319wyylZ0snEskbF5QwMxERMWogOBh9JjrUTD6i2lelqEJpuodhdF0YRJzzB-Z1s_cCgFvaAst3g9Ed_fhymuzcN1hmNK5DA4gWnUy50Fkc4uU1ajFKxyA1zi4-tMQrwhdTTIXuwp1tvsRZHhbSRGfjPGAScJvsAjSCke1bZENO35vRNvfDpWxn57h3T-0wecWUM3mar1m8TxvD6l3Q8BtOUUG78rmB4gBkRBNXmu-i3ENwqK2bKK1BJd6ixOW5K0OlpjvO6C_Q3LpjTAInNutRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
