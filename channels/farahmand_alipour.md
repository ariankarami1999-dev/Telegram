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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqvy-PGp_3T0ng4Ysbljglx-XuBh55zHziuSUGYSLmUclugNZz0idfXEIHbhzSns7RyhJTIYbXgVpqh0hCHX8-7tiqGRkeH-Q1FUDszFp9ZE2W0E2PIa7PqSL1GgtHaCEkFy8cFdz5tQfuL8cPPkCWD7FXgPG9jn_y9HhjwdFaguEa-95Ap4UF6hhKrCkaaA9fNIZJhZDRDkQXNDZ5Uk7sh8dVM9oEY9h-5AR11QtWDw1q4BST8ILPyMCeP3fRLQrOLRfZH3UrSHixaQ6O3zpp3k3FWJUKqXRLDA4B6BofqnkT7dKwP9XmfUoyW_YX4dFdqMhby7w0Y0cjI9WEyFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY5nFjIGwk0H5z8yYdx6FYEKTr1VuCx3amOE066Ra8w5QBHHZvNbQKCnpGKIy8qiBHsEYpZq_G6gK0xy1ZFkUCjJScdwEOlF7ljEHaZsbGCcv-Atsb3QrZDLkjDihXURD4TCDTjOuhwzDo2RreEjmwUWUm8r9tSxlHlmIlUfon3nXoM-W74IJT0H13etPY_-3nn3A1gnJUIKjxoERWgWmLrQpG1H0rXvUhH1aDJRgx2hQbPO9_iR-ytrUrmTx1NDM9Z3f0H1MarUPH-Fbb3IwCENjW7krsdSj0uNCTtavViO2Drx50I45geuT23i5IJL3vKDfKx0S3TQRFiVv6YLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMxyf9YurJ6f4tvYTCEimgCeREawnR_1El8SbJ6lZox9rAFjOZSWwYh2Z8Z5EZ0DR1j_bd4whLz-xLtRc2fbw8zs4YXJFy5pX_eho6PjMzP76ToQkMRN_GNKr7s044QhOjkWO1caaQ1mSkWSoLf6AeVxrP_CZfu78P0T14szFxSF0k96-qvA3OVnKWBTupcPet3hu3ix_gvxYD96Ve3xzZtDehz_8UxqzL0bcfEq7ss-wkIgFTgbYHzMF30fDzkjn4AQYOMfRljgCLMdx9vU4llhYwwC5S9xhTXZrpoVIfS3xBln3KO2vNz-2UuFKOWJa9caNpZdGo8u_xQsj4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqHft56kVzqcBvVktxflgsppdUAXn16bTm07CaSPcnY7Ucz_hqnEVpPC9LgIBThjiE6NgSzc4KRrvAok06BxdAhqq6cSz9n-RR-9oR6f7l2PzXXlxQnqhEkGU7IRiapMzqjlfFiN5POAZFbKeLZzi_fuZlHVtJNY0F5cIzByCUKHxKCb_jo0uYWixMY4lfnxqe9PON2IdB09ixm0fWJPxxVcjltW0CA7Trd7SMGmKnvZtxr5wCYyldybcxui-QjiuYNSo7gcfQ1vIH4U8oZNYEs-3Hf80Fn-FvG9OCIomWck2OtXrcZFswy5OF9z9NoVNJt7aw8EbI4k2ro8AuobPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stL33D372NHb7IB-Ybq_2300QymPj6TTyMecz4EPqxWxgDxFg2ofh5XH1wo56feP4CiRidYLwy1KGp8F90idbrZtwciY2L08HeaJdn2cHSansyrMWy3U8kiOD37fzJBINi7rji63FgjVVK2JifWe_9M-YjXd8MHI47sZZ7uDcoLsLNSTtgMwo67qwvHqto9LDpGlzai_zhSr2na9DVnxKh_6AuGeiaQ1NmyEEhsbBRqSgW6pcwLVp6krJTyehK-agJV20sJOulZUxsPrh8gY4ZK1OILZIhauWYZqMwgsE9uOBSXP8CbVTULCwzhnMHA723j5Xk5DaUzTzawlA02lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgInJrahE8QEumhODZyXfOi04sEc2LyioPStjinLyWarEYprHp5_-CP87oHEJTh9NlBAi-ZMTXptkyIDHn34Ws7gsZW02JFTc-qfhnm42GXBdcfjEYg5r27NA8z983n2vwCQclO5fKfG2Cblz92TXURkqYXYNtIEChdeJGdYu2q-ubxzgVG_uX4xANLsFs6yQfFXhTWHA6Nd7Z5tlS1KelyTbFEBsm4b58GRdl57Tm2I5MH7H9Pztf7wfBc3I5Wv8TmRnwyHddvBPIRoB6mFvGc6-L6qGFT1slSWeboPMMGAgxl6wQAf2J1DdLGTxjqFz2ZvW3T-pQFGvQMW5s9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=f88PtO-nJ_Z15CagUhw0r3HXT0tSXpstnCc4UqXZHhfIGZFIecVL6BXwKxQSnbgkClZEDUOZAbR1UdVcChPx1_PuHlnvDdOLF59w3ut6rf27agrYe_Zee_5VQORk9LYrIHGzfu9a_rrKnSBeGIzMLfImj_MZ99Za0Y4XxwPB0IXH-IHThnvP1P2QH0NYGMwitSL0_s3TrAPCBCvYwDaEbGKAf6_jkEEjcPSC36uKC4NlMDKKtrqX5UuA02f7ft5Zb5KR6PdEVYjv80iAogid--oPfRN6oABgWIWs6IiTeqaj5gXbn7DlraECxkRe1Kp_D21naH2xC3JO3w1Ldhl8Fzl4_Pq46MkW8oIzx3zS8ITUC-IYoqJ_kIcrBE197CIB-M2AVfaF2Wb3JPb2Pd_mmITyeTgPiCR-EhHu1a9NBte-rmluAjHwHHc8oKciEQ2D8ohJbn2y5j_pD9_iAltp50SaBvaqx3elqsZqq-4MRxjstxy2n0G3cWb9b8pLD-8TtObNeErXgoOCWWIzXe_W5FA2B7i9MngMEgUWHKMBLkYABWE0kuxZAqhItdnUKBp8oj8fhOIwBB_-OJIDawVy2sFN-KcCSP6_rvQVOzM1mV3ZQJTZCXphsOiBEKjMXFa8MArJAXseV-XGIJZIDNxkYa9E45idZyZvwE68_OodRPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=f88PtO-nJ_Z15CagUhw0r3HXT0tSXpstnCc4UqXZHhfIGZFIecVL6BXwKxQSnbgkClZEDUOZAbR1UdVcChPx1_PuHlnvDdOLF59w3ut6rf27agrYe_Zee_5VQORk9LYrIHGzfu9a_rrKnSBeGIzMLfImj_MZ99Za0Y4XxwPB0IXH-IHThnvP1P2QH0NYGMwitSL0_s3TrAPCBCvYwDaEbGKAf6_jkEEjcPSC36uKC4NlMDKKtrqX5UuA02f7ft5Zb5KR6PdEVYjv80iAogid--oPfRN6oABgWIWs6IiTeqaj5gXbn7DlraECxkRe1Kp_D21naH2xC3JO3w1Ldhl8Fzl4_Pq46MkW8oIzx3zS8ITUC-IYoqJ_kIcrBE197CIB-M2AVfaF2Wb3JPb2Pd_mmITyeTgPiCR-EhHu1a9NBte-rmluAjHwHHc8oKciEQ2D8ohJbn2y5j_pD9_iAltp50SaBvaqx3elqsZqq-4MRxjstxy2n0G3cWb9b8pLD-8TtObNeErXgoOCWWIzXe_W5FA2B7i9MngMEgUWHKMBLkYABWE0kuxZAqhItdnUKBp8oj8fhOIwBB_-OJIDawVy2sFN-KcCSP6_rvQVOzM1mV3ZQJTZCXphsOiBEKjMXFa8MArJAXseV-XGIJZIDNxkYa9E45idZyZvwE68_OodRPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNGLZr1W5Irv9-feCJbcMK9iLPwP0wJGI_J35GBlGboh4AH7WjjyPd1yDjSdsavkEZemJ_dkvna_KqtTRzoGBS7k3OJUY5ef7jDdNCvDnumyZSjoPLd-_Qn46eZDDT03FHU_deKcGVqitJG3sZ_GYQs42fmtNnrELZ1D6tOCX5nwyJ3TEhfv-GKzRKOcjIW2JJqRvif9vLNbVOdr5aHu2ZrJi7XF0ZCQGH5NbEJQOBdbSqRYz-eyK984MWRjvxkGw5bhv5vBbYs89ZZXTQdRZDqFlBkUSa-Pr-D2RXJKpbzDXZWqc5P5egPTdkoEKfvn6A-PaJmL0LHCOpFld3dO7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=JHE_BQejhfG7Dkg_jXsTyifoF7x1soguKYu2INjd-mJZ1SwzWnTMp0CdmauTYi7hC5CzUuWGAVAL7lppgrdypnqWDUzegWUufaPGPJI_DNTyonvl2AySyP9Z_cHofmDWDm5QgFl-v7eQrI_SCHy6rKYOyxaTiLiMjb60nQcVhRChI1qcAdiuc5WIdGtxywMGVVK9eRL_R3D8rHV9pAyp_5Q69G_luLPel1ZCmYefnwwOyX9DkIjssCtLSQ_0Ps4YAZSarVpIbk4nWQWSYagbYvmm3RmvV8kgPuxAL51kI-wFCeZySJ4GanGitSdAgURpLQxLYsPh0-d7Ff5qY58rSG07DE3Gi5k2RHoX_olszZ7KhLaReLtkYJsOLl-71etV3ybS43v3BYumALfylAcVRMqVkvlJhq3IIQqd_SQHskp5IULDC9f6gXID3JQHy9wezvzCpPY8fbB0KAtxn-gxyE5sqkw8IDc8otiS-5Nrp1kpNhSYw9mrFObbIJmcq0JvWy3EnEdLZv_Lf6uF8Kks_P-OXnsSu1BwFyBqteAYjhQRnb_X-oqBBR_YZss9JORQPmS5dlJNhs3dBj3a0s6J6u-YkUF6lO7hHPqkasFbcxmAlZF6qm2AHjaitMfl4DfBStveHgU7Dwwo4VQY2nYKW66dbtRDsunQYg5S6KmZvwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=JHE_BQejhfG7Dkg_jXsTyifoF7x1soguKYu2INjd-mJZ1SwzWnTMp0CdmauTYi7hC5CzUuWGAVAL7lppgrdypnqWDUzegWUufaPGPJI_DNTyonvl2AySyP9Z_cHofmDWDm5QgFl-v7eQrI_SCHy6rKYOyxaTiLiMjb60nQcVhRChI1qcAdiuc5WIdGtxywMGVVK9eRL_R3D8rHV9pAyp_5Q69G_luLPel1ZCmYefnwwOyX9DkIjssCtLSQ_0Ps4YAZSarVpIbk4nWQWSYagbYvmm3RmvV8kgPuxAL51kI-wFCeZySJ4GanGitSdAgURpLQxLYsPh0-d7Ff5qY58rSG07DE3Gi5k2RHoX_olszZ7KhLaReLtkYJsOLl-71etV3ybS43v3BYumALfylAcVRMqVkvlJhq3IIQqd_SQHskp5IULDC9f6gXID3JQHy9wezvzCpPY8fbB0KAtxn-gxyE5sqkw8IDc8otiS-5Nrp1kpNhSYw9mrFObbIJmcq0JvWy3EnEdLZv_Lf6uF8Kks_P-OXnsSu1BwFyBqteAYjhQRnb_X-oqBBR_YZss9JORQPmS5dlJNhs3dBj3a0s6J6u-YkUF6lO7hHPqkasFbcxmAlZF6qm2AHjaitMfl4DfBStveHgU7Dwwo4VQY2nYKW66dbtRDsunQYg5S6KmZvwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adm9DSkO5rZiNmG4sthDyeCpYERsXmTgGCuPJCF2nsj3pJRfVdAlCn9FGB6z-sUB9dMiB1pBFGM2Emw-gdFr1rz4Jc1J5TiF1BbZfUOBKMoyFUiI2Pwz4mHEp-niAw5bsYCgPnjKBuwk8OlGRS-t7nubBxkpG6WfHB108epGTAyBRDeCOJ1_8wFbjtOzzA_E9lXlg8Qg8Q6zpN6buq7UKYUyXLa-UIb1uNS3e5GdXgwGohQPnNcGi7sHqLKdi284kQfUY3k1C4__WY5QRoImfrvlfdL1xPe0w19mBhLk6FVNhIGebiy_riOn5vwelwfH68kyvrqTolmFydXijEVUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kou3cQbGqPNJU6_GGejQUfrqc9-Pb6dGcHaHgmKeDOh55_WxvqNZ5DaTK3JLauF5phHFpSGsH1IrfAWaJqSSXKotyKtdMYgEmgoRUWCDl-CoZk5ON629xp88kcGMr6FP-1Fdo6O2b-rb2dNZ7IHRtTiihKvS7zDsZwecD0AhyntuVtn7CVe_FN50GrBZaBQlmQEY6krZvvGXr0ayXV_IvtHd9XiTBksCC3wGxHwEdpCpAa42C8pcFY6AXB9rpS1jKROgm8cvTo4dse-7nD0yZf7Nhq79ASXS1xnr2vcDHocEhrU14V4b0AuNhFVZ3j8gVztuRV6vdlX8xZGfFbzqBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI421uJ-Gfszg6tSHqWjU6X7q7Ki95__qrdhyE7W21jXPCQJsBI9Hup_F4BalUSD5wdIYNesvdfzzvT3azoHftRR9PfJcBNwU9ZVeSMH5q1tl0eQ6NxcUpE0fIUqjYg9oYtAbSPS-QHAQZtRFlgvo-kgaqSpzcG0TJNluL1ZAZUZ65HMNJsnWLU8pwNWNT-Oen8zntaPb2QcZYcrMELVwe736KmmxYoX7peWUE1mcnO7klz3TmQAn_gCLLlXJ0SVIXuUaSm9MC_sq11SgNiq2z7ZaIc1vkZXs92dXn2XMdrtCQ0et99s_5jPDgAGicJIziuGodJhp7WnXGm456_G0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgqfDhUypMsrx3SXbUNMIvUc4UFowpuGpRSweoEnQpLW_v8VFgyYcgk60ZDlQ34iyGYAgkw7TDVXbMwWfHKm_xtocubCxrLQN3oziz7MmXm-tlnzEiJb917VC6UVL10U44k5xw4wQT0G4fNSgqrj8x7XW5wwW6OzVyXMTGyx_qt1ZXh9h3olN3SfdQArO8V3d777R3IimTPHJ1vdP7_Zhlf_yiizlfLRQrJMRmaCgrwUwjOXPpy8Rp5jb4nnr3oa7y6xSu6bEFTi0RveIT-1fkGPVUqcK4cEYl5H0n1UBu95YMF0ziOEzwhQdVOX10IVpAvtoYePRrypOvI5wCCJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCvm56oE7viVu_MGZrGUBfJ2rzxCbO2AMnWeaEpcW4K6rQqcR_g29nGCXqQuka_lEB7Y5QjLnq2C0wT9ICYM_xza64LAFuXJW-SuLr-5ycWTtfZ_iHdXoFOz5GO6zVGLl-MM0EfhrMvlPV0QNPXwyYJSHLiLh-8gO5HSHqIgjJrz_MKVRhv1DDw7d6BZTcWnS-cwYOmQDQ6nXr2lx1uz4eVX37nvnK9KboKDGyuJh5bNfZtrQEbk7fYoNWXArebXeUWMmK23IZLUyZyVzfx9ITaQ7lRHcNBVg961oClD1WJlf-b3kFhjKIOxObqDIKPXdcMYgQitsLe4n3ZEHN9RNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRLZ4CYSX72kn3N-aZuSev6ddvijoCK5ga_l7x5E6t-OR_ByBQXPh5-vP_brOAVlwT5qinN5BhgifZcfwpkVVVpD-ejN0aasVQ5WIC_jxTOjE6E_X1N3F9zr8V5XQZ0I2pqSlM_wCJLK-3XZDv6PHNokZp2CBG0akwnwQSXejCJHwSEhUH2SyV5S2WCzfuM9DC3uXEz90i2MjV7YPY44GIyAQ0xBiekL94vSLwVv2HtpDigCvJAUVBleR1mAP3L89Myxb2xubZWRAPvxMr-OMg7UCP2_Rwl-1tKG2LcnS5whXCU4CHjV6cMZ5f9ewoUfv81uemPjrXVoc9lVFvIv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9rmzt7alZbTFGjSB82dlgmaXxjDU6TxQcW_5kCnRZBjdQfVpD8L66SdvB6tO72DEx5Ot0xqRhXlIRDGfjZMXNWyu3DEGhtFtBCsmLbVlhSe3flc0k_vkrcq6-gHze0q6stkF87DsgThawVrm1RzVTZbY5sadU1AiJ8fM0UvJPuScps9nXh52IVroKDnG65WqIBhZcS_LGJF4Spn7Tm4TZfFQlVOAhH1GH7cpwDI0q1FF2jEBWRmDndFvQLX8rDgQD1jEEpBfsfi_Dh11o_6OpLFOUbzvPAaOI9BzzvEUEJGKAPPBT4LTYSmQe5g383fLkJbRc1JkwOLqJaLSq1xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLzbIqejYKFmoXG12T8xLdyQ5Y-lGEz6r0OutjbQMppUFiy69cNdXqzbxPeSfRcIkKNreG7BLD8VgRn_0NjBpnl08ppi0enjxqIK2iTNLMXa_8yROWQS4sV1ksvnqNap-KMJwbd_PvEFveDJl3i95PPUoDsj3Kikg6Hg4OZmrrhXmjjzpMc8AODKS5pvASyF0PnBBIHrjM8g3UyotUOLlT3I4turJqMMRktGZFZruB61J8_KsILqALYlTvAC0YGuS0OUD-87eGVx6ovEVlmuawsNvs1Z5_i6L1SqRwlqSxS4wrFCs2OANb34Y-YbvhiABsYhU-x0daWKbDruDnVsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og24R94ZGv8dqIO2Q9ViyBuEWxievg7QDMIo66Y2EFoKEEr8ffb8MZpzcHGTHCmgP7wT6w1mPZB7mVwPHDjBhivwC7_VWVEBVR4Rsz7-ueBQdeqlxfnKXJO1nS7YY2IrVDJRFup1TtM_4bmGp7MIXLp-bqG0iW0QWTOV0tBaadcDOC9VZ2O6pCvsBEpZN2F3myWAeVgzpEv6Y7SuzC3Gt8V7IPmXUJrm1sGnYuyJVFr3uALyYfdjpArpfJTiD9vp0A_D93S0tAJMKqE8QlQvmBSsIUQ5tL1TV5bxD2jX3THfswoAMSizrN4dbyvXUjtlP6L1Iegr0NuVypIXs8HYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWrDE00WdWbyltGuvfR0huHCuRFUAWMAxhvuZL3Yu37sSHiRT5zBwccQf6YlAyOjtFpt5AMbXEA2RAVsSRdmu0RxaslBDNa_reCh186k1yzdPYfhxGCfjjbevAKmI_vNJTMwSRBCdoHIxgJPB7OsFMvQmz1Nk0XhLSOMRYLYfL9P30G1gW0Vm3PW3HS9h1efnLBQqg2-d6Jvqsgq5K-l_U0EiBvEpHnat_7dUZZ3fdKJ1OEdnjPwpVxQiFCo5VEFsuUyvgmG6MftjMamDpUlmd-oZLZsUFszdWxYZ7GG2n6hjJmoznkaIszkSe7d2rMwM3GB2v8pgR28EYNzwKQ9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfMe9LmitAmCih2FL84rHAbmQUHwi6IhSF5jFNAqPMxFwQ7a2cHxAwSwEQdghmK09TsIoh6BeXWSOSW-1jlPrW0cO2RAEMzgUsH_4ijlKQDVT5AYM02yT9etdDDJyhf2vumaPVE2sZe_zz-2dEvRgWWuIIuKijV7dP7lxhdv7UP2ipdAZxWZijjvasrq1hhm8v73XiWjt6XXyB0vO35CRPRkh995HwhzNiEUY-x9LdX-8CJpDRyaM2c2HVOWGfEeSr5oG6Lioov0sWWqTkTVNC3xnA4LTgTaQ2mpUvsdt_-JfvtgB3bg5wLE3vK4v6xxp7PwUw3m8fZebanII_mYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV4vCDh9GXz1RZlLuANRV2aSwxnwLftw-HztduJEQNGosWyg3xIFVsPODUhNk8j6jTcATW2PKpNQe9dDWGY4jlFcnjFT5pfkNvPk4OIhd8leJmuW4XOXNtoA2OvY0xRSKAK8zT7uT07z2YIcs-1d1yIfKfntpCYSH3jEIlh5lbW1FjnaIsOkNxALsUnVkGAQyq3KV1MVP8rYoRKJB3Dz7VrpddRItEGD5jnZLPpsQV8n10OI2aLCYOs5cTRUqzfKkoH_rX5D43C2Zm_-g-zOV7j0tSxUYeSeapzbx-Ak0yWxS2d8BGbopwdi6sC-Hu0j0CT5z5fW2-Vtki3WoGhxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHy1KYdHfNAWyoxWB0EzrJ6myHzAFwOLrDMVfXmr4LwKEg1XaIc23WdyTZ6ERhffAcBohpp1eKA9f5JFlfuJ7BFP-W8yX-9ECX4DFKjOXsoJlN6Es-kYtMV6Vubfp65-tnz6XlHeQMIQzP_W2MQTIQM7o9T7JDLrPtjF_Vl_qq2Qge0ldl0gYe3mpYGYTzOr9bFoDuUwPW15OLqWpRmh-Z8H3THiuTL84dJPdFib4mLAXpTsKWQub0nwM1KX3mazj3vuQkIPr96Ld0uP2Z_7N8hEhCrqhDW0gIUaM6tjbYkBhaIba26CKSVhQ5ZH1XpXQMYyE8qzqiX9eUIMQzIxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhY3XKCk-NOCTP4gSYrUmUHFHWCOoLDqg6iSAMgKEeh6NbXKxA0cYN2DgCuLozaWDpvkijtWiWaU_6nRcMgw0mM4QkB1V99eQixahe626Ujy94zlZNOwwnjIwl7f9kAH63dKSFxAxKVxnmGP0ftUx8gOAGnuokhcwgBGEKqfxfC8PKiBRj63jUgouZE9-r7eElnDbcHWs0hz9X-rT2QM990kv5h86naXI_BDCUor0EgCKACb6_vUImR6ZltZwopedLDkp5UkGeRhpc4cQuMjJT-jDxZepLf9Tp3bSoXnclQhImRcCk36lOgTlN27t5Our8-E_r35a4pkoquKpAAdRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbaHC2QkwgM7i6-cYhyq6pPvJwzEGZ2zyHa6EftuAw7iTqgS3IYkepq0XK1kL9QTDdZXWSYD-L-iXi-BlWd8PcgERnBhhmamF9kDgPw-w7ZIWX1UgphR3Mi0injt9ouN1KYf9VAGhKQbWDezPcManOyn_TL-G8ZVGDmZ6w5WIOrgLIE7B19NKmFVWHaOfcSMKieNRREL_H2GTgayUB4EIITshFQY2YySbQ2B4QiYrwQE2csasQ3RqPUBuGm7fFfInIp0z5oY3mhyghmGC2ukQwxJJ-WT5hVJGOSYFgc-1iVtFypsXnNSk_P_hYznjbLjJy23k_U9H8DeRjo90L-wkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZFGrhQ54k_Wx3JKM2gcPmQ4VQ8Q3izviar_crCpELeNCSF10IyMlPNbV1UcC9WY2GjwPrd2mBlvJN3SD-ujIsAgIFIiG8l9ZqkC2nhnXVKloGYt0JhGslyBbruh_lh8t1EeDzdCZe8khI_Y52kRXDDRNytsGeZnXr3oKroxegT84mCtz7FyNorHe5rqmh1vPwUBLc2OQn5fE9Lr5jDwzQxz6pLFEmm3_MUjK2Ru_JepaE-i24A05e0lkmyXa5wTLO54q6aACarYCw0AfePysVH9XzBKXKmqK2aaApTZdBDF_fULJaQg6cdTtUa44_D9cK5zvcIozdSw3sHPulQWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_xPitbm2T05Iuz0-KZviBfbrM8atB26bGP93bkm6fd3zVGZMJGrEG7muFFU4H_yZJcnct-pSu4CSjfmHXWzIBEXnUGfFb-mDEnE4560VbazjAvMGSTMI-z6faw00E9jyNQQeNZ2mycyl_oTup7Bg3lqDmZSnPt7aRYGHmskji2ffluLqxats-Tn6Dbciknz8vbz7P18kfY4xMg9gdzGcAX_Jk3AYxb6dmRNJ3mjjFSKCUKvDumNt-Y_hNJbqtGHk60ZSVY2fD-j1LmtP0ehMoYz2tCQ9R-mcXM9bUcggBwA-sRNvWUBF2Ig_1b826L5nDDHgGXH3Ju8UdZblIgt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eyd15iZ1VloEk-JpYqjS-RjYfBtYKK3IfmAut6ivEqThBHssHFHphjfysEvqUtL5OzfUTaKExXbr6w1O-XXQhnGn3HBUZYeIb8rxyZQScT-RDWkxvufzwuY4hTv-VCgW-QujFfIT4XqrSiW6NvO-Jg9_nn6gQOwxIhG30ZPttDbrEI0NGyyfBxum-f_gesCRipczeTcRI6_X80847Kyac4VckFHqrx5LwcuYoGmIabGtu8ql6KqI3isc3JmvN_dQkDQSpB8R3KnhKsgK7RYP9c3Qnk9_zC4TaBg-ndbl6OATo5lzTzgDta-G-K8570mInkZemT5KE2x8wRhgpe1fEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmleNSBP_Mdw8cFE2QeuQhrjIU0JFaX0JSf7FL-BxET9rEQ0iVCVxXIUxbxuYpmi6zI_u_KPHFogBXhxPiq-AknUUOX0htNJHVJ2_3qRHVYBt7FtozgUoWwUXgA_XX1xa2LBKBmitXfCkrd39wlZW54lBeApj0eBjwUa9jy-vVPKT3AMz-BuisVEjqNzGalaF6AijEJR7wupC-NfGKDsHsio56VEUj7EsLmwW5fC08jA-zcgE_tAQjaM3FHB415TYqKgjTkTqxZ5jPq5B2QwK2IMshrtdUribprIGChn9-tAoy5wjQ4odVFutLwyaDN51PriYCgrv0tOoJVo4_MHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8qLk0DY5Fm0jfBelaZnCLP2tAFMBcOaKVSf3ial0pwxWNPvM1mA3fy9V-KRC5_qC0RFEOuZcL6AuJGxj5BoSLsUfadifTlu-K42N-vh9wWNQgvhNwSY_MDnLJtE8TCLCnexO2Fgj-Wp1T2k8bSU2DiacE28QX0-ZcZVcCOcOqNwU9nkLykqrlg4YS7aHU9gx6FZCw5Gd5nUB4xjOaUsbco0Vqc-mKJmLOq4L2JyFEJez1n5yqNglfuAadVg5hm0pS3Z49lj857NSPdMNpe_Se288YdVdiMPppN28uiaJVw39_d7TiLufRpR4AP_-k-OEbNauaa9q9Xo9mlL_t8PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0nsh7W7yx4LvMZvcZMtuirLmvQJvYt60XkRqiP1--T0rIN-pQBaAuKYjsMF3lWUEBE7mXtEi0fdaFB-ZqdNCLk6kRxoTZCr_3UGm0W5M99AZdM0600J-Pdzt5XZpzSODFISi12CWcqAqUS_yxBau1Is_E_VmczA6HkdAwR3HfuWqE1AXOrTqPptvHIvGkEbgaMub0d2lIZRDte9uRAUkgTzElvT1XXGkEZoOe54Wi4CVy0aikGSkFQ1NfeiwNAVlVbZ0witflvSFFXbmmbMA3CGPm0VrhYCN4WNc3lbZY5rsN614maIRJeCbMau9bhz9PWGDDO48PpDHTjm3JeJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfk8sfelso8DqtxbgalmkN8JzkZl2SqzCcdMzgyvxaJo_GF0zG1VGcwRiTlensyt4tsdlf24ugKJMIgZ1Y61ztgMwdEAQR86kVO4zijMoPcYDUC8sRhyDYGmMtQAEH5fUHV9w_cS6_vKyiM_oW9e-ahl2O1cuaAj0utcOw_eynz4MEZELBrFra5Xty6QlVvc1Lmp-OWs9D9JgbmUrrn-vpTN8bw4AWdfUmi2rrt2C2vkNuZWte81S80iEi5ipmhGZn2pRlzGx00uZCVe16w9En0I5Rwgy4_V1oeppLCdek89OiUKJ6UFloPdXmCXbqRwmYhWydZo8pIUagg06Ap-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYre0EXc0BU15fhBSkuhWlB808P29eTWNvNhREYWmBfp_GScZlmtaMNwN5zG_ANHu1OOVBW4F8qnwwb_vxK66zOhdd_LW8uhGoQYMgCLL8RKVwlPgFVMjo2w48JlumseubpS4cKPC2XnY864pHf1N7hSYqHbOapF-8iLAnuIq_UKeca-EbciUIy506-67Ql4vscaRQKvuroPgtwbGeSikRzaqlMpi8no61O-6kut-vArbwRLAt-kOfeOEv0JmYJXhGSn7Oaj7rMiZUEpBb7nlHsmt4KFpDusVbQL-22lDSgS7kQxpG-tvquDxrOWayaXIyZVUsM9f3gGHbvp8-tMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvWA8aEmc6UBn6y3RLZo2i3gqe-5ZvlseaiSCdko9NkNmKw7-l2Rw37iOf9eXrqjLBQmGmdUd0WTI1ofbHeOPvhZt7j8M_XqEGyC5f5bAD_phGnpVdwTPK7hMfq2abJbPcDnfxRhWXqhOsaAcbJ8hbdj_A0i7X-hjB9ZiBaAU1_Nab3gQ2DRyX17U4qmKxbGAtMmd_LWusthLjtPGdbEA6zcJCMOyv1IxtEvg7a3SKdXEk1R4b-5jtZt-wawmn0DVzQBouYgBsjNIBEUQQ_uT_72SpRhO6QbQxOspSwYrxiL6pu69ESihvmCyi2kN6Jzp1vA7Y4mHj_BqiyHTpbHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCp4r1eBMhsW1jXvjzJ7z4e1Q-8tpSSzuyEoIww-W-ArLyq1WiAEQOpAA3QjG9kWL0utfSm0FXZbAHHhDRM4vE0WY_OHTpC46IfOgoLqdQgHJLVAIv11AD-Y6uCoVZv8ekOPHEg1NCrNXtN4w5S2GYkxia9P1JkChhmsANGxz5ahEVcLFPe2IYXXDB8qE6U2QEv4H6BwGFjvya5yrVqC_lnxo752E5uwKF6fNcrS1yq8oaDUzg5uK1QyFJY_HUH8RO6SbAFNdbp8BI2o_bF2Gpeq0WRaAKosDoCJmj4afwhiOmjMYfnd319VPvOL2tVL-KGmdr3FRPd8KOd83Q0v_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdDxx7pAQU7pBRHw8IBao2A2T_99TMhQpsnD-NrkZJbOryX24e9RCXUDwztr-YpDo1w8Z3qpmtM4UH9kvOhdPkbQ7bUE2cr9WyzWrfe7Z8NaC7gL7-AdTYdzeNSvUlU9kwy7TBauE0TYtBjNzQzy65vpSeTtPCaQEYtO1DeK_Zez6DfGxA1WhtX1Oa_UtgOBMFnDbTPvbYVLc1IucXRpKHKj1Ah_LtVkhLjNlbRuooRasaWrMjkz362VKKJKA0ckSYiJu1zQgfrvucPzd3B68K0TBq9QZUhiXUYib5J9wzT6JF82LiZZftYwjKGj18A-A3ygtvguMZpi5oBcHtVd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS6sAHIFBI9Y-saJHl8hhtoaOUzsE2rkWx1l4TD4jNx_45mPAnlq9LFrCq0DepaG7v426YmoDfs1nzWFoMk28Igk0-efp8eWLP3qA5n5vwzTdVfDt3jkeWaWE5vl2oYBZrEJ0Nv95zRCua7UzMDRODNci7rCVKIBUBEZrg8i6cca3oz2XaaVaYTU5Bgb1naqVw5La09N3Q0Jzk70I8VpHXtsZhqoI5Ht0mLpUfxSJnqa5j137P83GsmDDIbmuv1xhRZCA-6CA1A5nlDAegfhzUBMZmfjvjwJR5c1uQt-aaUrOqSCGfvVeXGPH7OZffFjjOXLQe43920RZQrxZ6ZHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO9JKoglQLbVVurXvMDrIKLUAn0U2j3VeqEHCuwCJeqgbz26AscfbQ015y4kDrd68wuRp0bOeKWuKAVSh0qe_NZj9osuwS-JDrGDg2q2dC7uruLAQ0vSZVJcau6B1DB3r5J63Dm3r9VJzhA7y9rAf2OsXKodK8mKJLOQVH0-LCS6cSYCiv9NfxloKrsSZAIQhJQsqnS5cx0zgqznvsNulJPzHxUhQgga3uOP9NKxNzqMhHF3-RaX8zHlJa8MgZMo9akB29LheYnBy7F-yLRVJXwq01P8caqLuENsbaQEExFYRRQ7G3tgnpmcqPcXkUQfz80HV9bh0JCzkGVRfoxyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDPyu4Eixiej_WcZ3MWQH7RJxugjMqThAUuKBKP0uP-EKiw_jN51dMfoQuP99YsD9E2pWH1-D0b9QIZAFRyriBp9KlmY8Pjy5BB1zDvKZBrVXZ0pPn3TyR8CTz9WOE9l2RSYb7hepPw_6Mm5L-AR3a5obP1x5M_U7d0VZzpjc_BAoPRiWqI7CIMsA77ethWBxfBU8htAZlqAgYKWQ-_MCDCrjhHJaOEvd9mlM6JXoCn2Diy4S7xH32QHYYsvaFurKOM0lXNGkzFNhY29qJGFgnLcppefZrbu29Gl5-afmPmLivncl8kBDKnDrsjAG3CafOmTZBTu41K1fjYhW2CZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-pI0g-Rv07PXNjUyukfmVyfhq-Z4StTLPoBDQFnm1GXUFE_mp1WxxoYvCvNDEkcLN7mfha062-MCiw6BdzlFs3T3VKQH3GPKmdHvhvy3sBl3TGBvywBMzm73Xx04OVWHeros3wI0fM0sQxK-sEXGnQog2M9-DSXOyph8cCN2KLkv4lpy40ZOvg3TDpKMO1JuOfnfE2FXchlciZ8PPrd-tlT7GR1YD39RtT7nuBKSzqwtDLMRCxXIb3B0Oq7sEL1VxxO8M34mDidlt3Kr1emr5XxsZkCktes59MjAO5IsrDxnFUF5SLNXxjUAW7lEIXXICngYLaKzAqeNaFYWfJ3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOk2F7GQweVCA8ValH1oEtcC1eg9JNfJ3yRSqLDeVouveXfhE2pq52hLdywaUUVFm_UK-cWk46GvaFL1E-DT4tjxAGyeVtpHpRknuKwK9jogutvyJsZEC9CpiibFsvWfHtzW2pn2Ub2yYWst__nyYxgFtdb5hE81dY09Y3qwPrC1jy13zGOR8x6HIF2p9wlLGiZ70anw_PvDCaFdpCLL1diUZRevd7folG3qk4UP_JxLjiD5bCEDDzteOYepsfUnyjt061F0aOn_8ZYHeCBE3vQ4-xMX3RUCmw2Gd_bWl8LQJf0Z5G81djhAHrTaYGJD2ur0EFPfqdmkR4wFBZ0YrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qszIbGjJpruRSRwxUkbUmYIZeqC5F6EHAHC5J2pQ8s3ebrgHkh7px5eOqGDqW7LjuQcuZ2iMfirp0MrxrP-_Ak-s3GC1LMTKz9Jhe-S3zzBGkxnbSeqaBz9B6OIuShOmGaJjTSCxv8iHC9q77W7wt3Irhf-i-SLs469NGY33BDjYrFsxw61iLWjWaoNhApSgx41Yb-PZznOGG8gzyrgrSn6349Gnexvr7CyYL7obj5I-SFjG-um6Qg4k4WDulobYhdRIYRrTXmLDgP_4-0GXKheZzGFK6aljpdRZeEsxdZoPgpEuIy2ac1yhWNkGeWxOLEJXnPec_va51D4cUVHAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7FBKuACctF-MqAvM7P9wsCzqQby7HbhJHdFNa4ZP6cx0EIqIUazIlXhR7m_dQA3I0m24P8DHMIVwLHK3__WBO3seaVK52SzOnDfaJrY5GQuFDfurb2pzOKIf9Z9XtVOZ3X28txwBa5FA-svVJldrB2Z4ITY0sqNf6TRBcaGb2wq8iugzbQtam0FkewR0AUDGCGmFMWsa5kEi6WwKUint9sTSi4r4aGu5fDTGxQn8MtlnLqUdHrljU3QhPUxL4ZGLwx5es9nI7WYf2eViqDAU3j4jQ09t-lK0Lb29NRPebwBa8SMoLxo8mmcfsjkQvcWMwCWZ2cFEGsNiEmJWYJe0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6cSR-3izvhhLzMxceJBX3Ea--_Oj9Y5w_zP34dXccuaTjJ0LZ3sYjTkkGXuw7_CprxbN9fJAaa2X3vkQkQrlE7syDOs35eIEhHOtZX4INe9Je9y9gLhZdUTzU2UWvm93YheeCox4b7YKYW-ia-LXz3GVqT2UI5VIi7If5PIfo4dlhVWtqsvVVNkDL7f-u-qgK1ODPvBfF0XnYMShLf9bpDVnfoeYskBJXKufj_AIf48JOjAj-Tuds_xC0ZrppcbjgUApYEvwzy5Kbq0Q_JgS9hIiS53liTxG_UCLeslbYieQ76OhIqMR9Zr1rXosVKSEKuiDeftuCVX9nB4KvMN9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=iAXF4TkTDtc4dVL5WFlwEVjGTOSkzBCVgidzO5zgkSncqdzUkRFxwusixl8Uee5Ty3sfKz7B1WRNhu8tMhm-vf64zD8qC1IP7EpM1vc7F-tuvQho1A4s_9pDR7hq4ijnflGxbikbTKFKS01H1Q8D0XdQK9fzx9yCYryC4pNr3wX7IVrcYz2F0Q8QE21Peqcdspp1aobgnbR1x7HqN5Y3hQ9aHfcxSR8_ty269vF9YnU0vP2OWpVoNRZTxOVV140QqNXwGYSUFDOmZSWH5gMT10Te2HYAtjNvBXA4l4Y7xE-H7yf3E8hlQ3cg6D3SYa8wiIHxfS3pef6XnO40OdxoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=iAXF4TkTDtc4dVL5WFlwEVjGTOSkzBCVgidzO5zgkSncqdzUkRFxwusixl8Uee5Ty3sfKz7B1WRNhu8tMhm-vf64zD8qC1IP7EpM1vc7F-tuvQho1A4s_9pDR7hq4ijnflGxbikbTKFKS01H1Q8D0XdQK9fzx9yCYryC4pNr3wX7IVrcYz2F0Q8QE21Peqcdspp1aobgnbR1x7HqN5Y3hQ9aHfcxSR8_ty269vF9YnU0vP2OWpVoNRZTxOVV140QqNXwGYSUFDOmZSWH5gMT10Te2HYAtjNvBXA4l4Y7xE-H7yf3E8hlQ3cg6D3SYa8wiIHxfS3pef6XnO40OdxoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4rmOYwvcrEVNppcSo-iQL77u-whgD0I713qRiiKnmXIKS5aSWJvb0cwy35R4UBSq4esqqvNs6jczMMWLlFN-S8UZPeDmoaH5zjtaL59w2Q-qGVVYJ6wyPy0nO8qrL2IFQC3uwHQJ41FYRzhphVj3XBVl0OUd8M50iIE1sGgFUaVyyGi56lFS4AkOTCjH1Vnd6RhsiSnbe9nTe4hpVIWw_XbcEfk3wGnq0YAufQZgp3dZjL4TTSsXc4GReFS5ieTeBvlowVc8MHGe1P1HMISTmIwghabg7ai3LIaSBhM2h_-kaObUEWp38LBcVG1nIIX12syZcFzI6x8bKqsTIcRMA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sEdZ-82kNB6HmJzX3ZiNFeIpMQYOxtciSAIH-95dcalgp6NSTFxcYMkAkxpR8U5grPDg_rS-UoOPr6-q4hDGvGRhr5jU8fe2pI8WVil4adHlq4LWAChzccGUipmPgcviOLXcc_LhTi91ia3WfUQARWAW19waHBQn1IK413U7952fC83K-q4_ejgQON7j_cMIYX9fJktJUJv2JVnPfJ8OhRfExzuRrSgVDFNdJUeiOMVA020LEdAHiEInRMJiSllFwUleDS-_InJqsostHPcQfsU6-aMwjHDEerQ-Gv2xTzMMARv6mw8XT70iIapSHPZBdUVGpNtMPiGuiN3Nb_XV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sEdZ-82kNB6HmJzX3ZiNFeIpMQYOxtciSAIH-95dcalgp6NSTFxcYMkAkxpR8U5grPDg_rS-UoOPr6-q4hDGvGRhr5jU8fe2pI8WVil4adHlq4LWAChzccGUipmPgcviOLXcc_LhTi91ia3WfUQARWAW19waHBQn1IK413U7952fC83K-q4_ejgQON7j_cMIYX9fJktJUJv2JVnPfJ8OhRfExzuRrSgVDFNdJUeiOMVA020LEdAHiEInRMJiSllFwUleDS-_InJqsostHPcQfsU6-aMwjHDEerQ-Gv2xTzMMARv6mw8XT70iIapSHPZBdUVGpNtMPiGuiN3Nb_XV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCN6cLzj7ATaPjOiv4A3La6Di4gUxpsX7jR-28pkRd418m_ThZhrz8O6-3G21RRI2PTrCUv7I5MuxorUquRBQnH1mcscxSG2t4A1XOYi_hctvbUqjZicRoBgykeFrVJTBSf6PaIci-QSlNrTMMjNxmb6F1kdnBUMSw7rERmGdTC7gEWJkATyipbJihMJP87W3OWzZ6rc1YwhOPspJtbnIdM5B-EbHy80v2MiMA2m-ceyAVVDtchm34dBMxBmZRcuYhojyxWrMBM-U0ZNKsuUYATgfe1kuXgTiWYngBh0na1Q2In6UxOCLGa8Fga_v34oEKoWUzavZC4wgoLSUPBakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfom0MNvFMP-slKMeYPqXlUWF4zBIwqcVtSe4HUSpYK4yg5yHTV7P-YMiNKdIGPn82uCW2Nw4TEX3kWCx5IbcuxWyLdeH8rbsSPWWTwv0QkMyTxXxVbZPoRbvB-kbaNs_tZLsKMy8X52aBmy_JXT3saCRI_znTMWT_mLmNOELTDNWSRyvpPlA2EGeaUui7IhFm52_pGNITmGFLDxE2xZzNDCpTF9oofZTktlGrNZTm2pW3sd_tU8Q2xNr3QRFJjNtmsrBiQYykNXrVE5I3UYd24nkG2DwSBS6STtBhGDjcjHROLVx1v6WXULnvvhy6uSmy-5XoBKR2uoOa1Y4jEe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=pF00txmYKDSSX-obuuv2gOeVaj8edk-o2pBZGPd7yKMvpn-Oo94opw8iIJNZjNbRrdoUQjOdWhfdP-0TvkLnmNv0aOlhQzryGuvoGj5lX4dJczT4J2PSBIDO8TGY6DTI0w4omcKAo4wQOdroPHGBECDmmG52UCLH6RUCsbRSdEvPkOKoXtpBmL8zjgTsT-YkXuYtX4N0waDwk6IDsUPLmPZnUToHvRejAeim1jcpDqSmbpv-FRl190uz2l6z7J7WKsLTko-qKyCDRW8iyOgMCIjoyeWLwclKplPrG58fWZEMBF6Uf3zd3aw7u6ZhBaYesQn7mJlVpcNdMX7aLJPqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=pF00txmYKDSSX-obuuv2gOeVaj8edk-o2pBZGPd7yKMvpn-Oo94opw8iIJNZjNbRrdoUQjOdWhfdP-0TvkLnmNv0aOlhQzryGuvoGj5lX4dJczT4J2PSBIDO8TGY6DTI0w4omcKAo4wQOdroPHGBECDmmG52UCLH6RUCsbRSdEvPkOKoXtpBmL8zjgTsT-YkXuYtX4N0waDwk6IDsUPLmPZnUToHvRejAeim1jcpDqSmbpv-FRl190uz2l6z7J7WKsLTko-qKyCDRW8iyOgMCIjoyeWLwclKplPrG58fWZEMBF6Uf3zd3aw7u6ZhBaYesQn7mJlVpcNdMX7aLJPqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDPoODwWwhMGvq_L4jUSPs88b9jVtQU5QqsZTFUu6r5Epzd82iSD9XhNrBXkNXWLxWA_OK3Amqu-azwmg5dZuKGmKunr_qwt60FMVul7qkvvbEyVjHHk6M93wxIK5TJUfEOCoeLfSXOfkYUhQRSZBoNonsB3Xg_Tyb5Fgd02hKhydQSUHcyb0AVoV9kpiPbNDj5FhoInRk2s-1prYyrdkm67Xrs0YaLh6KFnnQa5IGd-d2s8t89n7COoFA4_7ysvXlFMfHlri2evhchenc7efVd7seyw-7TCxSEBlufyFiEPdaM5DoaCR3l9wAmNXyXu3YaPrRzayMZ1v2d_G43XIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcawEI0ZDSl149EHcfmkgDc4Iv-0NS8IMRwEL3FGjq_X0LpF0UmrT6IIT5KwcGwTB4sJ84wOZr4C8SJhO5VMAyFTC3EFUyujduVDqsC0ksvtWhhK79PJoDkHVhGmJOR4w0UpHm64ZXD_snBBh21Oz2rGytbu6Q7w0l52f7xKp0mLaWqxfouDUdxoXN9u-8BxHG4zh9pyOXKd3WLOsB6Z580es3D7V6iO1HaOqE2eZDi3Qg306klxE_1feaesDIamHe--s_hlradwmDH397GL1N8I4YlWt2Wj4kPdvJQebQjpzE4GU9RBCLy4oWbw_LLGdaMkobzcj7DZLCA38WwvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTnb2EWmh2bAkHYpmCirkH86KzORXIAQNumDuAPZBnGPYsagtIEcexiOuXKgHYOm-hn9p88IHmS4UDb8t4LpH0tF4lf1JHlveHfmFC2JTAsDmlNhSfkALvEjyB8gE1UeNTrUksIAY40d664ku-2X7m5Vgj9CdF6KWpK8ysyWKxIe_OE9PzkEnkVf6Ay7aaLph2VhIgUDG_uVpIXBv3eWf3GXJgZO9DCzKKL-WOAqzMgLqQJR0zU9r1CE21ncYyRX9aDJbl-5EzecEcxsNs_k2JVCj2s2mzC0ezPHJeuFOUCOtFfwvV8wwFOe8HaZ7c0Baqyk7bmPUhXC4rTj2GMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=mVMeBth0hy2FCGGvxm2xnulTfTr6eqeH9f4_gXBjtix-Cu7RR2XFxSykRWuBowt3Kp_Xp9uImGLcOs0TW2R0mfcrwgkcS5LcOWjIRVt2VxHbu66J-ynL0unH58Gmg7QyS-EHcOICHqXAK817MjxuJAlA2Bsk4WOloKnNgWC1H8X1dHnm4fs4GbERDMnQhKZDRdv9FQB6X17ZhUQfYITC9rSoMciSMvPCLKU7z-85Kp-YBtGcPJv_4eIIgdmZUJsjNYY_nIFYKYS8nk8kmDFpYdHm3OX7nhX3rn4msjacuiRCjbvofGONaJweER3qf5YlysprEMIBDdqiVP38S1aYQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=mVMeBth0hy2FCGGvxm2xnulTfTr6eqeH9f4_gXBjtix-Cu7RR2XFxSykRWuBowt3Kp_Xp9uImGLcOs0TW2R0mfcrwgkcS5LcOWjIRVt2VxHbu66J-ynL0unH58Gmg7QyS-EHcOICHqXAK817MjxuJAlA2Bsk4WOloKnNgWC1H8X1dHnm4fs4GbERDMnQhKZDRdv9FQB6X17ZhUQfYITC9rSoMciSMvPCLKU7z-85Kp-YBtGcPJv_4eIIgdmZUJsjNYY_nIFYKYS8nk8kmDFpYdHm3OX7nhX3rn4msjacuiRCjbvofGONaJweER3qf5YlysprEMIBDdqiVP38S1aYQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=BIpte4oBlCnbGgoktf_bC6ErTe4NqLY3_xtJMG58iuqSjuGtOUVLILGFfircOeJ7fxBBVT-iDIFZZfvOTwuHr3HsaFk0egwU9ZZKyXRzAAbwjL6XaJF-wrL2JeRS4VLBfMe4A4tQs9_V6WQEtCMGMIWWleg0XwvmS3sdGeD1Qg0fMYRpW0FlWCHI8XEq-zHF9bCoRd0OrtovvgFRizhKq-k7IJrjp9FGGjrFb0cppPnMjNhdzocbG35VD50rtsY8qyyBoefYM_xoIDfLae6hs4miGY1921Wu0LivF-EfxSfLNBDh4eIz9ENcd5TCppyHppIF4Uyeih5KKdX1CtTxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=BIpte4oBlCnbGgoktf_bC6ErTe4NqLY3_xtJMG58iuqSjuGtOUVLILGFfircOeJ7fxBBVT-iDIFZZfvOTwuHr3HsaFk0egwU9ZZKyXRzAAbwjL6XaJF-wrL2JeRS4VLBfMe4A4tQs9_V6WQEtCMGMIWWleg0XwvmS3sdGeD1Qg0fMYRpW0FlWCHI8XEq-zHF9bCoRd0OrtovvgFRizhKq-k7IJrjp9FGGjrFb0cppPnMjNhdzocbG35VD50rtsY8qyyBoefYM_xoIDfLae6hs4miGY1921Wu0LivF-EfxSfLNBDh4eIz9ENcd5TCppyHppIF4Uyeih5KKdX1CtTxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMnZrd8pf9EiB2iRTbQemQp6ZxsKGZTAW2LniIWFpGyGOmAFnJNJamKuoc8Yegy1aY4u_Wxx_ku0QuGCSazRN7KSKe3NnTj_TXypMjKDIxx4ujBKouomD8tNhXL8hFtF9m0R6sGxWqZs_A0ACFHS7E4PCdF6upWtXRHzbLcA1bp2cggMJH0UnHfEYDwjiJqSuKD_YTgmm4KnnwTw58SnnEtq847yOS3x2r5jAJaeGWXaCsOH1VrshImkr8e68DgOIr6MbZ_mtg67FTI4QTCqGBWzHJDYQP95qwhyvgFxygQHO6qpvhwSuotdqJG6e5RYsKErn9P2MY5UhAgoDcb0GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVl0QpprS78iRRnvg5ntcYtUuDYPBowVecTp7tLrYnMKlSqIS1vGFwUDQkoZjbwn2dB5yn90kNQr8RUy5EbIA7tQhaIublWGQcW6am_w885CfHfE7unuPRni7hzgEAIM2s7YMaJrH3-m2g7_sMGXEmKhUzi61SVqJnu5L-Sg97kKR_DbVlxQ0tO6frRChC7sBVCMJS61GgZBhdepefr3AOjVp6noxuMG43m7VZW12MKaZvBrV7KebORwpewE6aIRUDUs27XtyLmviRUHtoyER9oCALVUWBfrrJUbxldxZdoUwtKzDX-4XKWij055NjVSqUQw8fy5-UgvrSBApBL0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR10PBVTyWv-ZdHeWj8FlsLFXHdq0fYe74G1ckISkIbtgODC1RZpR2ImCWUr--ReNF1dgbsHyDaJQvIIfeawZTsdA2ZYp5T9h0bY31VNarAEDFJf8IULTkgBZ-60u3biOZtxOo2n7NrUNYWTlNKChYNre4hvuBBD5IE9cnlRsMMWf9a_XjJYNTFjCSSZSREYEI5ZCisFgIMEbk1TkeplMdLeSWUJA07FKGdmi1zhf8TW6zVJXYh2KVWsGBKGwOuJuBk_p8Fq3bPJEojw_RWkyRkvf-49JOB3toRuJ0Gjm3DElLO9pZviA0gbBN278IVtsFZtT___hFbhg7kHY8k1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miFv8L1a_FPGStETBzjqkWw8KcyNA02u-eDkRVebv198K2JSUjawzbDMSZ_UciV7p61O_-bBUXlYNHivWXI_kOovowsefqNyCg348UOLFaUmRIpUxvpexKUoUZ50PALDLIK1BRym6-NmKXWPbhVo187zeZxu2ApiJluHfvw7sJckHEIM8a8-hg5YM9K-l9LcmlZwuGLY_-pN_ji8IsXnScab_JjWI0IHObs3cbJdOPtWNIVsU1CIrfVEzojQscH5UnFY4AYU5s907VJ2D2MXQ-TthJV8rQsXm5RPiIUPUzdZQm9Uiq6cVnVjI_3vfDkvfOSBBIPm0X7xkuU7ljVKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l26VDUWGVOYiCbId2gxoPeRxLrDeNk5Y6FtYm4hW6-FhwaiTo72bonIGENpHbMSwl0LhSKaMGNNZjOznUdGbLxBqv2J_EChuZEytioTGETVelbw-bnxh9b8AzIlrXZ3stG33z2wnCo0_RLZSXLg15SYoOvyxQKOVa0FnvnXwFNsB7aS3mtD4XrRe2h9pHbbHn3kPNubx68SEkTxBXOG24l8WCq6_VJOCs1lWvfRVEfD77IRGrvsTk484_-CdS17BsaPQK_8NEtN1zwUWpEtvhRMCFqUZQPDZCJtAPgiBE92tfxZmtnc-QL3cYF4AHNvKYsLmZ1oIOeAQQH4NudQ0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VocFUxwVCr8QgNYeR_TIatbkZ43VWR4HqEX0HZ_WAnmrYOl2V_dLlrhi0WI_EfaHfo0HKeUoIVsisxjYQ89ZB6ppB6an7GIt-clZdFbWrUNIzzHrUWohhjb8bYpidfpbmst-GYRTKHz6XThSHNGtLSQCzUYnc-I9H2gWEYJjz3wticbaPdlgTNaGi2mam9ZLnw2kDuo3ua3fOVHCjYnDjQnfizPf4bTe5EFTrbBPyz05Ttk1LomNXpWaumDGBZpEgoCHNSTltsOPN9isRPg-_1ryT5fuMOU_72JU3bqEck8akl9U1Rn4uWxFS2YasjeZw-XmsotR3ZgY3U2kkqZ3kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWc6p-WaYhdYnhTq7jLyvijW1zOtV8a9joZgV1JEYPPYX49P951PUtb-apL-bzfV78dcO4Mkd9CINw5ybAlC2tYm124ZT8hAY6bbHGS4Ror4cDTqAALUYbswO1QtaOpBXhcxQVCexpy8bq9O7mNdA23ezV6YulXf49GEEebixhyKH0b0ScOfrr84yrnxSYNXN86kFt6gwFsKjUVvV9Dpkvvz_fX5T7WdvoR0M7mFBkqvy4qhXuXp4Ee521M02olW86hHBimcb6cTi9gneGBUfiYU3yB8nIX2FvbSg1-EFABZhAXHxh_mMTo08VdI87PUX1G5ylvqIu-UJEBCQC_6ug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=UiD1d8f5wD4jvlmG1yZjZVx9afOzmz1J4-4H81gqhmCDkte0agRG4Z1ffZ7N_p2_7jor-dzoBOmSdp5bvRWL5ip0s9pH0a5EHAPT47M9yxWh6S822WI7tS5yzrCsmPlLflLkGgKjnv_DfP2jYN9bMic18taJ7hfltr-6LFDWOmHMpmnWT_SGvj31wGp7UhrANkLdQhLR0ddHQDK6ZRyuKmIZ7UxbuvZ3PGze-NOkVb9A4u3iYvorlcAFBkH8BWS-C7YEXTSgq0-LC-RzE5kmKWGLP59vpRHKxWCOVknzLGvBija5Z9uL15BAC8lcxQZMDTkraDQ6c1N38sUp7Upg5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=UiD1d8f5wD4jvlmG1yZjZVx9afOzmz1J4-4H81gqhmCDkte0agRG4Z1ffZ7N_p2_7jor-dzoBOmSdp5bvRWL5ip0s9pH0a5EHAPT47M9yxWh6S822WI7tS5yzrCsmPlLflLkGgKjnv_DfP2jYN9bMic18taJ7hfltr-6LFDWOmHMpmnWT_SGvj31wGp7UhrANkLdQhLR0ddHQDK6ZRyuKmIZ7UxbuvZ3PGze-NOkVb9A4u3iYvorlcAFBkH8BWS-C7YEXTSgq0-LC-RzE5kmKWGLP59vpRHKxWCOVknzLGvBija5Z9uL15BAC8lcxQZMDTkraDQ6c1N38sUp7Upg5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=QtItw5kKMbdzxmAOw7YdR2pqCNu9olfQXaUxBT8qD-loYywFGrchw6SOczUgUkVAMD_Jrki7CShXU4ObSxJEPowlMPDmsf7bZt_ch8bOM6aiN8acyVn2L9sqPCrZxaPVVqObOaayWYsua5e_sXI1LnsQBf_vVieyXeU32iYrWkeHIeK5SpDqsPXoR-XrBKvTu-l6NV8El9WI9ZEDdUVTzrwDa0gx-YpvMxeHyfEsvQfupCXXwzC7zdvfzj6ii9r7ADHYr7rZbovJkcjaJ6K6zjLfYCVDXV0_v6HVUR_XyIMYC75co9mSAvdfzycrhquXOd7gGtsmxFwMtUbqclX-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=QtItw5kKMbdzxmAOw7YdR2pqCNu9olfQXaUxBT8qD-loYywFGrchw6SOczUgUkVAMD_Jrki7CShXU4ObSxJEPowlMPDmsf7bZt_ch8bOM6aiN8acyVn2L9sqPCrZxaPVVqObOaayWYsua5e_sXI1LnsQBf_vVieyXeU32iYrWkeHIeK5SpDqsPXoR-XrBKvTu-l6NV8El9WI9ZEDdUVTzrwDa0gx-YpvMxeHyfEsvQfupCXXwzC7zdvfzj6ii9r7ADHYr7rZbovJkcjaJ6K6zjLfYCVDXV0_v6HVUR_XyIMYC75co9mSAvdfzycrhquXOd7gGtsmxFwMtUbqclX-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=FRZCuz7JU2XshNKJ2qZ8-7qAObwdS_Cyl9OdhUsM3goZfmNI_TGpp3PAzLdBe7Q-imtllcXGdBOwqeXvPE0KCBhlw-qLvH03VTYmMfWR0tPo_kGLX3BQtpRO3DK3kD9i97tQL-Ckw2GeURde_z-631OvH9Z5fciRuE6kU4iDarnyscdCPFjyGYc3P5qOpkeo_ObRqSUnfgaD1cInbrejm_9EYve2t6QJ9bSaUO3NqUqURsTG6ogwISt4ns63YsiJ19nQIDabJ8GkpCo4mPIYnrFQF_xtL6KxX3qnc75W-6rxm7cZQUdr3mKIqixZeJe-mf2P0I5oII9Zk4qdRVOOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=FRZCuz7JU2XshNKJ2qZ8-7qAObwdS_Cyl9OdhUsM3goZfmNI_TGpp3PAzLdBe7Q-imtllcXGdBOwqeXvPE0KCBhlw-qLvH03VTYmMfWR0tPo_kGLX3BQtpRO3DK3kD9i97tQL-Ckw2GeURde_z-631OvH9Z5fciRuE6kU4iDarnyscdCPFjyGYc3P5qOpkeo_ObRqSUnfgaD1cInbrejm_9EYve2t6QJ9bSaUO3NqUqURsTG6ogwISt4ns63YsiJ19nQIDabJ8GkpCo4mPIYnrFQF_xtL6KxX3qnc75W-6rxm7cZQUdr3mKIqixZeJe-mf2P0I5oII9Zk4qdRVOOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=JGubiziyoVZ4tp32vsQXbmJTf74h-uRPBNr7TdUb-pwhVuOBSLC2a2fu_hR06iQnxmaNzAT1CJ1SgapC_iQ-C8-_vGajX1R7V6xShZ7DN3SFrDGHDBqPCjGPNS-0LjQvjyljPtkwFf3HlxVs5ICkUgvCV17vivLk5OwwjaTEppJ6vgjQVr44J7FxBTq4fmvg--EZXwEBUy33wKHt56jWn6kdosgStGDY9sFB5E2v6X7FtQwaCDTaNeDA5obiqldd4QLag5F6hHwz7yXZgWwnYMYFW0KdXTBoKEq6_abMD5Xg8CopJsCvgsIPi1oBJaJwO_Jo4CMvtyzlokQ3OuDNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=JGubiziyoVZ4tp32vsQXbmJTf74h-uRPBNr7TdUb-pwhVuOBSLC2a2fu_hR06iQnxmaNzAT1CJ1SgapC_iQ-C8-_vGajX1R7V6xShZ7DN3SFrDGHDBqPCjGPNS-0LjQvjyljPtkwFf3HlxVs5ICkUgvCV17vivLk5OwwjaTEppJ6vgjQVr44J7FxBTq4fmvg--EZXwEBUy33wKHt56jWn6kdosgStGDY9sFB5E2v6X7FtQwaCDTaNeDA5obiqldd4QLag5F6hHwz7yXZgWwnYMYFW0KdXTBoKEq6_abMD5Xg8CopJsCvgsIPi1oBJaJwO_Jo4CMvtyzlokQ3OuDNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=JDcbNwxesRsN7L83UB_sKEaxiGdS8MBxxauY_IzMtTZYOKvUVryZJ_hf3e94S0TLbF_HNpGS1FxmrYdoexbvRIvzms_N6WFQ2oKukRL9U_cg38GfFR-8vS266slETYYraJGNjLkEzMht0EWMtUoxhCIpt2rodPwuy-B6Jjd_wx6MO-B0aYXX49FzrilRI-MS7q5jpAW_G0xw9wHldhhd6iKmqjOcK7oSy_cGqAb7wDkvrIXOHod17aXD7fg3h9XzIiYBwhuOrNvOhTQE41KsQmp_cfi7jmGby-R16D20EePx2AHwFp-8tChMaW4uoTTdpl7eVnxtgGUPgMKOjHdQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=JDcbNwxesRsN7L83UB_sKEaxiGdS8MBxxauY_IzMtTZYOKvUVryZJ_hf3e94S0TLbF_HNpGS1FxmrYdoexbvRIvzms_N6WFQ2oKukRL9U_cg38GfFR-8vS266slETYYraJGNjLkEzMht0EWMtUoxhCIpt2rodPwuy-B6Jjd_wx6MO-B0aYXX49FzrilRI-MS7q5jpAW_G0xw9wHldhhd6iKmqjOcK7oSy_cGqAb7wDkvrIXOHod17aXD7fg3h9XzIiYBwhuOrNvOhTQE41KsQmp_cfi7jmGby-R16D20EePx2AHwFp-8tChMaW4uoTTdpl7eVnxtgGUPgMKOjHdQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=nV9-yx3tsevqoVVeT2fJj1J6OMACwfhMFpqwsdoyg0IOie2dP3Sm4FC3O4_7HinbsGdKNDMuX9-ZktpE2E6-GwMoijfs36Td8w7TabOGEZ4cMiZZef_cvIENIrGFSBeA9azWutVlzhMyEEel3AZJzliRz_GkUUR8w7zbEGhJ48743cUB8Mw8OvurkiGE4eCvpnXfdKQ3n2SfsMTuTDEmW8SMWS-5pzZCVVsHRPEijlNh4gsu3UUzBQ0ZhYyJO3AdNaKo_4oIxSMc4fv5XkA3FhqfJz7vvT7pqK5vxapQiMoQsEI2niLSqhFTDDeRSXhCWBuIJmnlexmybOME-NaC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=nV9-yx3tsevqoVVeT2fJj1J6OMACwfhMFpqwsdoyg0IOie2dP3Sm4FC3O4_7HinbsGdKNDMuX9-ZktpE2E6-GwMoijfs36Td8w7TabOGEZ4cMiZZef_cvIENIrGFSBeA9azWutVlzhMyEEel3AZJzliRz_GkUUR8w7zbEGhJ48743cUB8Mw8OvurkiGE4eCvpnXfdKQ3n2SfsMTuTDEmW8SMWS-5pzZCVVsHRPEijlNh4gsu3UUzBQ0ZhYyJO3AdNaKo_4oIxSMc4fv5XkA3FhqfJz7vvT7pqK5vxapQiMoQsEI2niLSqhFTDDeRSXhCWBuIJmnlexmybOME-NaC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
