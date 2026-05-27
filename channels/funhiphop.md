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
<img src="https://cdn4.telesco.pe/file/Dkmr1q0qIDesOoir0qVyT3LhdqKNetpIr3uPxft_lPMqsw83MPrKlMuA_7FYtWoIsWCm69LuNjIjeMdWa2qQMQ_jDg1iWkJxkM74ZyhT_TOXdXWflbDsExTNrdBnmC_WfVhSi32zzTNK4Xu0zfC_gVwn8RoaGNxuTwuQ8IhgxSLYWry4ceO2v8hNZ7uuKszCecpQyOlvQEnIR2rWiNg5lzbpjHobunc4dAivlZD4x9TlmaB-aO1Kn2GgKcKjxqS0EixK6qcD3r5kZEXx80w_aWI1sG74IvUXzqKZbrzxI9R_AnGGP1r0ctYfZg9x1sYk0m1KoF6h2jSsVX0nyHFCYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 181K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اکبرزاده: دیگه فکر نکنم دشمن جرات داشته باشه حمله کنه.
پ.ن: یادش بخیر دو سال پیش جلیلی و ثابتی هم میگفتن اگه اورانیوم ۶۰درصدو بدیم به آمریکا بهمون حمله میکنه، چون الان اورانیوما بازدارندس جرات نمیکنن حمله کنن، اونا هم عمه های من بودن تو ۹ ماه دو بار به ایران حمله کردن و تو عمق ایران همه رو ترور کردن کسی کیرشونم نتونست بخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/funhiphop/76097" target="_blank">📅 17:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال 12 اسرائیل:
انتظار می‌رود هواپیماهای نظامی آمریکایی در صورت امضای توافق با ایران، ظرف ۷۲ ساعت  اسرائیل را ترک کنند و به پایگاه‌های اروپایی منتقل شوند.
هواپیماهای سوخت‌رسان نیروی هوایی آمریکا در صورت از سرگیری درگیری با ایران به فرودگاه بن گوریون بازخواهند گشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/76095" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا به تیم ملی جمهوری اسلامی اعلام شده که اجازه اقامت تو آمریکا رو نداره و بعد هر بازی باید بره مکزیک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/76094" target="_blank">📅 17:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZByOJCruOb72Wod-Uj75gJCdY9QQSQ_bldajg5Mh3tdN9JaRVMfRQyzzyu7heKyf5uwX3D2-KUmZ58YtoKuk0CB66iNQLIQQabV7bxhKaiPPnwEQmQ6-qFXbhhU3CDOTTgaRoPPfv9td_2tasvQUlpo-o58XRGKWVw5_P7XFQ45MDDzsxmjUe6XJXN0PMJ29MZgvhCWI766NyHhHFMdKb8sBI-n6Z9ZGLy869pX9N86N9cioNBP2-CTxqcjqsXRpVaH2tUwk-4FYmkRGgmAW0x1RQeDHS1_Q_juZuJjgWsfgw5-HzBVyXX_Hj9US0LNjCISYwfHGxD3R_rbZD1a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/76089" target="_blank">📅 16:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯ ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/funhiphop/76085" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯
ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/76084" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/76082" target="_blank">📅 16:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza</strong></div>
<div class="tg-text">خداروشکر
همین کم مونده بود اینو به عنوان چهره مخالف جمهوری اسلامی بکنن تو پاچمون</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/76081" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انگار خایمالیا سردار جواب داده و میخوان برش گردونن تیم ملی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/76080" target="_blank">📅 16:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایران تو صدا و سیما هنوز با توافق مخالفه، تو تنگه هرمز چپو راست داره کشتی رد میشه</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76079" target="_blank">📅 16:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cznG5jBTNL4SzywcbITq9k1UEr_AL1oZYD_PBrUVlc71r4-NNacL9S4Uo-WMSviRWt8N3CMkYSX3chYPIUvFBYd5jFhcKMQaVwY5lskqRjHZ7T4Numm-TObf1oywaoKSCa-41yKCqSrF2Tnl8txaTJN5IzxMiPGe4j-6oOiVzzWRinlyleVCfImuiAa1l56Esoq0I-JKjlXl95VivARmI9W8XseazNPFC52fS-maJPIBRINTci4BffrOTH_dElWW4hxoaRl0Gq6jQPVtVZkY5WkVF0ZcHXpml7uLiW9BMaZkcrXiGDRBnQA9P1WDEy5VYkQ_q_DIEJxcoM61F7YR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به پیش‌نویس تفاهم غیررسمی تهران و واشنگتن ریکشن نشون داده.
@funhiphop</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76078" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رسایی: قلبم به درد آمد وقتی دیدم پزشکیان اینترنت بین الملل را غیرقانونی وصل کرده است
پ.ن: کیرم تو قلبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76077" target="_blank">📅 15:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش دفاعی اسرائیل حملات خودشو افزایش داده و کاری که چند سال پیش با کرانه باختری و نوار غزه کرد و داره سر لبنان و حزب الله میاره.
نمیخوام کل حملات و پوشش بدم ولی داره تو لبنان پیشروی میکنه و برای چند تا از شهر های لبنان هم دستور تخلیه فوری برای تخریب ارسال کرده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76076" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromꜰᴀʀᴀᴢ</strong></div>
<div class="tg-text">اینا اینترنت رو وصل کردن تا حواس ما رو از عروسی دختر شمخانی پرت کنن</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76075" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آخرشم پزشکیان میوفته تو استخر نیم متری و غرق میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76074" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjP1wydOuujVMh-k4VRlmKLDkReRjoJ3k1jFDJRe_X2RQ__EpIviYtQ5kaPN12RtHBEswm2YlXvwhQdG7KapQKpffLFBqNn2XWVUlTzlLugipTyudugQ8YHDwLZ9fy4Ny7QCaoNYooNj29bZxI2NyltZfSBjESjE74T9GfpZuplIjb6_EWMWh7d7QYA2JuwOr92x-y5osyN3d2RhFxfA3qyZvuU2FX02uKi7Zo0eXAFJ3gJSjGQFIk8z9ZWbnhhWGvGlk_U2fkSE1CU1pqH9d2zJ59Dk7ZFwOYgTM4p7pUAv3dvBxRinT4_esZ3bhwlFKoBrgnMpiP_Q69z__ldkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJmj0TZx6Y9Az4wQQyOosOCo54psJirkmxVSvG_dXaMgL_gRLiVZMR4BEkfAWzY2HRUJJlNde-LnECWvu5UE1lIMd9Ar-wlg5ESiE--LbPNPEgCeFl9Vdw1NBQMKWYkuHauEX21WCtsF5kw6BJG39_yM8R2P1dl_1YDDTal99DvuL1mTJdJNmE23gQYE97indk_s5Mx7x7VYMGUgq2UVrSSLXh-1gMat_hAx934fIif0wv4rOT5rZg7K1iPRk2lZUQaUwZ08UnuU8PeDM6aEuiA7RP6vSa_LM0wQ7jfxgfMw8tXoW6JpwkaqbqqyyXRMPfVUtP-eY_OYI5tmDYh_Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76072" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انقد پیام ندید، گیگی ۵ هزار تومن وی پی ان نخریدم پیام بخونم باز، فقط ویدیو های بالای ۲۰۰ مگ
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76071" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رافینیا ده برزیلو داد نیمار</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76070" target="_blank">📅 14:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فوری: طبق گزارش Jerusalem Post، ارتش اسرائیل و سنتکام در حالت آماده باش قرار دارند. به این خاطر که احتمال شکست مذاکرات هسته ای/آتش بس با ایران و اقدام نظامی توسط ترامپ است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76069" target="_blank">📅 13:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی ایران: بعد از اینکه دشمن توی جنگ نظامی موفق نشده، حالا بیشتر رفته سمت جنگ رسانه‌ای و روانی. به گفته این وزارتخانه:
الان تمرکز دشمن روی ایناست.
* فشار اقتصادی روی مردم
* ایجاد اختلاف قومی و مذهبی
* تحریک اعتراضات و ناآرامی
* ترور و خرابکاری
* قاچاق سلاح و استفاده از استارلینک
* حملات سایبری
* فعالیت رسانه‌ای علیه کشور
همچنین هشدار داده هر کسی در جاسوسی، همکاری با رسانه‌های دشمن، یا اقدامات تجزیه‌طلبانه نقش داشته باشه، با برخورد قانونی شدید روبه‌رو میشه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76068" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=farsbsZFzHSqJsLkukLg4TNICEN6cdK07tBpTeC8ylNHYo1JUHXOfvHpbiEjl3To92ukm3UteWzu5ftvEWG5Fwz3ICMyqqC3VjL1alpuKUI2BnXd03cmP_j0dkbTBLIFSDO81T1Cwc137C7kMobfPBvisrmLEfHw8BaiERMBPqnq2UKL2rNqbdOiYLRXON3N6EV4EsYEko9X47XzMkB_DT85a_xHGEtFyBq2-M1VEK-rrpqDzynohiohfVe7yTjPZryaDGXLkB-IcsD4k6ANvQ8x2lntvCoFpMoEaNnRZSCmKLn7g2guKJP9z1Ek4ICD3h1KTMyWJTbuXxPw4jGZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=farsbsZFzHSqJsLkukLg4TNICEN6cdK07tBpTeC8ylNHYo1JUHXOfvHpbiEjl3To92ukm3UteWzu5ftvEWG5Fwz3ICMyqqC3VjL1alpuKUI2BnXd03cmP_j0dkbTBLIFSDO81T1Cwc137C7kMobfPBvisrmLEfHw8BaiERMBPqnq2UKL2rNqbdOiYLRXON3N6EV4EsYEko9X47XzMkB_DT85a_xHGEtFyBq2-M1VEK-rrpqDzynohiohfVe7yTjPZryaDGXLkB-IcsD4k6ANvQ8x2lntvCoFpMoEaNnRZSCmKLn7g2guKJP9z1Ek4ICD3h1KTMyWJTbuXxPw4jGZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76067" target="_blank">📅 13:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آقای پزشکیان نمیشه اینترنت رپرا رو قطع کنی؟ تا عمر دارم مدیونت میشم بخدا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76066" target="_blank">📅 13:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76064" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76063" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV1hFrXkkgTfI6z6uT94FdyiJkZkVyf0UToS85Nnx41EDTVbDh2AuK7syn3MR4rUti62Gjdx19xEN3IO95H4hv-Nres5863ukcadZnXsyXmb7XjQD8KstP3bGu1SbexvCF9tJWRWY38ZaUeEUmpxv5ORhPMmkDd3xR5ZhlEycIwJ0FUMqcEyAsr4sLdPN69gdlfBPrPuqmgtVxXZkLBL7MhlJF-so_Oi1XKPumN4710gjrTeTXbRHHrhclgsWrJjQz15y4ZppsN6GYsnqCcywur63vBNORAxS_mS06CyX4u3x4svHkvnpG67-QEj56euA5MO9_VIm1EDK39BPD6zWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادمه ی سریتون کصشر می‌گفتید که رهبر سالم نیست
چیشد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76062" target="_blank">📅 13:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کاپ رنک یک وسط بازی هم تعلق میگیره به قیاسی
کار بلد بود ناموسا ی جاهایی داشت باورم میشد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76061" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خداحافظ وحید جان</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76060" target="_blank">📅 12:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زنگ بزنید منوتو به امید بگید کانفیگ فروشم
براتون اشک بریزه یکم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76059" target="_blank">📅 12:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گذر پوست به دباغ خونه میوفته
Make Vpn Sellers Great Again
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76058" target="_blank">📅 12:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">یه ترا کانفیگ میخوام بودجم هم حداکثر سی هزار تومنه
زیاد نیاید پی وی حوصله ندارم باهاتون سر کله بزنم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76056" target="_blank">📅 12:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کریر کانفیگ فروشا با گیگی ۱.۵ میلیون شروع شد و با گیگی ۵۰ هزار تموم شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76055" target="_blank">📅 12:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وال استریت ژورنال:
حکومت ایران قصد داره قبل از اینکه بحران اقتصادی دوباره منجر به اعتراضات خیابونی بشه، با یه توافق اقتصادی با آمریکا جلوی این اتفاق رو بگیره.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76054" target="_blank">📅 12:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینترنت هنوز به وضعیت کامل استیبل نرسیده و خیلی اختلال داره.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76053" target="_blank">📅 11:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه:
با اینکه احتمال شروع مجدد جنگ خیلی پایینه ولی ما به هر حال دستمون رو ماشه‌ست و آماده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76052" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctE9VIxWVTz8t0c-UPUo7Gmg0C3cAW7jETdqjv8WShH3a1Qbvppu4HGzETr948P6MOSoSMg8CMwwpxPlKQ7kAGsrEtluymhObs3LJU_wQnkVPGdurCjHA-qLokl4yCWe4F2f3CRWQKySwukRVxNUPhLFpGIedaz6Nbj8p38z-a2cQhFhkRmdFVJ3WMnHzJIsN4Qgykej4dCn9zgML5hb1w167cXAUkStBzCNf11ReyvMNc3H4MZV19C_QNK2fRKoMGXVkJAQhyQ_HKShOHqC3_-WbXXXVnzVW6fAp3zyH7ALJj6lCEFypImc20ZWzBM08Et-pYccAExjH3OBYsVcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرام خانوم برگشتتون به فضای مجازی رو خیر مقدم گفت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76051" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76050" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76050" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76049">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NClCixmcEGp5dccoKIX4CaCOA3JK6GIB6_1fCEtZJ5Q12fI2MmfNkPwTJZN_afCwZcQjso5hyaPTEWitt-Woz1YA6DdcNtiRbFDIgTX-THbRG26zMS0xT9J3GWBN0pmG3pAYX2lxZ4N2pwvCUL3v6J1_5WlKh6VuyL--aJN_mPpEbaYld5CD-rf51sWW9xnz-4xC21lDh0eJDyJ5qcezvzcY_90qLVRn2V6OqQfcC6dxZlfFbIb20Jw5_sZMtwIsbLnnZiohURIkzcncomHLbUgqdMW4eGvfpQnARfXU8JBSbUWslcTO-GH_1MSX2LrkLyl8zWs8Zf_o1mkCDYP3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r6
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76049" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وال‌استریت ژورنال: ایران در مذاکرات با آمریکا، خواهان آزادسازی کنترل بخشی از ۱۰۰ میلیارد دلار دارایی‌های مسدودشده و دسترسی به بازار نفت جهانی است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76047" target="_blank">📅 09:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=gqddhiDVaTfmy7KMMEk-rVyXCHTASj8_WXorlXLBFF8wwiRiu51mSrFK8v_xIfag8Lo8g1YQ7pIF_gw7WofTHnoh4RidkoygtVUa12noUPLvtViJj6L5Y8K6LDXuT-tPVti-B0dObWUkQCLPDnUjz5SsJBElmZJ3tIbnkPLJ3E-kmz2Dgs7j3Q_OCYF4d-VTJvO7KZH8BUPtoeyt-WXxwMTPQ8v0kV6kq9m_OcLRdfZnKxh-TOLuJ8pLW1VQuTHdT0re2rV0a2FvddNnxiwNds7rI6HtwH2Lf6Z-RPqIVPW6RPaanZpVr8AQtSy7nDR0wQ7YNGqiVHu8eyU6XaBZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=gqddhiDVaTfmy7KMMEk-rVyXCHTASj8_WXorlXLBFF8wwiRiu51mSrFK8v_xIfag8Lo8g1YQ7pIF_gw7WofTHnoh4RidkoygtVUa12noUPLvtViJj6L5Y8K6LDXuT-tPVti-B0dObWUkQCLPDnUjz5SsJBElmZJ3tIbnkPLJ3E-kmz2Dgs7j3Q_OCYF4d-VTJvO7KZH8BUPtoeyt-WXxwMTPQ8v0kV6kq9m_OcLRdfZnKxh-TOLuJ8pLW1VQuTHdT0re2rV0a2FvddNnxiwNds7rI6HtwH2Lf6Z-RPqIVPW6RPaanZpVr8AQtSy7nDR0wQ7YNGqiVHu8eyU6XaBZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شببخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76046" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ممنون از آرتیستا و سلبریتی های اونور آب که در تمام این مدت قطعی حداقل با بخشی از پول هایی که از همین مردم به دست اوردن یه پنل خریدن و کانفیگ رایگان دادن به ملت و نزاشتن این حکومت خونخوارِ دیکتاتور اینترنتو رو همه ی مردم ببنده، کمال تشکر رو دارم ازتون عالی بودید، دمتون گرم و کصمادرتون اگه فردا روزی باز از همین مردم طلبکار شید
ما که کیر در بساط نداشتیم ۵ گیگ کانفیگ دستمون میومد سه چهار گیگشو حداقل به چهارتا دورو بریا از همین ممبرا میرسوندیم کارشون لنگ نمونه، عرضه همین یه کارم نداشتید جنگجو های وطن، بشینید اونور همونجوری بزنید تو سر کله هم تا پیر شید</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76044" target="_blank">📅 03:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تا کانفیگا مفته بخرید که خیر نیست
صداوسیما: بازکردن اینترنت تو این شرایط خیلی کار خطرناک و غیرقانونی بوده و سریع باید راجبش یه کاری انجام بدیم. حرف پزشکیان مهم نیست و بزودی اینترنت قطع میشه چون حرف دیوان عالی انجام نشده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76043" target="_blank">📅 02:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رپرای محترم اگه میخواید کار بدید الان گلدن تایم کره گیریه، از من گفتن بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76042" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=Ugtw2aE_0VL4mIeIDyweS0-VKPlSS5xc_Fy-0zAoxbjee1I9vFW-bOgIJ2NAnBopt1lPwdgtYYRu024ZjQXY0q_KtEx1J0e6icmOPlQcd_IQivPQjoPGJcha-BgccBHEk7h3EKKNEo77O9QxEhL2SXYKba0ynJwHFjXRFPh1oTKTwSnS4vLmXmDv9BFNzaoMIP68oTJS0zKwmG4scnGeiBVnGmH6yF3feHzd8Eb5tZNZCRx3iudIf1rPWHfT3q7rswyMtRcdKFjffbYTe0QaJkNFBELJcR48LsUG8LV45TfA7VtaSvnkRJ--moygm1zwD_CUcd1p_fduGYOgh0OYsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=Ugtw2aE_0VL4mIeIDyweS0-VKPlSS5xc_Fy-0zAoxbjee1I9vFW-bOgIJ2NAnBopt1lPwdgtYYRu024ZjQXY0q_KtEx1J0e6icmOPlQcd_IQivPQjoPGJcha-BgccBHEk7h3EKKNEo77O9QxEhL2SXYKba0ynJwHFjXRFPh1oTKTwSnS4vLmXmDv9BFNzaoMIP68oTJS0zKwmG4scnGeiBVnGmH6yF3feHzd8Eb5tZNZCRx3iudIf1rPWHfT3q7rswyMtRcdKFjffbYTe0QaJkNFBELJcR48LsUG8LV45TfA7VtaSvnkRJ--moygm1zwD_CUcd1p_fduGYOgh0OYsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76041" target="_blank">📅 02:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@Ali_nor30
یکی از هزاران نفری که هرچقد هم منتظر بمونیم قرار نیست آن بشه، اونارو فراموش نکنید.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76039" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تو جواب سوال چرا نت پرو میخری؟ طرف میگفت چرا میری فیلترشکن گرون میخری؟ یه ناموسی هم میکشید بعد بحث تموم میشد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76038" target="_blank">📅 01:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBLpbLKqQD7Sq90jrBNATvySmBBzhbS-zmZwZA5nHZ5SeP3_vjzzGDkIB3BQbNqOnzQEX6YMjWVYkGgnyiy5xZD2_znWVeJLHHrcfkikJlH1hZ7jjyH5VaPPwCvDkrHtUT9Ma6iCAFEIMW1pamaUZf8iyiMH24mYvNRXn_z_AccZKl2BLC2e4Dik41GCdm8w-LNQTOsAdYi9_WA1jg23_txbZ2Ns6TUT2sJe0bPwe7JwfDI7O2OW-jDEZ7s7v-kFM1Z-14ivjJ8ezhE6qLdy26PLMJEOib5K977u1vVRR2qBL77DZ0hQiEWld7gqteLeYXhcxC5dEiC0VxAaS5H3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop | MEHI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76037" target="_blank">📅 01:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP_FaPjLRtRKGzntqTtOT-Y1PdLx5oQDmBVkavF50GvfB7pITlR978XBwSw5HdaoC_paf0kuWYlIlpfcUW3HluPgQrN1QzKjQHQhgjwvC-PxCNY3Cc8W8qGu8KNBvbIdM-AUg_FCLgupHgqhxRiZaFR6qN6p02Kly7nezqdSrdQo42zwjj4VExv0ldYDJkEFY2B5odQ6gAWKt_PO6nWAmETGRJ8iQedu6_-6zRiAs1cmFYIERRRyoCgruJMVtW6WK4VSRvm4o1fm_dBT4NqfN3GPEK40CyB3HcwATfHDihTrTtwDaz2rUb-Y-MWoY-GtjkzQLiRI0Oe8ShJEJkUzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop
| MEHI</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76036" target="_blank">📅 01:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پروکسی های جدید مخصوص دانلود سوپر از تلگرام:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@Funhiphop
| Siavash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76035" target="_blank">📅 01:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyD0cMe7sNvWw0sS7zdNMGX3xD9vF1iz8CF0i9hHI2G37cJqDe_dwcwa8280RlsheZ9rASYNpwvSOJMrNYzCbcNVGgW5QrsGioIAV5rmLOaHE6H1VhfklXPqARM-79pHaTjU-zpFdsGrfuUTgSorcjMTH_cUQeAkTVoVbRtwEKLQYM9-ZXDZ8-uciu07B8mfEGUJx67VV-Xc7MSH2o-NIHhoeAmq4OQOH6YKXf21G8lUYBsaujbIsDwtL4q3TmGQo3Li97uWNxVKwHco2qjICkSV5Qc3mpH1tDlyA5gHVk0aWjBOebnczUaG0HO2yDKV9XXmH9cX56SRoO0wu80-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😠
ترامپ: با توجه به وضع بد آب و هوایی فردا، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق میندازیم.
موضوعات کمپ دیوید: ایران، دستاوردهای اخیر دولت در زمینه اقتصاد، کسب‌وکارهای کوچک، تلاش‌های ضد تقلب و تحولات سیاست خارجی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76033" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقامات آمریکایی به CNN:
وضعیت گروه‌های نیابتی و حقوق مردم ایران نیز بخشی از مذاکرات است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76031" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFqH88gT15O5pfsqCR6KOrEVTvK4mLxrOYSNp9AkLz5tAvZ_poc0ZnmFNRMJettC3jds7ifENflTjfjp8UsNhDEnJGzw7r9I5IPRKUpKP4hZFCzYktFIzGsPd9Ag4y9Ual1ybQVYCKsIFFNg_vBmZokfKoiVlH7RTqSs26xmkkdBD4O692kro5tvJYxYMzyj0sdN7xXRVvHAjYTAWlwjYeY8MHo3pYLiYKZKZVwaButpvULHxuLSyl8DUSINNq2Gcs7rQ4OTIZNR7DmO3QFRUAunZQIXC9lbuN1b1Ok-NzKIVY9DsmHGkeKwZ9WsAfpv6mb9_3rrP724cIwiOYTM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76029" target="_blank">📅 23:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTiemlPTYj0TfQhp-69JgPIgen8D4RnlBb9LF8_sVfJUdojstve0ERwWgTydo3GMX5sNFLSEToDy3lMPshT2F6cFUHIPl9Zun1Ur_sAVmOJxN7MLSa7L540BR98QYMZTt3JX6NEiByXMtIZRtnQcVm687t1Gk-K7DRmg8at-bjwi2NpcBNi8Rt2IW3aQkRxgreVw5VRIb-3MPavrmrxMjjWPDMdgQmwbpn9Y1qq7rDUO7Evlsr-4iUjFVjte_Zq_d-JsFcyINcZ9ZMeAF55e1QU0hld9dzQ9b04sluRcVEA41jq96lQrVKsr2Ay7xjVN5hf_Ucz5mvZroOXDoB_KMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست فارس هم جاودانه شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76028" target="_blank">📅 23:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOhRGa_En5ygKEjwoyjquA7aoVK3PPQV-AYlacL7lSDjiK5G7VUSvBTdYgU5asPR8ob6JB_T0mqkAUKwBY6OA7OXUTGBLIPHB4aEdF4SHbNog_oJ_IrskhAy1_7N_HxaSPqyq_gFH-CzKAH677rs7stAe_lTO_A3JOsKH5HFev4qTOyQL69uXBPLBHd-DIIx_mInPgZkpoKoTVQPegG--uemiIAJfbeaYGOIUXqO3WnZ08Zns61C8kAFZUFCyqtWx-8mzLWafGu6NGt8co_IoxZUWmT4u9mJtFx3TFd8x03gtfnBPTZ4m7-CcHY3zxN7m-ET2Qz9ETsQmlQLB5S2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76025" target="_blank">📅 23:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانفیگ فروش اوپن وی پی ان نامحدود ۱۴۰ هزار تومنیم هنوز نیومده، دارم نگران میشم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76024" target="_blank">📅 22:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتم که وصل شد
بریم تایم لاین رو بگیریم دستمون با هشتگامون
✌️
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76023" target="_blank">📅 22:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمیدونید چه حس بدیه از کسی که به کانفیگ میگه کانفینگ، کانفیگ گیگی یتومنی بخری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76019" target="_blank">📅 22:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانفیگ فروشا انقدری تو این مددت در اوردن که الان میتونن پول بدن از آمریکا F35 بخرن به ایران حمله کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76018" target="_blank">📅 22:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76017" target="_blank">📅 21:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حاجی دوتا2 چرا برگشته به عصر حجر شبیه دوتا 1 شده</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76016" target="_blank">📅 21:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تا دو سه روز سعی کنید با کسی تو تلگرام ارتباط نداشته باشید لهجه اپ داخلیتون از بین بره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76014" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3-loWr_S5jcjJLBOb8QuEyxaTmbz2nz7uvnwyqHiR7lJ6Ql5dJUXTyJM-F1CZA_C4b5bISqixFafe00rpfo7fruhYRxbnHNuZ0_qB6OBBgqR_8x8sovBtLVlXQSV-6bVuEg4y6FJn2XPjlv97iqcguMRdPNk-71Kwbl6PGEFud6ZI_knqMKP05WJ4ztve4Y7D-54pLDX5kwRcIoRU6CNeIfjNqF6hVFvdebLUVTpXK6e-GU5GBZm2_vZHlafYD5ABCTB3vDvm3DUoGCtHImxCFOFARDiyDgi0jrCNWGKKGSweO8qMlSYIn6rrrX2sTJ-PMMNl8N9STXm1k1GWyc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">NetBlocks:
🫶
Welcome back Iran!
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76013" target="_blank">📅 21:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از منابع:
حمله به ایران پس از دریافت «پیام مشخصی» از آمریکا، در این مرحله از دستور کار خارج شده.
این منیع گفت که جام جهانی پیش رو و جشن‌های ۲۵۰ سالگی استقلال آمریکا عوامل مهمی در این تصمیم بوده‌اند، هرچند اشاره کرد که وضعیت ممکن است در آینده تغییر کند.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76012" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اومدم بالا پشت بوم ساعت ۹ شب
هوا چقدر خنکه واقعاً
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76009" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جدی جدی مثل ماست وصل کردن، چقد عجیبه اوضاع</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76005" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کصکشا درسته رو دستتون مونده ولی چرا باید کانفیگی که فردا قراره ۵ هزار بخره رو الان با تخفیف ۵۰ درصدی ازتون ۱۰۰ بخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76003" target="_blank">📅 20:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چی میشه که درست بعد وصل شدنتون اولین کار تصمیم میگیرید از فان هیپ هاپ لفت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76002" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نت خط هم برگشت</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76001" target="_blank">📅 20:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اونایی که کل این هشتاد و چند روز و آفلاین بودن بزرگترین کابوس vpn فروشا هستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76000" target="_blank">📅 20:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه تازه وصل شدید و موزیکایی که چند وقت اخیر اومده رو گوش ندادید بیایید برید تو پلی لیست شیپ همشو گذاشتم
https://t.me/+7joX3IWJYepjNzFk</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/75998" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمید رسایی، ستار هاشمی وزیر ارتباطات رو آنفالو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/75996" target="_blank">📅 19:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت ارتباطات: اینترنت خط های همراه هم تا ساعاتی دیگه وصل میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/75995" target="_blank">📅 19:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان به نت مخابرات وصل نشید امنیتتون به خطر میفته بد افزاره، بیایید کانفیگ بخرید گیگی ۸۱۸۹۱۹۱ از من
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/75994" target="_blank">📅 19:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب نت وصل شد و میتونم بازم ویدیو های مورد علاقمو ببینم تو اینستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/75993" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvym2vmLElkrLWNd0J722n5bAaDWXZEzBK8IlzrUgoSIGoQLPySJJjaZoT7s5FyyB4vgzKEWisTyST-j8XNsHS62boSsmkybow80_lHNYjvLxDG2ElGmfvZCgH9gAhqwDrvzUXsseA35WUNq1i2dB0glNxXWCYrne78OGK10Kn-E6p71KBS7fTPswF-ssoIV2m7UQK7nHCaM6m-wkYFIfU7gPAnftI8oM27VpDECgq-GKdQq-FMW2z0h7csvmJ1K-Suw5hXpdwSXG1_Sp1XhDAdViDLU4UJcNH5Ffp5TIGIz926bTYqs0Hf8o5rOyNreCLO2i24IRwQPqujF35KZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g5
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/75992" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده بدون اعلام رسمی، کمک به عبور کشتی‌ها از تنگه هرمز را دوباره در قالب پروژه آزادی آغاز کرده است. مقامات گفتند نیروی دریایی قصد دارد در روزهای آینده به حدود دوازده کشتی، از جمله ابرنفتکش‌ها…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/75990" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وال استریت ژورنال:
به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده بدون اعلام رسمی، کمک به عبور کشتی‌ها از تنگه هرمز را دوباره در قالب پروژه آزادی آغاز کرده است.
مقامات گفتند نیروی دریایی قصد دارد در روزهای آینده به حدود دوازده کشتی، از جمله ابرنفتکش‌ها و کشتی‌های کانتینری، در عبور از این مسیر آبی کمک کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/75989" target="_blank">📅 18:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ عجب کصکشیه، بهش گفتن پول بلوکه شدمون رو بده اومد گفت خب اونو نمیدم ولی ۱۲ میلیارد دلار وام میدم بهتون، گفتن خب بده  گفت نه دیگه من وامو میگیرم دادنشو قطر میده بهتون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/75988" target="_blank">📅 18:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ عجب کصکشیه، بهش گفتن پول بلوکه شدمون رو بده
اومد گفت خب اونو نمیدم ولی ۱۲ میلیارد دلار وام میدم بهتون، گفتن خب بده
گفت نه دیگه من وامو میگیرم دادنشو قطر میده بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/75987" target="_blank">📅 18:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز: قالیباف و عراقچی با پروازی فوری و ناگهانی اکنون در قطر حضور دارند. مذاکرات باقرشاه و پروفسور عراقچی در دوحه بر پرونده تنگه هرمز و اورانیوم غنی‌شده متمرکز خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/75986" target="_blank">📅 18:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وی پی ان فروشای عزیز چرب کنید که قراره از این به بعد ساعتی ۵ تومن پول تبلیغ بگیرم ازتون</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/75984" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyOb7b7iRay-RoW2UrRiOGtK9gs_ddAjTVgcxjIVnYBQ0CMUuDj_C4DG4HrHz-puJTV0jFXVgwfnvLw7NN2FjYkYCHwPxUt3Sn19yexiskfg5rFsQ2PXFPKMoh7i1G5C4yft-xxpfm1t3EeDcDLduCp34XQ4nDDKDA2ByU6GU28sTIzvAuZ568HefgYoXMfLnkLFlaKuC7nuytKBZPNCW0tLD3KQwgam4HAg-_BbOuNE9RcXCXYaLW_dQ2ehe7ugygCmvJL09lndjs25jvS-3_NqYck7HSM14qrOXG6f2O_AoT0Sz1tPQODKgIXiTcwrQsfMgJmfN1BFhabveSLW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعش کنید، قطعش کنید خار این اینترنتو گاییدم قطعش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/75983" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلقک بازی میکنیم ولی حقیقتا من یکی نمیتونم بابت برگشتن نصف حقم خوشحال باشم و از کسی تشکر کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/75981" target="_blank">📅 17:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ای شیر زخم خورده، به خانه خوش آمدی
📱
ای پیر درمانده، به خانه خوش آمدی
📱
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/75979" target="_blank">📅 16:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:  من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند. می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد. توافق بد توافقی است که می‌تواند به دولت اسرائیل…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/75978" target="_blank">📅 16:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:
من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند.
می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد.
توافق بد توافقی است که می‌تواند به دولت اسرائیل آسیب برساند، و ما اجازه نخواهیم داد این اتفاق بیفتد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/75977" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وای اگر پزشکیان حکم جهادم دهد</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/75975" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آقا خوش برگشتید
به یادتون بودم، همش میگفتم ممبرای فقیرم بامزه تر بودن</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/75973" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تا 1411 با پزشکیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/75972" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRQ5hrmjjZZJEoYL0ygTW1AGNW3x9yRgUVj66N-EW_TZLPI2xqhL2JCtEYOTSVDUus1qArdwKk2JEcrXILc1YfuysSCYz3GbOWCmyaET6_3bZZxfgeRvA1-t81PiNXQZoub3zMEDFKSYqAY7TOka0K3nSAReM1Y7UCU3ClHUdgCR9-cg0_2Bo1Clye2c69zMJCSc0eWAPzcv6FlagOVu5zg6aH8xMxT0ZSR2wwtlLQBxoWrKKNu8dSw9SwzwAQLTSRllZqtP-zLdBG23IO2Z5KTGq3k7-q2R996O9frIXPlnspZJIasz3szbVDwoy8jaE0em0RANbzbPC4QtjJgCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت مخابرات وصل شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/75971" target="_blank">📅 16:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حاجی من تو اورژانس بیمارستانم
کلی ادم رو دارن میارن از رنج سنی ۱۵ تا ۵۰
بطور عجیبی گروه شغلی همشون تو رسته وی پی ان و کانفیگ و ایناست
@FunHipHop</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/75969" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آسیاتک و مخابرات انگار دارن منطقه ای باز میشن</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/75967" target="_blank">📅 16:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات : فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/75966" target="_blank">📅 16:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات :
فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/75965" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه یارو از ۳ ماه قطعی نت ۲.۵ ماهشو قطع بود، الان تو چنلش زده تو شرایط سخت کنارتون بودیم از این به بعدم هستیم</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/75964" target="_blank">📅 15:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه آپدیتی رو فیلترینگ پیاده کردن که یسری از کانفیگ پولیا هم قطع شدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/75963" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عجب ماجرایی گذاشتم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/75961" target="_blank">📅 15:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کونیا من روبیکامو پاک کردم تو اون ۵ دقیقه
نمیزاره اکانت جدید بسازم الان</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/75959" target="_blank">📅 15:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/75958" target="_blank">📅 15:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/75957" target="_blank">📅 15:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یسری ای پی کلود فلر باز شده که دارن روش کانفیگ رایگان میزنن، ممکنه اختلال باشه و یکم بعد ببندنش.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/75956" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
