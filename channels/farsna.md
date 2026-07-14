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
<img src="https://cdn4.telesco.pe/file/jHvm9JOuobx8kcvHRrhlbzP0AbKrq46aRIinnbffTOa_mwjtlCIwGbIT6NfHA1qWRQGbEws7swxngNQATAVpdkzEaC2-oEf9Xzv3ppXZdjhNCF7cESbnN4v-7SLVHyEOQVFfZBR6yHvFK4DPPME2M5RMWRHC6wdVdnz9PPJsQdGRGpaFHnfFjsKoW5i3V-cK3xjnu8jSdHAf8et0F8oImaguUJt9ahCFfOACEYKtuEEdZc2cYY9X5naQNbfnm_TeFZELkeL8te6OzyfL5-Zy1OQFiySsP9k5usj--BgrVPMS4x4ECd2vPsM0fX5JUlg-3ISmStXpGTccYClFS1ZUvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-449890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازداشت ۳ گردانندۀ کانال انتشار تصاویر خصوصی در لرستان
🔹
دادستان لرستان: ۳ نفر از گردانندگان اصلی کانال‌های منتشرکنندۀ تصاویر خصوصی مردم، در کمتر از ۴۸ ساعت پس از وصول گزارش و تشکیل پرونده در دادسرای خرم‌آباد شناسایی و دستگیر شدند.
🔹
ابعاد این پرونده گسترده است و تاکنون بیش از ۲۰۰ شکایت در این خصوص در دادسرای لرستان ثبت شده است.
🔹
از تمامی افرادی که تصاویر یا حریم خصوصی آن‌ها مورد سوءاستفاده قرار گرفته تقاضا می‌شود جهت طرح شکایت و پیگیری قضایی به دادسرای لرستان مراجعه کنند. تأکید می‌شود هویت تمامی شاکیان نزد دستگاه قضا کاملاً محرمانه باقی خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://telegram.me/farsna/449890" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449889">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG6Iqw4aRup2YZdfpNbxPLqhg28_X_b3VlMMROjWEwHFDAaMhqpO9t5bFWpYCRna5GQypYJlvbLVPgMsumODWNz1TWQdt5TQFGnKFH6p-T93pZc7A8pkFWoFVs2aWVnuG0WU7ufOPrEhcEaIjPga4lGwXdxX5aHf4BMaPQZhMVv_5Y4cj4e6nE-5-v3vEjY8IW0s_BXCWEcKGYvFbt_DEjFkdrI0NtuZ4hZO1atzRD3qLL9asajHItRITis28Nnat-__syNHdNQrTpah_15NUuZMARYZscbW6Z7Ph3-aLilta0GFvPutJJ_1hwMTOzU6QHByO42vypvLoPCoCKSwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ شهید در حملهٔ اسرائیل به یک مرکز پلیس در نوار غزه
🔹
رژیم صهیونسیتی یک مقر پلیس را در شمال نوار غزه هدف حملهٔ پهپادی قرار داد که در این حمله ۷ نفر به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://telegram.me/farsna/449889" target="_blank">📅 16:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eba-jlDd18Vd0RvhGXIrTuedrcpgaxAVCr-XD_GGg3v8D2vAtpsqrZX1FTnh7h0H2-Yww3_vBDWKCRKCHbqszbxncpclF5XThzteqi0F2XdSGF2qzTe997XxuJCicWwc6J2vtN1LnhB2qolWOfZknfMv1n1nb02YKDs5NS9MHMhd0lpG5Q_vnb7yMdE-BAeqs3gNAMI2iHH6rtXAFNZc6OvMTAQPtjNNzL8flenEYytaAvisjsJA_4lJ-ZSEesjrz3VzoDfm61mOYw9EwMiZ1v927y1VyyHSw0b5meK6Tof94nE3R54PqH-M0QnAE1Fy9kC3rnsdryUS5EVz5wV3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMVfkXP0KN1prVJo5A7_VHcBGhjOgW0H4NsUGFHZXgyGGllYCODRWekTZkRUrmYclvHuS8hsFphRzUlUsYepYs66QWN9bUzVmAvhwrvqG-zWgAYxlgkxqgarQbvIr0Mj-x2-43DRmcp8iz0i1K1f2UUzwgUzgGkdNYVUoAKrpF2DQL8nyPPR_aEbIz2ipUdfyxZLPsGlRwD0RCoNDEQHRH58wH9hGWk1HQcPTiMSu4JkMZmV7gIQIih7fY9L2AJq4Kks0S6apTZAZP8wdqNKx74ldGeSXUnzJWULj1skiAoHkUH91PV1ANoiWt2vy-EHqVgPpzstQW6hjY0eyhfBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7NwdfIQlupul3RXa6RBBNs4QCo3Q1-2FAogKj_gI8bHbPihknCWqzu1gkDELJqwyi383OC8_FhrhWa93Ix6Coz7AP0N6umjG1DpDW8mGtSg5E7pHlgbEKFyFVZxqam_F2ATw1a04ZNU26aReF54oIOfTWOG0smJfREREf-tYCjTBO8uRP0Uk000LywuU0vXfBIgvjCkv37vK1YbA5Xn_xQNa7Vtw0YDZdLJi5FHw6_xSeOXMPN_WkVn9-fJtyHDXrQLFw06bp_gOYooj1O9P71qiC4RHAtwFpdW5NPSyWuVe0AFCcDks7cXoE79I3Girx9MlGdJOVrAWKau6IsstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOP3PmF_6sEpDq4BTilHe3ddFRWmu1rzPRurfi3uYKjc_oNVQ1TEq5x9q55co5MRnjUOeqQNyxu6c4jNlpH5Iovan8sUVh53rK1vr389QQcZlbKRS_skv4Hp1t5xFG6I3ML58-PmGRRJU8uv5U2f1iCJp3iK36DmFaN97blwsbB4oVphlqUCnVeq_6yGDsaFwT5uY5O1c-JCnYuYgtp6yPMzv78TceWWoh5qU6Og9FiWacYojLY-NS-8olHtfLxSL_yd4J2UEqkFvAtFlah00lvSQ4axY4zRE85ZKTm6Ysts9e1mLK0N6jjnLPzkOR3YKABpObEL7n5TYM7_LdsaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmj7BysSPHF-D15h7EgcAxw775Ne4m1SR1YK_KZova1Npjm19SLwEhj5RyFBrVm5EM5_KZtHTl-9m3_5Vm2WNoA3khN_9SEbNBqQOD9ZvIbDvrpL2hbPIcxKhJOUbhYeRxh6Fu7NWF4WelZvf3AiWFI1205DCrxSr6_fa_DVoQkOWCw99ZPIrCFmaRdoy3ksVNADe_NDxVsgqiSYznilvfYKrYciTUGWUGwgeIPreFlKa78iIuHYA0InNiQG4_b44dP_WJOPBqyb-exnjPKlZn7IhPf8GMda2Iv-yrLrC7YTEOVlrjetrl4YncqN3_4kseMwH6ny0USaSBRXSL8QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNx_aYxMQQISKQufCn22emvKKHwEtXacPCxOM6d229sgAPb5tJn6V1VsrhPqqYqRVKQo8PkqzMCFHdIUgcQfWmEQLbnW79dI-yHTsM4Q7ZaNX0iTF9duj_HGbUyYXI9Kx1u7Qaw8wGZZ-1k2ZBUm7UFq1eO6aC8jNTNahtja_jU2ObxoPLpjStGpUrKuFGnMqO_ka_8UsjvMrhx5AHaar4JzPRCAVWmTCQ-ZmpunwyyflKBn88fiL9COQrnaTTIC-T1s9PDDprKmLu94ZjYBaV1nSaQj10p13-HaDX7FLu3jHden3hQH_NUDbS9YsmHYfEpryfEFfm6I1Gj45yY5PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجلی وحدت اسلامی با حضور علمای شیعه و سنی در آذربایجان غربی
عکاس:
محمد مهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://telegram.me/farsna/449883" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ جزئیات حملهٔ دقایقی قبل ارتش تروریستی آمریکا به بوشهر
🔹
معاون امنیتی استاندار بوشهر: ظهر امروز ۴ نقطه از بوشهر هدف اصابت پرتابه‌های دشمن قرار گرفت؛ ابعاد و ارزیابی خسارات احتمالی این حمله درحال بررسی است.
🔹
براساس ارزیابی‌های اولیه، تاکنون هیچ‌گونه تلفات…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://telegram.me/farsna/449882" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449877">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ03KR3luAySza9B4-PKqRwkTDLH5ngp2yUCs4LI79hxLWHgt1mMjtD-XTRP2e6sLJlKE-z9zhU8t6ngoOO5BMvVKooRNxkmICBrcS8Ba7iZt4CchKGngA3C5CPAyWSSnPvqUu0AWely4ZyS_itsk7bRDy7YSkjRZJaFu--YFtOhFZesR8FywWGz0YjjBVXm_nB4eKuqaA-W2C_FjOnN-iF1bd9oHO4z9mesfVzbaNby6BpoRyx2IzpVRjwGV9YP6y5MSHW7x7MgJiIP-UMY_fVcEeAdxI2EaQ8y7HhgBzLdfcAPJySfvetAsRiNLvN1QrXZ9DWpgTI47f9I3Leylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEAqjdVT4EPkyLek0I91K1S7lnhrs6yUC4bKWTkf_GMVL57pe_y5T1RZmwOgsA2Ow-EJZyx8MclucQgM_9je0B3e4et8Bs9ilIIS5wuaLKS95S4mksLTOESFqJ-EWS53Oh88KMUdZzuI026lZYX7ozPmywLpbEnA59y96HBgvLktV81VRuAi1xsaZjIQIaH43lc56__FESyanOqV-DEMu93rQr6nb6vHKyOCg3Ne-J2lpgnvKU91WFQrwDvNd-ULpGcjQcl9wpwXE3goD0bv6qGaKzxzyWFdN1ccQDZbyalSjSt0L6j4KECPfBqPiLwF-Ign7U7GmcQQnWFjgv1QsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsAsgvZJjIpx2TXdRk2HZ2Krbf1zn_yC-T2c6Q9WtgWhvk4wooPH5GMA2BjDVFRioBw76nzX9LFgFEpadqFIVIAdZ7TwbSrSJ43ZiWOlXprElQ3h_6rjFHlGblx96DV0Aisax4iNdMbhQzy0ru6cP_YF1_v1-WrsOnYdRJQe1Wdo4CwDqNN3hXAB2avFAejBPr8AZ0_vTxOKiInNMhnRQSFLkGcpqUWjfoplIBtFjxZmzAsAoZAAhVTPwy_odtL0gVT4zqru9qx_2aB5JBKJSmxRaD-dwDvCqIkwoGNmyLyMtPDzG7AhEyAPcHtud4AxDAmXFw-DjONVrwxUi3j6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKbjCRYeHvxDrT5fPVr0JwouFo7vOzr-Cvh4rXHh3Qhlkcw4Zk7lLYBiGS_oyZ6KM0iIehrnjqCdVuU7ru1rQAyz8aCNyRNkO-njrNE_x3JXcDJsMW2AIkyG73U6HO0Fc4sTHO8JlCTtNsq8AcA1hPzYfKiw8Z6R4x04NuAVfcEM-gJ67MUa0ho5IXh-NsBKFqaHhp3Db4rEIp_BC6Uwkuwrv1TbGYxM99NFu0IuTOl1iEsqe7b2cJ_TAfuAFRukZuHEIYNA11GGmxT1y21plSrlkCkEGyUdvQDjmbe96syxn65wr_H9u7ifmqhmDBC3PNf3VWakEsHWdKIwyM7iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2ilu1Ekla05MK1Q0OR9YoFwKUbaX6MPBRk3tVqUZKIHel7BCHpyvPTVruCxWfAtzXSifM-dD4IV-UvNfWkT6CaG55Tfe73fBiSkWRWT5_NDKslyD0mtjaHkcrcfCcdTku6vNVmxN8kb2UoWAb1DOtllR0FV4LrmwmHxLgBKQCC7BpNcPriLnPcURZaCMHC4Mlz4q0d9Mkzwaissk9uzqr5PDx_oikJCQzKJbdMAQ1l31KtW02_QukNMyD6eQq8vy3heoKqQygtQdexCpQCrWBHSjBu7QIVth1m5Fp7gX3wbvHX96__TQY4_OEOwE6EuH3kEiKjat8ETMuz6ESSylg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نهاد مدیریت آبراه خلیج فارس
:
تا قبل‌از تنش‌آفرینی آمریکا در تنگهٔ هرمز، پس‌از امضای تفاهم‌نامه ۲۰۰ شناور غیرایرانی به‌طور هماهنگ‌شده از این تنگه عبور کردند
.
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://telegram.me/farsna/449877" target="_blank">📅 16:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449876">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvRjqvGnU5UsmpELY5TmCH9q_r8VC1o_DC_qTuoAWBVtAT1FmtZQS_Ayqt1Q451mi4nGpH3jfpK2cbFV73voWm3HcbvWF_5JCUAIuK6MN6fSm7mb_8WFdbpRSBngHhTqxD_NmbEjejmKgb-sk7wQZ8gU93kH3LE0P20Or-9Gw2xvkdycbFpFschyeI9QaSvkDd_zbbSnaDKnbB0eqpeBZNksMPLaNORW-PqMI7f4_W1XNFYaspNkY4lmK-vCG5knZsgzRR2xeDED2rYHXOsT9Sy7zUfydthF8xbkidD2EqaAW6tmW0B3St4HAcqz6WTXPp3foRreZAXN9Nqun-Znlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاجگردون رئیس کمیسیون برنامه‌وبودجۀ مجلس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://telegram.me/farsna/449876" target="_blank">📅 15:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449875">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Li1Fj5jJ90X9LOUDNFwMzP0Lllim1TWuXwC2VxHnkTwnSg8STW0Oh8rN2e16NhAo8GY0fVLLulgYWwbw_IFosN7HnLtkoTQr0CLdgdsjyvITk58YrQMb8WVQc3R7EPydLXuGqqYMOW_mh3mGngfirL5G6yFkBt5YxpXJvnctCH6C3azZNbsybuahn40Ac-KNkepNaBQrKt0_zrjBORiw0l8ZlMathorArHalu48_Eap4auWmIcXC5NL4lGqeMT7iTqd9rIi07Ou2qJav7pzpeUqwg2ivnVi0vAjxoFW_MxTwCXOuXH_Jz4YrfvDIl1eVUudrRdCOcxo4-wd6AAAIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Li1Fj5jJ90X9LOUDNFwMzP0Lllim1TWuXwC2VxHnkTwnSg8STW0Oh8rN2e16NhAo8GY0fVLLulgYWwbw_IFosN7HnLtkoTQr0CLdgdsjyvITk58YrQMb8WVQc3R7EPydLXuGqqYMOW_mh3mGngfirL5G6yFkBt5YxpXJvnctCH6C3azZNbsybuahn40Ac-KNkepNaBQrKt0_zrjBORiw0l8ZlMathorArHalu48_Eap4auWmIcXC5NL4lGqeMT7iTqd9rIi07Ou2qJav7pzpeUqwg2ivnVi0vAjxoFW_MxTwCXOuXH_Jz4YrfvDIl1eVUudrRdCOcxo4-wd6AAAIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات موشکی روسیه به پایتخت اوکراین
🔹
روسیه امروز رگباری از پهپادها و موشک‌های بالستیک را به سمت کی‌یف شلیک کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://telegram.me/farsna/449875" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449874">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCiI3QGoWYOlH5zR3fZ5gW4BbN3IEwe-7LQE5WueQc8ZU-Xzo0Ijh_lB1k62jJX19zMmPZFsCYSWhX1LaxD72s58d2-1spo2IYkA7Dx0ri0aj7kBuIykp_m3qBvAHCuDR4f_uoPkcPYgGLJVJ_1D0TUsml3WUOlViUlF8M9W0EAYVFr9Uq0P5LhCs_NYfK4Xmp-9OAHJp3uq3M15VHZvMWMn-E6nMG9qaVeuT5wupBI-gnL6VUNJq1iaLosIOEaEKuRHKjNiR464RAmWbO4Z7AzrTg3YuhbZgAHV71T8z5PL0BrOAcBXqfUcQjpL7YYy-LuGweLHpAqsP5txZMEC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ پیشین اتریش: دغدغه اصلی ترامپ، تنگۀ هرمز است
🔹
کارین کنایسل: از نگاه ترامپ، اولویت اصلی آمریکا تنگۀ هرمز است، نه برنامۀ غنی‌سازی هسته‌ای ایران.
🔹
ترامپ نمی‌خواهد قیمت نفت سر به فلک بشد. او آمریکا را نوعی نگهبان تنگه هرمز می‌بیند.
🔹
ایران خواهان اعمال حاکمیت بر تنگۀ هرمز است و آن را آبراه ملی خود می‌داند و خواستار دریافت حق عبور از این مسیر است.
🔹
ایران تسلیم نشده، ساختار حاکمیت آن تغییری نکرده و به‌نظرم آمریکا از نظر نظامی و دیپلماتیک در وضعیت دشواری قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://telegram.me/farsna/449874" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آزادی ۵۵ صیاد ایرانی بازداشت‌شده در امارات
🔹
سفارت ایران در ابوظبی: ۵۵ صیاد ایرانی که در امارات بازداشت شده بودند، در حال بازگشت به کشور هستند؛ ۱۴ نفر از این صیادان از طریق دریا به ایران بازگشته‌اند و سایر آن‌ها هم قرار است از طریق هوایی به کشور بازگردند.
🔹
این ۵۵ صیاد که عمدتاً اهل استان‌های سیستان و بلوچستان و هرمزگان هستند، در ماه‌های مارس و آوریل به دلیل شرایط خاص منطقه و اختلال در سامانه‌های ردیابی، توسط گارد ساحلی امارات بازداشت شدند و بیش از دو ماه را در مرکز بازداشت سویحان و زندان‌های رأس‌الخیمه و شارجه سپری کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://telegram.me/farsna/449873" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449872">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTkREIkvK0so7ve7hCyURgRL5IG5I1Iod2t8G9-zW8tjqLytsRPAUsf-v8wOacD58eSNZgWA0vwkH4D5VNbB7nsIIGXjDohe6rsHeBZoWozP9e9X4nnrFiZKjhoouPaOwb4beCyHkZRRleKMfq7GiVhRhUxKYlaQJ5ExDpHE0w5fz8X0My65jKi-C7UFSyObiPAcyeNm-b_7mGoMMEIcQzndmytoDwUTQhjABd_JeT-bexp5xdzY2r8VCEYq5MBZFjuYlANXGuScno9uLLeNOLnZ0hB6ooiK4o01JMaKUy3CUllRJ2XwQaI6_rPsCmfu8R0dstsc67mPrTp-e6OxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری به جانِ جام جهانی افتاد
🔹
گزارش رویترز نشان می‌دهد تصمیم‌های مبتنی بر VAR، آفساید نیمه‌خودکار و حسگرهای هوشمند، بیش از هر دوره دیگری اعتراض بازیکنان، مربیان و هواداران را برانگیخته است.
🔹
کارشناسان معتقدند استفاده گسترده از فناوری باعث شده روند طبیعی…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://telegram.me/farsna/449872" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449871">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB_NICydLXOipcZLISXxy7u1zAy9N-xM2FTjVWmKc9olBjC9_vfrO0Fwd1z1_mWAcono-TOUr65YlQhdm6zMxWl-sLj64IwThfHFt41dXhuUqzASgQZCLl3bNv0pJgbA6khap2hdvN6P_SpGRBPj1zud8qaqEwb4v31YlgI26ghGVw6zvlxkB51D32h4ZtjvkND2m0TgDk3t3YmUsRCyGBaqbP1Xn92wkXsegyzfGru-USeY15EobTYouhGGKcm1iRAv-F81vM-RkaojiE-B_OH1P3JLlXaMduEZUaAYx3xT6aR7ObL4N3FtLwYj4ogAx2titdu2chw40KT45Fb9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل اتوبوسرانی تهران: ۷۵ متروباس برقی وارد خطوط تندرو می‌شود
🔹
تاکنون ۶۰ درصد از ۱۵۰۰ اتوبوس قراردادشده تحویل شده. هم‌اکنون ۳۹۰ اتوبوس برقی فعال است و ۲۸ خط مرکز شهر کاملاً برقی شده است.
🔹
۴۰۰ اتوبوس دوکابین دیزلی، ۳۵۰ اتوبوس برقی ۱۸ متری و ۷۵ متروباس…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://telegram.me/farsna/449871" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449870">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e9a1337b.mp4?token=Ypz5Npste9XXpn8HJop4zc7Aq4JHnPlqP8VDMHg-HqC2UkQiRUifel7Y_JwJsFsZUcMi5iSzv2PMdhUQmyayzY1hxc_JMlpdWyaNPKrE4HlsmeI-17YAIRJPCLpKuyTZnQ9fU2w2o0b7VodbIvkBYy8jKo-MsFe8DNx_JMWsGFa7U09N9I82IZY3xPgOmWUBR0m2dMVp-efOgwx9y28M_Le6hTB3nDTvrqRwS5sevifPCJCGzJqa9k2brgDqi1v6QzqsqVxBT7EmrRNEqOgzgaSyjdwpKLDG8_TnpKid7IksKoK6elAq_baXQlCWevUC7BPbJrAVFwCWFAhfSZMi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e9a1337b.mp4?token=Ypz5Npste9XXpn8HJop4zc7Aq4JHnPlqP8VDMHg-HqC2UkQiRUifel7Y_JwJsFsZUcMi5iSzv2PMdhUQmyayzY1hxc_JMlpdWyaNPKrE4HlsmeI-17YAIRJPCLpKuyTZnQ9fU2w2o0b7VodbIvkBYy8jKo-MsFe8DNx_JMWsGFa7U09N9I82IZY3xPgOmWUBR0m2dMVp-efOgwx9y28M_Le6hTB3nDTvrqRwS5sevifPCJCGzJqa9k2brgDqi1v6QzqsqVxBT7EmrRNEqOgzgaSyjdwpKLDG8_TnpKid7IksKoK6elAq_baXQlCWevUC7BPbJrAVFwCWFAhfSZMi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ روسیه: حملات آمریکا به ایران نقض «یادداشت تفاهم» است
🔹
لاوروف حملات آمریکا به ایران را نقض یادداشت تفاهم میان ۲ طرف خواند و تاکید کرد، این اقدامات در را به روی هرگونه توافق می‌بندد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://telegram.me/farsna/449870" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8e353249.mp4?token=kwVFbzagC_H72DVZb0LdWDOAMUdS9TabhFILyodj3Zws9SRQyNAxJeWucnv5luuAEZlEXdC2WFidqFWmNTM2VPPiA5wc92Yi7iOmceJ_KDTKzrUuuMUsrR0X7m2lW0o6W-VDx18_Wu6ZDBJSINAAlxruiu-nZakxvceMhcLArHLUx5VBz4nOz7lmBv1XfnyRUPt-jVWOZCsnBqpDC64zfqi6Ky9rl2ijdplj8rgJrp-Hv-ZL44p_J2_JOQJZ2DUph_JOljwKVp1D76CqsVtbvqKWhPEfRoN1Pcttdy3_x7yubyRNEqOe6wD7_a6B9ktYzYdBSUPgGdDvbyyVBE2lLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8e353249.mp4?token=kwVFbzagC_H72DVZb0LdWDOAMUdS9TabhFILyodj3Zws9SRQyNAxJeWucnv5luuAEZlEXdC2WFidqFWmNTM2VPPiA5wc92Yi7iOmceJ_KDTKzrUuuMUsrR0X7m2lW0o6W-VDx18_Wu6ZDBJSINAAlxruiu-nZakxvceMhcLArHLUx5VBz4nOz7lmBv1XfnyRUPt-jVWOZCsnBqpDC64zfqi6Ky9rl2ijdplj8rgJrp-Hv-ZL44p_J2_JOQJZ2DUph_JOljwKVp1D76CqsVtbvqKWhPEfRoN1Pcttdy3_x7yubyRNEqOe6wD7_a6B9ktYzYdBSUPgGdDvbyyVBE2lLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله دقاق: خون‌خواهی رهبر شهید به ایران و جهان اسلام محدود نمی‌شود
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://telegram.me/farsna/449869" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449868">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf2WXzeuNwze3ixk1BTN-LnuBitmSjaQUBv74h_sLQtT8ZSW2MBiYJ4s4rsuymO2outs03nL8FcHfhh6gY0f8UCDOZD98VHd8DsuWvyUm5i7H67-zIYJ5yj4Ynsef1mpacMuRE6oH9hMVwXYRaIlt7Fh-P4kYkiyzsC5Re2aqBiKQYwZUwjZU4p3rBIRsad-AB3eeXd79zG3aowmg7dTRVrK61OAT_XcwhKw6U_F1yX3MJ1iuv0xSKThsTsh2jiyQ-X_xuKqHtqY_culNvsD7LNl7SVHnBA77Oud6zk7iSYL1d0zXLqmQM2AA31DqXUtrIbHluisj33yblM90G8KxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دست‌دردست برای امنیت ایران
🔹
سخنگویان ارتش و سپاه، در دیدار با یکدیگر بر گسترش همکاری‌های رسانه‌ای، هماهنگی در انعکاس عملکرد نیروهای مسلح و تقویت هم‌افزایی میان دو نهاد تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://telegram.me/farsna/449868" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449867">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a7a1cdf3.mp4?token=SMzLAPLmHdM6bvP00qUG_w6fZcm9a6DIWDkRv1XfoiBZAlN5ih8mDsawMzv3bC47GTxt9IH0JLz5zJVUKuMY3qf_k9qFVZ2_khD74ozblhlqySFuL1Ppmr4VIzzC4kfqPiyIaMrL9CX5w45I2X8kQxTAsurq4wlDYuMrEWELK2Kb6xH5U7b5paDH9pzVm17BD2cCvS_xpWgtmRajgHAv6NZYC2xarIFzNIVmHdd1cS_4bXz3cVku6ivPkPiXkb9M1WkQE7FSt7qXIMOEr8i2SqHLqd6irZ02HMn-pyAjrogFFOYx_Qq3x3kZ-LUCtDeRBLKN20tI6-2mQg1h-KIL_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a7a1cdf3.mp4?token=SMzLAPLmHdM6bvP00qUG_w6fZcm9a6DIWDkRv1XfoiBZAlN5ih8mDsawMzv3bC47GTxt9IH0JLz5zJVUKuMY3qf_k9qFVZ2_khD74ozblhlqySFuL1Ppmr4VIzzC4kfqPiyIaMrL9CX5w45I2X8kQxTAsurq4wlDYuMrEWELK2Kb6xH5U7b5paDH9pzVm17BD2cCvS_xpWgtmRajgHAv6NZYC2xarIFzNIVmHdd1cS_4bXz3cVku6ivPkPiXkb9M1WkQE7FSt7qXIMOEr8i2SqHLqd6irZ02HMn-pyAjrogFFOYx_Qq3x3kZ-LUCtDeRBLKN20tI6-2mQg1h-KIL_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: در سال ۷۶، ما ۲۰۰۰ موشک داشتیم، حضرت آقا در آن زمان فرمودند این تعداد کم است و باید به چند ده هزار موشک برسد.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://telegram.me/farsna/449867" target="_blank">📅 15:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449866">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6807a69f3.mp4?token=bKlgKgY_hQ7vrwIknSAq-7mwRJqKv1ZIZn0VSwkADIisK-xGU34mL7O1d9uoiNi5doLvJEy4k1HG1ClzXaOhkpobC7eO3LR-aq7tLrcX5UdvtQp9lQ-rka6Zg69S2dMks4alNayke1692ULNp_Kilwq5-Gnc0szRYp5siddpJlYQksGJpK1myl79xngoTosErHxBMWwjqkUV5DABZVezmHHh861uRn49mrS6GsdKvRcH1a_JrlqmMfqf8V2ZxW4k0PmKpPVmFcHZyaB-yn9plYCtfN8XU6LR-f7q4qEkpnl1UfmYm5CO1fh1Sx3yBL6vpAl8XZgRfoeCnPMRRJ2LsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6807a69f3.mp4?token=bKlgKgY_hQ7vrwIknSAq-7mwRJqKv1ZIZn0VSwkADIisK-xGU34mL7O1d9uoiNi5doLvJEy4k1HG1ClzXaOhkpobC7eO3LR-aq7tLrcX5UdvtQp9lQ-rka6Zg69S2dMks4alNayke1692ULNp_Kilwq5-Gnc0szRYp5siddpJlYQksGJpK1myl79xngoTosErHxBMWwjqkUV5DABZVezmHHh861uRn49mrS6GsdKvRcH1a_JrlqmMfqf8V2ZxW4k0PmKpPVmFcHZyaB-yn9plYCtfN8XU6LR-f7q4qEkpnl1UfmYm5CO1fh1Sx3yBL6vpAl8XZgRfoeCnPMRRJ2LsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش آمریکا برای گریز آبرومندانه از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://telegram.me/farsna/449866" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449865">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPLdzaWm-ZfEJbWCS39NM9GhT-pURDJImPtIe4_QTUzhluMAzuUEuZQ0kjr6I9f3jq2tXeC5zx8BWXeu3x9ka8WDdlRUtpG9-rxaGV3M-Lb6ehM6NJsA85XYnE9Y3LAg2Ge6QxtqHVkay2t_guYiE0_gOOR2uutXHHv_BFm0Ss9PxlLIrGt_oBZGUrSqA3r35rcGtGUs1RqpEuxdeE06lR3YJX_gJGMIYzIU_C92O8lsTsVeelAkYywERq5g8zfZBurQBoFR8DsmgTxCzrgtIx2vjJoExqomlRBx9Pyfn_MmiivXTzyN3YHH-U0JP-aQHlAvwaXhNMM9cRBBGxLhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استراتژی چادرملو برای تأمین پایدار مواد اولیه؛ توسعه معادن جدید در کنار استفاده از ظرفیت بازار
مدیرعامل شرکت مدیریت سرمایه‌گذاری امید، تأمین سنگ از بازار را یکی از راهبردهای هوشمندانه چادرملو دانست و اعلام کرد این شرکت همزمان با توسعه معادن جدید و اجرای پروژه‌های اکتشافی، از ظرفیت معادن اطراف نیز برای تأمین پایدار خوراک تولید بهره می‌گیرد.
بابک ابراهیمی با اشاره به آغاز فعالیت‌های باطله‌برداری در برخی پروژه‌های معدنی تأکید کرد: معادن جدید در آینده به ذخایر چادرملو افزوده خواهند شد و این شرکت با ترکیب توسعه معدنی و تأمین سنگ از بازار، مسیر پایداری تولید و رشد بلندمدت را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://telegram.me/farsna/449865" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449864">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRFV6nnbryUT10MW3oRpf9728tI-PzZnVVJijP7jLbuCrVCfLxGOYed3WkSEGMq-hl7M9YIGclOZgN_3Sc9BuFzmP5iPDReY5Cc5lXR0KaQxixYV6yisvwpHRzCOI35fRmanERFB0plwL7GDX2DwMVO8Y4mDahFZ2qcV_wMKnl0D43sZUeBGHjCOi6XOoggSEZONT5KDiHXy-xT524WcwRVF6EL2BKtKe8SC6Yx9GXv2wHGJ1sF7rBMvo87G0O37qGYxxv79EcPNT9iKwVlpZ7zTooMrEHkyKr3Wpww7oZzm228-_W52dNjy0s2wJ0fsSpqtDkP1A23x75yo8MBQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نگاهی به کنگره جهانی معدن ۲۰۲۶
🔰
مس؛ محور تحول آینده معدنکاری جهان
🔻
بیست‌وهفتمین کنگره جهانی معدن (WMC 2026) در لیما، پایتخت پرو، بار دیگر نشان داد که آینده معدنکاری جهان بیش از هر زمان دیگری با تامین پایدار مواد معدنی حیاتی، بویژه مس گره خورده است؛ فلزی که امروز در قلب گذار انرژی، توسعه زیرساخت‌های برق، خودروهای برقی، هوش مصنوعی و اقتصاد دیجیتال قرار دارد.
🔹
بیست‌وهفتمین کنگره جهانی معدن از ۲۴ تا ۲۶ ژوئن ۲۰۲۶ با حضور مدیران ارشد شرکت‌های معدنی، سیاست‌گذاران، دانشگاهیان، سرمایه‌گذاران و نمایندگان بیش از ۷۰ کشور جهان در شهر لیما برگزار شد. شعار این دوره، «معدنکاری برای آینده؛ اعتماد، تحول و فناوری» بود؛ شعاری که بازتاب‌دهنده مهم‌ترین دغدغه امروز صنعت معدن است: تأمین سریع‌تر، هوشمندانه‌تر و پایدارتر مواد معدنی موردنیاز جهان.
◀️
ادامه گزارش در مس‌پرس:
https://mespress.ir/x6RJ
@mespress_ir</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://telegram.me/farsna/449864" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449863">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://telegram.me/farsna/449863" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obO3U8sHVEnNkquPEp_IWO-cxHK1eAjIEQCX4A-03cB-NQyrKCdxA4uLwtU5IiqmxLqFSQBxQL9QfgBxiqq8AyTyaS29twX53RfE2mLMItwjKqNxPF2sOymv_PIrqTCg4f0GAYAutimrEmM4gg9BV8bf3KunM93NZUk_ccTYw60wQwxO-3L2GAxD0kPRhwGfV78AoG5sOqltTz1msU5WSealSeijvYyNX37W2568Vf1eucOI2xDNQ5z_sI8EBe9U9n0B_d7BKCGt4G1z0jQO2eGK1G2da5aIhFQhcvf9ZZyIhg5Xi0d4PnOeUsQd06K_OG2lpTPYsOjaQlyHUB65vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت از ۸۷ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://telegram.me/farsna/449862" target="_blank">📅 14:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449861">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حکم پرونده‌ای با ۱۴۸۱ شاکی در مهاباد صادر شد
🔹
دادگستری آذربایجان‌غربی: حکم بدوی پروندهٔ یک شرکت هرمی با ۱۴۸۱ شاکی صادر و ۶ نفر از متهمان این پرونده به حبس‌های طولانی، جزای نقدی، انحلال شرکت و مصادره اموال محکوم شدند.
🔹
بخشی از اموال توقیف‌شده به مال‌باختگان بازگردانده شده و بازپرداخت مابقی نیز طبق قانون ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://telegram.me/farsna/449861" target="_blank">📅 14:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1bf31e2df.mp4?token=PHtRfk_UVC-dgyWmrn9w3_vmpT3GdypiZiti2ZSFLDrgGzkf7L7JrebrGmM7Z4P5Fx_s6kseKIJfSMkV4GtO7tquhqLgZLkjwOVHYMcNis2bx1duUcRQ-Zx10ooo3wBz46tTrE7JoucFhmmd731cxUIorG1y6aJ1MfzOAm_jqAbs3KiXkVn7SgMfHQgGS2cOIn225pPohkKQ5sL_PyRSEVYkjm2vBAtt2mlRD9GatXIapeQx54yn2tdZu8ESCSZyOZxulDKvqtRTkitROJaCQK5NpMmrPs80nwuKCv2rolHVIFviCRPZdU-RrgTQnXs03t9LMS0YPtv9lLqeIo_fhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1bf31e2df.mp4?token=PHtRfk_UVC-dgyWmrn9w3_vmpT3GdypiZiti2ZSFLDrgGzkf7L7JrebrGmM7Z4P5Fx_s6kseKIJfSMkV4GtO7tquhqLgZLkjwOVHYMcNis2bx1duUcRQ-Zx10ooo3wBz46tTrE7JoucFhmmd731cxUIorG1y6aJ1MfzOAm_jqAbs3KiXkVn7SgMfHQgGS2cOIn225pPohkKQ5sL_PyRSEVYkjm2vBAtt2mlRD9GatXIapeQx54yn2tdZu8ESCSZyOZxulDKvqtRTkitROJaCQK5NpMmrPs80nwuKCv2rolHVIFviCRPZdU-RrgTQnXs03t9LMS0YPtv9lLqeIo_fhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست علنی ۲۲ تیرماه ۱۴۰۵ مجلس  @Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://telegram.me/farsna/449860" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGrS6vUiXMee-mP5rPeEIvv4p0mfcxL3iyMkTw9bawqWaEPCcxtxAdmahAbC1dpt8Dkxb-iHgij3_lNbZeKjsiGjpb3MP8rvL6HHlJgS_935IylOg0_Qlzw0MxuUuDD98kgkbZOUrQn33aOS6SU0kDG7GhXFrhBVXtxSiLDSPtiXPDTw4qKPS8_Y5LnomPwKxxMrocZ91NRmJ3HF28NUUTMo6-xytFfT-qtz_V__GpGsI1HqM9M23NEfQdw0EM_0y0sBFU660dIlNvA3CtW07JIqHNIvbc0mh0Baj2EAJYebqmLuX-GERtVyUGAXMAjJOD6KxyGd7raQRMnkfUn-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جوادی‌آملی: اسرائیل و آمریکا در مقابل ایران ذلیل شدند
🔹
هیچ‌کس فکر نمی‌کرد که چندین ماه، این خانم‌ها و آقایان اینگونه در میدان‌ها حاضر شوند و منادی انقلاب و اسلام باشند؛ رهبر عزیزمان کار بزرگی کردند و بعد هم شربت شهادت نوشیدند و شهیدانه رحلت کردند. این جریان میدان و حضور مردم را هم نباید دست کم گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://telegram.me/farsna/449859" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ جزئیات حملهٔ دقایقی قبل ارتش تروریستی آمریکا به بوشهر
🔹
معاون امنیتی استاندار بوشهر: ظهر امروز ۴ نقطه از بوشهر هدف اصابت پرتابه‌های دشمن قرار گرفت؛ ابعاد و ارزیابی خسارات احتمالی این حمله درحال بررسی است.
🔹
براساس ارزیابی‌های اولیه، تاکنون هیچ‌گونه تلفات…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://telegram.me/farsna/449858" target="_blank">📅 14:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=lPM_xKdOEGvnNdYWHnJB9e3qBAvJVvcseVdNs2QiM9pmCjh8d-cZWVGWMBmTD7bf4LBYvFLpIO96tpNOtisJrkyAhGwxFYQ_SBpvF1XR58LpVrnurcoXpwnLhvrOuNapW7wTBow926JP0RG7bhquMSYA7QMEpgD3C-vfevxgyrTS8RsjnlFXq5IKQhv_I_r8wLrXrrUr5-dTUGu6iMVgA4u4NlSV7kMeZNv7GPD_vK1u_cgxcBMxauoP-hP7nT13TozQPXnx59ArRlZvNrhOMyv4mj4fdwqnE6pQ-FuefrTYaJ7K4dCGH1Zpb2rwnABe4FT8mpsalkZjTr04FX8sew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=lPM_xKdOEGvnNdYWHnJB9e3qBAvJVvcseVdNs2QiM9pmCjh8d-cZWVGWMBmTD7bf4LBYvFLpIO96tpNOtisJrkyAhGwxFYQ_SBpvF1XR58LpVrnurcoXpwnLhvrOuNapW7wTBow926JP0RG7bhquMSYA7QMEpgD3C-vfevxgyrTS8RsjnlFXq5IKQhv_I_r8wLrXrrUr5-dTUGu6iMVgA4u4NlSV7kMeZNv7GPD_vK1u_cgxcBMxauoP-hP7nT13TozQPXnx59ArRlZvNrhOMyv4mj4fdwqnE6pQ-FuefrTYaJ7K4dCGH1Zpb2rwnABe4FT8mpsalkZjTr04FX8sew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با بسته‌ماندن تنگۀ هرمز کشتی‌ها همچنان در خلیج فارس لنگر انداخته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://telegram.me/farsna/449857" target="_blank">📅 14:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اصابت پرتابه‌های دشمن آمریکایی در نقطه‌ای از آبادان
🔹
معاون امنیتی استانداری خوزستان: در ساعت ۱۳:۲۵ دقیقهٔ امروز نقطه‌ای در آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت؛ گزارش تکمیلی پس‌از ارزیابی‌های اولیه اعلام خواهد شد.
🔹
ساعت ۳ بامداد امروز نیز…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://telegram.me/farsna/449856" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اصابت پرتابه‌های دشمن آمریکایی در نقطه‌ای از آبادان
🔹
معاون امنیتی استانداری خوزستان: در ساعت ۱۳:۲۵ دقیقهٔ امروز نقطه‌ای در آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت؛ گزارش تکمیلی پس‌از ارزیابی‌های اولیه اعلام خواهد شد.
🔹
ساعت ۳ بامداد امروز نیز نقطه‌ای در بندر امام خمینی(ره) مورد اصابت پرتابه‌های دشمن آمریکایی واقع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://telegram.me/farsna/449855" target="_blank">📅 14:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13186af33f.mp4?token=myxud-yDm060v__wGfaFW94Tr58ig5-Z_vMxrMvVNGhw0NNO_sgircmBnB1fOiX_jUjRdMPFr4mOUtjDD1efrZ1Io4D8UHLd_PkSa_xf2mduHZhkPyZFSeE5akbt8-BSh2gf8WlW5yTqLxJOnoYzBuIzvZDSj1ymoQmtfvpcwQ4io4r1NgL17MMbvPTFBJ8JmjkWNZ4UXYKMcAiHnLd5ePjfg-4yiJv4_PXQxZb4N0b6gVeZAdkALVS1cLmWQKEJcpry8_p_xrQ5TqEmCKiKpG_hSXiiqhDUAETzjqEGIoTmaLna_cWk_8G3ArRLgyuho081mc5eoColr9Gc5Pui9LQsWyEitjXLMwoXX3CcXUMIG6OVZBG9p7xEO8qXV8VerB9EMk86IItFBSEc8Gi-e2BZY-Y9cW42AswUDs44deff4XLc415U9hkUf9c2QrOGWI63GwVgx1dtoKhHI1DAeKW8lTGfdS56JyPBXgyhxzYa5jXByqeuqNcv2O8BVu-SJaTLHoqOG-jVhmRHW7q72MvfrLCoHu8EVdErlZKKIe-TRNLJCF7uBFFpiLNQgrQAz5kZON2kKk3quXeauV6K2-FTFJqeYSQC1l60A2OPjgjup72s1g_43Xak1fFFAtDWIcL8HAl-mQhFU4uQ97koSY4fk1PmuRkhHcDPb7DueTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13186af33f.mp4?token=myxud-yDm060v__wGfaFW94Tr58ig5-Z_vMxrMvVNGhw0NNO_sgircmBnB1fOiX_jUjRdMPFr4mOUtjDD1efrZ1Io4D8UHLd_PkSa_xf2mduHZhkPyZFSeE5akbt8-BSh2gf8WlW5yTqLxJOnoYzBuIzvZDSj1ymoQmtfvpcwQ4io4r1NgL17MMbvPTFBJ8JmjkWNZ4UXYKMcAiHnLd5ePjfg-4yiJv4_PXQxZb4N0b6gVeZAdkALVS1cLmWQKEJcpry8_p_xrQ5TqEmCKiKpG_hSXiiqhDUAETzjqEGIoTmaLna_cWk_8G3ArRLgyuho081mc5eoColr9Gc5Pui9LQsWyEitjXLMwoXX3CcXUMIG6OVZBG9p7xEO8qXV8VerB9EMk86IItFBSEc8Gi-e2BZY-Y9cW42AswUDs44deff4XLc415U9hkUf9c2QrOGWI63GwVgx1dtoKhHI1DAeKW8lTGfdS56JyPBXgyhxzYa5jXByqeuqNcv2O8BVu-SJaTLHoqOG-jVhmRHW7q72MvfrLCoHu8EVdErlZKKIe-TRNLJCF7uBFFpiLNQgrQAz5kZON2kKk3quXeauV6K2-FTFJqeYSQC1l60A2OPjgjup72s1g_43Xak1fFFAtDWIcL8HAl-mQhFU4uQ97koSY4fk1PmuRkhHcDPb7DueTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همسایه‌های رهبر شهید در رواق دارالذکر چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://telegram.me/farsna/449854" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ با رای اعضای کمیسیون امنیت ملی و سیاست خارجی مجلس ابراهیم عزیزی رئیس شد
🔹
عباس مقتدایی و امیر حیات مقدم هم نواب اول و دوم و حسن قشقاوی سخنگو و بهنام سعیدی و یعقوب رضازاده دبیران اول و دوم انتخاب شدند.   @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://telegram.me/farsna/449853" target="_blank">📅 13:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449852">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
شنیده شدن صدای چندین انفجار در بوشهر و جغادک
🔹
دقایقی پیش مردم بوشهر و جغادک صدای چند انفجار شنیدند. هنوز محل دقیق انفجارها مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://telegram.me/farsna/449852" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWvRUsXGLjeM2uWa68baEo2HmEnafHvQv146MbH_sUxKF8Z_Z_2p71oJ2WEAkuceOIcYyB14Lt2ROI_-KuQdrGOkJv-VKmKU5bPnQum-3jQwQTwTpqy025dUFWr2teuvymyE9zU7sFUdW8mOVvHx0QySL2WfTGS8p8BW8jT8M6MYe3KGRws92rs8B4qiD8s25ICdm8LmGaiu1xlLhB9RTrqUYXZStRkkz0GSQoqLsnOTaH0mCQDiKrIiZeZCWcrCJXtyYv8Y1jgY-YxVZlFjx1QtR0xXMZAk2-UgDc2g5Cq9HGP92lt7jSbg-nc6QL2qQCQlPK6sbc7hux-2ntxypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوسعیدی: ۴۵ سال به‌دروغ گفتند که ایران تهدید منطقه است
🔹
بدرالبوسعیدی وزیر خارجه عمان در مقاله‌ای نوشت که به بهانه و دروغ «تهدید ایران» منطقه خلیج فارس نظامی‌سازی شد، اما اکنون مشخص شده است که این حجم از پایگاه‌های نظامی و تسلیحات هیچ کارایی از خود نشان نداده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://telegram.me/farsna/449851" target="_blank">📅 13:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
شنیده شدن صدای چندین انفجار در بوشهر
و جغادک
🔹
دقایقی پیش مردم بوشهر و جغادک صدای چند انفجار شنیدند. هنوز محل دقیق انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://telegram.me/farsna/449850" target="_blank">📅 13:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
صدای چند انفجار در غرب بندرعباس شنیده شد
🔹
مسئولان تاکنون اظهارنظر رسمی در این خصوص نداشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://telegram.me/farsna/449849" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlVG8MsSl_uudEi7JuMVZnpskptHDOJywr1k0UlcfAglU8q6QsEL0mOeb3WvkO_AxsRr9tXKODKUTwY6NWthJIly5q92jNL0TaKfFBHN7pNI6O66KCO_uUqXuL530muadO2DEfFV_ExqXAoFNAfk0X72XBMb9FPzffQFLhNvFsBB-F5Ehmp7UpAnN1wGvwfXap--VF56D9ZMRy9GuCp3rg2mkLvthgTCw_6wf19vdEdEJNDDX7tQ-U988GKcPaj2tgbfHOzuiuOANT7lPB4XJuQXDp-Li_CNchwPyll0RmCXwKNlkGxHIC1GkW7tNipWIknfA2KCfykbmsv0Xbkv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDR2ne64mgwN3o8j2EZDDpRYSN8ofxT5-XxzVw0j3WURzQ6Vwnr6ER5QMIIPlwa7uFtzyw_hjzOZkNOx9-Sz2tj7783RSG-Gq09mDlOk7-YCb9tAYMgxSQbUIMmDwBq8MAGTvpdyzI__3ONYC87Hi0srwviV294AxfmjHQOmvcHpsi7VuL-pJbTqZlQ8XFILTg2ABa5igm2WvEAaEyBFx8wjkHjWjkHZrWAgYZmbIzlC_HIFSOCKdxgk_bB2BjFDbV37DbqhTGuypDCWeFnp7co2BSRtfapYDkUJQn26SXbB_koTjOzgE8AFS5caANQbdEuoTIsA8X48-b6mkDgXIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیام رهبر انقلاب به کشورهای عربی بر روی موشک خیبرشکن پرتاب‌شده
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://telegram.me/farsna/449847" target="_blank">📅 13:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95cbc38cc3.mp4?token=gZ02yeBv8ETZjdySnwtxUX717uCu4PV8X3SoQIuoQdYLW_y5Z7A63K6OtXhhTgt39l-T-6OS4of5h6ztnrMA2BF6ILkoYWAatdPHiI-z5plC07i0zK4KzlLnG9Haxl5EvSOFhzUt_2JmkBS4YlUbbBSzcqNExKWoyjicEMTWL7hkrqzvII6_CK9hEkpG9Z6ZilTZ2OI06FbfxZV8zbSsrZZXSBPwG1t9RYL8epPreXHxnUEQJbiTftv5vwWvMVLKfyppQPO4_3JJnUlW3fkRs_erWKefU07dO0ycNgY_g5d8KTHxfuaWG1ZGPZ7IW6Ix-5OHFRQUGm3cvlfShZKsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95cbc38cc3.mp4?token=gZ02yeBv8ETZjdySnwtxUX717uCu4PV8X3SoQIuoQdYLW_y5Z7A63K6OtXhhTgt39l-T-6OS4of5h6ztnrMA2BF6ILkoYWAatdPHiI-z5plC07i0zK4KzlLnG9Haxl5EvSOFhzUt_2JmkBS4YlUbbBSzcqNExKWoyjicEMTWL7hkrqzvII6_CK9hEkpG9Z6ZilTZ2OI06FbfxZV8zbSsrZZXSBPwG1t9RYL8epPreXHxnUEQJbiTftv5vwWvMVLKfyppQPO4_3JJnUlW3fkRs_erWKefU07dO0ycNgY_g5d8KTHxfuaWG1ZGPZ7IW6Ix-5OHFRQUGm3cvlfShZKsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ماینرهای غیرمجاز؛
سودش توی جیب دلال، دودش تو چشم بیمار!
این روزها دستگاه‌های استخراج رمز‌ارز دارند حقِ برق من و شما را می‌بلعند. طمعِ سودجویان، عامل اصلی خاموشی‌های بی‌موقع در کشور است؛ اما این قطعی‌ها برای ما یعنی گرما و کلافگی، و برای بیمارانِ بستری در بیمارستان‌ها یعنی بازی با مرگ و زندگی!
💔
🔸
آیا می‌دانستید مصرف برق هر یک ماینر غیرمجاز، معادل ۱۰ واحد مسکونی است؟
🛑
*سکوت نکنیم؛ این یک وظیفه انسانی است:*
اگر در همسایگی، کارگاه‌ها یا مناطق اطراف خود صدای مداوم فن‌های قوی یا مصرف مشکوک برق را احساس کردید، قهرمانِ پنهانِ شهرتان باشید.
📬
آدرس یا موارد مشکوک را به سامانه ۳۰۰۰۵۱۲۱* پیامک کنید.
(هویت و امنیت شما کاملاً محرمانه باقی می‌ماند.)
#مسئولیت_اجتماعی
#قطعی_برق
#ماینر_غیرمجاز
#حق_شهروندی
#قاچاق_برق</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://telegram.me/farsna/449846" target="_blank">📅 13:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEjcqq6oH7AZzFjV856ENB-9HsRWxHGUVC3y0kBDZ8_F3md4S_8k6MlBPjjXvq0w0JBXuJuzuypQyFfavx0G_5EdEFOJoVnBjdbDnMLu9ldywtVZ95is-1kbtfD16g1kYAHDUONrsJEHLlXtQubteTYW8-ZsAOuzs2H7OEIkxPFXj0Yc-smU0aE6T6xYMlD1yd0upZ5TEjWoELRJ7S2nLHTVYJXXRkrythan_ADYqAlP0yoSUDVmb5SiEIUxvKoWWgky03B1sye3XH_0QPNghq6eAyU1su--hDu6FIpHGHvzcuslvn-mnXzIn3_6uyg4fuFtpbtt08WOjauDkjmYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مزایده بزرگ موسسه ملل/ فرصت خرید اموال با قیمت کارشناسی و واگذاری ۱۰۰ همت دارایی و عبور از ناترازی
مؤسسه اعتباری ملل به عنوان آخرین بازمانده مؤسسات اعتباری دارای مجوز در کشور، این روز‌ها در مسیری دشوار اما حیاتی برای بقا و تحول گام برمی‌دارد. این مؤسسه که موفق شده است تمام بدهی‌های خود به بانک مرکزی را به طور کامل تسویه کرده و اضافه‌برداشت خود را به صفر برساند، اکنون با برنامه‌ای جامع شامل برگزاری بزرگ‌ترین مزایده تاریخ خود، برگزاری مجامع مالی و طرح افزایش سرمایه ۷۰ همتی، در تلاش است تا از بحران عمیق مالی خارج شده و به جرگه بانک‌های سودآور و تراز کشور بپیوندد.
بر اساس گزارش‌های منتشر شده، زیان انباشته این مؤسسه تا پیش از شروع برنامه اصلاحی به رقمی حدود ۶۵ همت رسیده بود و نسبت کفایت سرمایه آن به منفی ۴۱ درصد سقوط کرده بود که فاصله زیادی با استاندارد اعلامی بانک مرکزی (مثبت ۸ درصد) دارد. با این حال، هیأت سرپرستی با اتکا به فروش دارایی‌های مازاد و تملیک مطالبات، موفق شده است گام‌های مؤثری در مسیر کاهش زیان بردارد.
مطالعه كامل خبر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://telegram.me/farsna/449845" target="_blank">📅 13:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://telegram.me/farsna/449844" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
بغض تماشاگران خردسال برنامه محفل ستاره ها با مداحی احساسی برای رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://telegram.me/farsna/449843" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB8JoNr0b-rFgDxUXsc8QE_uPhYUJRoPo0yKS3Yiqz1A9udZcfGPZlhO50ilaWkEphbPcDEmE0_p02K0g448VFzKs5QZQZ8ZlXDMdagNj0Y92DWLymfqTbyAFbRI9pUvPHFjNjLTAS9lZJf0SYRDj06yJxMgMDcdz0SYoZ_yuEpeTW3g7mdBQOxzxdendysEH1frgze6PK5qHvvLSbc-3c6bR161m9FF_-jHCxWI2W3maZVNsjP5pG3x88QGlDyw8puHeoceVx02pOg8-12yxV1LLsmS6aOnHXzhOgzztz3_wzngFquZa-zIQ42Ej66BA5sxN0wW1NWBoKkqtiiSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۴۲ هزار واحدی به ۴ میلیون و ۹۲۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://telegram.me/farsna/449842" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYt-MAjTpuOBs7KNWyjKQIEpYJ7v7aiTZJFh6QZAHRI1pjRiZhxOzo8vCC6kkK0wo3muZlvhelBB9rFGpzDAR4LEbAGDjEkuJr3THBuXH5cShXKbmS-UGx--61vY_BN93fE5WK8fu_G0EqNRh2bcbJXzira96gISGtdv7r7l2bcjYxnUiviYFqIwhXETRTVeRRQz3V-WO0Ei6oD5L-74qkmNNJ3MDoHf9MFhLyWO7fQCRPUQtFCdxSWXVJA85Cg_QWE6ZsvJIcL1Apd1LijYmdiAE1qIzPyTB-qulLrNUbBpCFYf3deycEIyTczXBUbwKcbRwhvEp1OREdC5dkmjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامنهٔ
t.me
تلگرام از دسترس خارج شد
🔹
دامنهٔ
t.me
تلگرام که برای لینک‌های دعوت، کانال‌ها و اشتراک‌گذاری پیام‌ها استفاده می‌شود، با قرارگرفتن در وضعیت Server Hold از دسترس خارج شده و تمامی این لینک‌ها در سطح جهانی غیرفعال شده‌اند.
🔹
تاکنون تلگرام و رجیستری دامنه، دلیل این اختلال را اعلام نکرده‌اند و رفع آن ممکن است از چند ساعت تا چند روز زمان ببرد.
🔸
«سرور هولد» معمولاً در موارد مهمی مانند بررسی‌های امنیتی، اختلافات حقوقی، سوءاستفاده از دامنه یا پرونده‌های مرتبط با کلاهبرداری استفاده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://telegram.me/farsna/449841" target="_blank">📅 12:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
ترامپ: ما کوه پیک‌اکس (کوه کلنگ نطنز) را نابود خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://telegram.me/farsna/449839" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bd23a64.mp4?token=ejo3Y0xjlOS6V3-yHvY7obnffasHsDLFpCPFigZnutYs-riMQRDSPEJ1c0tfi9PObQ_I5cjDOvNl9ZhNSeMZtN2SpHg57AugCMg61lAYiyHmINzRXQZLFmgZGYzbEXRHy1KVScZTWOasODfQrn9J4YrA1pDy-tadrtYwKEp6vJZTuTry6UT6A-FMww69d2QPeQs4gxwBOWYhnfHEwlwFcLTa84zGoS0kpDdxGedaFmOZsfxpmu3vX1jlqRSMmPkS3_xgnhPKZpBeu1jEogctXf7U4IjeJHvdhIOy0oUZKqF31O4NlFIb_RaojNDbQLGywqIELbljvLjVxMQcbBh2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bd23a64.mp4?token=ejo3Y0xjlOS6V3-yHvY7obnffasHsDLFpCPFigZnutYs-riMQRDSPEJ1c0tfi9PObQ_I5cjDOvNl9ZhNSeMZtN2SpHg57AugCMg61lAYiyHmINzRXQZLFmgZGYzbEXRHy1KVScZTWOasODfQrn9J4YrA1pDy-tadrtYwKEp6vJZTuTry6UT6A-FMww69d2QPeQs4gxwBOWYhnfHEwlwFcLTa84zGoS0kpDdxGedaFmOZsfxpmu3vX1jlqRSMmPkS3_xgnhPKZpBeu1jEogctXf7U4IjeJHvdhIOy0oUZKqF31O4NlFIb_RaojNDbQLGywqIELbljvLjVxMQcbBh2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: توسعهٔ حمل‌ونقل عمومی حتی در دورهٔ رایگان‌بودن هم ادامه دارد
🔹
شهردار تهران: درآمد حاصل از فروش بلیت تنها بخش اندکی از هزینه‌های واقعی این خدمات را پوشش می‌دهد؛ در خطوط اتوبوس تندرو حدود ۳.۲ درصد و در مترو نزدیک به ۱۳.۹ درصد هزینه‌ها از محل فروش بلیت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://telegram.me/farsna/449838" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0611c8c221.mp4?token=EHTybMnN8W0aZZwXylPCLID0bBMTJ_njPDXTb7blPV16euzra2aC-PoFsFIm73PHp9nxU2-CleFojn81w4xCO6ztbOzm8HAMZKNOcPzUtmfmVjGVmjUMXSvisdwigaPt2zr6MK5V7cOwXG0W2uesNjPB6hhOZyzWBTspDp57OSN-1M65Yf-nMKPhzUz_dludKPZzgIxvU1kQ3WyCAJ0CGskttlkX9oMi6HGg1AyFilIgIPnMO0uEIbDPWSwBB2gArLSd-ZvwGV3KZtVxRoHFqoywm5no_S99Oavjj3Eno47YBXo9kMhf-uQazeyx_BnG1RB0D2Nvb6LY20D0RTsPFxCHTA-WiWH4WULuNlOsdZpCSBpjgg4KA5puTAkmYaT6XVWY-RDbPAMQHiqGw7mKVbTvKEWkvg9kx0mSfq4VO11W10JHNtQKq1YC-QR7upfJA0YDhEUQrqNZSzyMnLWS6VSu9h1PNfQjRJUzWyugBzQvYO8T9TknyGACcfxshOM11gWBJieLlmV32ST5dPY1bwDxs5-UbfdnHssmyKyA99KXY9gzcpn_5OGPfu0WowJxnLSz3e08T8nZVaXzGBZklI_L9v0yokR4jZkWMoq9Zvgplb0tgWgk0YH0CB5GLkHFrL7VOO7pV4TVEKlyCoVG_vwDWN2yDRaMVaynZtokvYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0611c8c221.mp4?token=EHTybMnN8W0aZZwXylPCLID0bBMTJ_njPDXTb7blPV16euzra2aC-PoFsFIm73PHp9nxU2-CleFojn81w4xCO6ztbOzm8HAMZKNOcPzUtmfmVjGVmjUMXSvisdwigaPt2zr6MK5V7cOwXG0W2uesNjPB6hhOZyzWBTspDp57OSN-1M65Yf-nMKPhzUz_dludKPZzgIxvU1kQ3WyCAJ0CGskttlkX9oMi6HGg1AyFilIgIPnMO0uEIbDPWSwBB2gArLSd-ZvwGV3KZtVxRoHFqoywm5no_S99Oavjj3Eno47YBXo9kMhf-uQazeyx_BnG1RB0D2Nvb6LY20D0RTsPFxCHTA-WiWH4WULuNlOsdZpCSBpjgg4KA5puTAkmYaT6XVWY-RDbPAMQHiqGw7mKVbTvKEWkvg9kx0mSfq4VO11W10JHNtQKq1YC-QR7upfJA0YDhEUQrqNZSzyMnLWS6VSu9h1PNfQjRJUzWyugBzQvYO8T9TknyGACcfxshOM11gWBJieLlmV32ST5dPY1bwDxs5-UbfdnHssmyKyA99KXY9gzcpn_5OGPfu0WowJxnLSz3e08T8nZVaXzGBZklI_L9v0yokR4jZkWMoq9Zvgplb0tgWgk0YH0CB5GLkHFrL7VOO7pV4TVEKlyCoVG_vwDWN2yDRaMVaynZtokvYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: رادار پاتریوت، رادار کنترل هوایی ناوگان پنجم دریایی ارتش آمریکا و یک سامانۀ راداری اخطار اولیۀ c-ram منهدم شدند
🔹
اطلاعیۀ شمارۀ ۸ سپاه: رزمندگان غیرتمند نیروهای دریایی و هوافضای سپاه در مرحلۀ دوم، با حمله موشکی و پهپادی به ناوگان پنجم دریایی شیطان…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://telegram.me/farsna/449837" target="_blank">📅 12:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXy98AfP5nSu7hyuhhXbzL539NvqF1bTLjShcZum4pxfqh9cMApJDMb_4FM3_SieMx3neFCtaMpcwla0j2SOWpVF5QYLOlnUBFISO0RRO7NkFMW-Ojq03JK51QEaqxoWb8Vs6Y72vCp_mUnAsTrtvqJd2psyWZsV-iMwpovesWt2LLPNT7jMvbawz7e-BaayJbp-1dBKGwrvEiJCLNltJgEUNmm-IWbc2IY-1lMyGOLOqqHvPuji-5yLoO55LgX0qZ4AcjEBQZApkOy3GQpWmQYQ8-iNG1xe6o_X29sukAoadDV5WdsmIG-fEUA0hdjpy7zTsxlu1EMy9_Sw-Kp4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ خدمات رایگان مترو تا پایان اربعین تمدید می‌شود؟
🔹
رئیس کمیتهٔ عمران و زیرساخت شورای شهر تهران از ارائهٔ لایحه ۲ فوریتی شهرداری برای تمدید رایگان‌بودن مترو و بی‌آرتی تا پایان مراسم اربعین خبر داد و گفت: این لایحه در نخستین جلسهٔ شورای شهر بررسی خواهد شد.…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://telegram.me/farsna/449836" target="_blank">📅 11:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8DKA9aEGHFK_wygbDYmLoMjD05CuUmPEjSbp3HAI1lKPLQJ2PZ7FF0nQmQ3YSc3IWlOvPFlXfBUN5xKRAd-xyUP7K6kYK8k359Yz_xivTzisry_Ft3wn3SfY4y8wucFJUo-6aObCGBH760f69ZKPqEOFM9P1j0rNevpfaN8FOWKxccDIto3bOhoKxOJCyZ7ZtcQxLc_7a3pZFxSZeqd7PLXbZaEuu9E-M6Sjm0PtDLIK4JOUg9Hw1ZFLReuX5M3OvDYJHfcArLgCfa1O3asmzmZsR6DXXTrwRxib4eL-CM9Eb9afgjWFKEeBDWr9-sK3HeoSE20CotaQosVZDcX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: نیروهای مسلح سر سوزنی بر سر تنگۀ هرمز کوتاه نخواهد آمد
🔹
تنگه هرمز هرگز با جنگ، شرارت و تجاوزهای آمریکا بازنخواهد شد.
🔹
احترام به حقوق ملت ایران تنها راه بازگشایی تنگه هرمز است.
🔹
موظف هستیم انتقام خون شهدا به‌ویژه رهبر شهید انقلاب را بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://telegram.me/farsna/449835" target="_blank">📅 11:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJcTFFWiypbFnwKjICW6fBejFoCIXPW-kwY0hjxA4VbsaWI2-KpzIL_FfTdQJBOk2zOxyhKOnmGuwuMKWKBAFIcCOV50bdOZVuVkhJyGaFqR6w6kwbFrQAe1VE1vrdXuFEGH6ZBf2jKSdW8HC7yz8oYnD3673aLVWnd4lOAbfIM_eQxJ0ZR94-N7U1QEvv8fGmeAihwf9jHMI7YL9Wk1oz87C3JjDNbf09NGWUL0b8W8ScbuYEdN7ONHmqNrdoL-_Enm5dooWd9o7MBEp9luYzttex8s-ke3Za4MNiQaP6JD63erd9XRexg-a7HReJNovoDb43YmCsjQVNW4aZ7npw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دولتی ارز اربعین، دینار آزاد را گران کرد
🔹
دینار امروز در بازار آزاد با رشد بیش از ۱۰ درصدی نسبت به دیروز به ۱۲۰ هزار تومان رسید. فروشندۀ ارز در میدان فردوسی می‌گوید که «نمی‌شود دینار آزاد پایین‌تر از نرخ دولتی باشد.»
🔹
تا عصر دیروز هر هزار دینار عراق…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://telegram.me/farsna/449834" target="_blank">📅 11:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoAAfAMfPG-tR3KvtLGhs3fAwkmvmIIw3_1admUTuhlfteQ4bOa6100XcSoJrfx0JVEPHfpsdK52dqauSwKrsUiRKpeQqZdu-Z_3SwfPIGPWxTTCQqT97mxTOsinvwz6OzN96UuryO4s7srikBFr9W59q6jeWwJg7dRPbpHE0giVagF3lL3netlBM2zF9tPLsWSGjpXQNbcOdpeGFkyRUbyHirVg9d_3DUfTqc3QfFw2atKIyetMNzf-Seka48qXgt-XGrbvzGoo79RMlgU5r2qXyA0Gzkdjlg330MjYA2sDNhNnnVqJwYhtnf6M-N_J15etAglA0jHhOiZUzKOxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولتیماتوم کنگره به پنتاگون برای افشای حقایق فاجعه میناب
🔹
سناتورهای دموکرات کنگره برای دولت ترامپ و وزارت جنگ این کشور ضرب‌الاجل تعیین کرده‌اند تا ظرف یک هفته آینده، یافته‌های تحقیقات ارتش این کشور درباره حمله ۲۸ فوریه به مدرسه دخترانه شجره طیبه در میناب را افشا کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://telegram.me/farsna/449833" target="_blank">📅 11:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کیش، قشم، بوموسی و بندرعباس
🔹
دقایقی پیش صدای چندین انفجار از کیش، قشم، بوموسی و بندرعباس شنیده شده است.
🔹
استانداری هرمزگان اصابت پرتابۀ دقایق اخیر به بخشی از غرب شهر بندرعباس را بدون تلفات و خسارات جانی عنوان کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://telegram.me/farsna/449832" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY4lBIHuvlJFXiTDKfalmWDCffa8BxooJqrUTqauB6fFLvQpCVkkXpxpC7XsiR9lJk1S8FlIuYFfVD1a8IDZ0pI11SAgbZxc9rGhCZvEUCRtocWq2AhnuhG_7DkPXbGC3ZJ91Qu_ANhnVRC2YAdl6urO4sChObDchIyQ3628UyJ9-i8EOuUdQYMuHKTBMFYl0i6wWAhoGaiNdGFU8IsBYf9mOW7UvrcK-bxV3sRRbqYM1FsR4rr71nqjJI6EuWYc43yy-1bIBWYziCtA2gLj5r1liuIsosPQDHu25yzNGHX6qCme7IPvcVqYuQvMyHifJbXR3dvHs-5DZ-ZK3oOWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از مسیر جنوبی تنگهٔ هرمز هدف موشک قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://telegram.me/farsna/449831" target="_blank">📅 11:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e135f00.mp4?token=VMiqo8w8fY0-IlYrKebC_9TUggsWfwVJOz788nqxDenSn7qdG53iBJBbUVoNh2e6MO2qiDZ5joxGvkt-wUFrsOkoOinGrbPC8g2kdBW9BPOnLKEruNnulh_NBlHheBAlp-u-lF9YBjlgyMKwpG-Ox0jX2mwsP20GAUrRl3bNAoX7fQkYWZSqrBo98Aasl21oP3aUgEgettOmjUXrW70oMDR4qoFqJzWb5GXGKHH1z6t6Gl--Cej1hWO-vup9zgzo_5c9x4gz4qcC3WVcFXtE3y5ihVxRJW7ocpk_x5r27XFPzEiqa9zwU8cBkrHgaCq1ll3qrgpowVgV0JC4hAeaiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e135f00.mp4?token=VMiqo8w8fY0-IlYrKebC_9TUggsWfwVJOz788nqxDenSn7qdG53iBJBbUVoNh2e6MO2qiDZ5joxGvkt-wUFrsOkoOinGrbPC8g2kdBW9BPOnLKEruNnulh_NBlHheBAlp-u-lF9YBjlgyMKwpG-Ox0jX2mwsP20GAUrRl3bNAoX7fQkYWZSqrBo98Aasl21oP3aUgEgettOmjUXrW70oMDR4qoFqJzWb5GXGKHH1z6t6Gl--Cej1hWO-vup9zgzo_5c9x4gz4qcC3WVcFXtE3y5ihVxRJW7ocpk_x5r27XFPzEiqa9zwU8cBkrHgaCq1ll3qrgpowVgV0JC4hAeaiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک پالایشگاه دیگر روسیه هم هدف حملات اوکراین قرار گرفت
🔹
پهپادهای اوکراین به پالایشگاه نفتی شهر سالاوات روسیه حمله کردند و دود از این تأسیسات به هوا برخاست. این پالایشگاه تقریباً ۱۴۰۰ کیلومتر از خط مقدم جنگ فاصله دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://telegram.me/farsna/449830" target="_blank">📅 10:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امور داخلی کشورر: محمدصالح جوکار</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://telegram.me/farsna/449829" target="_blank">📅 10:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌ موسی احمدی رئیس کمیسیون انرژی مجلس باقی ماند
🔹
اعضای کمیسیون انرژی مجلس همچنین برای بار دوم فرهاد شهرکی و محمد کعب‌عمیر را به‌عنوان نواب اول و دوم انتخاب کردند.
🔹
همچنین رضا سپه‌وند سخنگو و امید کریمیان و عبدالحسین همتی دبیران اول و دوم انتخاب شدند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://telegram.me/farsna/449828" target="_blank">📅 10:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انرژی: موسی احمدی، مصطفی نخعی، مالک شریعتی و جواد سعدون‌زاده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://telegram.me/farsna/449827" target="_blank">📅 10:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449826">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت
🔹
روابط‌عمومی سپاه سیدالشهدا(ع): به‌دلیل خنثی‌سازی مهمات عمل‌نکردهٔ دشمن از ساعت ۱۳ تا ۱۶ امروز در پاکدشت تهران، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://telegram.me/farsna/449826" target="_blank">📅 10:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449825">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اجتماعی: علی بابایی کارنامی، رحمت الله نوروزی،  سید حمیدرضا کاظمی، مجید نصیر‌پور  و ولی داداشی</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/farsna/449825" target="_blank">📅 10:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449824">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امنیت: ابراهیم عزیزی و علا‌ءالدین بروجردی</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/farsna/449824" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449823">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اقتصادی: شمس‌الدین حسینی</div>
<div class="tg-footer">👁️ 16K · <a href="https://telegram.me/farsna/449823" target="_blank">📅 10:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449822">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آموزش: عبدالوحید فیاضی و علیرضا منادی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://telegram.me/farsna/449822" target="_blank">📅 09:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449821">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://telegram.me/farsna/449821" target="_blank">📅 09:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449820">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جم
🔹
دقایقی پیش مردم جم در استان بوشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🔹
سنتکام ساعتی پیش از حمله مجدد به اهدافی در ایران خبر داده است.
🔹
ساعتی پیش پدافند هوایی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://telegram.me/farsna/449820" target="_blank">📅 09:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449819">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBpUw2whd0VHwtWebsQk0ANZubZadF8d69p03Z4CtxWeHxNr0bLMCmSqUMP8BM9GpO2hHaqFhp_vfu5ewudHYfYBUylopCf_MFIEBX2fouEUYOtr1-Hx2-hxp1IknpZiklMoB_u7cljBII9_wcjQBL2brAloIgLz9_wHBtMBLCZP2OhYTVSPJr_IKAZYhjdJDqTtHuaDnUuD2D2vERs_GXKOCazGu9WRSheHtu_kbsZEzGqPzo2OASrpwRl49Reg32GskMkDoM4XoIaMnVsowLdOaV1aG6QtGNCXxf2r4OV3ZFm3yWWpEavT21iPTJ1azPVNxNyDoR_FfstoHoz8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://telegram.me/farsna/449819" target="_blank">📅 09:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449817">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حکم اعدام ۲ تروریست داعشی اجرا شد
🔹
محی‌الدین عبداللهی و حسین پالانی، از عناصر گروه تروریستی داعش، به جرم اقدام مسلحانه علیه ایران، پس از رسیدگی قانونی به پرونده و تایید حکم در دیوان عالی کشور به دار مجازات آویخته شدند.
🔹
نامبردگان از عناصر یکی از هسته‌های وابسته به گروه تروریستی داعش بودند که پس از فروپاشی ساختار گروه در عراق و سوریه، با هدف بازسازی تشکیلات و ایجاد ناامنی در منطقه شکل گرفت.
🔹
عناصر این هسته پس از استقرار در ارتفاعات استراتژیک بمو در نوار مرزی عراق و ایران، اقدام به جذب نیرو و تجهیز خود کرده و قصد نفوذ به کشور و انجام عملیات‌های تروریستی در ایران را داشتند که تحت رصد نیروهای امنیتی و اطلاعاتی قرار می‎گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://telegram.me/farsna/449817" target="_blank">📅 09:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449816">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo21txYHFg8_C3APvmh0EKYc3Ryny6A5e1TSDL_etS2ZIdXIF2D0PAGIAU7mvpuIrpN-3Z1t_5OlCrQ3pZBsYCQ7Y38_QgNpuJUD_qI2FwVf5NVozWVZa5Tu5igSISoJeL5e7zPAW5tlvnKZl3_j5_JPzS-T9ZRyGmwN--ZvLnHf16d3lBO6kJx6hwHG0wSuBdoiGvooproMDedU8q6c7XWjv7SltxwtOYIOMObMFs8VqV3lgJZX2j84Z8zh2E5azouTvvg9Rk1y_VgpSTtwseP2oOu_qAI-V9-Vp7azzKYaVZqGP1o8h8zAmP9vZwVP_1iAL4z1k1-FYE8lKJf8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم صهیونیستی: تماشای ویرانی غزه حس خوبی دارد
🔹
کاتز هنگام بازدید از شمال غزه در پاسخ به پرسشی دربارهٔ احساسش نسبت به صحنه‌های ویرانی در غزه گفت: حس خوبی است؛ نه؟! همهٔ این‌ها نتیجه سیاستی حساب‌شده با هدف «حذف تهدیدهاست».
🔹
شبکه ۱۴ رژیم اشغالگر گزارش کرد: «یکی از بحث‌برانگیزترین لحظات این بازدید زمانی بود که کاتز اعلام کرد که به‌دنبال حضور دائمی یهودیان در شمال نوار غزه است.»
🔹
کاتز گفت: «قصد دارم ۳ هستهٔ ناحال که ماهیتی نظامی دارند را در مکان‌هایی که پیش‌از عقب‌نشینی اسرائیل از غزه در سال ۲۰۰۵ وجود داشتند، در شمال نوار غزه احداث کنم».
🔸
هسته‌های «ناحال» گروه‌هایی جوان با ماهیت نظامی-شهرک سازی هستند که از لحاظ تاریخی برای ایجاد مجتمع‌های مسکونی یا شهرک‌های جدید صهیونیستی از آن‌ها استفاده می‌شد که بعداً این مکان‌ها به شهرک‌های غیرنظامی تبدیل می‌شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://telegram.me/farsna/449816" target="_blank">📅 09:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449815">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQo6wCVx96TtkxA-rsYl84PfdiuXE4D0pEGP3UZkWOiAeOl9pFXy9TKJhC0EgtwvxijUDzCV828meYgpHCjiLue-qgYF6UqqYlG7wfI5iGZHeRpk7nxCcF3VvE-OZlEE_x3NqIaSW-XXgNb7PVEZ7UarYeaqa5oTsaKZh9AbBxZchceK-yyXS4Qbv3yfMUxdKK777c8NIs_8FqbZwIMZ0h5Z2F_okMkFrJBQdOw_2aREDo7N3wjLMenKmZXIqsFKIEkKewwMHKp0nCIEAmrEP__tVxSDyvyMAnl-MK6bJgnu_eVIVHrB9i5RJYonyNdR2_1F6fpuITJ-nTXFQ5FA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران سرنشینان یک برخورد دریایی در تنگه هرمز را نجات داد
🔹
بامداد امروز برخورد کشتی فله‌بر با یک شناور دیگر منجر به آب‌گرفتگی و دستور تخلیهٔ اضطراری یکی از کشتی‌ها شد که تمام ۲۳ خدمهٔ این کشتی با اقدام موفقیت‌آمیز ایران نجات یافتند و به قشم منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://telegram.me/farsna/449815" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
سپاه: رادار پاتریوت، رادار کنترل هوایی ناوگان پنجم دریایی ارتش آمریکا و یک سامانۀ راداری اخطار اولیۀ c-ram منهدم شدند
🔹
اطلاعیۀ شمارۀ ۸ سپاه: رزمندگان غیرتمند نیروهای دریایی و هوافضای سپاه در مرحلۀ دوم، با حمله موشکی و پهپادی به ناوگان پنجم دریایی شیطان…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://telegram.me/farsna/449814" target="_blank">📅 08:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://telegram.me/farsna/449813" target="_blank">📅 07:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرز سومار زیر پای زائران حسینی فرش شد
🔹
مرز سومار استان کرمانشاه که از سال‌های گذشته تنها یک گذرگاه تجاری بود، حالا با احداث جادۀ اختصاصی مسافری و داشتن امکانات رفاهی مطلوب، آمادۀ پذیرایی و تردد زائران اربعین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://telegram.me/farsna/449812" target="_blank">📅 07:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449811">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29781b1500.mp4?token=bvuNE8YD6_TWi2hNIBkzjW8hRqrxvEmJOMH7-6GrKrogpsfdj0wg2jONafqf3ISQwpjmE37uU4dh2swRyrAXqI-c4FGePr33pa4fl9iMSLquErld5s3PNwsyvjVxCBuzK1DJi9W1WvywFbP_VDoNYOquLxGk1hDDZD94CaR7CHdVmNKVgzHrzQn3YpuNWxubTxuLQDnaxmnGNj2jj-yWfZvu9S6d76AdSe5vTjsf5uxDhoQnz6_6RStNwLAhlrLMDiYjgiP8Ht-_y6j430HxG9u5E9Vh1vYh3EzvMw95jyxVCqGchSsLxzMgUtV2IjSABkrwkMEoEkcesDNqw9zYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29781b1500.mp4?token=bvuNE8YD6_TWi2hNIBkzjW8hRqrxvEmJOMH7-6GrKrogpsfdj0wg2jONafqf3ISQwpjmE37uU4dh2swRyrAXqI-c4FGePr33pa4fl9iMSLquErld5s3PNwsyvjVxCBuzK1DJi9W1WvywFbP_VDoNYOquLxGk1hDDZD94CaR7CHdVmNKVgzHrzQn3YpuNWxubTxuLQDnaxmnGNj2jj-yWfZvu9S6d76AdSe5vTjsf5uxDhoQnz6_6RStNwLAhlrLMDiYjgiP8Ht-_y6j430HxG9u5E9Vh1vYh3EzvMw95jyxVCqGchSsLxzMgUtV2IjSABkrwkMEoEkcesDNqw9zYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مرگ‌بر آمریکای مردم بندر دیر در خیابان، همزمان با حملات شب گذشتۀ دشمن آمریکایی به جنوب کشور
@Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://telegram.me/farsna/449811" target="_blank">📅 07:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://telegram.me/farsna/449810" target="_blank">📅 07:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
سپاه: چند انبار پشتیبانی تسلیحاتی، مرکز ارتباطات ماهواره‌ای و ساختمان اقامتگاه نیروهای آمریکایی در بحرین هدف موج دوم عملیات نصر۲ قرار گرفتند
🔹
اطلاعیۀ شمارۀ ۷ سپاه: ملت مجاهد و همیشه در صحنۀ ایران عزیز، ارتش کودک‌کش آمریکا در پی شکست شب گذشته در تنگۀ هرمز،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://telegram.me/farsna/449809" target="_blank">📅 06:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
صدای انفجار و آژیر هشدار در کویت
🔹
منابع محلی از هدف قرار گرفتن منافع و تأسیسات آمریکا در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://telegram.me/farsna/449808" target="_blank">📅 05:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
سپاه: تاسیسات و زیرساخت‌های ارتش متجاوز آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
🔹
روابط عمومی سپاه: ملت بپاخاستۀ ایران عزیز، عملیات قاطع و کوبندۀ فرزندان شما در نیروهای مسلح، ارتش کودک‌کش آمریکا را به استیصال…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://telegram.me/farsna/449807" target="_blank">📅 05:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFSD2cy5qLWddHiqVQA3j6UHx90kh0Ov3KkErPvo3MYKTSl_20j6nX5QgyL1XXnyHZpVUjhHzGm7bzwxwAOLAYSLYuA40ebsy9Z3wzPqnvDbzDqq6s_65CsG51HwWi_xmtgnb6F8c94Af1sge6wecq7G8A0qCz8PbOK2L-u9fvRkOcnvIB0UeG7nKBjEo_0c1K6tP5L8mil8RScTC-Lr8YkveYqGl7K1KvTHHyARH_jGEpdh09dGOOc6gUp9YCjE-VVyj7bVdU5E9_7EZR9jGM3jsaZh0lV7ZsQJWFLZnBwggzpUWFhvLz3DXR30IBg3OBMuRD3k7CVI-xAErme5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزیل: هزینۀ جنگ با ایران در قیمت کالاهای اساسی غذایی اثرش را نشان می‌دهد
🔹
رئیس‌جمهور برزیل: ما حملۀ آمریکا به ایران را رد می‌کنیم و هشدار می‌دهیم که هزینۀ جنگ، در قیمت کالاهای اساسی غذایی منعکس خواهد شد.
🔹
ترامپ توییت کرده که تنگۀ هرمز را باز خواهد کرد؛ اما برای هر کشتی که از تنگه خارج می‌شود، مالک نفت باید ۲۰ درصد به او بپردازد. این دزدی دریایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://telegram.me/farsna/449806" target="_blank">📅 05:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آرزوی ترامپ: آمریکا تنگه هرمز را کنترل می‌کند
🔹
رئیس جمهور آمریکا بامداد سه‌شنبه در مصاحبه با شبکه «نیوزمکس» مدعی شد: «ایران ممکن است دردسر ایجاد کند و کارهای نامناسبی انجام دهد، اما ما اوضاع را تحت کنترل داریم».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://telegram.me/farsna/449805" target="_blank">📅 04:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
سپاه: دو فروند سوپر نفت‌کش متخلف فریب خورده، مورد اصابت واقع شدند
🔹
ساعاتی پیش ارتش کودک‌کش آمریکا که از شکست های مکرر عبرت نگرفته است، با تحریک شناورها تلاش کرد تعدادی از آنها را از مسیر غیرقانونی عبور دهد
. دو فروند سوپر نفتکش متخلف
که فریب آمریکا را خوردند و با خاموش کردن سامانه‌های ناوبری و بی‌توجهی به اخطارهای مکرر مرکز کنترل امنیت تنگۀ هرمز، کشتیرانی در این مسیر را به مخاطره افکنده و عبور از مسیر مین‌گذاری شده را ترجیح دادند، مورد اصابت واقع شده و از کار افتادند.
🔹
نیروی دریایی سپاه به همگان اعلام می‌کند همکاری با دشمن متجاوز که از هزاران کیلومتر دورتر آمده تا حقوق مردم منطقه را تضییع کند، و عبور از مسیر مین‌گذاری شده جز پشیمانی، خسارت و تاخیر در بازگشایی تنگه هرمز و ایجاد بحران انرژی در جهان نتیجه‌ای ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://telegram.me/farsna/449804" target="_blank">📅 04:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
آژیر خطر در اردن به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://telegram.me/farsna/449803" target="_blank">📅 04:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
آژیرهای خطر در سفارت آمریکا در بغداد به صدا درآمدند.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://telegram.me/farsna/449802" target="_blank">📅 04:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اختلال گسترده در سیستم‌های بانکی بحرین
🔹
منابع خبری از یک حملۀ سایبری به سیستم‌های بانکی بحرین و ایجاد اختلال در آن گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://telegram.me/farsna/449801" target="_blank">📅 03:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اختلال گسترده در سیستم‌های بانکی بحرین
🔹
منابع خبری از یک حملۀ سایبری به سیستم‌های بانکی بحرین و ایجاد اختلال در آن گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://telegram.me/farsna/449800" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLiLIf5laxz0Zk-D_LdcCCUUITpMopFgHivV5Qiato4AST-P6s5fpAwlxZMWZUYX0Fpd1TSg7TYWV36Hd2KHVUYkh0Eh1fOsYK2Woy--krTdMPbImA3VrngkTY_oxt0dALIMAtzu_4Z3QrUw2MlZTQ3BvjELCyzZ7wAlMF6BrXDdpIS_X7wLUKYUvK3UqqJzVK1D5HOnYSz408d5ErWantkWvvOTsJsAoH7VtrddX4zT4UgOYhjLBnRlL-Zjpbp82HVtyipgFCeEIj11bx3Q-moXfnBH4ehvl_de45DUpOkfUliNEzfXWbR7ua_wW_w_CdNXhY11XN__vAWW-sI3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت اضطراری سوخت‌رسان آمریکایی به تل‌آویو
🔹
گزارش‌ها حاکی از آن است که یک فروند هواپیمای کِی‌سی-۱۳۵ نیروی هوایی آمریکا هنگام بازگشت به تل‌آویو، سیگنال اضطراری عمومی (۷۷۰۰) مخابره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://telegram.me/farsna/449799" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حملات تجاوزکارانۀ عربستان به یمن
🔹
گزارش‌های اولیه از حملۀ جنایتکارانۀ عربستان سعودی به استان صعده در یمن حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://telegram.me/farsna/449798" target="_blank">📅 03:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0s9lRGSLdcnqYSF9lkR_gAL7nguHGE2eNChblLFD761VVVPdFeG4CB-CrGiANgkAdSwQWRLEybhqgM8TcjmMw7zmpI2iWs4QE-bkb_uaYMyV4HgYhbMwyMETmFxbga7ysJVYwP6OCdXglo-UTAArgZoprH1MQydJUseK3qoMeSKL5DfMjE_HlwYVYq7UVr3ldBl1kF7cm9Wvkt2SDt8oyddprdxqR0FfsyBptcwWsaKYP6sdfTH0OAwotYB0tBCrroNK7GoBrF61YSRNwkrGufio3gZvONLlOODSFZnxlPhcFTZMrASL8QxIH7Za_-vGbEmd6jub08r1hy5UEE0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6MlufIHHkm4HbKFwG8AMkdQqsmyteBB9kvOxuDzlG8wBAJYlTtGzY80hNgHByRhISU95u7Ot25Ux6dl6gxjOcdzXr5VSITIYNnHYhYkI3iweWc2mds_O3tmSCrv7xP_ZKRViKxxRcM7M1_9inzVMZGubqBBSAM8oMYLOxsvca3QgooBW8lVM0f_cqvHrbE7G8BpCgWyPA08KQ61EiVgQrRncVyvq7az9kQz9qCJyyLTRbpiid7k8CkVZ54luNkh9lYqSijm7Ylt3kxmIYCh4PJ6sL1WDGSWBkugswdLSYpEFn21vLaEqZBzy5LQV5WSE-3teTA3EPxzpwPSwcXHPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات مدعی شد دو نفتکش متعلق به این کشور در مسیر جنوبی تنگۀ هرمز و در محدودۀ آب‌های عمان، هدف حملۀ دو فروند موشک ایرانی قرار گرفته‌اند.
🔹
بر اثر این اصابت یک نفر کشته و ۸ تن دیگر زخمی شدند که حال ۴ نفر از آن‌ها وخیم گزارش شده است.  @Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://telegram.me/farsna/449796" target="_blank">📅 03:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449795">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
برخی منابع عربی می‌گویند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، مقر ناوگان پنجم نیروی دریایی آمریکا در منطقۀ «الجفیر» هدف حمله موشکی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://telegram.me/farsna/449795" target="_blank">📅 03:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449794">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
اصابت پرتابه‌های دشمن به نقاطی در شهرستان امیدیه
🔹
معاون استانداری خوزستان: ساعت ۲ و ۱۰ دقیقۀ بامداد امروز نقاطی در شهرستان امیدیه مورد تهاجم و اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
براساس گزارش و ارزیابی‌های اولیه تاکنون ۴ نفر دچار مجروحیت شده‌اند.
📝
گزارش تکمیلی متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://telegram.me/farsna/449794" target="_blank">📅 02:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449793">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار در مقر گروه‌های تجزیه‌طلب در اربیل عراق
🔹
رویترز نوشت: تأسیسات متعلق به یک گروه تجزیه‌طلب ضد ایرانی در شرق مرکز منطقۀ کردستان عراق هدف حمله موشکی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://telegram.me/farsna/449793" target="_blank">📅 02:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449792">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجار در ابوظبی، پایتخت امارات خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://telegram.me/farsna/449792" target="_blank">📅 02:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449791">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
به گفتۀ سازمان عملیات دریایی انگلیس، کاپیتان این نفتکش از آسیب ناشی از اصابت یک پرتابۀ ناشناس به موتورخانۀ سمت راست کشتی خبر داده است.  @Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://telegram.me/farsna/449791" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449790">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZONMYMG_cPBMz2Pv47AE1xIu4D4yV_CrkjqdZsYoxtYuU0WFqgv5Y8COMfEq7aJteCw1gSeFjiTCXSXJtpQ6ol_W4Npc45odA_uDTCUl09N9cyObxJ86XpbEoptQB2hZ7ZClxPxECPOHK55sxXThW2C9DXEiKjgBgxu78nUmFef6Qu4NHZVyGZcp6RZRWC3-2mcSXPz8DdvOt1RMWcT7NnRaxqKMgvypGhySVmce2nT6PJlrciY13ozz0e4biO0LfWywzJ8kohQbdmwdplKlwz39fdXKbivBmV5mLz98VRDOHHJJFmZ_WXTJF1l_rHPPnRIOTWk-t7Z1-y0A102syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
به گفتۀ سازمان عملیات دریایی انگلیس، کاپیتان این نفتکش از آسیب ناشی از اصابت یک پرتابۀ ناشناس به موتورخانۀ سمت راست کشتی خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/farsna/449790" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449789">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در کیش
🔹
دقایقی پیش صدای چندین انفجار در جزیره کیش به گوش رسید.
🔹
طبق بررسی‌ها این حملات به حوالی اسکله مسافری این جزیره صورت گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/farsna/449789" target="_blank">📅 01:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449787">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کیش، قشم، بوموسی و بندرعباس
🔹
دقایقی پیش صدای چندین انفجار از کیش، قشم، بوموسی و بندرعباس شنیده شده است.
🔹
استانداری هرمزگان اصابت پرتابۀ دقایق اخیر به بخشی از غرب شهر بندرعباس را بدون تلفات و خسارات جانی عنوان کرد.
@Farsna</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://telegram.me/farsna/449787" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449786">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0a432944.mp4?token=QdoZLa-ChQnssldxRhmwijWXS9oz1lM2fScrw4Y-Cp3IRwTl9T-Hphg0FSOgzIAxlQq88yN1Kz6ieHd8fKTHT450Ib42hMNUmHOX8HUdnsd5u79fYZQNUGxzjMSa5m_-PyVxuwVKNTlAw-i2-zpu0sbg2tPLz1vmcQsG0_Zxi48egDIO5tM-h9tguVWaqtlT6INS9vGdLpgT8FDiYPQdTp7hjXDT2M74LSFtb5e6BDFAjmslCeuJKbyVdAV10c6nsmgH5aAAiliICUxdGbIMxKdBJz9FI1S9TAUSOMjT3fBtq66MkmaGYYSSm9qehCcce_MpFjg3LXTOXUzKbbtcC5SDId-eCspb_GCq9-AL6CisOIiSI1-yO9HcixRmUIrxTOqB0-J1Es7GOJuWKglg1W-ZrUfIL6EwLIFRFUhNu4L1cLStF-Irdk7A7kbbXDcaCp33C8gNVNAJLrD4cuTguLNGmygOtoJ19Ja7rInzDIur8IJUTSOyN6iSWJU3q-dSyV7m2B7M8iYHiVVreNvmVfut4_VSiWDOeD1xPSbaucQkJ-OnJxonwn2zoakUWJFGfaRLwsSfr1g1rc0cLgZSHIQoxmBcXaBMUr71CwE93CBaJtvPJt7_WIT8j-gqlDvH8cdR6pQJECsXopbMHlw-JBlsmwm44AZu6r5-rWqHIzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0a432944.mp4?token=QdoZLa-ChQnssldxRhmwijWXS9oz1lM2fScrw4Y-Cp3IRwTl9T-Hphg0FSOgzIAxlQq88yN1Kz6ieHd8fKTHT450Ib42hMNUmHOX8HUdnsd5u79fYZQNUGxzjMSa5m_-PyVxuwVKNTlAw-i2-zpu0sbg2tPLz1vmcQsG0_Zxi48egDIO5tM-h9tguVWaqtlT6INS9vGdLpgT8FDiYPQdTp7hjXDT2M74LSFtb5e6BDFAjmslCeuJKbyVdAV10c6nsmgH5aAAiliICUxdGbIMxKdBJz9FI1S9TAUSOMjT3fBtq66MkmaGYYSSm9qehCcce_MpFjg3LXTOXUzKbbtcC5SDId-eCspb_GCq9-AL6CisOIiSI1-yO9HcixRmUIrxTOqB0-J1Es7GOJuWKglg1W-ZrUfIL6EwLIFRFUhNu4L1cLStF-Irdk7A7kbbXDcaCp33C8gNVNAJLrD4cuTguLNGmygOtoJ19Ja7rInzDIur8IJUTSOyN6iSWJU3q-dSyV7m2B7M8iYHiVVreNvmVfut4_VSiWDOeD1xPSbaucQkJ-OnJxonwn2zoakUWJFGfaRLwsSfr1g1rc0cLgZSHIQoxmBcXaBMUr71CwE93CBaJtvPJt7_WIT8j-gqlDvH8cdR6pQJECsXopbMHlw-JBlsmwm44AZu6r5-rWqHIzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویری که گفته می‌شود مربوط به شلیک موشک از خاک بحرین به سمت ایران است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://telegram.me/farsna/449786" target="_blank">📅 01:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449785">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جم
🔹
دقایقی پیش مردم جم در استان بوشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🔹
سنتکام ساعتی پیش از حمله مجدد به اهدافی در ایران خبر داده است.
🔹
ساعتی پیش پدافند هوایی پهپاد دشمن را در جنوب کشور سرنگون کرد.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://telegram.me/farsna/449785" target="_blank">📅 01:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449781">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTTzVeFIUS3DkVT3BBCMUpbuXszYE_Wphlfz8JV5gb5H1_CRXE3PzKxpMLzY-pveixhCYJ66cH86wz9Gz5tQZVqC1PQTtHeAjnOMyL5CXclNK9OaVpkezvMQ7tdQ0b9KNnMKaMuspEUMD60XtCWArxK2vMy1XiY--mgE87rKLd99CNaR7LgvYlL9DCwhxBYEEIzFoFanjX-XWevj4DBdZD0cHoaX_92hsignJAyWqKnv2HEgFGLLbfHzlt6L9d5HvY1CfmTTIs4SOLFf8ntkihFHWqgcpuYH-ykugQ-w9y6ea2z1ZKixhH-ux1BA_Iv2Ks9atFNfGixxEfcgEbdheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lr3CkVyKIV12CmP8JisL-LTGAmzhrFn9AMnhlwDEyjGtdyaMIDUmyyKTd6fJ1hsao1L5FuxhxHMJY1sDprVUCjDo9pusF56GQiqGsbR8tTBhFDLV0VkAwhmgBNOK38JHf0KcBap3NdCMN75M2YcaUrD8yozb16BwUBYzPS59RHQ5iPThNDBbg1Ebn0MmDAraI-dT50UXiHy32_2MEdti9bbP2teX-m_aSeoMvGArQcjyto34WE2OVD_TIG5yX8ZgFx5RkE-3c5WaBAE1hpHcm_A2eOnvdaMJtYCGl4yMTocR5DjDYCcZFMKLNcNtlli2SYlJyjxOdKt0XRHyYgNn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoyoUD7L9tJiFyMiAviAuoEv4LuaOQV1t0ZIGoc0ApTGS5vxSslr7FZ_0V71xJ6h-_xtIdfxIWzNwjlrJNm_uBsMOjEKgz4I4tCusGGyMItZ1ZywcYpWd7QakvMTj0xmpaIf-FqgLEyyp85i3h14blvSL5Yi8VbMn1GfbD5vLXpL_3pODs31fIAYxwldfCIKQhB6Vnpk7sAphND7LYA7iMwMDqawaZQCK0vrKDjfOBOeGXm7H36VA0GZ7Uf1TVk6t8a_hiZzKyZlGTlcVRNTjd5HhIyozwmp_nWTlbZbL-kr1f0G_5ThaC8KKsZAxZ3TtFzqxahheBd8jSDSkBdRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1oHWPkcZeO6gMVtitcTprw_WL05h2pQ6NHG69GA_pPjktlT7-snHVm6jMvynZ6NhNDXL8CJCtbChzCvG_f_Ls1vyh85k2JZeCIAO7X4fdsQPmwmGv8kHuuUWIbcXbQHRfoVSLI5BtudDh5YHE_hr0ChSN686XF06Vt2WgUSr05c-dWvZSWfSyo0PHiet9wlr_sk5E-c3-_ZTKuRR9gxGEhIKJ4cOPK-8Yhu4fUi__Ythe-V6yO919CRePRsO84fjgjZbeMjlEhSr2pXTqWmlsRAr3c82f9gaDop0RCZggADo5J3oUm1o9roASU2RY0l2GltA3WWrvaID0kKNjodnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خلبان محاصره‌شکن ایرانی: خوشحالیم که پرچم ایران را بالا نگه‌داشتیم
🔸
به ایرانی‌بودن افتخار کنید. @Farsna - Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://telegram.me/farsna/449781" target="_blank">📅 01:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449780">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">زلزلهٔ ۳.۶ ریشتری در عمق ۶ کیلومتری زمین، حوالی منطقهٔ سفيدسنگِ خراسان‌رضوی را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://telegram.me/farsna/449780" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbY9q47u9hYuH5RN1tkLFXQCI-wYknns29eA8OqB7hkLp3M0pWvxx1LW318DnekvyQ6gZ0ureAtRItzPZXMQPUkn9t7hUtE7rHepuWszpkQi8oyiuQ19T7u1hVISTzS_kOLqqmDOnyTxYY5_4Bw5fg288hJBauqXEWOhwJJ0ExuagEqlW19m5HdBAYWvhHljbvoSBQ4-fF7sBJyI6ictgCpysbROEmyLdEid5wFUfcj0bcEOdDatZq4ctTVa8bLqGk67xvpGRXKp6fWqgtpCiiGclSdpRFUXMBgc_ljRVaPhBBoWK2ihPLPivMktfMaLrCZ4oaRUvgb3jY2Qv8PROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌بابایی: ما نمایندگان ملت مبعوث با رهبر انقلاب پیمان می‌بندیم که مطیع ایشان باشیم
🔹
نایب‌رئیس مجلس: ما به‌عنوان نمایندگان ملت مبعوث، امروز با شهدا و امام شهدا پیمان می‌بندیم که راه ایشان را ادامه داده و با رهبر انقلاب پیمان ببندیم که همواره مطیع ایشان باشیم؛ نه یک قدم جلوتر و نه یک قدم عقب‌تر.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://telegram.me/farsna/449779" target="_blank">📅 01:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنتکام از تجاوز مجدد به ایران خبر داد
🔹
ارتش کودک‌کش آمریکا بامداد سه‌شنبه از حملات تجاوزکارانه به چند نقطه در جنوب ایران خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://telegram.me/farsna/449778" target="_blank">📅 00:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449776">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05ee1d7d6.mp4?token=m4cTB_KTl2oX71FfNB6GdURgTeUoKQd5J0AWtDNOiRgaY_sOCLwuoclSegK5migoCUazDQCCYxRsauHZ_MFANV8SRbVr0BPp7Rr2VeRjrMiypk701oS-CkEe0nsW9I1UlNUnDkmsY4gAbdD7l8J1D_C7JsB1j3h_BkPDB85GBZY5UUHQy4UsMKeKvzoeSN_woV8vR-DxxPVysnw8xbXzcvUDomEMTy4Pab2GZMnEFrCJVtHoZJTdzApvgVxVpRfRAQsQNj8iHtIuKFLuhREDKh7nI9ozwx5he8_uiA49Ivoz7cPqEow4sCaVXOeUKmhvAILnyj6J4beUqHzy1dZVh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05ee1d7d6.mp4?token=m4cTB_KTl2oX71FfNB6GdURgTeUoKQd5J0AWtDNOiRgaY_sOCLwuoclSegK5migoCUazDQCCYxRsauHZ_MFANV8SRbVr0BPp7Rr2VeRjrMiypk701oS-CkEe0nsW9I1UlNUnDkmsY4gAbdD7l8J1D_C7JsB1j3h_BkPDB85GBZY5UUHQy4UsMKeKvzoeSN_woV8vR-DxxPVysnw8xbXzcvUDomEMTy4Pab2GZMnEFrCJVtHoZJTdzApvgVxVpRfRAQsQNj8iHtIuKFLuhREDKh7nI9ozwx5he8_uiA49Ivoz7cPqEow4sCaVXOeUKmhvAILnyj6J4beUqHzy1dZVh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خلبان محاصره‌شکن به فرودگاه امام
🔹
هواپیمای ایرانی که محاصره یمن را در میان بمباران فرودگاه الحدیده شکست، به تهران بازگشت و در فرودگاه امام به زمین نشست و خلبان و تیم پرواز آن وارد سالن فرودگاه شدند. @Farsna</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://telegram.me/farsna/449776" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzM-RSD1B7hvwPp5OmK5AwuMFh8nLOYhBXIU9JuX00W9lyNfbLpKNwaOBl9S-cBurr6ZMFIhnxRs44xdknepZ9ScwmTDGRI2BxgiNaJu6ZVkkjAeHZDw_IASp1k3jPauqy475v9zT20IB9ssBqYJWU0x3YD-IvXNtrG-O2z9TCkbacBETLKlEVWvkM7nSUrPuQVDSGMVWniEPTDqXl_Rc_CYFq3_ayZYjrUBBHz5PdIUECl_Y5ZWKUXcmj0TlgCVOgXu3_r58RaYh9J7dCBPivNzhu9kewqVjA9YZaReID7IHu6y2Ja14O028LeZRytricdv7JA7ePFe2jWwemIC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6xYMdg-JT60BcFkx3XJStwmv72cBY0wsCeswSHFgpz2eb7-ZSxjxPjuV5HaTnIYFxx3J5qmQ44W5tFUw1u3JAldfvM8XO_cCDgNpdEr9-qKhEDNvdX5PdS_KTa73TOgQ6QulgaF2KYwphr7r3AD7vjfWx63ZHlCOVLrvNwNF9TwAoo88jLSb1h-zhmSM4AYC0zhi-WBezgZK3ND851YOy7IZ64OTERqvnA3f5xcZhufa_XfmLqDARcfiNDD9WWRnfAbyjKN3LuFgH2mmiUVUysfRA4sQgfKgrXD7kS5rNxRMIsv0UdQh6ASlxHPk0Zjj46ajDvS3hvYwOiO-mfs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2Z8eDnbNLCdnNiKrKvoST_juPPv2XYbNHA2P2_IuxyToJ8nHgAyffNwNtHR6Z8uX1x4WSd-BTea1tdiJ_Pw3izRkdNPMFSqffKRyxpi_dZfSOG6T5iAeLYjs-4O0ZhrRPdFrjcaoNA1fV3ekXD0SibV9OUUKeTuQvYqzFNCbkCzptOegvTbB1THKWBzTciUowcUaw8yy4dJJF51hvKatrssJ7hGwNekkyLkML23RunHFZK4HxPXnFgAVwNxyngcGONiArRTpwBbHuBAwhmOtNJPia_3gvhcm2zoZkwYGNXyZo7PRXYYSnCj_SGibuKClB9iX5auS5-jLQZFcHs3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7zrKEd9qnL_wovkkvpgof1B-SQ2BeIAJar1FnkjlyEo8P7dFeqA6NyVK0gOehgRxcJvQ2F7ZU96YjlEGxbzrXPNVM8IoldrH-tzJrFNb1z04hvM6dc3sIw4d3C8nL79-2-4tbxeQUO69OdgYirBIsdMpk7rBriXBfJnMvK6VpSPLueazCcjIpQZpXbK5m3OmcjqiwfYhK4LZMl-S8kfnYfuI2qVAKDF6VUlkrnkY1qI55NwQ_ks80dHITLFRPMCGnpnPPp-QC69Inm4nXO6dGz80n_NKT9sifKaLDu5-a-i7p0mrgPBOIDxdEPzb5eDu6W-2fBzNdFef8B4RYVFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INQeQTcqi4SsvxQuQ9OwdLaeXAW787TFbS-w1ss9G3qK-DhRRxRHzw_MMmbFhkypPotG0lFkDneFojkhA4knwvd_b0Q8Wch6k514ssmAomertlOBaPK429-qCwNRiKlQa-gOpK-uk5Hkm19tmfG4s10BQmP-M0tAxQKGkUfq36-jJnXJV1YUfjrpqto0qmZpuASPlKlsm2kLOfD50xCM9b3-Ez0DpFg23WfNCaTW8G_kSnlZnf8vLb433AMK7NKv8KpHunXwmDJi1Zr0BL92NPQNuX9adqqjG_8pD3uzx6V8q6VJRZUHgVjCPg-gbVfgZc4n-6ymQozj_Fk6L6yggw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://telegram.me/farsna/449771" target="_blank">📅 00:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwHcoW1KABk0dNzl1Rjsn3deujS0FSqpqweXHXCKl6_dY-wmKRI7lQuWEnzZF1kuXK_EgnDvkzRpZyvMWq2euyW8S7rjxe7QE3Tqa2gff-pgEaUvtoQeTVDFMExLWcgNJmcPMiBl9ZRb0_BmoQyCROLi3mFBBStJmdjaG8Vae1-lHkJGgVc5r-MSe1CaZd8qmMaD4TY98V7d8tCuOcl-CQCFF0890eE_lFNwgb3Obs8Bihalpx7SyU7pZmSVNLCVLkcsuMlNW8ZD9s8FPCneCGX3XrduvFWFAirkTYAuS1LBYDUFmKqq4sBxc-v8kt3tJ5d8autF9_rsK0qbhFJknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLpvQ3uEkrdAjLOi1q2BKNusYcF7Yzy0twQZ_y-k1qrE4vjwm6334ByR6nhSjgafAY5gleqpdRXBHxGNAgUkX3r9OXFuF5MW9SUTYQrMMitgbAX6k2u_W02S2KjTeFc5VQIlGIBOTmr8-34rMRuWaZVQ07ecxX2-CGihRU6YsEGXjVZvCelLFrBiFKi05kKY1SeXlk-ateuMp5K0e7s8TYPSP2pFB0QUbkuf0pEh1-mlIlFaUPhfVcS0UeRp5G0SUtDVwPVkxrmcBYMRcRnarYo_lpJcXMU0p3801GecrwfByI4SaQq75k7dgoCv1Qjp6_V5QLChsUxeveOvHTpfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtZajfIr5SFywQnOBRSngETHlWvhqdcGgwqhUUekOoeOSiYdK_ItctG3m3xyvCfA6slRtjlaebNakCFleTRMCDWJA582UK-I0NR_esqmCyxceFdD-L-JvKlO9hBpegVZoKg05hhi-_FFMT1Jqb5Zx-JX1Zx9R5P1Z30YJ4nj7-RBlJN4_WniL9_lL5ANqDVaAQtQJWI3-k1UPVLo9PtFOtRhqC9IoUNHDUT7oOy2BEzBlcEDG6Ttxdc5ixxZmKElWgAZjVNdiMXAFoWJqa2Axf3PTGkR4ydf-tV0ZyxODybolcj-oTNsFsZvLQ8dEZ5p0ZdqJ_XJy6TbjA9aV9fTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fxhohD3OrabvYs19By145n1mJfYAkYfloze0SxYWPb-jIVwwAdC09PGTVOcQZhbuo22a2xWcysyz3FVL9n4gFsxZyBDP1piTZqN9sU5XmcGW8vyakX5Aduv2OLmaGMGpc_zKgB_7DvD7FbfG1PdpGGJ900SjTmB7Dpf0Xvh8xPnIby9jwHr9kambPeaOPBjwzF68Se9u-wv76qPG5-hfj-mvVUXsWKnV0NCGd-Nfrd91gDKyLY5qxe_5iC1J5y-GMIKe9276YBzgh2J-TKzvVReWj4VuzApiMpfJjg0AUZ3F2k2cbqWxJBZn3GSZi4MAfLNqzrAwQXP3QE4_OHcNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF3lyLOAiCGn6meVaWLGnyF09UiJz8EBY5JXvw6WHlnEZONRbPneWlR9c0O7e8SWdC-JM3Ad-wvxdz3uZylnNuEMNIPbeWqKHfwvniPD0GdQiulqCjh-EuYzS93Z_kvsJfdjRP5XHh2HVeEIzt4uaR6v3rX40SYL-g3SdhLe8jEwc23YTxdjWulu9y9Jt41FMMlT3nH9igKW-g3kCGTJ04767FxKE52gz5I6aGB3i8a6uIhBp_XnjSYuk7nIn3JHnyJ7PZTKy-b_imcS-CpPl94Kl1zd0hOpn5b0Rdru3uetPSYdkEKSBUsSYCBzVWxyYgEYaVTMpiLpcZMcFKt-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldNV1VaUssziahIVQMsSF_Yzc6FmBQ8paSTj3HZRyYB7AOFzTWSoVzkox4jiReSoM6rmv4YoTFL_vy8Lqn_h2wEYaVxHuPXPj_RUTD54XQ0eAjJSg6Ltg9CoXpSlxfvlf1brCJ0oNYiPItiXnPpxsWgSEaXs75swvb7_ThgQxygvKUWN0mt8hlCLIUpCSYingCX7ngPOmA_PSJU2mRUv-MsAoLTN5VKg0VLFayBhKh3lPiDEp0gR7UQsGzMYVELEvB2IpYTHhSj6QCJlRCDuRKv-KxN7k4-u_AjNEYyAT9tob6VlG7UNJRmxpxI3_YUdJTmfBo4O2OF6TcDOJy3zJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nd9Sormc2pdubSWpOr8D4rjOl8h1anZQh9Q-lT6FnL-Eikza-V2kwEN26edrJotEuxsTLP5tqGtk5X0WTBkHQjyvZ6wnijy-SbgO7IBPL7GU7osTs_SpgNk1iIu9TkZci70oeH5myUQsgBwtrfpjr1h1tKjwBsgFZ0TMYhN_ZRydHj2Lrh5u0VQYsBryrK878W8iT1f8vIrcv3jrJTzQtYrvKvIP8vearyYCKL24yck7pmywM4aI79-DXEc5RO9z0kbfjCnsCXFpTHF4idC9LABg7P8uQKyEDTZIXW19SESRx-6MTDfLefjZFHOlWSTA3kshfJL-a9W32tkk4UqUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsaj6vNIfDt7uUmeA-u4-pWTwjPZB3i9zLa6qD9_CXlkBBDurznarjTBSCx78AyjUTHH5ttaSlLT-hsq7SWAt2RE6NQMaPbv0uO-A9sAA5_fyjJrRKQ7-al3q_GiNT-jnNj--gnnfqkL5XYRO8ErPCflWlU9up6ge0cHiBejEGT0fv6SbzmPW27nBeYUSxwb0T1fxb2cTUCwLpMCYc0T4f-DSYbK40LXxMX8Qh8-0Pw_ln2eh5wQGRRSSTYnH687XQa7moUbsgMYaz5Cd77bxf-ZLQyUZOyUeGZu2B99M5M6G9Tfws2S3974FQOF0pWYU_R8mYiz3fTiQFyaKVHw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRZbwjMw23f2AZDFJoXpkXvINL-_8z-a-9M1OFHtfB6WTyxeh-SPl4Kfd7o1omEoytutxng0ouyLtglrsyn5YY2RAJ7L-HgNSGkEv-4uRShI3GvspdgiGJB-01tL6kUpzgI8hiEf2d9nTlaPrhGl43akOk45iKPQFiYL68LU0VQNv2cBPDypE48wq_a3GXBCBCPkxxlDv7csTzuPJuxTbZc4jrUfGbGvZJqgy0Wl7jErQTqXq59pBywJ8ybbd1SM_lIVNNGQjKjdbiVwNAIBacUBnETiwABQm0CWPIQvwoKFiuEt4PG_1o55Ap9AHxetTX3wrTCgabbJgliMHKZ-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3KSVrlg03qjeFHYPX5Yw_jCbXmTnso_eL4GnvQXUfq8ebPOs4SwMBEPTlHbQgvKeo7I8XYAnRKygapj2FYdoz3jBD21WPOkVc0rUPSmG6fPVxlqUTHszNLPMNguozHvEdon8fSSGqajW6PdqpwcUlausFmFgXQOWc2lz-JOFeVkSV116NkDT7Vc4KWCGV0-g5wB08Upn32wRB1tnzvfJ_M3vw313Bw59YVBUU_7-z7RaYWYt70GZk43fdC-AJtVHSl8_mOgjSIw4UP6Z1ZapG36m3GRQQjvMM3zthl7BVg8rzhb-NDgyc-OdpPHuU00mKoCuLqLYab4WnYO551qqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://telegram.me/farsna/449760" target="_blank">📅 00:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e2e270c65.mp4?token=QZaWAomey_GNzxSmmyYzeeHTZlTDOMJoRZqv2_CMIljy32JQNBk3v5_DMYdUuJ7ewzpjJYn2LolhKJNU_CJVFmN0zhDBeeaku91Sfq4Cauya6I4i96HketcgyY2h9UJZ5-pNC4Vp3pCYPWHP1s_D7nZJxU2eacaYBRaLCgklqK1WJYl8vGYD6IUbbJpp8gOng_KDnHmFfXwHH_6FMs5lLop6MBROq7a-K5R180tw48bYlCC8dP48gHKI9YpLf5E3X-o7kaii5NqSeKmXC_KPhEKvxKU02R6AfZKwXDObYfTM2lVaUbFXltgzI9_7Y7PehUi6dxmzbLmyVQX2_G02-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e2e270c65.mp4?token=QZaWAomey_GNzxSmmyYzeeHTZlTDOMJoRZqv2_CMIljy32JQNBk3v5_DMYdUuJ7ewzpjJYn2LolhKJNU_CJVFmN0zhDBeeaku91Sfq4Cauya6I4i96HketcgyY2h9UJZ5-pNC4Vp3pCYPWHP1s_D7nZJxU2eacaYBRaLCgklqK1WJYl8vGYD6IUbbJpp8gOng_KDnHmFfXwHH_6FMs5lLop6MBROq7a-K5R180tw48bYlCC8dP48gHKI9YpLf5E3X-o7kaii5NqSeKmXC_KPhEKvxKU02R6AfZKwXDObYfTM2lVaUbFXltgzI9_7Y7PehUi6dxmzbLmyVQX2_G02-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
هواپیمای ماهان‌ایر از فرودگاه الحدیده برخاست  @Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://telegram.me/farsna/449759" target="_blank">📅 00:31 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
