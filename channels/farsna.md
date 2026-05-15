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
<img src="https://cdn4.telesco.pe/file/jXZIhH7qH3uKnsPcTr8K5xbUxv2O9ytnNY2ojt7O4qlfN4nqvJTr5-XO1pltpNiufIvzTkD48Cv_EohRfFz_86p_u8vDjM_53ZH_4C-2PhGDdWNHKRlDtxI5Lr5Psc49l5hA9HGPwkFV-KC-Zlw2lyjSaXlWZqE3GEgI200YkKi4rQjHzdK_mrvrdsiSB5dcmhe3yE0Izn-IdXwbXUaWsKXA-jBts3iMHLM_QnAQnqHYnWY2sE96yuFrDe9HUZiCvvwj-KZrvSWVseatDt94yFLdt8irYJ9TjcVUf8UPbHPdSBxMiB9_N-cASpqBtC-xejb41BVqEJcWQ3Rj5_YiRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 15:58:03</div>
<hr>

<div class="tg-post" id="msg-435739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b16e61a6.mp4?token=IONPudncGtI57n0TXMVTr1p_YdOMiXWY4550NcRnMHem_IVhAtR9P_YTgDN5A7vrIhirNR6xqchsBldSlYqj0HbBzhZzwMPDP-HyYp8p9W4sbC_H2A-pupBOEBHLnC216EHbv7zlmB8cXgbI6QyMsDDVu8JAm00D4B_grSVcwICAX6a_h-ASpnAdAFidMNyP9qaL6rgB-iHnfiyaoM_FSzHq-j3wZH7e7Ka4NpPsCUk9oK3mvkPhLj8ueoEWIQb54AtwHLlvMKWgkAIyauTtFofH06ItILpNQPV_7Izm93d_U3RW9NrwiLcQm3JWWVKqw_aVTxa3JXjZnV4LwW8h3DbLterGeoIx08b7IZk6IuUvhN7Lhmz3f85eA5K9Iu5DcGegZO1Wwpwux6pZvlK7P6h-whYoafg3bZ_MmR9SmkOxDb-2zg55i-You9JiZ6QvuyzcyUwZnw_661LlFeDajfGQGPt8SrJJE12zi0oatTT8iKrRmIqQC7XrHDGHxKzL8oEiaodjnqHFkLWM9QR9-W2i9TYQXBes6bARpfMIwFynqpw429Ij8JybHPZIO6YyfdyhSlNHppZecS0iQPtz-1LSdWv2JABrfd6uOZws-JkxldoO6QmIUECP2Nsvn5J_UPHTqTHweZKo74KZt2VZX6gbpTh67_iijCYMorhcwsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b16e61a6.mp4?token=IONPudncGtI57n0TXMVTr1p_YdOMiXWY4550NcRnMHem_IVhAtR9P_YTgDN5A7vrIhirNR6xqchsBldSlYqj0HbBzhZzwMPDP-HyYp8p9W4sbC_H2A-pupBOEBHLnC216EHbv7zlmB8cXgbI6QyMsDDVu8JAm00D4B_grSVcwICAX6a_h-ASpnAdAFidMNyP9qaL6rgB-iHnfiyaoM_FSzHq-j3wZH7e7Ka4NpPsCUk9oK3mvkPhLj8ueoEWIQb54AtwHLlvMKWgkAIyauTtFofH06ItILpNQPV_7Izm93d_U3RW9NrwiLcQm3JWWVKqw_aVTxa3JXjZnV4LwW8h3DbLterGeoIx08b7IZk6IuUvhN7Lhmz3f85eA5K9Iu5DcGegZO1Wwpwux6pZvlK7P6h-whYoafg3bZ_MmR9SmkOxDb-2zg55i-You9JiZ6QvuyzcyUwZnw_661LlFeDajfGQGPt8SrJJE12zi0oatTT8iKrRmIqQC7XrHDGHxKzL8oEiaodjnqHFkLWM9QR9-W2i9TYQXBes6bARpfMIwFynqpw429Ij8JybHPZIO6YyfdyhSlNHppZecS0iQPtz-1LSdWv2JABrfd6uOZws-JkxldoO6QmIUECP2Nsvn5J_UPHTqTHweZKo74KZt2VZX6gbpTh67_iijCYMorhcwsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر منتشرنشده از دوران جوانی شهید سپهبد موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/farsna/435739" target="_blank">📅 15:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuRRYBDd3l6IkUu8HH53QzLlwmYtCaPMd7Tjm2cPApQKitiM80pk5JJRDkf6QeK2TfkfqR6HmlTIn_L_LNu2wNBsX5Grft-3JbLu7mv7__9zaxPnXRlLSsDAw07mmXjYY2Rba-6Sh72IT9bvBWgvESlqrKo0zcw6QmNZK6UO5ID0Er5dqSGJZY1gWIa81kAP4NNJFsVNjGyxDCQlmltFz5sgjbAzw33ZF2_a7vxNO9yRRB4-RT1Wgo8ujmG_PbHkVJytXNHQnYrJjwJvmteuX0HkFyRIVhXYgQ7_cB9z4GVYqnFQpvE4HK2h7jXus9HBixW5H03Ny-tzkucJBoVUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaTEx8u2G1SSqY9y7gVf8CJ96zUseNBJ8lktdz9q7Ru0pm3IguXw-lRHZT5pCvYnDSgXsi1Ws-lCKI7CVKR2aU_DMV0XL3Rqf2pSdFqnCcjbRj68jpZ1biHGjh6MBug2dow9ohVEgattCjl5aRLs_9kDMoe8FsaMHN2Rhtkm8zkmMHSuC44pF2wbHrco4nRaw5waYPJnD877CLFZdRYNIVf_pE7yolPxHJmQhRejaScFH_aTS7v7XHyZ5R4NtuStR-rALJMKf51VSC_7-Rb2qacvHR_9OhqBaJK4SU41993NUkqs2411Dm2Kf7Lm0nhnbghSTyVIb2c7scsadZ6Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaOKlFqHvKxDbjSNE38P7NP7NkmYarixq8DScsONsQunS1uWN5g7ixfMo33jTdBEauJxtSYSd5OJhMaDKPq7Rc6yIXhXN1la37QKIGWMJWx5yrieybFrrgF0rZp39E5MK4JTZPrzApIy9OFVMI2JzJxR10h1kvE-N_Z1Bp5oHXBJcFsO_O3WKbh5Hi57SA291cCKUvxBgy7HsPe09z_2pRMNUCw9gvJwkDXi_n6--dO6NbcG6NOLkltn2SsFa5hPqjeAlnj__tiTXoR39S4JC_2IjJ5pEIhE-S-Ge2kbdahmO2qo5I3I_H23tet5Io-2iSRoNaCD-GbGLFLjf0ja3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6mF2EErXlUBXcfGDIbUy2q8tpH6eDE7vdc46W-KwjZnC9aLaK6dBcUZVe7APcHLUQAnNQTLmO3oAcjYz8lRf_NSFqBbUF-1kTSiwW6Sl0hhBXjMiLhHzIDV4vyoP4Zohkp6rBAbsRCIArMKStKd7P7owseApuTGFaN1WY2pgHyjsPupT2odfHyFzS-ALvtwuGA79DXwG_UZ5o1mvvqU5aVz2tllJz-rpIx4P8GlTonSqKfpNOvR2bTdgGus8jbAuR7gAmNRg-OddRxmh7LM16DEAT9HKvqQofjcwFnhXYz60zVMp-IJSWn6Nvt6aXu71f4CrQPYgs0xHZQjKnKJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5LP6dkrg_jU4UKuEPiJa_QxiiHE5yRLMuW4UK9ufoba69Gu_Sfzvum_kgq97NSv9tyjO5-y9PwFeuXUo-yoXKl3x_OoXNJM390od_IVXPRewjWW-NUIU7ZRnwS4Rm02yB2L0wpHtqEk7XIQvueq5KVdqvqevTF_e90H295ctTaybrROWrPJTCzCyxK9Y77_uC30JM6Vx2U_U35JroNV0ETmziefiQbVlKZk-xV-W0FjmPI30tgle1vFbQQuN7e77-Insr2NI3N2oqw1LJYqCc-xADEZKB1gGn4mlZHkgewu9LgztgCZgIMYNLzW4yhTh9L7RqLGMSKbnK1hsMfHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AF1b3vQgblA5CGX7I4yC8NzDHJR7hbn6ytxpBC3pVJhZtTfGPKaYdyxNppzWhDuAr_wUSTFHVxoHYYavnZgp_4gLjRCQwQfnxYDWjBDhk1u3sl70pv0jVg6nukEbuzL3rgzQ3joY6QKcspKf_f86eodL4IjvCCfvi0XxHWM_fJfPaBZq9_lZ6NK7yQ4JDvcMcBg8xBvLv0krtOF47taOxKFCoWaeEGLf5HuBkryTgPkzF3D7DACBXpvVyUongIUY2VTinnFRjadfWiQcsTV0rrVLsTn-2oR5CbdEkuwachB7GJ52kHnxS9HjkQy3VX29kY--6484zDGJcCE-4uiVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_iuGTE5KEP_q36EgygIqZh4Lely74pvIuQNW1Na9770QuH8jq265ClIDamACXVswrcitFraKV_Ep8XUbzOkdtkWKa2AgSN-n9LEkiv7Af_1pXzE-LOjDKN-WKYH86_VXYtihVTxhrTP1f4jJxZI2TbgR6jZN8zGYgqQausGhyS_ovQp65O7oT1T3cHLvgWEznrOEwmX-sM85Q_1PIhdlLpx9mHPhs2WhysDqhvHkcIlsothuNTXD73OunzlHoj58dVGh2SB6HJySwYIQyH8AVdMhvWAtmTQifrNGo_1B5F67-fnx67B2ZxW0Hw46NnF_39ni5LkftyGBO-6HFtAmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیاه‌پوشی حرم امام حسین(ع) در آستانهٔ شهادت امام جواد(ع)
@Farsna</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/farsna/435732" target="_blank">📅 15:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXPkPm7G4Tg9B4214MIFGuGgqLN-yTl0xKzTc3NYIpg1yJL9mgM4P4pA58YAOIWdEr6WiSvXAZALjObeZ75o7O6UQBntmEHqvrABdtzzut0HjWWqKIWXwGV4TQDzKb6mkgHSzG6xHYf54gpLDmS8DOgpVOyOgliJnje7wwY7RtUggGlGJxa6Yh81hVo_Fa75ei8cArpvS8ueQfLL2xClbEYD05q9WnoPZSS-HayzWUEfzFxs5N5V9WZdELjaNNhOdpq7POEBRJ8QSaXwVHBPkblFmXcTobbPOL8Cj1m60q6Rw8excsJFretaB1JAo31buT2ng4v6NuD5-_gd4pbg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1IvVhaPky2BMhgKJhuDJUVJdXM-Tyv0le8IGSRr7P3DNZD9OQKNd0hfsONE74chlv-sjN1pa0LXlTEkwxZlOuYPbSqBQC0kvVkbhIXbikC5V2bvkZF8wC9nAJFtAmQtgF-_EHfg_1of8usIBjKLeaBt0-D0T_ne1S89D7sUGTcpYEkK0xhU7hsXQR0aUQVnsaDQphu4N2mH6IcbqmixlqQlMRIE1vrh2emesuLCcZusCNwPvXQZHyPHR_KSF6Joe2yNHdsRjimdL7LGJFokrBsE53xHta7dV64_ZfdJ1QRm72inJ79cXydMxzIUFifN5q3cKxmX7_dQJtXYfREXhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲ مدال طلا و نقره برا نوجوانان بوکسور ایرانی
🔹
متین چمی‌پا بوکسور وزن ۵۷ کیلوگرم تیم ملی نوجوانان پسران ایران در فینال قهرمانی آسیا با شکست بوکسور اردن طلایی شد.
🔹
همچنین فرزان احمدی، در فینال وزن ۷۰ کیلوگرم مقابل حریف ازبکستانی نتیجه را واگذار کرد و به مدال نقره رسید.
@Farsna</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/435730" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJEgN6Csc3Oks0P6KN8tbR17tDgcj8nRGhCAZYSYbIv44XTmGn7yopmd9mNLH69nJE4cg0a-2oakFXXhxTuR_Re8QoWfdThE9lxA2BmnKhVmOK-zzvhaqB1UCdKJMme2CQSfLDBp0a5oaPhLRfi2T_Rmv6ddJTkjSL_vJ3yFd49r80E_Glkn2YU2JcgccKoOSD98KdogoRNyy2JyWO9w5a4lhaq3msl2KgkUm-6WFlnknKVqCLzvwOCgAg2Y2GUZ8FGuOrG_UnlfJ-yfIL9yVemrmfUgrY4gqobTJ51wDqEeTzuxZCWVoD_tGlBCQ8u0tDVyCNrXdxynvaOvbRSlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها باز هم مصوبه دولت را پشت گوش انداختند
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد از بستهٔ ۷۰۰ همتی مصوب وزارت اقتصاد برای تامین سرمایه در گردش صنایع بعد از حذف ارز ۲۸ هزار و ۵۰۰ تومانی تنها ۱۰ درصد تسهیلات پرداخت شده و ۹۰ درصد پرداخت نشده که به توقف تولید، کمبود کالا و گرانی اخیر ختم شده است.
🔹
اواسط دی‌ماه سال گذشته بود که دولت اعلام کرد برای حمایت از تولید و جلوگیری از شوک به تولیدکنندگان درنتیجه تغییر سیاست ارزی، ۷۰۰ همت تسهیلات سرمایه در گردش مصوب کرده و به ۴ گروه از تولیدکنندگان پرداخت می‌شود.
🔹
ابلاغ این بسته به شبکهٔ بانکی اواسط بهمن ماه انجام شده و قرار بود همان زمان به تولیدکنندگان پرداخت شود اما بعد از گذشت ۳ ماه تنها یک دهم تولیدکنندگان موفق به دریافت این تسهیلات شده‌اند.
🔹
مدت اعتبار این مصوبه ۶ ماهه است و بعد از اتمام آن بانک‌ها دیگر الزامی به پرداخت آن ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/435729" target="_blank">📅 15:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d30b2d935.mp4?token=uuplcM_yRTgMyFAcq-zJTT82BWM8M6Grn5Sl1BRPeMcsU6tOnNZdR7-XwD6AC1-_9G9ffpExLoD2Y4ulhbX0cyS3kGFYt_U4THN8Fdth_T81XPQOVnshN8GyXyj0kgfWESphTe2212eGDH-eLP1JzEXSzfXSfPcs_EFYeOs0tSat1bAOWNStynraHYn0DuSy2yeKZl9wV3mGNaYkip5yeWhLPcgbRNDukTGNttuofVk-9CeRtEpWqN_8PVzu9mxHoMnI4J-S8Yk3iVj09TA1FLAlvLg0r04fx2IRuYKUp7gtZI2d1fq7bS1i_GS6NbHx9etpxL27-wBcVrJT2viMOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d30b2d935.mp4?token=uuplcM_yRTgMyFAcq-zJTT82BWM8M6Grn5Sl1BRPeMcsU6tOnNZdR7-XwD6AC1-_9G9ffpExLoD2Y4ulhbX0cyS3kGFYt_U4THN8Fdth_T81XPQOVnshN8GyXyj0kgfWESphTe2212eGDH-eLP1JzEXSzfXSfPcs_EFYeOs0tSat1bAOWNStynraHYn0DuSy2yeKZl9wV3mGNaYkip5yeWhLPcgbRNDukTGNttuofVk-9CeRtEpWqN_8PVzu9mxHoMnI4J-S8Yk3iVj09TA1FLAlvLg0r04fx2IRuYKUp7gtZI2d1fq7bS1i_GS6NbHx9etpxL27-wBcVrJT2viMOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!  @Farsna</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/435728" target="_blank">📅 15:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EroGAQq9_0k_Q5Z7y5mjC0llJe7pyK-pR7cT75LC5ZvF07EYLNrnNFVAp-0yGBl6xNOOiKK-k2jd6Pu9XK1azj7r74NHCHvdvtu-ZUIKzM4SWNT6nP2TpW5US9Ykt_iaGMhgbwl1xpPeK4Rk2aKhJXYHmnTIVLJhqJ2UOCk_KmxpnMXZgoKdgK5bYZJEDBK6wFvJZdGu-SBlTumcIcvTYu9I2LiQMxJfFKijST5gh_iNyPsuNwAKUSBtmNVIDBv_1oGlwKPFaxHq17ph0NOI58aJKAFXxsn6EFb894pCNd4C6wbDEHbavupC8ngg5p9Hr2XtaaOiyfpKH1WelV0zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزهٔ ذخیره‌سازی ایران مقابل دسیسهٔ آمریکا
🔹
وزیر خزانه‌داری آمریکا می‌گوید بارگیری نفت در خارگ متوقف شد اما شرکت همراه آمریکا در فشار به ایران می‌گوید، تهران تاکتیک عوض کرده است.
🔹
شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران، تنکرترکرز می‌گوید، اگر ظرفیت ذخیره‌سازی جزیرهٔ خارگ پر شده بود، نزدیک‌ترین نفتکش‌های در دسترس را می‌آوردند و آن‌ها را پر می‌کردند.
🔹
یک ماه پیش ترامپ گفته بود خط لوله‌های ایران منفجر می‌شوند، تنکر ترکرز اعلام کرد، بدون درنظر گرفتن مخازن خشکی، ایران یک ماه و نیم زمان دارد حالا ۲۴ ساعت از ابراز خرسندی وزیر خزانه‌داری آمریکا برای توقف بارگیری نفت در جزیرهٔ خارگ نگذشته است.
🔹
این‌بار هم این شرکت که پیوسته در حال پایش نفتکش‌های خالی ایران است، توضیح می‌دهد، هنوز هم نفتکش‌های زیادی هستند که ایران در آنها بارگیری کند اما تولید را کاهش داده تا با افت بارگیری نفتکش‌ها هماهنگ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/435727" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435726">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b95147575.mp4?token=Q9EK2sAOmsMEtA0swmCbfIim10BGs52OuTFkt_3wYXNBAmNmBQp_eJ43zJL0NTcRgaNqGAP3-ovCqeutz4zMj4ohYN5_QRDORAr52kHmFILBLUM8yq3eVmml8H8MR0xzmTaUHROXDnk2mIR73KLhcCP1WzsMvMoKdag6uRSJFdSoROlTXyDl4NZTYC4BYnfi8EMKRHLbVTu6KvPVJh2La8q0nxaRwtEbco_fyECZqaoM1ypU5P45S7zNLpoyiZ5HXCSnYaKGj9MRtyjnFpmkTRvm8p-NRiY52SNbZssTqIAB5pqao0Q8o6ybrveatnZTj3RZ3rKqJhvyqyj_Ir2JWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b95147575.mp4?token=Q9EK2sAOmsMEtA0swmCbfIim10BGs52OuTFkt_3wYXNBAmNmBQp_eJ43zJL0NTcRgaNqGAP3-ovCqeutz4zMj4ohYN5_QRDORAr52kHmFILBLUM8yq3eVmml8H8MR0xzmTaUHROXDnk2mIR73KLhcCP1WzsMvMoKdag6uRSJFdSoROlTXyDl4NZTYC4BYnfi8EMKRHLbVTu6KvPVJh2La8q0nxaRwtEbco_fyECZqaoM1ypU5P45S7zNLpoyiZ5HXCSnYaKGj9MRtyjnFpmkTRvm8p-NRiY52SNbZssTqIAB5pqao0Q8o6ybrveatnZTj3RZ3rKqJhvyqyj_Ir2JWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: لغو تحریم‌ شرکت‌های چینی خریدار نفت ایران را بررسی می‌کنم
🔹
من هیچ درخواستی از رئیس‌جمهور چین در رابطه با ایران نداشتم و از رئیس‌جمهور چین نخواستم که برای بازگشایی تنگه هرمز بر ایران فشار بیاورد.
🔹
درحال بررسی لغو تحریم‌ها علیه شرکت‌های نفتی چینی که…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/435726" target="_blank">📅 15:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C10lKxALjOCeYxh-AORHqtzEjoJX2RjANiVMAXZyzhXZ0i7amfNbdRbvhndP-XPIKfm0RADvwyizoPKGeW5yaB_sHlQmmcPK9kWHUhG1foq8dbtYEDWInxz4CHX_UmYk0tnHKSZu94eCBRHwzMH5CCapA4p3RdlGbgh5_pVU9R8UIiJ8EbDsYMy3JmGkxp8kIACchep9c1t3BRPYNEsaWaUPevErCQgauGMHXdcTSU82U6y_n__4V6JXwOo94vX3UrxNDIKGvs2zlsZOeV-oEBz-lE2zCv1UmwvzSzi42821en9F9fOEjuiifEPbN0qab8-jMc4m1FGU4I5WpqZ36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریکس خواستار استقلال فلسطین شد
🔹
وزیران خارجه کشورهای عضو بریکس امروز از تلاش فلسطینی‌ها برای تشکیل یک کشور مستقل و رسیدن به آرمان‌های خود اعلام حمایت کردند.
🔹
به نوشته خبرگزاری «اسپوتنیک»، در این بیانیه آمده است: «ما از جامعه بین‌المللی می‌خواهیم تا از فلسطین در انجام اصلاحاتی که با هدف تحقق آرمان‌های مشروع فلسطینیان برای استقلال و تشکیل کشور انجام می‌شود، حمایت کنند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/435724" target="_blank">📅 15:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G71FGtBVippAIZ0Q5amZEDj9F5YeLd5zdBK_Rh7RIDROiAun0cWMjIDY9X2mnYD085mMx6T2psvL9MJZqg6oY5OKITqfYGwJzUdHFAe4TZrjsuRJuzNlYRwy_edS8z3ZDAuEdTJshHI2jTYSpiGKfGIfPe3sx83xC9omSBxwNo4TUdg984wXEYH8Y8jpYKtLzTjXY1xtAM6lGoSs75K7vaudngPudhb9q65MLsCmHHjJUttGowUfitXayPzRe3ogpoXSOwQQth0PwcEiQMkOIVby1BfDZQymQgsekPUKtIkjrHLq8yq7Ykb0qPZdtrPRoK172BKpA87Y_5HFCy8RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: لغو تحریم‌ شرکت‌های چینی خریدار نفت ایران را بررسی می‌کنم
🔹
من هیچ درخواستی از رئیس‌جمهور چین در رابطه با ایران نداشتم و از رئیس‌جمهور چین نخواستم که برای بازگشایی تنگه هرمز بر ایران فشار بیاورد.
🔹
درحال بررسی لغو تحریم‌ها علیه شرکت‌های نفتی چینی که نفت ایران را خریداری می‌کنند هستم و به‌زودی تصمیم خواهم گرفت.
🔹
ترامپ در بخش دیگری از اظهارات خود مدعی شد، من هیچ تعهدی به رئیس‌جمهور چین در مورد تایوان ندادم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/435723" target="_blank">📅 15:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6ee_w0VW-u2UXDe-tRlofcK_Me-9-dnd_DOtEWi3hkq4nmh2jmDJtpNjDsxephd___EccSvJH51IM_gCyfILEPGe26b3k1GtfW5nAIRSVmJI-zHzhjUAxAMmzn0xqioRn2amBMIFZmOiSd2IqsLdnHjEvv0-hneBwp6P5Ga2dneRHmvH99WKPWLc2n-CkUaY67oNDFHg9m7EEtH78YVP2ROU-6qbOat2Tor0xX73lJ_X8sNA75zT-jxIvR0vUOkv48fIdd0WP0CuHyaO14DPjF5XW2iuAH_2sqL5l2syi1C_ImlPaTpveoLzmpTsSTTOpfUoS9isr4fHjEnrMYhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام تبریک پزشکیان به نخست‌وزیر جدید عراق
🔹
جناب آقای علی فالح الزیدی، نخست وزیر محترم عراق، کسب رأی اعتماد پارلمان و آغاز به کار دولت را به شما و مردم برادر عراق تبریک می‌گویم.
🔹
امیدوارم در این مرحله جدید و با تکیه بر پیوندهای عمیق بین دو ملت، شاهد فصل جدیدی از همکاری‌های استراتژیک باشیم.
🔹
ایران در مسیر توسعه و تحکیم امنیت در کنار عراق خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/435721" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9429126ab3.mp4?token=Cwkr1qZHoRTDNWiZ1Au4Gb0lBcmziHKoB7zBGEjlp0pYcVm3vtGdM24udhE1XEjgLkiX9Qd8ipY1OP_iRZmJJhnZC0SANZq0GSMLmH4YeCg870m0j4fBo_0fiNqgBLfX-QNSTEKlYPPUr7S-3f6ec_gowJyVgRTw3uCWuKAdJNRhpRpLEQ0VeIMZ6FJbPVgKJlxf5jedOQHD4KTkHZ54_LjodvKiDcmLpaH-Am4qSoZRbPmNss27NeDEN9ovFc6ge7S3vEerl0bxGysLBQBvRmJtPvPFy70ZHS4ffuHacAvTdO91O3eT5I_vg9Rcc1mltbMeO9hhKnWjXMMkZ6MUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9429126ab3.mp4?token=Cwkr1qZHoRTDNWiZ1Au4Gb0lBcmziHKoB7zBGEjlp0pYcVm3vtGdM24udhE1XEjgLkiX9Qd8ipY1OP_iRZmJJhnZC0SANZq0GSMLmH4YeCg870m0j4fBo_0fiNqgBLfX-QNSTEKlYPPUr7S-3f6ec_gowJyVgRTw3uCWuKAdJNRhpRpLEQ0VeIMZ6FJbPVgKJlxf5jedOQHD4KTkHZ54_LjodvKiDcmLpaH-Am4qSoZRbPmNss27NeDEN9ovFc6ge7S3vEerl0bxGysLBQBvRmJtPvPFy70ZHS4ffuHacAvTdO91O3eT5I_vg9Rcc1mltbMeO9hhKnWjXMMkZ6MUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندهٔ خبرنگار صداوسیما از آب‌های شمالی تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/farsna/435720" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7bd7aa02.mp4?token=S26HMR8hey_MUSOfjyTVtAWDdDakEz8bt3jeWb0XOYhJU77Fq00AhA-55782K7oU1PR7Or2HjhcI8arOlNuDDEM4n2ujRf4-0uQFWCYcjETrX5VCwgjymstnor3rRzWZEHsQfmTd0yRXLNcU9GtNRBQb4nuWgcZsNY4Dd_KBF1rvuqNthx3xor5D3hZ7wrsw4du_toG-8nqe1vY7_Cc89c0fmX5wm1BnguXfPLxysmtge_MCeE0CiKibgytYGsj1jQh90neKU4hnbUTbBOSx_2GRtZXEM-yzubjM_0Mfc-DYFVNkxUJIkqlVsPDJrf64Xz2IqyL3nfi7rnEFWPLDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7bd7aa02.mp4?token=S26HMR8hey_MUSOfjyTVtAWDdDakEz8bt3jeWb0XOYhJU77Fq00AhA-55782K7oU1PR7Or2HjhcI8arOlNuDDEM4n2ujRf4-0uQFWCYcjETrX5VCwgjymstnor3rRzWZEHsQfmTd0yRXLNcU9GtNRBQb4nuWgcZsNY4Dd_KBF1rvuqNthx3xor5D3hZ7wrsw4du_toG-8nqe1vY7_Cc89c0fmX5wm1BnguXfPLxysmtge_MCeE0CiKibgytYGsj1jQh90neKU4hnbUTbBOSx_2GRtZXEM-yzubjM_0Mfc-DYFVNkxUJIkqlVsPDJrf64Xz2IqyL3nfi7rnEFWPLDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/435719" target="_blank">📅 14:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMHGCppTegNaYob4afUHoK8y39fm7cjBRqfyXcmIIvZKAyaiimCD-oIhWCLC9J0VVnfcCayaaq3w1AwQi1AMvadflt3pvn09ZG9W2HLsJrj1KTLpk7aV3IDLSp3kmHnRJZ0_JuQyTLO-KTTX2Rk6pagLd7S6vs9_1WVCfSqawc9elexgUEk-ua7RnIHTDbDekRuZ8UyYpdTuF36yrycC_YYCFaosWjV22EtmxAgXofSO1nDhBCpAi-wGWTUHvGsSexhry5foLg8Yz0OWk_Sge_v-OaYD7wsf87UVfdJs0aLEVZclf1hrrXcezMwnNVqQiR4FCX4UeLnZ41bx72IfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!
@Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/435718" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/435717" target="_blank">📅 14:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی: ما هیچ اعتمادی به آمریکا نداریم
🔹
وزیر امور خارجه امروز در نشستی خبری در دهلی‌نو: کشور من تحت تجاوز آمریکا و اسرائیل قرار گرفته است.
🔹
در حین دیپلماسی حمله رخ داد. از کشورهایی که این اقدام تجاوزکارانه را محکوم کردند مخصوصا دپلت هند مه ابراز همدردی…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/435716" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی: با پوتین دربارهٔ اورانیوم صحبت کردیم
🔹
مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم.
🔹
با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم؛ از پیشنهاد طرف روسی متشکریم. البته این موضوعی است که باید در جریان مذاکرات دربارهٔ آن تصمیم‌گیری شود.
🔹
موضوع مواد غنی‌‌شدهٔ ما مسئله‌ای بسیار پیچیده است و اکنون با آمریکایی‌ها به این نتیجه رسیده‌ایم که چون در این مورد خاص تقریباً به بن‌بست رسیده‌ایم، بهتر است بررسی آن را به مراحل بعدی مذاکرات موکول کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/435715" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0beUrNOL3ofVdIlioqo47nJUEAqT2b3uZnmEAD0vYgC8nqP25F_iwPgKpxj3EpAeeRpioJrrNYQ-zIHIxl58vKDOKvabKnRv_BMgSWlxL6AmAepOLb9mYECsRZAFhPGrSWhxOKekutu7SZXiuuFHAA0nBUefcMS15qH4FSKcFZCrgFnxym5z3PltccW1A0D18sFgJxqAT7qnLpzr1Flu074myDDJL7TDNbKgbctHrHQicmWw892d3fvo-HxhXi1cIRVHJyVDRqr4-bcZe2IWyjOH7USu_RsF3GjeiUoSrhcpb8dgrMZHpQVF-aEfPavQAumIXaC90-HfLfNkxAcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام
رهبر انقلاب به مناسبت روز پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی
بسم‌الله الرّحمن الرّحیم
🔹
زبان فارسی علاوه بر ابزار گفتار و نوشتار، قالب شناخت و رشتهٔ اتّصال اندیشه و مرزهای هویتی ایرانیان را تشکیل می‌دهد. زبان و ادب فارسی یکی از بزرگترین ظرفیت‌ها برای ترویج فرهنگ و تمدّن غنی ایرانِ اسلامی در گسترهٔ جهانی است؛ و توصیهٔ رهبر حکیم و شهیدمان اعلی‌الله مقامه‌الشریف به قدرتمند شدن زبان فارسی، چراغ راه اقتدارِ «تمدن ایرانی-اسلامی» می‌باشد.
🔹
ملت عزیز ایران در دفاع مقدس سوم نیز همچون دو جنگ تحمیلی قبلی ثابت کردند که داستان‌های اسطوره‌ای فردوسی، واقعیت زندگی و شخصیت قهرمانانهٔ آنان بوده و مفاهیم انسان‌ساز، سلحشورانه، و قرآنیِ شاهنامه، همهٔ اقوام و اقشار ایران را در حفظ هویت، اصالت و استقلال خود و مبارزه با «ضحّاک‌وَشانِ» متجاوز، همدل و همراه و همساز می‌کند.
🔹
این حماسهٔ حضور و دفاع و پیروزی، تکلیف بزرگی را بر دوش اهالی فرهنگ و ادب و هنر می‌گذارد تا همچون فردوسی برخیزند و بعثت هنرمندان را در امتداد بعثت مردم رقم زنند؛ فکر و قلم و زبان را با هنر درآمیزند و روایت خیزش عظیم ملت را در تاریخ، ماندگار کنند.
🔹
از سوی دیگر مقاومت غیورانه و پیروزی افتخارآمیز در برابر تهاجم دیوسیرتان و شیاطین جهان، ملت را برای پاسداری از استقلال تمدنی و مقابله با تهاجم زبانی، فرهنگی، و سبک زندگی امریکایی آماده‌تر کرده است تا با ابتکار و نوآوریِ فعالان عرصهٔ فرهنگی در جهت تأمین پدافند زبانی و گفتمانی و رشد و بالندگی کودکان، نوجوانان و جوانان، مراحل باقیمانده تا پیروزی نهایی را با استواری بیشتر بپیماید، بِعَون‌ِ الله تعالی.
سیدمجتبی حسینی خامنه‌ای
۲۵ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435711" target="_blank">📅 14:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/435709" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عراقچی: آتش‌بس را نمی‌پذیریم، زیرا نمی‌خواهیم سناریوی سال گذشته بار دیگر تکرار شود
🔹
مصاحبۀ وزیر خارجه با کیودو ژاپن: ما از هر ابتکاری که بتواند این جنگ را به‌طور کامل پایان دهد، استقبال می‌کنیم؛ آمادۀ شنیدن و بررسی هستیم.
🔹
در حال حاضر، هرچند برخی کشورها…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/435708" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cafce2fa9e.mp4?token=o0EHBvkdi7zRHPd0m03_iay-yrjb2lv3lHRuT8uhmdy8XBoLNHk57YoAC9IhF9I_cPdWiepvcWgiw6SbKLxB3H8eOhVVHjsxAe6LMuUAF3M8g3vvhcQZUjsC9HA8YvKbQt98j35ADt5MuPX1zcZEgUluq9xhwWsplWg3m2Rc0vO4uzq0IT2M7dRuiY8cEJWx1vbtGaRpGNbclJs5NmuzaX0ntXr-NbOTul2xQuV9iRv43gxIkhjGCCWweE3ylD-plnRDQtO_WRzj_2Nxwf410zjaxa2nxXCAUYs3SJ1FFcre3xgy_LbM8a3j6SApCsCd0aIjP8o9GZ110r_SN-fCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cafce2fa9e.mp4?token=o0EHBvkdi7zRHPd0m03_iay-yrjb2lv3lHRuT8uhmdy8XBoLNHk57YoAC9IhF9I_cPdWiepvcWgiw6SbKLxB3H8eOhVVHjsxAe6LMuUAF3M8g3vvhcQZUjsC9HA8YvKbQt98j35ADt5MuPX1zcZEgUluq9xhwWsplWg3m2Rc0vO4uzq0IT2M7dRuiY8cEJWx1vbtGaRpGNbclJs5NmuzaX0ntXr-NbOTul2xQuV9iRv43gxIkhjGCCWweE3ylD-plnRDQtO_WRzj_2Nxwf410zjaxa2nxXCAUYs3SJ1FFcre3xgy_LbM8a3j6SApCsCd0aIjP8o9GZ110r_SN-fCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او ۳۰ سال برای ایران جنگید
@Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/435707" target="_blank">📅 13:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fju2jFI6HunZULh4UUdgeerM5Ay4GguQpj8AFsSd1haXWlDcimGo1ubth9GZqmYRs-jScSTKTTxbmm_0vCXG-KEHKvuI81nCCdSwuY1H9hACy9BGGCNURmYv1oH-4XZWRNZ07jxR8p9fSx0fyUQJQcWWwWkMCKM25_maSC5XAQFQAEPqTycHu4YFTZqOw3Hj8eCaRaX1lDkAT6uKZGTtuTErBfzDtLw32oy69mIXyIe3QNDPMWW0BUwA_gAdvvkifkCZ_fvKeSLJqdTE1Vzbqh0MjziV-Lh-g0irnhb4qwgzBgbcL7vdwysS3Ok3iPoGW72AjdsnAyu1UZf8t9cpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که نگذاشت آرامگاه فردوسی ویران شود
🔹
وقتی خبر رسید که عده‌ای با پتک و کلنگ عازم توس شده‌اند، حضرت آیت‌الله خامنه‌ای بی‌درنگ دست به قلم شدند و نوشتند که آرامگاه فردوسی نباید تخریب شود.
🔹
همان چند خط، همچون سپری بر مزار فردوسی نشست و آرامگاه شاعر حماسه ایران را حفظ کرد.
🔸
سال‌ها بعد نیز ایشان آن ماجرا را چنین روایت کردند: «اول انقلاب عده‌‌ای از مردم بااخلاص بی‌اطلاع رفته بودند قبر فردوسی را در توس خراب کنند! وقتی من مطلع شدم، چیزی نوشتم و فوراً به مشهد فرستادم؛ که آن را بردند و بالای قبر فردوسی نصب کردند؛ نمی‌دانم الان هم هست یا نه. بچه‌های حادی که به آن‌جا می‌رفتند، چشمشان که به شهادت بنده می‌افتاد، لطف می‌کردند و می‌پذیرفتند و دیگر کاری به کار فردوسی نداشتند.»
🖼
اما دیدگاه‌ رهبر شهید انقلاب در مورد فردوسی چه بود؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/435706" target="_blank">📅 13:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3sT1iCRt5AH16xXMPJKNRYFsNyov51zs4vXJpue1-HSzBq8I5PqQvjfwAVlEB36c9E4W3Iv6mE9WDstVcFz35wxBUOxccMVKbsWFej93WqZ9YddNflE3ZDvfCYjyalECpKREr_FhXiTKeL9Y6wrb-R6t9lntFORwy-DuMth6rF4NH-pUAerdsULaTXy2eb8Tvin6VlLwLtbLEBmnC_2hUolDqP46ytRaVkyPVNkPUwXSIXBafw7MjVYf_61rXokOId6Q_pQXn7LPSyHrjV_Oer5Dlgt3Yw2hzDPovfBJk-unIc4kEarK1d2oJObPLiUUesAdRjtQzhqmdz5tEe3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: ما هیچ اعتمادی به آمریکا نداریم
🔹
وزیر امور خارجه امروز در نشستی خبری در دهلی‌نو: کشور من تحت تجاوز آمریکا و اسرائیل قرار گرفته است.
🔹
در حین دیپلماسی حمله رخ داد. از کشورهایی که این اقدام تجاوزکارانه را محکوم کردند مخصوصا دپلت هند مه ابراز همدردی و کمک بشروستانه ارسال کردند.
🔹
ما در وضعیت آتش‌بس هستیم گرچه متزلزل است ولی در تلاشیم به دیپلماسی شانس دیگری بدهیم. هیچ راهکار نظامی برای  موضوع ایران نیست. در مقابل هر تجاوزی مقاومت می‌کنیم.
🔹
زمانی وارد مذاکره می‌شویم که طرف مقابل جدی باشد و در مسیر درست قرار بگیرد ما هیچ اعتمادی به آمریکا نداریم.
🔹
پیام‌های متضادی که از آمریکا دریافت می‌کنیم هر روز مواضع متفاوتی می‌گیرند. گاهی اوقات در یک روز دو پیغام متفا‌ت دریافت می‌کنیم.
🔹
برخی طرف‌ها می‌خواهند مذاکرات را به هم بزنند و آمریکا را وارد جنگ کنند و امیدواریم مذاکرات به عقلانیت برگردد و از مسیر مذاکرات به راهکار برسیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/435705" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/435704" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fc71f97d.mp4?token=lYOhyFfkgJx05hoc4H_DW7evyxE0ZSSyWzPdzchySSCZLe6zmznghfOL3AtcMZan6Xcc2gWF-jMk30h8s4kquon4EusGZ_RVylhzBseiNzMgfx-Ed9DSDLYk90ZOmdxiIi0neZCT2D3wTCKkS9JYktc-a-k_840aEzDo788pCMJjbi24zT7XRjm0gDUm8LYfnUKTaQo1vMzGYrk6ew42tx29gyqIJiLxEc8OlXYaoEQOnbLZrw9XNC64mOIevIhYfGTMLwQgShbJ8VMwsbyNvfuLwpg29VqTNRSnbMiP-jKF7_lDGhLrRLRPSz1gbCsV1HlzUR5khyTYKaODeNeoNi2zMkhZ_sI-JSeyaEEUFJQoOtwYDVybZFxZ4ZEbbeA0kkfcQsxi3IHrfDd3wyHacQYHxKXUnWAhW7cfgKEt2cnYVGpmPuYWSHgoKVKQooiCI2eoaQNtiX9y2h-d4ZMZP0QBzqPm4wcyY6O_t-ny_VJTAd6CQgzzV02vQHQZArqotvqziUqf7xNxPT7HNEwYKOktRNWjGxuBmHb6wLWnelLH082ZRHd8mD2CfyrONwtcRwXkcE1GHZGjX7vet3KEG3FapYS6F5naB46IFuSQJXpnu38ntlr1zmSjC_40riridbTVAisTeHURAQyxo8P3vRNoVRRi8R4fYMyV7ebSjm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fc71f97d.mp4?token=lYOhyFfkgJx05hoc4H_DW7evyxE0ZSSyWzPdzchySSCZLe6zmznghfOL3AtcMZan6Xcc2gWF-jMk30h8s4kquon4EusGZ_RVylhzBseiNzMgfx-Ed9DSDLYk90ZOmdxiIi0neZCT2D3wTCKkS9JYktc-a-k_840aEzDo788pCMJjbi24zT7XRjm0gDUm8LYfnUKTaQo1vMzGYrk6ew42tx29gyqIJiLxEc8OlXYaoEQOnbLZrw9XNC64mOIevIhYfGTMLwQgShbJ8VMwsbyNvfuLwpg29VqTNRSnbMiP-jKF7_lDGhLrRLRPSz1gbCsV1HlzUR5khyTYKaODeNeoNi2zMkhZ_sI-JSeyaEEUFJQoOtwYDVybZFxZ4ZEbbeA0kkfcQsxi3IHrfDd3wyHacQYHxKXUnWAhW7cfgKEt2cnYVGpmPuYWSHgoKVKQooiCI2eoaQNtiX9y2h-d4ZMZP0QBzqPm4wcyY6O_t-ny_VJTAd6CQgzzV02vQHQZArqotvqziUqf7xNxPT7HNEwYKOktRNWjGxuBmHb6wLWnelLH082ZRHd8mD2CfyrONwtcRwXkcE1GHZGjX7vet3KEG3FapYS6F5naB46IFuSQJXpnu38ntlr1zmSjC_40riridbTVAisTeHURAQyxo8P3vRNoVRRi8R4fYMyV7ebSjm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برت، تحلیل
‌
گر آمریکایی: هژمونی آمریکا در تنگهٔ هرمز به بن‌بست رسید
🔹
ایران به بمب اتم نیاز ندارد؛ چراکه ثابت کرده که با کنترل تنگهٔ هرمز، همان بازدارندگی و فشاری را ایجاد می‌کند که یک بمب اتم قادر به انجام آن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/435703" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoNAqZqb1kjpNopLu4GlJxPcP5b1wm8vWDSmGj4wjpN2WSv06BiveSreA3wUXMJEKH86IT-xoaK1x4WYcQG_v0sYNy6Zvivh9QCSpRco01l63kYbWkP6ErgrndKODWwuxXWeDpvUNrSKNfpnyNr4YfUgSStmoIZ-KNP_pvcVhp0Obuj5Q39yKgAi3XiGzUBZOjlw92qiU1jarfz6yKL9PJdm79QhAp-kmyPqtxuISfngxTE4lGAx3HEFCTjIiqjF7W9cQ2aXNtTb5NvulMiYBi4Abm5bvObttZ5CIPiiXo-RRsD6nXDWxLhEDEpFc0oaAbY3w5NbrDQVqjKiFRWhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب نماز جمعهٔ تهران: مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است
🔹
حجت‌الاسلام ابوترابی: جنگ فقط میدان احساس نیست میدان تشخیص هم هست، در دوران جنگ جامعه‌ای عقلانی است که به استحکام دورنی قدرت و تحکیم پیوندهای ملی، دینی و افزایش سرمایه اجتماعی می‌اندیشد.
🔹
آنچه در این نبرد مورد تجاوز قرار گرفت بخشی از حافظهٔ تاریخی و تداوم تمدنی ایران بود؛ آمریکا خواست امروز ایران را محو کند ناخواسته دیروز بلند ایران را به یاد جهان آورد.
🔹
این روزها ایران فقط در میدان نبرد و دیپلماسی اقتدار خود را به نمایش نگذارد؛ در میدان زندگی هم ایستاد و حکمرانی جوشیده از درون ملت را عینیت بخشید.
🔹
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است؛ تحلیل‌های سیاسی باید بر پایهٔ عقلانیت، دانش، گزاره‌ها و داده‌های صحیح ارائه گردد.
🔹
ارائه تحلیل‌های نادرست مبتنی‌بر داده‌های غلط و تحریف‌شده زمینه‌ساز تخریب سرمایهٔ اجتماعی و فرسایش اعتماد عمومی است.
🔹
امروز ایرانیان بیش از هر زمان به نگاه منصفانهٔ همراه با عقلانیت و دانش و دور از روایت‌های هیجانی نیاز دارند؛ زیر سؤال قرار دادن بی‌قاعده و بی‌ملاکِ سلامت و وفاداری نهادها، به اعتماد ملت و حاکمیت آسیب زده و زمینه‌ساز بی‌ثباتی ذهنی است.
🔹
جهاد تبیین با تبیین مبتنی‌بر دانش،عقلانیت، گزاره‌های درست، مسئولیت‌پذیری و تحکیم وحدت ملی معنا پیدا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/435702" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliGoLbWZhhLvZvWjXGhcIUFC9o2MQGTXFutKN4T8Bv_z-RboCANjMRgZhVJrSLDBnioI-NQQY6K6Tl0HyihV-vpSx6xOECK_e9IJNM_NWUdNq9kpfgCn0Oui1-ppNHELOzVv2FPyVPcdYmeDam94FfSkHYyZvo5fWCtgDJan3Ia37Ou6rS5hHwmUCt0zMoGL6C6C0D5ursW1Q_a8Wgs1431J_DqV-rBZ5feiF0_UQcsrKQ6E83lN0hkrQFUwH4RAbAuQ99O1dPUQfivlvJJwEBhJEDBPPhBORT8jud5NRNLOPn6853h8G_iEZivHRqaEHxrvVsQuVX-41IDLDVVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: حکیم توس میان پهلوانان ملی و دینی پیوند ماندگار برقرار کرد
🔹
رئیس‌جمهور به‌مناسبت روز بزرگداشت حکیم ابوالقاسم فردوسی: فردوسی با آفرینش شاهنامه، شناسنامهٔ تاریخی و فرهنگی ایران را رقم زد.
🔹
حکیم توس میان پهلوانان ملی و دینی ایران پیوندی ماندگار برقرار کرد.
🔹
پهلوانی در فرهنگ ایرانی و شیعی، در پیوند با عدالت و حمایت از مظلوم معنا می‌یابد.
🔹
امروز نیز ایران، عرصهٔ درخشش پهلوانانی است که در برابر تعدی بیدادگران، امنیت و سرافرازی این ملت را پاس می‌دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/435701" target="_blank">📅 13:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860008d3a5.mp4?token=bsHZf_ZZjDh3f59R7tHwfi_zgWlnbKAAxfjLpviZ-aFvzbz_jMWPT-rae3ipS9SeRHcGXOqz7w5ILjh8bciaztdqFIx3eD7htdPJYtJCWM2_ijdpAB63sYaJEBKSXV4emXy9WBXHebw0d6GIck0oGZTd0xf5WxCY6UifTJMKF4ja9E7YF1lmtibkL9vCVYh1e01ghqWJfZpHm3d98aza06gWZRvcYO3_lhS2w-iMQBBR0gbcJ35tPF_ZvTGRd-xlK3ZNBsuzghLqQd0yGv5BaP1r0UyBbemAliUDF8G1Zbd0wyKj8WDHkS7vjobfak2h2BtsRqmm6XRfjreVNCat6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860008d3a5.mp4?token=bsHZf_ZZjDh3f59R7tHwfi_zgWlnbKAAxfjLpviZ-aFvzbz_jMWPT-rae3ipS9SeRHcGXOqz7w5ILjh8bciaztdqFIx3eD7htdPJYtJCWM2_ijdpAB63sYaJEBKSXV4emXy9WBXHebw0d6GIck0oGZTd0xf5WxCY6UifTJMKF4ja9E7YF1lmtibkL9vCVYh1e01ghqWJfZpHm3d98aza06gWZRvcYO3_lhS2w-iMQBBR0gbcJ35tPF_ZvTGRd-xlK3ZNBsuzghLqQd0yGv5BaP1r0UyBbemAliUDF8G1Zbd0wyKj8WDHkS7vjobfak2h2BtsRqmm6XRfjreVNCat6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر کودکان شهید مدرسهٔ میناب در نشست خبری عراقچی در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/435700" target="_blank">📅 13:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkMiFEf3rNLcdTP83rVTy1dYdAlUpp6tys9_2bkPv-PUmbESF5PAGdpi8AscL-MMK0T9AjMR39Vha8EuPmrFBGKu3P6WWRY_sAJ7w7RQQx4W3-yId-4mMqN_Suv-6R6xjgfJtFZLU8eyoEDY850Hglz9f3fFAIzDwO_A5lIj92ZldcWxmymEK5gySragfEFqLXeR8YisROU0L-BsXUyaRGvv55_oo1Sh3UJ9_m0Q3RyXlVFVx4bYJluPxSpI_6EbATPo07JXkTteMdByGJy4bjnx3U9NNwSvyQCm_NvbTo4TpvLo9RVyfP53VQoBx3macZklvv3bq0j5GU4bPbF0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت کشورهای عربی با درخواست امارات برای حمله به ایران
🔹
بلومبرگ: عربستان سعودی و دیگر کشورهای حاشیه خلیج فارس با درخواست امارات برای حمله مشترک به ایران مخالفت کردند.
🔹
امارات تلاش ناموفقی برای متقاعد کردن سعودی‌ها جهت هماهنگی واکنش به حملات ایران انجام داد، اما وقتی درخواستش رد شد، ناامید شد.
🔹
محمد بن زائد، رئیس امارات عربی متحده برای همکاری با آمریکایی‌ها و صهیونیست‌ها علیه ایران عجله داشت اما سران کشورهای خلیج فارس به او گفتند که این جنگِ آنها نیست.
🔹
بن‌زائد، شخصا با محمد بن سلمان، ولی‌عهد سعودی و دیگر سران کشورهای عربی تماس گرفت تا آنها را به حمله به ایران ترغیب کند اما هیچکدام موافقت نکردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/435699" target="_blank">📅 13:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حزب‌الله: درپی پاسخ به نقض آتش‌بس دشمن اسرائیلی، یک تانک مرکاوا در شهر رشاف را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/435698" target="_blank">📅 13:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435695">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYZRFpUy8WwormsFXzzUcbT1zFl1C-6SpTbPqljcTzOSoSj6YuXyiLMCCcnpyd1c6S_FHNgf6Ck3lZCG3pxmGO_F0WR29AlvVVPmP2sVEu7_B4XiIkDLkPgI1rfnUxwn5dy1-nznFRH2M_9l9CMfg4xOafHWP0VMvZPn72GoIgqf7TrYMnplGZ_JdpPMI1u33mUwW7PJrOYF2P50w8poEvSJVkDwmIzyTd3gIzK-dbqN40i4WDTcrwiPcBD7SHR-kjBXAlWwGUn3MRqoWvHriTwJAnF_VFfPsP4BEhiU3ymR70KoSd0261J4hroNb6hX8OufH1f1qxaFtoMquuXG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_v8nSHXIPmn09k4Q608zM75g-GUdA6IW77FwAn9JA0GCyYeHErHz5NLAO4Z95lM-kLNEPeQ234GNr2OfbYs0buurQtX8RZmeALS1on2HXsBrx2ZO14bx4waFf3uedZUrrKRBF_cK3KLv0guayrGeYNHMPm3r28ooJGI_v5Cko0FRaj83SNW-dCndGV3dfwy6Tr1eFzaZBRs4Q-SqKSy1HsM4EBfTTc45Yyvanpt5uClgID30-4LbJDrkEs4bnHnpS5hmDDi_6CddKyBiUpsohIMXmtU8XSn6ko0cbhBbgaH0af-MA3-QdHAAJqQIVJmcdGJeySKYzu_tmlT4JcIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IL8boFUUNxYrMwCcSo2x1WdCa4FXBReZeMnyc_QwDZEdbFHZgH0-ZIU3OhcKkzYJ65WpzEOjG8rF6hUaJycKDI_TxyzSyzDs9H29Ty6eX8Uuhy_ahK-0_646nxlE8-7DUyHIZN_9l4N2dKx-xQQP8G0paFKkNejhZQaevf55mY-iMAHe2IQ5aUVU97Gp4m4WYPSQDR3_6L8DbDJ1uTJyOJIx6wx1UJCAN2-VHJIEViqhdjtV-mWPTLGNcTGj6BtMZAhLF4Bk-szNCoe_ghvAa7g8OJoBpwBNcRgEK_yFAfHbgztv8O17JqYdWRMpKIp7q1iU0z9edndWnTuOzbbubw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خنثی‌سازی بمب یک‌تنی در عمق ۱۸ متری زمین
🔹
سپاه لرستان: پس از ۶ روز عملیات گودبرداری توسط مهندسی ناحیه مقاومت بسیج دلفان با بررسی‌های تخصصی، یک بمب ۲۰۰۰ پوندی از نوع mk84 را در عمق ۱۸ متری زمین در شهرستان دلفان شناسایی و خنثی نمایند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/435695" target="_blank">📅 12:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435694">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ثبت ۲۵۰ هزار دادخواست و شکایت علیه آمریکا و رژیم صهیونیستی
🔹
معاون قضایی دادستان کل کشور: ۲۵۰ هزار دادخواست حقوقی و شکایت کیفری در رابطه‌ با جنایات جنگی آمریکا و رژیم صهیونیستی ثبت شده و در محاکم و شعب ویژه دادسرا‌ها و دادگاه‌ها درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/435694" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435693">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8379f709.mp4?token=OJQGRW-mkeHxPCv9uM6aWaQdW564tDjdEUIv8SftTW7dJpIH3M614Ke9bsD2slgF2fKk6FyUH12xe-ETZbSxsXX6QRNMxSAGlWezVJnY9Ra_DEcxORk9-iEkAPZuG4FS9Kzxe5UIDx_VuGpyOdm11FiGKgxTOpOpMxi_h63gtWSALw5PDxLU1PCL16LjEwPpSfGuDC9GYn-ztncR8-CUhlaqszm6gDK78KU7IARLHjvsVT3PnyZ6sMqbopJMg8hDdSTM_haDPSDpF-S8YYqO8MZHx9u6XO7nKF9fj_n0HZh5KUJZO7xBFIH1VAAEeJyhuio8BUJebki5yLe-RvbMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8379f709.mp4?token=OJQGRW-mkeHxPCv9uM6aWaQdW564tDjdEUIv8SftTW7dJpIH3M614Ke9bsD2slgF2fKk6FyUH12xe-ETZbSxsXX6QRNMxSAGlWezVJnY9Ra_DEcxORk9-iEkAPZuG4FS9Kzxe5UIDx_VuGpyOdm11FiGKgxTOpOpMxi_h63gtWSALw5PDxLU1PCL16LjEwPpSfGuDC9GYn-ztncR8-CUhlaqszm6gDK78KU7IARLHjvsVT3PnyZ6sMqbopJMg8hDdSTM_haDPSDpF-S8YYqO8MZHx9u6XO7nKF9fj_n0HZh5KUJZO7xBFIH1VAAEeJyhuio8BUJebki5yLe-RvbMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ موشکی و پهپادی حزب‌الله به تجمعات نظامیان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/435693" target="_blank">📅 12:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435692">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dab68a33.mp4?token=hIhe4zr6LhkoyE8c9bmJn5-TeNMrdB5HxCc-8V70rwIRJin72gPQisHfv7V7pUWZnlv1RQjZl8tzEXeqBZ9-08aNeRwSJycqXm-kuJh7-zlC3lE70kbH79-_WUsf1BAgwUnkSNoDc15y23QAYRUPhU8xp2RH-UzfHztTwKHu2fcB8MjyD0nl8V9GwhvBnptGkYLtlcJnPV7SH5fuDrYdtSWKnW0qEKrXknIB_0xaYSlWFccYep3NBizSdGi808f94xxqqJ6IEUzcrmWvDJEhZIOqDFjGWzuWEO1Vyhf8_8wWKoakQgaApbeqo6IEOnZXyEBHW_wRZZPeM0z-YQUJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dab68a33.mp4?token=hIhe4zr6LhkoyE8c9bmJn5-TeNMrdB5HxCc-8V70rwIRJin72gPQisHfv7V7pUWZnlv1RQjZl8tzEXeqBZ9-08aNeRwSJycqXm-kuJh7-zlC3lE70kbH79-_WUsf1BAgwUnkSNoDc15y23QAYRUPhU8xp2RH-UzfHztTwKHu2fcB8MjyD0nl8V9GwhvBnptGkYLtlcJnPV7SH5fuDrYdtSWKnW0qEKrXknIB_0xaYSlWFccYep3NBizSdGi808f94xxqqJ6IEUzcrmWvDJEhZIOqDFjGWzuWEO1Vyhf8_8wWKoakQgaApbeqo6IEOnZXyEBHW_wRZZPeM0z-YQUJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتگوی تلفنی مخبر با مادر ۸ شهید جنگ تحمیلی سوم
🔹
مشاور رهبر انقلاب، در تماسی با مادر ۸ شهید «رستمی و کیالها» که در جنگ تحمیلی سوم به مقام رفیع شهادت رسیدند و اخیرا دچار سانحهٔ تصادف شده و در بیمارستان بستری است، به صورت تلفنی گفتگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/435692" target="_blank">📅 12:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435691">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حملات پهپادی حزب‌الله به شمال اراضی اشغالی
🔹
رسانه‌های اسرائیلی از به‌صدا درآمدن آژیرهای هشدار در شهرک اِون‌‌مناحیم‌ و ۳ شهرک‌‌ دیگر‌ در منطقهٔ الجلیل غربی درپی حمله پهپادی حزب‌الله خبر می‌دهند.
🔹
این رسانه‌ها همچنین خبر دادند که ۲ پهپاد انفجاری حزب‌الله اهدافی را در منطقهٔ شومیراه‌ مورد اصابت قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/435691" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1yNlN5RUudHVlMJr25Fi9pNv21ZYPoIb25SwCYMezSfJz2LNgc64JyAGoPimoOV_A1mabozKDKFE6zuH0ayKrGmBXPe7F_CcQEr9_7BB0379QWV8uN8T0q-Vcz2s6WpUy3A5IgttnGCMmuq36XUJ67xPvaWyJUNezhpHqBhbR0MbEBmoDo8sNOO9V84AImF-ZTLtSWQwvTzAs_qdyjYqw6QnQnAjY9bDUXidiAvzoAQaG8oTkH9s1wsxagi7NX3PgqGQX8Qyt__7Rs4DsUXbigfmsBGMf6k1Rpd7XApf4UPjIk2J5IKkMh0wsBuLsZWV9VnbsWASCz1_2DYAqz4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجع دینی بحرینی: امام خامنه‌ای(ره) امت را به اسلام بازگرداند
🔹
شیخ عیسی قاسم: شهید حضرت آیت‌الله العظمی سیّدعلی خامنه‌ای(ره) چهره‌ای برجسته از چهره‌های انقلابی دارای هوشیاری و عزمی راسخ، و توانا در برنامه‌ریزی، و از آن دسته شخصیت‌هایی برشمرد که جان خود را در راه انقلاب و رهبر عظیمش امام خمینی رحمه‌الله فدا می‌کردند بود.
🔹
رهبر شهید انقلاب مردی کاردان، توانا و کوشا در بازگرداندن واقعی و راستینِ امت به اسلام بود که توانست وحدت امت اسلامی را در خط درست آن مطابق با راه و رسم اسلام، و تربیت شایسته، اهداف سازنده و سیاست موفق این دین مبین حفظ نماید.
🔹
انقلاب بزرگ اسلامی در این عصر برپاکننده حکومتی هدایت‌گر و هدایت‌یافته و عظیم در زمانی است که امّت از نظر علم و عمل از اسلام دور شده بود.
🔹
اسلام تنهاه راه زندگی شرافتمندانه است؛ هیچ سرانجام نیک، باشکوه، امن، پایدار، پاکیزه و اوج‌گیرنده‌ای بدون اسلام در کار نخواهد بود.
🔹
این انقلاب و حکومت اسلامی، آمدند تا امّت اسلامی و تمام بشریّت را از بدبختی حال و آینده‌شان در دنیا و آخرت نجات دهند.
🔹
جنگ امروز، میان اردوگاه جاهلیت و اردوگاه ایمان شعله‌ور است؛ رهبری اردوگاه جاهلیت را طاغوت آمریکایی، صهیونیسم گمراه، و یهودیت سرکش از آیین راستین موسی(ع) به عهده دارند.
🔹
در رأس رهبری آمریکایی «فرعون ترامپ» است و در رأس رهبری صهیونیسم «فرعون نتانیاهو».
🔹
استکبار جهانی بشریت را به سوی دو فاجعه بزرگ رهبری می‌کند؛ یکی فاجعه مادی و دیگری فاجعه معنوی.
🔹
جهان اسلام در برابر این فجایع استکباری، محور مقاومت اسلامی، فریضه جهاد در راه خدا و دفاع از حقوق و مقدّسات را زنده کرد، و بدین وسیله راهی پیمودنی برای نجات بشریت از این دو فاجعه را نشان داد.
🔹
اسلام برای هر انسانی که ذرّه‌ای از حقیقت را درک کند، حجّتی تمام‌عیار است؛ حجّت اسلام بر اعراب را روشنتر است و یاری نکردنش از سوی آنان ظالمانه‌ترین، تأسف‌بارترین، منکرانه‌ترین و عجیب‌ترین رفتار است.
🔹
اعراب پیش از اسلام دوران طولانی‌ای را سپری کردند، اما تنها پس از پیوستن به نور اسلام بود که به شکوفایی رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/435690" target="_blank">📅 12:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
گرامیداشت ۷۲ شهید جنگ رمضان در گلزار شهدای ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/435689" target="_blank">📅 12:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt7kmgTKyQwi9PfGu-sVD2Jnd3oWxjWgN0iUUg_SAxVzFD5dMa3ScXUatyzmmBt5r3wDq9p8k6SDNEwcLhfbVhrQExK0JuKB2MUW-J8PnQYLmeT31PlYIuwUsF-g7IyCKCT7_h4M4RB5zukItWDVQK38_is36KulMbQMfL6JyZBV3A7wu9iEpT2-CpNik5fiwAhupSuXydLTTpTrv0pSQgEauw2mWHM4r3fPdixz4GAC-DpdlfJUVfPvHgerkgji3n_bZe50oLJgjmnJeG02a-BaCopSd4H5qUdfbWm8BIO-QvhB8GgNmXUy4svyzeQLZ1g1xpcljCfm0mQmAtj1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم کشتی روسیه برداشته شد
🔹
اتحادیهٔ جهانی کشتی اعلام کرد که روسیه و بلاروس بدون محدودیت و با پرچم ملی می‌توانند در رقابت‌های پیش رو شرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/435688" target="_blank">📅 12:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435687">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015597adc5.mp4?token=dsTkVsN_kVFM5uBahU5W8CMWcCxZYDVM37j3aBOSwKq0qmLQ010aGeBIC0mswUx02DpNGxt38qetCpr5X_Rt-oCFtQuw75nUE3kd-BwLQSRo8PY4B1lqv8HL_VC2RKRRwRWAG8xeK_wGJTCtx9H1-p4CwQCksTnD7lCm5hhuE9gRMBs5pzBfQpRBcQJV_fd_AiR7yWbT_mEOPOQtsWTM4yECGcKlc2edikY4cRRN7LGSVGS2HSoobEX65NCkj_tCR74vg5AqFQj4wZ5Rn64A_hzUBOdtJ5Me7IfEtpT9AqguO4p52pA5ti7PjeygymDLMusXEiS0FY7Mk_fVXOYeNC6Zf-JzwLT7YxoYlsr5dW2YoP9NQBCPYSUS-Dn2Ncz_DGjgB49MnHRnUy4-MMPc87VHok39aq2YO7iC9dXxZuVLjDdF6DWJaxPBCzCn731v4p-pvpJHVoIkr1adNHJQfGE1Ja_hbxflbFmcO8Wy88i0pgyo-pNElucWsDtwsqrbM6-5wv-sAhjInHEpEqn3ulzHuVb3g-qqubka0kiznw5IJ4p_acFAMeiMAtxkimfbM1NuRG9JtfrrDP416b8Tq-jB5BWtsFpZlWGyBZkKDIADyxgqBXP6D6sbUVteWrr5NVNWmT_P_4NbG5fkNKUdVolEqNaCRYGkw5wSifkD-VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015597adc5.mp4?token=dsTkVsN_kVFM5uBahU5W8CMWcCxZYDVM37j3aBOSwKq0qmLQ010aGeBIC0mswUx02DpNGxt38qetCpr5X_Rt-oCFtQuw75nUE3kd-BwLQSRo8PY4B1lqv8HL_VC2RKRRwRWAG8xeK_wGJTCtx9H1-p4CwQCksTnD7lCm5hhuE9gRMBs5pzBfQpRBcQJV_fd_AiR7yWbT_mEOPOQtsWTM4yECGcKlc2edikY4cRRN7LGSVGS2HSoobEX65NCkj_tCR74vg5AqFQj4wZ5Rn64A_hzUBOdtJ5Me7IfEtpT9AqguO4p52pA5ti7PjeygymDLMusXEiS0FY7Mk_fVXOYeNC6Zf-JzwLT7YxoYlsr5dW2YoP9NQBCPYSUS-Dn2Ncz_DGjgB49MnHRnUy4-MMPc87VHok39aq2YO7iC9dXxZuVLjDdF6DWJaxPBCzCn731v4p-pvpJHVoIkr1adNHJQfGE1Ja_hbxflbFmcO8Wy88i0pgyo-pNElucWsDtwsqrbM6-5wv-sAhjInHEpEqn3ulzHuVb3g-qqubka0kiznw5IJ4p_acFAMeiMAtxkimfbM1NuRG9JtfrrDP416b8Tq-jB5BWtsFpZlWGyBZkKDIADyxgqBXP6D6sbUVteWrr5NVNWmT_P_4NbG5fkNKUdVolEqNaCRYGkw5wSifkD-VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: مهم‌ترین مشکل گفت‌وگوها، پیام‌های متناقضی است که از سوی آمریکایی‌ها از طریق اظهارنظرها، مصاحبه‌ها و مواضع مختلف دریافت می‌کنیم
🔹
در موضوع تنگهٔ هرمز ما مقصر نیستیم. ما آغازگر این جنگ نبودیم؛ ما فقط از خود دفاع می‌کنیم و معتقدم حق کامل دفاع مشروع را داریم.
🔹
تنگه هرمز برای کشورهای دوست، بسته نیست. این محدودیت تنها برای دشمنان ما اعمال می‌شود.
🔹
کشتی‌های متعلق به کشورهای دوست و سایر کشورها فقط ملزم هستند عبور خود را با نیروهای نظامی ما هماهنگ کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/435687" target="_blank">📅 12:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1tGpOGoShdzqzEluGgLRnwVQzmBLr95DAyMjxzLRFsKH9nunLcjGPJwPZsX07P0rszzXAsnXNt0nhdepuPVI3C3XR5wXbrCcc_r1XSSgjtNQbrPl4Qojo7quntDL9RgdfO_UjqxGuDnHZg043xeDvg9Imkr7PPIiyIHSO-cP14ECuFrktLwDsGR9omXhsrvmORzbZV5L-9R0jo1rmgPCy8SsTvtiJiFCrhti9F5vRaAXLl8ybpSgpKiTJRqZVeAZlr_7WvJf6Q91TsFQIJASecaEFMud7gvqmUFKMmP5fy76-eAixoJWmaSbEFYM9t09a3TaZ5l886vnI7MvjR1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارچ به جای آب معدنی؛ دولت استفاده از PET را ممنوع کند
🔹
یک نهاد اندیشه‌ورز فعال در حوزهٔ اقتصاد پیشنهاد داد، مصرف وسایل و خوراکی‌های نیازمند PET (مواد اولیهٔ وسایل بسته‌بندی) در دولت ممنوع شود.
🔹
پیشتر یکی از پتروشیمی‌های تولیدکنندهٔ PET در اثر حملات ائتلاف آمریکایی-صهیونیستی تولید خود را متوقف کرده بود.
🔹
مادهٔ اولیهٔ PET در صنایع بسته‌بندی از جمله آب معدنی، نوشابه و... کاربرد دارد و بخش قابل توجهی از خوراکی‌ها در دولت مورد استفاده است. برای مثال می‌توان به‌جای آب معدنی در جلسات از پارچ و لیوان استفاده کرد‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435686" target="_blank">📅 12:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOmgwUmJ5pYvaA93NX_DdGTuMfGnpLUFEi74igFsK8D3NLBfVcxKa4rlhZbt2_N9T6BcaK1OpceokMQlUi_rCaocMm_1Ywukvb3HeTuugfBed_9egay_39QrfeHpgrJQUlRQm_GQhUkFDrRSNNgU-utkXD0A456SMfbFE7ifz6FIUaGD1dA1rCwtY5APGeipA-HisNiWRisnAl3csIC6BKcKhGocIoVc0ds7nTblr3Fa2gPToV8a4zbpbwKNkK1viFkV2pawhfPCGXdMo3EsXWpv0q8mxeX3CcV9QdiZGDe8uxUD5mQuSg9VxMINV5N2ZImAArBaymdCKAveU-m7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/435685" target="_blank">📅 12:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e4de8e0b.mp4?token=h9mzKpGk1e9hdtIBCQZ7yTPuqqMd_HryAQOpemsLfEk0tfA6Z7PH21PlbNmrzeiBLu1hGpe_rFK35STzW_zG7zeS0OR6KgncfaAYMth6Cpo1rOwc_QvR4aolrV0pSe33AIzYeyOzjQmWxsauLyXxkvPLfOdpkEFymUtKhQuyFgIU9t7S1Y1y8g7nz3AxiTSeIDCvif9NeHMVBzd-nXHVmuschdSdtIyPUxvoAYul6-_qYBcNM8Ggm8-DT5j9m9N3wzLvnWzX92BK3C7c9KlKeXhZAzyHw6-xoSe_iO9SkD7on-3abwmkEQrdv7WPtfp9hRLBImia77FliA0jVVHIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e4de8e0b.mp4?token=h9mzKpGk1e9hdtIBCQZ7yTPuqqMd_HryAQOpemsLfEk0tfA6Z7PH21PlbNmrzeiBLu1hGpe_rFK35STzW_zG7zeS0OR6KgncfaAYMth6Cpo1rOwc_QvR4aolrV0pSe33AIzYeyOzjQmWxsauLyXxkvPLfOdpkEFymUtKhQuyFgIU9t7S1Y1y8g7nz3AxiTSeIDCvif9NeHMVBzd-nXHVmuschdSdtIyPUxvoAYul6-_qYBcNM8Ggm8-DT5j9m9N3wzLvnWzX92BK3C7c9KlKeXhZAzyHw6-xoSe_iO9SkD7on-3abwmkEQrdv7WPtfp9hRLBImia77FliA0jVVHIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی: انبار سلاح گروه‌های ضدایرانی ساکن اربیل عراق هدف حملهٔ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/435684" target="_blank">📅 11:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfhiMSEHiqT5Q4Des8j_MYDNKX8byAAT4UCiTuW8srFST_7isJ_MHkgi_2PzSShteQgWz3AuRw4wRZv-mA0YnuSAUwKY0EW0HQuPRjfgpZEddPe-kAM0BhCPulVbUdDjOdORfXdDNVMiRfDdZEzarMEGo7YlH-HQCFbHgs3ued7xKsjW5dxjj6Dtsa0Rvp3YllYSd1_dtHtBc72t-9PceBlYCCYMfFgVPAD_lTRBFKlpd3-7MLdB93GIiChVZqPu0Y7fC3qUQyGfIKRKTpzDc5F_bEq0houCUTDbv5WT1QjZ5yfuZmXhlQdgcGf5uY6QdVXfRl1_g8xNXKbLqyYuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پارلمان لبنان: به مذاکرات دولت لبنان با صهیونیست‌ها بدبین هستم
🔹
موضع ما همسو با مذاکرات غیرمستقیم برای دستیابی به توافق واقعی آتش‌بس است اما باید پرسید اکنون اساسا آتش‌بسی وجود دارد؟ رژیم صهیونیستی به توافق اکتبر ۲۰۲۴میلادی هم پایبند نبود.
🔹
من نسبت به این مذاکرات بدبین هستم، من موافق مذاکرات مستقیم نیستم و اکنون صحبت نمی‌کنم؛ اما وقتی تمام شد حرف‌هایی در این‌باره خواهم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/435683" target="_blank">📅 11:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjWYBg15ysnBKG5V4SHRKLD3XazF1_z50WPR48AVbhKbcJnyOMAZIfR3ZgUzfM8crnLL05ZdRWifvGqy6d7KEjPHdP29n4jJ4vc_j3kRranb9W_ccPVGeFuebexQMVtZowPbx1P-L7XtxxtU0iypwKxqfkEd8g1kEFch3LOyciKDNM4qKglXQKCS5NsZiLcoFEBOQE6x9RP6UCBgtrUroz5yeiKqz4x7FKuYz80REDj9-peoBsSps3ncMTCQJINQLKeN2y5Cyi96Vot3fzeAFdCegB_FHEntf7eX0u1jihLz-zjNyubLxzmJlF7ptfk99tJUPTpcXMFYaKxr3iDnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل هم به امارات سفر کرده است
🔹
سازمان رادیو و تلویزیون اسرائیل اعلام کرد که «ایال زمیر»، رئیس ستاد ارتش رژیم طی ایام جنگ علیه ایران به صورت محرمانه به امارات سفر کرده است.
🔹
رادیو و تلویزیون اسرائیل افزود که زمیر در این سفر با مسئولان بلندپایه اماراتی از جمله «محمد بن زاید»، رئیس این کشور دیدار و گفت‌وگو کرده است.
🔹
این رسانه عبری افزود که مسئولان بلندپایه ارتش رژیم صهیونیستی زمیر را در این سفر به امارات همراهی کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/435682" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRoKo98U21iJbmPUGhC1t7jSSxPEA9T0a_vwWK2tl2TxD0Azpyzg2iDics8uHbr1dByJimY7fcRCMQon1M4NliqacMmecRWeIxtkQ3cSJZRfcw7U7Qa3HSqnSqWalHI0o3idHpXkHA6RhFGenEd4LuG6cqGsRceQqTVR7HChiQrxdtmsDujNCZNHJRXgxoak_IfeNKaIl0ZNFZJM9UDHVj4C9zQXSBWxByHLcTycbmi_Y69lKXApOsRii1uBl6OOVMWaBJNYG8329803snJrTdtTXtIv3X6fkWi20i3VlZ3MYteLKLMTBbwH7rGYsnr5Zww0LaH-gAoyAcyEK-MhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: مردم مطمئن باشند تا آخرین قطرهٔ خون پای کار هستیم
🔹
فرمانده‌کل ارتش: آنچه موجب اطمینان ما به پیروزی و توانمندی می‌شود، ایمان و اعتقاد است؛ این ریشهٔ عمیق در ایران اسلامی دارد و هر سال در دههٔ محرم، شاهد یک مانور عظیم ایمانی هستیم. قدرت اصلی ما نیز همین قدرت ایمانی است.
🔹
این قدرت ایمانی است که می‌تواند یک جنگندهٔ اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، درحالی‌که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند، مأموریت خود را انجام دهد و با آرامش کامل بازگردد.
🔹
این قدرت ایمان است که می‌تواند دشمن را چنان دچار آشفتگی کند که حتی به اشتباه، هواپیماهای خودی را هدف قرار دهد.
🔹
در غیر این صورت، اساساً قابل مقایسه نیست که یک اف-۵ را با جنگنده‌هایی مانند اف-۳۵ و اف-۱۵ مقایسه کنیم.
🔹
مسئلهٔ مرگ برای رزمندگان ما حل شده است؛ ما برای پیروزی می‌جنگیم، اما شهادت را نیز فیضی عظیم می‌دانیم؛ همان‌گونه که حضرت امام خمینی(ره) فرمودند، چه شهادت و چه پیروزی، در هر صورت ما پیروز هستیم.
🔹
در پرتو تربیت دینی در ارتش جمهوری اسلامی ایران و مجموعهٔ نیروهای مسلح، این مأموریت بزرگ به‌خوبی درک شده و اهمیت آن برای ما روشن است.
🔹
ما به مردم عزیز ایران اطمینان می‌دهیم که با تمام وجود، تا آخرین قطرهٔ خون و ان‌شاءالله تا تحقق پیروزی کامل، به این مأموریت مقدس ادامه خواهیم داد.
🔹
نیروهای مسلح با تمام قوا از تمامیت ارضی، استقلال کشور و نظام جمهوری اسلامی ایران پاسداری خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/435681" target="_blank">📅 11:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/435680" target="_blank">📅 11:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXA6gdtOHGUm6ah-LsUC1vrvIXMVrt-Sv_QMsEwF5jha9qWfM4b6Xspv0sFHNt-mcxSUoCnIjzstKZMqMnLW2MIRzX9ZICzVc1jOWIzrluJEGHgTOKqeF1Tq3199I40VU2ZiisHRJmhVkjGCReCmsljGNKtEDK8fMeU4xAgtGm1UmU9c3AWo0ZxPcbNLyWwYJ7FIJmS4DRbguvpNa1cOCE0Vjf6ot7jqt4Jmwfns7NBqv8cmoFd4fQUF_M3vmBVnbV5wDCGqLYNhN8Ges0w8AJ0GyjQwT198b99UfRh2lDSaqkr1ikApgUkU_GPWd9uhxdSqH_Yv5Mf0TP6LYV8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر ساعت آغاز سرویس‌دهی خط ۵ مترو تهران
🔹
شرکت بهره‌برداری متروی تهران: با توجه به تغییر ساعات کاری دستگاه‌های اجرایی از ساعت ۷ تا ۱۳، حرکت قطارها شنبه تا چهارشنبه از ساعت ۵ صبح آغاز می‌شود.
🔹
همچنین این خط در روزهای پنجشنبه از ساعت ۵:۳۰ صبح و در روزهای جمعه از ساعت ۶ صبح آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/435679" target="_blank">📅 11:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYSrQxNtZ_1DFNnaHZItzUU4ZEFFvTU7v8p1O_rN0h7I-Ag-233D8PTV4LHg0jgjMEnWkf5qusMI9eMJfMITQTvR_gRiCRm0Prf8xlk22LPSEdFCWgyugNyswRTCRVHRNaL61wNG4oPfu19HpH9GMIumjtFmx020PSm5fG7KV5ScDQZAFx93qrd_MlKfDHyR2tRw7Ur_Vjzk1io2Qv5rv4c8k2c0gr5HvMaIoF-I6ZRo6i5MdQnP49KQGN_hLmzY3QdFgRL_Gg8q5LpFm4SEirPeAFMi5p8xrh7zUVWH5SYOfL6iGi8A-Z4CsR0WX-A-rJF5y8vw1hfkwZQPI49cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجهٔ روسیه: جنگ علیه ایران باید فوراً تمام شود
🔹
وظیفهٔ اصلی درحال‌حاضر در رابطه با ایران، پایان‌دادن فوری به جنگ و دستیابی به یک توافق پایدار است.
🔹
وضعیت خاورمیانه و شمال آفریقا به‌دلیل مداخلهٔ نظامی و سیاسی غرب به‌طور فزاینده‌ای پیچیده شده است. ضروری است که هیچ مشکل یا مانعی در تنگهٔ هرمز وجود نداشته باشد.
🔹
برای رسیدگی به بحران مربوط به ایران، باید علت اصلی بحران را که تجاوز ناموجه آمریکا و اسرائیل است، درک کنیم.
🔹
ایران بحران تنگهٔ هرمز را ایجاد نکرده است؛ منافع آمریکا کاملاً بر نفت و بازگشایی تنگهٔ هرمز در شرایط پیرامون ایران متمرکز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435678" target="_blank">📅 11:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۸ پلیس پاکستان در مرز افغانستان کشته شدند
🔹
در پی حملهٔ انتحاری در منطقهٔ باجور پاکستان، دست‌کم ۸ نفر از نیروهای ارتش پاکستان کشته شدند.
🔹
مقامات پاکستان اعلام کردند که این حمله در خاک افغانستان طراحی شده، اما طالبان گفته است که این موضوع صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/435677" target="_blank">📅 11:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfETNN2f4gYr75brpmmU9flu_X93if_iT6kkTwjEkePsDOX8JLfoMbdqu6D9KiGZi1frdqkaPg2ecmvKQJ1jsF21tl2VvmICGki6_RCwsrcz_PXHTOKvuTyz8GnQxAE8AykP9bdMKfzkGGh_83L-WDts6QmpGo9pgorifdTiJyavcwCIAc_yfmjp20XvbkIJtK_UOJxjAJxP8rtiEmUYkGxPyE7RkaFb4CdpE-kgYHCZO40JojXVGYylME0likXYBfICpEVucXerYm12hkGelnWwwE3Tr5SLoRK_EWXIXgRna-hGFuZvnBeYXQ2n4npVgzYKnSqUuoPPXA0iaRnyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین و کم‌فروش‌ترین خودروهای بازار ایران را بشناسید
🔹
طبق گزارش مرکز پژوهش‌ مجلس، خانوادٔه پژو و سورن پرفروش‌ترین خودروهای ایران در نیمٔه اول سال ۱۴۰۴ بود.
🔹
همچنین خودروهای وارداتی نظیر X33 در فهرست‌کم‌فروش‌ترین خودروهای ایران هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/435676" target="_blank">📅 11:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCA8xCJenCNkqDwQ7V1hNF67qT3A__rs4xHwkB90SEqh1xyEw4hyRFtuchbN0xzGZqz2nfVSp1YBNOPkvDG67T4rY8G6BiNLKHIbj_NeDHVbg60jNXL13yRsa87QzqCYeEMUJ-ISqQhetoMzqixbzV_w-HPe2uEHclD91R-XXdcJ3XzR0WBdM4asuAWQRvkA9DkYaA9-avSfjzx__QV_6djMfeRSTzA_-hvX_eZ7qnTmXUjqLd2bX4sGwcVnlZThjAuHCbMWFLB9fKOiKk6715Vaq5dWD6JNl9zpvfCS94KHeN7YsJ5JqcxHtEG7Aq0HJ0bod5b1ZGAKceuZGsRQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین هم چند روز دیگر به چین می‌رود
🔹
منابع خبری به روزنامهٔ «ساوت چاینا مورنینگ پست» گفتند که انتظار می‌رود رئیس‌جمهور روسیه اواخر هفتهٔ آینده، در ۲۰ می (۳۰ اردیبهشت) سفری یک‌روزه به پکن خواهد داشت.
📌
این اولین‌بار خواهد بود که چین میزبان رهبران ۲ قدرت بزرگ در یک ماه، خارج از یک نشست چندجانبه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/435675" target="_blank">📅 11:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4D9zYb106VFMzj7R-qZUreVWSjzCF-3_3arVFSt2QquNX60gDChAXl-_CC3VU66mpU_IMEnPXLS0T6lMJencUyzzGvzq5X1y0eQAwppBevs_sw68dTU-Fu7nnz4rnZVlI5VPgFybfyQ2iMxG-YMZeJvWzUv4CIdZ8XIszIWe6A6GTOdke0lMsp1W5gt1AbRXXsFFk3KQrjL5SYF0pvYHMJJjPajYimrTwFntcnpn20jPi5BYabnd9n4Dn6Y__B6GWOyOh1cBogOujAy6JwY9BBJmiCnGYytu3J_15FjnJo-GFW4ylijQM3ntF2aFAZCryGLwYxHFfOwk8r61nrZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تامین سرمایهٔ در گردش واحدهای تولیدی از خردادماه
🔹
رحیمی، مشاور معاون اقتصادی وزیر اقتصاد: اولویت ما برای آینده، تامین سرمایه در گردش و حفظ اشتغال و نیرو است.
🔹
با تامین تسهیلات حفظ اشتغال بنگاه‌های تولید، در گام بعدی، وام برای تامین سرمایه در گردش واحدهای تولیدی است؛ این وام برای سرمایه در گردش بنگاهها منهای حقوق کارگران پرداخت می‌شود که از اول خرداد اجرایی خواهد شد.
🔹
در این طرح معادل ۱۰ درصد از میزان فروش سال ۱۴۰۳ که در سال ۱۴۰۴ حسابرسی شده را به‌عنوان سرمایه در گردش به بنگاه می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/435674" target="_blank">📅 10:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شکار یک مرکاوا و ۲ بلدوزر نظامی اسرائیلی توسط حزب‌الله
🔹
حزب‌الله از بامداد امروز در ۵ عملیات خود، علاوه‌بر هدف گرفتن نظامیان صهیونیست، از انهدام یک دستگاه تانک مرکاوا و ۲ بلدوزر ارتش اشغالگر در جنوب لبنان خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/435673" target="_blank">📅 10:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsPzGMl8RGvg6wppHQqpXJud9tXBxnT2cXq_s2uAj0n-JX4SY6oSd4WGeRMiGrYpbTRuKVNTEzGU2wyAT_0a6SfSmY4F4qejJNUO8VA2pX7ynALcD6RjMq3uz7aclT-Ao8ZvlCa0aoQn9monIoSE_1jAgf4LkU9aT3RB2J4RtuuIWj8w-me1_HwA3xKMSfVLntRrsGPIQ0xbFIf2tpGi1tO2zyMj2P3WVpN5oCXPjGrI3WNPb3idLnn8_s00-vQRf6HVgQ6CGIOBX8Pam_Zhby0HlpjG6mZegfb8RFt_kx28HyLL-6MuF-s4dcz8H8LvnnEhWngHPvA6s9buW66I9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان ایران با نام «ماکان نصیری» راهی المپیک می‌شوند
🔹
کمیتهٔ ملی المپیک تصمیم گرفت کاروان اعزامی ایران به المپیک نوجوانان ۲۰۲۶ داکار را به نام «ماکان نصیری» مزین کند.
🔸
ماکان نصیری دانش‌آموز کلاس اولی مدرسهٔ میناب است که در حملهٔ آمریکا جاویدالاثر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/435672" target="_blank">📅 10:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بورس آمادهٔ بازگشایی شد
🔹
سازمان بورس: آمادگی برای بازگشایی بازار سهام از اواسط هفتهٔ آینده وجود دارد. زمان دقیق بازگشایی بازار به‌زودی اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/435671" target="_blank">📅 10:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4a7ed75.mp4?token=GCBpxYk_6QfAN9NzmZ3UGIs_7tO9E5xc5RpsYps5STDM24Hz8QmY8G6JOfLld_sGqbhpj2tANFoiRwcN2QGSaeHgrtuSmEpXgnpgIutTny8ZbKgLi3kwouwlnfZTWew-VpPc2ZVF9ZFyvhKKPaivA7J2rJvHf7AgOWtHCEOJDYVT4Rk2piy6i9Z9-3JD1z9tAw_iqQfTelKubwu5bXs9-r1s3lrlQFbAR56R4XJ9Eoy2gM3JciP6IDbOD5LyXzW6OzegHTj38kOZbzVAyURrlnSijDU9APZXvKL8LJmL3pXOwVitO_MDQDuNrtQa4RU3T0OlDiFyjrIDGTuLgA8ngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4a7ed75.mp4?token=GCBpxYk_6QfAN9NzmZ3UGIs_7tO9E5xc5RpsYps5STDM24Hz8QmY8G6JOfLld_sGqbhpj2tANFoiRwcN2QGSaeHgrtuSmEpXgnpgIutTny8ZbKgLi3kwouwlnfZTWew-VpPc2ZVF9ZFyvhKKPaivA7J2rJvHf7AgOWtHCEOJDYVT4Rk2piy6i9Z9-3JD1z9tAw_iqQfTelKubwu5bXs9-r1s3lrlQFbAR56R4XJ9Eoy2gM3JciP6IDbOD5LyXzW6OzegHTj38kOZbzVAyURrlnSijDU9APZXvKL8LJmL3pXOwVitO_MDQDuNrtQa4RU3T0OlDiFyjrIDGTuLgA8ngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ پس از پایان سفر به چین، راهی آمریکا شد
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/435670" target="_blank">📅 10:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX8yTp-jJlvKqsybwjcVXDptHtvyUAs-62JKQzI_jfsYlzWeE9DWgutrqwqIi6KDn75RG2LVQh-VZA8eVTFZiyc79nY0pzskhFaQWJLq_zWKgfp7mLRq_cP-0PL6UdaKfN9_91A6pILN6iB-pCmToEJJfL6HNDkMHMI1IEHOQFsV4CXiYIdsHMZRHBapGInIYAGJp5T8A4BElGDrQrtAGT1wDY6RNHWcuKjmWQfy3DaObPVdFwrpoKTThJvBMvxNM2rlqos56pFWNOALak62uxfZYsG6hIEsjkjGN3Icrs1B17KD2uTkJUttz8z_mz_qF_SNl_iWXjnJeGfbG9hIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت امارات از افشاگری دفتر نتانیاهو
🔹
شبکه i24NEWS رژیم صهیونیستی گزارش داد پس از آنکه دفتر نتانیاهو سفر وی به ابوظبی در ماه مارس را رسانه‌ای کرد، امارات پیام اعتراضی شدیدی به اسرائیل ارسال کرد.
🔹
این شبکه افزود که اماراتی‌ها بسیار خشمگین هستند و این اولین بار نیست که چنین افشاگری‌هایی از دفتر نتانیاهو منتشر می‌شود.
🔹
این رسانه به نقل از منبعی مطلع تصریح کرد افشاگری‌های دفتر نتانیاهو دقیقاً دلیل عدم دعوت از وی برای سفر به امارات طی سال‌های اخیر است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/435669" target="_blank">📅 10:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnLaOw_VkDBhRZSC5yz2t-8BM9NW9L3AMlAZii1ulahZWXS18hoVToDQ49ieRKs0fshimAyESuFVWD_joqmQfl8CKMUiKnuR0OHI70I63R96ODdWg2B8AhIOfNX-9GT_oR5yt1pSuQtvMTjUW5XbmzmBeAFrPGbOoLVbZK0AarWI2XK8ViSykcS7MIsmbX3fAh3KxqjEW2A23EBSgskgdx-49qtKtVicAZYQoTaWNnlIF8fwL3ZWw8aiN6bRI4KjvDMhEF66LWH_Bxv9oHKdiTw1SnpGfHdxvhEQA36lfp3ukg8RzIseX83WqGkeV2Iy2wPLDJfd7bBVXM_r4l1eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ۷۰ درصد آمریکایی‌ها عملکرد اقتصادی ترامپ را فاجعه می‌دانند
🔹
سی‌ان‌ان نوشت: در عصر سیاسی حاضر نادر است که ۷۰ درصد آمریکایی‌ها بر سر هر چیزی توافق داشته باشند؛ اما درحال‌حاضر، طبق نظرسنجی جدید ما، ۷۰ درصد آمریکایی‌ها موافق‌اند که ترامپ عملکرد بدی در حوزهٔ اقتصاد داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/435668" target="_blank">📅 10:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws42vGbgKxyigTnNsCOdOJs7WSL764B6BO9H6PabLRjGM4J0YARJAPhYrlBxMbkevyP7i8wXZpS7jpwt8E5ebTccsrZKkEgRNyBmG-g0kEnEC0xqWm7aXbSxrbpooC3LQeaKKbOsXmcetGwD6BMNI02WXhyiNJxGFR8MrKZlDB3OyWKqFHXGNEnRLTh1FLnJJu8KZiXsrkYVAHiC7eTb9MwOZGLOzJlx5w3G9jSdARw3o4-QsSvpjNzl9mErJHFxrGTPbKje6vHR5xyiVnsVav1jXi2kgeOAOUM3QFhWVed1-TyuzVsAbbYBKYfqnfuAA6NOTjBBCC0pf6vJvrXxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اصلاح شورای امنیت یک انتخاب نیست، ضرورت است
🔹
ما دنبال شورایی هستیم که نمایندگی واقعی از تمام قاره‌ها و مناطق جهان داشته باشد. بیایید از ظرفیت‌های بریکس برای بازسازی حکمرانی جهانی و بازگرداندن اعتبار به چندجانبه‌گرایی استفاده کنیم.
🔹
جهان امروز شاهد…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/435665" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL1ric5Zss32E04vVlAQUdFg9FVGDx2bONzZQ9S10G7t9abJezw0LPXoW2X6eTGn7BLsvBQX_aAVyD3CSHbwdbhpynUuNQbQLRXON-OdcanZCRD5tEhlJU08ekcwo_MoqfM1KJBAipZSPQDf64-yYzEz1CcQJsZeE3equb8ELQpsl7ROVo4cq2sgDDwsCf27CP4ClKyHr09wo85-mEpmwrOy9xMj5b6Ce7E0W-D2zXiQ_H9K8ZvSdJ-ZqNNISvWlywpt7FpWsUaRI5slN5ZbhY9M_JuOqbkEb7LIIZes88zNCWpEyd0UeHQiOcgNd-uKK-nnw2GutgkR1-YaE_a_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: ادعاهای آمریکا دربارهٔ مواضع چین علیه ایران کذب است
🔹
شبکهٔ المیادین به‌نقل از منابع دیپلماتیک: ادعاهای مقامات آمریکایی دربارهٔ تغییر مواضع چین درخصوص برنامهٔ هسته‌ای ایران یا تنگهٔ هرمز که پس از سفر ترامپ به پکن مطرح می‌شود بی‌پایه و اساس و کذب است.
🔹
موضع چین دربارهٔ ایران واضح و ثابت است و تغییر نیافته و چین روز گذشته از بحث درخصوص این موضوع کاملا خودداری کرد و هرگونه ادعایی خلاف این، نادرست است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/435664" target="_blank">📅 09:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNtxyXW1vcXCBCMbfC0nrg3l9oYuJzg-b9WxV8YnVSW-_hDSh2Cii6HlR51qA6mw-EaW1yhgV-XQQQljYpURx9kQAFsEiuuIP5f3HEhvxGuksMxGOnnzRscTIA4gzHXMqZnGHc5BaVgFefCGLIEmLfMQgZ89I3OFN3PN6L-iujpVB5vBtZ8FiAM-jK4MD9jSIFmrZxizOix_xge1sLdKIF0bASgx8KARsSH-OkLsGF0vuylZHqq9gvbcMISoXiTusP6rS3G8i-LM5nJXKorr-0wHXzRw49HY9Ibu3yQsA3PwfnQ7h-74PmEt_8W8cOuM9fqPfVIsqqkz_35oKHME8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاچاقچی‌ها بخشی از گازوئیل صنعت را تامین می‌کنند
🔹
اطلاعات رسیده از وزارت صمت نشان می‌دهد، سال گذشته صنایع مجبور شدند ۶۰۰ میلیون لیتر گازوئیل مورد نیاز خود را از شبکهٔ قاچاق تامین کنند.
🔹
سال قبل نرخ گازوئیل قاچاق در مناطقی تا ۱۵ هزار تومان نیز بالا رفته بود.به عبارت دیگر کمبود تامین گازوئیل صنعت سبب شده تا ۹ هزار میلیارد تومان از بخش تولید به جیب قاچاقچی‌ها برود.
🔹
در سال ۱۴۰۴، ۳.۹ میلیارد لیتر از تقاضای بخش صنعت توسط زیرمجموعهٔ وزارت نفت تاییدیه گرفته اما تنها ۳.۳ میلیارد لیتر این میزان تامین شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/435663" target="_blank">📅 09:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435661">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tiu75NY8FX_h0nyrW-OcOIFDoaAHmEf_vNoN5xl3AdBzlLtTN8Jua8uezLKhD3OV-z0H5-FaHLcTeS1L-sVQdVMFGnN-iH2FFHDACbBTZHVG1f0Yiv8a_UcZb3Vi1ZN3g8AjwtLjDZkfmYFZldO9P2hKji8KynlkZnNZa7wM5B-Sh_DazZKg8djskB4ddsknlIUT69CAer1oMB2kObC_AbAOGKq9d7N0S05XKjui5SlnX7KJXA43ss846IRu2OlhOLExd8zcmYAy3KbsFFNRl7KZI-x8EWEwNoHYquKh4zOv-j3tdCYgxS84tLnfkgQREDZwCjQHhZcGnc9qU5iXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGirWsCO-2IMOlrVgB5PbOKwDtDj6Y5R8uJpeMfOLpEUv-lo4BnsFYdlsPeuzDS3y2Kck8W3JsxbtrGWiuuEnXF9XiU8Yf_bxKQonJiRbMZhJBDkpoCnvO1ALObaVCVxaoOj9syQzKxGCHTIK9qXwNt2CGOOuperYvkr1QrhKyN2OvFTqqRDulRH1C-BDZ5FXcLoNoTgFKoaHVwugbKAzV9yFyyhKyFfqjODNFqvpyywiI7TJ1uJaSf4cCbdtE4rgRrisUH3BiUNMwzYTJ8sl6P5uEGuXnlt1ilWLcw__4HBUblS_qe8p26UXVEy4DnBmVn93F_J8AZDuxrx246QCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی و وزیر امور خارجهٔ آفریقای جنوبی در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435661" target="_blank">📅 09:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435660">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhkUZBWUPO89JvqdCwjvy5LOjEGIigUGaprtT21FoIN1iaDUUf3lZpZF280S0D7V5yTqqoHzhMa1yGIKGN3uBwdi5IZ2kG58nwSN_C1WsENxsLoPqiyXkEmBxkKIp-voWxkWdahujbe72QITVidhVBJRRrX_F5D95ACR19mRktaJQ5RbrJPyHz3xZYWD8ThkDCLrIOmGRSQv7dnD22u6iyLDEo09yHD7hDWkf2P8nw8s3AJizS_FUVeHORAih0mTwNecPsxoyYZndFzXNcZIL8msIWTCuLtp441h3yj116GeP2s-HxThR6ND50IepPYLzenDeGAbH_IsQivyEqZVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اصلاح شورای امنیت یک انتخاب نیست، ضرورت است
🔹
ما دنبال شورایی هستیم که نمایندگی واقعی از تمام قاره‌ها و مناطق جهان داشته باشد. بیایید از ظرفیت‌های بریکس برای بازسازی حکمرانی جهانی و بازگرداندن اعتبار به چندجانبه‌گرایی استفاده کنیم.
🔹
جهان امروز شاهد بازگشت به دوران جنگ‌های بی‌پایان، خشونت عریان و یکجانبه‌گرایی افراطی است.
🔹
کاربرد حقوق بین‌الملل، حقوق بشر دوستانه و منشور ملل متحد از سوی متجاوزان قدرتمند، به لفظی و دروغی برای توجیه جنگ و اشغالگری تقلیل یافته است.
🔹
از این رو، ایران بر ضرورت اصلاحات بنیادین در سازمان‌های بین‌المللی، به‌ویژه شورای امنیت، تأکید دارد. اصلاحات مورد نظر ما، اصلاحاتی برای «توزیع عادلانه قدرت» است، نه صرفاً تغییر در نام یا ترکیب اعضا.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/435660" target="_blank">📅 09:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXHeRv9fnMK0zsEofRSAh8PIA5g_BnV-GUGoD7B7vD_X7-jJJ4hzNSstpjtmXkoGs_Wt71tc0pTfTeah3UIB5FqiB6mmJEiOUbx5I_rtLl5mSOSP6VPFlFnlwE9jM5Zno3Rzjz51McYh9zsLW-A0DCClI-7Mns26ea8rXf67DDof9ZpapbZ6zA54AHZ0ypfZhfxPZkHaDuCRzLbjDoGsU35Je1qavpjs-_lZfl140y6BBYLoUEVMuqusbNLyFi3rkjdb17ZjnBrEgrn4fbkoU1G_QsSINH40t2DoQOToaSCJcVoaWQN-siZVDgT6W0K-WAZFuBV8Xrr_rrJPZ0teqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط جدید دولت برای متقاضیان یورو با کارت ملی
🔹
مرکز اطلاعات مالی وزارت اقتصاد، ثبت مشخصات دریافت‌کننده، هدف دریافت ارز و محل و نحوهٔ هزینه‌کرد وجوه نقدی درخواستی برای متقاضیان دریافت ارز با کارت ملی را اجباری کرد.
🔹
بر این اساس، بانک‌ها و صرافی‌های مجاز موظف‌اند اطلاعات دریافت‌شده را در سامانه‌های مربوط ثبت کرده و سوابق معاملات ارزی را مطابق الزامات نظارتی نگهداری کنند.
🔹
بانک مرکزی به‌تازگی اعلام کرده به همه متقاضیان بالای ۱۸ سال در هر سال، معادل ۱۰۰۰ یورو با کارت ملی خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/435659" target="_blank">📅 09:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999bea2fda.mp4?token=W7_1f5BoP9ye9193GnRmCtOWCsDfE0ZACelOO56T5YZIySpi4zhIwfjoPE9CQ6jF02yo7Cr84SriqMnMttFdV28Xa5N35RXiCHWHnzdIEzf2o3ZDj7_u5Ae2udefiI-JChhqFtoYyWugFzyduwGUvwC6V5A-USufwSTLwmtgjan_BMNj5vVHhpRDCHa-ZpV--H8XD5WRZCgbfG7LudQeVHRCOXr8y2fmOyTJmlR_ec-3ggkdWu-_Z4pXLAAzpFqSPTjhFZIkym8nzyxXDDLa_X8b4EvjzV8cKy_weMS5FsEeIqWMlt2c_W5lAT_bCoUDljXjED1KspDvTe8qGk9K3whtGPlaBBN5Kp7_hchHAw-06fkOJbcDYPPkRoFNthXQZ_gUMZXWMF2rMABUGyItJ9VaTbYxQBfCp1kifPgFZ8LkgvadqaduMF6dJ6s3BvbzXlrDnqPjfA_qCXdeQGAjzVHw0JuaPgc8DKd9yb1wERdlnl1UayBbq-ZTz-de3ncSuBiyNvBE7Kila1Ez4qGyXwnHxHIbhdBG75ogbt367-Htw-mJU3SukRisnDWQubfFHUhIXFxudJuk-7TQqBh1dEyzvhWNNa2cxnqXcWMd5ByF8zDTAxCFnexp6HJ2AFX_M08Oj0LGixEkmJkfX7_IwNYtRBr6P-8fgqIs02OcvKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999bea2fda.mp4?token=W7_1f5BoP9ye9193GnRmCtOWCsDfE0ZACelOO56T5YZIySpi4zhIwfjoPE9CQ6jF02yo7Cr84SriqMnMttFdV28Xa5N35RXiCHWHnzdIEzf2o3ZDj7_u5Ae2udefiI-JChhqFtoYyWugFzyduwGUvwC6V5A-USufwSTLwmtgjan_BMNj5vVHhpRDCHa-ZpV--H8XD5WRZCgbfG7LudQeVHRCOXr8y2fmOyTJmlR_ec-3ggkdWu-_Z4pXLAAzpFqSPTjhFZIkym8nzyxXDDLa_X8b4EvjzV8cKy_weMS5FsEeIqWMlt2c_W5lAT_bCoUDljXjED1KspDvTe8qGk9K3whtGPlaBBN5Kp7_hchHAw-06fkOJbcDYPPkRoFNthXQZ_gUMZXWMF2rMABUGyItJ9VaTbYxQBfCp1kifPgFZ8LkgvadqaduMF6dJ6s3BvbzXlrDnqPjfA_qCXdeQGAjzVHw0JuaPgc8DKd9yb1wERdlnl1UayBbq-ZTz-de3ncSuBiyNvBE7Kila1Ez4qGyXwnHxHIbhdBG75ogbt367-Htw-mJU3SukRisnDWQubfFHUhIXFxudJuk-7TQqBh1dEyzvhWNNa2cxnqXcWMd5ByF8zDTAxCFnexp6HJ2AFX_M08Oj0LGixEkmJkfX7_IwNYtRBr6P-8fgqIs02OcvKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: کشورهای بریکس پس از ناکامی آمریکا در مقابل ایران، به ما با چشم دیگری می‌نگرند.
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/435658" target="_blank">📅 09:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
سخنگوی ارتش رژیم صهیونیستی از هلاکت یک سرباز صهیونیست در درگیری با حزب‌الله خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/435657" target="_blank">📅 08:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435655">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecf055bf9.mp4?token=hywEkDSc_IE8AOYR6zZm2N8ONjrC4aZVfhG8h2ssol_R-iYPs26J7gsgINHQrvwyzEKV1-mwCUQFVs3EJ6hFTLM6xSIvC9JHaaee9nFfzITYBhf4t9dY4A-0gPnfrn5IcdNHCwQp5v2Hm65EwOPBgmEOAq_t6pUBlzJ_VrOOM9Av1MZxNWBQiALGkOUVFwFYFPpveKdOh0QNretC9C7SFv4GckSRvMSz-nLv2ZDgbVooqFEkYGXEUzKuFi4McVuvYq56Ur4v4Az6bypAlpNOQklsNonhudRqlX1ykn77hNCfIhzt8sS8353ChniPOliNt8yjPXMN5iewqa16XuhqqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecf055bf9.mp4?token=hywEkDSc_IE8AOYR6zZm2N8ONjrC4aZVfhG8h2ssol_R-iYPs26J7gsgINHQrvwyzEKV1-mwCUQFVs3EJ6hFTLM6xSIvC9JHaaee9nFfzITYBhf4t9dY4A-0gPnfrn5IcdNHCwQp5v2Hm65EwOPBgmEOAq_t6pUBlzJ_VrOOM9Av1MZxNWBQiALGkOUVFwFYFPpveKdOh0QNretC9C7SFv4GckSRvMSz-nLv2ZDgbVooqFEkYGXEUzKuFi4McVuvYq56Ur4v4Az6bypAlpNOQklsNonhudRqlX1ykn77hNCfIhzt8sS8353ChniPOliNt8yjPXMN5iewqa16XuhqqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: در مورد ایران، درخواستی از چین نداشتیم
🔹
ترامپ هیچ درخواستی از رئیس‌جمهور چین نکرد. منظورم این است که ما در مورد ایران به‌دنبال کمک چین نیستیم؛ ما نیازی به کمک آن‌ها نداریم.
🔹
ما مسئله را بازگو می‌کنیم تا موضع خود را به‌روشنی تبیین و آن…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/435655" target="_blank">📅 08:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435654">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=HPwz0qR-FhiflpyIbiyCcFYfepGCm7sypy_Land1kdgku4TvcQW0CGMWW3m2ZlNqvF1JKJRrRY5XQsiNisw8uM86-OkWQp79DP7cB44GlOG0oiHlEADN7TjpArg7oziCej5ZLgOFDMyiV75-Zk8cp8CQD1fBUs2nGFgwg8k6n2porRFIPW_87UaseglPlFDhrII78ITdfg2lil06kPuJgAbXuhvD4bc7znkYhDo-Eiis7EmLK_mlimXAuWuZb7PhnieZq-e0MiIeesagcs7WnZVy84Y6A2-kWDfvJcD8oj1pLPUS4DC30It3xil3aoMoH8hquYki1uxtwi0iVQ7PXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=HPwz0qR-FhiflpyIbiyCcFYfepGCm7sypy_Land1kdgku4TvcQW0CGMWW3m2ZlNqvF1JKJRrRY5XQsiNisw8uM86-OkWQp79DP7cB44GlOG0oiHlEADN7TjpArg7oziCej5ZLgOFDMyiV75-Zk8cp8CQD1fBUs2nGFgwg8k6n2porRFIPW_87UaseglPlFDhrII78ITdfg2lil06kPuJgAbXuhvD4bc7znkYhDo-Eiis7EmLK_mlimXAuWuZb7PhnieZq-e0MiIeesagcs7WnZVy84Y6A2-kWDfvJcD8oj1pLPUS4DC30It3xil3aoMoH8hquYki1uxtwi0iVQ7PXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/435654" target="_blank">📅 08:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435653">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5790d0b.mp4?token=Kox4G_oiRt9tpLyi3O8TMLN18_Fe6FvluBL5ngoFi30xnCrsbWzHaXz2dg8AjFKr6HZNTF_mQbHrarlkCY4sGOACHqb11PrM0xXyelkXY--EMnswYIV3zD2HaS65enlGj9unPCaaNm9P2oZYOyMMbX1eSuNmm2I2kM6hJEV9YePWR48tsmBTHiCZVIC-qPTEoZRiequrnU1jxxm2ZQuHWviIueZ2stS6LNwO1jAlFuEcbugmM8YrcuQqfRuoGLuPPLML47wkQ953tE21EvGm8ssOz8qKc-mgDdQvMHF_AWgtU0_eLH1Z0q9xxzxdhgBiYZhbwrQoi1bAmz3mCOrd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5790d0b.mp4?token=Kox4G_oiRt9tpLyi3O8TMLN18_Fe6FvluBL5ngoFi30xnCrsbWzHaXz2dg8AjFKr6HZNTF_mQbHrarlkCY4sGOACHqb11PrM0xXyelkXY--EMnswYIV3zD2HaS65enlGj9unPCaaNm9P2oZYOyMMbX1eSuNmm2I2kM6hJEV9YePWR48tsmBTHiCZVIC-qPTEoZRiequrnU1jxxm2ZQuHWviIueZ2stS6LNwO1jAlFuEcbugmM8YrcuQqfRuoGLuPPLML47wkQ953tE21EvGm8ssOz8qKc-mgDdQvMHF_AWgtU0_eLH1Z0q9xxzxdhgBiYZhbwrQoi1bAmz3mCOrd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از تولد و زندگی در پارک ملی گلستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/435653" target="_blank">📅 08:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435652">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a1079486.mp4?token=BdBCgHo_MUl087JlogGjx1z63uuaKiR2K5kOL1-HY-QJhrruxNNF0HbSuVXR8-lQnF72fuBhJ9XZAfwEjAOfECaxPBbYS1K4MBXEO9jONVUy_tHIuvShXq0bJ3LQslR5KxiiVVbvd0Ygs6o48HFUwUJ5qg6hh18DKxn8OL4ZMvtJYDQyHtRB8dAxH7v7WRLfVrYbV9Lss8JfIvU5_8hUCzVyNoJyUE3mGGO1fI354qawPyqmKW-O4-F0_UWWjkk6o9B3jjfZ-10hePxAx8K3NrASTDCOcL-z_jEf-CmEYewXcqZu9TIjpYsvZOZzLvSS3QbNz2rIlnx90CLS8wotJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a1079486.mp4?token=BdBCgHo_MUl087JlogGjx1z63uuaKiR2K5kOL1-HY-QJhrruxNNF0HbSuVXR8-lQnF72fuBhJ9XZAfwEjAOfECaxPBbYS1K4MBXEO9jONVUy_tHIuvShXq0bJ3LQslR5KxiiVVbvd0Ygs6o48HFUwUJ5qg6hh18DKxn8OL4ZMvtJYDQyHtRB8dAxH7v7WRLfVrYbV9Lss8JfIvU5_8hUCzVyNoJyUE3mGGO1fI354qawPyqmKW-O4-F0_UWWjkk6o9B3jjfZ-10hePxAx8K3NrASTDCOcL-z_jEf-CmEYewXcqZu9TIjpYsvZOZzLvSS3QbNz2rIlnx90CLS8wotJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مورفی، سناتور آمریکایی: ایران امروز بسیار قدرتمندتر از زمان شروع جنگ است
🔹
جنگ با ایران یک بن‌بست نیست؛ یک فاجعه برای آمریکاست. علی‌رغم آسیب‌هایی که ما به ایران وارد کرده‌ایم، گزارش‌های اطلاعاتی نشان می‌دهند که آن‌ها هنوز اکثریت موشک‌ها و پهپادهای خود را در اختیار دارند.
🔹
آن‌ها همچنان برنامهٔ هسته‌ای خود را حفظ کرده‌اند و هر زمان که بخواهند، می‌توانند عملیات نظامی را در تنگهٔ هرمز از سر بگیرند.
🔹
بهترین راه پیش‌رو این است که ترامپ همین حالا محاصره را تمام و پایان جنگ را اعلام کند و امیدوار باشد که کشورهای دیگر بتوانند با استفاده از دیپلماسی مؤثر، راه را برای بازگشایی تنگهٔ هرمز هموار کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/435652" target="_blank">📅 08:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
برداشت گل محمدی در شهرستان گرمه استان خراسان شمالی
@Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/435651" target="_blank">📅 07:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2aWO-KfF0WgXQmT91_2CqL9cO9QMICdvba4UnyTQJEd3CPMHJSUrHBC27cB_PEgAD3eCIvQUs87cW3W4gkf1cT4GaxPCfUW1V54XpuaEf5TI2j9O3ynOU0lpmtj52Rg478pVrdvRQ9Fy38kNneqOr7vX3S4BLhu-iy9NFMQ0QOQxeOQ05InZxVWI3JCsUyxER0s1DCV2h-R_K1k46OrCOi3ri3jOYiTLigkzR-4TdXZXUSpfnmO7ewR98PM8Ld-6ygD6ml-1yv2cWCnp0BnDkUfDAvDVkUR_IZkGLIlaUASV2nGfUEovuT86xW_iOe4vrK5npWD-wK1Yxmrzp7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد تولید اوپک پس از بسته شدن تنگۀ هرمز
🔹
سازمان کشورهای صادرکننده نفت (اوپک) تازه‌ترین گزارش ماهانۀ خود را منتشر کرد. این گزارش تصویری بی‌سابقه از کاهش تولید و اختلال در بازار نفت را ترسیم می‌کند.
🔹
تولید نفت اوپک به کمترین میزان در ۳۵ سال اخیر رسید و عربستان سعودی نیز با کاهش ۴۲ درصدی، تولید خود را به پایین‌ترین سطح از جنگ خلیج فارس در سال ۱۹۹۰ رساند. آمارها نشان می‌دهد کویت نیز بیش از ۷۵ درصد تولید خود را از دست داده است.
🔹
در این میان، خروج امارات از اوپک نیز زخم دیگری بر پیکر این سازمان وارد کرده است.
🔸
حالا با توجه به اختلال در تنگۀ هرمز و کاهش بی‌سابقه عرضه، کارشناسان انتظار دارند نوسانات شدید قیمتی در بازارهای جهانی هم‌چنان ادامه یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435650" target="_blank">📅 07:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QbrzRO5KEp8AeirFJHVVqD_cls5G4hbdhxGFsXWkU8hQBo3sGmslK8m5M7GyAMhyiPR8QWzVIzVTxXAEzYx0ZErhM8hqqgcIWLBPIsNjYyz4oLd5zPCd06iC8dHf1rNz66jgiU1pmFeeBWACrJm0y07u8KHBuVvzz_Zk0TF7_5LXbdMsWIcSkZ2Y5i433wn4cD4uGA3oNGh_WkXZz_U39CgNo6WOboZkjiBQhpSBBBhQO4A8ql9GgzryCA48lkl_UJeJ7HtDg_LHpkBvtOc0gAAdeUoLMNl1849liiqv3rcyIQO3Z3adGualOtSNedLiiJMl9QuShlWnUqkjeqeLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIo6RjuDrnXgXP0SpkodFs_Sws3Eu1NQcwpdPt87bvqTJEBlcyYIjWuhyGEMbUnACcE0KpxLjxohHdgIfLYV0A4p7kqYEWv_h0smYU0mfitrVa5RDqE16cdQC0rC9uX8zHUMTLDCjVdiIqbeT2UWMv-kIMyfT7vlVfuCtszl5jHhHIgTGcExXtgsDmpzBrXEovVEG5NnJJgQ600QpuwviBUvL7h_ivErZhEtYEZzkrUT1zT_ho0Yh6G5PIpWdyt7mfy4ZYTLoPZAIOINh9dH7nyVahHPbpFxeOFpPIoY0Kver_7HFOmValLr2CV5Mw3HcYQ5bZwzbfIJ1zfZ6Wns4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCbvK1ShaZlb46BjryCW-GTJIGFK9TmuoOoRf7A19jh-0wYIF3_6gaZkjhkncyXxAdpXQJDh7XwjLO88JaQupI8Xj0wvOtKpGAv1XDUOXfLMsSQZ1M61_rQ7UZ_r7gRxm8Rc6YfTxcpwmR_kNdF9i6Py3Q8hdw-K4BYUmSTB3pMKh__SWK8PInugLVkD5i9HG7TuArK51CXpOcgxcW-9XF5MX3hLGXSYZ5q_aoSku_j8icNdE1Ess4Y11MKOA7ucHpYsNayhNCQUacq5v8NXaR9Dd0TjTWDNG68Z1vtgs1BUyeLt0nWQjK3LLzKg037EA27FIx2aNOoSaT6gUClI6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی با وزیر خارجۀ هند، در حاشیۀ نشست وزرای امور خارجۀ بریکس در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/435647" target="_blank">📅 07:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
کالابرگ سرپرستان خانوار با ارقام پایانی کد ملی ۷، ۸ و ۹ شارژ، و امکان خرید از فروشگاه‌های طرف قرارداد فراهم شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435646" target="_blank">📅 07:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXDtIULT7kc2PR6Ak7Me_PKsbOK7YS3vvx3u8SesC9_0tdABrdgcAjNJAf5i-KRflKdEbYjaXIi_3VLL0fZt8UheyaQrWDYAe18k-WV9tNUJ5L8byInhzjc-P44prHGjSPKxjAcMhfZXF3DBteSUHBWNt_B9sTRoFdX8yK5XTRPGaab94kRMxlW6t33sEjJrBq_hOQ13HfmKJEf0uPLQ4en7YAcc7vwvUfwaUsmSKyYac82o5oygroX_mAv5uhd3KhUtbphcFSJb0fvOJOVZ-sICgWQWlDCUmkx5op92BUBaIMRM-QaklLXEe-T6DKAgAFy-dXQ6Gu1mVD14-ai2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خیانت به همسایه، پنهان نمی‌ماند
🔹
بقائی، سخنگوی وزارت خارجه: مَن خانَ في السرِّ، سيُفضَحُ في العلن. کسی که پنهانی خیانت کند، آشکارا رسوا می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/435645" target="_blank">📅 07:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همکاری یک اسرائیلی با ایران، بدون دستمزد و به‌دلیل نفرت از اسرائیل
🔹
پروندۀ یک فرد ساکن فلسطین اشغالی که بدون دریافت دستمزد و بر اساس نفرت از اسرائیل با مأموران ایرانی همکاری کرده مورد توجه رسانه‌ها قرار گرفته است.
🔹
«احمد دعاس»، رانندۀ کامیون ۲۷ ساله  متهم است که با انگیزه‌های ایدئولوژیک و ناشی از «نفرت عمیق» از اسرائیل، اقدام به جاسوسی برای دستگاه‌های اطلاعاتی ایران کرده است.
🔹
بر اساس ادعای دادستانی، او که به واسطۀ شغل رانندگی به نقاط مختلف اسرائیل سفر می‌کرده، تصاویر و ویدئوهای متعددی از مراکز حساس تهیه و برای یک مأمور اطلاعاتی ایران ارسال کرده است.
🔹
دادستان‌ها می‌گویند دعاس پیشنهاد مبالغ مالی را رد کرده و اعلام نموده که این کار را صرفاً به دلیل تعهد ایدئولوژیک به ایران در جریان جنگ کنونی و «نفرت از دولت اسرائیل» انجام می‌دهد.
🔗
متن کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/435643" target="_blank">📅 06:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a9714e59.mp4?token=rvac1z8ITrl-nP1DG2xm0NYReBw4o4c9XCcHu04b4VB_NETcRyQ-AwE6Dpem31dutbZKIpHi0-B0ShJSEBeivxB1IXEK8l_aWMi5V6gH2ENvewjpQGKoGtoXhZ_ecVrwwdP-7ESEdzlS8fn1GK1Kf4-_Y2ehX7rp5Aat1_YtzjpiIFfUrXRTxDsPPVrUpEd6pOQ3y8Vs-lS-_OCzoLluJteYdnhwu_Dh6kcUCgdczy1d0APum4owyXQGZnVWK6UtHfGHa2GvMxGPE3FzSGRti9hzOQlAD90AsSbVf24w61-4xp31RGZVRwLnFC_ykyTldoCxFwfLS-G4vk8jO-te2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a9714e59.mp4?token=rvac1z8ITrl-nP1DG2xm0NYReBw4o4c9XCcHu04b4VB_NETcRyQ-AwE6Dpem31dutbZKIpHi0-B0ShJSEBeivxB1IXEK8l_aWMi5V6gH2ENvewjpQGKoGtoXhZ_ecVrwwdP-7ESEdzlS8fn1GK1Kf4-_Y2ehX7rp5Aat1_YtzjpiIFfUrXRTxDsPPVrUpEd6pOQ3y8Vs-lS-_OCzoLluJteYdnhwu_Dh6kcUCgdczy1d0APum4owyXQGZnVWK6UtHfGHa2GvMxGPE3FzSGRti9hzOQlAD90AsSbVf24w61-4xp31RGZVRwLnFC_ykyTldoCxFwfLS-G4vk8jO-te2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاکبانی که تلاش می‌کرد پرچم ایران را بالای بالا نگه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/435642" target="_blank">📅 06:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epMiaYTZdSYjHnehRcGax4TrdGgwAZkKYh9opI7vBAK-sLV_IpJdxeUvMy8xisSCLpi7OwSMQnBL6O1c_EGvk19uaM_m8af_1BUmZu-Za4dbg1hnQmYltsDntuUO65UPwCOkXn0KcTuE-PNAJWcCdRX1HucK8IEmNWfy2fpkGIG10qPuXr5zuv6YnSjF1gwOVQOVtjvP58FZc-DwU7BKUpzXVG3WK_ZCf9OojlzTO661ohCTXKA-LCWLtcBc5NeC6nERnZpgJnIy95T91BG6GsGQcHwx52Jamvxpcwg1JOjZE-dJJC2RqFDHEL9WuI8jeEEZwVukmRQnGHqSYd7RLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران غول‌های فناوری در چین
🔹
وقتی هواپیمای حامل دونالد ترامپ راهی پکن شد، فقط یک هیأت سیاسی در حال سفر نبود؛ مدیرعامل شرکت‌هایی هم در این مسیر حضور داشتند که بخش بزرگی از آینده کسب‌وکارشان به تصمیم‌های چین گره خورده است.
🔹
از کارخانه‌های تولید آیفون و خودروهای تسلا گرفته تا بازار عظیم هوش مصنوعی و سفارش‌های چند ده میلیارد دلاری هواپیما، بخش مهمی از منافع این شرکت‌ها به پکن گره خورده است.
🔹
ایلان ماسک به‌دنبال خرید تجهیزات تولید پنل‌های خورشیدی از تأمین‌کنندگان چینی است. اپل هم همچنان وابستگی بالایی به تولید در چین دارد. انویدیا نیز به‌دنبال ازسرگیری فروش تراشه‌های پیشرفته هوش مصنوعی H200 در بازار چین است.
🔹
هرکدام از رهبران فناوری برای این سفر یک نیتی در سر دارند که جزئیات آن را
اینجا
می‌خوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435641" target="_blank">📅 05:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e37c5896c.mp4?token=frnGMQv6tAXJzty6nkHzQBuf4BAqZkL6lhqbs7Z6aaQyy_relNg-lg1hiunzwUpVHZeNF1hdiQsGshVaZZ-HowO5t8MTKfEOA9vVVpWOyr8GOdLuhpbL22aV0ZuoZvWWGCerUkJoBFS06oHVfjVcwzAwLPlRaBHFh6aVkO5XKN-xvzKxQlUPdDhV2bkdoczq599YVERAzs-_88mb0CtyQnnh6ZLIpiemEuXZY-igs6Cz50ZKUbpf1j-3a559nM7bZqd2CJ1k-F7dNPHEF9J7F63zGnaJbBYhp9SZR9AWzLmV_3UvhkyLi3Ig-Rba8MUG2egzY1MiM2D0dElNguyqRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e37c5896c.mp4?token=frnGMQv6tAXJzty6nkHzQBuf4BAqZkL6lhqbs7Z6aaQyy_relNg-lg1hiunzwUpVHZeNF1hdiQsGshVaZZ-HowO5t8MTKfEOA9vVVpWOyr8GOdLuhpbL22aV0ZuoZvWWGCerUkJoBFS06oHVfjVcwzAwLPlRaBHFh6aVkO5XKN-xvzKxQlUPdDhV2bkdoczq599YVERAzs-_88mb0CtyQnnh6ZLIpiemEuXZY-igs6Cz50ZKUbpf1j-3a559nM7bZqd2CJ1k-F7dNPHEF9J7F63zGnaJbBYhp9SZR9AWzLmV_3UvhkyLi3Ig-Rba8MUG2egzY1MiM2D0dElNguyqRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سنتکام: ۶ کشور عربی در جنگ با ایران کنار ما هستند
🔹
۵ کشور خاص هستند که به معنای واقعی کلمه در کنار آمریکا درحال دفاع هستند: امارات، بحرین، کویت، قطر و عربستان.
🔹
هر آنچه انجام دادیم بدون اردن و همکاری نزدیک با اسرائیل غیرممکن بود. آن‌ها فقط مأموریت…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/435639" target="_blank">📅 05:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
به‌نظر شما، این‌روزها شجاع‌ترین و باشرف‌ترین آدم کیه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435638" target="_blank">📅 05:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تعطیلی موقت دریای مازندران، از شنبه
🔹
ادارۀ هواشناسی دریایی مازندران: باتوجه به مواج‌شدن دریا، فعالیت‌های قایقرانی، صیادی و گردشگری دریایی از اوایل روز شنبه ۲۶ اردیبهشت‌ماه تا اواخر وقت یک‌شنبه ۲۷ اردیبهشت‌ماه در دریای مازندران ممنوع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435637" target="_blank">📅 04:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4445eb560.mp4?token=CqUDzas-64kWsJsLsjxHkVUJ-LqtTe2kiC5vuaO5lPWaDOJqe_bKVmPAykbnMrX5TAPsoa8WfBBCDW-9_vt1U-yghDcqUXmLFv_0xMn286EFi4GpOj7zCIyEZKwb42rRJu3twlC49vBnG2uRbcGhiAOU6cmYdPdYgiZfcbc9JZb6wv_OykDYLbhlVqoWXuy5HQO8-bTgkz29lfPpfJfaPQBMId7eb-0m6abH8dDrMrORGb2bFIlPRnleAXK3QZi-RZkCEK7rBb1bmW7jriFleYi60BjVgqn_H3hdp93MPBfU0guYrMMeGQ7S2pF1WdyUZ4CPrePOKMMuryonfNsm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4445eb560.mp4?token=CqUDzas-64kWsJsLsjxHkVUJ-LqtTe2kiC5vuaO5lPWaDOJqe_bKVmPAykbnMrX5TAPsoa8WfBBCDW-9_vt1U-yghDcqUXmLFv_0xMn286EFi4GpOj7zCIyEZKwb42rRJu3twlC49vBnG2uRbcGhiAOU6cmYdPdYgiZfcbc9JZb6wv_OykDYLbhlVqoWXuy5HQO8-bTgkz29lfPpfJfaPQBMId7eb-0m6abH8dDrMrORGb2bFIlPRnleAXK3QZi-RZkCEK7rBb1bmW7jriFleYi60BjVgqn_H3hdp93MPBfU0guYrMMeGQ7S2pF1WdyUZ4CPrePOKMMuryonfNsm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غیرت و حماسۀ میبدی‌ها در میدان دفاع از ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435635" target="_blank">📅 04:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">درگیری فیزیکی مأموران مخفی آمریکا با مأموران امنیتی چین
🔹
شبکۀ فاکس‌نیوز گزارش داده در دومین روز از سفر رسمی دونالد ترامپ به چین یک «تقابل شدید» و فیزیکی میان مأموران سرویس مخفی آمریکا و نیروهای امنیتی چین اتفاق افتاده است.
🔹
شاهدان عینی گفته‌اند این درگیری روز پنجشنبه زمانی آغاز شد که ماموران امنیتی چین از ورود یکی از افسران مسلح سرویس مخفی به محوطۀ «معبد آسمان» جلوگیری کردند.
🔹
این اتفاق باعث بروز تنشی شد که ورود هیئت‌های همراه به محل مراسم را بیش از ۳۰ دقیقه به تأخیر انداخت.
🔹
خبرنگار نشریۀ تلگراف که در محل حضور داشت، این رویارویی را «بسیار شدید» توصیف کرد.
🔹
طبق گزارش‌ها، ماموران چینی اصرار داشتند که افسر آمریکایی نباید با سلاح گرم وارد محوطه شود، در حالی که آمریکایی‌ها معتقدند حمل سلاح توسط تیم حفاظت رئیس‌جمهور آمریکا پروتکل استاندارد و غیرقابل تغییر سرویس مخفی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/435633" target="_blank">📅 03:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf2ce3d4e.mp4?token=nEMTAT3RtZBATH6R0wb7P2K4UmoeBc9w19ew-H5Xc3tzmy360MHqpWfqrnZle1GS8cw-7_y3Ucu-ri0f47BkmCRc2gBrg0lWOCALMepuGEr5nB2le76O7bBZSn5urxCRH6XSzxy09v-wKzERu57KdnZGYugn8-soA5GDF4pYY7B77mIyqY2BuPUMzQu-rpR7M6-HsoF4CjJ6sKAaOXjzT31iS4uKpI2ry8D2xlmxsZe00mt3ft2Dhj_zu-z1Vm0dMspQfZWdEovQG0GCyL_YOdMNy9dPBFPnyt2tZj-1ytuMMVD9fgwYz-Ev7UaaU3kj4D2T64-F31HARD2a5AbiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf2ce3d4e.mp4?token=nEMTAT3RtZBATH6R0wb7P2K4UmoeBc9w19ew-H5Xc3tzmy360MHqpWfqrnZle1GS8cw-7_y3Ucu-ri0f47BkmCRc2gBrg0lWOCALMepuGEr5nB2le76O7bBZSn5urxCRH6XSzxy09v-wKzERu57KdnZGYugn8-soA5GDF4pYY7B77mIyqY2BuPUMzQu-rpR7M6-HsoF4CjJ6sKAaOXjzT31iS4uKpI2ry8D2xlmxsZe00mt3ft2Dhj_zu-z1Vm0dMspQfZWdEovQG0GCyL_YOdMNy9dPBFPnyt2tZj-1ytuMMVD9fgwYz-Ev7UaaU3kj4D2T64-F31HARD2a5AbiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هدف ترامپ از جنگ با ایران، تسلیم بی‌قید‌وشرط و تغییر حکومت بود که هیچ‌کدام اتفاق نیفتاد
🔹
داک‌ورث: ترامپ، تنها در عرض ۲ ماه اهداف نهایی متعددی را ارائه داده است؛ او از «تسلیم بی‌قید و شرط» و «تغییر حکومت» در ایران سخن گفته که هیچ‌کدام اتفاق نیفتاده است.
🎥
ترامپ گفته است که جنگ زمانی به پایان می‌رسد که سایت‌های هسته‌ای ایران نابود شوند؛ اهدافی که پیشتر در جنگ ۱۲ روزه ادعا شد محقق شده‌اند.
🔹
او گفته که هدفش نابودی کامل نیروهای نظامی و زیرساخت‌های ایران است، درحالی‌که جامعه اطلاعاتی ارزیابی می‌کند که این اتفاق رخ نداده است.
🔹
حالا او گفته است که هدف، بازگشایی تنگه هرمز است؛ در حالی که جهت یادآوری باید بگویم این تنگه پیش از شروع جنگ باز بود.
🔹
بنابراین وقتی نمی‌دانیم برای چه می‌جنگیم، قطعاً نمی‌دانیم تا چه زمانی خواهیم جنگید.
🔹
مقامات اطلاعاتی آمریکا معتقدند ایران به اکثر ظرفیت موشکی خود دسترسی عملیاتی دارد‌. ایران نسبت به قبل از شروع جنگ، کنترل بیشتری بر تنگه و اقتصاد جهانی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/435632" target="_blank">📅 03:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f21a5aed.mp4?token=NY6J4dOwXznwbiS7N5n95JUw-yqAzzOn3_PD91vMUVB8xn7ZTIr09pxWs08FBN5lnaoOHAE1js38iXFMIOnmg9LMHgW7TLvWUhxTZSy84Pr0wf_lJNIhOtdMBzvd_ix4f_CONAoGhEWu0qrBqFKzP0JbgqXyJmtApzWibH_0_ZcaI5FEnYn1eyiD2E9uhndjV-wE8llhWYmN7VsjIWDyWGzeVo1WFt31NYnwypITNpJjHCs4ayPt2eKUQMA8V_GTc3zl7kEoq5gHQxrv7KIW52TH5-RcLBxbV01I1ur32FVFtBi9LJSNkP_FJJmKzCvMZIvl1GlEd7J5IJV8QJ_1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f21a5aed.mp4?token=NY6J4dOwXznwbiS7N5n95JUw-yqAzzOn3_PD91vMUVB8xn7ZTIr09pxWs08FBN5lnaoOHAE1js38iXFMIOnmg9LMHgW7TLvWUhxTZSy84Pr0wf_lJNIhOtdMBzvd_ix4f_CONAoGhEWu0qrBqFKzP0JbgqXyJmtApzWibH_0_ZcaI5FEnYn1eyiD2E9uhndjV-wE8llhWYmN7VsjIWDyWGzeVo1WFt31NYnwypITNpJjHCs4ayPt2eKUQMA8V_GTc3zl7kEoq5gHQxrv7KIW52TH5-RcLBxbV01I1ur32FVFtBi9LJSNkP_FJJmKzCvMZIvl1GlEd7J5IJV8QJ_1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غوغای قمی‌ها در شب ۷۵
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/435631" target="_blank">📅 02:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZzAHKlMSFytim4oPwEnG3eRTjRvHrtbLj-k0ZrDuIIV5r7FsuTurdp97nwddSfF2waR3VmoEf9_4WcLnTTJCfCic2thbHHAN00axaJ8pkKHWCjCRA3hCqG734hQTQl2Ttk16mu1VkIAjlXs3pQ95-SRQt8lIwu_TvoiiuN466gb1L6HhacG8FEYI-AZUG5dCb9RjEqC08ETpCWhNvrHF4Wrr0IreHQBpdZpvOFrBwRWn3MS8Iakkld8oSbZFrZpbVVw2BVbfTUiNt1z-ebYEIYT9MisPPZt-u57lvgYq8IDo0c-WROjmDqhOo_u3vbN7k8aHFS-MWG95LmbmuzIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسری بودجه، دلیل لغو مأموریت سربازان آمریکایی در لهستان
🔹
ارتش آمریکا روز گذشته در اقدامی ناگهانی اعزام بیش از چهار هزار سرباز و تجهیزات به لهستان را لغو کرد.
🔹
حالا پایگاه دینفس‌نیوز گزارش داده کسری بودجۀ ارتش آمریکا، یکی از دلایل اصلی تصمیم پنتاگون برای لغو اعزام ۴۰۰۰ سرباز به لهستان است.
🔹
درحالی که سناتور جک رید، عضو ارشد کمیتۀ نیروهای مسلح سنا کسری بودجۀ ارتش را حداقل دو میلیارد دلار عنوان کرده، شبکۀ ای‌بی‌سی نیوز گزارش داده مقامات ارتش رقم واقعی کسری بودجه را بین چهار تا شش میلیارد دلار اعلام کرده‌اند.
🔹
پنتاگون پیش از این هم اعلام کرده بود که قصد دارد حدود پنج هزار سرباز را از آلمان خارج کند.
🔹
به گفتۀ مقامات، این اقدام سطح نیروهای آمریکایی در اروپا را به سطح قبل از تهاجم روسیه به اوکراین در سال ۲۰۲۲ بازمی‌گرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/435630" target="_blank">📅 02:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1967133bbe.mp4?token=VT0i0lTpfPPtQz7AWxnx3dqGKlqt3btK5-0r5DpXgOKTpQAU26Vee1fBlRkZ19KT4ydQkpSrAxqlz4NVxSg2AuAHwhijtLFmWqaKe7q3IzJA34nIXI0Lo_vpVcQ6N6ne8-GswLP8IVVEftAmvZA3jRwIzAA0bihsEJp9SNgq_sMMbbmi1XWlV-J-61k5FiqWFiCE2VtmdqKycazo5CUJFWsUGeJZ0cACHkrP4oMvpyXGOYY2eOD2eLxHpasWMqTWwDHaWCwba3uqZI7t6yndEPr11fUmvqqTu8B-NnZZiFdutEbavbpXsrfxKSPu8tkrM2eeQi1N75GS04TYjXsqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1967133bbe.mp4?token=VT0i0lTpfPPtQz7AWxnx3dqGKlqt3btK5-0r5DpXgOKTpQAU26Vee1fBlRkZ19KT4ydQkpSrAxqlz4NVxSg2AuAHwhijtLFmWqaKe7q3IzJA34nIXI0Lo_vpVcQ6N6ne8-GswLP8IVVEftAmvZA3jRwIzAA0bihsEJp9SNgq_sMMbbmi1XWlV-J-61k5FiqWFiCE2VtmdqKycazo5CUJFWsUGeJZ0cACHkrP4oMvpyXGOYY2eOD2eLxHpasWMqTWwDHaWCwba3uqZI7t6yndEPr11fUmvqqTu8B-NnZZiFdutEbavbpXsrfxKSPu8tkrM2eeQi1N75GS04TYjXsqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
هفتمین رأی‌گیری سنای آمریکا برای پایان جنگ با ایران شکست خورد
🔹
مجلس سنا برای هفتمین‌بار قطعنامهٔ پیشنهادی برای توقف جنگ با ایران را رد کرد.
🔹
جمهوری‌خواهان تقریباً متحد عمل کردند تا اولین تلاش از زمان عبور ترامپ از ضرب‌الاجل ۶۰ روزه برای دریافت مجوز…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435629" target="_blank">📅 02:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9997533.mp4?token=sf1tAU-g7vzuN4j8TTzd3s3XfyMy_8EJ9Oc1y4tgy3Sgt4GW43Oe1Bv8UHguAW9NrqddOwtYCK4HWcOZmnxpkY3_x3IXsga-99bk2ton8RFWtuNSuXohK2Xe8dEVPMZjhV4yxpBNQMMXXhDRl1dq0zxsK1Y3oyQttxkq7N91o-5dCP6Hdy-sDXB8IlB54Plk6MgSnI5pZGp7laLgzxi7V2bxuBChMEQXhpkHQlsZGO5gKUtcc7JoTlDspXuqMLDhzfwxT_aRCCiysVi9aW-s1bdLgBniKckNTJG7AFCZFXFx_Yrciid3cnaT0yKhc6MvgwdqggQsTCUJdjSBIofTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9997533.mp4?token=sf1tAU-g7vzuN4j8TTzd3s3XfyMy_8EJ9Oc1y4tgy3Sgt4GW43Oe1Bv8UHguAW9NrqddOwtYCK4HWcOZmnxpkY3_x3IXsga-99bk2ton8RFWtuNSuXohK2Xe8dEVPMZjhV4yxpBNQMMXXhDRl1dq0zxsK1Y3oyQttxkq7N91o-5dCP6Hdy-sDXB8IlB54Plk6MgSnI5pZGp7laLgzxi7V2bxuBChMEQXhpkHQlsZGO5gKUtcc7JoTlDspXuqMLDhzfwxT_aRCCiysVi9aW-s1bdLgBniKckNTJG7AFCZFXFx_Yrciid3cnaT0yKhc6MvgwdqggQsTCUJdjSBIofTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بامداد شب هفتادوپنجم، و میدان‌داری تهرانی‌ها در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/435628" target="_blank">📅 01:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUdtDkKdrsmKMV1zOSj-qmRK_LctZ71Cr7yhDqnxt01evptChNikQI8-2flDbHEztUmOY8A8nAXxqGAW3rmzuyf1sNhN9xdLm6qz7lKQerqE4AjslVgHEADshFWcOtYzB6fJ_diFGBKLHXxLO1kw0v2Ydh-60nEKmHZMmA7irFGoXlHoU1fACOqIPqkACWXxRCjvOCAL9Qoq5YcXKnWU6bBujzdd1mV5hsmN26w4TeKktXwsMQW5KkuexKSvxyXZ6anDGIRJI0mY8LAFOAn2wYSkpHg2HaJzzle8L-CtY8FFEGuvp97w7RkAboM97q0XSpMeDK9MrDUBIlNvscSEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام موافقت ترامپ با نظر چین در خصوص افول آمریکا
🔹
دونالد ترامپ در پیامی در شبکه اجتماعی تروث‌سوشال گفته که با سخنان رئیس‌جمهور چین که آمریکا را «کشوری در حال سقوط» خوانده بود موافق است.
🔹
ترامپ با وجود این حساب خودش را از سخنان شی جین پینگ جدا کرده و مدعی شده که منظور او آسیب‌های دوران ریاست‌جمهوری «جو بایدن» به آمریکا بوده است.
🔹
ترامپ نوشت: «وقتی رئیس‌جمهور شی با ظرافت تمام به ایالات متحده به عنوان کشوری اشاره کرد که شاید در مسیر انحطاط باشد، منظورش آسیب‌های عظیمی بود که ما طی چهار سال ریاست‌جمهوری "جو بایدنِ خواب‌آلود" و دولت او متحمل شدیم؛ و در این مورد، حق کاملاً با او بود.»
🔹
ترامپ دوران حضور ۱۶ ماهه‌اش در کاخ سفید را «درخشان» خوانده و گفته منظور شی جین پینگ آمریکا در این دوران نبوده است.
🔹
ترامپ در پایان نوشته است: «دو سال پیش، ما واقعاً کشوری در حال سقوط بودیم؛ در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده جذاب‌ترین کشور در تمام جهان است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/435627" target="_blank">📅 01:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b785d46e.mp4?token=qZqj8l_OUZ7D1hlpO0qbe8CcakMUNyQvOm_ZjXHIRy01J-viv-dxP03T4HCEeVePCBohTYDJR1c8Kiq0KYmVJzbncZfWX9A8AdxkXFnFUv-aLEJiAxkUy_337j6uFJC3q441W17mo8iA9IbrHhJHcmpzJ9If4uB_dJoVXgSx5S9cXZT14qamU_WaIzp9nQ-hA3i-KhpUxFQk331vW7O_CSdOiXVdMcHQQF7AbzkP9fb4Wht8UPs9bgovo2m4jjBGNg_zCpUyMfKVX3CSzb7Ow5wjrDdjHE84srYRtANmKRSDi1kq39zOTpbixaAHr_6TnBtOQ3H15hLh8--lTGbpEa4ibjWcZzV46X0g6LmIYkVXWpbVmT4vucAxKU6xc6ejoWAkAVx38TBJLLdwt7LWFRDhaJzYXTHSLuvKFzCCkuf2e5kgHSYyGr3WDghL0t1UdMPy_lkqu7EBnVA8trQH1xxtgnSWBahTNAaB7ED6wvxMV7lxpbNi8KrZbU9g6f39gCYaf0YEfmtSQ12h6qMwRX9esjs_ngJdOBPFEQVENIlg9SPdepktTFGN0NSi8TM6spi2LVsdMOCyKOlQkRzSvC6caL4WdWGEuh_LmR82UHPIT0C2D5dF2pmVz5VWCY_InT1_0jwulCbIDlzpiGCRipBt50e_3tbA2oDfgYhCI4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b785d46e.mp4?token=qZqj8l_OUZ7D1hlpO0qbe8CcakMUNyQvOm_ZjXHIRy01J-viv-dxP03T4HCEeVePCBohTYDJR1c8Kiq0KYmVJzbncZfWX9A8AdxkXFnFUv-aLEJiAxkUy_337j6uFJC3q441W17mo8iA9IbrHhJHcmpzJ9If4uB_dJoVXgSx5S9cXZT14qamU_WaIzp9nQ-hA3i-KhpUxFQk331vW7O_CSdOiXVdMcHQQF7AbzkP9fb4Wht8UPs9bgovo2m4jjBGNg_zCpUyMfKVX3CSzb7Ow5wjrDdjHE84srYRtANmKRSDi1kq39zOTpbixaAHr_6TnBtOQ3H15hLh8--lTGbpEa4ibjWcZzV46X0g6LmIYkVXWpbVmT4vucAxKU6xc6ejoWAkAVx38TBJLLdwt7LWFRDhaJzYXTHSLuvKFzCCkuf2e5kgHSYyGr3WDghL0t1UdMPy_lkqu7EBnVA8trQH1xxtgnSWBahTNAaB7ED6wvxMV7lxpbNi8KrZbU9g6f39gCYaf0YEfmtSQ12h6qMwRX9esjs_ngJdOBPFEQVENIlg9SPdepktTFGN0NSi8TM6spi2LVsdMOCyKOlQkRzSvC6caL4WdWGEuh_LmR82UHPIT0C2D5dF2pmVz5VWCY_InT1_0jwulCbIDlzpiGCRipBt50e_3tbA2oDfgYhCI4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم کوار فارس و علم‌گردانی در خیابان‌های شهر
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435626" target="_blank">📅 01:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzkPrjXNoylrpW7eMWKPxG-cSZZ7aiLz3MXtcphJ8M0Rb9rF3D419rTp-j13e5x1i2CSm5Z_7WpBsMdPVC08euMX2ujwL9KuOloCuxLoezJv4S6ZvJJn_qmccKynzw09czMtj9MSnpAWC9BSmlTC8NEqgq66-iaK_kwJMMOc_A4y7gM8CtTM_TFVdcwJ4tI732rJ7MTudFzLFevOycFkRV4gis3CwGV4SPw-I1KgkflIOr6HE1EX4-K5ETxNSM_26wr_1XB9HvHIVHLiPZnQ2TveyniQ6M6ZIEXTrd9nWjBns3kX1jQoKcf2jlHx2xXxpUvZvi4FHdneHeICZ_etjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شناسایی ۶ هزار موتورسیکلت احتکار شده در آمل
🔹
دادستان آمل: یک کارخانۀ تولیدکنندۀ موتور سیکلت در آمل، با سندسازی و صدور بارنامۀ جعلی اقدام به دپو و احتکار ۶ هزار دستگاه موتورسیکلت کرده بود.
🔹
این انبار با موتورهای احتکار شده پلمب، و پرونده در دست بررسی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/435625" target="_blank">📅 01:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: فضا را برای همه نوع آدم‌ها باز کنید
🔹
خواهشم از خواهران و برادران متدین این هست که فضا را برای همه نوع آدم‌ها باز کنید؛ بگذارید همه نوع‌ها بیایند؛ بعضی از افرادی که ظاهرشان شاید ظاهر مناسبی نیست اما باطن خوبی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435624" target="_blank">📅 01:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
موج هفتادوپنجم حماسۀ مازندرانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435623" target="_blank">📅 01:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جو کنت، مقام مستعفی دولت ترامپ: وزیر خارجهٔ آمریکا گفته‌ که ما مجبور بودیم به ایران حمله کنیم چون اسرائیلی‌ها قصد انجام این کار را داشتند
🔹
در واقع اسرائیلی‌ها به ترامپ گفتند اگر او رهبر ایران را ترور کند، مردم ایران قیام می‌کنند و حکومت را سرنگون می‌کنند و این اتفاق بسیار سریع و آسان رخ خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/435622" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیعت مشهدی‌ها با مشت گِره‌کرده
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/435621" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
مردم شهرکرد، ۷۵ شب در سنگر خیابان
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/435620" target="_blank">📅 00:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv9pVA5Snkb_Rb69QETrYBnlzeIFkqm_Twn6Ja7XASGeGnMc4E0qDLFGWH8--dyAp4lZ9W4fZbdHFyS3QTlyS7yUMi6Lq2-9y9uyRiDwtarkhIPAxBRI4IscKDmue37i2e9w2V7sSWgHdTlBAiyVjETw9zOWoH9xuexvgqC4oxioYqJ-syAZkxmMxd9xEyCCo6hij2y1KP0NRDwC_Y21nxBL_s-6hwktFnPQp9PvyiDK0LCn8XwyLZWDYeeODxY61TWbdmSV8DWBOz8FKd30BZO19l3LK4ttBaUHsSUGZVc7YIpdjIWlzV01Pgdv9pkrybkke-Ubpkee04VNkxCFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از شهادت پدرم فهمیدم «شهیدان زنده‌اند» یعنی چه
🔹
فرزند سرلشکر شهید اکبر ابراهیم‌زاده در گفت‌وگو با فارس: پدرم همیشه می‌گفت «اگر احساس کنم جایی به من نیاز است، وظیفه دارم که به آنجا بروم.»
🔹
او برای این منظور، حتی علایق شخصی‌اش را هم کنار گذاشت. بعدها که بزرگ‌تر شدیم، از او ‌پرسیدیم «روحیۀ شما به نظامی‌گری نمی‌خورد، چه شد که این مسیر را انتخاب کردید؟» او پاسخ داد «گفتند به نیرویی مثل من نیاز است و اطاعت کردم.» فکر می‌کنم روحیه ولایت‌مداری و تکلیف‌گرایی او باعث شد چنین مسیری را انتخاب کند.
🔹
مهم‌ترین ویژگی اخلاقی پدرم «مهر» و «رواداری» بود. او هیچ‌گاه به ما اجازه نمی‌داد درباره کسی بدگویی کنیم یا قضاوت ناروایی داشته باشیم. حتی اگر با فردی اختلاف نظر سیاسی داشت، باز هم نمی‌گذاشت درباره او با بی‌احترامی صحبت شود.
🔹
پدرم نسبت به استفاده از امکانات اداری یا دور زدن قانون، فوق‌العاده حساس بود، هرگز اجازه نمی‌داد از موقعیتش کمترین بهره‌ای ببریم و حتی از ماشین اداره استفاده شخصی کنیم.
🔗
ادامه گفتگو را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/435619" target="_blank">📅 00:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs6C9F8rk7Uq7nXEVoRSQJk2L9c6StdRmpMo5nxgHAdBy_sNgfK63bKak2jZ3lG9G1FOmwF_xChFFUHLtM9dS1CU34IBB5s_8CMMwYInOF6EegykQSG69od0_Q5YIbICtKw6GvwyuC8sac6mQusjrgytRJ9494y62dm22gIogg1KuuwshF3rYA1KG3DAUkDUP8ijV-I5Wp6GeJ3h4g2yiBhoRsCJGjP2KjUdFA-YBfEkfukIxu2Cuyd8LAzP2RuQ2aANyGdCg2cO1lCsZwxreJ-HeKPzmIjI2rz0Nad6Ubp3skbuwZlBgnvZzVK4MzA3Fmdz0pXOvhJUfqh_-v1UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBw4W_dgeTwWX57Stiz4lN7qnw5bNJSoChLTph-E8uTgUzQSAQoF4BV56XLc2uxddvx3KiafWPFD7LEKW5l5rLgTcMZwuLQx1hWxrVXCxlXS6PiiidtZpaFN1H6KYG37bz0cMNO1ye5AreYoOGFD1hc_fQFZEDokyWhjs14fbTlmn-GhbgqBLMlG3I004OuUWvA_KbipZKn7LPrqxShoEvEUTClPYk2fSxxaZ-PTHy_vUEPecVbmQSlvfuDIqbdnea7vU23GhI8gJR263rGD48W7TP5PlZlZIOJWwLzeIE6curEV8s6CMO-zrp_riIPLpF10h6A769a7e8Sb4aTzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izYwCmZTsZOyWKiWg_3GTxIFDZ7-nHvMHiKR60FHkeXYyFtf9YkPj2GaYLm0DhqWjVnFbaxz9rUZY_ixzPU1GluOrNYUzwo0ic6WeQfIVJF65H72gsEBAv2Uu70rp5gzqjiOWZCV4L5TxCR_2HYs0WNo6zAfFxPY01Gy5A61oUozzb-WpIdJq2jVC_j7W_EpyPkSHFl2A63JxWbpgfY6nEG079-3cO1j_k91wSIwAr_1wihhbxh0sQTxl2W4JRXyfrftu2B8UJc7VoXNzAvFqggjNM3Z6D_3hCipF8DQyrWhfNINHmoC11KnaV50mqHQnJDbEahpuWWxVjBD0qE8nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حنظله: مغز متفکر سفر نتانیاهو به امارات و معمار اصلی توافقات ابراهیم هک شد
🔹
گروه هکری حنظله اعلام کرد که با هک «ساموئل شای» طراح سفر نتانیاهو به امارات و معمار پیمان‌های ابراهیم، شبکۀ مخفی او را افشا کرده است.
🔹
به گفتۀ این گروه هکری، شای نه‌تنها هماهنگ‌کنندۀ اصلی تمام توافقات پشت‌پرده میان رژیم صهیونیستی و کشورهای حاشیه خلیج فارس است، بلکه تسهیل‌گر کلیدی روابط پنهان اقتصادی، سیاسی و امنیتی میان تل‌آویو و ابوظبی محسوب می‌شود.
🔹
براساس اسناد منتشر شده، شای، اپستاین را به «سلطان احمد بن سلیم» معرفی کرده و از این طریق بسیاری از حاکمان فاسد امارات در شبکۀ اپستاین گرفتار شده‌اند. موساد نیز از همین مسیر برای وادار کردن آن‌ها به پذیرش خواسته‌های خود استفاده کرده است.
🔹
گروه حنظله اعلام کرد امروز ۲۶۵ صفحه از تماس‌ها، شرکای مالی و ارتباطات محرمانۀ شای را به طور کامل در وب‌سایت خود منتشر کرده و تمام اطلاعات مرتبط با شبکۀ مالی او در کشورهای مقاومت را در اختیار سرویس‌های اطلاعاتی کشورهای دوست قرار داده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/435616" target="_blank">📅 00:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طفرهٔ فرمانده سنتکام از پاسخ‌گویی دربارهٔ پیش‌بینی بسته‌شدن تنگهٔ هرمز
🔸
هیرونو، سناتور آمریکایی: پیش از اینکه به ایران حمله کنیم، آیا این فکر به ذهن شما خطور کرد که ممکن است ایران تنگهٔ هرمز را ببندد؟
🔹
فرمانده سنتکام: یکی از مسئولیت‌های من ارائه طیف گسترده‌ای از گزینه‌ها همراه با خطرات و فرصت‌های مرتبط با آن‌ها به وزیر و رئیس‌جمهور است. فکر می‌کنم صحبت دربارهٔ اینکه آن گزینه‌ها دقیقاً چه بودند، نامناسب باشد.
🔸
هیرونو: بسته‌شدن تنگهٔ هرمز توسط ایران به ذهن شما خطور کرد؟ بله یا خیر؟
🔹
فرمانده سنتکام: تقریباً ۱۰۰ بار از تنگه عبور کرده‌ام. من تقریباً هر روز به تنگهٔ هرمز فکر می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/435614" target="_blank">📅 00:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین «حیدر حیدر» در اجتماع هفتادوپنجم مردم رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/435613" target="_blank">📅 23:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDF8lJFHRfpd5uW4QTdoGyBC_rd21yaSigxZ9aE331P9szWJS52DqQGEGx7cPmg1s1fKV7hKvEXxl8mnrgx9zc-BSOCLAA7JlQF2c_IiIp-fa0AGoY2Jw_QeOkahAVXPCtvxHToHpXV_gXvCXtxR4EkZqJgxXeehOfii60pJ2zRM-0i8ZyayYpcJAOo1SUjTMPr2gxlkQA858IbCbHWjEP8JOj651G0PwKrv42UyfBFMe91MOvnY4Lahy-UafJJ16nwuZbsQztorSkzwFm2Msxe5nTi8CfhtUo5dKajrsg39_yedlxJVlK2QNr0zpFcGj3U3XCcLmhbGQJREzfmNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: حداقل ۱۰ دانشمند آمریکایی کشته یا ناپدید شده‌اند  سلسله این حوادث از سال ۲۰۲۳ آغاز شد:
🔸
مایکل دیوید هیکس: دانشمند ۵۹ ساله آزمایشگاه پیش‌رانش جت ناسا (JPL) که در جولای ۲۰۲۳ درگذشت.
🔸
رانک مایوالد و مونیکا رضا: دو متخصص دیگر از JPL؛ مایوالد در سال…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435612" target="_blank">📅 23:51 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
