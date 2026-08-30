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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqvy-PGp_3T0ng4Ysbljglx-XuBh55zHziuSUGYSLmUclugNZz0idfXEIHbhzSns7RyhJTIYbXgVpqh0hCHX8-7tiqGRkeH-Q1FUDszFp9ZE2W0E2PIa7PqSL1GgtHaCEkFy8cFdz5tQfuL8cPPkCWD7FXgPG9jn_y9HhjwdFaguEa-95Ap4UF6hhKrCkaaA9fNIZJhZDRDkQXNDZ5Uk7sh8dVM9oEY9h-5AR11QtWDw1q4BST8ILPyMCeP3fRLQrOLRfZH3UrSHixaQ6O3zpp3k3FWJUKqXRLDA4B6BofqnkT7dKwP9XmfUoyW_YX4dFdqMhby7w0Y0cjI9WEyFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY5nFjIGwk0H5z8yYdx6FYEKTr1VuCx3amOE066Ra8w5QBHHZvNbQKCnpGKIy8qiBHsEYpZq_G6gK0xy1ZFkUCjJScdwEOlF7ljEHaZsbGCcv-Atsb3QrZDLkjDihXURD4TCDTjOuhwzDo2RreEjmwUWUm8r9tSxlHlmIlUfon3nXoM-W74IJT0H13etPY_-3nn3A1gnJUIKjxoERWgWmLrQpG1H0rXvUhH1aDJRgx2hQbPO9_iR-ytrUrmTx1NDM9Z3f0H1MarUPH-Fbb3IwCENjW7krsdSj0uNCTtavViO2Drx50I45geuT23i5IJL3vKDfKx0S3TQRFiVv6YLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMxyf9YurJ6f4tvYTCEimgCeREawnR_1El8SbJ6lZox9rAFjOZSWwYh2Z8Z5EZ0DR1j_bd4whLz-xLtRc2fbw8zs4YXJFy5pX_eho6PjMzP76ToQkMRN_GNKr7s044QhOjkWO1caaQ1mSkWSoLf6AeVxrP_CZfu78P0T14szFxSF0k96-qvA3OVnKWBTupcPet3hu3ix_gvxYD96Ve3xzZtDehz_8UxqzL0bcfEq7ss-wkIgFTgbYHzMF30fDzkjn4AQYOMfRljgCLMdx9vU4llhYwwC5S9xhTXZrpoVIfS3xBln3KO2vNz-2UuFKOWJa9caNpZdGo8u_xQsj4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqHft56kVzqcBvVktxflgsppdUAXn16bTm07CaSPcnY7Ucz_hqnEVpPC9LgIBThjiE6NgSzc4KRrvAok06BxdAhqq6cSz9n-RR-9oR6f7l2PzXXlxQnqhEkGU7IRiapMzqjlfFiN5POAZFbKeLZzi_fuZlHVtJNY0F5cIzByCUKHxKCb_jo0uYWixMY4lfnxqe9PON2IdB09ixm0fWJPxxVcjltW0CA7Trd7SMGmKnvZtxr5wCYyldybcxui-QjiuYNSo7gcfQ1vIH4U8oZNYEs-3Hf80Fn-FvG9OCIomWck2OtXrcZFswy5OF9z9NoVNJt7aw8EbI4k2ro8AuobPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stL33D372NHb7IB-Ybq_2300QymPj6TTyMecz4EPqxWxgDxFg2ofh5XH1wo56feP4CiRidYLwy1KGp8F90idbrZtwciY2L08HeaJdn2cHSansyrMWy3U8kiOD37fzJBINi7rji63FgjVVK2JifWe_9M-YjXd8MHI47sZZ7uDcoLsLNSTtgMwo67qwvHqto9LDpGlzai_zhSr2na9DVnxKh_6AuGeiaQ1NmyEEhsbBRqSgW6pcwLVp6krJTyehK-agJV20sJOulZUxsPrh8gY4ZK1OILZIhauWYZqMwgsE9uOBSXP8CbVTULCwzhnMHA723j5Xk5DaUzTzawlA02lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgInJrahE8QEumhODZyXfOi04sEc2LyioPStjinLyWarEYprHp5_-CP87oHEJTh9NlBAi-ZMTXptkyIDHn34Ws7gsZW02JFTc-qfhnm42GXBdcfjEYg5r27NA8z983n2vwCQclO5fKfG2Cblz92TXURkqYXYNtIEChdeJGdYu2q-ubxzgVG_uX4xANLsFs6yQfFXhTWHA6Nd7Z5tlS1KelyTbFEBsm4b58GRdl57Tm2I5MH7H9Pztf7wfBc3I5Wv8TmRnwyHddvBPIRoB6mFvGc6-L6qGFT1slSWeboPMMGAgxl6wQAf2J1DdLGTxjqFz2ZvW3T-pQFGvQMW5s9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qfRKgAWkPCuj4Z5wUqJlZjTtcVpA322v_t1ohVTmjw3RaIu74Qkwx_0lMi4gJG_of_lW4cckA2I15ZR5gqAURDoqxrpEtAu9wkecevk4l2DLtqCr7Fn54CeDv9fcJoykrrGdRvUg_WMhKG38_XrBcMnBYA8PucahYaXOmRiICHLscF30TpmDigWPiXpECFytKnP4z7tbetJtKopZ3v8UqCGDhHuZuHfz3njlnM_YvmItOuW5kO6OARFCMSMMJDfiZsXaShljcdjMw9gd7pVaJJApnNvvs8VEtgIw03zQGkzRRv17WiLmKKMxf3gh4Wh-ecJDzW5_xKpFnsSLWHqOuwcj-qkmde14uMRs44EPJZkLf6Zg9FT63d57f50HJSdCNVkYLUtvugHVxFf0r9c5fU1L8zyUuOAIiQGIiXenff-BRislu8eLZNStFqiExMU4CVg66mCLXCsjrJlB2FfnrOKuwuP_igu2L7jbWSt-Nyemkd2ffIRpiYj4TCX28XVg1Ju2tsZVBu9_PkSMYVVsNjC4H6hUm6K9tLabpQx2pvH6CIPNE2sdtPqAT1X7JAA37wgket1QHRbVrilyGG4YjVPKQMyiiCc3v4dNOox7R8qzJmk1JEq2h_U8CbaJXxcKwMCaR2fyq0qagPSA69rerxcBy-RH-1IwkMWW5MrwZ88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qfRKgAWkPCuj4Z5wUqJlZjTtcVpA322v_t1ohVTmjw3RaIu74Qkwx_0lMi4gJG_of_lW4cckA2I15ZR5gqAURDoqxrpEtAu9wkecevk4l2DLtqCr7Fn54CeDv9fcJoykrrGdRvUg_WMhKG38_XrBcMnBYA8PucahYaXOmRiICHLscF30TpmDigWPiXpECFytKnP4z7tbetJtKopZ3v8UqCGDhHuZuHfz3njlnM_YvmItOuW5kO6OARFCMSMMJDfiZsXaShljcdjMw9gd7pVaJJApnNvvs8VEtgIw03zQGkzRRv17WiLmKKMxf3gh4Wh-ecJDzW5_xKpFnsSLWHqOuwcj-qkmde14uMRs44EPJZkLf6Zg9FT63d57f50HJSdCNVkYLUtvugHVxFf0r9c5fU1L8zyUuOAIiQGIiXenff-BRislu8eLZNStFqiExMU4CVg66mCLXCsjrJlB2FfnrOKuwuP_igu2L7jbWSt-Nyemkd2ffIRpiYj4TCX28XVg1Ju2tsZVBu9_PkSMYVVsNjC4H6hUm6K9tLabpQx2pvH6CIPNE2sdtPqAT1X7JAA37wgket1QHRbVrilyGG4YjVPKQMyiiCc3v4dNOox7R8qzJmk1JEq2h_U8CbaJXxcKwMCaR2fyq0qagPSA69rerxcBy-RH-1IwkMWW5MrwZ88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF_2d8aP-UR8dC_nZNEti4shf53VbecMSPmrAwcazkzUdckrW5IOnjT2hy600UPsPurwAiXnZ_lDlF58-pR8YTrOcFV9rQucivplTwk0hW1jg9dB7-wUcBf-oIEJtB13Ln8vVd7YgyZvh8IhwfZQpP0V6Sa_1UB0AAY5Te7O867IJEEbuv0KxFQQMFgHspJSnj8K5XZCeqPT1HpQ3bsWDqhV9P72erGSliYQsiInNFoeffPTomRF32c5668PGMpRj5kPI8_gDOlbBvLQ8BhZp3dlNcV5cfFXH44i6AB8NC3EKrbKZiGk-ewic2j621w6XMupbBqKAq19Foog_WAXoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBfJCtpgoRE9jmYH3AeeMNUEsXm2eLTP0HmzmhHuB53TZZB_46dbEkkLTPC0KX5tnN7qLaGiZ9mNFUXxN9_fRcDtkV4jhKOs9S97O4ZGqf1k_i0Uh0cKPbHe2H39-jUmyRmrOMv5iQ-FcXva48DAunom1mOvHO7j1mOEPtxuFVWGgdj8U18z0evebiLVq1D-H-kmHA7eHoaUvRZz_q72Hnk6oogT4CYsZoplBVQpvpLpbtbCOdUmOg75R4Kp_NQthImVQShE3fS7Cu_GEFgQ7qIQEbDZjxVnDc2dLLfpLYCxwcJPEk-IMOWWCM4wVJgk7IiD02TfkWmYPsShMiJ1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIpUUf8LqDxJQyPY76cSm2QwQpdA5nX9s84O3gkJqputm9bc0gakaozxLadRbvDJo0iCPCzM0HZEdH4A886cQrCgzI9Js8AsN-W7c4-_LZRpH4pgMM3dYpTOiGiiVywu3aCPhLBJLyCRg3KBsv2t_MIZyO4N0s5MGcCoV6yCVow-0pqHTbQOYemyZFWQXO_z48j1VpLPOkmGB-QAcXyJt4aXE18NEQw5Imt1_-i5zGBrCd8nFxk2berlwjH6kN6UAfJVFq2kfuIb_VJG2LSoeEobUE5AP7_cu_W3P9y0f5woQ6h3zGXag9tZvwAsc4qatROHLsPLPDyIl0XSUA3HUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWCpdNM2_VlnjXoFVh95o-DVexUWyFjewyr9IC40ehb2P-cO-jAkQukrPvjrms4U_AwcfFRsSVetqUEMaKYXpVD5HpLUBnc6RBPpAaQFdS0neIUmr8R6XYJbxd2bsiNXV2pEABW3BwrY6YjYfYe0O5dOcWu27D6GX8ZlClusxuujInPAlhao_qZqmlm9Ch2xjuym8VVUe-yuPTcZXo5sl-fl_tI2Z5RadroZUklfv9YJTxomMWASqn05SFBdF9Mp_Js-SNvZZn133Yb0nicwIy1orfaPgdm2tgWrAo0OD6X60B5p0Q9fRVp7Agd3FxP2PikRo7o6JY0sSmy42wlBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr03s7Da3qxhE86l05YQNi87srC-_olUlNTvtb_SUSLhVXgdaHxYnv19jdwM6ShqehYxJJz4YB-hfHvyRhUUReRiPZPCji-oct1xigtJzmfo-zdhlb5q1wmMzZaTsYqV2xKFK5y1hkfieYF3HlG2F82iIp9scRg-_UX4R641b7geVcem6p6hlg4XvDkt8zTPw2CTnlJtLl9_3Yt4a7ABHozW7TPVcxdPqfsgntRUXP9U3c2uOsbvsZ0juI1EUENMnsQo5Sd_KAyNPFuHJZEY2qtqFJdsxoF9dFIH65slybe19sZrg5EAJxJdSKcanHMgV8fyNzDh46agfCnuMBS3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5g9OAPYcmJcbSNn3ibdR_F1BQ5lMCTd6jkwUtIljFvY48yo75X1nXUcfaVyMrfUVkxXTzLUSLt9PqXVkmjPnt7vc2dIui8G5b_bjJDzDXASWXHfxV05nX7NkH_Z-N5BLwq9cRVCxEiVEJBpXQwAGutVMmwgP6EyMakTRol0I60Oxf5GVnX5sZUepxaQjwvFK9WBU36nEz8XOb9e-MbumM0wLW1lC103fqeZtQ9P48VqJU7lZrwVh8oshCIGr6zcqP5xyvDpi3ZcarBjiS61RuenOdWU9AZqslhAphaW5vMJZhhFsnG3Uzb4-9Jj7bgNfyO_uwkoGyzXxJEwbWLufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMKYeRgtpzzSrvw6Rg-dl-3oDc9Tt2CyWrPvhyKLe1QU8nositf-7FiX_4FLT_CG1uN2jgE9vgpjeeTxhaDFfpFv0_gbFZ8HD6UbqFoKBU2iE3iEF2I39D16psUGPf2r1j2L6QLBGbBlPPdfD97YVy6YbCKVGZiQT3jbg93KsZNkEOohvScyRlGaxYEnNNlpKYAeVUS7E8_SZViNtXsrCKFeaVtRFSozYC_5ZajbaTjgBBVmj_vWRRgYbR9g21cf0T80IWaWRGIKE-QY3DEGUySYE3bc_Qu9eKkAJw5MmV9cctPJ241Ylx6VyLxW8P26KJMICGONFyD8dNhgcoChRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX7DGaykRbc6V0sZh8KvcNdJP3zRtWhijAs936U0oUjKN0gdPERdy0Mi9Zoh5GdUXA51I-_QukL73RWYvjstdcY2GmLXo-ugeXyp0wfjW4X4-EGigDT5_83PXt5y6YC8Of4cFvIuPi6Bg6tOoZFTh_NiiiK8e4w30qmsRz7D51EQPGrqN4FbNckT1hWlSeyy_t1ZRvKPL9z-_FnRevsQwf3nSBDb0mWts8h0VObo2N8Sa5En2UlaDpeIrLkD3x1xzp2Ir6prktMlKnqV-MNJlE1h25QSukzCqrNi72xIJxyafS7IXD3FpmtYPUs8QlaP_ILSefZ5emRW2VW9wyiujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6a8V4O8dBGyjMvdoLpN1NmyhGtotVw_IvV97SZpjEjkfJOBAmmIhgBt2Sss8580LNBg1wzGIVlwKT_zDDNdvQoE5vSmlHeNsfFNJkJWg1LQ7dGxEQAkBKzted2CHnLMMxdx_mDugXdurPE2ehIBHN2GVQh_0SZ2EJLwkdFFImAr310s89RDpivVs-0DymN4M2pXBr8VUM5iiARfq2gyVc8V-sYO3_WG1GVuYZXoDgeJeZU2vLbx3eb1QT8Dzt83zLcEgZcRTXgDWWmXYjmSZZA04-2DjCFB9WZ0lk9czXNPOEGJSM14tVIkR_5g1DbyI-wD7caNqZCVxZtl1IWDiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpukmP5rwf4WIupyDRQ_638fwlnWzcp7eru6_yNw_xmfmiPp-78GWu97Qp4J6p_RFH-9j1724WpLDq_0ERLJ1taFBEAckcbt5h5HTSXoJhBQ9lCFdWZvCBisA-_HwFSftPmkvIYwKr3yD2VPZyRPOTxMbp5g7gOcSXtAxUgvFZdkuDyz1n1m2AskWWn0SKLNqG-4WTpq-KnzY-7Sz4R0M6vZuy3WIUXoT4qlBFQvQDUiZVe-rm1lxrp6i3C9f2xMtRL0JyWqxJ_fTT8eyKl0zqqzglkTmhy-LZ7u7mzNF130Q_w7mLxry5v89N8jfBzCTHqCkUJdPrI_G2bMXzpBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PP1dmH2TyC9Gqu_sd35PgLpNsUf6Q7-oyc4lLqXXT9pabBsxDg13rEnRnV9f4vLEqa8NnwCQqbCDo-ZQ06r4XP2rCPHVzm4s-Mxjh8Zw0lR03Tie9mjLVsEh-8jE39VPS-S7VLeQHh3-1VtSCqb_wL8IDc56JX2AVyji0Ks4HJ_qqGtpGePkeLD1Uv7SWLMBkrmmRJYpqFUe0e6pl3mkq4IkaRk7RxFWTMmYi1Z50XizULEApWxi91C4HjlMlL8OrjZ_eLQbetNVm1oqU1sH8oZ2g-M0kY-s7Jivotmmcvv9LL-MCN-UNpFFv0NcuOUhFp1pDSMklFgWJl7TNR1zTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMnO-7HV6Hdp7qZ91mNbY82pX1J_eQNN5p0wKD1QGmX28sD5RRUQDavOYyCNlIThEocooo5V6qSVcuc5hLCLRcp04T9nfIL6WVvZOtib8XEQBtk0_EahIGGFVRvVlEY1UY1fxV1sp6MOD2giuAPmrqV7ydVip8QVkVHZuP980RLk5bKIdf7kEsdJqco_GwklrTnF4Ffk6QAHncO9G9Y4Ej9i2osDiHPXxq0o5GyD7gcEULWazYMCXmXCNNFQSQA7lMPt7aUr1xIxrKcVg2W98iwZZQBQPk2K5jL89feJNjN5bzdSAhwSTdqCVAjNdyp0iXTE-HHN7mM54O3lfxZUbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVrei5i5yOJKZw2Lx5hqX1m4lKIeYiEPWSd_2BI_auTfMmU_O_OJfGUpENSD-dy-hkWROPRJiZ8NrDyvE6AABm9G76vRAJOO6qfvZVFSppVo9a2zk5aH8rh38Pr6cLXRwkCdACxklYRViumOR9NZtK3JFUoEc_loktwO5cI87yly3Ro-6BmUAzzaODbCS-qTqoV7xko0O42iOz0pIXN5Sd2RBzf1jfZsEBKZJD2SkbOKIobaMWYzCGM4Sxz5P1TxHny52DoHgU5eBzSidT0juBULKfWPtVHns01BqAwRO7pRyqahry4rarI3dirlbs4IGroT43R-LNMnOOwgLkZI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSRxDS98xVLtm3kS8FUUITKnYAyULOFJksVjiPEnQvGwVhq8t3pcAFp4IuhdikWTc1urDXx6jSl9sKLmAa2NzYcJE1uNc1ziHRyYotac98-GwUcAX5EBruRQxb2djL3phDqHMPWdnr908z3-SrBzPUFfjSc5T3iO9K9qmDbGMY1yPlCO2-hHmrcR4OEY2dLxxrslZjxr1U7RFcAwkPXGYp0xBqmXPm1B5WWRQbll2PkndnqcgMiFIZrXTOzsMhmwl0dIwF7nCwOryI-LAR6TfOTcRCeteNqe8BKHP8wxMqBKWuK-GJgbr4C7Su7rbUbvMRETd7I9YtJi1pHi6nuccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYUAMH3IAhIgyLGblJZS7rXsGq2d1PEchBS8XPTRPJnjRNiF5V6hIQmVRumIaeuXM5uaQE-zH37YsOJ056d2iE3Y1L1OO3IdxUW8njmaO9Hpuz0hw9fR3SdTdeoDlihKafHJfYt05m8HcCQEZVGAgN0egndoH407jyWdPEpQHsoPsgtEep3FNFR1byZSew5t_vPgSEUE7HNnZe_DDl6lLt3mBMgFA0FkmT9iSr1OLBdMgo3hai5nH-u8eYzYrq1i6enH9lZqf2NWSNosXiRvxd7YPFo7ttHvbSbHhCpTfnbx7wmumF5_T4cGaQKNHC6oylTzIRgzNEeaWHAkrZlJXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayh-i01qvk1-scpCy4TEU7oaoBx3cDKbflU0eFRooiw_-JuIKRxUJkpphPM-VvWP5NBCD4J7GO1imWIw6VrPu0WShLaGwqZM25n56pQgUAR3l3n3vhizV662z07a9LEpNQMmjbLRsR2LYMjbFfDpcGLmz9t3RHVZDLa6fXN5vrkK0iEKQaqVEbGLUjjprsg3L4aU6D6dMq8jolg_0pAXdsMNYXHaiAjVke_PhBUCRUfM8qE51Hrj0efIBTn2WPPOsGPugOK0Xn3fY17D76ETIGCZamopc_a6NX5YfMe1Fwttixt4qeLiDIYtcplrd_W2KmnkCCFzYqZ-Cr8s1qSQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH5Ua2uWTaImAZU-XS3CSOP9tRfOBWduJPVrpN0IXcrdW8xsDmmXeBtwufQlOeVNMVk3UHGCea4LNZvxo-qN1sgXlOWFd1HPpEdIDMbSf77OZdzSjY9dIx2nJXdjrPrEWtgDwCqp65RREdl8NdjQctI2o6SbPzUPpdbMjTN0f_qpYvGkTJFUC3nW7_K-SBXGZNLifDkQmOEEjP1MXc8zQvG8RT136gy5SpV2hivPUiZNmtI8bMRndT8nTz-aQWvzrlzCT9VjpmjFRbbcEYz6eY-IGBLeCEtysh9oHKghNs3Bz8eJwT5jrq1YkXVRRptQG8tHLEeMJZwne5kg0xDmlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8lp15Z_1ReFN9YYvqRPqL9mzJM0fsjacLT7JEXGgRo_tmTY2Cp_Uo4xGz4LzqU8IV91n0Sq_kTpt6lOE5scRJozHuj7kThYUK4_FH3PRG8avXEDeOA4Qpschm6roNeHoRf_kqjZDAo_BzvKH5ykDsXfcub6wSpBrF8IKtCkeap-91RKJUP_HNFW4uJBZNxpqfSaU7yZYZKL1tvLcV9B1EcKe7EbwQJCHpz7krTmJRqnixuAvoCVFc1-I_eec_xzS6YUU0aUnCEs-JkmATw3fUCDdzmG-PEvMdG7sY2uQ3sUjF9XwX6ULpunwdonkQLCuiLHuiowDjPXtfDRYB9pOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2ZRJ1oP4xzvT25AFdWVu3gG8tlUsndJWDC5IxhPleKU86vNdScJPJ87ieqiowsIGE3-OJ3QzqxprZslGi5faanigBeQQa3tNZ3UMrgnzYvzQp-SnnBi1lZG5t-33peYqCFJmA42YOoSbKDDwjfpj2LCvA22zkXYpTeuzJO7UO3X7Hz-jcHcKuoVIeFNynkFhZEMkISrEQacaCuUBdaQwWPxcP48wdxTOf_0u49Zsc2ZTCFB5iA9-2qwo32xBGmvX6HgygTzKz_wcilH2C1e3OIjGzLlxRz1Fu083MSEC0kB7p0HBB-GSppTEDPRJFdEXgdw7CLQUI2z1nvNkmOU7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI2Hwgnh0uJdFvT_Xk1Qe_ulqzwZa2q5RUL3aFWNpHaxwKGNpFedd0_vjMechLEs2nA_1K_WQjKUbQFGrdNvPWTcK3cxf0j2TqOo5zhxexYKftWFm5mafsYGXk91nQ7-wmcb_yUJeHeTYAv72Hv2IvKas2tvD_6i-mgCsydgpXUHg4NlWCAjihK6NPwIS54eIvqCwx9dY7GiUQaLCg2K6I1yZdiGf6ytkWtT_dNyoj0Q0QyMAFvlVhFQM2BDYJRlOWZ6wYsPR5Q0WC8YCwP6BKMxmrzrVNzlHSi8JNvXUBqN82mwRiJm-r__nLgOn2hb5aOZw9WdERYFLaurwutUMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=OD167dJc-r6hyK_1Yx0c1x47687vVExAMkQK-DNiJgIoRE_9CEbCiyZQQpTo6L1rENRFnhqBgmTlY25ktXwJNeqoFsATGvoSc977auiHA4WhmGW75PvNQni688GVFYmxbtDNk8sObqjaXYFStBcYK2ndbqJ5I4Ibj3B91RRx2mz4s-k900NPors3lnafjzB7Asp448JuJl43bJ0C0acz32MXzD3voLG_VMvmDbkVSi3_FSvZRGQhafJpFGRPONL0XIAzb1wRzQkZnUuShimkaXY5kX5DBq_bEScheoFRu7WSYJKZNAbu1rHE5bVhJYj9asBaDNzDf20oO-24Zy7Mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=OD167dJc-r6hyK_1Yx0c1x47687vVExAMkQK-DNiJgIoRE_9CEbCiyZQQpTo6L1rENRFnhqBgmTlY25ktXwJNeqoFsATGvoSc977auiHA4WhmGW75PvNQni688GVFYmxbtDNk8sObqjaXYFStBcYK2ndbqJ5I4Ibj3B91RRx2mz4s-k900NPors3lnafjzB7Asp448JuJl43bJ0C0acz32MXzD3voLG_VMvmDbkVSi3_FSvZRGQhafJpFGRPONL0XIAzb1wRzQkZnUuShimkaXY5kX5DBq_bEScheoFRu7WSYJKZNAbu1rHE5bVhJYj9asBaDNzDf20oO-24Zy7Mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=pUERd2UwPGk0N0B7cVBplTay-kDNw2PqrKNFuwdYEl9HCCjdIszMXoCzjlSFIQUYRnl5j4ThZXZ9-Sg3Ha9E3WMhn-KmvJ87GhmwzRQFiki8ulFEXum-andkDlKZeh8_VuCoZ8LUaCHpBl2RnS-J5N8UZaNQ9zLX6Q36yWrUYr3cFj9HgBJLUc-yAOBkff9ohqormkjCDT6aXNDHOzpPfowf-2QTup17TNLM9UnBFEjfT4AGxugm2-sMzT74Js2j-HSOTDsiQoNZFbGSmmczK0MUOYUtsThxIuH9FE0HybChdbqjD1svZpVHXcz7eCejhTpejJVDEVrBgFzSq4h5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=pUERd2UwPGk0N0B7cVBplTay-kDNw2PqrKNFuwdYEl9HCCjdIszMXoCzjlSFIQUYRnl5j4ThZXZ9-Sg3Ha9E3WMhn-KmvJ87GhmwzRQFiki8ulFEXum-andkDlKZeh8_VuCoZ8LUaCHpBl2RnS-J5N8UZaNQ9zLX6Q36yWrUYr3cFj9HgBJLUc-yAOBkff9ohqormkjCDT6aXNDHOzpPfowf-2QTup17TNLM9UnBFEjfT4AGxugm2-sMzT74Js2j-HSOTDsiQoNZFbGSmmczK0MUOYUtsThxIuH9FE0HybChdbqjD1svZpVHXcz7eCejhTpejJVDEVrBgFzSq4h5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXNzI1HjPLEF2LzIuAzZ8cAn-J_nh1rvrYuehlj5V3xLlx_1PxoC2PzWDW1tvM-8Ec3SbBP9xcAMGgQncwf9P1pZEp83rCmc959xZ2C4uTUrZCT_l9M3nUUaChZZCl_zwUNr4iw7R_uWRklHnmpOcS7fbgMzwx3YMYBA4qRakK5eZDaIg4PgK5eRyN7-BQiBNKFx1crSi93Iur_mxsTWoYxs5DR4zvH2QpoArlFxIB5L8LebWuorYx0ZUfa1KKemTmSzb1HGigDRUvejweRerpjEh_qR2v0tojSuJLs03dOUSTg75w6ldzAJXwK4p88BTMx3AcqSnN3_tteCuxZfpA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=tIZDmKvKK0YIJIcSIMxGfKUxCMuxCY3B0ghvR2KuYr8HkgQUUUMpaaAfl943DGiz09K--UBFPCfSI6wC2XRCRQElI5k1dhP-EcBEEr-5FK3S_wvmbWcv_mm6j_P-SqD2Xoqj5KchwLA9YKzZvmx4i6MfH9FGbf_ARlL5Eh_LdCeU6Qmr-ig_CvZo9-_TBfcEbycdaDR11yaAqljQ6heBHPzb8XduaiXewN-iE4jKlRfynOXlC_03uSnLy7botK-_58opcerFsTMl8Jpvq4cP891pFegaQ9vqd4VcM8T072OA6_0ee5ulcmi59fVz-mvxCAUNxTqGRwXVPJm3bVT38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=tIZDmKvKK0YIJIcSIMxGfKUxCMuxCY3B0ghvR2KuYr8HkgQUUUMpaaAfl943DGiz09K--UBFPCfSI6wC2XRCRQElI5k1dhP-EcBEEr-5FK3S_wvmbWcv_mm6j_P-SqD2Xoqj5KchwLA9YKzZvmx4i6MfH9FGbf_ARlL5Eh_LdCeU6Qmr-ig_CvZo9-_TBfcEbycdaDR11yaAqljQ6heBHPzb8XduaiXewN-iE4jKlRfynOXlC_03uSnLy7botK-_58opcerFsTMl8Jpvq4cP891pFegaQ9vqd4VcM8T072OA6_0ee5ulcmi59fVz-mvxCAUNxTqGRwXVPJm3bVT38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
