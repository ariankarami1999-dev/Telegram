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
<img src="https://cdn4.telesco.pe/file/kMA480aO3f68fndHC4hfG6R_FWf5dLBG8Gc3gO4v6jfzcDIhmnQWE4Hb3HdGdWwuXe-NLIsP8dO8zJ2yY07hL8dvPOgFsHTQMcYR86goavRIV4yZEdxbV4b3c1BZKPuYERw7PlZ1-TEYoXFc6rHOpx8KE6EhFB1QYfQVQMrlE0-vKYaQmjsIm0FooRTTuMzsws5dEvkTgUhX9VCqpZu2VFNV8ZtktZKsTmOyPgR8lsC9rjB7sPY7Q8s_o5gdkjF8DDj3vtu9hhHNs53rH_1BFJftUEtTYobIxlGoXH55tAWy_8npmAdarsrfjuo6DoHTRhxRCg7Gcud9kPWnySH9WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 02:35:05</div>
<hr>

<div class="tg-post" id="msg-440588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل به تلافی حملات ایران، گذرگاه‌های غزه را بست
!
🔹
سی‌ان‌ان: به دنبال تشدید تنش‌ها با ایران، اسرائیل همۀ گذرگاه‌های منتهی به نوار غزه را بست.
🔹
رژیم صهیونیستی پیش‌تر نیز همزمان با آغاز درگیری با ایران در ماه فوریه، با استناد به ملاحظات امنیتی گذرگاه‌های غزه را مسدود کرده بود، اما چند روز بعد آنها را بازگشایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/farsna/440588" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اعلام وضعیت اضطراری در بیمارستان‌های رژیم صهیونیستی
🔹
وزارت بهداشت رژیم صهیونیستی: برای واکنش سریع به وضعیت اضطراری، پرسنل بیمارستان‌ها به‌حالت آماده‌باش درآمده و فراخوانده شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/440587" target="_blank">📅 02:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440581">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAbB6SZkV--mfWO_M9yHypFhD12VHViImqfp3qhQI0KVamD-ZBcaeCmZf_nREoKkwzZQcd_h0kHTL4Vc6GjbBJIAodX4vkxeDRPljcO3DJdeYAWukuVG3hDOmXWGPUTqMLkwpJjNZGvqLpM0Ok8TW9q9i7xn05fy5AdBF5c2XYxr8rW-ZKeCGwK6MKnYIHZgjHFdpMXGOYmZ6B4fORrjBXrYlrBT6WWk8yC-0l-f2i4mF2YU9wP3XkQQ47uJUlpLbz1SzpjFa2KsQ1TjAV6GBN7cWDP3dDN38ig03mlT71UJ2M4O1_YtdaIYdTjENYXkw1OF4cC8llvJcevwZhi3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZ98wFJj58Wgl34PgGXNXza28rReLB4sj-FM6gMxoKRNhRzPOBb7ssXRbrovJvWiG29r0OHKEwRAw_AygUo1IhrnI0rihLHagHpbCMjNC2tKdYmVru6xVbN2snG5C20fYsRGT1Z2l89lew8xvmMQHTcek4EW4GC4QLJy4wzX3JYvo42TBQZbmHvjrW8bgrNgmhZkwyV6c8A3MLuRAhWK9yOpLIx6wUQWZuHMvkvDCzf0i4bkOym5HNjYGGOYEW0sla_QBhk4B5Um1XFdSL7-G90sI3oy2MS0QI97nQ0KmWwdIWlgPAkVSc-nTzg7w2196IhAh98r_fpkKvDUMbTndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxGZ5YB23lnQhYcjwUqyUmt3NQMA0JHUo4xjUs-IAtxZzoacixso1eKI0TyEfxyrOtETpCKL0uz8SXNY9hOGgeMEyvjtPCAaZo9QirG3wIuLu2x5_eHcgvlet1k_M1ol07t2RELAywn22tnyHvhXMFOIipPIF4xb0zonPe4NdFgjtE2wWGbwX701pDmwMBdhUKS0AbTy48e2wajZKrG2QQLgLVhBoQ5KQYiRL5H5h3AV1hgt3PT1YHRfhiVxueL0u_hAcTwHo2I72VawUn6pG3e6TyWmUcuXeAowTUk_4JQB-bM4e16jh2Wugj0ha8tsCL1bM70KUYvx7X7wcTduug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUyT5OT_4ANeKp7CCsI-3ZhLFBkQq5nx5RF0r9bAABU1MNg4rze0hLX_cSPEPTFK3A_InJLQdpx99bAuBNh-lx3x3ubKxyoot7v9WgNjxk59XJ7RqepaYVDNCVIh4CDvvJunP-aTSLL81W-jtrUQCwdgpYgnwc1xEyZJ2DhywTaMvReC_SoDWltbRRqAPoNCx0Yxy5llLtrK0LZOX01zOFzuoO5hpOVrDRkeRRlHjywTXbJiYCgNG5r_hOX_flwIkQkId3pr51Xzs4cpPFr1E20U2Eg9N3q19MyCJ74v4lao424MKy8PukQrGxiuLJlqyi0k12LpErLi7QH2mMVSTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8JoqjED9lS1Y0neeZq9vFfrOUVbB0VpmOMzqKa-XMmBgnvkbLw44DeNlBXy_bYNEplOSL8AomcfxJNs10OCVw7nFujalqVBdF5LYn308gLH-7G4qEboWfcd7X9Gcsd1tdfzhsWKnqt2aYe6kqCeIneKjoelOc12ClJ07WVXYhKSfv8rZHCgBA5qxGpLebdptyIGmRzcKRhnNWprF6xErWixbXV9UqaMT7lkygQiOpcd4jBUWEfnUyMiMLLPcGPTtDzmyEImi3s7dIxEf-zEkwCC2iN5SKn9dkDuoGoXWeSfiHyy7DAUl2AoJfw3Mp7nmIOH9xE6VnSHeKp5wYZshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgncbChVQO8h659bxxw8hWXTeG4dL3una8lbr76VDQp3DQg4d7ofQkYmrMlwmJv0460_4lFJlcQWo1Zpa6IWqBCec-OeQ9-WUfzdDswngG3PuI7T0Umbfa-4FSLumuTJ6uP1zOQWXh_Z1fJccMk7gPkiRrs6U8RTLPbh-oGp3RBHBQplvBziazqrMdWb5iTsmX6QC8Zz1qfmXiK4c3b73cyK9-WYckr3C6E0kW6R5Vs6zV0xWNp4DEJn7GKm7kYkgL5F23pQY2ubdUBRNzs-hur9vPelDtxAATZzS6B2MOtlGdwH9q_8GMcEouiAit2UX1UI2kBd-dWilItLa9BCJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۸ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/440581" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVD8oP62wHKnYyCHKMFyagfYtNmwrhKlQVe814Noc1PE9QuRT8HxadQ7zpoiwsWcobUyCaPMuxnSHf5xagzeqdiBPg2867tEkigF7gZPehUJtYsoJf7BN2998ZxtTdEL7hs3pQewTZDg7ocEWU2TNWAx1N3R3huEIKQGe9AwSH8orqtW65jeMD9Lshxt1AUGCXxwNs5JC6NJRHaeKFQ5PFmpKQrX18ng2rGkKNrb2ZlNUA9T2i1od8K4s8LAOBXATUNsuxqTS7TJouyJMwNvOxX9xj9v17qF1UHqXzMMmOB8ky5tsGro3JtNOL4sfnMzvmAfEIdiaX-3r5tSZCHSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6ewJm1i-tyeM9TAMJEYn75KIjRL1dSHneQoBfBOm1DR8Z1uGgW54bBGIfFQooslU1kHYDs5Tl_090b5jka8-i8aI3BdqfqdKTMx1SBv9Ztil2QNPXvY0ls8wZR7KrwlnqpGCNs9wBMZGETdIv2lND81PUyDU-UMH7tNjqcJv64sSzrNzKW5jkGbI0Og7_B9pDg-bge5P0UM6WVQzL1tFKI3A2w8cdLS-S0iZVnWFT2qxD9BQsJtyBYm5I41r0n1WwTl35mY32fbO3G2Wugcb59dSaipNguRHPdB0Ctpzr0qxT1qBn1kkfbHlpTKI8gKeyYFNkbzPNwEHtN7LuWpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFDEHA4J0MzFOL8L3rhExpqcB7vYWIo6zyOVzKbg9qs8323viYV5GaFYT9VYA-N5hBkBo_JRF3vKIu5dPWilIkb1zqM7be6cZFXVSQRv0zHzTsuFuZ_Qi8fGquto4UMBF1Sso4R8l3NxreqDM6DbzjJYkStnrAN2se5x_uwaCn5pz4xvmA3avjOEIaUNcPmT_L-elOqkOTJb9VynHLGzaGE0UfoFmAMsFb6O0W5sw78y9Bn8rLyleQT5UIkGfRTjI42zkaMcLwLif7TInmkX03wB9lNFW3twu9N363Lx5dYEIqreHSYvneA_cLb2fhzkvNoeTxX-AIxC82IkqlvADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGdMY9Z3W_gfaYpEDdd9ONeDHUwtQPn7SM5jSaM3iT5oAuVKnqfbkjv3F_hqrzv4BGo9OX76WidannbJJ2ZvLoxWOVpQKpIDWmL-4ufIfa4IZEwM4g0ZmAiJNPwnK13gjCeh7slKFYu3V5j-sZ0HN3ZtHU5_ACNNeJNegTGueLXNAjqow2sOqPjytkyp60qrVJj4iGqfcgGstvnUVaiQuGqNghOfA8TCPo3S8dV005BkFpxzQ3neofR74IqKq0sJOgFVDeAsaTsjSii7FWwjXymAaXtW5OlSrm-SyaKJALIGRQGcFpuORzjMdXQsLixJSeyvcdQluv7Zt2e-_qu0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpA9_Z31fxbTf4mug5EFE_4Hi2cbTclSxYvXEwsL4L7WLcte6q_Koz1z6fB9FSmyNorAJ0CPPWTDwyS__lw7pd-mAMlwG_hKkHL5tv01YN_KH7Lf95nV4rVbIMrNNqSdNz2HNv2c4SgwCASpkdsY6K6rl-n3VU6-ugUuuAqvBbVB3y43LgW09cIhvJQScnqyXkTrwOwYTIZVD7xjDeLbD5DVdoro3XNvEj-rzeiUBto37IpSx606irj3oilXD3XqdavV_D9TOpyH6lQzd4HuJZ0ppBOAk8L12een7D4mRFZHu3PNKILtJlf_mu-bZZNCTC6Ul-6UQmI0vGEG0UyaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxILYMAzSy3z7NF8hhA0JwM1u-kc-Kc5hONaOVWKwas6F5t4P61f0GZ1J3WyxfZutlRYUdI-BaCRSy1kZG1edrQQmEwQXvOhx9LntfeYh3FWZrHx11kyIi0KOeEJmqq-aWYYCycCqM0dZwiLUTOaIo2PeSUI3U9iQAAF3LzhR8UJvrlozYFbZZ5sRyExK10ZLwnTTqZM2NQKaXJrVksc_eNzBJ1FF8zazcpFBlhO88P99Lsf9FfhgwTI3L0uWkwgbWKE8zOCEblBTZ4e5GY70Su9C7SyJ7cxAsvSCEyprjATZBPBPjL4O7YmmJ8YWA2y7VXajFzBLQB_b1SOodqRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0PQozQnsHD3Zjpa3xB04w02LVi-2iK7iwUo-bQSkVVCm2AiCWRbJfqpji-HqYJ3wEzpAV8QC8UqURE0l3H2uyQ8aC6s9lwxYGE6zFDFoQvst3sFAweEAnDuhLLeJSBojjgGu33ml5cj1wvzXVulFFdwocwCmyXt6Ee9s48DXUF5IYhERQ5hI-BdAzDyC7R9qEZ5Yd6iGY8NT2i5FgXK_KhszfbhTvYtahZYMGCNSybRiCvHIZrvF-SVquVXaXAYRlygeeHeP_dvSLCpuM_ArYGA2eGy-EaVrTMxUxrOQR_qlYNfTRs4tZoZp7AMgtreVIEi_AEsiCr4SEuuxW5dKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhrOJQfJildGh57UNDMOqnlyWr6rRXuxwVaWeWPsNC1mW5t6-TJMf29bUMyPML6HTQnLinNbBHsnqKcLPUR9OTyGdwZTFdgTXDb8AOzh2U1s6LK-85mTC1sBPWl4eRPVEPw_6Xu2sa4OAKvMl2fcAIlO7eiqUi9FH7rSvRCQWGQFImJgKCLu9mU53HyUsavfvNVhuyEwXSkeuYfI5iAaaWADhcrolZavJKiBtz8zJ7VBvE5VtD8tR4MzLGSPqcc61wq3olT3ticgFwTa4P5ZO6_6aL0dSJtR122btQ0LJf5giv-y2W78tQCxbHuEFpioyLD45R-KPeKLY8Cu9WrI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_2EvU7ywiHu9o97afJusU5jcIKSZK9dFQGxfqWjRCzkVrRiwguRt4e5QlCp-pqbjlDYWHP3bNFlN7qhghXWlZslmCKA2p4UCnVs7oLe6F4Wbw0xPSIktRVQkYPyKwXM5o-lcsKXgcOSX87sg34OR8cQkWNAICeThb-ZmABQq8ffnXRNA3oGQjGddM0htejBfeB3atAc3JCI50owSvBD4Y9IhfmfzU9oD5R8CUuM7jgtu2Fv1OMzOj1qvsR-Wtvrhye4i5YXoXTDkirpJhUfAFSH8AKyVa1mhIlLxZDCu3Q7UOXr964QDoRNLgrUza4mLk7zIGR1dUMZO2icalg3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTcmDT1WdGsCFXmvux4n7Nj2zZ5h0I8AI2JAaTqjmBsuxGHITsANDyipB81ifwaSXmG6DayiF33K0x5lx7gVUnCRQpk95SNldnADZaYiTnQWFggCOZHePbT98DLAcfs1pSmrmbl0TGdH867_o2Lm2II_IIa5dLeuWkS7wo1tj9hCyFmIfg99RAYopZTc4p3mF9RCWVggImXkn-y4IJPbs1E5Q9Q_fRkoNUyBMZadfqZIGf9KqM6TiStiwt7GoyL-KqX7Xzirb1_3NVfzh86dlUuIdgCGJRXiqcqkdHqIQ5_bxM79wb_9FJ5zAm6S6q4_N4loKlyKm2oHwOphRi--mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/440571" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8fb8a764.mp4?token=bAxfwtXWdQwhnjnOfOKPBT0nPZKX-VSXDI3SC5rg5fXmYsxrAeHbGiZr5D3SvVWNdUqJxYDUX1wjnTWTAK5i49pLZE5GHTYGJcJRIqm3vmW7KyvoEUvYYetY0udH3iJLAIh90fDaCI_aR0mxlUyzUIJAxAleKr6mMfgxbDKYq4hc1MR_j20CBqu8svd4sX0vYALqGCzexInMe77AMHlaayPfEpUQrZvEScNYSrRD_3wsWfFqtYZc4qszKkfOLrYVDdNoU0yaeNR2q6kX96Zw9iEfzSkUcCpF4fOv-92vSD9Ol04k1UNOdAswXvdY21oA-xqXGSdQP0oC87pnjyjsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8fb8a764.mp4?token=bAxfwtXWdQwhnjnOfOKPBT0nPZKX-VSXDI3SC5rg5fXmYsxrAeHbGiZr5D3SvVWNdUqJxYDUX1wjnTWTAK5i49pLZE5GHTYGJcJRIqm3vmW7KyvoEUvYYetY0udH3iJLAIh90fDaCI_aR0mxlUyzUIJAxAleKr6mMfgxbDKYq4hc1MR_j20CBqu8svd4sX0vYALqGCzexInMe77AMHlaayPfEpUQrZvEScNYSrRD_3wsWfFqtYZc4qszKkfOLrYVDdNoU0yaeNR2q6kX96Zw9iEfzSkUcCpF4fOv-92vSD9Ol04k1UNOdAswXvdY21oA-xqXGSdQP0oC87pnjyjsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد قدردانی مردم ارومیه از رزمندگان اسلام؛ دست خدا یارتان، علی نگهدارتان
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/440570" target="_blank">📅 01:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_7ZJa91rzR3InfuC_k7pl5rOk7lzP_LYrJateHFbEvYpZi5z0BKXB96F9o1vHtlrKdrsUAm0JJDQUsJ8inokmcg8rlWu4JvXxcl3Tr3sDMapxRIQDzHVv4lkhcno5uQbCFVH_DD1EDL2-qkTR0FtRcSMA_rFm7Ly9igJR4h6bKkld1uSzFgjaWrhvfwEUHvM-H9p9h3a0Gv70tunPHvgCE8pU5Egl-XoOhk-9Lff6Eba9uEtJQgJsQRyAKeckhls-KiiUjp0pJSlLHJq9wHy7FPJy2wzJYNxKmsQYBpu-xIhvtXZr3SIuib72sE0lQWoknMZB2aSAZSaJxmPuI5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
توییت ولایتی خطاب به آمریکا
انتخاب با شماست:
🔸
توقف حماقت یا ورود به موازنهٔ ضابطه‌مند‌شدن دو تنگه!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/440569" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
لحظۀ اعلام خبر شلیک موشک‌های ایرانی به سمت سرزمین‌های اشغالی توسط سخنگوی قوۀ‌قضاییه، در جمع مردم تهران در میدان تجریش  @Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/440568" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ محکم بزن</div>
  <div class="tg-doc-extra">حاج ابوذر بیوکافی</div>
