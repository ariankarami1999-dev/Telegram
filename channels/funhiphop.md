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
<img src="https://cdn4.telesco.pe/file/TpaV0ml2c3MIAnzTZVEg2sFKcvT_DAL42RO67qEmpHUk9w7cKVpVnicdTPAmqbNTgMelC7piRCRYvDjEONi_z0ghn8ttG9ReM4BOI2NhCca_mTUZDoEsRR29pi53BIKU5YN1tvPCtl1HkknLp7zuLoQw_7t3sMbYeUwAr_76_f9xACEru5uNth7yCmWkYaMG5FGwG8oQTmiOuZD2fEGTFkEwNiyX6SQhMpvduM4ZBw2j-0UXOpz7A0PZrtv1jmwMedpenXR8sAVaKZSnuSrg5fhN4DijJNZ7_O9cwnrPf50GYPbWWtRdrUXBoB39l5e75H5RPwX0mXaL6IPSbl3CWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHgadWgVXamdpZ6v9-iFifUpyxB4r1qf7RWiAkzvCgT6AP1gTe9R6kWUF7c2vY9VJXUgPCJPYpuBgYROgQy9Y6CssD7_3ZUuNOje0HUoaA7WXNbpDogTQ3fcs_jlQKCEntsH881GR7Q-EINLcOt3y8Aydz8L057p16XxKb0uouzVtq2S1T7eIn098vmgqSuHrnsPqMhEwvqzQDEtE5VLtbekYsMbM3WOOKMWzIVvCym-0SWGULLHhIqcszfI81I9Eax_wWEKrKE5PI4tdJHBt_7oXhN0zDQ0SrgveABZoFx9XBy1XpYb_l9l-GZibNsGEOupYj9s9985h2bEzWr7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbQ4v5fRpWaif8QGHxYbUIgkxnMTUwziDGFF1r_ZieOYLrIYP8Z2eKHoBW6w5AJepKi1jif6CWbyvoxh54c7C5Ju9mO6oN66SVg4D_M7CpeaZnBOSxJAnXsHO8JkuxHv8TXGAPYY14qDC72iROSWmzIeArn3eRJ1MZl6FGypmkVcJThPi4kreJOBZyB3B7VhAA0x0ZobIo33m_z2qT0b0cY8nATh0QrEPBo38IaJhpffcWKXpmeLOzlqkbKMSaY4VTFkr20LB5Xt1ww3xEFvU6ol4oDcK0qJaxyg6Met-A62fq6QMJHBLCMtxExdMPxp05t9KLmfYoBZn06xIRSydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgRw519GFBI5g8QeAi_nwNoUxQB-WUS655pPnV-qv-gK3mac0UGn2E6Iopg0v2sLyWU_NqB0sQjuG-8O15YHHp33v7XRju1rK8_S-egNzUCXd0jzXlkWvcRicCUWQDhIS0IyEDJD6gSCv5-OJVMtwdwAsGpa3a6yYOWesgdnQiCBOWNtQ8jJYF5z5n4Sgpy7Bv7JRvdzVZqCGl2gtuwkgO5pVipqfjMTfqhaQ-AtYnrRqc26lN80pNfz412KtFJuLGuEAw0FbROI5WSudA0XRxdGbx8IFZhTXGh8OhsLjqUiN8E-YrzuKfcq39TUar1fPy6QKl23kDZKCb7iD_uXfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vdBdV4MPy2VBd71Zb1FuiHt8fAmf71VpT3lE-aip2xnji7qbLAInfu7ib58wt_948cKgsDGTspFf8QdHgGmbD_ezUujrt5glIlGx1-eJ23uSCRh_6Oww-C1ZdpLWhaXKvtNHcKJeam4VKEAVc1azO0ARiZvAQ300aIwjycOcyjr-c_LpfwXdgb94_LsUNgZnJcuCozub7Aqn-M8jUn_rbQWlUlHocsan2Dw31Yu5-9nthjkymoJw4i_YR4R36ckm3qMHlCqgNF1SUzPJPnNqLSYg4k6XbefwIIgGqZRmXVpFKFAnmcVD31-IRla8cpYUQrA1tuwLndCEQiPv4cJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkg5E5gGdbYD2qSgtPvN1QOBCkAvZGjRovPJZaCiCYWYc8_gJHHVjZHmQBPcZS2EPukBQjVvTkIn5gAg4NEu-hOun54z9iB5T3ie2Svz4nloEe_rQVvq0l1izR7DQmviTiUA59by_EU6efaw21reOShuw-6YQcENJ7fJXqd_zX1wnP1giKcoVe6o4IuIq44CLk5grj12mOYTlh0HrEcZYlu2Cvh8NwCiFk_n8ZjlZw3nr0ZF2SWdNicnqkP2aMDC-aq2oDntZ7BqXrNT6mUee4PBdrWF9L8Zn0GrCQ93GiLL51MxbU-C3vRm-sQ-NE9vdeXj79k6PhhktwkUsAoM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :   • @TrollSporte  • @TrollSporte</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77981" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2JZPSMuNltA6Arl--KViJB_pYmDVe4nrsUpopXzwT3Gk9SwdXylQXV1FpDhvTiGtYAZX60REDJx4BsCslXGQSYWV-GI8c9-7U5rqOjlOO-sUZEb6j4LBekW27gSg9aPOs7bIAvs5w5dAmu_z5Jqvru0kk9a3BkkjcT4CNvuXCCzRG38hF4-XniY6to_S4bDff4fV2vLVW8iJflf9twFBwKpSnV86zokykSgvt56MaLzE7kSQeSgwXRhsPE8MyHiKnL3EZAirKIZbwAYzRMqqqeZqItEHo1RU1o79zhTkeZ-nTJLO8Ape0gKOn1tDASIdvy0bj34j0F7pLEzE1ZPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77979" target="_blank">📅 00:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJWckV4vDJIDvaVCf6mOsuYDD6pAEv0DCYwJ4y2XgZPFINERNF2E7pAR9FdVEnU-ByrpgjYZEOJjRk3FW4KiTCQLW-IDJ7VwASPYUIeCNQbBH8u-Lyj8UaUzXg8IpAEwUZqtNKjxNax2ejEedaNDV1CqDcc2Js6AuAOe-U7a-oZ-riMJdc4r9Ax9RkABL2JnIKZLM_e3eCKWCTOGjlJmuAd7TcbMZfTLT_-TfuyUNPooVltHLU3RmRMEVoYcBvxSA8TAohq4W0wK_efZ0vsuU9RpEHYD93OOyGebCzKeOSbLb50VYeUsnkXgvJGd38b3ejpPIIhKcpqOu_HOEpEQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi2nz1AwFRPBW7WAmrBThaGsFOA3-FrI5ldFDbktrK_4YfQJpoFO6TeesJgxoxn2hJzRMEZ9fmy02JLO_M31viMc_xJMpTwMWKUDqhwACVpEqjOsf0cqYQFdazy8Shh0Obgvjrt84N0Ie8zN0N2zKc6ll-HGVLnmqEJUrLQdNoBdqrkiIG6wlbuGX6_zr6P8eQ3QSHq5gNQ00IUQPaZFLfeeYAcTXgeu1s5B77cRBBpPG_mgRzz9iamibkN86Bd4S7OybA2lgLFSc8zSyXsQ6HnqykqN9xz74FWqrRsONHRDPq4dV80AmZ1Z6CgcRKTNcGXQRDRKp7tMnaAyv39ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXIreo9FVflbE8G0Hqlt_l4VC1plS-jf3VHnX7DpJJcz3pw94V9icjKpdcGZDPPHiccvb91EQSezdwrJesnqXNN7n3Tmww0GJUw7BkXsKqET_cSudGqqjbIym1pxutFvnkTafgysbFIdovy_1BRtIne14ytjtclVlsI4y9rniwUHtkxhrV8RRdKH3fBkJpfhu7wOLEDHvp6QIIj0e7jofpwOX0BRJATY7r-42mwOpUsj4dJDYVvCOT0eioUNCyYbtka1n2xxkb66ncbGwcD8DLAALpaxtmyWlyIXV8gqe9k9cWuInVmhm0pOPyw_Ix14hhh_0XF5cCv_fhpnXuqNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRM3VX4w6iUZz_mN8Ob9emNBrC5p1CLj4Wm4kStjXbhQgcvxDMYp13lH_JzeWiMjQX4ET9FCxzAHrAJSDdnI4j6wfdFwoLCsri4AcKIENCeoq-L7pUe5J8dbVMmWm3fhYXcE3yStjDbdnrzZ5EzhrLHxpBiDkU5S05aSCoF9gzbNqEN-Z4BAcvx1RQIIRf7mqmdJgGBr_hm71VUkTNUvMY8s4sopNdeoFlNTUDRNFA-vF_XC5PBkf2ANB2DUPgMIJeyYm9oqSmFqh7Kid6XvIh9LDb_H3F4_nTkj8gYGTAtcLyjX7a7-u8BX94he4N3QP5DPONM-KsFFVqBbOqLVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKDtlgsebzWYXbzFDFDF5CYAz71J4vfoR7I-QFmyYtaQk4LUnm58uA7WT1g9WjnwgOfTCAS6knFXUG4GTBqn8VqvFQyX0sRNdcshcy-H95N2EWfCUq4H5U7z7GjJeTUrZOSLNEqUr1O2aZ7-Siwpo2Jsveghw5oD24ecPO5QIYkszm7dQwZDDCx_ngeRf0nKn_keVdsFr_e_TeaqEbuvglBKXOxcYQLUllE6ijU32Rd2uApZKBMYiZvxGP8XPSBSC8oTXc1DuogAKImTNfrgm9V2r3qWIQoeg4IYwpj5YrdPzD5BakS1bICWtYyvJBSLPWp5VIa9B7UQNKDd9VxRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvJuZBiRU9GlQi63OSNQhMLBrhCGkpv6FGT8n2vM3rtAhLCOQpzKXXhRdbRqNo34HdA7M7VL09udvxtNr9udV3V-vI8svOYAOsy5XxfzL3E1cYohwcCSVTHUyjEZpuy7xgO5Vs1erhRQiTzTMHtD29p9m-YG2hzmQLivAXOqi3J3XNZPUAly1Hs0uykM8T1eQHqEOLXyzk_DtlJWcBLFmOV4MtMG6KJcqh5p8addW8Rj2Zw-k6AlC35CvOtPGhd_JahAyc-OzXYlrFlEYE99TEt6oomk0eFcs-6_q92A8y33TO93kCqF-bOc46rYkyHIUsX4FU4S2f0J6QxgsMFGKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvAZ0JFOkqM3D8PDK3dHEL0VFayP2oW_eWOzI4hHtS4hSF6NvKSCt3Z5lkttD5OrpNCWaVnYIFLUvfbfwvBFCG0jOOO-kbMpBH6YIDH69kiDVOVEZ7495ETT0-4lcCCfj_8h8416MVEjBCA5l-8ZYZUuXsUJY-WiGDYeR-2a9r8gVVUvs38eCnWcgh8589DZ64IzllojQ6M64439UT2a26nVHXIRlHnH3wdzGAgQR7tkYljPF4QZoI_6e6D732vzs6ZbUVVFsZkFmwMBGV4lgLmGDMhX_XgQo7teecffoHUbfHUT5tJuES0cmzD04LdCPmxaX1L8rD-minUqseJguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77952" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD2RIUuPGy6CqjwEduKPF70Ydaqj1jyFx9PqV_Fa8AjJIsQqcMGkKDMg4B_ykbV98-X9TNOOhUicEF7oN46wz4LoPFd0fu1WibDz1QfAIIzvYdvC0t0HhVr9-zgqAjRkTU503Vygz0_iKAJr7tFszHWi4nUjJntw3CGu-0_uS43U3kBczpVb_c72fHeOvMes1LR7gd-dWjEUsTByA4DcBrOnqFF-LIeTfW3WjhQ_jIvdmBu5K4enn2Z9Ec6qc_jiMynDGt9sGUkAgqVjTVEBEaLV462uZQRTxQ-v-NvO8T3AfxgFR9CFsIomFyyHOqGtq6Eig9KBpUb5iQVWgQAI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g25
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77951" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAevDdUyvw6jAguDThSty8Kr5YEe-Tbqmd8m6htALOOXQC19HuHcP_DQDC7gkeH8qmstNH4DCXtsp4eAh9jnA6dmO_GIN7fisOxhtqjyfQJExTZ1qXL4QfZtegrD5JQyAIYTg04a57F6_sxfYR0CqFz_EIFfzJUS57-1tbvp2NCFCHU-I-FsRgL2h_d2vqVaNJhNa4laM1O_2lKk5_dnQr-6HUNXBFD0NAlJ9_-3YbCXQ5-r3lqx-wORAzNWkFJiR01PKqPDRwVzCV8Tx1BQt48kjgwZ51nGdNjYjjCvLfE-OmxSl3vJnsaCzizSwSJgyk916YXcZkeOuvxvaZuQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbNO5LoUy6eqOwuFTYn9X6Eu-7rvb0E4ZWyBom9zNzPb1s8nKIzsoparc224CdbQdfhDUepkRYrksv0otQCtMPxnAeWdxcoQLwkDaj0PTWGHW8QVOLxaciUQmuUJGGmHD_RMPqTAGbogUNIX_L_iHCSnYI9yiVOKkSgLczWvizb2-U1JJl-X3oim5fQNkdPGyxAl5qooYadKfq8ESMJxtD07TLsHZdFhHdkY3dQnbTGiUqzESvKczW7FZ4CkMwu-Wurm8m8f8UJ7dkwKijcSZifPyG2qsmVhge0gP4bUXohwkAd6kFB9kcFHNb9w8qVZaKhSoqUf5F7IC73r8srSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfCIVUoRDqwp1HBzdd4UoUJ8sOmah-jUXEbqT5lUep0XPZ_e0z-w-zEesLCWaqjLB68e-ymijQcFkJk4db67prZdRLzct-vjIyMt0zWOneSnFN827SDD5ZKZ0X6Lcbw83Qn6cXAj-rnlnPh5hR6Osz3JC5sbCaXC4gTOvVPMbLN4XRbm-YiohCqWj210tmltoF7UgExUK7dLwu9fF__eMGt1bRmeiTPM2F1ytXfFey5zACgDBEW3qIeerIVQPmkFTo4ivvzbNiCZFaux_qN50Dg2CMKKPWKoQqkjuxXrr9NBawTZEyThDAZLPFKKe_-Z5j4UsM4bhS-px6wVaacgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یعنی جدی ۳ روزه چارتا بانکو نتونستید درست کنید؟ بعد ادعاتون کون خرو پاره میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77946" target="_blank">📅 12:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdXvQ1vm3rO49MVqzDe7WDYL_-O-_QAYJpbe9H970A51ZS2Jm_n41jw8QLvpN6nBrYSNzxck5RnWaD6-NtE9ddp30t9DPNEXZuNakXAy7qQj3PMbkq14gafKyFxZ26nlrLIX2WyI99zd4XEv3fRLD8iaXVIkNl7cOzRtJxOQfKdV3RUTHQ7P3WEeecSrYLa7HTN_dLBOyS1S8sx6nu4AUeREcaOohrws2Sk-jNwwHoPU68jGZTiYqJracUrJVNizxIjuY2WHX65_fQOFmdoLwygANAcm7wav8QsHCzu2UquEreMXLGi5OdeCWnkQC940qfXUcaXQHiCPpUZfp483CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=OEiVI8jBzobhOtz-XvvVTHg9CIHsqf97x8BzVGA4_LPIXTUDk0qwZxYYPxTGMy9hb0AZqrmQaCiX3kYCu7T48jML4nBa46FT4m3l9dI9pfXXpWL-xC3GIfGbJsCNJFPuGS8jjoVUjck5J0Cr8OOtMwDdNyatssF2Pl9xjAy8GKeU_WBosP4EvMcic-PXCW0dIBcaH3D1UO7kOpHsAGCvom4U6vqKS4iU_40pajTVC3BEjIOuZqH009bLn0xJBH47linjafTQapU27b5G6jepWgBX8uZG2E1ch1XnVc87In_XA8qbfrVTAHN3x-zwoVGxA8Cey0UwZDZVvEGwSpIR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=OEiVI8jBzobhOtz-XvvVTHg9CIHsqf97x8BzVGA4_LPIXTUDk0qwZxYYPxTGMy9hb0AZqrmQaCiX3kYCu7T48jML4nBa46FT4m3l9dI9pfXXpWL-xC3GIfGbJsCNJFPuGS8jjoVUjck5J0Cr8OOtMwDdNyatssF2Pl9xjAy8GKeU_WBosP4EvMcic-PXCW0dIBcaH3D1UO7kOpHsAGCvom4U6vqKS4iU_40pajTVC3BEjIOuZqH009bLn0xJBH47linjafTQapU27b5G6jepWgBX8uZG2E1ch1XnVc87In_XA8qbfrVTAHN3x-zwoVGxA8Cey0UwZDZVvEGwSpIR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgRuW1h6BWwvXNWKlb4klLj4ttZbJbL3ekQtVA4u-HsSL849Yl4qBW5z1BvOGZJigShJdukPtLzG_uez2WTGHjx2GuIYMEgsrOjFs0kbNDkIsuPEiUahlU8_mLClDAUDixEnjYZ7-sgiERHwz94dfxTNUIOYk0knRdrO3zq69QmtQl5gwC1mnDtRCg8UNeAET2K3OW1YiOjDUw6zGzbwRMAohc5EaD1NNZnXUDrUQMkRb9N0j4Dyr1IHiOHcBwoKpbgCLERFuYe0FQ0nXdRbFrTn8GaAuGF7c4pFPRyPYMAOnBle4-dEqfL4HYKvNy0EfCVw6getJ3C7OQ9feNqDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77936" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4mjiyASAx_4iwbYkpPH8012LS6pKK-U-BZZ_GyXhEBXIlZ14KC_Bkshxy-FK-a6JdU6docE8G19lCcb9ph4Ts4MWA95oQbsJAq1gxi8g1EOkmIvrEzaGEdpHKnn6INyVXX87I2xvjtNLUCB8JnLzuwxz2Q8Zkg7FpkIRaj7TF47JAaRt7LWoad4Ahw-GIUB6fupDFcjuMyQJl3CcVqty24lcgQL8SYVQQvhLWwF_JFxDaBAbZxlSuQZBLo7rcXlD_PzTGPaxgv88UgAVUsNZXK3LHHTLonhlhjGU9zU8rXZVVmR-Zp3gn5T4S_f9iJ7UMcvI51-t7b8SpF9b5WEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r25
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77935" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOMREZRDW_zVqHeuWz8YU_wuYSZJ-BQ2rw4VtpIGlwVekp4dZ7_IwkOX9YVWt-xMAX5Y-NRrISAuYx4-7rz9UYqpPswlTtD1iDrQWphWL3DyZ7lK8iM-A3Wt0KuFGLGk1Tf_tOR7GEejVa1R4zeV1KAxkdn4nZ4zFDpNv1ugVR21LeYWFIGfZQUjdSlyWKu8F2wwbuv0M5hspeMHpUvcERwRzcaKhRoknqzcixr-3bMyN2ks2PLVZTn5Wutq4bT3qiU-ZM69JaP9HUxE2CH_h7qvCH_F01KWL8u-AtVIxs9i1mkBoBPGJCapvzH56I6U0tL17e6nT1Whkpht55LSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا یجوری داره آب می‌ره که انگار با سیناب رفت و آمد جدی داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77934" target="_blank">📅 09:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توپوریا مادرش گاییده شد و تو پایان راند 4 دیگه گفت نمیتونم ادامه بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77933" target="_blank">📅 08:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77932" target="_blank">📅 08:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlAil3RVGOpFpflK3faSICPLBBS7h_7CwBcXws3EQ7eUWaKgmUeZQ4dR7K_9S272JQzJnPeiG_GeoCLybhgLIBDCC486xFuzuuj5WD6ZGuTGwEBFD6qKwbI8J3dJXSxtF6ZTssOcLjCJdRHJlBzYY1bp8kmvJz9-6wzQyYOYbHywYzwHy1geZbna5a2IkZMmxMlPYLEYKysjUI4IgjIxPX8HuP5m711Kk3QqBvh4z2jaq7EVJqYbf_b8i2dEMjufWBx0H827TUfSgIsZQP-IKd0OctOD5Hs81-E51_CQEatoJY-knM7ootwxV6J8QmjfM6UkerT2JtpEBOqewAKnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77931" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گوزیدی داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77930" target="_blank">📅 07:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfo7trHLvS280bO6r1w-L2cMgTCnifqHSeLWHpXOjAIGW4t2TPdOpcwIjcHuEz2pMgI2s5kebGMP_cSC1Lzt8jQzR6gSNyIIxynIA-Hz6I1XL-boyYAfLqyFEvatXOp-F6ZLoCNzcDAZhHNptB7MZSwxB2NAnCugZUgDGmb0Vi-n4WnRyJ6yUiHF4yVn7O4_hrjj1HUHIaHUz_HEJmoVWtkm5TyBYh0bJ_rUgJHbSzIQGsepWFqUXljYkA0g6vcRs97uRQsWnQH4zfJ7-O51xdESrsluuOeHbID3GwY1C5ezfTEgHR_K3rutYWmpCQxsGrpEji62ZWwWtB8OA9vxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوزیدی داداش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77929" target="_blank">📅 07:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXPKP74TwhyV0zkkTRg71ta559Nlu6UvuI4_1gWHibIdPlOFDbo_vjcDo0LqXGNLOlL8NlI_cLMTGC90avO9if3Kilt8f8PddgMW_SnZyIYF3nawwVob9F0jVd4SdndC85YctXHhgDIyhMbsRsu_FVTBEDpKbKpNmp3simXekRB3EUksz_rKui2-ZBPpLay64gtfVZo6gPFy66s8Xm9keLpsSlmxdiQnArGNXBu7PsusQgTIK7KoPlATjbivHRzN0DlNVBY-dij5ucdNb8wymQrZcYA-8wS0tXohhJOiDE40eGc7hrq8tgke-w3RPa3v2-VZyIBYkdvsqxQljobinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7_v3I3ZSqaTzDEVCa70bd-KnIQrg9sGyawcu2lIZ_-WhVPAwGBZRr_ChZb4POMrbQC9cFKYxnTOBBbXUaWHxlS_r9CHyebVqSDkzTvevrBZ2zymhZi5dWc9GT5W1BT-9QIbdOfzkpz1CBQuMvJDGVG14ZRtKwUSqNsqLU5zZAaoWCfDcoYp7oNbcgvrsM6ZyqFd7Bn4HVQdvn3ZG-wa9oEeXpFS3FZo7pt3ESQK9w78wnZl8vpY8ec0XQRHy3eL72POUCTuwBx0Vw6VNH5Lfe4C95LUi5j_hUwSJQYzZ0CpXeJEhNdmk3j0kHz6__f6FECR7Sl_a6Pve9L46nKuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ویویویویوی خبرگزاری Ynet به نقل از منابع آگاه:  ترامپ به ایران پیشنهاد لغو فوری محاصره دریایی در ازای عدم حمله به اسرائیل را داده است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77921" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=JA6u5YWAHhmmimNqAO10k7kV9USMkVGViOjBHTUgXV7SLPNnClGA3CGNIIbMCC3gndqMs-60kd_707qeKOZ71pBAUvsk353qQ1vsCfQcasEgWjxv7ChLRlGtpXFhQAQ_tJa8ALmzqiouGiKOwQphz7jJ-T74MHtZuwwx3SJ8DYVwjAARgn_1qkmMRaGs2-dYLPwYs4cXDqdDsenBPnQ7iQ1XOG7nBkxpCkBnH58k1itDyOrV8XpCbMaFwcD_krS2KFFG_OxQfYSD6V7u40hfDIeLt4D5o_VAoj8KtFL1urGlwkXs4_AlrEwQroCG8Eu7MNhD0PrK1JyBDmweO2SG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=JA6u5YWAHhmmimNqAO10k7kV9USMkVGViOjBHTUgXV7SLPNnClGA3CGNIIbMCC3gndqMs-60kd_707qeKOZ71pBAUvsk353qQ1vsCfQcasEgWjxv7ChLRlGtpXFhQAQ_tJa8ALmzqiouGiKOwQphz7jJ-T74MHtZuwwx3SJ8DYVwjAARgn_1qkmMRaGs2-dYLPwYs4cXDqdDsenBPnQ7iQ1XOG7nBkxpCkBnH58k1itDyOrV8XpCbMaFwcD_krS2KFFG_OxQfYSD6V7u40hfDIeLt4D5o_VAoj8KtFL1urGlwkXs4_AlrEwQroCG8Eu7MNhD0PrK1JyBDmweO2SG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچگاه علاقه‌ای به تغییر رژیم در ایران نداشته‌ام.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77920" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شهباز شریف: به توافق صلح دست یافتیم. جمعه امضاش می‌کنیم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد. پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77919" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این زیر یکم فوش بدید خودتونو خالی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77918" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsrQiXil6IL3yL0zmGYTP8rm0L_L1--N-sJFbotIFUGirLTtAELF5OUHFO-_Q9sPPvxKlUNmi4AZ_2swd8vp_id7dl6Hgn2u7VSe0QlMPofDNtVOj-Sxb7Df-f7iLzA4PvM19MV8vVmkaCKupmntbhHOzBB15llnY_20Qla0zvdJhzz7flnQFehpAGCjaqJWcKGvzE9fJq4lL5g-yMN_H58Z3Psa8ugFx83PAaOgpV3TZ5HG3qqsKnxu-qaleuuWK7Dd0ZyBhHqPDJYQlifsC-Fqf22UWGejxfoRzb1DXPJ-8PB3aXLapmpZPsERzAlt-Ccu2Ai5Dr_1WpaNQQad9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف: متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77917" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ژاپن گل مساوی رو زددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77916" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:  قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است، اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد. این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77915" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هنوز چیزی امضا نشده کیرم تو چنل هایی که خبر فیک میذارن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77914" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گللل هلند زد
فن دایک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77913" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:
قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است،
اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد.
این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77912" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">توییت جدید وزیر کشور پاکستان:
الله اکبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77911" target="_blank">📅 00:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoxeQo2-tRvggo7eeG3usNPy1dXrH3GZwS1fcqen2sEFEy20sudtblKlvfW4kO46_PJf3zxTuxnuvW6LOpSSYgEgin8Rg9uxuiONZK7858VjdD-MgA6Ede_yoASGAPS1L5IIfG_UschsOIHr2kHrPp5CTsuzEA63daeVDlbjYVDVnJ59nG4JM1HdCKsNrlVDiDsGzRDOTf0SWdv8hI6--dpqL_ZKbITUR6q2KO-_5YqSbq4uC2JR-QTOGdea9OVknB8qF0X5sACL--54wgAH6w71NW8xxrXNiGkM_AGQcQ5_FaDRqHdVNke25WErCtIOCYwqxqXx9BK4ULtCTbmYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یه جا به بعد جدی جدی داره تمام تلاشش رو می‌کنه شت پست تولید کنه:
ویکتوریا کواتس از بنیاد هریتیج کاملاً فوق‌العاده است! ممنون ویکتوریا. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77910" target="_blank">📅 00:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=p-ICidqm_92Y43qL1P4Ef1OsZLc3ylKKuqSULxbnvTApDKbuVs_KxPVgeqpWN-U5MM0fEJEG7uOPXQ6Xdzl5e3l76yQwom_0Xq8ua-UDCq0YpwZi2H_XMZKzoCoQWv7_xrdCp8SmZlTIK87LNMGGrvW9m6WSE_lhA3dK-gjo79MNIjAD2p83nG1F2lJy-KjtUO9KTvqpAusOF4XzW6T_jy_oNDnfMSx-zmeVWekXd851OOJhegf5Xqi_3XS9NFxvo50iaXHEXImts-4whs952w8s4mHiFUUHFINWCOjtrcP-kzVgs93pZ9olqdpyME7aCUYTPLy4cDCMLhNjNUyQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=p-ICidqm_92Y43qL1P4Ef1OsZLc3ylKKuqSULxbnvTApDKbuVs_KxPVgeqpWN-U5MM0fEJEG7uOPXQ6Xdzl5e3l76yQwom_0Xq8ua-UDCq0YpwZi2H_XMZKzoCoQWv7_xrdCp8SmZlTIK87LNMGGrvW9m6WSE_lhA3dK-gjo79MNIjAD2p83nG1F2lJy-KjtUO9KTvqpAusOF4XzW6T_jy_oNDnfMSx-zmeVWekXd851OOJhegf5Xqi_3XS9NFxvo50iaXHEXImts-4whs952w8s4mHiFUUHFINWCOjtrcP-kzVgs93pZ9olqdpyME7aCUYTPLy4cDCMLhNjNUyQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش بسیار تند باقرشاه به بعضی کارشکنی‌های بعضی افراد در مسیر مثبت و سازنده‌ی مذاکرات.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77909" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آدم شخصیت و استایل مربی ژاپن رو میبینه عشق میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77908" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کی قراره چنلای فوتبالی تلگرام فارسی از گذاشتن عکس ممه های طرفدارا تیما با کپشن "کاش فلان تیم قهرمان شه" یا "من دیگه طرفدار فلان تیمم" دست بکشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77906" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ویویویویوی و عجب دنیایی شده پسر کانال ۱۲ اسرائیل: یک مقام ایرانی اعلام کرد که دونالد ترامپ به ایران پیشنهاد پول در ازای سکوت درباره حمله به بیروت داده است. ایران آن را رد کرده و گفت ما خیلی زود پاسخ خواهیم داد.  مقامات ایرانی همچنین تأکید کردند که «ما برعکس…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77905" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مگه قرار نبود امروز توافق امضا کنن؟
چیشد پس؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77904" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_Qdi51hkMDD8NKyDl-d0hHOK7CEeKsr67wSzmNRC9NZ6e81MpUlNEBctKHnCLeNkfJeA6Z7ve7UbM-jfOX1SErv4_w3icjeWiyTRJgcraUnFtv1tlfWoX6cdjK6t9_7R75jQXv1Znwxs-zR9fLKgfiBYxYAOFCnBDluym_67qyFJEVEJSibcxk0SQHNh6lSCx9yGn7NRKLPGP1Niko-aYT0mlH-gTTExzfJLBSOzLUNvgQOqRGLufwVGUN1SV5_hiULbl5jMji6fDczUO0_esdWZMc7BCDAEm_StgLKqbVMMEKgXWieZlBs9A_nW0vNK1OzSkcP2wB4oCFVgaeZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77903" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmpe-FpgV2giDkoL3_0Yj_IwTGB3JmNk6uhjtI9PfT2zMicr0igQMzDNEGx5aFytxsSD1c3tYtgBK6EOamJQoj8irewsXk5smVMM50NkfepSOTQZTZFUsU2JwON2tsqedEMQSWLNfpFUWovkBKzIvE6NlBJP_UcEpCOdD_LWqVWpwmE-7pdlwLsCyQzea0l3gurQv3gLlgz8s1v1ZUcsBnXU3SgKEyVnxcOLvLbip38RPn5Hbr3bbKdygyogPI-M1Px_RjnE7vNn9CN34LRn-bUL9H_9Cj_nmM_lBqSTcpW3cOxgxgqT9RoWp7JUR6DEhvttIjYfnBMG9OgiOaOBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77902" target="_blank">📅 23:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس در گفتگویی عمیق و تخصصی با شبکه خبر:
هدف اصلی این نظام نابودی رژیم صهیونیستی تا زودتر از 15 سال آینده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77901" target="_blank">📅 22:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRiQ2Th57cm6gBHmMz0HPXxVGL0cjTj3pGK-i7-_fpUkLlJK1ZC_48zFbyzLig_n5wK0gr5-9eY1KnSvnXVLa4xO0ubxBJW_6TMphWfZPo8mB51_Wj7i8gneHO9CE_iqikI9izFBNYosbMO1-74T7nQbQRGrIHsne26XtVLx6zXbP5gwWn1PsRvmdk3Xa2KhhuIQoyohq3Sqg7Y6CZ1Q8r-Lw0sqRy6DsrE4Wcwy6A8Ciq44aMKJKvcYKOant9ooE66IUHMb7KyNG6X_rY1hLA8kTw-jtWgI0e5wr2EnWXu9Wgt2lCCoe2fTOGb1fuzfwLgp6SqoNs8RR9dzSLJOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه عصبانیه:
آنها هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛
مجاهدت‌های رزمندگان غیور لبنان و
دیپلماسی مقتدرانه جمهوری اسلامی ایران، حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند
و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد،
بچرخ تا بچرخیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77900" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هفتمی هم زدن  فشار بخور برزیل فن  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77899" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">همچین تیمای تخمیی اومدن جام جهانی بعد ژنرال معتقده که تورنمت سخت تر شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77898" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هفتمی هم زدن
فشار بخور برزیل فن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77897" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
