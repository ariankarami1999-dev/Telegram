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
<img src="https://cdn4.telesco.pe/file/gXis_16m0au0RuGBYO4IcdNp0Ho763qEt4zIz6wAG5tR6KaltplcwEB-eI8DpG3tpBfYpZ1nU6skjaSqII1N4K_Ruhp2blD88a0hWtn2DLDgNy-K1G23eJFyU8r_aA7IQuECaD9zDwSnzUmB-0p-BimhxgP15AzGXKfq_EmNx4i9WYTHp0ncPHQ2MIZj_MXLfvkV0DVYN0rCyW3vfSjkRBWkiU5wBRzUwqOXgQndDGmPpHuaCSIMYDKB7cH41ZECOiVOmw0EC95K_szY--nfjL1YYBn8alg3_heNBVcGdko6nSesIJZkCTp1gSCpD4utXs-zf_eAF32Ooha9fSBDMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
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
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqvy-PGp_3T0ng4Ysbljglx-XuBh55zHziuSUGYSLmUclugNZz0idfXEIHbhzSns7RyhJTIYbXgVpqh0hCHX8-7tiqGRkeH-Q1FUDszFp9ZE2W0E2PIa7PqSL1GgtHaCEkFy8cFdz5tQfuL8cPPkCWD7FXgPG9jn_y9HhjwdFaguEa-95Ap4UF6hhKrCkaaA9fNIZJhZDRDkQXNDZ5Uk7sh8dVM9oEY9h-5AR11QtWDw1q4BST8ILPyMCeP3fRLQrOLRfZH3UrSHixaQ6O3zpp3k3FWJUKqXRLDA4B6BofqnkT7dKwP9XmfUoyW_YX4dFdqMhby7w0Y0cjI9WEyFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHugfv0kSBOsWiUvMHMvkbVhWUqXemM0MrU5lYWO9tA8YoLnzK28on8ciJD7kWWc-xXcSgZ_SZ6fsCrPbLC75Pj1692RW_RgN14T7TFVWiNUtt1g-Q-pTzR_C_lan6hzCq1tAQkjEUDTZnSz5vdj7QEv5qm-_Mr73IfAmKe8gouo1WICGe3F3YEz6NqUzITRg65RfigKtXPB4XRdU4KIsJgB795iJ9AVCow7AVzzosKucb8YKjkSOPOYCAgquEmZvlZYwNf1aMmWaq5wNb5U1nTnrQvzJp3lh5vfo7F_gBkWm6Lt5k3EODPI9jhRFDEuR_fAjnDhHOQ2OGjnTZQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY5nFjIGwk0H5z8yYdx6FYEKTr1VuCx3amOE066Ra8w5QBHHZvNbQKCnpGKIy8qiBHsEYpZq_G6gK0xy1ZFkUCjJScdwEOlF7ljEHaZsbGCcv-Atsb3QrZDLkjDihXURD4TCDTjOuhwzDo2RreEjmwUWUm8r9tSxlHlmIlUfon3nXoM-W74IJT0H13etPY_-3nn3A1gnJUIKjxoERWgWmLrQpG1H0rXvUhH1aDJRgx2hQbPO9_iR-ytrUrmTx1NDM9Z3f0H1MarUPH-Fbb3IwCENjW7krsdSj0uNCTtavViO2Drx50I45geuT23i5IJL3vKDfKx0S3TQRFiVv6YLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMxyf9YurJ6f4tvYTCEimgCeREawnR_1El8SbJ6lZox9rAFjOZSWwYh2Z8Z5EZ0DR1j_bd4whLz-xLtRc2fbw8zs4YXJFy5pX_eho6PjMzP76ToQkMRN_GNKr7s044QhOjkWO1caaQ1mSkWSoLf6AeVxrP_CZfu78P0T14szFxSF0k96-qvA3OVnKWBTupcPet3hu3ix_gvxYD96Ve3xzZtDehz_8UxqzL0bcfEq7ss-wkIgFTgbYHzMF30fDzkjn4AQYOMfRljgCLMdx9vU4llhYwwC5S9xhTXZrpoVIfS3xBln3KO2vNz-2UuFKOWJa9caNpZdGo8u_xQsj4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqHft56kVzqcBvVktxflgsppdUAXn16bTm07CaSPcnY7Ucz_hqnEVpPC9LgIBThjiE6NgSzc4KRrvAok06BxdAhqq6cSz9n-RR-9oR6f7l2PzXXlxQnqhEkGU7IRiapMzqjlfFiN5POAZFbKeLZzi_fuZlHVtJNY0F5cIzByCUKHxKCb_jo0uYWixMY4lfnxqe9PON2IdB09ixm0fWJPxxVcjltW0CA7Trd7SMGmKnvZtxr5wCYyldybcxui-QjiuYNSo7gcfQ1vIH4U8oZNYEs-3Hf80Fn-FvG9OCIomWck2OtXrcZFswy5OF9z9NoVNJt7aw8EbI4k2ro8AuobPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stL33D372NHb7IB-Ybq_2300QymPj6TTyMecz4EPqxWxgDxFg2ofh5XH1wo56feP4CiRidYLwy1KGp8F90idbrZtwciY2L08HeaJdn2cHSansyrMWy3U8kiOD37fzJBINi7rji63FgjVVK2JifWe_9M-YjXd8MHI47sZZ7uDcoLsLNSTtgMwo67qwvHqto9LDpGlzai_zhSr2na9DVnxKh_6AuGeiaQ1NmyEEhsbBRqSgW6pcwLVp6krJTyehK-agJV20sJOulZUxsPrh8gY4ZK1OILZIhauWYZqMwgsE9uOBSXP8CbVTULCwzhnMHA723j5Xk5DaUzTzawlA02lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq90r0xb51cHTMMMxAlLFuaufFkdT7FjjU7ATHyAaifn01_WnA_pTBjyv2OXCmuA8GLKdvTxTb0kxiof2YqLYXovbAW-Ndk8l2yAB3yqKz1xzr5YmmEbexwDgNyeLH80hN3Op-45rCG3xrJPIOrc_ju6--On0mcKtEO_PbvItIEXT03owyFlyB2yYotKY82sEScgjhvGf096DGOtwozWytKyH8ubtarPH82DXQy6T9gW8jBcZRU5oyZsS5a0yp8z9rxZkmZENl8d3oeLqs0jDbUIavS21YFVxiupVyCWpxORHC9MnXLXe3zpjbmDqLlDdmLwe1BGqtv60NznP6S-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgInJrahE8QEumhODZyXfOi04sEc2LyioPStjinLyWarEYprHp5_-CP87oHEJTh9NlBAi-ZMTXptkyIDHn34Ws7gsZW02JFTc-qfhnm42GXBdcfjEYg5r27NA8z983n2vwCQclO5fKfG2Cblz92TXURkqYXYNtIEChdeJGdYu2q-ubxzgVG_uX4xANLsFs6yQfFXhTWHA6Nd7Z5tlS1KelyTbFEBsm4b58GRdl57Tm2I5MH7H9Pztf7wfBc3I5Wv8TmRnwyHddvBPIRoB6mFvGc6-L6qGFT1slSWeboPMMGAgxl6wQAf2J1DdLGTxjqFz2ZvW3T-pQFGvQMW5s9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Nn4B8fFsCwTiwz5QVkXLq_-1m7z71Ewik5Zgpwhhf69n9NfdB0XH4yQ3JGeBwkdAiwwisAl8jRTsK9yOhcySAoq_6hwZ0mGqzG9Dlfdd5fLuMLbJPCzLB7N4XcbyWQCsRQdqIzVoN6vy26jrrzGFBuUJe8N7EVpg8eHiLbWLYnqMqnimvLhIzmfFVczWmKuLDjmHN_rjaqSb8kLfVp1BqB--N9UC9xyX9yAUElEotkmQhx9GOI64S7CthPGdd822xWr285T8dJXGfxijL0Bdo-1MkRPtPRN--GaV0eP_vwFSE_SLSQjSqUo7aRBm2snzCRMU0lF9rHzUxN5nH4eQfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Nn4B8fFsCwTiwz5QVkXLq_-1m7z71Ewik5Zgpwhhf69n9NfdB0XH4yQ3JGeBwkdAiwwisAl8jRTsK9yOhcySAoq_6hwZ0mGqzG9Dlfdd5fLuMLbJPCzLB7N4XcbyWQCsRQdqIzVoN6vy26jrrzGFBuUJe8N7EVpg8eHiLbWLYnqMqnimvLhIzmfFVczWmKuLDjmHN_rjaqSb8kLfVp1BqB--N9UC9xyX9yAUElEotkmQhx9GOI64S7CthPGdd822xWr285T8dJXGfxijL0Bdo-1MkRPtPRN--GaV0eP_vwFSE_SLSQjSqUo7aRBm2snzCRMU0lF9rHzUxN5nH4eQfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6V8Qrsvd9-8sVtDHofAePe2DYsZsFHqeS4_hMGlMvmTMQ4WX4xWX2iTXAz7OCmo5xP-sS6BBSyamW8FjLZFMTzWMHvmVm0Z76P4QfzeErlCCXzB_MsfiQ4TzUXCgNamxEZo2tZTLSTdu026VYK7YKPZU_4GKvbQY3qDTAm4hFz_MiU9HHo7991MBk1eSl0DOpYj-At8qXqlTwjciNn4kEtqVzuxYeB6J2PixFODBjuVwRM5POTcjl0fkmueISve2nbojUOCzgtVvWl34sRVVqlIF23Yq12BQOVA4mUXYZimsAdLHFrg5jVFrLqC3BObgbgL1cSdmhmwUzcVZR5MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oC_9tT6oUQ2hd7GFaQ09qmgOdw8OA-LbYD7MUexCFkAIhF-OjKCIRtB_tJHqdf-B6W0kTmQtUaoPu15InEMegXXL7C9Pdwt9EuRHrujcmHB4D0C_PG8jcv7nxtoBUzz7oQ5IHTS15YoNxi730GHGqvHAtGcsygPEw-x3C_JU8FpzXtjt4pdxI9jDlLzFl2lUSd_Q_2m3Swp4o3ie7RfSLczzlhx44nIwQgM9HBpOtQGEa6u4A56xNj5YspnVAnVjijKTHuq2pq3rHa19iMJxXyys2yZcKF9v_UkfHeaCMrSbjzAyiIg8W_0n_NcAL0qXPTYu1DAAwVtEw5C1gU8vGIcZnWw_Ok_X0ONye_B2wwztcKRV9-A1mDKkNCoXIYz8LKpEvAbJHATpkt6xtTq3j4XHHP7jonivl7goKQ9ZXCf8yFUSjYAKiUi0IwkP4wP3qBSW5zK6knfV1KLnSREAxvxiE7c8f340NcFWIAM2vv9ZABns23WLEi_Jda3z95lSLxIji3nHaIaOXuAXuQu7ZSYAV4el3-ENlhPMw4VPbd6jpD38-L80flC1cwJ2HNw8VVVzpksuRoT5WdsBbFnGf7jTFJCEYX58vNmZfYO4N6IEyDikIFc-5TAQFbAz01a6cOUqy8yurGsyvUxPyb_o0PXuxXR-26qvG5qpUfmf3WY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oC_9tT6oUQ2hd7GFaQ09qmgOdw8OA-LbYD7MUexCFkAIhF-OjKCIRtB_tJHqdf-B6W0kTmQtUaoPu15InEMegXXL7C9Pdwt9EuRHrujcmHB4D0C_PG8jcv7nxtoBUzz7oQ5IHTS15YoNxi730GHGqvHAtGcsygPEw-x3C_JU8FpzXtjt4pdxI9jDlLzFl2lUSd_Q_2m3Swp4o3ie7RfSLczzlhx44nIwQgM9HBpOtQGEa6u4A56xNj5YspnVAnVjijKTHuq2pq3rHa19iMJxXyys2yZcKF9v_UkfHeaCMrSbjzAyiIg8W_0n_NcAL0qXPTYu1DAAwVtEw5C1gU8vGIcZnWw_Ok_X0ONye_B2wwztcKRV9-A1mDKkNCoXIYz8LKpEvAbJHATpkt6xtTq3j4XHHP7jonivl7goKQ9ZXCf8yFUSjYAKiUi0IwkP4wP3qBSW5zK6knfV1KLnSREAxvxiE7c8f340NcFWIAM2vv9ZABns23WLEi_Jda3z95lSLxIji3nHaIaOXuAXuQu7ZSYAV4el3-ENlhPMw4VPbd6jpD38-L80flC1cwJ2HNw8VVVzpksuRoT5WdsBbFnGf7jTFJCEYX58vNmZfYO4N6IEyDikIFc-5TAQFbAz01a6cOUqy8yurGsyvUxPyb_o0PXuxXR-26qvG5qpUfmf3WY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC2rpgpr6M6hX_gnxgN4disZN4s6DxaORbXklSUphQvfVt4x_gNUFgN_PuMj8HMwSxXWwfX81AGwHAD6FN3ritlnmld1Cd_gIrj5OPbx9SNrt_1pjWhf03dGrWaf5pGD5Oo5Kp6dMxTo8kQOMp6SZABwniw9xmMHa8voDMgvEtLEwaw6JHIV2yYwZOfvAutWghVpllPH_tCnub64eabxeRTBtzapoA1-FHo9eBDxIQvqPgfj53k2GZR8g4XfEQKhyckKv9f_hbyefm91R0RXInPYvp72Em4mpZMAp4pT0gGT5tU-n72yNk8YHwo_1P5sj_M05Uis1j_bRqSPWKO3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Vp0cgyQQcp0XCfvrHheNbqHMu6yKQYg0mvcXG2U1BrFppurvaPTsawCXIiNi58dOFX1L9MSwdvwbwQYxppCNiUmprj0RcP6vF78ENLqNmtpuHrpmuddtRZsCz9UBqkplyKrKfitkozI4djK8FVOIkBt3EK0bJqFIZxiz-V736IddwBKyRrNvdKZugCwFcdKPRtvQwixvM4N1udYzS3qAL4xI7h7VU1FK5Y9pQykXwHlEnWDTVroSUvVSX-rspSSnoKV-C1TcgC75qXkoQJZDRmIS5cenay0J80kEJuCYraVtny7f4S1gGDK8fXXAXr4FkgFr_oOeOT1HMVHsJie46ySKebAfYUtR82ZIU3N8M98IK5XdmEpPLyhD227Qa7XcLehjnXRzOpnvbuTs_Vm4CifdlxOugEDYu_j7eLxNrLSsMw4clpViOkCVQ3KWwJp5--BbXEaqwhJXK51CMzQ_vsx0wGcjcBYJ0gmUWPpk1jDn1Z-9tWtyAugIeqvJTwApTECHPIk6KNZNCHbLRFTt09z4ZDx5GM1iFw6-k66fhjkS3nQarl_0YFGZUnzKhtmqPcqySERfytmWJ9gU3ysojo3WE4yWfkG8OmDpkMeteI4CLxWxXZIJoNLTZUDwsrptlcRMe-Qy5Ei0RKGC0h19BorySaFapv5a_bgYEc6t_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Vp0cgyQQcp0XCfvrHheNbqHMu6yKQYg0mvcXG2U1BrFppurvaPTsawCXIiNi58dOFX1L9MSwdvwbwQYxppCNiUmprj0RcP6vF78ENLqNmtpuHrpmuddtRZsCz9UBqkplyKrKfitkozI4djK8FVOIkBt3EK0bJqFIZxiz-V736IddwBKyRrNvdKZugCwFcdKPRtvQwixvM4N1udYzS3qAL4xI7h7VU1FK5Y9pQykXwHlEnWDTVroSUvVSX-rspSSnoKV-C1TcgC75qXkoQJZDRmIS5cenay0J80kEJuCYraVtny7f4S1gGDK8fXXAXr4FkgFr_oOeOT1HMVHsJie46ySKebAfYUtR82ZIU3N8M98IK5XdmEpPLyhD227Qa7XcLehjnXRzOpnvbuTs_Vm4CifdlxOugEDYu_j7eLxNrLSsMw4clpViOkCVQ3KWwJp5--BbXEaqwhJXK51CMzQ_vsx0wGcjcBYJ0gmUWPpk1jDn1Z-9tWtyAugIeqvJTwApTECHPIk6KNZNCHbLRFTt09z4ZDx5GM1iFw6-k66fhjkS3nQarl_0YFGZUnzKhtmqPcqySERfytmWJ9gU3ysojo3WE4yWfkG8OmDpkMeteI4CLxWxXZIJoNLTZUDwsrptlcRMe-Qy5Ei0RKGC0h19BorySaFapv5a_bgYEc6t_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj7ZJpYy--gHeJasJXfbNFquaWBF1A5A_dnlSIQiTwM0eVZHKH8A_MvWe_x11yFeUgc20jH85Zbsk4W8D222lEv1I3V1lUl9XiKhG0QBLbNPFgqnSvfbrY2vwh8CStp4Q4j2buo5q_1WsU-eHfI_WwIO9pgwxe213qCWGKd3xXCfxbpCK4HcKEMKPscWAz2HGVMq14sGSDW4r687_AMHlehfNWi6p4joYuYYbtSQlmFR6xAjj-IYdn7Vvg8Z2aDTjeNdF6Jdwv_JsfZDdd_2Bb0344fvokDlUhvXtwufRski4sCznz4S-8rcMakh16VdZhvAKcuupWReTQWnbrmxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWP6UI03x6HqPm8VeKPUSsV_ngM_MFcG4tx5Dy3JBrIOPVoONaws9-mEXNG4k1DuJye2VJx0udPkQzmT8yi1IA-kwXel1Lhc60t3wLrJkLoXO9vi59MeT9HInDIou6Veor7Q-Xvdg4FONBw6_HAC8eJEui1AndaE4QqG8uaouQ72uxRXBL6LFPq9kFD_fanWBDvmCJGRF4kBV3iWiHeG7kXRtb5TqmIgwbSY6aHzqKaGKapSdXHyhjdL2NY4TqP4n4Q4YuAuHMYTobpOyGNXGO3AjwDuv9EfbvsVEOtNO8u0MfJHx1OehbdrfIB-SKfPp2dWFgCFr8NM1GhysaXngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCrDQC-sI95pWc2PgusDqHHWvAcdoYbqGQVj-GtYIx_mJbFNUoJPb8iz-JunkxjNal6YkeytDeMmQfk8P6UBYk6oSoqnU5BAcdnjd_padC2NZ9rLzbAAKSmPy89iVl6mFW9_vdLkYjaeOgcFUfLrvpv_TtOJg481w4HWGDmx9ho3XU_1e-eWBD17MIyIBj1CZS-n0D9hgZn7M2JNZDbAWHkSIJUxHSBzzf-bHuoAQeSPlfKQqCHTqKbhGxulHhKMP2zshtG-_d-Vf2QcIfcT5nmljeKxYYgPWBYF83XPR7acVJGa6qFPk59bdDpHS5KFgwFir7Up4W-cz8rGzw5uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRIgoaUjZSEQYw8k2P1w0RgZMMtCEv3JT5w9fvD_wS3h3spaAEHYzuSWikp7WDtNTfPichQ0iveV8ZI4ytC39E3niwYS819eFxz6bh4axMCTXJ2BrwGXgldzytzjbhafWP2RDu0zFjy7d9fOqXgshxSpUNAdo5u58QFuQWr3JjnNY1Iq8vAL3VCMI9ruiu3KoSBrUnIK57OZE5UJTL8YrjPbV5jQd-COIcFgNRRwrflpJZDAnb0dijKx8ic7V5FG_Cya2oKGFbpgQuIfmnFU5r3vIXM6zSlzw9aIHNopXUDFEoLu0wSktcFgW1NRuZzqg5gzMSTMwmqoG307ukUz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeJmIx8frarJEV5_RQ63ftbyl7hySAY0sLfdV9dKf_HwR0Vs8Lks44vvcsYFZbp4O3YDlvd6XN0E2W06IEFqtLw0_b-UuGUysf77fZIOy6hMW6IhCkmriCRxZR18sCPCFf_LPt3QqyO3MntsiPAcM8rY8xDAPUkObZ9ufNzSgqIYxFzn3thYD3hYeMHovZvjSpZBajUTKHouxRbsIcDSDir43btN01T-E0eg0A8B5HExEENKT1nm37bWO5imS4-r4Hp8w-axfFDmU7b4Na5a6DwrPW-Wbd5g19shLROmZ21EwZZgzoT6nAmAjhQSHyAv9sfxfH8RCVKwV7vUHy0qEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWYhp87tEXU9iy3I6gwAjrtY1-QH_VZZ2VFmHQTAJHeVf-YBAtUHSsyoO6YZPyDlJ7rkfQlCsHxk-LrnsXvUPEweVw9lOG9AYdF5oiYMjUZiUITKDJSQir6A-epugWJQ6-jthhwZuz-rQ1PCFaIQd3as8BbqCqMokyp62slq1AYG26DmWnj7kR36-xo4mRWv7I-SvZtFUHI_gPwBx2dpI8KTgZc6b7beEHoRKyXPPdFD_Q0qMqSINvqcXBmYsTupMssjrQtmsAdv17eZfGgrB39E2YfhNOABxSVT553oNJUKMhxhfOUSd26Dl_RurB79P3cx_tgkree-sLlfz-XozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCVjCDsgB0UGfCYJazQHqcQ-6ZoaJ5HKzcwcYceyvVfkkixQIybUsAwZVBgA7DzlYtpRRgbso9PdE0jywDi417dTJ8qlRgEFwgCkxBvwy6PwGawiTuGsJfwShURtcdWFm5Uj2iRbkpCPOh5pBrNK0aHQuRGMccufYEco_b2KDc-gvFTaj0P9UelOI_oMuBWf5cydY_6sGJipcHywp4KKvsYxI6NGwllJWMVBgG5OOlLT0O97IxMBa8NoC5Zh0bKFFyV8gUYCRSisH8viTWUx4p578yYTJM38PQcWZVxuXN0a-kY5hA1cOHyE6Mj44EbWu5XWOxVRbFULX2VBPnahAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6hL8hjmpyeH47r_rRN3NjZKZiwRlj1RWO42JR9X1X_F90LX82He_vN0AzI9o9AYftOgDNYHJigs3mdHGOFZ2U6vnH9mS8c29ZLMl7qfOYECy_BIjkCy8rxqsIJKxtoUIbtcpO905LBnKq4KhLrJ16TQxTNW-WZVsOyqjW3JKLWrULxoDFCeVU0ppLMwDEgbViIqoinP7hQkOrVuXE3hKBIF0m4CWhgn5V_o3Ew6M61QN71VjJuUhF12DrwQHVYBl0sEfZ7qAbpD36NEY-ocHJfV3rz8WfeghjDyfxmqJjxyKi-bL0OsS2m-DoklRAPvE0kLll3jqX1f4WGH5RGyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2nW5gCr4C7QsBqrs4PptbQQcVDlkAacbRgeQ1qLCT1E_L4t3yA7ClkrztTMOd3G36qioguIuB7jmN7qZr-uu_gmywsVAgod9hDlIdiViIxVCjxD7IcRICoyvfUVtbnc3dWshsTsSqDb0QLyacfjrV34Mqxur9O5cdSm_3HtC52ItoVSN16vTe45sHkLZT9r4nqboZKJWxGMWHCQRPADNrBDp3NqnIKLshc8q4BdSvjWRSRhhpheKgZXYhBGlXilRoSQVpvJ4aTjATB4yzwr5aAkTmHhVcQEExCgmycQqU8B0CR8uaZEGlgG_cUZhIoTAYaz7jrobSXI_DjXAmaKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPc-z9q76R3sPFq208WXNTBIBQGqN-a-HfkjluMZiCQsCHAqebTOBOwvTstUAhHhWYJkuKnZ0j4ggxxL3M0FTOaEZUrlAnAKtXDbLsHSfUgVCqbctAg1k1upmvCNyio5NDP9Dq_eqOVEgsL7o3FCuSeLUzhjGR493bflnVTZEGoJlSNiuwVEFpD4vMIXehZMQKGw9zHAsWpZtwptt7pi0nEUCm-KSXWHpqmMTXu2C6EeNbtaAotIK592GBNPVKYDUIuWIUI5Vg1RRkM6RRubPQe8VyrMaY7jUcQWM7QMXpMi9hKArgtLY7ED38aWeIKSz5w9197pDbfbbacGv0SZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZDu_icODeNHKfb0wUGB4pCprTlZOQ1YAOTjazcjgCUr6VwjRSE4Vabn3eyCn42LD495bCrVHXholVeOXNXQDTT-9cYXad_vhvfzgEAHi5V4M00OO2O52mZsylRDFXhW6nUZu4Aqvzu7MEuH6AAoUkmiOxzyn88xUkbkZF4Y8KHbEvgM9FsoQxBLRoQdX1pPWYGP2EBdUsQIe7yEjiuQrqknagK6KTUD_61q61K_LeiVvBWRzFWfV-rwW3t3iHnYnE9Cnk_i8EjRYNHhN_88Sg3sAakm01bhomRwQ3Ix_jMLSNacPkKJU8V9cyXj8WG28s1mjdinHPdm0tmkCQrsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaaKyPU1UybyBWFVcZ5jiZLLfIw8-GqTZHLT1AnzEuO8Ie_3T69vZ0Fd9VwehcLHeyZPXkH044ZXqdOilSQfJYSfgedBvayWuLUFXCmxIQzD5frHPs-Ek69Uo4IGnFiCe3DEZzs0fjnm6J9NfUs9_M97NpveSVJV8fs5yyaAtmpitIdZmRhFJAHSAsJygKlaD9Rc58J9YuuK6cFuD6JRZ1YTNCuzisZBc7zuKEnfCS_4HLtNLeIZlcA4utqVM53LRJErEwZdxe2ghJVPy0fAF-7gdMRl9urbNY6vY3_IU4Oal04b_luYwQA1V9Tq13lL7lIAtyGXV_5T9dGaXlTwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU9IY7E9-WPrPkmG5xJsOprIuOjJHEswCMj2h8Wx0MCh6cEp0pY-uGtPkW0kt7Dik-SUu_wZ5dflr54DbPgN151CcOdGHbxCyj9ZCpS2K4OqbnHB2JIuHgvcjAL4OSHhJTTI7NFm5i0a0RpevMzoz8R0BUgP4ic_ClrmUxVzOv2YJoBcbUDBiId-9mV7_1t6CwsPsRG4pEHtUFAhEOXwq85wc3s0WavqlXYwb9ILVkhw14hYQPj-LAusIK8xeycFcQEJ47NlIAD771kREwmmP-IuNHANFo0omzp8ycEHVg_mOcbfk9DQPEzpH2QcuOl3z03GT4Pk92_mPYMiFiRrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYsaUKB1EiGWvFDaUFATmJBvscWdMkWuJZgVmdTucKDhOz4HZE8KRZGMcv9H9CrHPTF7EOoB5P4PJ-CjdeyXM0cAcyy5SMcVz9fWvtlKy_D0CuCfFjij9o3IU2GOtVnBxyhXTaq9TUBClvQrMyufuZrk00HboLzVQKCOK5spJfbGTPaEjOgjplefQqerSeCVfrUr8zSb4DYy3ODMicHKR26HyIHxi2qoDf0Wl6qcqC-0a1vjb7_tUViCt7jCSfvu4dGWPG51lKXzpvUVQzNVNo445gQ-RajTbPEUSUnuQ5SFF8yr2_WYBqYtlXiLc-jMV1WKZ_9mdQWpYxXy7oUDCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_cL5oa08rKPJ4784hsJ4bY99JEHulIIYa_1iBab7-VGZEnQ--DpGSjr1iqdFUX8FnRe3DNq9vfHT5Vk9QdE9wWRxoW1CHwtJr-ecg3qqc2exlaEIPEA5kghI28jkL8lrqJzSPF3NeI4Uex8Xrx9-ipXVgrtInpcHB3r0m1k_B--1dTIi9dXBuA7lZdC_UkM13FG8QiOMQ0N8bC6DfgTHhs1cBDWJfuMFVkILtxayyXHx9XMxky9U37MRhZI9ciz6afcb75inoxWqmlwHGFeLA9tsAG-WVSTHi8Di77P3k46VqlU0isc-nV_2FVNh-2xXHLi0W5_P1qNO-OG09UIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP_gGqNnhmJPNHgQdSyB581wMkFRgu7j6_NlTnrZTpE8kG3DB_t4jHCGFJ5BGdg2vd_61XDWrtFAQudrqrbQAmGRSseJckehRw692yDATKcekGZciLY-PjrV1W-iOCAD1yMmH4x4Cj1ra7zvkcpkfNhx-2vDCsmCrz9y-2diIQotWKot7t1WVc7qSnWwciTuIKhQAFhQaENIykGn1nZ1oJA3abMgN14u4Jr4nh2mUA9Msw3LEZipUMfesarco_MXuZGA4J36K0z-uHxT5gu92Bekyy_q50SLRJMJ9Wyu7PtzX96wJxDpkUiE835w9--qcH19yoYs2_u58fdcOLBHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d91mOEZ2OB4mYV_bD-FE3GV8Mgz5-miF_En4Pb3Bvy5XJvvr-tqYLMg0lsxRloOySejw3i6cHa7CSu4bto-YOhZeTNzg5cxd0oQe-D_8xypHH5up64phxCnViB-4vdnqjaHnYpUs7-wceHxI4Pb9vUBIGIVVYidG6i2EXLv1-A_a78BNPW2StHoJU42lQdn7lB0dy74oips2eJ7LqnqixvbZaYHZZpMlemn4m0SGCP1Ddp62WKjdej6C8mrxvmyGytEVkesGx2x0U8-cpkIsygXXtQCOKu0kNJk5brIDhQYU_2dvkpqnk-dTegpnx1zZLnkPNIXEKXH5Q5iN4CUz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLk3y8kFO5uEzVWDm6eF0KKUAYen3IJouFFRV8siJNujyQXcEz6glE3n9ZQ7Euw4F-JykFMNl8TilPkkGMJS59uneOIufdoQ10vSN-nEsE6-aobAJdv1RmZZBrGV4JTTwToSCxg3fCGq9WGTsCJcEjymagSJsySD3uVVQ2bkE4Ugu9RX1pRfIq1zltCtF3XkWTK5Kx4n5tHwhyZH5Kdf_XGH_6WlZqG4wYjq5TL5VEomZyg8uyeZA3em1Ru03y5pmn52gfmwhfdNoS7GNIlW_HkO6gg7gDOUPLx8XFfHCRTTKJ9CzxQV7uXCDRB65mqqqnQEVIEfckTQte1Ell8lgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPmOmygjwTzrCu0b_bUSbvSfRUL_Ddw5fUPZeWzm6zsyy0AgLKM1W5oN8nt01ArnKNsiLrNaCeu7IV4s6cEMPK9kDwmRkHNuoyVrqw2lUu3IrKMNunYDIe5sLNVzKQl-tLimS22Xydaie7NV7EIzT9xPqLOGX0SeSGGhZnHikkfrzcU-W533YId0Cjp9dJ2_Kv532CbIm8PuJd4Vbd4-G5_X2z2vI7Qq7lCDIQ711otnJ8tZXBkdiHKNkSk2bpxGmneuZKQccNWMXc7P0d0anwDXagCEsLcEKvGa7GG5Nv1DUmb_SIIT6uN9dWno1YkwFFpkAdWK0tTRI0XUOtU_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozsHxkVYD2-T-ScUA1HpI4wN7o7vTYKEBo9ggqcLp7ZfO_uEvvuvEN6qEzUeQFdcQCx-z3etaOuDveNqtELkb3SM7knZWvH1I0MNKvyyI8gmlStdHuHMmNLoaw7mqYQjhlFvrGQQQmRvm2JMajxR_Gy28vKorquvPKKUGVJyewH3UhTCAL0WtoUTwTYHqMA4IzkNgE0jXlO7gt-c6gA2Xmez0AhfS1JgQCDyWVE-Ydbz2ftYlw1Zsquc6CMmir1tFXZssuobjRn4wmBYRtBxoqqiepKTZnZJh9NFXsL-hV6eu-lnV09BkCysUIhRqqAkzFltSrMmPgErs0vV4gTs9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJFdPr70s-eSenPxK-QvtAzKtKT882bTVA9wkNgehRrujx7R7TxLpXBXcZRuR_69OPppGIFiN7RHd-NPqgCeTX--BkpX9VO7XEyjzsPzsTDp0lTii_grOJqQU1Ox5FZdIa2W615FD160-D4CCIvcSZ5ld-2ParTUoW1Hu43kUf0ZsnOWXVfNRaSrx0k7tZCZ4yjQ52tsfZ26kLzXVhRWFutjM0Wq8fdzTErJO08wFelWWAmXWlxo66bHz04O0OD-XLLee1llwJwQ1nAQYSnjVdXgb6L8369MWS9nPNu737l7XRZhRyems5Ox8XlP-xdqkIF2_85506f0LHALRKzpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daWCaHOVTbBuat-ktdlg9Yku5slEKpMEntbnMjv7KvQwKKvMGeCFTTDdKUhNTjodSgf3WM5mE0VIo9ey0NXB7gH4PNP4QGWNRw6kdj52U68Lf2rs0sPGKddFTtULdS6sHfgNr_lTa8Nq-4pIAZzRNY1FpqexWxkAonRH8q9M_cRPXTb5VgCJUvVbN2qNoqfpfUQyps7E0UwHo58gpxoPlhPRfKRFGnudMcoQNMa-_XbsOenia5s9s9ROYnhX04iuAaz9iYVmtkbs43SZX5-S3vS_bK4pEslVh_qb50O37mH-wtbxlzQHuDlCBNjxBsFFfCVLadwTPWCu5oWL6XMMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMugUyKg-KjOR0LmM5TqvqGGzR8DpwQLh1xzBQD4eBnJNJpgBwQ4cY2MLdTdmu438rmncGWYy9A28HTwFV7cEWeYn6y1Uie67j-frFyBs0dIGAdAJ5n6Hu9K0L7QHjR73vtwWM0thXsnvIYhOxOGdnbkce4OvlLo8EWvXHjQCafxlVaUZefXSzh2Cp1HDzD-6fI76syzn-koLoPPd7yYuYJ3YDcJABs7X0sucxwUpPqsLpaOgnMVEY0pRDZ12cpxfMEldyR6saLMdNdkWLOY6RFjHH7GZRyHwWTtZswrC7CNs7udnRiwfjhCQ2iHIpGQMiSi2f4GhRrmqS0FLqHiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocyBNo-lNG8sAiN7o4bLmtAWkjTojf5C4rcMZhasxc96Mh8U7mSZ7IJQVG978AB5snNg8mx2Fhe9kR4QekmfNz7eUWKpuOgPJFEj4vkeen9NkCKaCdPGLJM2plOKvK9XTk1QYwwzdx9grfU4TEUBGaeE3EGulj6zIchHpuNgKZLN11vNrcRaqWhUyaIbN8OmXzpHbQmx8KOCkSPSsiE6UFkkKNZuk6fnnogb0RgOOHrrkEjLMMhOWMRY4wa8Ss4s0SK6cdfo_l9Ua2ask_h6ar2_YXeZyDszzQky82DVqHQuOoQReTQBKitiXuAsWnGYf709k3NvMdOynY15i6ycrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axkantGZgw9E_MJBEwsIMbK_bf02WhA2S16ZVdPl3m-o3AML5QMzgj8oKyNvPWH9gbwnUSrUpzy9xiTvf8tvXCCerLda_1eKPOtF5qEsXuplgolDMdKVjy1Hha8vSjuHTl1WtHUx3H6QZE-GLGTTdyBxJt9YWTdZBbgKNGAkw4GNjSr7CmbeZEoGgCwGirQltfo3Y09rtgPs8BvVRqczYV0Ez1B3WKc2cwqHF99ypdXE7XTpF1JpZXAMbhtGRcGgx8Aq3UULYb_GiRhVuTTv4w79m3WZsRaXT-pHH9xF9yMSDBd_-VkefjqiElNtpw7SMvo-eEZ343AY6u90lLN51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx7XxfadqDwRmQdXRD6pffUm3WSOiqgrf_oTX-yjeRjKq0LH30fiZn3QHllOybUoCVr08RIX-KIX8aHEfwT2XuezcP6Q_Ic4lUlFWs5q6fzAYjikw8sU4Cmh_l1HsqTjiu4aEB8uQu07Ryr-efoqJDYLnt8-J_fWPz_rAjnGsVFTcjvSLuLlpzVv252EQyUi3knZb42QPBdtV0tHnxJYxm5vzflKS8j2O9apUKAQg6P9U567qGe6K7o2CsXzeUdFEka0T81cfc94BFFvpF1xRiHNZECcRUb5VvGY2s9D6-Q7KY1DJwIy1EWatq1EFM2lXAVSYojDF0fKg60z-jljhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XML85PooVK6MFdSX2wn4Mk7z0A8vFK5Io_4LRZ6FGjJbm82FTmSaXOXRBDAZtjnYeJdvuKEiui96KbM88chCMys9Hbsj6KRz-3hXHtOIorI71Mr8PBowzzPWwTtbTSH7sTA-mG_8_e7kcCy4oELq_8YBVq3URHTQDMzfrRX7v4InybvB9K967JBxpFXWCjtEiEd0npaL1nOV7PRXuj9vXGSEFmKArpgfGwFTEN1bMD_43A9t5lf0r8WgDPGsyjHWejM7jMFNmsN02vV92Bx4msDa3F5s-lgYPCcH-6ITZLEc2g-oUr5CRICBZqigHZOM4lEAHaDK68OkEWLukDhc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyInslNSkz7TSaaT4IdOQHufVLC3nEtL5ATvcK6sKspcj8BjKUciG8uPf7O_V0a2t28U_EXq0mspGCrwL7KozOQkWINvOMtF1v7AKn9Euzn8w9DN9zzzwr6msLIe-_bPBoNn8pg1ktY7hlmIH0YYhJZZlCFlapj-ddvxAu3gDxVC7CW8Glxp7d2gNzaVl2VuznX9elOG12LKAz60uRakEvHsHiga4uirCOPC3brKyTFD_yzbLsT1-v2DYoum4zK718s-Rj7HzeCrOfwRyMLOCnD9Xnf6JzTEPlCeooFV0M9P1G3KYN8l34glw6NL8Vp8PVSlCwLQcPKThHH6r2cIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYLvLr0bt1nYMIoMwh-fd6w_tV9d45nDgrKvfuD6AH6wpYd0ppDCYBewS7vaj-jH-1-7FqO2csPyGA-Il1gEXG7sZ4qd7-QLrVjIFvMU8OUqP5gyd3bSRvsSgNlUnbFAoJqKgnFavvNMpGysOiC5t6ZnjadijDbAi7wT_Pb6DP6TB2U7lDD5f1riyYgZLjgLEG43vFa3hX7dhyud6aAiElj7gwKj90RRn7Gy6I-71rY_3shjrMdIXwQKsHPtNj1Fn99VZCcEsbNQ0MVOTfYPen6l_JP_Sa8apnrCXVoJI3SrnpfwwKzdrvn5IucKuZfs4jnVKooEQMTgj5e31nPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlqhiD2GXFyvKd8j596_ox6hMHykf0OZ1VnCoNJRXDonzApIRPoBQxYkILCBq3iU1k6ESYued2ChfMhk735mMfrVm5Vd0GFlllm4SHih3-h_mhrR2GOis16_oPqQuIRAVLds9v-1NQ8nmshglAf4I7MCznxh7U-ApwyyS4CL8QgfOBOivTW7-fj9IAnVlLi7hFDUEg95JNcrtLpshLDSg5vd_EOa3dXwhENfGKknLOj27c-SkTqGAIG5-MCcPMhrERT_M-vWFx3LSMLaa2rVD6OPd0-ftWtJCHnSqxxddAEx7GABXlRe6Ip4ydhk2TrUQJ7_fCHD15CPW0DKS6mAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzdG_jkm-L4NSKFOP8Ykvdpqb-6jLx1aG11e3d6jZF1oryRWBlKUofD71HNcLwekpinrAODo_HapUChLVyIXZb5sUpnt8F3Hq00Z5_5g6GDei1QZsYM4ZFQBK7UU1u6Q1NfBNjICyrD4kY0jwvGMQCl5wsobOZ1rdtBynKDOc3O3367916tvnjjgqOXNV75tg-qm9HQyIPnT38D9efYrdgqHY68HJuHJg-FyeMfJ5V7qVgwn6-ODxdAGlPnj6gfGIDRKJLe0v-dNlNOyVpfh-8OdugMQPEfsgOA3JRA1I4lUe82NtoN8toBpAIyFf6vvOrR_qIbcwODl-WH_dOOFog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIa0PfVNA7eGvCHvvFYuxLhPiVIGWwuKR0b5cKDq9xkaUkEnwXlCsxkiQcOlGCAKSg_Ck7bsRH7aCewE1F0ZUw4ZiCezbGgvQOn-LSRSOp0qbieNWpsxVg0QzyD9NwUoTDoUTebMx_cRM-M6a5xPBHB5FQw9py7clgTHwpk2rRCs2FJMOAWDqsD_d5XJivllwEhlk0EYLtY67ca_uTlXnuSp-IlNAFRralW0gNds2aS3Lx177lK27gXEaF4GwRo8WvapfamgCYgoAbvzgMLeiWltjwNahT-PSm6TuUWitGrmSQGYa6CfIaXocgCeQv6C9NOUZFUkBEK21CVlZMXk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSyND389c1HhkW4hCM6TWuVpy0hm7AYtJjwRhx_AjjKqa7YsOHn8F77muDf5TNpjd6vXBC9T9g9rPYb4_tyJygoeh8XnvdoCDmxeQs-YVd0-sWg_33QVPmg4QAqACkErZvI9YP68X7PqJ6TXFRQlYnKpi_FqLthEYOBUocpUlnVDOcEWZQBku2-LTEDghXKN17MKEbmAgecNV-JPRtdgkbQDMidNOVcoJxss3S2e5r1MxY53nMzRiGdyMIYB2Ss_Zad6aTpcjdSx7Ma63igIKr2E0RbxvQKIIDetZN31SCi6BN8rlPdZ1B5qnyvr2HIDLYW37UOxp8u7VuvRSHyktQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWzdxcSXWcP2sLsKxpp9-n5u6bIk-Sv5MWnm8vqls_0UpkxM3ABKbfWnFrhI_2F4XZwvx_R7-LiQni_1oxPtPoTdlckhFelczFzTdxEevYkmYmbo8FTWrZxy5PQp9WS7I20-hBuT0auCecWJUXct6v1eWlb5l5iURNPrgOwoOZDIbgRJJxPFFpA-qd8AXbV9DqPRsIS3rzf-wE1OhUXzlkh1jZVibSRcxhnNvaGYASzLSQSE2ImUlZai9GcDpL7sliZWHwu47JI0y5WJTSPdzcruS1Tx9aTjNXSQtNMLm1P2NRWT3vP9Wv_u8kItoeY8pN8R2vLrlP3zEE9rVwQEtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=bt0_m_aglpsGHeIi22Kb8glKyU3wuqgViNE8miOIezfb-yLfKumE7fTnVrH6qZyesWTtkqc61N5zTJ73YoZBSd5gUJ7do3XYf4-31LkD3zCaRn5UmYGOVR0Zryglg96vB8KTgKLZImScr_ZKT4pCTwjhUgit06jnbs4aHyFFzxnMk6_Gdgqt7gFd3NQ2Ntyb-0TxxYhEm6t9Yrqd1SKvcUGjIFvYtdoK2Fx9MMUAhM1oLENrC5KUBj89z2qCumoBdeFA4r6KOjXaB9UsfYw4oblpD4IFeZEiM3f4j6RMXvZCNQNb6Mlnl3P5soEmEZP-mgGstoLXVzZjlO6ytlXIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=bt0_m_aglpsGHeIi22Kb8glKyU3wuqgViNE8miOIezfb-yLfKumE7fTnVrH6qZyesWTtkqc61N5zTJ73YoZBSd5gUJ7do3XYf4-31LkD3zCaRn5UmYGOVR0Zryglg96vB8KTgKLZImScr_ZKT4pCTwjhUgit06jnbs4aHyFFzxnMk6_Gdgqt7gFd3NQ2Ntyb-0TxxYhEm6t9Yrqd1SKvcUGjIFvYtdoK2Fx9MMUAhM1oLENrC5KUBj89z2qCumoBdeFA4r6KOjXaB9UsfYw4oblpD4IFeZEiM3f4j6RMXvZCNQNb6Mlnl3P5soEmEZP-mgGstoLXVzZjlO6ytlXIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swu-WwM31f5fIsBzm6hgjcxpzFT5bDQF2TC32IEcuCUw2hoFIbKJIpcdGXT0c4imIvriR0d9lWfrDiYhq0L8hPKvslEjO-Soest4vyfsxR3uvMDmosMuhyc96rKdojU9Zq-G6aO03v8jmN1eZuUQCdzxWYW_ItEyf_OEQu00fTOc75QTiruBDPGgAF_lM6k7giQkAZzYA_rpCIuE79IMCISOaMcPPaoiTfSQOvPSPhPmK8kpU-8gzy0zZyn_iy2les2lVy4JDP7sOlJhGfHoRQXVS0NwYSufK6MN2J8bTM0gX3uwmF_i5ExyTntqhvuZhsDhDHlCa09fOmEocnYBgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=WH2YMJp0RRE6Xm7vJ3TJQsNvYx-5KqYs2Vwi56TONIWOHSIvGnEYQU0OG7IxKeUnV795yW6msjkEhbYjJ_HjXXiL5HqanOz7NXz-t1_3KnTog6Ym8G9GXdaqmgegqzxGSX_Fc2GPiaHwuBmWmmGoTWB1Mrq6gDqaCMLGSB9piNneYJpKsmPYtDTc4Dk3RplcVoNmKveeml9Ch9vhj9t-fSLnnVIOx6NEhc-ulQ1pd4OyWzEBcMjXnEmQVIjFmO1aiozFCN19-294IbunsqjvPpQ21wYuR6thVH9Yl9gT2Zq_QgC_aGEnqV8uOqHbEOXjfl6ZKDQpHgM_nIX-BLVejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=WH2YMJp0RRE6Xm7vJ3TJQsNvYx-5KqYs2Vwi56TONIWOHSIvGnEYQU0OG7IxKeUnV795yW6msjkEhbYjJ_HjXXiL5HqanOz7NXz-t1_3KnTog6Ym8G9GXdaqmgegqzxGSX_Fc2GPiaHwuBmWmmGoTWB1Mrq6gDqaCMLGSB9piNneYJpKsmPYtDTc4Dk3RplcVoNmKveeml9Ch9vhj9t-fSLnnVIOx6NEhc-ulQ1pd4OyWzEBcMjXnEmQVIjFmO1aiozFCN19-294IbunsqjvPpQ21wYuR6thVH9Yl9gT2Zq_QgC_aGEnqV8uOqHbEOXjfl6ZKDQpHgM_nIX-BLVejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgJZqx_PnnmcRB25ELSqgMgSur-ja771TATe36NMZilgt2a1Np2YqDGNhOUsGF_w7ZGYeo1VMHWF4PoT2wwBn626js7GpoAJ-IZSOwch4wiGknC5dLI5PRLmqS75BashbcS8jbCsKAGDeuHd_HUfsBwLopMyif4geSoOjAuJGLz3vHRlmXUY1-bJlxdnayWcvs3eM6t_rzDhPLMno75L769xex2784PnZhZhX1e8MaD3AqZqQRrCBAM4KmyL_Qom-9Rwd2erLFfUR507RxUxbkUQRoKgC0SbJygcNyqrPL8r0N7k2LpOjVRAJn65lRr2UofcmnEqi_DTz66tQpgNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGXxLpFviMnsrMTV56RMtUmzQV-a7IDEBr8EqnbMqOWOXZT102Kn6uACpYuicn6fjciiQRpXNKEihuVU23eh2ruGdAcGqodegXefEuLzwGA--9n0j9JsOJ-JjS9R_ceRNfqIqmyA8whzAYHSXuB4Lbq1wgpsnItYBBrAJ2diPiKULmFDFIHqHs8zilAyMKEOp4n3fPc8z-azWtc3y78GPk5gGKoOPKk6fB9QYY97rymftLJeT8B0xstrCV-uiPZk6U-_pdRXlwNM5VHKB6m6VarE5mzJOGaBk4cb1rvnVy54eq3PFzTu4XxJRJVLo3baCrYNO5j1m3JdYH8xUvbRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=CwqyINHbo02kDsRxxu7b1pkSJ7xqvjYb-5IYk1ehbhTGfQwWrMgzhu5uS4DyBME3zzKYRQmLg7nxiqnrsdoIwivqgL0axGkayQSwnJwkKdER-0Bb81gc_Uzru5n2dryFs99K0xiFhJwk12JPBgwYB2xuJssVu88IJZnCwQ75NHGe6mOv_l8L2N3IxEdvJl1p9GT9ourEPtS6gvNrD7aqyqWFXCruOkHI6wzczQqO-wJ6ljXNJbahv76J1ok2bfx_jYpggqGKbVMxQDPpw9yWgwke9LhZOp0AI0BcJLYBQdBfxR3uRJapLi7HXCoM-nkwHlTtBt08m9D-zG1gBKJblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=CwqyINHbo02kDsRxxu7b1pkSJ7xqvjYb-5IYk1ehbhTGfQwWrMgzhu5uS4DyBME3zzKYRQmLg7nxiqnrsdoIwivqgL0axGkayQSwnJwkKdER-0Bb81gc_Uzru5n2dryFs99K0xiFhJwk12JPBgwYB2xuJssVu88IJZnCwQ75NHGe6mOv_l8L2N3IxEdvJl1p9GT9ourEPtS6gvNrD7aqyqWFXCruOkHI6wzczQqO-wJ6ljXNJbahv76J1ok2bfx_jYpggqGKbVMxQDPpw9yWgwke9LhZOp0AI0BcJLYBQdBfxR3uRJapLi7HXCoM-nkwHlTtBt08m9D-zG1gBKJblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7yGkUaM0HENRMfOg_h1WYgAO3F5F3eq8gLM2jGg-1PaSDZJ_hkHCm48jgw8k2_5dsvaGGQD9b-eOzP8doWGw4A0piN7QpotHD-b8SqoT6ovXl1TdWmZedwgnZKt_PEfarnP03kQX1BdaceSgbf4A3oOKug2bzZJzu0Qy8wIuONX1pt0N8SyDfa44jhiyEkctmZG40fruU8_obQJ67NLITB1tHCy52-0pqF9owNKZ5VFY5_2f8dZ0rryiS3ycoC482br4DIWELzoivel5wVoiXNI7KI-teUyA3fMJ666ASt_TRPoNxRTq2qkk8t-SIeeYM-Xm8ja7OUu9j1NKBnXBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOv07CB084IWj8zegvBHsZaarRn6P0J-R0vk8fnN84D7xAiiMRDQgujuyN5ZvJzdA8r1DhQ881e1IPi6jsUt8uBl0KODMDvpRxs4q6jUjtJY8dJJKiNo-T6dgOdgZa2HPUknBDsa-RjyxuRw_aKZ1lueKFLRthMXJtNSQ6nvZeubldB6hMblUQC80-n3XUrCJd7ZSV23EKhAQeGIAmUTX-nNQIdaC9Src-NTTd7JFO61x0cChoU6zwUNezNzjrDCrDzuwR8Hu_dsVzvUfaXvsJODWHG5_HMRs0JHtUefOSXeRCDQjTkyUdc_PLugEJbPE88rScFkjtSPhP1um_oMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7kefLSmPS_DE_VKsHMvvkLqYwaSdel6F6YGO-tgVfQJHbPOs9HMzqE9ViPswNrt0Sv86wLtxCVWESjZCd1RNaJNX7afTaQ-N33MR--jup0E1qsqInnnseMVlp86kxFdxy5uLGFdpALruPBGRlYbx3h3UkxBz1S06h-9sRJ0V3ZhsyRgObgH2WaJQqOZ4m7_uPG9yxRXeNBSF82be-EwpKKGmoxk8zGaBgd0QzgXFBqMyOaeYkdP02j2XKPjLfpYVCLDOkuth_6BieTwT7uswuU2Ihqred29feCMIkkUW3UQXkxx8lz7d-VGUbAJ8bWtlGPHhzKTVZXKqivl7MzlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=IJg9k4Q04psetcHMifL8Nr1CTqMN21kGCTDA_NX6HVHk3CZXL_NHk1-vU25qfICfVdEGt-4QukvBa0qPqTK25z-8qfyLYWy1AYn-qUfT_gt3zqbIFJ2w2FrbWYgAEOiAJv36Nrg_gc9lMw6l1kqV44P1thrZkUs5qciDbwzUyy7k1D53GISbfDW9ffXeQVRyHjgeTUq0Z06q-pmoiO2b574B5a69ctqJEZsrky6nR7Xnqj0Tf6sAqUYup9_wT_hjKaGoCeYN5X9E__MERMkeCqTs2ZWVHMhBAKEq-WOIc8frE9f6vtQgOLds_NLTUFhYMCBazNEo5n2kBc3HQbNXZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=IJg9k4Q04psetcHMifL8Nr1CTqMN21kGCTDA_NX6HVHk3CZXL_NHk1-vU25qfICfVdEGt-4QukvBa0qPqTK25z-8qfyLYWy1AYn-qUfT_gt3zqbIFJ2w2FrbWYgAEOiAJv36Nrg_gc9lMw6l1kqV44P1thrZkUs5qciDbwzUyy7k1D53GISbfDW9ffXeQVRyHjgeTUq0Z06q-pmoiO2b574B5a69ctqJEZsrky6nR7Xnqj0Tf6sAqUYup9_wT_hjKaGoCeYN5X9E__MERMkeCqTs2ZWVHMhBAKEq-WOIc8frE9f6vtQgOLds_NLTUFhYMCBazNEo5n2kBc3HQbNXZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WgttAMuI-C_5P4kaoLE1M2erFGg0ggVFZzycITOGmC3alnt_f-YLFJmY_oaWJL7Hl9Be1rILeFUUXZLV5JrbZEs77EQRc4tfgE2DX8MGSOMvAnlDgByiSAe46VitYgAVanV4_MCGNzNH_18NGiOC8o-J0MjuXteuMxoPASqO9he2WdHO6fu7nDFPOG6ah7PM39f_9LPcyFZSkkxGF0O9COzc8FsvYBC4GlnsCaKUNxtQDVgLu0U8ES41VdbH015P8ny-_jRXcnsqazOR_zIUeEuO4Fm_TMlV10sVHtDsxuRFbJDehs_O5rIcNLayq7ItBgIv8R3fpoImDar1KvE8og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WgttAMuI-C_5P4kaoLE1M2erFGg0ggVFZzycITOGmC3alnt_f-YLFJmY_oaWJL7Hl9Be1rILeFUUXZLV5JrbZEs77EQRc4tfgE2DX8MGSOMvAnlDgByiSAe46VitYgAVanV4_MCGNzNH_18NGiOC8o-J0MjuXteuMxoPASqO9he2WdHO6fu7nDFPOG6ah7PM39f_9LPcyFZSkkxGF0O9COzc8FsvYBC4GlnsCaKUNxtQDVgLu0U8ES41VdbH015P8ny-_jRXcnsqazOR_zIUeEuO4Fm_TMlV10sVHtDsxuRFbJDehs_O5rIcNLayq7ItBgIv8R3fpoImDar1KvE8og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmuyD5RU4POiqPlGGJthOZn5tuesTxHD_mVWWMsQoNfTy-py5jlBRdKR7pE1Wq-qpwEXIg9qrhcz8E73KtmoXjEYV08vjDXIV3jLfZlUeDD4oxd78yijzJ_kb3GwWzqEM_nX0clcJbOFJJ3mTJusZTnwWc7oKATTAAGSMGwsXUTkALf4jm3UJCQ97F1gNUIlnGf1OJMp32anK2Ek7ochcgqL8_OLUdGDYQajtsqHL1sOnkP6wxwuoIRupH_0W5BHDIjstTGwJio9WqHg71N8eMvcZs6oNy2L1aH58RqJUVjPv0uaaZ22pLQy6v20c3DYNRAbTFnXMHuwVVtEGMTAoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAxYwH431bCz8JOFaRJWV0GH_ZnDK2E-Lv2SocaxfCbdxnfY950UmybGErW8pjKdiyWERdd2PQnm0dodawqbpR45-Wxb5fXvpMC5hA9eULLXfHSApiJV0XeSqfY0Kw5-9R9FzY6E_JNBRP94GwGzRl9yxy5UsXpPptXdnL1t3-A0CF-rqBjoq2dfvJOg_IbAz4h0Id6LkOBAHZVQeUOOgaeN4ybDkK_xrQjrYxtPOOM8VHE3jkcThG_2rUleGUI6TB2RVNd1G9G6HmPd4XSvuYFAWsqs-AO-e4mjQUF4hXZpshLDPoKH4hlhALP7oj_FBi3bEGXQUWfhF0dbEi6HSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpMuJS04RoTC0IIY_Wr-A7UTYbAM_L_7sTvd_mtdoxYsPEhjdmA8etdTxkw4PVUJSkpexDlwG9_nAbcBR_md_85KHwJX0k_7cv7TaSwmzVSCl70JarTTjhALzMsET0egdHrPp5zCc_wHNAhmLcAP7TDtTbsYFD1H0bXSXx2J3ajtCABxv3Pwv5GbPtebTVJ_YTaObTSC3CoWBq-zWMpUilvIrJtCgLMBxnYvgh98ZavSr93NFmJoV0_PrydKt0QvEkt4JZAUZ3KLu2QqiUpddPPwPfEWygjUl1cRTymPnaDgww7uY8b7zNuJKw6lvUrM1_1-CaEAlsDteyWk65WqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSs-evV3K7AVkE7LqzluForva_Tk-EQQ0_ULKCOSocZYv7CP72GRYMnEydvjrw7LGcLJYKPJvrEHvWcGDYLR9N2dBaImBtsmhdvZUYLbxfEHiPu75yvP7FCUoshqIL87uyfMe1GwF-du6Qw57qXqvWqU4FzZ5WUH1ion9qAeaR2dtqZ6ATFBQ_YR7t02YfwtE9h72oIfEjPKG6pgSePzEbaBWdXtV3D2Z3ziuXJTNcoalnPMlGsSfwK-fMvfrj462L0pshRJAU4U7NgjNpBgOjo9K2j1m-OY1rAWujnrpfL2PoYD1gTy_MHc_ASB8RxOc3f84XCMQhqnwh1FblQ1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBiDLRap8zsJJTOKsGwPsVgYg23tzZxmF3iyPVglC3RCvAjdYQIG6AE5DN3Hqn_HeRNJH2z41e7VwRBx2x4KEihkyUHw4oBSramvvx4qJ0Nb7hDM5ObSkNVdzZ_Ftg0nWRT2NWJEGd7Pa2rgoppH8C4DeWqKjcknmDNpUn8we2JbnPePr52jUf8orF35NIaRHkm6Uzg2fsqNqMDFhmxAtpqSljM8gWXNRMgh4xZoMn8w5DpE6hre8zyiMzAWS5_S-PITnZHzd9KTXVSt9_BayzibEZ4gfRfg75pQePY2X9UjFGzON3jDHRd6PdiNoDJHLiJildzOOZt4qkI4-2WrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syhf082xxShaDmX_Db7VulSihOf2CN0_P8hkuzjD_XpTbrYI1NFTpxXAVF1R805pC3suEgiHLb6Gtg4pL5dH1qmQ9h0U7jpsxP0ummZaMICS1JZBCMt-adqgpE6XToRqYWiFfATL9Jx2mK2uR-1gTJs7lC_S09VZ3sDsFyenduPdUwWUUXmS0HdpNNFzuROqsp-l3mlWBD0D2jvs5tjY8p3ym791YTmDPuxOf79OxWfwqqeFI0ceLPKZgNhtVTAZMLHVTb1qVQ9B0zwoNRBzFLqS_3u8lEDDzQfFMxvst69SqJwkOvivYMdoJBkZPYxGpPCByvhSYfIU-Lk1hfV9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnZ0arbGhwPEgPBdMrI68obhcidzS2YXr1RXx1kq8yT0BpnSW7ewnu6RiBywhIAun3bvcXbR0hGsd2myU0Fka4y5jBQx0WeenpFJRjgDhcMtCxInHvrrhsEtVYsTbj8riKtybV-zmVFLdW-mufl1Hpa52UcOPDt73t1GxoJhLNI4ql7X-mJ2F4NzWHWUjh6b-BPYaqoQi6PZVgdJgUZIcNRS_bbtSKJTD6C6woZhMJ-ubt8tHDTIgFoQQzXAHrudFHGyXaORbMmh2SP2iEo2RdRzZSMsxc7gG3MthvhM-l7cUVQ7F1BQssixM2oj-gsCE2lKbvfSx6OTDItMSZVaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=k6rx9RBDGuVSO2y55icbMPoKCtcEcBnmB_1PI2d9SKebS8A5aoLa-VMx_B7jZf5fPHubrRrYE56xaGGya-ueh_AnMeODqHiqTg_5VmI6il1213oPcdcA4BFZJXNZInlVWTIXy_zQXrMA1PKWm_bDB_MF5RXk4Ns156bUfYeQ5jA5CAsGjpdN-jn8roQy72zCR7_tEByHcGMLnOhKbe_S5OjUSl3-0ekzW6UNUQKjCVCfTYAx3cGrk35-k_RJGBtfJs3JH5HHj53lRtk2roVEJXAf_vq_sYRD3aHG4w7Xnr-AOYvqKVnWCzmpmh5AjBCa-QH-gFQ-0EEtPOuwngMPNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=k6rx9RBDGuVSO2y55icbMPoKCtcEcBnmB_1PI2d9SKebS8A5aoLa-VMx_B7jZf5fPHubrRrYE56xaGGya-ueh_AnMeODqHiqTg_5VmI6il1213oPcdcA4BFZJXNZInlVWTIXy_zQXrMA1PKWm_bDB_MF5RXk4Ns156bUfYeQ5jA5CAsGjpdN-jn8roQy72zCR7_tEByHcGMLnOhKbe_S5OjUSl3-0ekzW6UNUQKjCVCfTYAx3cGrk35-k_RJGBtfJs3JH5HHj53lRtk2roVEJXAf_vq_sYRD3aHG4w7Xnr-AOYvqKVnWCzmpmh5AjBCa-QH-gFQ-0EEtPOuwngMPNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=PHT9ofuljXokIMy9TB9xQNk657MFcVHFuwneq_1XDOFhDTZCRCjY75-IESYffzFRTzolPQg7gsGfs47Hg-J09sFCYs1grhwuQNLuP565uUUjjxdhO0zA33ecd-LcDis_3H4JVXkscRH1bULUUtFC_F53e8RnNvnsCeuEvq3dz5KILZBa8AvpCJ7A48z2lnHPCnUFZ-ZrNN57b0A-YulqgcGkazPBJhRiKThOQVmWpNvltp3dQtkrvHJhFJ2MYJoD7fqZ3J0y_hPwnWZkHZ4qJBT1bkcgLPY3tfwQVJSpLee2PcyvhyG8S3wjqpoG8BKy6k7HmhdBKbOAcBMUI_nrjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=PHT9ofuljXokIMy9TB9xQNk657MFcVHFuwneq_1XDOFhDTZCRCjY75-IESYffzFRTzolPQg7gsGfs47Hg-J09sFCYs1grhwuQNLuP565uUUjjxdhO0zA33ecd-LcDis_3H4JVXkscRH1bULUUtFC_F53e8RnNvnsCeuEvq3dz5KILZBa8AvpCJ7A48z2lnHPCnUFZ-ZrNN57b0A-YulqgcGkazPBJhRiKThOQVmWpNvltp3dQtkrvHJhFJ2MYJoD7fqZ3J0y_hPwnWZkHZ4qJBT1bkcgLPY3tfwQVJSpLee2PcyvhyG8S3wjqpoG8BKy6k7HmhdBKbOAcBMUI_nrjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=BDcAprXk9AOP-2aDv3LdCxQYwy1ZTlVorfdZDOSBcBwg1an6Tqb_SSuEkPQ10_sjGAByuUz3MPOK_ucu5hkWrLxFcKFWGOKY0I2F8F2Gcnh3rpL1TjCG-dbCDo5UAYoLUAmx5qn2gZi6PK-MKXWy6AMDmSkeWQ9UCLzsrgkgSR2cG8_pgn8I2BVjFXe5C5U-aql1u5Pt7oVKxz_vhy41Bymws1mueRIF1_uyqXT4D1cgnV332fOFdcxk_WxGiVuo34rAqt3VzA2XV3jVtvUgY9gN_iQPn3GpoquLh-U8fomLZ7N3LUC6IqjSfSu6Fj0I46ggiVaMv0aPEhX1dH8B9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=BDcAprXk9AOP-2aDv3LdCxQYwy1ZTlVorfdZDOSBcBwg1an6Tqb_SSuEkPQ10_sjGAByuUz3MPOK_ucu5hkWrLxFcKFWGOKY0I2F8F2Gcnh3rpL1TjCG-dbCDo5UAYoLUAmx5qn2gZi6PK-MKXWy6AMDmSkeWQ9UCLzsrgkgSR2cG8_pgn8I2BVjFXe5C5U-aql1u5Pt7oVKxz_vhy41Bymws1mueRIF1_uyqXT4D1cgnV332fOFdcxk_WxGiVuo34rAqt3VzA2XV3jVtvUgY9gN_iQPn3GpoquLh-U8fomLZ7N3LUC6IqjSfSu6Fj0I46ggiVaMv0aPEhX1dH8B9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=h1Oc0dBSSzN2kksmvp6b-BU8qOV6LNlYPE0GZems5r7KFGhnvaL0ti6KsF6P_yXfFwdTwyHbBAngCjvgeI_Z86zNBD0NsQVe47Ba_qcJFuEsD5C7W4a2h1e9jHBRxHYTv6NLFpeUbNC42jWu8eemUx7WpuAWksdvjYD9ESijyCOmd4PmKL_2twrjzFv-dkVLa2CYI93lciIiOU1SVJpOLzKxq11q9UEu_sl0U57qdudyS9A_smozTCbncWncWfgOhmIZnnMrTV9f_emsznjzmpzW7G7fXTd0DblWLhups8O-JcrejWx2ldDpXF1MUO_4RpKhyewEGEQosKejNYSOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=h1Oc0dBSSzN2kksmvp6b-BU8qOV6LNlYPE0GZems5r7KFGhnvaL0ti6KsF6P_yXfFwdTwyHbBAngCjvgeI_Z86zNBD0NsQVe47Ba_qcJFuEsD5C7W4a2h1e9jHBRxHYTv6NLFpeUbNC42jWu8eemUx7WpuAWksdvjYD9ESijyCOmd4PmKL_2twrjzFv-dkVLa2CYI93lciIiOU1SVJpOLzKxq11q9UEu_sl0U57qdudyS9A_smozTCbncWncWfgOhmIZnnMrTV9f_emsznjzmpzW7G7fXTd0DblWLhups8O-JcrejWx2ldDpXF1MUO_4RpKhyewEGEQosKejNYSOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=WNCepUR-uTnwWd0U2ULvcdMXAHXcEQcSBmBjdiza6e8B3XtlQvOO6GB74H74wkSWCShChnaOnJQZNluFwcp6xvsPFWKZIGSFs59U5fWV9tyqwKvaodGupUjRaIaqDLcAvFafBJcUQ1lfmYnpgyvojOI2ii5QiL4cTo6L6DyaAiRg6GekgagLMSgpQiU_ev7bShOVH7c5Cy9TnZdylJqGG9ngG78En8y9Rn811osxpoGf3CeWgETc_hWOJ0p8Ztl4tsqrR39suak2khvnxzLi9fOGmyTf4MiZa971vx6Q6mI2hsCMXwVUot6PsSi2x33uf1d2cPdNM64DKC0x_L4Ulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=WNCepUR-uTnwWd0U2ULvcdMXAHXcEQcSBmBjdiza6e8B3XtlQvOO6GB74H74wkSWCShChnaOnJQZNluFwcp6xvsPFWKZIGSFs59U5fWV9tyqwKvaodGupUjRaIaqDLcAvFafBJcUQ1lfmYnpgyvojOI2ii5QiL4cTo6L6DyaAiRg6GekgagLMSgpQiU_ev7bShOVH7c5Cy9TnZdylJqGG9ngG78En8y9Rn811osxpoGf3CeWgETc_hWOJ0p8Ztl4tsqrR39suak2khvnxzLi9fOGmyTf4MiZa971vx6Q6mI2hsCMXwVUot6PsSi2x33uf1d2cPdNM64DKC0x_L4Ulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=ol2FFZJ4IWv8H4oUHBNUT1ctoCk3cZ6NeRtxfFz-Rum9CZ1JV4_i-IG_mXqdjEpKjHe5GC5BsQBHOhE3Lj8TcqNuM8KhaNDzLtrhIYm62dbb0K0ZdIY6QZUPxgCjkSopLaJTXM84qEBlq76Q4lMskeqdDF-2WzdlIWbJlMN57j5nKdrHG6gsTLxlZa2nyf4CamXccquNXkQbVpcPpVQcG2aafFrk3N_vOw-GwEG9_nvN2blLefq6bK7WHTqx2gZJCYTgZg7A47d6y_G-Jb-byePIeR3mMnb-SwHd7G47RC--uEbHVVEbyyiqmpiFYSeP3UzBEGM_j951GqHZioE14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=ol2FFZJ4IWv8H4oUHBNUT1ctoCk3cZ6NeRtxfFz-Rum9CZ1JV4_i-IG_mXqdjEpKjHe5GC5BsQBHOhE3Lj8TcqNuM8KhaNDzLtrhIYm62dbb0K0ZdIY6QZUPxgCjkSopLaJTXM84qEBlq76Q4lMskeqdDF-2WzdlIWbJlMN57j5nKdrHG6gsTLxlZa2nyf4CamXccquNXkQbVpcPpVQcG2aafFrk3N_vOw-GwEG9_nvN2blLefq6bK7WHTqx2gZJCYTgZg7A47d6y_G-Jb-byePIeR3mMnb-SwHd7G47RC--uEbHVVEbyyiqmpiFYSeP3UzBEGM_j951GqHZioE14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
