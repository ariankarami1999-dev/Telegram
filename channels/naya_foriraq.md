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
<img src="https://cdn4.telesco.pe/file/UiJuPDp7w3uPxgtQWiVdh1sE_fKT5y-_9xb14_OOQPyZBD0qg89hp13VlkWA6zupSDGnCsoQ_gBg2Cqu1hN_5iXHbnol_N8EcJBhpds1vxpkfmOPfsdgZlj-ziWamm6eYbcmu9BSSfnjOJdR-ByDcF6aDO8r82LFdzSbDCJ8-7ulVtGtAfm_yOW2C1Y44aQiwx-Q7SIgwKC4THaNrwQ1kThzlFnKEhZNV8aVtkfOnXS2WFUf0yl2jaorx2Ws4q9OQ53TPhBMsyZsGuerU7QbUOMohj3m0Pfc6ldcFYd6edm-3po-Naa7BhE3uATK66dFUfeRqkVEn33TbLWlqxkxPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/naya_foriraq/91665" target="_blank">📅 16:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدوا   العامري سيغسل عار الإطار بعد قليل</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/naya_foriraq/91664" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/naya_foriraq/91663" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmSAuqPPVwrszH6tKSquf-J3bLQf4C9KWUdhk_iNx8Lz_iZWgEWpNwMSELdOs5luCNwg-H8wGH2nGOlltCxP5mFzWHd8drjZ4bggsSUI3Yo8RFnedGfbXQx9VQYzyEGVpLjj_r_7fgfOmeyKRcq2Hmrs_BQgIobmk8x8WV7H4VxnLfKMJzX49D13sV0pl8oMB00bD4D86QX8aikWydwb4w_PMERuKO2EwmwGful9h_eY6bdiiaQPfKen597X3P-UVTXWRTdrIWW6EBmgjf7-lWPECTBjwkkkKETrGIZj4CZugQuC_sgvqCxPb_v1gKeeXqyg4SxWZftrj7ArMjUA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمانة المجلس الأعلى للأمن القومي الإيراني:
إن نشر بعض التفسيرات والاقتباسات غير الصحيحة من تصريحات أمين المجلس الأعلى للأمن القومي بشأن موضوع النقل الجوي، أدى إلى طرح تساؤلات وحالات من الغموض، وعليه نوضح ما يلي:
1- تُنفى الادعاءات التي تفيد بأن إيران ستلجأ إلى رد عسكري بالمثل رداً على القيود الجوية الأخيرة.
2- تجري المفاوضات بين إيران والدول المعنية بجدية لرفع بعض القيود الجوية غير القانونية المفروضة، وتجري متابعتها بشكل مستمر.
3- هناك عدة خيارات غير عسكرية للرد بالمثل، وفي حال الضرورة سيتم تطبيقها على بعض المطارات، مع التأكيد أننا نأمل ألا يصل الأمر إلى هذه المرحلة.</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/91662" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cT8VV7lxUPZDDxC-4H1AbNS8cLvFqDh4G3FtYmuzXWAsyP43paSO2ezVMP_e38jywqHxb6ca73Y7j0LTu_C2wbEzJqdqq6KMjnOmj6Yden7B7ZmVp1wovXwaw47_HtKyI1Wl1ZXTNPzNbkaTc_SyM1y-zru8HGizqu5sgRg_1P3pLjtiGry9l7Q8roET89-0VmoKGN1dKRsO00xq6p9aYr8xrbEeGO5-Yefcv5PO1gV4B9_w9rrIlNXH4T6M5QHJxrhPJbMo_0fGZmQAMvkOZumRSqSleNKeW_JDdTKGgUE_3BT0P4t7It3cyLjMUT8xN9M7tmkb6MuYTf6ZdIcUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnQ381OpRjWGuRlF8yl0BGUKs8FeuvxC8KXIEAT4XD7ATbyPcHsaNL0ieE6LXM1ovEKvAoGhQMWVdLYl8_vr1Jowh0pWOpkxFcEtSlS0695UkM2MAxWRHOdqEbqCxuOTpc6Kds0IaJM12xbkdg6GZEDP6Cty7R6onQrv9s9Q0qlrfbZMqMVUwsv6J9yJFRrRG4ntIz0wZ5O-HTYNq63AB6VoyxJ7shRtShjqdfTpGUHsBjh0PmHFHMgt5HHb9ob5wJR9jIhZZQRBPZbKrnPmmCBGxkEAsIx30jYT_l4ZcDYqsw7ZyNZjO82OmyFTd3SIWHUUvptBjjkZvpzaU89_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JALDIcZDNst5q7wByRBKWUbSXcGWRclTUI-is5oPr8WCqDNb1JMBkjiwXhLWhgtcW3re7_Hxwtjoya9p_as4Zo2V23q90q0i1vqIE1vBuqZWFHXXYpwT8VJ4_n6OL1al8Rqi1LPSOQLqlQThzKc6G-lfr34vm9klt2NdWuyZJNJoofd5zkk7U9wAvOLs_YXlCWS9Z7jeBKuMQ8bPVTtK4gL-V02ZJ6M3tzw0nidVA8ZalT8IlYBqimVXM0rCuaqeUM66EXjx6049nRxOntiTYbx2Tsw7h2lYYjdQPQFx-3H1DkaVZsbnoDUuO2I2YeoRenu7FmXdpSCf4r8obliSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im7WVvduIqk3XiELxexxWTRVaNv3qsvQ00hdgG5wpL07VFpSitQAwR4lUKu8sWuyup0w4gNHyj9bLFTWu3TwmlbudNMHM9CgVCFyiWkH-nmyDvU8AuCsndJF7mOgCQbEaFcV1meLzlkqm29Z46-Js5hvx3j-YSkwuoq8pEenVbKpNooqTyNChDEIselLhO7F_jy6HcmO5atRbkMj2vRQ9HgNOVBPxf4R9dYrSWfVkxWZKBLhyuz-x_I3028bMjdkePmQXVaRSspHQmiNP595Vw2Jtwo6nUaPOv0HSCwhdEQAUU0pmtsyK0j6GNeXMf3YS1USSpeTi2LoGf94XutO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAzC3BwvA7f3A1Y42ipxwU6fKxhBMa8_Yh6q9WDrIykfiQio3jm12uq6xuA-WQD43Il0pRAyA5OSpe3gBdye9WrhDPjUej7Nt251oC_8aalxI5qASwvcJJ4bXexcJyYTEhfuOVZlbBOt66T0SQpQwwLx-ta59aP0oJdrZxPiSnahH_93t6vXaEBXFEy43IXrhfGV9QrA9BiG5qAXr0JwnGBM_yqSQYD2KM8S8ri-j-y0RcMtGkGKwCd0X-GA7nD0xTT--KF9yRF2voExwTrq-wEOZ93VU02h3yyHVRR2feXmLzUqWWn9U30WsQw8t-ga4uTX3KlxZwiiWRvxJwyazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz70HSsI5ev5u26De9CHdvaulTHVOoxV1Bur8c_RNYIR0m38YC8drlujOUC7gtzUJd98Wl0O1GH_j1-ObO5re-fY0ZU-T2yCW7wlm5s6VyBebseVxj9G34mcfXJ1nT2hJFwaMROqTSjL_ppsXDbrHoSnUhkFNAyMFiISAC9nNJ04iSD4TrVXozOk2d9PdjDyj7Uu2kpX8co2X22HAfCflJdDjcVMu1frNIdCFyCV54-rPkO6llU5Sxf00Uc1UbZApEHEsC6gRF3T7o9kAFOxK8uJLrEpirzLmPN1SUhR1mqApRl2UU0oR__3X_9kiWL9DPFrwMNZhhNgICFn9S8gng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7rbs7it1DyHq7NeoDz0aQnKwtu3lJKPWRTwceaucz5XdaRy5YRe5RvJ15rT2htlqmdJYKlG-ZbmTeeIQnPkbi7l4mAiJlm0MiCYY3W0R4weTb4s_dCfVHzRzRb9CRlJsKtX6yGKW_KpN93sbne5EvwGA5XigP1cVocNKhQ4bqJ2wOhM1lMBNgF1hyTNdJ-mp1ssLOdCTDwuusDBYfRUwM73D_ueK858fvorQrsNlxRToNhM3Gu5Rj4yNbqbo82a3sCcI243NfrAHAWhavIUclBVCC4xPFsuUHVYT5D3L7lFf1HCv0QSzbc1YDYxDPloFCR10XJ5bN7n4dBO7WP4Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من ساحة التحرير.. انطلاق فعاليات إحياء الذكرى السنوية الثانية لاستشهاد السيد حسن نصر الله والسيد هاشم صفي الدين رضوان الله تعالى عليهم في العاصمة بغداد</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/naya_foriraq/91655" target="_blank">📅 16:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL6JTqYGAFTjXm0SLNZUv1XA0WOFoSTPpE6-PX703od0oly8hCWwj_xIHckNJ6vM9HtOpNILyQJAhKBHm1zEoi7ivd3cQs31wIVSofeO5XR94Zzy4ZISzyL6bvnSWVf-_msfFfk3fTCgf-0zJe8oDKTbXL4MWpy-FHDFe-fEIz50fQixwecepptFlPS66xHOnUoBrunf5ROWrFBGk8pDmhQZHC8LdIxsuKgVgYJRuFjMTZ2ulRxjsBdj7rge48KBfgxsHz2jSTP2wljO1qe1tuI2BWgEeMotuUo0zeA-UqoC8bYxpfAds_23qw3jT_2iAUtjFT4nSXH3mXHSwtLPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سوالف الگهوة   سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/91654" target="_blank">📅 16:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة
بداية كورنيش جهة التعليمي
استعدووووا</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/naya_foriraq/91652" target="_blank">📅 16:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الشعب العراقي سيقول كلمته
ساحة التحرير - العاصمة بغداد
بعد قليل
تسقط الوصاية الامريكية على العراق</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/91651" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
🇮🇶
المرجع الديني المدرسي يحذّر من الاستجابة لإملاءات الأعداء والتضييق على حركة الزائرين .</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/91650" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eGoiAeemtcV4YELK-Z-V8zJBDEkQNnYsnP-7jrTTcpIANM6UMflt7RNU1O4MpdWOm2cjXyYOzpgRFEmnyZItJRv8KuD7HpCSsLpJw3ePko9UlsEAT76kXOoZ6IortDhIik3srjcZprek3BV_bzZmqE-c0UL9YGUg_ysS33nHNV00nUAPejboRorP6YdyPfqfkE7e3gxTr0BQIw-faqwqqVwkMNRFapmua-xM7yojPjyQiLGhenZZmOOfU1cCzwQTglEOlMhDH2Sg_BI7N7oNzH0rGAeZXDUgPCt83hpjQM5ysxXQyq4QQyGlkNSeye4E1Cs51S5SStNgEbaw02RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
كتلة إشراقة كانون تؤكد رفضها لإجراءات الحكومة بشأن إغلاق المجال الجوي مع إيران.</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/91649" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة 4 عصرا مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/91648" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb71pclX2cle8Bbh09GuDRwEkDjagtde43ny6WK9Y2TdyGa4I8yY9vqCLSr8lC7ABsX7wWA5JXf09nYeY9bIiQrVIT676erQ8XiKy1yWvhYIXHE06G8eR1PpPyXAjLyB4jX7xbqunXAxpF9BIMAsm2HfaxI5dnyA3zKow7DaBHWaeuQy10a5uVQVIZtf_NYZB1h0AEWqIQ9btxk3Y7GCJvBUs7Dfkv-hj6bRkRLp_dPQk0sbOob1nk7YK9gLdXs_55HBoNZVp8AqE0HbCWWeg4UJzifz5p2LB1nFxLApI3KfFPWbzDVIq1raQ3Wdu5Qk-_ikSkJw2W_0H6Fp4QjWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
العراقيون الشرفاء سيكسرون الحصار الأمريكي على ايران
ما ملت امام حسينيم</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/91647" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAbyOr8ss-6cgqQL_5E2FJvZRSVBITebA6wlkoz7X84Wy2nYbWv4wh_HPLqabkZK1Ij6_wbMEmQy1R_CQb0WEAkB4c8BgN3crGHhOe0q82MntHfwHVKyQMnE3QYxyv2kDgBRK3JNRz0jyxUveRbAXuBbExDoAxPlzBz5G2X_2TuK1AlLivnTplg44tagMM80E95dD7IQ56Zphuh5hPl2XyHYGfZ-PHChkW7QanO-4EnQt3gbu0rknLxJfma2knoAZlviHmTwZPzA-FlKE8Ue9sJ9h0qm83f7zO4WqydPwYaAvWKyQyt8yOuajmKxXXuVupyeANE5bNLiJbkQZXKp6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇱🇧
تنشر لأول مرة
نفتقدك يا أبا هادي " درة لبنان الساطعة مع سماحة الشيخ همام حمودي "</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/91646" target="_blank">📅 15:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎬
*افتقدناك يا أبا هادي*
🔻
الشيخ أكرم الكعبي: أنت ممن يستحق أن تبيض من أجله العيون، وأن يبكى بدل الدموع دمًا..
🇮🇷
انتاج: مکتب حرکة النجباء في الجمهورية الإسلامية في ايران</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/91645" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇶
النائب الاول لرئيس البرلمان العراقي عدنان فيحان:
بيان حولَ الموقف الدستوريِّ والقانونيِّ بشأنِ قرارِ تطبيقِ إجراءاتِ حظرِ الطيرانِ المدني الإيراني في المطاراتِ العراقية.
تَجمعُ العراق وإيران روابطُ جغرافيةٌ ودينيةٌ واجتماعيةٌ ومواقفُ وتحدياتٌ مشتركة.
هذه المشتركاتُ تُحتمُ علينا، دولةَ العراقِ وشعبَها، أن نقفَ بجانبِ الجارةِ المسلمةِ وشعبِها، بل هو واجبٌ شرعيٌّ.
﴿مُحَمَّدٌ رَسُولُ اللَّهِ وَالَّذِينَ مَعَهُ أَشِدَّاءُ عَلَى الْكُفَّارِ رُحَمَاءُ بَيْنَهُمْ﴾
﴿وَالْمُؤْمِنُونَ وَالْمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ﴾
وواجبٌ أخلاقيٌّ.
فإيرانُ أولُ دولةٍ فَتَحت مخازنَ سلاحِها، وأرسلتْ قادتَها ومستشاريها للعراقِ أيامَ مواجهةِ عصاباتِ داعشَ التكفيريةِ، بينما وقفتْ دولٌ أخرى تتفرجُ، بل بعضُها يدعمُ داعش بالمالِ والسلاحِ، وهي الدولةُ التي تجهزُ العراقَ بالغازِ الطبيعيِّ رغمَ حاجتِها الداخليةِ إليه، ورغمَ عدمِ تسديدِ العراقِ المبالغَ المستحقةَ بذمتِه، والتي بلغتْ ملياراتِ الدولاراتِ منذُ سنوات.
إنَّ هذا القرارَ المُستعجلَ وغيرَ المدروسِ لا يتماشى مع مبدأِ الدعوةِ إلى النأيِ بالنفسِ، وأن نكونَ مُحايدين، ومُخالفٌ للدستورِ، فقد نصتِ المادةُ (8) من الدستورِ أنَّ العراقَ (يرعى مبدأَ حسنِ الجوارِ، ويلتزمُ عدمَ التدخلِ في الشؤونِ الداخليةِ للدولِ الأخرى، ويسعى لحلِّ النزاعاتِ بالوسائلِ السلميةِ، ويقيمُ علاقاتَه على أساسِ المصالحِ المشتركةِ والتعاملِ بالمثلِ، ويحترمُ التزاماتِه الدولية).
فالعقوباتُ الأمريكيةُ الأحاديةُ ليستْ (التزاماً دوليّاً) على العراقِ لمجردِ أنها أصدرتْها، لذلك لا يكفي دستوريًّا أن تقولَ: (أمريكا فرضتْ عقوباتٍ، ولذلك نحنُ ملزمونَ بها)، بل ينبغي أن يكونَ هناك سندٌ قانونيٌّ عراقيٌّ أو التزامٌ دوليٌّ نافذٌ على العراقِ يبررُ الإجراءَ المُتخذَ ضدَّ إيران.
وإنَّ هذا القرارَ هو تعطيلٌ للنهوضِ بالواقعِ الاقتصاديِّ والتنمويِّ؛ لأنه أضرَّ بشكلٍ كبيرٍ ومباشرٍ بمفصلٍ مهمٍّ من مفاصلِ الاقتصادِ الوطنيِّ، وهو السياحةُ الدينيةُ، حيث يُعدُّ الطيرانُ الإيرانيُّ الناقلَ الأساسيَّ لمئاتِ الآلافِ من الزوارِ الإيرانيينَ والعراقيينَ بين البلدينِ، خاصةً عبرَ مطارَي بغدادَ والنجف.
فالحظرُ يؤدي إلى تراجعٍ مباشرٍ في الإيراداتِ السياحيةِ والتجاريةِ، وخسائرِ شركاتِ الطيرانِ ووكالاتِ السفرِ، وتوقفِ شركاتِ السياحةِ، وانخفاضِ إيراداتِ رسومِ العبورِ والأجواءِ التي تستحصلُها السلطاتُ الملاحيةُ العراقيةُ لقاءَ تقديمِ الخدماتِ الأرضيةِ والملاحيةِ.
هنا، وبصفتي البرلمانيةَ، أوجهُ سؤالاً إلى الحكومةِ العراقيةِ:
ما هي خططُكم لتعويضِ الضررِ الحاصلِ نتيجةَ هذا القرارِ لقطاعِ السياحةِ الدينيةِ والعاملينَ فيه، أصحابِ الشركاتِ والفنادقِ وأصحابِ المهنِ الحرةِ، الذين ستتعطلُ أعمالُهم ومصالحُهم؟
وما هي خططُكم إذا اتخذتْ إيرانُ قرارَ التعاملِ بالمثلِ، وتوقفتْ عن تزويدِ العراقِ بالغازِ الطبيعيِّ، وانهارتِ المنظومةُ الكهربائيةُ، حيث سيفقدُ العراقُ ثلثَ إنتاجِ الطاقةِ؛ لأنَّ إيقافَه بالكاملِ يتسببُ بفقدانٍ مباشرٍ لما يقاربُ (30% إلى 40%) من القدرةِ التشغيليةِ للشبكةِ الوطنيةِ، وهذا يعني زيادةَ ساعاتِ انقطاعِ التيارِ الكهربائيِّ في العاصمةِ بغدادَ والمحافظاتِ الوسطى والجنوبيةِ، وشللَ القطاعاتِ الحيويةِ: المستشفياتِ، ومحطاتِ معالجةِ وتصفيةِ وضخِّ المياهِ، والمراكزِ الخدميةِ العامةِ.
وأخيراً،
أؤكدُ أنَّ مجلسَ النوابِ جاهزٌ لعقدِ جلسةٍ استثنائيةٍ في حالِ عدمِ التراجعِ عن هذا القرارِ، ولديه خطواتٌ عمليةٌ سيقومُ بها، وكذلك إجراءاتٌ رقابيةٌ بحقِّ الجهاتِ المخالفةِ للدستورِ.
ونؤكدُ أنَّ قرارَ العراقِ يجبُ أن يكونَ قرارًا وطنيًّا مستقلاً، نابعًا من قيمِه ومبادئِه، ووفقاً لالتزاماتِه الشرعيةِ والأخلاقيةِ والدستوريةِ، ولن نسمحَ، تحتَ أيِّ ظرفٍ، أن يكونَ العراقُ شريكاً في الحصارِ على الجمهوريةِ الإسلاميةِ.
عدنان فيحان الدليمي
النائب الأول لرئيس مجلس النواب
26 - ايلول - 2026</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/91644" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/91643" target="_blank">📅 14:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
‏مقتل 11 وإصابة 30 آخرين في انفجار بمدينة ديرا إسماعيل خان بشمال غرب باكستان.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/91642" target="_blank">📅 14:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">النظام السعودي يستهدف معلم في منطقة قطبين اليمنية مكتوب فيه أسم الرسول محمد (ص) في اعلى المرتفع.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91641" target="_blank">📅 14:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني:
إغلاق مضيق هرمز أمر طبيعي عندما تقطع الطرق أمام إيران.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91640" target="_blank">📅 13:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🇮🇷
ائتلاف الاعمار والتنمية:
نحذر من الانعكاسات المحتملة لحظر الطيران الايراني على المصالح الاقتصادية العراقية، ولا سيما القطاعات المرتبطة بالسفر والزيارات الدينية، لما قد تسببه من عرقلة لحركة الزائرين بين العراق وإيران، وزيادة الأعباء على المسافرين.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91639" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
وكالة الأنباء الألمانية:
استمرار البحث عن 18 مهاجرًا عراقيًّا يعتقد أنهم غرقوا قبالة سواحل ليبيا.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91638" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
🇺🇸
الحكومة العراقية:
"قاعدة فكتوريا" خالية الآن من التواجد الأميركي.
‏مباحثات في إسطنبول لإخلاء موقع بعشيقة.
‏إخلاء تركي لقاعدة بعشيقة خلال "60" يوما.‏
3 فصائل سلمت أسلحتها من مسيرات وصواريخ.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91637" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_5qH7L6kXpFgp1ce6oz1vbKvjdfSD09HAyQ0lAtkMwVLVw-V84kx0ZXjagb7gG3SwhmNcYQyllP-O2wZ088vL3kmJpCs5JffBz7OHC-rHKnMePFxM_i1jtyFNXZU0lfYyyaNaM5t9GN4vBky7Bw-FWehMMlXVZ7x7Sz_ePnycgWmd4euvwa02PxB-NrsqacF7ScUs90GKbXcALbQNfGwR-vd_H54-NZ14CcD87YVif9BJn_43zs_0LSzYJEHwgZ1vfJCFIau_9LIcQQE11mmbOqPkz7PHoLyyCUuOHB4xGZzQm0FfEATx6E-TkM-mOt5EWtgEaG5nsTQB8cAqUo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ قيس الخزعلي حول الحصار الجوي على الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91636" target="_blank">📅 11:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية:
توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91635" target="_blank">📅 11:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91634" target="_blank">📅 11:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opZIea2U3FsnlyaMdBkrR4Xi6oAAVNO1nzaAZu-kl3OMx5unqzVGnJmv0TVqSRBnG-RTlCaKK2RkW6hQKFLwB6t3Z29uygqMMTbsCMNaLPP4kgk09eJyznU1aOaJXZTdaWG7bdKYZi8hCHkJfz_UBfpVh8_obPCVGw8mi6e7FDW9MMkL3LafuhjfNM7e1Ay_6v3xUWbQcb6kpd7S3tGVFtZwZlFb07jEcajGpSteKZeyso9mlnBQebgdz-kP_MOZR5LY76B2Q6KguroQ4PgIlYNimI-tWa-_0qTBVZMMxUVw-LhnhJR_iLosP55Oo102Rn7vd2_N8Clsms0MHAj7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
حركة بصائر العراقية
على الجميع الوقوف بحزم امام تمادي الإطار التنسيقي بحكومات في الانصياع وراء قرارات امريكا الجائرة تجاه ايران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91633" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
اللواء كوثري بشأن الحصار الجوي على إيران:
سنتخذ إجراءات لإفشال هذا الحظر وسنوقع عليهم مصيبة تجعلهم يندمون على الحصار.
الحصار الجوي لا يمكن أن يستمر.
الضغط الناتج عن الحصار الجوي على إيران يقع على عاتق الشعب.
لدينا خبرة في تجاوز العقوبات.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91632" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
مدير عام مطار الإمام الخميني:
الرحلات الجوية إلى شرق آسيا، بما في ذلك الصين وفيتنام وماليزيا، مستمرة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91631" target="_blank">📅 11:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
وزارة البيشمركة في إقليم كردستان العراق:
التحالف الدولي أوقف المساعدات المالية لقواتنا.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91630" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
في السنوات الأخيرة، تم نقل جزء من القدرات الاستراتيجية للقوات المسلحة إلى بيئات آمنة وبنية تحتية تحت الأرض.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91629" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
المكتب الاعلامي لرئيس مجلس الوزراء:
الحكومة العراقية تجري حواراً مباشراً مع الجانب الامريكي لاستثناء بعض المطارات العراقية من الإجراءات التي اتخذتها وزارة الخزانة الأمريكية بشأن رحلات شركات الطيران الإيرانية إلى مطارات دول المنطقة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91628" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THxOc_Mi5XN3bIcdfxJRDNhlPfvSnkLV6NWXCz7Kay3ZkGhmcGYf3ESSib2Kz11cYMFkcFFAdDRSBi1c6mGO_xJQSSzpi6cMEy54BBJmNrSnnwMVW6NLp34e97NVSZXwbrwHsobxFKR1BoTXqPNFA_dzyjzdYEmEtTcmhQb_7aQWnzq_jydd1usiVQGoK23zuo8d7mfpPfS6GMg5xw6H5ko-h1TobRqrYj8jsOgPXzb89F6m9Pz7YL4KQv27BsktOmQyLWiSeEr9otHwoMs53cTbtTUaGVtLxoiZgezPiBNlSgXpse4_MweinCZqlwlm77wbzK7u32rK0vN6Hy0M9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات للطيران الحربي الصهيوني على بلدة سجد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91627" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBP1yz3c-GIRrkQVQkzuC1TgfPHdYccR4ZIdKkIaZLhI-zcCX_GZi0LK6huHc-e5oBJmr8r8zYq3rAnEL7IdW2iPfx1sd4zpKNvtMaTtfao-kP5tB9eWZetVHtsqJtuSBj57mGXnw3xsFxDwPIlnkbzQJYNiiDQ8VeEnUSuCiJ6Gu_zUbelV6nv3vbESzm9J7iIbGUE6pzAGR22vJc4mqfRKEPxm80LPYSv02szRPC6wvOxAGH-JmmuriRfs5-jRV0YAi8i2SZpIuae3txQfGFxc_Q_ZP4lE7uyh2-ykfrODFUHDZyoInMBYhwiHDaYX5IAgO66GAn4NNwKjeWpr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات عنيفة تهز العاصمة الأوكرانية كييف في هذه الأثناء.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91626" target="_blank">📅 08:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91625" target="_blank">📅 04:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">النظام السعودي:الدفاع الجوي اعترض صاروخ باليستي أطلقته قوات الحوثي تجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/91624" target="_blank">📅 04:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3PpqI8XmonpjLOU6GX0_pvtC3phMKVpFHGYEUxIxVvotuY2bGvDt24ya7xua7ZSLG48VZznFSCkoSDBLkh4RmscLs9RnUFdi7QM46-UhZUVFNAXmImirozhKE7A8dxTSXAks9weNG3vuV_ABk195clUfc7bob2l46OoTzvzxfCU2lCDG04WAKuDd0hdXxgyJO65cKBiCgj9TMjt3jCMWE7X0UBaiuqc4dYaNWz_OCMbTYgJFYT0NdsI6r9gmMjGEAfTk9fr05hYEGK1cD4ztkNJsEOgw73Kz1jeweeg3iW-V7OEFjRnFcVrsVUo02a7hxCNzirpddqTIT_UC_oxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد: جار تأديب وتربية عيال ابستين</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91623" target="_blank">📅 04:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91622" target="_blank">📅 04:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POZ-253ndDK6KCUdW5BuRLFxnFMLPGlcSIEg9_AUdJ1bpYrunG0PCWzk05qwiW7tCeACMDZOdTXgvm7OAqtFEBrKn5xBMzwHIwvgnu-6yv4-qUtXYPPh1_l_xj7LUTrYNcLBD79qSXWfrWYOXI3Au6fD6iEHuh-9WnTCcOV7mC2AgAoKki3qs_wfXfJ93DaKD5c0jEaLbqnJIoHLN7YcwgRqWmoLJ6rTcB-2yvzEregEX5v4ZpTdLJC0v_94EF07KiT0LMBdrMhl2hpePVQbk8O7iWXeyESSl8NNIIbbMBDBtVJl-5DXc3r_5vsSXQ4jyEtPnzlgpkuVK3Vp42pMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
ترامب ينشر مضيق هرمز تحت عنوان "مضيق ترامب" وسط توقعات بالرد من قبل هيبت الحلبوسي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91621" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91620" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">النظام السعودي: هجوم على الرياض</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91619" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏النظام السعودي: نرصد ونتابع تهديد صاروخي ومسيرات باتجاه المملكة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91618" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تفعيل منظومة احذف تكفى في الجنوب السعودي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91617" target="_blank">📅 04:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ابها تحت القصف</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91616" target="_blank">📅 04:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91615" target="_blank">📅 04:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91614" target="_blank">📅 04:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ول ستريت جورنال: ‏ترامب يرفض وقف إطلاق النار مع إيران ؛ ويتوقع تصعيداً في القصف بعد انتخابات التجديد النصفي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91613" target="_blank">📅 04:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91612" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز الدمام الان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91611" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91610" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ljh45Vthbrp6GpLiGHYhKRIFPxsptMrffjdTswfMt8FQZ9qmfuwVnpEkCxCOObgPpBdze4IluT015x5XWssn4yZZdSgf_yyd0fTfOwuETsR5DLOO2j-T7CXUQmnq_BpQrdENu_Ahq8TLQGIsAjDR_PplwIBRzHqy2HljZl3jn8CyA84YdZd5MHznzkkZhuYhKdrpf3AImpeEYKV9ffTEHv7b83BqSl-7FxyTECuZhpavaiKPhsBslYGHKRcUIFVNCb_UTX8f6h861O0YRauqfwVEXlNibD2-NLpd0-HCG_pfCJx_dZMtL-VqSxV7ZGJpLMBVol_yyOMDLlooI9mL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91609" target="_blank">📅 03:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا
صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91608" target="_blank">📅 03:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">والعتب موصول لسماحة السيد مقتدى الصدر
عرفنا السيد مقتدى الصدر انه مع دعاة استقلال العراق وتأثره وتبنيه بمقولة لا شرقية ولا غربية
فكيف يرضى ان يخضع العراق  للأمريكان ويشارك في حصار على الجمهورية الإسلامية الإيرانية المنصورة بأذن الله
واين تغريداته التي تعلمنا منها عن المشاركة في نصرة المظلوم على الظالم ؟!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91607" target="_blank">📅 03:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امر مستغرب جدا
لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن
والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري ؛ نوري المالكي ، محسن المندلاوي ، عبد الحسين الموسوي ، عامر الفايز ، الحاج ابو الاء
لديكم برلمان كامل وزارات ماذا تنتظرون  ؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91606" target="_blank">📅 02:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
السيد صلاح المكصوصي :
لقد تعودنا أن تغلق الحدود وأن ترهن القرارات العراقية بإشارة من سفارة لا تمثل إلا الذلة فإذا كان منع الطيران يقطع رحم المحبة بين شعبين دمهما واحد فاعلموا أنكم لم تمنعوا طائرة بل منعتم الكرامة وأسقطتم ما تبقى من هيبة الدولة
من يظن أن منع الأجواء مسألة ممرات جوية فقط فهو إما جاهل بحياة الناس أو متعمد تغليب مصلحة السيد الأمريكي على مصلحة العراقيين
فبسبب هذا المنع المذل تقطع الزيارات المتبادلة للعتبات المقدسة آلاف الزائرين العراقيين الذين يزورون مشهد وقم وجمكران والعتبات في إيران وآلاف الإيرانيين الذين يقصدون كربلاء والنجف والكاظمية وسامراء اليوم يقفون بين حيرة الطرق البرية وكلفتها وتعبها وتحرم أرواحهم من زيارة أولياء الله
ويربك طلاب الكليات العراقيين والإيرانيين الذين يدرسون في جامعات البلدين طالب في كلية الفقه أو الطب أو الهندسة يمنع من العودة إلى مقعده أو من لقاء أهله لأن قرارا انبطاحيا أغلق عليه السماء
ويحرم مراجعو العلاج من السفر لتلقي العلاج في المستشفيات الإيرانية كما يحرم المرضى الإيرانيون من المجيء للعراق أرواح بشرية تدفع ثمنها لأن حكومة بغداد خافت أن تغضب واشنطن أكثر من خوفها أن تموت امرأة أو طفل على حدود البر
وتشل التجارة مع إيران السوق العراقي الذي يرتبط بالمنافذ والاستيراد والتبادل التجاري مع الجارة إيران يدفع فاتورة الشلل والغلاء وشركات النقل والتجار والأسواق تترك ضحية لابتزاز الدولار والتهديد الأمريكي
هذا هو وجه القرار الحقيقي
ليس أمنا ولا سيادة بل محاربة للزيارة وضرب للطلبة وتعطيل للعلاج وخنق للتجارة من أجل رضا سفارة لا تملك حقا على سماء العراق
الذين يدافعون اليوم عن هذا القرار تحت ذريعة أن الحكومة مجبرة وأن أمريكا ستضربنا وأن الدولار سينقطع هم أنفسهم حفظة مدرسة نخشى أن تصيبنا دائرة ومدرسة بيوتنا عورة لا نستطيع أن نغير
أي سيادة هذه التي تبنى على إذن أمريكي بعبور السماء
وأي حكومة هذه التي لا تعبر عن شجاعة الشعب العراقي حين تقف عاجزة أمام قطع رزق التاجر وعذاب المريض وحرمان الزائر وتشتيت الطالب
إن الحكومة التي اتخذت هذا القرار المذل تضع مصلحة الضغط الأمريكي فوق راحة شعبها وعمق علاقتها بجارتها إيران فقد خرجت من رحمة الموقف الوطني ولم تعد أهلا لأن تمثل من ضحى بدمه لئلا تدخل داعش بغداد
فلا عزاء لمن جعل سماء العراق مفتاحا بيد البيت الأبيض</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91605" target="_blank">📅 02:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة  أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية   وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91604" target="_blank">📅 02:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة
أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية
وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة اعتصامات داخل المطار، على خلفية الدعوات التي أطلقها الشيخ أكرم الكعبي لتنظيم اعتصامات، فيما أشارت المعلومات إلى أن الإجراء تم من دون علم الوزارة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91603" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avkVAMNgZCKoJD-bkz_Frc779HRpq5rlLAxadi8Cg_3oB51iMSj3uKcqE1MGv4kdWpyXB3hDFepGRntU8h6Hpz6UrFZYq4E53C-GpVh6cnY_urgaRlVGdPQ8zoZ9DDh2SawdBdT3ThV6tJX-85dzdJYrg0qf93Spscik2P1xykRp98PnlQP7-dtxwWCPcQWCvxaN31bTHcdNPmYsIFLz2-0ZoV-Hj4vPd1-1Uwz9C59n80gA2w6WiA7JqaDKDVVMTXSJK-sgdLKz7WH3O1LlTjjmc9Qq_UXE6yyMvxse2HyZ1a9VRFJGS-eAcKPPHm46vpH37aAi6r8qS2M5LLfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2103610717991563618?s=46</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91602" target="_blank">📅 01:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91601" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91600" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InCwQ270HGNUhQM_Xx1h9AqoaJFsJwAM6MihQo99Twp7LGxv20-B2d2cL6gng-JXE6IvjqxGWU4R9NXpbqhISy8lNbg7LmJAhOc19_dYm4PAHwi9rOX6_7JqQxzzTi3VY5Xm2R6QxFH1wEzDuYBe8Tv_8kJj0Y9KKPCYGzJIeNtnMNhjSAnUnLuBjGqx4Q7bySdTu40NNwCovuBMSegHit3Lpj8SMoCUoti-x4YaIovqu3bMIsUXOIuTpc1JkJtHlpMxN6ORyg0XXc7_xMSWp4GlTkznE7tPMuY0M9hm9GngkTxMGPXVEwCMH4c7KZm1dpl0QhT9F35CEJUearWhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابو جاسم الذي نحبه : كلا كلا للحصار على الجمهورية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91599" target="_blank">📅 00:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇷🇺
الغالبية العظمى من ناقلات النفط التي تعبر مضيق باب المندب حالياً مرتبطة بروسيا.
لا تمر أي ناقلة نفط مرتبطة بإسرائيل أو السعودية من هنا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91598" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
أضاف البنتاغون بهدوء 37 جندياً إلى حصيلته المعلنة من الأفراد المصابين خلال الحرب الإيرانية هذا الأسبوع، ليصل إجمالي عدد أفراد الخدمة الأمريكية المصابين إلى 861.
وتشمل هذه الزيادة 29 بحاراً من البحرية وثمانية من مشاة البحرية، لكن وزارة الدفاع لم توضح متى أو كيف وقعت الإصابات.
أعلنت البحرية أن البحارة عادوا إلى الخدمة بعد إصاباتهم التي لم يتم تحديدها.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91597" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91595" target="_blank">📅 23:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/91594" target="_blank">📅 22:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXePME5tcT39ZXWVUY0eV1oKnOuyA00nQH-Z_L6p1b7RmEajEcFw3obPd0fKKNdswRyt_fzOgKZ0e7OZfkvuKfs0A59ksKLKM2y-HODQu1H275lF3gb5Q0V0flH7aqs2boZeZDbKFK19IMK04M0xFl2o7jzLdjv90ZSXrn5PJcIgfb9C11TYkdA4xpRKUysUKQQ5knnYc-9htgG10TTan0Y4bf-lorVNpw-Bf0XPb34TZxw8uFFlbr45BFrHLo5RM_AoLdPyFqR7dVaix4Vhbp0ArqywkW5ne1VkFo4sh_dzvnaoDkEAoeQfYdprLg0tXH99mFZgrVe3j2ky6Gg32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sH3zJOq0Mo9Rp1X4hibYnHxTpOh3ZOkJcd1XAGX0IcRHm8DwwGJXy0K8Y-6grAMvdFfQVXoA7JPNpUJCAVmZ_hTFMakHNluZFJzUuLia-gB5zaTLs8TTPrnYhMJ90f9NaOIFpigf7I6c0frFYyQZzGWnbGfdSXTbU8XlduK3VLVKDYBy5icGCVhskaEcD1_IIEbZv10FYpmN67eEfd5xHTR9q9p-zG6XY1Tra08lE3FqMBe41bRSNI5HN-DOZRbovMobXhvtGOuh0qlgCfdWoBciXsvhrqHksj_CACYQ5sH2pl_2VyZFO7amwtuRB1oEz8Byv8U9hsKnR2yh8V02QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhg1ft5iCD2UHYRz18itVtiElxR5aHiPKYgjsleWkbAaCFE6DBAYMiFo6xGRjLFFtqG0UYYyl0So_HVEsPNuBYRJ3o2V5E26LozhimYIS6s4DkgixMl2vElwGvBKZ_gYg8y5m8EmjjRmCm2ogtqppUiOq4EOMkxREKJzrIjBe1k1Wk67pqIAp4miB-lLm6V8FST-9MIfypwFHe8ndnZqm6abbMxKobMoVVa34FjpbW4RpH8rMEYMypXW9c4a7GbRO6OTnvXVYTkSPazM2F4dyP1b71xFOVzm0A9F89AFH2JnEvg32G-bKtAWCo0RFJuw4hXzYJxcvRef4GCSYte_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiWTghnpG4_gFVTLU2JlDH03Z5NGpWbnoaBPp3XzPVYwGZonmz_h0NwQp_PGz_B_UWUUD6rQIqzPoG1J09x9p1hkzzaHn2rZ7P1Yc1-kd_JxpOwBL-JZIV3ds07kbA115DGerDRIXhcdY9HqPcPplZklWcfN3XXo7PaApCKD6OnbcN14zTtTRLV0fVRBW58uFRecN7mBrQ2sZCtZupRQ-zmE51-KbFdFme6mqpErPxfCRxo6WwMBpSUD13iEzKJOYEHOs-HOGNrVg4Y8NaEfXvuFIIPnUtd-Jym4uzGiJyzpnYwc2zfLX-inyAJzliYi5jnc6hszXzn5dpnSszwkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد من المسلحين وأسر آخرين فضلاً عن الاستيلاء على أسلحتهم وتحرير الباخرة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91589" target="_blank">📅 22:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_4kOV2kFUxgTtBDOsV5l7G2YLiB02HeZoLIVNn0xQEQGTDnsoCVgciW2KLVhZHiCm13QwofMCpZtM6HM7ZgSowZJPhlx_nzUSgFL6zlSqhMAs5-OBQ02tdkyWEbVVewTPS_YnAfW0CemJFUo57e4LHqGozilo6MwSyl_7rt54MoNxb6wUHZ0mXgJSQXcC9OYMvor9iDg0vy3ylJPnNOsQfLc3OnBtijRBsZ81aOexVEuEnkDlh0hinmEt8fbOTbmPCM33mCq0BMeyVh9P0NMOKBf6xPrXiT2KMken5K7Te6FhvVh-eW0c4_pz-ly9v9XPGzFZiqYU4igz9p0fAHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جماهير البصرة الغيارى تستنكر وترفض
تخبط الإجراءات الحكومية الأخيرة وامتثالها للقرارات بحق الشعب الإيراني الشقيق.
موعدنا معكم
🗓
الزمان: يوم السبت 26/9/2026
⏰
الساعة: الرابعة عصرًا
📍
المكان: كورنيش البصرة
نقطة الانطلاق: من مقابل طوارئ المستشفى التعليمي، تحت الجسر، باتجاه النافورة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91588" target="_blank">📅 22:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
انباء عن انفجارات جديدة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91587" target="_blank">📅 22:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9abc32c86.mp4?token=Xm2K3vhoz6qhWdwFLSzPINzSWlFmGMEgWU9DIkW9zFbmkMh-mSZ6iKA2E_zx7haoCRzLLbu1o0cUKC3nVsE4wKZVE4VqovrXHpT5IxKsBKmFfxcbvtsj9k2w42rUkN7hdeS6Y6Cc35HYAR3HH9rw8WBnOvC8mvDn5j4nW1p0XrPyaIBIbrcbqstO9ghUdwuHj1_1BiHW7VBjsgfpoDmUTUEdh931o5XWH41lr9J0j7p1e_zZX4wki_wYYqc-uhmyN52H5e5RbH3L1-qpwC9TCD0AcA3BG3_AP-iAVQ1jKXX2xXFMcZRJgXNyyPMq5bzFWtdtd24H86EneXNgRxOiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9abc32c86.mp4?token=Xm2K3vhoz6qhWdwFLSzPINzSWlFmGMEgWU9DIkW9zFbmkMh-mSZ6iKA2E_zx7haoCRzLLbu1o0cUKC3nVsE4wKZVE4VqovrXHpT5IxKsBKmFfxcbvtsj9k2w42rUkN7hdeS6Y6Cc35HYAR3HH9rw8WBnOvC8mvDn5j4nW1p0XrPyaIBIbrcbqstO9ghUdwuHj1_1BiHW7VBjsgfpoDmUTUEdh931o5XWH41lr9J0j7p1e_zZX4wki_wYYqc-uhmyN52H5e5RbH3L1-qpwC9TCD0AcA3BG3_AP-iAVQ1jKXX2xXFMcZRJgXNyyPMq5bzFWtdtd24H86EneXNgRxOiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نزاع عشائري في محافظة ميسان جنوبي العراق مقتل شخص واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91585" target="_blank">📅 21:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ed9a3394.mp4?token=N2svZNoYGxLtIZnL7_Xp0xyU8yjezVISCh_HfKo7JLWSTr_nPbCe0b0vUEW9VuQ4x5fljvRf36zrdsbcd-T5ue1TF2QU2YOVUvNUfxQo0Aw6T2V4IJlQhGL_ugfhTL05au92QAfHKL5EukJcgGndFfg7t9L51UdhHf25kkoB23W0eLYM5WI9K3fbrebpGu5o2Djp8cJe-mhEeCewCRo68HHQDDKx4iRGaBGqfWZ07EYpaPpHokLwfic7Q8Oawu_VmqmLLTF7b4IXTg7LH1kmBqMp-hYpjfnbJ09nTT-quDaH_sT6HnurTZ_AtD-c1WwKk-wNCxERAbZJBQmuEYvBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ed9a3394.mp4?token=N2svZNoYGxLtIZnL7_Xp0xyU8yjezVISCh_HfKo7JLWSTr_nPbCe0b0vUEW9VuQ4x5fljvRf36zrdsbcd-T5ue1TF2QU2YOVUvNUfxQo0Aw6T2V4IJlQhGL_ugfhTL05au92QAfHKL5EukJcgGndFfg7t9L51UdhHf25kkoB23W0eLYM5WI9K3fbrebpGu5o2Djp8cJe-mhEeCewCRo68HHQDDKx4iRGaBGqfWZ07EYpaPpHokLwfic7Q8Oawu_VmqmLLTF7b4IXTg7LH1kmBqMp-hYpjfnbJ09nTT-quDaH_sT6HnurTZ_AtD-c1WwKk-wNCxERAbZJBQmuEYvBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇸🇦
🇾🇪
مشاهد حصرية لنايا...
من الانفجارات الاخيرة التي حدثت في سماء ارامكو بالسعودية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91584" target="_blank">📅 21:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-UDZ_DS_-u4ZK4FEHlxtlUvzsy8gXRIxxF_4t2h3y0XTMXP2BUK_HU88m91WM_JzZbfrHDgPK74ebzd6Lm25uwKKaLZG-JQdAGEC5swk6cHazp56w9HCixsMNc97B5MBv2hkW0HfwIx4SejusPnkDcU65DsUEoPVu_lDV1HwRJANkwEkGsBUOOPcvpqFs6k72ROjtXvmkBl9o1ior-3XvKQEFgky4rvzC7n7mueWsEtbUE-pDzd373ILw6iJzhCY70NqyfJGvaR5p35EGAEbSmsX3c2S7jfkZfqYic1jYpux_wks4GTOMR2t0y4GeJ2tfQBkz7vWWTuXmZv1t6GGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي:
في حال عدم عودة الانسيابية الطيران مع الجمهورية الاسلامية فسندعو الشعب العراقي ومضايف الامام الحسين والمواكب الحسينية للاستعداد الى الاعتصام في المطارات العراقية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91583" target="_blank">📅 21:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4eW08DKGycn4ozwcE9X2mdek3bGLPaV0J6LVoEoxC-newIlQpNCPnqfH9tvXfHUwwFvH74dHWrEGZunq5ose0n_3z9dfT7E16Mc8CY_BJM_7YbpvEI6hnlHoolTrv0pcfeS11ejqV6Ra2MwvIwBaT4ce5Hjwq7x3tWyvvGIv0PJExua3vJkpMNkOHjdQ75uY_JTuPL0aYPa1obPEzWC600lDkYSDctPXf4rsgsJwqJbgSiuno-gBs3D8x24oc9Al3Rr0X-9rFPDHJlx3Qvhspd0Lx9AelIS_7GyrzZmjD8e8qRCMWo_SyKOrmDvMcNDh78lcw8Jrx74WhyFHlRqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91582" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk1u6ukAQKKBuMYz_sfB5NrGUXwRSLg7ynWuSD2gIuh6UdUj7MX1_dw1-4QKP4mImh6pAftX50tuHEXatYfBUQ7GcmjK9Au1EYD8CcCKYDAbidqrel48iNyGok9SZOCmVX90u_Xdk-qn1Rj3k7Wi_IboYlKbqQiz_fcrexL6StN2tzXY1Ptz1gtQ9qRvlD2xk6UyxnqHva_lTgTPVmcKXv3Zg9cmnpdpL1IgxRxQqyHejvR3DKtlBMi-mJr5vy5bi6n3IyTkIxxDsAvO-Bh1WBDmV2t7_A8bU3xhPjD5S31D_cpfrvva1qCGLDdnjtlKGgAdE9ZFrd4N5EQ2W9QxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91581" target="_blank">📅 20:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية الأميركية:
نريد رؤية عراق ذي سيادة ونزع سلاح وكلاء إيران فيه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91580" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يفيد بأن رئيس دولة الإمارات محمد بن زايد، حذر نتنياهو قبل السابع من أكتوبر بأن حركة حماس كانت تستعد لشن هجوم كبير.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91579" target="_blank">📅 20:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">إعلان
📣
🇮🇶
🔻
🇱🇧
*تجديد العهد..نرفع الصوت..لن ننسى الشهداء*
موعدنا غداً السبت ٢٠٢٦/٩/٢٦
الساعة ٣ عصراً الى الساعة ٦ مساءً
المكان بغداد - ساحة التحرير</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91578" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
🇺🇦
بوتين
: كانت روسيا مستعدة لاستئناف المفاوضات مع كييف بعد الانتخابات، ولكن أوكرانيا حاولت استهداف موسكو وهاجمت مراكز الاقتراع.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91577" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQaWZc2SS9SMdRqQxlLiLsIJ-bUN0pl6cd89tcwKZGslWJdeEbKN9p6vAYnhAmO3okr0kJJXn1ZTwZabHtbkoGFMW8IBJeN3x9AwFBZdV03k_1JQArHZj5claNj7kAb5FTf-3juLCiEY21WgtAaT_JeqF5VusRIeTPjs22IX_nfI_NOZG-6duhweQOU0oKPrRNmApjblO1u0nHCTp5D_WUyCt43VBPU_zJGqMT-Aad3ndfg6o9PR-3TZ08RiG-6kPGUN9kyzMkO9xUqEW5YcHUampw6gZqR628PwG3dpy1FMh2JDUc8L6dlOYXzR8-f5Z_n9DggO52mEVjHJ_aN3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
: ‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91576" target="_blank">📅 20:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91575" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
‏
مسؤول إيراني رفيع المستوى لوكالة رويترز:
سيظل مضيق هرمز مغلقاً، ولن تُجرى أي محادثات نووية مع الولايات المتحدة حتى يتم تلبية شروط إيران، إيران لن تقدم أي تنازلات بشأن برنامجها النووي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91574" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
معاون الأمين العام لحركة النجباء للمعاونية الإعلامية حسين الموسوي:
طهران هي التي سمحت للنفط العراقي بالعبور الآمن من مضيق هرمز فهل هذا هو رد الدين والشكر العملي؟، طهران التي ما زالت أياديها البيضاء تطوق العراق هي التي فتحت حدودها للتجارة العراقية ومخازن أسلحتها للدفاع عن العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91573" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق الاسبق السيد عادل عبد المهدي:
اغلاق المطارات العراقية خطأ كبير.. وتنازل عن السيادة الوطنية ..
والتضحية بمصالحنا الوطنية ومستقبلنا
والتراجع افضل من الاصرار على الخطأ.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91572" target="_blank">📅 19:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي: التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91571" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي:
التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91570" target="_blank">📅 19:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 14 غارةً جويةً وصاروخاً من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران، استهدفت محافظات تعز وعمران ومأرب وصعدة.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1032 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91569" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
🇨🇳
ترامب طلب من الرئيس الصيني التوقف عن دعم إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91568" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇮🇶
وكالة تسنيم بخصوص تعليق الرحلات الجوية بين النجف والجمهورية الاسلامية:
كما سبق وأعلنت إدارة مطار النجف، فإن القرارات من هذا النوع تقع ضمن اختصاص سلطة الطيران المدني ووزارة النقل العراقية.
في هذه الحالة، كان رئيس الوزراء العراقي علي الزيدي قد وجّه مكتبه بإصدار قرار حظر الرحلات الإيرانية؛ إلا أن هذا الأمر لم يكن يقع ضمن نطاق صلاحيات مكتبه.
وبناءً على ذلك، وبصفته رئيساً للوزراء، أصدر الزيدي أمراً لوزارة النقل بتعليق الرحلات الإيرانية، موجّهاً الوزارة بإبلاغ مطار النجف بهذا القرار.
في العراق، تُعد المسائل المتعلقة بعمليات الطيران في المطارات مسؤولية حصرية لسلطة الطيران المدني ووزارة النقل.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91567" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91566" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: ساعدت صور الأقمار الصناعية ودعم المعلومات الاستخباراتية المقدم من جهات صينية إيرانَ في تهديد السفن في مضيق هرمز وشن ضربات دقيقة على قواعد عسكرية أمريكية في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91565" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
🇾🇪
التلفزيون اليمني:
- تم بحمد الله طرد تحشيدات تابعة لعدو السعودي حاولت استهداف جبل نمان وما جاوره في مديرية الوازعية.
-
مصرع وإصابة عشرات القتلى والمصابين في أوساط التحشيدات التابعة للعدو السعودي قرب جبل نمان وما جاوره بالوازعية
-
إسقاط 3 طائرات مسيرة وإعطاب عدد من الآليات التابعة لتحشيدات العدو السعودي قرب جبل نمان وما جاوره
بالوازعية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91564" target="_blank">📅 18:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئيس الوزراء العراقي خلال كلمته في الامم المتحدة: نؤكد تمسكنا بحقوقنا المائية المشروعة والعادلة وندعو إلى إدارة مشتركة لموارد المياه وفق مبادئ التعاون والقانون الدولي</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91563" target="_blank">📅 17:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
رئيس مجلس محافظة النجف الاشرف:
نأمل من الحكومة الاتحادية عدم الموافقة على تنفيذ العقوبات الامريكية في مطار النجف الاشرف الدولي المتعلقة بحظر الطيران الايراني لما له من تداعيات اقتصادية على المحافظة ومعاناة كبيرة للطلبة والمرضى والتجار والزائرين.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91562" target="_blank">📅 17:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صحيفة فاينانشيال تايمز: الحوثيون ابلغوا الاتحاد الأوروبي بأنهم لن يستهدفوا السفن الأوروبية في البحر الأحمر، مؤكدين أن حملتهم تستهدف السعودية وليس إعاقة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91561" target="_blank">📅 16:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اردوغان: تركيا لا تكن أي عداء تجاه الشعب الإسرائيلي أو تجاه أي مجتمع آخر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91560" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=aGKrBT1gKkLVSVD8xztq4NoioG0XNJLws1aYALzb8ITmlPxy_i4QjuvdWgCylxYVuNWZ0vabAxFxD7a9vBAoUhcGBDZ3Q6WSIC93lXkLajpzokBWz3thI1WGpdMFC1ioRmvLzUjGFndSmn5sE4mcSLzhSLCooZ1zkYD16bcLQyhG_EnsQ_-YMuAVAWX0MbuO_ErX0cPH9K_t2vcZd0XFsZbXcexpluVsytonqzBcJktlwGK4EcvmbpoRJ87YnPYoWWpKGJhKohds_ClZwzMlrpU9BZKLjP-0GYQc3FoqWFFilFzoAMb2_5sIVqJgEoumpiLMcfbO_3Oy-1wotgokyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=aGKrBT1gKkLVSVD8xztq4NoioG0XNJLws1aYALzb8ITmlPxy_i4QjuvdWgCylxYVuNWZ0vabAxFxD7a9vBAoUhcGBDZ3Q6WSIC93lXkLajpzokBWz3thI1WGpdMFC1ioRmvLzUjGFndSmn5sE4mcSLzhSLCooZ1zkYD16bcLQyhG_EnsQ_-YMuAVAWX0MbuO_ErX0cPH9K_t2vcZd0XFsZbXcexpluVsytonqzBcJktlwGK4EcvmbpoRJ87YnPYoWWpKGJhKohds_ClZwzMlrpU9BZKLjP-0GYQc3FoqWFFilFzoAMb2_5sIVqJgEoumpiLMcfbO_3Oy-1wotgokyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91559" target="_blank">📅 15:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91558" target="_blank">📅 15:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91557" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنها در برابر دشمن ایستاده‌ایم؛ این چه اسلامیست؟
به نام اسلام، و به نام محبت و ولایت علی بن ابی‌طالب(ع)، همان پیوندی که دل‌های ما را به یکدیگر گره زده است؛ و به نام ملت غیور و حسینی عراق، ملتی که تشییع «رهبر شهید» برای آنان نه صرفاً یک مراسم، بلکه صحنه‌ای آشکار از ابراز محبت و وفاداری به ایران بود.
با این حال، اگر قرار است در برابر دشمن تنها بایستیم، این پرسش همچنان پابرجاست: این کدام اسلام است که در آن، همبستگی و یاری متقابل تنها در شعار باقی بماند؟
از همین رو ما ملت عراق، خواستار توقف فوری جریان گاز ایران به عراق و مطالبه بی‌درنگ بدهی‌های مالی عراق به ایران، که بیش از سه میلیارد دلار برآورد می‌شود، هستیم.
همچنین باید معافیت عراق از محدودیت‌های مربوط به صادرات نفت از مسیر تنگه هرمز لغو شود و نفتکش‌های عراقی نیز، در چارچوب این سیاست، همچون منافع آمریکایی مورد برخورد قرار گیرند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91556" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1vD3Se-2ZkeeZqT8_aQ8T3KM41A0mcVSNo5_EJjKx8bYwJvliXJzqYRt2zGrIwdLm5_p0c4sphPiiJ5sEybd47afeuNutkjx4oqwUUOc8Swuo7DtHwlTmeECng08HhfSRQcIdhPRGqmI_UN7D_kYq3sP7zJQLyVcx8zVnTFrM2e3YObRKcJNxwmUBh0Di_8a8S99H7N200iY1Vd-6forXhrXOOL7Wpgt6kv00yNRUwEv6tP1S7Xsql7QUFBApBE1KH57o0aF8TuiSKCwrEcJi7JnQu0CD1u7zQMTbhAp5obVrD2yZcvqhE358R0fYijCIfYc7z_3PWXmwmt_pEaKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ناشط إعلامي إيراني يخاطب الإطار التنسيقي الشيعي في العراق:
إلى متى تريدون أن تحنوا رؤوسكم أمام أمريكا؟! هذا الطريق ينتهي إلى المسلخ، لا إلى السلام والاستقرار</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91555" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk6XyBr6gOM6MF3AP6Wg--88rRnRHb36IBfcP58rLJp4lJAGpV0a5asXvrpSMZqQ4MgscJkhXTytOnq1yFvDiTiP7Jj7_SSjVIoUHTRXZXn_MfeYRkGHlXThTLxDLCiVd7t7BHLVLLdiXwEPFS1x3MnTsw4rrY7iUN7qf_8A0hNxgIaKyVEkALx_6XTNyCRLAZRaW-ycecUQTcK8o4PbxYRcqMf27ASvngGSGIIoaEFnZPTkLKgSvJaweLCxYPX5vtQuAjHZ54i5bdJsjq8pqxNt_IFtpgi7L93TOgxQZotm0faTow1GYvu3_3YrOrBEP-Ip7olCKTbQXUncjqqIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في الشمال</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91554" target="_blank">📅 14:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سماع دوي انفجارات في شمال الكيان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91553" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
