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
<img src="https://cdn4.telesco.pe/file/P7nTMMYZW1uopl_LxhZtKZgHZpDaQ6rLs8PMneULNQ5ZkNWAMBJyePT2jv6Vx8xuFN3xTdc98P-GWwnWwmCzS2CugbgpEVkt9CUztCa0AWA1SooBI96HMX2MwS4I3WxHzuHkAUeas98vWhLiyHEb5GQAk4PMNF4QHQTU62TEerC53U_9sJq3rD0CbGgbYdUQ0VjjeDs9r_5qMF-wLKnk1SxVl-TAC0zBdVToHklHNpmuZauCXT63mQa0f0uZjx4ipF90BOtzxgDQ_zW1boo2ZVPPbCSXMT9IIC6gq_srQWqmx_nsvhpW-w0yxTvKHv9-Okdbtp6ppLRfsGeqH7-nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB2Gku5GCQ7qvHr--elo9hawIyLDnRFTDNqSg000Vy3Fce77mD7-Dl6r_Gk-WcTh2QnhBHkdzz_5lSosLjwE4nOnwbwPNjMyMRwWaBlTHbBUpkqiNaOV2kOfIHAcBSw8DDaxrD3C2ZHBqKvqhLgaVfezybAvdO9AesASy214DEeZB6XfnGXOVAr5-FxCcR3DtqRkpmdbDFxQ7tR6cNt6FQcZ4_d1AY2421MdrYT6ITVutregPwZBKVJJFlmWS5wKYU6g8eRp5hIOCrFs2WZKiPL53HLspSvIjTbtF0x5fr_oEHC765LpU3mZz9li-MYOD4zJw1YtHkyL0fTiQHVkpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 247 · <a href="https://t.me/naya_foriraq/80723" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد باكستاني يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/naya_foriraq/80722" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTi9XoW869kTFUeDmlInSZy-dXNxq-SeQedccFuXPJ8fjUH7PxMc5yuIb1cwVQRIIvcqTRq4XU1yRMkTmebp3by706Ce6VbaFfU_g_nRZQE9A-EfjTSLl782Yi4vpVSWpS9p4ygTEwsn784m2zzGMWZJrA9lFLlCVJwAgM4b-dqte6s2x5qur8lqAx25hjPMqW8P996wwo1gKeCfMx4f8BHB4e_29rxxcOeKkEnli5pYMPOpfz3pimFjetgi1JMpYFzPwB80nZaayRLQmUJZgtPnGrOXO7hyuNKXAh-AH1eofvlGlHK5ltzKues4MDx-aG1IqMHSriSeuNZRAS6ZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/patIZyPr4oByQz3EjRBpQmQzdijPn_TeHSoy6Xhb3gk9X4hktMPocTlG-s3ASQz0tkaOqsMkowxDB6Zd4sqRUjtBqNqAcIuzaZMIQ0JA6IW-3ZaBM0ysE0vOsefZO6ggMvaxj9rS4NM3-JXyBLBYbY078JKirPDL4rlzb8ZDIXGLfJ_A2Jm28ZlQn6GqnWwORIKzv4Y4QnB13hKzhcGIhFQFvWkvwrnVyPrOz3wDPbtNHzONu3532m-S6pKQgaotOgrSa_2DU9InK8fcXW2tcIOiA5lCqkkuE7u2ncScRUcCwTu_YeYLzI498QZrjYCtiq03_C-U7uy3GZ3XXRKMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGO_poCRiyGLBxo2ROgwTNMYqciS-QWBu-1QEwpsOP9dQ9h6Zpx1W0NdOBjDEnJHq_Srt4AgMTnrnIR-VVvYhTKHu-4XKzCsJTapLwyW8WJ6J8fUVSlO3p2KQgYnJ4N8jwgi1NXv_qeo_ZjjN3hKVOTIwcfB6C00YPmXB_0dj24RS5z9O6T_kIj_EKoZRxiPIZPzjkB-f0GmShAGfQDuLrmSEhJKZD-XzhMkGFP5HRU0bDkJVdA3sTRD0x31FrwnhNXJBBCYyw8N0ulqEX_KhZ5Fw4oK8uYgW6F8KpAVb742jtP6nMfEbfwZ-YXa9BmjayErpfCmLsoS2pL0H7Dr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBZ50L2nCTDmOGPDTS0-UQ7zoaf0_0-mHypArdc12olSZgE-zRkzB50d1KTm1DV6gYL4OwLvaUsIvJbhv16bs-eitj607pq81qWoFAN5Hl3PF4-7gwi4lxGpdDENRaX9DEK2jXmnw8J2EwPtzN333u-8gkzLZWphMOxI_p8mFh6UHqdydCC1H-ExeyQooNsDTHADSsEgiaYAlNNpvZFdEwFYxDyaWfRSgBU1sriCiow3qJiSCBIrrUf9ths0HdqPyc04JYkT0aRQsTUSYMAyQ9hDS4vtlSdmEmO1FfFyRMLJsMcKTd0N2gq0Pst5dd4oQndUqOh-j9CfvIQJL4CQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2xh6-dioY2AFAuq0KFCChRcuqZEGGX05kMMkGms2eTNiRxcfFjyEjzbaU5EkEnGEvAOPsk06r8dF5Q5vLe7GetZuMZI7iSFEt0fBALUUT2xFXSWbNnifmUxA8yL-HZBM3Pw4Fy_mtIGfgYrpBJ3W0OCUQHu1j3DdpAHCpg_TBaHiL6nAPSSxD_hkbPXcZL_21UTuCkm8maB55ItD5bfnJ9ELtLoCLIaknse6U8XftEXmiogwDpnZ3YWZMWOST7rbgqQzMMiwhPtW2YtTnjCif8ZlqXZwFvHyEzXZrKUuVZBj2Un1iuOclNYFozJR-3grtQTWEKFAzr7l1xopvt-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEtmoZ66sENNWBWjafY9Z9jaZrEaWsWO7oDmUe3B2H9yPib5prtD77M1jJLgDZLMnyzrUONajrvongAHz_cd-N930ATzOk8Oawd4dR0CMToOx9GmdRINK4YntppETXnnWF73ze-yHDsFDAbJQcDccKR-ZUx_47pzlpbjtsvuRcWHGjVRgkXmpRvczK4YDkOSRNxXYt2FyJuFZ9OjrNCfm7ZLrR71PWtYNDlZMGMDQxEeIPXMYCAHz_vVMK4cV3MTXtTqGYbK7bJ2eNgRJfAEVEzDhtRcgMRbRdT5BlUS_HYXxP5DlNs7iB5YhkjOkKfm0jcv5iHBCNFr0SRjMUCGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoiY-EAi5AimwryokBeFYrd_jQSNpvddv06sgoCCuv1QRKuvsOCARD64Xqz3P99rcK0huQTwJfP0-N1mpjropHgjD2hU4Si5nGju0uurhtANJGrhNX9U7LNyLLmqGTUy5Iceu3dkC2HrUo-c193eDqmVQbAB6KRQwG_gK5GCu8AKnOH1mbWdWWDqIJBQDeUx_qquQaF5fzn8NTbDFRJnoGRLlMx8w9WygnYPgrw7l7ccU4QWflRXaw6-3Accp5GWmKfA8sudzZduND0cerGt3Kubr1fCzyCwG-daG6fVa5kPpTQ353AoYa4WaFVaDJ5wmL2IN8ypG8GXJh2khC8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elZbAcAaXDDJXyGALxlePAPNfnbwNHOy3e3_g3Znh_2vIXFNbGlaGfMpMNZyzftnHq_HCot2KbtCm1gO83Ace_kEl0tvcPXfAzH7GteBAQT-a8dnbnzsiQx9Rn9HSwEA4u9Pfb1hY_3Z5JCvEFNhn1TGa7si9yYtaXIapEhtdQrykkqFHHyMcGhlnc0ZT76ULHLaSNFhoVTP-lxJ1NWZr_vRJMG3kYHydfxuSK6tj5CkxydkRiC6QXRtcpNxX3Y1bck2cw3-OHZNQq0ZSpLfxspmL3hfWa5w3mL88oB3KsZXm4gCYXQzRuiSAx2DMAlKJQeaFrA5Xt986Yke4x0YuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وفد هيئة الحشد الشعبي برئاسة الفياض يصل إلى طهران للمشاركة في مراسم توديع آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره)
وصل وفد هيئة الحشد الشعبي، برئاسة رئيس الهيئة السيد فالح الفياض، يرافقه رئيس الأركان السيد عبد العزيز المحمداوي، وعدد من القيادات ومديري الهيئة، إلى العاصمة الإيرانية طهران، للمشاركة في مراسم توديع قائد الثورة الإسلامية، آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره).
وتأتي مشاركة وفد الهيئة في إطار حضور مراسم التوديع الرسمية التي تُقام في العاصمة الإيرانية طهران، بمشاركة شخصيات ووفود رسمية من داخل إيران وخارجها.</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/naya_foriraq/80714" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد هندي يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/naya_foriraq/80713" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد الجيش الايراني على هامش المراسم: نعلن للأعداء، بإرادة أقوى، أننا سأخذ ثأر الإمام الشهيد والشهداء.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/naya_foriraq/80712" target="_blank">📅 13:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
السيد مقتدى الصدر:
بسمه تعالى
قال تعالى: وَنُرِيدُ أَنْ نَمُنَّ عَلَى الَّذِينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوارِثِينَ
كنا وما زلنا دعاة إصلاح لا يجمعنا مع الفاسدين حتى حب الحسين ، وقد كنتم وما زلتم معي في السراء والضراء، فلنكمل طريقنا لدعم الإصلاح وحملة الإصلاح الجديدة التي بدأ نورها يشع في ثنايا عراقنا الحبيب.
فهبوا لوقفة سلمية تدعم الإصلاح وجندي الإصلاح الأخ الزيدي رعاه الله.. لنقوي من عزيمته ولنثبط من عزيمة الفاسدين الذين يحاولون الضغط عليه وثنيه عن المداهمات الشجاعة والمثمرة التي أرعبت وأزعجت الكثيرين من الداخل والخارج.
فنعم نعم للإصلاح
وكلا كلا للفساد
وشكراً لكل من أعان الأخ الزيدي كالقضاء العراقي ورئيس البرلمان العراقي والقوات الأمنية البطلة ،
وأحمّل الفاسدين المسؤولية الكاملة عن حياة المصلحين وجندي الإصلاح وكل دعاة الإصلاح الذين يرومون إعادة هيبة الوطن والدين والمذهب
والسلام ختام</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/naya_foriraq/80710" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95caa026c0.mp4?token=njX3KLiRAwduP04Loq4JOCnpzqvL6wCHsB50kJzbWDI4wtkckCwSZOyFLRYTsUfI-tLCxEHby5Y-Jcg1YV94F3tpP6Aq9_Ethg8BZ5VeFvfRanNArWRaTgOT1YgbjfR1D3MKTeR5kukW3PWTQ8zAyKLuRQM2M2jSf77ZBAH1bl6e742DKEEc6UHmrJVchrKRCA3qtNM8y7jSnD-DgKwYHVPvNY9e_KBkkZuoBv5XIkDUmic-0vPa_UdT-JH9XT5JQ0PWfH8CQNZo9hAc2XhsDtp347i-9BdyXpe_KwKhmrGpUeIRRb5VThoyb5zY1TSP_cJKm5odf_ma48nx3KwPWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95caa026c0.mp4?token=njX3KLiRAwduP04Loq4JOCnpzqvL6wCHsB50kJzbWDI4wtkckCwSZOyFLRYTsUfI-tLCxEHby5Y-Jcg1YV94F3tpP6Aq9_Ethg8BZ5VeFvfRanNArWRaTgOT1YgbjfR1D3MKTeR5kukW3PWTQ8zAyKLuRQM2M2jSf77ZBAH1bl6e742DKEEc6UHmrJVchrKRCA3qtNM8y7jSnD-DgKwYHVPvNY9e_KBkkZuoBv5XIkDUmic-0vPa_UdT-JH9XT5JQ0PWfH8CQNZo9hAc2XhsDtp347i-9BdyXpe_KwKhmrGpUeIRRb5VThoyb5zY1TSP_cJKm5odf_ma48nx3KwPWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد مقر خاتم الانبياء المركزي على هامش المراسم: لقد فتحت تلك الأولويات الدفاعية التي حددها القائد الشهيد للأمة، خلال الحربين المفروضتين الأولى والثانية، الطريق أمام القوات المسلحة للرد على العدو. لقد حققنا النصر في ساحة المعركة بفضل جهود المقاتلين وتوجيهات…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/80709" target="_blank">📅 12:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🇮🇷
قاليباف:
لقد وقفت إيران والعراق معًا في الأيام الصعبة والجميلة. ورغم أننا تجاوزنا فترة نظام صدام البعثي المريرة، إلا أن الشعبين، كبلدين شقيقين، وقفا معًا للحفاظ على سيادة بلديهما، وساند كل منهما الآخر، وقاتلا، وسفكا الدماء.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/naya_foriraq/80708" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3f19945.mp4?token=E5BWfHaZu02F-xPwNNAy2CAk_1RorxzJnzIbRMRpxvahuXtj0EtqjkdCsDEpptK3-wfG0BLafSIJfBvuohjOhcOlPVt6cJ3dDttJZ5d_02YlmyQ6ItgXrbcvrr4PxG7te9BpIofYsxxmIKaoV4Yk_zPzE5_FM7ymIpyLIrayt7YnBlq7XeLpk9p6CV5Zab4eF_EuM9qKCgDIz52OL2wXsjXzsiDofBsxD1RUn_z9hZzvgTEhOYrWB6hGLFppHSZ0fL5L5P11TxdZvD15Z4PUMC8kvc_CzefGFSZ2OfTcxeslvqH0W_DlDil8ZYEQGHXExtOO_VTbrsnV98dizcRwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3f19945.mp4?token=E5BWfHaZu02F-xPwNNAy2CAk_1RorxzJnzIbRMRpxvahuXtj0EtqjkdCsDEpptK3-wfG0BLafSIJfBvuohjOhcOlPVt6cJ3dDttJZ5d_02YlmyQ6ItgXrbcvrr4PxG7te9BpIofYsxxmIKaoV4Yk_zPzE5_FM7ymIpyLIrayt7YnBlq7XeLpk9p6CV5Zab4eF_EuM9qKCgDIz52OL2wXsjXzsiDofBsxD1RUn_z9hZzvgTEhOYrWB6hGLFppHSZ0fL5L5P11TxdZvD15Z4PUMC8kvc_CzefGFSZ2OfTcxeslvqH0W_DlDil8ZYEQGHXExtOO_VTbrsnV98dizcRwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كبار قادة القوات المسلحة الايرانية يشاركون في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/naya_foriraq/80707" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=c3n2r3NJjcSMH1l_qnrJzua3xVQxbGZO1at0BL9A7UdUPTpfwPfhtW4VIve18GNBN_Zi3Rnx0GYrgyK6afNCQm2dT1FMTYaRqQXfp497gT-NxPIJYQneDQwY7Uer-Ahg4MMmCjUbfsYuiBJ1AImymmrLvo3bQN3OcwIaB3QuGlmF4kG8nDUMpLBokb7XVBLZXxD23v2VJRzdzQv-gVkp5FFHTE2-dFXFDthwOuBfl0-m4dy_sXuDyFI_4IdhNCv58Cl6yBCeFzoT6kqfNxGfCL0sM0o5kVHRzPl4btEJuvARwjaZVwdudPfW8tBTDI8vBO0Z2MUEoh-csM0FxHaipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=c3n2r3NJjcSMH1l_qnrJzua3xVQxbGZO1at0BL9A7UdUPTpfwPfhtW4VIve18GNBN_Zi3Rnx0GYrgyK6afNCQm2dT1FMTYaRqQXfp497gT-NxPIJYQneDQwY7Uer-Ahg4MMmCjUbfsYuiBJ1AImymmrLvo3bQN3OcwIaB3QuGlmF4kG8nDUMpLBokb7XVBLZXxD23v2VJRzdzQv-gVkp5FFHTE2-dFXFDthwOuBfl0-m4dy_sXuDyFI_4IdhNCv58Cl6yBCeFzoT6kqfNxGfCL0sM0o5kVHRzPl4btEJuvARwjaZVwdudPfW8tBTDI8vBO0Z2MUEoh-csM0FxHaipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كبار قادة القوات المسلحة الايرانية يشاركون في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/naya_foriraq/80706" target="_blank">📅 12:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=q60A_DMv2SSSe236sRLBFhBgO7Ta-EL3BcnJKLs2kBzUIxKF68fH6xWnT66RQ9526BfuiPnNkw3SLh_BOO__9Ey-TBdkRjOXYbL9WW2yIaZg5DFYsZElHXhTscc8HPh1m4SVDsZ8F3yDUmyE1687TZO56bnj_rJogJYPaufZjpPaEmdi1DZE-w2EmvKh0JtgZVB3jyteuyNpf1kfABXtphovSA-0HqU_VsGjpBAab5h4U5TTqcBadIgosS2GLIBODx0mNXuVvISsPOjJ8YjZHL40ia5enhrJVD5fWwRQMd4vNgu1cd9qZBhoaHcstX7OOIJtaUu6hBDPCViT99tk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=q60A_DMv2SSSe236sRLBFhBgO7Ta-EL3BcnJKLs2kBzUIxKF68fH6xWnT66RQ9526BfuiPnNkw3SLh_BOO__9Ey-TBdkRjOXYbL9WW2yIaZg5DFYsZElHXhTscc8HPh1m4SVDsZ8F3yDUmyE1687TZO56bnj_rJogJYPaufZjpPaEmdi1DZE-w2EmvKh0JtgZVB3jyteuyNpf1kfABXtphovSA-0HqU_VsGjpBAab5h4U5TTqcBadIgosS2GLIBODx0mNXuVvISsPOjJ8YjZHL40ia5enhrJVD5fWwRQMd4vNgu1cd9qZBhoaHcstX7OOIJtaUu6hBDPCViT99tk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل نائب الرئيس التركي والوفد المرافق له ضمن مراسم تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/naya_foriraq/80705" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وصول وفد سلطنة عمان الى طهران للمشاركة في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/naya_foriraq/80704" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P555MEEgjnpvFd7CH5F89YYSCS2dzlOLy70Gpb1x5huRJyc2geXCYkgMdoa4OW-yO-Ce15mbZa_mmjnQD_2GR9yr9eyVPiF2yf5YtVh9lCGSkoqIuPrbTTM2GPjlX4hY1-8ZET2L1dhLezvN3n944e3y1jdfkfGF2WN1ciBe-rYzKgNVV8andY5WFwtT_jy0ryUqfKcJhBPUhpNNM4kKyECIu_CCih3zKjzZgizuVuol3GW2TB6D7P71LSF3IH4_vB09ukMXvHegECrkSQm7OZnBAn4eMBmjOO-8bAjICBOcjjIH05bxANnnFGFBLdegTnoKdanaJVpZmRx0KF7HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أكرم الكعبي الشجاع</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/naya_foriraq/80703" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مشاهد جديدة من دخول نعش قائد الثورة الشهيد الى مصلى طهران</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/80702" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9252cf910.mp4?token=LnZb_fIHM3JTPu2oAywi7XGaVuUlhrjNcmbNNQXajIU5j_D0Y6ugcce0rSdceNICv5HQv2pqph-nwuJwOdqH0qkhVvgZWuKwanuoExwVgGGRMKK8OG032JpBI3lY50VkYX_TvSMxWLw-di6J0Qni7iJ2-TreSFDrX9HmVXuBHZYIv060QVKzNltRlecZx7kZk9L6r08XwgCTO9m2kVoZyvQYIskWM6qW9xfK-SYDOS82i0VXXKnqCLuQO7OQT6YNJQjN5aNzw7uxiuFOKKWRI_tHGINeeLkVw-FwRKwmuFykfWGcdA63B88yrzFO6Ky1J1rH2a8tbEQ93DHszFm3jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9252cf910.mp4?token=LnZb_fIHM3JTPu2oAywi7XGaVuUlhrjNcmbNNQXajIU5j_D0Y6ugcce0rSdceNICv5HQv2pqph-nwuJwOdqH0qkhVvgZWuKwanuoExwVgGGRMKK8OG032JpBI3lY50VkYX_TvSMxWLw-di6J0Qni7iJ2-TreSFDrX9HmVXuBHZYIv060QVKzNltRlecZx7kZk9L6r08XwgCTO9m2kVoZyvQYIskWM6qW9xfK-SYDOS82i0VXXKnqCLuQO7OQT6YNJQjN5aNzw7uxiuFOKKWRI_tHGINeeLkVw-FwRKwmuFykfWGcdA63B88yrzFO6Ky1J1rH2a8tbEQ93DHszFm3jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل الرئيس الطاجيكستاني والوفد المرافق له ضمن مراسم تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/naya_foriraq/80701" target="_blank">📅 12:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2919107021.mp4?token=cL47DVImh0I0drqrcfqXOXfLwDlCCecGckq0cc7ZtqQkl1vXy74v6JOrMbJ4axtq2WLi48suabI5SzdmTtyWloIGriyFJ5PALTXet8GlgxanRbWfWBoVKCH0Sn-X7zRdcD7UHew6kzoRvdOpdVMCMLyX6REDlpChZ2gQF5t1FYquv-6Tspdf2yGlHdXiGCuNz2HhSLRemx7eFaN-mkvFox1xeiYAuubdH-oi7Ms5QXEFK137mPQX1RAejVb9dHSgEQ-aZfALbT1yI1idGNvTYhCUPdOTe6AHqd6x6XlK8PRbkZNjlG90J8oP4aPicMXD1a275tc-2ntU1CDNi294GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2919107021.mp4?token=cL47DVImh0I0drqrcfqXOXfLwDlCCecGckq0cc7ZtqQkl1vXy74v6JOrMbJ4axtq2WLi48suabI5SzdmTtyWloIGriyFJ5PALTXet8GlgxanRbWfWBoVKCH0Sn-X7zRdcD7UHew6kzoRvdOpdVMCMLyX6REDlpChZ2gQF5t1FYquv-6Tspdf2yGlHdXiGCuNz2HhSLRemx7eFaN-mkvFox1xeiYAuubdH-oi7Ms5QXEFK137mPQX1RAejVb9dHSgEQ-aZfALbT1yI1idGNvTYhCUPdOTe6AHqd6x6XlK8PRbkZNjlG90J8oP4aPicMXD1a275tc-2ntU1CDNi294GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل الرئيس العراقي والوفد المرافق له</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/80700" target="_blank">📅 12:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUqcF8PqDw56Mg8ETH5geEmFS5cBPNXA3742_aMxkonEuzM-wLsy8yA99p63a7TN6wWJWYgpIEvHjjUzaI8goB72pGFOOz4wc9Q_fwQGVJIyNVxXGt_TzZJZBazMLMkUX9HXr8cWjrEJd3fHdI38Cq2ZaVVaELrrhlDCkD-KcNO0gDex3Z2C6VeQKA_EUSgCZRK5AotahE2L2LbCnhx9hXWyWFURYarSC2jTkQCDnY3C0z-01rcei_5IeiHPrpmpAM2sUtTSG7xKix16xwv1JjSqDtc4xb4uB0ghtXC2DzB--t22d6HkEriG39ecZCW3WWZjf8icGTCct5a_K_pdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من المبادرات الشعبية العراقية الساندة لبرنامج تشييع السيد الخامنئي..
فرق تطوعية ومواكب حسينية عراقية تعلن تأمينها 450 الف وجبة طعام للمشاركين في تسّٰييع السيد بالإضافة الى توفير عدد من سيارات النقل المجاني</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/80699" target="_blank">📅 12:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d928237333.mp4?token=UW86wHgkzWoT_wF0qStoRkNfkqq4B9germmoGeJjWrMl54KBHlQk7yMxtogvTJKWgveNBYQ_tlE__L107tMZJZZ4scmiyAnbLhPMnVp234PJSX5DIAS_YPXpbtn6IKrnVMWvZ4IzphUGalFe2oXRXXq_0FplP6wDZQHuoHr8wERDGhBJzMfhJ3O0GEeUJpolT0HREDsBXgF0Vttcj_qb9SNMiqTJyEeB3XtF5H0g_Vl0UGMoiKqlq5ddwcOmyahbUIfyjEm_83MGz-CDfNcpZ53kiGBoXuFlbwBODVlZ2AbZh-DxoE3f1uGg1a6P6VNgWLeV35fyZl1faTZS9keEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d928237333.mp4?token=UW86wHgkzWoT_wF0qStoRkNfkqq4B9germmoGeJjWrMl54KBHlQk7yMxtogvTJKWgveNBYQ_tlE__L107tMZJZZ4scmiyAnbLhPMnVp234PJSX5DIAS_YPXpbtn6IKrnVMWvZ4IzphUGalFe2oXRXXq_0FplP6wDZQHuoHr8wERDGhBJzMfhJ3O0GEeUJpolT0HREDsBXgF0Vttcj_qb9SNMiqTJyEeB3XtF5H0g_Vl0UGMoiKqlq5ddwcOmyahbUIfyjEm_83MGz-CDfNcpZ53kiGBoXuFlbwBODVlZ2AbZh-DxoE3f1uGg1a6P6VNgWLeV35fyZl1faTZS9keEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رفع راية عصابات داعsh الإرهابية في محافظة ديرالزور بالقرب من الحدود السورية العراقية.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/80698" target="_blank">📅 12:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMwR7-m3jvQZTajwGyOGLQLB2munHPb_CMQyKZy-KE-UwDqOd597JiJWHZkeOBc3Q8J_8ATWUT1xPwzRovQ8xtnhwMUByGp5I_FtdAV7nla7FdBxLN5JteqQwsD7exyaXsLoZiLkBt9Hw_qTfU3mi0-SEXbbEPW0z6LFIJ8-myL4Yjg3XkRfKgvvDo85tmpbHjSQF0sBAH-pycvIjYxdR05TkReJ8WEUSNW-3lVtiSaXBEbQBEZXsELhVFrEfGBIXScC00tLaOpSrPP1KiFKeLWCLlqO4DYRkifYEzcMLqfAWbhKeN4_v0zja2_5FL4W_8Bf5ImdvmTV2uok3ML2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعيل بقائي:
يصادف اليوم ذكرى واحدة من أبشع الجرائم التي ارتكبتها الولايات المتحدة ضد الشعب الإيراني. ففي الأول من يوليو/تموز عام ١٩٨٨، استُهدفت طائرة الخطوط الجوية الإيرانية الرحلة ٦٥٥، المتجهة من طهران إلى دبي، بصاروخين من المدمرة الأمريكية "يو إس إس فينسينس" فوق الخليج الفارسي، ما أسفر عن مقتل جميع ركابها البالغ عددهم ٢٩٠ شخصاً، بينهم ٦٦ طفلاً بريئاً. ومن المفارقات المؤلمة أن قائد هذه السفينة نال وسام الاستحقاق من الحكومة الأمريكية لارتكابه هذه الجريمة.
إننا نكرم ذكرى شهداء الطائرة الإيرانية ولن ننسى أبداً الجريمة التي لا تغتفر التي ارتكبها الحزب الحاكم الأمريكي آنذاك.</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/80697" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28885a59f4.mp4?token=f-2zKA3nhEFGdE0akByMPGkiiz2dTm7kuXPXU0c0GSn0l0ser7-5rBxq5guCBkhNx4Wclf7UXnCYgVOkNtSkBUWLisoKNfDCc6f1JBOXDBpg7Le2uk4YTJNynY29KpWjAa-N3QobR9FklH1UvkOmcbPoLhhuyAWc3nAOHLNt333Paq3LRPleChE1UgDoh3DUm_H6NzkifgjBiQRHy6PP2ZGny7WCdVtFMzq0ASJsRjT7OvD6QriHCPl605axU-gTsllsP4KZhaK7AqnFnCmSdQBh-NKnoVJVoOlUCM3vPy4AtarQ5MGYLM8Wyo37SF0ZjmI0NoSloPRjOe5jQ6MOiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28885a59f4.mp4?token=f-2zKA3nhEFGdE0akByMPGkiiz2dTm7kuXPXU0c0GSn0l0ser7-5rBxq5guCBkhNx4Wclf7UXnCYgVOkNtSkBUWLisoKNfDCc6f1JBOXDBpg7Le2uk4YTJNynY29KpWjAa-N3QobR9FklH1UvkOmcbPoLhhuyAWc3nAOHLNt333Paq3LRPleChE1UgDoh3DUm_H6NzkifgjBiQRHy6PP2ZGny7WCdVtFMzq0ASJsRjT7OvD6QriHCPl605axU-gTsllsP4KZhaK7AqnFnCmSdQBh-NKnoVJVoOlUCM3vPy4AtarQ5MGYLM8Wyo37SF0ZjmI0NoSloPRjOe5jQ6MOiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لنعش الشهيدة الطفلة حفيدة السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/80696" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حزب الله اللبناني يدعو للمشاركة في التجمعات الشعبية اللبنانية والدولية المتزامنة مع مراسم التشييع المهيب
الزمان: الأربعاء ٨ تموز ٢٠٢٦؛ الساعة ٩:٠٠ مساءً.
المكان: بيروت؛ باحة عاشوراء- الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/80695" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30b0001f.mp4?token=RwNxSVL28ujthX_fMie3w4CrGs4ESrzRBRDHafeoIzi17jigMUwVXNRMFt1xENG159vjfgTa4TV7hmQk4cXsDYAJrZ6yrCkJeDwjDKYtrFKZg-TCLlvEXLFBJISRtEoMQCj2fdv3Gp-k2DqcrJ3JKwWcLN2pATHae-gpiYRzL5n002owSN4RaCimiFo_a2eQuHbvh9tNmFqx2HYo3BqhbS9zPqSFjqj-5ZDNnds6x7RUOIuIHNqNiCbKKMd70_MRAcFWglMuD-rQN-PLhTtxVVxyXD38TT-piuASyMhfkdKGvoGK5bLz4DA-HLrO1HGPu86lbLyPgxNelmtInHG8P4yXOP5iW6C88q_FOPzM_405CDdm4WkhxHcugt35JfGKPw4fvONG5JxYmtwvutKm2MYRM8W0p-PmD9jwDENfa5FQ8c0l2Gm6tHOd456Fmf-wuJ5rIO8dpVHdh1szWoWhc67qm51rrWsyvnqzaMP7EBj5Hczpr9q-PN2wBU1Jp8Kp4gSiIwMKCY9sWnPx62K0IJUfwqFMdT18B0baC_yNBBRWikO3kfs7wqANFILz35gomJdtQqUthMOMAzTIGoNl18zANNNG0rdJ0h3sDiRvVfNg2DIOYrNKuDgeV0juk2Ayf1wepDXf6gxaGlTLOpSojEy7IMXenf45x8NUlxf59ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30b0001f.mp4?token=RwNxSVL28ujthX_fMie3w4CrGs4ESrzRBRDHafeoIzi17jigMUwVXNRMFt1xENG159vjfgTa4TV7hmQk4cXsDYAJrZ6yrCkJeDwjDKYtrFKZg-TCLlvEXLFBJISRtEoMQCj2fdv3Gp-k2DqcrJ3JKwWcLN2pATHae-gpiYRzL5n002owSN4RaCimiFo_a2eQuHbvh9tNmFqx2HYo3BqhbS9zPqSFjqj-5ZDNnds6x7RUOIuIHNqNiCbKKMd70_MRAcFWglMuD-rQN-PLhTtxVVxyXD38TT-piuASyMhfkdKGvoGK5bLz4DA-HLrO1HGPu86lbLyPgxNelmtInHG8P4yXOP5iW6C88q_FOPzM_405CDdm4WkhxHcugt35JfGKPw4fvONG5JxYmtwvutKm2MYRM8W0p-PmD9jwDENfa5FQ8c0l2Gm6tHOd456Fmf-wuJ5rIO8dpVHdh1szWoWhc67qm51rrWsyvnqzaMP7EBj5Hczpr9q-PN2wBU1Jp8Kp4gSiIwMKCY9sWnPx62K0IJUfwqFMdT18B0baC_yNBBRWikO3kfs7wqANFILz35gomJdtQqUthMOMAzTIGoNl18zANNNG0rdJ0h3sDiRvVfNg2DIOYrNKuDgeV0juk2Ayf1wepDXf6gxaGlTLOpSojEy7IMXenf45x8NUlxf59ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من قادة محور المقاومة يودعون قائدهم الشهيد دون الظهور أمام الكامرات.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/80694" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb23b13f3c.mp4?token=YC8ohGfEpvnLgSjZ3-jQyooPgf2XaF_MZPMo5jnUYlaKkSx0HSetM6kvvgYfobMBrVX-jZXNHNekFG2zinuI8FTOebZTy7VRDz2kmYrA4NcuXGoSBT5wCOUIssfrDYmiQTjH3qaWyEX1u0ofC5xZBIyG9RqzU8NIq_5Tzb5RRyjqw87-dMsGAw9yuTlvxZ7eGPT4pUxk-xZYATlNWVctpmtD6MSI8MosS_RkCZEkmxdhNmdULa0MMaUx8UcDf85Eh8FajQDacDiyqTpl5NDqcTNetVKQQADnB5Lg8SpW9Xk7FKSm8O-Jd7grvyKhhA7DrCHFfexwlkeGrfrbk9Sk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb23b13f3c.mp4?token=YC8ohGfEpvnLgSjZ3-jQyooPgf2XaF_MZPMo5jnUYlaKkSx0HSetM6kvvgYfobMBrVX-jZXNHNekFG2zinuI8FTOebZTy7VRDz2kmYrA4NcuXGoSBT5wCOUIssfrDYmiQTjH3qaWyEX1u0ofC5xZBIyG9RqzU8NIq_5Tzb5RRyjqw87-dMsGAw9yuTlvxZ7eGPT4pUxk-xZYATlNWVctpmtD6MSI8MosS_RkCZEkmxdhNmdULa0MMaUx8UcDf85Eh8FajQDacDiyqTpl5NDqcTNetVKQQADnB5Lg8SpW9Xk7FKSm8O-Jd7grvyKhhA7DrCHFfexwlkeGrfrbk9Sk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبات الشيعة من مختلف أنحاء العالم يودعن جثمان الإمام الشهيد</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/80693" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjFFao67M8xMGiqyj0AiwWX-xTnJgcojt3t1bwgKFa5vOcBHOkdx7G28lzJWkzZWlRqJwwuMTqkiDAwBS7wMOle6LNpBl-MF-al7G5ljc3G01KWotemjliToWY1sQFheNPGAuv-8hqp5uY9Lu8vx1LD8AsCa7fyNbXWBb_1eTlx7kNWJkZ8evNn0AjzIG0gU1zQPUxDxZCoaU5EjgIfRqHyaQfT4TI7gBac1UJjt4Sf31f0gHTOpxrXBpwSogmqaKp3sqFyCJ7EeWRcpbzKNv2gpfY6-9cT1yZRPKp78IVkzLAqhwqnMfVfy7l_vEWQmvwrMvzVxQrYZTceAq7QITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpBbyw-aD10hdRWfUtDLohrdAtr08IGJ7cFIx69vBEfQPe0oCbXq6C14B_Yh8vXR7396qtmJMRnG_eY5eux-ZyoVwHfO3YnSHEH8tR1pgrWW_kxnfQuTojgc38ntGTF8Q1ADgV3KJt5DDviTKkF_qf0XsuESVf1d3yUnaV0K8ru3orpCOmb9QSNW0b_kGHL0ivWAJVPS-s78ZnVwWfFmmAEySO31tNFbRRzlm--liQwEgQpfzNAkegEr1LJl9qbQolcMJFy8MSq0JzxzNEnMml02QdRlbWh2OH_ohSByasgctjRQp20aAwpIt_VH3tiLHPzEuTiudWDoa7IdD9ELPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMnl_cH9cYGEeqpg06_1mfghiGdLK2PP-MdSI1hRBRdxQw-HgRgbmzItvqYW5NXMNIxeCuPQr6gOHdqov50iTdOAxitBB2JTyWd8PqMxAMyBP6P9fcq0wcpKbsJ0Argic2jKq8y15gxXeaexXqDO1h5keh7BO0Gq9axS1KuIQSa7ss8_hviM0VZRx0qFsS4wgHscq9Q31j-SWeLbm28FqQQjLV89VUxrkYMObZGRDjuWk8PDaDv_UluUWS6DrdAj-sdDGBM14C58ju9znQvl4YJzD_Lb8cg79EHc9k3Abup9ch406AVWHQkEDkAugLUNX-22kmvZxIFhfvYpDLdQvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لحظة وصول وفد هيئة الحشد الشعبي برئاسة الفياض إلى طهران للمشاركة في مراسم توديع آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/80690" target="_blank">📅 10:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqgCbK9F4rJuop3W2b-3sMoBD_YNImC-fnbeqzbKMqd_W5VrB7pw470DmMb5a8WInl6OhZEJshBdmsMMfyuDLyAHwRDRz_wkpZ5j86kPh0VbJCPIXVs4cNNWlQRdRY6ebV0TxrJ7XjoHuW0NvwB6o6rfeYYfkkMzV8p3QOIRvWvPcDMVd4k9FeAl1DrTbNR0D5TSws-qSGRGyR0lzOk5etX0phHj-vgCIRhPF4kfuuphSQAl8MM-LiUjlSmGdTaV9El2uqywiZyzjMEFHOjRrKQu4zsRLCjsABmJiqM5HpdDCK9gdUCCmCGjuTnSZqnK7mM5gPo6-DjcKreE1G9gfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTaCE7o9Zk3r43iBQkkLtLxIXeyABB_OBZusxGBJWRmdU_oJKhO19CjSy3SCUO-EIMrNyla5e6v6qPemRMXg6Xj39YIAK_sXK0IY4EGGLDa6G-25bghbqBBEtvKaPb5i_HILUHpQOqZGwAO4P1Dhq_8TVX1FtcXejCMr2CaTUP8fwSY3nzfReJcChObQcLxurTDnbUXa2wzaXBqx-u7YhzD67MCbUl9sFk1drUeDsTQa8FxrBn1Rl4knBZYKSdiv-Umfk2PVkL7e-PPdCzEM3Ay97s-q5_20sX1-wQwzwUotjt0oHewyD46PM7_VkD3ckPmU2imtN_90RKA27CrxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skUa_EbQLN4tdQfhFoWUsp67lsNv3-FbMX90vZ9tKtxf3pXmEPDuZjqiqf58lIC9ku85Nyj7n_hGlDKc9sg-t2TgGrb67LQE42KvMnHtvkob-o1J_aAa1UmYRInoq6lIV2HSXwKfbqOVg4t1CJrb12ZdqvzRf9oUDkK5PMpz7ib7S-jNdQ0iXwVqaL2zoW-d6mTOYIzbQBBzqWjTKyD3ZiQQkKj7Mh9o6F-ov6D-MIDex6AcIYvBUDKW85hI2cxM67Z92_zzznoLmD1fsTL0BLGuE6k9mdd-wJS5nlGU1zcmk2kW_pqevruvVEZtz_-WXm8Si4eEhcFyhfyMK-JrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk6A_8d_V30PrR7WMZpoX_EmWHUcb_ntKDXYuveEx_fyrjKOkL_10kA3tgzWFxytGbvTmnjPvJo01DMMnt8lzwxDs5ocUbu8Css5DToKKuaECjysGXWgjHZdZG3KAfpZbDlovmF9sMJ1weRN4CybZ_HIJlXhF8fB0ziiPki7-k96MCRBOEBAVuW5V53WA7pyuIbaXyGN2Mtxwl5oVMRirXV6T8PkfcCbPdGlGGbWAq8B8vdIE9vZ8XD4WhucVKFtNuRyen7oPSGcwloViFYmzbc1jAI_HvBbXOoNiyisjEbmGC8SF6N36uqnGl4Pq1zpuL5zD8iFIivoFzB6XajZug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاليباف يلتقي برئيس مجلس النواب العراقي هيبت الحلبوسي في طهران</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/80686" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9b81b411.mp4?token=VFks9gBkyd_vhXowtDd44LRG7o0S4sr7LwvST3kT7aomWtg2g9O5MEPicum3Ltck3UuCXXFiA_AM3UhtS7XGSG-Tei9NKsZLhdJgkJOCcAD0R6cqVZnVS0br4ZDQ0nkQ7aGv47WIn-datdVjeryCK976oWRa9cxP4AgmZ8O7SYPLYwAYuthgq4zADz0u5qCG6KBpuaFott2xJ6XUofE4Wib5jYLu2xxTVIy4XIRlH2uPbsROwocz1mt9690KURxc12vqn2GJv-LlKU41p8aLuLlgEqzn4tj9Ow1GYEahtfZxXXL-6ZPFHXv3upZ7ZXpw_UnSbNYl8ymkbpUfUpcmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9b81b411.mp4?token=VFks9gBkyd_vhXowtDd44LRG7o0S4sr7LwvST3kT7aomWtg2g9O5MEPicum3Ltck3UuCXXFiA_AM3UhtS7XGSG-Tei9NKsZLhdJgkJOCcAD0R6cqVZnVS0br4ZDQ0nkQ7aGv47WIn-datdVjeryCK976oWRa9cxP4AgmZ8O7SYPLYwAYuthgq4zADz0u5qCG6KBpuaFott2xJ6XUofE4Wib5jYLu2xxTVIy4XIRlH2uPbsROwocz1mt9690KURxc12vqn2GJv-LlKU41p8aLuLlgEqzn4tj9Ow1GYEahtfZxXXL-6ZPFHXv3upZ7ZXpw_UnSbNYl8ymkbpUfUpcmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من البرلمان العراقي واقليم كردستان العراق في حضرة السيد الشهيد القائد علي الخامنئي.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/80685" target="_blank">📅 10:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735bf69606.mp4?token=Ew7ZYHvEifiHlByBkp2Qxy96d0U5zEmwIXFDlH7H3lEYcXvnu9vkaHBZvegSzdJh7zv5kJ-p6odTALfKRby0iLKhRxppE9OOz8BUeJcOBI5Vw0KEj3BUicCZna-Se7xJaLVIXrmeR1eBKXSitYfLULqALvOCkj_W3Ka223VdFrFb1Rhzw47gxuibkOmvvv2eJWq8E4O154hYflq0pMECo3-wnyf_7Hs0H_f7gnPsrSlXv8jYSDXMwZiH_SLM_Gnbz8qJvJAYztW4Bu9zt6VcEdyqQ_gRHFPyzGD08oAGFgQglRAW_wEgxD4t8xgcIPf6waqCuAlkr2npPEpV6W-oPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735bf69606.mp4?token=Ew7ZYHvEifiHlByBkp2Qxy96d0U5zEmwIXFDlH7H3lEYcXvnu9vkaHBZvegSzdJh7zv5kJ-p6odTALfKRby0iLKhRxppE9OOz8BUeJcOBI5Vw0KEj3BUicCZna-Se7xJaLVIXrmeR1eBKXSitYfLULqALvOCkj_W3Ka223VdFrFb1Rhzw47gxuibkOmvvv2eJWq8E4O154hYflq0pMECo3-wnyf_7Hs0H_f7gnPsrSlXv8jYSDXMwZiH_SLM_Gnbz8qJvJAYztW4Bu9zt6VcEdyqQ_gRHFPyzGD08oAGFgQglRAW_wEgxD4t8xgcIPf6waqCuAlkr2npPEpV6W-oPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من الاحزاب السياسية اللبنانية تودع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/naya_foriraq/80683" target="_blank">📅 10:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a31886a48.mp4?token=awldgQv6aQPyUcra4IQyMklWL0KZsCTam6u5YTrF8Vsry8LEwvtthl3o4fwo7RpZcaoe3gQAE9vUN0HvU3xpmqd9fo1RKDdF62NEVG-LAslMs0IV4eK9H_8-k38RB5MhWCqCKtZXsDBarkQ4VqlrBLP02LeVat1o6R1X1FniSVuPoxibTkRCucar135mOppjtEIWcooMh0Qau8d5_CGkBYx-i3xuo3IAz5d5z5iDcUfLQrzDgPP32KA7qVp5uLoNRxT_vBN38Ru9FMF_rAHBH5bZOHaB6hvdMNhZehJx2sYj8-x1WPE2vKohrdUXRDuqnzf1kRJe9-0vjYP2MYTsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a31886a48.mp4?token=awldgQv6aQPyUcra4IQyMklWL0KZsCTam6u5YTrF8Vsry8LEwvtthl3o4fwo7RpZcaoe3gQAE9vUN0HvU3xpmqd9fo1RKDdF62NEVG-LAslMs0IV4eK9H_8-k38RB5MhWCqCKtZXsDBarkQ4VqlrBLP02LeVat1o6R1X1FniSVuPoxibTkRCucar135mOppjtEIWcooMh0Qau8d5_CGkBYx-i3xuo3IAz5d5z5iDcUfLQrzDgPP32KA7qVp5uLoNRxT_vBN38Ru9FMF_rAHBH5bZOHaB6hvdMNhZehJx2sYj8-x1WPE2vKohrdUXRDuqnzf1kRJe9-0vjYP2MYTsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عائلة السيد حسن نصرالله والشهيد القائد عماد مغنية وقيادات المقاومة في لبنان تودع إمام الأمة السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/naya_foriraq/80682" target="_blank">📅 10:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36e33cf4.mp4?token=ci-zYOS_s1_fwtTf_u3El0LHQ_H6MUZTG3pVkqa8TBZQMguWC97aG00iXSif80xhyhPxmK0MVF7pau1_BRXmecZei9SmvaFExD80VRSTPbBO8VFblQTrLdm1GA4xD1_Db6OA3ovHd-ex-yF7IDZIuEk_oqOCB5UsikUkT59B0uBVRSuLmjVCZvvpbCuTtydMnLf8JxNiS8DOuYi3jcLSmPLzBbgFoHIzC_8YQ9u7BChx3PlDH-EwVXZiIaB3GOhfNLGRN-k93mf3mSjBYJ91BeNdwQvVH_8zBnoqNdiAw4p3k9P-NwblDp1ht0LUf4_Cm4A8bEjdpURr6e3C2QI7z0eAl3oPicw6Kcl4SO2zobEW4Yr1TV5d1gmMRIBvMB_Qr2kSXQUrDydtKidioabTotvrWKRplSeJ5LMOEj5fHSLYzFas-C0_j4ylre7FK8N5QGZ7Cg0o65crF1tOHWgxnI8Vs530i_v6ms2zhxo6JpT_FxaTnotmqQuiotZunUw6_0An8lmweTdyziX7nBeGbvukgVSx1gjKpajw5veocFonNB1rQwmi4v2bO6MMrZb3odgUDOLYQlYrqYoMwtZw9dU9rz7pmZb8HAA1BUankzv8ju2L1blJo1fri6mkTHTFa-k0v5AVYUmF0fRpSnaIIIOwzj_TMg3A8atIJazwpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36e33cf4.mp4?token=ci-zYOS_s1_fwtTf_u3El0LHQ_H6MUZTG3pVkqa8TBZQMguWC97aG00iXSif80xhyhPxmK0MVF7pau1_BRXmecZei9SmvaFExD80VRSTPbBO8VFblQTrLdm1GA4xD1_Db6OA3ovHd-ex-yF7IDZIuEk_oqOCB5UsikUkT59B0uBVRSuLmjVCZvvpbCuTtydMnLf8JxNiS8DOuYi3jcLSmPLzBbgFoHIzC_8YQ9u7BChx3PlDH-EwVXZiIaB3GOhfNLGRN-k93mf3mSjBYJ91BeNdwQvVH_8zBnoqNdiAw4p3k9P-NwblDp1ht0LUf4_Cm4A8bEjdpURr6e3C2QI7z0eAl3oPicw6Kcl4SO2zobEW4Yr1TV5d1gmMRIBvMB_Qr2kSXQUrDydtKidioabTotvrWKRplSeJ5LMOEj5fHSLYzFas-C0_j4ylre7FK8N5QGZ7Cg0o65crF1tOHWgxnI8Vs530i_v6ms2zhxo6JpT_FxaTnotmqQuiotZunUw6_0An8lmweTdyziX7nBeGbvukgVSx1gjKpajw5veocFonNB1rQwmi4v2bO6MMrZb3odgUDOLYQlYrqYoMwtZw9dU9rz7pmZb8HAA1BUankzv8ju2L1blJo1fri6mkTHTFa-k0v5AVYUmF0fRpSnaIIIOwzj_TMg3A8atIJazwpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود إعلامية من العراق ولبنان يؤدون التحية إلى الجثمان الطاهر للشهيد القائد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/80681" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkDsxYHn1EvH-n_A2V1nsjTd7vwSgPyIIM3QE1jCTbgQ4-2OaIZW3C-yuzQ9bzF8NJOUbfI067tdUaphHpxTSJtMjue5Tdx8FStjG40G9jzJ1DsEfmb1PTDkpuH7LmhG2rbpQDu00UAaa73PDNpF9qplw5UPBKUERZTzCe-FFaYQJeYIRQluRCxX6BgIl2M8qQTveVekWCZFm9JGr-DI34Qwx7Pk0UaKOQKSzzQS4B9BbNjBk27S3Tmd5ZW6IFnHjguVxMGbmuEnGAdqVLOuzd5wGLFuCITtoqVm8zX2qHHGzuru445um6GWYC08D1GoLp7EGUn4ZfUiV8woTAYMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف يلتقي وفداً من حركة أمل اللبنانية الواصلة لوداع السيد الشهيد على الخامنئي نيابة عن الرئيس نبيه بري</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/80680" target="_blank">📅 10:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a61c2f6831.mp4?token=RW7iQmJdd2U9PcZEg-UDZ2xg9yijX5d05xZsHJzCudUEnpMBLN7gsCdbDwxJdRpVa6HPBrxCTNog73KTIqMRG52IGip0P5p3dJSzDPNTztuM49hTsw1K-its6pFoYF1yN384sVoGiAPzw-WnRYbKevHL_H8yvl4G3VGnGg9E7J_yVv6_PlUHvMQ6lsEWPJI5P9KCqMXMk71AOvfzLpZHU7cwW7uHFDxYUWvS0qwymwQzPXDxe4dknXUWDaCKzmYjocdFVdk125_Jm6-mYY1mRmq3MAj73PN3ObePQ10Pnz6IlgnI_6tbYKD5-eU7AckOGwXK87YaUhnlYhIe021VAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a61c2f6831.mp4?token=RW7iQmJdd2U9PcZEg-UDZ2xg9yijX5d05xZsHJzCudUEnpMBLN7gsCdbDwxJdRpVa6HPBrxCTNog73KTIqMRG52IGip0P5p3dJSzDPNTztuM49hTsw1K-its6pFoYF1yN384sVoGiAPzw-WnRYbKevHL_H8yvl4G3VGnGg9E7J_yVv6_PlUHvMQ6lsEWPJI5P9KCqMXMk71AOvfzLpZHU7cwW7uHFDxYUWvS0qwymwQzPXDxe4dknXUWDaCKzmYjocdFVdk125_Jm6-mYY1mRmq3MAj73PN3ObePQ10Pnz6IlgnI_6tbYKD5-eU7AckOGwXK87YaUhnlYhIe021VAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود كبيرة فلسطينية تصل لوداع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/80678" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c971af3f.mp4?token=sUek6XXjlqVDFAroeyjS4pMGOv4fY-O8imcPYvea-bbLu0zbyIiQZd7uN_QKGUQ0-oKZj8m8STnX2qIc0ruHBU6tePud_P59O5RopHIjL8VuRHKxKaRlETtuR7rUhvvWKuu6LTGzJkiPEAVc6yjWXzXqVFw70NWcbPNu_imBr5P-09hA5ItADPHgvlMq4s_vot6OyCJVLB5h4iTerozPzZUsOt6b20Mj4CpeLcXYO8rW0DAIhHRkhaWlhsF-QIYCr9nbbgXL3ndIyfH-R_VMAaxRwoL4XdHyoseX_6Bd1_x_XFptMuexV0-xOi-QL3e_OMyVT83S-jm1BQ2dm7MKNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c971af3f.mp4?token=sUek6XXjlqVDFAroeyjS4pMGOv4fY-O8imcPYvea-bbLu0zbyIiQZd7uN_QKGUQ0-oKZj8m8STnX2qIc0ruHBU6tePud_P59O5RopHIjL8VuRHKxKaRlETtuR7rUhvvWKuu6LTGzJkiPEAVc6yjWXzXqVFw70NWcbPNu_imBr5P-09hA5ItADPHgvlMq4s_vot6OyCJVLB5h4iTerozPzZUsOt6b20Mj4CpeLcXYO8rW0DAIhHRkhaWlhsF-QIYCr9nbbgXL3ndIyfH-R_VMAaxRwoL4XdHyoseX_6Bd1_x_XFptMuexV0-xOi-QL3e_OMyVT83S-jm1BQ2dm7MKNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبهة تحرير فلسطين في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/80677" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906f02df65.mp4?token=nhvJeLijqtEwfpr4CuSdpPK6iGmhx4AafrurHJSq0MkEd5J3BqXIEDnCPgcs3EPUhevneyoh-BGB9BawS6q3TI0vaLq0h95zPwyYeOVpCqE9Ic_PtgeclmnOL8VDUsrg4XZ48tOH9yIAIGHFWf9NEp1e9gtQNisUeOvC_5aVxrL7piC7SAnCNubzo_ak1ZyZa-p2tCiN_WLTtPGuuISIjIfHP9sHNd1vCuyQzCSk15vWZ12a4iirOcTlJr7hHbTD40B43c-EwL_EuOyRfwN1IiXXy3tFQmasAtdd8PB2DdiMyGMRnf7Cq3UH9qnZSsYq6ppEhYCQ4yiYAqlPqg9rVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906f02df65.mp4?token=nhvJeLijqtEwfpr4CuSdpPK6iGmhx4AafrurHJSq0MkEd5J3BqXIEDnCPgcs3EPUhevneyoh-BGB9BawS6q3TI0vaLq0h95zPwyYeOVpCqE9Ic_PtgeclmnOL8VDUsrg4XZ48tOH9yIAIGHFWf9NEp1e9gtQNisUeOvC_5aVxrL7piC7SAnCNubzo_ak1ZyZa-p2tCiN_WLTtPGuuISIjIfHP9sHNd1vCuyQzCSk15vWZ12a4iirOcTlJr7hHbTD40B43c-EwL_EuOyRfwN1IiXXy3tFQmasAtdd8PB2DdiMyGMRnf7Cq3UH9qnZSsYq6ppEhYCQ4yiYAqlPqg9rVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الناس الشجعان تتهافت عليهم الكاميرات والجماهير
نحن نحترم الابطال الشجعان</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/80676" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9716e3e815.mp4?token=FDScCs8Kze98r3jq6qPOKih2z8PDyzF_PSRmNnsZuWp22VCzRb8cBuXn0nKYIVfHsGFhH1HYEcM5NRVp8NwrFy3ZrkyUHGBgS7eTlPjSD6DfHNFpdI9qOeY0Sx75uP6k5kGmhWeWZDBERatN5HmHEI9iD2oNciZH5kdieNtfisIvEikFHdjH8SuWHWbQPfnxL_UoOyeV6pt7Yi8aUWsPxWC9HTNn0dLXXP1Ix0wQU-OBlnfft3u32SuHZkFp1bKf3Ih_vQCdZJwGvLDSRuok9-09LCLyMws4YPhevQ6r_aj-KWG_QOTbcq957CtngDpxWVly20YzrAsPC6XQrMtLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9716e3e815.mp4?token=FDScCs8Kze98r3jq6qPOKih2z8PDyzF_PSRmNnsZuWp22VCzRb8cBuXn0nKYIVfHsGFhH1HYEcM5NRVp8NwrFy3ZrkyUHGBgS7eTlPjSD6DfHNFpdI9qOeY0Sx75uP6k5kGmhWeWZDBERatN5HmHEI9iD2oNciZH5kdieNtfisIvEikFHdjH8SuWHWbQPfnxL_UoOyeV6pt7Yi8aUWsPxWC9HTNn0dLXXP1Ix0wQU-OBlnfft3u32SuHZkFp1bKf3Ih_vQCdZJwGvLDSRuok9-09LCLyMws4YPhevQ6r_aj-KWG_QOTbcq957CtngDpxWVly20YzrAsPC6XQrMtLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الجمهورية العراقي يصل إلى مطار العاصمة طهران</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/80675" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=BxuQ2AJn0Wn1067bg4sa3f5d8Z0jA6JgHAHORv6EqHuM45zr-s5h-Q6303s-lubKZWQrWI6I7kk_1xQNM3qJMklx_ZZLqA4WOSo302jS4OA65XYGWvwSeKOcx5sQ7-cYeOtKvm9g4ztg0CJz4nkrpVvjA4yz8S1XPWFjtKZRyu1jtiYCkZboM2e1vpMxPOEDTkMdIPVs7OYuwevBscDdN7BshyJkphn5KPlrqlqDlmh6WVs9z6-DU3VNpQ6eLoozp-WESU4f-StrR1HZji4oAiprUGTAue9zby7xnYSFdYA_2ZIKPlZecWUNZjyDNUqTKihchxtHl8UUfsJC5CULJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=BxuQ2AJn0Wn1067bg4sa3f5d8Z0jA6JgHAHORv6EqHuM45zr-s5h-Q6303s-lubKZWQrWI6I7kk_1xQNM3qJMklx_ZZLqA4WOSo302jS4OA65XYGWvwSeKOcx5sQ7-cYeOtKvm9g4ztg0CJz4nkrpVvjA4yz8S1XPWFjtKZRyu1jtiYCkZboM2e1vpMxPOEDTkMdIPVs7OYuwevBscDdN7BshyJkphn5KPlrqlqDlmh6WVs9z6-DU3VNpQ6eLoozp-WESU4f-StrR1HZji4oAiprUGTAue9zby7xnYSFdYA_2ZIKPlZecWUNZjyDNUqTKihchxtHl8UUfsJC5CULJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شيعة الهند وتايلاند وألمانيا يقدمون تعازيهم في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/80674" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007756c400.mp4?token=D8KO4DTeEsYoPRs0kKzyXQhAjbb54t1cxMGP3WADh3-9u8qVDRcBDZfMDg27Z1Aj1qnuvkIjb4umcyvBTZG5qR0xHDulz1xAoUgA4XZZ9p0vvefZ0WR159tgibJRl--kQxZ5sUSxD_Ut_di7Z0d7jTPjmAZng2fpSPzkBDeM_WK19_vpjXJgIIY34Tttjmxfhi1sA0a8aExJT635TtGT-GVNmLFNCEnl1yBXF1rfZ4sNSc1k7lF2qN3-81ong5URTNC8VcqddWmB1YGcRWKY_hEB-c4M1nKzhK_9iey1KkGa6cVIbTY-CuDFKsUIat36mNHfezBseVITCEPH4YnOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007756c400.mp4?token=D8KO4DTeEsYoPRs0kKzyXQhAjbb54t1cxMGP3WADh3-9u8qVDRcBDZfMDg27Z1Aj1qnuvkIjb4umcyvBTZG5qR0xHDulz1xAoUgA4XZZ9p0vvefZ0WR159tgibJRl--kQxZ5sUSxD_Ut_di7Z0d7jTPjmAZng2fpSPzkBDeM_WK19_vpjXJgIIY34Tttjmxfhi1sA0a8aExJT635TtGT-GVNmLFNCEnl1yBXF1rfZ4sNSc1k7lF2qN3-81ong5URTNC8VcqddWmB1YGcRWKY_hEB-c4M1nKzhK_9iey1KkGa6cVIbTY-CuDFKsUIat36mNHfezBseVITCEPH4YnOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من علماء روسيا في حضرة الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/naya_foriraq/80672" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204fb36bdd.mp4?token=LefZ66EW_zt0rs_VknBeNz2N2gtaviSUnaFvTl0BIDl48FTsvKHZg8_jQEo9OPc6545K5habMxa5x-lBUqFvrS7dw_Rmfuk8h2lm9MMsuW7cpaWQRv77OOhJ-UXcE28kJWrsi6fI8_GqWfVBuf44i8ZB3NqLxo_673Uz9oCwDHrEl85JwnLFnUEFL0uq0dH-dTNQxcLfxzOyUrR8hlmD_l8NMtmqSKwB0eWcXAXBh4_DG-MaXiH4BtvasMIORiQS-_02VJJQNAabdOn9l1AVB-8bOBInPf5cF6lHu71k50i3vWAIhqo4xTl8CqFCcMPaHlZwRcLjG5NeFj0eoeW2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204fb36bdd.mp4?token=LefZ66EW_zt0rs_VknBeNz2N2gtaviSUnaFvTl0BIDl48FTsvKHZg8_jQEo9OPc6545K5habMxa5x-lBUqFvrS7dw_Rmfuk8h2lm9MMsuW7cpaWQRv77OOhJ-UXcE28kJWrsi6fI8_GqWfVBuf44i8ZB3NqLxo_673Uz9oCwDHrEl85JwnLFnUEFL0uq0dH-dTNQxcLfxzOyUrR8hlmD_l8NMtmqSKwB0eWcXAXBh4_DG-MaXiH4BtvasMIORiQS-_02VJJQNAabdOn9l1AVB-8bOBInPf5cF6lHu71k50i3vWAIhqo4xTl8CqFCcMPaHlZwRcLjG5NeFj0eoeW2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيجرفان بارزاني يلتقي الرئيس الإيراني بزشكيان في العاصمة طهران.</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/80671" target="_blank">📅 10:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d0a2771d.mp4?token=NtORTpVCPowoewszSVZBS-hcWjbEWb1xqSZe6oLPnzZ3Y78PndUJnp-EqCi3vnUBlm9kVIw7ZUsIDf84sDCBg-pMNPo8Crmgo-IMph-oxcxEZMR_zcSXh7fwgnlYl9pnnW43APOMWi6BLNZY8IGoYGm_oq1e_pO2d_tmxByfjSEyR3RlRyhfb56a9ggg36QW8IXXI5cXOxiMacJce9eoPHckaVp85FDSwyhTzQ0cBhaeSR50_dvvO8jOJFW8WNJ_f3EBS88n2WszsNXEyrr-1hlQ4FJUAqrZ_l3H-9NJBsxxygRcZQ2FcHrQhEHB3lVLAeWaq9KjTSRo4DA3aLFs0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d0a2771d.mp4?token=NtORTpVCPowoewszSVZBS-hcWjbEWb1xqSZe6oLPnzZ3Y78PndUJnp-EqCi3vnUBlm9kVIw7ZUsIDf84sDCBg-pMNPo8Crmgo-IMph-oxcxEZMR_zcSXh7fwgnlYl9pnnW43APOMWi6BLNZY8IGoYGm_oq1e_pO2d_tmxByfjSEyR3RlRyhfb56a9ggg36QW8IXXI5cXOxiMacJce9eoPHckaVp85FDSwyhTzQ0cBhaeSR50_dvvO8jOJFW8WNJ_f3EBS88n2WszsNXEyrr-1hlQ4FJUAqrZ_l3H-9NJBsxxygRcZQ2FcHrQhEHB3lVLAeWaq9KjTSRo4DA3aLFs0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من جبهة المقاومة من سوريا ولبنان والعراق والمغرب وتركيا يصلون لوداع السيد الشهيد</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/80670" target="_blank">📅 10:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c74abecf.mp4?token=CPDwroqZqQbE9skcz4y768_btWYbZTptQZw-UUcrcyD5hgv7YGJV8rvpCvttroJxML4-wyhaVzK433iaXM20_2kltmZItoKlp7vsx5ELY5ah0tPVFrcNTDLMAzeuDCm42WFyCVz0BxU_Lfd8bHcEh5yiNbPZiYtDCK-iAAbA5jOwc_H93q8MROYivyq8ihzL0pXRr3FMq4EOO_jz-hhY8_9CLuoCUiDJszsUgGtKAkxU6J87qU-1bxWToNUxJRk8TUUKyz2U3OA0ome6OvpsnvSpb5kSbcDVTXwgM954Qdh58DdCrgq7yQYgLSbTaWDCl9eb7mAat95VpwRrXNdEXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c74abecf.mp4?token=CPDwroqZqQbE9skcz4y768_btWYbZTptQZw-UUcrcyD5hgv7YGJV8rvpCvttroJxML4-wyhaVzK433iaXM20_2kltmZItoKlp7vsx5ELY5ah0tPVFrcNTDLMAzeuDCm42WFyCVz0BxU_Lfd8bHcEh5yiNbPZiYtDCK-iAAbA5jOwc_H93q8MROYivyq8ihzL0pXRr3FMq4EOO_jz-hhY8_9CLuoCUiDJszsUgGtKAkxU6J87qU-1bxWToNUxJRk8TUUKyz2U3OA0ome6OvpsnvSpb5kSbcDVTXwgM954Qdh58DdCrgq7yQYgLSbTaWDCl9eb7mAat95VpwRrXNdEXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الفاطميون من المقاومة الأفغانية في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/80669" target="_blank">📅 10:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCxOdRGet-mnEZ2VkFiMOZn9NgoDUb1hWEL59iDHg-UxbxnjTtyInjWtlGZh4HB29Fl2qJjp4JIpPaqJXLgXTKUSbFdztRHb3APiJsHTT_NR8SRt-DsiKAIFLz7r3O8xuwfnpFszV0StGybx6PeeZl-Qgc6--NqrfDZjwn77ShteEhhO66iPaX5Fl0mFBBxHz46K5iZHPEfvwXsrK2VifGQB-dkBQqP4RRhUUW_7bEeN1T2Qqqvs-9p9nmue1aHd2Dy448pCT_8YW1iPRa4HYazz1kpy2N76e6fRKSg85ZoAeKXGm0Pt9QjAqrx8BUVYQYWVxKRIwo-fKuOZGgHupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوفود العراقية برفقة نجل الشهيد السيد حسن نصر الله في طهران.</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/naya_foriraq/80668" target="_blank">📅 10:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jm_QJc7vJvYF6_e_GGJgxJrF043numJvZSxT0UhlKA3ulmr-QQMBbD4TVDhjI2r1H_UkQczePU12Ghp0RM-z0W7haVWDvSyHtCt2zsYImn_sJ0m63nIoR_bYdEEQSgVyqylVRlh9PqcYG1neyZ_cqgt1B7r9Bl71VEt_m6HT0arz25rum2_U2YIxSRqlq8cok6zBD6N-ldNl-GUqYkMWXgllrhheZQzDFsCJv2XAliMft3fVneBFMr_PizYTWG1mBPuadTm42qflAebc3KwP8__sbI_OwsxzPjjYUOQBJhejle1tJdxC_owjNaw0yqoLRLBkzCK1axwtRGEHmGm6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZtXncATIbDqsDD-TjTzmI_yQOFIFNdIG5JLrafj9S6dMXCs3lEJE_90rf9JRurrHwyT45T03sGfxmbDjX6LWVFrhF5NIS0yYLHJwqcD2bgHRYy_-gQCyUVisYErd5wV2OCRovskCOlctZQw19X4G-J3fEg1djftIPnQ9-ddmWqtxC3PY09IaBW-ztYve6XfoCY6ZBaF5Z0qjG9erQZySLIVrhZnmvjRB2pdcPE7oo8gVqLxlSOWemg-vEQMd7d2KdyWbUIsNYZGowKYBM3clKG5RFfm1Bn1jO9HJrBKggLdWVYUoldRy7qEYImepX7LZT2BzKzK5wTsDhZd9yPxkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الشيخ اكرم الكعبي وأبو الاء الولائي من طهران خلال مراسم توديع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/naya_foriraq/80666" target="_blank">📅 10:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846eb2bb69.mp4?token=DNhbEfZUmQPZA-nwRgcSYh-UxTmOeoqYrwcfjG7V_yvoChRge5AC6afMNTmsKJXiDCX-srpdtyZemKb-9A6lRzYWe7G3Mjyb8MU78nPDyjwDIMIeNG39lKKQZTflrxlnb8hfAxFQ4PKId5H3VD4Vkmhy2fPFFAVt3wIBFJersso02xIHRYUHgvww-ESIEDQC3cGjwcqqhxZ3mcCSVQIsBooBJNhBHj_uq-jkxoOjCfxA7FBGMSYRXTOd-LQPjeNDM4qtvgAEjrPCJCwjGvuQSOBYWg-BceDeMHqNRl86VlxNh6mRbz0N4jG_x3evflSuUa6C7QOQHTyrO7n8H2j0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846eb2bb69.mp4?token=DNhbEfZUmQPZA-nwRgcSYh-UxTmOeoqYrwcfjG7V_yvoChRge5AC6afMNTmsKJXiDCX-srpdtyZemKb-9A6lRzYWe7G3Mjyb8MU78nPDyjwDIMIeNG39lKKQZTflrxlnb8hfAxFQ4PKId5H3VD4Vkmhy2fPFFAVt3wIBFJersso02xIHRYUHgvww-ESIEDQC3cGjwcqqhxZ3mcCSVQIsBooBJNhBHj_uq-jkxoOjCfxA7FBGMSYRXTOd-LQPjeNDM4qtvgAEjrPCJCwjGvuQSOBYWg-BceDeMHqNRl86VlxNh6mRbz0N4jG_x3evflSuUa6C7QOQHTyrO7n8H2j0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من وداع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/80665" target="_blank">📅 09:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4990178830.mp4?token=Hep28oXnOerBNnrBrlpT6ISebF6zdr7erLqyYGiwhBCzYWFXwPinAjnZ4DT5xBsXUtXghV0mlQjWupyBiInZp7Pv_C7U0WJSiY8BQsnaYTA22pHwhXnYWKSUyz9Mvz4qfFYElbKBTGD58DoJjbQ2LM7LWyGEsOQp4GEByB72QUl25lA6A4ogqTiEuGq2BtgWmdNiqrEeIE1VF31MuoXpx4v2ZWpd3DNgdqj7tAl2rKPldZWq5MS_DS6z0M_NEJ8zgdYJXn8o_9YjsduDH91HvDUhXF172_Utt6nwCqAly4JrtomwdVcTEZrgFtGDz7s8jNZ3_kUvZt7VuQL5Hta3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4990178830.mp4?token=Hep28oXnOerBNnrBrlpT6ISebF6zdr7erLqyYGiwhBCzYWFXwPinAjnZ4DT5xBsXUtXghV0mlQjWupyBiInZp7Pv_C7U0WJSiY8BQsnaYTA22pHwhXnYWKSUyz9Mvz4qfFYElbKBTGD58DoJjbQ2LM7LWyGEsOQp4GEByB72QUl25lA6A4ogqTiEuGq2BtgWmdNiqrEeIE1VF31MuoXpx4v2ZWpd3DNgdqj7tAl2rKPldZWq5MS_DS6z0M_NEJ8zgdYJXn8o_9YjsduDH91HvDUhXF172_Utt6nwCqAly4JrtomwdVcTEZrgFtGDz7s8jNZ3_kUvZt7VuQL5Hta3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الرئيس الطاجيكي إلى إيران لوداع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80664" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNMbGTQ7rgLr_OJoSMpgLoRa5j6WpbCslmjoXOSZe6-ife5MfyCFO2HUBLimg8-3YxwVPxL5zWQ999jmjfhgo7ed6RsWgpDV1EFi7L4qvPpd4y7TtkCcTroUZ29H-i11DCmXVKe3bGYejrJZYKQx5yKos1q1qMCfKPKD2-naYjOEcbg5S7qIVo2_UtFd21Yag53RxYaWhWm0RkukhOkfNzD_bhzMmykKQ-vJuHjde5-gnlBeodukVcJkvkxWkPUlBT1HQ5KcySxaDiDizp8XO4Ai2aTKKhmPF-Kaa9zFm4hpK3aj7YPlQWQJqPC2ASUEEdum4VyGu6azkpT9r0J7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9ks2X7PJSCVBs83beIi2-KN1szOkACqOrZBxycibZshtU6BLmXWEImUVdb2vJQwq97Hlb4DbbGi3AS0eLvT5RjflntdBTBilqzu1-QLb1-8oGLxn_r-8ovMyu9wffwxApG3gVhKJmZDI4eFIB8hc1ePEVfw4M-bBek4RKA4MmqXZZAMH1WUngn5nxaz3XdRrk_HIInYQz5yuhYfH_CHajAkzH0OjB3baz1LUvhqx2KjJhlCxY3dhoMuXxa5OusBAEdAeY9evWFqBo_YIw9xUOZzQWGglIpCBAemvqqllPkqY6bWmQAIqoX3yv8F7-5n4Hx3_ZZJUQpMFRt8npoH-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقاء وزير الخارجية الإيراني عراقجي برئيس إقليم كردستان العراق</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/naya_foriraq/80661" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292c198e71.mp4?token=Hbz31hyepoOjKxI-NhGr66CG-VZJ8DP3okp5D77jKdZlBL2mc67ifuQz3dTTjmFjKqZCuUU8tDJKY2Nm4Fh_TxhRKUvnRhtaJdZrOjWEg5kPGMgAGtQi5ribQ9qWFQw6Ax3MdkYa6pXncaFxMyiHIK1fFprtFXGpSP_XUdCo0e3bPRD1jE7FG3I9KIZZpDYRV1M05HnTwCa1YC_mod-BGILE3XIOBmhAeIdbtuIR0pDtOqE9Era_SkTnOEzj6TIA3CFGtOT8VKIYA9SCOEqTVgS4hwR6EnaAZK6jL3quv2jZDnZQNMEfpHTeIRh3x-lQWLRyy8SB6XxSb0dX669zrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292c198e71.mp4?token=Hbz31hyepoOjKxI-NhGr66CG-VZJ8DP3okp5D77jKdZlBL2mc67ifuQz3dTTjmFjKqZCuUU8tDJKY2Nm4Fh_TxhRKUvnRhtaJdZrOjWEg5kPGMgAGtQi5ribQ9qWFQw6Ax3MdkYa6pXncaFxMyiHIK1fFprtFXGpSP_XUdCo0e3bPRD1jE7FG3I9KIZZpDYRV1M05HnTwCa1YC_mod-BGILE3XIOBmhAeIdbtuIR0pDtOqE9Era_SkTnOEzj6TIA3CFGtOT8VKIYA9SCOEqTVgS4hwR6EnaAZK6jL3quv2jZDnZQNMEfpHTeIRh3x-lQWLRyy8SB6XxSb0dX669zrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد المقاومة الأفغانية أحمد مسعود يودع جثمان القائد الشهيد</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/80660" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
|
وفد حركة المقاومة «كتائب حزب الله» العراقية يؤدي الاحترام للجثمان الطاهر لقائد الثورة الإسلامية الشهيد. | 3/07/2026
🏴
#قوموا_لله
#تشييع_إمام_المستضعفين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/naya_foriraq/80659" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رئيس الجمهورية العراقي يغادر إلى طهران الان</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/80658" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حركة أمل اللبنانية تصل لتوديع النعش الطاهر</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/naya_foriraq/80657" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفود العراقية ضخمة جدا ومستمرة بالتوافد</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/80656" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/80655" target="_blank">📅 09:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/naya_foriraq/80654" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يستمر الوفد العراقي الأكبر من قيادات الحشد الشعبي المقدس بالتوافد ؛</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/80653" target="_blank">📅 09:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد العراقي هو الأكبر</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/80652" target="_blank">📅 09:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdbIJSWp5WogQ55REvVn6kpbTSmS2amUFIUpIlu_y4Af8if3SnLxWNa20yBMvie6XNNA8gsXO8xUSYCiBbVIWS_VeidEwSr2_iWLQvpfaIgv75D49TGqOE9iXu2bwu4P3f6pCVuLcEYecA-U3ge1eVukCROlhnbNacpf3Mq-hQJRd3MpHM0ddzUD_e5HiOT0hv6SPTZtcRQ45B7GlWGEK-0ixymilr0-fA3JXumAA0TL7Yl5KLToKHxro_CW4kHffNmJd9MXaS-aXiSVPDDDr6b_O413na8g7ZZouoi3RAkRCIhPeQrG3jZHWW0eELdNU5crDjr9fJOByqh1OEENAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف يستقبل رئيس برلمان بلا روسيا اثناء مشاركتهم بالعزاء</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/80651" target="_blank">📅 09:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود أخرى من الحشد الشعبي العراقي تودع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/80650" target="_blank">📅 09:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة وصول قادة الحشد الشعبي المقدس العراقي إلى توديع النعش الطاهر للسيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/80649" target="_blank">📅 09:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حشدنا المقدس</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/80648" target="_blank">📅 09:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxn2JCs37qJezjgtNA2FWYjDVQovF_dycsRR7339fhbcxKH07FAtGoCxfQgnPKoGKtSUqkzat--qsbQ_uYhVQwe-kGW9Bzkf8Z-qmL1HfuIiK5MyPtDpc0Kre_iIKFB9QQHfJbq3FOjUcMWQIzeqR4CInFvBDDsm3oWJ0mpjoivmrqiXQz-aHMeig3FtgoSnrokJIyDjurWjEso2eZKUtkCRr2DBKH0vg1XTkFq5jgjiPjn_oDkkv-S34cvbskq7wbfMso-t-HBr1P4-LUKlnisXeJiYhXP2NWJ5zpuBj8Pt8WZ-WGciOT3ceu48xHUGE16fqtp1D35kMFkUGvy-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حشدنا المقدس</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/naya_foriraq/80647" target="_blank">📅 09:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efa0982f3.mp4?token=M8JLDOd3EX-MuALEX7Nf_8Ir9_VYzzwMfr-0o7rHqz3fF4sow_DcMvg-aNxHkbDh1kJMbRTQikErpDnfL0Gj0ot-r4pG7VJSRrVjtHtAVR57AKUsUNN4pmvudFWlHdUrBDKMk2ZknTuuC88ooQv87N1uPc4FcFklOfv7ihhxooy9oaZV_ustJI_NNgGGSN1tw1XmP1CW-FRkSiRMpxQVwNbrBCSlWQCOh1bqEpk2S7tHrNTI8k5ef5A4BnP4kzuu90sC_ADxnnbS9fEXjKkgokq_6wY1oIrS4EXh8o4pqPQ3xWbhv6HmK44cld7W4rsKcPXE9OVaW2lvYw99U4KxpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efa0982f3.mp4?token=M8JLDOd3EX-MuALEX7Nf_8Ir9_VYzzwMfr-0o7rHqz3fF4sow_DcMvg-aNxHkbDh1kJMbRTQikErpDnfL0Gj0ot-r4pG7VJSRrVjtHtAVR57AKUsUNN4pmvudFWlHdUrBDKMk2ZknTuuC88ooQv87N1uPc4FcFklOfv7ihhxooy9oaZV_ustJI_NNgGGSN1tw1XmP1CW-FRkSiRMpxQVwNbrBCSlWQCOh1bqEpk2S7tHrNTI8k5ef5A4BnP4kzuu90sC_ADxnnbS9fEXjKkgokq_6wY1oIrS4EXh8o4pqPQ3xWbhv6HmK44cld7W4rsKcPXE9OVaW2lvYw99U4KxpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود المقاومة في العالم أجمع تصل لتوديع جثمان السيد الشهيد الطاهر.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/80646" target="_blank">📅 09:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5969afaf.mp4?token=rA0aWekh46NztkzVdDmsOwBP0YZ1y0Vd2bToKCr1hBgPHfaqr64fTqJA7RDe2GUe-RFVIMg4V7z7kZaIOTI-sn23PDjtba0z6L3jGY2g5ML1HNSf85rVbvXaGJBGzmeASSiy6lj_XNvDbugHWGzYeargPDt5j9pMODcR1HOX29dGPR0ffRYUOuJUZlCAM_MYO1Z0J6lHVcxgt_aN0qOpZf6L9Rr8zkSboLTxJMYmu6fv721vlWHXi_Ef4dN9xXW3eXMrVMgOQCcVA3i5KWx6a1h-tB5jIU1BB-6FjO_TQ20KJwkaGqmzCEaDXZ_1WNWrMK8LjWRZCbFHNuzoZO6KQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5969afaf.mp4?token=rA0aWekh46NztkzVdDmsOwBP0YZ1y0Vd2bToKCr1hBgPHfaqr64fTqJA7RDe2GUe-RFVIMg4V7z7kZaIOTI-sn23PDjtba0z6L3jGY2g5ML1HNSf85rVbvXaGJBGzmeASSiy6lj_XNvDbugHWGzYeargPDt5j9pMODcR1HOX29dGPR0ffRYUOuJUZlCAM_MYO1Z0J6lHVcxgt_aN0qOpZf6L9Rr8zkSboLTxJMYmu6fv721vlWHXi_Ef4dN9xXW3eXMrVMgOQCcVA3i5KWx6a1h-tB5jIU1BB-6FjO_TQ20KJwkaGqmzCEaDXZ_1WNWrMK8LjWRZCbFHNuzoZO6KQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من حركة النجباء العراقية في حضرة الشهيد السيد علي الخامنئي لتوديعة.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/80645" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">أكرم الكعبي الشجاع</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80644" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c60c851e.mp4?token=hYo9bhS0RslY3UhNu5TJjorPbzSvS6mfepVZZyGXeHxGzkJgGSqY0M8pmALfKQewUim5ZCEguBhiG3HsEj03iq-8H2gsCgDA17q1YPxmamqxuj_egkA5cmC0usHzzD_SzmJKCYA0txzLaNdYap8i4e1SYkivz_F9_m3MoauWYpK0LZd22PD_DxqpNdEBQZehPUdX2tLVp9FF9R22dURoXSEvy4QFYuQtEajgt_DZks4BG6_l78nkxNehxRFRvb0KWM1itp_xaiFy5900mwcJdDM4PSuuhxNn6izMc1y1FtTdQK2nVn8gqbGIJopSolZ7MVWk_XAq-ptUgOoKiBHMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c60c851e.mp4?token=hYo9bhS0RslY3UhNu5TJjorPbzSvS6mfepVZZyGXeHxGzkJgGSqY0M8pmALfKQewUim5ZCEguBhiG3HsEj03iq-8H2gsCgDA17q1YPxmamqxuj_egkA5cmC0usHzzD_SzmJKCYA0txzLaNdYap8i4e1SYkivz_F9_m3MoauWYpK0LZd22PD_DxqpNdEBQZehPUdX2tLVp9FF9R22dURoXSEvy4QFYuQtEajgt_DZks4BG6_l78nkxNehxRFRvb0KWM1itp_xaiFy5900mwcJdDM4PSuuhxNn6izMc1y1FtTdQK2nVn8gqbGIJopSolZ7MVWk_XAq-ptUgOoKiBHMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصيات بارزة من المقاومة العراقية تصل لتوديع نعش القائد الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/80643" target="_blank">📅 08:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ea1b8acb.mp4?token=ZoOimjnaRwusswK57aPsxp9ahzP5cWtHdcSrIQ_31AEXu3xrqDtQyQbwgafaA0P7XBUdK0qaI8H4-jsyJHuLGEXclfFvnrri9nyE9UxZQ0iDH6AytqF3xSOSCwAMniPzUwPXOh69gxdhiDcLi697JEd8UO6vNeo3puReZQLLwLz2BnbWNNJvsj7aq438toLEQ97nF7ED-gaTCpVmVIJ6RDOy9iVq6SsXnh32PLNA-xp59ehb4t6Ioi9zhGvtPpf9_8-0RLqI6xacp3qSSMi3bzPu1glISDojwfjb3WszZ8OMkw_tqMeHz4FGVlqYKdo83oLiiTmVniY91UbP6ljCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ea1b8acb.mp4?token=ZoOimjnaRwusswK57aPsxp9ahzP5cWtHdcSrIQ_31AEXu3xrqDtQyQbwgafaA0P7XBUdK0qaI8H4-jsyJHuLGEXclfFvnrri9nyE9UxZQ0iDH6AytqF3xSOSCwAMniPzUwPXOh69gxdhiDcLi697JEd8UO6vNeo3puReZQLLwLz2BnbWNNJvsj7aq438toLEQ97nF7ED-gaTCpVmVIJ6RDOy9iVq6SsXnh32PLNA-xp59ehb4t6Ioi9zhGvtPpf9_8-0RLqI6xacp3qSSMi3bzPu1glISDojwfjb3WszZ8OMkw_tqMeHz4FGVlqYKdo83oLiiTmVniY91UbP6ljCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس إقليم كردستان العراق يصل إلى إيران لحضور مراسم تشييع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/80642" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
المتحدث باسم وزارة الخارجية الإيرانية:
▫️
يشارك في هذه المراسم ما يقارب مئة دولة، إما بوفود رسمية أو شخصيات عامة وجماعات شعبية. ولدينا وفود رفيعة المستوى من الدول المجاورة.
▫️
يحضر المراسم ثمانية رؤساء دول على الأقل، أي رؤساء أو رؤساء وزراء، بالإضافة إلى رؤساء برلمانات من اثنتي عشرة دولة. كما يحضرها وزراء خارجية ووزراء آخرون وممثلون خاصون من عدد كبير من الدول.
▫️
تشارك في هذه المراسم جماعات وشخصيات شعبية من نحو مئة دولة.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/80641" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tISa-8rtq32nqnLq8mQQrNIzaZjlzOt50ava41UMZrBAC9Q8t4Armq6QkLJX04P56h4laU-VsPFZ0lFB1VJnkwOiNxvs_avVtAS2jNpl2KI-8tc8lxzyKcVGjAwLMg8kG9V20GVgEDiWsh-7Uc8hTXPIKgdGfgPqfuaEthRrgf86jXhtup5mz4DUSPfy02oVatXa87cN8GpnwuRPYVKSUew2IJWdz1cgoA-kIAQC-BOq_RCD3VzH6uu7Z4CG7ItgL26LRb8kWzplkIASh6BA_l5afZizCanCITchzYIzmhQvnJW8O7AXJx7KqM5Z0jIMLxRz3YgLT1yxalhuu63Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام العبري : ودّع قائد الحرس الثوري، وحيدي، جثمان (آية الله الشهيد السيد علي الحسيني) الخامنئي، القائد الأعلى الراحل، قبل مراسم التشييع.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/80640" target="_blank">📅 08:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6d86c458.mp4?token=ZfRvf5IRJ-vqUkS2-XVeuFcWkyx8kwe5RKO1TaGFisQtW2HobhF-DN7OmToVJog_zCd0ezK9LiY2hqnhqm7pVnoRumhnomDkYUyKSkN8g8WKDSDpwRubtkpO_aslNEpcMqMB1yz3bBKXcBNLiM1_isAFobBIBS9rQ__TMHgExGPeL_lfia94ECLpzCxv221bJ6FJC5Mx8AZijotaaGqrIG2eLrD9HxCuL1LRu6wx6t3EBlkgNmlXwezDLx_zY1fGVkidhkJ7a1ZKuWzyoESTKt6WfC1hpsVHpfydkg-BEAFF8wd5w6m70sBByOAqKl-BnbAZ2Y_J1J62tzALFOELwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6d86c458.mp4?token=ZfRvf5IRJ-vqUkS2-XVeuFcWkyx8kwe5RKO1TaGFisQtW2HobhF-DN7OmToVJog_zCd0ezK9LiY2hqnhqm7pVnoRumhnomDkYUyKSkN8g8WKDSDpwRubtkpO_aslNEpcMqMB1yz3bBKXcBNLiM1_isAFobBIBS9rQ__TMHgExGPeL_lfia94ECLpzCxv221bJ6FJC5Mx8AZijotaaGqrIG2eLrD9HxCuL1LRu6wx6t3EBlkgNmlXwezDLx_zY1fGVkidhkJ7a1ZKuWzyoESTKt6WfC1hpsVHpfydkg-BEAFF8wd5w6m70sBByOAqKl-BnbAZ2Y_J1J62tzALFOELwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من روسيا والصين تتقدم بتعازيها إلى قائد الثورة الإيرانية في وفاة الشهيد
#قوموا_لله</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/80639" target="_blank">📅 08:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الآن | وصول وفدٍ قيادي وسياسي وبرلماني و قادة الحشد الشعبي وفصائل المقاومة، إلى العاصمة طهران للمشاركة في مراسم العزاء وتوديع الشهيد الإمام السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/80638" target="_blank">📅 07:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvP0oJM21gdfkq9h0-V70Qln98pvxWoAvqmT5PMEx4u6fikvkLFhEmmcNwGV2cCAtLTnN9nKL1jDVA31RqzKkXemXAp3rPG3eKPBsGD9gldwCBtK3ecqsSu1rZtmlvlqL7mjA_wK8nknamKpnLkkc8kZF2hbHPDbRkFjZiXiA1irM50SBerFtNqlFHjesQ6Sd-phoI9O9KtYrfjg5iEkTrvPIUseSSudWkK28zXo_HdC3WIHnw3hps5kyOMTSdJDttW2TybTeJqSoJtrHgxCjQfGqC8BC1pRPPTZs5fEP1U8utpjlNy_bzR-U-DVj_EUk9G8tX6xYkcO7Mm0fiEqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج قاسم جاء لزيارتكم...</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80637" target="_blank">📅 02:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
قوه تداهم منزل وكيل النفط علي معارج في ميسان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80636" target="_blank">📅 02:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
قوه تداهم منزل وكيل النفط علي معارج في ميسان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80635" target="_blank">📅 02:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7784288888.mp4?token=TdNVzSqKSoPMGAxwcP0hU6NqVTdLKH_xLvl857ILzCh_8nseLGK_puhb4LYy_zQFNA6bKaqpDTXmxIkCvGv1AK-Oat6zwA3PPS1GoIkcf1YJLK5vc-iweSQXPc20W2Tay2q6-ls5qB63vaUd80ili2m-VIUp_MMUEQFiRC2AIG2bD3_vel9LzEN5nEa_NA5-1Tnw-bFvFo4IED7d4hKe14_-ZP4ixk3TRIgTYWeeYpCi4NN_fl7Bbg4KktaS7HL8MvOKqqSvTwpDDqGjE831QRkE3PHeiR4KfNSwmFXshmwUhLUrHJwqNHrIadD1z5PV5ZQNZ5wD7HlHpJZ1i1jh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7784288888.mp4?token=TdNVzSqKSoPMGAxwcP0hU6NqVTdLKH_xLvl857ILzCh_8nseLGK_puhb4LYy_zQFNA6bKaqpDTXmxIkCvGv1AK-Oat6zwA3PPS1GoIkcf1YJLK5vc-iweSQXPc20W2Tay2q6-ls5qB63vaUd80ili2m-VIUp_MMUEQFiRC2AIG2bD3_vel9LzEN5nEa_NA5-1Tnw-bFvFo4IED7d4hKe14_-ZP4ixk3TRIgTYWeeYpCi4NN_fl7Bbg4KktaS7HL8MvOKqqSvTwpDDqGjE831QRkE3PHeiR4KfNSwmFXshmwUhLUrHJwqNHrIadD1z5PV5ZQNZ5wD7HlHpJZ1i1jh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحاج قاسم جاء لزيارتكم...</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80634" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONmyQfuqH6OWgAB1QGaMG1-rHQV2T811z8wTLehLOeogSMflD0vKMA0SCWU994Fzio22kgc_BlrhejqyocdiBYxvabd8CGyFegFb9GGn3SGSRH6Cr6_l4B4Ngfiu6DJHA3WaF2Dhovu_knYgFCtql4xlJqAQ8Rlwq13TXqO0lN9WgOHZ3ISpko3MDfCPV5FHCFtQxFhYfuPWRh_xu3kt4ZFs2pdO2tGGRUg2I3HNVYpCxiRNUtA2zhUJ_kRsIDdxuVkp15ZoRpPP6ci8Plw9R7Ew0C0NIvB4MJVxDTgVfEoKE2jU10CI-A1nlhMbmvw6F0Do-2e1Td8ydvGqrImw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNiIf_oXaDgrF4Tvz1JwgYup2VHV95MOA2F97k19zixyL9vY8xt6SJYHTE81lMQA5w1wLjMCAcmpK1nUx2UEBfAWlj49Mrh5XBZxfH9NApizfobjkqGtxYpG9eR7mfBt9_zftJtgWrFG-mAaJEf42B0mcEIdnSaUlDmBuO1zjrKkF4_RdvLuzLo12AbDCRil1MfWHI9OV1dbm94xoO5vyJjkosAZ8xuor8zWcefBB53EP4BH0OPdXs6d3y1Y7pjgN1SlwLPAdBGhRjENMH07s0dsVDIxNbzxUQyyRslId7DdC_jSVB_rw_4di3jyRMeY1BulOnVcU95zoJWs2VUWuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
غارتين من مسيره اسرائيلية استهدفت المنطقة الواقعة بين بلدتي صديقين وجبال البطم جنوبي لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80632" target="_blank">📅 01:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
ترمب:
لا أبحث عن تغيير النظام في إيران بل منعه من امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80631" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbhVVk9ITk6yjRWpRcQJc6YGThLr_ysQLJ2Pn_AhavW5HGXBoN5RgnwxAcr8-LaLgGinEjSF-W9KOmRq7ymcjlVjrsB-9YqWH9lx04zO8DNKs97KMBrwQi370-kK5FpBgt8szsUIpidFp_p75cEmJ2y2FMiE6lvuhNg6dznmhF40i4mv28xcgYEBQnnQdtFuOQkzMa_UyyzHAHgf3JhuaodyAok7KlO81s-7cTiI7wxnyqcZzAT2RIyR-rGYlf6sDgnWp6ymh-mC0j3nehW3_whYPk_VYWIhaRuxS85-TgTaIuWQgIasti9r0THnXV9LjqoevgPNI3fUGZLkNkUAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏
هيئة الاعلام والاتصالات العراقية
تقرر فرض غرامة مالية تبلغ 5 مليون دينار على مقدمي البرامج الرياضية في العراق (حيدر زكي - عمر رياض - علي نوري) وتقديم اعتذار رسمي عن مخالفاتهم وحذفها</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80630" target="_blank">📅 00:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Omwo6zW1C-Ij6522n_sdPKm-nr4giKy0RfMlr0GiGWVZ8IUJzqZGt0b7KbiK9UuvFuQ0AdZ4tqlKN-tZMoJlyl89wL-eGKMwousQh5DoXAR2HQIewqAKEKP2LdkAk7UK5piiLFTG5rOONhbGrHpI6szSfM65Kdwf04qgNf2gb2H55gOBPfP6hAHwtiKnQZUoagO03Y_eslnr7mPrfxSbtzyou0udIsCWpGapRmZpx76hVVpbYkVl4sUMNFqYDkuMASung1eMnFy5JY5v6KhuMOErrdU33JGDGGwxgAADqb1x6SrdUB_9JNhN3oAnxb-ofhbu6m1NAQ3jFoXtUloJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAL7D4uscQedsLANNhlML0qyh6UBvCWSabJoZuOEV_errhUemxSp8M3RXK024XpPc3xouNFYKOnBmxYpPyjT3YzGidCxYipBSxZai8lHcapm-p30nRVX0mYI9tyFilUMS75VwSjrpbTBR-O_j27X2Lr0bulPDE0JPVvhMiurLT0n7oVx224pMHY6rnCsZ1jbmZvEih1vnMA21VWbHeD-BSAK5rxYizZoiZ0BCToD1NNQa5diED2TUF-i5bH1M1UL783Cu9R91khi-R3M5L_hZEm6G8VsMWSft44pZ-NAhNF5e-R8jgqqaKydQjXIkb5EakL20vgMD6HHIn0mvCfOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0CNJTtdFO1x6fYsaV5lQvdwheMiS4hlI27rz_0AG_pvjl67s-KY7XvskqJ2QPPCfn-XHsKJU1OXsuYTDlR7lU66tKPyOWZUGamDtC_BVDo6HMLKcADJDOyvWLPCizBeHnLaxO4jPGH4fjCYAmZab6ovolMrN1IzIqscYyNiWgZJUT2r3mv8d4b9TUszxNFRGUmyiiMb0nEXNKvgJtjvOn0JguualFori7TuPUYloxWyPTuNbj6pnFA1jkWlVVzf15xo3I_A-QILEAXBhJptp2EXrt-EPFuJeho8kP6mRkeOfKm7KSebvCiuOXapryEkoT_wnB1Y4Rm1BH43TjacBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icWZgEVr4mobws-r4Z0gi1BOop46xjRoR59stbiFzgnwkocdsRfUsgUFOwHp4pdvr9S99WQjw3eBZyGe5kNn2Z9vNCdsVqEAJc7Au2OzkDZdDnMz1paCqci3P7Tgs8CRSAJgzZTC1Sc92FN44H-xyImNL1W7CvvPaWw0K0MifLEGVGihIUItWSirfS--gljAN9ZTQJ8xTqFMHw34zwdhY2ygFwIEcIvHd0jJdDLV2y7PtfToqtjYtEMfxjgHpd9wtyyu2mMPlI_vH2A2ycxIvVgIrMmQHqHnzWnvZT-N_IPqZg1ReaRLv8CNyfmxCmsut8eKsL-00ObIzpvLajQ7GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
لحظة دخول جثمان القائد الشهيد للثورة الإسلامية الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكيّة) إلى مراسم الوداع بجوار حسينيّة الإمام الخميني (قده)</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80626" target="_blank">📅 23:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3396ef5ba6.mp4?token=MIrl7aZELY3tRE1R-i1AwdKiDyjPgq--pFIHMgUBNXxgAt5hakkZT9-8eG68-2lA8HeztipT_glTroksKjczEGolkh4d2UHseNe2YdP8Gt_wRcFkFZ0EU2ImkR0uu0Iem31ARgV6087LoYC8OkOT5nd0L42hIyPo7oefC9U6F-kLvs57EjlpHmOWP4XuJPg3dYcGCx1iLSMdiFUSu93tRyEbXyEun05fBG1y09Qun8L8SnYSpmoMfUqd2nTvvvt6ppjfxcVqKyTdigYTB2tPAxGLfTzyoXPOkGuhO7TwoEVeOBypk15W0CoXCwJI55sCqlOeZ3KFzsnjKrMzSDRJZLCiv29F8_8RsCSPK1LwHQlqQU2aiTeovnzukiKCa3aBYeENCUWIkMi_J4lX3oshPXy8btBAIg9uaSGHVXoxVdCC8fSE61q1NbB84FlNMk6FPV2QIX6pl7y6ZOlPq6LOVXgijglx28tNgr3LL0E2q5DKJFS0rUPR6DrvhVKU-ZuepqAc5VaQn7v_CkOR8qJ-2eemK729V_ahyK_yMXW-VUQ1I0K-VSa1FrcP7leONVTDL_ppABKQ0A0x40P1E0Asg5BP7AYjsPQNhaJ909RdbcNiDfjPrpMLy4609kExMugcQpj5bsE0weyAMuo_5D3HMyvJJ_CIZeMyYZ-wh76f1WI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3396ef5ba6.mp4?token=MIrl7aZELY3tRE1R-i1AwdKiDyjPgq--pFIHMgUBNXxgAt5hakkZT9-8eG68-2lA8HeztipT_glTroksKjczEGolkh4d2UHseNe2YdP8Gt_wRcFkFZ0EU2ImkR0uu0Iem31ARgV6087LoYC8OkOT5nd0L42hIyPo7oefC9U6F-kLvs57EjlpHmOWP4XuJPg3dYcGCx1iLSMdiFUSu93tRyEbXyEun05fBG1y09Qun8L8SnYSpmoMfUqd2nTvvvt6ppjfxcVqKyTdigYTB2tPAxGLfTzyoXPOkGuhO7TwoEVeOBypk15W0CoXCwJI55sCqlOeZ3KFzsnjKrMzSDRJZLCiv29F8_8RsCSPK1LwHQlqQU2aiTeovnzukiKCa3aBYeENCUWIkMi_J4lX3oshPXy8btBAIg9uaSGHVXoxVdCC8fSE61q1NbB84FlNMk6FPV2QIX6pl7y6ZOlPq6LOVXgijglx28tNgr3LL0E2q5DKJFS0rUPR6DrvhVKU-ZuepqAc5VaQn7v_CkOR8qJ-2eemK729V_ahyK_yMXW-VUQ1I0K-VSa1FrcP7leONVTDL_ppABKQ0A0x40P1E0Asg5BP7AYjsPQNhaJ909RdbcNiDfjPrpMLy4609kExMugcQpj5bsE0weyAMuo_5D3HMyvJJ_CIZeMyYZ-wh76f1WI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة دخول جثمان القائد الشهيد للثورة الإسلامية الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكيّة) إلى مراسم الوداع بجوار حسينيّة الإمام الخميني (قده)</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80625" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المصلى الذي سوف يتم الصلاة على امامنا السيد الولي في العاصمة طهران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80624" target="_blank">📅 23:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s57DxaAf_COalK3ySnMABh8Zx4zk-yY11pjSwVXdoc2YpHBlGgX8mn5NjfOy423fY-ARPCdKp7QR7eJOBb91PnsXvHRlUVKC_FxbRPkmzP1FbSpPj3yNqm7sfLYw4xL2OelNojxyWZXPEsBX8WQ-lOgo1TlG3RweKAuqk59PZn6qcahT_2jH_TR4wmL_k761YtbL6LrDJ8YpNvnB1d7RFmEq3BGbCxv1FbTIl4Ydmasw65I-ms4rvG6_kdQb3zxBnrdnTlJX2ZlG_-3h79h3mmm6ZkFadgcQFGTcg49irvLMRi-8LxpTi6ms1EFAPSebXvLQ5y0urPjqeoDprq6MIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بزشكيان:‏
الآن وقد أصبحت إيران، المليئة بالأحداث الملحمية، تستعد لتوديع الخادم الحقيقي للإسلام والثورة، أدعو جميع الناس من كل عرق ودين وذوق وتوجه سياسي إلى تصوير مظهر دائم للوحدة الوطنية والولاء للمثل العليا للنظام الإسلامي من خلال حضور شغوف وثابت وتاريخي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80623" target="_blank">📅 23:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoWqjmQyc3y9gS72wABoPVsnYNNw6kkI98jNnr58ZeCMnt4cSMSwtZTkSxoGDPOfp1gus9H9sBEa97ArGbAlt4NQIqiDA4ySmNK-Q9mOa6d4jN6wwleCZqdpg8fx4g3RnTc5qZoL7Dbl-yT8trnVjaB5mcWCkDIRdLm2zI5sDsK_sc-rny5-HzIC6pGGUG1J2Whd_n9H2bzIJZD4Yy3AsNKhEIHlDn4TzCJqrsGDS3dK8vGb55Az-wO92dbnO1Wl4o_di22Cvgwf8E1jaZm33CPEHlcQVezhhB7SbRF1oI8f52WgKEwrQwuf_C97mFRpqtL2MF2KFk57Fy2a6uHFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في الوقت الذي تقوم به حكومة الجولاني الإرهابية بهدم قرى الشيعة والتخلي عن قرى آخرى لإسرائيل.. استشهاد شابين من أبناء شيعة سوريا تحديداً "نبل والفوعة" واحتجاز جثمانيهما بعد معارك مع الكيان المحتل في محافظة درعا دفاعاً عن الجنوب السوري.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80622" target="_blank">📅 22:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">صوت مجلس محافظة واسط على تقليص الدوام الرسمي ساعة واحدة " من نهاية الدوام لشهري تموز وآب.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80621" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
انباء عن انفجار في مدينة دير زور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80620" target="_blank">📅 22:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6-Zhd5zReoRnat2_w4Wo8zPkkG7hDBxbc1ewwWmPDMcbLHnmQI-JuGKtSwvcg1flrgHeD7QEKQeEG_MjVjTD3EC4m-NM7plTJR8ze3-8eWO6UI0X8bq-uLfxipGKOTPOK46TgemX2EgORx-FsSrK-d5ewrepydy3w_By1YPlrJ596-DYBVJxqDdULUjTn1naWio9hXBGKoA8TosdY7l4ZglJkcc8w0eGKA_u_2B_VlmnXzfHREdsTS4vqX9N9rfp6IbeGlx1FgXVki8YSPB1G23lsIQG1vrxR5Yc4ANkBYradBxurdUgCRCE00tUU0xQfFdpTQJ1e9ZMfm8B3Wdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عراقجي
: ‏
هل جلبت القيادة المركزية الأمن أم انعدام الأمن إلى منطقتنا؟ الجواب واضح.
‏وبالمثل، أثبتت قواتنا المسلحة القوية أن الغرباء لا يستطيعون حتى حماية أنفسهم.
‏لا يمكن الحفاظ على السلام في منطقتنا إلا من خلال نهج شامل وجامع، دون أي تدخل خارجي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80619" target="_blank">📅 22:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80618" target="_blank">📅 22:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80617" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇹🇷
🌟
وزير الخارجية التركي:
تبحث إسرائيل حاليًا عن عدو جديد.
طالما أن إسرائيل - أو أي طرف آخر - تتصرف بطرق تتعارض مع مصالحنا الوطنية والإقليمية، فليس لدينا أي سبب للخوف من أي شخص، أو التردد، أو التراجع.
لا نمانع المواجهة. إذا حدث ذلك، فهذا ليس مشكلة بالنسبة لنا.
إسرائيل ليست مشكلتي فقط؛ إنها مشكلة العالم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80616" target="_blank">📅 21:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇫🇷
‏
الخارجية الفرنسية:
قوات التحالف الدولي ستنتشر في لبنان بدعم أميركي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80614" target="_blank">📅 21:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=b2gIvZgMf8MCjQOtGi_k0RF6xqTOjYmm3YoN59Cmm8TurdI7WXyn8gKOrhk6ZiYKkYBZZjb6Yig9fE6IhK2o60iNejKvItuVh0BsD-qSRPQmo5Qb_FUKW7c88VJ7aFhJj3NGxOYYceePAcbhVulT-72BaCloBN8Rxuc6dpyheu6eQfQFgI3VpksKxVz_FBDmPUfkowvMX-haEltjQSgDaxXDK_3ZfYVTFBRTELazCSLAuJMF25IYu17X0j5eLmOfNtDGiTkzTJc-CnVk7Qs1l7E5aruh9T1VFTuOt4F4ukNEv5XPB_rpofboVKxtVDQ5RR29cM6jDP7n76gjHPDgMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=b2gIvZgMf8MCjQOtGi_k0RF6xqTOjYmm3YoN59Cmm8TurdI7WXyn8gKOrhk6ZiYKkYBZZjb6Yig9fE6IhK2o60iNejKvItuVh0BsD-qSRPQmo5Qb_FUKW7c88VJ7aFhJj3NGxOYYceePAcbhVulT-72BaCloBN8Rxuc6dpyheu6eQfQFgI3VpksKxVz_FBDmPUfkowvMX-haEltjQSgDaxXDK_3ZfYVTFBRTELazCSLAuJMF25IYu17X0j5eLmOfNtDGiTkzTJc-CnVk7Qs1l7E5aruh9T1VFTuOt4F4ukNEv5XPB_rpofboVKxtVDQ5RR29cM6jDP7n76gjHPDgMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الرئيس الكوبي حول التهديدات الأمريكية:
إذا حدث هجوم، فإن الشعب الكوبي سيستجيب بوحدة ورسوخ ودفاعًا عن سيادتنا.
نحن لا نريد الحرب، لكننا لسنا خائفين منها.
ونحن نستعد حتى لا نُفاجأ أو نُهزم.
علمنا فيدل أنه لا يوجد أعداء لا يمكن إلحاق الهزيمة بهم.
قد تكون هناك جيوش قوية جدًا من الناحية التكنولوجية، لكن في الصراعات، هناك قناعات، والقرارات التي يتخذها الناس، والتضحيات التي هم على استعداد لتقديمها من أجل الدفاع عن سيادتهم.
قال الجنرال أنطونيو ماسايو: "كل من يحاول الاستيلاء على كوبا لن يتمكن من أخذ سوى غبار تربتها المغمورة بالدم".
هذا ليس مجرد شعار. إنها قناعة تم تبنيها من قبل ملايين الكوبيين.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80613" target="_blank">📅 21:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QejByX-p-SPMHR4fiRj0vSk90Z5NEHzbXgSpVHtRkLtMBw61ZmYFHL8r90r9tgib5pg-mwegggQNhH0dhrgkNLFmtUT90Un5k__VQy6jms8h1XTLk6OINoTVonalNwDmxsSHp1AnSL_nssndW9ftb9nY0-oxOE1N9e30R7o5nRoaLbptnAk68B7gUAahRufOMsjdSc6RLqQRUsDsei8OiqVjOGjENOpLmiP6YNzHmoCaTCrJNd87JZY-0b8zFE-S_sK4qG6SubVeboi4da_ChVRijO5gp3Vn3N21a9nmIzxTO5ZI9wK5zgSHNPhcLiRq-jpHZ7ms0u51QB1uUCtWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أعلن اليوم يومًا وطنيًا للإسكالوب احتفالًا بإجراء اتخذته الإدارة الوطنية للمحيطات والغلاف الجوي (NOAA) والذي سيفتح الحافة الشمالية لبنك جورج لصيد الإسكالوب، محققًا حلم صيادينا العظماء الذين عوملوا معاملة سيئة للغاية من قبل إدارتي أوباما وبايدن، ومن قبل دولة كندا. هذا يعني ملايين الأرطال الإضافية من الإسكالوب البري الجميل سنويًا على مائدة مطابخ الأمريكيين، والمزيد من فرص العمل في نورفولك، وفرجينيا، وكيب ماي، ونيو جيرسي، ونيو بيدفورد، وماساتشوستس، وجميع أجزاء الساحل الشرقي تقريبًا. هذا بالإضافة إلى تحرير منطقة شاسعة قبالة الساحل الشرقي لصيادي جراد البحر العظماء لدينا، وغيرهم (نصب تذكاري بيئي أعلنه باراك حسين أوباما وجو بايدن النعسان، والذي قمتُ بإنهاءه!)، ونصف مليون ميل مربع من المحيط الهادئ الجميل، حيث سُمح لكل دولة بالصيد باستثناء صيادينا الأمريكيين العظماء! لقد فتحتُ المحيطات والأنهار والبحيرات والبحار أمام صيادينا، وحررتهم من القيود البيئية السخيفة التي سمحت لدول أخرى بالاستفادة من مياه الولايات المتحدة في عهد باراك حسين أوباما، وجو بايدن، والديمقراطيين. إنه لشرف عظيم لي أن أفعل ذلك لأني صديق الصيادين - اخرجوا وصوتوا للجمهوريين في انتخابات التجديد النصفي، لأنه إذا وصل الشيوعيون إلى السلطة، فلن تتمكنوا من الصيد مرة أخرى!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80612" target="_blank">📅 21:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=gI0O6Au3VgyYdX8zWV6ykmummS0H3s3aDGxYmphPyLn2FcO-NfcMvNKbVg8ulMoIFcFRbv65PO1JwjNlotMK3qKRdKKQEt3uS4lmNALUBXuJkLzxUUaeJZ2VNFkEQFyTkLjMvqQBKEipv_A_ORCQyLUw0JPH0eI26XokgFCUrfpfBKL2-SZ5LzaPlDqrGYjgTdYgcldVquE6_AE7QWSY_I2RVRilPILuIEeBvOeE7Bj1vHnYGaEcfUFVWc4HtoZbh2HWOmB_tBn4jt9IHWnP0jo7yIXOcj3vbM_6FsMSMYSeDJP5fr-VlvnVi2sd6-wMowOho62ec_yNmrlFtDsmNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=gI0O6Au3VgyYdX8zWV6ykmummS0H3s3aDGxYmphPyLn2FcO-NfcMvNKbVg8ulMoIFcFRbv65PO1JwjNlotMK3qKRdKKQEt3uS4lmNALUBXuJkLzxUUaeJZ2VNFkEQFyTkLjMvqQBKEipv_A_ORCQyLUw0JPH0eI26XokgFCUrfpfBKL2-SZ5LzaPlDqrGYjgTdYgcldVquE6_AE7QWSY_I2RVRilPILuIEeBvOeE7Bj1vHnYGaEcfUFVWc4HtoZbh2HWOmB_tBn4jt9IHWnP0jo7yIXOcj3vbM_6FsMSMYSeDJP5fr-VlvnVi2sd6-wMowOho62ec_yNmrlFtDsmNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المواكب الحسينية تستعد لإستقبال المشيّعين وتقديم الخدمات خلال مراسيم تشييع قائد الثورة الإسلامية وعائلته في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80611" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=k1le4vLPYjZ7_Wfx3noVLYFTWShZof5YzzoygpZ2n9cJKWYH2tN9RytKGN4aJ-mptHtw2XzzID4AJxM8SjgUMJUJ5dUJu64MhAl0azbHpQy3TpdmplukcPywahShG6jMhY8tESPP_ifdN4ravBfZ6P--zD66O_aE-G_fPWeIg_-Pa7NNp26RZaGbFe1bFx3r6LoLOxXIZBEOQ9K09xd3BimBGGLqKh0dvndoP9L6kRJIDPcJNmTUor5PKB20LcF7NoyAtroFhfinrc989C-xvIitYVtAaXIfFg9b54Z1priNzqiR-7a6uIZaSAjQepVHK4ZpuJVndbuhhWbKF-TT4VTzhgzFRDEoeuvQYBgraoXRPaTZomKO7mPc9lhjNQb_X4dBvYvGq6y5yt0CaLWts1LU25WzwQvf-V-59o6shg01zlLMeXp4vurktpkqnqxmTvnsAT3VNstTriYnCOZLkDkSo4HfFQRUn-H1NfvMteSF7UnfZCEpGFtmOilZ60CMvA3UEJa6f5PGj5ckzn82yUYVpP6-MCpESPA_wZwyRrJcGNBekUx-jsvO3PLzN2Qft_dj4vbAnCk9irGaJQSWe_qsSlGve998PjtNaBxZtc8ucsjmY-ALa3PIjZC1G9g1xBn5CcI4j8FZQxe63YeCts94-SeoTSLoVxHdFIC6mSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=k1le4vLPYjZ7_Wfx3noVLYFTWShZof5YzzoygpZ2n9cJKWYH2tN9RytKGN4aJ-mptHtw2XzzID4AJxM8SjgUMJUJ5dUJu64MhAl0azbHpQy3TpdmplukcPywahShG6jMhY8tESPP_ifdN4ravBfZ6P--zD66O_aE-G_fPWeIg_-Pa7NNp26RZaGbFe1bFx3r6LoLOxXIZBEOQ9K09xd3BimBGGLqKh0dvndoP9L6kRJIDPcJNmTUor5PKB20LcF7NoyAtroFhfinrc989C-xvIitYVtAaXIfFg9b54Z1priNzqiR-7a6uIZaSAjQepVHK4ZpuJVndbuhhWbKF-TT4VTzhgzFRDEoeuvQYBgraoXRPaTZomKO7mPc9lhjNQb_X4dBvYvGq6y5yt0CaLWts1LU25WzwQvf-V-59o6shg01zlLMeXp4vurktpkqnqxmTvnsAT3VNstTriYnCOZLkDkSo4HfFQRUn-H1NfvMteSF7UnfZCEpGFtmOilZ60CMvA3UEJa6f5PGj5ckzn82yUYVpP6-MCpESPA_wZwyRrJcGNBekUx-jsvO3PLzN2Qft_dj4vbAnCk9irGaJQSWe_qsSlGve998PjtNaBxZtc8ucsjmY-ALa3PIjZC1G9g1xBn5CcI4j8FZQxe63YeCts94-SeoTSLoVxHdFIC6mSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترند_تركيا
🇹🇷
في تطور خطير بساحة التحرش والمضايقات
😆
..
امرأة تتجول منذ ثلاثة أيام في شوارع إسطنبول وتتحرش بالشباب حيث يتولى نشر فيديوات لها عبر كاميرات المراقبة في مواقع مختلفة.. منصة تركية: منذ ثلاثة أيام وهي تتجول ولم تترك شابًا إلا وتحرشت به، ورغم ذلك لم يتم اعتقالها. ماذا لو كان المتحرش رجلًا؟!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80608" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80607" target="_blank">📅 20:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80606" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
إعلام العدو: حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80605" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
إحكام السيطرة على الشريط الحدودي العراقي - الإيراني في هور الحويزة بعد إكمال سدة حدودية بطول 50 كيلومتراً.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80604" target="_blank">📅 19:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskmPyTNIYOJ7NgoGzwX4ZCH-2inqEd9ePSKC60CVb2PcTg6C3DjyhBjKySZjNcj9Trl8PbM1zEmK3eaHxqh5pf2xPKa4KvlZeHR6QhpHDfDuZ_8HyXfpRBrZQDyjwVq3M5o3lBVlLsK5dqNCKvi7JrnH1-a7SslwGpENOQmSsf3WQSOG5142_dfJkKT2Ty9WldZDMhtsoYniT5ynJGaZl59nkQU9bHLsDe_uaCHcKjtSfLtZPNS8JRvAnru-CwetDPebbcJbaqNlx2D1oeS_IXWjav_zUfR8HhdrCRuhdM3bm5kBnoVcDbpqZckI-6JVf5LgFbnAB93iUzQ4u96tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات للطيران المسير الإسرائيلي على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80603" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=Y8JRNLJmZcikg23GBfSPW2W4Dcguydc27oUSo2_0nmEN2VCUPhzKz9ISCYkOf1dsfvxeOrVpxKwkZDBEOkXUJna_iiGXddmdp3yn-wTZznQia4jCr9Iyyr2m0wTbw5McQMixn22tz1CqS9wHJVF3W8GuV9YEnOsGTWpYNbsHT3jPZ1Nu8gm9tPN25RjtMZkDHb2fujX7KeTuOflE_XQnz_zB8Cur2A5pXEbtfPWVmfcII-so1TcTcQSemRe8ClCd7mrSsbwu1UxV6Of_PspKlU6RD7w9vhC7CKlyyhyrHzCJgcZ4tsYGmj55nPKH_x5TwWOO68K7VowIJ6UI8-VZPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=Y8JRNLJmZcikg23GBfSPW2W4Dcguydc27oUSo2_0nmEN2VCUPhzKz9ISCYkOf1dsfvxeOrVpxKwkZDBEOkXUJna_iiGXddmdp3yn-wTZznQia4jCr9Iyyr2m0wTbw5McQMixn22tz1CqS9wHJVF3W8GuV9YEnOsGTWpYNbsHT3jPZ1Nu8gm9tPN25RjtMZkDHb2fujX7KeTuOflE_XQnz_zB8Cur2A5pXEbtfPWVmfcII-so1TcTcQSemRe8ClCd7mrSsbwu1UxV6Of_PspKlU6RD7w9vhC7CKlyyhyrHzCJgcZ4tsYGmj55nPKH_x5TwWOO68K7VowIJ6UI8-VZPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إعلام العدو:
حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80602" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=qj-mBx2TccNU6iRqJB-RGPQmrS6fCCNQZayKsdghsvhKjxjqfJgUc5iCv1QDhOkBQCMHtq3OhU_X4alwC0MFgJayFphfFBN1xeLHgfwX3ZZ0DnnQd2mJhsx0bfKmr8Az29j4kuCYAhOsXJk-6a-6a3tBBYJ9uXpL8_CqwrhPeKE-xHf0awooBZqIC6YjP3G766ca5RtKUoFBpaeSqvuG8bxvdu-1jsgei_F_h8_kjjTRo3rek1fGGwLFzlql19m_F-zYz__eyepQBNV4JigAo451qpWywmnYEwkTgNynvX-Aqh6eqH7CkH2bR1g-W6MJqdR6mNZRJHmVTUM1rE-h6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=qj-mBx2TccNU6iRqJB-RGPQmrS6fCCNQZayKsdghsvhKjxjqfJgUc5iCv1QDhOkBQCMHtq3OhU_X4alwC0MFgJayFphfFBN1xeLHgfwX3ZZ0DnnQd2mJhsx0bfKmr8Az29j4kuCYAhOsXJk-6a-6a3tBBYJ9uXpL8_CqwrhPeKE-xHf0awooBZqIC6YjP3G766ca5RtKUoFBpaeSqvuG8bxvdu-1jsgei_F_h8_kjjTRo3rek1fGGwLFzlql19m_F-zYz__eyepQBNV4JigAo451qpWywmnYEwkTgNynvX-Aqh6eqH7CkH2bR1g-W6MJqdR6mNZRJHmVTUM1rE-h6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80601" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
‏
مندوب إيران في الأمم المتحدة:
سنرد على أي انتهاك لمذكرة التفاهم.
‏الولايات المتحدة هي من تخون الدبلوماسية.‏
حرية الملاحة مكفولة دون رسوم بمضيق هرمز لمدة 60 يوما.‏
نحذر من استخدام مسارات خارج السيطرة الإيرانية في مضيق هرمز.
الهجمات الإيرانية على القواعد الأمريكية استندت إلى المادة 51 من الميثاق وشكلت دفاعاً مشروعاً عن النفس.
إن تقاعس مجلس الأمن عن أداء مسؤولياته عزز مناخ الإفلات من العقاب وشجّع على المزيد من الممارسات غير القانونية.
استهدفت القوات الدفاعية الإيرانية المنشآت والقواعد والأصول العسكرية الأمريكية في المنطقة التي انطلقت منها الهجمات ضد إيران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80600" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
القوات الأمنية الإيرانية تتمكن من قتل 2 إرهابيين في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80599" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">إلى عموم المؤمنين والمعزّين الكرام.. استعدّوا للمشاركة في مراسم تشييع السيد القائد علي الخامنئي (رض)
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80598" target="_blank">📅 18:45 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
