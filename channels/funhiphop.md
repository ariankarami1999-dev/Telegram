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
<img src="https://cdn4.telesco.pe/file/HfJSe5UwFFZCVarDNV4cpzw61oFwxuhTFwli7f7-ySw-nr3JxE3ZFo_TqCwp8xTwdv7wFIvEVbrFe-Ja3-pQltjwFHhEEkrpde7phhDhm2aWcqRtnRRSTJjoQcnUmZ9p4jfV2w2bAf5lZ_WAhpujYwZ9vhpvB0Cv0UKHt3TWsJDA3LJiG8VZ-g6rAoQ5ZnPp05fv4mrXrfjNXvRI96Y4K-4VuuAu0CcmbLhZPPCR73GYTdFjBwgWSVElPig96_LljM3K2FDBglrE5XycboJEEnifvRPxGIf4ahhiZIc2JgJIhz0o3YS8DEzT9JHf0jIIeb0c3ylQ3pJqeS3sLhTcHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 465 · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cer73tiG828SWX6Z9reWj6DNE_4IS3bpz13lkNpCTgm9RBHmH5ljlKM0lLWYtg5Slnwzf4RRB_uF9hK-u9NAMrfYo7eZ_waqsLF1fHoWQI_7QQrU2L2whgmD4uKRxp2GxcCepHAp90lgi3EMn7dBF9NMEbQug0tliLP1ZMrT5qhJ-FwgGx-j6CyuZLZ6Cn1auy7EaDxFhrd49kx5kTWTV0a4bXMdkc-nWcd5Q2Qyi5s3HG8kxGi_pRzYWHAC6m5Pox8dL60TLoj-5cGxhMOCfWdKKmYRB5V3MPm7XMdvvg5_n9gBbyRGk93ImyaHU8A_x-pngJIIbX60FEYGwr6cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjM11XoqbphBZ0LMd4TFLX8tiAK6zlwip64KM51_PUyKOqkbN-gTOhyxJzzv2VNEE2CY8MWVaeorNie_DMrpzoD3jYvI0AqnWYiQwT7esBJRUZMMTNlLO3LgyCHnMkk45CVzsJB8sR7oVz6wblVZE_8fbFJLGMFZsFOy8hH4BjEdlELwkrNlW9Ts1ktFd5Q3zyrgf7DUKN0M-TEUa34aVV9a1XJ8AzzkkhM3TdyVQLLYaa0AHmAwYWIH5gEGlzXYKOu3aNPLSTinUQVoTK2I33d23RfDd3EOPephuUDtSJuzmKpp_kKoCwFHEIT3cpJdlUds1HhIJAkP78rLQdCUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKcMjSOWELu3KToDWF8XV7WfGpFFrvdL4U0An2UvyB6xaL4xv0BrDF2LhGJ0wla4Aawf2oPs6DFx4Q9tyMRppNdYNn6asiHU0qcySOcb3nhRgR24QFbsVi1FqgLe_dQNGMEYDQUYoR-CT6iStIx4P_smrjr_SHv5r3wRWyRk8dQ_yQE0J2nmD1SC0ryg_hVyNxQzqRb9N90jG8FDElKl3nycV9-Hj-VllWB3BpVhE_Q297W-hlnGLEajbNma9uZjB-6miDTYgbqLaSCefbRbyI2EIi6qEsFZ1hq0rcoVrl7ymaS5qI0R4rT7uKQRRKAhDo0203N55ma47BsFjHde_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJ2fwuu3JO8ywWyEZnpp-U_yNW2jMHKeFW1_KZhFywzte7hWz1Aw-DHvzoX5hd0SnKNbx47da7NP3Rik7EIMHcR2hU2Tjd55lp5sMneRg-lwRGsEaP0GwCPgB1MO-i9Tom-RZKbvZjHiwi_7TyzJ1RS-TfWqfJ8ukIoxvKfHxnBP2PZH5TNujH7fTS-s1pDo-b5P1Ifh75Ij8fc3wZP1-8TqwsYVZ5uODu76G8cBhjIrjHKxtbNtcdS3veze6-Hyfqb7b7BXImag_iN89wppH13f-zhAc4SyuW2VZNSdA-VK-efkc3ZIWjDJRcCnHfPKDhEpcGY02YgmctaPfb51tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82899">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HOkodQfAiX9gORq-KGyhHXKkQGKslLn1pEDIiFZ7ObcjKbi9kdU_Wjb_wV84orM40SGtowZMO5zkyXZ1dE5jJY53UWk_0GpT4iXRhigONwV3vuyTCiYZNi3vUHe8pHIiVPitIqansqZ4TddirL5BfRduedGqoB_NTsp3eT4lyUE2jZQo_DvuaScHAJOLGumDneTRc8T1LyCU_WKTahkg4hqkmS8MWsGLAsAL4Kwfot_fRxN_Ckb98XKK7EOrwgq8QVq1HDDlNjir6qFhMd_sK6FX2RsU7ygQsbnRRY1X7YHkmB1SL-nXNxQiar81Dnv2vCcQi6fR6t_vPWB7bl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g11
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/82899" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtK7NTtI8JknMvEsaLqAxf4wIQJWi5agi-MBv8vvpyU2I2KYXmXvohkbBaHAWsimM6dQ8LrEY7iQt39TsRcnvomiW4_R6PniyZzcPxKyFU_auOX2hi9SL7778F15qBIzZON0hvypyVylcw3XttjYhoHceeR_4g-NRtccrbAu-rd8Hf0AFF1VLUQ1bPZotQsIpX2oBzSU2kV8nUu6Xokx_1nnSquwoBze0fofAg67FYjwbsDED2yNkORJkFznFUZ_plWuXQTwjetW9G_nWZJe8068IGTQ7rVjRiFr4iBCQa_waGLzVWJgGnO8SC9hVvAtzdhg3VAnOfCD5an82Ft47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0kuqz6LcTpvM5s9eWRqYlZ7JP5tFlAXU1v4kue2aO5bBMA3-4Gf1u8n4G5Loff-jF7b-Wj71pyimc-oI5ehxsJP2S3U7cfNe6fCz0oINtUoQaHFnt0tdhiO1QpT7HrijP0kFK0OJGq566WRBGHAbYZEc5lMsjulHrTDXl02U1lhc_1Jyg_vvhKWWnWiKBE7t9de2Bh5j_Jt1A_Jrnd8Pw8wqkAOUCz55UAkad4XdAIJBnPTn6KkXokyJ7t0dFxkGOTVILEo6RdMzvltPtwoI607Ms6PWyCsD_Hwq1TgPC2GfPIN3E9v1qiWuqjLQiFm7VxhlmY6584gvHxzQpD5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcAIV_6lMNGqYyzO1RkPeU3EjcpwI4nMNM8Qry6fQSm1DUTqqj5tZLZjEQU-3qp8LUy23i_nBj1cOEjhjebFchQQ3AnZrQD_rN3J8wafwXU-lbdL50YeSp2JYMoYgU7rI5NqD8hqq2k1DHoLqV50a42mlsIDCwpJiXZLTWIossJJl-5RhyXmaW6kNpQwe10d3ni1XpnvfIw9iaOjhhaOJ3qV8wEGVdwPxUVX_gbRHKc4nNVSkmx-ez6gUBKBVW-0MBhnm0KhYrUxVlu93sw7s8kN4gsUx4s28QF-91FToTWf1SJ-Lm6oqAY0UxAWzsOaFt5zAkem3VZe296T6VyoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82884">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_OPnlf0_jBb6OoBQ-vpReKOujOxHdZ_yccqDpcv6Sgl3Hra1TG_H5zEVj0GUD6nVHhQIRe8opePjF0lci-w1z_zzHeMD8N93UUUfNOidkcjP69S5zl_lRdbPhgKOOtoi0-1P50Fnwv5U51FbRdbjfV7OI9lgXpUwFgl4q84qOmiMhyweiuRL6ZK3sHh-QdPMMc6FGdXCK5H6xvnWWSyJMoKMn5n4jgshHe1mEhpzmVmb4fdPmdBpka4f8eujBW6-1-U9PxEpnizfw9ATJCzIPydqfkwKpoZh6XL3R0rE7q8Sj7J36C1JMQYFfVaXMQhQH8W036Vth8nlVyRPhEOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82884" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQgBw1iFDkjguk0LeuYrMSVlm1dGbbqA2WNkmKO38hOT2o_IE2QuOKF1SOaFkYaOQq4kIkefLv-Roe5UJiC0xLJp3Op_bHovVTvzNfgfinvtM5cIkN0Yg8h4fmyF5ltv50G7uJVQAiVns2o452XNRooUvpg02RCNoj-FLAzFxtzz_IylsR3cH8EXPmP8bj5BrHj_KRW9mSsSQ_ROZ4K6MVb1j2NVowjPAkeC0qOLENVnpZvBp3cZfN1X4ZBh-qRBoOxfWN4WSFf9aT2lCmcOeU_TWttHcYil_x7A2U6dqMDqWljHNmAKTJhpXA67fr-nax0X5oUISm4VfVejG04MOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaYTX-CIuf_P_CYMf4ts_xJdqoR6uuQWP8uv_G95JLmy_Fh3_eW0wkNpJc32RUC0EE8vqtOWtjgJVmqNjw7Xmcs92w4noXmJJRRPdLxOR48YSTPcBMhmtUPwWFV-f3F9lT40aNLzumdr4HY_RCKOIdleQlOFITLrOELvGD7a6x0DjRfUtDvlCTvkmxxW63XHHmZB-oqZpFHc4CEL2AgYG8II4aQzWX_vs0McgGxxTDSzpanhwpQqpwvv91LVggWCJThViIem42nIIhO2IrhBvCBC1as4BUsydShjCzymKvBHkIM59HHtU5GngjKsRqJMmWY7WhBq2h2cmfBVWUsNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH_CZVFst_mEVxpQiVyEgVYenwR8JflZuTZqm5SIayQnuOXn8yKuG81mqfkGiVXBmMNozvsWU4MaeTy9CoajvA35IBwxaxlNz4sgxEkfO63iLgOXFX4aAD9qX_w0lN_XNFVsNAmD8PtD5CZaZ4MaKgRBrv_gvjaHiJZcFIedb8WD6lufbTOkoLKpsyl0F91DmcvQnfO1s9irZYTAxslVB6iW14oHb2p_5AUE7hHWuAEIyKxIgGDAfQ2mv7_YaLqKtOgUx6_MvdtfWtQD-Od6JjewgQiBRICprCJXxZtOqjfPqIbSAsBrHYHpsSDKmHF9N0zoZxo5e15jOBdIIo13SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn5k3-aIGKPTSuZusKE6xRMbxPG5vLahUm9gcbBXsU-sIRQOLeKuZ68ts_HYEFyXPVuz3uPaSsPkSxduj_vxqH50EaY6Fqq2G_Xw_QO2DgieKnrZTmLHASQkYjSzZgmTnzxfZQVIfv_xqaad7Vh4m0im_Td61AlZVMlYuskZCOk60mWUmHOn08QJlcL-fz8LpWEc99rZgRoWHsCrcYogEGPb9HUfwrRZfI9JyyXKyKBbDZPZEtqR3NiIhYO53OwU1tN8of-IzCVctMM9csi84uVr7Oy__jFw2S644MLNeczT3D3vLQqaxveKyt_hb6Qj3CNHAup6_Nvjz-2XcP7Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj3kzBp9x3y0PFXVC41w62Xnw4RctO3xT0FElyKmB2uvPJkWu7dEUuHAArQDCj9wgi6IXNz6Eoxvd7fRlLFRRmmATsf-2f3x1zAw3HLqQcDx8H-QMQGD3OXml2xZvGkNBylISJXs_VZ30hg0jRMw8f1PvdXvkTeJMwpHP41JKJvKTJrsCUTbODHez1CC9RaohPZHhSOdMqk0mTuNg-RwFKqifmL7l1Sz8Z9Z6BO_64Cb9wpvi5TJxDLUQvcMM8f0Y4_482RJdCP7fmtU6JQQI2i75i1Lzw7ILEPlK6eHaINYjAfkTH5f6r5gNmJ1kDXCBW8FwgXBAq8QqehAHczO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGyT88C2Yn6T99BCnma3TPOqQSUrapoLSldg9uFsPmvH5VDrus3AZR2LuSLimq92wN9ZkXhKEBMqnUeqEaYp7a2ep_5PPOJmT3_fSNsM0q-dk6w26i68_mjNOCI50BLSCQ0fxjGla1GU1p7VkbwX0CE8G-SePDWiRkLzgajUw8QIQLrMs1JyxVDkhDtTGcQy_QR-NR0LOz7ir2kzX26tlT3QJy3nXcSd0LHSlxoadYyev_VhpuEQ56sYPBPqdlNk1A0ImMCQ4GG9LyNcse5wewk_iHFfE6Bu-DLEbYvk8cYDkyD45oWuyGrrgeC3yP3SwTLNCIZhZyPybakJ76oIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگید چرا دیگه به سجاد شاهی فحش نمیدی، دلیلش:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGfPG86Zn5tq0IgSAQIBpVeWpaa0uYkZl07jAh1Do-HE-8fRGiL2r7XS0x7MuXNwVDaJMcwac83dRWfO43D8dvkIKTb_TQlX1WCO6kCFo88ASeTsVNFV1By3QgKp09OfvqPOVYp6UVFvVjQQXafqAsMRIaEa4rZVpKZW61CQLAAa6YVXDAFBuauw-YrO7nVV6aZsfePRaYKEOrshMK2nroq9LxBl8fkZlQGeWIiiouL-z5SkVI6E-qhLfLueyMY_MLSBdjFUpPm8m8sGTO85eg21K698lHmtz15C0Lu9V4GhEqcZgczS_3WqxUbXK8b45T5cDhH8cln8E01tjrpiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82863" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwbxszkUBhUEjuuhtRnHSDm8Rvs--K8-GbiVGBa9GUeunkj-kjfZbNgEpKO7dnNauz1Ueyxm6OEIh5zcNpz_62fujrBbgFFwsAQuFt-EtO3C5phewyELohbL9lFyl1nlvkk-4uxocJOZPWn-5nZwvMTJBbk2ayLv1-IcFHZuCmj1dHvjBO9O33xa9u8QLhp1yT2l4VADiTxCr9bJ_iJ13RAvkPfyo-dWg0Ip2ryDZNPwPei-CinKQ66fvxb_pV78QBUIE86z9W887pIwkE5iMcVez5bN4-_7Epb4jcHvNYBn_t72ffwasF3qGzrZfYh6g-h9cPlfNe8qHhvKbkoQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTzt2T3ksufFN9KKBYU9YQOHguXmngNC9kWwSNc4QoKYncIw5qECPwOyE4EArZVbVxOxRO7YndG0kJ0QT9kFvQS39hBLWk5fNHyCWSKLK7MZ99mIjh7i8CA6cBe26yUfBNE2LkNaZDX9Ybnvo9tL08iS-dJLbMRmOnoUltwaJbVrNO9A3O_mV1janNpwFdAptt8ig8BrbQiXJGwcBiO0DFKfl0ZsVlksRXW6zTfFke6_25bJEesnNhkAz9SYYc2AUio-EEeh3DCbp8V0QC_mUupygc21_f-hC9nI4rp8YyyLXwwhScU791AEwpdSg90tgTIUw_vlLcN6pc5L-GldtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxX5M9ea-NAvFEjXNlV7iRAKfH6c2QLL6uqdcz7LKBRZPw4ZhNjWe4bN4gigU7JiVRECynDcLyWGLOT-zgW3hWDXLMqNvg4VRns4QCfFF1n02testYPy6ECkmgzEVqtWemo9Sm1y2wwckTqpHahRm82C4-ZmybvmKU2001nZckrGN2jIXYOzx19z8ixOVfrYC91fK4iQbYjt5ICusCX4Mt8TOzUrMA-ImL71H8qKqWPg13Y6yBYBE6V0p-H9_4rO1SwylH3xgpqClyliIx_Gys6X_XWVZ3Bs388VJZC5wpkfob8zHQtE9NysHdk5DWNwv3mTEiq0pNpZKA6WX3f2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان چون این روزا قمیت دلار لحظه‌ای میره بالا و شما هم که دیگه براتون مهم نیست چون سِر شدید، هر ۱۰ هزار تومن افزایش اعلام قیمت جدید میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82856" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82855">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f513feec.mp4?token=ABNtYVA7Z_JiZHl-rIb0jbuHi55T-6iu0aTx08MzuY12Uhdi9aJ_M8Vp9V6TYrbNGzsoRkgAJ5S1CSirfXU80lcFv5utXYru7n0IDiclBQByqfZqM18Olzn9oO7E21njaC7XKZH1SfK-wunL4tQL4VEruo7Q1x54PnS5jb8cpvumNL1GhvonvuGu5d9rS33609l5tiQHrOIhMy_IbU1Ct7QWvn3M3w_rGguuDYhksWmKOCOK_pFh_05DrGziILCB0kftw516GAtiYWK2MAbGUSchSoRvvMnDg1eACbd9EMD6M5L3YtjU_xohXQ8vofTbH9356Z9UflI7Dg5H9IY3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f513feec.mp4?token=ABNtYVA7Z_JiZHl-rIb0jbuHi55T-6iu0aTx08MzuY12Uhdi9aJ_M8Vp9V6TYrbNGzsoRkgAJ5S1CSirfXU80lcFv5utXYru7n0IDiclBQByqfZqM18Olzn9oO7E21njaC7XKZH1SfK-wunL4tQL4VEruo7Q1x54PnS5jb8cpvumNL1GhvonvuGu5d9rS33609l5tiQHrOIhMy_IbU1Ct7QWvn3M3w_rGguuDYhksWmKOCOK_pFh_05DrGziILCB0kftw516GAtiYWK2MAbGUSchSoRvvMnDg1eACbd9EMD6M5L3YtjU_xohXQ8vofTbH9356Z9UflI7Dg5H9IY3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکار رو یادشونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82855" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82854">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به طور خیلی طبیعی یکی از دیگه مقامات نظامی آمریکا که میانه رو بود به دلیل اختلاف نظر با هگست که تندرو تره استعفا داد(اصلا هم مجبورش نکردن)
این استعفا ها قبل از شروع جنگ ۴۰روزه هم اتفاق افتاده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82854" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82853">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu5A1_RYtW0rsRSl4kFovTRK2mTIGPhGh9N3gMhDSlZWlcw6zAocLlytSpgkO7rDAU0Yumk46sC_ZRUK50m6T0f2PVOX4Knb7T3H2-0OHiCJrJjTv3vL7yRj-X_IMJe3_w95m7wv5D95XJ4dk7hPfzi0aGbUuaEoVpfYWY66Mbz1vBhleXEei314hXaPbZczPbXw5cFyWugDNmOloQkSPFYbthDhuzoBeHwEs6uUBTWuTW4O-Eef4A39cYymbwfs_6EFPTnxW6CCcPdtiWNoSBxDt5ezTDtiRkvLJKIQuP7J5pfUw8p4zvOokCJcFD204_clM5anCtJL0SIWHFM8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82853" target="_blank">📅 14:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82852">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=b_K48OvUl5ADaWircEN7_OL37v33oT0GUuMlLe_BWIeoaa14ax4V_JJKrZdYaZdCl-aul2B7E6YU8sIjmwPWoPwfJlhzcQKUjVv-TazkkQIFJcCosKF1XgBe8VfV4QZeIkIK19r16l_6-LJfdFzG-DD_zvX5fVwyHd5IcPvrwTuPXuz7t6m4RSkOL5At0dJsm-N18r-dWZ08Ffzm9vUhvUNSDJuV7Y4bFUvBe10tOSWJQN7zoG7tY1INRjCvVpZaZ4jfdWaEeleiNWAwY2pbweitStukp7pNUYlmle7zz2i9b6vgn8NhKeca8U-dw367ILmHv9Hr1wkQcQTYnuMvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=b_K48OvUl5ADaWircEN7_OL37v33oT0GUuMlLe_BWIeoaa14ax4V_JJKrZdYaZdCl-aul2B7E6YU8sIjmwPWoPwfJlhzcQKUjVv-TazkkQIFJcCosKF1XgBe8VfV4QZeIkIK19r16l_6-LJfdFzG-DD_zvX5fVwyHd5IcPvrwTuPXuz7t6m4RSkOL5At0dJsm-N18r-dWZ08Ffzm9vUhvUNSDJuV7Y4bFUvBe10tOSWJQN7zoG7tY1INRjCvVpZaZ4jfdWaEeleiNWAwY2pbweitStukp7pNUYlmle7zz2i9b6vgn8NhKeca8U-dw367ILmHv9Hr1wkQcQTYnuMvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده خدا در پاکستان داشته خودروی بدون راننده‌ای رو که خودش توسعه داده آزمایش می‌کرده که با ماشین پلیس تصادف میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82852" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82851">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82851" target="_blank">📅 14:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82850">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82850" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82849">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOR4D67UYmHH7eLvT8EqPfy2KxRhrhsANU7gKHpvnKMjZ3dq2IJtEOzRI6j7kp3ziCNFSciuOVBjyktK-h0prDyr6Sv99xDx-WP5_eXw_XWiteSnyChat1p9gEN7vMqvmnfg7odggRH5QSZJJHi1ynmBhzcy8noDwN4_Uqjby3u_bXP7lA4_zbOkqcsK73Jtt-8ulEvau6_l3inpUGBTo6oRoKbyZmSJTrrCKexQmkSIfeCE4yrD3UiEyzNh2pxjm-cyQp7wXXAmQfpiWJD37cH7R9ac1y31OVN_Prv6nPHmrWXstvOoc_mRFq98sxDyUfmgoCSr_RB0galuHmvzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82849" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82848">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ69DU6PPXS8Du9ZAOifGzpDDshngAtNf3UYJuwd7JbEyquVZF8hjoYwnSLx_ZaKsd2rFHMZuhexiTonREPePvnIQXmNwuaq6xVBT7yDRD9cotQWrUGmcj5oZ_kzJ7Tyf4-PPw4xZzhKgjIyBvHcsO1WOl4y8gfyj0Lh2i93CD6x-l9BRJ7htTnBqgNMoytac70Ui5FY1Jsin6EDBNIg2GeBmOvR_WqBFxDdaLk69vjzmZ9hrPoxj26SoVrLqm2W0lsuUGOJNPIB939XMUWm_SDLsJXObmtzkwiviWlG0qeFbod51fiWN1P_kyP-axcKyitVZAjSjbUd41VVT_iuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من جای نخست‌وزیر کانادا بودم بعد از این توییت کل نیروهای نظامی کانادا رو منحل می‌کردم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82848" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=AR8d9vP2iHnPKJ4zUVHNeegDhFnaIuT0H0qyQkg3FALKMoe291WpOj9-2Etwh0yAKHFGMr5BIkfU9Ism-YKk2YVVlRr4_n6zxQvLULZ7Z2I0rOd_Bz_pwfsUGMYwgSSj9v2f7xFKHsEu-TFMYTMC2Wcr-4S93LKvlBPcoZfAZ61IdXnfXnkkJJRaYo7XvAER74lB2r0tlpDV0cPMDUAUgwzk67tQoRK34VOwjrjBsZLUGeHy-ISfns2DWQ6jma0GY0yZyEcalalbHhglpXEZgNkHRY6VdkAE8fK39QSLe4_N3ksFXW4xwnSpLkopcQK56g_UHvef6wIXV9wNW8TX_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=AR8d9vP2iHnPKJ4zUVHNeegDhFnaIuT0H0qyQkg3FALKMoe291WpOj9-2Etwh0yAKHFGMr5BIkfU9Ism-YKk2YVVlRr4_n6zxQvLULZ7Z2I0rOd_Bz_pwfsUGMYwgSSj9v2f7xFKHsEu-TFMYTMC2Wcr-4S93LKvlBPcoZfAZ61IdXnfXnkkJJRaYo7XvAER74lB2r0tlpDV0cPMDUAUgwzk67tQoRK34VOwjrjBsZLUGeHy-ISfns2DWQ6jma0GY0yZyEcalalbHhglpXEZgNkHRY6VdkAE8fK39QSLe4_N3ksFXW4xwnSpLkopcQK56g_UHvef6wIXV9wNW8TX_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری اعتراضی سنگین جهان پهلوان هادی چوپان در واکنش به حذف شدن از مسابقه ناعادلانه دشمنان و ناملایمتی مردم کوفه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82847" target="_blank">📅 12:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi13Jyv5bS_2oXcwQu5nPgx7eL33tAAIPDMUpNg0W8um8-ChRHQPuttBi5bHDHNCTVpP4J5hz7fxADBRlnLkk-D3HbgtKEj71opkOr4D24jpcGOb3lspAcq0QHxViAoS9ZzVPQfPDJYlq_E-SjKZFNrckaHAs_RkxBVuLRfQvp09iah1HFiwiyTF673JYwuEcTh6PYlbUew70dAw2dCkv1T5dIpLclDaCsP5E6OdxNe10qN88ywxgTl4w-cZy7e5rTKUD-_ATkh4naWYSMvnSsMBMSxdd9Nl-HJ1eEr6Q_-D6n9U28QOdVxYbIa7uhkirwsRnwVttAuny6j42wSctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhS3SPUEMUvBlEv78mUwXOeLXsoqpGKKXJXFxL3vax-bemn-SynLTfckTI2Yt2zNlC2sBD6nzApKsBliA9mAEx59GEfDn-KZXkkOBq1T2nZcx0OU2R6lUR3M4vWEWw3dJl3OySUAv8aC6234fjis7f-Sh1j6eeIg14lRRn3r99VPSlOTwLEjLy5uBqkRlMNADGGkvEE9V_oyhdaH3RE8d-mV31lZiGYTU2k5kPI4bEmjbNo8gh8xhBxChrIWTrcfyYNfmptkI1-E0x6MLW1EF03BuaSIq74c6nNUHAGamCIno9ESnHH04qTwCQkuGJlQhljoarE5UlvGlCt8WOiaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82841">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhawUKIKLB697h3TzRayDbTaQT7HCrcqvxm1oP9cgKOBNlNxaGttyYFdlpia00_zflk_aLWqCyUtYMrqBvbEZZj1NkWlol-_HFu6u5ja5PUSt-q4Ufw-_b-XYGz5h6WEyyNsnyRYkCMTfc57gg8WhjNXRdogz7LZtu8wZBiKVAz21RNQTeVbBvXJgDsitx7H6Ji-fqnfpue-bhm2x6dTQunP0wT4jaaJPzbzpy_qAUpPdBmAYHc_aT2944Vavk4NsSVVa2HiQVdvTTai00spX7_RfnxFmxojawXVoLkG-9VqqTj0DFfF3A-IDfwxEIn2ew_YA0eIp0O8OzKMlW8WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه ام اومد تو گلوم</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82841" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82840">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUCOWZtLgt58Xhmi179qS9J8FPygrMb4C8NW7aqEw0TIXDuuryHXP516U2WEjGOaXaBb94GPncC3ctcYaHpVx3_AY8T02W9Zwp5hVs7JeJWdWVYe4lHgOEMEVbawNGo7ErMUd2JfUshbBepZBuAPlDadhet6hemNCujsezF81bnv1rEXNERF5GlMcFciqceabc6rJK4dokxJUIjOFhasPYZSkCiFgNUYpS3EMFK6_-CRXc3eiNHDK-1kNm9UurZFMmPllb9tuQBCIuN-RtRLbO1P6ioMAn1bk75hriDAmqoOuN6A8LoInpIVTCzRBGNi8wHiHCT6qa1OHwmkz01ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشه یه نفر بتونه انقدر اشتباه کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82840" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82839">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNdlI8aNVk8cBxOQU635xW51kIsP6HbZWb-7vBm2tw1LI8jMytX7D4fQtnhEaJ21ZjiGzy4d5UTWpc479eBW0DyinpNMSHxHeJQfPR-IUhc7-edP2I4V_IgubddYlit6a8OaJgA2tt2_ht0k2s0CFQScHDWneA3retWWPmOoN1cGKYET3Y2LL1PFOkK0Q7c4xAjJ4fuYY7Z32rx7-AuGV5mrCAuY0InROKZkTrtfYHTIUizJxEfoTFiJRrG3KdmWUQPuU5P4WQtMc5fGPh6X_9mUTTDYWJ8QlCgeDo_hVKoIGzmySCRcjoSuvchHonvRHVVVE-AeJYnQbujGw0Y-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این چیزا جی تی ای رو پی سی قراره دیر بیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82839" target="_blank">📅 23:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82838">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پزشکیان در واکنش به تذکر رعایت پروتکل‌: بابا ول کن پروتکل رو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82838" target="_blank">📅 22:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پدافند جمهوری اسلامی یک فروند موشک به سمت جنگنده F-35 شلیک کرد، اما موشک توسط جنگنده دفع شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82837" target="_blank">📅 22:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcz-LGuc6xu2WZ0Qk4Nvjz8-tobnk9ELCQ4VQvnSxCOBCD85UN-rh0j_sS5q1pWG1rren5Bkm-GIVEvTk8lkrajRCiNktNcK2x94r6jcmjZYtkIreSdxrCJ6_6R2tKV2Jxii_nQlSqB7WcSl4MW6Exw63w8_h1IyLhOGucrjvP-lBOeCBmGmSYIJnGT-3u2tHcBjEbps906Xh62v0k-I9UuQgqZQlIVKiV6hkKuZykxpsBG4d3MZgrDMXTpSs2Fazpcw6vWDdnm0iaaYtIBGYPD3JK2UtHSpiO93jqnP5bcPsdFLimquv_LU10oYr8I8WBOc9GBfmhzSbWPytQhXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بیا تو چنلش بگو دکی پولمو بده بخندیم یکم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82836" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ گفته میخواد امشب جنوب رو بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82835" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVxF8fuXZJSOuf3JWbqijz4JCPtKmMh9Z_DekcrMXUFJlrJNiuufxzKLInjBLUQIQLvZX4Wd84MsVu3PS2hn6dI88gCgP1VOcCwV5Lb0LBmmmK044tE1p6YIEd95CgaO-YV_j9N1I569xYPr-1zpiFAOaa0HjazZGTB3ZDfSJ0ML0YtUO71RrGwhE5wvDcQMeLSjRMwRFDbuJWvDqwHXDM4ABWfQIDajF3FRqwkxVl5YlOXxUfvjebitZ-f6vmBRDk1tGZRbZL5ze6a0fCOK_TZLeH9PGyOEzMao1CXMhOzz2Iw8Rsv4OMkjx379NWkwO7uRGQfcalCPAD4ozhe5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82834" target="_blank">📅 20:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82833" target="_blank">📅 19:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دالر ۲۱۳
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82832" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WChoGL-uu2xT1GI7-Nxi27ouJbjGl_CfhuhvwO8FFqWx96wJN7yZt-dmdqDl65Yp6pcGiFzjN3Lt9DvgYRVFXYtDp00hckstO-dkqpLjwKd6zuqlG43jHtT3wWFYpZMn_Qir0GLjgPAYPE8_7mc2WiqBjBfcrilvzgelFwprHheqbrUMrQYPfY6bBbrQt6XET5l6EdEEyibmFw3pfmZBqLkbvnHA4f-DwoaWME97TroDyrWsRkrvuA1qBxbkAEgo1RBIg0QX2bRVpAV6AZyBjSl87vfEYXq815XsUqwDhYi9iKobXBkH_SV3NaooOa_VHQfMJA2WzFX16oilu2d7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82831" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QASYWndNs71D_GH2X0bG8N9DcJB7AmMdO_STtbh34iCu-gQ3OCIqL2RAWaFslstQwtybaz_VOLEGhVEZJevPMUWhio9Xb41PkDr0-FzGZtgr_via8P8Zi5oOenOpPIAQo0UWBtg7u17olKvhEgAZP0s53Y0KfyVTRlY_pYIvPo6E8NFeB7_z3YqVyhhxq46Csok4ImKIhvIRLbeqe2t18-7H9f1txV7MOZgkhp9wWRMwVzf93uv1Z25P3_wEf4W61HSjS_DnqMaSj9E8FyGLprtYtyc444SWm84me9RG5B3sNhAQYqH-e6g8MaJybkPFLi97m-cNeymhqCrMkjtsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخندم و رد میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82830" target="_blank">📅 18:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82829">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82829" target="_blank">📅 18:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82828" target="_blank">📅 18:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82827">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=B_5--ySinrKfShbkmArNHUZGXzR76vbsebBfkxAnikFdNTZoXVhwBJWBMBObyHJLMZOjle1wZG1C6eaBNwcuhCosPFtM7HDYDcm6jcqCTxtkmB5zHMpMeFJEDScLbfWGfX-oIgJFeQGxOha85wLHnPje_4oBuMLurVC4y61i3-HIhX_7I0CQGNil1kP7zxYdZJuGFhDsabMVKb1D5fx3hCP8qw2DoqqVTinNUD85t25sDagnqKzhHDxz1lxNnxq9rCBOQkfwH9jU2DbY214Qsk4X-GUcFOjUquWpKA50TCsjED1C8SB1xl7Iyo5mBUme0FVnuhEX517CRXs36I8dF7r0oGoYG05zQ_Ln1A02WD0lJCuRWlIbb8bEr5bnV01XAupvRDxTgVppXDGDFV4OfvZwWXWITuYa1UOXUkFj6BwF4oiLyztRCfIB20pxUd0C_nAKrpPyts1Deb35GKE7pR24f9k_0frLScXIEhT3x6kq9ofYh_PN7aQq9dkqDzGmUKhJeo-XydIobxM4cJtayoH_qL34m8-k89azWSQS1XUn_c5JVt4oeba9lhMZNLN2E2uJKY5udf-a62YnRzt_5_xNym5Qx-DCxNPyXAX1asYz7O_xK9-8nI2yUoFi1MQBCJiVbwou_EeiyTc2iZqWKjSGEB6sDsic0rMqyPddlug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=B_5--ySinrKfShbkmArNHUZGXzR76vbsebBfkxAnikFdNTZoXVhwBJWBMBObyHJLMZOjle1wZG1C6eaBNwcuhCosPFtM7HDYDcm6jcqCTxtkmB5zHMpMeFJEDScLbfWGfX-oIgJFeQGxOha85wLHnPje_4oBuMLurVC4y61i3-HIhX_7I0CQGNil1kP7zxYdZJuGFhDsabMVKb1D5fx3hCP8qw2DoqqVTinNUD85t25sDagnqKzhHDxz1lxNnxq9rCBOQkfwH9jU2DbY214Qsk4X-GUcFOjUquWpKA50TCsjED1C8SB1xl7Iyo5mBUme0FVnuhEX517CRXs36I8dF7r0oGoYG05zQ_Ln1A02WD0lJCuRWlIbb8bEr5bnV01XAupvRDxTgVppXDGDFV4OfvZwWXWITuYa1UOXUkFj6BwF4oiLyztRCfIB20pxUd0C_nAKrpPyts1Deb35GKE7pR24f9k_0frLScXIEhT3x6kq9ofYh_PN7aQq9dkqDzGmUKhJeo-XydIobxM4cJtayoH_qL34m8-k89azWSQS1XUn_c5JVt4oeba9lhMZNLN2E2uJKY5udf-a62YnRzt_5_xNym5Qx-DCxNPyXAX1asYz7O_xK9-8nI2yUoFi1MQBCJiVbwou_EeiyTc2iZqWKjSGEB6sDsic0rMqyPddlug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Send him back
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82827" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTFigV89eNRD8E4DHJZ8ckZVk8eRImNyyQu-Fa1XMx5FgjjC9RiChDjaqEuZADw5K08uJPvlhlSIVg9BgfOc3YpQu0o-Ghdb0_wo_1htfs28tELz7p9SAKTTqMjdPpxjpzmJFqGNAzxBp0rr4s-3-W5HrhmDl9tlrWUMgqsuSUpzvJCnhf0f1I2HeaBSAgPHTEhdxdhTMhIpZTqkw3p7jdH0LG6Z3Sb3L_N8636rEiDNVFBw1JaPmGQ0HeMKC8gmAOGEWWWieiXlsi1FVoVWv1N2Qu_yTryUSipoZEpYfT0LnJABiKQWQM9dY4adSgblD9IYGOKRlVYXdX3Dbvjr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش اون گوشیا رو بکنن تو کونتون که انقد تو خیابون از ملت عکس و فیلم نگیرید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82825" target="_blank">📅 17:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82824">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=O6p5BdVeyLaWFV7sBYej1hx3TS0pwxYOj4dImHaAqDrLaPccRUUoYBUNU3pG4u2O0tHDpWfBt9S7HJmMmyA9blP_RgCSLrdb49kcLY6EA7x5pkGVl3UGDdMWAaIuHt3ZNBM5AegoFFpLP07gjsf1WNT7krD5HuMouCaqs9YgvdIyaSQiPsvt7mu-F58rQoZld1don7m8SEMRW7lfAPBH6UzcO9BURGDVCZ3Ye3gKV5CfGj2E0TeaIp122N5G32Kdnp3ZKQ7ccCyTHbxG_PMRc_qshjDs2EuOJ7hdCcXAVgULhWiObGXGoxhwmybqsxuZ8-CyZ3cWfUNzMvQYAOH7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=O6p5BdVeyLaWFV7sBYej1hx3TS0pwxYOj4dImHaAqDrLaPccRUUoYBUNU3pG4u2O0tHDpWfBt9S7HJmMmyA9blP_RgCSLrdb49kcLY6EA7x5pkGVl3UGDdMWAaIuHt3ZNBM5AegoFFpLP07gjsf1WNT7krD5HuMouCaqs9YgvdIyaSQiPsvt7mu-F58rQoZld1don7m8SEMRW7lfAPBH6UzcO9BURGDVCZ3Ye3gKV5CfGj2E0TeaIp122N5G32Kdnp3ZKQ7ccCyTHbxG_PMRc_qshjDs2EuOJ7hdCcXAVgULhWiObGXGoxhwmybqsxuZ8-CyZ3cWfUNzMvQYAOH7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشآمد گویی فرشته حسینی به میهمانان شوهرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82824" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=cH7zXtjPX2-xUPe1gMvHo0YZJ2sAxtGfWAB5JnmGLn6czMRqJZwXtDboQoCGI3bSCDbA4uz0DFcL9tEZZLUQFzRDw4hWOn91HjlzWVXMsz7SUPKufgpk7QJ4GGHMOYE0fxgSABieRbw76L2ehdJCc5qEvGlGBvCOnN0-4WnvV5P1ASv0nHaw5rIMBWCNfd-h8sqfag5cKSLF0LtErAMqPtcK58EgxfQiZFAtflZpRh8iyUBRf9dZOVvxJuPDYBlnA7Q-aUWzCJUsG-oTXlL97DTZEV-YNB3NR-CRsZiU6DTYZ3PSw2pkcNKoob1tWUuyYrCHFqaJA-YWBdA9kGdWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=cH7zXtjPX2-xUPe1gMvHo0YZJ2sAxtGfWAB5JnmGLn6czMRqJZwXtDboQoCGI3bSCDbA4uz0DFcL9tEZZLUQFzRDw4hWOn91HjlzWVXMsz7SUPKufgpk7QJ4GGHMOYE0fxgSABieRbw76L2ehdJCc5qEvGlGBvCOnN0-4WnvV5P1ASv0nHaw5rIMBWCNfd-h8sqfag5cKSLF0LtErAMqPtcK58EgxfQiZFAtflZpRh8iyUBRf9dZOVvxJuPDYBlnA7Q-aUWzCJUsG-oTXlL97DTZEV-YNB3NR-CRsZiU6DTYZ3PSw2pkcNKoob1tWUuyYrCHFqaJA-YWBdA9kGdWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی جدیدا تو اینستاگرام ترند شده که مردم  میان میگن قیمت خریدشون چقدر بالا رفته و آخرش میگن: «من اصلاً ناراضی نیستم، چون اگه ناراضی باشم میشم عامل موساد؛ پس من خوشحالم!» بعد هم شروع میکنن به خندیدن یا رقصیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82822" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC5_Nuyw5cXGek9HEFFFloN9Tm9TnwROkVZlava10YI_mB6pJbl1OLssMZtUmRe0CWuc_9_0evomCDeGdYLmwV1iTJEDRI_MXapcv5s_TR_N3LMLbozR2MLhTgPed_xyZuqpkRHYIMMgKOCNyA2BaDW2TKlO_QZCJDVoPnwt_sn4F-uM8I81kWoPF8WutJJZ0BqqVtcfd-5R0ALSA5tdCc9R-O_LSTkd63XVoEzNiSEqPRZTTWaQAB3DvHLA_sEnJbKO8irYKzQwaj_7318nDokUrTz0BxzwAaCG3AtuAoIHQc6CN4CQ-4fhRBgkAjMum8TOsu5ktS6KgFNJ_dBTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون لحظه واکنش پی اس جی که تصمیم گرفته امسال بخاطر تنوع سقوط کنه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82821" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjRMOTK7O9co0mHNphYFS0Fat44ZIraeXUfv3IJ8I0jsbxENQB3sQQPiIl78zhSP2CbiUan_OYFilVl6AHVbH_sMjQZhuEuvCrP_m3ydCLpm_g_fC__e8J5a2ejSSCBN_vUqUj7YjVwc3hpIdyDmI67CJahUk06HRnFEcXl4cgfYOMWSVLRrz911pD2pzVeB8C0xSHCVeyDeOV8v0JhIMoy_jtHt5SK9H2AzaQAaAOaMLQG5HziRc_HNYNY3-cuBJCxIcV4m_UkghUPuYCA9iDK-jecp-6SnMeOwXiEDPElH-jKPFi91PcEx3o0REXmZuHIqPUw1zpiIabmqDuy6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوس دارم بدونم مالک این برند کیه و به کجا وصله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82820" target="_blank">📅 14:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روبیو و ونس و امثالش کیر بسنت هم نمیشن حاجی، یماه نشده ترامپ ایرانو سپرده بهش فلجمون کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82819" target="_blank">📅 14:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeoUY0AQSYuGn6V2YSpRTXkEFhb5rUNhmiFYePlQ0jKJwSVA5f1fiHAcj3gOew22TDDVlbmi7Ol5WynBhlK_7DWVMSgdGSeNunLUYGcdBevpZL3mXEF9QUFVHXeBzL3vCAYq7gQyB96BdNcZrQ98zVTVuSaSoSlHQTboCL0nijz_7wh9sX7cPvj5Tk6GUhOW4-kbvkRASN-3RJKR9Qn1arYiso_jxhOXR1e2bpYrgSrg6EtgqFnYfpsALRjvz8HKw-eKZ4r7rEIpky-8WJhLci4phcRgEb57ROHzGU_TsmgXmcZtV8d5AQ-chDYrRqqTuDmMY6MpX2xNrNZ5vYsR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cdn-IZ-LgLK9EuGFHIFKWK9uTLylXsGFfjETbdP6XNKh58UXWGwfzW61F88G6a5brscc28sGeyis6SrqH6xYSsLopLWwA1ustzVq2YpOGjNp4B5lOC02GJXhP3fVq4OPLyh4rbUCwttWl50haUpDsyS55_V_p1SDuErzFQ_v4opRgKyfa3AKHV8CZB94kNNuagNYcCCv49ChQ_2Cf_4xZhSd5HPJc1qCZ8GuVxSkfVWGFhONIcnMgv5S0vVAYkqFmBZHyR2xsMvac5HT7f-jqcppIeEV-5ZcwOeUnQAiWVI2Uy1h8hVQrFDS8y-qf5DmR5J7lYyCa2hgbva21-XFbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسایی که بیشترین فالور اینستاگرام رو دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82817" target="_blank">📅 13:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این گربه هایی که صب تا شب تو گپای رندوم میو میو میکنن بیان براشون گپ اختصاصی زدیم فقط اینجا میو کنن
https://t.me/+CAwWLYMxGAU5ODU0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82816" target="_blank">📅 12:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4Ubfj6CyCtQ7B0xNLZZkAZOWvu9KhQ7ZmEwKp5SAGVp823FKDT7CC9G88eOytPqB2we43S2uUtJLp45gfcKvrCRmabZs4w2r6SsXhqGXLMQBzZ6wnQbPztPnAEs0nPE1GvFZ1b6VgSB56EndafrWAACk7uW5Lkl8ARiYFMZvquo_lVNm5amOplFNQ0svhY38--Pm06xHKu5c8Nykmr-4BVWgkuiY0DbR82z98Q3RfVGKZg20kmb4km4g97iiE8FmBQ2fz6KkVcH_krzKqtntoYDhuQ7EuqMYpbQAXOxSIxITl2yoYSoDbvy1Hwmxrx1jIQvgK2go3ml4IuMXRIwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من به شما چجوری بگم این سلطان قیمتش با اف ۲۲ رپتور یکیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82815" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان عزیز جود خیلی هنر کنه میتونه با فرمین مقایسه بشه، انقد با پدری مقایسه اش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82814" target="_blank">📅 12:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1WrnxsYEx_VKUzsNeBh_ccbSodSydx0sk4VK-Y3r_c5YyHoFs-UmyBpWXmViCPod0U4f7BeYB8-DLobu-tPseWdIffZ3S5Y4lQs-AAIc-oQlPHXs-MvDX8Ln9j6TWWiOJUv65nIOKviU2lwFxJZZttcOA3cagWaTsPq6XilO2Dx86aLLIIGxc2Pqf_yTpT_Vl9sgnDJi2F6iAuGDkf_YREBkI9Qt5lK2U1WcZqQ4-2Q-eq1BJb9aDtxs16gZJideOMo661KKPMlnmeGKILW4X_WDavwqpyat_0FwGGyKKuwyjVMIuHE1EONF5j00iuxPEbiM2__L0kO-u0eEgt8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میترسم از خونه برم بیرون بیگ شگی بیاد بگیرتم ببره باهام فیت ببنده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82813" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPOaatvXgdB0hP7z03yIBWm4kH_48pks_UzMhHcI2bBTjhQF-h48tej5llUEF-fk-VnBhhRDJ5GxRlKx4JRDD3nSrMgdJZHw2fac33ojfUtOJwyVY5Vm9KDx7kJ-cMZ1IGkz-bjwm6lt2LreZoHLdBkRVBlXXy7LBi_UzJPFusU5K2HzOhBNfMcs7NZ-ZEIK5vIXmp_wZETBypQXCP2aBSKqbMREPEH5W1_alFpjb4LxwoGrUhkkGxqEc56vLX7OiHzb8id9X7XLqtK94MKXjzYISMhYd-MGFnpbZcuWhM_hEpG0wxynVKdBADFZsheYm1O9eHdYeaUdB_gcyvYo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی این بنده خدا رو از دهه نود بکشه بیرون به زمان حال برگردونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82812" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgNxvGvw6ksDXjr9yc8qn6U-xawNAjcYpzOGU70K9QKDHPKvZx6ec8WgFpWyCie_e6QuQ_P9vsvg6fMVB4_R7kycxQt_H8wUp6DZd5lkZvd9lllJ8k2Y7jw6yyBgaPEAgXtdUdG-2l4XqgIW9vTNJ73-rNkbCtRCSUBs_L8MOPzZaNdAyKVXrhZjjcPWD-04hqkTJru2rHvoXrAVhIfuvG77eSulE6RWAMqjmMz2zlCoAxNd_R1dDrAMcEBD700BoKF17A0m9I55UH48O3THS1NgiP05yZ4Xg-afabWp_77lssVjrQ4IQuFrAu3CY5fd3O0a-fqU50FHxeA6IYvZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید خانوم منظوری دارید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82810" target="_blank">📅 11:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq42XVOyVYqsWYs5d_NVAp-PtMp3XiTuyjy5J25YM6lNDOM9yKfIEnOwIILIQOGZwkTO8vG4D-t9fx4bQuUvA-68KftXlbCM8oL0mjmGxHfjPk9_aGMbrumTAvugBAaZLtCc_ZlxeuG5JtasdYz4bgkGIWxqsU0NAwSpjCIPGhvDxD-fFLYelEtwbuJIkdLSMr-WQUQMGXZIPMaFcYNiMnqNv_DxQhgut854QRYY97NI2xn89VYFGO6PdU5KN_wTyBYfjRKApu3q2BALKyaWocWmeV0DObk_sdgv5RQdIdms7t_N4Bibru8TFir_MBTOtVpVXbkqCNncIb2qEcOAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیلی که باعث میشه بتونم این مدل مو رو از استاد بپذیرم اینه که پسرش اوتیسم داشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82809" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">میگن تهران زلزله اومده، ما که حس نکردیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82808" target="_blank">📅 07:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
