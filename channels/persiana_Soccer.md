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
<img src="https://cdn4.telesco.pe/file/vJM0Blj1ZfLHKPSPvru6ho7JvClCvqDsL9rl70_CST0BTh_oGY_MYQDHaRV5zSg6Pi2EGW_soVY9I8NqyMV2PSRHe7IPmaKGoK_QX8wUbw_-5V-QVa-oIniKWX5Ka5_sNn8ABdi8lTgEQcBIYvXDx3BoMLS-6-vo8W5Wj2B4DdJCzHjUGgb09lMgsEyNqrahyZB9KyV5JHrE51G_kmlOlCYMrksorM0oDbcUVzS2mQPzuJcmLTCM5mOmTc385MsjMIvAwokZBi_NFKANFd8ob7rJGx4V_E6ZdTc8LkNG1oLbFpf2Twf3CHDwf6DrDGxxmtd4gPLQNhQsUbdsxiPG5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 319K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 01:45:57</div>
<hr>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edRwBUnrb59i9Et7pXImwkNoY7bM3afO-n8hzWI9Uv5XFbcgrKU-s1NmmsPN0JiVFPDkQcphbP4uSch0XdwucdrsxzCUnjBvxU9YGiZRbQaEgL-gVKvgXej0GLhpB8DaGd-Tjb7wbAjbyBRrvdnGZjPu1O2wxtGvz4FKXoQIRQ3GTHgZyUq_wnY54-4qnciSDvutkPVGVmqDjt5cjGr1lxeVXOhD_55l_AQpsXayQGIRvun-BudGuZQ2NsMOyeyD8hKY7k0-ownrYDs2QGLTxnNq97GeoRJ09rpHnPsYlBPZ-qNsJBLQMRiLQZX5FFfSSD_aB4fXCekn-fpnnECwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/accJl6ZcLaApOqI1KQfxiN8ZX8ceqVCV3XtZOH3XggpEJnpkRVHOF3fFgGMOiIeUKUTb9k4RvAA66-cN9v_5l9TFW7Q_UvoQBkQetVm273aAu2rGU1nZoXr8Pwco3C7T-11c-iPUo_WIK7df_uiwNeXOLXEHIsqE40C4POvCqvy2OPSy4WP7r7YvjpTmf91fUteT6OU1O1SSuxdslzM6rNxZY7KfTnP0U8fT3yrjMgiN89_wl0uUT3EnDdaC0MQXjxyjLA0SyFjWxg9BxWozNdH27kVY0cWk5nZ-KqOPuKtYPBD2PX-skCmY1TE0HZgF1zI-myIeAyYhh-UdSeY_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KX-c_0WBLbYOIaXQcU-6YtoIP2N-2A_TO-14EUa-y2xk7-G9nMX-g002krofuL0wctCyq8UNB3Ig3U7cu4xkblSmrKrHOzh6Xa20HUMo89le4VzAGOPzOdp4BStyZ4LjzbuzEL7c5yYscZcNPUvud1Xotou-uj9xkxEsTpKfH-7wSAqr9qxIA9wUsSU0DnCpw9Z2CTEuKaTfRVjLnPEZww3fWOleEKwzDFJ_qGwEvkXDKkE4ueZ465cD3eAobgZwCcI5dVQz-hwhKsbdQDS_rwD8iZuOOoP6nzRpyOu_A2S66H2ZJ0pbRlRFtz8dSvLPDmDJhYsWDsk-UzEgz_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون4:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/persiana_Soccer/24333" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFWG9fqbF9H03lsb-UoCOpW-CfkuBOt_-spxv4kyJYPAVh6U7sunwmWtPkcv_ddeyJudgqlE8qIS5KiHO_ZSUooS4dbzGsOGL9IHW5Lf2QnRcw5U3J7ZsB5gT_CrMraJMklDqesh9DkN9KisZoSjcr8JqA90ZJhl3LG11k2zGUNPhnjGd_X8CGxuduCiyRLbrVEYQ1J4a1Hz3UHyd_S5MRstCtaSr0fA0dkOdrr2gvkBFnz0jNq3UIgF_kl6WnIYP-HrDbwx5AHsd3xhmByv7mOzn-AImhG4-Ity9a184Omqrq3Edv06S0WSXsgGK90qDW71-uG1d_WErnVA3wnXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6CBuK3cK43lwvm_qbdkxEbF0sbg-GrixjlC1nAGA8zdxEqSh9XRHz1c1CMxacrGyQfEJd9seMMnHUb6A2jaeAH4-WKrGFXSMZOWFJEhwOVOto9-XR1oK9uUCl7TuewAg5cJovZ4lY5XuY7XF8sXLRSJFQlIV8qhealf9gSBy1T8ZaWZMuQpYXuwiY7KCm9nEEb0tiqXrCWdyj2vXPsDEJNJOd-BSiKGVN3cpdCG8VluQsalQApBE0a5syFpC0eMCLBMuXtEiVEJd7T1VvFDj5VGgOj7cAUCw_qQsfVa8t5J136JiKnhVNOusrgVIWrkrS7ClorsxKdfVturmqEJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4gfAY_0Iaa5O-jKCQQf07rKXiY0PBtO06p3Y4JOOyWP4AW__I8XG8cWCOK58_O1Rm-Wqm7QmWhc9PerUn-8A2ms4XJgxfIiwnXm_e_MY660Of1psmXmgi9e-H6zpHMpbTzC2uTVupQHPXpsnoz53doQVwqrr3kIsCS5qbpPykcv5PgAx57FfTGXHcY_d75qTYzWLoSFjIUtA_TpeMhFp6T6n5VSt2DvuMa6l_kXKB9GFtncNoKGYAnUO3s8XHnLbYtGluDT7MeDg5VyJa-8FY9HrHIa39SnWSci8M_uREHfLmwUCykRd0Ni3PWj6oHH0bg_seTCXcfZ4a6gvKW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL2ni4C0e9p-inf_x5YogIlGHgOeLymVQaXCwAGa4bQAUnylhpUcLqSY6h0_Mk5Yv-q_7adJ9tkWMKTjCYUcq1AYUj7-QP5CPDY71uh5bb8f1eiPwQ0PPZtp6MVIRUfU0DnVRBkVtmS4SFV4F75grmcReqzVOIEbF1DMmcp-YKKHVqfPDorlnb_jEj9uTleUFACd_f9tV68H3x7DCyHUDDRI1qe1c3-8XQ03xWL8ndQDvDYP2xfRnIztpc_7Zc4nTxuczTtl6m5TxMwofnyMcbS0IU9EZh_RbC0JmUv70Y48ONtYA4P1HRTi5z83eDzM3Nssl4fTXGyvNVg7V0m2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO1IJxixU2pCstl14X75VHdUifvGLz4lMPJVc2c8hItBHCJs-Xrrc430s1vVd-ecTbCc-0f1-jEW267G92ucypEGO4P77tm3Nm1mkkN3hOvIFg3Lz1tdySMSEGm5uTvpQgLgjmDAOzPT2Wthg1SNy8wiBlCO_WUMsZh5BDRzxATKKfN8bW1ry4k3XGBIjxdzS7AEwny_Z2fH_OPWom9u2Bej92L8_dCNPG5QEZ7269AepESThiKtYmfP1VXN2jgJPYP6vMBlQKQKtHJbwoC23lb_ikY3ObEdanyiMVAY-v2HxUfmSZPEWWfIvFalAbv59hIZriHmb9uRY0GWMTiDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR0WiekFz4jdqsXUCt3VDZk3E0FQj5nniBN3fsMqdm1oUiHci3KOw9v7qZrf5cbRzzjAaopvPSQ_vpjuBVjfEl-RzEWYNCfJSoSldtXnRYPY9tta4atlalcRA9kr2JY_UKsNZaaprCUhEtK0t0-ol1F2lsP8SHhV5IUPcNSCVthPQJylEY_WpRRzAVL621TdvK47r6pVGOlITvpn6WlUHdG4wU9uRQ8oW_5Wdf0YrWasbMW45wwX7mPmxCTvkfbeb51c3PVv1-ChicwMHik_CsUmdqD7RWa8C0LNH9mnhODurEk8J0hPcITSndhxe-W-2X7QHpFqiACld0vF8HKfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8l2ySwHLQk4diIzrQCq_dLoeBnaScaVGbXTWKMLVR_GqXayBmqYYDUfI4Y5YlbVm1soLjqvCU1s53drO7niunwf8-0IDpSHViVPtooISvTOs-Xb6YzVvjfc6t3Itt-sGuS_a7n08uMqNNr54Kxe4ruSNRXXQuutbSXyl5neUMeQDUUE1lePXaRixDZ6BUTRDrD05Fwo4kWILcuH6hm1hrbxmPmPlcrvSAvhxJQG0pujZ-1HosU78bMqR_ZDTdbUBIoULrI0ihDNKo30hhWq_YHYgc60QxmgHwsZWbp4aowQ7TA4inv8Asmbkbwr4ExbIJtUkSnzXf0wMnNOD5bw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-kuFEOxe7QQl2ZOlm2XnJlGd7jAPiLMP_6EKX6QjBT1sZAgCQoVFk9UyXaprrskVHnd-1GEPNQhWFeFXjLP3iLR519LKGnat5NDdGR7jaMpIsT5UWVh-RLcw52Q0Brp1oCQbU0HAACCW2pmUHl68lDZOWG_94rttqYP9q5tzLvWCPnr-7SDbzShpONFAUVD9y-cFiPLR_Q_dK12fqL_DXqMyzW2cKZwtnH-QWSgsCAfefaAnzToMLSEA7edRyuNGmDsRpGVyFdkU1V996CnIcAdiXj1_vc5L5JBy8zti0clQ4J4J0DifqcqaVsh9Xw4XuZQLCfC8otgjq6MCBkucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPXqPtarPI_5FQaXJb_NbNp_ZYDvMzJogUh5GVmCHMhyw9_sZt3qSU0A_Ywity9aOeCPSPhvAfuYNX4ry6mPkPK_x05MsYZ7GVRBCvWV6ZJ65hh5oNl2Xii8Bb6dlWittZMEvSVVhd8pUHs56a_no1gfgDMybz8tZ4umEEdMVdelu9ja9I7OAVYfylWmoi9szqKOehtbUkWwtM-AtIkV6I3DrW_qU06aow18lOnjOn_8BGeMeikkm5s2TQjwJwojNSDR1I2Lbv6X6DBk4ZVo1DTJpi5i8AJHbEeR5jS3m7ulTfSOmnKIYLSjk-tjHAVHXrJQNTUt7eDnZJp6aL4Dew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVIPWyCIMrqAzTn4uTuVNMmKYCUWneqpgTZ4jFDMLOSJvadpPL8MXQfhDoxNmdo4iugvuoAAv6ZlGV5GrtY53xpeJPl_9fREA7jY9UfFPdHru7JqnSmsl14BG9hyWAcPweQdZYGQva2bJomyaP8z961SgRN9pAZFfrYEdtMEzx0wE3fL3fCvMIkCExFXOyNUU2wUvWOiX6zespsy1UTvHYNnjkSv1coInCtnYLCc5ST-00H1RSVzwcLQPJPPIZPWxmGMN3drvpWIiDVfTMYQxDl0YFLCSMBgsXJNWbOKujLjKvMrXtR4npoq4rppFNXXCk3hv7M5UShq1fJBMps_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzUzJw32Ckb1jJNc9ZpgoXroJ1ubZc8oSTffwYP3YiDNvwgfef1rqnGLsJAv6IUc2bOeMTavcjriUyS_G0XBLp_J8R2kncd9D5oHRQaObrBlH407BkJgwpiabA30OWSI5cfyG107ZCaUeirRZM0OQYNv9xhkSwcJQICJCHUubb6gGU7Sh3prypRg2gqEOAvQeg_OIhYHUrylQyV4Bln5KSn5aibpWU9AuSfTJlM5k9a8_Laf1idVpngGeDPXWSt1NKbShhm7HvZBze_CI1NJrRxP6R7MBNd1J8w7e-seo6607ppNdu00Sclr1MKmNwIVF4hyAOrCD5kwSMJBpnvtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=d1yDsjVeBIc9oKFaJfBwqPNAvXrqhKbfzf0sxRTlcK6NbLYXv5lmHGzXQUO5JprN9VVHJpyk1NUK8IBqLnqqAw9EAkA08V81MjuWVOT9qMhMvzwqd5P9uUreCJPRB8qMUNmLzLarLdDz_gjaFCQ_SZt4dz3bDFN0Sc1wbUeDLAb3zbvljqnSJk8AeQgAvHCZzVgmJaBsTVmEoJby2K7LaBp9iS9Jp2xrGjFoC906q921u04y092IHuqN3ej2m7cWNRl4WIqk_SEBez280IQ-Z1fgtaQR1y_Ub9RCkn1554AMQwvkr-izD_nDZQ0upEEiX0ZbZZy_yIHeIryGdLSQmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=d1yDsjVeBIc9oKFaJfBwqPNAvXrqhKbfzf0sxRTlcK6NbLYXv5lmHGzXQUO5JprN9VVHJpyk1NUK8IBqLnqqAw9EAkA08V81MjuWVOT9qMhMvzwqd5P9uUreCJPRB8qMUNmLzLarLdDz_gjaFCQ_SZt4dz3bDFN0Sc1wbUeDLAb3zbvljqnSJk8AeQgAvHCZzVgmJaBsTVmEoJby2K7LaBp9iS9Jp2xrGjFoC906q921u04y092IHuqN3ej2m7cWNRl4WIqk_SEBez280IQ-Z1fgtaQR1y_Ub9RCkn1554AMQwvkr-izD_nDZQ0upEEiX0ZbZZy_yIHeIryGdLSQmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVehkLXYE6WAwkg0SmDHz4c0NZW_42tE7U_VbqMjyaCh2PmVAr_wI4JmdHgLhAVJnkvZf7XMnIR0n5a2Z5WT8crId6ZVg0UnHyN5AdktFK7z2XWlf3z3PHgwm6rqEBC_yjDfZtf6aou64czIwcEDVF8VYzXmg8-6ZA4e-cM5KgDcb82YqI9j6MiR2iCNFBMqOowPaHete6Cdc_rdg4tEd1QwnetgS6OHyzoehglPbrZH8iMAsbEnacp9iiqTDDkcYn3yiKwl_pi8C2RaaHRp51Hf6HsxXPm6G79hQ3ERsPIIbDE5iFshmAAAnGyUV1dV7CiFZ-5fo9LM4C0hD9ugoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpVWLebVihNR9K77JY_av4-wRuQTTo7KAx91bZIt5lHt8dY5J9z7Sq2l-kcwxvQDb4DeYjyW6GvVtWjuteJHBIOdxBx4HimkNKGmPeCcb-16I-tDfRQQYjOYpWuF_tYzf4_sI8ijxBwlUTEBv-7Xqixpo3kSOhQKZiK2Hmktwx52_CAU5oZG_cmja4aML8aMUSJM7jJhcR1QsFFmBBbGSsQz11RKm3X3MP6K9_a8VcutlZtgJPo9j7PXS1PPcBFaFtMQkkwK1Krfkmi9gnoqsUlFM4HmQANMTwSmof3W6dFN4iXfi75zjf6G9aMXNSxNzqwr5T0CaP3kCQJOdEl8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvsnMv3vt4V0sOVR4Nr9raHMAU6qWv34dzBclTt68sX_Jbz70vwnsKJVXY9nDN8NTwuUV0Lu32kHeZaCIplUyC5z0rhnI4bItKEEUgc9r_3mkSFW5SJyp15SNgfn2t1I2UQ_F0BhiB0pvR5tpJn5ezoeyruCJS_FEEh0Dwo9QH-ap7OCttptwtL3416KBse2iKGxN4ia_3nWsQRnq6VxvQfT6h_5ZgFWc4gVK7r06zTyqeaq3UbCtzkGrBOrWmioISdbl3_MVJbik6ZAB0pUPRBRAR-2xsWrX1xzwkzBJCEgIWfjWD_DUdSkIzELeoRTYueP44VPK8jUO05UPCnUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpi2wj3hQy4a1-8bHosTb0WESfuAt7ttdpNTjiSP2hdNxVO1KJrweoZdFESvvjmfIPAuZpHD4CYC6tHd4CusaOZQt2nlxlYAOtLarqF7QVhFfiAX_7jNXGJilHOSmorNNzDxoO_Hi1A7QMxpY7sR7uE1eHG8Irpm8YNlNOMqnCrAX-R_5qqmRr3s6fzELqBhtB33Ee7YD0srkr163igbVobehCqYGauagTdHhKlB8jdeMJlMrieO9bALnKdN0sA6X6-J_ZAzSRhSf3iG7JF44fIwZa2B6NWWYkNTC91GZCJD2sIPsJwL-ZyMlRPu5qVOriBiSLEcJsTC9giWoyh6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmyOoFANsiTVZjgBInoOoMGwUtF-6lxQW8_HORejoxJ2aoHpIuDKHj9Q_ZZxk3GJSX2c8RladVyvmAjBrcUyiLRTY6x3ZmOc3A7zGpqSh5qYorubvQR1xl2kkMpFXHAzKgqC8_qVc_AB6ccMgtRxVb1Zz43xcPMBpLOW5Nj5Q0N_Er2VVhIuM_LJMx81ojV5RKm0AbM8B71QuKW_a0SY8O3fQYg-Uu_ol7oA2ArKq-LbGwTZjr05GqsMJa26o80QRLr0o3aDwvxv6fCxxLgnDPfrpHNQqVdfUCgVjkyKbrHAwV_dUyVKGppOGidMtlEmNrZ0HI_8dsx8_LbEMHO9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AET_kiXQx0WNOyqJWAd_5GVVWc8R9atSbGwM4slDFG-TVmk9Hz-KhDO4qMdg2neRYGrIYR-YHGFi29sfaVWNdsSyI10zege8hsMaC4UwlGdfi8f5HxUsatKT_iajIT70IgFTPKVQamrHCC6KqiR_5hc0G_dpCEJSWcwNqcPgkZkEjh1K2SjtwxTovEiRXtM0_yTN3TnXRgPAnwAD-s4xs8rXpPBqUq2sqb-29sWd7BTLyZuyKPcY8iu9wJQi7736fa7RTEAmV1ZpH6Ii89WXOB-GQA5G_MnBaNZ55KajBiWus8Pa-BBkNtH1zNH9Nh-olg9yrLPMablQQpVxutHNEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSYn7-ioeRIbJ_T_jRilYuqa6W8KDFG1Tpt2IgplubbzNKMahKRqbVEazhx-QYXELiQvvbuTYj1HI8wcBrWlOqUzzAqbxhVcrZH6auP0ZUyydIL04nBl0kWpZfAaF3nUr2OOQfPHt9NiVHXAyj7RjjB2u_UB6vRgEQnWuadZB8tkrusPBP7xxSXHIoEnaMkFjB0nUeWfjgInmcJbr12W_prep1bZ6FUsNWjFS81_vjSV5zi4GlLyT--V-b6gNckgfDqTa-_zKbxxcIQ0Xb-KwyzRS5S0FGlNRVniuf2KxIqnFt6LooorNBAX29wnXA8wKvUWDLl93x08PsIoXCY2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9IeFauLZau5llPLwpXgjCvaGhvIzIcgkvlV2UI40J_ogERkzb7S7useYuDlE2rgTmxie4-tanOSc_tVd5wfH0Ylh5vamZ6w74GBKcefEUIP454DxIk3_cHc5LTWCfII-HWlX3nCTz-62sybsh9NFx1D5Wwa_8DntYf66O2qXDi2EXhN_myD4iVFlGbjD804FovZJlnePZWGp0A27-0fVGXtQqXBW_ZhontNlNZr-FfVLZirKClnGk7lgl6jokloKA7b4XrZYWSWuhLkeQdbTdjUyrUjduocxUMd0WVDMWXvRyETt2Q3mVZuN2e8vE5H1eP11lFATdYDD74XDJHobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfHICObVCv37RTvgM4kAwP9oF3RA7NBqz1NQwAqyewVp8yDJie2oBG6qNkn4obQCJYja7nO_pZtF49w3lDzt8WY2DGjkadIGuhk--oMyjl5g5olbFl04wDDfOwbr8UnLI33qOKjVOkIu8yJWa2d5ajQRbLRXpUdBw-J_o6uqFRNSvyH6jP7bGhu77EOJWikME42vviykQ7mlygtFNdBdxjvyCQsexwDcZTHGXr0b9vq6lVjJxnhZ0XUnmjqxrMFT5IsxTccVH3KhUJycuPhwZWu2k6AolPUVEZjmsQ4OkGZTjwQof1Z7wArZ3AqUV8wMcfzAWlcclgsnwBwLEOHi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYA5P33ktXDECMQX1iNTLGok_Z0A-gxXU-Q78mahS4CowZrcmh9VejW0kPOPotwmsn0rcr4X0hxxOiOcbYJpm6Be0-NX_CB_rc1Ibu1XD0_ctybh-UoLpNKdgletRYdrYuWCy5Gw6o-tvB7JhA1ClPccZQBp75AUfEzYngE7MpAjd78uB98Bpic6kVrw44bKu8Ks317GthZJHtwo99Zg-8yPsOnRl0ptaaOSC45YCHV7bQ3J7G5v-W0WMGYd50bI4LV7bVR9Ukn-T6wh7Y7ZuAnghi7CsrRdNKhCSBcwkUtodlSJGr3bl2S-8WxbAnofSPl8A1S7fRXH7txH7exlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkCZCc_YUJBZ3EXANApcIeJb8nvbvqIDv3ua7JgNdqwV_fxRqKs6kPkFmgq8BjVv7W55IpiQTBD1lwaglqY5qfY6ydbi7r8S7howUpEqlGnoicKA4k6wCshRHfJMXMiAF81AR841msmKWa9amJlQEp-_u0-mTiIoLnMvgXgw7cCHvz3d6exAEZGVw707wPfm5G5V6szE9Z1rbn6OdCWv_UjDIT7Dm1AUthUeRCQ-lt47VwyAharaimzjw8zpj2eMNwWvvHnbakwE3IgkEUyz2ClEFd25qBp-cHH4jiBkPs8fYiXy9Ssc6TrDu24OLdutwCLGX3P9Eg34T_Nx9s3NDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNw2gbBa6C-EPgtWczg6q8iPoRNiUDEBRouFUMkrufCF6TqDVOkFSu6QtqxBSP_M4Omf7wxYYZa-WyU-zqIdVpiH5_6jEFHDnAZ_JrfKXa01AI6a16RpYkfC-bA3p1elQarX4teLL5P9QACZ-9jUVH-iod14gMqVBlnIqSM7MprPlxPcaUChJWaHVRjXr4kf4jAJ3OIrjqcbERQqvZ_gVAnJurD6RMt042SMQf_0bty5bx5ZPXB52jIzTChll_nnSwure7aIKN-P9mEqhqMyeMTRwMGXFnSQdHwN86iFnCm4cydShwY01VzAu-JJyd4uHfo73C49vHarWbITPpXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NydwSm1lZnoCbhGDg3yJJVsWGWFfEIOc3BaIUJF6r2MtVyJxj33akODBrt0aNhxT3tVAxsEodEuottazk_4EyCogzcbygF7d8N1HqJR2yGW3mFUqwUR30lumXuCr00oD30OmKkdv2mj368uHZ800z2UqgydzZuoP6Vuhn5i_1ANuLohfa_JWuGtBLgk7VLwhl8ETrfuLJxqnKYBsgeV2BLxXLdD8UZpw1fSVWPMRtDLnPm2jryu7F01LVig31asMYTWEMSD7pvJ4ZddwgvhNVribuT6pqwmApsZD4tUwRUckYbpT3A8qkl5ao8FUNIHEqfx-fRI44aBf-xyOCvERwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E53bu3FewOeLDicpOcTByDelbj7quZCGqnqHjaNuIpdq6lwcaHxilwNfnlhI5fpjm1NEMZEeLmkyzErKe1IR76M9-1ZkFvs0RxRCH2e0Uw5pBNNE_E7gsfVmBzCimKXOV3CkkzGlUqZQQSp8xirV2xs-SqxCUuqaSi5d_4EyUHPIfQQG_E3hW_34ygj7uJeT_odKwTeKxGD8_51EoVD_yzY-ZqxOeFyjMvqwEDwUWFgGa-DbjhhdVIahTif9JUA6iRN_cizshPHeCMe60v72DnWpslSfecVeQQUMQpEfsXLp3t_t48ETX2gMUBaelO2r5Zj3TtaTrqqHjx4E7PPuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24300" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCnRBN80NdKFoeqUElnJWDig1T5MpvDAucp02BrpOyG-uDu-Lvp6_aSHYyPk4TwaETZekJn8W68EHK9xUsXM81B0WXwBw5K3s90CPvtPIP5PI8gyDAIjdFxtQQKhFEDvqMSSp-kXDtaU4d44x6Bj0Rc6hifc_sg9B5wFlM1LfFw3optASqNRU1WK0tPHiA9LPD7QGiePq_W3IPm_B4gpQ8S89vnIFvQmkbqJ6ZTvSjWkERvNHUR9fT_4Ih8Mg78Ium8vhzkxZ-qUcIf9sj_eFhlSBIBLIRE0aa5xCLWbyl4zmBpX-pZ33vxb09c-ebjvB20Dk8vZPcupnaAoCtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeofOteOtfv49iTbiKDtICYaQiJBC3hyj5b3fhWkYi4JCArfmK9DrCChGNheYmn0xoHORqPQeQ-F8oEPyGaUbpwWGvizrnu-3pQlc1IxJI2Vl5b9XAaRLcJfsgYOWHPubl45MAM0oJsnmGmF5131ggSW_dhzDPuXAf_DENpdoY4Wed1jlwdnAvvWauYvQ9l8CAtpHKiYxH9EKgVZA1Ouez5GXhjJMxA4c6k9tylie200a4XoMMHJTkT_-D5uIs3hjAsdzZhWBjxApm22coVqeAShNY7alkpk1ceLHbDk_el51sc4VFpy-1RK2j8xDWs8i_zTJqJ8lY4d7EOE_DgTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk8i4dZtDd6iJlaer3xQlAV6VrJId0JPG0eajbN7pXsOOsAHARA6oY7EebsY0WeNeNoIp88_OD8De8jxCy5JRd6188BDeSw1pvr9vNlP-gl_sA-BR7BlPk3bsPQcsiKKhw6abAVw_krNfBw2PcZEEaaGeUd8jn337EPUbKD_OU8nhMsS7yOA0MNkSfu_NdPXvo_aTpTGek-WC540_-El58pNAHP7_pHmy1fbyFDGGHVGm9Fp98UCUAUhldy2yP4xF3Gt1P6JWfOCzhOCv8r1AVTiI5iW-0ff808iPc6u5mzOGbTSq0Ui5BQGRXVkz08kLOBX_8ZrgJhA8S-FOkWBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMv4Ww29uOrlMAj10zJgWxiXDX8gAfZZlM0NStZTU2XNAtTzYLunw4Bp94TSL1y7OivgzU5JguOrsTZTcorjfjPLYryoVblhj8rWvJ-Egn6KKi_vG5pteMlLCvsH5mZXE3LG5oDP6gZqNdnJzKA_LeWMkAbLPRwvBc0f8-RaqkG2yEOk9M4dBAM71ROMpO_wClMLjkaLbxGki9pJihMklzo639xLmlgBsGmJ1Z9Q07KWp_1JrLX6ZeLaXkEP4i9SAuqpMbXPxRSMGNJhMpAcRYiCe2RnNCAGBtAra-V_ELGkKX1dpSpQwYSfZBo1t7O9yWtC8Q5wMGcS7jSvgc2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quSX8VY3KdIpyXhwCYRcz5KVqjb5bqR30toV8BI4kDzGMXhPlBWxVlsoxGZo4wLwjC5BgtunzqZKLjP7A2pYJlQdnSyNukQqG9CfS2OuJGh6bGDEi6HpkzWaQemWojL_Pajdvfk72A2yFrfVNLZIjKRiGu7l7Uy2SHuRYqpbeQ4DLG7Tbebg_bXTHBYkrr4osVQmb-pfqYLddZ7hBFynJuavMz5CnVuf_IS6hwoLOT19vl39VYrmHhT4geGHLThfzGT904yjL4tMD4hCwC80x1qJdbKaN4o9hFJUq9tgUXyhDfnVScEzGR2S9Osk8CCDX7fnG1VvnvQ1RdKsgVhj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER4lD-34eS7qANi2h6x9xi5yuWry2lPNZBSNvu5UUpqp4IyWzmcGCkqGFoehE8pVEQc5lpuXWzUleMH7ZvtyV8uC5naU0vH2C-K_AW2bf-D6-t2EiVTTOdCCf37C2d48ZQe3_jsZ2t_5v_Sf8z80QM7fQbCG_NhEftq48UbJw3Yyimri-2Xk1XZ5tuCRAxM3IGMoyTdFc06mVZ0jLQoUUUybUfimIV_HcY99ptESaIYX2OqfsaKRsuPZTuAfiW8jojT92Rioenk59MYrgCtTtc-lTu-SrGSiI2wNOw15y1B8LYbOwuJ9oaj-zwl-JIuTyDTOgWS07u09k8I7U_JM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLq9elDtYlDLewjW6SjnytXvujVKLjID3b2Gk6JADD3S0IssGoKUFJavNR7XYxYRZKBazRd8jRjN80dtAQ4AXljJf6TCp4Vb8d5zZHCQqEVKZh6xnWH7-IKwl9cRnW5Qwe8ubbYecU0e9BCizP4fDtQZyfJk2hzUJpfRZ2cBUvPz7_iwFHxy5TNuCADn2LTORwAWuo4fg-wu6nPKRSMi1ZoupjfKWY5Y797EOjLOprykRdMSRffB0y3XcwO7WQwBNasIk3hfxqiJqi_F5BJ2_gYoe1xtk1pVMtwcmLMp8r9sDzUrLvyW0_3rR_X4SNDupRzjHVhHUWFtvsV2EtYhCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxwUyl_7LIfIXSIM2G-tN3WZew_CDSRk_HBex5rLVhjKn8C4J58znxeBE4ErsIBjQbzij06tqArZnPLkqdihpb0kpcNJQ5aMMglxiV6aOUnha-Qv0g_1fn60nj7Dlps7OF6thHMe0nG9S868TG0piYKYqMVp-E8UEDAPMV4G-16H7Nfw4djWLpRlLpQNH23hiJzx3RLYh2FjuYCguhWYWiRfPuOCYu0a09zRs6v2otv39diLye4OoALpsPWFtx5NJawzolgXlimWHVs6bpNOcJln94M1qQ5nXojVb_TjMRT8x5kwqDw5Dvlg65cCNNs4QYRx9St9XYxuSxPxXTaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5VeMnqkCFBU6jnMZAr3CntyfS05X2Yq2JCijG4CPDINbZSbLQVqucwrLjLFFpWZZzlZvV0B-0P9LYhl24wDU6S8r8OT-4R0vVl1ZyZIGfiey90ECMYklV2UjQLogibDTp51v0viSSuiVHMdaYEqKu1l3RFpMguohcn--A-GB2aDWyD0vMgvGDDlO5MAlnuEYFNbRgfjySqpfcnfCmq2fGxgXykEiIAi60qkUda1mfc_bDsFiCqGVimwCCJhx0Jcqf2xWWXzrDnFXoVEQ6kk7iLPDie7j0_dzerBtXtihkIAQP9so29p1wi4Bpf3FPiowP4a6HcoiOPCdclZKzQ0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=YJly8FzqbrLq5970Z2lpsCBn14jM2X6wnvjrJRI7f7-a-nIn3QG--9Sdm73WyFQiYGcSGQjimLROoQQjwcv9y2UUeJ21MYMnLtMRCZmK1IkSscWjkeKOZo7mVNT-Z1zpq_wZgiS0iTyDMNiH_30Icjtt-baNkMUgc3TBHJDrmHNOwiA5FTgTJl2yw0vSAkbf3RsOidIO2IUAcemMejdyfTnjvXkEsRwNQoI5GpQ9mEFKM5oZ4_9iFOcurZkxcj4CxlaZWpl6jILOC39tCLTH5V6j49xfiAiRAb0uYd2LrV9apwRzp8G8AVoD6qR-GWG1zmiaIEaYs6HjmlwrK2l_9W83yPAcGlxSuunpXc9vj1KKdUd9LTD0wYBOtf55ZZ-WVJJG8zu4HtdOkAf7MuauhakVQnp7rFkvyIObbcMfQ3lx-uGcqpGMrdbv7A0ydcTY8Z_82Fe9fwA4EKr3UhRzv81-TJwm5D0bI9-zXH-NoAwb6mya1h8M0m8PDUou0MGFMqDUXT2JWoJxtpNbMm9ANSQf9ijrU2Rro2bH0IKicuHT_H2zlS0xj336xH_EzBxKwIWKYICehRRN-K-X6sCvxlURJKpHfazkwdi-3fIhR5lq1Qaa4CMqs-ic9OdcjB-zziXOAQ5ud-X4oaM6wJvlw5wv6NNE97rYUjl8cpjQams" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=YJly8FzqbrLq5970Z2lpsCBn14jM2X6wnvjrJRI7f7-a-nIn3QG--9Sdm73WyFQiYGcSGQjimLROoQQjwcv9y2UUeJ21MYMnLtMRCZmK1IkSscWjkeKOZo7mVNT-Z1zpq_wZgiS0iTyDMNiH_30Icjtt-baNkMUgc3TBHJDrmHNOwiA5FTgTJl2yw0vSAkbf3RsOidIO2IUAcemMejdyfTnjvXkEsRwNQoI5GpQ9mEFKM5oZ4_9iFOcurZkxcj4CxlaZWpl6jILOC39tCLTH5V6j49xfiAiRAb0uYd2LrV9apwRzp8G8AVoD6qR-GWG1zmiaIEaYs6HjmlwrK2l_9W83yPAcGlxSuunpXc9vj1KKdUd9LTD0wYBOtf55ZZ-WVJJG8zu4HtdOkAf7MuauhakVQnp7rFkvyIObbcMfQ3lx-uGcqpGMrdbv7A0ydcTY8Z_82Fe9fwA4EKr3UhRzv81-TJwm5D0bI9-zXH-NoAwb6mya1h8M0m8PDUou0MGFMqDUXT2JWoJxtpNbMm9ANSQf9ijrU2Rro2bH0IKicuHT_H2zlS0xj336xH_EzBxKwIWKYICehRRN-K-X6sCvxlURJKpHfazkwdi-3fIhR5lq1Qaa4CMqs-ic9OdcjB-zziXOAQ5ud-X4oaM6wJvlw5wv6NNE97rYUjl8cpjQams" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=N_VNEUI5SzBuvJbSzu-O0tnFAmDPzvzuozR2dXgDKQB1B514rRS1WJM5ntvRVB-9DcC36rz-doRrapOrX7sYLSkFQGqN0BLXfXxq2ltrKMONkA8bPFT_g5W2v26g3Xm7hLY9UYyDg0BuBIgiKBdL7R-nJl6IPKI69AHABbJIJILyizg94awWFZk_3KSeGMmo2dwd6oCY3SiHk8xKuPCWt-63xCEYdBo_ytVXVluQ5XQ1rS-E-0qMooM4FfdNTuws5HzpIjjJHLQlRWZu4himAAM0NfSMkwSf1QGxM63qD-omgSSDx5osIkbcC16u-gAiYsnHDnf3v9bljQZMm-tvGbO2ADWcMRYdjb-Jw6dkwN0XylsslJlqYrUijwjV3FhoniL8G_-BLwO7DXYPect4e1zK95gR0AQxgc9OrCrX1VDvahG8IGB-Cr3fdfCwccNyLYqYhZ5zSXDovn2hlcKaGiQhk1Nb70xpdDMXijrd9cXWZTVlzVkTNzcq4KU5smjRVXIJD6DSr9rgk9p3u0E0cdMhiLLHC2l5Z9S5-JHkmmQjbA_F_UemBwg_vIfD8h95D3sqcMWp8HAd5cYWVwC7vCiur9TGsUscJuROIDY_jBIrlss7PA1bNdwVaH_An6C7fohP_cOjTLExcwc8Sj_4JmQYJlPtSxhaj0ROuQaogG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=N_VNEUI5SzBuvJbSzu-O0tnFAmDPzvzuozR2dXgDKQB1B514rRS1WJM5ntvRVB-9DcC36rz-doRrapOrX7sYLSkFQGqN0BLXfXxq2ltrKMONkA8bPFT_g5W2v26g3Xm7hLY9UYyDg0BuBIgiKBdL7R-nJl6IPKI69AHABbJIJILyizg94awWFZk_3KSeGMmo2dwd6oCY3SiHk8xKuPCWt-63xCEYdBo_ytVXVluQ5XQ1rS-E-0qMooM4FfdNTuws5HzpIjjJHLQlRWZu4himAAM0NfSMkwSf1QGxM63qD-omgSSDx5osIkbcC16u-gAiYsnHDnf3v9bljQZMm-tvGbO2ADWcMRYdjb-Jw6dkwN0XylsslJlqYrUijwjV3FhoniL8G_-BLwO7DXYPect4e1zK95gR0AQxgc9OrCrX1VDvahG8IGB-Cr3fdfCwccNyLYqYhZ5zSXDovn2hlcKaGiQhk1Nb70xpdDMXijrd9cXWZTVlzVkTNzcq4KU5smjRVXIJD6DSr9rgk9p3u0E0cdMhiLLHC2l5Z9S5-JHkmmQjbA_F_UemBwg_vIfD8h95D3sqcMWp8HAd5cYWVwC7vCiur9TGsUscJuROIDY_jBIrlss7PA1bNdwVaH_An6C7fohP_cOjTLExcwc8Sj_4JmQYJlPtSxhaj0ROuQaogG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3CGEHmhaQmYg5dSk1EdImUdxHykYwEO9vSfB1NTzny61mG64Hp7_KB8-oOIRc0dLkkI97LnhgqeqQzNiwX3L3hT_yFswVZgpdRoB5B_uwMaoa5AOXcRTEN7nQCnWYe0aWV2gHSC06vL5mTXfkjCt52W-kXS9kfQ17lP34CnrrEfd6scXMafOiJVxHoi0Ql5iJ02qpmDv1sh6qeFr26JBIkDo_UyJI2e8XbjPy4hQRcPNdyfp6RDWaNX4VeMHg3rcNzgiFtXMwRFbNw0ku1bQkPhc8GdiitEdyogfjM2Sc0n7PM5FXOlc8nSZ6oJlZ2TPlavpW62nCJGqj9B4r0p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9q5sDnw4iAo0mMxfO7Obd81YSZpBdXnppn2-69DrUrI8eg5t9iFRpk8o5p1pWbWfiXW2Cq-TCQe2nxSXDNA0aIyMHmUgaH7lz04gBvp-xrYh1HiinTmkwC7_xPL-9NMb_3FTGt_Uf32OxMB-fZIMkYnlx0BeazAsDkOpGdW4QyddhvJDMS_b7VVZBc7nXEew58NVQcJ0i7JHYL_O7Lf90birPrUTHW6F9B1nEbywBfIAA6UKeNR84e_Vs1OfXbz94b1TnmXrolBekGRHqA6l1aHAPfZcerw5jeYnz1-bR2G-FklH_zB-dSwJaGzATjGsXsEtljsjQL9QMNTDHEtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6z95D7IXMX1aoLie0vVVZnFUQgCGlQ_VH72njEtAYXxt5bJP2f99a2A0bh3oAgYp7hNykenWrMqf_rk83YvLdEqKAXHHcmjT-rSA6cgE4LpWn5uZWXqo6THqMwjIP4RhatOQEeppsTFolNLZcLDLnDFGQeyxZPMWJSJ3i4mXxx71vCEym_DFTOTR4dpzC8Mkdiu8pZ4IGsSq1bWLkZh6QEOFK4dG3QDRESWxIIcexyxv4MyxRG2TLYgydjsncmRPvY2-hjURr0obcLX-GzJCuOF5mbDSDuql9uSPnNfYWWIGn3lXy0uqgV1p05J-NE0SPmGcyekbu8rdtKQ6pP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glbc0Es68fCkYP3Ruoq89qVKacBTTJgDa0T4FzCAjrhWmV0VI8azJMgEWZNYFcB4v5pxCFwRJLqbrbR7_Xi0PTaqCnKeDWm8hioYUDqJbGxok86-MvBXCNatf3gm4eOa6Rvij4p3amXvb13x0PDoDWgVKxUtCIwVa-C_RL7LiIwyIg6jnrDrLbmhC5PXMjeLwA3Qkq2C2jR9xKCOHtyn7BK1lvjvdNaN4vq6dnjBylClP4aXKu9gpYWitRBLs694899cSWllCSMTJYHfmJnA1N02gvqzN2WfKfFWpo7Kh6x-8s9NxFRteOJ6C_dNl3Pz9hVtJpN6-UVFbg8AM7d7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgSqcUD1GhnVOaRGTmIWxcdFDkODhP02_iUBbDVKMtmtVTdrtjhDCY-2udXJl3o-Gdl4_snSxY7p8uS964swkKuxvXXo50nPbRRJ0tU2Eji8YUbhl6lQPv7Gqt3I9oflW8Gf53uQfPmZESZZlOhUSFwazc4GC4U-zABRDVqx179CpNcj3yzOBRIF4D6WEjmRFwhics-0UvKU00GZceX2OJQcLvQ7Q_Xs_UMTisI_hogsose0SyHrxxa_GQYQvpakvVOtxDNqXg_SKcqxAZpHyMfqU03G7-5mLebbaJCWLXZOWadjESLhndeM7T7Iia5c4FIYA8zYhRpqV22QcIbiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=WXaZe1D6eJ7M56d8ca2EJMESWUNqkw4eDakVZCcgUYX-5IP6RylVKliWTwSXtp1P50DzXdDugaiUgxpTqrh6wXrKkcM6gkLAGbI1QfhW-yRyAJ-RQmy9YYgwKpM2DtCzlmhYhMMrOCDDzirKC6V0m_OD-zJxAnw5I-YWOdr_57k7oLGVRwERPWfnQrqZWTMEbDYJLQCcF-adbaTZWSNrs61KDHGSDYYenEUtGzFi_OJSBUJD4bTNiiMDnHcjhsPKVT_F5NlSrDPwcrpSQUAU7DDnGbnxnh1A4e9qY4Pu1uTDfvXxSAYvHk71dN_wy-rQdOJMLOAlOPM7R9gZlZxXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=WXaZe1D6eJ7M56d8ca2EJMESWUNqkw4eDakVZCcgUYX-5IP6RylVKliWTwSXtp1P50DzXdDugaiUgxpTqrh6wXrKkcM6gkLAGbI1QfhW-yRyAJ-RQmy9YYgwKpM2DtCzlmhYhMMrOCDDzirKC6V0m_OD-zJxAnw5I-YWOdr_57k7oLGVRwERPWfnQrqZWTMEbDYJLQCcF-adbaTZWSNrs61KDHGSDYYenEUtGzFi_OJSBUJD4bTNiiMDnHcjhsPKVT_F5NlSrDPwcrpSQUAU7DDnGbnxnh1A4e9qY4Pu1uTDfvXxSAYvHk71dN_wy-rQdOJMLOAlOPM7R9gZlZxXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze4PoLsJjOcxN2xtEbZOZwAmzgoNCBlrkZ_GByHEkTC9-Q2wVNpg_f2NTtcMQlwrIBwmJYeBDmOuDMNAEWPTWkWOZA9smkyqwQjv27aBqradREzA4BEUQbSgtOJKKdK43qyKdQ9_amiB34Q9jaRek0MfOUPk26HLeXQGKAbuX1J8Xmlk86b9JOHoyk_9Z48G_2jnuOVCOFtys1l8VNsHV7uzNgl107VYeMsoNypxZUpdIabR7p9L395N3mKI9mzK5mFWQ3KmkFGYYDnTcQ_8IotdKuty0lKbffkQkwFdqp5A0ncAjVJBjlRqe3uYdFsXyNlgfbmxiHHUdx9YtZV6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/turbLwsurFqbViAzB9GS45tmUmdhiGoHdxfQwLm5cKpWymohm0CqtIfqmwTnTqIW9rP6uMakD7v0fmeFyfERplg6XxzXG4AD8tfKYDvVl6kTUh-SUNJ_gi_NV2WsgnFBtMT3jiXe_j2gJqgfzuNg2eIHkdwBxJWuiDek6sgOEUtz8dXvYL6ezpYVQlQn3JvPyMROzju2WDHmrtlneWc4jPVanGZyNmH93d0Pc6ml8OrBaqYE3FEi_830hvfmsbVIFdK7KLL7VtRQWHVoe6loWTfsbi6QoFHyGA5zZWHUyYz6jM5r4Ga0790KWuVu96r9H6ZrJLbiZXHZi1d74NRPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQVQjctDsVzU_ZlnnbK7jn4yf7-qSY3jVZU6Y9RYPNERs0i_bjJq0dN2yXp9WpK1WtAXblo-HECiHsVfGBo4jG8o2H_JzuavMCB5Ia1fi217PCX48yEpvD3pUdMsfD-ZMkW_6wQkhyBVasCIqihis4sQb7ozbidkqB5LSGtkTnC2LdLecg0VkSXsUNG3mS4VCAJId2BV36hwN5ChCmUhkBuV9W9rgNuSDTIlY_Sjjj9S7TAFav4zTBIU3puwMLCORPcsU8Sc8V_BQPE8Tv2n4l_mqnJP5QOPYuJWbVFw4VxG5P6U4cCGRTlDjYlFjruEpuHjd16y7QCdoR8qTAo3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=vkGyvtW2eSzT3oAwYK8SvY8sv5qfm70yyBhTYxXA35ew9LwnE9rEyrV4OMhAt241EQ_FcfjC16SsHuQNTWMsTMzHBMJHbROlL95FegmkXjpQk_NBf3vZuIgxMHB0xwnwLfTQzE-zHhAzctzbSIo3wrfSzHSfHWBo8-12mEs3MvvLwgShDmbYAGFNvCAZeLbCADJs7YgjMaG1K45XUw5Ir43RZP5VnCW_Tg_nTlG9Dst4VvlLnUGM3hwuHqHBdVb98VxdZzItzsiXT8ixyD3ZOqRzBb9OqUjO6oLItRUqbSQhTSAct-Ck5GG4H7AigigDkyA3AJrARWm4fN2P3pemCJLMakSzrcyLID8UWqFGGgw1Qdj8S6E0XTlXLMIb92SdQ0A6uGhtKX974oOxeo1jZzR5XEpL3aaKXKgt3hv1dJBWDsy38IZnDjFBzZObQw1hjhbFN8TsyJP9ZsXTR4r0xTXTOAPVMdeQb13RBV-CGSDGuMjhF9EFBGCi9mAiS_Uu3pdfSWEFJUCVvM1p5AbcG_G9LiLhL1QxzZ1rCJPOzk2vvZgSbet8fAIN0sB_lB5F_e-WQ0HFp9qqXgCn7bDD6-ZD21mI_YEahoDrb_YSREb7c8IptaAb2rZFPbmQ6DX32rdmnunyNH9tFlwyu-gBECTcqcvsrzrAWrT4kn7_Yc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=vkGyvtW2eSzT3oAwYK8SvY8sv5qfm70yyBhTYxXA35ew9LwnE9rEyrV4OMhAt241EQ_FcfjC16SsHuQNTWMsTMzHBMJHbROlL95FegmkXjpQk_NBf3vZuIgxMHB0xwnwLfTQzE-zHhAzctzbSIo3wrfSzHSfHWBo8-12mEs3MvvLwgShDmbYAGFNvCAZeLbCADJs7YgjMaG1K45XUw5Ir43RZP5VnCW_Tg_nTlG9Dst4VvlLnUGM3hwuHqHBdVb98VxdZzItzsiXT8ixyD3ZOqRzBb9OqUjO6oLItRUqbSQhTSAct-Ck5GG4H7AigigDkyA3AJrARWm4fN2P3pemCJLMakSzrcyLID8UWqFGGgw1Qdj8S6E0XTlXLMIb92SdQ0A6uGhtKX974oOxeo1jZzR5XEpL3aaKXKgt3hv1dJBWDsy38IZnDjFBzZObQw1hjhbFN8TsyJP9ZsXTR4r0xTXTOAPVMdeQb13RBV-CGSDGuMjhF9EFBGCi9mAiS_Uu3pdfSWEFJUCVvM1p5AbcG_G9LiLhL1QxzZ1rCJPOzk2vvZgSbet8fAIN0sB_lB5F_e-WQ0HFp9qqXgCn7bDD6-ZD21mI_YEahoDrb_YSREb7c8IptaAb2rZFPbmQ6DX32rdmnunyNH9tFlwyu-gBECTcqcvsrzrAWrT4kn7_Yc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VajAIN-1mQCrWKgGn1vXdNK90McQJee5ibLWRzbYq2NogrC126EF1WSuJb0z-UaI7OAWy1-MtyhkCNAVe5Iejpa4XhIue6TjC49-KT1g9Srzb7EoC5b6PTpDaaMwJBJbEHNsWAJE0PmzCUX0bvg409WFq5_2aa-0cDXUx945LJVgpKMtgAebCoEoUBryUWGE6gpphIrtMkS9D7IDPFSCDbnj97pCpjpjZ8XVmpUBGhLx_1_6aqu6qsM7ChejQqflpQn0LdCMbscZ36itgEHTrlvQHlS_SvIKeR26Pa3AcrSqUcI93MlcUNpgTWFFAAxaGgyCCu7g5Q3mZxyCqC8Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_aUcrGCDRCUyWWrLrmSHN6sC5-wOkwJV-2Li9rbKeIsRMXfMcxzV5B3MXtwrRhbWNZl8aAXEOTDTxetLtUWhGKBFsHw-BN3ve1OjUKNhlStNLbZhlo7tF9Gu857H8r0Jz-h2lcAvucUK8KX6h3IJu9ZpeqWY6b8fZRoJczL4Jlaqro4Sux_hr-E6tDnrjV9_iwgizcpvkNQpjlij10slgbJamDV86N02TxkY4y0VGezDvda3pU1ksmFETt-898oc_mpZkh7p8E9yAPYS0LbMB4f1bhsgladqnDo5AibkVhJIkUnDIQmZ4WATBXqUAftgKAIwoli0MJuz2IVaiTAH0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_aUcrGCDRCUyWWrLrmSHN6sC5-wOkwJV-2Li9rbKeIsRMXfMcxzV5B3MXtwrRhbWNZl8aAXEOTDTxetLtUWhGKBFsHw-BN3ve1OjUKNhlStNLbZhlo7tF9Gu857H8r0Jz-h2lcAvucUK8KX6h3IJu9ZpeqWY6b8fZRoJczL4Jlaqro4Sux_hr-E6tDnrjV9_iwgizcpvkNQpjlij10slgbJamDV86N02TxkY4y0VGezDvda3pU1ksmFETt-898oc_mpZkh7p8E9yAPYS0LbMB4f1bhsgladqnDo5AibkVhJIkUnDIQmZ4WATBXqUAftgKAIwoli0MJuz2IVaiTAH0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=eB3jFebf0pBXMjpFfA-GtHm_nf1f6yYp18jsVa_iJNRlijL49fHnUksbNlGe_0y54_-tYELMWEpkpqB0PQjeSniRzVFbZ_8gLHtLZKsB6zi1KSFJzklgingLcsJO4p44VPWO88dlcVkXo7rOUyL9g_JN0urxpQeISXDpm5s1suG13fO3TLJTZUXAjHJzWO6WVcA77OmSVhYUJ3ojg8R1GRcUwqrdg0Osf-X0jXG32UVeDXp95A-BT8z5UolrHBO6dsKNsNclGOiTlW3AicTPfU8LRcOJ_Ig8KyUrrZEIfDM9XvbCKmH4zpFHA2OsceWyvqW6wkLs4VcCc02szaWS1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=eB3jFebf0pBXMjpFfA-GtHm_nf1f6yYp18jsVa_iJNRlijL49fHnUksbNlGe_0y54_-tYELMWEpkpqB0PQjeSniRzVFbZ_8gLHtLZKsB6zi1KSFJzklgingLcsJO4p44VPWO88dlcVkXo7rOUyL9g_JN0urxpQeISXDpm5s1suG13fO3TLJTZUXAjHJzWO6WVcA77OmSVhYUJ3ojg8R1GRcUwqrdg0Osf-X0jXG32UVeDXp95A-BT8z5UolrHBO6dsKNsNclGOiTlW3AicTPfU8LRcOJ_Ig8KyUrrZEIfDM9XvbCKmH4zpFHA2OsceWyvqW6wkLs4VcCc02szaWS1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HibX3xq-R2c7NSk-BJbESJ4-Z7VAm44BdTrVyL3SBBgKBgcPlyjA9NMykCSPq8yPK34tHNjoB0ePcL4D65XfM24jS9eR5ee_v9caG8NJ_QjdYAaR59o3MIoYigAyID5wdRUp0vp3-mHydYPv7EZzdtqW5HliXG295wRSM_NZID33vOk90ifRtzfXa71G1ve5DnVJCQcWKfLNpxKcVEXFRN0FGZ3IRgI-x80AvhG46ceQi9vmopgPV3U3zK2wqw22mPOg5DkTpcaPLI2Xng06NQbOExm9X4220zeRdO5LXFaSHqLn13PSf2_S5eYkKqIFvac0dgjpbbL7GMfyq-HV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPES6kXKN7R0yW6jcXmVEg5-bqcT3GcPnrqGA21BBhEdeqcptBs7DFN2T-SUDbpD1f96BCxWC2goy-o_Mv_yYVa5eSMJI4F8lQZ2hSeO_f79e3crqHUokcr2rklMa2lEauNatKK-ZrxX81o95-hyjTl16nzJ0OGcdNwRMaYcH3hMPZ9aoeRxyv349m4YDo4I8-sdjLksxCWonHHjUhllz7-Zl70pVJXfVQlrshLS9BEel76pEaPvpz2Et94KmpwUFQuhLRtRGjSCB3S8nmEkrs_dTBZCV3Lzl-GkgtxVId5oIAxmgpdSBohhOfvwxRFDSwqUASMqGJa0Vp6cBe3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24270" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9-OOEqmPZeUdMV82UjbKe3HYZ2_l7MeiTly3huDDtt878rd0401-RMy4MVPq8xpQgpJSodfKwc4N6HyBj4uDJTQySgQQoxWs5wcgieCgts0vl9sRkyA8bVKD4EUFWAvaRsxWUoh4xgHtV0Gr4qnKQzhpGEdBjoqwgOze4uHjjc9Gewk4JJAQIByPRe3yrdYINht8BI3aREG0CIBd7of8p6lhcTwji23c4tqMUt67snPIr1-otIhCitCMCqrVzwu0BCK6tgsqrRgxH7JrUW2fXWBjZoUYaFyuOrdvuzdxYppptU1FwWtDZNqQzl7LFGbVtyMkekUMqxkScznld0cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjQ8NY7kJ9lv_FB-V_1xpFLnEVDEb8tFPweAa6YLWHKVSZdD7_yamDlKY2Mz-_55JJbC_mBb-N2pEYsGXMIXNup8Pww7WM0noY2B5UM9JzQVsRz-tEtHTB_62VoFoKWOs4g3Ams9Rcmmzi21AfCWC3w9FgRWvFtLC10yKVgOJ2bb7eWy9ioCKD0BfDpwBhUMJE1VSDyqdCz4I1eJGw_dgFylYLcQvB4vLDIyPwgStzslSifhwbXNJaWnjxYMMT66btaaHPPoZEC6UQWyV5hF4gUcTaBORqDC3KLJRSfy67OPtted8guRWGB0vAR00mSCgo5ozHvCnXF_A4bKmB4Gbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M89bVyNN2jPBMLXWpkrYq6aAkH23jRK5xhbNFh695gqt9cKnN4Pc6zIEdSyIwI3-IzpGGJrMY5OF4PDsMhrA7ml_BNNeQKNLVGXPGyFxk9tYVUmfFt90BED1JDffj-ZPHtoHsgw0PR8AiiQPEWRvRr6k_-tHpNCfYH8G9iMHXmYrnJCDWxNh1cNb3UlupL7NEX8CjD4vmbmQAAOigc-tEq0bl6s-QTWm1jWvdl6FGMwwqqFQ4uvfVPiVZUlduvijjd0J-Jr38PMmjk-hsHz3bgy0Zm-ONu3iJfLjdv6pOPxqX2Y_1umM-siZFOIT4J9oEU1n-T3WfFyWVUbRLZ5yJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ2ZR43vNu7EVq4ggzWJVwew9pZwjp6yBSayAzrzRzv9_flfIpEZjEIiu4ZJROO9IAm7FCNFWIbFqGliGYCvRJtD87c4RsFhLvcSbgKucXmyXMMHIClCLo5FzYdRIhwhy9G6DjUiS7bl6j-QP1nWX1tDINLjPm-KWvmhAq2kW6GNe6AlVdvdpyUEHCzeMRdeVar_0fXNswkMu9InZuoAddkuJXYjIc8ztHSv2JIJf9H1TTj7IRWZiZo_VQz0diJfVjfgChNJmtczksmqMy9Q0kk12oO6ULnUAwWmovGP5fpZdwUob080WfZ4fsYHEJuZ8FmvUSvZ1_MxO11-igi6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=cZkJXce_An7nz7h0Gh7NWMpTTTmExsqzUMHCGzcm-r3mBZf8Wyt0gyh3QR-9_SG2MEitMUatCKmSKOejq7NqE56MwOPfUVLeaQDSOSPRj_4SVju6TZLIdzwbWxRoh2Df2VMofZGsWv9ULt0X0M16hhU7AR6jom12EtHzcH38xnz-zxwsBCtNgFrNFh8QYPcJJxuD551wc_IJXFwZQdiNQJvTei7e3gf60DQqceYMe-e_Sj1DVSD_KvBdLwyW4M_Pj56sCezSFYJDWR2ff6NsoWRpDe6F91mAd4bEuWiuV5CNxYI9973z4RVW66t0OuELj_tF70MV1aQhFIZ2g3rWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=cZkJXce_An7nz7h0Gh7NWMpTTTmExsqzUMHCGzcm-r3mBZf8Wyt0gyh3QR-9_SG2MEitMUatCKmSKOejq7NqE56MwOPfUVLeaQDSOSPRj_4SVju6TZLIdzwbWxRoh2Df2VMofZGsWv9ULt0X0M16hhU7AR6jom12EtHzcH38xnz-zxwsBCtNgFrNFh8QYPcJJxuD551wc_IJXFwZQdiNQJvTei7e3gf60DQqceYMe-e_Sj1DVSD_KvBdLwyW4M_Pj56sCezSFYJDWR2ff6NsoWRpDe6F91mAd4bEuWiuV5CNxYI9973z4RVW66t0OuELj_tF70MV1aQhFIZ2g3rWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8gy4NOuVIOFZxVjArLJ8CwKZ6vujsQl3Blg7v2cbRejy6_78lCPf3ACvqPO4sC9hl6DClYLMnuEHnziZEdkhcrqh2EnEMikKytbEx-yl7Y7mSL0tfmOFkc_1zFxbuPy7cy6WPt_oj6nUIuAYJVVC-J5013_muNKiQcHk523dyjjjd4Y7289-hCt1RlSKI4SHVl7BD6IeEOBfQwybi_CKRuDcEMhGz1CHndTwZwX3TTl0S9KYqZz_C2mAQ1_H5qaDbNbSe9-392ctdu-gh-89geYX12MFUe4PSe8zjQdd7m4nU8M4umnzjHDgUbxCbSfxsEzBvPhcQY0ihVkSpetyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaHqpU--BH5IJE4R-SLQ55RUL0upbmPmY68hpAQoxoHwF0OmpgQgQL_YjGMff52Cj437LTjMohKwN_aK7_DyvLCzgmZS2cdOr6yCl-mkxDby9id8KPGYG5Z17L-XD0iSbm3QZshQ9DNVYRQU082Iv0RCKSx4xU5444tPO_zGTRqFyrGw1pcAQYap9tTD-YPZcEB85fyDq85ubhK4Vdb8G0I204j7_FSoLqvyHeNYrbFdqbb_jbU6vtHMcNLojzN2gSfp2fXg6TKZmjERaKptLAEVuT0OztJpYY6gK_KPPyJh4X8C5TwhwvpXyDurW6a0nFUYvhi8qCwPmOGb6MzBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=vdOHXiUEAfTd8pPJQnvLhS5CYvgKMuD02m-MPFCXP9_PEPUI92FPAPSxJERPytZqHmk7wJtVJhPrPpQggWJrryfeWr6Lak1hhfbMLpbi7nvDJN-sOy8as0V3-xMIHmeXMdoR_9N65ZhpQBbEj75KeTF4AmZ2CUHMoYjv0-E6z98USZZnP3WddMIX9GPubmPgXjRrCQ7MZcYduEmLC9UnZFsv3vrxKL40XV4eeQ-Pbr5rkXHizpI6Dfm76Z4F23Iq2t9bhv1-abEVWl8DzzABnZDyhD3TtbLcc7IBen3cRA0H3FtodTYqfkDUCn2_wgyh2GdFb1Hfa3aYbvafUkySRHdZj4gbaaBzLYQeDbtM0ifqxI_lfbhwVwlnjiDM6znG5n3tQFhvvLvnaLT2kcoJ2KgIMF6nXCdGd02OxkQAFBd5C1dN7Gxt6wh4wodKd_iUdwv0EkUbE2lR-_SlqpXwxBsd0eakLUWdYcMBpqJf2jxbZAhfOjvPUAThLUwdqNOwhGXY0HDw4QifLdh08nk3mIf7PYBbT2sHdc_K-MirZIiXxnICbwLDgNjnee7VgvjHx4NaJ6SumlqkB6CFIRO0P6jYcH59NUMJ5XZmkP8kQIbP2BpHFPUe1li0VwHDgOOgwXbfrCSOBJaAhyTIfY9UDNUl5U8tAIsSG3kU3yaZYwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=vdOHXiUEAfTd8pPJQnvLhS5CYvgKMuD02m-MPFCXP9_PEPUI92FPAPSxJERPytZqHmk7wJtVJhPrPpQggWJrryfeWr6Lak1hhfbMLpbi7nvDJN-sOy8as0V3-xMIHmeXMdoR_9N65ZhpQBbEj75KeTF4AmZ2CUHMoYjv0-E6z98USZZnP3WddMIX9GPubmPgXjRrCQ7MZcYduEmLC9UnZFsv3vrxKL40XV4eeQ-Pbr5rkXHizpI6Dfm76Z4F23Iq2t9bhv1-abEVWl8DzzABnZDyhD3TtbLcc7IBen3cRA0H3FtodTYqfkDUCn2_wgyh2GdFb1Hfa3aYbvafUkySRHdZj4gbaaBzLYQeDbtM0ifqxI_lfbhwVwlnjiDM6znG5n3tQFhvvLvnaLT2kcoJ2KgIMF6nXCdGd02OxkQAFBd5C1dN7Gxt6wh4wodKd_iUdwv0EkUbE2lR-_SlqpXwxBsd0eakLUWdYcMBpqJf2jxbZAhfOjvPUAThLUwdqNOwhGXY0HDw4QifLdh08nk3mIf7PYBbT2sHdc_K-MirZIiXxnICbwLDgNjnee7VgvjHx4NaJ6SumlqkB6CFIRO0P6jYcH59NUMJ5XZmkP8kQIbP2BpHFPUe1li0VwHDgOOgwXbfrCSOBJaAhyTIfY9UDNUl5U8tAIsSG3kU3yaZYwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=SiNwcExGYTZc_QpGsqDZxJvWo12fdUmtPhXsJ4UYjWuG45KJDAuoO5wzgnNoEJhv__IDWKyf6V89_s6pobPEGWoDnbd2d9f2ozb_eOMcsupK255o3jgwNsqiBorKkj1k9ykitRZQJNedm5_XEXfx0kYrWEitYDJJ9qh5OE1JHIEhpKjuziwj3WRlNlxkymN2PLewLulnq1H19-RDOOSo89RWVjIwrAhe_nmgDwa6NHAHOpeENA3HAIBa34IhKhRTBigB92aOnWG4TdHUDPWY6LWsAw1JEpujXFzS1iY77UaXA1qVL3f_OTB0f-pmd4wwrn3XgrzjS1yrYRtpaAW00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=SiNwcExGYTZc_QpGsqDZxJvWo12fdUmtPhXsJ4UYjWuG45KJDAuoO5wzgnNoEJhv__IDWKyf6V89_s6pobPEGWoDnbd2d9f2ozb_eOMcsupK255o3jgwNsqiBorKkj1k9ykitRZQJNedm5_XEXfx0kYrWEitYDJJ9qh5OE1JHIEhpKjuziwj3WRlNlxkymN2PLewLulnq1H19-RDOOSo89RWVjIwrAhe_nmgDwa6NHAHOpeENA3HAIBa34IhKhRTBigB92aOnWG4TdHUDPWY6LWsAw1JEpujXFzS1iY77UaXA1qVL3f_OTB0f-pmd4wwrn3XgrzjS1yrYRtpaAW00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKuN3D9dC0MIg__HgSgKEFtNBUoewb3vmyH7r1fJQQXCeFuAPlDvOoDOiU9jW7fkl7spZDWCIaph3vBxwDFXIF6ksSENctiLdU1MQ2BhiWw2Y9q8EE1kqrD8EXkGm0cSSPngMLeCe87X9Rsnhbr0hOMdtlQcYkd-uGnwjYWFN8tRD5MdAFaemsE9EapKzdBrx7bfbrTB8ilSX_FVc8elwB5lkNWcXH6M29kQMrPKhtlIb6u_9PEcBXHm8M1dF4cnCSPwdYzx7c3BpnKmybEqFdSn2wJxohle2ZccvitkQPtOR_VTDBcxZSbP8t6zTmOPer2Hc7wn-s1r9v7D6pJJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0Ov6TVE9DhAMnqNPRu_oYXKCyzb8c1UdgDnuoD5pjW27UtzPNrGoahaE6IDNxemmL6uFb-RbLJGK_yfewnJnP9JbVvEbzbXh6ZS41hKDkpZzwtWNNQP1YO_VOzdYFP1vmX0z5vNCfRikUW37_leLIHGsXNjz6720hEYuxBomyASJ3mxinJ673-_8dJwa4AXbRqtWPv9OcBFC9ljbIt0e51QckkBM3nj6Ra-kgGfjHDMQvssPBPcXRlR3SKIdq8l4ATUMJW-P8cc7dg3KiugjRhvoryaxSpICgvZJSoIZQJFT3OWyYFk2rM0DSsUIYhe1OfzI_TantmJ-tY7EwKmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeMq8ACC0PdCHaYNZyBcqE0ZpauWAFAVrKKcZb-G1O3BcPe2wWKwFX8Vb3Zx7yiIjhkmdaPt7WZKMxqLNhE13Ix8ALlmwAibB1cBmQSEjhLxw6e28kFYR7eOF5afgs2IHX2kJ8CxGWUl_D2ywkp3oaMzActzV81Ldf-kSCPqOGGSxomlBCaE1pIxRNPwMs1MECyjjwCl4skzdThdrpm2zfNBMn_X3B4q4B3e2OUFuBweXuI5-0USnc2--XwcAWv37JqLiQ4Pt2LEC8cjaPhck3ek48Vh0DNi7-pIiampddGp1F74S9jzI6v4xMeW3vM3EdgjqtsfULzFVUsktHsYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avYXZ0984zp0vIAj1XD5oYqPYcL6Bbg3IK20eFiaw3IAKHcGm-dYCFgxgtVPJTbxUbvNjIOwP_pwrxF4b6YqInHpfIPzxKaE-WSY9-DXa6OtQF735TKA6KU0dtT635fwQGPo_x7hhU_RhS5O6awJvkYW6kt6VUWNAllttWp0QqrhG07qtbYKuH-zhIOnyQAxM9wDzvbIETRjmPlN29n92HLUbGKwKqYrkaIm8G8NjAKWf4fixJS8ZjPD4SHv0Pu3U-Ut65f4-H42VxqaCDPZ3MEvxBjwbli3-jF2cj0On0bQA1NXyaySbzShprrrNnBHq3wKvLDx_W8sQDaGV8Q_nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR4NRKJR7y3eWhjuU3MMVHPKfDblTY_oXSAdpXzeUU996RQrbd3izuRO9aZUEad9juTs-YOZlxpwHwugCdvCWmx9mf8AztABn-ozdIiebxjBojvKrbil9y8sLHdIUIh4Wg-2gsdWqbOAuWlk7kxXJZFgTmC-b6UdVE_cNDJMmjTGr_dheVZOpCOYJWBhX3wFhQ9svTSkh7FD_4MV-DI3wKmWnjdqt6CDfiHw5_KL19JOxfwIpJOtPKXakHsTn-6oXH3uxRLI012ttsNBVv8fZu_X6dX0NH4Ca65pFk2B4EZKVEheLo9s5o_aH0JXrQHy8ESA7xOapCZ7BD6kNYeM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n49MHGVkSBb82EJ_5meoa98Bs3d-grzVYM5Tbr-gEtApZuHt_S1_eDc3CetjpSlP-u2LP_y5AWglZ6sjWeg_r53KhkS0qc_S33gRA4rQiUujCX5QxBEjl8NkN9sMnFYJljGgNTnnsgoR2cY9rsVg93EYTWUA0Moc17-gk-2UEwpgNecWBsn637jrdBheD7itxXEXR-BnrGA0UPCHGg8B2A6Zw4vGz2yKlJn5XRWFlLBe4Cu4AhMd5H0AjR6jmTMHg8DWxXKvdNPlQqIGjyAy4RypP_2KQ8kuw4LMlbANELKVJqZiP5euV4IWR845ikfghspj8G3v-7ahCNyY9HwMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgXVmd57ovxcj1_3_447tNNIWpRmN7OkuIByQHoYoDQa3iE-wphrHf9IC2en14yXnktZ2d0BVY3nAfYPbRZwL_qG4jVDNy0hJpezb0ERfT1DuwLq4hxonjJqFqxX3xx_Zkf7aQCaFPDkO-lyynCCHmHGKYCAMZ0snd_dVsyzSwV8tFVkQvaT_ri3zJ12HNYp5ZARuJcwLIjRHL6XUgXtffLPKbqdbWqCUvL5NpkNJxysNxt5AszPD6mMzImW5jPYuptBd-vvJnaarHxpjWmgpzpI7cot1Tj2w-TfHYEnyG56Ne9pRa-dcLVcQFHmlrMC9QtqfOrlpaA1Auv9VRckAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LszCRsPR9FC5RjgH-eZT_kBVqe0_WLl19PHVjWoXMs76397nVEG_mMb8OoA6IANXVPNV9afXOUx4M3aiVBv20cjXnvsaYS7BDHvuGmat0VFTTj_g3WFKvBoWo0UyW5NtmZqdE-hZ9OfbhFgrfpHmH3mgStp1O-oxNctCVTn4DV35Tvqv7inNn_ihOzgKDf-ze_9PrAD4Dn3TcD2JoUizPToPquW-yHTzBMoXW3fOA2kBX4-7_9ON6oL_hbkI9m1E6Rl7oPiYO9qTKfklGJTGdMudq8PEf8lB076X5ACm8h7hbfxUetLDwFHBusXsrhnLzd9d6cEl_Z_akw9Lr1Zgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=SzIW7z9gP0eBi3_KePX9gJ91mQp_ycyzRkDfzvqW8jS2j_p0h7X0N0GozKSj4taBZ-pDBm5HRX_pTKOgHkcB1_UDf0WtcfaZD3YFQPqzd3bpxzcD8qFveeRprW9xGM6FHsnxDkIRPkRuQWNiW24KFVLSZ7hwcK4R4xg-gSuC2gdXr3H-Tcd3FXkzJRfUg2IbDjE9ZG43FRi5w4D4LP2-oPB4fsVakUG98zcfJ18UqG8o4PBHdviAT2Mt0D-s96azJtmmRXKfk-1BuDnZ-Zo2i3pXOJvhbsek3QYZIm1gPSjVJXWfIW22T8RU3Ryp2CbPTV6qtLk1bQTAy_98reIZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=SzIW7z9gP0eBi3_KePX9gJ91mQp_ycyzRkDfzvqW8jS2j_p0h7X0N0GozKSj4taBZ-pDBm5HRX_pTKOgHkcB1_UDf0WtcfaZD3YFQPqzd3bpxzcD8qFveeRprW9xGM6FHsnxDkIRPkRuQWNiW24KFVLSZ7hwcK4R4xg-gSuC2gdXr3H-Tcd3FXkzJRfUg2IbDjE9ZG43FRi5w4D4LP2-oPB4fsVakUG98zcfJ18UqG8o4PBHdviAT2Mt0D-s96azJtmmRXKfk-1BuDnZ-Zo2i3pXOJvhbsek3QYZIm1gPSjVJXWfIW22T8RU3Ryp2CbPTV6qtLk1bQTAy_98reIZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2M_trIlmFoV0j3MnRs8oQB0LH7-HF-QGREFnL_XO_RexckwEFvWG9D2fQ7G2eaxNFcx_DZPoNgQeXg4tqkqwYaHs3Gtmcou35kNa1xfM6ojaThtoOR_Jmr7EuWH1jHdhNnJekRbOgE3f7Nx9IWJti6eIIpVd0jXBAgwa3Q2akBqah0waBie_Mk7g_3Gqg5_GgtLPpUdReH5869YpoSJbG8fN3v3001-fwKNtW2rWP1VfUE6CCn0TwZmzwdAQyEdv0JyKXteOrOUABSFIsaZay79l92VpTtWCHyjFn0lHnPWZZ-jREeJaJL9rUrKCQB_M4pSVcNILIey3vqAwdiP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3kkSpjoJs5uldFVxnju_7MW43oThwz0JPzBLqkJiEWgiBIqStonPRrNnphxY71_sUNnJbXyb_fcEu2oF2G00dDBaLSBuJlKbbuMvaWvOc9goqHWY8XlcOhaGV20UDSxzCQZurc-SaNI0kCG50QO1h0d9GK5J4_MLLBOXf4T6RVYhRhk4hzTXc1L9_xFT8ZFlZNwLBiJqtHhJdh439-pSrCoennNA-2c8vzZBVcD2eMGkG4TUM02-LDbdHJJW5ANsHMEpgz0pbGCPrIfJLMPsP71kIn7VAKUgnHdxw3tSYxuQf9nfnuDqKcwbRqRoTDiI0W_-xBGA3W3-gbsORq5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqo7dPrwRlwDlN-qgAKnYzCD-K-YxNwuuV7xFS0BvdKdfMZ_rOpKlddxs-IqySI2_DjEzt7rEW6OoqyheZoyUmAj8mCpyJs-doDTS2n9JY7Lnhs7N_VsceGXXOnv7XEqnhgPzey9UC8y0NWERXPeWfKoJ3uKGQQrnmgNoP_DALy3zGgQLeCQSKqpLWubmPz6WkZnLq-7HrtRzpbVP2BMRNRJt9MSx3ziBfuKimU-dwuV4JV9Z8YjWE4Fk3H52u1O07fqBojSlMkde4wE8FN4Hx04yUp2DEaw3F_nCOp2wlquKLzb04_vzGEIdH-t11Vf7KJkKBcIhGk2X31whRUFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKzNIIPiI1SgInPaDKvyg0dWn5esPRj1btpf7Gt7WXTvW6Y4eaHbrYiYeYt9FT0KkyBZ9vr32dDsT5D0o0SFtFDNeKrbTifXyKaKKzKQPNLO3n_xV1PEdMpTxW09EcmKyT6-pNEsGcR0Wea-OqlaCO2gZyCRs85pQ7IEeZ8lLhhP-fowaX44iNlaxUurUzwG3m637LfQN99_gmXOm9MBNdaf6y3l78teslgecLzJh5Yyt_osuxpjMgDqLf3902UGtup0BsgLiNGGakWNU7KJxKnSe6lK4wwaL2pRGWzc6t0iA6hHKEVu62UBOGs4WrTsL7IgzC7HnEOhwMDsntYdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkp5ojnQeUuhX4XtRPbaIWuhfDCmmRyW7sw3CJg21Z7bEOQbTwTsAi5FedwhahB1DNAkZLJIBPgZmqCgfpFizH1vhYdEfcbE9uunp0WJMoVMmvly3BmTQQsvQiWRgl7OcL5SVsdnFQozSNQ2zK_LoLC5Ts1S-QxGG_0aI6ky7D5AdNpR2v8NOR9Y1pKu3Ww8qrINnci7ep5eXMHXu1qrxyu_CckutMlRfo6SU7KjtqOqF7bi8YIXXAaGZTSTfKRakQSGAXdXohhR4O_3HKd9P69ZLVUedckn8Lr3hiZyTtWhfEc5YoDTPMFZW4bH54rbFcG_rNOyb9xazqZz3iRPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwEWgmCwvr-bvcn6nfGvPAH_-VvHM8zUDOPEUkG2sO-x78vPOw_DM2478sdBag_skkkQkeJQNVmuwix_RAZuKKOz-r1O9irWxyVZ5g5miUOZwCgwLTidNeBtvXOgDhJeI4-TZx-yWcCr4QCmDO8i7XioH8cwCfCJ4nh724avX3uYw_yKrQE4_OShQ2OIqYQJt5XwBDOpXVrxAar1gIgA0Jqw-RifQYRwLJiufhxKLywY28yGldgWjzEgYsFUw4J34Gmsz5_RrxwNxO_p2LtMyflxM61XHwKkzPsFjfLTvOpGEKPtJoLLqP58NxfQQ65ubgE8BPsRmPueJ708IwWrAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGq2UohZzUSImg7_vDn8BlFnFyXRlmW5Xja_ALqMCXJrnp3ETJKejrnacoosZfLKd6kLyFpI6A_9Gi6uOVbqN_jvHWfhOGUSUTMaVAJYoLSGgsURgNDwGhf68Gv9wF3gJapUqeb7L7-GrdfkTNmyisgf3ioufkIKb-vw9MksFtCmp1TuNlOIhAYIwIZhmuRgPjzNF_KN_1uR5JhzMOKtIbwmhuxFuMWwtd9UP1u0b8ZfOt0tBFIRYjyhYEYCvVuREj4d9GjdTUBu13RfYPEQ0epS-5ckgQNwie-1MGr4HPY3f-S_70Th_5-WoSUokKAUWX10Uz-DXmCvc1mBs8USyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV7ZgcrFQzZjbORaiEwjzrSY83Sat9TKJCBSpagA46117P_TmH7rWCfKjXTN0B2u-vNEAgB_TDRMP6FHsh_PVjiXDeL127gEYDryelfg2EVd8y-dzb1NgkJ1aYd7flSmmbST4DdCWi8hJjTpSCRxFxtjRf1vbxQN6Vbqe_rHM461FbJBqw6cOkH38BHpHlP6DvhVzVeeI4CydfgfNBssQoB23c_5ZN_8j_4iZhuM0kggiMEvoe5sKJ5aukQad0At6xPqgU96tmD0M0g7a4luF6uf6OQdknWoKtX2cap0m4X0FbAlQ-JUrJFiVjKk0rJ2FYg9vxaX7rbzZR1HpRigaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=p8Cp5-YnpFZMmQ-wpjbde0hex1yPsYHuJ6aCuJ-JJ8kiazza8EO-pSdx2JacVM_ht-AcY3hpisn8Xwe4LOD9wBwm-W_B3Sd8WTQkSegCxxvg-suJKBMaArm3MsoehPtXYILmr0GwDVXJ31DL2x-isyfYPzLuQc2VWr0W6v3cxPu7QTqdDPkoMPzggRK5-WAjbhSrlC3Hi2FkCybaa-PRpUgR4N9CtaC1Jv5Pt5AT2UEh2UBmFav4NpO_1CsifYHwomlFigy6z1EvJgCpptlmLsjC1BhOiMK94m8ElxJQG3SH71dkvZjpfFQmG-RWqHN4jr7mw9OrV62zGLOza83Z6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=p8Cp5-YnpFZMmQ-wpjbde0hex1yPsYHuJ6aCuJ-JJ8kiazza8EO-pSdx2JacVM_ht-AcY3hpisn8Xwe4LOD9wBwm-W_B3Sd8WTQkSegCxxvg-suJKBMaArm3MsoehPtXYILmr0GwDVXJ31DL2x-isyfYPzLuQc2VWr0W6v3cxPu7QTqdDPkoMPzggRK5-WAjbhSrlC3Hi2FkCybaa-PRpUgR4N9CtaC1Jv5Pt5AT2UEh2UBmFav4NpO_1CsifYHwomlFigy6z1EvJgCpptlmLsjC1BhOiMK94m8ElxJQG3SH71dkvZjpfFQmG-RWqHN4jr7mw9OrV62zGLOza83Z6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3W7yd6Kj8zfbT0SWbVhhxiZ2ns5AVOf30nkS-jo7JCg-yWRt6vpdV0IxOHPW7b5qw04p1j3vAb9jr46twk31WqR3BlQYTsaFCeCHxZ2qTrpaawUl0eY8PKKwS_-h89x9LD7jBota_bwMyFT-k7LOMdarctgrcK_6X1WtwOALwM7CROaUikUpJT55dr3Os196N49uFwXVT6nJ4P08yAIdoZpzJ_wqI7mk4GKfPgIFrZIaVIYH8huXCAby5MWzcq4XhbYMiP1eRxi9K0UCtDzCjqav26a4KqxLhcZ9dJxJT9kivoYfvPyyGIbfz4wn89ouDno7PmsGcrdNIEJBFqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huRqKb8X7ENq7Qg_Sqqyvb_2aizzneuf6AP8QBnQBw6v8B5J-BggUTXhHeGpEucLZ_7qMfrDEanyod-IRUydbwpN2-YHn3uqV3hBaBHJPDI3LsoQQn_oIThxwnNPlsurm3AZnSy7EjrJPj6lvfSVLhAih--92CUQbJ817oWcZKJHPn5PwJzgRUeTIfyQGA_SGd4HvLRrCpaigT7QE0E26QpTghAOHytc3BwRyNRjAuv3EUB_IwWd9Djey5dr-tV_JSpgI87bRs_1qecgzo7ctrJvQ4iSWUpyDpUPHJ46mlCn6ZbgaYFW9d-uufiS23AX0LpqD5obZYE2AD5EfsLM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqKZGV2x306eItvl2XFys7rcLqIMcmmZiK764ev03RZbALplzwbtD9pe6zKRlP8cMSJaZM5DFGJIZArdsh8Cj6IQm49hbpdjHq1GEW5E4zaFNrcXlo3urwFPfvNvf0civ3LO8f3n2661fbMshUR4YevvgiDsNgAsH7ZLGKxznh4RIFIXq7YkbEypb-S7WkiJrTxOYZgcqPjXDnXvZa07Ri1GhT1i9nrCf06q9JEJJvm3-DuOjU_j82gt9GACcTM6xWYkA-AYmUtzux2FIHK8oapqiPPE0SL_aV0D0mjsCXXgxTFuLSvYva-rYNWTjdXvUaW5dptE_KmiRjN45Xwk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO5XVyAwDKQAFw7N3_fnP7KrSTvu5hflhVCIN3h0kebWlI10JAN0dfNGTnNXxjuUPOZpl5_1R5Qa0ThUomOqVr8VMd6LFLWNnULbxjcfnoG3XA_G2Mb915e9T0t9720ff1Z5hxmTdRd-yQ4JbG9aREhMPJJ5-WUaHQDoNyngDsRBsMiU5LVm5UAqrETylgvIZogT3Muc20XtHIfpVZJ_hLYzDXKAfDJCmSsw4MPmQX3Rt868oq9iMzNCmY8FCHuDvCiRrKD7Ea9oWpZzTgD0ABfXCEhLrWuwPx2uKTD4HlvsGbdLxr_T1EottCqLF4-Eb-M6hWFlm4p-wxh6MU6qSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1dhExya5Bz2da-8FvvE_P6t8Wvkq3DeqnqQyh0AGGpkRWbpMPE28z7thMOBbyfhPaLIgXWrfsKQjKGQoGeq-Y3l3knvOu_c2oTFPIR_ZlMHbfoQ2vuLZO4PjWxDalZyvy_dVSbzWbiYgLYEW9m1q2xV_kH8o1VNLRUqTEUWAPk721eLe2A0vq68DM9R3RSvWw_R-Fdm14xUCQnXbhFh1h3NP62YYjwxnMX5dX9QEaG2lGcFmmb1KtJ_nInfpulj0uHkIB39Uc-Ta8QX97jnXD8wV_qfamTDEDYAwCAJfmZ2taTtVsZHnmNrGiTxXfopAHYwLaEzfx-mSu4tCtezdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfQJZjD7lu5XGKRzdgQqY6Xsy4PW1MLlZnoAHNZulOUxS1jKWXStigHLammX9UFC66knKaeuXgQYFPaVPfI0R6qmfZ4VtRj3GyVX_pZ71cPSYkZ-2Hze5jWmiwjWEclrP0-h4MG4F4u_Qd-hZmIEYiYv5SSD9ngVYu_Y4PbHSK3Wx4lPpCnqruiOiXTNeH7gtgHovqDj36rsbeYOPE1KDG6cXCmJ4WTQ15ZVFDZwIXE5Po69DG6gmxt3zZuSAmh7PsXE2Tn7MbAdGlkRKwy8D67os9vC34WTDduys-bCrYNVF9Z7MWnWZWx9sXwoXIS_bI1EjbYAP_wGbce_StdZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucAmcy1eEjf-YfKRxVCqtmyXk4ja4txJw-tLxDjK4tyL80aqX4AvyqKQZ1kF9txMQMqxYsgoqAu6yhdDa7guTrnecdPdPgFad6hd5aizu2z_NK5-FKDl5YtGHRpATwGDlBGPX8j-mJHLFALeGCQL_DVAn2DykD7YKovXP_jYA62kRILb5FdfuYyvUGNHR1OiRqmO0Eq5jntSP4JiFyWtN8Xh8NuHlmEyUxxgFvCeQMn8zNHy-efWsjKt1dU5w4jm2ShwGo946iaozifVOH7rAPWgIRVM5MeNM5yex3CvSafu0VNicHkObPchjknBE7pvoJAzxahE3hI9Nbp1B4DKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx3OX4ab_QK-WC69uGh0eniujlaelPL2sJCIBGq8h5d7GAX1P4DOBCLn5f-12hjwbioT7vDOM07e18wExXoQHKxW0LqkeCDGOZyVqquYzLVfyXTNhnqCviY_ZLxyCmY7F9UdRlqoNNEZsHeiAQlYgFHyhH8ZmwdtiRmOlibO-JEQ63lXYgB-LTGsb1mHco8dInijn0669ysO1uUEXMzDtHhSknWhfyFkwxp5GrIrQkoDvTbFqhsMQdptMEhg_aIlnsxuOGFd4dH1qaZ-gNbyhcGdOcO1Qx072amH_QPttVwBwfkEeI40klhYhAa2u8Rc3T1QoK7gKSmc8qzm2utFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhoDz2mLQmNgr5P-Ey79Pw16U_aSAB2__KlMc3m2v6BHDaOrW90gtF8vfBi7fwa6-kem2GJdLUSw0ruMDszyhr5GFal7OsIthdbAnYtESr4cyQupn7lCoWX1gpgcVEOKdCWvjKTiaF186SI2tFkwHHCPGb6bkcEmzBU803I7wfdbdWqcECtOAEfWc3bjh2WDrBG6njyWXH356uE0GkM0tMkhhE_CZhtlzbRF_vM3wB9E2Gts93OTCDoOfqISMT7COm9-Bmt8sspT5OdO4q-m-s9mpQGz6IpbUDk0ICqFF0x6NnjdW5mILbZe36YpNo5Fb_POF23fG9GRcZ9i9yPPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD6f9H0sabd9wOGUzUwm3NxZUtRDLgtYpNEkbzlKWKjoEWJda3Jbv-1QIGf5X5Oe677mjC-5lgUGEy7zBtIJdCriz3SDbmoUr-KEwzwAqfJ6nmt55iVuwQ_e2pcoDkc3QRyIVn7z_ZRcW9XawN9qpqTSu0EM_3LLIcWGcBj0NhfMKfqjP8siWqHdFZmjWjpJTAehMTd6HPfwlNkefXiblnsvzZcw6a8x8JtCCJY-83cWLFoKwFrdfqvm54QBxE6hRaEGHEGaC3RI8WiLzMc7WunRCqkzpDOgaUt17NwavDUr7V2L7yVAlohP22nICgWhfB-HURBv83fwXJPkR-2Tqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=BJ3rxDYrFNNt2MaWyEwxJ8xjs6nMzD2PoFlbWJnyvuwwzKGH112gEQf3cB-jgwqv-4AcJhuwNf2V90c5V-7nDQtojuDNM_37HKCHhLAbHVXELOfYKgnHE-_vLzYCe5Nc9eFEwV_2EoZDzKU128JOhAS_qal8FHXwjJHiD01d6QNm2koKwtZpNkR6pcCg1_8HveKNxv5f-Gba1ixtIm89EUmO9QY-Y-flxB6_b0_mCmvRyYx5I9lT8jXk723NtZ7eV8V9XLzibyED4rLx0dmszItvdQDp3GkK3WN-r2H8yxddyvV0JjkfrDYF4xUqDkMTciemCt_aAHoyBr5pAijMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=BJ3rxDYrFNNt2MaWyEwxJ8xjs6nMzD2PoFlbWJnyvuwwzKGH112gEQf3cB-jgwqv-4AcJhuwNf2V90c5V-7nDQtojuDNM_37HKCHhLAbHVXELOfYKgnHE-_vLzYCe5Nc9eFEwV_2EoZDzKU128JOhAS_qal8FHXwjJHiD01d6QNm2koKwtZpNkR6pcCg1_8HveKNxv5f-Gba1ixtIm89EUmO9QY-Y-flxB6_b0_mCmvRyYx5I9lT8jXk723NtZ7eV8V9XLzibyED4rLx0dmszItvdQDp3GkK3WN-r2H8yxddyvV0JjkfrDYF4xUqDkMTciemCt_aAHoyBr5pAijMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=RTgP5ET2j5O0luyAYkGwf9pUQP4eAlvUrwK4WfiafmOA78PTv-WaWFHYBi9JEPqzYc_PH377wVcV022l1V1Uy67xIeJGMVMaWmQq-hPvHbEpeFuYGf67auQMOVulQvMlk9-6U5HzZyvE1DDbY4HoQs3StZ0uwCUqQf81HTDc8S0OL-_Hq9h7d9oiwvxC7cigEOgjoV5CQDCrs5oNg81nc7-yFqNZG4LV4SC7pN2hSBHqT-Qgh_AZxTgXR6P-yA5X0VPTmf1QcasxxkIXaqz8A2lJq1bVejtueOoiOMv2hN02V_h_N8avp_FLht9DHC2WPggib6vONie4msldJq5Tow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=RTgP5ET2j5O0luyAYkGwf9pUQP4eAlvUrwK4WfiafmOA78PTv-WaWFHYBi9JEPqzYc_PH377wVcV022l1V1Uy67xIeJGMVMaWmQq-hPvHbEpeFuYGf67auQMOVulQvMlk9-6U5HzZyvE1DDbY4HoQs3StZ0uwCUqQf81HTDc8S0OL-_Hq9h7d9oiwvxC7cigEOgjoV5CQDCrs5oNg81nc7-yFqNZG4LV4SC7pN2hSBHqT-Qgh_AZxTgXR6P-yA5X0VPTmf1QcasxxkIXaqz8A2lJq1bVejtueOoiOMv2hN02V_h_N8avp_FLht9DHC2WPggib6vONie4msldJq5Tow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGJcJbSlyUI-mLJbQY4RPdZMjaNJU41ysUm9fO-5ea6uLxJ4GtJbJ2z7p_V18BBvwOVbnXCW31BVZT0bvhRzH34uqnhdws-C52wcqDJWCXMZ-XfVayGoSwQ94_gvCgwX8Rk-gW81e3-xyrp-U9mO1cTEw15sQtGXQTBlWBls2R3_A1Vg0PIuWJ5yGdb6Fq71I0MxATXdFZv5C2z2SgL4PaFX9LHzpk-q8hW7jLW9yG-G3tomkH8AUwKdgamGznL42Z0TrFADzATsM1kl6cYCJCs2_ekZfCeMwwKPaTDmaY_EQZ0OZgArU9wFuSiXDXpKILHoiJQVJv6Wbx6o_TpOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsQcxDS7eSWvz1lq9zt5KBcyG5jVdWmJnri54QyxqTzOQhEbm2Wy6oZxyLn5V_KXD3M7CASlXpf1wJWn8Br1qIPOvXQx9iMgy7cz4Ac4VhF3JqIu_dPU2Hx0Ir6ixUwcc09t91et7hMQNUsGbYrf3BBCz4vKps9QVzeUl8cQie2yJ1y8O6SDlVBHaejYTuQsWyq1Sg_0Ky8AvC32qi7JOGIvnXeOp9rKcC5OOuwMcpccKessNqasx1CVqmjCcu-ZkF-Y_LU14aT14SBeRE-oDnntr_5nuI95yoOhXUXMpIO3anOG-GmEEXV_mLKD5vHxyVGDHMe7AzI1e9AKjF1o3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
