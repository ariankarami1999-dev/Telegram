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
<img src="https://cdn4.telesco.pe/file/XB2ythHcej57DlD7JhmuDuU8mbhG5ZetExkrw9SfezzBic6ya87Eh5W4z7MBG831jUAENXyuRqTRFjDTYPX8kFuva4C5IyDxeP1aHvoPwjpnJTyrMWfS38HNBN3D0bRFOG3a0skbTmQEe8y2i02X27AJnZe-phrt5Fp9CyoIUbuBKgbTGOHxo5e5fJABkD57tyo_RTA56V9kWbYZSbpAkyImkLzac12o3hJUvkGcdrtQ38ub7jbWzBjIw5xPIKP8hN5KjL1JODIEVyIrtOL86k8bwF0xY3lH3FN09tcOi17n7kjbibPLWh-LSK2egiKSmDMuqYuzH1x4rsz8ujp8-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=NoQYvRpheZIjZK-Zc3SYcgdVOKG0pqr59ZlthUY6sU6_ls_EoCAbDtPFeMKj8RkRgZgsnx5-st2m6xHM8Awk9VhwxBoV0evSt5T5jceRPdHuEHUm8Qm3LnxmodC6Is2sjL8-Xneu1V3ysibbUYqWpTt6seYY_y3D8UELq8H7kXE0lyWR7KFnZR3RbCdKzjjHwE4t-ZCFh28HlsVmmAfiZQOGd5_Uyca4yW-eCEt14guac-mTrdFq9PBQHuGHUwo5cSSPmDz2AXV_OD8RPWqTqdObByztq4FQQE5VrgB4yWkI4XguuQaZUhIZNhcB53dRbIJr6RX73ueIEiQvLt9uvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=NoQYvRpheZIjZK-Zc3SYcgdVOKG0pqr59ZlthUY6sU6_ls_EoCAbDtPFeMKj8RkRgZgsnx5-st2m6xHM8Awk9VhwxBoV0evSt5T5jceRPdHuEHUm8Qm3LnxmodC6Is2sjL8-Xneu1V3ysibbUYqWpTt6seYY_y3D8UELq8H7kXE0lyWR7KFnZR3RbCdKzjjHwE4t-ZCFh28HlsVmmAfiZQOGd5_Uyca4yW-eCEt14guac-mTrdFq9PBQHuGHUwo5cSSPmDz2AXV_OD8RPWqTqdObByztq4FQQE5VrgB4yWkI4XguuQaZUhIZNhcB53dRbIJr6RX73ueIEiQvLt9uvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=V5ye6SZtWow51uNAFwT4W-2kbDPRvKkulKPtDT-CRRL1knr3pdXJYKJ6az7BPMuvgytmIqbXAP-TrYom1CcRIdsNBRwwZYunFThIXWBp4eJ4fwnhq51RTafw2MFKN6qW6h-NYQMVK9MVMk23BeW4kg2j0-mAGvAyeI6QBFunDAJBBcjQxXELv-BJiZN5uIdl7s1KUHmqHtIjxgQ8Bf4uvNMy4DuI_vhnr4Iap8dFWRscwd4gZzErumemGADJFeTmqmM43ELkurQ7GvVXr9-1lT3Ao6pjPnwxlANZf8L8Hmz7sKKGOr-u0X0M3JrOxgJNdW27uZJVmgjCLXvbPsCwng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=V5ye6SZtWow51uNAFwT4W-2kbDPRvKkulKPtDT-CRRL1knr3pdXJYKJ6az7BPMuvgytmIqbXAP-TrYom1CcRIdsNBRwwZYunFThIXWBp4eJ4fwnhq51RTafw2MFKN6qW6h-NYQMVK9MVMk23BeW4kg2j0-mAGvAyeI6QBFunDAJBBcjQxXELv-BJiZN5uIdl7s1KUHmqHtIjxgQ8Bf4uvNMy4DuI_vhnr4Iap8dFWRscwd4gZzErumemGADJFeTmqmM43ELkurQ7GvVXr9-1lT3Ao6pjPnwxlANZf8L8Hmz7sKKGOr-u0X0M3JrOxgJNdW27uZJVmgjCLXvbPsCwng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRN1vAdZN3zvzk5eS6gTFkmRYThuURK5tPe3e1MDqq1DQA8O0q4xZzr8iGvKUFPVedgOieK3WGZQtPfms9dXmTWOU3VwIxp5q5zgGpGhB8P5k-nec05qLl3miJa7PU7ZAK6_UyAs0hr64bIhrvNpHBFcosnKtvcAkFkCIhL2Iq6Nj2a9X4arcBoJvOuGG9IoCIN0AKCwc9_DsPm7pEJORzStpEExPdYNx6sxlybv8OXkjguqUu4CGkZPl0kUEa8q3nSmrilHY7jIh50a9gA2dyTpDI3u7l5xpA07nNMM3v5E2fbQKh0QI2Ctkz8pPzUDnyUAllQgJeR3yzXUxJ8dYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUyRcX9XGqv_yzGyU3aTCxfsQ2DV1JQFncQVA8sdBMeEtr2SdybF-wakj9Np6JI4M1KI5gY_UCb_s5eKvXlph_I6gCkajKIlSakTaCw7hetO-arljL3-Sqe5_wqd7sBjwffPJyMUGbUjyGNco8iI7va9xdOTvyo7vGEmG9FLr7RKj4znoTESUzoDz_dtjhhZFDRTrbV4HGbS0_bY6vOYvtLkiTvcUptEb4adED9iutV0NmkFZZvRfKmvqiQEPZwrltkzH-dsnj37nh_Ft8jv7OQOSQSsVpi-2ap2fa7EYe2hiMFdHoZ4td9RjZ1GkOI355uXvOsL52PL5T_BqU6txQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkTe75OFyryke6oaWuwV8WWxW9gixcC5x83Xjv0vbIx7pRC6lXiBgtknLXNA_hc3NqlvJUGYQ9Fcq06gLMtt2IglaOr9WTHIWPjh8GTdJPPzvVDZuekWwOoxBucNIZ_V1H4oowkfLJ2-nRQKunFx5z_BYv6hwIRt72bNgyapM_eppiJuGnRBkJow0v2wuDuE6QVASqFl0i7Ygy1XPTvkS4pLNS_DE_CLD4ZiRrv1ZLfMeZwNzv2bKWIeDwcbeUJrw_9REYFlpoPQelBd5hWrNP_dGlT7O1qlTnFRFVJqs4Y8ogN0t3wgKit2dJFFZ85nnY7WYkpRNUADdTmeVPzH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv3_swxgGbeAN4vCo6ax9guy0BVUzGe7D1qeS6OnU8DLHFV9jh8Z9wZvoahy7Ya1k40uGZjlqPGxXYV1dBowwo9adZqpCj6Pxp0Aq9z-Dkx9dzqPXvbpmBFJ_8e3d-41Y0yfcIR_-6OL7khp-PmwNldZcyDK4aP34HtZ8Ck84MMMoNj2yOSbfRRC-AwsxVX_gnaxhoRkX2DOv26LOZ_cho9nyrlCCrQrshO5udPV4lD90WQFzJhHbjIB5bxTQAbLYsGlQudmWuQxq30s1hm36Om1jOb9eRAsLFMU7zH9eJLjkdFuZEkHx-6tdxy9RhraDr00ywsOGiMNycB451Ilug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEzM2lQQpXMbr4EzEqQGCDjE5915gjR9UsgYOsPiryq5OKZsOIHdkI0IuNtISM7AJpnhOVaCXD9QHpUpfD5-L2d278g3SKt-tMqwJO1LSJMdbzrD6EPvjBvIcLB9YfmKYjnVpvPstd0MhmTRiJGoF7qFafkv4KlRFDMO8RR7ndt1fEl2kSnXjk8EQc5xRcTTiWLtz-NGVxtXlSOXmjOojZcJP_6AcnHGdbBvWEReJbrMjXGiwsBrZtHxJLFMc24jpErLg3BuYS9T-F0H6C9lPnGHu5rPj5Dpa-uYfvtDYqYkQx9D3ulEw_Gje0q9j2mkglE_VHUrOmm1IzdjDqPcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEgBPAxlsTAM7E7E9j7JVFNj3NU6G1qrlJIXT3NZB25fCpFYDTwn60ELPxNbOtuhFZInXgdO9hYKv9bCOxgWPQ08ndjBHQtV0YSaAb1wdjfd2o6WulSNAlwkI0KpPfe5kUIHzEX8IWR31DCZnzGhvNp4UxX0vn5MJFWnmdcN_TcOeMa1SmERSwkUuq52Rm_3yFAi71LbLvP68qezEIMqX2h-xuh76WwVK4pzz3wibmUhAxWq9WjBdMDH5lWeJBM3UcJX_pxINTTzb-zPdd-0NpQQebXP1l_wzysw5qMRZFWhz-5qE9NIQrmIS2A2h2glA8rDiiClylsMirJ_P-kkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSnAG0UEoU6hw6xR9H7dfpd4waX63lchhKQ8DwNzQRklC9ev4E8Zvw8c-Dt2H4Fj0MyQn396TG_Ja1agBh_dsol8NkED7c8VOfgft7bt84jwdyzKhgxmgMl07Ome3n0IOwGFkZQ3-bz7XepjT9_RSKQv4Osn327XKIJYW3Jjp7EfJU9LQEpHHI4zlEye8SKmLO7dmmuMieJG6oL4dzGGo2ThRNyRFotpS4Nb4OwU1A15D1O4gWVVATA26hICISJqCoUlZnb4z1YVerK-A-K-BleMQslgRXnmGR5G2iBt_2XYw5ZNjVN7W7DtmGA66zW-h6WB57-UFyNu1__rV_tFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpC8BbFsL13pV-XuR_aT_ZLgu12s6ydbri2e1sEar4W1wjZXTe8xN1ATa0xjW7MKRdEPhQYW6qIrqIncjbp5pDlEAt0pE-pOmpBaiexwDLYFnI02SnOPTKnPV4c8RKdWHX-ylvM-mqxe-9ZP2TqpMHq_pY5u5jV1acQgLxjSEyOskVaHk1WOtcXz5CJy0ddF7paX3TzCN5i5kU7ZXFmeuPrOA-WEq3raAmP8mOnMnh1tbudnw32y3vE0uJkl3KFRCB5IA8LocOQiNr4AwWenIxS6k9HsU-dGbtLveYHpLmTVmvrUPAHl0OobKXXsG8I5DrKaPXj5Aw5ymfOZXWz4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IXBb5btzF50ITGMRd-fLwo-ktT_ErxRwHruaSMem5Q6EL-fmPJmfFf7IgfDyJGKvgG3oF_6-iPW1EoWnKNkt1qwYXkKsspiu0ah81vPntxe4-TlJY2To3nMBttk-2zx2FESAPNzyb6Skn20gSjxZCvMqSSy27DLne4abLA0LHUO_a4VPH0AucEQ53ttjC688WB2hmPLkZzD1o-GybQOSfTG5orzYVzSQXd5MnvwdFrad3Oh79Yz5s_iy8Evq1xNbE51o6F968KzNqaVfalzBhS77dXTMSHpWkeVpaWF_V1IlIq0NrGaLn0VX_7dg3iNYRfld7MAZVGUCoRK53lh42w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IXBb5btzF50ITGMRd-fLwo-ktT_ErxRwHruaSMem5Q6EL-fmPJmfFf7IgfDyJGKvgG3oF_6-iPW1EoWnKNkt1qwYXkKsspiu0ah81vPntxe4-TlJY2To3nMBttk-2zx2FESAPNzyb6Skn20gSjxZCvMqSSy27DLne4abLA0LHUO_a4VPH0AucEQ53ttjC688WB2hmPLkZzD1o-GybQOSfTG5orzYVzSQXd5MnvwdFrad3Oh79Yz5s_iy8Evq1xNbE51o6F968KzNqaVfalzBhS77dXTMSHpWkeVpaWF_V1IlIq0NrGaLn0VX_7dg3iNYRfld7MAZVGUCoRK53lh42w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgInJrahE8QEumhODZyXfOi04sEc2LyioPStjinLyWarEYprHp5_-CP87oHEJTh9NlBAi-ZMTXptkyIDHn34Ws7gsZW02JFTc-qfhnm42GXBdcfjEYg5r27NA8z983n2vwCQclO5fKfG2Cblz92TXURkqYXYNtIEChdeJGdYu2q-ubxzgVG_uX4xANLsFs6yQfFXhTWHA6Nd7Z5tlS1KelyTbFEBsm4b58GRdl57Tm2I5MH7H9Pztf7wfBc3I5Wv8TmRnwyHddvBPIRoB6mFvGc6-L6qGFT1slSWeboPMMGAgxl6wQAf2J1DdLGTxjqFz2ZvW3T-pQFGvQMW5s9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DweePqedHdpAxvexiYCXYzJE5PMDsWixhDhNZ1zDgm2WGAD2UxptEVs6XBHvE5swupift5DO1ihG34W7eam88f8_cbKb2WNPyJkiaYn-JCo3K8qvRm2GJk7TY412CJ3-ODkGBg4-ok3PwRoLOUpJfNKTTtL0FqEXgL3L21BZ_By8NKR_tAJ3CQ4h68Hp9EgpLiou0-ZH1E1sg3QrJqDKacTFmLaMdFpi60MVjCRKsDi64S4h5NQzK-vcWpYRBrnI0XkTzy5Ejrev-ma72NSsaUupK76V0nqZ3Oa-x8yofUINO-tkqj2UNgIYwluBvfOZvyKpIDaF6PRU22qet0TYLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DweePqedHdpAxvexiYCXYzJE5PMDsWixhDhNZ1zDgm2WGAD2UxptEVs6XBHvE5swupift5DO1ihG34W7eam88f8_cbKb2WNPyJkiaYn-JCo3K8qvRm2GJk7TY412CJ3-ODkGBg4-ok3PwRoLOUpJfNKTTtL0FqEXgL3L21BZ_By8NKR_tAJ3CQ4h68Hp9EgpLiou0-ZH1E1sg3QrJqDKacTFmLaMdFpi60MVjCRKsDi64S4h5NQzK-vcWpYRBrnI0XkTzy5Ejrev-ma72NSsaUupK76V0nqZ3Oa-x8yofUINO-tkqj2UNgIYwluBvfOZvyKpIDaF6PRU22qet0TYLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG-LphQoTR5T092ojTU417nZ5ZNwuLHgAMIGosCkm3S7rZs-KdlUMpUrzrAOiFarjrUrARfctqBw91QP__JSY3u4TK_o_m2vsgLaLMNAW-3n5bj5UaK6OgDb9zMSncwXIQPFaJBFQ-KJsCEUN70A4x0ReQKfBAQkRQLw2Lp3ZCtclt1eTHJrIaG1DAWT3U5_GW_XL8nijD-qqDJ1zGURUIanA5zwNqqD5Tvdt500AM_R7wIsz9ZVc-3Qxy3KMOXM4i0CANdw40YeMsPgZIbQueI7XX4vZHsSi8nqNOerDGWVUMYCVfGWS5My9WYMrm4mWOjb23WBavH2epzZQF9Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahIslxjLgEfiobp8OieOrWai1cnUqsMPSGdSbbBv4ohFpmua0wVMqkQlanwBeMotbAlSvLwhQBR7MT0R2qAXnB4k7Rg88xaepSsnCRGDyj02NFUVWMB_DNGRju_8gvlybhX3sg7V4vqjGTKjDo4O0MytGui2U80JrhSoNF9obi7jNv4w7KQ48chwuklRsXsvffIPCypJRyulOHcbnAlR6m4BtqHZmy9r0a9eCVo5gQrMiOa19ANygzdpUVf2-wL4apbwzVgVExCFmRO-OJBjJ_CITy7sWM7nKn_anMbK0q3Xjnu1Ab9FqWNdXEsXwMxmVyZedyf4DS7RsxqFAAcuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Y2rVvL1HMT7fMgq3DjxtsEbIJLJ9Fjkvg5BHpXZSKipi6cCv98xIARm-ev6hhjfrKZUKKW6VsI40PJw-2YhexVxf5xGr01_dwesGEyzyrJmh_ateOTRFRwdaq5xhreCXE0wkOug88bH3l8gry_dd8QbOYWPJ7mEAs-ELmYUJ0mZXBUw5YwX47WsTmbRs_Ntidtzbqev8mqEPnmfDkiD9GDb-9CTLAFU7sfUQS6jl-3TBScLCN1HGnmxWTeP3M27sXqIuUiPtsSGwW4a8BeSuc1IKX8gZUUKhrZLhgLbSOMk0JHCFyyMYrgQjfHd4ImFiEoym3sL_DlSsaW5xIENLmRBmXCiv2N8oBJJEDTjjYLQLplGKIRYN9CPa1HCJaH1dkGZPPHRGoLGQY7jEcJwOi5-srhndnjsyfpd1ov4GusH3dFRVJbZNUJkz49BABCxOEqB3b_3pwRgWkz0afRwm-odwhmvW8oLy0adDYRGbFeEi8UfP4sfRMF3USg__j6QGhmZOVGnEespsM2wdeVDcZRc4JT7_WgmV8kRvFDBy1SZ3sEJCK4ArpAk1umHDSD3aFjOBqDbVmYPLSJls3yUc6--GLqGSaIfsP535EnCgl-jIi4IU7MJfz66e_6Phpzvlp-3sprA02SWOkgq5cZP0iPUCaRxo_u_-WSLSV24snwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Y2rVvL1HMT7fMgq3DjxtsEbIJLJ9Fjkvg5BHpXZSKipi6cCv98xIARm-ev6hhjfrKZUKKW6VsI40PJw-2YhexVxf5xGr01_dwesGEyzyrJmh_ateOTRFRwdaq5xhreCXE0wkOug88bH3l8gry_dd8QbOYWPJ7mEAs-ELmYUJ0mZXBUw5YwX47WsTmbRs_Ntidtzbqev8mqEPnmfDkiD9GDb-9CTLAFU7sfUQS6jl-3TBScLCN1HGnmxWTeP3M27sXqIuUiPtsSGwW4a8BeSuc1IKX8gZUUKhrZLhgLbSOMk0JHCFyyMYrgQjfHd4ImFiEoym3sL_DlSsaW5xIENLmRBmXCiv2N8oBJJEDTjjYLQLplGKIRYN9CPa1HCJaH1dkGZPPHRGoLGQY7jEcJwOi5-srhndnjsyfpd1ov4GusH3dFRVJbZNUJkz49BABCxOEqB3b_3pwRgWkz0afRwm-odwhmvW8oLy0adDYRGbFeEi8UfP4sfRMF3USg__j6QGhmZOVGnEespsM2wdeVDcZRc4JT7_WgmV8kRvFDBy1SZ3sEJCK4ArpAk1umHDSD3aFjOBqDbVmYPLSJls3yUc6--GLqGSaIfsP535EnCgl-jIi4IU7MJfz66e_6Phpzvlp-3sprA02SWOkgq5cZP0iPUCaRxo_u_-WSLSV24snwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TptpDosSShr0V2w20jZL9X_xV5jF_hip-jUbSFecqs9ZhJhWV0qevdIxx6KmHkpu40XIuVhaWtO6yZEBqXPAOSv3kmZIo1wfdnX44ZR3e2m7Br9PM7qqwoT4ay5KgWZg6-itEQZA9vvwu1lKTqbsQwoAwjQKA1RqDFCaQt8wV8gTzPwBWGZavWz2IbHKetlZS1D0jq0k1yQcZX8uugDbDknS19uf05Ps2CPr392kITJRmAhcJggPrb4zBNb8qjbgLPKCfuvpiAGfgQ2tWWCV0uXCz8yEgmwPanKz_2SYO4MNjQ3ri8JhcDdUHo0e9OTu17QqqE1G_k0EgtXPRfJqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=MPnEq2axhVOg2mqGtMenZ67IwVNC-hNCvNTJW5jtvqHzGgbNLCoRdBsxVmNTptjKqU9r-cIA-bUdu3bH-RmgNGV7FXw7-xJN32hngISSlxI24ct804jQn20jt7JRnBsPlOUpNOKJnQrcooKexJA-OHHYdiNdH28OscnsjjorBK6Nq8ss_vOp0BmOhUcQNjH7a7Mce9mo-6nddtTm7kS_8Gj7HnXxTe6ruxtgZHfJnPjwCc7Nu3GdMuR5QjuetDF_L3XYXBhuHgl3WOHjabN39m9T-vI2oMtI33pXWMET1etfrzs9K-4btOUn0ORbbagMW4VIhIkvAlD7DoVHrJjSG7uJu0LniA2R1PGV6JNVo0u5tPjarzhU6sa53weYx5hx7pX5SNYmJy6c8VcF85s6SKVgpdL1hgn49iv2ZBr7PcRIKIiAn7cycNdVVmgqzVGdytIAyn3mt3VZn1pvj4STZ4YeKjq29_jDTLFy6lWI1tpV1c4FMFCskxcHZP41wXAvMF0PqsD4NDvg97jN8q295WGACOj8nHr5x-bt17bUBWoLz_98wvrHXAJr7pz7IoXk-cxAD-2Sqe1hwJVXicdMyRYcRxfx-tnq5nVcd5DDhhS2-zHFvZIFPz1MmFTvuMD3RHY8AVUDV1A8lzvLsDr9o9G7hi4LzbTCUPBAWb0ksvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=MPnEq2axhVOg2mqGtMenZ67IwVNC-hNCvNTJW5jtvqHzGgbNLCoRdBsxVmNTptjKqU9r-cIA-bUdu3bH-RmgNGV7FXw7-xJN32hngISSlxI24ct804jQn20jt7JRnBsPlOUpNOKJnQrcooKexJA-OHHYdiNdH28OscnsjjorBK6Nq8ss_vOp0BmOhUcQNjH7a7Mce9mo-6nddtTm7kS_8Gj7HnXxTe6ruxtgZHfJnPjwCc7Nu3GdMuR5QjuetDF_L3XYXBhuHgl3WOHjabN39m9T-vI2oMtI33pXWMET1etfrzs9K-4btOUn0ORbbagMW4VIhIkvAlD7DoVHrJjSG7uJu0LniA2R1PGV6JNVo0u5tPjarzhU6sa53weYx5hx7pX5SNYmJy6c8VcF85s6SKVgpdL1hgn49iv2ZBr7PcRIKIiAn7cycNdVVmgqzVGdytIAyn3mt3VZn1pvj4STZ4YeKjq29_jDTLFy6lWI1tpV1c4FMFCskxcHZP41wXAvMF0PqsD4NDvg97jN8q295WGACOj8nHr5x-bt17bUBWoLz_98wvrHXAJr7pz7IoXk-cxAD-2Sqe1hwJVXicdMyRYcRxfx-tnq5nVcd5DDhhS2-zHFvZIFPz1MmFTvuMD3RHY8AVUDV1A8lzvLsDr9o9G7hi4LzbTCUPBAWb0ksvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRUZ7UgYJUM1JPpeYUoQofTSxYDccaG9_ph3u1A9SFVGucr4tFqdQnHWiTLkj1OownDEjZciHbfh7Uen1bHh_26G3j-j9LPrmKJhjTlDaihOqaBMOFrtexhL0do6MUQyGxj_zBvBL4tiUe7aawvjxdlulLUKNXQLsvO8o6z-0AorxcFJZmvtKJnCCO_yBuAnd51Jq-if4ySb0Oe9M9l93nwo4v5HrfIgjrptuYfNem0_Zx5s5THD3l6oei95syTpyr6dbTsVx0iZyK-uy4ZnwSn4xJSUdRcmzHs9eaeyKhEu5vJLOhFPKNvsQevJLBj9oTgL4BaZPo6MU4lsaPdE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLjEsrn3kC7hKEMXfLXLtkuEl5VD19-KTiDaAp4_3nOmVHFNcTZQMqe6IuYDjt_u-UEIO2b0vFfswJZfqZuTfx5b5L_kepyd86bwFOd8zsAsOPxAddd6HQiZNMlmMpXTl2_4kwY_T2Gax9-X3JuqoZ-6gzgI0KF9i-hKEnbCUhe1f5HedkPCNcxvNJaeFLFlKYijlc36n0WV9vckjGhz5macWHpwR6ddRv_mw7yUwhaGmAHtgOEp7ypK4CYMIpJ3QfNuAHzptXkPZBbwc_krxxPBBvxbmixEpuppzUXwJQpmQF1mR3vqz75jdBrvL5DFOfSlPoy49Pl_s3YFSyQkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhP12_gv4VoftfBWqIJZ4QRoy5GPf0GrDZ0z7xJ4nICiB1i0uJNwsFdBpT1B79J68HWaKpFvgckglEqepOTTmN4BchQqGc5UfP-Vl3a2CpQCXGWD84mcq8Oy6t9PJZrvYfReREJZu25DwXEqPgOKWr1G_u1VQuzSSZcNyGIqz_jq3aBPVsEqzcMYuKWWzP4HfL51rZQqLNjT_MX6K0nh2gAr33fidJ_gjpttRg2DT4KHLoDT8XeFa5CQ346SjdIUl_cJ8w3u75RKzjrjxH9G1Uo1ceMtLYPXmnnt11iY7y_sOoKqx_9eG2uLXDcfmaQF-xIKgekPQvHxshCapSgOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0xk8BvHWzgI4SgTFr9DOCRVDiXLzSRY52k74Gr15Jov0fu3YRvE69ZxzB2A4RSP9PFgz1optsN-nvvr7U0EaAGgIjPmUNK_yLzhIbSIfmbEfI7WKqCCgkoiBH2lU9LqxadzpXvxvDdskCXBxDXC3fEg7afjkQyeyArspEzKnq6-EeHDGnxjADD8En4VFgyJHDp5TDUSh-0Yt28ubELQ9xUnn-zHrPSGU-kUfCaRadwxaZlBctJwY6HhQ1TFca12TmyEJc2F59XreNrjAUnw_IVakBOnXXIyVM1xoI7Z6izCMOqpuzH1S9leMcD4GBQPp_dkit-Ex4754LL8VkLyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBPCTTr4b5TYS-TCnKk40ZSvn75Ti4luWL9__EboKFZ2p_jwEpiESZuwttM32XnQnDj-UuCw4NVNtM_ZiqoV3nhTZONgKsrUzePeh3U0OD_8dTQCuMzsFMZNv0zNqWmsBds-zGPjzNCsuiH6U6h1Au1bLQKAth1QuwH6tM-dXkPU8JfTOd36QnzIVvuQnqc-pXde3Nail4PedyvkfsSqQyhI1yWhEFZ3_z4tv5iCxzVUerFF7siiqP5CitzDeAYu6QTcrFFLQeBh0ipDbAMMRWvoxzqMnMBydEO7AHFPLZKn_y_-TekgWkotr72NurLwNQAis5KooOY_CaJzksN-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUHD1GZvv_w9f51B4uhGHi6wFPhMsHDtrUDMhB_-eLbJJZHhPcFiIrOVZeKudU3XCqucN5e32P4JtVWWNtWrX-KBUm7JUx3o-TbEQ-mpEREVPD1dV3l7faubxhM2W-LYgJ7NYutBxzvPXYwIzzSK95QJrdRMZBjORHI4bvUteP42Z0FlRgCQ3oH4sKAA-YeFBWwRaP5RVUXMldcU_rGqdUyDMNz2hN5R7FvjjhyFnTzIWBHJRZ8mKt6tXhqwl8F3rMwMO3-6WenFh2KTYn5NaFOgl6KepN8z4_GRYp3bO_aqj1sqHnh-2GCL5Mh3NW9GtfUP_9ArVurUUMGNbw-rAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peHTBUO9fPA3yt0UereQD5UW20vK4de0mcy_M8Xj6MtXhyMl-QoiI5LI2tc9Fvkbb2Fi-_jKRec4SKEfZJG4Lro3nhPwGs09_a21g_XwMOnqrdmGT23XpZGuf7WrCMJz2p2Naap7XKHSAfwIz1DvVaLj2BEx1mzTUPyXPRrC6KVR31h3tS9DSlbNHZTHBdLh_iQY_Eu6uws0Fn6ezNBvpPNg-otMSMHgJhJWSzr2rbKocDvaE02cpIcsfioBi3R8STl-UfPYyHw1hFKIa4Yyv6rNbYW-AsDhE-TtikocZQw54dtX833ABYNOkAtNpu58heGVG77OP2PIjSAwD6H5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKlJH8CrnOj1l0-1c_vgPpiHMlhNQ7KFx_un8JuobjwY7otq7jCCLLnmV0Wv5McyJdTQwJ9_egiyvvW_7cangf_xoC2s9aHJDht1M1N1EFx1OSaTEtj4r4OUG4aOXgNgDWfdypvbLRBwvCSC36TguCy5BrJCq5jfM5kOC5x6YGHU7NoMO4YSa0X4XdOaIJimfPScewqEL2pGFRg-uX_DRiVpfDXtkEv9NvboYJnTAM8BOEgLXyfzs02xnz9hggK2oLo11T6DQA5mj2Tgr5AiJAKQaiIYyxq4BYChcGPMWLEo0TCZzGdqLiJopxyj2_ih9x5_qDwMfRXf4Qo9thdu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egZ5Ekf6idqPwzP6WvkizW2xCGwcOaibjJeY2IwmLzvfcDuqb_lJiN6So-8TdAnBRa-ync2hcDvo3APKaq77lca0tGS7YrhjC6zwKn3RtaTVoM_bmO_taZzo3yCN5S2nBjIG3JX01082x5b91-wBZX-qmKsXDrQNWZoNrryToqRQnw9XaPU3KL4pUTpfX0YhXsHgRXDRMgpihp2r_QPYp0j0jAIVgeydtKoXMRi56MddzaGsdZE-pJfU4-FDc4-LxqmjIdtSgYsEu8VntBFpaNZcXsE87uuw1b0kXO6bP4NNOO0IoEO0RTnF-5RwzO5LkpMnKa8LEmDC8IbMvl0w4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlRZN28SBglBbxpwdzXo2dTRETndRd9lK0p_E_Z0I44svFo3oApBuNNI2hzvGUzWkSFWt9_KwXDokAtPyBnHKQ7qKgwI_NG_qgyLs3grkx9oSlOLyJxjFUxMxndd75EM2QOWgiujQtxx2nj8-O4bGa0urYxS2xXBTyREvfIqd5vGUvihs5tH-WBLhOp1x6DRPfz1F0KeyIsEzpum3SayY8JbsbUjdD87VeOAiaHGwnHvdBh_Fp98oczQheZlhV6AVGbXm8jigrsc6x0YOxsu2snKU0KqdrY0Dn7UNa5tBAhJhpMgQuh2zXu8N-D7cDZLo7eRiEc2BC2yOHWIQEYXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLc2t7hgPAnVyOUw_IXythwuWdF2sXFkowuK63eMeYi_y9EqhRQ1WeVHS-1tT4eR3Od6u-4lvt0zs3Ah6vtR5aC4m7tCky1me1ZVPQCZgIdNrneeZah2naCtHw4drmtVU3JjN9i6w6CN9u3Oda6AQPkMmFjqsSapdTI2KliHq4V1ObM2dmU3aJG4cqIWPVe38xBSwNicZRFS3MwRJcz-KT4LShvY0UD0bquNpp7ic5P6qf3_9uphPXSbOfXUMDUwdoVm-bvOIVUV7Ky4YMdyMantr-52NXYRwb90x375NJ0J9Q6e3NxuOzfzokHyz0YwBCaSfTOHCg-aOOWrl7VoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4OOPYLiW-uShkVMpgpTJbo5U68XyOtaWf2ZCjNGnIA5n35nGUCA_wapOBvJOmUbmRQb-3Q00pMG4g4kkzqtxwH6VAJAxgpRwcuqUZlAUS2hFl7vnTQuBnlvUCnc1sOrOZmbDLp0koB8OtrhGPktaRnPn0_1J0Y_HhJ8EPG38tHtxHX4ZS-ZrMU37QJLEKc4UxiAj3-g-bPyGPhsg9niiLxdj-EVFJoWX8E7ubwqTwkk8pGcGfAlMVT9vBkfb-U_5euZKSFIn0zuvLv-NlZxE-d-aPrRMqiko37-eqAZa6Z_B3outk9epkZ8HlNxtR2pMU83dv2skEZ7p3ZQMbtSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqbFOyX2DHPL2kNRWcaog1njlkVKb6LzW_UaMoQXY8XKNVA_Yz_nzbPoieMfUh351DeI1I0r0x7wmi48EFX1NqJrQMMelcN9yTQQ6vGu2dhPyhnsgd_2iQAPSyIbaaLozJAdvgjvv-wujp8Zi3PnAD3gl0HEXeL8b0AJxxTqzeoJfgiwLbft1zCjL5GIY6Q4OkL9TGIksvqLq7Xq8nMIDnjwV5zDe70Rzu-YJNUNydyCoIlTt1ER2InAnMukdQCmSBRjuVeQRoVifLUp5oDnbv0168JsChsYBN6W84jrUkaoQE7eu-aCmm10Bxm3xiXXSI-wqOeZNUDDlhxlZpkXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0JSjrkEhPnbFAoQWBrtcK9H4oOoem8hfmPYjHUjLqtMDPai9yKtzNSbWnT8PGqLru5g97ryRGCs8Dd2ToHIja4nYaHXuLeJQLsBgtFBu79bNj3oiDH9YGVuqxxKLxdo0dLsmz46QJLm-XJmhXDdJeT5HO4YPALT3h0XyBIVKC_AR84YabVKs6TbAlyQL88J9ch09Dx_QUqJR1pTzpN_VbZcU5PBISjnrMfRp7P5D2E4e0HiKMuc-u8DCr-7yKOEhjF8PdvLBjvz5n8_NgzEAMZCIgbiwFwBG5HxN_z6-fPIEnCRNWOrFuG9cvVHpkGvgv3_btxNeQ2vYX7o5ng60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWVkYLvsBb14V7cuAFgUh1jK7SkeaAVL3ZXBTd1id15pZN24nmkNndZpzdbn-jIL8s14w2ANdrVVW4KoIiSWTJ__HgQ9fQQMk2OW86M6azW9F05KZAkltrY1Q2A_RX9ALCBcvwafKghC1n6AP9c0rcR0_gdtGGyroJKxuVFO9wdGlxpllbt7ycWp3aRb85Jlj2akLsTdlYeG2Wvuh0weu8Xe_xi2KgVAFuK9bTUNFcvdtQc7elzYtYXNpsf9SrB0QZgV22BquFjDvpQSX0HuM5ualluAftVdJuVYJLkr1Y1yhgPOREefDuUZzQ2RT__3phbo0MLo_FcA9QcjcWgZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaclr43Ak5_eVy-boO17QawnTGBWpllMFJkSgh7kwzEFncyQe96kkHA08-Yh2fsoJra_Yl1_VdForEvRy268KeBr0oh4J9s6sVE-QgZrRN2qvy3DUNNv_NGAOlsLAGbe9youx_R_rwXfajwVudn34ZguBLr4pr33RIOB8u3v_eEVxSrhAu48h74_7dyYj2os3EmaaA_Mtva9Egpzs-JBGBK6b-E1hpuhvvDe579yJEXkERWdJMLZH08WxaQ-N6bVeFej0D32qPZQWyUi0BzU9Flr7CVAUGBAwKK0lbUTxlVYOTMdU8KcnlrRa1YV_GAySD-Yp3tomiWISRrchCgf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgVRhhJBGtfRJo2w7YIh-mq8kVvhC_uJYalbdJkT4nGbbwqxDbQEBFEFzYKdX9kwzuQlc-RD16zWwhKqvPo-HtpVRY2gZwZqdNQiceNBy5pDKtrlomy2FKsUJ0vgF8y1p2Qcr64mWQM6-9ACXUoMP5GpnVvB0mR3DdkxGFnKcxE9ePa_4A2ml-fgO6GuzRd9NKqVlObSc5v2sHl08jnoL8UAwAkHh9Zeigrwxs7pYm2640MXB-FtFypvqXy4DyyPEVNaIwE8Zz5f9KWGEqKD_bMM-6Vy7hlg9q6TQFsL-XGt6VLFY5FyKcBDfP9-xkzrbr_-vklPv-QAmgI3Lo1DNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi1O25pCPDDNQYwgMnCC5i-dbYJt5k4oM_XPzKwdutwMk-cl9iseAoMj6qOwNuQmBAP0Ru6ljpLRugpd8q-y-JMb9pmZGidsqgXWQDErLKGNho1tcbaJXdZ8PaORaE5ESsMg4l7K99kjALArhjkmnL8JU-jnqhAfFEuPldNYHbYur3sMBnh0SltAl322voVeY8hCiYtN1_lRFmDfq68AFf3d-uTvy5nnlxLL3YWxX1q3VKLZJ_7u4-vknTSfBZRvNS4IlbU3mMNKe2cuM7jOvWK3DxVir_4k8Ud_AbGgFL0OnNMa0cmBM6GigvDLmAAFlwwU5ofePaOmyaoHyFdgBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTxP3cqDXGYO6VQaU-YcZMFy-hZpaT48CPRtlcIRatSY8uRYW4l3mkGWJ83-qNuSWE7oKFUWvDbCQqOEQkNljg2x0mYQlLhMNMRuZhc9X11hcWFgVv7-SKiYJPT0qmyJyyUpWmmCvsugtIuITZWL9T4fdrSDaPsj9Sam3CGaVBnmF3eDDXggwotC1V12YUHifW5WgQ8xJCr4m_z7PH56C2a7lUOhIuRnpBMTeRMIDAlelHg7soZekXXVehOi_9rdK36H0l4zLXv2de3EbbjsRzwRTm6CysnMNPplx5Bpzpkf_qCeckFj618nG-WZ4zeRzKi5KRSZSi0XsFVRIoIDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acMwmY_m2QHXvX9J7aGYN4kFLccmr3koh4alPFJh2zcNbGCv9i-4mMpE6WHVNNm36SHn_zPgWzgMpPHpv0sOQqnimQUu9ObC1WAuJdKpbcj6p4SsiJ85toY58FnVA711S1X17FVeNGgIUNl2yni8RdHwTb4noppquQgiMiFJE3VMIm77F8hmYqysiFoD-PPKv6aMWt9t4ts61EetNci4Ckfij6w6QM-e-z_o-Li1DPgs9m3RdkhDFKyVMRyf9Ch7Il9yLe2RTUblgJXxNJL5a7fQCOquBuBQ0TChRToiSLi6est6VPXpTaBMYuKTKdGQ5vzRG51-jySUTY0CgpoBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfieLQy7xlCeox6Sogpn3gg9DD5jGmMp1LCgpvNLGny2BW4no_6LBJpDST_rDXxrLIaSdviiB_HzYvb0oiCHOdeH0A91du4-x1ct1FpYjbxXK36eLA5sNN4Fl9rRpfkBl4sPIcFkrmXde0JtqqgRqdN8S5_UidjvmWIP54DI58aGBIxzdT4IzVA_GRO7KHGkS2C5YxQudWFRZNjArJgfMuiBapYhA1zQ3KX1ref0snvAFOviJxgrj3FVjIXgnvqowDO12zaaNQJ0vXsDT3P5MDj33-lehTx0qt_FuW4yhL20oqO_4Szv4tklb4ve-RhnwVKgXil8KWUnEOtRR12cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIEcjhHbdTv3vBvIL8xU0UlX8F4saafp4Ca9mI1rvMbOK-tzdMHOMg3GOalffaiCEc3nOFYdTrHtnh12S47pqprelKAaXKtDonkwI5QDigb6AOTCZXOeQE4nGiqth2RDYM1CxeE7JCtbA17vE_vbRjrvPpSNGe1vfukuFpjZMGlPCvGMjFh3_I9_iNeffeLP-hAKkK1iCDtjnxhjp3HMyxDU6lGAVASsReRHNuuHiBzyVE-82e-f1wIg0c3NMtmP62XIEJFHs13Gyfy9OqEvwcfg3Ec5_MsteKJLrQ7oBnvCJs31pu0WDFXrUEGwTzjiLcAQ9_1Jgma043H0vzRHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-A5xDyOiqFp7gwKUYHqB6fB_Y0gfU0WJlAZi10MVfg2iSjXuXdrLyXFQT-4V2oE1ht-J5D-hQD5UhFEnH6zh9jqufzlHxU_peZnuYPD-d4T426s-okNRjtk3bvzCPKf8g7gzFE3fJuRcgeXqEADTZ-5vR9MkJUwDlWgQVGemYpzd9Flv90bTcOh4x7qnc6CCaq3uPtFRtk-GyXgx3sLcfqcKuhufxfnTgR_yaVNkOTg5RWEy4lQjQUd5pUEAHFouMD2UfPTuKNqOnBrkZH8dXJ4cYhd1G7Z9cTEc-D7CqsorbKo7BNUCqhFA5m1hCslY9XOjrtTLRhNAK-DpNKijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apezaiV7Td9feH6vMC5ZDfyP2aMfTq703FNcdIfecrxHbjZz9z1bJDR3nx2UpZ7B-mWvAGOoGaJ4DhkgfncAtAgfrRrL_G7pt0BS8eAarfflUmjd0dkpeqVIdivOqWpZl5fx29Y5IE32ZcTIpucELkYBi-Zd-ZPcnCiFQ3siQOwFVnT4zY2X7sG7ZP6E_rp3ZxWeoINOUgaxGZZTbJSpgYhlT56EWYR3KyqIqmXDGJDO5sIYEHoD5gGJmiGMQ6SK_cApxoqpLeb5EwDFM8bCJ6jkXi15LYNo6kPhS5n5ocGifljFXho7qSo1z-mvuw2GMmmiFUcO2FCgacj8HRPrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezcw4e2NRK3rflNdIf1K7EpTdLUfx5UwHEv2vrJ5TyJRup2eAhibKfLNkRy0DVdEMBdqx99saCqXCl91ry-CXw-hdTRkBtsBD1EwuKMhG_A5Z_-hm6Q83mRo9reIWh3EtMNeEPFmEmmb4kYFHCTbdkcpLvE9gFPwajsKCN0AF-BksdoVHD-IMniaubXpVpauvDf1wtZDMXXVewor_eZ8FEvtSp1uche1XiDOAjZGRbt3m_4FgtPDB8MBhQ9LIsCrlo5eLTmZLYQ1olEohFyM3mDkXZmtbkcu1wKfkc15saxz8ggA8Dh8Aoc3Md2wH_Z447CwKMsytr2pKZ3Q1ab8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1CG6TX64oKXNj4S1t5lw5K-VLJQubGERaNJVKcx6fGBnLi8kVsi8W8xWQv_iOTpyQWhN5d6yBtlynqFCBWDLkGx3b_O0j1uSBVdfJEkwIwYWwib9OtmUDKiIMTILZLPbuIjIhMC8Px6P34rMnDBynJZ6DG0RLCCBaLGPe2HM1gazFSlWBUT1rWkFSaUxGTQuVjYW6gn-d1CdjzM5uP-gn_rI9NPm44OY27UjstJyn-l8Cbu4lUQSCi_XDVeY5yoRal6KCzRheRvHSJTXa7GjD7A95rFzQODeqWalZQIASmdjdKhO3OtPHTf18JpQsg3c5OjeZD-kf2LCPu-djS46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqL45u94PvgtPTLYlRyKf0SSMUTrAzxZh1OBcXwgpwepr3Hmfw1vK_oggCa5MVoNem_8dS3ElNoHefE3hI9wcH8rE8am-c-rX_c-7qJYQ5DMvjtaH-CXB7j5i1YW9c1u8qeETxwoatkBg-ASy4SPX933Xf86rPiyFW0bDh4vV8RvyYYRgSsc7OfPIC7C9bww3OJ4rK-Fi5xReH10x3r2Pob2ybUSW7SNE_wHC1ltiW3R-_zyRoqbk_l4OJU3IkMLMKpa75t92taMMKa7FvazX7Ctxm1DiY2fg29hkm-K4UMOeOprOxSZZKy9FVCPNj48zqTW5tQBqfBusvrl-QMvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUdWVku9huh11p8JTJelasxMwiRHl8l7DSn5wVVlw_FMbkLUaPm2cuAeGSG_XlH6JEYCJT-WcLBUfHvl9OBSEIU3xC4a744iKjuyL26wS1WXBx2TZVwBlbAbt_J2tdPVCMyRxgqgHRPR1kLJETmVZNcu16dOB9E8_1lVxZyzZw2qTyFfeKUw4xcA8zR4eZnMBiZJekbgw_0mSyoiN1n1Tr_mf3vXCBaTNEiQ8eYd5TQfsB8t6hAljMDwgODppWCxdJZf3bSFQVcVg01-AUGWWalTJcXRc2Hlsemr-VR94DHLTIeAd7Huu-ZECwtiAClePeKfMtswSIsqSDKufDNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhI0M1DbBSibvDckU_EwSgFsqGWCUrdrNCspWdA6D4yHT_zx2P_-2V0XmCTUV0eHFtCgoXbRyZRl8D02PSOE6xUrFCqkn35fresIYiyGK_wS4YgK206rAKx_XOus6iDxw9lSryuos24fqQvxT5QgGsj0B6oOGa_KiqKrX66fAFcFIdMS4NZ_BsztqdxFVknM_86w4fLoQw2NXZZegRmRvi-FH7IVRerd2-4WBR-PqqbILaRYMB6S-jH_WvsGIfEsGb8vsp08DHucxvx0jjwtfdL8qcecUjxXQjyxud8VXlNbbI6cX1rNis-o7mr-QQ_G_BceWJRvBrgXhQ9evR1KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkBC2zRm8pUgNbCADO32LFbkd9_lbgnVXGDlTlZSzZrlFry9MF9iQG9NOe2b4ROgtkxhspkL-oPEMocO2BvmSuGu0YQsnkQaMCKxuapNoU8uX0j62BL_CneRmpZINck5nC9DfTQea7ctZGDJSb8CT3zYNHQqnZd0pj22o5kqEuYMYcKD-SMQYby6rNRr4e_osIknG6sqng0U3U7U-eu90KgIlU_AQuf8ZjCRsaPlO3nyIPmLZsc-AsasznmXyAbNylg96egLJ6995PwOtzom1LSvswa6OMrqlL8RYMhhJthWLT3L_QW4P3VjQFEHUGUzjYZ18KbqpMyrO3_Fg7NWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9trSUXJMlSEAqijPqd6RObCOLt_GRUAHRJY7nKHAi6p5KRWZISlLzWkioWyyaBnpVOMhlmO_f-zT-eL_4sLpQ6m99txCekZGx0cdj8jnRAfvD30DUdrIR63VVO3d2qxtPfIZlxF6xZaYNE-IlsNHBeHltnswF47GnIRzSxpg3mws1wUkVa-LXojIvARwnZ0rIr_Hk5qtGABkRqvRCYx_fm_6m3abvNYkpnvbvA_1cAriQIzbfCQRiSJZZzi3apVjB0-TGQlU0svnuJJzojKYb-RkTvu7cvjBTwVQblE_62qEDK08nULBNQid3ox_m_x59LEcJzcNTtU38Qy1-Y6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxNfAN_I1UeaYlrDIVXB1PVpmY0djg0QxPjudkYKU0KzRlcHoZoau0Hv4ISUR9bqgDbYcbJ0jzQtHin1JpHr-63pw_s_iIvRZNmbq4J7qhJnPxlxNsToyYws8x18fZeJEtQ7PmbT6Nce2Vy4vvXHNCbCSd4I6TqpOqdROollb3Yl11L31rNeDz0Yygy7BUvtEY6fdlB8ZBkYgv2hhrQHKTD_Ya0E-sriPlVNOm6ZAC-UlfKQYayVQGgabjyu9qy_uYPT1SquYfxcuj66LT_EDWNPu6x4fcpv9OKptlA7ZlpRI5Hhx2AmjDf7TKzhvkMpuzl79o0MLlNlNUF5E8UXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwYkL0ZuUJGzhIZDgU_8Fb70mGyTtr_MEVNQeT9cBlxp-FroAkxYzZ8BOhzKva-UvRgEgC6_uCqVDzC8pr0qzJb8iCu_O1JHDOHFjyFBplMWlo74B1SaJILpTE9X-Nuozt-soFJiZWR4XxL_Lm7MOS7iSQMbLvGE-K-EX5Kp7o68i9cWhAI0qv3rBgKn6NB-n8fexxuO6VkoRJzfuXmSuIcdRw9Pu7WFnHys-j2nkYhgZiLW30wSCqKp4_KI89via69sOJV3srDneQCrno4JCy6oPvzxdUcJnmrCG4xL-JRqI8J08HxNgfXaB-P6Mea4JvibAv_sOZM31uWtwOI44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACq8AQmZ2vSSvQdROF40AZmor1Dl3j-qXpuVzMfXcBCyL8pxwN1AUONxDeE-ASrWoENjRDJP8CENkmbrnCdb20HHiUJX0Y5NUR_Bi3xX0BfX8g6e2q6Nn62uVv_RHkmGQ8Q-Mhxyz4BXYleytJGe68SmQE1clzcdGqI_hXl7d2OxvYdkIb0g31Ohw8lJboPR7sR2Oq7w1cp1jPeavFQSWD6MnbjKaUQl8nsmtuvEFBxHwJ9jJa08hjpWbKQzIlCXgrZAqTgGQJNpsHjl0uIpIoGTsxDb1fUuyKU7ZfXnE27rbCaUwLqDsMVhRMGbplCXg4OiA5QnXPykvWkexyFkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=D9FvzmsJTnfkbN-SQ7HHFQSkkQFJYruD8ekNXPNGdvro5-vh6BgkBWlxzjP30zql_iZfo7Aew68PtCnjSDhezNcu8pC4CSma_mtGQeNFD0i2Dcq9VVT1wp9kjoLN7DsxZYzS13FDtetduZT3dusFLQ2Pn7bbG-LDARsNdQcjbUc-GPO6wd9YYGiP7zZMQ7mKBZTvRZYahJqxkhEMsm5ochYmSkN-gsBl8FXq7SKap1hSAB-TOjB0jLBt_CsoRTEhOVXwXLiom1Z_1BiNrIo_-AY9BIl3f34u8EVEpI1qgkGZUAmLNDIEPt014h_GyZw9-XIJCE4pFKdNVutguVL83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=D9FvzmsJTnfkbN-SQ7HHFQSkkQFJYruD8ekNXPNGdvro5-vh6BgkBWlxzjP30zql_iZfo7Aew68PtCnjSDhezNcu8pC4CSma_mtGQeNFD0i2Dcq9VVT1wp9kjoLN7DsxZYzS13FDtetduZT3dusFLQ2Pn7bbG-LDARsNdQcjbUc-GPO6wd9YYGiP7zZMQ7mKBZTvRZYahJqxkhEMsm5ochYmSkN-gsBl8FXq7SKap1hSAB-TOjB0jLBt_CsoRTEhOVXwXLiom1Z_1BiNrIo_-AY9BIl3f34u8EVEpI1qgkGZUAmLNDIEPt014h_GyZw9-XIJCE4pFKdNVutguVL83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLzkzQcuk0L4oNfKHyg3mQpDXR4szGQa1tsvNqOjMsC5HEl9slTNNJypcYd2bKmb1PlY6n4DRSy5_WP6GNWMEI_bb6N8qZaUdzZkEC8hCsQeGstzGzGl__xSCQESoEEc71qLP_86L7e4c7oBw7416bGmpfXeuYryTsEZ8usk3AVAE444r7PJc9FsY7I6l3BZY-QohrcIARKvqC83QBis11jYztD7hP0fklOMekl-HWe9LehA75h5UPEgWXPz5n7XYyrCRhGhSE45gesG6K1aytaT7576Gobosz0bz1nMun53Ejwh8oUsmeb9jx8W7sMbJ5-6uB9xjU46o4xlSva38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=t-OTlg2nG86SoX0uepEEQ4bhGLS3qtJ3ZmLOTxh1SvTZKqc-BcdE29-4tGiJB9nyYjsaFklOj9uwtA-u3T-zLjG2cMt2rXw-rg0oj8vr0ZNkYIp12yCT33B_0Zit0o4ACpggEiridNo3iNm-4n7TzslUkCs9o40TXlA3YjpC0wmCoBdivXH_yo_ZUpKo7buUQPl9wThYISstgTNU4axIM9iYl7PovXu_w5LGNYAglSGWV4l2nzTD1SlegMx_rEPOJbRDGJ0D9DGvrJtDq5klqgZt5Qp_dMWTSDbmp_Ht_cHUt4xcFPHyI3t5hSemptPpvF9VedJfpsUfqSeD17gLag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=t-OTlg2nG86SoX0uepEEQ4bhGLS3qtJ3ZmLOTxh1SvTZKqc-BcdE29-4tGiJB9nyYjsaFklOj9uwtA-u3T-zLjG2cMt2rXw-rg0oj8vr0ZNkYIp12yCT33B_0Zit0o4ACpggEiridNo3iNm-4n7TzslUkCs9o40TXlA3YjpC0wmCoBdivXH_yo_ZUpKo7buUQPl9wThYISstgTNU4axIM9iYl7PovXu_w5LGNYAglSGWV4l2nzTD1SlegMx_rEPOJbRDGJ0D9DGvrJtDq5klqgZt5Qp_dMWTSDbmp_Ht_cHUt4xcFPHyI3t5hSemptPpvF9VedJfpsUfqSeD17gLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNpw952YH6LZBjz_huY7ugU15jH9aJ8qvOTlMkxsd9vKzX5HjRqncD3qQLRvTZEg448vXVcOxhdCN2Hz4S6O5A_CZBfLzhlc3-FbcAE7Trln7h_297FjRvoROJROuemPisWtOBHll9qFsdwSBPavGarJx12G6Wd2IQIXQbUAqEL9qnCqeoiBooTNAkEYcC0ZxcGCWkxRyk0mky5QiZoyF20aZz1C-3aCeaGMSirdE4ufcF0TDt9bHsm8mLgOW7GlgePWhjfNDBZCx9k9yW_1AaSdTjWxFeqkRJeIAbCkpWplYBRMJ_kvnzKtCv3J14qr0rQgQ2GhGn2Oyl0rTzJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7Sb-guYCAnel3wzpAWmOD4KMWLQUjQRHudZzu-bD5XMRAEZjcDup6CBNA3qIfhvkMdkazUY4Tyr5DsojlqOaExNY9UnBZtJMjKNm0Fb32TJ0y2C17kvZ8w3SpBv1KF_NiW9S0S6egwbuZUy3X3oGoMUOnW0E9IDMnNgAsjgS_KpRkUlHzp4uFiqMpoVCOZ68ebKmPLTnfnReB3RmiwJUewyUKEWxnu8cg1tocEAXc09TlCknR8sPG5lkRmplrycSsBBgCK-rkIDzJY3hE8TVQ-iFY0pxJSXXKB3kJfBY0VqbN8TLLwevYsUQo380-IG-PMVgmkQvj0cZmzsVGA72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=MqcHie0OiMmFz9x05rPJdwn3UvxbKXRg71y3dndR1pv6Yu7lwmtgk9aj-XaXAE7lI6DronJ21PI7OWaCtQRnChfE1G_CXFjSQMAC7YP9arzDALiFr3fBp79xOkAri-6ADlWk3K7n3HaL0Bhrv9aquGOOCm8DfcGTGtSKqpkTKTqgQGhc-HtJ9PJbFi5UDe5bSP4sf6QfAGZeArbFYCZ-C9A3frCwC5F8ni3N0Yrjb2k1C5Rv2EA5Eafr5qg1kvy-i2JFnOr9ATvMlnBLgFHUzKY1E9BTx3AA3jniU27oMiAAoVWjeLJThYErcFpDPw5_lINOViIHcDo2p6BOhQzPgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=MqcHie0OiMmFz9x05rPJdwn3UvxbKXRg71y3dndR1pv6Yu7lwmtgk9aj-XaXAE7lI6DronJ21PI7OWaCtQRnChfE1G_CXFjSQMAC7YP9arzDALiFr3fBp79xOkAri-6ADlWk3K7n3HaL0Bhrv9aquGOOCm8DfcGTGtSKqpkTKTqgQGhc-HtJ9PJbFi5UDe5bSP4sf6QfAGZeArbFYCZ-C9A3frCwC5F8ni3N0Yrjb2k1C5Rv2EA5Eafr5qg1kvy-i2JFnOr9ATvMlnBLgFHUzKY1E9BTx3AA3jniU27oMiAAoVWjeLJThYErcFpDPw5_lINOViIHcDo2p6BOhQzPgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCIVD6gZZu3soVRfx2wRE1cgJwehLLpYgnD4J_woNeZtJHW92jt_OOjkNKotLpBBNy9ICA0fQDgpBRFUI0otTHP5JnpgwASZOOWvX3lSMrmrxrVuORxhGBimYPPVfJoudgWP8UML3SqlIILt-YXxOywmX4AqR8R1zb4EvaxsyxNSjPzUdVBTZ3PMHEB4f-hxIPrxd6v914PkqqbLPpx5JBA7XkI5jv7UDIMsxxo3BTX2nu4dUG1KjpfEyGFauMniEkAYpIxvj-YmqgVsFMjO8dKF_Uwj4ZNWIbb-0MkuRV6XoOqEiGmg5P95ZWPI6Khv5tbgIA3j8EV7O32xLVkvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jca-vCfJ6rLIzOfp2VX_Ha02vwqeWIFJXG8dgQvp9oXbOhVNUvrHl2iYndCcFJenGQ467ACbNh7mcVxVjBbi-8lC4lIz-sBIAMBXGPxcZydtC0AhS8wqcUfjfcxjXf3WIcO98zK6h4HIj2lupeVe44nUxwuCJ0URYfztVXMWi8chouiu8EjquPMVUaEinZq_XFd0qMOXPlRIv5Y3t9uPQUjXitpCl-CWpUqSK6dlkhNqMIWjXFu1jDXThL-Bq3FbNILyREpUPcghhB5Ye2Y3oEFa1PpLFVUp-K3wNfCzAsGiGgogG6Ua4znD888FoNB1V4cNvgjG7c0gCvnfZojkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSso1mAsvxVWZBFAq7KOzCit32HiH0_mg6UOTJgkgwwNrk7b6cJbBO-qGYOole7up4qy83AiIjo0wZxgRR5crR-911bmIHeKcsKjpZVr6pLcjf40sMOcGE19ZeSkdtZKYL_VXJIgIPYkdO8RYLW_HuQjNUTAbeuRcI5xxR_pnh89Z4bWNL8wWOaJz6BeETr54EAV0rSCofiAMYdfNCD3S_lIr-0mcwbccUX8kGWifP6P72ZktWDZxyh_votj-NBrTFTwetm2npuRma5USjaPG6hhJ9AfyopBZZKtHTk6DFSz9KOI3eHCwLOjS3PkLOtJN8IOO6vpcW9Fa0tqG09zcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=kMoOzrQUnHEZFQ3LEoWIeMAgnj13WwzDM2JM_WxMntWD3Vr8KagLmTUYNxh_dC9gnxBTuyDmw2gGxuWKkWdEIcfYSzvmI6DjhMNsKJF-FkVICiiPxCetpWUZzzopF9sK2vdNPoAMa-lPpIEy_gRc-Td_dzKu373j818WIpwTAakQTtaFIwbvvFRQDPB2WjgnZlchc900ts-XAcuPRzHJWqjRcesF7sZNfF4r_B4SND5rcDDSh_tu89i8nPfOYxVjpZovwcHzBS-JC-cy-R-Ge1ivk8dllwSLR2R4WHyIKot8uRvbAAzFOQyc6NoSni7HnoL0YRnRLGWmKnU5xn2lVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=kMoOzrQUnHEZFQ3LEoWIeMAgnj13WwzDM2JM_WxMntWD3Vr8KagLmTUYNxh_dC9gnxBTuyDmw2gGxuWKkWdEIcfYSzvmI6DjhMNsKJF-FkVICiiPxCetpWUZzzopF9sK2vdNPoAMa-lPpIEy_gRc-Td_dzKu373j818WIpwTAakQTtaFIwbvvFRQDPB2WjgnZlchc900ts-XAcuPRzHJWqjRcesF7sZNfF4r_B4SND5rcDDSh_tu89i8nPfOYxVjpZovwcHzBS-JC-cy-R-Ge1ivk8dllwSLR2R4WHyIKot8uRvbAAzFOQyc6NoSni7HnoL0YRnRLGWmKnU5xn2lVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=mCZ4O5p-ks5HU7prDSlW58Xg7DBtgx0jGUK8hKIMGS4rhJpueSMg4EEfV-H1nYc4DP-RI9Z8s8amd-FuhvP0OxVZtsOfHUKSK9U5Ht5TEIBErS3BlFHqX4Yto_Csw-_tCqEUiqMRB7NmauLEWjMEJeaBH-7wCn_LqMHFrs5C-VSuSYyElUwzS8-Dty59UHF9iT4XIJUzRdhjSpftGLcp4T4IXjDpoxSG7BUPh1CPv3cutggps7IUDrXcEwqzXfoNkSb6X168rwaHKXrFBFNmHllmPr1ImkkUgf9j-YQ7aPW7jQ6ItOy537Cfzwny_K_trZMrVjwpxp_Tf2ZIfOAXjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=mCZ4O5p-ks5HU7prDSlW58Xg7DBtgx0jGUK8hKIMGS4rhJpueSMg4EEfV-H1nYc4DP-RI9Z8s8amd-FuhvP0OxVZtsOfHUKSK9U5Ht5TEIBErS3BlFHqX4Yto_Csw-_tCqEUiqMRB7NmauLEWjMEJeaBH-7wCn_LqMHFrs5C-VSuSYyElUwzS8-Dty59UHF9iT4XIJUzRdhjSpftGLcp4T4IXjDpoxSG7BUPh1CPv3cutggps7IUDrXcEwqzXfoNkSb6X168rwaHKXrFBFNmHllmPr1ImkkUgf9j-YQ7aPW7jQ6ItOy537Cfzwny_K_trZMrVjwpxp_Tf2ZIfOAXjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwAVwEQ4vRzHwW4nx9dOJio3cH5YkyfyaNJM4-p17Tf1oNZnSfjZeCZNbTysbe0eASLdPEAPo1-ci10EN7N67vpcDizop8ubaAke1Wh64rJ1w5cM25AAnLaKz7YLyfJxxeDuNsLQM01PUOsnBNWBkq06W2OrAzgawJgB3RMCz6ebCCcII0jfhzPxDlzpj4Be1bO3tec1iPdwCVJOgtnMnl2xQTVEzIk5ynSxe5slRhNffDUYJXYrWpxL1npImmtvGm2EpHXPlxd8pLtTDw2tur7K_NLcA5y3z17BFeVTfhELuqL8fCyDIBbOfpTR4O_2Pi_TQoGsn66xV4Q8N-rc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op5hEjkLLZmBY1SfpORBXKlUqLFQFUi90ZsLUYcmVxOgDDIv_WPTGjSTSHhsdKPfljopLXuLwgfTxjib8Yl3usIn6HrOrz644Pb_8AMU5MQI9K_lh8YLCMcCdSWNFgRY4pfBAQeHF2mHt-ziXpsR-C3EslOBiNJFH6rgYPJksx4oPBsCE9eKrU4ACAdlzkdJ66fcocpSf3ee4nT5JpV9aKorqhJjsJQfDl3lj70k0WvPf4grP9Ob_2knBsgfpvfryyQzdZj42nnZZL8d-f2yBJbGeF3zsoBzJI7WC2BTeMd-VTtsL_2Ns3on9AlcW6mRCYlENx1ElRghWZVUKV7Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e21oi-ZHEHCdUbp5AdgGGspNx811oVSpGJFHENwKL_bAUkDgQW5VWkivd2bfcJ8zHhT0KK4ea61-neN0q2mHjbyW0hsWksr6mp7Hrh7aWrQZw1t4VaD7aZEPPCQB8IABhfMM1Uof6R32BPUK_7eZ3X4EuM0RprJnBMByWIn52as8TuYn64-12YZirFOn9uGPf06oLOvIUsKagSQ3k3W1R-ufQtfrJU96Tn4EYyu0nKBbmJwv17wuoIY5FRhmwYO2gov9I11c_PzgFojHmWh_YBkKiklSCwN3NiIh2KcKTjex8Q_ozaoqAk2ub9MabOrgCw6RTgdjwgklOF3BkOsY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjVxnZI7I5Q9iDzVIGAjSgbwen1RQSprBbEA85zZzi_2AidMZ99c_j3nTWPCMRIFJXcDEMO2BAV_SvwYmQ1dVPh1YIrqeZEpzNJcQlYQuWJokFvVqrv54u319h0EH4TS_qZDiXEJDQs6b_ja-x-gn5jaatLD_SvxWJMSBB0C81EOH4Zc_64UqlWmRQ7f-IQBXizBxJB2DnuTaut8v5Vva59-E8XHUyOiynMydqhYVrZoAxIKD6Ug3KCsjFRt5DfhQLzZ29KIzfkHyJjj_fz34kD8Wm5Nzzt2VXL8viGCELRO4R0_takMXiiMsqKZfwrjDKbeWczn3z-lVUZlMYX7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXByNAvvWidcu6l4Iv3lXa2x-K1wR3Ij7tdmT77A1hW-qMejG0Ac0FzOBgm09yjGpoiWAErJdW-yUizxpPkb5YF2QJX2OEDS0twqh6jaZqckD4a-b6qVmc5rskU6Mp5lo6AYlef4EKKqWnYfs-ygJ9Ryp0xlh5JLWsu5FbAjW1-ApO2y3Zms5Q-nxYDON382I5nBVFIx26rv2_OvSXgl-agWgi5gmyYAaixOLRx6U62EeJ4u6L9tZppwhUWXxC8qSmSQKXPdNqpx0U_-dtqMCs-Zc4m53Idm6btF1xtRB0pGgpP0LGBPHUPgg6o5oyY0GnooSc4zz2J0WenuqAb7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfs8Bp5Ac0UddR03D8irvtoGSt6zRzJblf1e5vpfWc41iarKoZhNgVQCVYKQq7cuU9S2mJoASTebt4DmeHhPMMacEXlQfqCGzq78WF7W_me5cjb-MRFDWKMUM9y9huzc8ECotoXODMGRFQI6Dzf6LRSSr-vl8u3MYlKdfwiViDO0FckuwG_G_ZlpG4rWTyOXUX1x5tLx_RSwvFSxrfSTdYbUulALm_uT15CEdYSFKoDa1_AXhQrMY3T-Q4b-XYh5i1JUEoxB71EP9WP3J36f_OLe4Of56NRF9qhyLj-w7EdAcJyi07Ek8Dvb3q4zxgUcA47WK262oE-JW7-64owP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEe91tydU8V4rL4NTHXJwZ2zRfs3dZ_cl2ov-1TdrIwbxjgg05DL87ng3_uKd69cV4XBTlI5hQxTTAnmtBbv2GBNWu9UExrZpwl44Ox_rJSE5Xih9mqdLs2QzzA0QbQEgclSI7V4dCP_UuunA3jpSeVfxlcmYN0ZrEyKVQySHoif9wlglVhcpbhWdos72xfS8ObkLpEB3CpzUgZD48xgsbTjGx38jd3Jll_Csm3E2jP3sFOcHcYMyFf8_toIn8Q1u7DxAKjFo_tXmFC-1-dNBY1vaWhiowUpQvvEMy6nhoZTwWYyH25xfw_CGTFUUoqBxnuJVNb1UKNVIC_7E3sABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=J5GXHjmfBP7kROnPunD9ruMqFMkKV5ixWUrJFOGPM3MMMCvXliZ59ADmIKmO92dRPb7aiTAIFV9tX-EJ0TSfXBDlDjCB-jbCZWWb7wNpmddzMU7B3CKvbG3JFudUlU1wcFCt6rqxlF5eym5PdI4AMFxDuNDqP2yZL6Uq_j1c8PHAFM_tBlU8-aivrhreD6QMpeCYkF7Aaf1GreCu8cmYq8D7RFeWayexSCKqPA6Ihb7fk_UoLFbvfzkyF7bl2zqEc1LrdYRp0UwqXohGY35-xmpI2Uy0V0afXRiWzu8LMi3ZqIkgDxAGTOyVJ4Kvry09tdebN6iqoLNTgCQywBZUgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=J5GXHjmfBP7kROnPunD9ruMqFMkKV5ixWUrJFOGPM3MMMCvXliZ59ADmIKmO92dRPb7aiTAIFV9tX-EJ0TSfXBDlDjCB-jbCZWWb7wNpmddzMU7B3CKvbG3JFudUlU1wcFCt6rqxlF5eym5PdI4AMFxDuNDqP2yZL6Uq_j1c8PHAFM_tBlU8-aivrhreD6QMpeCYkF7Aaf1GreCu8cmYq8D7RFeWayexSCKqPA6Ihb7fk_UoLFbvfzkyF7bl2zqEc1LrdYRp0UwqXohGY35-xmpI2Uy0V0afXRiWzu8LMi3ZqIkgDxAGTOyVJ4Kvry09tdebN6iqoLNTgCQywBZUgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=s9mskg8seGQFvhB9N54SQQ03VhAVo4zjFV27CHmt9qIzlwmMVAuaalw0zcFFbWXzOBS-jBtlL2y5uB9_bf8kZYxPAwAQARgxzGys9CpWxnzrSj_itz37xoqaj25zqoDsDvrZ6DJzpzuY1Ph6Kk60AFpeJ6PAyZ_z1fF6svW93IlI11j_vbl_aDcYMKog0ZterbA04vCC_pAKdQM7cxNoyFo1Zew_t2GS_4afwSqzwBx60Q_MFjYKozwKNvGJS2CrD_gNC79KKX5LzU1zjCqZK7i8XXtJ0lSqW45E7ZLU-lmIx_RR2Z7mUG4iOL0hlO-CAo4eAocK61DDO3EIV5K7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=s9mskg8seGQFvhB9N54SQQ03VhAVo4zjFV27CHmt9qIzlwmMVAuaalw0zcFFbWXzOBS-jBtlL2y5uB9_bf8kZYxPAwAQARgxzGys9CpWxnzrSj_itz37xoqaj25zqoDsDvrZ6DJzpzuY1Ph6Kk60AFpeJ6PAyZ_z1fF6svW93IlI11j_vbl_aDcYMKog0ZterbA04vCC_pAKdQM7cxNoyFo1Zew_t2GS_4afwSqzwBx60Q_MFjYKozwKNvGJS2CrD_gNC79KKX5LzU1zjCqZK7i8XXtJ0lSqW45E7ZLU-lmIx_RR2Z7mUG4iOL0hlO-CAo4eAocK61DDO3EIV5K7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=JNCmNcJ-qs2kLdbvsZVi5-_Xw-AtgnQ6iLuz8Hs-kugfw59rcETUFUmHEzrmGc-4s1wjPsGp1aP2oWv47-Ai76h7OjbtDrk6qFRFHgnMos07EcIDbNoIYEEF9G0HaGPHp64xUBp_jmuxyuHmWM_PLcjnWlELAUJiBC9KdE1n5W7n6Ab4nNwhCrdhBimWGF011uxJ-CNwrwvIA9C3nQxfV4etDEdX-EUzhOlJDtSXG0KqYgcpkyxLHNCwhR3C0q-HITEIH2tQ2bGPe6fXJO57divsEm30eylbvB3Cb5qKj5NYf-HzqSEQGAj4qK7nogTkM6ZEDw71ZVt0G0bXsmcNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=JNCmNcJ-qs2kLdbvsZVi5-_Xw-AtgnQ6iLuz8Hs-kugfw59rcETUFUmHEzrmGc-4s1wjPsGp1aP2oWv47-Ai76h7OjbtDrk6qFRFHgnMos07EcIDbNoIYEEF9G0HaGPHp64xUBp_jmuxyuHmWM_PLcjnWlELAUJiBC9KdE1n5W7n6Ab4nNwhCrdhBimWGF011uxJ-CNwrwvIA9C3nQxfV4etDEdX-EUzhOlJDtSXG0KqYgcpkyxLHNCwhR3C0q-HITEIH2tQ2bGPe6fXJO57divsEm30eylbvB3Cb5qKj5NYf-HzqSEQGAj4qK7nogTkM6ZEDw71ZVt0G0bXsmcNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=DnKeNUjYbY5BmtTvvh-nT39U5LDC73Qme6fHndAyXnirx-5DqI3sKOrI2p-a1wmDy2JmB4of4LyyR22Z-aingJ8KLxaFRMMdH8sxu8hmkjBGcd0v811xzpT2E8b4-3tfIcRu3pbaZQd9yIuwYIe0EfOwKUzq_GSSXamM142s3g6ldsxJpFC_E2mI5FTwvtoWViPRIZl-lzBc52zCxxNSa9gJiWLZaPM_5MWdjy0_Ns7E0PeWYnUfYzBWFnUI0sH0PWZCr3OhJjRJmR4iNEifzkMZfgQdJV0KzqgiQ4pOPSyGREANtc3YKvFTHoN328i1NcsQ8YCBc_E2hyJzTyepGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=DnKeNUjYbY5BmtTvvh-nT39U5LDC73Qme6fHndAyXnirx-5DqI3sKOrI2p-a1wmDy2JmB4of4LyyR22Z-aingJ8KLxaFRMMdH8sxu8hmkjBGcd0v811xzpT2E8b4-3tfIcRu3pbaZQd9yIuwYIe0EfOwKUzq_GSSXamM142s3g6ldsxJpFC_E2mI5FTwvtoWViPRIZl-lzBc52zCxxNSa9gJiWLZaPM_5MWdjy0_Ns7E0PeWYnUfYzBWFnUI0sH0PWZCr3OhJjRJmR4iNEifzkMZfgQdJV0KzqgiQ4pOPSyGREANtc3YKvFTHoN328i1NcsQ8YCBc_E2hyJzTyepGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=i3YPqFF6nvSTMI4rw88IbS3WdmL-qhn1rg1rmgd612DZql8L7RmzPd_rfvJao4qLv8lUsP4qhfUt1AHFSsAhsGbcq_EYnRjz8O4mxANfC9QRBCjZ7JNppgrfYnNZ5ZHbjEqXGvpZhraAl_YHV48LTzBdJfsUR4u-gqHmRgGWXd9CreebOp7ReI7DKVa016cxVpMftCzujS3xyBniP-cLX6TBkxbeKhOcWqiZJ80bbiAdjTXsVm5XBYpbtPWoZJnn9IrS6Ro-Bruva1-JHDO3qWxVvm6M_CClpeUQBLJR-7Nh4PDa8whwWkh0o0E0H1uva6dH9xnOiSoCeAIRkTPnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=i3YPqFF6nvSTMI4rw88IbS3WdmL-qhn1rg1rmgd612DZql8L7RmzPd_rfvJao4qLv8lUsP4qhfUt1AHFSsAhsGbcq_EYnRjz8O4mxANfC9QRBCjZ7JNppgrfYnNZ5ZHbjEqXGvpZhraAl_YHV48LTzBdJfsUR4u-gqHmRgGWXd9CreebOp7ReI7DKVa016cxVpMftCzujS3xyBniP-cLX6TBkxbeKhOcWqiZJ80bbiAdjTXsVm5XBYpbtPWoZJnn9IrS6Ro-Bruva1-JHDO3qWxVvm6M_CClpeUQBLJR-7Nh4PDa8whwWkh0o0E0H1uva6dH9xnOiSoCeAIRkTPnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=idI_nKOdjKSaHhNEaHhqKrCbmRG3hwbmOw9-fPa9iNT-mFkPFXMNLl8glYJpEkMBCH0XtcMhyqMVJ9WNE2JphXfHtWzbZjqnrEncP7yl35r3irlpGetFAO9mQrRZN0nI3PTCCXGAPL9cyVkEIChfk56EFqvE2hDI4tR4tdInRaFVeeyH0g0owKUm93RRXi8NdSHuNr5SN8G3yCHpBm1jjhIAfHvkUf1Df6zTS4WspgARt4SDRBHMi5dMnCjrbuGB7kO7WTPEh6PAq6XPrui5XcxQhKD7lVNqWcToQSrJOYicK6X6AsO_VWXPCznV9c5C6QQw5HvSC1KS8j0W7-j9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=idI_nKOdjKSaHhNEaHhqKrCbmRG3hwbmOw9-fPa9iNT-mFkPFXMNLl8glYJpEkMBCH0XtcMhyqMVJ9WNE2JphXfHtWzbZjqnrEncP7yl35r3irlpGetFAO9mQrRZN0nI3PTCCXGAPL9cyVkEIChfk56EFqvE2hDI4tR4tdInRaFVeeyH0g0owKUm93RRXi8NdSHuNr5SN8G3yCHpBm1jjhIAfHvkUf1Df6zTS4WspgARt4SDRBHMi5dMnCjrbuGB7kO7WTPEh6PAq6XPrui5XcxQhKD7lVNqWcToQSrJOYicK6X6AsO_VWXPCznV9c5C6QQw5HvSC1KS8j0W7-j9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
