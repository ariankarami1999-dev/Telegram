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
<img src="https://cdn4.telesco.pe/file/kQTnWz9_dPFhiQrfnjHw1dBVLYTjOAZkO1Fo8TtMqbHd5O-dkMHJL9qSQTxl09qB2jKIByRpwSeekQDXo93iTg6CszYrgOUMNyC7ZC5e0Ja-VZxTL35_RRg1uYjOcTd6ZuXPU8elYLqkUQgbeTboSW8-GbOpD-cFwkXMZrDKfcQUTWIM7zS2MvUBhhKlSAKs8YsTeMGLZFrQOJzmxOs3lQ-ojPRB8Ye2ZgQyQ000nvfuNaOUXxmbcIUwuQbBtQXmbaj6QCSxnshHM2Tu3CuNK1Urk7L5hfPKC1DuwnACUWLy9MMaFGjkKmgk-p-sIjfrZ0B9cWtdHYsNCBBkKrlo7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 17:46:37</div>
<hr>

<div class="tg-post" id="msg-455888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbbm8NQ-cLLvqXijWrf05H8ChWnz0ohyvAHeNdBBRlTMLns5_grgosFDKTYmKt62Q8-K0UP06PJbvIp0DXRfF7JPBsd5NSc9cVxMK3LN63RRZPzs3GhgoHyZ5E8yBKVBpaGYYaO-aPjUrp8DzdWYy3HVtjEV0G9APhdCoPrFtxrYvMODC5FsmnwYewbtW5rqjTO7CR_Q0nPMxQ_jZLhFMfhohtK7sKTC0OvWdGLf-YMVaKyZV0EB9mc1IgnPT_08-DcZWMV7pOi_gJTjPTao2OuB4bFi09upyVVxnQtxYLSSoEFWxdsgzpbnh4XnVheP7mXzPsqi3Wsoh5E7YcT4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای ظریف پای برجام و کنوانسیون خزر
🔹
اگر درنظر بگیریم که نقش طیف اصلاح‌طلبان در برجام و پرونده هسته‌ای‌ ایران تا چه میزان پررنگ است، عمده مسائل مرتبط با کنوانسیون خزر نیز با یک درجه پایین‌تر به این طیف مرتبط است.
🔹
اولین مذاکرات پیرامون تعیین رژیم حقوقی دریای خزر در دولت خاتمی صورت گرفت و نهایتا امضای کنوانسیون اکتائو در دولت روحانی بود. حالا هم که دولت پزشکیان لایحه الحاق ایران به این کنوانسیون را برای تصویب به مجلس فرستاده است.
🔹
اما lمحمدجواد ظریف نقش عمده‌ای در مذاکرات کنوانسیون خزر در اکتائوی قزاقستان داشت و اصلا امضای او به‌عنوان وزیرخارجه پای کنوانسیونی است که به‌تازگی از سوی دولت برای تصویب به مجلس ارسال شده.
🔹
در روزهای اخیر درحالی‌که رسانه‌های عموما اصلاح‌طلب با آب‌وتاب فیلم صحبت‌های ظریف در رد شائبۀ سهم ۵۰ درصدی ایران در دریای خزر را منتشر می‌کنند، خاطرات بد مردم ایران از برجام و آن همه هیاهو برای «هیچ» این تردید را ایجاد کرده که مبادا آش کنوانسیون خزر به همان شوری برجام باشد، کمااینکه آشپز هر دو نیز یکی است!
🖼
اما آیا خاطرات برجام تکرار می‌شود؟
اینجا
بخوانید
عکس: محسن ونایی
@Farsna</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/455888" target="_blank">📅 17:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1014712f2.mp4?token=MbzQUCzdHYCO8hbE3OMDrWx2sCC7rXJVM1vqe8SOHKdIJn5QV6TqsXCyYF7BNoowQK92rPLje5jyr4rt8_vN2BAWJOuMw48ouj3muvul9e-BGjAZ3HjeEoahk02kF9oPkQPlxdQdXS2wOFvMZnCHfo4PtuHNug5Fa8q73kQ3RRIdx3CLb4458CFgOZdGJE4qzkn-Gm4SgwAX2I7xzUVl_qyxfSo7o5gU96V-_uWHxDF2CfDNYnNH3pXxEqcomZwkXuXF_7QKlc4Wwno_vXAwuesrxoehLo-EmCpl61aU5Hnv6NsPK7YBzfGYn3RkKKHeVDVIxN1fQ1zD4oz_14Qzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1014712f2.mp4?token=MbzQUCzdHYCO8hbE3OMDrWx2sCC7rXJVM1vqe8SOHKdIJn5QV6TqsXCyYF7BNoowQK92rPLje5jyr4rt8_vN2BAWJOuMw48ouj3muvul9e-BGjAZ3HjeEoahk02kF9oPkQPlxdQdXS2wOFvMZnCHfo4PtuHNug5Fa8q73kQ3RRIdx3CLb4458CFgOZdGJE4qzkn-Gm4SgwAX2I7xzUVl_qyxfSo7o5gU96V-_uWHxDF2CfDNYnNH3pXxEqcomZwkXuXF_7QKlc4Wwno_vXAwuesrxoehLo-EmCpl61aU5Hnv6NsPK7YBzfGYn3RkKKHeVDVIxN1fQ1zD4oz_14Qzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در کشتی‌سازی چین
🔹
درپی آتش‌سوزی یک کشتی در کارخانه کشتی‌سازی شهر فوان در استان فوجیان چین، انفجار شدیدی رخ داد که تاکنون دست‌کم ۱۰ زخمی بر جای گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/455887" target="_blank">📅 17:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc4OaqNGE0oqyCeWTVa0E3CPiF8YNufaDliWb7YUREYYkHFxk5KZ5GgoyaVQ8kk0jcNCZRSgim9or_Id04qgW3opA7LhtXwVXnr9pRYqYRyx4mAfvm7hDYgluc0QnuG0SxZ-y3s04cP7xX6sDvKQaflMILssE4XgodhumJOsYLQ0KcDg6Cs59rVZn6wESKSXVfFESAHLsJ2Bk_LsIRYd1k_Q_CyxSvbSZQCefNx5BiGqmFe2QwC38LqlXY2u3xjvjXyV1f8zaH5zVt9mOFam6sH1VCc9VYxKfYqLMcGt3B9-Iv3LkuYF39g_8u4KWEVKY4wHuh_02zbgszJVp1OPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش الحدث از ضربات انصارالله به مزدوران سعودی
🔹
شبکهٔ سعودی الحدث: درجریان عملیات امروز انصارالله در منطقهٔ العبر، ۲ نفر کشته و ۱۵ نفر زخمی شدند.
🔸
پیش از این نیز یک منبع امنیتی یمنی امروز گزارش داده بود که درگیری میان نیروی دریایی وابسته به دولت مستعفی یمن و شناورهای انفجاری انصارالله در ساحل غربی رخ داده که منجر به انفجار ۲ شناور شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/455886" target="_blank">📅 17:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455879">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv7obRQUNE-ifk8fPswHuk6BY0wivss2TLMt3ZuNoKa1oqLUUIibJ3p3fm-q4l_mrqxtlMbxdBDWk-NpA4AsLcZMLRCU4tzqH33fxeS5s3IRIu4UWjLyceZaQKgcYMR33VDuByWhiLXvvRR2T_5S6ihzjLyJKL4gyCxnCM5nhCSgUfs8kvObn-2pXSEqpJpD1lh9I35ElfFCUhqH39slo6NtKyi5NetbskehrpZBrp7BFwV5L1WdFqDEbEzFs3ddDJMHXDa1_FuJjNUXM-cSkDoKlLuZ8eHtUXx4R5MxwjuhZye43jWapgWZLg-Y4PWVp34rdi6wMEXHVjDGKZjnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Piu6md5zE56KoyW_8AlTqtfXDphFXo5mrXbQcSzgg9Hc80zDbEBWQ3B3ZJ7rWbeBsdQ3oxcTZDPPdgCBaQOeyuAn_z5kJavQaLI5unEdCgDAdQYcDM19P-Ps_3Yb7oDJY5Xy9mM5dNU0mXONZhSDWe5WJPfDsHg0EtB_D_fKv1TrI9LMOyUarglB6jgF1ncJFuvU3cXwL22qHozOl57zVaEAzRnuCikhI-noSiw_CS9EPyx0PPZwENmz5PbuFiIGCdJ7Chr4KjuJD0q9psGG3iORRlbs-tSbXkSeD7Agr39EuBZzymdzV8UORmfPvbOP4IgubJhPB1LVOuGavVsSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMR4KpKNrk49EQ-hlUPFjAcxh_rtUbOsBnho3X5Cn8xe5LJ4F8st5mnmRKlNtDu99bGHlCT7aQ0_C-Ua4QmzPZ2mf_Sx--1fEuTmnDPdVpxWNRYgvotuPITEDEQr0VGUt2fLyDM7AG8y5tK5CcfGoM4G20eAB1dr3JV5G20jeNjiDrwx1b_RLNpsOOWqe9agkmj8UcID8JpXi8NQyc9Jv_h97x-Qjdu8Jc0GCVo15EPelDB8y8NaIkxEhu_DmfvYV2It3TZPjz2ITgLd_85mIBsG6SLYjmryclEz8B5sqyR2Iuv7sPzgnyBjUtSIG3o2yebAkN1SLCIjOxK6u7PGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxXtoeJNn7hpbroLtzqRMThbfVL_OWC2rUaYpZTCsEV7FOG3vD9zKLP_0nkI7jSVs5J3yhjoUi2oUegGCNLNzl2BiPLtvbLs9HYLJrlH707RU7ChjrHGOTMFzDUjAkJETinaREq_7nJitZqE69H41NLXv-Qwm7OXxhsCSwHei9AmrSyu4LtQRrnER75WIS7zyi-ZLryPppmPisSjOCzPZVPkh-SowDu0zTRiVVxgeecgXim6Y-wtmQ5l77xk9Xj7QZD0wO_PtfF5kEXOh48updrUzHgQ_uu-iEVDqx9C-qx8cAtUgH0aaV7q-LyfZX0CCvPr5bDD1WaHFolMuHlq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRe3qyu7m1c-p1jyomy8F9z_dHIbh5xt77lP0id374157fAcPb-t07JENmTirtPRR5jQhdEvopZk9KZlrpNWmQC4wi2gWVGLOuWGHrxZDcsDZIueiuwhLGM91QQuaO1WTZMh33vEB5keb3p7qe44QPYEdd_gep3hCl3xZLfW-s34Unhj0CvsDhYsgriOwjarMnHqoGzRhgJZS2QfwcOout71UJIf_pitg5MC1WAz4GgI2CU7rKHB1he3lSJBCmvNOPWiN2qGKv6KSQm66oJ00c6MKuUvvo-9NWmxB-vJZ0dzVMUjq1tYucEfjbO33AXp9cTsn9L0SZFeDYVVXmJjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cx0y7_-FaTgd92kDhY2cRxJyG3R5Wyy1zqBIx7Eeqtnoqhitt6dJjy_tGLilyxNhih4cfYbSjpQp2QrVbrUltbbBQtQ2S2-XCIsyj7A9f3IwX72WxLAWfLe3upKZhEsV-Q6F3D286I-_1VLpSnjSrAalakjd0BDqJPaKmeQig7bhsRBLfjNJuxplK2jmEjyvnjr2j_BTcC4jEzwY5ZnGDszmj9cmBIG_XDGnBYAbWjfBfGZDQlZe54N6_wDUeFuLAuT-gqshPEHaT1ecKDmYAlS2SV55drxTwF_Uxkfdo3tN_C0d5WoFX6Q89HLCRP2HTjy03FUMb_TzuGN5u3qbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krow-iIheicwE84P7b0HbUI-Izuec_ZuvKw1PXgFWEyqsbjuTilpwuQhCG6lWVBzFv09iEbcy9HzcGmcXCT-cZUKJMJUYA-u7DnVKBFHu_1zkR6OrphvwH0e9Okr9Uh3sl8-_gtONHYrOunyvsINdLBEfOuN1xR_PomrROziblYsEe7Mi19AV-gAaJlpD6qL1Bd8gbqm7YuFx1kW8NctJBCFeUTnLfkwJd6Zv9bSaQ8VYp2md59_cMmZCapCRV3qhWx5wFKpE8-Bb2ngPvQdFIsV_0HP61bXF-24IXNBv7deWmkOpXczKn9YPRgZuehxhtk6CG2zzEga59DRvykZmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
این‌جا تبرک‌خانهٔ امام‌ رضاست
عکس:
ایمان جنتی و محمدجواد مشهدی
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/455879" target="_blank">📅 16:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455878">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704533da75.mp4?token=QJx46blTSviSR5fAvZhphPls6N_QxoddXSJqgyN3X5m8ACr92LOTTOo1mKlf16JXlQgt3IFqZothRGaCnDEkeCPwTQX0TkCSYZOnSGKynlgnFDK2aNxFRd8PiA7Ubv9ogYiPpqo5F16Sv39VP6l0tRIsjuRLew5kmiMOk1Vl0_CslvzSo0e5VwY-WCMgYb8fTIho1-OJ479xzTB00kKAu0LoqGy_0VxHAZKHNTTtpHSLWrzRdwIPqHGWq52j79g5pkNHNFOQYcaX7OPg-inqx9IAr_CZU3kpyhODI4MuzqEekc5SR5D-B4UtMImEsNzcDaHkpSP7V9P-W4hyzK7IwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704533da75.mp4?token=QJx46blTSviSR5fAvZhphPls6N_QxoddXSJqgyN3X5m8ACr92LOTTOo1mKlf16JXlQgt3IFqZothRGaCnDEkeCPwTQX0TkCSYZOnSGKynlgnFDK2aNxFRd8PiA7Ubv9ogYiPpqo5F16Sv39VP6l0tRIsjuRLew5kmiMOk1Vl0_CslvzSo0e5VwY-WCMgYb8fTIho1-OJ479xzTB00kKAu0LoqGy_0VxHAZKHNTTtpHSLWrzRdwIPqHGWq52j79g5pkNHNFOQYcaX7OPg-inqx9IAr_CZU3kpyhODI4MuzqEekc5SR5D-B4UtMImEsNzcDaHkpSP7V9P-W4hyzK7IwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقام پیشین آمریکایی: در بن‌بست ایران گیر افتاده‌ایم
🔹
مقام پیشین وزارت خارجه آمریکا تاکید کرده که رئیس‌جمهور این کشور گزینه‌های مناسبی در قبال ایران ندارد و در یک «بن‌بست» گیر افتاده است.
🔹
«هدر کانلی» عضو ارشد مؤسسه امریکن اینترپرایز و معاون پیشین وزیر خارجه آمریکا در امور اروپا و اوراسیا که با شبکه بلومبرگ گفت‌وگو می‌کرد، در پاسخ به این پرسش که با مواضع متناقض ترامپ درباره مذاکره و همزمان مطالبه امتیاز برای آمریکایی‌های کشته‌شده چه باید کرد و روند کنونی در چه مرحله‌ای قرار دارد، گفت: «ما گیر کرده‌ایم. در دو هفته گذشته در همین وضعیت گیر کرده‌ایم. رئیس‌جمهور گزینه‌های خوبی ندارد.»
🔗
شرح کامل این گفت‌وگو را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/455878" target="_blank">📅 16:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455877">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4ebc018.mp4?token=lwIqZtxJMLmf_L8eVjhryp-7wpnvtHGf6OBtXVp4SAy8-b5m-UyQ9b10HPlVIdpmkdpe1kVBuPKJfwX1ou7DnTEaPW81o6Lsd0hYIvcbP91sIj0dl-XvduUHXWFYDXLv0UoFFceAcGmRmlhDHA_ogtpCH1AL8q2y8Id3jDfOqJtoI9YTIIszQW1HkeeYM5feU0pkj81Br05sYwpIoYjHBPNIxDwBboxD-aeRTa1XDwtc9vwbECJJw7iwMfpteLn6WjG0XurThtMjcARWTMHNU5M4jk5ixahcynMkZtDBvTApXN0cyOoP8pzSbVXX2LBMdnYlE7vBdS9wnFWuLnQwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4ebc018.mp4?token=lwIqZtxJMLmf_L8eVjhryp-7wpnvtHGf6OBtXVp4SAy8-b5m-UyQ9b10HPlVIdpmkdpe1kVBuPKJfwX1ou7DnTEaPW81o6Lsd0hYIvcbP91sIj0dl-XvduUHXWFYDXLv0UoFFceAcGmRmlhDHA_ogtpCH1AL8q2y8Id3jDfOqJtoI9YTIIszQW1HkeeYM5feU0pkj81Br05sYwpIoYjHBPNIxDwBboxD-aeRTa1XDwtc9vwbECJJw7iwMfpteLn6WjG0XurThtMjcARWTMHNU5M4jk5ixahcynMkZtDBvTApXN0cyOoP8pzSbVXX2LBMdnYlE7vBdS9wnFWuLnQwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانه‌های ضدانقلاب آب‌بندی شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/455877" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455876">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
یک شهید در حملهٔ پهپادی اسرائیل به غزه
🔹
منابع خبری گزارش دادند اسرائیل یک خودرو را در منطقهٔ «الشیخ عجلین» در جنوب غرب شهر غزه هدف قرار داد که در این حمله یک نفر شهید و چند نفر دیگر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/455876" target="_blank">📅 16:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455875">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff3c4526a.mp4?token=Kr8U8QRDdqpSlmQRYMegLOD-9b6Bk2TMot1qT2-gUeFcEbKIG-w-lLUb7bd14YbTiL9301mR4t3Ga9qDg-gQLLXzUqMkJPQy7LWK2WLLQ1LXD-y-mjBcEsqDIjkm3LbH8qJn5s9LmelHVuhV6fkTsNjtDWIWEG1AN0EKoPXkd7HNm6DjGiEQ4iGsvix9mrBKw_Pf3VYls9zABfIC0H9z3SgLBryzIqGwDOdbhwjCSgt7XHL6hD3WE4Jl8R-bnGUHKKkC3tLvZiiDrsSj5aI-EONuqdFo-ZcTODocXYQFJ0rCVJCWYxZZrqdS6Hvwv0s_I5Xx6P5F0eGyVoArAB1d-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff3c4526a.mp4?token=Kr8U8QRDdqpSlmQRYMegLOD-9b6Bk2TMot1qT2-gUeFcEbKIG-w-lLUb7bd14YbTiL9301mR4t3Ga9qDg-gQLLXzUqMkJPQy7LWK2WLLQ1LXD-y-mjBcEsqDIjkm3LbH8qJn5s9LmelHVuhV6fkTsNjtDWIWEG1AN0EKoPXkd7HNm6DjGiEQ4iGsvix9mrBKw_Pf3VYls9zABfIC0H9z3SgLBryzIqGwDOdbhwjCSgt7XHL6hD3WE4Jl8R-bnGUHKKkC3tLvZiiDrsSj5aI-EONuqdFo-ZcTODocXYQFJ0rCVJCWYxZZrqdS6Hvwv0s_I5Xx6P5F0eGyVoArAB1d-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طعمه کردن خبرنگاران در ماجرای فرار ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/455875" target="_blank">📅 16:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455874">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جاده چالوس و آزادراه تهران-شمال یک طرفه شد
🔹
مدیرکل راهداری البرز: تردد کلیهٔ وسایل نقلیه در جاده چالوس و آزادراه تهران – شمال مسیر (جنوب به شمال) تا اطلاع بعدی ممنوع است.
🔹
ترافیک در جاده چالوس مسیر (جنوب به شمال) حدفاصل بیلقان تا پورکان و مسیر (شمال به جنوب ) حدفاصل ماسال تا مکارود سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/455874" target="_blank">📅 16:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc49227da.mp4?token=QIBKbwOasiOaCxUYr_clj8bzdo1Gs-VmhXql7RvB6h7niYu4RBUftOiWmfXo4-XJcVhQ2vu6mrBA9Lgsf6skpoCnDQL5FNHkahqzztCz9aRG3fr3-9XtlgDDOAVPb-A8rCgqqoLkoefkorzu_xMgo3SAk0iY6i_U0JQDyn1JM5zM-CFY3oFlNC5LiR0bt_cG6wnbHBxMVpRtm-uyZ5vsduU--IBdVZ8NTynJDFOhbSJeCK0DPfhZ1pfg-xA39t1FR9gkZUlwEKR92KCTFBNAahIMpCzoUoerR3LhjlDotjDv_RrQbEI1fmdzwINsAVaRembMVt9PBePDQfIQIdntKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc49227da.mp4?token=QIBKbwOasiOaCxUYr_clj8bzdo1Gs-VmhXql7RvB6h7niYu4RBUftOiWmfXo4-XJcVhQ2vu6mrBA9Lgsf6skpoCnDQL5FNHkahqzztCz9aRG3fr3-9XtlgDDOAVPb-A8rCgqqoLkoefkorzu_xMgo3SAk0iY6i_U0JQDyn1JM5zM-CFY3oFlNC5LiR0bt_cG6wnbHBxMVpRtm-uyZ5vsduU--IBdVZ8NTynJDFOhbSJeCK0DPfhZ1pfg-xA39t1FR9gkZUlwEKR92KCTFBNAahIMpCzoUoerR3LhjlDotjDv_RrQbEI1fmdzwINsAVaRembMVt9PBePDQfIQIdntKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هت‌تریک طلایی وزنه‌بردار ایرانی با شکستن رکورد دنیا
🔹
حمیدرضا زارعی، ملی‌پوش وزنه‌برداری کشورمان در دستهٔ ۹۵ کیلوگرم جوانان، در رقابت‌های قهرمانی آسیا در کسب طلا هت‌تریک کرد و رکورد دنیا را شکست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/455873" target="_blank">📅 16:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=IMAr14nGiHP9C75Zvg5K-CiVgKUmGhFh8Fk87_ov7MPrwVOR5z5WeVCPM3lnE5Q9KggQf8W9ejd-rxzfWI85jb4jfDZYsCXHnezIJSA0KjAZ0yeuNq3xo4dey2Eu-gYkkfHxByROE6-UxXDWeJpQiDFM_kO4d6Jyoqjk2S7eWuPHrLUpsj3hUdsNOMl8rxv7xy1F71ThdiTWdHlNrfhFkv790yLkkhoTHKRhwZW7RGfK1gI6CM3I3lC-76aLyfQK2L-yTfX4M9K4I9u30d5fPWexF2GA7ZnWGfz7cu-X3Y6_lh1oJqjZkFM0bi0R1EHKr8Kn9vHX-Q0aYp7GkaWGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=IMAr14nGiHP9C75Zvg5K-CiVgKUmGhFh8Fk87_ov7MPrwVOR5z5WeVCPM3lnE5Q9KggQf8W9ejd-rxzfWI85jb4jfDZYsCXHnezIJSA0KjAZ0yeuNq3xo4dey2Eu-gYkkfHxByROE6-UxXDWeJpQiDFM_kO4d6Jyoqjk2S7eWuPHrLUpsj3hUdsNOMl8rxv7xy1F71ThdiTWdHlNrfhFkv790yLkkhoTHKRhwZW7RGfK1gI6CM3I3lC-76aLyfQK2L-yTfX4M9K4I9u30d5fPWexF2GA7ZnWGfz7cu-X3Y6_lh1oJqjZkFM0bi0R1EHKr8Kn9vHX-Q0aYp7GkaWGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان وظیفهٔ فراجا: مهلت مشمولان فارغ‌التحصیل غیرغایب برای شرکت در آزمون سراسری تا پایان آبان تمدید شد
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/455872" target="_blank">📅 15:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b50fef7d.mp4?token=s8DeTrwmBkJycR2ltG0AylWKH3FktgT2peTDhkeIZN26-A1iQVErFjLNz-ExndDyDhYhJhNP1GIlc17S85eo0GAkZTwE3B1MSULv0gbqPx1ZPZx90cno4LapXzsojvOEsAg8zzJ-atmq4BsPj8llqC2wjscs4edexePwHqFYMrHO6t-6UzYSMrIBlJVrTN1KK-4rDpgbiBF_C9f9GEaOLxQOz0ZzYpRmGuIBWU8rpwH1iadmkoi8G9r1BUN3Yq-OD24c7t43tc9MWBlqtV0Ws1YeUQkMeUeJvU_R9Mg_jUgbf2xqrKVnZP8h1bCAzley0QJx1oFc-zUOmCdIoD_Zwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b50fef7d.mp4?token=s8DeTrwmBkJycR2ltG0AylWKH3FktgT2peTDhkeIZN26-A1iQVErFjLNz-ExndDyDhYhJhNP1GIlc17S85eo0GAkZTwE3B1MSULv0gbqPx1ZPZx90cno4LapXzsojvOEsAg8zzJ-atmq4BsPj8llqC2wjscs4edexePwHqFYMrHO6t-6UzYSMrIBlJVrTN1KK-4rDpgbiBF_C9f9GEaOLxQOz0ZzYpRmGuIBWU8rpwH1iadmkoi8G9r1BUN3Yq-OD24c7t43tc9MWBlqtV0Ws1YeUQkMeUeJvU_R9Mg_jUgbf2xqrKVnZP8h1bCAzley0QJx1oFc-zUOmCdIoD_Zwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: هیچ کشتی بدون اجازهٔ ایران امکان تردد از تنگهٔ هرمز را ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/455871" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455870">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpDJEZCkY8Xpg-5l65GWNzUTkScuPsqA505nvUCrYG8rSQyAEH8fkKgVk2m87XD6KKirk7fYrJuJ2Ms8eTQVTy6imZSNrOjyCO8DE7JmJF13uoTuueiFNae0cdl7961Q5p27kK9MUfYdzpHxNcCxYslgKDDq61-pAA1Ckw20xFMYYynJ3bK-FNyDUqzvy40ovJNYXF70Vv_mEFC_QETErCDGIWyww7SvbXYvWrLiOlX3svklajPUTcNBEPq4AI3Pbm-F2D9i4y2JBrPdjW4GO6YgWbrT4pg9uZcsXWvptijIqzTod1tC7V3tIIk_kDeCAWVPqSZPEp7aglHJTIhWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دلنوشتهٔ خاص مهران غفوریان؛ خوشحالم زادهٔ خاکی هستم که امام رضا دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/455870" target="_blank">📅 15:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455869">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67b734a3e.mp4?token=JIptjvU3G8LgMFBWRNF_IJ-XlnMUcFUKFxZvKuBq0Gz_8FMQmOnPA78CRQHVJfNjWfC_57_Jn6hG5wnUtoLEgKbpuY3kDVKMz204Qk874qIihb4ey5QU5lMYm2Sj_cYDZo9qeCbvuoZUz22BCAZ0QOBc6WHNSbsgDMEPWyS993RuKbM8Sx9MOqsoeGBLtniYfrwd-NO8kl2Gz8FHlmmjfSzZg6Ou0vfOYHxoDI2plRLTRXM7UcMnfw2o6PSmgP7bk7kV0sbDZMipwLa3atdkkZDgSpQqyBb02wpvbpB-fKs73v6ZoFz6kJN2ydDQZFPevAA-RuS-L-Z8lUplO26EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67b734a3e.mp4?token=JIptjvU3G8LgMFBWRNF_IJ-XlnMUcFUKFxZvKuBq0Gz_8FMQmOnPA78CRQHVJfNjWfC_57_Jn6hG5wnUtoLEgKbpuY3kDVKMz204Qk874qIihb4ey5QU5lMYm2Sj_cYDZo9qeCbvuoZUz22BCAZ0QOBc6WHNSbsgDMEPWyS993RuKbM8Sx9MOqsoeGBLtniYfrwd-NO8kl2Gz8FHlmmjfSzZg6Ou0vfOYHxoDI2plRLTRXM7UcMnfw2o6PSmgP7bk7kV0sbDZMipwLa3atdkkZDgSpQqyBb02wpvbpB-fKs73v6ZoFz6kJN2ydDQZFPevAA-RuS-L-Z8lUplO26EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعا مدارس امسال با رنگ‌وبوی عشق به رهبر شهید آغاز می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/455869" target="_blank">📅 15:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOuMnBg40yypmuYrUaGeLr7bB_5FCUSoErFTuXXVVLatq7F4LhH9eT34E4meW6_sw0E6zM5CajWj4PhQNdHqTeKmgZrn7BRiG30QUT-Aj0emgGvCH_95msuvOVIaMSJ8WDtZfOrPsEV4C1LW6qCMWbbr5PsqGi2j8F4OJaI0iMdI-cY5EPA8ynP1pL0OSmiyXwDTYzF_KSPduqIjOGD3W4KMk4K87E3JJmbciq_o7w8BDRPQrAw4U_TKuPmV8i_8SNurH6TTxunnSMSk2PBpaUMZPtUQ2QpoTOedLcz2pVGTr3BxU0L_o4zB_YE50SVjI1X4TjLHntHbVuktFUnthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکسازی آلودگی نفتی قشم به مراحل پایانی رسید
🔹
مدیرکل حفاظت محیط زیست هرمزگان:  آلودگی نفتی دریایی و ساحلی در برخی نقاط جزیرهٔ قشم مدیریت شده و عملیات جمع‌آوری آلودگی‌ها اکنون در مراحل نهایی قرار دارد.
🔹
با تلاش نیروهای حاضر در منطقه، آلودگی‌های مشاهده‌شده در جنوب جزیرهٔ قشم تا غروب روز چهارشنبه تقریباً به‌طور کامل جمع‌آوری شد و بخش قابل توجهی از سواحل آلوده پاکسازی شده است.
🔹
پایش سواحل و مناطق دریایی همچنان ادامه دارد تا در صورت مشاهده لکه‌ها یا بقایای نفتی، اقدامات لازم برای جمع‌آوری و پاکسازی آنها انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/455868" target="_blank">📅 15:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سفر هیأت امنیتی بلندپایهٔ عراق به عربستان سعودی
🔹
بغداد الیوم: یک هیأت بلندپایه امنیتی عراق به ریاست رئیس دفتر فرماندهٔ کل نیروهای مسلح، به منظور بررسی شماری از پرونده‌های امنیتی و موضوعات مشترک وارد عربستان سعودی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/455867" target="_blank">📅 15:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
کارشناس بین‌الملل: تصویب لایحه خزر به تمامیت ارضی کشور خدشه وارد می‌کند
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/455866" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d921022c6b.mp4?token=bn-D8hgVUzx4mNg6rtFTTi0MGmmRDq3cuOFcuDigGKI5k7ftNVzoGa8y3yVHVrphQmAj-7fB9UpBl_sDPu2_U3bIVwg2bbQGbdx_D_xeKiJ1kw_D_ptvhaQe9e1k6esPS2pApLWYR2n6PirZUezlPNUynnnQ4LNur5ue33I9uqTqIpMT7goWTLzypD-TfsXVCDcZm3bKB_vGXL3ZY-n71fu47m5ekHVQKj90VMtBVxowRi_HWSSOPF-D-VqMO63gGYIxRL71S8YUk37VF4dalr0ObhD3Y58QGuI2tz_vO1MHyydQbzPrXOk0kJMk_MzFQjGGAqg-_5EMZ5bBTymVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d921022c6b.mp4?token=bn-D8hgVUzx4mNg6rtFTTi0MGmmRDq3cuOFcuDigGKI5k7ftNVzoGa8y3yVHVrphQmAj-7fB9UpBl_sDPu2_U3bIVwg2bbQGbdx_D_xeKiJ1kw_D_ptvhaQe9e1k6esPS2pApLWYR2n6PirZUezlPNUynnnQ4LNur5ue33I9uqTqIpMT7goWTLzypD-TfsXVCDcZm3bKB_vGXL3ZY-n71fu47m5ekHVQKj90VMtBVxowRi_HWSSOPF-D-VqMO63gGYIxRL71S8YUk37VF4dalr0ObhD3Y58QGuI2tz_vO1MHyydQbzPrXOk0kJMk_MzFQjGGAqg-_5EMZ5bBTymVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم شاهچراغ(ع) در سوگ برادر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/455865" target="_blank">📅 15:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e9ad1f54.mp4?token=Mo7Dxt0vtYWLbeaNnu2B8jk0MBNSWTv_5TFFlyALB8TZmMEAvkxrqzDdqj0qvrMOU7l6p8WSSm92EcMM3ip5B3NGNSA-5_KjYin7xmf5v92ZybeMNzmCiwNf1fpg_VS2-HuTe18LlnVR1JICK6-tyFDAthcX_WO8huL9aw2qo_7HMOgq0uqDLheZ3W09wASZugGCZP5o1dVJE1dBfXe0JVCcbttiBsdajIhbyAxlAClew-48vxv8omLpzfdEffUegykSE7_NdDUkimuFsrIty2KvKLAKg9x0inavJMvjekF1yeQ7wQjzKv5vY22oKu2jOUvzgYmfMwafkniTr7yclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e9ad1f54.mp4?token=Mo7Dxt0vtYWLbeaNnu2B8jk0MBNSWTv_5TFFlyALB8TZmMEAvkxrqzDdqj0qvrMOU7l6p8WSSm92EcMM3ip5B3NGNSA-5_KjYin7xmf5v92ZybeMNzmCiwNf1fpg_VS2-HuTe18LlnVR1JICK6-tyFDAthcX_WO8huL9aw2qo_7HMOgq0uqDLheZ3W09wASZugGCZP5o1dVJE1dBfXe0JVCcbttiBsdajIhbyAxlAClew-48vxv8omLpzfdEffUegykSE7_NdDUkimuFsrIty2KvKLAKg9x0inavJMvjekF1yeQ7wQjzKv5vY22oKu2jOUvzgYmfMwafkniTr7yclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهدید صریح وزیر جنگ آمریکا: حملهٔ نظامی به کوبا روی میز است
🔹
پیت هگزث: اگر کوبا مطابق با ارادهٔ آمریکا پیش نرود، از گزینهٔ نظامی علیه این کشور استفاده خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/455864" target="_blank">📅 14:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8843ee8d8.mp4?token=ODj-sg_WmfnxejxjvIOPds0Z_x6IDT_j57ynnXvG0wWmCdDuTUIguOrR83lG3Z4IBpNXDSugqrqFCPaL1H1Xf6_pMH1SpZuoRzvhMAZr70VQ66m0cCDvW-wbM1a_sPjHVzktM7vybuixte3BcGe6qME9eTr6s3v6TrcVb57GDxNLTCh4CY1TwE2Ry3uuLSLlOAxgCLqKxBrGUToU294ruOfnLpCOAdGG38MSn3hDYaPAKqDI_fGinqqmHslPiyzT1df5aNx2fxLw_XT7YSrZEFuxWXk6K1y8IWF7EHxpkLECZ8ErWe2ZFblV54JVMBfiNZXPzWrBYodf1JDg2Mfm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8843ee8d8.mp4?token=ODj-sg_WmfnxejxjvIOPds0Z_x6IDT_j57ynnXvG0wWmCdDuTUIguOrR83lG3Z4IBpNXDSugqrqFCPaL1H1Xf6_pMH1SpZuoRzvhMAZr70VQ66m0cCDvW-wbM1a_sPjHVzktM7vybuixte3BcGe6qME9eTr6s3v6TrcVb57GDxNLTCh4CY1TwE2Ry3uuLSLlOAxgCLqKxBrGUToU294ruOfnLpCOAdGG38MSn3hDYaPAKqDI_fGinqqmHslPiyzT1df5aNx2fxLw_XT7YSrZEFuxWXk6K1y8IWF7EHxpkLECZ8ErWe2ZFblV54JVMBfiNZXPzWrBYodf1JDg2Mfm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: شهید نائینی سنگر فرهنگ را به سنگر جنگ گره زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/455862" target="_blank">📅 14:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455861">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e8c1f37a.mp4?token=kx5SWWCYPRx7vFrggRicUY_FOg2yI43wZsfjo6gQiSRoxDPJ0T2yU7Q-XntNA5tJHsRG7TxiHUpoOEDRbPElUysQybLaOcZTMRNgb_o2Bx9foKChwIyhXELFl_vQg1oYFJUgw0PXBHWguWWvU2bajjNWDlBB_U1QSz6-1E50081rXFPBgdN-wEOmusLHdmI940aKt50lneLk2hZU_rMhQg63ByQ3SqmdpA6z_HF7WRYQD1vf29o7kuajLyGO5iU0tK466LkLqXtxejw6g5iI5eLSt_saMORq7yQrd0nLLbMfTK0hwZPzEFZO2q7nNCSYClqns3YGz4jcCNypilrRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e8c1f37a.mp4?token=kx5SWWCYPRx7vFrggRicUY_FOg2yI43wZsfjo6gQiSRoxDPJ0T2yU7Q-XntNA5tJHsRG7TxiHUpoOEDRbPElUysQybLaOcZTMRNgb_o2Bx9foKChwIyhXELFl_vQg1oYFJUgw0PXBHWguWWvU2bajjNWDlBB_U1QSz6-1E50081rXFPBgdN-wEOmusLHdmI940aKt50lneLk2hZU_rMhQg63ByQ3SqmdpA6z_HF7WRYQD1vf29o7kuajLyGO5iU0tK466LkLqXtxejw6g5iI5eLSt_saMORq7yQrd0nLLbMfTK0hwZPzEFZO2q7nNCSYClqns3YGz4jcCNypilrRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آهویی که سپیده دم شهادت امام‌رضا(ع) به خانهٔ یک روستایی پناه آورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/455861" target="_blank">📅 14:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
تیزر مستند «دیدار آخر»
🔹
مستند «دیدار آخر» به تهیه کنندگی و کارگردانی هادی نعمت‌اللهی و محصول مرکز مستند سوره به روایت تشییع آقای شهید ایران در تهران می‌پردازد.
پنجشنبه ۲۲ مرداد
ساعت ۲۲:۳۰ شبکه دو سیما</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/455860" target="_blank">📅 14:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/455859" target="_blank">📅 14:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/455858" target="_blank">📅 14:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxVjt2GYknQCTfLNT6W8ATpSOuIzw48AtFjWRM5xpyQqlh02KNPNOunMkgmVpwK8qm0W_H0kdNoxhZ0nm0j96qpyE9M9FLrJCMqRCOjgcw8WGR-w4WtQIKyf2FGWB7OJRK0wDrkAUp74-YUgDg-fDRPqpOIFbRzCDARE84JAL9eB7OplnZAsJ_o3Ln1jHvNPvSRbRRFr4iceTYU76HPFs4ir_79uGYwZpJHh8hD0SAJYZE7tuFXHlz5loUVGxIZzocNL8oI_EqFnoSFyRT611t1bsJiCloCzQ_ySpByin6d5JRHEvM9kpZ-yIpojU_lKqEY7wRCqyJ1Mo57MBcVEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس حساب سخنگوی نیروهای مسلح یمن را بست
🔹
پلتفرم آمریکایی ایکس، حساب سرتیپ یحیی سریع را مسدود کرد تا شاید بتواند صدای عملیات‌های پیشدستانه انصارالله در معادله «محاصره در برابر محاصره» را خاموش کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/455857" target="_blank">📅 14:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک باند ۴ نفرهٔ سازمان یافته</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/455856" target="_blank">📅 14:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری خیابانی آستارایی‌ها در سالروز شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/455855" target="_blank">📅 14:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/455854" target="_blank">📅 13:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHoAkR2-v3Nq4hCyXoPJyMXs-Q4DxCkcy0c7Fw5c6bv-EeHkLwHM9345SEfYsZyC-MgJliRkaeHCqIMeIGY87DW9ZgON22BRwLDbkKxbd2Gg_KMIpCoFlLs0gH_IFH4A-MxF8JV3QAuQCI8IxhF_fWvPk0kiZVCFLkVTY7fJOu7vG5Vojg75zjZMJby3TOIoQief2NzUib3ZOkeg5g4kzknYG67NGtd3HZwkxW4nN2plKhLtS8WoX75lcjT4XWFQL10dN6B62Sfe_djnluaON0e-tAPO7mgbGgjqAHjK69_7_IU7gRHhW-kiiVGKO0rGFKA31nLWDdKN7AYesgLVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال بازنشسته آمریکایی: پهپادها و جنگنده‌های ایرانی دمار از روزگارمان درآوردند
🔹
ژنرال بازنشسته نیروی هوایی آمریکا، گلن ون‌هرک، در نشست سالانه سمپوزیوم دفاع موشکی و فضایی در هانتسویل، آلاباما، با ادعان به شکست سامانه‌های پدافندی این کشور در برابر حملات هوایی ایران، گفت: «صادقانه بگویم، پهپادها و سایر وسایل هوافضایی از جمله سه فروند اف-۵ که از ایران بلند شدند و در ارتفاع پایین به پایگاه هوایی ما حمله کرده و بمب ریختند، دمار از روزگار ما درآوردند.»
🔹
این ژنرال ارشد بازنشسته که در پنل تخصصی مقابله با پهپادها سخن می‌گفت، بیان داشت: «این برای من به عنوان یک خلبان بسیار شرم‌آور است که بگویم چنین اتفاقی افتاده است. این اولین بار در چند دهه اخیر است که نیروهای آمریکایی هدف چنین حمله‌ای قرار می‌گیرند.»
🔹
به گزارش پایگاه خبری «وار زون»، این حملات در حالی رخ داده‌اند که در کنار حسگرهای مرتبط با سامانه‌های پدافند هوایی مختلف از جمله پاتریوت و هواپیماهای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) در آسمان، ارتش آمریکا سال‌ها زمان گذاشته است تا یک شبکه یکپارچه‌تر پدافند هوایی و موشکی را با همکاری متحدان و شرکای خود در سراسر خاورمیانه توسعه بدهد.
🔹
این پایگاه خبری در ادامه می‌نویسد: «ایران در روزهای ابتدایی این درگیری به‌طور فعال رادارهای پدافند هوایی و موشکی منطقه را هدف قرار داده بود؛ موضوعی که به گفته کارشناسان نظامی، خود به‌تنهایی زنگ خطر جداگانه‌ای برای نیروهای آمریکایی محسوب می‌شود.»
🔹
در ادامه این گزارش آمده است: «این مسئله این پرسش را مطرح می‌کند که ایران برای پشتیبانی از این عملیات چه توانمندی‌های دیگری را به میدان آورده است؟ نیروهای ایرانی ممکن است برای هموار کردن مسیر حمله، حملات موشکی و پهپادی گسترده‌تری را علیه حسگرها، مراکز فرماندهی و کنترل و دیگر مواضع انجام داده باشند. همچنین احتمال استفاده از جنگ الکترونیک، حملات سایبری و انواع مختلف عملیات فریب نیز وجود دارد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/455853" target="_blank">📅 13:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455852">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی به هنگام ورود به کشور شناسایی و پیش از هرگونه اقدام ایذایی، در سلسله عملیات‌های نیروهای اطلاعاتی استان در شهرستان خاش، تعداد ۴ نفر از تروریست‌ها دستگیر و ۲ نفر دیگر در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ هسته‌ٔ عملیاتی آموزش دیده وارداتی مزدور دشمن آمریکایی-صهیونیستی قصد اجرای پروژه دشمن در ناامن سازی استان و ضربه به زیرساخت‌های اقتصادی جنوب استان را داشتند که قبل از هرگونه اقدام، شناسایی و متلاشی شدند.
🔹
همچنین یک باند ۴ نفرهٔ سازمان یافته شرارت و مخل نظم و امنیت عمومی در شهرستان زاهدان که درصدد ربایش شهروندان این شهر و باجگیری از خانواده آنان بود، در تور اطلاعاتی سربازان گمنام امام زمان(عج) قرار گرفته و به همراه مقادیری سلاح و تجهیزات دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/455852" target="_blank">📅 13:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم نهبندان خراسان‌جنوبی در سوگ شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/455851" target="_blank">📅 13:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljiRCg72t6ikgZjrB36I-1dQm9OBmT5BGY1FDQ85RsMQUvx4mLars6c0IATIwiJHV7MrsEcSefbQJYwEPAbsENRiJ8D2EbqQBDUiM3FgKAZyI7sEtO8AVW3-27zn-SxH7u1ya3EzY0UDuxTO6EOnQEX-i8PLeBTNWeLM3eaZH0BS-CHWSfgojlWDeyZ4pf8GMWWKgFoIChiWi5dfyoE7K7tnU7Q-_wEiT0ffBHXVmcj6wsgDnwPdHW-l3BQNNP-eaurt67bdWRHEF4WAxO2pRNBl07oQ30A089NxrRagxLlx1KaK_rh90hbC2fTnzX4g7KLvH24aQbWgfqNdnYb0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JG03kG2CFpsSw9O0U9gFvQhiiEQtv6AeWhkvMl66QfFOcQnqVdxcAUSw12uAydlj6lpRd95XlhYX0WRBcr85sDWsUVS7S_TQDpOuh5PZHHxnR-P3e1JNbOPPWM7nkhRrlmJS9BZqbkvSdey_qS-wqzEPniFqNmP8fBsq228mpIHul44RJjEjr3zah4Qk9u_1Baz5ARpDCzBmhjrCczq_WP24Sa4L_bhG29oVnGpIfak47DlyscBdcwIHq6jEwBFteM_wfPdKuUzKrYXdyQbh2hKXMesjutlveB3se3htBZKvf64-AX8nQPClfgAzeo7iz0jcCCwtU_Zu2vlBh5f4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmMxMRMxFjB8pG4NRGDPIP4v6VuV0mp0FqoEyOub1At_3usEa8NluyzzRCMrMObhL4E7jkA-DSIr8ZOzS4kXTMmZSKiiasf57UGX9A8d33gI93tYl6BZJ-XtD_u-GZaLjZIThMj-E9PqMdFGSwKm6vPk1VPCpwqLRHm51jGtAV9D4kBorcJq85p_zGC0Sc0g7-Ih11klvlrniPcs9WKTf1_3UoNN8crD5JawYNEzVV7t6fQHeUv9HmoSVGfzWYdTPQBtYVmenvNx41ZEO68VWRtf03s66Fk_nWHz5nAX9y6luQmprLvuzkdb52It8V92xgtcm_VOUy5fg6bLKvOZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2sIXXQZMeT4RUmS6JAL5ddgaS6UUebQDqFXMt28MAtiXLc_gEuv1YY-mYaAnx5v9PIgdZv9vFTHpK0RX5WrdrpKInAXkX4IryQwQOSCIpXQTLf98BLeSEBfC1SHyG-nRlVNLkAkHMalDn8Y4rJuUlKgyTP2JjZE6SN_M_rJ3q-hbNkulFKFYjtQwhb_ybwX2pCfVtTYwNG8cI6M1drVOlXtP4dzphP3U3hC-pAxMK7_Z6Sx81eKIVcL2VBUtr8lA6WF9SyjF6i5jx9cOHKG08MQ_IhC3iRHcXWYiDaSZ1xGMiiSoRANXDGaZcsA6xAZoJRymLmu7Ee4NC_sorPdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvoyBngm1pwJuXfHIwcRsGQXStT3mriXnJqTQmkv4s7SUbklecsaK_FQt5OfEmlKUJFHTe7fERXK-xnwLd9RL9FeciwVN8bZ-tdHeFM8EnjreLOROrCWqFyMaMNtwkdUbEtLZihPOTkv9FqCGMPQtTWNG7da7vtxUNYTjeMkP6wAJgv3yUu1sOc_bscGlDeijqTuKy9aBc6HzB9rrRuoIsrr_vh8dobqkeqq_uumpE0o7x8H4BDuFChMZLHG83eHqvPIIzn8HhqhVDHdUijDPZleTRFoAMFlZYu9EvuAg-ho8_JB3WGuk5cjAtYy6Hfjh9iWbl48MvE7pAAoCF3fdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQpGb27tV2L5dA5qYuzAbVmots9Unq6p8FWZ3IAVAu11h1x5tQgw5kEJNp8UcmBCndh07Clz5UNSZjM0qddBaPIiNtSrQao7MUZucm5uBibyYLuhpFeVK7QqxZnTyUVwp2GrLIyURi0PQ0EcDglMt9BbfSM9jJ-bK8_-xIOsxjaWbbfwbWufOtlYZ92iQxq6eOiN8g2aYF_0LSOKXAeaBbnGPzLTF-Hoc-srLdVyEJJb0d0DjaiPeCBxhw4RrIAwx0jFqOzZkjRMeqOvY0V6fKH-rInF6-rLD9GJTah5Naz2IxOrwjIIEg6UYYgwTkYR5YEB9MnE8oYYXpdGDCqtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVAC8qm4bv_yitBG5cJrXyCq3ySlrIBaAWz-XWkxHdIVbqeZWJC4EDk55Wf3WsL_mHt2H0yGPHq_MK_weavGuMCFT0Qi-F_IhEBgoZiuyg4TErO_ycWXpEAbERe3BgfbKzIrB4n9yfeNwN940ESL4FCZSeqfueto_G1H711ysJvOrxbzfAoKJCLzgdc-ouXl2kgANGMB1QQTZirpL84wbsfS1JJ0ggXJmjIuANypI2zzHkapCDsX0TZ9l5ep0NonNt25FVd-Lb8aYoFcIZhl3XP9X4iXf5Vs-oBCxpKc-IKWtION-Av_Zzwfd0F1g4mfARQc1ptf-DQ1iCr3b7JwqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تبریز غرق در ماتم شهادت امام رضا(ع)
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/455844" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطعهٔ موسیقی «به رَسم کِرام» با غزلی از رهبر شهید در نجوای با امام رضا‌(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/455843" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ صلوات خاصه حضرت علی‌‌بن‌موسی‌الرضا(ع) توسط رهبر شهید انقلاب در حرم‌رضوی
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/455842" target="_blank">📅 12:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_V-7swnd3bKtqkApx0jJH1xPIxnfQTpJsp9LutodVlodgGnNV8symGbsahAIPDfxcbcSPXv77ciRn471RV91US2YAFDwjKQPcBbojqKIVE28BgZGVF14Zk5sQ19LVdTnMOcwSh0EoLM1c-DNNRKdNIa9XnOOinYcjWJcG7lKQkdv4suV42D43n4v9c3k0BJ7l300ow3-LlnOnOaFRq6ee-iesnRp2_m2Gf9B-SaP3Ux7mbcIEMzYsDDoF4-zQp1eLEfexYn7LafLc49ma5FGYTLJAKZ5cWhAyleg8m_jqhToO9uHrXqEMOU0iCBEDD00AXS2YjG_VawrVKYSIAsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVXwB1FHcJFcLAWMBfu0KN_KEoxojtJy5pEnHn0Y0mbff0b_xpVeQDAH4QFKmV2HaYogwOsM2O9mKwC8gafnDbyx2OLGQegfNTw68n-2eTB948b5EIi39CEGBeGzoqzAU_3V8bKKz9g5imDeEqT6zHR5P_EOpaciiC_-J0fu-i3k5MDpv3thU2MqQKKbfdUC7PzXM1YrnDKDjJ4Hk4lGX6ZV_9-_Ig43qOIeKG7yfuYJMZIvkdWVsa_PhbbGrk_W2FocaKT74WxtwyZkcX1uO2tp1C0uprMFUyOIDzy16X3NvYxuXRjzuBMyqgOOLgL_vIckc9cuWLfhPY1b6krvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR1I9cG0S_fDtOAhrMzafoxG_zNi8vMWoAFq9CIy8K80XXG3B0QjHSJ0gRmUQO720r0T2SqpK7jmiBwj_JJXJQiTWraw83N56ywcTBOBg6G13SPibLO1gyVA2B8aU2HZvYdV7AMohvtkxrw81lKYCdPIhiY5haXDj0JS-bUW1AIShsoO-V5AWPoe4E5LmWqA4RGwVonz513eNt3AlQaggd6j75i8T13LVJygGHUP48pE-GPXHNtli2K3W5FeNcuBOtZaSwKO2JHfpbCNAai1zoFLgTpXKJ9zWnUnwYYbUHyRBOOtfBzSbYmsXgfVKzjOcc_s1JlUNQFA46MQ1A6iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNnCuSWtSNwBRZsyotoU9wBOlYysHvpMr9rbpQK21j0cw0yOFDJpwNepG0lj2EVp9dcVm0ZHpmdcQhuUvd32KBjKIp8D9Jov9Ax3ojyOsnrXkFo58MnkuFGXbkYh7KUFK-2ivKK5saN7GTgrc-34dpgQLNXSjA_-Nt67UDfYr-M9JLHPSoEZpSv7h_47oAgxQ_-RLLz9aBT453h9GVZsuIkHUpufds1t3XIJSQ2RGWMfzDkXQPCB-h8wxBcOerm05DkllvrIMQMAFA3qx0jxaJm03yQ-gUXln6q3LAJv5U6Su9tPiKJXEWvcRmKgks2jZCAkc8cn7MxmFSA-SCAXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0RceKuJ3JIBcnYG-iyEk3XJ9C-yZMeWeac7klKPmfOK5VaOicz8CVQD8oDpTwx_EIO1G29Vfkg42TKDg-DVmR8pQ_EVLepdl4Y8NcXHPbqhLDyPGpAQURVv1OQ71bi-USo-jJpNDptfRsjO-5Q3cX-ac0iyjNBoz2G4cz-t01gs7-uY56WnIeJoANEDMGmtasSW83iGPpLKpjrho7IN225xyo6FNLql1f-rFc1dxGlFhKxTDtLIHKBcDYS8RAQHGmE8E7ZMFUvyRLaHGlTRDQMDN-M61DwpJ2FnENyesZs0uKzLVLlnlT3jVQTdxvQU0pR7u_2l5xcCU7qYIfXJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXN_2YJs6DjzWxRjRD2YI_gWmPhy9itRgsIhOyI844kR6JsQTPPhkz2ZgRd_QJb1cFdoIoshrkslhtXILZSlCvOBJoH6bXm-PN9iX7hGyxwW0Y7BZGfsaxPt8xYP3XrFMtKrgwSdjH3aUI03JPwHY1hdwNsbUxUBfvxtkodWf4MaloAsVUe71ehL_R6tGUZ1K4oHAHnCRIJnKnaDQWWh5daYGXmlbzRjAuvHPjggjfWC0TfW8Ic0wgi6gk9XdQowB_joC6xwv2kWBcdANQsUT-2q7DRad_LhAPfWpqmxvZUb-tK9fkqwZ77lis67QTguR6ZQlIjJPxjZ72exySr-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1SDSao7KGwiEBteMKSWvZQRZPlerblvpqckWj1hbsb1Tdu6jYq5qoGECq_g33CAMKAQVk0lHDEZ8kK03z4nKdR9r15KFUUiRKsIqqPn1rPcBLR4ToAbXINDWKS44U6fJxUtZ_jwj5-Uf-8Zx9veiCgl18F_Br6Bd7gS8hXZn_YAXPnLQUyOvdcA0EMSxQnGOBHlTndkhtJN-dzJGlafiZnYIxjqz-Lln0asg1o8Sl-JX54dJAioLmiP-X9Y8Vibv9e_9x7w_5UcDGMEDHylymtnZLBOGbJFVqy89ndQYAZcIJQjftGKzHrxArrl_Pj6o5YAA_rMlDyhWLcxvQg46g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین نخل‌برداری یزدی‌ها در مشهدالرضا
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/455835" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرازهایی از زیارت امین‌الله که سال گذشته در روز شهادت امام رضا(ع) در حسینیهٔ امام خمینی باحضور رهبر شهید قرائت شد
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/455834" target="_blank">📅 12:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM2e-8RWnQl_6T7u38Woh5HDDuVVUVwj9mOC4Ip4DBLw1nWXuVSH5a-9pwvwtAhsg5OOlTHvlBIpox2fkOtSMjLkilR070qSJcpQfrUvQtJEYbbYcNXQlK6Mli16VR-ny3g41aviOtfHKEqJtKchDcrBpCQ8xMpEe-1U16XrSJ_aAvT9IKnVCi9aNELNTiTEsWVzys87H05CU5ftqHxHnluwRFj51aZ-CI8H-1c1QkYvlKnaDjNm-_fgtRwrmguwPNllF9T4Lh5ki2PZwmji_PvjMXZnit2ywgaHwKeiXjLKJ8X5sLV7sl-pt1MQ7RJJzlCOVy3HUCZZQ5pDznA_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی:سازمان ملل در حال مرگ تدریجی است
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: من خطر فروپاشی یا نابودی فوری و ناگهانی سازمان ملل را نمی‌بینم. فکر می‌کنم موضوع بیشتر به نوعی مرگ تدریجی شبیه است.
🔹
سازمان ملل در حال از دست دادن اهمیت و اعتبار خود است و سهم قابل‌توجهی در حل بحران‌های جدید یا جنگ‌های بین‌دولتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/455833" target="_blank">📅 12:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h66gv1R1a6u41K6Nx3yAzfbCaHu_RbU09bjy1F-Xj-UATVMhERKGHq0PkRSrS7JwP2Jlz3MT6Zownsk8TZJKT7dRv57YS3TUuzcuBIhd2VORuMGe4tLTSLI3qccKsT4owvhx7MK73zu7fTLO9iR2kp0pumAr3911utp9ygkNG6F6CLsDA9T-TkUg60msHaKox9-9k_hSa8yUQ8YFuMdKXi_IwtVwBc-nnWIoJ0RBIjl38ZICAoQccTLwtzg55szjxYi_lyrDoHdxEsjM87JDnXO-8XQ36xUe227zOURiNVyQibG_Iz_HuRWs_QNF8Op5tnKg_HenOD-QYgKqEbW34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار سنایی‌راد: در جنگ احتمالی آینده تهاجمی‌تر از قبل عمل خواهیم کرد
🔹
معاون سیاسی دفتر عقیدتی ـ سیاسی فرماندهٔ کل قوا: دشمن تصور می‌کند با ایجاد اختلاف داخلی و فشار اقتصادی می‌تواند حوادثی مشابه دی‌ماه را تکرار کند و در همین راستا اقداماتی انجام می‌دهد، اما تاکنون محاسبات آن‌ها محقق نشده است.
🔹
امروز نیز اتحاد مقدس مردم ایران زیر پرچم «الله اکبر» و «لا اله الا الله» شکل گرفته و باید این اتحاد را حفظ کنیم.
🔹
در داخل کشور باید به این موضوع توجه داشته باشیم که اتحاد مقدس، هم سفارش رهبر شهید و هم انتظار و مطالبهٔ رهبر معظم انقلاب اسلامی است و به امید خدا، با وجود اختلاف سلیقه‌ها و تفاوت دیدگاه‌های سیاسی، هرجا پای دشمن در میان باشد، وحدت و اتحاد مردم تقویت خواهد شد.
🔹
به عنوان یک سرباز کوچک عرض می‌کنم که مردم هیچ نگرانی نسبت به توان دفاعی کشور در برابر دشمن نداشته باشند. ما در جنگ اخیر ایستادیم و به اذن خداوند، در جنگ احتمالی آینده محکم‌تر و تهاجمی‌تر خواهیم ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/455832" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان قلدری شرور اجیرشده با شلیک پلیس
🔹
در پی انتشار ویدئویی از صحنه شرارت و قدرت‌نمایی فردی با سلاح سرد در فضای مجازی که در آن متهم با استفاده از قمه به یکی از شهروندان حمله کرده بود، تیم‌های عملیاتی پلیس اطلاعات تهران بزرگ بلافاصله وارد عمل شده و متهم را دستگیرکردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/455831" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم‌رضوی در سالروز شهادت امام هشتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/455830" target="_blank">📅 12:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBYC-eeCkwUtnRuvKu9xd93V8DQYrsiHGrzpdD0qhjBGdlvsuAWAVpnckX6bRCOiN-j-BZS9W_g9O34SXPvJm4PoJ0AU0iEmPspZqV2_5LDcwwm0L30Sg99S9__UJ1xXoPZNTJ0J1lI7CH-kqV7S2RSAomzlX7UlK5rIZHCa4KAoKl5lxENEFOB7FVfKQlbMS03Z_mEOpTOywibttnRL2OaCKP_OSnTBpoMna4y5Wg6iftW8RzFyR-j92O2m92UzDWT7xubpeFJMz-n6njIL2OHthatcnfyKhsfxpQ8LEc7xb0HME9FQzWGNsI96FP48UpnfEkURXNsZfcbdVhvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران: بلندی‌های جولان بخشی جدایی‌ناپذیر سرزمین سوریه است
🔹
وزارت امور‌خارجه: ایران لفاظی‌های نخست‌وزیر جنایت پیشه رژیم صهیونیستی مبنی بر تعلق همیشگی بلندی‌های جولان سوریه به این رژیم و نیز نفی کشور مستقل فلسطین را به شدت محکوم می‌کند.
🔹
اساساً سرکرده باند جنایتکار و مافیایی حاکم بر سرزمین اشغال شده فلسطین در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهارنظر کند، چرا که سرزمین فلسطین متعلق به مردم فلسطین است و توهمات نژادپرستانه رژیم نسل‌کش صهیونیستی نمی‌تواند این واقعیت را تغییر دهد.
🔹
علاوه بر این بلندی‌های جولان بخشی جدایی ناپذیر از سرزمین سوریه است و جاه‌طلبی‌های استعماری یک موجودیت غاصب و اشغالگر نمی‌تواند واقعیت‌های حقوقی و تاریخی آن را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/455829" target="_blank">📅 12:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riaxsymK0rLrtD0Qclf3AThWrRVzfB0Zb6fTWPSfCi-dKZitdKC8PcI50vuby1t63F1nO6A6KixSygOlZCJ8Y0YPaEStHD6cOnLdnXhWEZ2qwunqW9lvyC1AI0HmJ-XzFi9zh4TrtH2mPboScQSpzaL4UfW9CLDQ7euwheTdYwW7bD-v5iMmLaZcVXxvbvOTZNT0HmwDPByZi0eCNfM_8eqxxS5Pj2ZH-Hwmdi-rhwpRaY9x1oUPwRdNfulsHJmsS7TkpL4Mvm-ISwcYw3bVmtlzFGAlzbd3P8Roh54E1fQzkeLZdByl1XPbvYXfbEB_GQnY6-CkgXLeu_1LZTUaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQF0ykdx_7yRNCToQDNIudJUK4HL2ADS89k34BMhYY9v6Q5_jegmEdpg1R9RkcKZjniAWVBIj0WL12CbB-9kguWPUZIYu5os3HrvO7cIjoeF8Of3wckKxYkHNQz5Hf72oAKGAt8LWmpZrxWALRDHTsygScOxzKZq8L4LfICMgJX-eXYEUpbbYnst_0MEYeADMqxgqbGfz6hAdB6iuBZ1UvjNYS3lZNPceRKhzmo7LMxq5NJ6Eu_Qj13APw7XLUET3_5YbMeXdmd76AUiHP_uBDkceSYgZQkIQuv22P_h6KTcKF7k7M3mYqKM4Lvt05YJywaff3xhOyzWDtMuu9X__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnBWiOYDelEugyHq1ySFatA-Nzymkihcy1Mg5gRxJePoBezTvE3YX5pocss7M3OLOv0eyuWi1I7DSkpWPzzILnXDFBmoYezvI7Au-Q2ertDPxjwz_NIMAcCEcgXYCi65_Abil9aB0m8I0wpzffcv0LPkz-D9CrLDtKdnuLUvM-tlLyCCAoijgPTOtFp1RHG6OPlgtKWiEI347SJSsV7Yq2k0X7qHGWHbq6OIsXgmtPNuF7rHLymShi_dTOE71lzlcdqd2ASMm0qMsG-OoTYZCz3MX7y-KnVNSDQQKjLV_E1kasCfXF88IbwF2jKmZj4tFpeOrlt6G6rb2fvQtKQ85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvolG8wI64P8XtfNkgeyoYosYh1g1_j1CcokIYUwXdmRtcxbkU6cBrqNITikxM-SBV2BkTAgJ9xubdE_VzkhnLmhouerq9PEUXQjn5O9QeNse0KsJbSdpKByh1en_AWh5MUGH9Un6g7nVIDFmyz072yejDSEz3LfCxWA1sl25i_HDhLBu1W2Y096iUAmaChbKas8r_2JezD4pRkWx0oWoX3W-jQg22pG6iBxc0NTn8WrX7u8VkY0BfEQ7S13tbLm5Neh3MnEVQB1Bo753RN8K3vaZaDcbxtxnP72Vl8fqXXkDMCFBPw6gsQXWf-_gmLIEg-WzcuBlcnfdBvO2M2INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFu93nnxAaBtKKn-UxARgEkWbLOPhUcpSujPpl1qwUY6ykVwkvhJy4L9hbNrhgjGRX6BeMfMxeGuHC8lILm_RPJAxlkyj_DfrbxToqznFaJbsh09PY9QfCjgAovV6oL3-ewRcXSSO8YqbZRSFg_qc_YXUp2i2dMprc9O8vx3PQHJ_mQACgJj-SAgrrSUQHoRQu1b9pQb59o61F3DTiCRs7MjwssNvqMT1NQzCa1jTK6UIKzA24bdpKM_ApU2kh7wQ62arVzRmFWFDCmlN6UTMravxFBjENRygmeOTYLYl6O-y3lPpJ08jUwSdZYopQdGVnRN8z_w-hqyDRO1KfhplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Edb0RRjx1ttYblbF03DW6LPuE74uyvTrHtr2oE4nLWhvFMCPSaVYVAI_nvVR1OCgjZQSoRDoAyzvlt9-KieskLI6Ww5XrdEzvmz4t3FONBGYGoPAScVu-CQDs-4RaQEBlvs4ABKUQZz7n5NSvVsA03rpxhLaL6IOghXyWmn8E-NXb67YjtjX9Aly7-clkjD7P8XQr1I4N9SejuQaV90ZuiIfjWnflikIklehJZxZdAtEqBworfVlk3CPTYgECe-yjN-k66o7myQbx81GGMPmDihPqbG7Wqp8knFwgdZAjX-WG8TyWNRl16XJeXZ-7oDbxAh_oaBWQZXUbRuUKThXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul0tqzTlhKGkxtPOCFnC5OS-J0FUP0PwnqCjcSIfiiv-LCU1WkNcci7QlBh9kI0FyanjHN_gNy80XXoQLwWlk804UYZIxEIWzq_LACSZBqU847uUBFTp42ZnQw_oeUYWyE3K1OukSWbM7zvRKQWZzzeoM7XqFSGAeAwZ5HJ6TcisQ9otMlHlDOnGV5iQx1HH2CAh-2wKZuQfRZDmnEAPLmoH98IsuSkhJ7M7DlBV9PqqQo-KPAnv46JgCe9KoeFkYfdT6XocouLva3-pCizK9GRLV-TL3PDCnqiivmklSOOJqkYJpZgSnpbatxCyrPjFTZ9gm-nSkgSwjXZid3AXKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سالروز شهادت امام رضا(ع) در حرم‌رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/455822" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیغ مجمع تشخیص بر گردن بانک مرکزی
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص:  بررسی سیاست‌های پولی و بانکی در مجمع تشخیص در حالی بررسی است؛ هدف این سیاست‌ها، اصلاح ساختار نظام بانکی و به حداقل رساندن آثار منفی ناترازی بانک‌ها و عملکرد بازار پول است.
🔹
گزارش کمیسیون اقتصادی پس از طی فرآیندی طولانی به صحن مجمع رسید و چند بند آن نیز به تصویب رسید، اما به دلیل شرایط خاص و ضرورت‌های موجود، امکان ادامه بررسی جلسات فراهم نشد.
🔹
استقلال بانک مرکزی و اصلاح ساختار نظام بانکی از محورهای مهم این سیاست‌ها است، همچنین با توجه به تحولات نظام‌های پرداخت در جهان و شرایط تحریمی ایران، باید مشخص شود کشور چگونه می‌تواند از ظرفیت رمزارزها در نظام پرداخت استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/455821" target="_blank">📅 11:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4fVby-hm42jvdW8Olb5bv7RqnSphlpXzqMwstuoixUQdMKWGZhoQbJQAaZZIIlYc6emj6WVlqPaTyeVnNVukjELQ-qcEK51DZiWWqwMmznYIVu-KJoCAX9Cv0mKO3N5p7w9LQQ69xPhmayeQkFfW_waPIJuMHT_R7OF1pq7NG_OPH4JgfaFR5Z2XI3G9Ckfl6cu80E88A5GY3Pzll_5M9lnQwkb-AS2STW0J5DyRs7GTnPvAEXy3DU4-UtzPFHHMCXKalhvYDJEj7ZKSfd6gJ4Rma-TfRwmHv7CCM58RIUAhL8zwlGuhzYe9zGfNkv_YeWnEVyIAdGkg8Uio03Tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طمع ترامپ برای درآمدزایی از تروث
سوشال برایش دردسرساز شد
🔹
دونالد ترامپ به دلیل راه‌اندازی سرویس اشتراکی که تا ۱۰۰ هزار دلار در ماه برای دسترسی زودهنگام به پست‌های او و مقامات ارشد دولت در تروث سوشال هزینه می‌گیرد، با شکایت جدیدی مواجه شده است.
🔹
شاکیان این پرونده، نشریه اینترسپت و بنیاد آزادی مطبوعات هستند که در دادگاه فدرال ناحیه جنوبی نیویورک علیه ترامپ، دو دستیار او و دفتر اجرایی رئیس‌جمهور شکایت کرده‌اند.
🔹
این شکایت، سرویس «تروث ای‌پی‌آی» را هدف قرار داده است؛ سرویسی پولی که اول آگوست توسط شرکت مالک تروث سوشال راه‌اندازی شد. شاکیان این سازوکار را «بی‌سابقه، فسادآمیز و خلاف قانون اساسی» خوانده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/455820" target="_blank">📅 11:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از آلودگی نفتی در سواحل جنوبی قشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/455819" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5dTax459NLjdsc44tq0BVzS35nOHV8fxSz4bdnUUY_dNKpHhRI8VvXRU8u5wyVVRi9ExWEp_6GetxAxok8mtfi89xkuNas8GwiRvKaS8FO9uMtZYw8jlcBbLXZPR8u07i1wBlm_CwMPeyxz_rOPdYnyzATQRKAlnTqQ7H5FFYweBqTksuiQK_fi1HBHcjzGK2HSS4eUyDkNWRRWC28_nEwNqavr2oQQ-WsfAyGq78InmqTPxgHYqzFlanEn4JfNYqx91GCtBabDydLi9qqlTThB6scOS7mjF3iMk5QGDt3-XmXJhDXGWw4sVbuJ56R-e38QL_8r-UQSjsGRhUzt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آمریکا در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی بزرگی شده است
🔹
آمریکا مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
🔹
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
🔹
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455818" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
آمدم ای شاه پناهم بده
🔹
نوحه‌خوانی در حرم‌رضوی به‌مناسبت شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/455817" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دستگیری ۱۵ حفار غیرمجاز و کشف ۲ تُن سنگ طلادار
🔹
فرمانده انتظامی کلیبر آذربایجان‌شرقی از اجرای چند عملیات هدفمند علیه حفاران غیرمجاز و قاچاقچیان سنگ معدنی طلا خبر داد.
در این عملیات‌ها:
🔸
۱۵ حفار غیرمجاز دستگیر شدند.
🔸
بیش از ۲ تُن سنگ معدنی طلا کشف شد.
🔸
یک وانت نیسان و ۸ موتورسیکلت توقیف شد.
🔸
۳ موتور برق، ۲ دژبر و یک بالابر نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/455816" target="_blank">📅 11:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrgHHIiX0YXm6padaQc5gdkPaMBdi3DrOqZLAXo8ctILJUvD2suQn-f1Y7fQsRFEQn6fu3X0V1NMKQqjuq5SZLOs3dUUb2jyk9xrCkMn02zChSWWgsJcxx96hFHWOAKyKQWmYAqSN4uM7CuI6QT-AMoFnf7VkiHJEpspAPlmiGpSP4iiEWkNXNzYv78wCBh5vC_g9o6wYFmhZFGOuTL5FHW40bZbEVMNeSzjW7r3WCSDWcoSD-cgHSBw3cfA3sSproAvvSeyj9hpSmQ-D_PMHyAPYE9ePbMo3lSVY2VL6U9jBxGCR-narMF0gQH0ln84c9x6qIx7ylqdnNzCQMJMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙️
گام موثر بانک صادرات ایران در حمایت از اشتغال/ اعطای تسهیلات به بخش صنعت ۷۲ درصد رشد کرد
🔹
بانک صادرات ایران با اعطای بیش از ۷۲۰ هزار میلیارد ریال تسهیلات به بخش صنعت در پایان بهار ۱۴۰۵، به نقش‌آفرینی موثر در حمایت از واحدهای تولیدی و افزایش اشتغال پرداخت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/455815" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioLQsq9fQf7fMLShzVy2ZO7_FFrSyoUkGhVsdN6sumyHUve0P1x7Lxz7M5Ik3saZC4CJQUhmTuYFfs2zLI6RYGmwbZfkRRdeDS8PTRzaIkWuVFBepLb_3GD5hx9yhzJ9QpcL1D4VzjufrUisgdIptOqoRfkrYUsZpMY690N7zpZD46d_1SkYvregAgbyFg0YIyJ7Sr6eiurThszVMOchC6FO5R9-4G9Yo6LoAhqYVwT6BGHfigs1VsqKJ2ZCcjHF62oWxaD1H8JkcIXpuuLCdvuFkdDS7bhRLtTD5Dn-eAIwcVEk8MHJFXFgYW1cErsyQJrooQeZGOfB7MU_xO5k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ فروشگاه آنلاین مذهبی که ارزش یک‌بار دیدن را دارند
۱.
فروشگاه موکب‌آرت
۲.
فروشگاه پوشاک معراج
۳.
فروشگاه ربیع
۴.
فروشگاه ماهد
۵.
فروشگاه مغیث
اگر به دنبال تجربه‌ای متفاوت در خرید محصولات فرهنگی، مذهبی و ایرانی هستید،
این ۵ مجموعه
می‌توانند نقطه شروع خوبی برای شما باشند.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/455814" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/455813" target="_blank">📅 11:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریکی تاراگونای اسپانیا در لحظهٔ خورشیدگرفتگی کامل
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/455812" target="_blank">📅 10:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF-4M0ieQYqjfm-_DW2CBNcwFNz0e65NuEsg8wX34Mi7L-5OWA7sFWvN_m8VKX5mJOYRAfx8U_XTi7qHuRLco6TZ78RCm6epffQld3abQkKZ7062nJ7emUzEnfelIMCCWlmct5s1u9dsnjFqVGa9s96PV143iGPVKEAgONQymsQ5XpI-xipzVt7EbsJOmkCtfRJY53Ae1847v6FJmP2B8cErNc6krpyDYxKHjPWq4QHV4veEKQGFswHEBPBy3CCkKFdgCPXsXfYgXoscrcpGNECY4lvh8Lv4PCQshzxX3wwBJq_mOV4J22-5FcWhMdcntScF17bjvemkXOBIpqOHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزیدی: عراق پایگاه تجاوز به همسایگان نمی‌شود
🔹
نخست‌وزیر و فرمانده کل نیروهای مسلح عراق در بازدید شبانه از مرکز عملیات پدافند هوایی، با تاکید بر نقش محوری عراق در امنیت منطقه، اعلام کرد که خاک و حریم هوایی این کشور هرگز پایگاه تجاوز به همسایگان نخواهد بود.
🔹
علی فالح الزیدی همچنین بر تأمین تمامی نیازمندی‌های پدافند هوایی، ارتقای سطح رزمی و فناوری، و فراهم‌سازی مقدمات ایجاد سامانه‌ای پیشرفته برای حفاظت از حریم هوایی عراق تاکید کرد و گفت: «آسمان و حاکمیت عراق، نمادی است که اجازه نخواهیم داد حریم آن نقض شود یا امنیت آن از سوی هر قدرتی مورد تعرض قرار گیرد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/455811" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستهٔ عزاداری خادمان و زائران در حرم بانوی کرامت برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/455810" target="_blank">📅 10:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMEMMueWHCsniNVlac-Qc87Clzzyv43_MQAyWoSf8Nki4bFZW0_vOMygPb6Bf55ygZKCZwo4CaLxEeKKSii-Deb6PFPhhhvtg7FNfbuBxASlLDRQHO63Rco9OPgAh5_gIagPuhbvwR8gp3IyccvfkGcgK01w4wQe3A3x02yEhhuXbDirwR8xIU_DUrLy0R757mlammIXX44msu12DJfVGBtbDmoa5Ifbj1EW1fVe-fkCmsS0KXFQcU-kSbaYs39L_04EhuRmkO3XcEmfR4BXGpbP5fymyc5-YnmNNhQL-ykVwrH4E79HxSsx3zZ-XSAF4ARwUnpDu57cTw5RcoJa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: آمریکایی‌ها قدرت انقلاب اسلامی را در مراسم تشییع رهبر شهید مشاهده کردند
🔹
حجت‌الاسلام طائب: بعد از مراسم تشییع رهبر شهید، دشمنان متوجه شدند که محبوب‌بودن یک فرد در بین ملتش و ملت‌های منطقه را نمی‌توانند با هیچ قاعده‌ای محاسبه کنند. این محبوبیت برای جهان به خوبی به نمایش گذاشته شد.
🔹
آن‌ها برای این‌که این قاعده‌ها را به‌هم بزنند دوباره یک جنگ دیگری در تنگهٔ هرمز راه انداختند و دنبال تعرض جدیدی بودند اما به لطف خدا آمریکایی‌هایی که اعلام می‌کنند ایرانی‌ها نه نیروی هوایی دارد نه نیروی دریایی، بازهم با شکست مواجه شدند.
🔹
امروز می‌بینید که تنگهٔ هرمز تحت مدیریت و کنترل جمهوری اسلامی ایران قرار دارد و کشور ما در کمال امنیت به مسیر خودش ادامه می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/455809" target="_blank">📅 10:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c994b8a7.mp4?token=MxZaeFIflQSjMLaUauVu5PxT4Sg3xv0jTrffIhaetvl9h3uo3tN9rh-D0Hvbgssum5PnDZKHSQ3BET1dcvsPE94lAo4bR-bB7HlEL7_VyJA59cdhdYPnVXP69agLlYpeEP4J1uqPDo1oW8J-W5QAUoEgVN_SqtRCyofxM-2SGP7F6Hd0hG1-fEzK2j1dDSYxLyQ4fs-Mp0YS0PKeOkCnAQwRYD7KQKTRR7rJB4tmE3JyWfL35FrE0yIT1wiVmZlRXYvi4vJtt9hfx_c5yC1dv5joPt4u19qfo8XUDXqEMC_N3j-_LK2OSH4cy7l7rMlbXabCvQON74gZb_huCGCMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c994b8a7.mp4?token=MxZaeFIflQSjMLaUauVu5PxT4Sg3xv0jTrffIhaetvl9h3uo3tN9rh-D0Hvbgssum5PnDZKHSQ3BET1dcvsPE94lAo4bR-bB7HlEL7_VyJA59cdhdYPnVXP69agLlYpeEP4J1uqPDo1oW8J-W5QAUoEgVN_SqtRCyofxM-2SGP7F6Hd0hG1-fEzK2j1dDSYxLyQ4fs-Mp0YS0PKeOkCnAQwRYD7KQKTRR7rJB4tmE3JyWfL35FrE0yIT1wiVmZlRXYvi4vJtt9hfx_c5yC1dv5joPt4u19qfo8XUDXqEMC_N3j-_LK2OSH4cy7l7rMlbXabCvQON74gZb_huCGCMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط بالگرد نظامی در تگزاس؛ هر ۲ خلبان کشته شدند
🔹
یک بالگرد تهاجمی ارتش آمریکا در مزرعه‌ای در مرکز تگزاس سقوط کرد و آتش گرفت که در این حادثه هر ۲ خلبان کشته شدند و ساکنان اطراف منطقه تخلیه شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/455808" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455807">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145f4dc47b.mp4?token=J8qLlVobOIFcS255WWX3Ofob1TeIZOgrO1ukCPPjikJaz0zy7e2_bdacOY_xFkiI7oKLeaJQk5duRzjt3H8wKuVp3_DmV5egfIRLV1AqZPV-yGFEE6N-FU0pRM_XVM4w3dykYThyHZ12V6yMjmLpRSaPr8PJukkBJBvEJUB4SjbdZZ3KpZOmCaYKxpYOPNQ6hBNP-_8_OqvL6K2CrpCaKxAgEKhESikYbClB1HvpQ_FLksOzZEFLvFnIgggzv_um8BVDKZLHsdLjjXUITsvYJEbPnSGUohr1Qs17UEXLFR6ZhF7zVhEj-eLzouvPPsYUXHhV-6JE3V_fMt2LZXlN1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145f4dc47b.mp4?token=J8qLlVobOIFcS255WWX3Ofob1TeIZOgrO1ukCPPjikJaz0zy7e2_bdacOY_xFkiI7oKLeaJQk5duRzjt3H8wKuVp3_DmV5egfIRLV1AqZPV-yGFEE6N-FU0pRM_XVM4w3dykYThyHZ12V6yMjmLpRSaPr8PJukkBJBvEJUB4SjbdZZ3KpZOmCaYKxpYOPNQ6hBNP-_8_OqvL6K2CrpCaKxAgEKhESikYbClB1HvpQ_FLksOzZEFLvFnIgggzv_um8BVDKZLHsdLjjXUITsvYJEbPnSGUohr1Qs17UEXLFR6ZhF7zVhEj-eLzouvPPsYUXHhV-6JE3V_fMt2LZXlN1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک و مقتل‌خوانی آیت‌الله علم‌الهدی در روز شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/455807" target="_blank">📅 10:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455806">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
منابع عربی از یورش نیروهای اشغالگر اسرائیلی به روستای قصره در منطقهٔ نابلس خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/455806" target="_blank">📅 09:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455805">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUYxvEcW4A-3k8zlWzYxCepwBI_KiuiFhbDnzNPlbOWNTYToCuxl1y5f2tOkaC_2ao9GljO1zRBN73ay43p98aF6xkugYgIRPqdhQagzEOCfwiSSCkKZ7t3ZRBvE8v3nxWDCYtGArIDEyGjIdDXxdNRwo44xQa3610p8NG8qVxZntAc7eNP2yIXmHoFBIjG-rnIhssMeZKBNLVaeWEWzUhsvfXMF3Gq6YyFRoZbLy-NHVzK4fWXzSYRcDILQBva0AiCJcNfpn86HeMiIODkT1wLSVhLrGuiZlHtcjYYM0YEHAdqA90YSxC-wa0VzEBklgH5AgKFRlW5tTYQUEDCb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار رئیس سازمان بسیج با آیت‌الله سبحانی
🔹
صبح امروز هم‌زمان با سالروز شهادت امام رضا(ع) حجت‌الاسلام حسین طائب رئیس سازمان بسیج مستضعفین با آیت‌الله سبحانی دیدار و گفتگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455805" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455804">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661f970a60.mp4?token=HXv1A8ihibIRXUDliiOG-sEC7-2IudI9JvwwWP5SBrYsRzXnqRVofLSyBT7r5EKsB0XO-RwTrmTY9HxCLreVlASw16U0eQ8kv3zBbUwxdsUl6mQJ_J5f6ARcFh98tmIS_Y853Z9pJMH84Ufe0gEka4jJ-tPnh1zfuJn4wSLmfp1T9L9k8Y2WpCo1mfOZ1WdYDdq3m6240Uc5M6rWl_IHT3MeO1egmFDv64g9w118ErdfiAaBdtT4sF_Tk2D61CkK8dReZ4c28E4OdSJMNBfpR4oQCbkMPCGfsr630PhJDeytnISCeM7pWipVJZ4eoqwiCFIiK5UiWB5xQqD4vqOagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661f970a60.mp4?token=HXv1A8ihibIRXUDliiOG-sEC7-2IudI9JvwwWP5SBrYsRzXnqRVofLSyBT7r5EKsB0XO-RwTrmTY9HxCLreVlASw16U0eQ8kv3zBbUwxdsUl6mQJ_J5f6ARcFh98tmIS_Y853Z9pJMH84Ufe0gEka4jJ-tPnh1zfuJn4wSLmfp1T9L9k8Y2WpCo1mfOZ1WdYDdq3m6240Uc5M6rWl_IHT3MeO1egmFDv64g9w118ErdfiAaBdtT4sF_Tk2D61CkK8dReZ4c28E4OdSJMNBfpR4oQCbkMPCGfsr630PhJDeytnISCeM7pWipVJZ4eoqwiCFIiK5UiWB5xQqD4vqOagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنجیرزنی هیئت‌های یزدی در جوار حرم‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/455804" target="_blank">📅 09:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455803">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b215ea36.mp4?token=M_TelJ5S3mIg8ZMz_2m2yGYG5Sz5QOTltKgQoNNOIulDGUWeCXcizXW7Aqy5IsegbQaUB-bf6SmDBWony28zP66LKa5HWGGaGMjmiFghzgwV_0bMvGYsWdRiCSFVFuFBvNlioVGH3bOS2bWTkyEoiF3bBnOvI-c2G2s7Z6C5ifwdDxbPFOXllYKOlv7UoY1l-p16_WbHrKDSxh9G_2zQ7Pbu4qWavn2dNZBKj98FjZE-D6eP52VERFGBtZfHzIo8S-z-52jqSOpqBfAXDD8BbwuS5fdP3HPU97kTX9vYCXE4evqKH8zM3X3W_cCYfKQQ7iCYKsBZUschuzYZP43Vyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b215ea36.mp4?token=M_TelJ5S3mIg8ZMz_2m2yGYG5Sz5QOTltKgQoNNOIulDGUWeCXcizXW7Aqy5IsegbQaUB-bf6SmDBWony28zP66LKa5HWGGaGMjmiFghzgwV_0bMvGYsWdRiCSFVFuFBvNlioVGH3bOS2bWTkyEoiF3bBnOvI-c2G2s7Z6C5ifwdDxbPFOXllYKOlv7UoY1l-p16_WbHrKDSxh9G_2zQ7Pbu4qWavn2dNZBKj98FjZE-D6eP52VERFGBtZfHzIo8S-z-52jqSOpqBfAXDD8BbwuS5fdP3HPU97kTX9vYCXE4evqKH8zM3X3W_cCYfKQQ7iCYKsBZUschuzYZP43Vyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/455803" target="_blank">📅 09:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455802">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444b4437d9.mp4?token=RdBn7YoDp6bC6F1eCI16piQ5JMPVGsqDLa2OJzdKY8dpY5UuhJJ3mLKI4ktxC6SeUyITNDKodl6enQSl5CnaZ9dthUGrzIy90OhNP02W42thS_nde8c8z5V3nReKGk_N4qHpiALsXWIxEWyINvRU0xYWUAD7bVqWXBAVlK9tZ2CymiMS5jUr0yXqx1y0LfT4qxPboKs-RbkVg9o9ynZI7JF1tTvJFUGXiqRlNUgSpUUTz5LKG1k19HNbAYaapDkHHpdGQItcE49eZqdG4mhq8j0tfhn9MHDFZF299fhnI-mHCsp8vfhPPxW9a-ONvb29wd4OiDgc51kagz99fkRVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444b4437d9.mp4?token=RdBn7YoDp6bC6F1eCI16piQ5JMPVGsqDLa2OJzdKY8dpY5UuhJJ3mLKI4ktxC6SeUyITNDKodl6enQSl5CnaZ9dthUGrzIy90OhNP02W42thS_nde8c8z5V3nReKGk_N4qHpiALsXWIxEWyINvRU0xYWUAD7bVqWXBAVlK9tZ2CymiMS5jUr0yXqx1y0LfT4qxPboKs-RbkVg9o9ynZI7JF1tTvJFUGXiqRlNUgSpUUTz5LKG1k19HNbAYaapDkHHpdGQItcE49eZqdG4mhq8j0tfhn9MHDFZF299fhnI-mHCsp8vfhPPxW9a-ONvb29wd4OiDgc51kagz99fkRVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویژه‌برنامهٔ سالروز شهادت امام رضا(ع) در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/455802" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455801">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
زلزلهٔ ۵.۴ ریشتری کشمیر پاکستان را لرزاند
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه (EMSC) اعلام کرد که زمین‌لرزه‌ای به بزرگی ۵.۴ ریشتر، کشمیر تحت کنترل پاکستان را به لرزه درآورده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/455801" target="_blank">📅 09:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnM0IFbx4N5SgHMHhIZUvomZS-zOdYBgNscU1WL_QbvoB4oEInqJYtTt7gtumWglN5oEh3xORj4P8L5_TJQvlgyvMh46a_oPoNF4_dTruMQHvjsWXpcwAbWECy0iEI-a5WUFZLVQq6C1tZkRBSfOF_kx_5vrftZSbT4SObeB6W2oR3WLCXefW_caZ8xMUM8nKQAqVa7JH7UlCKnt6yzuK_sscrjMqy1mt3DrXAJkN6X5bx09KQE_wuiNocUE1oScpRTfcmcYOd-kgGxcqJ4DATWNOSX5tyWsa7l71sDpG723Ej9KGvf0FYdw9Tmq3FKYYFfd2JBm5oXbZbj8-10Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند با ۹ طلا رکورد آسیا و جهان را شکست
🔹
محمدجواد بیرانوند در یک مسابقه فراموش نشدنی که رکورد آسیا و جهان را شکست، مدال های طلای یکضرب، دوضرب و مجموع نوجوانان و جوانان آسیا و آسیای میانه در دسته ۷۵ کیلوگرم را تصاحب کرد.
🔹
بیرانوند با مهار وزنه ۱۶۶ کیلوگرمی…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/455800" target="_blank">📅 09:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3i3-XAFio9bMxxFYY4h_5xdMVE3UtS4trVVOz15unl_BhJ9eIr7_iyZpiWT7ml5p7Z5Un6OInkYjJScTUw3y3h-dXVIJ1X8jJwBFU0nEO-FlNsGFMx-PS9pH1zEeFLKGu9jL52PI73eAFbA7aK5iWkeozceOY4ll7MtReXdzuakg-f1czqiqllq9k0d55-7IdcevGg8ppBkyi_zlUfdtgz5yU7sQRYmwCi_30V-mSyVSm-KCzgJJgYU6Rf2jE70O7DIk75TL_iCj8ANeWkpX3st9PPFLZthX7x3S3Af9xSCbAhpwA7O5S0zX_701xnm6By3L6jywLJv--YpuIrKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم صدای گلوله در مدرسه آمریکا؛ این بار دستشویی دبیرستان
🔹
مقام‌های امنیتی ایالت جورجیا آمریکا اعلام کردند که یک دانش‌آموز ۱۴ ساله در سرویس بهداشتی مدرسه به یک دانش‌آموز دیگر تیراندازی کرد و سپس توسط پلیس دستگیر شد.
🔹
بر اساس گزارش اداره کلانتری شهرستان هیوستون، یک دانش‌آموز بر اثر شلیک گلوله مجروح و برای مداوا به بیمارستانی محلی منتقل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/455799" target="_blank">📅 09:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
اجتماع خون‌خواهی گلستانی‌ها در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/455798" target="_blank">📅 08:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455797">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5c9795e3.mp4?token=EkpD4CVj74ScGeu2mCR3dXKJ_PbFVwoS0st6ChRm-gu7TMgg9id6axB7W7fBaBRM8cunrJYVaGgQ_UCvEfpTWFauH5n3UWmv-CPmeLo0oz_YLiVXGKbm911nKGk4JyyLrmJTzdJC5bAfFgjLzvPzsaAzpsJSQb5OhfVQtOKnl3Hp6N0fWNDPUJUzQnb1GlxPWa07x7Ky97CRYlQ4zPmYP7EaqspXBHeU0ihfulpj0xxf7JD0Md9SZCEj5JJ4zUzwtQDvSTS9lAWXA9srczU0eF9ClLN0kglNMt8TxX8o9BaZRbEpTWEAxT3jgJFSbe02snm6jKWumxlQ0zAtsdWlX1QZUO4is8aAUQV13Q04w1pliBHqhx4C5Vq5WAGeNx-DP6k6O3mTp12n6kXhBVpl4M3yZr8juJqkSeED9YqMgX8yVC9reXD2ZGR6lAAgmAEoLfMeqjIP9ni3wUAi8ZkCXt-9NArDO9seXqUw_arW4wiI2e_I7TYLctCVwI6eG0gfWxu2hoAIUyE4cU6uNYujo0ZXB1JbxqCkmjG4-qEcOz9MSsGMwg_vXdT8lbHDhsgQFS2-4wUAVvbA4K-5jguHYYj46LlsSGyfx5AxpqzJ839xkTuEVvG6touC0AA3ZRT-UwQ3W_ded-SRPWchAXnvtl4_p8J0KUG3jfoFzxihQ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5c9795e3.mp4?token=EkpD4CVj74ScGeu2mCR3dXKJ_PbFVwoS0st6ChRm-gu7TMgg9id6axB7W7fBaBRM8cunrJYVaGgQ_UCvEfpTWFauH5n3UWmv-CPmeLo0oz_YLiVXGKbm911nKGk4JyyLrmJTzdJC5bAfFgjLzvPzsaAzpsJSQb5OhfVQtOKnl3Hp6N0fWNDPUJUzQnb1GlxPWa07x7Ky97CRYlQ4zPmYP7EaqspXBHeU0ihfulpj0xxf7JD0Md9SZCEj5JJ4zUzwtQDvSTS9lAWXA9srczU0eF9ClLN0kglNMt8TxX8o9BaZRbEpTWEAxT3jgJFSbe02snm6jKWumxlQ0zAtsdWlX1QZUO4is8aAUQV13Q04w1pliBHqhx4C5Vq5WAGeNx-DP6k6O3mTp12n6kXhBVpl4M3yZr8juJqkSeED9YqMgX8yVC9reXD2ZGR6lAAgmAEoLfMeqjIP9ni3wUAi8ZkCXt-9NArDO9seXqUw_arW4wiI2e_I7TYLctCVwI6eG0gfWxu2hoAIUyE4cU6uNYujo0ZXB1JbxqCkmjG4-qEcOz9MSsGMwg_vXdT8lbHDhsgQFS2-4wUAVvbA4K-5jguHYYj46LlsSGyfx5AxpqzJ839xkTuEVvG6touC0AA3ZRT-UwQ3W_ded-SRPWchAXnvtl4_p8J0KUG3jfoFzxihQ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این رزمنده هنوز در جبهه نگهبانی می‌دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/455797" target="_blank">📅 08:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd14256e04.mp4?token=rQV76zpFU6zuaoaF7Zwf01JcycHfFitD1b0r_FDwBPtZCbp6nQ-l0iK_B125Bhtwi6pU_D-WDmgklNrBLd3qJ8jtVm8LSKDmAZelj8o0iXk4si_YQQciaCpb1J3Uc7kwUiAcOn0ZAsHo_zINhYCZL5eUteqH1IwAaiwVPGvAOen_vzjhupo5JtbF5F9qCn9LvL56GK4n6wRlA9i37bUCEzAyVmlgx28Q7d3J9twZn10lGIzdcMy4zHLlf4Kpb10yVofuoQGTTfMEc0hUgSYQZYpTrO26gGWp0usWobP1a1db9Z_B9cTeTO7qhn9q_cuAFYE0DbKzb9MzwhT1qqyusrTFv9TVcuo-sLvmUAwORwRgENAdaSbkfEcfsf5LasY7Yd21AjLxvL55yqgkev9sgIaewiS8MC9E58JRGuXzVVMlCWnsjAbXho3saNOvqmnbqc9iRKPQzR7okuXaW9Gq5uvatM-xRBdXpkVz9yq-l5VptAm_R9lHMfULAnm9d5m-jBR0N0eVn54jZWDwTZp1HVmw6OioR6klm5Ax5wOv0mkHWr3UtbHlB3rLNQ5V2M_Vu2AEgxOY3JKYh5KVc_ZLkJ-ZXSoAO6CUk3duKF3eG4fq0GmrlDCeeojoSKoXe2OOH9SsP_hWF1elmhDh3HZlbwUaiwgF4N18_-N4RmAzSw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd14256e04.mp4?token=rQV76zpFU6zuaoaF7Zwf01JcycHfFitD1b0r_FDwBPtZCbp6nQ-l0iK_B125Bhtwi6pU_D-WDmgklNrBLd3qJ8jtVm8LSKDmAZelj8o0iXk4si_YQQciaCpb1J3Uc7kwUiAcOn0ZAsHo_zINhYCZL5eUteqH1IwAaiwVPGvAOen_vzjhupo5JtbF5F9qCn9LvL56GK4n6wRlA9i37bUCEzAyVmlgx28Q7d3J9twZn10lGIzdcMy4zHLlf4Kpb10yVofuoQGTTfMEc0hUgSYQZYpTrO26gGWp0usWobP1a1db9Z_B9cTeTO7qhn9q_cuAFYE0DbKzb9MzwhT1qqyusrTFv9TVcuo-sLvmUAwORwRgENAdaSbkfEcfsf5LasY7Yd21AjLxvL55yqgkev9sgIaewiS8MC9E58JRGuXzVVMlCWnsjAbXho3saNOvqmnbqc9iRKPQzR7okuXaW9Gq5uvatM-xRBdXpkVz9yq-l5VptAm_R9lHMfULAnm9d5m-jBR0N0eVn54jZWDwTZp1HVmw6OioR6klm5Ax5wOv0mkHWr3UtbHlB3rLNQ5V2M_Vu2AEgxOY3JKYh5KVc_ZLkJ-ZXSoAO6CUk3duKF3eG4fq0GmrlDCeeojoSKoXe2OOH9SsP_hWF1elmhDh3HZlbwUaiwgF4N18_-N4RmAzSw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهارپایه‌خوانی حسین ستوده در جمع زائران عزادار حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/455796" target="_blank">📅 08:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455795">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پشت صحنهٔ خودکفایی دفاعی محققان ایرانی از زبان رئیس جهاددانشگاهی
🔹
رئیس جهاددانشگاهی: بخشی از این دستاوردها حاصل تلاش جوانانی بود که حتی برخی از آنها هنوز تحصیلات دانشگاهی خود را به پایان نرسانده بودند.
🔹
در جهاددانشگاهی صنعتی شریف، دوستان ما کارهای بسیار مهمی انجام دادند. یکی از این اقدامات مربوط به هواپیماهای F5 بود.
🔹
پس از خروج آمریکایی‌ها، برخی تجهیزات و قطعات حساس این هواپیماها از کشور خارج شده بود و هواپیماها با مشکلات جدی مواجه شدند.
🔹
جوانان جهاددانشگاهی صنعتی شریف که بعضاً هنوز تحصیلاتشان را به پایان نرسانده بودند، با استفاده از توان مهندسی معکوس برای بازسازی و فعال‌سازی این تجهیزات اقدام کردند.
🔹
این اقدامات با همکاری جهاد خودکفایی نیروی هوایی انجام شد و توانست بخشی از تجهیزات مورد نیاز را برای استفاده در دوران جنگ تحمیلی و دفاع مقدس آماده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455795" target="_blank">📅 08:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d701596.mp4?token=f4vSObYot64_EPGYVgD-ML_ttCmJxMfmqRUxOoNyX6QqnlfcUKKIACCtqvUQQId6j69U88s1xoBG3KtemBEb-g1N3VG4NsDFRZq-q07dgGxJWn1SZucs4f3s0QPr1HxCyLZH7_PR41U90ONLJCejHlbGxnIPUYWaDGswPBQFAJU8rZn_HWWuwPR4ePIiJTuaQp4DCUpVTN8XLQfYlff83buO06NccCZJwzDTNUrp-nffgos_ruwUSks24BKQZdajgalj7p7N73ZG95ujP1gMQEQZQ9IbeMU_lCXk80QE7b7nz1OsPkkNGkGST1jGJ8ZbtzfitL9ZOKE5oTaMwp05sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d701596.mp4?token=f4vSObYot64_EPGYVgD-ML_ttCmJxMfmqRUxOoNyX6QqnlfcUKKIACCtqvUQQId6j69U88s1xoBG3KtemBEb-g1N3VG4NsDFRZq-q07dgGxJWn1SZucs4f3s0QPr1HxCyLZH7_PR41U90ONLJCejHlbGxnIPUYWaDGswPBQFAJU8rZn_HWWuwPR4ePIiJTuaQp4DCUpVTN8XLQfYlff83buO06NccCZJwzDTNUrp-nffgos_ruwUSks24BKQZdajgalj7p7N73ZG95ujP1gMQEQZQ9IbeMU_lCXk80QE7b7nz1OsPkkNGkGST1jGJ8ZbtzfitL9ZOKE5oTaMwp05sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین تابوت امام رضا(ع) توسط خادمیاران رضوی در کوهبنان
کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/455794" target="_blank">📅 08:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105c882a85.mp4?token=el6_0lG3ZHf4M1hUs2GS2r1F6FI1ghzZ2dnmF1NCF9ii9RXOkodBFeXSC-1RgCVT6iDycFDyYU2wE2tIq_Rh1exrU04Jh0CtzLoOsgT0KDtB4-5HCOQ8o6MtNTO9AliRby5dufYKX71zE3itcie6l2T_ijQJ6PaAruc4DyWptzze21yYCHiAHQHBT5FEtCp2RyZMdBw5wuUF4EYbbXFcgpYAbaUwTSoSn2oEGmhTtsIYducSC7APP0Z3pSEDBpYQl9IdFyjcgvYO2DToDYDDky0yas7Xghxcasm67udpRQ4kaSW3OZxmlkMRZmNXmRPJWjTFVg2A9DgB4IhQvBrD9AWm4nqnMYIKpf_pk5m6qdRhHi3_fAkkAHP3erUcC9bka57kPTW2smGgT9QLLhjzC85u1gI1YpEmPOuz8JtqydA7pPOev3-WQgK7ZmdlC4F5kFAfGWuQp-zdx5Ra_j2zHWNq_Ac3w7qm9GhlMj5poMWtzRnzFO-5Rvk_NL1uoNPRCJE57ZPZWvWTzo2_MB-90ehR3gjRqew_p9OP8Iufu0e8YHcoSRK7OI2tOd-m_OSTvNKTtV0MYYGuEOGeWOAFUbq4O0cMFIH1Jzfsc3C-uLiwVPydOmE9zhx_Y_qr-MCfG_ZxvfG5mubCtDo-nFbAZUNZ4V-ezLuNdjGS88GhUYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105c882a85.mp4?token=el6_0lG3ZHf4M1hUs2GS2r1F6FI1ghzZ2dnmF1NCF9ii9RXOkodBFeXSC-1RgCVT6iDycFDyYU2wE2tIq_Rh1exrU04Jh0CtzLoOsgT0KDtB4-5HCOQ8o6MtNTO9AliRby5dufYKX71zE3itcie6l2T_ijQJ6PaAruc4DyWptzze21yYCHiAHQHBT5FEtCp2RyZMdBw5wuUF4EYbbXFcgpYAbaUwTSoSn2oEGmhTtsIYducSC7APP0Z3pSEDBpYQl9IdFyjcgvYO2DToDYDDky0yas7Xghxcasm67udpRQ4kaSW3OZxmlkMRZmNXmRPJWjTFVg2A9DgB4IhQvBrD9AWm4nqnMYIKpf_pk5m6qdRhHi3_fAkkAHP3erUcC9bka57kPTW2smGgT9QLLhjzC85u1gI1YpEmPOuz8JtqydA7pPOev3-WQgK7ZmdlC4F5kFAfGWuQp-zdx5Ra_j2zHWNq_Ac3w7qm9GhlMj5poMWtzRnzFO-5Rvk_NL1uoNPRCJE57ZPZWvWTzo2_MB-90ehR3gjRqew_p9OP8Iufu0e8YHcoSRK7OI2tOd-m_OSTvNKTtV0MYYGuEOGeWOAFUbq4O0cMFIH1Jzfsc3C-uLiwVPydOmE9zhx_Y_qr-MCfG_ZxvfG5mubCtDo-nFbAZUNZ4V-ezLuNdjGS88GhUYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی باسم کربلایی در نیمه‌شب حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455793" target="_blank">📅 07:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RavycDvN0IFC2uH645wAb74CGP5bi-cIQblnI-2RNDePwXDZLZ9LsaQIWCT4N7xXmg7IdzTLepy_rRh9nDhQkxTZCTggYd-LSuBIvvwX5DXJOUI5NrygDWvnyAKdLegB8IYmQ88e_ULumDGvgvDc55AoGmYcECYzHSmTSUiMcv9CoVT_S0foSDAtKIYrbrHQMHTRVZ76EfuVhVXKK5nnIje44Zn1krIZhe3LlRmZ7nan5n3tXLRZawOo1qGBAerCadDV9Sg9J_qIujOoHmMWKUP8YdBRrl1AJEKnMI7weCEPeXQeSbF-WirFBYBxyKGQsrQtGIs6W0hFMEiqA3crIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: کشورهایی مانند فرانسه باید از موعظه‌کردن جهانیان دربارهٔ «حقوق بشر» و قوانین بین‌المللی دست بردارند
🔹
این کار یک ریاکاری آشکار و شرم‌آور است. حمایت شما از نسل‌کشی اسرائیل در غزه و حملات تجاوزکارانه به ایران، هرگونه برتری اخلاقی را که تصور می‌کردید دارید، از بین برده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455792" target="_blank">📅 07:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb2SlndEfn4k9Bz9wvibgWWecZP2yeCKMK7Bm3aP6AgGn3uPNpS4AKeRwB7kcev4mDtp0NmGB0SJiCWBMRQQyXZr5yrw7vDEGNbY-jfL9DPgAbZycVwfAp0Eggw7lXKLIDz1J5_VIXlyfpClAIpfxdpzk3MtUhAjIRiyx8FWQj2qIq6uNsrD1NMNT3DZOgK3RTgz1UJEZDwms47WhqImGxdrJ-59T-BKuwjFOZW9cssgHPctgKE8QGAr4r8rTosEczLTTHmh-Q1HcI-qJT2yiGYLzZvnkCFwXccehgQSnfkvhNTb-WQKD4mjlsf5bu4TK9plcup6jpNAJk9rgIWQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر رفاه:
کالابرگ مسافران عتبات عالیات و کشور عراق حذف نمی‌شود
⚠️
زائرانی که پیامک اقامت در خارج و لزوم احراز سکونت در داخل کشور دریافت کرده‌اند، چه کنند؟
🔸
کد دستوری: #۱۴۶۳*۵۰۰*
🔸
مراجعه به دفتر پیشخوان دولت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455791" target="_blank">📅 07:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455790">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQd8FeYdkIN4zzKjz6FHMRrJjCgh2A_HZaCCH1bRZO598ZKciYqch9QKU6HqWERlZc6mkUmvEhDuVn8sFM4ti8pz3wwqk9dLlzI5T1FzFWLxVUi20RFeHb9FExtSVBBLdIgvcIXvsdPqQx1G8iLxQP6PU4UquOe4QJoTq2xNjPh5Qxx95mO5HJOLTAQ66jpjB7UgoOgML5iKdFjpGY9lAZE49YE4upxS9xHix4RvNy-NeN0V7CONrci7nUQdNyi2Kq4tx-DO8iB0WeOA-A_DFHyaeRmJWRlMpujj7su0yvGOwOAYOJPdm0qX56RK0eg66TEcEfTwCD9YvsaiMeSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آقای قاضی» علیه یک عادی‌سازی خطرناک
🔹
با ورود «آقای قاضی» به آنتن تلویزیون، به نوعی فرمول آثار ژانر حقوقی دگرگون و با فرمت متفاوت تجربه‌ای دیگر از سریال‌های حقوقی برای مخاطب عیان شد.
🔹
قسمت اخیر این مجموعه به مسئله تبلیغ مواد مخدر و قبح زدایی از آن در برنامه‌های اینترنتی اشاره کرده است.
🔹
طرح این موضوع در قالب یک درام حقوقی مسئله را از سطح یک هشدار رسانه‌ای فراتر می‌برد. در این روایت موضوع نه صرفا به رفتار یک فرد، بلکه به مجموعه‌ای از عوامل از جمله نوع محتوای منتشرشده، مخاطبان و مسئولیت حقوقی در قبال آن مرتبط می‌شود.
🔹
انتشار بخش‌هایی از آن در شبکه‌های اجتماعی و توجه کاربران به موضوع مطرح‌ شده، نشان داد مسئله تبلیغ مواد مخدر در محتوای اینترنتی، برای بخشی از مخاطبان موضوعی قابل بحث است.
🔹
«آقای قاضی» با قرار دادن این موضوع در چارچوب یک پرونده حقوقی، امکان بررسی همین پرسش‌ها را فراهم کرده است؛ اینکه در مواجهه با محتوایی که ممکن است به عادی ‌شدن یک رفتار پرخطر منجر شود، مسئولیت هر یک از بازیگران این عرصه تا کجا ادامه دارد و قانون در چه نقطه‌ای وارد عمل می‌شود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455790" target="_blank">📅 06:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBvi8-VzAejB3WWHpBKHDTwI6WTErOL_q6EJluOZORddm7uHsxtV8NQjfHSbJtIIvxAi0BV3eVq7RLrUZ97LW11pHz_M5b6uUBZ0SfA_gQsCu2qsp0gOOauZU13tFzAlLBy3sFPqRWfRivo0SeOMX0XdOve1g8WAZlQyLdrplHnvREuVqhDZu5n91E68Z1vTr4Lqr7doxy1rknsQ1j91V3YeD0Jm9AkphSgqG-4Anf3lULOtEX9YlwgzSSBUH7TIA-9eRC3VHPPvR7oDOxPZvQBDd3w3kY8ciGPsBfjeS2tBSb57nbaRSdvlp4dQEZT6SiRB1pKTeqpx3N2NBhUDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6XQetQ9wvP8I1P6EbTf4WnHmOT0Y-6k6ij9hqkytwIQciDv3WSFK7SDgGYnFRbXPtxBO9EdEFRcx5NNuIVbMf407gbSzokPZnjxNLOaLfdSi-tQ5mrQaH2qY-q1vWgIDTKrcYrHwYCBHErw91E-SWK8NLfVSnaJTo8ZCZxUs7XLOYCLl5CXLCsPT138UAFkG2w50sXwI0U3jomHpUr8UH3R44lQaE0HH3TNJG81tC2DgI_ny4qDWSb2yGx34VM4qyObnmHa3-G2B51bMlzoJPp7NLa73Ju61EClEAE4iRrj2xBVofsMp6-PDIW4IQj2HPTKHuN0kpGhxE7YgW3sPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzqDfsweXbhbqXG6G7GdZ37L5jkJ9gTtplhCTrrtp3ovusL38CIWSsIAx60YF7Rz2R5DoLaZzBC1EnclrU9jKvkBD7Ad6RH6YyfQ5KcrsMX8KAwzUdv0M6e8M34ojM9YhCxfNmmT9aJ3gc_dFVSO4MmjT08vNMCnPD7RmVlFSDr6t08lLgIyGjzHQ7t5xZ0e64aUps-Dyj1B9vEQjMHbIWYhf9T_6utAsv75aeA4j6I0bIeSHcAVMtP0A-NUW6ZUj4fk9ZHnS3NdLQQtAHbIDaxVtSjw2mxaWV9Bc3QAoVA6-TOxHt3jm37RAHaHhx3k8IwTmCBKysFTa8O7yqM8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEUj3N5jYVLu0gVOXSbMpNct_Lq54HTt78Svae6w7PtyCR8cSkBBEI4cfma04aIvISivpPk34dyijPd8iRP-042rFXft2SVU1yb6w11BxSN_4LRCt1a0f4kCRd_CQNtQ9V-ADIsPhESZ9E01JfFWltfBB0Jy1JSU19eMOAkRs4483Bt9BCaZRZ419M3RyR5HVGwFWB0hsk7Vf7w4fjL-SJut6dv3k7armhepf-eplyukdqrlBcNyhlF7SXom6UYLT5Y-7pBU1S4qbqr7gdXpLkyauYTMvyRv-2TjAiExfrm-BDtE5rsuzp7T9jFkaxZHUpNcJL9mdL377T249tFgVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران پیادهٔ امام رضا(ع) در راه مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455786" target="_blank">📅 05:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تماس‌های تبلیغاتی مزاحم و نسخه‌ای که ایران کم دارد
🔹
تماس‌های تبلیغاتی ناخواسته همچنان برای کاربران دردسرساز است؛ فرانسه رضایت قبلی مردم را شرط تماس تبلیغاتی کرده اما در ایران هنوز بار مقابله با این مزاحمت بر دوش مشترک است.
🔹
در فرانسه شرکت‌ها برای تماس تبلیغاتی باید قبل از تماس، رضایت فرد را گرفته باشند. فرد هم هر زمان که بخواهد می‌تواند رضایت خود را پس بگیرد. اگر شرکتی بدون اجازه تماس تبلیغاتی برقرار کند، با جریمۀ سنگینی روبه‌رو می‌شود.
🔹
در ایران هم برای مقابله با تماس‌های تبلیغاتی راه‌هایی وجود دارد. شکایت در سامانۀ ۱۹۵ و در برخی موارد کدهای دستوری اپراتور؛ اما مشکل اینجاست که شکایت همیشه به‌معنای پایان تماس‌ها نیست. ممکن است یک شماره مسدود شود یا دربارۀ آن شکایت ثبت شود، اما مدتی بعد همان تماس از شمارۀ دیگری برقرار شود.
🔹
تجربۀ فرانسه یک تفاوت مهم دارد. در این مدل، شرکت تبلیغاتی باید قبل از تماس، اجازۀ فرد را داشته باشد.
🔹
حالا اگر قرار باشد این رویکرد در ایران هم جدی‌تر دنبال شود، چند موضوع می‌تواند مورد توجه قرار بگیرد؛ شرکت باید بتواند رضایت فرد را اثبات کند، لغو رضایت باید ساده و فوری باشد و برای کسانی که به‌صورت گسترده و تکراری بدون اجازه تماس می‌گیرند، جریمۀ بازدارنده در نظر گرفته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455785" target="_blank">📅 05:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کشف ۱۸۱ قبضه سلاح غیرمجاز در خوزستان
🔹
در اجرای چند عملیات همزمان و مشترک پلیسی، ۱۸۱ قبضه سلاح غیرمجاز شامل ۵۷ قبضه سلاح جنگی و ۱۲۴ قبضه سلاح شکاری غیرمجاز به همراه ۲۶۵۰ فشنگ مربوطه کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455784" target="_blank">📅 04:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCW1FJ1lVFnvuKA1NXMLo6LiCfD7Qz1IqWTz3Bp9rtHaeF_G2UOngKo6c_bvL48eZp223r5GRLOp-6D7nSoI623-DYA0JLJgvdEPLjhjousbuJ27Vw9Pl2IF6op1D7ACAPBQJBXBF_kyTGH9Nd7ZWKX9CZD3aZuaSZ5O8-HUaeUIipu75SACa3w9clAKNAi9zBTzl0GsUSh5uKXrhzqfKdidxtQTyQREJzEBpsDMExo74NdmC8_wUC68WU3mF69fRMK_Qora49Rl-1YMP5OSv6nCA359w43rvo2PIa2ra0g-IMj0ftQ06zZmcfbG2iG5SEphndZbCdVDXo3Ilag4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbm57Fm0VbFqlYtGawJ7NmXiu4qQ3BoVJcGg7ZNu65dbiKgcX-YtLwq3xBhNOkZU3kRIVL6KYgRg1iJ58tYDjdpyv7dK4D_JSc-SYVXNT7tEYsMiPGaUTjlu-2QwlX02Je8eLZzJ-I7QH55Kd5e1TnD0pGOh-0b3HSR8xe8aoWiDXZIl9X8heQuq-hRtFH1g8fOx8BATim_3jOp-NXfUNnRMhLs0ezq-X0eUN6ogIqKcLGyhF0fPPFVj7k2AHxELMs9kebvrWNX50e6RTxwiNwkLqDs_-0e-6YECsHFX7q49s081NtQ6nHonwA2OAltZLiG-1K6QIuzt02iclHwc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_N9OrHR85jwmulJbXEWz32kIx87dqlFvHuoh4NuU6h8DNc-wvE-q38bT8N6uawmbsvlwfTWLRk8EccIDtjhCo3tqxsiYT_p4Q_JcFyFCMZLdlpLSTdLszYL2DinctG3ICuHw3u9mwOip9P_dOvjFok2ujzElzMQdlad4J5LErLivBMgvqibu3TJarKh12ki2bIUIUNR8jdhCuMfLDrMsI2oNsZL7_bdOzG3kDKsdWQlCJOarI5Rhws4tfn1YbGJVEleM2pvMlFc2Ejhup9D8jHibgQYDZivUyKJVML6kisd_8tTxGeBbvXSl-QNUiguPYM3U9xil0zzdziGX3XYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzjqNjZlvYMzL786jZIgY929t3CQPOR9l99Le7zxuh5zomceHIqGCVySfQP2PxSvKaFKs_P-S2m56jSu39cvbyLmcid1wfILPUOLGchhnHo-R5hWRPQa02Ny0kf57LEwT6-JN7r7ur0tpAmCmL6VFht8UXNHR7Mf_ValtJT9IFwPjTcmcBiiRc72sj0O-lJIUv9feO8dRvYRH64I7P0HEeNJPQaAOFfa9EqDBt5U6dicyZGRQkKn79y2lXFGHWGmfZY1uGB-OVb74oOKJvQFpLLYWOtqm11LWWCE1P7TtV2Qlxw9KCDQS6q7laEu86eaC0Yb0mFMdRDV5zElvqtz8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع انتقام‌خواهی کرمانشاهی‌ها مراسم عزاداری شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455780" target="_blank">📅 04:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455779">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930bda4916.mp4?token=DdegjDtEUd6D68i7udGnUkEaP9g9sAj6MPiJTEFqKu0yw6ivwxjXM1xZoIHD4QkspLLKMdD4xG7_-0biH1BizVYmnEHOwX7MKj2X4ybHKdqP_dyCfyqvgAYxeJkomaQXRw62QrCeH0vlddrYZsJFvyX3BB_DL0WdFBVqb6olI-zqvgGofbhSmJUBUnSMm7ouf01EY5W40kvCYFcr4J-mh8h7VoTCGzBpVyZDg3c57-DnoDo0FFX4l-D5i6wX01rKYeFLSnCAgvk4wDNRopgnsS0BpQXxiAptTkYOfYqa2VODtM2lL3BaJvbGQiGLtNAyyWWAjfiAh3rm_W0M8JP50XeamqPHaeGRSQn8vvuaKQrSqMK51xkvjee0OguTZdRHtPP-MEFI5eVfBCRRQYm6LWmuFvybaFpL0Ilkjcz7jWJCkn8_3-r4_5xZv_wEHkZ8gq1h9y1ChxGLKhFSPpL7vwmfybUHVGDumnxFJBG9rwCqHhJvKH1rquR_fYJgu8tygYbXAyYJxLFoVyqBjiQqNJoTEmCy9Z0o10KVrT5zUbu-GRPvqQrL_4SNfBnJRhFT-k3AUOAUNi4kChNg_e_Lt9aRsRp4WiyMHda3vG_Jve21jQ8_PysySn6lD9gW8gJyAnwjfXET7TtqEXk8eJPpHc_6VSzHlqd5ODNos3qrdtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930bda4916.mp4?token=DdegjDtEUd6D68i7udGnUkEaP9g9sAj6MPiJTEFqKu0yw6ivwxjXM1xZoIHD4QkspLLKMdD4xG7_-0biH1BizVYmnEHOwX7MKj2X4ybHKdqP_dyCfyqvgAYxeJkomaQXRw62QrCeH0vlddrYZsJFvyX3BB_DL0WdFBVqb6olI-zqvgGofbhSmJUBUnSMm7ouf01EY5W40kvCYFcr4J-mh8h7VoTCGzBpVyZDg3c57-DnoDo0FFX4l-D5i6wX01rKYeFLSnCAgvk4wDNRopgnsS0BpQXxiAptTkYOfYqa2VODtM2lL3BaJvbGQiGLtNAyyWWAjfiAh3rm_W0M8JP50XeamqPHaeGRSQn8vvuaKQrSqMK51xkvjee0OguTZdRHtPP-MEFI5eVfBCRRQYm6LWmuFvybaFpL0Ilkjcz7jWJCkn8_3-r4_5xZv_wEHkZ8gq1h9y1ChxGLKhFSPpL7vwmfybUHVGDumnxFJBG9rwCqHhJvKH1rquR_fYJgu8tygYbXAyYJxLFoVyqBjiQqNJoTEmCy9Z0o10KVrT5zUbu-GRPvqQrL_4SNfBnJRhFT-k3AUOAUNi4kChNg_e_Lt9aRsRp4WiyMHda3vG_Jve21jQ8_PysySn6lD9gW8gJyAnwjfXET7TtqEXk8eJPpHc_6VSzHlqd5ODNos3qrdtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیامبر اکرم(ص): از هم‌نشینی با مردگان بپرهیز!
🎙
آیت‌الله فروغی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455779" target="_blank">📅 04:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D31QDD9pLu0NxtmolP2cVmkG0Sge7RNU3u3o3ZOxKT28kmazQ_1UPQ3nneAQXWHVD1UA5aiyG-Zd4G2V_mmjQXVOJUxbu9y2csVSWVq0xX22YZu0vSC7_MJxYQCRVlNdnzqL2X4IUtsdwre-vX54tB3e-zRTejRdXn5DdvhLev9TS1GwhvwQ_ecyowd0mVyxi_NxgVSmarXHEwtXelZUrd35DoSdLScxAeCbCc3g1OvGgBZgIc8Yz7-nn4yelgssvFkSPbuyG2093hPjaKENQs4cCBogjvLSn0DXePegNoUJlKgyY5fR1G-6YTwE7oC8AoDO0HOhxjT8KvUUplrLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آمریکا درباره تهدیدی که ترامپ را در کامیون غذا مخفی کرد
🔹
یک مقام ارشد آمریکایی بامداد پنجشنبه در مصاحبه با شبکه «اِی‌بی‌سی نیوز» مدعی شد که نفوذ مخفیانه یک گروه ایرانی به ترکیه به همراه موشک‌های دوش‌پرتاب، رئیس جمهور آمریکا را مجبور به تغییر هواپیما کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455778" target="_blank">📅 03:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSfkBBivHq0TOAZTEqO4sQ3DE2lBClGffZ_Z66vbGW6LUlV2eJhzcdl0fC8XY7MgAu4XgmkSViZDjNkyt-iA_cpnLueJIBnGCN8zgQWUNX2jJxFFz2T6G0WnNYHcO7pXXSEEHwWWlFpJ6Eg7xmqTujH0eTsZusEx-OdNbxGhtIwb3l24L_PQq5x-MR8wWCL48OJLP48pz-YCoERkeMeK9LwZ2Nh2LzjnYzB_ytTl9NbxdALRpvwZClaAgAktn3bMEEEdKtcfwI-ygpuCIWdFm1VfpLF87n55EbyAEG43oUSXcS9XhHfmiLZI2va_E-7YgKIeriWrW261k_1btJNykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا: خروج از عراق تا ۳۰ سپتامبر تکمیل می‌شود
🔹
خبرگزاری آسوشیتدپرس به نقل از یک مقام آمریکایی گزارش داد که آمریکا در مسیر خروج تمام نیروها از عراق تا ۳۰ سپتامبر است، که به حضور نظامی در آنجا از زمان حمله سال ۲۰۰۳ پایان می‌دهد.
🔹
این منبع که نامش فاش نشد، گفت نیروهای امنیتی عراق، پیشمرگه‌ها و نیروهای امنیتی منطقۀ کردستان مبارزه با تروریست‌ها را رهبری خواهند کرد.
🔹
همچنین در این گزارش ادعا شده که همزمان دولت عراق نیز با فشار برای خلع سلاح شبه‌نظامیان حامی ایران روبه‌رو است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455777" target="_blank">📅 03:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1c2852062.mp4?token=fPxbsuJe84suONwbx2vGV9vOduI02CXJ0ye3AKywdD2ChWrZAWbnHIHgfc0OM_Gx-cIJYobMDlg-9ThzxxIrzc5iWJ-lw6vLrdxixc0Lb_ttg2980zN_mGWis42BqfrZFrnYK86eznAB79iL5z2ooK1PAyvf_3c_3jeMejVDZ9na0j0s2JfVsSk8xHIM6NUyxBshj6D6e8gSEQvPFiBUrA6-m9WEPLTh-zyM3jfEjLQyGJt_9BbcJAwqLShWBN5694xPiozWPDOevY8XLQyS8Hxm5p21_UskBCtoz1-kA_tMf90qeuR-A1ypiDDHSlQf1FqWp-n1pUN_iRyMvFKeVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1c2852062.mp4?token=fPxbsuJe84suONwbx2vGV9vOduI02CXJ0ye3AKywdD2ChWrZAWbnHIHgfc0OM_Gx-cIJYobMDlg-9ThzxxIrzc5iWJ-lw6vLrdxixc0Lb_ttg2980zN_mGWis42BqfrZFrnYK86eznAB79iL5z2ooK1PAyvf_3c_3jeMejVDZ9na0j0s2JfVsSk8xHIM6NUyxBshj6D6e8gSEQvPFiBUrA6-m9WEPLTh-zyM3jfEjLQyGJt_9BbcJAwqLShWBN5694xPiozWPDOevY8XLQyS8Hxm5p21_UskBCtoz1-kA_tMf90qeuR-A1ypiDDHSlQf1FqWp-n1pUN_iRyMvFKeVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانۀ دانشجویان مشهدی در جمع زائران امام‌رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455776" target="_blank">📅 03:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfHsBABjOZUAutWZOCZ2ai2KzvsraaNwNUY99mYEysovL-jSG5gQeoON64cvfneoB1Axc6ebbNi2s3KTVrsZNCgcXXwgkNLv1amz4Uzllj6GY_TU51VyU6V1QyxtQR-t-zaunKeHcugPBsl7T5zSMNdDbQflfe8OkqpFkQLxKn6aj6dgZzBAv6bM6nGK37JGnqd7_M02QtfiA-iaaUqaNnOWHXnO6i_A2pYK7EQ37S7lhkg16SQWj25F8meMjyYinTBuV1nJvNaYzACAwb7m2s5f78CvXQ0XfTz_XfwSV-eZMTTm7e8eUuab3lzE1SbwQVMS8xfuYYdhi0TjcSjTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhEFWBRf_baBNPUeRNUtcAy_r6KFTHDHrMH_TO1DZggnsfcLwWo1yzKwGkvi5Nq3CDCcr-KI0UIG31-KsR2drrm42M1cNbjSEE8-Y92B3LoHnJaUsqj0Rj313sK91_bihZfvIyX0ebdUFn6lkHZr8WuyKn3KfTj3Bg3bo1_rGxpczILkS7MwMbEb7NLiznfKmBPd-63ZSzUynreeaAzA6gqCJGs8Uega__2BwXZw6glxD-QxSLJLS5Jsd6HS31CEhZ7wSCMe_BZpmKzlvWwiF5w5bxKqkL-swPLpXTdotvFYZo904seaJmZiQXpSK3QI_T72qvanyFV01vgDMJpWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jkvfl0Um8f5fideDsUKHnb8EvsnA51nHOWRSRB1_SNeC3exOyQdHsM9n_j55aMYa4R8kfCqbXqn9wFFl9kvIWV3rD132V4dz2NXcLIaPpEJOxODO9F05uWgkWD0zebKPeh7bOgizEGc3wcgXN67N5uibzbnvHnHNkeqbG739cryqGyTsgAydh6jsTwMtxi8Duo83LpGGLIooX2yFPSDGIb9joPvDuTSuqIZFp1tVWAQIOC-s7oykP7XjYiv3ncY__GzM_1wbTIHoUWtzWDCfoY4ewBSyZ1rqcezTkYObbIPai1CZGyCuBXp6AF-MSE1PGuKkR1BlCcrQi0477YxOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlxd5sbwukOBDB44nSz9a2OiaELr633haWpsguy15_2kqOka04Iu9bnypb8Rg_Plw6EZHMi2ipGOLe7PPl5wJr9C81DFmMBzyBB7ImoCcTv8L01ayMsIlDc1ePAesHV4tH-P_e67KYPWXcPV5dQnv1LOhlvDwj15lleGHT2V4eti-QfpnHpBH2Z5H7ORXTfzchoO2aiLnUstuurGqbcfXN7xs36fVgsA-t6CClDEmej1GzccWrgbnoGDRAlciCQeTNItAhSJs0rTf_dJ8y3rflui_TIFPsC9FRDRRehArJCaJ0BMcri-9pVWkDjgVwma2OTz9EMtDW6StJ7SQLfVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncu4Q6zdTquIEJA9Egt9AgEgFtPzUVBDXfsAvDFWwz3TJ4AF6v33D4Art5NVOwu7I8_iMWhKKBIrgH7HRHv0HhbUu7yrZ5l6y5iZL2Q7VjXmJlDBjHjA12Vai9EpRGIMNvcBBk-o-IjnHKcC2Ddmt-1CjtNW5n0R89rXYh5z_gywLPYaTTpzwSFgZkWMlWZmSn29YhpR8Cr165wt4B5baOLK85KfVGT7gF8pdZsLCXkGP-yA7LDJ7zILF2qQ48QyizeBzxX2HCSQpvam8MB9f9QVPuNshaBZ_0-qAyILVxE2ze8ZU2mOVVqjWWXK6QwZthSh2Rtj_yLVCIJE7eRIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpgQBTxnmpuvQii7N19guRx3-GCuI_EMVnyOG-G2AMtf78_GX6lg05BxE3IKdqgjh_7x5pr5m61VML06NV3qEKuJXCR4BaCPIv12-QMPizi5J28LSFhsy4v6l6SipxUgEKeKALR9cmV4KnDjlwyPr7krBqSeacMiutob0RyRiMQEtSD3YJy04mEn3k6ggH7wgPbXKKn9_U_s72uVL0KmDeGgpQuIyvKaCi4Ls5Ah8PM_rLQdzVdsfk7s_u4kYPyHXa-tHLqI1MEycI4Ldu8aPgaymLeRz4oj929yq1M54gTchTuaPv6xrMWRKLPF9ZL7ivNBBJxKlRgZtv_NcJ4CWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doDwM3mE2lskPV15ubWJ3NpFWZSrVgfvWjnkfwDUXfIoUvHu5lumjCpjUb2BMOmv5FObxhlxpf1mvuCJjlr3Gjv7bG1YwWmFD8xqMJZZROxwjZkTU1T2nQqXf9pX6J82iNgoMHPrRceV7ehWlf8oq2_sFZlKNN-7LLklbihu5r2maNykwuLtdlk-A7pVYGtwBZGCQU0-M3mAB05GX9hyMxZFVA-pmdKcnioCyJHnKclzx_P5Vn-Z_Lt4HymwVJ9V7zFKj_qOz0goPQbWFJroyK34mVObLkxcGtLoHABLJjiF7UR_2TmEmzcshuFDIBAiEKg7RZmwImSyp4IfVLabLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از خیل عظیم عزاداران امام رئوف در حرم مطهر رضوی
عکس:
امیرمهدی آقاجانى
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455769" target="_blank">📅 02:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455768">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb3JnHl4WvvAIVCsZD-vrdNMpatWQE2KUcf64l6M8lB3EH07mQMcEmh99sB2REo6P8_EBn09eiApnhoQsNVdWqTdkw3dE4Si9UYM-TpxgiluzsgiFEuJHsHYeg3ZYtf8Ih4a97iABL30-CkpwivOUZaCTncMY0W06YUrw50R_lWCoh6006UfcQJIsf84GGaq2kEG4ICbPf0XTcn6NaRZVl-m0apOoKlmAefYjCd382F2ZVfy4dHye5NnKEuKqSMXaKTusBmYIhIIz9WURMjIt6dv0g50kPBnS0IAbYuLS9tlGSvZFCo4Rkl62qWxND2Lf98ZA5oNlEilfrh-sNjEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدردانی حماس از بیانیۀ محسن رضایی
🔹
رئیس دفتر روابط عربی و اسلامی حماس از بیانیۀ دبیر شورای عالی امنیت ملی کشورمان دربارۀ لزوم تن‌دادن آمریکا به پایان جنگ در تمام جبهه‌ها قدردانی کرد.
🔹
در بیانیۀ حماس آمده است: پایان دادن به این جنگ‌ها به نفع منطقه، مردم و آیندۀ آن است. ادامۀ آن‌ها اما فقط در خدمت برنامه‌های دشمن صهیونیستی است که مبتنی بر تجزیۀ منطقه، بی‌ثبات کردن و از بین‌بردن منابع آن است.
🔸
پیش از این سردار رضایی در توییتی نوشته بود: پیام ایران واضح است؛ تنگۀ هرمز تا زمانی که آمریکا به جنگ و محاصره پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و با آتش‌بس در سراسر منطقه، از جمله در لبنان و غزه، موافقت نکند، بازگشایی نخواهد شد. تا زمانی که همۀ شرایط برآورده نشود، تنگه بسته خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455768" target="_blank">📅 02:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmBYDVmlcllKiyFdi4VSkMKAWbJlym_U6Ss5XKCPd5itOJs6AmIgX_95pP0KVowAY3FIG8N_MljoP2Wz7UXZk-3SHMui30hS5fXvkWNThyD0jb5zna2drx75MQfMkTAJKpyoIPtfuQz5stoi_xoIu1DVXemamb_n5ZMOj6aJUcY50Q2qshZEp1pMb98H7ZYiNa0fcKAB1aiuTzP398Ou_yJIGAYPY2W0v2qwQlOmtF_xgP6huZ69Ku0en08NlgCbmKXPkrh4067gpxvKMPGeh6VbkGDZixLfMSVgaet147_BzWX8ysdpPBNgyYBxicSLwNBtp3IfAlTROwW1GksWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش منفعلانۀ دولت لبنان به باقی‌ماندن اسرائیل در مناطق جنوبی
🔹
نخست‌وزیر منفعل لبنان ضمن اشاره به تخریب سیستماتیک زیرساخت‌های شهری در جنوب این کشور توسط رژیم صهیونیستی، به محکوم کردن تصمیم اسرائیل برای باقی‌ماندن در مناطق اشغالی بسنده کرد.
🔹
نواف سلام در بیانیه‌ای گفت که حملات، تهاجم‌ها، تخریب‌ها و ویرانی سیستماتیک خانه‌ها، زیرساخت‌ها، ساختمان‌های دولتی و اماکن مذهبی توسط اسرائیل، نقض جدی اصول و قواعد حقوق بین‌الملل و قوانین بشردوستانه است.
🔸
وزیر جنگ کودک‌کش رژیم اشغالگر عصر چهارشنبه با حضور در مناطق اشغالی جنوب لبنان، مدعی شد که اسرائیل از این منطقه خارج نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455767" target="_blank">📅 01:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGJYHpBxBCSWD4jT9TD0yuQVUnl6DGmfmOGEPGsQoicEASUZLiTpg5WIEUm0GNPO5FlrqassL4yv7krm0BcWb0kDuvjne79MYOiJXNoPr0_WxwaSvUS7JIRFHpuU3AhQWYRW9jYpBD7HCzsX6n8MCkRvBl6LxOfxM5NWYzqPkqPEV-BPrFWF59ZvuY0--wFqATW19qM8bwwFrAgn4toopMSMKV0F9jFE3BcUHkDG4OSH81Bwd5gXsaUIcQ2I8tuF7_NkZ0jtBMyqJh-lFjmvA667DIBjrKv89nN5HiAAuvtuz6Vu5doX9uWbg6BVXFHa4ADuSb6VdMCDMQ0xbk6rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ML5CePI1lGew-P2sJq0kIPJZd4bmhntPFPOqbZdgvTGt3dqqBPhS1QAE4FIZddVeMjhJM_SRsTCgGmGbBrlM9V0IMDKd6SYBlNYIEDn1RS5kr6vwxqjMl-yneYd_ofVPV6TGnzHDuvu7TXd6yhdR34ZQiiQjSIm-bNvrGhJedYF-ekWuOkuRKZVURIVs51QEPliMrdxonzQAFth7pLMr-oKby10z5Qizh1bTDB4QvPTqOu_Tg2b02uvja1sb44T0uKdT0mQy0jI4QY-t20MVQ9J_Mc0Bh4bA9aKWtn4nfj19VJq53jeTjgV17HBQeZZGw8JBzIJ4_NJ5_kdc-FaazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyB_8AuPWKB1fAA-uqqp6OhnRqyfjQwXeiVY4ubEyalG73uoaBGxOFAmf6sNK4ZFHiDAmAVYkEs18ZoE-WOrQkAiXqDECKZmc95CFwAKn_wKB2y6Rtx65sJTn0GDL4U4V2icJr4aHiZCt2tUnzmiQ4n0H0uTgAyP45CjWxGOTR16g7w1Jx6EGF7omdW1lIdNi_-xNdKAzvTPeA5LpESOrFD58Dtf8S_94O30nUt-bX6DR71vYCB_9Q61z8JbHsfJjbI5by4BQJ0_pidZp637DZVbSEHQtGaJ8mTyfPC1lQ_9JzXnplAOrBNhCkoT9bzxMwpGguLA4BZ4Xg3NWw0a_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_Ndx5N8sc8IXL0EhbjnQHmDBurtRQMZ1IY77dpcjENu-9-bSbCnOggC4eHtEnHH39dY5LoqpsS5cYjZxABTrTRM3IMki9cx7hdtHZoJlhbDs1pd2txQg0tn6ZiW4W9sYY9QfPKkDL3kR_6yTQth6HAOR5UFFiOW7n7-tGdX-FVASxBdXDWE1XdAUEhqIhp-8cmW8Cwrzmgudgn_5cjVpMqa2YIt5Phglxp5FuL-Gy5Pp5tXDAHGKnUP8DAC7H9n61JWcaYjm9sADL7VKZYN9mZwbyFXlhiHL4xnOKHtf7HSe2GY36CqV6pbBvjZkmZak_cp6zqleBuzvU3YNl_2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmCsIsIcezs75Kt8mi0KSphPw-bRtEQKGINVTvDeaT_6CszG0OPd80BgbAatOzE4rIKM7DVxbNEjQTr3J2h-kJJHf--DYakaubb4r4fRSoU9YFJIWnDBiy33XfVuMApBqRm2bgpbTWpWYIdk_qNrBd5V5HmoyFTVyx2nhfLFk6JUnOrZRRZX9G66pvfYGg-OvYSLLpz90JYDU0AF9vjbNOxjFXDKOSLMAPmB1Cr---P1GxTzuyO_nEmoHpCDfVAPWgj1Hr-5Ih21N3URJNscXsVNVbNhJTTnB51D-jl8NCTJgUfUq_m4Q21Bc_OlUCFE_mtEeAJfr4FweqAfif1jDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم چهارپایه‌خوانی در حرم مطهر امام‌رضا(ع)
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455762" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCP2QLB8j7gjiJuS0ELLn6xgIHueQSOskevXTqEhRHiVniytAJOukYV7Ag9voA6YoiJNNx_f1ybLjGTrkDkJ-x04HjQ1xH5MLfjaHHwoeFhwuZZPxUVp8Che6esJ7b87oo1_l-pdkD9PPTSKSzfezH5j7-r-GL1REGUvnnC0n2ACrvtz3ESbnRhHBi-GUXykFOcUfnLVqK9wK87W1sZQU0NyfP3h-5iRrMvR4EAPe9Ut3bCGR_UBSk5oztHiXxElulx2zhZRomkemaiJC9gspJEefRemLh8aut6tMIpionOlje2rQspwdNPa_RkPvmzfJtqZh9gt0wOnJBzZRX77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات متعدد صهیونیست‌ها به جنوب لبنان
🔹
المیادین: توپخانۀ ارتش رژیم صهیونیستی اطراف ارتفاعات علی الطاهر را گلوله‌باران کرد.
🔹
همچنین اشغالگران، ساختمان‌هایی را در شهر الخیام، شهرک حداثا و منطقه بین شهرک‌های مجدل‌زون و منصوری منفجر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455761" target="_blank">📅 01:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30da54c2e.mp4?token=RuMkfrq4VRIF8L17HJs15KGWyF1icZk207ncqtCSe_MBJ-mHx9Ll-2nMunAWA32xTIs2HZLY2aLxFbs2lNjyhE_A38ryX90Jrc7Yjzy6NQBQY2e8ueF1RA7n6-vSNV8cGgOPWRTSWuGuFS2R340n21_YNGLyql29h7uP_VQ8dZzYOsW1UkAdeZ-7FrACLWOsxKL5RlqpXy5_7Oah2Tdo2M5lZGkZ_Og4GB3CbGALUBqRy_FhxnmKRnIz3gDMgqDJuNEXex9BTiayp0IOxco7EtsU8b4LAVwJhLtMnQQ3ELqtgRi8DNVshUnzuX_GjmlBEpirLSTo3ABcSxNrPGUToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30da54c2e.mp4?token=RuMkfrq4VRIF8L17HJs15KGWyF1icZk207ncqtCSe_MBJ-mHx9Ll-2nMunAWA32xTIs2HZLY2aLxFbs2lNjyhE_A38ryX90Jrc7Yjzy6NQBQY2e8ueF1RA7n6-vSNV8cGgOPWRTSWuGuFS2R340n21_YNGLyql29h7uP_VQ8dZzYOsW1UkAdeZ-7FrACLWOsxKL5RlqpXy5_7Oah2Tdo2M5lZGkZ_Og4GB3CbGALUBqRy_FhxnmKRnIz3gDMgqDJuNEXex9BTiayp0IOxco7EtsU8b4LAVwJhLtMnQQ3ELqtgRi8DNVshUnzuX_GjmlBEpirLSTo3ABcSxNrPGUToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🏆
لحظۀ بالا بردن جام قهرمانی توسط کاپیتان مارکینیوش
⚽️
پاری‌سن‌ژرمن‌ برای دومین‌بار متوالی قهرمان سوپرجام اروپا شد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455760" target="_blank">📅 01:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e503c661.mp4?token=AvmAdqAT7qleUJQSwCuZ7MEbrYa3JT3_3o6j0dhCvZjxuuVOlPKG7vDTaAXOWcT7MaVjdiocu63lhieadtNi3QUCWuY6tgITHjzkGPzBaHXxsi2T_TwQg6LsSR9KBJc5V5HbOTpIv9pWzVw6XBqvo2iDf82VKFhTorQEs5cuPw1-eXzQqoNotCPe42VbdfHtXFjrNCY3dMOksYU7rRSCtM4iGX0QRC7rDomlTe0WOcb5TvwxrWa3wUCS3vmRGyymY67eAQmovfGf7I54hu7lv3kfeS_ymM01bjTsDJvbtgrrJn3GzFdcUvJBV4cyrpfyqcW14mWeYEBLsElh5FC7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e503c661.mp4?token=AvmAdqAT7qleUJQSwCuZ7MEbrYa3JT3_3o6j0dhCvZjxuuVOlPKG7vDTaAXOWcT7MaVjdiocu63lhieadtNi3QUCWuY6tgITHjzkGPzBaHXxsi2T_TwQg6LsSR9KBJc5V5HbOTpIv9pWzVw6XBqvo2iDf82VKFhTorQEs5cuPw1-eXzQqoNotCPe42VbdfHtXFjrNCY3dMOksYU7rRSCtM4iGX0QRC7rDomlTe0WOcb5TvwxrWa3wUCS3vmRGyymY67eAQmovfGf7I54hu7lv3kfeS_ymM01bjTsDJvbtgrrJn3GzFdcUvJBV4cyrpfyqcW14mWeYEBLsElh5FC7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی خاص از خطبه‌خوانی شهادت امام رضا(ع) در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455759" target="_blank">📅 01:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf11CtJLHnEedNgyEWVvTAQirjU5l3Rdz32rZyTq8nENU1aAASJm-WR6kgP8QwQm5cnEMjU2_0oDQ9aLeyx2EngWh-YixErLFwReL69gfl-8I9qlbD2ERWmMkIA-GTuGBsMYPtlsAMTto3sInWorzSJDTnSNNm04C-3hv0KKsy9B4a3cGj6MRLGyMQUTb5LaMwvVCzLnm2D6XS4UxnP5IY56otp_08mlTcHjfSLKA7547RCOt0aXlA59agwGcGfveZHJtOP_YQNRpdaCyMftSNKJCwi_RV_tkQriGGM6rKqRNH4ueVWgDSb_W9vXhqyTqMm0LcLHaHf6-K2LHwtTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساحل قشم آلوده به نفت شدند
🔹
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔹
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455758" target="_blank">📅 01:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تاکسی‌ها و مسافران در کرمان سهمیه ویژۀ بنزین ۵ هزار تومانی می‌گیرند
🔸
مدیر شرکت پخش فرآورده‌های نفتی کرمان: سهمیۀ بنزین ۵ هزارتومانی به تاکسی‌های اینترنتی، ناوگان درون‌شهری و برون‌شهری و مسافران در استان کرمان اختصاص داده می‌شود.
🔹
سهمیۀ سوخت خودروهای شخصی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farsna/455757" target="_blank">📅 00:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAKmP6fqCAEpx4JTLi7Oh06W9LzZlQxmrcMxL2PodoXxlT9GH-27wZa-gNod-W6El6bGnm6biHXZePH2bBnzzPSmorH5CVWQK1HHatSSwgwkeYx56Cs1nPWd3GWZFtMWs_KgCoKxdGPKza_d3R0MM_Etrft8BTxh0J0l2u1bCXkLIhgXjDRlB2o3Nqh60-wqKCzFshKnLu14b3b1vdbSqpdBj9anQkuAOXqDQgWJKao8fNi0svUbMrlnIPhS7qlJGm5D0GNuaJup2HiHRhfolsXAz8GgmstGRiBFbiFXA-KVHCAY8Lg3ZgDn8R0i_JOFmLNf7iLr99-FbdXO03Tplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکسی‌ها و مسافران در کرمان سهمیه ویژۀ بنزین ۵ هزار تومانی می‌گیرند
🔸
مدیر شرکت پخش فرآورده‌های نفتی کرمان: سهمیۀ بنزین ۵ هزارتومانی به تاکسی‌های اینترنتی، ناوگان درون‌شهری و برون‌شهری و مسافران در استان کرمان اختصاص داده می‌شود.
🔹
سهمیۀ سوخت خودروهای شخصی در مناطق مختلف کشور برابر با ۱۱۰ لیتر در دو لایۀ ۱۵۰۰ و ۳۰۰۰ تومانی است؛ در استان کرمان هم با توجه به اجرای طرح جامع مدیریت سوخت، علاوه بر سهمیۀ ۱۱۰ لیتری، ۴۰ لیتر بنزین ۵ هزار تومانی نیز اختصاص داده شده است.
🔹
وضعیت تخصیص سوخت به تاکسی‌های اینترنتی نهایی شده و هیچ محدودیتی برای تامین سوخت مورد نیاز پلتفرم‌های اینترنتی نیست.
🔹
در خصوص وضعیت تخصیص سهمیۀ گازوئیل، هیچ‌گونه تغییر قیمت و تغییر سهمیه‌ای اتفاق نخواهد افتاد.
🔗
جزئیات و شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/455756" target="_blank">📅 00:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d352a6c411.mp4?token=p3aYojDhLLD_GKzwCahir7qtqv7DXhKGDprNH87-mCSaA18Bopq5Ah8BXIDQmgv9qZA_HWO7bLbJuNolaRbpg9xk1EfLL5HUjcK1h1n3X3vKOgmm8lJToTkE2Y2jlUesXlMyh8VpcmJxkkSPZvZTuqqqsxBIkHX13gLbVqA1K6aI911IaMxApdbY1gIudL4hBkpB6hw4FsnDYyTh7kGFwNu9NYUbFeRl3QJubc839jZEsZIg2gOyunzAH481OEVrqLMr7-9cQF-jo2NV9J_UGyIJe5v6dLw0a2Wzp02S8vSvZp6XjIeGuLmLPr3653WaDdexzJ_lPKq_sTtIjqV-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d352a6c411.mp4?token=p3aYojDhLLD_GKzwCahir7qtqv7DXhKGDprNH87-mCSaA18Bopq5Ah8BXIDQmgv9qZA_HWO7bLbJuNolaRbpg9xk1EfLL5HUjcK1h1n3X3vKOgmm8lJToTkE2Y2jlUesXlMyh8VpcmJxkkSPZvZTuqqqsxBIkHX13gLbVqA1K6aI911IaMxApdbY1gIudL4hBkpB6hw4FsnDYyTh7kGFwNu9NYUbFeRl3QJubc839jZEsZIg2gOyunzAH481OEVrqLMr7-9cQF-jo2NV9J_UGyIJe5v6dLw0a2Wzp02S8vSvZp6XjIeGuLmLPr3653WaDdexzJ_lPKq_sTtIjqV-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی استون‌ویلا به پاریسن‌ژرمن توسط ماچو در دقیقۀ ۴۵  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/455755" target="_blank">📅 00:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjXR7JfoLMBwmA66g3Lz-WZo-cYy7aglmMd-QCxsApgEZEizIc6QbtPB9DsHlIjLLKQBdWAdkMuLKpp3RpXqtN2bGvdk3mo1BfNrPcieYCVfAbkbrGDa6fsjNv7WOzbsGiAjyPUH9yFdykuegcySFsntCM2EELIAQ5NEHyoxBEgY5imECbaMRDp8CrShG0R5eamDcRbwcWcGiLb1xHbQ2Ur1p5L80n_N9RDacKxTW2EiJ_wt-YUY053a7pta5Ch9-N7uZn4rgvum-nuHs7jfhNDGw_jmiN4VzzBLVRg8Q5MOxqsb4uBhd4V6eBavoHSLGXtCrmB0P_Hf-7c32ue70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای سلطنتی امارات در تهران
🔹
طبق داده‌های ناوبری هوایی، هواپیمای جت سلطنتی امارات(A6-RJA) امروز به تهران سفر کرده؛‌ این هواپیما دیروز هم به تهران سفر کرده بود و پس از یک ساعت به امارات بازگشت.
🔹
هواپیمای یاد شده توسط مقامات دولتی امارات  استفاده می‌شود و تاکنون مقام‌‌های رسمی از هدف این سفر خبری منتشر نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/455754" target="_blank">📅 23:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYSsSMX6l31N4rxeNFUVOCicOTt2m0hOoJonS8qVdASYFYnHQT_rzkIAj_kkGgEhcBLDo41yV4NZN5ZcT-HlDbYanPl25KsfkizoplHejrDIKcGgW-i1aMMvJ7wXjN3WUtoAsRqcc2rNI8RjT4a73yjL3CGj4wudHp9JKWulESm4C0pmSvd5aOZZ6nONe4AyNHo7o34rFjRMDaC8j-dX9qKI7zy0lm9bFB55HaRWh606k7MZKXay3WLVzE2DmJH9epnD3JjfZar_956g4t3T1vsU_TgE-xN_Fo3DNG1-wymT1pQqM3aYS5IEc0JGTtsgOQEoPuKvq85YnBwp_k_6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی کارولین لویت با کاخ سفید
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با انتشار پیامی در تروث سوشال از کناره‌گیری سخنگوی کاخ سفید خبر داد.
🔹
وی در این باره گفت: کارولین لویت، دبیر مطبوعاتی فوق‌العاده کاخ سفید و یکی از مورد اعتمادترین دستیاران من، در پایان ماه از سمت خود کناره‌گیری خواهد کرد تا بتواند زمان بیشتری را با فرزندان خردسال و خانواده زیبایش بگذراند.
🔸
ترامپ افزود: کارولین اکنون یکی از مشاوران ارشد من و صدایی تأثیرگذار در حزب جمهوری‌خواه خواهد بود، در حالی که ما برای به چالش کشیدن تاریخ و پیروزی قطعی در انتخابات میان‌دوره‌ای تلاش می‌کنیم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/455753" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455752">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807de0eb7d.mp4?token=gAHjs1BCU1aX-vjfOg3iqZBAF41OeTQsqUB-PQ69olzlFQFZ1-SMoFyb6LeH20WKuW-xncNGnm2vQdejbnuEb1hFgPKUzZA9jb3j-5mkgTgLfNljeGeTjROcR7m1-xXRGvUN--EVLbKN-_BvLzdnf4-9JYelV8BpU4zq8QSjd1AQZEBh2G451GY_UfDWVTpqxb_IaS1pj_0jHSY5kOkvw8Dld9q7BCEnCWBeEfMmEmEyhQyZqPhmQXvTWLFfnxlavlrzG0-vIzNSVJQZGHgxgzJbswb3QeUKxHsxVKldAGlD4crwjUa6CPFp8uefmNMrwbi3M3w4CDYZp7fA_6VOUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807de0eb7d.mp4?token=gAHjs1BCU1aX-vjfOg3iqZBAF41OeTQsqUB-PQ69olzlFQFZ1-SMoFyb6LeH20WKuW-xncNGnm2vQdejbnuEb1hFgPKUzZA9jb3j-5mkgTgLfNljeGeTjROcR7m1-xXRGvUN--EVLbKN-_BvLzdnf4-9JYelV8BpU4zq8QSjd1AQZEBh2G451GY_UfDWVTpqxb_IaS1pj_0jHSY5kOkvw8Dld9q7BCEnCWBeEfMmEmEyhQyZqPhmQXvTWLFfnxlavlrzG0-vIzNSVJQZGHgxgzJbswb3QeUKxHsxVKldAGlD4crwjUa6CPFp8uefmNMrwbi3M3w4CDYZp7fA_6VOUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پاریسن‌ژرمن به استون‌ویلا در سوپرجام اروپا توسط کوارتسخلیا  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/455752" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455751">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f104184f.mp4?token=lUc9nt871uT8UtgAy_X-OdhdKFrCGzR3Rh_9NQIJtuopeP3TEU7kGlAYWa8KzMBIfKZdQzN_BlzmiXxhST25fyzQlZ5n4GroucoaXXR_PFc_oN9q6nrP-OCH3JDhCyfC37R-L4XD4qExxEH_q3lyXKPLrfPBAlV88HHRrg7Zl13fRaNJPuw55U7su8xJ-0hNGvzwDNWD6eVIQzeY-J2iin8GTyi3kKuhM_aeqwOXeX94xfU4I8RIbKsxsUfTXdiA4MFl0Z4v7uGcOl7AyEiTJ0MKbb5aIhUEynwKtovG-SU6hpsUTuNdi0OkZpEvaqur9rZA0-7zL2lHB_SBBi_dDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f104184f.mp4?token=lUc9nt871uT8UtgAy_X-OdhdKFrCGzR3Rh_9NQIJtuopeP3TEU7kGlAYWa8KzMBIfKZdQzN_BlzmiXxhST25fyzQlZ5n4GroucoaXXR_PFc_oN9q6nrP-OCH3JDhCyfC37R-L4XD4qExxEH_q3lyXKPLrfPBAlV88HHRrg7Zl13fRaNJPuw55U7su8xJ-0hNGvzwDNWD6eVIQzeY-J2iin8GTyi3kKuhM_aeqwOXeX94xfU4I8RIbKsxsUfTXdiA4MFl0Z4v7uGcOl7AyEiTJ0MKbb5aIhUEynwKtovG-SU6hpsUTuNdi0OkZpEvaqur9rZA0-7zL2lHB_SBBi_dDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پاریسن‌ژرمن به استون‌ویلا در سوپرجام اروپا توسط کوارتسخلیا
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/455751" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455750">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a26d806e9.mp4?token=ei9-KTh2euhbKgvtgRFklZpGbD_bMCRJ_3iwVc97JwqFUfrLNWbwIKC1xfyV7Ew-_Y-exBSBUNH3eMgTwA_HxDF4U8SxpjAVdfoAyD9auJjgPibVsbSooW5OqQ2OozW2KaK-TaZ_vQPF88FOrjuodLraR9epBBAomRMtO1c2kKWLXZPCHxBKzgMFhpV4cEebOuyfijrhuw_Cq7Sjmh06vxC4sTvGiIz7haOgX7r2u2RmzCNegtYQyr8kfEv6pprWkdlEyisKS4rcIGYKsqXc_SM63hTNArlvuMYct6gD8OLutmFnaTKYnm2Ufhyw32nkMxegw5uRjC_bT6b5biz0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a26d806e9.mp4?token=ei9-KTh2euhbKgvtgRFklZpGbD_bMCRJ_3iwVc97JwqFUfrLNWbwIKC1xfyV7Ew-_Y-exBSBUNH3eMgTwA_HxDF4U8SxpjAVdfoAyD9auJjgPibVsbSooW5OqQ2OozW2KaK-TaZ_vQPF88FOrjuodLraR9epBBAomRMtO1c2kKWLXZPCHxBKzgMFhpV4cEebOuyfijrhuw_Cq7Sjmh06vxC4sTvGiIz7haOgX7r2u2RmzCNegtYQyr8kfEv6pprWkdlEyisKS4rcIGYKsqXc_SM63hTNArlvuMYct6gD8OLutmFnaTKYnm2Ufhyw32nkMxegw5uRjC_bT6b5biz0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها دل‌هایشان را از خیابان راهی حرم امام رضا(ع) کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455750" target="_blank">📅 22:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455749">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nugXHex_SGoNLYsFTfldRFUMBMLH499T-Tc5er4uYCefAQ9870MMwnjpUQFYSE1MmYhAOtBYwdqTWWkHjSTVkC3TsiOTgS9UndoML2WnxwMbva7wZwX5IQCq6l-wrxMlMVDm0YXrdKNArewy5AmjNz4pmleeX0EqX345DYwEvEOKZSbxOPo9ia3FlTIKF92IA75cAtsRLmtE960GivDmzEFuHf6X8sMMsg-4j0-bSCYcjjMtn6oO1GCfyw6S_8ugH0ikDAnYGZZYo3m_OVmfYGImLjKS8aAAv1leLY4HChu-nj4pIrHMS0p9hJFnbGinOFmPAzlTS2rQD5gHbd8kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصابی غیر منتظره
🇳🇱
ژاوی هدایت تیم ملی هلند را تا سال ۲۰۳۰ برعهده گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/455749" target="_blank">📅 22:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455748">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی نیروهای مسلح یمن به مزدوران سعودی در بندر المخاء خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455748" target="_blank">📅 22:39 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