</div>
<a href="https://t.me/farsna/440567" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
محکم بزن، کفر و شرک رو باهم بزن
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/440567" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زلزلۀ ۳.۶ ریشتری هرمزگان را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۳.۶ ریشتر حوالی بندر چارک در استان هرمزگان به وقوع پیوست و در برخی مناطق اطراف نیز احساس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/440566" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630a9342bd.mp4?token=qiofLE0d5pyDqCQfGUGRksad9_D6STcxsfG_Wa5UjAgf4UbdjpgM0lBTBiCe_4QHNhoUfv4q_H05kL_WjRUkRZfvh6ctn8GtFpQVNevdrloeoUlSqzh8ZQR1OXAHk3W7qhlhGrGhJKguDN94JYcHmz-a4j2u3oU4hD170HDOz2eoaOraQP1Dq6l4103fdhZ0MYVEs2C_httTTZCWGkeikaZsx7-Kq20MDD5ex6F91nQJrNlhpu8rer6C6RcMibtk0PYdQCZLTcaEadn6eYXpgUOsNAZl-DkicDjymCU1Xkv1abOpWcPy3j35Yg6-dgcoKaVzBITJWSiz8pkz4wqWtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630a9342bd.mp4?token=qiofLE0d5pyDqCQfGUGRksad9_D6STcxsfG_Wa5UjAgf4UbdjpgM0lBTBiCe_4QHNhoUfv4q_H05kL_WjRUkRZfvh6ctn8GtFpQVNevdrloeoUlSqzh8ZQR1OXAHk3W7qhlhGrGhJKguDN94JYcHmz-a4j2u3oU4hD170HDOz2eoaOraQP1Dq6l4103fdhZ0MYVEs2C_httTTZCWGkeikaZsx7-Kq20MDD5ex6F91nQJrNlhpu8rer6C6RcMibtk0PYdQCZLTcaEadn6eYXpgUOsNAZl-DkicDjymCU1Xkv1abOpWcPy3j35Yg6-dgcoKaVzBITJWSiz8pkz4wqWtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظر مردم درباره پاسخ ایران به نقض آتش‌بس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/440565" target="_blank">📅 01:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یمن: پاسخ ایران معادلۀ «تجاوز بدون پاسخ» را ناکام گذاشت
🔹
پاسخ ایران، معادلۀ وحدت جبهه‌ها را بیش از پیش تثبیت کرد و تلاش اسرائیل برای تحمیل معادلۀ «تجاوز بدون پاسخ» در منطقه را ناکام گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/440564" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ2zIpKtSNaQCkUuxDXMXO5z9jMWYVZlRUpIuNU_emzPfMVgvBwrWG2Ct4_NIFxkPVaKacP4CpfmKk8Xhgu4dFxUk51uY6IaHlLsWBnWDTq17kJ-F_GaWfnGFDU7Lmn_qUNrF3x-cD4x4WaHsC412bKD5QcT6se9m4Omi7l4P8Bbl1fbCA3EIF21pBxBEbo_5HVbrqwhxJL7xmmR8rIYtJItYxgqDfP1y1wabmfa6x-ucFKgZ5Qi_sRIE6EvesdMPh51lH1-BsqmM3p_6KDviCGPovpTkO6gckfUv8zNVaezRVXMe3hhqEEipGOdAMYs7AbqqQxRfFcsMMX4655Tog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: به حملات رژیم صهیونیستی پاسخ قاطع و دردآور خواهیم داد
🔸
امشب آسمان سرزمین‌های اشغالی را ببینید. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440563" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=Jwt2t_1aHdpnHGc2QGYFGZ-Fbce-qD28HaxSjxTDZEiS05oaI8smrMmGttyvn3XWbf5kbB7HMi8bh8XYxIJmY2EzY4pkyVNRdxR2qned4Q6eFRLFNK5cVBLDO9U1wC8uYL4IM-zSgKQ8E8v3JiCaOjtbpyGjFGx4ww_oAMoUh1FLK3JAcaBSJ7cEC_chRHi_jG3XXe3R7QGNEOjBr82K4dAye9ihxYY4rbzLPN9W9WmwEqH3E50XUaTgXklneRqQgn9piecD08Tl31VVojb88eB2SKijc83tcjUvuSrpIvMqrRt2ww_yQ_yST581tIp8QoUb_bQAHZcXTKe_utCfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=Jwt2t_1aHdpnHGc2QGYFGZ-Fbce-qD28HaxSjxTDZEiS05oaI8smrMmGttyvn3XWbf5kbB7HMi8bh8XYxIJmY2EzY4pkyVNRdxR2qned4Q6eFRLFNK5cVBLDO9U1wC8uYL4IM-zSgKQ8E8v3JiCaOjtbpyGjFGx4ww_oAMoUh1FLK3JAcaBSJ7cEC_chRHi_jG3XXe3R7QGNEOjBr82K4dAye9ihxYY4rbzLPN9W9WmwEqH3E50XUaTgXklneRqQgn9piecD08Tl31VVojb88eB2SKijc83tcjUvuSrpIvMqrRt2ww_yQ_yST581tIp8QoUb_bQAHZcXTKe_utCfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440562" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e30d14c42.mp4?token=c2dNMVPVMBwVuYM4-7O_DC7owtrpQQi8zJo8wvzTDxh-3zHtlmF6z-vGSRm5PgHc88clYo5NSJWnylIqfN-3bCebvdIe51NB1-RR4soyDjLzru5oHReY2K9B7OqcR8hI4PPEpuiEUB5qQ2J4BCSbJzrAfTPB6cTdtQSyGk3eGHnTog6rT5Plabb-DsasuTJFRr709UVnTIXBWQ0cI0-9A8ke9n9H_QxAbUZBbCPAUV0kbNzLGVF33fFnftvQHexqJONGwdbUuGZKuKfQlWSwRzas34rf2uS8d-PvU_SooLN0DBhLkG_zGyD8RwTB6b27KziexY9sl_7Z3BA0l-JDQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e30d14c42.mp4?token=c2dNMVPVMBwVuYM4-7O_DC7owtrpQQi8zJo8wvzTDxh-3zHtlmF6z-vGSRm5PgHc88clYo5NSJWnylIqfN-3bCebvdIe51NB1-RR4soyDjLzru5oHReY2K9B7OqcR8hI4PPEpuiEUB5qQ2J4BCSbJzrAfTPB6cTdtQSyGk3eGHnTog6rT5Plabb-DsasuTJFRr709UVnTIXBWQ0cI0-9A8ke9n9H_QxAbUZBbCPAUV0kbNzLGVF33fFnftvQHexqJONGwdbUuGZKuKfQlWSwRzas34rf2uS8d-PvU_SooLN0DBhLkG_zGyD8RwTB6b27KziexY9sl_7Z3BA0l-JDQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم به الوعده وفای سید مجید موسوی: خیالت از خیابان راحت سردار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440560" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40243c0011.mp4?token=H1vTb6f_NnJVlKNwZLF5RR3vq4wAh7cg23K1AYnz9JUIRHjQRB1tN4FKYpMPubwW4I3pP1TOFFKI7DHze9C6q6ZdprrPbBA8c1xnkkeCqARsU7re5RyjgudwG1WbPxR-xS3OWJDZDFwi1WAS0Jbtkqw_ID1LiP8ioVFNYthGcGX16zXnPHx0s0ocnmJ_k6XNG3Tt-WycbaSXIYUY1qyfd_HH2LLB4W1t-Cn_o9zWRHwrUQ2OgRxRk9MBNJPwQ9R8e1WURmRdF_mHNpL9HEtp64jAmrKH99rpGA5QakfXx-eCna2RbZhxG2CCtFWGlOJZEnCsW4NlEOXHrn3_Y_R1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40243c0011.mp4?token=H1vTb6f_NnJVlKNwZLF5RR3vq4wAh7cg23K1AYnz9JUIRHjQRB1tN4FKYpMPubwW4I3pP1TOFFKI7DHze9C6q6ZdprrPbBA8c1xnkkeCqARsU7re5RyjgudwG1WbPxR-xS3OWJDZDFwi1WAS0Jbtkqw_ID1LiP8ioVFNYthGcGX16zXnPHx0s0ocnmJ_k6XNG3Tt-WycbaSXIYUY1qyfd_HH2LLB4W1t-Cn_o9zWRHwrUQ2OgRxRk9MBNJPwQ9R8e1WURmRdF_mHNpL9HEtp64jAmrKH99rpGA5QakfXx-eCna2RbZhxG2CCtFWGlOJZEnCsW4NlEOXHrn3_Y_R1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی مردم لبنان از حمله موشکی ایران به انتقام حملات اسرائیل به بیروت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440559" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
آمریکا بخش کنسولی را در قدس و تل‌آویو تعطیل کرد
🔹
سفارت آمریکا در قدس به تمام کارکنان آمریکایی و خانواده‌هایشان دستور داده است که به‌دلیل وضعیت امنیتی فعلی در محل خود پناه بگیرند.
🔹
سفارت همچنین بخش‌های کنسولی خود در قدس و تل‌آویو را در روز دوشنبه تعطیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440558" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
وزارت خارجه: به‌دلیل نقض مکرر آتش‌بس، چند هدف در شمال اراضی اشغالی مورد ضربه قرار گرفت
🔹
متعاقب نقض‌ مکرر آتش‌بس مورخ ۱۹ فروردین و تکرار اقدامات تجاوزکارانه رژیم صهیونیستی علیه لبنان و جمهوری اسلامی ایران، از جمله از طریق همدستی با ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440557" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
وزارت خارجه: آتش‌بس در لبنان، بخش لاینفک تفاهم آتش‌بس مورخ ۱۹ فروردین ۱۴۰۵ بود و دولت آمریکا مسئولیت مستقیم در قبال نقض‌های آتش‌بس از سوی رژیم صهیونیستی و پیامدهای مترتب بر آن و نیز هر گونه افزایش تنش  در منطقه دارد. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440556" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
وزارت خارجه: عزم ملت ایران برای دفاع قاطع از امنیت و منافع ملی خود در هر نقطه‌ای که تشخیص بدهد، جدی است.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440555" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
وزارت خارجه: عزم ملت ایران برای دفاع قاطع از امنیت و منافع ملی خود در هر نقطه‌ای که تشخیص بدهد، جدی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440554" target="_blank">📅 00:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=Bi8lXruyEu1CzDFstFCcCKt1tfM-Z2uQlVtB4BfVM9FagF48WsDYCciBcfgugVtajRprCgiz99mPNee2Dc7QV6_ORYezsps_ns3XUhtCsEaeiXA_B-CXH5u2eGBTX_WDotSBgxp73AktEv_OFUbR82bMK5uX8bzx33AZdFGYvgLpjMu4EmgxAdvzsf67UlUwI9EVWL1qNUrR4cHv9aUVuivWizpcsiOm5iA2VauO8ZIE88y8GAKrmyzifHDu534UuZrEUBTODT11krrFqxZgxkiSekzO3AXAtwAWMMSOAEutqUkpWkvl7yTqtav8vcXlxwsGnWVLeqyj-o58vyR_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=Bi8lXruyEu1CzDFstFCcCKt1tfM-Z2uQlVtB4BfVM9FagF48WsDYCciBcfgugVtajRprCgiz99mPNee2Dc7QV6_ORYezsps_ns3XUhtCsEaeiXA_B-CXH5u2eGBTX_WDotSBgxp73AktEv_OFUbR82bMK5uX8bzx33AZdFGYvgLpjMu4EmgxAdvzsf67UlUwI9EVWL1qNUrR4cHv9aUVuivWizpcsiOm5iA2VauO8ZIE88y8GAKrmyzifHDu534UuZrEUBTODT11krrFqxZgxkiSekzO3AXAtwAWMMSOAEutqUkpWkvl7yTqtav8vcXlxwsGnWVLeqyj-o58vyR_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نوشته روی یکی از موشک‌های شلیک شده سپاه: ما درحال مبارزه با فاسدان جزیرۀ اپستین هستیم  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440550" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f9735a5a.mp4?token=JuYQt8i1PngsqUxb9XT5JOfCPul-DZKIiy8OIb6bH-UKy6BMBDSLRTEVieJMveUPsngPk1-bLmgulmIqnGoTO3HWzs49br1DwdJNEA7zoQfvrkDhSgAEzmtJJ0ADl1J96V-WQrAoe-q_Bdg1TdzsYgS5PYywgiKrXAU9SFy7upeZ6oF-erefF-WdG62_iaMjOEKiQQ60Z23ocIrRWN09XmleBg0I2X45_oiwutTZ1M-t4bPZig0qcL50L3uiEOlz5dWbXUBELrp1udY_3qQl_Pp1XXKTu0igEVm3hXFCuch7Nm07TqvBgW3WQTqMjV70aEhAaO1_7NcJ8-6iYJ-qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f9735a5a.mp4?token=JuYQt8i1PngsqUxb9XT5JOfCPul-DZKIiy8OIb6bH-UKy6BMBDSLRTEVieJMveUPsngPk1-bLmgulmIqnGoTO3HWzs49br1DwdJNEA7zoQfvrkDhSgAEzmtJJ0ADl1J96V-WQrAoe-q_Bdg1TdzsYgS5PYywgiKrXAU9SFy7upeZ6oF-erefF-WdG62_iaMjOEKiQQ60Z23ocIrRWN09XmleBg0I2X45_oiwutTZ1M-t4bPZig0qcL50L3uiEOlz5dWbXUBELrp1udY_3qQl_Pp1XXKTu0igEVm3hXFCuch7Nm07TqvBgW3WQTqMjV70aEhAaO1_7NcJ8-6iYJ-qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اعلام خبر شلیک موشک‌های ایرانی به سمت سرزمین‌های اشغالی توسط سخنگوی قوۀ‌قضاییه، در جمع مردم تهران در میدان تجریش
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440549" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEI02u3gkK801RpA7uPJvmwkNvpKvYaG1n_FcGx7qK_NOfzbVn4dVKXJ45rF82MsTHFPvGW0_f_wNgjeZu0HS8z9FFuXcBAnh21V8-972JsNSaKzSg6MOhqitW_-ONoT41gyI_swuJIFwTB7I4ENj1CFocuXroU0CHW_y0gaqLl1gIwCSJijMswUiDjB7AxZYoCRxu2A50ERuMLOIczQq3oxDg5_79o-IF622DkrGTLcNYSPd-i9NbsXlMzSqs7NpY5do-af7-b5Zk-woC7BVRb-Fh_hTC0yq8_c6GmSLm6l0PfTR3r9wClVjTtp-cctQTv7Eui9yiCLRO_ssmp1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نمایندۀ رهبر انقلاب در شورای دفاع: صدای خروش ملت ایران را در آسمان تل‌آویو بشنوید
🔹
دریادار احمدیان: این صدای خروشان ملت ایران است که در آسمان تل‌آویو شنیده می شود، ایران و ایرانی زیر بار تحمیل اراده نمی‌رود. مسئولین کشور با اتکای الهی و پشتوانۀ مردم مبعوث، تا پیروزی نهایی ایستاده‌اند. ادامه مسیر فشار و تهدید، پاسخی قاطع‌تر و کوبنده‌تر در پی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440548" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">استاندار کربلا: جسم ساقط شده در صحرای کربلا پهپاد است
🔹
سازمان هواپیمایی عراق سقوط هرگونه هواپیما در کربلای مقدس را تکذیب کرد.
🔹
نصیف جاسم الخطابی، استاندار کربلا نیز اعلام کرد که سقوط هواپیمای مسافربری صحیح نبوده و جسم سرنگون شده یک پهپاد بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440547" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/440546" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حزب‌الله: تجمع سربازان دشمن اسرائیلی در مجاورت قلعۀ تاریخی بوفورت با موشک و توپخانه هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440545" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNwZefe4BiSgvBhrdcCe3LVmDdMXtIhDjbCdCEAETdxp-IlEXJ7nQVO9qr_voIu89MmB6kV_4VsxAn26huR6JVZwhwn7DxrvSHADQgjBp6uU0xjqIo8-TrlsZZ6jWTp3Y_nFHEede-oixXVmGnkhMIwJmRKl8aP196P82RPBBI1dDYGm5Dwx5STDuer7xSjJQUeLuTNxPMSvxBi865SZnC0_P9mP1uG6-y-oJMtIPLmpOotkAkL0mrUT7PEVHFLH2RZWju8GreuObuZw98f9adbeC7KXiPUEJzzCnYLH_pzRjtorsNUOza1zPoNtfeyCLOmNUQGsZWJJfAlo8LWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌های تلفنی عراقچی با وزرای خارجه انگلیس و ترکیه و عاصم منیر
🔹
سید عباس عراقچی وزیر امور خارجه در تماس‌های تلفنی جداگانه با ایوِت کوپر، هاکان فیدان، وزرای امور خارجه انگلیس و ترکیه و فیلد مارشال عاصم منیر فرمانده ارتش پاکستان در خصوص آخرین تحولات منطقه‌ای در پی پاسخ ایران به نقض مکرر آتش‌بس در لبنان توسط رژیم صهیونیستی گفتگو کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440544" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زنده خبرنگار بی
‌
بی
‌
سی از بیروت؛ موشک‌های ایرانی موجب خوشحالی و هیجان لبنانی‌ها شد
🔹
پاسخ ایران خیلی زودتر از انتظارها انجام شد! همزمان، حزب‌الله هم رادارهای اسرائیل را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/440543" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440542">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r01O-UGFyJgddnos49BL7_5PPNM0lc_8fE7kMFw20YnJ4h6eO4JBZwgDYMdgpt8YnmJPRo7yDhhttegEfGZrOkrAShgOCcrQiJDRpA0mtYy8ztX-4qJCRcU0RX-VtLvyHjua-VYRj4xHnHIp0tdnBDYUXbqSFZq8E621fUrW9CsXZqlYOdEPxOUs-pA3frTSRl03KMa3ZFH7pQ_j5dsjPA1lS9_1a0xlUx2mUiqTtsBcEsPszDqqoRZmZpKv-RbAnvstYLZJ8ILdeW7Iw0yQteP0yNAjhKBD59u9IHNbgxSdHeBrpde3ckSrlz8ey-azMUgnawYBOkaAMwvw0UvHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440542" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEhyWtMkPcBZHYHe1wFoNIENa3llM2KkzyJDY5YWuCPuTrhUFWXdPDgTymeNdS1a_DoITJ6onHofK4TEikh_NHyeIB4NLUz_EOUhdNiIsAyXtu5zi2CTumihCleQWTpudnGhbdKy_3wUSGgoUpFHgE5dN3PKjgOHGuBlVMvZDz74jVmIzBZNDAo27hW1xoiP05PzT9Xn_wKIdpArUDxb1sfeYfcBzxmGbl04fBuPMYshQZJ3QtvWdkNTCcF0ii-ugfh20Jy2aKyeQPZxKY4RBD5XYUqFlVKrRew76F08c4Mv4pzP6CwF8aTm1X5PDwKRgdKvTcKwQbIWO8K88_UYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: صهیونیست‌ها در صورت پاسخ به اقدام ایران با ضربات کوبنده روبه‌رو می‌شوند و حملات ویرانگر علیه رژیم و حامیانش آغاز خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/440541" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم انقلابی البرز خواستار مجازات صهیونیست ها شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440540" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440539" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG5V-Gc0zUteRs1oai6N2mqUmm32OYkIBK-oFmrEBRpce0spih4Y3ntCQkGWKoKjkIaqHYU6AXMRJW-QZBT2K-n-YzcpolOpiZY3HybvFL84gqKdnRYEx6AlSGAtF5OhohAJSpQqzX_Y5fhw9Z-juEkEtWKYnUQ8Zj2Oh9UlX7C7ixYmFiaTkMF36qiJEMZbE55KB7k7cda0k6gXUerZjZdLkiW1a8EOUrQ9Iudpagz65mi_XOMwxm1T5fa2MYIPGFHChxDM1hrXBnqH8qpnWnaxaX-gunU1ruYWTFvEChXpDnKoA0rJbmhXhZCC0KP6N3U7cSBRmniWsN3DuZA0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440538" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام جدید فرمانده هوافضای سپاه برای تشکر از ۱۰۰ روز ایستادگی مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/440537" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440536" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم ارومیه به هدف قرارگرفتن رژیم صهیونیستی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/440535" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: سید مجید نقطه‌زن، تل‌آویو رو  شخم بزن  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/440534" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در میدان انقلاب: سید مجید دیو رو بزن، تا صبح تل‌آویو رو بزن  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440533" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFfcpr4pDgFHr9zuo4ySa4srJR_zpS1TeqohPEdA8xVTs-CORqF1Hskr3L0ykh06ST0MfyLZHbmf8aVP-S9MdErRCvf8ibTQwPaXaVIuARBmrmTW9XrSJYxbWaZt0ThHAeM0Cpqnv41_nebNvNKcdxtpD-VSuaGX_WyLRmZYW6f8AggVvcifSqsNrHUGpXAHP2jNcINaWOgm88goetong0CD8wfdZi7jYjr40OPBOFVSdu-S8dnd5rVwm0XCI8Tjg8h7aI6IZibJxlKNv5UIAZAl-sbwON61ylS4uEq3vmhNtnV-mrcVx5kPDxcxTBZLM3eJWwCA2AaXQULxcblZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود
🔹
ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/440532" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440530">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم در میدان انقلاب تهران به شلیک موشک به سمت اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440530" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPuqJ9yM_ZlApAnuyYJ-Qs9h9YiMfbimboCweT3SA063grYRt0bA6_i8sEShSKWbE_xNssncfden7B09xxdc2S7GfDTMjFo58m7-q1cSt-Fr1VdJBYbrAqiSWSl7Qh2hfE39BmcU963jVF0Z6PRQAOyC6z53EMQG3I1-OOkaMChOakp5MxBIjQQOdA1YsV7Dhu_ta8DfzdqJWVdrzzbuJLl-viEsP-YwS4-7L9YlZQ7UgTPgubz0ioPchsujy4BPCGbl06m6NVGsYu-NzCbeFwmwvN-kxyxs-xr9AzP_W7_--afw7UUyVsJCloUXYDzLjD2XvXyOTLw2ZvdepeKQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نفَس رژیم متزلزل صهیونیستی به شماره افتاده است
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/440528" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izY56D3UZVj9-pATj82qwc243kZfYNvfxfsszJphXDWqbj1qCxSvoEMoV2FpiAV3Nnr8rc2padzXswmf3TSFgDme03T3JVjTTceBFDpowQMeUn5TYx2S45NiD_bAz8NsUUa6p0Yf_eNV_Y3Qtyg-TIf3EzhX6GIsjj5nGbp29ao6OGj0s0unQOxE5ocVGqXNLmFXajORQzPYYqt3RqWBR0-yahc_6GZcG3MwgpRd0HTNu4p-U9ZUyE8x5K253LwKRsbngf4ILQ_hoPpBelk0yZnu6eXNCacMLanMVbnUzVWj28u0UOqouuIyrp4Kf7ZrwamtIVvUj_VieXlPIjG13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توصیه‌ام به ایران این است، موشک‌هایتان را شلیک کردید و این کافی است. به میز مذاکره برگردید و توافق کنید.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/440524" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پذیرش آتش‌بس توسط ایران در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود؛ لکن مثل همیشه امریکا و رژیم صهیونی به تعهد خود پایبند نبودند، هم تجاوزات و جنایات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگهٔ…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/440523" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farsna/440522" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: در پاسخ به جنایت گستردهٔ رژیم غاصب صهیونی در جنوب لبنان و کشتار و آواره کردن گستردهٔ مردم مظلوم مناطق صور و نبطیه و سایر نقاط از جمله ضاحیهٔ بیروت پایگاه هوایی رامات دیوید، مبدأ این تجاوزها هدف موشک‌های بالستیک نیروی هوافضای سپاه قرار گرفت.…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/440521" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/440520" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد  @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/440519" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPuQHbOCr0MEq8PIYHbxqin2D_-FU8HQAdf0ABLaNFSNHDcDN2Wt0cgI7zgY1iVoNVqz2uqgcQfyUZOXqFNbU8U02IATClB5oCfDPdTvga36NB_8rQKGUDj4R0-7HHlY8ZVaJubjTeYJb9Y3TAQ9xbo7bWPyuqDpiXgc_VL1Nh4YqaYSx9sk7cmqOcU388IHnc2oI_32CY5nKbg6s9jjgtH1A8OA1ktPRNKCSf7XT1YTqKVdIAu0dDf5HTFjSMYxeuV_stTeqxBK1OQj2LW553M7wTkzReZK7RsJYbrM8i4EwIcoT559OywE4RyAeUy6_PpQpBLX9HnURevjPk5Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ایران بارها اعلام کرده بود که نقض آتش‌بس و تجاوز به لبنان را برنمی‌تابد
🔹
امشب متجاوزان پاسخ خود را دریافت کردند؛ این پاسخ هشداری است تا دست از شرارت بردارند؛ هر اقدام جدید پاسخ کوبنده تر و هزینه‌هایی سنگین‌تر دارد.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/440517" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5kdBbAM0ODt1vlRzmE5Ksyto-3fGDkpYqbfRE-yG39cyQz17d1gArcsW89ZHSJLI0D-K1yM4BwjYMuJ6mPs4F-ubLLo33exZzDSDlEhkEPt7xTC0zwBG3-WjH5NQXehFvGKFi_zUBNaAH3H7WYrgXvZBVEXAWrjejxJYz7DIDswjacKd6s9Zk54DuEdqpAwGXO3BH7aIshTcZep34DcOSoG6ubweHhg8tLTtY7-yrONlCcSefloQdUME2ZNTGIUk8q9KUoFuNXmPN2r9i9IwjKMKvm7uYKRp4U-pVf5tNgIsBWiDflctHtTzdHv7_xR-qFAuAPHGGvmTpeB8MJtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/440516" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTbSFcXXyoiC3ags4zEsRYuLgQl7pj6EYOrop0EMQLNNzI4Te-uWnhmbi3-SEJzIoJpq8T3o3Zp14LxqD95lnpalaSnmQyoH28sBRw-TT_qCB08tWpQAsQFzYTcugwpLuHy988EhWHxD98H4HuDVqc-qanJwNQ6Ne4jhJqYyVYx39o1B-zV3tQvdc3JIgfQESrn-KqKOubFgw_8bgTYmMUwX2Vm1LOfA7SRC-ydP6r7EtVA2im8CbGWeM1J7BQ2bai_MKyKHZ1fzIHOLs5suyHWVeoQvtEkZ4Iew75D3d8oBNllMAMNwGEQ21vpIOAwpvCvTaxzoldymf12ABijscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام فرماندۀ هوافضای سپاه: الوعده وفا!
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440515" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
حملات موشکی حزب‌الله هم آغاز شد
🔹
پس از حملات موشکی ایران به فلسطین اشغالی، حزب الله هم دست به کار شد و شمال اراضی اشغالی را موشک‌باران کرد. @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440514" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم یک‌صدا؛ بزن که خوب میزنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/440513" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدارس اسرائیل فردا تعطیل شد
🔹
شبکه ۱۲ اسرائیل: وزیر آموزش اسرائیل اعلام کرد تمامی مدارس فردا در اسرائیل تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/440512" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی دوباره نواخته شدند  @Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440511" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از
موشک‌های ایرانی بر فراز فلسطین اشغالی
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/440510" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIx9hMPMsAA5olU0esWXKftE1y2fcqPc62VlXAo7S7dqY8Z1GcO4plVl7tysxNzN9EyTmiPGkQt_lZnBB_rAGuw4JnHFU1WNMHfminYaJ9_9T9VhG7EgsrWwWWtyE9Oil_4wYl2yOZGTSAYbQ8mII7F9UQjhmv4CEkgxg0UteLjUvlmPq_qlgBxlsPAJPO2SlpcnFQco-7DhUIHOqMKfivbldoQg0QsoGwf0M4UvGAx8UMCWaTikt0pBD4JN6DjTa0FJhFTQPa57sUhcyAvlVFpUV-qfx4Oz1foKyratHe6BTC77ozbK8cgjTd-E8mMIWSUcZPr3ihkryZbvGKocrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
گروه هکری حنظله با انتشار پیامی، از اجرای یک عملیات سایبری علیه رژیم صهیونیستی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/440509" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه حضرت خاتم‌الانبیا (ص): ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و درصورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران، با ضربات کوبنده‌تر و پشیمان‌کننده‌تری روبرو و حملات ویرانگری علیه رژیم و حامیان آن…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/440508" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2rpAuyprZjs51l5JbSjoAPcrM1GhStwCFOv-L3AmSzysuuBbdEvPAu35oD-ic7Zk2vz6439X26tCCrhI45f-SmppkCJw830GQcIRP7uua-C1Oh2NK58W8RC9nZS8MFmeLqPKw7V4VGKDm_ktuu7Ckehi_2y_hRAvgDae1PznlMNvviMfRu3lNKoAsM3CJxZj1v4nIvpqn6wRxrzJmRsjkKVqroRMfvFo705vp9qKxNeH1oOV9mOBjRqxPUnTBBgTXDkYUA4-w-CSlfNpIAzrhsrdPirwNvun2hA5DrfMhJs-9fg-m7j_oWQo6HMnxvln1A6fd4CkTdVAocsrEyPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440506" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
ارتش رژیم صهیونیستی: موج جدیدی از موشک‌ها به سمت اسرائیل شلیک شده است. @Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/440505" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
منابع عبری از شنیده‌شدن صدای انفجار در «نهاریا» و «طبریا» خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/440504" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
جبهه داخلی رژیم صهیونیستی از شهرک‌نشینان صهیونیست خواست فوراً وارد پناهگاه‌ها شوند. @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440502" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
منابع محلی از شلیک چندین فروند موشک ایرانی به سمت مواضع دشمن متخاصم خبر می‌دهند
🔹
همزمان آژیر خطر در سرزمین‌های اشغالی به صدا درآمده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440501" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf3d2c79e.mp4?token=pAWLPrF7UNpjXtWrbyMAcHBOBexrqXcz0iP97h5_AgW-D1HKKBKJ6G2fEWVj7zFApD5AQ5pGAuiWa-jPeT1pDgVuHD0rsOfqXVUL1n1K-0ehaIt3JSnKpyCNMleTbY1dFkPwnjkZc2KL89OnjYtYnqoXne2Iy6JGI3qJgd8Zhm1xyiZGnY7ty7RqBn8Ow6_SQrldXheHWD3Aiog7fjS2Ik3QKAEpINUCXjL4OITxewFNEJ5JW62a8xV5_IVqwTDc0jwg91lKZ9bZdVyea9flMA39IT94DrAHsvt1vUdq-7gnOKxWNFDxRhhllXZw6GwI1K4SOsJ_Ab3c6L41CGHwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf3d2c79e.mp4?token=pAWLPrF7UNpjXtWrbyMAcHBOBexrqXcz0iP97h5_AgW-D1HKKBKJ6G2fEWVj7zFApD5AQ5pGAuiWa-jPeT1pDgVuHD0rsOfqXVUL1n1K-0ehaIt3JSnKpyCNMleTbY1dFkPwnjkZc2KL89OnjYtYnqoXne2Iy6JGI3qJgd8Zhm1xyiZGnY7ty7RqBn8Ow6_SQrldXheHWD3Aiog7fjS2Ik3QKAEpINUCXjL4OITxewFNEJ5JW62a8xV5_IVqwTDc0jwg91lKZ9bZdVyea9flMA39IT94DrAHsvt1vUdq-7gnOKxWNFDxRhhllXZw6GwI1K4SOsJ_Ab3c6L41CGHwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farsna/440500" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2fuR4stj16rbJtF_IHkGOkPh1YLrbaoFy1CvmBFhrVEuFFXRRDGfOk53RP8FMfq1vP1YefeV1wgoOMPtGbA2qivpWR9ZM8e78Lf97NpLip2KI2TsfnAColVsZDNsFmv0MlaBEyvbvguX3kylrquD0plurj_XdedYK8pI6FQCOybCp1nlJsOZ_cbMNdmb1COw0M0jriJ8iR3SpgV-quxzRqj4hTM0r5df5VA7Px-Yf3jAuG_uTPJkDt_-7k_2g1cwJmi-TQm6OgdmDux0SOXE9EFuAFVmOS35L9H806LN6Ej-Cml4xdkMc9WY8n1t4I6ZRLOG-F78IO9C2xQQEGOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملهٔ موشکی به شمال اراضی اشغالی
🔹
جبهه داخلی اسرائیل اعلام کرد که شلیک موشک‌هایی از ایران به سمت شمال اراضی اشغالی را رصد کرده است. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440499" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
حملهٔ موشکی به شمال اراضی اشغالی
🔹
جبهه داخلی اسرائیل اعلام کرد که شلیک موشک‌هایی از ایران به سمت شمال اراضی اشغالی را رصد کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440498" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آماده‌باش آمریکایی‌ها از بیم حملات ایران
🔹
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از مقام نظامی آمریکا نوشت که نظامیان آمریکایی در خاورمیانه آماده دفاع در برابر حملات احتمالی از سوی ایران هستند.
🔸
پیش از این رژیم صهیونیستی بار دیگر آتش‌بس را نقض نموده و ضاحیه بیروت را بمباران کرد، حملاتی که ۱۳ شهید و زخمی برجای گذاشت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440496" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701c82e151.mp4?token=QQTXYXsaUX3fKkmoO0f3bi9BInDKvfrWOaiS_pFegdsJIMTUZMTJgWa3tjpG2oCJkJLA_fEBfWtWntyZNdOQcu0hbqrLnP-1Kz5ezFq3Y5iQavqP0yTw8RhD8Xl1lsnnpesCOmEvRpxRVZHU9Nx8jjsabIa7mAnHECykMY11J9QCERH9o8ZsTY_XFJD6B0bor45KkwL9QJK-oRe9z0AVGpGcXgg7BtVXsKw2R5HInzVr5_ApgsiXBkoTy2PtdrPNfm2Xw5SJzd4vzAm0hsmWHWcY3vC_FyYn8lFcRcOOmWfBwzwq0Os0AqQX0g_b_rNO2Sp95hyN_lI7ij-ildwQMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701c82e151.mp4?token=QQTXYXsaUX3fKkmoO0f3bi9BInDKvfrWOaiS_pFegdsJIMTUZMTJgWa3tjpG2oCJkJLA_fEBfWtWntyZNdOQcu0hbqrLnP-1Kz5ezFq3Y5iQavqP0yTw8RhD8Xl1lsnnpesCOmEvRpxRVZHU9Nx8jjsabIa7mAnHECykMY11J9QCERH9o8ZsTY_XFJD6B0bor45KkwL9QJK-oRe9z0AVGpGcXgg7BtVXsKw2R5HInzVr5_ApgsiXBkoTy2PtdrPNfm2Xw5SJzd4vzAm0hsmWHWcY3vC_FyYn8lFcRcOOmWfBwzwq0Os0AqQX0g_b_rNO2Sp95hyN_lI7ij-ildwQMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شهادت شهید علیخانی از زبان مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440495" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e9c6e26a.mp4?token=WhDzpyAzHAlSahS_IF6nZZxGbFq2ojFWAVWuUTRjOS0vFzlPC9NiYbjrpLO1umVY5pSLx9WM6L2Ckwz8Op4LqTT5uxAwuTfl4dkSSrURNITsWzayOb3NJV5KUuO_mdPeUOBRirwjB4dI8wUEJqhpB-NiakUYXwYZvOUugVg_iEdC7glguwj5K8xlAeVI0-SYC-XbBApGeEfj38lPQ_eARF0EUxWLeWL4FamxN6jblRNgJdIV7DoS6DWshvCtpY6UQ8_w5I-_VTyHjmRnM7CnQPxjzC81OpK2YxeCI4d7eO9a1LKeks1xRhdFk5mnN1V5hLgJT2I0Dwz7FRUv1JdWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e9c6e26a.mp4?token=WhDzpyAzHAlSahS_IF6nZZxGbFq2ojFWAVWuUTRjOS0vFzlPC9NiYbjrpLO1umVY5pSLx9WM6L2Ckwz8Op4LqTT5uxAwuTfl4dkSSrURNITsWzayOb3NJV5KUuO_mdPeUOBRirwjB4dI8wUEJqhpB-NiakUYXwYZvOUugVg_iEdC7glguwj5K8xlAeVI0-SYC-XbBApGeEfj38lPQ_eARF0EUxWLeWL4FamxN6jblRNgJdIV7DoS6DWshvCtpY6UQ8_w5I-_VTyHjmRnM7CnQPxjzC81OpK2YxeCI4d7eO9a1LKeks1xRhdFk5mnN1V5hLgJT2I0Dwz7FRUv1JdWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباسی‌ها امشب فریاد خلیج فارس خانه ماست سر دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/440494" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">۹ زخمی در تیراندازی در نزدیکی کمپ انگلیس در آمریکا
🔹
نشریه سان: وقوع تیراندازی در فاصلۀ ۴ مایلی کمپ تیم ملی فوتبال انگلیس در آمریکا، ۹ زخمی به جا گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440493" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b67285381.mp4?token=AqS35aCsLK_uF_vntDszn5vQK83ZHaT5RLyq0CFi0-hXq18J8rx7PRkAOIFqNGtfrTx2IxwYgAR9QIN3FGpXmhS_zYTBDFH0JTXw2IPT5m3Q4gpX5F74Gt5Ro6yfYDXg1POZh1dtYNmz2brIIxQkjTe9VPdxmlPOC8HL8TbibFwmOetFkr1WRXyQkvfvN9dQP9dxAlFk6hnJc45ODPxGoPyq_t8lyOx09KJorut8_rVAZzx8qrAyOgB9s2yWhT2Ig__14LPrCBtVoHcsdmujIuDMX9mUiZFandk46sBsUdRVPg5GYEHxDR5h-ehif62-u1rkPjppaMUwwDBdonFK5zxcn-9znEkDMhdGSJ3AYgfWbkLyHzhaRqKSidUsaX82DoYUz6ByM8bP7o9ljytDNAfmAzi3RHgCzDO0UTl6cFIgYWhcTnwgvY_S44P3c4-kYjExj7_l6ziF67Oq-avgQeaAuVMHUswWDxGWM6LaBgVx8f-eYuVV20XaCg4v01NRFwtvwsIZbUALISZtUko1jUlq_okXz_Z2kwbTkNK3SAE5i0G8ppjVLHoLTshGGyo8pLVRsJLMAYCQxZKbdkv-dlATtF4kiywnAzPlp0MP2ARMls0i0D9ltfzUI4_4DL75jmoaYTGa09BocDfkT5GF1L0ywX5g3qxjf7LukqpwnAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b67285381.mp4?token=AqS35aCsLK_uF_vntDszn5vQK83ZHaT5RLyq0CFi0-hXq18J8rx7PRkAOIFqNGtfrTx2IxwYgAR9QIN3FGpXmhS_zYTBDFH0JTXw2IPT5m3Q4gpX5F74Gt5Ro6yfYDXg1POZh1dtYNmz2brIIxQkjTe9VPdxmlPOC8HL8TbibFwmOetFkr1WRXyQkvfvN9dQP9dxAlFk6hnJc45ODPxGoPyq_t8lyOx09KJorut8_rVAZzx8qrAyOgB9s2yWhT2Ig__14LPrCBtVoHcsdmujIuDMX9mUiZFandk46sBsUdRVPg5GYEHxDR5h-ehif62-u1rkPjppaMUwwDBdonFK5zxcn-9znEkDMhdGSJ3AYgfWbkLyHzhaRqKSidUsaX82DoYUz6ByM8bP7o9ljytDNAfmAzi3RHgCzDO0UTl6cFIgYWhcTnwgvY_S44P3c4-kYjExj7_l6ziF67Oq-avgQeaAuVMHUswWDxGWM6LaBgVx8f-eYuVV20XaCg4v01NRFwtvwsIZbUALISZtUko1jUlq_okXz_Z2kwbTkNK3SAE5i0G8ppjVLHoLTshGGyo8pLVRsJLMAYCQxZKbdkv-dlATtF4kiywnAzPlp0MP2ARMls0i0D9ltfzUI4_4DL75jmoaYTGa09BocDfkT5GF1L0ywX5g3qxjf7LukqpwnAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از نودونهمین حضور مردم شیراز در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/440492" target="_blank">📅 22:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuC0SzFypAvbwYInQikTvcsUH96POHQgo4HC2yXEL3ZkpImENGUHbbDjNeXzUZ7vym2T3rson5BANAO-_2br0eUsqlUFHLw4fNTZPLY_dKhoAw__NqQ8ccxt3s9bHS1UXjvlgQQc1xQPkemXP3P-Tjt3_Zp-nkBndnoaFSQaKcvWm7pbjJtBcRfZ_C4PPLCYQCWpiEY3LTy5JkQa6M2z77c1zjFuxNWeNir-SlZzyhYz7YKf2zskJ07eLhLobxBENKVfTYGeqv3_Z_3P8WQCgARMBzKUZleoRvdYkZEmOexBKLeFGhsy7aIJGDE1SWr822n1RPHKsHFjspGF131KsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXta6vXcbIp-A7t3-G01W5QA2tJ-EslRO2L6BSw_zGINzigQaTKy84aVH48urZPlDougOAAQ5blMqTmKHd7O3SZ5JsRaLAVRyYLJpFnXLpqOblxfhmDT0o-TN-gkv8DMbgizgsgOdwFnjPLjNa_ltIaJaN5LBTA3_2fQ3UMJzHK-Mg0U-CgUjEcA-OI9a_JWkQkSfTh-qC4-_fgLJNjl-rbm-C-rpwLMKr4rhGDDYC8CMFewa2juVyIjMSji1goBtd9jUuNlxPvz-x8oDrg8eWvd_fueeBBGmlqOpJWdV7ywjTmBZOKcYff1Vnhq_F38NIb6V3keZoJpFSPAEXu5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYykXEr8TTAjBQ4WyiwCXLMi6KEd3AZU0dfZb_FlQEfTD2TfF8he6YmZViqn7CEvhnTM5Ty97V3KLt8WOCbbMLv8HoWkrhh87aUjF0zhMR6LHqVhFIirSGAtP5JNVMWUYMrqrM18CozOSGgjf6_RM-Ro_ZAmqnqBVeBfWm4VYjiTSvU8E39WkLYRTxMRqNHiUYrMVrZjX6rtPbcgxIxaJvpXLDEJ0h5NyTqZ4Uy5SVTVeFW-VctGjLTi-BZ-jIcQp5KvLY8KCBUtK9bQVUmmxiDFnVt68gG5Bnok_VPjDAeOi2xC60yWFa6VEl5txKm72qstCVT6e1wYviAmVj62Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-duWEy7glz6wCcImHdPawRF-KEQYbXhFCFwucHg-zFs4q9jUFFjCIu19sYW5sYRIaxtsPaD6xSrfiNOoasWgM94qX20tL5D30z0_oz9tFfQWqvPxW9gzpwPMNH83GFF7Dbpp33hZsJ5F4TBwRpkFUhWDCNHSLri9i36IeIH-QnhAxw83Sw9UoSTSbvsEGb8kWXDlXruucSzVwJvMttNUIzQLmIPecCcFpWB8jxJEsC149KoXM0V2xe9ZdcMbhywZDnK6uqW-_QXXOzXDgXce-ASnFitsPnkg5G-rReU7Q63HWONEVymZT1yGRQOdmJ12Vg2WPdOVDsvYjKSBlzokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rU7P2WDpBFka6DOGFiueCqllzRbn5nxuuDTzvYAQ8EijHSxAOD2cQfhRcXkAHPH14Szd9sBVdgrtjHeu3gdaunHJzhPFazOwmJYyrjssyZT-JeAzVXfAEc5yTNAmtTfXmG3OZ3bd4HqSii5n3mzUquzVQ152T5n7QSL1gl5t_hbq_1VwGjoO8IzTAx68BZazwgsH5MaqtrQdkULZc40XS3GeqiB5Upw546D3OGq13to7CXiAOx8KWYXWL4DUVSYPWRp6DITQI2ewZE_-CAUIXZIU3H2qx_H4QR5zDSOumxpTnJDSBn0OLNckQIon3zG6CaBJfPoLQuzJZ21SnPbdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfdR0et1Lcu9En7PjhmNS7nhNffiZcR1nmm1AgbZuhhhGEFcXykeepXPz4uJcizMdFkI40vEEF06drKocvYoP9EA_fWRC_cfOZ2n6FzgIh9DX_28EUikM7_ulXAGQOqh4xs8Br3RvxI3YppSUwZCwGlb2f3XyQt070hNuAguv9q5hZVd3wtVovDkd7P8e9MpFeLkLBxXnKKXF_5URwyUOx_RkyjgFY7euBehW1bO4myvp-ZDFjYt2xyuAkOSm2jMz_tv5u6tdwfAafOzUvpgfXO26CK1dUU_jaCPGS8fV7wwGumkiiV6rh1qUyYO-lSDQikNLRRMDhZ12LX5tKUkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICUK50fj90tT-JFW6McVfwgK9VCisg4vn1J2uLLDovT4kxAZ5_ATmOpAGZehN7LlIGuhluUkmB1BC8ijHMXx8DqVYIaXTPhPipIABhM9OsNQEVR2YRXcCmV17uhdICTRHpoJSp7G6ugxMLwpi5ORcs8V0hzd-ImRexDy-V5jXiCrWzJYoAHhX_w5NpHVTEKgVNeR8RnNmxTEYl-a5B7MsStjUvhK7dhQHMauTdYj_A8q2ahOHLIXpBMBFzCDyVCEZHyro7-E6EfNlQxcEO3kNoNJ8nBW3FK0YdKHHyDtKkO-wRxEI7_JhLV1YFJSbZxN9hZCpBWoFB8NU5mhv0IJ0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست‌سازه‌های فلزی هنرمند همدانی
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440485" target="_blank">📅 21:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0Uze2VdHTYl4Qs8kWjjKJH1Xbx8XqA_D6kIzwUJhG7UP7zg2thWkl-ycLLLAlwqVs40CxXtPx1vPtmmx3yr5mY-S5YQkXzKhpCl2bC4ChdfsC3R2NvY0GCEJ-jQrgBJFR-td8ZtzR-AS72-Al5wXV5ARrF9jn9g2hTADvmiccxYw9ZOJ-ER7bNyIDkXE9rZ6XO4IawunwTBQIlCZfKUb2RTI2Zm3_5cy1MeDNaRD2ZR2StVSCdv9pVMLoZp-_wxpjVBj-QoDVZnc0rCshczd7HptLnDLmMkUSOz7lO8YahRibhHgJB63UOMVbxdLlA7N4oEE5RMx7Eye_SzcG2z3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be159b4b4c.mp4?token=Fm6NN9CcQ3PJBoRXIqResJ5k9Rxay4uyI_Q5u1zp5lzg5ccZObyAbT48FCsrXUxWfTLnAshvG1Emz2mvioPbkKyf_rXbStBd7eENPs6Nlrm3xeXR9ExBaq40e6jhaV6r_f8Oqtw7yIwJZvIv0EqHn22kDEIajqGt70U6eU07XJYQvgME1hYZAwTsP2aqAZxR6tiEUTQsMbbBw3EBH5I4CxKyCs-WHUv60gMEgYkLvMYilKgDkJoSy5FymJefJo-McG1k9D5atbsL95rQJ1J7OcqpCUSgsiCpEW6UlwrypSTiDGmqxEwRSrVnvhQzCZtayuVd3HDrwFXMWtrxWj8VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be159b4b4c.mp4?token=Fm6NN9CcQ3PJBoRXIqResJ5k9Rxay4uyI_Q5u1zp5lzg5ccZObyAbT48FCsrXUxWfTLnAshvG1Emz2mvioPbkKyf_rXbStBd7eENPs6Nlrm3xeXR9ExBaq40e6jhaV6r_f8Oqtw7yIwJZvIv0EqHn22kDEIajqGt70U6eU07XJYQvgME1hYZAwTsP2aqAZxR6tiEUTQsMbbBw3EBH5I4CxKyCs-WHUv60gMEgYkLvMYilKgDkJoSy5FymJefJo-McG1k9D5atbsL95rQJ1J7OcqpCUSgsiCpEW6UlwrypSTiDGmqxEwRSrVnvhQzCZtayuVd3HDrwFXMWtrxWj8VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک به دنیای فوتبال
اریکسن باز هم دچار حمله قلبی شد
💔
در دیدار تدارکاتی، دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شد.
✔️
گفتنی است که فدراسیون فوتبال دانمارک اعلام کرد کریستین اریکسن هوشیار است و حال وی نیز خوب است.
📌
اریکسن پیش از این در یورو ۲۰۲۰ هم دچار حمله قلبی شده بود.
@Sportfars</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440483" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5d171bf5.mp4?token=D3imaNgqXvMG-EIojXy6i2QN7Cx9u9l_AbXiPiNjrYxZVApCzOuWpLwzgHPg3tEU0uucnqc3zfw5tw92LTg3yrSygrkn8gqIjQT1QJA00EGbP0MYiPuzsj_XLFh9Q9-4wyaxx2dos9uZBJO9Rh4Sqx639Ui9FQOhwa1IQNq1C8usE1QrZHY3hd40-YmVfWbBxdATklF7yQ4dZxyMblJ4nD--RPhRLR1-8BquOdOIDbxWdXgod65IUQ36bZdlF4hWZLADeZzCaDSysdQnohcSLs2X-FMk8_MNLCy4hWPwlPjNWP2sTsiKSH653dN2FKvJBb28hSgXguXxdLor5YPX2YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5d171bf5.mp4?token=D3imaNgqXvMG-EIojXy6i2QN7Cx9u9l_AbXiPiNjrYxZVApCzOuWpLwzgHPg3tEU0uucnqc3zfw5tw92LTg3yrSygrkn8gqIjQT1QJA00EGbP0MYiPuzsj_XLFh9Q9-4wyaxx2dos9uZBJO9Rh4Sqx639Ui9FQOhwa1IQNq1C8usE1QrZHY3hd40-YmVfWbBxdATklF7yQ4dZxyMblJ4nD--RPhRLR1-8BquOdOIDbxWdXgod65IUQ36bZdlF4hWZLADeZzCaDSysdQnohcSLs2X-FMk8_MNLCy4hWPwlPjNWP2sTsiKSH653dN2FKvJBb28hSgXguXxdLor5YPX2YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۹۹ شب‌های اقتدار در شهرستان بسطام سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440482" target="_blank">📅 21:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48e558a2a.mp4?token=VQip9jhhL6MQVhMRCHmtQIL6TZayTIb7RQ-Kl-h5harJ_3irmL7gKwVZVKj0dQlZd9HF7slJf9kEX0DigBI4zeyximK5i3VKHL6oStSIEVuB7G07H0o7pIxN8MXoy6M3jjlENA319mwKhzJDEefNJf8_m09AcMcwjbIwQYIIaHMJipc1HiqC7SFmO6qizlJKCDO_HsHVSKxewRGeXWVEOEg_J-bVQ0fHTsTop7AqXaAgY6G-sr4zwr6WgV9Hiw3R5cjKdpm38WQp684cWfRWvLgEu3iYzIUdgkWnJWhftS8LeCCI8qfWtCug2M6SGjpxqfeS1xcFD9wdn5BwREH33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48e558a2a.mp4?token=VQip9jhhL6MQVhMRCHmtQIL6TZayTIb7RQ-Kl-h5harJ_3irmL7gKwVZVKj0dQlZd9HF7slJf9kEX0DigBI4zeyximK5i3VKHL6oStSIEVuB7G07H0o7pIxN8MXoy6M3jjlENA319mwKhzJDEefNJf8_m09AcMcwjbIwQYIIaHMJipc1HiqC7SFmO6qizlJKCDO_HsHVSKxewRGeXWVEOEg_J-bVQ0fHTsTop7AqXaAgY6G-sr4zwr6WgV9Hiw3R5cjKdpm38WQp684cWfRWvLgEu3iYzIUdgkWnJWhftS8LeCCI8qfWtCug2M6SGjpxqfeS1xcFD9wdn5BwREH33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور گرگانی‌ها در موج ۹۹ همدلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440481" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
حزب‌الله: دستگاه اخلالگر ضدپهپاد ارتش اسرائیل با پهپاد انتحاری در اطراف قلعۀ تاریخی الشقیف هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440480" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f993d294.mp4?token=ko3u8Vf1oGzoukK7Kj6lotpXYRt8gSNwIocdqMalEaPeXyE3G4yAkSdgfqZLSxi1R_l8TMel7sH5hMrBQW8FxzN6lfDyS4QZBd_aSYL4mTB8d8RiqzqtGkOUMblm314A3BqVgZvB8lPj4y6IbGLTlTB8Dk7lyjSkYBLIYJlbtRdeegmCNHrMHBZomzsGaYqO-LxJv8m03ieoVx3F6P91_1xJI_JU7Qzb4W4SugkMcMgz1MdFE8OxXZQO5iW_6CBX2aHuJ3BdGZNb86eAst25fKJpBO6C25iJgqyRQteQW2MKed8v_dJjRLaJwfE1nMgudgfqglevKtPpdKUygOSVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f993d294.mp4?token=ko3u8Vf1oGzoukK7Kj6lotpXYRt8gSNwIocdqMalEaPeXyE3G4yAkSdgfqZLSxi1R_l8TMel7sH5hMrBQW8FxzN6lfDyS4QZBd_aSYL4mTB8d8RiqzqtGkOUMblm314A3BqVgZvB8lPj4y6IbGLTlTB8Dk7lyjSkYBLIYJlbtRdeegmCNHrMHBZomzsGaYqO-LxJv8m03ieoVx3F6P91_1xJI_JU7Qzb4W4SugkMcMgz1MdFE8OxXZQO5iW_6CBX2aHuJ3BdGZNb86eAst25fKJpBO6C25iJgqyRQteQW2MKed8v_dJjRLaJwfE1nMgudgfqglevKtPpdKUygOSVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش سنگین تگرگ در شهرستان اهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440479" target="_blank">📅 21:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
معاون وزیر خارجه: دولت‌های منطقه که قلمرو و امکانات خود را در خدمت تجاوز علیه ایران قرار داده‌اند، باید خسارات وارده به ایران را به‌طور کامل جبران کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440478" target="_blank">📅 21:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
معاون بین‌الملل وزیر خارجه: ایران متجاوزان را رها نخواهد کرد و خسارات جنگ را مطالبه و دریافت خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440477" target="_blank">📅 21:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
معاون بین‌الملل وزیر خارجه: ایران متجاوزان را رها نخواهد کرد و خسارات جنگ را مطالبه و دریافت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440476" target="_blank">📅 21:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZB8lGX9mPPe4wtZi20RfqUM3H2d1bLZp-FtXBmBUsLhZrRXh4ACEzX1DUU7gssCn1_E5rki9qgE1hcNG8WvS01MutD6GKr80vIxy5S6IsUqgmbn8d0EswmuPNYk8R_inMyr-BcrDoYrbsfXlSbAJ7r8XuRSY7f8Op_EKbFgTDuVgBtHHeolqlXN0pU-KtpQbwXC0UiQuvbHHNiP19w7bIpNSNU1tiSTWtedZdlrF_3o4w1zob5_2-GdOvsOFFoLPzIhyb4sjGH9iuwKhgEUsy4lx8WXhchUQIHv8qcxIMTP-48Ajk8pPWwVebeStpShjq7xL2LWNOSjHbinfRNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440475" target="_blank">📅 21:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHpU2ulWDpHk2_adpcy940eCPri2mBmsyXPCCrpPpDyBwUwQYkM3pgPWtK8kunR6VBrP0-nqF76F1K4LbRsUWmlr-M5FqEpwKHrh3yhXRAvT3N_MHrEfnbuXanzjmGTJxoclHGNQkeaLH8HOHjynbweYEKMzhYk1s6ank5uV-eOW342tsB21rx1bArgHiKqeF51QXn-oS3HoCecy8473ZSM8phsb9fFK92hN_z-B0NQzq4TSZWbh9g_20mHqU77ideHCxGX4k0azlZTA5j-enhjL5aCp5sKzpOVM9Ms690WUUxOCbUKQeLbi3I0p6uBNRhllYA9W0Om6QUM9eJbM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر لالیگایی سومین خروجی استقلال
🔹
آنتونیو آدان که در ابتدای فصل در انتقالی پرسروصدا با قراردادی یک ساله به استقلال پیوست، به احتمال زیاد در فصل آینده پیراهن آبی‌‌ها را به تن نخواهد کرد.
🔹
مدیران استقلال باتوجه به عملکرد و شرایط سنی دروازه‌بان اسپانیایی، تمایلی به تمدید قرارداد او ندارند؛ البته باشگاه استقلال هنوز بخشی از مطالبات گلر اسبق رئال مادرید را پرداخت نکرده است.
🔹
آدان در مجموع ۱۹ بازی با پيراهن استقلال انجام داد و آمار ۶ کلین‌شیت و ۲۲ گل خورده را به ثبت رساند.
عکس: علی شمشیرگر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440474" target="_blank">📅 21:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454ea6fc43.mp4?token=hoqaLwfW4xhwR8lpAV_5ncn0R2D_Po3I7rcJkPM2ydvyoH8Yj9pxMbaQy9ugRRakP3x4PFaApqgGOAgt18HzJMBQCECLzLfLvNr2_RxyPcc6M7qiKKVQ1sRVbx2AfZXPNC0LNtvI6WjlVWXiZGwunT8j5ugSnE6S7_o88uVXGASeBXXlZXhbJvqIL_9EyoFAF4IiTTHHDSsFnWzezYvTQdF0kdQZPdaXZah4w611fXq_G5Ifh3IUyHk0lAyKRIS5YWaBKMNlj-vjQMPUcfWfkNrve9jZohObaDDwdxvk5gXF10DN70ZghumJ3gPXc9CoQ4u3qzzIkKEeiUj5Ysa65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454ea6fc43.mp4?token=hoqaLwfW4xhwR8lpAV_5ncn0R2D_Po3I7rcJkPM2ydvyoH8Yj9pxMbaQy9ugRRakP3x4PFaApqgGOAgt18HzJMBQCECLzLfLvNr2_RxyPcc6M7qiKKVQ1sRVbx2AfZXPNC0LNtvI6WjlVWXiZGwunT8j5ugSnE6S7_o88uVXGASeBXXlZXhbJvqIL_9EyoFAF4IiTTHHDSsFnWzezYvTQdF0kdQZPdaXZah4w611fXq_G5Ifh3IUyHk0lAyKRIS5YWaBKMNlj-vjQMPUcfWfkNrve9jZohObaDDwdxvk5gXF10DN70ZghumJ3gPXc9CoQ4u3qzzIkKEeiUj5Ysa65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دولت با تمام وجود تلاش می‌کند و مدیران شبانه‌روزی سرکا
ر
ند
🔹
وقتی تا اینجا رسیدیم معنی‌اش این است که دولت توانسته مدیریت کند و مردم به آن شکل جنگ را احساس نکردند.
🔹
کشورهای منطقه، اروپا و آمریکا و آسیا همه به‌خاطر جنگ تورم و گرانی و مشکل پیداکردند، مگر می‌شود ما تورم و مشکل نداشته باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440466" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153f1c205f.mp4?token=kQxeOd9-fjFMiKKtC-Z-59n0tyw_wUjbE-F1umA1iMoAN6ydQoHpsGcONPfe1_f39p50s9tdex7stIUBlK4jSKZMUsz3FAxJWzuxfajCtSlHvSFUlziQ1mgGFt6ZP2oEVU-YqnAvq8iUrunOO3NHA8XynC_-zwl50mcq-pRRE9jNqh5-JLLgdXpAgHvM5Rh0N0GTiRS7eUChx4DBBBFYcmk0xBF4myb30AFEXLZZzEwGdE-WMVcZfL6haAtKykbnNsi8dCC2sKvmo_jDp3mtcle7w7yg1xC-diCJIsxfJggD0VFEauhG9-f7-I4bch0sE7O0aQZgRvl6lxJ39xMZg6IVi4GIJPHw4-RJggvN2p3zQjn1npQcZFbElVK2SNilea1HhSxYUb2cJTfOJG8K0Vs4M16gPVhZp-RPfSz5PfMkaQcwndqCiWFB4st9KYC5MV-nWat4HZpN9akJ_lXk0MphBR4fwojCnsfIiiIjvTYWDfHeW5DBzTAtM4_8v4nwb5C2odpO9X3QHNfEvV-EZ1jvi_rZgCbKqUqgPpqQxkWi90nNY8VMwGST6N8SVx7gZNQ2oxW7i9cp08_jSYhAFJ7n9r-vbCHjEF462xl4KVAyWfKPuQmzNfCsEgivrAzLw_AsK7JGjadxYmynRh19b7IEtLaoidTpAqr8WmAbu6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153f1c205f.mp4?token=kQxeOd9-fjFMiKKtC-Z-59n0tyw_wUjbE-F1umA1iMoAN6ydQoHpsGcONPfe1_f39p50s9tdex7stIUBlK4jSKZMUsz3FAxJWzuxfajCtSlHvSFUlziQ1mgGFt6ZP2oEVU-YqnAvq8iUrunOO3NHA8XynC_-zwl50mcq-pRRE9jNqh5-JLLgdXpAgHvM5Rh0N0GTiRS7eUChx4DBBBFYcmk0xBF4myb30AFEXLZZzEwGdE-WMVcZfL6haAtKykbnNsi8dCC2sKvmo_jDp3mtcle7w7yg1xC-diCJIsxfJggD0VFEauhG9-f7-I4bch0sE7O0aQZgRvl6lxJ39xMZg6IVi4GIJPHw4-RJggvN2p3zQjn1npQcZFbElVK2SNilea1HhSxYUb2cJTfOJG8K0Vs4M16gPVhZp-RPfSz5PfMkaQcwndqCiWFB4st9KYC5MV-nWat4HZpN9akJ_lXk0MphBR4fwojCnsfIiiIjvTYWDfHeW5DBzTAtM4_8v4nwb5C2odpO9X3QHNfEvV-EZ1jvi_rZgCbKqUqgPpqQxkWi90nNY8VMwGST6N8SVx7gZNQ2oxW7i9cp08_jSYhAFJ7n9r-vbCHjEF462xl4KVAyWfKPuQmzNfCsEgivrAzLw_AsK7JGjadxYmynRh19b7IEtLaoidTpAqr8WmAbu6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ تهدیدی این مردم را متوقف نکرد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440465" target="_blank">📅 21:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bb62d0a8.mp4?token=bOmpDe6sS2_2c2CU-ULv7m6ttPYL32UeFLEqsloBfxM910IHKjO5xFfYUg18acr8rkkgVE7FlksEL_Hr5TowoPsPbBhB687xojl7dLjnfGu2QmRd3tVsMXJDhyqurx_FJ5xTPQAtgxC8xJX-7RW9OwhnX_Yt_M9bPgzHGQ62CHetzubH8f0j4XX-xSKim5JeWbVZLj6VGSqOP0qKYJVyinwYKH7iP4PN1srdMphdZ1JBY6oQuPxB9JHAAEUDAoytUqpeltMROnrZtOP3MgrFWTq0eMnBS6oE5DLraw2luOLu7fbUSEL4Cf8Oa-oh5XCilWXPl7jMxuL8gKKQkaYBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bb62d0a8.mp4?token=bOmpDe6sS2_2c2CU-ULv7m6ttPYL32UeFLEqsloBfxM910IHKjO5xFfYUg18acr8rkkgVE7FlksEL_Hr5TowoPsPbBhB687xojl7dLjnfGu2QmRd3tVsMXJDhyqurx_FJ5xTPQAtgxC8xJX-7RW9OwhnX_Yt_M9bPgzHGQ62CHetzubH8f0j4XX-xSKim5JeWbVZLj6VGSqOP0qKYJVyinwYKH7iP4PN1srdMphdZ1JBY6oQuPxB9JHAAEUDAoytUqpeltMROnrZtOP3MgrFWTq0eMnBS6oE5DLraw2luOLu7fbUSEL4Cf8Oa-oh5XCilWXPl7jMxuL8gKKQkaYBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشت و مرغ کیلویی چند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440464" target="_blank">📅 21:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb13583a9c.mp4?token=RAKn3QwKgIgW6rpBMAu48jQq-KB88gR9oJilWUsbjvL2UhFYxKeuACSOkRuwCK1MrGY7oWTI4FqopwmxcZvLflZ53TTGsxt0j3EDIFMpWf8ZcanACCAVZfgVYq6D0tkj9-XqVPC7d29KmTorEOc0ChUNNZz2rTQ-2b7jF5nTGYE15yjpPQsfHxN5PkgoQG_VBdqNMTVi8iEWp66wFemrlT2ghKV6fm8uj1z478nWFLtzLsgy-__imVYjv2dedKuOXHD5zsBmf5-dKhTj4ft-Tszh1FuoSPysyupZZTGoQEj9y6QxIlLa84QGwtwHxsAvbJK8TxfC8rK9CI27eDW7SU2p7l9np6WRJEfkxGJAs3UZRgSs3GnRNzGWqIlARkKlmPxz0aG_Mi9bCwKj5Slse3FTZd-EO9R7HhuRM114VcaH0Gg8cSjrrfuIoelzlYdemPhoXUFrSwSkVIVh90-nAUK-qg8so4Rr78i5_C5tz00lUYr5xXauW1hvFRbiqIaEuDXpOBEGrMjt7cHt2CF39ag2T8bAb5AdW6WOILrON6Z8y5ItFElKwPGlHjBGWIyb66h2fShFTWiM9IM5M_HjMfXUSn6RjScp93HjmVuOzxk9TDJCEu0SKVmxEm1zhexswWSCTRX9tgJOiYWwh_RaY0WAQhodxPqa-NC-VPVCEqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb13583a9c.mp4?token=RAKn3QwKgIgW6rpBMAu48jQq-KB88gR9oJilWUsbjvL2UhFYxKeuACSOkRuwCK1MrGY7oWTI4FqopwmxcZvLflZ53TTGsxt0j3EDIFMpWf8ZcanACCAVZfgVYq6D0tkj9-XqVPC7d29KmTorEOc0ChUNNZz2rTQ-2b7jF5nTGYE15yjpPQsfHxN5PkgoQG_VBdqNMTVi8iEWp66wFemrlT2ghKV6fm8uj1z478nWFLtzLsgy-__imVYjv2dedKuOXHD5zsBmf5-dKhTj4ft-Tszh1FuoSPysyupZZTGoQEj9y6QxIlLa84QGwtwHxsAvbJK8TxfC8rK9CI27eDW7SU2p7l9np6WRJEfkxGJAs3UZRgSs3GnRNzGWqIlARkKlmPxz0aG_Mi9bCwKj5Slse3FTZd-EO9R7HhuRM114VcaH0Gg8cSjrrfuIoelzlYdemPhoXUFrSwSkVIVh90-nAUK-qg8so4Rr78i5_C5tz00lUYr5xXauW1hvFRbiqIaEuDXpOBEGrMjt7cHt2CF39ag2T8bAb5AdW6WOILrON6Z8y5ItFElKwPGlHjBGWIyb66h2fShFTWiM9IM5M_HjMfXUSn6RjScp93HjmVuOzxk9TDJCEu0SKVmxEm1zhexswWSCTRX9tgJOiYWwh_RaY0WAQhodxPqa-NC-VPVCEqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان کاشان و آران‎وبیدگل را درنوردید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440463" target="_blank">📅 21:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CczRFu3sBSDeBYKb745op2h4AsmhwwQfv4mdSpX9L6PjwPaFJkxE2fXcP-dpvXzUyIMifJ7x306Snm5tjKg3pmZOEiOtvOtDAnoRzpi-_HRWYb3hVzXo8kJcTtHtI0MVPsVXbe8GBd5b9daYJ9PWxkD6PLzHMGv1IMOcUXcaQSfa-MyQfHxVMuC-u946ZCtJmNMDJOME4UzyccD89k3Lh-qiFMDgRIB-vCPoOoc3NZ_p58yIxMWrrT23P07KYMdr7NtwiZF98STgBuUS5wABzBUtFgEXvMBWZQddLJlEtiza_-9bEhN28PtP2oGqtNE-XRSS5hIAGUlYZ-4WTiRi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله وزیر جنگ اسرائیل به ترکیه: اسرائیل درحال فروپاشی نیست
🔹
کاتز، وزیر جنگ رژیم صهیونیستی در پیامی خطاب به وزیر کشور ترکیه نوشت: به وزیر کشور ترکیه که آرزوی اداره کردن اورشلیم را دارد می‌گویم اینجا قسطنطنیه(استانبول) نیست.
🔹
اسرائیل هم یک امپراتوری در حال فروپاشی مانند امپراتوری صلیبیون نیست.
🔹
شما و آن «امپراتوری عثمانی» که اردوغان آرزویش را دارد، مدت‌هاست که ازبین رفته‌اید و هرگز باز نخواهید گشت.
🔹
شما دارید تلاش می‌کنید ترکیه را به یک دوران تاریک و عقب‌مانده برگردانید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/440462" target="_blank">📅 21:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ctbhFC1fTChf5G9XrRTMUFTsD3nd9dI9taUbGEXOoxUKzrE-DzBgaSpnsM0wjQ90md76_e-5EN5tkNz7ZqLWoG5DK3BIn9vmWynHX7QLm2ye3kCGPcJG099GomOPiVNWwg1xP4U6iFA9QahOC36JZEG83k4SShzrQAyo4v-JeP7w1vW4jMuLtDHg2nFYVFE4sQSlPQrGXZ6yGW6s_Xl7iYYDhgoNI0a2aRtUpkY9ABQs9FpkVqaRzCbXMxWB23TIZ9ckleshy1jpZ4jD3oCHJKT6BDw9oYPggS4iqLHB4Ids5uKxQXgAv2Cg5PChZLL2gsYa5Og52IyH7lSyjGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیباکلام ۳ ماه از انجام فعالیت رسانه‌ای منع شد
🔹
قوه‌قضائیه: هفتهٔ گذشته درپی مصاحبه صادق زیباکلام با یک خبرگزاری، دادستانی تهران علیه نامبرده و رسانهٔ منتشرکننده اظهارات او اعلام جرم کرد.
🔹
پس از تشکیل پروندهٔ قضایی برای نامبردگان، متهمان به مرجع قضایی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440460" target="_blank">📅 20:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx8YX2vPB-Q3ws0KZDXJuhE4drMfBwVAH8ijRKP5o49Y5xUByjk-z5hpdHCp5mPAUKUmi6fYU8ezXqsYL2SHU658_sDgpn9wTcMXlEf901VibfFgjaF7lwOfxo1c1NuVAo5ci3wsBWX3Zz7js2ecMbXJY2N7w6uqoad53hhWC1QBRNc_1d4RF1Xx4c8K1F4WCPm7CSgqqJGxZ0MIEnQu052Xfr68tntA7E_mteTLkcRn8vLRVRn6k8Q1Z9rBsJRpRCIMGOQ1gZvR2iewrzOBpZ4cnQJx1YyId9OvZuAEld2_RPBfY9O9-szvpLERN_HHvKAwl5eZrS54VNNux9P2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماینرها ۲۰۰۰ مگاوات برق کشور را می‌بلعند
🔹
معاون برق و انرژی وزیر نیرو: هر ماینر معادل برق ۱۲ مشترک خانگی مصرف می‌کند و حدود ۲۰۰۰ مگاوات برق توسط دستگاه‌های غیرمجاز استخراج رمز ارز مصرف می‌شود.
🔹
کسانی که دستگاههای غیر مجاز رمز ارز را اعلام کنند، به ازای هر دستگاه ۳ میلیون تومان و برای ده ماینر ۳۰ میلیون تومان جایزه می‌گیرند.
عکس: وحید بیات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440459" target="_blank">📅 20:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_TudCqq3VcjaPPgeV_9RqQFvwW5ugRLSBLQpgPbRGTa8PxhC1I6T3TMfXXU4K5WyDJmRf5ROJM47R7v-MP3UOmmlWEQWeNiTidNPgs0Xy26SxY0JOw_phfLWApl0VoXfzWjKrh4gQs6L9ICvSnbIxdnzRsojmiyaYY7M_zYvFQ20lay0PeGsy_RbDOiWhSkieqQUkD8RPDZviVLJZEudxfoeXATg9y7OqfnJo04NDMJ13dMqS00vApwyY2VT-6shorNXfjiR-NKqp3w7JPEl9A7ql1KkhIv1oRuHgJsOXIxz6KeWPQNTTzzuE-d5E5Nt6ASzT9q-j9rygw16HnZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسروپناه: تغییر در مصوبهٔ کنکور خلاف عدالت است
🔹
دبیر شورایعالی انقلاب فرهنگی: آنچه باعث نگرانی دانش‌آموزان شده، احتمال تغییر قوانین است؛ در حالی که تصمیم فعلی بر پایهٔ پیشنهاد وزارت آموزش و پرورش و با هدف مدیریت شرایط اتخاذ شده است.
🔹
اگر قرار باشد تصمیمات…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440458" target="_blank">📅 20:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f750c48735.mp4?token=JWErlZn6Zyv7ToiKxMWDilIukF2KiDZ7gV9CHMyIHq0sI3N2Jj6XCI8y9Nd_qOIlfkLmAkrMVts8mjB1CfKan_j_CFWAa0YzbzOOnFjTStZDdXRL9SmgvwshhhP5P2nF-KHfABO_Gm54aVdFcL___Nggo73yn0OoGkvXFKI7GQPei8Ptn3tIaGGGmDaUJjazB5FebaN5hGuUIpt1TA5KAlOkQe_ZXLRCys9DrbttEK7RbGVJxpbkkaucMwH0WWpl5_XiKU7IR6vcMYFfjhXD9hCjFzIPWY4zXa_5OLenZyvCVJGqT2T_NKsnFN_iCx98v2Wdwv9oGYnzoaS5KuLQ44bE-Ufb7z8Q2pMhECj3LHeyRhdEXyDVX2YYXbsx-4z5WwE4dPy3eTcnOqGPCKSSzBZOVpuHPQfHmIl7yHuF06FiwSNCX6u63ylVVw0y3BD-biAldlVrGRhKi7UDqBvdRK7pLkh1_2zeXIsRMz_urybKnZaBcuunbWU_E1jHclhARGT5rfWrZN5zheaxZ-kw--m5RZh0gVVIb9g3QhmhKmGp3Wpst7YByLQPsycrqjvWVjkXknFZtOiyu4RwPxNJWWq1p15DlfXVwsbAysNn7nG-5_JWi0Y_Y-D8P5qsr4aijqHRBP28RJJ9K0AAZ0kEtf0fAEWW3_joqWTRh3kXWH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f750c48735.mp4?token=JWErlZn6Zyv7ToiKxMWDilIukF2KiDZ7gV9CHMyIHq0sI3N2Jj6XCI8y9Nd_qOIlfkLmAkrMVts8mjB1CfKan_j_CFWAa0YzbzOOnFjTStZDdXRL9SmgvwshhhP5P2nF-KHfABO_Gm54aVdFcL___Nggo73yn0OoGkvXFKI7GQPei8Ptn3tIaGGGmDaUJjazB5FebaN5hGuUIpt1TA5KAlOkQe_ZXLRCys9DrbttEK7RbGVJxpbkkaucMwH0WWpl5_XiKU7IR6vcMYFfjhXD9hCjFzIPWY4zXa_5OLenZyvCVJGqT2T_NKsnFN_iCx98v2Wdwv9oGYnzoaS5KuLQ44bE-Ufb7z8Q2pMhECj3LHeyRhdEXyDVX2YYXbsx-4z5WwE4dPy3eTcnOqGPCKSSzBZOVpuHPQfHmIl7yHuF06FiwSNCX6u63ylVVw0y3BD-biAldlVrGRhKi7UDqBvdRK7pLkh1_2zeXIsRMz_urybKnZaBcuunbWU_E1jHclhARGT5rfWrZN5zheaxZ-kw--m5RZh0gVVIb9g3QhmhKmGp3Wpst7YByLQPsycrqjvWVjkXknFZtOiyu4RwPxNJWWq1p15DlfXVwsbAysNn7nG-5_JWi0Y_Y-D8P5qsr4aijqHRBP28RJJ9K0AAZ0kEtf0fAEWW3_joqWTRh3kXWH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: طبق متن موجود در تفاهم، فقط تحریم‌های کنونی برداشته می‌شود اما آمریکا تعهدی نداده که دوباره تحریم‌ها را برنگرداند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440457" target="_blank">📅 20:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub0JMH5zTIwFPYztqL0kCmi3dhLGakUBWQYPrYkqV--Dg3HjadqT7W4wg2OZoj46uH6wK1QC7o1Dxen8Zvzk3CkLUnD6S6F0ATlZudYL1-spy32_GVTJnrT0jM4Whm5CNEOygKzQBOXyMLg6vxJ2g7ppxv33-ne8q_x8Sy3x15AEs3II7Q3lbCa6raM-fVe-eqATeSzv4Q7kM7JqqhU-LVL84f8UrAU98Vaohb7FkLmZHHWvTTWCpyUvlJwqQ3Z0JwFwb2p9gGr7Q8_FiCfOv9tJyVUuI_fianV4vql8Hb_9B7eN5mTjnFwXV6uwO11VIqwdUmdd5VrsIQZUkUVkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت مسئول امنیت یک شهرک صهیونیست‌نشین
🔹
در عملیات تیراندازی ظهر امروز در شمال کرانه باختری، مسئول امنیتی شهرک صهیونیست‌نشین «تسور ناتان» به هلاکت رسید و چند صهیونیست دیگر زخمی شدند.
🔹
براساس گزارش‌ها، دست‌کم ۷ نفر دیگر از جمله رئیس پلیس شهرک «تسور ناتان» زخمی شده‌اند که حال برخی از آن‌ها وخیم گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440456" target="_blank">📅 20:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb3c4a972.mp4?token=Fe7OjmSnGu4EMrtWiiwUhklCzo0AD6TJUCynLy5YKfbBRBvxOrQJoW7M-M-rHNy4oukzWLOAYIHSjy6sDo2DKCBDvuvJ3Zh--Wb4lHuS_ZdmNUaqPfw0IaG7csy2zpE7hg7_gsfno-h2aHnJsu1EJVyD3i6H7IZqN9FMMZwxyBXWH6IwSSVmHM6xXiU4_tAYgReOa1lIP4drVv4V1ilcE-opTauRwWaFThLsIu0mVVTMiu2saz01f6294x3cghYol2DsOBv6bcoRTvy0cj7JS5-oxm6G_PsHIIMQ-hf4k5TFFf5T2FDkTtCQAXDfV0qZ9sh3a0GDbnkt3LwcEFz_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb3c4a972.mp4?token=Fe7OjmSnGu4EMrtWiiwUhklCzo0AD6TJUCynLy5YKfbBRBvxOrQJoW7M-M-rHNy4oukzWLOAYIHSjy6sDo2DKCBDvuvJ3Zh--Wb4lHuS_ZdmNUaqPfw0IaG7csy2zpE7hg7_gsfno-h2aHnJsu1EJVyD3i6H7IZqN9FMMZwxyBXWH6IwSSVmHM6xXiU4_tAYgReOa1lIP4drVv4V1ilcE-opTauRwWaFThLsIu0mVVTMiu2saz01f6294x3cghYol2DsOBv6bcoRTvy0cj7JS5-oxm6G_PsHIIMQ-hf4k5TFFf5T2FDkTtCQAXDfV0qZ9sh3a0GDbnkt3LwcEFz_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: جای تعجب است که ایران پیشنهاد واگذاری تنگۀ هرمز را داده است  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440455" target="_blank">📅 20:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
حزب‌الله: دستگاه اخلالگر ضدپهپاد ارتش اسرائیل با پهپاد انتحاری در اطراف قلعۀ تاریخی الشقیف هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440454" target="_blank">📅 20:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExCjEbak7vhlgvsDsGyFSOGFO5PME8Zcm6ZTxcXdXlhOsFjrh-GkPjzMijAv6RRBOeu0_URVITa0L3hPSd8AoiBmprwWLv3Lx8XBXGS1f_qMPkNuJL9EKLrAdWGj616IwRKo8XSBpqalwHhcO1ELd07vCryIyN7ntMj3wegfH1zX3GukRJL55bTG0P2IZBN7UaclsGTtZdCaJfA2Am2QxESqGARfe4TwxZZR94ShI9y81gjEb1WyQBXtgCIxXUETdkLykmXB6JELAEdgAaydECkOC4mMDJ30vyl-Ht8eN2-V7ZarEqWKeljXlsM1u1cVSrkd23MpID3Kb_cnKWJILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازسازی ۲۵ مدرسه آسیب‌دیده از جنگ رمضان در هرمزگان
🔹
مدیرکل نوسازی مدارس هرمزگان: مرمت ۲۵ فضای آموزشی که در جنگ رمضان آسیب دیده بود به پایان رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440453" target="_blank">📅 20:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قوه‌قضائیه: پروندهٔ عباس عبدی و مدیران روزنامه اعتماد به دادگاه رفت
🔹
قوه‌قضائیه اعلام کرد پس از انتشار یادداشتی از عباس عبدی در روزنامهٔ اعتماد، دادستانی تهران علیه نویسنده و روزنامه اعلام جرم کرد.
🔹
در جریان تحقیقات، علاوه بر شکایت دادستانی، حدود ۸۰۰ نفر نیز از عباس عبدی و مدیران روزنامه اعتماد شکایت کردند.
🔹
اتهامات مطرح‌شده شامل «ایجاد اختلاف بین اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» است.
🔹
همچنین برای عباس عبدی قرار منع فعالیت رسانه‌ای به مدت ۳ ماه صادر شده که شامل مصاحبه با رسانه‌ها، انتشار یادداشت و مقاله و فعالیت در شبکه‌های اجتماعی می‌شود.
🔹
با صدور کیفرخواست، پرونده برای رسیدگی به دادگاه کیفری یک استان تهران ارسال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440451" target="_blank">📅 19:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند. @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440448" target="_blank">📅 19:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440447" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده  @Farsna - Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440446" target="_blank">📅 19:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440445" target="_blank">📅 19:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله راکتی سنگین چند روز پیش حزب‌الله به مواضع نظامیان صهیونیست در شهرک العدیسه لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440444" target="_blank">📅 19:30 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
