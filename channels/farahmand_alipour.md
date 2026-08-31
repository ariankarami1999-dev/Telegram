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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqvy-PGp_3T0ng4Ysbljglx-XuBh55zHziuSUGYSLmUclugNZz0idfXEIHbhzSns7RyhJTIYbXgVpqh0hCHX8-7tiqGRkeH-Q1FUDszFp9ZE2W0E2PIa7PqSL1GgtHaCEkFy8cFdz5tQfuL8cPPkCWD7FXgPG9jn_y9HhjwdFaguEa-95Ap4UF6hhKrCkaaA9fNIZJhZDRDkQXNDZ5Uk7sh8dVM9oEY9h-5AR11QtWDw1q4BST8ILPyMCeP3fRLQrOLRfZH3UrSHixaQ6O3zpp3k3FWJUKqXRLDA4B6BofqnkT7dKwP9XmfUoyW_YX4dFdqMhby7w0Y0cjI9WEyFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY5nFjIGwk0H5z8yYdx6FYEKTr1VuCx3amOE066Ra8w5QBHHZvNbQKCnpGKIy8qiBHsEYpZq_G6gK0xy1ZFkUCjJScdwEOlF7ljEHaZsbGCcv-Atsb3QrZDLkjDihXURD4TCDTjOuhwzDo2RreEjmwUWUm8r9tSxlHlmIlUfon3nXoM-W74IJT0H13etPY_-3nn3A1gnJUIKjxoERWgWmLrQpG1H0rXvUhH1aDJRgx2hQbPO9_iR-ytrUrmTx1NDM9Z3f0H1MarUPH-Fbb3IwCENjW7krsdSj0uNCTtavViO2Drx50I45geuT23i5IJL3vKDfKx0S3TQRFiVv6YLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMxyf9YurJ6f4tvYTCEimgCeREawnR_1El8SbJ6lZox9rAFjOZSWwYh2Z8Z5EZ0DR1j_bd4whLz-xLtRc2fbw8zs4YXJFy5pX_eho6PjMzP76ToQkMRN_GNKr7s044QhOjkWO1caaQ1mSkWSoLf6AeVxrP_CZfu78P0T14szFxSF0k96-qvA3OVnKWBTupcPet3hu3ix_gvxYD96Ve3xzZtDehz_8UxqzL0bcfEq7ss-wkIgFTgbYHzMF30fDzkjn4AQYOMfRljgCLMdx9vU4llhYwwC5S9xhTXZrpoVIfS3xBln3KO2vNz-2UuFKOWJa9caNpZdGo8u_xQsj4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqHft56kVzqcBvVktxflgsppdUAXn16bTm07CaSPcnY7Ucz_hqnEVpPC9LgIBThjiE6NgSzc4KRrvAok06BxdAhqq6cSz9n-RR-9oR6f7l2PzXXlxQnqhEkGU7IRiapMzqjlfFiN5POAZFbKeLZzi_fuZlHVtJNY0F5cIzByCUKHxKCb_jo0uYWixMY4lfnxqe9PON2IdB09ixm0fWJPxxVcjltW0CA7Trd7SMGmKnvZtxr5wCYyldybcxui-QjiuYNSo7gcfQ1vIH4U8oZNYEs-3Hf80Fn-FvG9OCIomWck2OtXrcZFswy5OF9z9NoVNJt7aw8EbI4k2ro8AuobPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stL33D372NHb7IB-Ybq_2300QymPj6TTyMecz4EPqxWxgDxFg2ofh5XH1wo56feP4CiRidYLwy1KGp8F90idbrZtwciY2L08HeaJdn2cHSansyrMWy3U8kiOD37fzJBINi7rji63FgjVVK2JifWe_9M-YjXd8MHI47sZZ7uDcoLsLNSTtgMwo67qwvHqto9LDpGlzai_zhSr2na9DVnxKh_6AuGeiaQ1NmyEEhsbBRqSgW6pcwLVp6krJTyehK-agJV20sJOulZUxsPrh8gY4ZK1OILZIhauWYZqMwgsE9uOBSXP8CbVTULCwzhnMHA723j5Xk5DaUzTzawlA02lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgInJrahE8QEumhODZyXfOi04sEc2LyioPStjinLyWarEYprHp5_-CP87oHEJTh9NlBAi-ZMTXptkyIDHn34Ws7gsZW02JFTc-qfhnm42GXBdcfjEYg5r27NA8z983n2vwCQclO5fKfG2Cblz92TXURkqYXYNtIEChdeJGdYu2q-ubxzgVG_uX4xANLsFs6yQfFXhTWHA6Nd7Z5tlS1KelyTbFEBsm4b58GRdl57Tm2I5MH7H9Pztf7wfBc3I5Wv8TmRnwyHddvBPIRoB6mFvGc6-L6qGFT1slSWeboPMMGAgxl6wQAf2J1DdLGTxjqFz2ZvW3T-pQFGvQMW5s9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=l9yMwhOm1DJHz_aFPypWok50sQnhmG_nwZKFeDCQdOD1HAskzCG7n9tMjNB_AUG27jkN9MSLHxGuKbgcifFgKK7MhvJqPgSI97Xph-ma-CuOtPPjEZeGwHdncVFcARgdK9xgtAe1jL_Y4RyG4EMqqOTH7wovGssJYwU4mreTA2o9JHe7os-8rnshNpc-c4paKMyaezTriFvsKubOIzzuLzhD0YUV5lSVhmjOh9eyye4RLd2B4BPAjbcgDnKcIslCgSbZgei6xHWyh_gbB6dMZHcxHJZiu8P0Nuhe1o7lHwo_ETp2_GH25iOVGgSFoXR2xXvCgXYYJw9-5cKIJAvEZbe-NcB73tuY1OurzrehBiLUb0IwsObbiLDy6PYpvCPpkjcg72Z4r09WZz273USgNNgYG23aaIMoxKNWN-Wy9bbtKQTYVH0zdEWRRzjVwYBsGwjVM2jL_lh2rM0uHxAUfAw1UOn_uHjSSwpSSKlelKpP5oMYB1Fcpg3zDm8-lY6kaVM_48f5_4_owCCWMhsuazE0yYmshYyOWZ-utODm3wNhbrLCyuMb5aotWAOIWDU-UOdK6VTwLpiDAI4rvR7jswEJYHzR70b5WhjtuGB3L5K7TUDYnQoM4Zl8LeSfP3X47Ql6VQJLk-sYwxgf54aePx-h9e5Zhn5U5fdhGcyslVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=l9yMwhOm1DJHz_aFPypWok50sQnhmG_nwZKFeDCQdOD1HAskzCG7n9tMjNB_AUG27jkN9MSLHxGuKbgcifFgKK7MhvJqPgSI97Xph-ma-CuOtPPjEZeGwHdncVFcARgdK9xgtAe1jL_Y4RyG4EMqqOTH7wovGssJYwU4mreTA2o9JHe7os-8rnshNpc-c4paKMyaezTriFvsKubOIzzuLzhD0YUV5lSVhmjOh9eyye4RLd2B4BPAjbcgDnKcIslCgSbZgei6xHWyh_gbB6dMZHcxHJZiu8P0Nuhe1o7lHwo_ETp2_GH25iOVGgSFoXR2xXvCgXYYJw9-5cKIJAvEZbe-NcB73tuY1OurzrehBiLUb0IwsObbiLDy6PYpvCPpkjcg72Z4r09WZz273USgNNgYG23aaIMoxKNWN-Wy9bbtKQTYVH0zdEWRRzjVwYBsGwjVM2jL_lh2rM0uHxAUfAw1UOn_uHjSSwpSSKlelKpP5oMYB1Fcpg3zDm8-lY6kaVM_48f5_4_owCCWMhsuazE0yYmshYyOWZ-utODm3wNhbrLCyuMb5aotWAOIWDU-UOdK6VTwLpiDAI4rvR7jswEJYHzR70b5WhjtuGB3L5K7TUDYnQoM4Zl8LeSfP3X47Ql6VQJLk-sYwxgf54aePx-h9e5Zhn5U5fdhGcyslVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLC0q6DaMjnbHYH5vM0xM-DNGJK5ItGfHfvDQatfWEyWd_T2MRA9h7p92N_EOGqALQxvNyKWfqfBUj5Zkt8YZY6CqclkqBw4Z71FMN4CLW4Rp-iUhKCRPGrmodaU_fvkqBAtf_BiCUe6LmtW1HgthojCQdY939FVRGLIIIAPDEqMseE6EIaeZ2yW9__vWU00DG93nR1qpo7yTMdhkf2qJTOTkVq_eDgbk7sf1BaV9TzaLAADiNHWLT8Z1kZxOoCl5MZR3f4JgCJsrusog_PiVjwj0lbjCeBiik1NxufQcCXLVLAHc3EAQx7VV0rmlReBOa2ojJ7pD9lgL0nISRWpNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Qo9yh_m-FCZmVU-BVPv1jUW3GWBdpsd5YEoksffUExSsw6tUuJ2kxGaVeOZnEIbjK7fuBPf2gu59TWqXwEOI2MKuan4WsdB5oikbXAbDDcvBGgMN40R-OInvORj6aPdrx_sdd-1tzGUiaFArTbT6O4VaOn1MB9Dt0Ee4hXW8szinmRjIZ9I4Knv9gHGapBZSHVdNyHCE-Pg7-69mQuSMH9WhzSbIqpIt-_4a2-ZpJohtjQowSbSV0FKR4hTH3wJ7P1_Mjz57BS8CfdRlYfPK7ycEXZoYoTUSSlTGWF1-hBYnnk0uGxI77a3hINmKhc6j98EqWP0Oy-Qgg4z4CHzMRa5nkLe3u9LOZxYzVs3FhUN0aZhitThqON3M39o0TsicyA8ns7KNMyUEBeQM1Le40LydCu_wkczI73pBoA8gd_pMdhqBufq0d4VpEdBQlaOhMAZXljhBZ3G1E0abKsuBk3kQM0EEB9d0SZiYuxLYQb_rWjWURvHaRDskRr9k5jPWUBHURhTcOcS3oYMlRUE2dwjcyOLZ4zfLdcD4MMu8X35JQtNfJYIDL7erU-lC8vFMiAxnUjGIwgpNc5PqQ8qksXZYpENLxuPFrkSWRRD45oE60iig7SEPCCiYoKOLVb-ay4Oa6afF_5PhCzcAVruK1eQ2QlndaxR70XZcFChEXOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Qo9yh_m-FCZmVU-BVPv1jUW3GWBdpsd5YEoksffUExSsw6tUuJ2kxGaVeOZnEIbjK7fuBPf2gu59TWqXwEOI2MKuan4WsdB5oikbXAbDDcvBGgMN40R-OInvORj6aPdrx_sdd-1tzGUiaFArTbT6O4VaOn1MB9Dt0Ee4hXW8szinmRjIZ9I4Knv9gHGapBZSHVdNyHCE-Pg7-69mQuSMH9WhzSbIqpIt-_4a2-ZpJohtjQowSbSV0FKR4hTH3wJ7P1_Mjz57BS8CfdRlYfPK7ycEXZoYoTUSSlTGWF1-hBYnnk0uGxI77a3hINmKhc6j98EqWP0Oy-Qgg4z4CHzMRa5nkLe3u9LOZxYzVs3FhUN0aZhitThqON3M39o0TsicyA8ns7KNMyUEBeQM1Le40LydCu_wkczI73pBoA8gd_pMdhqBufq0d4VpEdBQlaOhMAZXljhBZ3G1E0abKsuBk3kQM0EEB9d0SZiYuxLYQb_rWjWURvHaRDskRr9k5jPWUBHURhTcOcS3oYMlRUE2dwjcyOLZ4zfLdcD4MMu8X35JQtNfJYIDL7erU-lC8vFMiAxnUjGIwgpNc5PqQ8qksXZYpENLxuPFrkSWRRD45oE60iig7SEPCCiYoKOLVb-ay4Oa6afF_5PhCzcAVruK1eQ2QlndaxR70XZcFChEXOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL91kTMam3NK7GpGkAJsQHyGcC5yl6HMx5PE_y34dFnOMcVflNrr-N9xTB1VnO0EO-OsTfCeUZlRdZgX4FfuCDMQIGgt2NDQ6svVmUFfYKlf3qHR8rYWz01FUmAoWMvaxaMjfiLfAusi_ncG_zHrYWj5I5zl7cRSzgScHoFXxq7JQISkkL1wVq8DAYPTRuwnqtPlWVMtR5Syha3f8ErdN-gbveyjqrEBHbO6BJbS3f3mcLrC-K6AaZ7p_b25ZdOtUkXyg7Sa_YE1WqPUdi-xFRNyNHG_5aWOBe6ltsJXatY6-JEBhYRFbJ-rvjcaWGbCUA8cAyvTVXgmDPOVHklfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK7D8U-v8Mowk6HzCWMOpAncBNO63i_gfqJMDRIIGc0UQX1kTNe4esnGLEQ7tpG1efZ49-mARj52MZkeFHBQtAlFGy8VREwq3UqlWUyk63SUK3i7eRRjDi4ILo6eZaMQs1LNdzPkLGdZadZ-EKwOJa9SFk98gcFp71P_g2dvdcgymMUER9nzmA4zFPQWvy9SMQQZtO9BaFVrS2GbyWHQvprqYD2NEwsXRRrNCo97Z7pK7WfKWbwhoJ4RtYDPcxKtwxCZfs3En6vkhUdzw0olVR2ziNJqCvVACe4ZvuDW1m_znKArtPqeWDXfMSASYf8dL8k29fXUKliYbx0ADiltdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBfJCtpgoRE9jmYH3AeeMNUEsXm2eLTP0HmzmhHuB53TZZB_46dbEkkLTPC0KX5tnN7qLaGiZ9mNFUXxN9_fRcDtkV4jhKOs9S97O4ZGqf1k_i0Uh0cKPbHe2H39-jUmyRmrOMv5iQ-FcXva48DAunom1mOvHO7j1mOEPtxuFVWGgdj8U18z0evebiLVq1D-H-kmHA7eHoaUvRZz_q72Hnk6oogT4CYsZoplBVQpvpLpbtbCOdUmOg75R4Kp_NQthImVQShE3fS7Cu_GEFgQ7qIQEbDZjxVnDc2dLLfpLYCxwcJPEk-IMOWWCM4wVJgk7IiD02TfkWmYPsShMiJ1gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYOkO00OViJArLuDIjvv7DqgukL8BN98hkvig2lSw9k2IsOL3osFbp7WLJDPH97oR9a1IxCKSV54cjaZ1d4swSN0Y9xb5oa5ANFY9UvAyGVjUxuOXdZ92IOd7jtZlP4VKSHfFXylni70bjCOnjf9MmCNcZfvYGmv6U5ek6ssOVxhRv7GetUkua_H1WWf37HA4jtxN1YPkV67QK87uHqoHNkso_i2fm7_JeDKEPv5PoawThBn2KTqHXdrei64d06r5CPDsdoNgCFrfujBwV2RHKfJi-z4GZwib04YM09J19WySOVmPHeZnAwyBhy7CnTNYG6qOk8TmuScqUey0fhQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAcRhDsA5dnwLZqwFSooJ2eoRdG75Se5CZp61qaAWMhmHCNAq2vITfJvSs5L99Nx2LTMijroOk70WM4ldpm08CeaWtW_nhGSWYX4HtpQfmsYdvpikOS_bKlo3kiv5BO4f__VKqSHMw25douB4YOBdBDt-vaeF3_Jw4iJHJW31Z70eU6chaRFHuP7EUAEYjefYQhJyahzH3WLcQvu4pEZQ32ACwYXj2zYbP91ylUtKX1hmbnx1PMXfQl1WljGYCZT4x350bxT9_4zfBPJBFUsmZK-h0ZY5fOkiV4bzkJGYBjJznCoBeUmExS9fQIccRMxCN_hWkCvsdF9Khh-7Whu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCDmBC4rzfyILSLP0sip2oED6HqjLNWXnDGjE-ucVvcoSTyTRzgViGPoaED_h0mBmOrYSz3Qs1zjSvNAinFNyKz6GwxFBVN-9h64pLKl0v0bLbITHSoO36s8V7m83Cv_aMV8oY0nRRseSRKEy8xYrNyVfKjykOE44NQ7NzVCK9xbSFxPurVR09qz3GAzLJSgt-KoO6KUh2p_ahZ5X4W1gVwPmqE9tKY-ye0bBPFzhwkm66Z8-X2x4QKqMfBRWlSrCwo9RM2rgMq7cmhG-KaHbbhxHJgBt9e9VfAxEJGrbilV-LO6ji98FButZYxbsTvhUgSgV2QYhAL3dF9y51Iluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq2dOK7fEQnaMKNjnT56XnTQcoDkdjJPVCOHGM0Cjhhg_GxAmYIKfoZIhhn4BkSHIwce5fo0TTTtjguCHownkFKBJVe-EItYf0PMakFi2p-ZlKRDIc8BBsnFaO4jdcIfEM8PqxNFNTjU-_h2ZtI5ullorGstSFkYajqspmsylwGyfBa1Z3qw9ZHoNl2Cz1XNIioTvSQeN_J45Y07Si-3Q-sfffkmknqf3v0Ut-pspsovruXzOxcflobyoT-tFe_kkGr6kxJPjQsg-INdtwXKCGBc8WWr5IMcpTlUGx6IQF-ZuQIt1WrACsZZEO0UKk_2AewXASoq57ntYi6g2qHZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDKcjMYbsr5BJ-IwuZ_n-V8E4GbtTn_7JoydIbpps3FS9W-GIdbiUeoNjrAH-oOowzfHuaHfGJ1YbSbsXub9dzlXFOCPeivxmNsvsGfJYdHvPqrzDWvQ8z2XogS1FJmunmr-DEw1LISDOjzWDDKXK7OQHtOjuwJPW4hnV3qC8PDawex3_W6u5uizW2cE6DJHOSTB4Mvmr9q7cajTv7a9WDKbBIL4mvm2ezQoWEaUbS0KYTwDyGyk-YmNZkgrWY_yY49J7WzyqlxyySFijOhYUJ_kL95pOfExkOcVICiQQyfe_XehLyH_JURIXhJXLBFNOxFG5LxY-Pj3ewZy_dTteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmAreDNRqb3-bC0mBxU2jXEHluM6fUZB1dm8UT-tIAHW87C53YQ6_5ILCrfPFY9YxcoHevdcb7p4hjOWDeVUkssSbn2QJtRiB8ZU6A0E1VWRQJiYwH-0oTnfX3p_XbX6m7p694A2bu2s56f8Jaa59FL6HteCPfRtC9TfNed3RVBtXDSY4KQH3BiLfG_FsNf6epZS2Nm86iqpiqOJYIiSPjjL0Ir4PX54-W66X5p3XHbdLXZXyZ953n02iR3C950-ZC5xMqzpHM4ejUtb9t0WrG6ZDuX9QiMZRTo68qZNoDJthwIeYnzQaT4--CbwGYd5wGJ_YZKhK0kETPkX9xYxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmA9jldHOWQG7QuWU0PP2F4zxASTpK-L4youNtn4EYT1WHdQyKuGUIzsssnvrUEY73qA_Y_9fC0N3U9Q2Q9fvX5aa328yvdnehkhpT3o2dzm8oJrW6qpA-H-jTQwEOY82xir-xmmMppIc6jfwAR-sm2TlyatvQW3RhUWYKZazGozokfVhjtK9WbBbDnyX3aO7Ah156vFlBfXaFLecnyKVL3VVvzJdukC598WNRLWxgYkV-AKtUV7viNMYPei6YC3kcO86xOXiSgHxql1ne3JtP_8RrqF4K93nWsM-If9iiZEIgC14ACEGzAeJ09fShy2LdXxDxYP_CN54n6_NtsDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr03s7Da3qxhE86l05YQNi87srC-_olUlNTvtb_SUSLhVXgdaHxYnv19jdwM6ShqehYxJJz4YB-hfHvyRhUUReRiPZPCji-oct1xigtJzmfo-zdhlb5q1wmMzZaTsYqV2xKFK5y1hkfieYF3HlG2F82iIp9scRg-_UX4R641b7geVcem6p6hlg4XvDkt8zTPw2CTnlJtLl9_3Yt4a7ABHozW7TPVcxdPqfsgntRUXP9U3c2uOsbvsZ0juI1EUENMnsQo5Sd_KAyNPFuHJZEY2qtqFJdsxoF9dFIH65slybe19sZrg5EAJxJdSKcanHMgV8fyNzDh46agfCnuMBS3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0LjMx4-B8JJVLYNeSsKepQjdMkpecUoS2lDtWFVNu7B2mfoII9Ockc74PsztLUZhkvS6HcZwG_XrcBcJsGSZ2gr_TXVdx7Y_e6bYpXlK3GDiY55J4_9QMzAGUS8_cqE1dx-JvmLruxdQZz1tflv34qyzedD85C-4fHlbHJr_IO4gCd6jRkc006B77haKaiFD87yBXj-Gqn755f7wANWkRvZoa-3ftIlBox683q5drQWAvaTTu25HTwX7Mum26wZsaJTuOvZGEsmhse1f110FHKZ6FgW7jLdQT6EaE4N2cPWCBe9gg0ZWGfLmlDh_RoHMdmjra4_V3qs83s0O_7J4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4Rqp9nXNUTz80D9Bq0xSi_RnKxIQJW7hu0uK0HKFsV-h2Frv9HYia4wHyMkqDmA6DeZ2_xkE6ZW4pgZavifU7bJwuI97tPKAEO7h11L25a_7HjHWETh5d8QChhgW-aMN2G1LewlQtVEuUHiYfYkC8oJ0oqhK2XMH8pZxZ_bUsxYIAUxzVNPXjE-z8O7pBFgB9JrAzYkiXKuGwOLbBLgzmVa-JNn0QjQwlYUzHZ1B0FcWhWLZIiC_kA2c3f_ON6RO3EdGrF6FlIkBk4YGwUNEcXQ1dcc5FmgxivYiXdcA0CBSjSOfVjpMs9HZtPiS6FRXY3-am-TjJqkWj3BLg9Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cATCNAMkL7cZxgSm19m5h_nwbED1lAkvz5vKN7RH5uyK2wlHixFnUF_tRLemueJWznh4nc-PI9MDx-Vw05dZK_3OQuMa0n62MJfXDSVnTjot6np_9QioGhgKAIRHw6Du-pa3_dq0C_AnsuA_pncE7Ugzb85ZpGlSuWi3nRgoS899L4AgwDx7U9pwp1O3y5EL5FcrZwjf1na2lSi-BkwQamyhCJCZHKlA-fFRhnBlyVRf0BQEr-4TWguH_QcAc7X4GNWs88-xkPOmKHMfBatGZ676AMMB5egZVMotNXllNDUN6pDmuGFjwm3t_2bJ4y1jW3k9UFNj3eFn1PMwQffmCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfqB1tMVXjgdfpGhpLeaFmOSjoiMLD8fAhnNIMoJ34gUgJC89oa-PP4FpaJKx0X3F0OoR5aV4rDDKB2C4OjOzdhsjoYyR-NEqMnAhByND2ft2WiH0iR6hi7OJlzfoie4c4m73eY0fntj6DsaTztNKUJZlw3LXL6OHFJhuOOXKzvazLhVFm1-DcZuLXz6sEUPiu7HaEJE1KxL7uMeDwbc1wk5cTRo1bATBTL_tpU1WgpFaz7vkdS5dxRgweQAvOgne8zVA_IdRVCWkqpH13-RlJYR5cWpp4I79eU8bKG6salmZJPy-OXnokMSLCI_fk1oyY7jrY3NpBK7vtoAXT840g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUXpqxBQGmE8agfauJB79w1irVaYFWuEBFBqbWdtUo7z7fNtoa_MTmI5SaHc6HukLySp0FwI_0BdwuWSa3NOnpTji7arq4RA70pKqfWTldM60PuA5nWwS4OFqrv5EtCKL-5SIpXeub6pMTs9kXoHaBju4IwZU_6l1BPO0zvxJ6U56c7KhW1wJ8dp2MiwSdzfRnLED5dInIgkG9KjU3KCeM6wy_-5QBNzPouyuxlS40hwSRs7ffeedQPIV-i6QU6Zkmk3Fv6-tsaE_YQYBnALSW_PIgzrtKQCh9MXUwhcjI8Z4MkZ2wIPlnJV13ECew-w-36EN_eITnbHWHOjVuFULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7HYWm43oxT9ruV9joL9sGyN_uyrYGqF9N1sDIFkgNjbEEguHIUrgncb4OEAUOPOs-qc4CI1jv-DRIiaI7WqDhC0G2qxrxtczeqsEDThL1XIZF9lpYtPTY6kajsIvFmQYxEpuXzpFIn0BxXeZIh9DZ7Fei0m8PxgPev_F-UnHonv4DsUSuXKXQCanjsUkOmwM-jcCefaEriJUiN7Qs_JirS0p4wYtziHxRI1bzEl41yAClpjxFvGSA6d0lMF1PXjNK4AQ7R4EaC6kIL8jw8DwnqwfKjKj829IbjSQNLPkyw1vcIohcApH_4b1wvbOGAVux42YV1Yb3eCgnXDnbN-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLp_a5AOC0Wa4DlC3SHRF4nunarzxMmOiChAzVkwoSttq3PYlpuRWD0v4RPxIK-GjlIIZHH439jUPX5w3JHrQy4kwDDboDzylh_vvh7-ZRELvwaN0CbRNSg4IOKUktBJ7M5zYE2lL37AhUs8n2mXz-tu3B87sa9O0HjqT9G2G7JMZL0kDSPaNxAQcLNh24r2EtgGBxu7c1sow29XmcR5PQqad-Kr05CM-hgKqcfWJUPzBgMZdxiAd8j0-oJj3yqojoVp___4-vsa8aLifQhk82RLLVE0cb4oIDuMGRaoJD5pWhnDrHmEFpWDq9StxamndXCE368m7jdR86awJeb8xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4JfZAHbRZ6hdfUbiQasDkXGQdiMvDjn51xPa3LbvC2yealC3vEhIaGv3zX7xWPsGcZno2RwLwBJjQ2KrzoM_pdAf92iAILuxQWpbW0XTuMOEKwsB4s90yrC0dxO27T_tu6HRpCjejdCCu1Ww6xaE4K87CCRhJFSRkvNsxvTRpw6gPS6tWThfaJyvllnh98ZrjXT0mYmQYZlTpbT8Be4clwCUs_WWCAfPHO2n9WBs-1lOACIXT5vZ472L8poU3TOWbgc8vyy0uKC4mhIEl8jixh8uiRSLEjx3k_gC1s9l3DGquIrSTEVjfr4Mvvh7s7CiDVPxqaRNlaGFczXbGhmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFn_On8lOYVvNXjpMowjJXgjM81_RNdGvUSWVhKZLiKnuOXHe82Tkvptpp4XP-v0tMz_RdP0Sc88GaP0hyV-1zEfbTfzvPk4DSFPDjPFFP-zDoAsYubKhpgJOZCkdOoc5M8Mstnqcr7qFqryHMRkomwF9AqRq8yipUidYv_Ld5c_HlMfrwfGwGnf_s8hSIDGk5pONPh9fUGoVgsRbzh2kQMv0UqDKHgT1rZr5WjHk_-QKuVkOfF6ljvwmeex_3k_DaoFgiayGF0NRgyF2h3VoJm2ViKG12ZQncW-6ibM1vx1elA3E-9hgbjPRnb4pbQoqGBAzTJ7wAWJuoGPSAUUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGEpBU-tFE9l-dF70mzjTte3tKEC2DfERqgtBAtcTKT0VYr-hERfs9d5OLPdQYVT77ECwtrIwSB0bJVbCKlrfRLr9wzmPpqYQPxZlxO3QcGD2MGFVDgDv0qxeDM2NYxdIok0EXqcn-jRXlIKROCXyAY4YmgG8AaaK999pTqhLxWFspZNpPKRVu_rXMd9FnT_dQFoifwfHRV6o2jxEm3c-KuRUBy1d3G5HVECu4l-BVxtiXYsG1JcEL-ED9JcPNdd1gz40HCqIX905ngwtHz-mULPiaIR2-LvcYhOdv3diUYrw_XMIGrMUsnq0Ff9eMAFkGZUi8ZVG0U1WDIVrFeqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMi-76PvQK6ST89pCD_IMSxeTRhdPflpidDtgdGfJV7Ov0bHayujmAdAixxsEmm5cBsXXEddbag5OdFQsAcenZpIENm3KCwZHuWEvUTl7weYKxX6SKqwPnAmGZrYE7Lqug_NDAp-P_fZo-s3oWm4jB-RWbRe1PI_1BUOS1sppOkhwhxcBEfCEnqwBJRY9kqjX9ENBHtmzNGZRZkehSgxKcPgZvZOGQYnoGl_apPKxdZ-kVWvOR3TVD8D9G54OQr7emg5PRpmsh69UFf7oD2xyD_Gn4KSnR368_ARF-ICWrJEyayD-E8tqbl4NQCZymeMVzTGm4QB4YBsfcWgTHl26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYgQqvr4QQEj9eTMvF-P2fUdQV_6EEVeAOhqSX3rYcETCedKmUMr7Kif32l11vrubn_q3wJBgUFgn5UWsB80UwZWJk14jHlQ2NcZq8JvofJIn9JCheoSQq0O4t0NSIBImabt3HV3r9QdoeG1Qg95_5fwdwGv49UgCIBkbdmLv4Zkz9W6lD7IZ5AW5zQC-l5Y7waTM1H2AxY3N8tscMioPegsIyFj-GmsWcEqC9c8hFDlKrdJZCCinQ6CJlYtZtCbTs6-wI-OgQOf32Zj0Cbvwk1Aub-jX5ncrysu2XUzJyYNaRmEUelVK-8AbCaCEzwvXM9EdD70AmxH7RSNSUcevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjWX79zwdXSEF6QCBpn8s4k88_JP-arR3uVtC_bib8SVnsKKsfzg3tgAMfCp4-V2Scd9TNiz5GTWzhTck-e6MemPKGOsAhhAyZjSMAJslYdUVlQq3DY_QQ2rmYW0WngGyMTHWob3te0T-5HJUfsXtA23nS_8RcEYiSWBU7EBDOI2KIsZ8675CoRtevh4ORpmlM-jdeXDxufjOTK4Suc9L07XfE8nSgskfpIHNjlnpPu6j5Qf4cqh42K_rjiXqc84haZkz8Kz0TkUMT9V21ivSsgVHlH6H1b126uI4dsG3MbFFW7H5U0nOcRlTau1QKOrQ2TGBu6_xxCLcsO7CEEMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guUODq87GC5yoJdjmMiAb5N9QiuI-5UDPQ5cRXxo5d3JfeWDPb67SXUspjqr-MLLbWYwBI5KiNc-5msVJ25g4g0YqqXFWi_A59lt0pw1zTsZOz05o6_pZLE2xJbY3e7vE_09Iq66d9ku5uVM1aBmRAwqHJsAwejrikUKSAWFoP3loX56h2PtwcmKk6mEQ3IKgk8v4CL23Dmnpbgg1134aCe8G4jEqJf-wjZ65PqnKobFD-TRR6DH3ld56CpoRJF-WuMItzk39cdS0rkow_w1fqqL1Vae_XOtYXJnojpTtKXOnJzjf3HiA8NU_JGlO_OrSbm35EhDVwlQVxxs27W44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5652QOHjrYfB7bLfObr13LETOKSJ-ioKGVKIaTkwMNtXtMH8YsANfoQ5bBTFrEtK41WZoPfZ9TAXRIrWdmNpnxrQ77R08q-_ONGC9snDRC_Mfq90i5REfPHWe4BVhmA7rYi_yvheYBit6P1bo-3yT1p9INcok2Icm-CeWihSo53KqNILc2oyktH956ceV5PpJzpg2kyhmnX3g40VqjvqIHdn05AfSft1XDCQEfWu_RrS-uZ1FyLN8zrE6bp3nd0HjKlScXSYboiWmd-M8XyJErrNeeqh1GyuaPUhmgPhqeSppNh8kD8LDoU_qNO50k5LIfVxMYDKke0iFUj5xVq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmYyJk3rhf-_3DvpkemFbnfwg3hGy7Khu7C2WAjGQut0zadS5N3HwOUDM1wz7L0QeMLqqLzBFpbBJIcllovV8DunD3Sv-P6RejSWNGMCoyPXoOxnAy6Ijg_a7-1moaL_CBpM7a4xa2wFKHAA_Cv1bXcJV772M107_kNECRYSpTthpL5SPaQ8fINVAiUx1H6C6QD3k_SBplFs95U4v36nM_izhW5UnM_yfkGQY3LE2fpZ04mrwkOdJXp4HGK48UkE7Nee1mws7HM3c4mk_itBWU2YiplN6w0VsZ8Q21RJUdzTZ8XyTlm3zOLN-CDTPwW836wwIkSBJtMehyeirChxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLFujV1stHO9kXYFYiqm44KmMcs78xYjHFk9p17WyOoaMPIIe4fPlvNHauPfGREHPeHrSCB_VYn3mFn6FF2cO4dc66RMTg0r_pvzV4rr5nTiHt62-kiaWRzFoQhMGfvUYEga9oYXxKoLmI7gnybZ7Vb_d1Hk61WfVPu-PNOWxTg9LP1V1kzl0B9_TXVrtd6iOEdss3WBZj4ilOTIoZyHgvGqOcheNzuHoTGN83WxRvrz3IZliYy7F_yFBt9g9SXVQIHVfM69U6VUFazhbr_WwaSamMPgTqgz1bKFb-YKdpQuU2mSF73v4gpaBgIGhFUoABa-N1LlbB7SgChTPS7MwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQmm-nI4j9h-wJ1K1Q5lfT668f0l5_TN0KfP7kNS-k3qUw5Ha7hHRYr71y816fJDFrJ5ou6DwLK7Ghl0wyxoV6H4hIoVeaJGDw7jxGrDGqgjk68wug2QVqvmccs1Goa2ALNSasxaKcZCIT6cdH9twgl_2tsRcZqL779teBIYkCKZmiw3Xq4-V3DSxmhRobYLeLmyQMYFdF_wh9o9Z9i5QhpD_hMJgks6jR2Ij9pa6ebgH4SyqqydnXWFX-mDt4I86hc3AJxV2s105FOOaG9zJUadqQTnX5TjG6vrRE4YRbV1AR9XSmFppRgpIiWCXlzlRuumnKquaUN-5WfkUb4nNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxrHnJiIGjCxV2A5_bqYlRKCOu74EyZ6pAxr02uwzZRYlzClk9tI2d1d0wXZBDzH5-Vn7tI4WiE_qqd4skzJfmzJ9QVDRC_mMSLydcm6u50fGjesTNfpKNtgXrnpXOjPOPQx0Ik1-mlnpVJtlJF2pCXYDGxqGI8gQeWAXLVW-gnmCIv0hmeDRUBjEV-P1YEFls76x_gq2SmGPxHL9Orw2RkIJXYy5i0MHbnaSs-KyPZRn1LQphQ1N8a6U3f8PALpzpMTnSRuB8zc93OyWBLCMM70kzdTIxHpMFVHyAskjciWiypktvyQKCxl7vVD1GwpNvik04eQbf2Tosq1xxcmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huPnnRy9Sq4MWrlbypYjd1novQXeqK_IqArTc6vdrAMXSc0EmYR0mQxG7RPyGX5v13mafl4u08bOugz-0oKcn8-JQeuRVu8dPQ9Ickr1Q3rFz17sHntve_0SX2kO_tDHGZtZv2WPTCYVtwDDmoXr6S7EReAb2HaiZTd7hsTp2wvzpd55oGeLsJooSwZ0jKGOut5XBFOMJ7bhLPg7YhRXk1U37b_GHA9aT9YfjpcEnFjJ4Mbfxv15RgShbhk58iywUt7hkx93oIufmeLbmcM2PBYcUc3vas0ajKVxUqSJXLIBavzGVeX3Yox9N52FQzgBKHDCkkr4BadAIXado4N-zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq6I5AjyHYtsQyIhUOp8j-7wtWDkqvIf2G4nc_1lQemVz_GglkMTT9plegJ4gH1KxL92UdgJKd1Pv36nvgAhfJ_JsS6yoq_7QzZGbuyyQw0Nq4vTs1xop5FgFM2FA8T0tTfpvYYEiXcwVeHHvq0DZJsZjQ2_7jtCQKX8OAAI0TmnGvBnJZX0h2Ns-MDA_rN6GNqL-yXmQ6VlufXOS9-SjXmiWStidcqC6f4LxaNPBXGQ0PJ991mUM-EOHf7mlRpLoMuSlauSJNwaNqUVaRFWtzfLAEWkusmxbq28WgfXbIfsW4Zwqcafk7E4S4sk8rOa5C4620O1fVrxOZegP8Semg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQYH6uxPZSHVMmjtjeaRcPN7qKTOobMupABPoZwRDo0xiWf3S8zF3HKzYn9hq0pIpXGj4EEvMqddQhglw_qJaYNZ-gWJZtcQbL7wfsrIMPV82ut2RytM5O0p0SSORHzz0_PZL6C1aMbn30jqsVnNn15vgCxv0h3aY0lBh0TG142eGM-KUXqgJg0YITrirFo0yShy9Cd2sVOgWmm0eFLxjwl_C6u7PWL6tm2tB0uHS0egJVpi620_6v2d2L0xQTq7mpgJv7DKF29rrAOuGjv2ZDPjo-vC1M_6HyY3Y_nfJyenvAAIC4OWJ-5sm0zEMFY7FrkZ30zkuMkQFMxjf7lnFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7FuA7EDfTbCPcQcdJMbvEPwKY20MJsfazy7qMcc0V29LDY3AILBe-Bc1UAwJCa0KOMW-C4W9S6DAHiO_9u4Z8ZafQQst5wReXEFMV-KY5hSuMusC3mywUbqTjZQe5NLw_j10CLyN2ahunjM199UATauGxIFkwKBB2P_YTbY3LRjiAb3ZV-DI4J3Z2wq1MjyFoBwQLp3s07RcHp3s4gKfBzwO-vUmi_Mclf1cxAOr4b6dMtico3kMXzPO5yDsZgV9cnFtRLurU2vjDZf_-nFXxF6PLeRgI4BrVuQHsJmOQbpkIEwdojvfxkDY2tUqA1kcF-m_sORWV30BCSBcSCmDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=kcMEMJJ3ElGRQZfmLZGFESRdFbGs-KEAUwgyjt5SDtulLSYzKrvJo7Ls3_UoltY_cIrAL4-sKwFoIiIaVZsXrzjksGpfJfxvwKkuU-308Qm2FSTDhga8FqVp_tteTGNqoCfHBLx7euvQqHF6s81RzIcw6d2lX9BDTffa2mBpzOEcAk7-TqPAjjcLLKEDe_RISBVqObxHrZOG5vGcqhBjAm322siBdessyD5mbBDuNkevunCwTZWTR1c0Lmy76nzaZZSn1IQQjDcThj4wwCE53h_zyloLRWgt1Gv8c8VMDu9KfxdNhwn2aTmbRr5mzrGlLEYYmp486gOpv763UOvljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=kcMEMJJ3ElGRQZfmLZGFESRdFbGs-KEAUwgyjt5SDtulLSYzKrvJo7Ls3_UoltY_cIrAL4-sKwFoIiIaVZsXrzjksGpfJfxvwKkuU-308Qm2FSTDhga8FqVp_tteTGNqoCfHBLx7euvQqHF6s81RzIcw6d2lX9BDTffa2mBpzOEcAk7-TqPAjjcLLKEDe_RISBVqObxHrZOG5vGcqhBjAm322siBdessyD5mbBDuNkevunCwTZWTR1c0Lmy76nzaZZSn1IQQjDcThj4wwCE53h_zyloLRWgt1Gv8c8VMDu9KfxdNhwn2aTmbRr5mzrGlLEYYmp486gOpv763UOvljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkhW6PvC2It9zQ-a2pn3u07FCCEsaeSJdqQiAd1DZhtBJ1F9YFoYdJ1n-rWBOWD6hqM8yP53ncZSuFNIhZhMr85mLTW2htdKYYkcejVMwcVoUWQ7u9A_BXjXV9hj83_nySIKchRSPd9EDn2Efeyu-RiCY4xK5sEij1MByq0sy2cQ2OCy3L67AeWrTC4CgrtrlYfgfMxKjqwbKWI7BCKg-p0-lNspPViHRTpxhy3lWi5RPulXPdO4ZlnlCpT2UYvbG88oXadovMhyU1OP2xOf-s47Zts3lFXikhwpJuVOBOF4q7sH3gWnVNsssnzGUDtX9xYFzSkELay_VJ3U8T0dg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=JmYwkrtyhfNQFW2Ik2gdgYsfFsCAROZWwVVRGPby5SD9Oo6YqLUlRKypbPf_nX32l27Ol-NrZsZPhLkSJ2qFqAaOvwbo4clX0EpR_GgQGQ0dQA9MYwSkXSycfqAlRZpj6T9bB7u5GfYYbkRj9uRQUNQ2sGizFaRWYuMnCn-aVO8PSIO-S_LGJ6eXH16YwZUo4v75a0u8CqcZpZ9QTEKLLWWLtDC7jAmqQO9YD9L0dzteMn3B0x076dZqT641UTMJGlBkRVn16ybUVoCnBdTRVnBySwJ1HukDod1DS0JeRraA-zEmYJIb_IGOgJDIF6mPw98c-XsheWVmbrBj996fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=JmYwkrtyhfNQFW2Ik2gdgYsfFsCAROZWwVVRGPby5SD9Oo6YqLUlRKypbPf_nX32l27Ol-NrZsZPhLkSJ2qFqAaOvwbo4clX0EpR_GgQGQ0dQA9MYwSkXSycfqAlRZpj6T9bB7u5GfYYbkRj9uRQUNQ2sGizFaRWYuMnCn-aVO8PSIO-S_LGJ6eXH16YwZUo4v75a0u8CqcZpZ9QTEKLLWWLtDC7jAmqQO9YD9L0dzteMn3B0x076dZqT641UTMJGlBkRVn16ybUVoCnBdTRVnBySwJ1HukDod1DS0JeRraA-zEmYJIb_IGOgJDIF6mPw98c-XsheWVmbrBj996fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1nAT_ctSAwBdrg0oi7qcgbr6cg2OpmWsmBiC6wu7ZLBGD_Nh2klrOc90zNlW5NVF5lF2-pd_-myBYDeYn699TSHBNCghI5fPftTWhE9T7CFKeRAzXFTD0MB2XqbPxgEYYTn35UGeWADmHA2VhuF_ct9LhPdRSKvc_4fBNaKFO1vmETbCaO4AMlVc34cvWIF5meHVr4v1O94gx-5HUoDC-vVmajOGeuqPX7QAJqzEwQH36g2hot43ellr2uxATveB0GKdga8WZXr2hHKuGmeZdsa8h0RMpb6R7Oh7g-oLb9UICRFb8BMOp7iM45pC4sBtZ-NEUlu1T2SVoc1ANwU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2e7O_NEqjAxoUzsmQUPER5aUIRR5DZu0pp63dOyNGFDGflRkxq6sDr6sc-gGP2MEGk0DodZmoKI31wiYd6S_oSHvBWh-3hfJtSZcHThP6xugeiE34VtrpI1iAUCq-maBmy1esVhz8nwXFouu0OtpaVr1leYjVhJFfvdabDpYGzOwsxnrv-YeAG4j_YWHsmGofKixM1m0kyCaz3Wz9coD3Kd4JCsidET--16msHZSw0RBuWoU1OSoUJ8RIJBhmt9nZIqoUNic_etJVMQ4MlIDGhYd2PhGa2p53TD5oLtO1Xm-VtNBA3osX_aJ1umLDPQeDamAZW4P26UVdLR1ipvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=PPkv05zj2FVuhnE4--yOPEn24071R-cHyiANJQhy8jKndfjbY-oPplW6JQvU19c2_vIV3C9G5XZSiQYrkKG-GOTOtVGyTRTB4qIgzO5IoMY8Vk9MQBwFjfDih4kDAwxrnNEqlLiS7_0PxH6Z8BMiD9N9VOz05KuXEoRyDnsKtMLzCrPE0QC_pDNIfX0zqbNWi_ZH0yStlfb1qaK1BpHrnzWpIhuTBnMoACNAE6s96EtCm-qPo5E9AbaG0FKvpFpmG-DTNEcgGM3vO2Ce_BUpHzDssmnhLtahIOjSwZSt0HbV4_YNE8WYDYY-6FEx0LytaSfF_9Ql3eGOHIXGklz7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=PPkv05zj2FVuhnE4--yOPEn24071R-cHyiANJQhy8jKndfjbY-oPplW6JQvU19c2_vIV3C9G5XZSiQYrkKG-GOTOtVGyTRTB4qIgzO5IoMY8Vk9MQBwFjfDih4kDAwxrnNEqlLiS7_0PxH6Z8BMiD9N9VOz05KuXEoRyDnsKtMLzCrPE0QC_pDNIfX0zqbNWi_ZH0yStlfb1qaK1BpHrnzWpIhuTBnMoACNAE6s96EtCm-qPo5E9AbaG0FKvpFpmG-DTNEcgGM3vO2Ce_BUpHzDssmnhLtahIOjSwZSt0HbV4_YNE8WYDYY-6FEx0LytaSfF_9Ql3eGOHIXGklz7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3nHB1uDpvpZiTEhNx-sec-ebSPyPnYt7ILJXJEw_NVIstgsgIagu1gWEXZkjjjE9c3MyxNq4mdz3-DnnUyeUdckF50yt3UyslyIQhbQIIiYucDwlyN7uDIvkIqP0oOjizUjIX7XIkh30Oz7roG1VnWg6_goxv2DAxAMQ7_DnegECXsFUUZQTyeIit-pmiuZraQz1tcdudv9Nsbj2AM86Kbv29Ee9VWtJMSD6lEGCbHKY5DQvVxuzTaRj8MW4CNEVNbTsH9jp_ekxFE4VkKLngvSc-zwgoRTnhT7QyYwACGWiKbbnXbfxQgqjdqyRPK9ihOEZnjvPHTKIxjR0ZHkGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiQKXT5_SLE7FSP2cuVlbhYMAIcrHrVtYopRH2whRsb8DbasfhI3SiAshOnr1IMU6OTqomQ1dGdOdRQEmNp4mQc4Nejo0xh4yANrGCX_XcdicekKszSIOL6ze1_0l8eHybNNKGbKa-EmioLWtGEJEuLnN_h_9dxvjFEywHejw_0_rCrDj3C9qPj4N9KrNPSv2t-3ubP9PhEB0n_vPgKvPrVh4Q_EAFbtd2CKzSpP-MAysmJVIFtcu9alqK1x2HdxLgqMY7Hv3su4aE5dV_Qw-7vN0xPhQahY6Ab9WC-aawpS786iq5zI8hR_bl3nzUTwr7XIoUmgtx3dWbQTqKemaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6hFCz1ip1-rItYaAkO9-c1EtNywymUQ1ZEGg0rnrP7MXITA_303INGIyumIc4i8dEvuIZEGCVRe01l8XdqmUDf4qg4eb3Y8OHkq0pKn8bQBXMFShJB5LBGMxviib-AXHT8KR62nO_LA43uJ5xoDwSOxRAYc8Ff1wBm8wivfwAVBn7lu1EGnXaR9ZN6bjuBUo1ysExW5_Rj6GyZpgfmlVVWk2CJhbM_g4NmWHdhCWBRsPXs8D5py5ilSXCJxtwPt4Bw2TFOZ03pM0iWUpSWOk34wdIP70Uk9iGkecvBFt3uJRgYxRBR-QqGw-iy-EH4Gd-IJbRKkuUQVJToZWCCA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=fNrE-IFuuENLgwErpj6D5itt5usNfw3m4p6dToFaC_50EzGRMeqz2HZccc3LFVVH1MeZ51bznY4zdg_R-CMTVI96V8qFQVOdmmEcvvksQNeQYI7sxafwcHijmvNw2ZdXMWxxcak0LwoagQw_s7qN4FxtgqMH6PLKvEJVQqZ7B0Z2eldiZFh3mNBXhgUisnhpZD-49VYo1uPAQbKaOsV_ASZ_HwFskyv4NG3RfFbSEVnbT8poRrQ-4hebL-6V33IavZcXh3bwkxfuegwm_veleI6cqzsqXvnmShRPSJs1NWD_qRfRKuZ0MLPsGsz2GexqIC3LsoNQ061M_CtnJShoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=fNrE-IFuuENLgwErpj6D5itt5usNfw3m4p6dToFaC_50EzGRMeqz2HZccc3LFVVH1MeZ51bznY4zdg_R-CMTVI96V8qFQVOdmmEcvvksQNeQYI7sxafwcHijmvNw2ZdXMWxxcak0LwoagQw_s7qN4FxtgqMH6PLKvEJVQqZ7B0Z2eldiZFh3mNBXhgUisnhpZD-49VYo1uPAQbKaOsV_ASZ_HwFskyv4NG3RfFbSEVnbT8poRrQ-4hebL-6V33IavZcXh3bwkxfuegwm_veleI6cqzsqXvnmShRPSJs1NWD_qRfRKuZ0MLPsGsz2GexqIC3LsoNQ061M_CtnJShoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=AmiGWDo2zkvlMoNHE_BfMpj06fsW1gC0YovtIf7glA9p7weR6fjXbSTuxJ2HeKP4j44LUE59YW8lxWiUtbmZ525krro-aJJRyFQrBXVzswcv52lTxIzVp8rMRd-8ck9ywPVPeSZj63p0EAF219csrtGIyifGClXaKaD545tYee-P7kQrlpPR3RcSBJgfNrVYaQ3XCH0SmlgS3cA4awUZMh-vLjhXHs0BR3MYfxYjDkAv6fFQlgqXQxxYAXGmjwupjyZAmBY3Lwsz8C8JmxVwLyJiVa4q9Na7KSzDnKgvO8ARUYACB6mEt-0OMQYMcZJWd58jHryhgOrfAjvtao_E5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=AmiGWDo2zkvlMoNHE_BfMpj06fsW1gC0YovtIf7glA9p7weR6fjXbSTuxJ2HeKP4j44LUE59YW8lxWiUtbmZ525krro-aJJRyFQrBXVzswcv52lTxIzVp8rMRd-8ck9ywPVPeSZj63p0EAF219csrtGIyifGClXaKaD545tYee-P7kQrlpPR3RcSBJgfNrVYaQ3XCH0SmlgS3cA4awUZMh-vLjhXHs0BR3MYfxYjDkAv6fFQlgqXQxxYAXGmjwupjyZAmBY3Lwsz8C8JmxVwLyJiVa4q9Na7KSzDnKgvO8ARUYACB6mEt-0OMQYMcZJWd58jHryhgOrfAjvtao_E5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMX6hY4pH68b1VOQd4j4xWqsiX-OJ_LuAVQ32mODCc1MrtN3M80GHx2qf76E-QDE6TvTYJSZDxvdgEZNy0uBMPhSKgCgKIzKEjLbcrji_2RT6G8QiRBBGpPfKIraRTQ3Mp-JVZ4iJXSQTdzwW7kFqIA67OlSWR63NmBaLZjF9eIcpTrgY_3JroOIzI_EeDokE4sYDK5WLQHAx5_Vzs224XCiFudVAM_nEEmxDau12lxDZwZjbobTCyoYvGh21t4yStoYvSfgIwZlZg8R984syeS9oPiuekh6v_rNIzGe6viW57ZyR-EApuAwclKryg0oZFbpVVmq0PWdPEijkC4cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoLyl1PJOwloA1hrKgLRDyPGZ74FZ21DeMB2gMl14YRSb5_3B3gGCO71_5oDTX79Pz8O8enY9q17et_xQ9GZuwPq2m6V7XtPQ8QqL6N-rIatxt6vKhu76m2_RPOH-LpapYz-cNIdjpOsOSoYC75VtsNzQ8gPguKvPvlX3nlVF4mxqfbPrf27Jhc_iAuTrmQsQ4f49usGKsaQ3rFDYyjYLx3raq7gpXxiObLoQHK783na5U1GoRra2HauWkg8vrsHtphfOEcLzy0ImDk1b260nqX9mcxjSI_azGYMBP80rTL47zD_ahQ57CkF04ETr1MstNgBJRU08qnxXGrL2Xz31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0J92rGHqSM-3YyA_o8BtUbY8q2v-J1gRXu8hvrb0kJN9AzgR_D4usE6NbiRq--B1iulBZB_uE8t1rzHV9nFaWwzulgAyfL2B8VlsG9J9SX8vaxzfwlivipzlttUpnfUVE4S3gaQRarydlggiF_UhfaBy7X6wNERU4w_awm-iXi4TrEvHXfYqGb-HtXEaTiTjvPH1OCBB9ZE9MEhUkfjqFuLYpBnlsBBMKbSMtcBwzWG3gdboyT3AW2-9TzL2aCsbLXQppaUSJtKtnbUnXDs51Qi5m8CgQHHCprL1ujXQxVllxiNHXEfZZyuu8PVp4OE4oHteo9Ldp6AXOQieWMaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R46nZ6IwHJNTBelyMulhmcZTf-r-D48GyXysGoSgNn6d6RmNew7grkxb18TayUPjmLrzSyMs4QPBikgD5hMN0SEqCpP7ByFjjsTvrTxqG4r_8rzIp5uL9vHudcTsqtpvu20REip-WeA0eagrEfTeFI5r-xR1MYrSpha4kYEDY-eSVvCSwDAr5rZmKbnYaz3SJoNf63oe1J_Yh5c3b42e4SL_CqQJkEvWLAMKyELeiusqLMloASFGbTcA3hw-GcDahbITj8TyPZTO-r0G3sDwb23_BHVFRWrQ5K6l11j_YZGMEGNmUHlkjBwDiDlhSIfmQPB4WiipCz-B_qNDdW5h4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdTYklOT4wxix_MoJFPBSX11AoMHZtIW0i00Tv-_CdwgqrRF9PBi7BYCLJPdTrxD0AlgnNZjKf8uCapKg4A9XD0BqiFnDrsjAtwDoLV_ADGnMs1dqGTOelc8CWsLmJYDIn0XpPvFIpuyU0y-dGN7gn4NnX7F4fKzsp-5OzFbFY315aW1YBHnDhBJjxLRE-_HV6Qp3KgZEPHrPLPbAek5uoCiOl8juMFyFbGZaUtkq53pWuVYUUSUF9csP44snIi74qvjZaRqfBkw06VFHiVm1WQMvjLaSnANF7BtDkfOTqA5UX6yDroKQS046ahFS2vfvsjl8miaIwbkOmTUJeleuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTEIP74ty0RCs6jecjOSQ3260TBgAdjhSFsZN-h7LJpCttL8GvBIXcLfqMK-dw5zNwob8oC_tRGTzIdIW2sNRqSpkP8ioQidMt9vW8saGz3FFKPbTcYqe4Y3127F66jPj5IOs-tPOZx55JYdYJWxBSuKAO4Y1T-p7XHNXXXgPCh038ZEy3hl-Sfgb2c5CHoZfCI0JE01pu1kZiohlIGbYaOt8NpXNue0Hbz3HVhL07CtVby2GOd219n40yhGfVfSq06BGgHShE8V8_AmcQ0YwxbOwZDnm4476YQzBBB4i2VagUjNNg59vAgZi8TxhYpsEPY-65o9NtaYgf_IZC8jDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMLkVHzX8euwGJ_y-_udI-2-I7jON9gwOh3amhDRzVdadSgyHQftx1BHHavMoKzx0KcJOhu2HxjS7G_GXYdnHwCnFO7mCPKLAqIsiZgifFF3CacRI6G5WE3fZOKf9S0Rg_p4VCTwUmENKnBvpYtaMZOCLdjrp4igHdEL8Wk7kt4HJKk_8KCM7rlGyMpCPArHwX5BkQhix2eWM22mlLl5ucqYwgCySyKWdP_qV-1xvXbIYBpmiP_LtXoMnZAJOQxq4VJX1orK3D5PufAMH-PHvJZFinJRaDJBPQeG-_fwjmNyL_1K_XlG-UkGDB1L7tsjZm9L5qSgVLUNYsaeH-cJ_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=O652qbZeDe7mqSo0djs1KmqRcbCnUYCFrdUiuX_xHwjXveXKadBa1fYGrLh5WyJUy7mpvlQ3LYKXqb8vY0f70S3F3-PXh32v5h5u1GoG-tjvjbKjDPwNn0FsLmQdRty1nnz1d8YEbUyC7582n4suHNyDg5uKRdnmh0zzrwsMDQ6LGBsnCOWbaNk_gUIYbE4EE-cu7zJJAycCDUQC20tPfyErjOmo5Zs-NNu9le-dh6SFf84bphtAMjpSDMSrQpUeEIVXKgU-_RZ7ED-OA6HlMxRDBTwumnLIPWG08whAAi-kwPXFRWx0ehofOnz245Cbc7OsyviTgPlgqs_r0-OS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=O652qbZeDe7mqSo0djs1KmqRcbCnUYCFrdUiuX_xHwjXveXKadBa1fYGrLh5WyJUy7mpvlQ3LYKXqb8vY0f70S3F3-PXh32v5h5u1GoG-tjvjbKjDPwNn0FsLmQdRty1nnz1d8YEbUyC7582n4suHNyDg5uKRdnmh0zzrwsMDQ6LGBsnCOWbaNk_gUIYbE4EE-cu7zJJAycCDUQC20tPfyErjOmo5Zs-NNu9le-dh6SFf84bphtAMjpSDMSrQpUeEIVXKgU-_RZ7ED-OA6HlMxRDBTwumnLIPWG08whAAi-kwPXFRWx0ehofOnz245Cbc7OsyviTgPlgqs_r0-OS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=rYUbVGLSSOshq6xwKMa5USxt3dUMbP7qZhPmWXcAwzLkTxLUpjiPux0cclCvSg7GXrhVKGTYgq9Gr50WucIf0yopDV8moNpsLxb5vyngg1sQr7w1yahyDZcOUG8jQwS3hCKCsNRotLHIgpfTBK7FSIdnChjLkY6FKAVJ6IHAvsu06w1vRA9UunLo4W0mESP8MBtAaMlIfcKSyDOCQOQmZdM2qtRglDgmmNRFvnMlgc8ujFMrJKOsmngleC7I4aBeR6AKemm-hqFpvDnO6dAw0TdFG6jIHshtfknWNzCyoPaALJc8aMh1VrW-9G7obDD7as29b6ijBxQ4pU6BalOCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=rYUbVGLSSOshq6xwKMa5USxt3dUMbP7qZhPmWXcAwzLkTxLUpjiPux0cclCvSg7GXrhVKGTYgq9Gr50WucIf0yopDV8moNpsLxb5vyngg1sQr7w1yahyDZcOUG8jQwS3hCKCsNRotLHIgpfTBK7FSIdnChjLkY6FKAVJ6IHAvsu06w1vRA9UunLo4W0mESP8MBtAaMlIfcKSyDOCQOQmZdM2qtRglDgmmNRFvnMlgc8ujFMrJKOsmngleC7I4aBeR6AKemm-hqFpvDnO6dAw0TdFG6jIHshtfknWNzCyoPaALJc8aMh1VrW-9G7obDD7as29b6ijBxQ4pU6BalOCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=VUYrbyS51cKlsE5pwPmx_SNttniz_tBXL5dWzI9NOO3TKAjp8XzAzAicohe8lfBdZgLPVm5r-w0SuMhWsKh5DG9mw1_i_A3V46Jn4qi0txs6Mk_ap9kLMbW5175gnFmfzn4EYJUVqaqenFwidu5bzWUoNG1KJ6OxPwEs0hWJG-N_xzhN6C9Qw3akox7-icsv_KeqktFSe8Q8aUP558FAZAJjFSDA9dfTfGFR3yFVL3F_y7fsUT13nFJ-QmWtvyYgtqqJ6iOLuYOtBWR2shBEIKzatSw79wOTD8pm4-cXvT4TYnjIP9E9GRAYhQwepEvSiUtxQ9L1W0i2NwYhvCiQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=VUYrbyS51cKlsE5pwPmx_SNttniz_tBXL5dWzI9NOO3TKAjp8XzAzAicohe8lfBdZgLPVm5r-w0SuMhWsKh5DG9mw1_i_A3V46Jn4qi0txs6Mk_ap9kLMbW5175gnFmfzn4EYJUVqaqenFwidu5bzWUoNG1KJ6OxPwEs0hWJG-N_xzhN6C9Qw3akox7-icsv_KeqktFSe8Q8aUP558FAZAJjFSDA9dfTfGFR3yFVL3F_y7fsUT13nFJ-QmWtvyYgtqqJ6iOLuYOtBWR2shBEIKzatSw79wOTD8pm4-cXvT4TYnjIP9E9GRAYhQwepEvSiUtxQ9L1W0i2NwYhvCiQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=vvsSbds_cga1gWXwSSkHCHVjp3nDlvezMPFfsykMKBTm38FAYSX2q8SOdHXZfEVpx8WR6MnJTptLdYqlRAIvXu275fJBZdI6ht-9tCp7ypcxKIcZ4Tha3DtSVCZYyGPyHZBIylY1U4CCgvyyXuOThhlPSj0fK_jnLoX63mxec2UCoXGTE7gs-25BEdv9Xhlf9E_-to9gjAChkl-_5GGv78Ni02CGjPV4veaA9p7hpIAp53SB6PXjkODnxc7noYnyLY52BTEICACxo_WzXFOuMZGukbSj7B-HmfXt6XTJL5LFNRCrJaj8Hn16Awbk9QBVIMFBDhYmd1-C7A1qttfsfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=vvsSbds_cga1gWXwSSkHCHVjp3nDlvezMPFfsykMKBTm38FAYSX2q8SOdHXZfEVpx8WR6MnJTptLdYqlRAIvXu275fJBZdI6ht-9tCp7ypcxKIcZ4Tha3DtSVCZYyGPyHZBIylY1U4CCgvyyXuOThhlPSj0fK_jnLoX63mxec2UCoXGTE7gs-25BEdv9Xhlf9E_-to9gjAChkl-_5GGv78Ni02CGjPV4veaA9p7hpIAp53SB6PXjkODnxc7noYnyLY52BTEICACxo_WzXFOuMZGukbSj7B-HmfXt6XTJL5LFNRCrJaj8Hn16Awbk9QBVIMFBDhYmd1-C7A1qttfsfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=aD9Ed_sUIQ-RK-KXHh1coweapQmlBsIP1RK1LHMsUHLRmoUCVvc3h4Z329pUA6PppxWoD8FY0pkpLQ9AlGLP07ABam0nHQGDfpC_X1NDV6c-DmxqA54N_3bdb01_Arl9ed9sWL-IhXsPaLphuuKEhxCd1oQQN3fuVMdL_81bFyNw5Bj1E1JKNJHk2aiyNKZHvs9UPU0jkSazABtGBwvkao1odw_wjxpIMf3CvgsYr2z_83waqSq6XbY-os5J2t63Zw6mX3gPR-tI0AHtl0Vg3HMJrr7aOMmQEFRYSY9WpUodCH-LL61ICj0FwngLr_zWkRCLk3XpuLr42y5kjubohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=aD9Ed_sUIQ-RK-KXHh1coweapQmlBsIP1RK1LHMsUHLRmoUCVvc3h4Z329pUA6PppxWoD8FY0pkpLQ9AlGLP07ABam0nHQGDfpC_X1NDV6c-DmxqA54N_3bdb01_Arl9ed9sWL-IhXsPaLphuuKEhxCd1oQQN3fuVMdL_81bFyNw5Bj1E1JKNJHk2aiyNKZHvs9UPU0jkSazABtGBwvkao1odw_wjxpIMf3CvgsYr2z_83waqSq6XbY-os5J2t63Zw6mX3gPR-tI0AHtl0Vg3HMJrr7aOMmQEFRYSY9WpUodCH-LL61ICj0FwngLr_zWkRCLk3XpuLr42y5kjubohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=BuSkoMFOgDxebGK0kLXm8wHS9r5HTvhy6b9MsVBpHuCV7URw-0gCgYpy3Y7iV3eBF28l0wOVMa152zGORX2sZjPbnAt2EdAFkXr_Brgfe8NAsfCKW1yRxzepWtFzUCIjcYW_TckwghiXgAbhTxum25CJTcdSqKhqTrT0pOf9tacYfzwy3WN1cFGtwTHzQd69lm6AQx8snlwII9JdhLty3dtehLHjr6KW9ViTgz8SxoRgSLUQSOJtBuYhU9wTzqEV8OrJ_BLLWYj_s75OtdO-jR138FULkEGUGnSk4ouRNvH9I7a7F3IrdJFMsLoAnzqxau2D6rr3Nz_GEVZNvlRX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=BuSkoMFOgDxebGK0kLXm8wHS9r5HTvhy6b9MsVBpHuCV7URw-0gCgYpy3Y7iV3eBF28l0wOVMa152zGORX2sZjPbnAt2EdAFkXr_Brgfe8NAsfCKW1yRxzepWtFzUCIjcYW_TckwghiXgAbhTxum25CJTcdSqKhqTrT0pOf9tacYfzwy3WN1cFGtwTHzQd69lm6AQx8snlwII9JdhLty3dtehLHjr6KW9ViTgz8SxoRgSLUQSOJtBuYhU9wTzqEV8OrJ_BLLWYj_s75OtdO-jR138FULkEGUGnSk4ouRNvH9I7a7F3IrdJFMsLoAnzqxau2D6rr3Nz_GEVZNvlRX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
