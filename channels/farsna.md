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
<img src="https://cdn4.telesco.pe/file/h2tjply15PTLXzwr7pu0qEV957XkvB22ZlnthkrZF9BawlCuhHm6kYYYq6bwozCTHCU1uBV9ZbMCa5Wxh50_ThHC-UpWTT4A1t76eSTguaF-wTfYVDrXV4X4hJcnnlYjJHQl4WRE5sebln5j2mvGPZ6V8pzLFeZaC2PM6MebgjdkKsNme626Q4RRQHE18pFZ127LBIBP2DOArjhlydEoNPiHZmsVAR4WkAGvrwFUL1Cu098W4NOw6nohbhmb-fyb8bwxqRo-_1FL3Ho3AntLHdwOHyLFCD1T7k0RSYK94mu1yr9tzy6CBbgM5ReAvLu1ar0SvlCKqDcU41gh18RseA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-458755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1G_uiM2rJFFEEPxRipcI1fFuNBspnDIlWRJQp17cCo6dkFWjKf9yGZkjhJL7_q2feKZGggoAym7PtGZayN0kSBt59LKIR-pbHVIkuOvP8YxpUj_knk5uLmgHQ5Dnt_bPxAHnUWpZ6aBEHHv1v19XwRUr6mgb5hOpDPf4apW5IeMUBzkPUlv_dg07h0zTJS2u17Uix4G9Nnqtvedsp9KApePsIYLWz3TkZQU8K0FjEYhp2OtCZiRWZ8MB8fjd6moHlqeF85UDp35tBSwjA67EhBqxa86cHNK_KfgbeegmAVkvRfUk2qABEPwBjcMRVBKtDERDgPmPitQgvEdGS76Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/458755" target="_blank">📅 07:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در چگنی لرستان
🔹
فرماندهی انتظامی لرستان: عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده در محدودۀ شهرستان چگنی طی ساعات ۱۰ الی ۱۴ انجام خواهد شد.
🔹
شنیده‌شدن صدای انفجار در بازۀ زمانی اعلام شده، صرفاً مربوط به این عملیات کنترل‌شده بوده و جای هیچ‌گونه نگرانی برای شهروندان وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/458754" target="_blank">📅 07:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VydKff7BOJmx7ZOx3Duq-ZTAlufygJJVWvm27pLjRyZih42h1GuOkOikD3QyF5SyGr8m6HecMMWXGDb6A08JIbB4u3SFuqL0AC0pg6shULHiy29HXKdvF77OXIP_dkUcESX5fieiVuQrsBF3Fsin0SOkzpU8YCSy0xwueyaZjiB85N_y2CxDP-qsT24MtoV4ewof3YueFBgr9W0mHSLcRC8Mc3tuFKunOesce9z8Y7TqpYWp2KcDGASLPSQZJ1EPOBMFZCNin76s1pIxllHKwjzm8Y5u8pJbSUXts7YB-S-nV-mqFe6HfONXW51gxFtr04blFe8MMN_Mg1zuWS8zbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال کشور از دوشنبه پاییزی می‌شود
🔹
هواشناسی: انتظار می‌رود از دوشنبه و سه‌شنبه، هوای خنک بر بخش‌های گسترده‌ای از کشور حاکم شود. این افت دما به‌گونه‌ای است که بسیاری از نقاط کشور دمایی کمتر از حد نرمال را تجربه خواهند کرد.
🔹
همچنین پیش‌بینی می‌شود شرایط جوی و دمایی در نواحی سردسیر شمال‌غرب و شمال کشور، حال‌وهوایی «شبه‌پاییزی» به خود بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/458753" target="_blank">📅 06:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d5ce90ea.mp4?token=REyCM6mwZ13vvcz0MsTnPI6lC7h6QG8ziIt3WnnqGBg1UqIMMeT_UE0x0IKZCK1OuGIERdJnX_Aw03Kp4I-MBuFZF3JDQ35GUYK2FMXNU7lXfxLZcYem8k9EGmwJvzqc4Ajy_plBdzKgwLm_fd-YuO4o1nE9C66TbUTqEOTkEF87NDe2STWtoDE_6SrFBHpPDwMjk5JWXG3tM2jIZ9frdeviuN7y3aRhJLyh_9vQDeXUpUSNnjGdEQMPQMnfEYtd-xNNq1cpqZEZEPEsZIKPo0y-oz_fdc4xIzI-udyEsqTSmnUAU_vmPKveZBzUU-gYaYJu62YY23vq5P_v1wS9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d5ce90ea.mp4?token=REyCM6mwZ13vvcz0MsTnPI6lC7h6QG8ziIt3WnnqGBg1UqIMMeT_UE0x0IKZCK1OuGIERdJnX_Aw03Kp4I-MBuFZF3JDQ35GUYK2FMXNU7lXfxLZcYem8k9EGmwJvzqc4Ajy_plBdzKgwLm_fd-YuO4o1nE9C66TbUTqEOTkEF87NDe2STWtoDE_6SrFBHpPDwMjk5JWXG3tM2jIZ9frdeviuN7y3aRhJLyh_9vQDeXUpUSNnjGdEQMPQMnfEYtd-xNNq1cpqZEZEPEsZIKPo0y-oz_fdc4xIzI-udyEsqTSmnUAU_vmPKveZBzUU-gYaYJu62YY23vq5P_v1wS9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران مزار نورانی رهبر شهید انقلاب؛ ساعتی پیش
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/458752" target="_blank">📅 06:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m69dSEPNxLFFF1Au5dvuzsAmUrGoeOZLTzUuI3LjoEFXFYvkhRnt0ldx5A0lrpE72a7OKGvpSlsU9BU-sznSAsTrkraJDiSRx2Xhuy-mgZzPmD0fv06_XtHq1UPrcG6GN3cvNBkSfvDWddNxqR4NHgU4Qzh0ck7tIJTyQparlnJ6Md6EEG2E_XF3ntmxemfYqxkzyOzhX16quB5gSJdBehNCiddRZqNLVTwYbSZNQ-IhaVxXPn8GzjuCexrviT5vc9mFQUEfAMzYkORs0mK5s6jPwuCIzqAlHH7P147y0ZNSnxEUkYAdX7n4M6O57TtQqchzciWF7B7mERt4feB_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXWnBV6X58h39o0j9_hbx8M68_lhhmAMxCiTNHIi75nQgy0sG5iFD0jcy6ro-8YdXj2TLBns6KDwkUpNqS5MzhxRpLwQwuUIo-AHB8ShiTxgO7q4xsHF2L-KeOrg_EJUyxvl3pUkcE2jeW_hOzIZZShN_m3wlw1UoDys2PoiZZ-Xmx6-jXiOktBGQFUbainZoIV8rKULtJoaQmogS9mHvfGSF9N5WzfBVpBS5-Q59lpb-MqAiSoZUNg8bYmoSvJwFa5Af-qacYerVgA8EcOwskClOphY5FK8EG-xn8tVj7dbUl90bOQ014494vnEY8YgGQm-Bb6dc4_mJdHow1nylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی امواج، پیکر نگهبانان خزر را بازمی‌گردانند
🔹
فوک خزری نگهبان سلامت اکوسیستم خزر بار دیگر دو پیکر بی‌جان خود را به ساحل بابلسر سپرد تا نشان دهد که توازن حیات در این منطقه بیش از هر زمان دیگری در لبۀ پرتگاه قرار دارد.
🔸
با کشف این دو لاشۀ جدید، آمار مرگ‌ومیر فوک‌های خزری در سال جاری به عدد نگران‌کنندۀ ۲۷ رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/458750" target="_blank">📅 05:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSRVJFWW80EyIv4OGFnt9alQqTcfEYsIG5XgebejfghOtVC6L_zJ0qyKzmJNxCsbub4yTPjoPInt7HdwJdnmbRcHq0a_0z76lGtWYVUmwXEQ5XALsMWg1PnwFx-lsYGLCkf7_YWwfiTh1jZHfJMym7yCPwamuRP4XIVNizTBmYRCbaaKt-JzzmEp0Va_vnEwP6afzrV4H8JVgfKQuQl9q7-fnIHPJpmsyY1YlgkL7i3WdGR_QGFbeUOBomGaArpnn6mnnLumHt1_OXlJ7ufKtyC1lKsjuwVPJw_ql_6QTgLoGpwTAzQ6WSojGmOLFhVSOiiRMtQT8fogVllzBvEhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازۀ نجات تجارت ایران در آزمون کاسپین
🔹
در شرایطی که اختلال در مسیرهای جنوبی و افزایش نااطمینانی پیرامون تنگۀ هرمز، تجارت خارجی ایران از بنادر جنوبی کشور را با اختلال مواجه کرده، نگاه‌ها به سمت شمال کشور و ظرفیت‌های دریای کاسپین دوخته شده است.
🔹
در این میان، شکل‌گیری آنچه برخی کارشناسان از آن با عنوان «اکسپرس خزر» یاد می‌کنند، اهمیت ویژه‌ای پیدا کرده است؛ مسیری که می‌تواند ایران را از طریق بنادر شمالی به روسیه و سپس به شبکۀ حمل‌ونقل اوراسیا متصل کند و بخشی از نیاز کشور به مسیرهای جنوبی را پوشش دهد.
🔹
از سوی دیگر، خزر می‌تواند به مسیر مهمی برای واردات کالاهای اساسی، غلات، نهاده‌های کشاورزی، چوب و مواد اولیه از روسیه و قزاقستان و در مقابل، صادرات محصولات کشاورزی، صنعتی و ساختمانی ایران تبدیل شود.
🔸
بنابراین در شرایط فعلی، اولویت باید تکمیل مطالعات و بررسی همه‌جانبۀ سند و نه تسریع در تصویب آن باشد.
🔸
چراکه آزمون واقعی خزر برای ایران فقط این نیست که چه میزان آب یا بستر در اختیار کشور قرار می‌گیرد؛ آزمون بزرگ‌تر این است که چه میزان تجارت، ترانزیت و ارزش اقتصادی از این دریا نصیب ایران خواهد شد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/458749" target="_blank">📅 04:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7c0c7eb5.mp4?token=GezJzLDZRTY2YJ_M2WIQ-RO6GjhkORRAmi4RDCF2wAkL1oLPZmZz9J33HOZGTXBKa5Wwi_6ijIfP7wq9h-R7jnNFA-WC8b4SGG3SDOn-riwSZ1BpovzQ9_0XRqiHPY-vaKlYxUkd80ygQIRAHtOKpGslmYgicu5kTdP2PxOvxF50QVh69daBIbiA1zELXSonq54L9KIjTHwH-Al3zr29HeWQRIAkEjJ-_J3pEywEFuSGtmCbKJPuiWf5XR29KqPKGQzUelZ4n8xelZrDj4H2h6Hdtdunsf59ZUWWPzjAEV92D-T-jc0ax1L64X9M-j4_T9Gb3pbctb3nB2fDikWhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7c0c7eb5.mp4?token=GezJzLDZRTY2YJ_M2WIQ-RO6GjhkORRAmi4RDCF2wAkL1oLPZmZz9J33HOZGTXBKa5Wwi_6ijIfP7wq9h-R7jnNFA-WC8b4SGG3SDOn-riwSZ1BpovzQ9_0XRqiHPY-vaKlYxUkd80ygQIRAHtOKpGslmYgicu5kTdP2PxOvxF50QVh69daBIbiA1zELXSonq54L9KIjTHwH-Al3zr29HeWQRIAkEjJ-_J3pEywEFuSGtmCbKJPuiWf5XR29KqPKGQzUelZ4n8xelZrDj4H2h6Hdtdunsf59ZUWWPzjAEV92D-T-jc0ax1L64X9M-j4_T9Gb3pbctb3nB2fDikWhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمؤمنین(ع) در آستانهٔ میلاد پیامبر(ص) گل‌آرایی شد  @Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/458748" target="_blank">📅 03:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrHoGox8ayQSlke8vj-8H2NzToHg3uxYQ2dCscOFdQCeznx-g7iSueEORWAlOqMC1SEVspWL3878LBL4SseQtIXAKz5OA9sBlR7J-xlvMkU4LNKyumPtQAS_qyeN-OHI0CA4UA1DTwl9SESB2ZJpONDV_Cr_LoKm8J8HQRkaoySn2Oj4PU4V4xnTnoYb_67EYUFiKMnErcGxFdVMoon9nAovQL6h4UsVD_-Vj0tXDndedMafjEokOn5o8DsRPCYYkZNUb8XW5dL-rdO3xN-hk0BIO7VH2IqBCLc7wvdjKtcwyPykMCSfjbClq6Pf2TwSkENQJHVazQOuGXl0S-jtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایدۀ عجیب چینی‌ها برای ساخت عضله
🔹
پژوهشگران چینی روشی آزمایشی برای ساخت بافت عضلانی در بدن توسعه داده‌اند که به‌جای پیوند مستقیم یک تکه عضله، سلول‌های عضلانی را به بدن تزریق می‌کند.
🔹
آزمایش‌های اولیه روی موش‌ها نشان داده این سلول‌ها می‌توانند در بدن سازمان‌دهی شوند و به بافتی شبیه عضله تبدیل شوند.
🔹
نکتۀ مهم این است که پژوهشگران تنها به افزایش حجم عضله توجه نکرده‌اند؛ آنها بررسی کرده‌اند که آیا بافت ایجادشده می‌تواند مانند عضله طبیعی فعالیت کند و موادی موسوم به مایوکاین‌ها ترشح کند یا خیر.
🔹
آزمایش‌های انجام‌شده روی موش‌ها نتایج امیدوارکننده‌ای نشان داده‌اند و در برخی مدل‌ها، این پیوندهای عضلانی با بهبود وضعیت عضلات و بعضی شاخص‌های متابولیک همراه بوده‌اند. همین مسئله ایدۀ استفاده از بافت عضلانی به‌عنوان نوعی «عضلۀ قابل تزریق» را مطرح کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/458747" target="_blank">📅 03:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biV2YorEsv_z2XHJFZS3vjMHHVXGtdthdEvFJHyyN3uP8ceEcyfwFRV2duUFz12-4d8ns6DHQZV7DeIuiBz2_QoEhStsXTFP-3b4xMVahZMsYcGRFw3Pu2MnW2DIO-4vxORlD-MQXaWvXJFdwp8l1W3u3cyoa_Ze6O1t0pKvpKXijcgH-mhpsq7suFs6WdfbjC50fsFccETbZpcadXV6a3D3R4DnW_XWP0K-4LF_2xu1ib3r2kYPWIIeBgf_-CX8SDiFhY9whdHnOcwOMzFU9Ayt_88WJOFHjXwETCmUPZ-EzjgzuPJsOvinaP5EUxbAr8WRpv83ldYhBlDWI8d80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداردهای خودرو از ۸۵ به ۱۲۲ مورد افزایش یافت
🔹
رئیس سازمان ملی استاندارد ایران: استانداردهای خودرویی در اوایل امسال بازنگری و تعداد آن‌ها از ۸۵ به ۱۲۲ افزایش یافت تا با کشورهای جهان هم‌تراز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/458746" target="_blank">📅 03:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3bn-1hClKCjOXP5OGKqGgvusTpAI8HpFKAzuZqRd5VLaRioMlgiya9Z8gUFMmJs0IATDVUuqzn9gnKlRPsP-KPTQ5SoeTRQFdv6F-UpXOB4vYsJmU7PzwT_hGhg_Podzy9-N8U8GbjKrZoLYKBtm6XsNGKqiaALx0O0sGIWZH9JFVgTMyvpgKGY6JKvy_YfM4Y4omy_BgrcPpRf5dWM8Lcdw_MdBZ0OVeNRaLKnRX3TAL2g5wxhCQiecmMG8KVHuXxO4N4jLzuA5kHIb7rRPwAZAC6hMocaUzIWA5wO1q2wXDniYxRqKv-Ivf0ez-omE6pPoAdUNlnzo-poSNTs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: «بزرگ‌ترین قرارداد نفتی تاریخ» را با ونزوئلا امضا کردیم
🔹
رئیس‌جمهور آمریکا، مدعی شد واشنگتن و ونزوئلا به توافقی تاریخی برای کنترل بخش عمده‌ای از ذخایر نفت این کشور دست یافته‌اند؛ ادعایی که هنوز از سوی مقامات کاراکاس تایید نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/458745" target="_blank">📅 02:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4pqZdmqKzaFbiuNXKAQZAryrX_g_Z2VuP2RwtT9NFnWzyOIaqBgs72nrdOfIF1yEjL842oo5caxawQMMVqfzuLFw_pkmJtTgjoQRP-EgIxwTzG0Ee_shzRjQuTViO7G8lNul7oDCTmTdH3sBN6DKGYEcQkJfvJbaFigvre9lD9_jHEi5YFSm7WuCTs7uIesTPxZExxhL9OsaChkKy8Pv1bpchusR-9JOGGftZGpjmmhTNqfPVI4FYxZNR0sYIhK25wHOvUvPdYQgXaJKDpSEdD9ty6qnXGH_J0GCIswkMChxpferDyjS93Q3Ls4nrsE-WYVNcOfKN4_ZGb84uY84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا به دنبال جانشینی ترامپ
🔹
شبکۀ ان‌بی‌سی نیوز به نقل از دو منبع مطلع اعلام کرد پیت هگزث، وزیر جنگ آمریکا در بین نزدیکان خود احتمال نامزدی در انتخابات ریاست‌جمهوری ۲۰۲۸ را مطرح کرده است؛ البته این تصمیم هنوز نهایی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/458744" target="_blank">📅 02:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANEdBqGSbGcga3w7ajwo3t1zdUZehAQx7XCDZnG72IbGF-NuZ0J4rL2FDJz1WoiNP1DUujzbHK4hwr6r36P3zLyk56nEAVbmQoPzsYSxNIjiqVqqHJhMCA77EROmcpqDfGk09ReA-OkxzHyeJ7mKt1wRNQgsnU8qHhOzN07ixkYGvveYrHPn6jjjy_cqSDQzQT614J9zBImnXSTlFn5SQRSWGlePJj2GMShMEdpRDkhCZ_iMyzJsoHeDVPMa_cSeJ_28ST6g_w5TFgJuAlT7eKkRZeZZi8C_dPNx43WCDkIdi1sIhbW7Nh5Ri4IpuLY9YzWSm_-R6P8rYU1kCcSPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNtp2ilq_LNSwpDdmN7ZMqOrJUvdTFG_hpdkv_jM6Ng-flTkyhWnRBIsQJTXqRDLfNdmTgeWi5L3ZJZxNMVAkNnqALlD9DfoeMFxnuO7qYTVL1W6GM_E-bedrOmX788XRn-z_NO43AAUPLw7rpr3pzsQSGnDqZeJElZTRTQtUIMQvlWVhtA9t0H-vvwJk2soIXYjXmP2DpKdgHzyB6iEDN0QjLZyIvpCN8UDxbJQDTZ3AgSWdYJ4BAiERyoAo6kMNdSyLZTnPv1XOgYjKNMwzh4Tc17-DhXGA1Q-Tce-8WR9ijWja-B-Ec_uCgZ13A-azt5SnfyvEdSGcCQR3lRgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AppmNJhUuw5BCkU8O8o4M8CRc5I79eEuMvyhaY77jzUKOHu7ZjL3WerU6ahYJRPD7JHvcK9DmReOAzCa0FPlUbNIOrMO7BAKpA_uli7DU5hDeURCKJMx231Qd83yBe58z65Ujs-i-LjsOZykv5q6pgA7y6QZqwPAwcGhj6fwteATwQhvp7iwHrMjdU1RPHZlXDCRjfRRg9rCZTCB14gaUZNT_dv9ChM4cMCQJaHd-UVEgVqMmFF9WXxfzPQHtfLeYNGqSVZP0YBE9jPeSEOrLQ1SXErn34ifOB2OlOVoLNxMJQPc7pHv2Jb-NrUzAJ3XNEqFv5ZhP3FfR8iJtqzlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l57inzlGwEPtkpNwJLS1n-RF6yOSSAaFQKY9C_CCu0HJeGNq6w87R7iHH13dhiJb2mLcf8IV62-eVQGjCuWh_yK6c85AUw3vjlRa6SL9S5wTY0w_Pes4y7g8MStYqH6dijkURl9PO7TmPDMUPwvDZ4gGdVZREjubTIJphZP-HtEyMmywKjVczNHk8rndWBnpwk6Fvw7xtK81Kez9iNShQihJJlouFcQiiZc_3p8k7eEvmRV1L1M3ihx4TSR2ykT9ABhAIlSK1rpG3AQUemM9to94GShf7oUqzbg672VVcUtBJ9ZWjzlNJuQnZIBbwItkhNSWJGIIgPJXNNQXIqc2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5dzD7zd1ZauHQj31XFuL0asSFNcKnAYiHO80VHcM5bylJf6LLQ8JG9TqVhLN3ipBPZtOlBPnX8lwE1CjSAK3fFpOd8u_DZxfUd-C7IfqZe_vF349DrotQksWCY1KJq6jk0tsrvFUD1A25M1h-way3y1wER2O7gbF7kPxCfU8kO0G9I-6GQV9He02umG5yT_9X1yexwX8qqqmMZvNM4HjAIe6SdLAddL-hSz-YsJ9K8W3V9bCAjS6ogVRGfT52ichS5vBFc1VQdsgDn9BxvJ0w17T02jLuTbiKTGj7n3D7vGhWHK0txKTBUWJuILcjXDUAKCPJZgLjM2tRxwqDb_gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع با پیکر مطهر شهید مدافع وطن در بجنورد
🔹
بسیجی شهید علی‌اصغر نورانی در حین گشت رزمی دفاعی در منطقۀ جنوب شرق کشور، به درجۀ رفیع شهادت نائل آمد.
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/458739" target="_blank">📅 01:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4b069905.mp4?token=ceL5UO6jEvM88KsAQbjINJ5lMFVvaveJ7swtazLEkNBlpNhyg8Kq_aLSGZOG7Lv8P2aG2EFK5sFMopD1URPOqePit9uZlraLtbyrCIBX1NZPvXWAypHTJNv72cOpBWToImqsd3ivT6u-JZOHODUAhmdvuHmlSIZHNxYTDnc4CaHS-FGsU6Zc13pda2FvnAzbaBkmU3lzFcawu2Dx5G0zXuLx1d2dZW3WmnmJV3txpkkV_b3GyG_Sznd0WLE_JtB0PzFNo3OFFVefoJOiswf-iZKE3uQ_Zw3Um5rps_jOTWKER2m1u54zxJ2JqM8zsT5zBmxAU3Wz_Dw38_c-sZmlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4b069905.mp4?token=ceL5UO6jEvM88KsAQbjINJ5lMFVvaveJ7swtazLEkNBlpNhyg8Kq_aLSGZOG7Lv8P2aG2EFK5sFMopD1URPOqePit9uZlraLtbyrCIBX1NZPvXWAypHTJNv72cOpBWToImqsd3ivT6u-JZOHODUAhmdvuHmlSIZHNxYTDnc4CaHS-FGsU6Zc13pda2FvnAzbaBkmU3lzFcawu2Dx5G0zXuLx1d2dZW3WmnmJV3txpkkV_b3GyG_Sznd0WLE_JtB0PzFNo3OFFVefoJOiswf-iZKE3uQ_Zw3Um5rps_jOTWKER2m1u54zxJ2JqM8zsT5zBmxAU3Wz_Dw38_c-sZmlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریستوفر هلالی، روزنامه‌نگار و تحلیلگر آمریکایی: ایران پس از این جنگ به‌عنوان یک ابرقدرت مهم در منطقه ظهور کرده است.
🔹
کشورهای حاشیۀ خلیج‌فارس حالا بیش از گذشته می‌دانند که ایران یک قدرت منطقه‌ای است که نمی‌توان آن را با زور کنار زد.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/458738" target="_blank">📅 01:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c8c594a9.mp4?token=DdftoKB3uw-pCo7fFlKOBZVxAzMFSB0G4z9-GtsZuFJnEE0aUrmV4mikkltC5PP5WPBXYgsqrnivbI1ONxlugeJDDtPXMOMCgp3GdQ31QXSP7Qd4iiv2Mryqi7KIayag__DymlsDrpOyh6Vh0CNaiW4Io_k5GFKT0gLw_d2l47jn0Cp3VwVKbNCRhh3PlIlr82z8lB2HyUbvx2mGb76Ab9_oxeNedBRshH1Z25uCIpcdPfOPXEgQuhOdK26pvqi5hxxVZ38JVbve41BmqDusEQ2M9rbJZjYjytawO4mlAcKND8GLMcW0EIWXW2tpvtnxg3b5v2EXcm-Xl89Qw4LrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c8c594a9.mp4?token=DdftoKB3uw-pCo7fFlKOBZVxAzMFSB0G4z9-GtsZuFJnEE0aUrmV4mikkltC5PP5WPBXYgsqrnivbI1ONxlugeJDDtPXMOMCgp3GdQ31QXSP7Qd4iiv2Mryqi7KIayag__DymlsDrpOyh6Vh0CNaiW4Io_k5GFKT0gLw_d2l47jn0Cp3VwVKbNCRhh3PlIlr82z8lB2HyUbvx2mGb76Ab9_oxeNedBRshH1Z25uCIpcdPfOPXEgQuhOdK26pvqi5hxxVZ38JVbve41BmqDusEQ2M9rbJZjYjytawO4mlAcKND8GLMcW0EIWXW2tpvtnxg3b5v2EXcm-Xl89Qw4LrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علیرغم فشارها، با قدرت رو‌ به جلو در حرکت هستیم
🔹
دولت را با ناترازی‌های زیادی تحویل گرفتیم که همه لبۀ پرتگاه بودند.
🔹
دشمن بی‌حساب حمله نکرد. با این وضعیت کشور باید بهم می‌ریخت؛ اما با مشارکت مردم و رهبری رهبر شهید و مقام معظم رهبری، ما ماندیم…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/458737" target="_blank">📅 01:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbbc03c349.mp4?token=Xap0r8i7gt5PJhOmc45O13R0sxlDTxXpe1sPnH66VvEzbFq_Vf2O-RX2W2k9NLm472MyzJEX5bLr0EAYGHv7iBr4LkbC7EyKTCZpxXn-m-5h5Ubg_faFxQn6gIfG20-MqY9KLZdjkBAu-lGVozPidaO8-ExBydFfpgXbqpbdNUASWC5ZhJJQVT9f8i8W6-aIdHRyqVXDeAaiuI_OktiNMt2CzZf-yE587F2gTy5BGQvXl2gK-UHyYU9FQn-kp7XJJu0pOUuBY28f_NNLuCAY7GhwA0VDJqyKAlIDaG-uK6Vo8QysmroXbMJFAQi1vrTP4DJFnxwp1rSKaFqawaeDZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbbc03c349.mp4?token=Xap0r8i7gt5PJhOmc45O13R0sxlDTxXpe1sPnH66VvEzbFq_Vf2O-RX2W2k9NLm472MyzJEX5bLr0EAYGHv7iBr4LkbC7EyKTCZpxXn-m-5h5Ubg_faFxQn6gIfG20-MqY9KLZdjkBAu-lGVozPidaO8-ExBydFfpgXbqpbdNUASWC5ZhJJQVT9f8i8W6-aIdHRyqVXDeAaiuI_OktiNMt2CzZf-yE587F2gTy5BGQvXl2gK-UHyYU9FQn-kp7XJJu0pOUuBY28f_NNLuCAY7GhwA0VDJqyKAlIDaG-uK6Vo8QysmroXbMJFAQi1vrTP4DJFnxwp1rSKaFqawaeDZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامۀ دولت برای تأمین مسکن اقشار مختلف مردم چیست؟
🔹
پزشکیان: با مشارکت مردمی می‌توانیم مشکلات محرومین را تا حدود زیادی حل کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/458736" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458735">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c249723ebc.mp4?token=rhDTBKHuPcVTUt9fOAkyvYJMM6rE3Z2hqkrzDGI2jtAObi5pSNHNgA4NWkWh9cjAzJJapyrscUNzog4_6S-eD5laW3Cbill29YkEYjWeFEW8NFb7jTRnd0TaEtN5lENjhITe94s9F6USqy6oMrMbPTJ4aUm8OqML3r6SnnVVAEKpmEcerk9KRljo5Vt0aN6uKIWkMq1eGIyvt4uC5dUmU8BS0zf2AIZdKJFtLhImNWDy87s5j1CWk7kD3Nz2jNSr_4V8CbM-bggtIDjdVJgUsVwQ8Cw2fdl5mg1upRr4SgL7BVzZBaHDBtumUgNIhYGFhZLW_ziBAtQxByZ6BSxdrY82Ao6gVkMNfWDnRI7koSDYt3NbELXDhe0mjV5ELCW8OqXTo6FIttozRyjeZN3XxdJXEQiMX4DY7X46l9jh9-1y_OEKpmmQIHbWxv5vWuDNAsTTPyCe3u3xweyWfjU1l18Fkk4pvmn9YxDWw7JdSlityht_qzPwMeKlY6UwWj5NoezCf7m_Kx8mI7uUAz1Xm0_eqiqoxdlaN_v0iCP689ao4AEZD2DAwUPUB4CV88CwMPPkFAofitWK-s_ztTXtOzpBWSweHmd1DDLOJAIXsDd-Tz2Mgx5zxmRe9lPQwyNa6D9QKbEJFTWFIcL0teviUqRxyvU4EjtgVi3LCfTuG00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c249723ebc.mp4?token=rhDTBKHuPcVTUt9fOAkyvYJMM6rE3Z2hqkrzDGI2jtAObi5pSNHNgA4NWkWh9cjAzJJapyrscUNzog4_6S-eD5laW3Cbill29YkEYjWeFEW8NFb7jTRnd0TaEtN5lENjhITe94s9F6USqy6oMrMbPTJ4aUm8OqML3r6SnnVVAEKpmEcerk9KRljo5Vt0aN6uKIWkMq1eGIyvt4uC5dUmU8BS0zf2AIZdKJFtLhImNWDy87s5j1CWk7kD3Nz2jNSr_4V8CbM-bggtIDjdVJgUsVwQ8Cw2fdl5mg1upRr4SgL7BVzZBaHDBtumUgNIhYGFhZLW_ziBAtQxByZ6BSxdrY82Ao6gVkMNfWDnRI7koSDYt3NbELXDhe0mjV5ELCW8OqXTo6FIttozRyjeZN3XxdJXEQiMX4DY7X46l9jh9-1y_OEKpmmQIHbWxv5vWuDNAsTTPyCe3u3xweyWfjU1l18Fkk4pvmn9YxDWw7JdSlityht_qzPwMeKlY6UwWj5NoezCf7m_Kx8mI7uUAz1Xm0_eqiqoxdlaN_v0iCP689ao4AEZD2DAwUPUB4CV88CwMPPkFAofitWK-s_ztTXtOzpBWSweHmd1DDLOJAIXsDd-Tz2Mgx5zxmRe9lPQwyNa6D9QKbEJFTWFIcL0teviUqRxyvU4EjtgVi3LCfTuG00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: به‌جای گیر دادن به هم، نواقص هم را برطرف کنیم. من به تنهایی نمی‌توانم مملکت را درست کنم اما باهم می‌توانیم. @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/458735" target="_blank">📅 00:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5f0f13f6.mp4?token=blO9qKTYMlBgsy34FK_F-HNjNGNJQNCvC7lqQHJtNEEPl7_0dUJGK7CGdxpmTB5A6Aj0n8NDCrhD9leZTnImFRkhMPcL3bDmqUoim6xCvBi4mozn6vepOJA6qlup_IhV7zYWVADbd6Mv2kaIzTI1UHkkCrzw3NGBuQddLv6sdLTb03HOQpW2L6icFkQWBj0-ZX0-PX7qALwtySKifCXPf8PivaXh9rnryHjGzu_VFwdJnEn7DhiT17j8dzFLi_vob8gG7DrsMaHxrxLsDmOnplWNLXHhAykwNdmynQifqkJJi_JDiz0-U1lV7IIbk_tuq4ij5Lcdw0Sdujk04XEfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5f0f13f6.mp4?token=blO9qKTYMlBgsy34FK_F-HNjNGNJQNCvC7lqQHJtNEEPl7_0dUJGK7CGdxpmTB5A6Aj0n8NDCrhD9leZTnImFRkhMPcL3bDmqUoim6xCvBi4mozn6vepOJA6qlup_IhV7zYWVADbd6Mv2kaIzTI1UHkkCrzw3NGBuQddLv6sdLTb03HOQpW2L6icFkQWBj0-ZX0-PX7qALwtySKifCXPf8PivaXh9rnryHjGzu_VFwdJnEn7DhiT17j8dzFLi_vob8gG7DrsMaHxrxLsDmOnplWNLXHhAykwNdmynQifqkJJi_JDiz0-U1lV7IIbk_tuq4ij5Lcdw0Sdujk04XEfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل اجرا نشدن طرح پزشک خانواده از زبان رئیس‌جمهور @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458734" target="_blank">📅 00:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=Qw3VSEQoy7p_VDm7scMKjdIhHfZC7gkECr1FavDIz7u5sqWvfe4dzpwtsEW2sNnx12v7hmR3NyuqB7tqpxpUkF7HCyYBGex7PjQPfdg-xgqO7z1sKymdyHBU0vSUjx1VbnaoOTTYa7eqMlbEYaqZa5F5JIH80IkWljDEBM8HvmU_KQxza2UceZEI3V3jLKaTr1qLfoqY9TEqJJ-6PhJDFsSUR-eo_VXGwqFSbqBKmrZzjQc7wbIGg88aaxQq-rWXTk8xRHbyJBoC534ViE4Gk1ChTP_gRD0faXw-oE9nhXQIXRCqjB9A-0vaD9PxKIbvgIuxI_87zvfsqKEdljhD90X652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=Qw3VSEQoy7p_VDm7scMKjdIhHfZC7gkECr1FavDIz7u5sqWvfe4dzpwtsEW2sNnx12v7hmR3NyuqB7tqpxpUkF7HCyYBGex7PjQPfdg-xgqO7z1sKymdyHBU0vSUjx1VbnaoOTTYa7eqMlbEYaqZa5F5JIH80IkWljDEBM8HvmU_KQxza2UceZEI3V3jLKaTr1qLfoqY9TEqJJ-6PhJDFsSUR-eo_VXGwqFSbqBKmrZzjQc7wbIGg88aaxQq-rWXTk8xRHbyJBoC534ViE4Gk1ChTP_gRD0faXw-oE9nhXQIXRCqjB9A-0vaD9PxKIbvgIuxI_87zvfsqKEdljhD90X652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید مدیران ناکارآمد شرکت‌ها را برکنار کنیم
🔹
برای مدیریت کشور به افراد کارآمد نیاز داریم، نه لزوماً رفقای خودمان. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/458733" target="_blank">📅 00:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c231b724b.mp4?token=lHBNmRpGkCLJDvuxCIWcIfSv0Ehdpg3hgTNNyF3IonkCQsMMErkxDwPy8Ab5HK29IcfJswIvPYvtrKkdaoBr-2czVHvILQIvr1arv1gL1tL5JintjVcXqQV9Dk_NdtXdKGDog_nkfDaWzk1ZVhEh9OTejDyETkcy9IJU95KRfBX9mFUf8mT74CZ_C2OL_XVPCbVr6V0ms9SEPekh0OqXqeXLDFm6Hgw0qcMHWjHAE2QFPpM_TcvtvRyoWVYCTVL-5GAeTQw1Mc3g6avhHNZxn6vfK0k5umnPuXQiJmoCDU2ZrjS4q2VN8bul87jlxlSGiwgvZDboIHsWiCXYC3IKLwZsEnDWMf2Hm22jR1PvG1ORNxppMAUuabDb3pMc_dy5bTi-m9pWs_5p9yvOzh8Wv8aeXokpPIOk9boSStFIWsouqjiKpD4iNe0oPqYBNziFxxUu_P-8XC6GX1n4P21f_al8Zk73Qr_LIj5rQPivNDWLA5S_NTr4xManQZic0vbNLx_Y3t10IGw0LuuJ6mL_iYoQ1dDKXVL6pfCJfQznencmFCYUmPa4JhBWVvDQeWzZnLQsU64JqKADPfEGuMl5LcOPUP5fRLTV9l-ujbwO7TwVNHJHOvZXu9d5Pv8iJuDAYY_Ii8_t5Opsb4RCCbFkQjnsLSPm4LmjR8i2MqgXZ6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c231b724b.mp4?token=lHBNmRpGkCLJDvuxCIWcIfSv0Ehdpg3hgTNNyF3IonkCQsMMErkxDwPy8Ab5HK29IcfJswIvPYvtrKkdaoBr-2czVHvILQIvr1arv1gL1tL5JintjVcXqQV9Dk_NdtXdKGDog_nkfDaWzk1ZVhEh9OTejDyETkcy9IJU95KRfBX9mFUf8mT74CZ_C2OL_XVPCbVr6V0ms9SEPekh0OqXqeXLDFm6Hgw0qcMHWjHAE2QFPpM_TcvtvRyoWVYCTVL-5GAeTQw1Mc3g6avhHNZxn6vfK0k5umnPuXQiJmoCDU2ZrjS4q2VN8bul87jlxlSGiwgvZDboIHsWiCXYC3IKLwZsEnDWMf2Hm22jR1PvG1ORNxppMAUuabDb3pMc_dy5bTi-m9pWs_5p9yvOzh8Wv8aeXokpPIOk9boSStFIWsouqjiKpD4iNe0oPqYBNziFxxUu_P-8XC6GX1n4P21f_al8Zk73Qr_LIj5rQPivNDWLA5S_NTr4xManQZic0vbNLx_Y3t10IGw0LuuJ6mL_iYoQ1dDKXVL6pfCJfQznencmFCYUmPa4JhBWVvDQeWzZnLQsU64JqKADPfEGuMl5LcOPUP5fRLTV9l-ujbwO7TwVNHJHOvZXu9d5Pv8iJuDAYY_Ii8_t5Opsb4RCCbFkQjnsLSPm4LmjR8i2MqgXZ6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به دنبال این هستیم که برخی از ادارات را دورکار کنیم
🔹
حقوق پرسنل را کم نمی‌کنیم اما مصرف سوخت و انرژی ما کاهش می‌یابد. @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458732" target="_blank">📅 00:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=NH_svoSdJG_zGSf8K3gHP2c-nHkx8_UrE9nS55o3Qos9fb4J3fNXiMWk8Cg8BqwAHZAKRh2mnxkO85E0hOiR4n3ysyOX8uSddQPJDwFgVc2DIIA7id7ANk_XvJlsEmlpHFmXBbP2-Zh9mCBKQrW1HiPbtDRcDeyWpysXIJg_PV27tdJYecl-zP8BafpdJL0gE4k2cmlM3D-VPmls_2GW7IsvN5Yr5uAnq1OEUud9TGAHjH7Ze93HyCRatbpCRzgfFEeLzlqSXywOHVCOy9HuwUyDOpXfeQQGDwbTsNg6bLPXycDBDjxACTZ-B-rojoCA7QvuwYjHl1mpCM3VACNz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=NH_svoSdJG_zGSf8K3gHP2c-nHkx8_UrE9nS55o3Qos9fb4J3fNXiMWk8Cg8BqwAHZAKRh2mnxkO85E0hOiR4n3ysyOX8uSddQPJDwFgVc2DIIA7id7ANk_XvJlsEmlpHFmXBbP2-Zh9mCBKQrW1HiPbtDRcDeyWpysXIJg_PV27tdJYecl-zP8BafpdJL0gE4k2cmlM3D-VPmls_2GW7IsvN5Yr5uAnq1OEUud9TGAHjH7Ze93HyCRatbpCRzgfFEeLzlqSXywOHVCOy9HuwUyDOpXfeQQGDwbTsNg6bLPXycDBDjxACTZ-B-rojoCA7QvuwYjHl1mpCM3VACNz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
🔹
ما به خداوند متعال، مردم خود، توانمندی‌های داخلی و تسلیحاتی که با فناوری بومی توسعه داده‌ایم اتکا می‌کنیم؛ موشک‌هایی که آمریکا و رژیم صهیونیستی در مقابله با آنها ناتوان ماندند.…</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/458731" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXVPyfZeruL2tjHFw5wCUrnOT86JRAM--jZ2tu0ahQIQY7DaTv1Z02iX2Z5bLxIC9FaR8vpPAGhw-AT96mY_RlmpsSIPqvEC0ET4JEmmXL1fFJq-dt9QOlWsUcmaUwHxbSqNyTl1hkqpuJqu0gDcgQJVkJGh8-qvMKhEzC46rmKev7oV_kIXmZlX7eUtkwmBkHJObKa9QyvRzGn94ZdbcBAwPTVAbNV_HKm3PBSpjAzRvHYytWDAcnV43CM_MeL1d5NWz_aGB-O-95VtLH99d3Ta1i9B8p2i9lieO5bBdqHmzbfRWOPIWmdLRuslcFMqwAy4yebTPY7KW9LDT7A8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا قانون آفلاین است اما قانون‌شکنی آنلاین
🔹
روزبه‌روز بر تعداد برنامه‌هایی که در داخل کشور تولید و در فضای مجازی منتشر می‌شوند افزوده می‌شود؛ تولیداتی که گاه در محتوا، اجرا فاصله محسوسی با چارچوب‌های قانونی دارند و عمدتاً در فضای مجازی منتشر می‌شوند و گاه مرز میان سرگرمی و ابتذال را نیز کمرنگ می‌کنند.
🔹
مسئله فقط تولید و انتشار محتوای مجازی نیست. وقتی چنین فضایی بدون واکنش مؤثر ادامه پیدا می‌کند، برخی تولیدکنندگان حتی یک گام جلوتر رفته و همان الگو را به رویدادهای حضوری نیز تسری می‌دهند؛ گویی میان فضای رسمی و غیررسمی، مرزی برای اجرای قانون وجود ندارد.
🔗
سؤال اینجاست: آیا غیررسمی بودن بستر انتشار، می‌تواند به معنای معافیت از قانون باشد؟ از
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/458730" target="_blank">📅 00:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElUngpAwYoQrBxHe_YUoy4v_OpfDwdNJ-uiwp0njcsFO3wO0-tAiicWVcL9bEjbc81OISQ5klccTZV1pxoU-IN11J0uXCrZ5BMueK3ECvYWlX3qsQvnzH8R9vbDolW6m3SyxgnhiabK3RG9Y3tboNaGML2mQW3tJ9zGM388rjKvztAgnlzSXsEU7XxJMkfuGhxw9_0VcXLp7hrO2AuOtuAIzCWY1C1Bmab0zp1X_0TzQMEllz76h2-5F350NHJl5BNmty_iT9090VDuXocqq7V5fbfT10KYtdBsSfDOzPRCd_erg2Sa6tYH1tv2NI0Qgc02kq7NA2yox-lwygnq-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا پیشمرگه را هم رها کرد
🔹
شبکه بی‌بی‌سی به نقل از چهار منبع مطلع: دولت ترامپ در حال برنامه‌ریزی برای قطع کمک‌های نظامی به یکی از متحدان مهم آمریکا در خاورمیانه است؛ متحدی که اکنون هدف حملات گسترده ایران قرار گرفته است.
🔹
وزارت دفاع آمریکا در دیدارهای اخیر با مقام‌های اقلیم کردستان عراق اعلام کرده که دولت ترامپ قصد ندارد توافق امنیتی مربوط به ارائه کمک به نیروهای پیشمرگه کرد را که به‌زودی منقضی می‌شود، تمدید کند.
🔹
یروان سعید مدیر ابتکار جهانی کرد برای صلح، در دانشگاه آمریکایی گفته: آمریکا با قطع حمایت از کردها، آنها را رها می‌کند؛ کردهایی که برای کمک به آمریکایی‌ها در تحقق اهدافشان در عراق و خاورمیانه، هزینه و خون زیادی پرداختند.
🔸
مقام‌های کرد نگرانند که قطع این کمک‌ها به ایجاد خلأ امنیتی در اقلیم کردستان منجر شود و دست ایران را برای افزایش نفوذ در این منطقه بازتر کند. بر اساس این گزارش، از زمان آغاز جنگ آمریکا علیه ایران، تهران صدها موشک و پهپاد به سمت مناطق مختلف اقلیم کردستان عراق شلیک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/458729" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458722">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZV7yspWu1RCaJffEWNB9BvMF7GgRwDf9voxcTAjuqiJGoR47v0T5YQaH5hvaFhu2UDB9uKXkGqzq9FIvm8oWDt_1vJ-UWDky5CicUhlUphDvgVWm0BvijgG3P8UQ4ms_lEVcbmy_CDO_VpL4hpij7ss37OYLW8KvqURkpe2IyFLyMaMpZjge31qbS-ur-fVngp8irAkWgQT_lsLie8TLqCUB-9ihGfxlV74zRmUu1FmskRixlh2c9XY1lklkCcZxEXFydGbfWXbPZMXNU0G8_PO5v1YtGXvcv3yi19aPSlj4ofnpso-b2_TNPW0K8XjcBSjeGb6GVLAUmTnMbvU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1omwHrSY2ERn21-kkE83ThkQB_zhCICuh53AgRI0uLaoPreReUse3QdynyxARNwD_1UNHtCkR3BuwCuziAqiKaQfIodMCAW_CuLBgXo42q0UixzBX01ronRxLUvCl_XqoXq5EgCzO_Mk2f4wU7LuoELtBmF_-xMvqsV_SMKpd_U76AcUUBFJeDbdG_0staLKvHNhc2ksZxLHZtAJ5d7PLA-mzUmJ--MUkUwmycP-sn002mriZEa_9mUr7pP39gqsHukhcCNH8bvNr3tRqDmdj0mSop0Y4cKSr11IgwuVBpx5GwFMR6fk3oGzEDEAG1vmj-NAO2-WSVpFHiBe4X3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOHe8Uk2CX3opvGibdvcjKe58ikGDuVAmX6IBTBDpZhSILX642yAM6KzbAiT55DLOGrrEFnwwUYQ7X-3pnVlkBi1-2z8keFuhfL3OEefmlZ8fsz6bgn9vZzf_OdaAc5oIafjzwPXdI4If2HfiBgrA9x-H8hPk7RU-WivPWOm4fxKJdbWDdIgbWcvd3kPDbBQiRPseq2RFRKY-PfGPgA9DwNJsAnlbwS5XU5bYVriai5ocuj2zocqyTZEFKFS51diHk7q7NpFcIAZ8SEEyzZZVULHXTeSyp6gwJQoI8EZ4Ye4zIHUxYlBx8uaiaaqGRuh3eUsWahliwmLGa0fXTiKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxD2YVvg1opbxZZa8yZ-2kMIYv2CFM7HbsV6Witbz5v9pm0iF0LvWNWp8QZA0cze0SWjU5jHzC33akmBZBfBylzBp_QD0Pjolil0_XJ9USPqFP5MDs7X10KVDVFMxZXVP14YAMO45JT_EGaHQac2KmjTtDdCyLT75LjNfLfOlQlNiA_eU8qdU-oOYqvFMpZ8e0t0zsmr0m3GMovM8FbSaGT-EZPOnVJu4D2ZiDAIP946kqhj4TaLw-WsyIEuQSHh0TsRuNcbqn9hQchH1Mq76RhWnlXQpRy4u78vYDmOjPfKjD44m2yyZaQXODkxUxwtkLO0l7nSdF9Hv5XmNMH0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7msgYk0j3jK_I6Ysa4wtmBlq22xrphCdS2WiHYH8-b9TWBMzztJfcSwTcR29AKVamBKrb0uy68ICKvF0CoTbhRlTSS1R1Ad3WPbkJfjeKZlgZswYZ2lVCuPbKWFV9ExC8q87U-EYuN98yiGqyJFvaAKgVRampF-6JRtxrs9XqwDNcl_bhVBz1XM71CGo_RqaexsxcPWMTU9S4zGd_qjqcnXN8sx9XyRZAaU8vZF_xjk9NWAGYeF8J3lj_XZLkrObYqsStF1jIRb8zqZEuJsZRsGO0wPnNOLTaZe6kr-pOKEur69ZsyiztZFkl9-toO-G7zBESgTdv6QO2K0wK36jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pw6cLL8-iqiVN26TRg5g0-SUCjojxznbMrnqxiVfLLBLfkuciZbd-vEOtQPNwR2RzjpvGwMUhgTej2RPXTH5D2qDukSpAb3RQzOcCcc707bA_7mrKmQ23cBrzRKhFdMlj76VQzysiCKPrkPeNKM-P7QodFDZttl2lB3UyEy3Ctglf7aXNEMMzJwZJCcU7bMtqLVjVAmfS0X9KXavVskaVa-PI95f7s1_JaIdnArHS1mKP_6ymXArtHAOJC34NxiHCBxdgBL0UbljxqhQQR5pZ3FouOw_Obb16wxnhRaY-Nr2Du1mMYy_0nPSQ7HKX3W7JGWiIOjXheeyQPc_UKSfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQzpqVqN0sLbCizp9gvpEXonSxMkxpZ-TmZaWJQ_OYnGIKXKi6WAF-sHCiHtJNm23Ii7zoADH_RBgCdHcD8pbiEX9eIYae8Rp6AONpPgAmjLTbNsMITNbD7CAa5X2OrzrYCPs3PVIiwm6djgbG_Me0Fh52V6iZSoGM9f15fZZsX1QffqlwPQsnqhXaxEOnNTkkjuTregEQrj2sd64mZTPcZJZa4KSYpP-t8t00R8-j8sxl29pbJG3wgILnVC5MA_SxPbELnGqP90lkwFqJat2Yjg_B3GcwI0GbMkJP_XzAVfl8t72xPJYJWI-Wz9WPHSuEX-ZbC3S4Oyc_U02xIYjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مهمانی امت احمد در سنندج
عکاس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/458722" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=uOtsUevPdjEOrC86YVnaknxIuXP_XMA7Jjk2sf-KRWlOMknBmv5OcypZR-mn4L7j634qhgaIr5JqiX_Qpyyh92Qjb1u_KKRrfmV3HKDSeRycfY966aHNG5h_fSagHhKLFXisWo7OM_Pj0Cmch1RZqmMI8PrKJC38pMiW9W_9M8LxKqYbqgItlDBOmFSUhFuU-W4_VcdSOk7vlQrzgOZdnQ-eiqMmgWwSyeihmt3DItBtNsDDmA7q69rMqmDpOqk4TLTzrkjuxP5fSDpW8hBf9BM01ZsBahBLrdVPcrDUV70AEAz9QzAjogqcafdhLEGgDXQkxIT3K7UCI8ilTISB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=uOtsUevPdjEOrC86YVnaknxIuXP_XMA7Jjk2sf-KRWlOMknBmv5OcypZR-mn4L7j634qhgaIr5JqiX_Qpyyh92Qjb1u_KKRrfmV3HKDSeRycfY966aHNG5h_fSagHhKLFXisWo7OM_Pj0Cmch1RZqmMI8PrKJC38pMiW9W_9M8LxKqYbqgItlDBOmFSUhFuU-W4_VcdSOk7vlQrzgOZdnQ-eiqMmgWwSyeihmt3DItBtNsDDmA7q69rMqmDpOqk4TLTzrkjuxP5fSDpW8hBf9BM01ZsBahBLrdVPcrDUV70AEAz9QzAjogqcafdhLEGgDXQkxIT3K7UCI8ilTISB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کالابرگ را برای برخی از دهک‌ها افزایش خواهیم داد
🔹
از اینکه نتوانستیم کالابرگ را افزایش دهیم، شرمندۀ مردم هستیم. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/458721" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458720">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=niFQvyhDjmNhe1vvVhQpTQArTPccwBUDEYuEd8jReoi5q-8izNoAInF2VnuaTm5BlpwpGVyCeb8f7NFgmSwin9fb3z1aQFx4st03wrlYBUv0r8u6d2tQK4HSgfHyFdEdhGE3A2YRsag6olU296hfdO72NUnEGk672jHafjRdFElOGveNq6cnwxTjEHRYR_Lih6spRQ00Z-xYm5RmqofRa-cf2Hbz3_HiTYn44u1SHE9tnWPc9S0OIvDi77uGlmm7bfrUdmcR9N92wNtDVh1dVytT3S7q5jYw8mDaf8rlNl3EM483RT2D0B7n_rc9RCXFYSVTraeUxJW11U3Qwt8Z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=niFQvyhDjmNhe1vvVhQpTQArTPccwBUDEYuEd8jReoi5q-8izNoAInF2VnuaTm5BlpwpGVyCeb8f7NFgmSwin9fb3z1aQFx4st03wrlYBUv0r8u6d2tQK4HSgfHyFdEdhGE3A2YRsag6olU296hfdO72NUnEGk672jHafjRdFElOGveNq6cnwxTjEHRYR_Lih6spRQ00Z-xYm5RmqofRa-cf2Hbz3_HiTYn44u1SHE9tnWPc9S0OIvDi77uGlmm7bfrUdmcR9N92wNtDVh1dVytT3S7q5jYw8mDaf8rlNl3EM483RT2D0B7n_rc9RCXFYSVTraeUxJW11U3Qwt8Z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر یک مقدار صرفه‌جویی کنیم، از بحران عبور می‌کنیم
🔹
برای زمستان به‌دنبال آن هستیم که گاز خانه‌ها قطع نشود اما مردم نیز باید مانند سال گذشته با کنترل مصرف انرژی ما را یاری کنند.
🔹
اولویت ما این است که چرخ صنعت بچرخد و تولید استمرار داشته باشد. @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/458720" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458719">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTiFAb8WiPVrVOaodsODg8XiqVasp4i5QF4zUEe2qSEOEDxN_7HPL5PqI8XIvK51hElxlc3yoAA-bXXCeSaVf8tiFCEtT1fjWiQaUIdkQgvnXGq78wX4NQFtHjZcKBD-TS8NxKinwkyvbMJQvBCn4-Q4Jq4MDy6MVQmoG8BXdas8_DXHkHFMuRbY8vYPJzz-ZopKI-A53DxvLZMrVS67b35udDFHHB1TM3F8e2m-TL_1K5U7UTavTRZyNHYdKSwioMO1xaYYmaBf_dJD_DSecCwWpScdd-b3xC4QZGQP9yEtbkTX3XesCDxtHxU49eZtSqrYEgME1o-9RWQMiCZ6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: تاکیدات امروز رهبر معظم انقلاب روشن و غیرقابل تفسیر است‏
🔹
سرلشکر محسن رضایی: تأکید صریح رهبر معظم انقلاب بر پرهیز از «سخن ناامیدکننده»، «دوگانه‌سازی‌های موهوم» و اینکه «ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است»، برای همه یک راهبرد روشن و غیرقابل تفسیر است.
🔹
‏امروز وحدت ملی و انسجام اجتماعی یکی از بنیادی‌ترین مولفه‌های قدرت و امنیت ملی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/458719" target="_blank">📅 23:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JECFZ9FO_N_9N1miAVL_BNFCh2e3rlPwczcq6n_gwcHqpH27Y3UvVswlDa7fpeuqtOULLhZN8ky4LSawcK8Oinpz-kM7DBa8AJBHj87YdQ7TOyxnXyWqYvZVMjGV0MlDNcd0SyIsva1Ilcxs2cKqYOmDRvLpmUd6K0c9h69utaTFLWhkcH-IofKBxNvOPHnLC2IIqoOq_WDoqWPqtPRcPI7SOq5GOlJgdX9oQER95OdVfc_44IFKtWwLKcd7Juovkxmv0I80L1mda-fj5ft1gDnyP0wL9BIeNQlqPyI5wFjjrg8KHJh9YP3zhL1IiSd3073pMkONMOsuuZdGBuEHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: تسلط رزمندگان اسلام بر تنگۀ هرمز کاملا قاطع است
🔹
اظهارات مقامات آمریکایی در مورد باز بودن تنگۀ هرمز دروغی آشکار و تنها به قصد کنترل قیمت نفت و سرپوش گذاشتن بر شکست‌های خود می‌باشد‌.
🔹
تسلط رزمندگان اسلام بر این آبراه راهبردی کاملا قاطع است و با تمام قدرت و در کمال اقتدار تنگۀ هرمز بر روی تمامی کشتی‌هایی که بدون هماهنگی با جمهوری اسلامی ایران قصد تردد دارند مسدود است.
🔹
به ملت عزیز، شجاع و مبعوث شده ایران اسلامی اطمینان می‌دهیم این روند تا پایان شرارت‌های ارتش تروریستی آمریکا علیه کشور عزیزمان و اجرای تعهدات مقرر ادامه خواهد يافت.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/458717" target="_blank">📅 23:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea0fc875b.mp4?token=lYPwjFxWZA7aHDDbbmZN7zGsFTTGTKvojkMSPh6nE2QjBWWX-yld_-nFaDFy5gcW35dsE_Y7PyKds0AvczEaZUfSJl8BX4pQ2JV9qM7JX3BZCg546j97nRe2pitTcYridO42QMsPyJqydA-2aPVkAQpRV1a5rVqBiRs3JPN7Sfvw-wglrJGe2TEvCdd-YIe2pvdp4mmyy5fGQySvYewVWYpjOulEWTKlm2lyulXpGfymBbX5f8JCkZdr6KoO2nYh1d0EDh15TMjA52XYCQYWssguIp5zwUdP_B1gOmVLRhiDIX7w5xK1_drMjF7x4AlSHsGGO5bmI8aSJ_Ta7eP4lDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea0fc875b.mp4?token=lYPwjFxWZA7aHDDbbmZN7zGsFTTGTKvojkMSPh6nE2QjBWWX-yld_-nFaDFy5gcW35dsE_Y7PyKds0AvczEaZUfSJl8BX4pQ2JV9qM7JX3BZCg546j97nRe2pitTcYridO42QMsPyJqydA-2aPVkAQpRV1a5rVqBiRs3JPN7Sfvw-wglrJGe2TEvCdd-YIe2pvdp4mmyy5fGQySvYewVWYpjOulEWTKlm2lyulXpGfymBbX5f8JCkZdr6KoO2nYh1d0EDh15TMjA52XYCQYWssguIp5zwUdP_B1gOmVLRhiDIX7w5xK1_drMjF7x4AlSHsGGO5bmI8aSJ_Ta7eP4lDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌توانیم با رفتار جهادی مشکلات‌مان را حل کنیم
🔹
کم‌شدن خاموشی‌ها با وجود اثرات جنگ، ناترازی و کمبود آب‌ در سدها، حاصل مدیریت بود. @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458716" target="_blank">📅 23:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68193682c3.mp4?token=V1XwrqSOaK0RPpMDsS5ROQ8kpxnzYSnHUFL-ZU4stKhwlrf1JZ0lwz5T1cERW68r5zWoVzZFjVPUn0alPbCkAgsLu1HxyrCBIsDsR6cKfuiKWvS68fpUR-ng-r6B74Fp4qGkQJwdgv9gkGDSs6TrDlfTUymN46gvo7NCuuftBW69PhhdRshizt4yPsqK6E7kzvTsdTCCRoESq8m3_8zLFLxjJUV96PG9ZU12LYukEGQSaER1R137SYmzSefFyBOTlrXlkPBxtRVmtzCscPuNGKBbVdt_VT4kQFOcz32FxnIedxC_k5t7aA-MFfnc8Z8aamejWHWDB0MYfkx-UfU35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68193682c3.mp4?token=V1XwrqSOaK0RPpMDsS5ROQ8kpxnzYSnHUFL-ZU4stKhwlrf1JZ0lwz5T1cERW68r5zWoVzZFjVPUn0alPbCkAgsLu1HxyrCBIsDsR6cKfuiKWvS68fpUR-ng-r6B74Fp4qGkQJwdgv9gkGDSs6TrDlfTUymN46gvo7NCuuftBW69PhhdRshizt4yPsqK6E7kzvTsdTCCRoESq8m3_8zLFLxjJUV96PG9ZU12LYukEGQSaER1R137SYmzSefFyBOTlrXlkPBxtRVmtzCscPuNGKBbVdt_VT4kQFOcz32FxnIedxC_k5t7aA-MFfnc8Z8aamejWHWDB0MYfkx-UfU35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۸۱ مردم کرمان با عطر بیعت و رنگ انتقام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/458715" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUQTQIIy4W81isSGzSFoI0aS4ZE7M5HJIgXxSkoedrXFm1TUsqghUNOhijMHvWqAotxgkyJPV_xDJgxClKsgilhYrDHFug0EreRWrzpnJPOlSS40n3HlJ-EANH485mKMtUAjKdoiJyKPE-KGHGjz5P6kjmlKqcxYzLyfoForvWgi3Xk5_MsQMUvNYzEMwj0XmpsL-6zz3ffoejXfYzneFnBd4YWZMfNLMMh-zPDzuIwOuET2fETdgK8dKo_L6nzFgXGNv4nM7pGBy6KeXgxRm_fBRqR9OG8Zm7k8q8ISVcXz56A-3P61lPixgkDg8N4VepxVJwpLwtRpa2kqTHfYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ قاب امید از ایران؛ خبرهایی که باید دید
🔹
امروز، ۵ شهریور ۱۴۰۵، «بسته خبر خوب» را با بیش از ۳۰ خبر از گوشه‌وکنار ایران تقدیم می‌کنیم؛ روایتی از تلاش و امید در سراسر ایران.  سایت مدرن پسماند قائمشهر؛ ۲۰ سال انتظار به سر آمد
🔸
پس از دو دهه، سایت مدرن پسماند…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/458714" target="_blank">📅 23:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3b9ae266.mp4?token=vyJH5amBS3Iek87-yJXHg_E2dwSBKy5DrrvqD_uEOlQo6YARhd9-EQxau0SNP5Jl8WU1VhE9OD8dWSQTW7W7GPcJNDVE4X7F729zHl5PCIJvJiP_WVboMYmWapScd3T2TFXQjmXabdzF9JrbLzhX4Oc3Ixkq9XwUxrxMFsYAToEAKo4Xz_SG8eIjOM5qwXeZBEahzbj7P_Z4oHP49hvWLJ31d2F6ACVFII3R7oN4ZC-OkNFG5eM4EYms7PF7i4Jw4grs84Q8pYSbBoHQqzqJeyQP9G70MKqVIn-cNxZX7QQmhvKMwJNvDhFlE5nMaaB0Xv1tcXjjuNMcHB2aFu_sbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3b9ae266.mp4?token=vyJH5amBS3Iek87-yJXHg_E2dwSBKy5DrrvqD_uEOlQo6YARhd9-EQxau0SNP5Jl8WU1VhE9OD8dWSQTW7W7GPcJNDVE4X7F729zHl5PCIJvJiP_WVboMYmWapScd3T2TFXQjmXabdzF9JrbLzhX4Oc3Ixkq9XwUxrxMFsYAToEAKo4Xz_SG8eIjOM5qwXeZBEahzbj7P_Z4oHP49hvWLJ31d2F6ACVFII3R7oN4ZC-OkNFG5eM4EYms7PF7i4Jw4grs84Q8pYSbBoHQqzqJeyQP9G70MKqVIn-cNxZX7QQmhvKMwJNvDhFlE5nMaaB0Xv1tcXjjuNMcHB2aFu_sbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلایل گرانی‌های اخیر از زبان رئیس‌جمهور
🔹
تحریم ادامه پیدا کند، گرانی افزایش پیدا خواهد کرد؛ هزینۀ انتقال و واردات بیشتر شده است.
🔹
همه تصور می‌کردند در کشور قحطی پیش بیاید؛ اما این که همچنان کالا در بازار موجود هست و به دست مردم می‌رسد نتیجۀ کارهایی است…</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/458713" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f34877f62.mp4?token=GTOdxBwJq1GpSx3trvPsYaAYbiV4c-ABKlioqsMOuknxXg5NNNkHeMpEuCVjen6kVTpT1F9Ekjz4tuEtC5F0IDAM4jVBMbh2PEeSXmIdu1yEtC0sfwAD_DHXYPEfbOS9406J084FKxAB8xkEnMbSQA-K4XY8oDtt8xFaiDldzAHEi6upLghjd3DhUWc7OmkRD6mP6Mbi-Jie7axLg_eHZb3gXMYm1Lp4F5grIBo96_NnWLDRSW4r8BNqY_BI4RqV51F7C-tMhDQqklNM4dH8oRJ6he9Q0eHEj9eObZUE1P7VwML2aKbLwyus35j1oclng7nXOUHczKyWpansMga0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f34877f62.mp4?token=GTOdxBwJq1GpSx3trvPsYaAYbiV4c-ABKlioqsMOuknxXg5NNNkHeMpEuCVjen6kVTpT1F9Ekjz4tuEtC5F0IDAM4jVBMbh2PEeSXmIdu1yEtC0sfwAD_DHXYPEfbOS9406J084FKxAB8xkEnMbSQA-K4XY8oDtt8xFaiDldzAHEi6upLghjd3DhUWc7OmkRD6mP6Mbi-Jie7axLg_eHZb3gXMYm1Lp4F5grIBo96_NnWLDRSW4r8BNqY_BI4RqV51F7C-tMhDQqklNM4dH8oRJ6he9Q0eHEj9eObZUE1P7VwML2aKbLwyus35j1oclng7nXOUHczKyWpansMga0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/458712" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4c2df493.mp4?token=HXUtekfjd0-TMmiqVtPDROj2h4INZEsFbS4YF9Hk0w1rulX-Rvoc5J_7nCXHYldZ-L_if3VCE624ntYLiQXAFOu0Q1s4dgTL8LWHH48vuU9z-gcyPdT_78k8UlmKPnT1Ddpzt-9IkKxCsNelSeY7Ki_FWg1pzqtr8gIszU-FDd7-MqwicaZSTGHAw_-hbXMr8Ct0T-YFids456_OgGqxmsJJioXGdx-WpPh2Kac2cLezSby-OTBDgqmUZiLrfrzfXvG0Ms2RQRYuCL39o23t3wMMzJdbB_Lq5v3of82y0JwlXk6fFIdzwjH9x9ZA3tGJZgOPYNJFZuYbxrhoFJnTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4c2df493.mp4?token=HXUtekfjd0-TMmiqVtPDROj2h4INZEsFbS4YF9Hk0w1rulX-Rvoc5J_7nCXHYldZ-L_if3VCE624ntYLiQXAFOu0Q1s4dgTL8LWHH48vuU9z-gcyPdT_78k8UlmKPnT1Ddpzt-9IkKxCsNelSeY7Ki_FWg1pzqtr8gIszU-FDd7-MqwicaZSTGHAw_-hbXMr8Ct0T-YFids456_OgGqxmsJJioXGdx-WpPh2Kac2cLezSby-OTBDgqmUZiLrfrzfXvG0Ms2RQRYuCL39o23t3wMMzJdbB_Lq5v3of82y0JwlXk6fFIdzwjH9x9ZA3tGJZgOPYNJFZuYbxrhoFJnTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: افرادی که دستی بر آتش ندارند، تحلیل‌هایشان در جیبشان بگذارند
🔹
طرح نمی‌خواهم؛ اگر کسی می‌تواند مشکلات را با شرایط موجود حل کند، به او اختیار می‌دهم. @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/458711" target="_blank">📅 23:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=cCsc424Vz5oE4RMt6RhDd9k0Lh_LQmc4I4QjrkHqireFxIGQQKI2_oDKYQxMP7ZViRAKdB7DYxXOs10dhmx6Gq3FrQ9VgNFPZSBiHa19c806_RxFuZ4STk6nvHI_eIof3iTSwVGNT3AfShNciBv9wyWj1Sak5G2mx8E1zQ4PAkcIGeVoQrIq9Ee7cn5FLq9G2WHHr8d3Q_P3uaUE2Az46zhlZ40oaFfOD_Plj-UcWAGyzAY1dPKUdiAK6uJ9c5f3DSE7eJwYygUcSmkAaOz8PU3U6uC0oRnk1Z27JogD4M2jHu_hYytcKesWvpjSd62tVgWLDZYT7tf0AsIWt5sPlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=cCsc424Vz5oE4RMt6RhDd9k0Lh_LQmc4I4QjrkHqireFxIGQQKI2_oDKYQxMP7ZViRAKdB7DYxXOs10dhmx6Gq3FrQ9VgNFPZSBiHa19c806_RxFuZ4STk6nvHI_eIof3iTSwVGNT3AfShNciBv9wyWj1Sak5G2mx8E1zQ4PAkcIGeVoQrIq9Ee7cn5FLq9G2WHHr8d3Q_P3uaUE2Az46zhlZ40oaFfOD_Plj-UcWAGyzAY1dPKUdiAK6uJ9c5f3DSE7eJwYygUcSmkAaOz8PU3U6uC0oRnk1Z27JogD4M2jHu_hYytcKesWvpjSd62tVgWLDZYT7tf0AsIWt5sPlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: کشورهای منطقه که برای امنیت خودشان به آمریکا اتکا کرده بودند متوجه شدند که اشتباه کردند.  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/458710" target="_blank">📅 23:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458709">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75fe5677b.mp4?token=OPmFp_XIfXiheO2DrVtguy-_6H_91xqs_cocDId_OCfXOfjqb9fyPsgyPXABsW0EqX2ofW7FwhHjJI7InXprdUrUAWzXshy0l3u6I5vTzfZcoAvLbOmrZHb-SoXKQXNZ2kxRYFfqkZUIPBh6ubmtWqm8uEiwcWXrAGiPGpEywlczCOk4Eed0MBXyWntaTA03Rg0TB8LkODguWW3YAY_ox_ZApQbkgSjIlmKVqGx2CJmalbOD0wJjq6MA5OChYgFt6LtcaItbr-o49ZLBZlJ9ZdxQzVI9ERCohdad-ZcyZs8DOZEElQhtxR962EFFm8xaXY4Mzb7hKCg2HtofnN0YTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75fe5677b.mp4?token=OPmFp_XIfXiheO2DrVtguy-_6H_91xqs_cocDId_OCfXOfjqb9fyPsgyPXABsW0EqX2ofW7FwhHjJI7InXprdUrUAWzXshy0l3u6I5vTzfZcoAvLbOmrZHb-SoXKQXNZ2kxRYFfqkZUIPBh6ubmtWqm8uEiwcWXrAGiPGpEywlczCOk4Eed0MBXyWntaTA03Rg0TB8LkODguWW3YAY_ox_ZApQbkgSjIlmKVqGx2CJmalbOD0wJjq6MA5OChYgFt6LtcaItbr-o49ZLBZlJ9ZdxQzVI9ERCohdad-ZcyZs8DOZEElQhtxR962EFFm8xaXY4Mzb7hKCg2HtofnN0YTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نزدیک ۹۰ میلیون بشکه نفت در زمان اجرای تفاهم‌نامه فروختیم  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/458709" target="_blank">📅 23:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458708">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msKj_maen8zd_czGMjFWcTOAQmMejYl8cocolCs0U9utzpDs3_Z0S-jb3o-o8lbEJzdN9ZwloD8jjw0nvkGlEgjLqTNNllkU22o0bw9-s0bwjr1Q3cq5fd-JEZFktv9Fom-1XEdyPYRPK-pukHjAIXFIvbNml_7HpRD1UFJpgq_nO8WQh7bRcrcFamp3xow7LosRQ2byVEgc9slMf7uRKjG8Dp2vuxH_IdIrOb9CNQIlimbItmLhsQ7vP2JnLh9GvfCJ_lqVcHF2WDerVuMCijAD-zMl-HxVcG8iyS32a07dqcWCblsj-H1iVrxhTDb4snPNIz_XZKNou-Q2soDNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال در برابر فولاد متوقف شد
⚽️
فولاد ۰ - ۰ استقلال
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458708" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458707">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125b371944.mp4?token=pJwWov2AJIIrtYTghc7npTzFneYtnmpL4hm_MLMgzE0DItCTTpCkWA3n71lW8rU5Jgz8mBMh-EyCtLq5Q-av7zMFEB-oFgIdz0sHCnBKCnW5LavDgL3DGuXiuSYe7mGOez6YuT9bChX8Nu_sTa3-BDt5D9oxlp1eEUMiD2UEJ9JiUfLwX2UB1aGrL3USBdoq_dZ4nWaVJoYorp8G7Wlc4uphOm28ZQwKRHsbZMfyMbtKiX7eiv3Aj28DDjXRzB2JxnOOgUuUXQUssVoDA_2FTsbermOTszTWvfc-0k_8KRbaVO93b1oKyIsDmhjkGrYPlUmnEhni-bofzL4PO9-e5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125b371944.mp4?token=pJwWov2AJIIrtYTghc7npTzFneYtnmpL4hm_MLMgzE0DItCTTpCkWA3n71lW8rU5Jgz8mBMh-EyCtLq5Q-av7zMFEB-oFgIdz0sHCnBKCnW5LavDgL3DGuXiuSYe7mGOez6YuT9bChX8Nu_sTa3-BDt5D9oxlp1eEUMiD2UEJ9JiUfLwX2UB1aGrL3USBdoq_dZ4nWaVJoYorp8G7Wlc4uphOm28ZQwKRHsbZMfyMbtKiX7eiv3Aj28DDjXRzB2JxnOOgUuUXQUssVoDA_2FTsbermOTszTWvfc-0k_8KRbaVO93b1oKyIsDmhjkGrYPlUmnEhni-bofzL4PO9-e5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نباید نگاه صفر و صدی به مذاکرات داشته باشیم؛ اگر به تعهدات عمل نکنند، ما هم عمل نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/458707" target="_blank">📅 23:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458706">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c176c1e0.mp4?token=qanuBqE3b9dLpcLvuKbIQLuf8DhoQ22AcUvFpD7OayonGBBr4TY9sMiw77iX5nxSPDXvBLpFEMMZgH98VzMmOH1yvy7MZqflotfeudP519fVx-mNVqHEXqQ9Mocq8kpdHNtmQ6_fjAUTbXxUEc8DI5yVOyCbLrU2duJJLkpsMy7Qvb9C5QDCd38Hkdd74aIkWjt1Aw_eb11TevgUNOsJXminoTdbUGkT-NFbfexIBJSPilwh1-3LahFjD1mEB1M0ihd9NeIJ0R87t18UMdzAF9fGDiozW97Ut1wdlkdfA3sQbuk1DdZXTNuCfPFnQx-F2OOsd3YfespA3H-BSr9kUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c176c1e0.mp4?token=qanuBqE3b9dLpcLvuKbIQLuf8DhoQ22AcUvFpD7OayonGBBr4TY9sMiw77iX5nxSPDXvBLpFEMMZgH98VzMmOH1yvy7MZqflotfeudP519fVx-mNVqHEXqQ9Mocq8kpdHNtmQ6_fjAUTbXxUEc8DI5yVOyCbLrU2duJJLkpsMy7Qvb9C5QDCd38Hkdd74aIkWjt1Aw_eb11TevgUNOsJXminoTdbUGkT-NFbfexIBJSPilwh1-3LahFjD1mEB1M0ihd9NeIJ0R87t18UMdzAF9fGDiozW97Ut1wdlkdfA3sQbuk1DdZXTNuCfPFnQx-F2OOsd3YfespA3H-BSr9kUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هرکدام از استانداران و مدیران ما می‌توانند خلاقیتی داشته باشند که شاید من نداشته باشم  @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/458706" target="_blank">📅 22:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: حزب‌الله مانع اشغال بیروت شد
🔹
شیخ نعیم قاسم: ما این دستاورد را به دست آوردیم که مانع شدیم آنها به پایتخت، بیروت، برسند. ما مانع شدیم آنها ما را از قدرت و سلاحمان خلع کنند؛ زیرا در این صورت لبنان ضعیف می‌شد، آنها بر لبنان مسلط می‌شدند…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/458705" target="_blank">📅 22:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCzMCRFCkXVTymnDXP-9eJp1a6UiAg9OIHYCrSz_59Z1kuH9H7vf6MizvE46_CXtYyviJvPmUENFEkYR7W_w3DG3A0ZpIHhfhVpEuE3UeS7F9p0Fp7OLwRn6OA6CO4Vv_u2Y2uxGx-V_IaIu1w2i7Nwi-CWWgIV74sLx93SRMmiu-Ye48lBYqnuWNapve9PPz8hYyMpVLWJhftXJMYy_KatxlTvsbPMPtRj4q5v8fhOEW33vJ9_XA-HNwMMUYz1NP0TmGKL8zmaWhhS-FC6rkYcaEDMAiTni041D28aApXEG_7VSSdp_-tqXhwaOqqWmymfRVPUVvxxTMTl1tR2CkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: حزب‌الله مانع اشغال بیروت شد
🔹
شیخ نعیم قاسم: ما این دستاورد را به دست آوردیم که مانع شدیم آنها به پایتخت، بیروت، برسند. ما مانع شدیم آنها ما را از قدرت و سلاحمان خلع کنند؛ زیرا در این صورت لبنان ضعیف می‌شد، آنها بر لبنان مسلط می‌شدند و شهرک‌سازی‌ها آغاز می‌شد.»
🔹
ما با توافق چارچوب میان دولت لبنان و اسرائیل مخالفیم و خواستار لغو آن هستیم.
🔹
این توافق غیرشرعی، غیرقانونی و تحقیرآمیز است؛ این توافق حاکمیت لبنان را نابود می‌کند و حقوق لبنان را بازپس نمی‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/458704" target="_blank">📅 22:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03320cd5ba.mp4?token=UqTnXlYwZBB_t4hL_uw1TURP0qPdP3pnhR8QJipl_qaQSCnm6gjg6FeyGT3djBr6PKfmud8Koa46N_ELPfEXvvhFQ2RkWXei6A-2Jinvo3-EYbuk6A3-iiphhpq7FnAJG0SGzreEAKYveEE_HyDdpSs4bTOHw3zGB9xvYdk71memnj7psz663DYXf5S5DWVyk2vvFDnHzYCQUDADoUFkzj0EWTG7N0Dgb7_KHwicORPW9Ydk3bu6T_w08pGfQcZWlurLrQOyJwK-UZ48Qi4xdZBDmpb-qykaYj-EL_CfLfPb4yJvcqqAug3zYFIF4Xs_rvKdDPlIYiWRsgJVZ4jkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03320cd5ba.mp4?token=UqTnXlYwZBB_t4hL_uw1TURP0qPdP3pnhR8QJipl_qaQSCnm6gjg6FeyGT3djBr6PKfmud8Koa46N_ELPfEXvvhFQ2RkWXei6A-2Jinvo3-EYbuk6A3-iiphhpq7FnAJG0SGzreEAKYveEE_HyDdpSs4bTOHw3zGB9xvYdk71memnj7psz663DYXf5S5DWVyk2vvFDnHzYCQUDADoUFkzj0EWTG7N0Dgb7_KHwicORPW9Ydk3bu6T_w08pGfQcZWlurLrQOyJwK-UZ48Qi4xdZBDmpb-qykaYj-EL_CfLfPb4yJvcqqAug3zYFIF4Xs_rvKdDPlIYiWRsgJVZ4jkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کاهش مصرف از راهکارهای اصلی مدیریت مسأله بنزین است
🔹
روزانه ‌۲ میلیون ماشین وارد تهران می‌شود و برمی‌گردد؛ اگر کارمندان ما در اداره مربوطه در شهر خود بمانند، کسری بنزین جبران می‌شود.
🔹
طرحی داریم که با کمک شهرداری کارمندان هفته‌ای یک روز با حمل‌ونقل…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458703" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03238b2a29.mp4?token=T_0jrsIdpjK_JqZiM72y4s0GWl0ZKmpfiWhmEvuztatecyjtFXzrnkNMBGwOyQI9elgEK1OIV3DPiNaU7bqpCw7VunZnHPVNhNDyeCqJHphLWxI7Ghckkq9ipxY0IZBFRixPbHlJXk2Bm7kfFC5chfLto_jCZ57lvK-Ab64q8Vbd4o8_wt75VNs8t54eiSmjA-oLt6WKvb94-AvZBkvWMPVDDXES4a8NsYh2J5aJVV7kFDJ5IsWdK1L-sSge_kUAeDKtcL5gC-ee9JCcgR91skf_JDu_lB8OVvTEdXMybqwunxNoHnmoGE6AAjphLCxHWM5mo8eiBQvYNeE-unJhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03238b2a29.mp4?token=T_0jrsIdpjK_JqZiM72y4s0GWl0ZKmpfiWhmEvuztatecyjtFXzrnkNMBGwOyQI9elgEK1OIV3DPiNaU7bqpCw7VunZnHPVNhNDyeCqJHphLWxI7Ghckkq9ipxY0IZBFRixPbHlJXk2Bm7kfFC5chfLto_jCZ57lvK-Ab64q8Vbd4o8_wt75VNs8t54eiSmjA-oLt6WKvb94-AvZBkvWMPVDDXES4a8NsYh2J5aJVV7kFDJ5IsWdK1L-sSge_kUAeDKtcL5gC-ee9JCcgR91skf_JDu_lB8OVvTEdXMybqwunxNoHnmoGE6AAjphLCxHWM5mo8eiBQvYNeE-unJhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کاهش مصرف از راهکارهای اصلی مدیریت مسأله بنزین است
🔹
روزانه ‌۲ میلیون ماشین وارد تهران می‌شود و برمی‌گردد؛ اگر کارمندان ما در اداره مربوطه در شهر خود بمانند، کسری بنزین جبران می‌شود.
🔹
طرحی داریم که با کمک شهرداری کارمندان هفته‌ای یک روز با حمل‌ونقل عمومی در محل کار حاضر شوند.
🔹
به‌دنبال کاهش مصرف خودروها، تاکسی‌ها و موتورها از طریق برقی‌سازی هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/458702" target="_blank">📅 22:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
پزشکیان: اگر توانستیم مقاومت کنیم، به دلیل انسجام داخلی است
🔹
باوجود همه مشکلات اقتصادی، تورم و اشتغال چون مردم با ما هستند و وحدت داریم، توانسته‌ایم بایستیم.
🔹
با انسجام و وحدت خواهیم توانست در برابر فشاری که آمریکا با کمک کشورهای دیگر وارد می‌کند ایستادگی…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/458701" target="_blank">📅 22:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkKP0ujI8CY-Vz8R-W0m7CGR7tynoDCJ0wHiuXwitB6_X08AfgYvKk3T_mo4b5HzAldISr-S43Es0llHHTR_sNdK8db_PySyvX8dTPeeWOmz7TmEYy8gNPSUT5B41TO5GDH6XlTA3fJyxaCApwOU6Sl-qTMeKiqBa3otzjKNXqcmybhWYfLwFRe2CcnXg0tbxY0gbOppDkR3DXM8oVjCfiCCZwyALBE4uaSnBcoqHtwSDX5nqKwxX9gSA5yedStUm2UDSxfheBlGeCMFPyCZs5A1c37t1nV-8ADSzDQDzyFDqQtIelH_CmawB9j4yFUMH8j4wXWSVicngk0jiRUklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: پیام رهبر معظم انقلاب، نصب العین تمام مسئولان کشور است
🔹
باید از دوگانه‌سازی‌های موهوم به هر شکلی پرهیز کرد و هر اقدامی که به انسجام اجتماعی آسیبی برساند، برای همهٔ ما حرام ملی و شرعی است.
🔹
با مردم و رهبری عهد می بندیم که تا پای جان خود را وقف خدمت به مردم و پیشرفت ایران کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/458700" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25dc44ff1a.mp4?token=PnwdzopSflm55D0viTKJ97GmnGhUkt-IfSi2JspTcuRYtI6Pfg3fahJ6A-Nx6OZLQkqNc9VcqTTPTGy20iU04Scv9VLqo1sa5A1mnmArL4ot-PHMPHz_seiwNQCUGbb3MROvwK0XWHjJgO1Vj9AQB5uoH8CBSqosUxc0eeNwdTzxBjj_tVisX0T3YJXcnggwh4NoeqiDrte5lw7dGPoqpEdgDqIsYpw0UCPkprTvPL__kl68WDVrsIqO2D1IiuMBQ9UsUMp8uD-6VgNAVLSCIVZyjgmn5fx8xPH7XWXUhvreQ53xt5B0DZKBlOGCpH97YSHV_ekJ52lemprioF1d5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25dc44ff1a.mp4?token=PnwdzopSflm55D0viTKJ97GmnGhUkt-IfSi2JspTcuRYtI6Pfg3fahJ6A-Nx6OZLQkqNc9VcqTTPTGy20iU04Scv9VLqo1sa5A1mnmArL4ot-PHMPHz_seiwNQCUGbb3MROvwK0XWHjJgO1Vj9AQB5uoH8CBSqosUxc0eeNwdTzxBjj_tVisX0T3YJXcnggwh4NoeqiDrte5lw7dGPoqpEdgDqIsYpw0UCPkprTvPL__kl68WDVrsIqO2D1IiuMBQ9UsUMp8uD-6VgNAVLSCIVZyjgmn5fx8xPH7XWXUhvreQ53xt5B0DZKBlOGCpH97YSHV_ekJ52lemprioF1d5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نرخ سوم بنزین بیش از ۱۰ هزار تومان نخواهد بود
🔹
زمان اجرای این طرح هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/458699" target="_blank">📅 22:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1cc2353a5.mp4?token=VeATLS6Rn9p4n57SrLEv3-DTD4AWLdS5Nl3WnF_HFR2fk57c2XcgRNECY3mBYdR79e7XP76JcMn_mQ6QZT3QCy6gJFbEtXM1Utgd97etiHAaOfWMZ_wi2kUL_EkD3_odMdxVku0cQIzM8zfIYGBbsHq7Ty1fGiBFvScBFyDaiDgKKY3MAf101SEIlISgyaR8gX816MeWhKRQbvBpO6G6l5Zkx2278Q-ObCHw-wXY0CpE4zM8xwkE3nqWN2MHdkG268gVkSSS1C_VEalk63nBeIXBq_cDYI1jILblTcCVjIZAD09wI8NKhflqCeR-gXkpGzXDnakJrjq1FCnDPnHWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1cc2353a5.mp4?token=VeATLS6Rn9p4n57SrLEv3-DTD4AWLdS5Nl3WnF_HFR2fk57c2XcgRNECY3mBYdR79e7XP76JcMn_mQ6QZT3QCy6gJFbEtXM1Utgd97etiHAaOfWMZ_wi2kUL_EkD3_odMdxVku0cQIzM8zfIYGBbsHq7Ty1fGiBFvScBFyDaiDgKKY3MAf101SEIlISgyaR8gX816MeWhKRQbvBpO6G6l5Zkx2278Q-ObCHw-wXY0CpE4zM8xwkE3nqWN2MHdkG268gVkSSS1C_VEalk63nBeIXBq_cDYI1jILblTcCVjIZAD09wI8NKhflqCeR-gXkpGzXDnakJrjq1FCnDPnHWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر توانستیم مقاومت کنیم، به دلیل انسجام داخلی است
🔹
باوجود همه مشکلات اقتصادی، تورم و اشتغال چون مردم با ما هستند و وحدت داریم، توانسته‌ایم بایستیم.
🔹
با انسجام و وحدت خواهیم توانست در برابر فشاری که آمریکا با کمک کشورهای دیگر وارد می‌کند ایستادگی…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/458698" target="_blank">📅 22:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615ab2c430.mp4?token=jMsN7FD8L2z-GKWzdWiQMyGHjmeK_3x641nnBYNiW9FPA5ZKpmCvNf2TEPp9uBiAVmClUcYkTjVX7K7yJFHmk5ngStRQHff6IHS9hiDVr2EoeBlosnVMNFxjvFISHi58e-PFnVdy8yBIcAMfdnhqO_1WV6eyiW4t3MtjEBEbwPpOXL2A_MiNJmFcx2KyYrFF0FQlc8jrLWxWENQBKaCdGXE6NR1M4Zgk_NhiMcIgnsxYjdEx4mFarnQkJrodxztmVVJ9IABCGZ75Y0AQi4uiNU7OjaiIgLHAfyIHAXjw-nSRXJPz3gVytZDPJZPrSwnolxsahGReXKDZ_XMlDho9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615ab2c430.mp4?token=jMsN7FD8L2z-GKWzdWiQMyGHjmeK_3x641nnBYNiW9FPA5ZKpmCvNf2TEPp9uBiAVmClUcYkTjVX7K7yJFHmk5ngStRQHff6IHS9hiDVr2EoeBlosnVMNFxjvFISHi58e-PFnVdy8yBIcAMfdnhqO_1WV6eyiW4t3MtjEBEbwPpOXL2A_MiNJmFcx2KyYrFF0FQlc8jrLWxWENQBKaCdGXE6NR1M4Zgk_NhiMcIgnsxYjdEx4mFarnQkJrodxztmVVJ9IABCGZ75Y0AQi4uiNU7OjaiIgLHAfyIHAXjw-nSRXJPz3gVytZDPJZPrSwnolxsahGReXKDZ_XMlDho9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر توانستیم مقاومت کنیم، به دلیل انسجام داخلی است
🔹
باوجود همه مشکلات اقتصادی، تورم و اشتغال چون مردم با ما هستند و وحدت داریم، توانسته‌ایم بایستیم.
🔹
با انسجام و وحدت خواهیم توانست در برابر فشاری که آمریکا با کمک کشورهای دیگر وارد می‌کند ایستادگی کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/458697" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8eaad66.mp4?token=a7SVgqzUBAARnW9SWC_FT8DGU5e8A9Fim9tFcTigrjQVHL8Qz0B_8hw9oWxs72BSYG-JTnNqvvSFxdNg-416QZrKOewf3USYTsYHKs-5jSJ_foFyvNX1WDF4KT3xLV10t7ZIOD_lq72EjYTvVULTP9AekxyjaBsco4si29zd7ndzV31FfnBBQ949fqkMTCQkny0HTc6tmObjkQS1cSVLXzSxMCaYsMaFWEpsWcRWjwwW8c4QSYH6mdbm7a6NngkLrDaJQmUil1_LdDwZ1uGG2ORFGrGpDu0Do6reb58MFxfGobAMMvd_JSbPWlEwfi8nSAua-j5Gdf2Pp1-Qru9dmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8eaad66.mp4?token=a7SVgqzUBAARnW9SWC_FT8DGU5e8A9Fim9tFcTigrjQVHL8Qz0B_8hw9oWxs72BSYG-JTnNqvvSFxdNg-416QZrKOewf3USYTsYHKs-5jSJ_foFyvNX1WDF4KT3xLV10t7ZIOD_lq72EjYTvVULTP9AekxyjaBsco4si29zd7ndzV31FfnBBQ949fqkMTCQkny0HTc6tmObjkQS1cSVLXzSxMCaYsMaFWEpsWcRWjwwW8c4QSYH6mdbm7a6NngkLrDaJQmUil1_LdDwZ1uGG2ORFGrGpDu0Do6reb58MFxfGobAMMvd_JSbPWlEwfi8nSAua-j5Gdf2Pp1-Qru9dmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: طرف عمانی قبول دارد که باید تنگه هرمز براساس تفاهم‌نامه اسلام‌آباد اداره شود
🔹
به‌دلیل مراعات نشدن چهارچوب‌های ایران در بندی مرتبط با تنگۀ هرمز در تفاهمنامه، تفاهم به‌هم خورد.
🔹
اگر آمریکا به تعهدات خود مانند برداشتن محاصره و تحریم‌ها مانند نفت…</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/458695" target="_blank">📅 22:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ee2fe477.mp4?token=igggLjqU6KyoOFuGrQTyo0e1Y0TjPJTflHrEfe0CVAWG5H3Ir6l_biU3ZF5W0r1addnrc4y-uU6JvZKLiu_hhOKKTnzayzNNvUFVcGyRQMwKck5aXwlBBPHtR6StitrSK5Cf6hRQrN8Wvj-tzSwPIa1FAhjOYzSEMTP7tC4WZX9eofYBPnTIcAFzpvVLD_5UiTQweFIWTpSilpu_V0NdwBUUsBDRo_eq8fDTImKkRfPA36xRD62vGZ0ashchSaLsL0u1NrCfJIUc7RDWsNL2ObU1yIwR6Xx2fAuxOOavFrHIc7k6CCoArg12vx9SsyHRxTT23SVK7AYjdgWkm8FzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ee2fe477.mp4?token=igggLjqU6KyoOFuGrQTyo0e1Y0TjPJTflHrEfe0CVAWG5H3Ir6l_biU3ZF5W0r1addnrc4y-uU6JvZKLiu_hhOKKTnzayzNNvUFVcGyRQMwKck5aXwlBBPHtR6StitrSK5Cf6hRQrN8Wvj-tzSwPIa1FAhjOYzSEMTP7tC4WZX9eofYBPnTIcAFzpvVLD_5UiTQweFIWTpSilpu_V0NdwBUUsBDRo_eq8fDTImKkRfPA36xRD62vGZ0ashchSaLsL0u1NrCfJIUc7RDWsNL2ObU1yIwR6Xx2fAuxOOavFrHIc7k6CCoArg12vx9SsyHRxTT23SVK7AYjdgWkm8FzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/458694" target="_blank">📅 22:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ef7b2f8b.mp4?token=QEEMRvc0H0SnjK1Un6vR1lBzCGiSW4PY20tNligHll43cmKoSgjYSMxkPp7orbv2Qt56t4wm8uPI5Sg5o8yZERT0LDI_hBMwiDtWAIJ4d3c_lF_CmogdkyZTut4YuhodYjWOHnxVAfFrmlN7i2dYLdIZKMSfYMfBDQhtAxx5bEgcqKIM2ZluKyR55dvnRcqgtmIkIgDUi3usEdEjhAdv-IMdSd6SUUBONMYGeT4fVR9AcwSNP9aePsi8gNHXVSzj9MDeZIGBsepZAAYlKVK_yD9E3tPNKKWuqRpp0yjvU1irhms_IMwUJy0yC_CKa9bqQT4ctF4wE7rcrN8Xq8C1CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ef7b2f8b.mp4?token=QEEMRvc0H0SnjK1Un6vR1lBzCGiSW4PY20tNligHll43cmKoSgjYSMxkPp7orbv2Qt56t4wm8uPI5Sg5o8yZERT0LDI_hBMwiDtWAIJ4d3c_lF_CmogdkyZTut4YuhodYjWOHnxVAfFrmlN7i2dYLdIZKMSfYMfBDQhtAxx5bEgcqKIM2ZluKyR55dvnRcqgtmIkIgDUi3usEdEjhAdv-IMdSd6SUUBONMYGeT4fVR9AcwSNP9aePsi8gNHXVSzj9MDeZIGBsepZAAYlKVK_yD9E3tPNKKWuqRpp0yjvU1irhms_IMwUJy0yC_CKa9bqQT4ctF4wE7rcrN8Xq8C1CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/458693" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b15eae0fd3.mp4?token=bSdNSsW67hI7uAFYd7KfUkGytknoEuSKCO-nkKJPQ6Zdyonw7tCPt8etBkCgRq5-QG0DroBhC7N_GsvT53sJickRe7pAQl6l7OEcRImcCVWH2MrxZSpq69PdSRW88jxdZKUA7g0L3XEEsZuF7xbqxj6HEXWxUAqW10Mt5hMrYkLuKr9r3kWGz_BoVWwosoCzTUz8UdLKnQQgYXwVpotMbpF1e7KuXPM5xQ3nTDtpHkZStq1Qm5XsOMcVlufkpgy6x8-YInYRL4POAzWmlRZav5Pao0Zdf6V7qjGB_IGo6qJe91nISwQqAakoerWgHGjLxSSULsA5rYQsKz-iL7FKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b15eae0fd3.mp4?token=bSdNSsW67hI7uAFYd7KfUkGytknoEuSKCO-nkKJPQ6Zdyonw7tCPt8etBkCgRq5-QG0DroBhC7N_GsvT53sJickRe7pAQl6l7OEcRImcCVWH2MrxZSpq69PdSRW88jxdZKUA7g0L3XEEsZuF7xbqxj6HEXWxUAqW10Mt5hMrYkLuKr9r3kWGz_BoVWwosoCzTUz8UdLKnQQgYXwVpotMbpF1e7KuXPM5xQ3nTDtpHkZStq1Qm5XsOMcVlufkpgy6x8-YInYRL4POAzWmlRZav5Pao0Zdf6V7qjGB_IGo6qJe91nISwQqAakoerWgHGjLxSSULsA5rYQsKz-iL7FKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: دشمنان با مشاهده انسجام مردم ما تلاش کردند اتحاد ایران را هدف قرار دهند
🔹
وزیر امور خارجه در نشست هم اندیشی با مهمانان چهلمین کنفرانس بین المللی وحدت اسلامی: سال گذشته پس از جنگ ۱۲ روزه در خدمت شما بودم و توضیحاتی ارائه دادم؛ اینبار پس از جنگی بزرگ‌تر…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/458692" target="_blank">📅 22:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkUrtq6RMVoz4ZQpPrMdZdqeslHsb3HxedrK5N-R5YqsGbQ2A0Yg1Vw_E4UqsQXHPJohtmrj4IVyjuN2tkQaaDal22F6dlsFSPl3-TJxrzig8mNgbA6KnQ-f2wqVxUEayUNJlfkUAjk_gjDzJXffruZvnY7AgIrccnc45Z2LPd7sRBURkso1CnoQGLiikIe2oTC6ohTwXayNHxg5Mxcn7PSW7PgivXGI8DDDH_lfEOCL8EwBzEvxww2A3ZhA0x7tk7i6M8cOBHNa4N7InJH8FyzPpsgMx6_2n1IXVS8KxcEtN1mVfMC4bWkhhSTpFnyQ-snI3u2AOCt-Qm1ip0uksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: دشمنان با مشاهده انسجام مردم ما تلاش کردند اتحاد ایران را هدف قرار دهند
🔹
وزیر امور خارجه در نشست هم اندیشی با مهمانان چهلمین کنفرانس بین المللی وحدت اسلامی: سال گذشته پس از جنگ ۱۲ روزه در خدمت شما بودم و توضیحاتی ارائه دادم؛ اینبار پس از جنگی بزرگ‌تر اینجا حضور دارم.
🔹
بعد از جنگ ۱۲ روزه دشمنان تصور کردند شکست آن ها در جنگ قبلی، به این دلیل بوده که برای یک جنگ طولانی آماده نبودند و با مشاهده انسجام مردم ما ابتدا تلاش کردند انسجام مردم ایران را هدف قرار دهند.
🔹
دشمنان برای ایجاد اختلاف، شکستن اتحاد مردم و ضربه زدن به انسجام اجتماعی توطئه‌هایی را طراحی کردند؛ از جمله اعزام گروه‌های تروریستی مسلح که به مردم و نیروهای پلیس حمله کردند و تلاش داشتند با ایجاد کشته‌سازی، جمهوری اسلامی را زیر سؤال ببرند و آمریکا را به مداخله نظامی ترغیب کنند.
🔹
این توطئه نیز با شکست مواجه شد، اما دشمن تصور کرد انسجام اجتماعی ایران آسیب دیده و خود را برای جنگی بزرگ‌تر آماده کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/458691" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q041UwiXdDLjl3uFvBiixB8JDj3V4KYAx-k6sqb3uFa_YgDpT8WMcRhk0IbfFu_O-QxFMiAqQztJCn3iweaWDQkej0V2A5F_Bxgu8GYBP0kZv1cY6fAtvRi4cD1-d4dc5WpV1BKsOqPFdlpbS4OxDFwWCcoad4vZlIrlcsDPQMLtciT3Ek2wXgKgSpELfhojSyvB-ud82xjTmOnQeBc1tOgHX9DOSDO69ta8BNwdfjWCLCdH3SqEziOHFqMD__LZq8jXkZa_2rQp27k2fAcY-6OEVOvas8wzgSRKi6jVdWxQkZInTVraHiiG8CAGUbOlXNl5X3ahOSk2-s5cKlO3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: در جنگ ایران، کشورهای عربی با واقعیت‌ها مواجه شدند
🔹
الجزیره در تحلیلی نوشت که جنگ علیه ایران، کشورهای خلیج فارس را به بازتعریف رابطه با آمریکا و ایجاد لایه‌های جدید امنیتی وادار کرده است.
🔹
سلیمان العقیلی سردبیر روزنامه الوطن عربستان در این مقاله نوشت که تحولات پس از ۲۸ فوریه و آغاز جنگ علیه ایران، معادله سنتی امنیت خلیج فارس را که بر دو فرض استوار بود، زیر سؤال برده است؛ نخست اینکه نفت می‌تواند بدون اختلال از منطقه خارج شود و دوم اینکه امنیت کشورهای خلیج فارس از سوی آمریکا تأمین خواهد شد.
🔗
بیشتر
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458689" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba965d44.mp4?token=cjr5rDdtSkASOGjzAJm9wfFE-RcVrm_YAicP_hpnGacs347bcluR8s2GMMoKSqLedt0YtcAWABXQpL3L6apBZGL3kDJiezRotCErJHY-BssVQ7LL3bNyvxMx-AtJ-rqVZNKIogJrzP3izGQEoc0mIHh_wvfk9wtS-j2eaRwRIw60O5y6GAW-7kwlWX_MauPC_GCTNiWICRoHOteAd0zdA-xdTajUl8PwlpgUUCJf3nb8wzpRYJ8GyGKLyRD3ddDwyI43FJ-XTEmbw7YNNGayvjV3iIWQMAG4DNCCA1RM9XHQ4NNKiEn91k9jj20FdSlQBQRNRfTCVmYiGziGY7b7gbvCpUEWM-461ypeLAEUFBonAQYAb_DBiTszbTtjS6YP9uXkW3VO0uqjJrsgqBgyCdMl98xI4zS2iVlfHyVxURwyLFxSc08BihWNJsE8eug0fdG9cLv8vreCO1FuwYtmfqmzc3Amcc04w9pj_MxpOM9mlkBzkMV8B_hfaYfKuLuwhQ9-PiN5KITC1b_iBFNQi-AWHuODlqkaDa3xThqe_eo8AQ3HwGd6-zlHmF9vG16JF3YFUXSrgW3MGpL8sBj8EvHLN7RQTQKQCSH64Z7TRijiCNTPwNjQ5BgLzrVgRHYd5BVScCco_5RMVPu9nm08mwClF_0J7uUMN_6JMtkvHgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba965d44.mp4?token=cjr5rDdtSkASOGjzAJm9wfFE-RcVrm_YAicP_hpnGacs347bcluR8s2GMMoKSqLedt0YtcAWABXQpL3L6apBZGL3kDJiezRotCErJHY-BssVQ7LL3bNyvxMx-AtJ-rqVZNKIogJrzP3izGQEoc0mIHh_wvfk9wtS-j2eaRwRIw60O5y6GAW-7kwlWX_MauPC_GCTNiWICRoHOteAd0zdA-xdTajUl8PwlpgUUCJf3nb8wzpRYJ8GyGKLyRD3ddDwyI43FJ-XTEmbw7YNNGayvjV3iIWQMAG4DNCCA1RM9XHQ4NNKiEn91k9jj20FdSlQBQRNRfTCVmYiGziGY7b7gbvCpUEWM-461ypeLAEUFBonAQYAb_DBiTszbTtjS6YP9uXkW3VO0uqjJrsgqBgyCdMl98xI4zS2iVlfHyVxURwyLFxSc08BihWNJsE8eug0fdG9cLv8vreCO1FuwYtmfqmzc3Amcc04w9pj_MxpOM9mlkBzkMV8B_hfaYfKuLuwhQ9-PiN5KITC1b_iBFNQi-AWHuODlqkaDa3xThqe_eo8AQ3HwGd6-zlHmF9vG16JF3YFUXSrgW3MGpL8sBj8EvHLN7RQTQKQCSH64Z7TRijiCNTPwNjQ5BgLzrVgRHYd5BVScCco_5RMVPu9nm08mwClF_0J7uUMN_6JMtkvHgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت عشایر عراق با آرمان‌های رهبر شهید در  دیدار با نمایندگان ویژۀ رهبر معظم انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/458688" target="_blank">📅 21:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ شارژ شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/458687" target="_blank">📅 21:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d231e6882.mp4?token=MnlDHz2U9fI-wDC9zcWmCHRTsscEjimMr6RPVSsl6MxneiHx-1nErYolqnImS8IwLseFHEoEGYpht64RVI2b3MpaR03mdTfxX8Dl0srjv5L-xKNDShZ2eAchmY2ezzy3jMG1migAFX0Fj22ZbdbvCqY5buciu9s3xiJLpvOc43tNPb1XIuIGrlLsuDVyQ7gHapWlQze0g3bgzpIiPcZuFd-YUWEnXUUGRI5ZLmFmszHznGz_e4NEfGUKL9N3fJ8C8IHQXsCP8UetMOg2S57KCBgMkB9KslECjM5Z1iyqg5bqi6Qzs5M4ggQXe0pxwsQZz3gkFbz8TLEKSBlIzTujkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d231e6882.mp4?token=MnlDHz2U9fI-wDC9zcWmCHRTsscEjimMr6RPVSsl6MxneiHx-1nErYolqnImS8IwLseFHEoEGYpht64RVI2b3MpaR03mdTfxX8Dl0srjv5L-xKNDShZ2eAchmY2ezzy3jMG1migAFX0Fj22ZbdbvCqY5buciu9s3xiJLpvOc43tNPb1XIuIGrlLsuDVyQ7gHapWlQze0g3bgzpIiPcZuFd-YUWEnXUUGRI5ZLmFmszHznGz_e4NEfGUKL9N3fJ8C8IHQXsCP8UetMOg2S57KCBgMkB9KslECjM5Z1iyqg5bqi6Qzs5M4ggQXe0pxwsQZz3gkFbz8TLEKSBlIzTujkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۵۰ زندانی با کمک هیئت حسین ستوده آزاد شدند
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/458686" target="_blank">📅 21:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beafc80603.mp4?token=brJbig-ydl-Pcv2sJ7C7sZ7kA_JcS0b2YatGAn2fdzgdWIx8oMaWk2465O6rCCUMhr78I-HKUD45-jyeauucRjbpnnPxuJ2IBpDFiFLQ0Anw7I_cjg9xKHw-68Rg1iHk5py4gizH5ph6yTcLq1fc9dWIJFa5WnKbuzfgfg6f8Ym9w0RQnBTzX9iz3y2oIh9EnL5_xxwmxKufZC4nXELjirrdIGhX_-1qK1oDW9TpRHK1FdiZUaCNIU894ov8qVWusIqQc2JvUkzubyYuNo-kdR9MkAyCrr0WpQkOZydeHKKQdYlddwPtTxux6nkh-evX9vrR-poyz1SU9_Q3XO0zPCPeMMTcLn4L3ZAuhbmYX9O0mJo4xgY2NWK8Y45RNkjhZ08tM67awpiSeRbcRlGc8P1aWQFMLSGAbx87njeK-Tx21qCsS1F68IoCCHscAD4YOlSbMn7s0SZS7fz8ZAEW52ITKLGj4q7g_3jOkvD7TuOI2kMOyT4mE5KXK0TtJrdejTHo2DhfCLV41vk1Wx3UW0ovNIZo5BGih64d3x5-VXM1zKf2wBShoLtEktqBoZIKQwU7zCb17G3jYMD_8Z9hwJOVc07CEwtY9Hc1F-6pCwyUgSGtU93uJiWyfQYhocAhhdKRZBW2pEKhZLYkSV7Qh3beJMF-ajaaLxl1WxoDatE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beafc80603.mp4?token=brJbig-ydl-Pcv2sJ7C7sZ7kA_JcS0b2YatGAn2fdzgdWIx8oMaWk2465O6rCCUMhr78I-HKUD45-jyeauucRjbpnnPxuJ2IBpDFiFLQ0Anw7I_cjg9xKHw-68Rg1iHk5py4gizH5ph6yTcLq1fc9dWIJFa5WnKbuzfgfg6f8Ym9w0RQnBTzX9iz3y2oIh9EnL5_xxwmxKufZC4nXELjirrdIGhX_-1qK1oDW9TpRHK1FdiZUaCNIU894ov8qVWusIqQc2JvUkzubyYuNo-kdR9MkAyCrr0WpQkOZydeHKKQdYlddwPtTxux6nkh-evX9vrR-poyz1SU9_Q3XO0zPCPeMMTcLn4L3ZAuhbmYX9O0mJo4xgY2NWK8Y45RNkjhZ08tM67awpiSeRbcRlGc8P1aWQFMLSGAbx87njeK-Tx21qCsS1F68IoCCHscAD4YOlSbMn7s0SZS7fz8ZAEW52ITKLGj4q7g_3jOkvD7TuOI2kMOyT4mE5KXK0TtJrdejTHo2DhfCLV41vk1Wx3UW0ovNIZo5BGih64d3x5-VXM1zKf2wBShoLtEktqBoZIKQwU7zCb17G3jYMD_8Z9hwJOVc07CEwtY9Hc1F-6pCwyUgSGtU93uJiWyfQYhocAhhdKRZBW2pEKhZLYkSV7Qh3beJMF-ajaaLxl1WxoDatE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما اهل کوفه نیستیم، ولی تنها بماند؛ شعار مردم بام ایران در شب ۱۸۱
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/458685" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4C8bCSqdCQEW-YL5a1LmEeGg8VZfcEFZ2uOW8dD9mlykjAbUf5Yb7j4RvEm-W5NmMAXw-zyJsla353kgT67VNvD7adApewORccp778CvucSOha4UiFfUBFvFw5AxsIH4izWv2LiYh0gLuhH8_PKaO56QQ92RfLQFB1o-MiZ8ffG014adguCekOXU5St_o_8RNUw0i-amg-GtEffmqyAhOFtlKcYeJxXTK41UZPQvdDAAbCYiRA-_zzx3WognvoxMbtDuqKQ4NmI8HCXXgfBv0MHVuqP0vcRb-VWeEKl6S_u3uKk1NUbsuHMZHTjeBkYOqkgwG7POsCTqTJvgwC5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار آمریکایی: ترامپ از جنگ کلافه است و کاخ سفید محیط شادی نیست
🔹
کاخ سفید دیگر «محیط شادی» نیست؛ این موضوعی است که یک خبرنگار آمریکایی هم‌زمان با افزایش نارضایتی دونالد ترامپ از جنگ با ایران مطرح کرده است.
🔹
جنگ علیه ایران اکنون شش ماه است که ادامه دارد و مجموعه‌ای از نظرسنجی‌ها نشان می‌دهد این درگیری در میان رأی‌دهندگان محبوب نیست.
🔹
مگی هابرمن، خبرنگار نیویورک‌تایمز در مصاحبه‌ای به شبکه سی‌ان‌ان گفت: «بر اساس تمام گزارش‌هایی که ما داریم، اینجا محیط شادی نیست. رئیس‌جمهور مدتی است درباره ایران روحیه‌ای بسیار کلافه و ناراضی دارد؛ و البته، خودش این وضعیت را به وجود آورده است.»
🔹
او برای دیپلماسی بلندمدت یا گفت‌وگوهای طولانی برای تلاش جهت خارج شدن از یک وضعیت، صبر و حوصله ندارد؛ ترامپ تصور می‌کرد جنگ خیلی زود به پایان خواهد رسید اما اینطور نشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458684" target="_blank">📅 21:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMNC8dj_yn98QR_zByY5D8BBtE7HBdoYSmqHWQU9Jag1tIePREK_4pRmS_7AClQjpz_8hjGkrDvs85WEOKNssTZSQJzMFG-jeHczLMLOYUe1NHVvZRm8ZYe9bBQi7ilGDzgyCeotkq9iQXh2zEKPkAh1TdJLzVwKdAORnbc2Kk50a5Y3ItGdQa38DkaLdOu3x7uyu62F9XEya586Y2bST2aiPRpu1_s0y2_-cNeYhzXentZRvapCB7O8aTt490g9KALkCGxkREs52sM9X3ub3ERDIevcZzNPQfWjEn1dyRDsbOdbOLpFJNGJxAFNo0Ea2M3w4g7dty_BTCMixSkGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: پیام پرمهر و مدبرانه رهبر عالی‌قدر نظام به دولت چهاردهم و اینجانب امتداد حمایت سازنده و بی‌مانند رهبر عظیم الشأن شهید انقلاب اسلامی است.
🔹
به ملت بزرگ ایران و رهبری عزیز اطمینان می‌دهیم در کمال وحدت و انسجام با سایر قوا در مسیر شکوفایی و پیشرفت، حافظ اقتدار و عزت کشور باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/458683" target="_blank">📅 20:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌  رهبر معظم انقلاب: توجّه فراراهبردی به مسئله‌ی فرهنگ، تعلیم و تربیت از مسائل مهم کشور است
🔹
و از جمله مسائل مهمّ دیگر، توجّه فراراهبردی به مسئله‌ی فرهنگ، تعلیم و تربیت است. تعبیر فراراهبردی به‌معنی آن است که تنظیم راهبردهای دیگر باید با ملاحظه این مسئله…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/458682" target="_blank">📅 20:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ رهبر معظم انقلاب: هر دوگانه‌سازی‌ موهوم از قبیل جنگ یا مذاکره، وفاق یا تندروی، سازش یا جنگ‌طلبی می‌تواند به مردم عزیزمان خسارتهایی بی‌واسطه یا باواسطه وارد سازد
🔹
و باز از جمله مسائل اساسی کشور که همیشه باید در مرکز توجّه دولت و دولتیان و همه‌ی مسئولین و…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458681" target="_blank">📅 20:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9CC-pNWTnkHoRjSvCwDggCzw5n1wYt4_blvv_SdaBHHncUUjXnsFSIsID4Mx9lOpNh-qVpAnxHHj9ks0F776D-7QwzpwrPbe88wMpVrKe-uY-FtC_xkOGzB8uP7USxkYZQ8_aEpd6jC1iOK-P_uSNQsoqzbBGn502gbSMsc0gS1pDSsVvEaH4x4iBgmgZMmYCbk2mbA5UG1CL4N4fAtJf9Xy_UZAHKfaRI5v1OeCyDe3c_kE6bdYYJF6fk4A0V4LD1ijRjolUsvafFH2rH9AQygtPXn6fTAlZ9ymKjkBX_3-Moxl2CJoHRsuL7vZh9GGgLuL6rJKClRzCxI3I4acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: دشمن سعی میکند القاء کند که مسیر پیشرفت از خواسته‌های نابجایش میگذرد؛ در حالی که مشاهده‌ی آنچه او  بر سر این کشور و منابع آن آورده، خلاف این را نشان می‌دهد
🔹
مسلّماً آنچه ذیلاً بیان میگردد در کانون برنامه‌های دولت خدمتگزار یا به نوعی…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/458680" target="_blank">📅 20:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: ملت مبعوث شده ایران شایسته آن هستند که خدمتگزاری مسئولان را حس کنند
🔹
مردم عزیز ایران که در شش‌ماه گذشته عیار حقیقی خود را در جلوه‌های مختلف جهاد با دشمن، حضور در میادین، انسجام و همدلی و همراهی خود آشکار نموده‌اند، شایسته و مستحقّ آن…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/458679" target="_blank">📅 20:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxVRGcYpfFQhQ46fXFweo7qeZQ4FdK9hA4ZIKdQqXMxqh2RcAbPspbZCELK3SLzTrsAVy4jtpNndyBoUazBjKgCwMJWh1o6QZrJpUk3w8ZRZQUQB4uyzq8DSGUvx_jY50LY5yYMjBFPhoafCvtreaapqNEBMvwFxepwRpk9Fah8mioc6Xl3qt43UH1zhH4b47BDqDvL9h6Kh28H9mCyNYtvADvmjiE7BIjOG_qG-KQPNOd7XY4Cqwlr1UKzFCTjrn69557EDknUs3T2k_A9xmqDrPHNeCwZfrxib8FnntzLkq4Wx20lLk0ZLu--qQR7BdrtJ4sXxEi3whxgTV1dgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‍‌  رهبر معظم انقلاب: گاه بیان صادقانه ضعف‌های خود در وقتی که دشمن به روحیّه نیاز دارد، کمک بزرگی به او است
🔹
هفته‌ی اوّل شهریور هر سال، مناسبتی است برای پرداختن به خدمات دولت جمهوری اسلامی ایران. امسال دولت جمهوری اسلامی ایران مفتخر است که ایّام هفته‌ی دولت،…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/458678" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رهبر معظم انقلاب: قاطعانه اعلام می‌کنم ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است
🔹
رهبر معظم انقلاب اسلامی در پیامی به مناسبت هفته دولت ضمن قدردانی از اقدامات شایسته دولت به‌ویژه رئیس جمهور صادق و دلسوز که به‌رغم همه محدودیت‌ها و دسیسه‌های گوناگون…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/458677" target="_blank">📅 20:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrEbTCXXLzL7BuuihBhzL8pjlHAA5VstucSvIwFQ91r2qLcZ718N7Sy9ytFb0peBjEErzeIukMWz4qE2AnNog6PPXCYVdqOPpflh6LfzMzyvVDBpkiFoAyZKGGYgDamrlxCZAZWnBJDIHvYdOkD_YRFxYwFf1WbRPKlRDEVpeeOD2RTggBLZ7gRvqP_hBNY3y6NmygNKK9Z8jNPoqPPr7r-T0ykY2U0pWGPxF6MSn4bh0g3ImnQoXVvUkR5G9YFnsS5aFHRt7NmIzP1NY6FMu68WsP-kWgBx0VmB0t_uRKcE70pw2E_F9Z6cdkbJnQiRZPgss1mrLnxv0DWcRzwnOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به مناسبت هفته دولت تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458676" target="_blank">📅 20:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش رژیم صهیونیستی مناطقی در علی الطاهر و شهر النبطیه در جنوب لبنان را هدف چند حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/458675" target="_blank">📅 20:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bc682e4b.mp4?token=FPjG79wX_Y1Dj-z1WXcDWJxh5GKWZfG8U5Reht_Ry_LxJZhe0RnoYB0BjXB9zfhiBkJfyy1VcV-qdQ73KhG7SY26Uhb91sDMCow6jL83yTEqyp6byUKe3MUgjQtoC8L9N5SsBNxnJu4LVO-pN_yrwRf55qFI97z90IB82ByRIhVmGxDD6XxlrszsxhQYXNYNg5YQAlf1WxUIIIzViSEF3a4Dna0sylBFwfPteS1R5kIlLq5H3OOcEN1sXhDNREdF0MFZd4zFCHccDfHtshe8KpZ1jh-idu6_4ASk6bbAzfJH_snxTgpJGTNs16dUs0AJmbuP81pD502iSmBz9Wy3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bc682e4b.mp4?token=FPjG79wX_Y1Dj-z1WXcDWJxh5GKWZfG8U5Reht_Ry_LxJZhe0RnoYB0BjXB9zfhiBkJfyy1VcV-qdQ73KhG7SY26Uhb91sDMCow6jL83yTEqyp6byUKe3MUgjQtoC8L9N5SsBNxnJu4LVO-pN_yrwRf55qFI97z90IB82ByRIhVmGxDD6XxlrszsxhQYXNYNg5YQAlf1WxUIIIzViSEF3a4Dna0sylBFwfPteS1R5kIlLq5H3OOcEN1sXhDNREdF0MFZd4zFCHccDfHtshe8KpZ1jh-idu6_4ASk6bbAzfJH_snxTgpJGTNs16dUs0AJmbuP81pD502iSmBz9Wy3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت: با تجربیات دو سال اول دولت برای نیمۀ دوم عمر دولت و برای چهار سال بعد برنامه‌ریزی می‌کنیم.
🔹
رئیس‌جمهور آرزوهایی برای کشور داشت که جنگ برخی از آن‌ها را عقب انداخت.  @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/458674" target="_blank">📅 20:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BToJm1Mwy3GZTdeOzCBZvFdYiympuTHBjDmRKgS-UKLKaoqi-ogdrbQ9mpvX6mAjskG3PymFQFlckhATKI1G9Wjf32_SWE1vcC8ieAsXjjW79YTivb6ZSzAYDxSwA90RyzsOV0KuLLzisqjQ24qh88VakzP71bGTqz-jc1wrVpb1OmWbsRct-r6PmxQnCHWd1MJGxLMOV2U_VPNAd0ROLjKwT-Vt1vh0oVV6Om5MzicxkpkpHpn1ckwE_e3DmF9qs9u1nUeZh2bPvD4uNmwAW88sq4n1PbMVkyQt0MhPCHoHvA43voaF_Vw6Z4Ttht5SqadWmrLAMU7wA9knlWg7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: تأسیسات نظامی را به زیر زمین منتقل می‌کنیم
🔹
نخست‌وزیر رژیم اسرائیل با اعلام افزایش ۴۰۰ میلیارد شکلی بودجه نظامی گفت: ما این صنایع را به زیر زمین منتقل خواهیم کرد.
🔸
به نظر می‌رسد سیاست انتقال تأسیسات نظامی به زیر زمین درسی است که رژیم اسرائیل از جنگ با ایران گرفته باشد.
🔸
در طول جنگ ۱۲ روزه و جنگ رمضان بسیاری از پایگاه‌ها و مراکز حساس نظامی این رژیم هدف اصابت دقیق موشک‌های ایرانی قرار گرفت؛ هرچند اداره سانسور ارتش اسرائیل به شدت جلوی رسانه‌ای شدن این موارد را گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/458673" target="_blank">📅 20:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e02222f1.mp4?token=AwNokDLB91h_Vqb0CNTjP2X-RTgRi-wbjqL071yM0GAcfoyI6MAx5mvzNdIhGfQwIkVWQUioS2xiTQW0RdZX1xCJqNOO-TNupBuVxl88LJ8bCB9GUw3TOXtutyJDNYQURgqirz-OVnbYiy04f-EsibScyprRQALtOIjxZblgV741N2CEpKh4K5N5UAAjkAznEcipEs-GnJAYAk0yePi0cJVFSgQ2dziL0FWE3B1lJHyLpjlLgJGjEYz5xf0T9-pzEz3na_VaVa92N8sDpDzJOzQDXY2nZ7nP7aIfx2poohy2XsmY6f-u9_FKRH9x9KD2R15L4D6mjVPHO988OQFTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e02222f1.mp4?token=AwNokDLB91h_Vqb0CNTjP2X-RTgRi-wbjqL071yM0GAcfoyI6MAx5mvzNdIhGfQwIkVWQUioS2xiTQW0RdZX1xCJqNOO-TNupBuVxl88LJ8bCB9GUw3TOXtutyJDNYQURgqirz-OVnbYiy04f-EsibScyprRQALtOIjxZblgV741N2CEpKh4K5N5UAAjkAznEcipEs-GnJAYAk0yePi0cJVFSgQ2dziL0FWE3B1lJHyLpjlLgJGjEYz5xf0T9-pzEz3na_VaVa92N8sDpDzJOzQDXY2nZ7nP7aIfx2poohy2XsmY6f-u9_FKRH9x9KD2R15L4D6mjVPHO988OQFTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس شورای اطلاع‌رسانی دولت از تاب‌آوری خدمت‌رسانی به مردم در زمان جنگ  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/458672" target="_blank">📅 20:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60357b7cb5.mp4?token=rjaF823AIhR5WpAItJ9m5clrUVlW58YhHsJlkNOi1JwVgYfPUWxYgtE5QHEov6Hd8TmMKGSOJ8jFdaKfz-ARFDtanpDGd3u01Z2YoKbFDwMakjTVDZhofcbW_-Q3CaIMDHBebRxhnACwJYKoooa9jVanlnyu_yUhVbfae7lKFapT5PNebCE5H_2Q08D1HThwcFiYHeAgTMZTBvoNItWIrPneVBsKbWEwRelvRssshSTr1UwftkfOGK4B56W5vrMt5SmxyMEUtz9oNEZFaV4LwOCzefzUe8YJ3wsGq1kLl0GjKjDLXR-OYaoCES592NV7sPAbOEedDdtXThD6uCZS5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60357b7cb5.mp4?token=rjaF823AIhR5WpAItJ9m5clrUVlW58YhHsJlkNOi1JwVgYfPUWxYgtE5QHEov6Hd8TmMKGSOJ8jFdaKfz-ARFDtanpDGd3u01Z2YoKbFDwMakjTVDZhofcbW_-Q3CaIMDHBebRxhnACwJYKoooa9jVanlnyu_yUhVbfae7lKFapT5PNebCE5H_2Q08D1HThwcFiYHeAgTMZTBvoNItWIrPneVBsKbWEwRelvRssshSTr1UwftkfOGK4B56W5vrMt5SmxyMEUtz9oNEZFaV4LwOCzefzUe8YJ3wsGq1kLl0GjKjDLXR-OYaoCES592NV7sPAbOEedDdtXThD6uCZS5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس شورای اطلاع‌رسانی دولت از تاب‌آوری خدمت‌رسانی به مردم در زمان جنگ
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/458671" target="_blank">📅 20:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9aca688a.mp4?token=riLv6j65Z3pzY_J2gKYK_qyDse9BRkbvrCOEgiCRxDjiRPsN1iOZbCVTDF_GyuRlvTuphRGpmxP_ocyzQL0KaGRGtUhJ_uKTkqUUwG0kR-TVwu8dTJDcTFruaDeJCLGgLoQCW-YYBxl4uIBSv_9A2IcRPAGZ7yrk7lZ4EGs7NlCbZGWKeWRJ5yzcghd839LbtLdu2H_Y_bKIIRgVTiau2-c16RydqBu1mYRi45oqLQHP-Osi2NrEhCLCotzIHvghYmlZEPkDNybBhuLtbYWzHJi-CMHCZhs5vWl_LcMlsTxHTPH-QHdHItiX9WjHvBCwhf0ZUFxFaQLK5J7fqwoErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9aca688a.mp4?token=riLv6j65Z3pzY_J2gKYK_qyDse9BRkbvrCOEgiCRxDjiRPsN1iOZbCVTDF_GyuRlvTuphRGpmxP_ocyzQL0KaGRGtUhJ_uKTkqUUwG0kR-TVwu8dTJDcTFruaDeJCLGgLoQCW-YYBxl4uIBSv_9A2IcRPAGZ7yrk7lZ4EGs7NlCbZGWKeWRJ5yzcghd839LbtLdu2H_Y_bKIIRgVTiau2-c16RydqBu1mYRi45oqLQHP-Osi2NrEhCLCotzIHvghYmlZEPkDNybBhuLtbYWzHJi-CMHCZhs5vWl_LcMlsTxHTPH-QHdHItiX9WjHvBCwhf0ZUFxFaQLK5J7fqwoErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای مردمی در پاسخ به یاوه‌گویی‌های ترامپ به تنگۀ هرمز آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/458670" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dafd32e13.mp4?token=VownApcfHtapp6w9Yqh3caMWka40_8y5EvONhgRvY3Qfd6jUx1lyAH2OzyPlYQ7JsLgMBC8P3rplNLPPFwou5PvfSF14SRDJZR7zKZihU7PZHtur9eZuONmf44bCVJnr0qFYI-iwO_y6E2yDaNaRChSx1EwBDLYDwv_Uo3zoSzvosE8IbwkKp7RfOn2zqUNkvQZdmm2DkuAtg2YCZ-7HyD-bgmyAjbda8POd6LOWPogEH4KEN1p5_anslrJ80zASdUpJsA9Jv_SCYC2DxUne1rHCvX3_uQUwTHDXP_zBrQwXm_EUrEuVA0a794GtkNipburfSts-QAWxaiQnQ6zs3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dafd32e13.mp4?token=VownApcfHtapp6w9Yqh3caMWka40_8y5EvONhgRvY3Qfd6jUx1lyAH2OzyPlYQ7JsLgMBC8P3rplNLPPFwou5PvfSF14SRDJZR7zKZihU7PZHtur9eZuONmf44bCVJnr0qFYI-iwO_y6E2yDaNaRChSx1EwBDLYDwv_Uo3zoSzvosE8IbwkKp7RfOn2zqUNkvQZdmm2DkuAtg2YCZ-7HyD-bgmyAjbda8POd6LOWPogEH4KEN1p5_anslrJ80zASdUpJsA9Jv_SCYC2DxUne1rHCvX3_uQUwTHDXP_zBrQwXm_EUrEuVA0a794GtkNipburfSts-QAWxaiQnQ6zs3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت: رئیس‌جمهور به پشتوانه اعتماد رهبر شهید حل پیچیده‌ترین موضوعات کشور را در دستور کار قرار داد  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/458669" target="_blank">📅 20:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به مناسبت هفته دولت تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/458668" target="_blank">📅 19:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دستگیری ۶ عضو جیش‌الظلم در سراوان؛ یک تروریست به هلاکت رسید
🔹
سخنگوی پلیس: ساعاتی پیش، در درگیری مسلحانۀ نیروی انتظامی سراوان با همکاری سپاه و سربازان گمنام امام زمان(عج ) با گروهک تروریستی جيش‌الظلم، یک نفر از اعضای گروهک به هلاکت رسید و ۶ نفر نیز دستگیر شدند.
🔹
در این عملیات، مقادیر زیادی سلاح و مهمات از جمله ده‌ها قبضه کلاشینکف، نارنجک دستی، آرپی جی ۷، حدد ۲۰ ‌کیلوگرم مواد منفجره سی فور، ۱۵۰ تیر فشنگ جنگی و چند دستگاه ماهواره استارلینک نیز کشف و ضبط شد.
🔹
نفرات دستگیر شده، از عوامل شهادت همکاران انتظامی در فروردین گذشته در سروان و نیز عامل شهادت یکی از کارکنان سپاه در ماه گذشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/458667" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ec1553f1.mp4?token=IKAf9jzRj0daWVHcMb17hRjudY6CQqh_MmyuGwGetx-wt0o__sfnlWx8YpF3-8mWMv2gVyPq9uGqZiWWXyBv4lIlBG1L7fLzTiqomqJmkaMI90_7GUHDaycxGD644-hy2EYpgPx-VYD-BQfx6JW184StU88rBU_h1qmFAamC42Y_S3pAw6JAeYyRY6KYrOkPG46V-w93mYuCCMtJLQ1bnI2WP1rvup3JS5HM0PoQ5pHIbGAu_vJ2a2qAQhJHNvFAzPNF3jU9_f7GSJLSWJdQIdhtrvfNi9Ah-sZylUkB6Ms-Xdp4CY0ic6wKIZopU4xLETJbE3Ik8UDWfev1hyQTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ec1553f1.mp4?token=IKAf9jzRj0daWVHcMb17hRjudY6CQqh_MmyuGwGetx-wt0o__sfnlWx8YpF3-8mWMv2gVyPq9uGqZiWWXyBv4lIlBG1L7fLzTiqomqJmkaMI90_7GUHDaycxGD644-hy2EYpgPx-VYD-BQfx6JW184StU88rBU_h1qmFAamC42Y_S3pAw6JAeYyRY6KYrOkPG46V-w93mYuCCMtJLQ1bnI2WP1rvup3JS5HM0PoQ5pHIbGAu_vJ2a2qAQhJHNvFAzPNF3jU9_f7GSJLSWJdQIdhtrvfNi9Ah-sZylUkB6Ms-Xdp4CY0ic6wKIZopU4xLETJbE3Ik8UDWfev1hyQTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت: نسخۀ دکتر پزشکیان برای مسائل حل‌نشده، همدلی، هم‌زبانی، همبستگی و اعتماد است  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/458665" target="_blank">📅 19:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6fPIYYtGYHUUyG5PaD9JRR_ghDmJe2xig9AzELYiszD-9xEPbfo8He1zaIpJ_qZiFZND7GLbaJPv4xGNfMwprg1wpASscjT9Qm-WZF8Nu_35huYmjvtV3Hplmdh_xCi3fCG_tiThYOKjw0YHuMd_a1bCHAsV2uXrhdBTaXsOLz-Vzic6wzhTlpL9wyqOWK2dMW44ttzYW8AIEFPvWE6s6FBjN7zvjlrylB5_KW3H4p1qeUuzQN0Xl9jXD1YKsaqDCEuuvzfYuAAuvfG5DObr0EO0x2fCbo7LtAlgMJ8a2BA4TmKCCaQa-wLEblB_VRbpAEk6jOGsddf2Kqr98xbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت یمن: با هر هزینه‌ای به مقاومت و حمایت از فلسطین ادامه خواهیم داد
🔹
بیانیه دولت صنعا در سالگرد شهادت نخست‌وزیر این کشور: یمن محل تولید قهرمانان و رهبران است و هر فرمانده‌ای که در میدان جهاد به شهادت برسد، به لطف خدا ده‌ها فرمانده جایگزین او خواهند شد؛ در راه خدا نه عقب‌نشینی وجود دارد، نه ضعف و نه سستی.
🔹
با وجود حملات اسرائیل و آمریکا، این کشور همچنان به مواضع خود در حمایت از مردم فلسطین و آرمان فلسطین پایبند خواهد ماند و از حمایت از ملت‌های اسلامی تحت حمله دست نخواهد کشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/458664" target="_blank">📅 19:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55421da1ca.mp4?token=XSyEa-MWBERLgTnshOXhBzUYMz95kXhzNnnF8E21-soj2AZ68tigXIUXyZWBXLIv-TYuZqH9iMpG9F15naC9SXqY0WwxBOA6xRT_i34CBLmL9erin_ReM2FVGYwKQo8jFSWjOtP3z0FEn57crKAY5Yb-RhJX4mSmWlNcG3dAROvIsAwQjyjxB5RLgvBH1T3jbU6HKGB_Fdh46BnT7L2JOsOVb4i0qacxREgyy-Lrb_B63aJJvZNAYcQW1zFb6H85B4LOt7JPY-8YtfzMwQMg63hiZ78a-BPgYz26kqIY5Xg-z3eUj-vo2nXW-__52y7iS3WCEm4VemM01qsb14ku5g0x4dFEvEApjtxzkg4-72JO4RlJ_pxcun88EePHBTSyBClb45DkfsnBgzMG0nfTS4RB1aAx0lKvauMGz0azKIthixpTRdo1jkJNLmM-tAZAdb9Mn57EgCiuDOpQzPZff1ceNqer_FOgC91rcuAYW6S0OSYL3Mdekz9mMpi3jBTs8PI-OZccZmC2aviUQlpdZX67ozhxx6aMNwUO7KJcuT1glkoxLscCQsWrAT9Z4dUpWvfYb92eC_x8YWfsyXjbOXGnbUhRI1H41v_hCp3NwjgNxN_WjElV-hsK_LsmJun3v3pLrc5Gx2kb-DaPPFFmETZrhlLfSEJic9iCzD-aimI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55421da1ca.mp4?token=XSyEa-MWBERLgTnshOXhBzUYMz95kXhzNnnF8E21-soj2AZ68tigXIUXyZWBXLIv-TYuZqH9iMpG9F15naC9SXqY0WwxBOA6xRT_i34CBLmL9erin_ReM2FVGYwKQo8jFSWjOtP3z0FEn57crKAY5Yb-RhJX4mSmWlNcG3dAROvIsAwQjyjxB5RLgvBH1T3jbU6HKGB_Fdh46BnT7L2JOsOVb4i0qacxREgyy-Lrb_B63aJJvZNAYcQW1zFb6H85B4LOt7JPY-8YtfzMwQMg63hiZ78a-BPgYz26kqIY5Xg-z3eUj-vo2nXW-__52y7iS3WCEm4VemM01qsb14ku5g0x4dFEvEApjtxzkg4-72JO4RlJ_pxcun88EePHBTSyBClb45DkfsnBgzMG0nfTS4RB1aAx0lKvauMGz0azKIthixpTRdo1jkJNLmM-tAZAdb9Mn57EgCiuDOpQzPZff1ceNqer_FOgC91rcuAYW6S0OSYL3Mdekz9mMpi3jBTs8PI-OZccZmC2aviUQlpdZX67ozhxx6aMNwUO7KJcuT1glkoxLscCQsWrAT9Z4dUpWvfYb92eC_x8YWfsyXjbOXGnbUhRI1H41v_hCp3NwjgNxN_WjElV-hsK_LsmJun3v3pLrc5Gx2kb-DaPPFFmETZrhlLfSEJic9iCzD-aimI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز جشن ضیافت امت احمد(ص) در سنندج  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/458663" target="_blank">📅 19:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1165d827c0.mp4?token=e3Ynh5Bm-m2NdbSBg91-AhCNO7AACThyLnP21QhnoQyzdPSeoDkRGs8nCD6ivZ0vmuhCucANlflDhimYFKyk8qKXRKTa9mZDz-qcMhzabwgoN-rZIb0KreNtKFRzB-_TIK5tQUrVsGBRvlh4aq3FI0lZunIPYcaBKkJ0U_Iib6teDqyKYkYmWVmDrMkcfBkwQtZF1KgBGgjDCxJnK5FtQC4mEEELK7Rcgum7Q4YfXng5XrP--i6EmzbqHOnawTbtaQswfakwfNHxGoDt5SrTNalScvD2KUH0M3UXLK0L4Zt64csJ7P6JxNv-oPd7k98FulFlVsi1ynnMJ1pQHV9CjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1165d827c0.mp4?token=e3Ynh5Bm-m2NdbSBg91-AhCNO7AACThyLnP21QhnoQyzdPSeoDkRGs8nCD6ivZ0vmuhCucANlflDhimYFKyk8qKXRKTa9mZDz-qcMhzabwgoN-rZIb0KreNtKFRzB-_TIK5tQUrVsGBRvlh4aq3FI0lZunIPYcaBKkJ0U_Iib6teDqyKYkYmWVmDrMkcfBkwQtZF1KgBGgjDCxJnK5FtQC4mEEELK7Rcgum7Q4YfXng5XrP--i6EmzbqHOnawTbtaQswfakwfNHxGoDt5SrTNalScvD2KUH0M3UXLK0L4Zt64csJ7P6JxNv-oPd7k98FulFlVsi1ynnMJ1pQHV9CjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت:پزشکیان با سیاست گوش شنوا، راستگویی و دعوا نکردن امید را پایه‌گذاری کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/458662" target="_blank">📅 19:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7caf1ab76f.mp4?token=ulMwj086eOlFaO33iEw0Yo3lKU5M7YbtKLuIBgejmb4OTRqcyuk43NHr-FbwMD99V2bVSYDdU8a2wOrvd1YHgZ7AB5l9YHY0fQ62mnmJZQFP65yb20Jbbz_4DszAX18IXsXoZP9Y8HDSGxWDJRSiN-mxJCM61z72YDePgMhwH86P02ClpAvYFXIs6Dl68JU9qwF3lXAYjNWiWtn149uaelfI-ZZ00h37wJdCEhPzry_j1j61JlpBSyefiRlHJbopP1gcNOg7l9nm9Uqkw9ac3wg_pxTW38Knbp0VMgYDBf-_KsC59x7IVFpmod9jPdb6DDQRCD0PT6gsQcEKPNHxcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7caf1ab76f.mp4?token=ulMwj086eOlFaO33iEw0Yo3lKU5M7YbtKLuIBgejmb4OTRqcyuk43NHr-FbwMD99V2bVSYDdU8a2wOrvd1YHgZ7AB5l9YHY0fQ62mnmJZQFP65yb20Jbbz_4DszAX18IXsXoZP9Y8HDSGxWDJRSiN-mxJCM61z72YDePgMhwH86P02ClpAvYFXIs6Dl68JU9qwF3lXAYjNWiWtn149uaelfI-ZZ00h37wJdCEhPzry_j1j61JlpBSyefiRlHJbopP1gcNOg7l9nm9Uqkw9ac3wg_pxTW38Knbp0VMgYDBf-_KsC59x7IVFpmod9jPdb6DDQRCD0PT6gsQcEKPNHxcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت: پزشکیان در این مقطع حساس و پرحادثه با دو مؤلفه صداقت و سلامت توانست اعتماد مردم را جلب کند  @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/458661" target="_blank">📅 19:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50468e696c.mp4?token=OH0gcf33P5Bc_95dwmx10eMLFKwEB49q1gYn0P_1ZbzLsGjLR_66uscLsAaFjLB-vpUgqgbmcNJyjHQKmhD7IxcmQIIuRBowCgMIVrCEyaDWoeAhtr4DqypBU5s0zNx_-5ECqoxretFX7y1jFTekVDCw1D1iveWnv5--f1v7ZTzg7lNlUo2iZ_nU9pkHyc3ra1tTI4nAkc45xWpfxjYR5yZD_XYx_GvEClDwHtzIKikQAEbWPpjOVhqb_8XUJVYA6ieI50GXfAbYPOEJOYAuVWDhhj0pqh2C48rypvDX3osgSSxPh2VFcdiYivprT-NJGw1WkLw3a-93dICiBEWUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50468e696c.mp4?token=OH0gcf33P5Bc_95dwmx10eMLFKwEB49q1gYn0P_1ZbzLsGjLR_66uscLsAaFjLB-vpUgqgbmcNJyjHQKmhD7IxcmQIIuRBowCgMIVrCEyaDWoeAhtr4DqypBU5s0zNx_-5ECqoxretFX7y1jFTekVDCw1D1iveWnv5--f1v7ZTzg7lNlUo2iZ_nU9pkHyc3ra1tTI4nAkc45xWpfxjYR5yZD_XYx_GvEClDwHtzIKikQAEbWPpjOVhqb_8XUJVYA6ieI50GXfAbYPOEJOYAuVWDhhj0pqh2C48rypvDX3osgSSxPh2VFcdiYivprT-NJGw1WkLw3a-93dICiBEWUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای اطلاع‌رسانی دولت: پزشکیان در این مقطع حساس و پرحادثه با دو مؤلفه صداقت و سلامت توانست اعتماد مردم را جلب کند
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/458660" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلاش خزانه‌داری آمریکا برای ارعاب موسسات مالی از همکاری با ایران
🔹
وزارت خزانه‌داری آمریکا امروز اعلام کرد که دسترسی‌های «بانک مصر شعبه امارات» به حساب‌های کارگزاری در موسسات مالی آمریکا را قطع خواهد کرد.
🔹
خزانه‌داری آمریکا همچنین اعلام کرده که نام مدیر بانک ملی ایران شعبه دبی و یک شرکت مستقر در هنگ‌کنگ را نیز در فهرست تحریم‌ها قرار داده است.
🔹
وزارت خزانه‌داری امریکا گفته این اقدامات ذیل سیاست تحریمی اصطلاحاً جدید آمریکا موسوم به «عملیات طرد اقتصادی» انجام می‌شود.
🔹
بسیاری از کارشناسان مسائل تحریمی معتقدند که عملیات طرد اقتصادی بیشتر از آنکه به دنبال ایجاد نوعی تغییر پارادایمی در اجرای تحریم‌ها علیه ایران باشد یک جنگ تبلیغاتی است که با هدف تسهیل خروج ایالات متحده از جنگ بعد از شکست در میدان نظامی طراحی شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/458659" target="_blank">📅 19:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حماس: تنها با خشم و مقاومت بیشتر به جنایت رژیم صهیونیستی پاسخ می‌دهیم
🔹
بیانیه مقاومت حماس درپی حملات امروز اسرائیل به جنین: تأکید می‌کنیم که این جنایت هولناک، که به سابقه خونین رژیم صهیونیستی علیه مردم ما اضافه می‌شود، تنها با خشم و مقاومت بیشتر پاسخ داده…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/458658" target="_blank">📅 18:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvgL4rhFZDUKpXAXXh3hFthGCi_hJznhYz3RnNT5FO0CKmwcV1nb6DNAxtl_E_RehMS7xSsn6NUKh6G5dcqEs9hw5sLOLOvQaQa8IzGzJjekdegKa21MTiPDXRjhjtP57_I6q5pJe74VNQF0WawWeqgJZUUfElLeylCS0pTwRy51Kf6359tx0ZvzV0zK2CKUw8QT6Cfe0YgNZkpvXixKix55YgvkG3UqOSkBhr3BoyH8JiGgcXNZsSUZ52CEuSNOA92Vc_730pnx7cdP_3P7nIHqLNZqB5Uz_nHI2ZNA5NnI2Oh8Yf70jt7PHO1Xw8zClkYyhqlvP-4xzCtdeEHLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtBkLDFOANublZT4GEbvqqrLNwl6PZm2svZuCHB7FncJkV2yX6o3LQTmKQga-ByJ97MqGZ07P7iHVm2sarPIy7Myj9uaTt2-oKLHw--JWB1tyuhxHRfrhtx-eBZ7_WMV6UK1KEhN0UsKpaAeVFVt28BOORTaKo2MsxIpqBwiYP-_xDrsErO5qIYiNH9JVL5KDV3Odt6cqmOw5Rfvz8d6ky6Ha0YffWTIWOydyD2aoa13cWbuRu-umPGuLeszv_nQOmuA7fYze0_GaBLNhdaqyjZ6xCoJ9XAwpRWipW8KuWjLHyUQWQW7QAMaW7bpGBN98V8hlIFppwPyzakbjuqZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUJAjyrRYSZt5NNvljlbrc_zwFVv_DmWG_hDsrvv4W9W_JYtr9gJOKsVKHMkeSvtdSOxazJXP7a1_SK7zZadki6tPC14WXg1ZSpNtU140utuqKz-BdZnPgS5snEl3IA4y2Slkr-GAy3begDdtUrjJrqbcAlP-_vTd-7e47PUXleDXBPf-YBbRBmikKDxVveqAH4NsLhHXzuQcxlEmkPlV685kNtU4FBohkryWDoby6pyUFqtz82ds8JluGqiIf90hBBYZJJkzvsrW6LxJH7qRXVTjEwGFwFUJ2OHHSO0XFEJQOdlcyZzYe7ZNIwYcseuo_KIJJXY_AR_FBgKF91myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_ssaowaWGex8Yc0oqAZxZb93u477lqhuItD4f8x7OK4UckF7o89AYZJHKKSwdrqus-XEO76H6en7gx2N7Ulwuc7-0YAKvmrWsxxGd0Ea90GK30_T80_KIRp8zNZ0uudZDSqWqgY39h0eK6_qPQZJGfSywwpljHJMHaOS0-XiJRi8AkPHFMcdQCcQiP2CnTItCQiRFP4PKQ_fpqLk02AIIxJwTIlH8H3Xd9FyLSS3ndflL33mRMypwe2XJf--I2ozAeJFrFxocTDAaGGcCg4gNdPpCGno_Cxd1nhf79GCJqU_koL9Nc3cX9cPI3PqzCuX0bAh4A5fJVpqbDwwYmeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bnf6eVYMHi9mK4y5cco147_dx4fgiJit5BME89rR6FkJbGo9m74nysNjWAJRk2RUggYFXXlD_VTdWA-UxuBxR14SWEnimqVpAlVgQpfc87dg6JYUVtqdg2TvsY71oNF_yQsaLmwRbBs3Y7kPiqzutvX8q7FPR4Xx9b8REa7UOUmueuQ5BU7WukNj5ArCoSrnSTA0RWVgdhe6uZG4FPLMPGGN9mqEPXhOETDFx857TJlGvlAoqD20LBjxwJk7fD5yww7k1HVNvCJtXUwayQ09v7JdOfuB0faGiA7qeAvRPx1VxZ-DaEmpV8pDGPi6jku8xa1IGJjo9IYooX7Hh2jWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goMJIK40bkDBSQLWjgbA5dfhdnBszBDluOu7eZnorjiwz0BR6CAEDboakg9aTtzypwXa-n1CY29m4PdjLhUOonMDpkTkN6mw2UVUw4DkfZnsgzT3HNMdLrges-AiHIfSBgWAC6kr_kUHZFExWe37FiKlQa1WN4h8CoAI39AuFLwl5OpXDg06I84cIqOFXmQ7I-lf53nySqNptrACOHHKwt6AVinD7PEdfC5rrZUPA31DOirSPLSufkxrK-s1oGy5SKKEnBgOVL7b2wysPJpRzzeOJQ9C5QWN5fmVQPRUxwI-Wa8u4jitMS9FrzcZVhlBDlsiVf65aAJQu3NzRUKkcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عراقچی: هیچ‌گاه حادثۀ مدرسۀ میناب را فراموش نمی‌کنیم، نمی‌بخشیم و همواره آن را دنبال خواهیم کرد
🔹
وزیر خارجه در بازدید از نمایشگاه مدرسۀ میناب: این آثار سند حقانیت و مظلومیت مردم ایران و کودکانی هستند که در این جنگ به‌صورت ناجوانمردانه و عمدی مورد هدف قرار…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/458652" target="_blank">📅 18:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffde2f1979.mp4?token=j9rTXRZSX95-0eICdrYC_uS1-etTTLx7tr9qhUoTZeT5QY4th58g1HxsVI-RReuP_7LZZf7bkjwK14Zw8R22BhPCHMuynVan2SY3v5I4Wz1sFPcgoTAdH9THrue_oT_kGrkheCW8MWXH8fS_FrRA6zRipiE6PFXz4JCOhcdYtupy2pTc-qrdZ50RbpoHorg5x7S9WUmfXzzvnDdhEAyLNCl_yZlFyaVJaGQXVbUTBmptn5QXQ73AXETWzy4E2wWEihqz6QuIXM99kjEOdkboh6jl5h773JEIdnPEx6CMe_pusFSil68wxXazepgEjmJ7mXBB7oI-lvHWotw-ugXsnHsj4SMyjhdZrzV46zHS5l2KSD9RW0nj0TSG47vzLJ4GZeIX0TE_KWBfGTLJAIhvJ_wvIJdSB5844TkhHuN8CbaYvr5BaDEBopinhR8RxR5jysv88pIzpOvCMnJmyCVBOuXAvdPjWg6W0QEKxKgEWoNeOPera9fTGNESB5d82uA9-AyijXGti6eIgy1UTn84R7MS6s2FE4NhUbM1Q1Jq_b_n4QQa_2TPOlYwO-Llob8Cuzp8NGBRiZ1Ov6Gm_US1CIGZKaF3mPzAkU8dZsDmHnxrJvu5243QbZGwsx9VEkAejqH7XQ3b7wKGlWUFzuRcQu09xMVEude1UT0AUy-sBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffde2f1979.mp4?token=j9rTXRZSX95-0eICdrYC_uS1-etTTLx7tr9qhUoTZeT5QY4th58g1HxsVI-RReuP_7LZZf7bkjwK14Zw8R22BhPCHMuynVan2SY3v5I4Wz1sFPcgoTAdH9THrue_oT_kGrkheCW8MWXH8fS_FrRA6zRipiE6PFXz4JCOhcdYtupy2pTc-qrdZ50RbpoHorg5x7S9WUmfXzzvnDdhEAyLNCl_yZlFyaVJaGQXVbUTBmptn5QXQ73AXETWzy4E2wWEihqz6QuIXM99kjEOdkboh6jl5h773JEIdnPEx6CMe_pusFSil68wxXazepgEjmJ7mXBB7oI-lvHWotw-ugXsnHsj4SMyjhdZrzV46zHS5l2KSD9RW0nj0TSG47vzLJ4GZeIX0TE_KWBfGTLJAIhvJ_wvIJdSB5844TkhHuN8CbaYvr5BaDEBopinhR8RxR5jysv88pIzpOvCMnJmyCVBOuXAvdPjWg6W0QEKxKgEWoNeOPera9fTGNESB5d82uA9-AyijXGti6eIgy1UTn84R7MS6s2FE4NhUbM1Q1Jq_b_n4QQa_2TPOlYwO-Llob8Cuzp8NGBRiZ1Ov6Gm_US1CIGZKaF3mPzAkU8dZsDmHnxrJvu5243QbZGwsx9VEkAejqH7XQ3b7wKGlWUFzuRcQu09xMVEude1UT0AUy-sBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز جشن ضیافت امت احمد(ص) در سنندج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/458651" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPR7gTx5_kCArRNDKESQwI1QdQZ0g67cYsqnhocchQ0tS4M3btQ_kqcSn5QIV95n7U9jZm2hhWCAAYzyZ0rchb5BnJ5_axrewzEUpIMiLzUoBmkfjDx-eNeY9LbobffheJRpQ_6v45_-VdtgQ8o2EN5lEsFNTot04pUpW0ilSQSK6ZZQQwiWwTZTrZaeOhTgWLDNEG52v4z81tTBPDi7o7-OmUsjkgulm2r1uV7eN9NnkZvX8tDSQa6IlIqaJ5ktZwarFhlseUKl9kNuwp4BuJCLFPKNkt5lbbSo3oO2DfFiEiunqVGy6-cOQHUknoGLLWskdRqtCr9AI5ynqFBO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان هندبال ایران از آسیا گذشتند و جهانی شدند
🔹
تیم ملی هندبال نوجوانان ایران با برتری مقابل ازبکستان، راهی نیمه‌نهایی قهرمانی آسیا شد و سهمیه حضور در مسابقات قهرمانی نوجوانان جهان ۲۰۲۷ را هم به نام خود زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/458650" target="_blank">📅 18:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDLY_GfAIDEbCKY0MnvliomLWl6xQ0zI8H0I92kaSWHCqz9g3I0F18QSSVWux1K_Y8jQ0zFDP2NLvWTmFPVsqQUAf5DJmSmUI9TJvR3ashoM6ZjKMb_FxaFeFzUyJdQm_9pvRO73rO1EpbYON8Y-UypJUU57Vh0znqW6Pc_hD8gfbWx0xqMezU8pUR6NjOWmsvX1CSBryWNF9oUOsEUEKPnvXyJiX37hKLayZA5a1wn5md1HASPvvw1ta6Nkc51xNFwS5V77E3hqsQf8lWsnKPcSh9C6Zx5gSCeC4ienNAM0dtUXGULnSZjx1GEm6I0uTzVeDajFjr7zINt3mjG0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفر ول کن؛ روایتی از یک اظهارنظر جنجالی و پاسخ به آن
🔹
ساعاتی پس از آنکه محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور، در اظهارنظری بحث‌برانگیز درباره توقف غنی‌سازی هسته‌ای صحبت کرد، واکنش‌های گسترده‌ای در فضای سیاسی کشور شکل گرفت.
🔹
این اظهارات که با جمله معروف رئیس‌جمهور خطاب به او یعنی «جعفر ول کن» گره خورده، بار دیگر بحث درباره مرزهای تخصص و صلاحیت در تصمیم‌گیری‌های کلان کشور را داغ کرد.
🔹
محمدجعفر قائم‌پناه، در بخشی از سخنان خود که بازتاب گسترده‌ای داشت، با اشاره به موضوع غنی‌سازی گفته است: «من اگر بودم و می‌دانستم آمریکا می‌خواهد رهبرمان را شهید کند، دست از غنی‌سازی برمی‌داشتم!».
🔹
او با تأکید بر رویکرد عقلانی پرسیده است: «چرا صنایع ما را بزند؟ چرا راه‌های ما را بزند؟ چرا پالایشگاه و عسلویه ما را بزند؟» و خردمندی را در دستیابی به هدف با «کمترین هزینه» دانسته است.
🔹
این سخنان، که در برخی تحلیل‌ها "ترجمه ساده‌ی سازش" و پذیرش کامل خواسته‌های دشمن تعبیر شده، با انتقاد تند برخی چهره‌ها و رسانه‌ها مواجه شده است. منتقدان معتقدند که چنین رویکردی با روحیه استقلال‌طلبی و ایستادگی مردم ایران در برابر فشارهای خارجی همخوانی ندارد.
🔹
نقد ورود به حوزه‌های غیرتخصصی در همین راستا، یکی از مهم‌ترین نقدهای وارد شده به این اظهارنظر، به جایگاه و تخصص گوینده بازمی‌گردد.
🔹
بر این اساس تأکید شده است که لزومی ندارد مسئولی در تمامی حوزه‌ها، به‌ویژه مسائل پیچیده سیاسی و عقیدتی که در آن‌ها تخصص و اشراف کافی ندارد، اظهارنظر کند.
🔹
سابقه قبلی و تخصص گوینده در حوزه‌های تجربی یا پزشکی نباید این تلقی غلط را ایجاد کند که او در تمام موضوعات کلان کشور صاحب‌نظر است.
🔹
این نگاه، در تضاد با رویکردی است که از مسئولان می‌خواهد تنها در چارچوب تخصص و مسئولیت‌های تعیین‌شده خود اظهارنظر کرده و از ورود به مباحثی که نیازمند اشراف کامل بر ابعاد مختلف امنیتی، سیاسی و بین‌المللی است، پرهیز کنند.
🔹
منتقدان، سخنان اخیر را مصداق بارز چنین ورود غیرتخصصی‌ای دانسته و آن را فاقد درک درست از شرایط حساس کنونی و جایگاه راهبردی کشور ارزیابی کرده‌اند.
🔹
هم‌زمان با این حواشی، معاونت اجرایی رئیس‌جمهور با صدور اطلاعیه‌ای، هرگونه برداشت تحریف‌آمیز از سخنان قائم‌پناه را رد و بر ضرورت پرهیز از تفسیرهای گزینشی و اختلاف‌افکن تأکید کرد.
🔹
با این حال، اظهارات مطرح‌شده و واکنش‌های گسترده به آن، بار دیگر نشان داد که در شرایط خطیر کنونی، دقت و تخصص در سخنان مسئولان، از الزامات اجتناب‌ناپذیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/458649" target="_blank">📅 18:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W99n32h5ozrO_EiXLjtBi7qwhkbU2eECIYxDdQ5FPH1If3Nm8o6H77bbD6-Tey1-qdO7QfRk3TOCtRlwocIT6_8h45eGyUX7iMoxIf41L08XNAAbYKGIQZleHdRtXdorwl6AyTtRnqrcVc22HlPrNv8vGi_yQr3FhmQGvPKTsDXyCRSr9Zh9lQ5iFw9uqY5KDyVLMGlHGwMZeoN6G2u0-dJ96FWxStT_17N3J9K_kxeSaEMBGJqZBQbsAhrmDAXhOXGqOo-evcWUNspzQ-AprZ9MZpiHG8Q7PAOKlPZiVrcnG7TS6CPGGAAIRkxQwI4KxfqfdOwQnBMDvoSka86r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ رژیم صهیونیستی به یک خودرو در شمال کرانه باختری
🔹
شبکه ۱۲ عبری گزارش داد که یک خودرو حامل سه سرنشین هدف حمله پهپادی در استان جنین واقع در شمال کرانه باختری قرار گرفته است.
🔹
به ادعای این شبکه یکی از سرنشینان، فرمانده نظامی یکی از گروه‌های مقاومت در کرانه…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/458648" target="_blank">📅 18:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox5txA7i1I_HqT7EWQlx03IVQM8nFh5akPI5VK0Tr6ri2gSWAu9jkMQGH5BKs0wrGkFPW8TYojzsmv-YjPKbuj_N1jn5rB3K0RzpyjaW0BG7xCauxgALNYhXKaLrz1H-EmWsbe2UnoMq4RB0vAZ3dIHwLdPaahXxO5I-KKwE_RyM6uzaxhso9EIMU1VXrM1J6XrtUflQGmtrMz1Lh7QWtQFg0dmW5jyN_rAR54GRmHaDO8xqrFmbvQKADaTTn0ul1aO4zT66RtBV4wyn8CnmpKetHZ2lInA6rnzmGfbtJYj-7lA29D6oIjqBCOR1rOUgQy6FeaMcFECXauKEuB9IEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: هیچ‌گاه حادثۀ مدرسۀ میناب را فراموش نمی‌کنیم، نمی‌بخشیم و همواره آن را دنبال خواهیم کرد
🔹
وزیر خارجه در بازدید از نمایشگاه مدرسۀ میناب: این آثار سند حقانیت و مظلومیت مردم ایران و کودکانی هستند که در این جنگ به‌صورت ناجوانمردانه و عمدی مورد هدف قرار گرفتند و اگرچه آنها را از دست دادیم، اما به اسطورۀ قهرمانی مردم ایران تبدیل شدند.
🔹
امیدوارم بتوانیم این نمایشگاه را کشور به کشور ببریم و نشان دهیم، البته اگر طاقت دیدنش را داشته باشند و اجازه‌اش را بدهند؛ البته از آنها بعید نیست که اجازه ندهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/458647" target="_blank">📅 18:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql7_JtVFm5fmLOw-7wKFJQQg0NZADcFvzBAfgwLpG5S8M77FWZA3HW7_5U2YUmUkaDEZiw2iJLNrXCpbVfuSSp9jVSciL0jCS9gOzSkmoAFAAblUhvaGaN5xX_uSHZBjbkFxHdCotiNTR8glx2JrWYu_O4Qfzh94eK1pq3F-ZN-XFP7-a9gNRi86oQFfOENxaTBENxKy75PjcuDv3cxkq1fs3_3LRuX26tBR1v72XIiw7I6V23PbxSUFqXQolx9uY0TWEpAEudt9yFkxHAKfAPmcOxVPZND5qFVwkaCR1F8FVXFq_AdXyGZeMSkXed1lH9xa11QAFyKWk2bC3PYvEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۷ محور جنگ شناختی دشمن علیه ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/458646" target="_blank">📅 17:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUVvKLIfGmB0eNhQ8BaxTh8YgxluE6Pg4cFzHiX7PWwBh-56YrYZnGKI8n6OsVdEH7mJE9xcFE2afMJ537k2ZszADb9FAJKLpgKk1I2IfXap8TgFTEAsr8X3RywGVYruTwEGy5u76SZXmoNt28EWoGhwMojZS977BPI0eiVyRrQXb1vkvR5ybL48G3lCwatP51e1bSAXYpVcXqJHr6W0KlnVBZWRqZCLZr-oh80RFU6nuIkECzUUmQWtTDqUSS3KscAGMz0SsKSpYinKrA18E0gdKBs0uY2tipkNXnM_d-Way9Mmmy3p5Qz4KRPfu3lsXE-GfyA0pfCi6sPgO0p0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدۀ سرخرمن وزیر انرژی آمریکا به ایران
🔹
درحالی وزیر انرژی آمریکا از پیشنهاد همکاری هسته‌ای به ایران همانند عربستان صحبت می‌کند که نه‌تنها ترامپ برای ریاض پیش‌شرط گذاشته بلکه این همکاری را مشروط به سازگاری با منافع کشورش کرده است.
🔹
کریس رایت می‌گوید به ایرانی‌ها گفتیم که برای توسعه برق هسته‌ای با شما همکاری می‌کنیم و اورانیوم غنی‌سازی شده به شما می‌دهیم «همان‌طور که اکنون با عربستان همکاری می‌کنیم».
🔹
این درحالی است که ترامپ اوایل مرداد گفت که پیش‌شرط توافق هسته‌ای با ریاض پیوستن این کشور به پیمان ابراهیم و عادی‌سازی روابط با اسرائیل است.
🔹
رایت در همین سخنرانی می‌گوید هیچ دلیلی وجود ندارد که در کوتاه‌مدت فناوری غنی‌سازی را در اختیار عربستان قرار دهیم؛ دست‌کم سال‌ها بعد در موردش صحبت می‌کنیم و تنها درصورتی‌که از نظر تجاری منطقی باشد و «با چارچوب امنیت ملی ما سازگار باشد» این اتفاق رخ خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/458644" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f224bf81.mp4?token=BXqq5GFrr_nLP7r-LDRD12qK8w36Obvuut69wJSWCfEobXb4KhhWxw8Lf4ID86tz6hXOChp6yhuGS0EixIX2iubAleZvv4jjLPy7PnC2oxP4aoDoIKauzHX9PZI367QK683KCLOBhZqj1B_L9s9W1NC05b5h11xUo4oEqoyJEdY-jcSRyaLIuWs3mcvO9oJfmgkTl55bIWiC2bDBTWDDFLJ2CwPhqKrCq-kqr2cUMG_PcSGQgMdYMnI2RN2DZli2wXdrL7ECUWcLelVSIyrCl11U_jW5EjmUL2oXsRN8vgcrj6Vm6DUnO3rLLeur7NOxqVCHtv6VdDaWBhJVKa-xVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f224bf81.mp4?token=BXqq5GFrr_nLP7r-LDRD12qK8w36Obvuut69wJSWCfEobXb4KhhWxw8Lf4ID86tz6hXOChp6yhuGS0EixIX2iubAleZvv4jjLPy7PnC2oxP4aoDoIKauzHX9PZI367QK683KCLOBhZqj1B_L9s9W1NC05b5h11xUo4oEqoyJEdY-jcSRyaLIuWs3mcvO9oJfmgkTl55bIWiC2bDBTWDDFLJ2CwPhqKrCq-kqr2cUMG_PcSGQgMdYMnI2RN2DZli2wXdrL7ECUWcLelVSIyrCl11U_jW5EjmUL2oXsRN8vgcrj6Vm6DUnO3rLLeur7NOxqVCHtv6VdDaWBhJVKa-xVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمیتۀ انضباطی به استقلال و تراکتور هشدار داد
🔹
استقلال، تراکتور و گل‌گهر به‌دلیل هم‌زمانی بازی‌های آسیایی با نخستین دیدار تیم امید در بازی‌های آسیایی ناگویا اعلام کرده‌اند بازیکنان خود را در اختیار تیم امید نمی‌گذارند.
🔸
کمیتۀ انضباطی فدراسیون فوتبال این اقدام…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/458643" target="_blank">📅 17:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملۀ رژیم صهیونیستی به یک خودرو در شمال کرانه باختری
🔹
شبکه ۱۲ عبری گزارش داد که یک خودرو حامل سه سرنشین هدف حمله پهپادی در استان جنین واقع در شمال کرانه باختری قرار گرفته است.
🔹
به ادعای این شبکه یکی از سرنشینان، فرمانده نظامی یکی از گروه‌های مقاومت در کرانه باختری است.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/458642" target="_blank">📅 17:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=lIdFk4FxcQt-GpWj_enBOeFxFCjJ-Vc3riTmtKlczkY0nyEXsxJ14CaVzsUOJDU-0zc79zvHWW8dJwOlY5v-DsRcdiae6h3Y0MlPVMKIXl88z5i5qZYF5JTNPlZGAOLy3cKOsj0dr7z7J6cBgiRS0nh6zQt1CHlz1A3x6HGu6cM5hGrruOHE2gQL2HmKM0xENBAfIDXVoGqjtJkB5SzuxfxplvjII63G2iT1zQXkv6EFq2wvxyR2GQQEYPJsPZh5n1Csr7B89V4CZYhETWFtDNPXQk-GABH5H08ofDriPIvO2FwKhXYpY6XCUuayAd8T8IRlTDp00k97ojgdsPJ8LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=lIdFk4FxcQt-GpWj_enBOeFxFCjJ-Vc3riTmtKlczkY0nyEXsxJ14CaVzsUOJDU-0zc79zvHWW8dJwOlY5v-DsRcdiae6h3Y0MlPVMKIXl88z5i5qZYF5JTNPlZGAOLy3cKOsj0dr7z7J6cBgiRS0nh6zQt1CHlz1A3x6HGu6cM5hGrruOHE2gQL2HmKM0xENBAfIDXVoGqjtJkB5SzuxfxplvjII63G2iT1zQXkv6EFq2wvxyR2GQQEYPJsPZh5n1Csr7B89V4CZYhETWFtDNPXQk-GABH5H08ofDriPIvO2FwKhXYpY6XCUuayAd8T8IRlTDp00k97ojgdsPJ8LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی، کارشناس مسائل منطقه: افرادی که صحبت از صلح شرافتمندانه می‌کنند بدانند که در شرایط کنونی صلح به معنای تسلیم است
🔹
هدف آمریکا تسلیم جمهوری اسلامی ایران است و هم‌زمان با پیشنهاد مذاکره، تهدیدات و فشارهای خود را بالا می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/458641" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458640">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTFLnPiTmRH6rNvzAaq2OwJHXJ-RHZ7Ps9NdT1fW15dMLgk6ZVMmbvfd8JBiy5ZSx-E8iTUmRoYXiEsf6-M2friNBvBhN6mWvpOOixi2yii3xPSPjl3PTjyWVtcSCJ2qwzduZb9GMh_7C9RUZYMFgAbexu2v-f3rrO2IsOsnH1gk8qqgHCriJ-v_SHb_ty-nJ5RJow82HcFaISkl1j9e_jSIHqcnL1g_FIkdVUO_yD_69ltz-xPb5k7iJx0a0vwGRvfnZgJRG01yYdf_cCeWG2f0nMmmUxJJYYXlQ4KuCx0JnH8a6J7a-CL52G0URwG5vERWZ0YdzuVN7LYgTuCAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ سبز دولت به ارزانی سیب زمینی
🔹
معاون توسعه بازرگانی وزارت جهاد اعلام کرد: صادرات سیب‌زمینی تا پایان سال ممنوع است.
🔹
قیمت سیب زمینی به کیلویی ۱۰۰ هزار تومان رسیده بود یعنی نسبت به قیمت یک‌ماه اخیر ۳ برابر شده بود، فاصلهٔ بین تولید مناطق گرم و سرد عاملی برای رشد قیمت شد.
🔹
دستورالعمل صادرات و واردات به عنوان اهرمی برای کنترل عرضه و تقاضا و قیمت در دست دولت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/458640" target="_blank">📅 16:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts8tGEVMxOZ9jScG4QH9SOYEUsZH-T_hEIKCi-ORTpE2OreRiOlkfU-wb-6cqDEJ7wSqhf_GcfjuU7j9tjp-dHPS3SJJgA_c9AJEXnuDvON78KOiR0jSKVfd3CtX2FJIgc7xaUi30BCF2dYN1d1z9apVNCwYxLmJ7kzR10q_fsUAVsEu2ZDZJLpzEiz9eY_llYpZ9C3bcYXA-nX0RWC3l2EsacnUtUwBkLIz_sjGqOvag4hfKbeZjpyYEqIj9qd7uUsexRxLNOcVprTQObpn0TTXqP-ic1POR9Pyp0T47nIoauRM6JE5XDv1vNoynU7svEigPZWRzvns7DlhtKpWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریورماه است و هنوز خبری از واکسن آنفلوآنزا نیست
🔹
از آنجا که زمان طلایی برای تزریق و اثربخشی این واکسن از اواسط شهریورماه تا نیمه اول مهرماه است، داروخانه‌ها از یکی دو ماه قبل اقدام به ثبت سفارش و خرید این واکسن می‌کنند؛ اما امسال با گذشت ۶ روز از شهریور، هنوز خبری از توزیع واکسن نیست.
🔹
سخنگوی انجمن داروسازان، درخصوص وضعیت تأمین واکسن آنفلوآنزا در سال 1405 گفت: سالانه به‌طور متوسط حدود ۳ میلیون دوز واکسن آنفلوآنزا وارد کشور می‌شود اما متأسفانه امسال هنوز اطلاعات دقیقی از میزان واردات، منشأ تأمین و زمان دقیق توزیع در اختیار نیست.
🔹
او در ادامه بیان کرد: هفته گذشته واردکنندگان وعده توزیع واکسن در نیمه نخست شهریور را داده بودند، اما تا این لحظه واکسن وارد شبکه پخش نشده و متأسفانه شفافیت لازم درباره میزان واردات و محل تأمین واکسن‌ها وجود ندارد.
🔹
همچنین سخنگوی انجمن داروسازان با تأکید بر این‌که اکنون در زمان طلایی واکسیناسیون قرار داریم، گفت: تزریق واکسن باید در همین بازه زمانی انجام شود و تأخیر در آن، اثربخشی پیشگیرانه را کاهش می‌دهد.
🔹
در این‌میان، سازمان غذا و دارو باید پاسخگوی وضعیت موجود باشد؛ زیرا سلامت گروه‌های پرخطر شامل سالمندان، زنان باردار و بیماران صعب‌العلاج به تأمین به‌موقع این واکسن‌ها وابسته است و نباید اجازه داد این فرصت حیاتی از دست برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458639" target="_blank">📅 16:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458638">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9HIIDu0JSG6KscS8jIet8LDP84ZY90YHO3ScMULHeanLKVivWIg-_ahgaDO6It-ukXnvtJTrlumVE4jHBfqPkvCXk1HuA6BK1z9BUQRUhi0-R5U9zU-2XGt6XiINYjN1CnRULNLD0YcsUr5r4VnfCo_YsOFQzzADRQVQh89KwkAp9lVxk9s9XJ8im-O1vHYvc6w0enQpUsAISpOrSbZldrMW89BXBZ4Mt9AxEEYjlQ5gY7e_d76kBqVIUH0b2e1PMBb3xrPXJPOyYvYQtVDamF-0cvv5pXHpgPlShuest2FmDCh-tV6quddqw54LL_gf_4r5UzrCTy9wZ53BBsGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خوش اخلاقی با مردم
🔸
حضرت آیت‌الله العظمی شهید خامنه‌ای: این‌که پیامبر هیبت الهی و طبیعی داشت و در حضور او مردم دست و پای خودشان را گم میکردند، اما او با مردم ملاطفت و خوش‌اخلاقی میکرد. وقتی در جمعی نشسته بود، شناخته نمیشد که او پیامبر و فرمانده و بزرگ این جمعیت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/458638" target="_blank">📅 16:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458637">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8xhZfiodJx7_OWdSSOeZcXCUVbF_6et3fIxW5pWOcOKdoWY52rJdSfpf-yCc15q9AfjUmv3umnqKnKEdaISlNWOh5RPDk6MrU0t8XQHBwuBrSYncs0b_aj9-IRAZPcunNvXYlUlPOh1n5nCxowU60NzAdW0MtROUxGjVMnteHGDjRHNq9d45YXKcF61FRBF62JPNbZyafTBhy5qwO90HkHDh7Xbu7EPvkNEpoz0GOQL0DSA-FbPnSEnBSXEuu99mhIwPedr6V0shA5KL3nuAU0SvLV3ovDrPDPEy_Ellx-MFFxPLWrbqz7s1R_DZ7NH1jZdTHUk3oRM6dfxKoB1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار جدید رژیم صهیونیستی در حومهٔ «مرکبا» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/458637" target="_blank">📅 16:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajM6U5q9dgn58Tp5za0ruzIpwz3rVOlLXNipf2hv5k9JL0m0hX4Cs5UTRHNysbozHYAOMbbi-VIgaljtAnPNm6_s38Tpd1ptrqCYCCHZSsIJe9Zk-uDzr-YIIB860HEGVEEPOt5ls-UQfkDCZu7-389RsZ46-2At1L6Nbj9acV5e5c1KurIDlLhdh76rxWDv-PQAzwXCS4ZlctIdFIDA9vpNfTFrYTnLnF933HzVOox63ETkrEwL5GxeERP6uBvMRWZTh3b9aAlGsZ1XgrdqSzKnl0QAucR1sfLO9ZBved8DfMSlIt0QFSwNecF8DEKMUq-vr0A2emsbxzRswQX2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ چین در خط‌تولید موشک‌های پاتریوت آمریکا
🔹
وابستگی آمریکا به مواد معدنی به چین آن‌قدر عمیق است که اگر پکن بخواهد بازی دربیاورد، «حتی خطوط تولید موشک‌های پاتریوت هم نمی‌توانند تامین تنگستن مورد نیازشان را تضمین کنند.»؛ این را یک مدیر سرمایه‌گذاری در بخش صندوق پوشش ریسک کالاهای فیزیکی با اشاره نمودار اس‌اندپی گلوبال می‌گوید.
🔹
نموداری که نشان می‌دهد که چین سهم بالایی در تولید مواد معدنی خاکی در جهان دارد.
🔹
اوایل مرداد ماه وزارت بازرگانی چین ۱۴ نهاد اروپایی را در فهرست کنترل صادرات خود قرار داد که یکی از آن‌ها غول دفاعی آلمان «رین متال ای‌جی» بود و اعلام کرد که صادرکنندگان چینی حق ندارند اقلام دوکاربردی مانند تنگستن، گالیوم، ژرمانیوم و مولیبدن به این نهادها بفروشند.
🔹
پکن ۱۷ مهر سال گذشته پس از اعمال تعرفهٔ ۱۰۰ درصدی ترامپ بر کالاهای وارداتی از این‌کشور، محدودیت‌های صادرات عناصر خاکی کمیاب را بیشتر کرد.
🔹
حالا جدیدترین آمار فاکس‌نیوز می‌گوید که دو سوم موشک‌های پاتریوت آمریکا در جنگ با ایران تمام شده و تنها ۸۰۰ موشک باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/458636" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIzPS-DApLfIEsjjbsibAknCs26IcCH4pFoHzfdaNbwrV-XYwLQB6LfpayjKTGyTioGhxt1AFjom-vHwQDk52ipg4VVOrsGHP5EXV7INiOk0ZC2eLmb4fGxkGQxzM0fJyN1xIwPwMspkmsYesnGpPRNbLAK5o7O_n-gxDHBVomNjzR_vlEJxxfpzlROWp_mGQogBpyob2IFXw1_YRX4yiCIZ2BKWkecLdDUANnjZeJU-fsDHyvVnHz8yaZWqcZ10etMm_uffUBSF3xXTkgebhS0f30T4SVMHgRDlY_747AVJ0qIyFsJIoUaRnWIGg0xsTa-nS-wWl0-6IJOkUq_KbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: آمریکا به همان اندازه که دشمن شیعه هست دشمن اهل تسنن نیز هست
🔹
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی: اگر امروز همهٔ امت اسلام در کنار هم بودند رژیم پلید صهیونی به همین راحتی ۶۰ هزار نفر از برادران و خواهران بی‌گناه اهل سنت را در غزه به شهادت نمی رساند.
🔹
وحدت از عمق اعتقادات مکتب نبوی برخاسته و همه مسلمانان باید برای نجات مکتب اسلام به این موضوع اهمیت دهند چراکه امری ضروری، شرعی، سیاسی و اجتماعی است.
🔹
آمریکا به همان اندازه که دشمن شیعه هست، دشمن اهل تسنن نیز هست؛ چراکه اعمال آن‌ها در افغانستان، غزه، لبنان و ایران و جنایت‌هایشان نشانگر این موضوع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/458635" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
