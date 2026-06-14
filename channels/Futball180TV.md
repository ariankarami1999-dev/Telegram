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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 543K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-93053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbQ4p9kd6yl9xHrABiszmni1bDh2DzrcryG1cE_DJ18FuNT9ThRNpPmdZYx8rJzeYTKkkGuQgW0AKRqt2FGoopUxLGgQDnAjduOo60eehW2l9vvgiYgssBjnAOeKFdmQolT1RPamEpvQVS7OwZ7TbWSlyBhE3e3nWqivqhlFmPmMfrzz4GrT0PaxU8T1tqVFuoADm6ho91HzEGYIajqa10Xm_KFi75TVD9sWt1IIbAPZZfLwMfydOw9KTfdu1ZeDxPFL5XeTjk0yJJl5jmUQTwb8npGs3g7_-wQg8mwBJHnT-ZXrBm856AJK6c_dmdJoqK1tQtXew5j71gKrdttrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تیم ملی آلمان در 10 بازی اخیر خود در تمامی رقابت ها پیروز شده است
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93053" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93052" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icSj4IH4GQPoqtx0KZoWHOUazunxpbdUlh2HMibHTaBPv0s_4BZ4NjPlcBzqRJzeopyLrQvc1kEvHRKKEK_biU1EAkjMYo4O0MidY5UiPGixpSsYyKqkikTVYpBFZHuWxckPpJGc6DDKjafw2m3jqcup1pW9OQ7Taz3g3kYOqW9FLtji2TpHNHoAj2u7bxOmZ9nKyDQ1QLO99zMleOJXyaTyT3ilbmrA2n3zfj5QOcw7hLzdFtC4AilM-aMUbeUwC3evGwqCnUBNqSd4l2mL2rpTTKkHaqi_9J-Xs2r3T2wg5-YjBBXnFUdFuIeU8z-9XyQwJJ1Pkg48btdbEVpJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آلمان جلوی کوراسائو ۲۷ تا شوت زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/93051" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
#اختصاصی_آبی_تاج_اسپورت
🚨
Coming Soon
🔵
🔺
💣
💣
💣
✅
بعد از محمد خلیفه و بهرام گودرزی، سومین بازیکن جوان و ستاره هم در حال نهایی شدن قراردادش با شخص یکی از اعضای هیئت مدیره استقلال است.
🔵
مذاکرات فشرده با ایجنت این بازیکن از چندین روز قبل به درخواست شخص تاجرنیا آغاز…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/93050" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D29-yxYNJuCOqV3CVzWnyJDE4ycgmrQk2wtJb8xdIfosUSNin6UQfBmV34d72dxkWyv7Y2qdAWMNLMqGlcyTKzAtzvpY-67gQbJMM1EUUGQmD7TAIKCcpuvzS02V7oNczLLix-df9yQ5tGza_O83B0oEp79F4_3dxccqlgi0LsvYKZQ6KQC2dQP7Quwwhm6P1WvN6VuZGKwOFAyrKjWP25HZ2IIpi0jju0AxI3sWX-lv2bM5Kg-xZNJCKGEUuBH0E6gB_nhalInDTm_LRamMm8kdudftEGaMHy8v14rstzTLJhBXsoKouwopjJ3Sh-VWe61LXzsAoIDs_JyKfg_H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAL2vkfTX_cXXXulVTvC0DnZ-PHyjkY9NrPHugyjSX8Sbtwt8U55P-oje7W8Y9Blu7oJedd04EHnQS93naAeT8tl3zevWHmo3Fo-dkg5ynREa3BwjEwWxcfcdsRfE87NgaAbIcM8arE8Ji44P1nvP3-DAIB9xC4B2v78V7T3ACRWm4hem9IvSjnhgFa37YjbfU9nyL3D_nqJ0Jhm1XRBH6bHeE3BuzDCj-h28P85DEkZRc5gWmh-p4Cp-SEaFettJF6NF5tFl8lA2d2hN6wLbiLYXvr7mybumBHssDU1xveL5jWcrRNI8Z-kvNPzDgn4-nf-62s6SsIa8a4ShYviow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtmaB_1MUnEZjdvbGOBQK1hKe3vqy9RzUaPfe3X6-GIKhqsMpcZleaCAXL_gipELK4FDVDEp45bpFhoGxFQHZZZEsfOV_FDqBYL-dQ87tN8rUJP8jbTHuB2Eiz59psM_V6Zm59Gw_3VZHzEKT_0TMkDDgiQh8w-bA1aSSrgx6fZIXLmKj1CE7s7xwT3jJw7SJoJvMAIXMIawrSa55fK8lFrPgWvG5MOlhg68Yt0EPOQnhX6OAJDKwGZXH_AHCKeXnrggZ5yd1ICdSjfZ5qKIBRjORDZut6-hbuPuAqZ7lZnNmHZQ3WNm5Oqj6rcVT_sIFa9tBNL3KnuCCc_mhEIDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3MXbFCtzS0AWm-3ZQaaXmdFXf7_uND378E0KqCIhhqjS0hi5BmODiz5t7gHbn3eILD11ToZ7pHMYrYv1Z0aFWjkwjuLl9xQ4fosnncMH_sQq4yMHuq8RwZ_Sq4M78bKmchelHay-5JYACvqVxDR9GwspjU2W4tVDqE1S1flHcrpTW3eX-Prn6xt78vHznqtfaxioYcrczOTonPU17H3Huyf3JNQMuCR6aEbeD_I1fj7KyyNizDsUBHrdyPWiFcbskNWd8prMrn1zULsxB9bSdLm5jbz2kWe7jlQJz9VxqHv0RZ5Tlns2maFJ2Dg-a46pGzvBZtE578lSBLazAURew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE8HsH7fEOGjpUoDsVozz_U3SiZCucqsJ8xwelqNFrncmtLPajyz-xazaBwKpHfMf9vJiRxEC4WgpQpuqb5dMMaU4lHHEG1jn6nXRod_WKmdxBP4ndr9GMwA06c7MrUkgOv6FPhE5Bfy4odvBaHxXz395vingLRIPzPKr60dvXc0Ou8kiNKREEva6z2nxYRz9TC0ZBU7t9vPdSvHZ29b7ObFl42uVD6yIxEeo5CIMIVRgaZSpz-5dWnA6_kjXu8uqTzGZ3kyJ3Pfu930nQOP3KLN9p5BEqrJBUZAnvR3mp6PKvioHIztF_x0ggIdg9lKXnoXsa28wL6__LlnjC1nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja1BDJkwcvRELHNkbGoK4z5yMfKX0vOjQwrPJ8MyvQd87QF5CiXypqJkxAIUPkJbumOp1ZeLYhh5K0ImQdj7SOOn2L0oMmqpwCDwiyZuJInTuOKG4fbYc9pl_WjG6YbIdnOMxvvZcn6PIoPktbrxgznaJbANcxhXIdBqVm6knltHlXtTjCPqXlid0rFHoNtHlZsNhlFrD3E9U75F_ugby2-Hxgd7QO3pu2PnU0zh-Tm14Z_mt1U-pSbDmzUvlCVCNyglyNUV2nuM6DuxM8GA3fHQHMcPxCGcGAMUhT_lSwS4z5goKElQxLC0dm61IkumJzSOZIOgGDKsyqOZ_kON-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy3eSRsLYc0nTHok3gSGAAK-N6wh3VHkjqjKon46yEPz3EoeGWx3pTAZM6eb7Cu9Asjo2EHxrCQYEIDk0SM3BpBOXkjJNnhJm4iO_3_n0j5eoa7kRz_04VOKt7Q3ku6q3h2aiBraYj2Z897N3YHeLi4eoJbES7xBj7GGuYbKYNtTrnwMVS63mJc6GcOiVheWjcFmOcjATseflpmrYIavcu0KCWWuGl25BOjPwmA0gdjIritvM_3syJ4N3B756J2LJn9jM4DmFfX940u25GuVrLm8Kh6YqL2r53_b9D-KM8Cz2zZ7yQ4c3t3h7iaTl_DyZ3P1CJDhm_dV1WnUVd6DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJmJElSvNHI_YG5eWDZy4SqZCpST3bEga8a2DAB96NDLqaZ7Q6YWtWJhSIiLXLx2QnoCTev7DzgFbA5FanIyswCtVbgE9DvTpXcnuqcpPA6cIQr7WSeCSsXJDEINrJVUMHQNtjyuVKOw59dQpf5KJp7PLTkJzbqrZLzNJzwxCnfDjQsczjez177iYm3Z9NrjMVzFKmyno9_32hm4ipe_ZsDhZbompS8SIQvosanqOLPMScEbEO9gMGDJFDRYVhy7OWMG924f634G5QflpC2OxaLf-90Aojaon5T0WFoand-wU3zkYK5zfvQGLhW4qSK43QoRko6iprTNH4CbFefZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vbmq7OXWv60-8WLbDutJ02J7OOqmljqZQgT1qboQc3cC3EtChjHV2UuR_SLrSaZeYkqOtu35GvBHIQPwVRPXToLGDzP4FGnkyMzhN276sQOxwViRDDsACt8eFpmQP6OeqxTdc7aoYEzcHhJoD6p2EzcsDT_cGe3v7MGlsqxq8pWGa-hmwe5a7XsblD4gEoPLXnmCsheBpjmOn1g7EnZhvCpar9ed5vyrVraOTVmOXlYoKzjz5VP81ZnQ-Gj1A37KuO_YKi9PTWU58a8nIPxUwE2LMaaiWwBwPoxq-MlamhLyMfdUZIiUAx9c6qZ45mRUopPy8AG5vOsPhBzUs6BQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jk-Isi5aRSQaGPN0UXpj7hsM5eDzI-dQJJDyzWcbM7xBwM9sMFJUnIbkgU1O_2pU1daCBoPAHidedLWHXLi5a40L7H_q8J-iDHJJn05zuPW5OkuynBhxGAK5ebS1uC-uGHr3DOJFtyInTa6ZAQsPe8R3kpps9fQRewMeHi0oura4ix50YuZvYnH6yarfkzQMGo3_evaUbn7qaQ2K7LHCB_xG6CNBOAB4sO7pVChTI8_cWvNlIH2-z5yhKN3Cj1kzdvtoLv-9zMpu-bGKO14kegd_lkGL9LCAQ9_EjWVLoQFD7RjoJLq-9DITXdMn1EvmX_6bFM-b4Wu7opck65tIhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب برای نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/93040" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArEezXPnAUO4fo6kTlr0V4cEggscbQ5JEtWqYm2gPcRhvFg4z21YIiDmAx25f1_VUVteCiw6_rukcfriTgQAhSez8Lg579rlZdeTxYv6ihLeCoW_QfsOzVBKJsXkAw93VZzK912CVOg_tI6pIjHVbmi6Gjd8HNg33LWauRYhxldkSPDNbDZH2hH9MmOXoqSK6jcAvh5EKJ7nil6wxtqRNqOAnzmpJ4FfK3JS2TqY7PBLk0ok77oMwqU3A9XEmo8UsKFkXcy8fRqhyCgwAa5ii8chpfn_IsrBkLSX8wczxpAOlGyx1IUrQxDkbY-I6nL9_1prN2rxF5j6a6i1cWAdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/93039" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVCU_WlA4K6iX7rnAI5w76qNdmPjCij3robI4hAqestbQXmIb4G9q1BNJs21eFhZSbfCPEAyzqdwyvJ-48KUtJP6mew3Gu8uFTUq_PsK5EY2Ifh9NBAPHGsan5mgs4Q-gTBF8bA0hN3ZBuODN_fqMkvoNIwpwIbvBOGGHwQKkyNkP5-InBCgMKCvkIcrQ3_jAMX8xNXzifKh68fk32byfz9m_h6zcZcnP51eGKiPA_4Um2NAAc2vSNKrCBN3pdK-dZW35m0vfKWhYXmEU-mlqk8Ca_26jiH7mvJQ3Tp619BDQDXJs_yvNCnDbYIQawvBE982wVlAxaYUlBwJ31oYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🔥
🔥
تیم ملی آلمان تبدیل به تیمی با بیشترین گل زده در جام جهانی شد:
۲۳۹ گل —
🇩🇪
آلمان
۲۳۸ گل —
😀
برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93038" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هوادارای کوراسائو دعا میکنن این پنج دقیقه هم بگذره</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93037" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل هفتم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/93036" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هاورتز دبل کرد</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/93035" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آلمان هفتمی هم زد</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/93034" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6OTy9zDZKxodWNoxqmImZusRfvev3YlGWhxpqS9Qa7HiUTghl8gqNpP_cZPET2zwl1zJEmcI3FaH6LUwzOdTf7HrP6v2Ejc1xeoieBVKSiMZdoB5pbf0ZWDY3eG3YX716w_faItKaDpRQG-2kj-uurlObEYFRTYav-f5idJOaIyvEVHpEv91wfUuNlGgimZ3uMNtsYPelV94ug0d9Hhh-85aIbxGwlZhhbj7AeOCHW-7NGv4C_8nnWkXvlVvVTXSBht8l3KEUiLXiIrdbCa5twcKlKLvehTzyFI02FPujsFOcZ2CGWlFig9Vq_NO9sOXwyq_go6sf-la9Ga_a8BHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/93033" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل ششم آلمان توسط اونداو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/93032" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آلمان شیشمی هم زد</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/93031" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQIUYvvCSejeE7UgEE8WsyLugg-Bpbn5U5YQIL2ze_T8JcNlDWr8IAXFTtsuSJfguud_CQNpkU9FwRgw2e51GKnpStHAZ29J1dtMNwpxB6a-a5Ou5ENcyd65YywtGyaZGYHoz9LBIaJZIreC_sPNrvvaT_9wauIPcLX37s3rQTyqMgcrzI20PFetr9hSxKxy7jHLP_2n1yTERvKUMjYZq_MkJdIb89wdsjBGwa4j6xjRFn1R1IAT1So04bRep26gfbe_kcu9UEuH0Jw4SnjZyhq2szgrET7YEFKMcrpi_96QEmansxQCWbar0tiBVey6fEVjxgbEq4ZApz_QJfv6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93030" target="_blank">📅 22:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rZEm68Jjzm92CnKBxDwA1vPg3u5h0E6XaH2AUmCttEjAjIWtw2e1tWZPX2sxA5eiY7RM3c6kdLiCknNndb8o2XmKQawKx7DxlYr-GHdeGKwtPo8DwnoGixk0dgrBWokXSAMDT5jgcd2Oeqc9SVG4R1q2vZkQnJK0YNEIAEt88JEWYOL97HuyuaZJiwDTSF70-eit_v4lV0iIZTzMOneHSogqhxZzfeXs9KGXz3Kj_vlV8XT7YEZ3HlMXT9cpQ9-b7WNuvPFJnYGH6_XkeYd42-v-94S_GcXyXQPuNWskkKCvGIM6kfUF2a7-W62QEp23Fjyt28rrJ8l10tFTZyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار کوراسائو
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93029" target="_blank">📅 22:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
پشماممم از جو فنای هلند
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/93028" target="_blank">📅 22:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل پنجم آلمان توسط براون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/93026" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ناتانیل براون گل پنجمو زد</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/93025" target="_blank">📅 22:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلگلگلگلگل پنجم آلمانننن</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/93024" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📊
بایرن مونیخ باشگاهی است که بازیکنانش بیشترین گل را در تاریخ جام جهانی به ثمر رسانده اند.
80 گل - بایرن مونیخ
79 گل - رئال مادرید‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/93023" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کوراسائو گل زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/93022" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg60JmXiCx6RFjTwI5nYzfRWcKXPTG02u12Vzw_OArQYP6KyGWklXBIAt5JHiNMBzELmQvO5lTzPS-2qrlSeTZd3vditTwua7xLN5P_fZakqPW0lMNq9gV8_24K-CQPEb7ENBwTFr9ovSwuxyjlBL9DuVeQX-N6XkInJZAlGrr-I3KHcO3ToY5KJoKQNWxSFfSs2Ya-ay5pLCra07_pNGfAoJMnDRGtgRfJEDprGJMvImZC7pe9-BstH6YOoHRKtdNcrWEc_zh3_P1t6tgg3pkkTnWK63LBPkYajwqNUqwxE-RenXsnvyIYRSNBuQ1woXGnEaAIKCKsBy1vPVGpIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کای هاورتز در جام‌جهانی:
4 بازی
4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/93021" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kujou88A9MidY0OrtF1IftEoTcOqnoI6TO0dEeld7TC-fxqHW7CMbEMlIQ_0dopDycRRPcRBYotbBiYkeow8DWK6r19F2zgbMkxGn7VyoMRK3QSlxrkrS_u-DJLT9ViNyH6ANpEER-2DVKkrWMEdZZ9XqfttHjBgzHhHSpxOdty5J3sfWLay-efL8BanH_kayDX7AkCcqXTDm-hyGmuHSQc12HhSybBmYcoi-9-FaFBhHlj-EkN5zMmV3FJvQjvAoiJOBUG4XJg9H3f85JTYNt6THnIAAGX2_PzVm5dqBwawQBr7QIq-yL1O3Uocz1bIEinrMxgYxEl64KFbKj3bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه
😈
🇧🇷
دیشب موقع گل وینی یکی از هواداری برزیل کنترل خودشو از دست داد و یه لحظه ...
⚠️
👀
🔖
کلیپ کاملش رو داخل ربات زیر گذاشتم
💥
🫦
🖥
🔞
https://t.me/FoootyHub_Bot?start=HyU5AoEy
💦
⚠️</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93020" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/93019" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/93018" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBkCPE0n_HkkH0bGgcsjbOrCRTgeaLGHhcd4fUOpx5tBYP55CgOrfeufZ6Sx4gNnVpGI3oUDaujHmn17GaxwR_TseAm2SoUQwJrdln15PwMUvtxeE1MdEBcbICLoBczUffZ2XNyCWt1e1Kq4BMp8pAyrFnYW9y3TOmonLmOpd000sEtvbQBqkvEyT2fbdk4qlYF3BaBuYKAZhh7CPN9GD9LrCXIL7XhjgnHhIzvb-flo6yPNMzSw0ThJl9sGuPnIUA37N9h_0gt49XvRzl2vcmFXl61pN5PABIMMiz8e2wvWdcvLNXVUVPHooz8Lg21Y5d0YaIhRk2e0OtHi-RiQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور هیتلر در ورزشگاه برای تماشای بازی آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93017" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/theusWaZ_TYax9nJ5XCfYaCsnNYlVznz5UmBObslk8unS-9KINphI9ibRGeezyNo6gtAQNMAN-Bo1gBriBLd1ub7oEH2sateb_a62ze8sRfOKDknDbZrbnHnLKl7uQiME23Y0QlXEb-SKCspwWNBoetzmNCo0vuOhzB6oTzuBPaHAZMZVY5NAQztjp9SzXfP40kHiPL6-DX0b2D3ffOoo5HPnAPUkVLe300f-cN9_Jrl-2SXIuJR6QnAuDv_AoiQBjKNJXu6CFsJwqMDoNtkUYoHzTInqgsunpENjZL9FJz5Y5Lrjawr141OpmOgzYxvGLqW9tkOMXHptvQELnZc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇳🇱
نمایی از ورزشگاه دالاس قبل بازی ژاپن و هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93016" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل چهارم آلمان توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93015" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلللل آلمان چهارمی رو زد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/93014" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گللللل چهارم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/93013" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/93012" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENa3Wtk6jwnSJPOGmSdDDlc7wqEaANghrLwUSyEFt3Y-VRnhwULun9HR8qIeamHfDEXh6rDZwcxbKjU6AAkBAOfTB02Al_5Sx2GVeG1WDfFWotKxj0yE74Yi8R-mJQqhDleVB4uOZzDBAiB4eCpL0iEl8fvCGEtj0xTunnQHYPOsINmvLt7wIPwxnV7M1QttjkLBlg73TqgpOfeN0SthZNyNA147S6cl_6pHgb_nP-O98jhog7Hdvf8MpZTP8JPy8xAFh1If7d6g_rAHVg5le0Rl0n2PfmxoDdlhgDyxhUWjgsdRFCbubL8075zGX1wcQ-04y2M0JIMrDepdrVuC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار از 1 ژوئن 2002 مقابل عربستان [4 گل] در بازی افتتاحیه جام جهانی، 3 گل در نیمه اول به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93011" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfF3x6-8yYvyqbpBsSEuwT31NtBthbXDBhBd7f3oV2RQWS-JtsJVwMJgQEaYWDLJlc44KNzxdaI4CSZpxonI_Fw9_SnzD038iCgsCh5yg9VySwvFHjxezPDHB5Wh_bGcZqON2zV4yMN_YcEZ91ktkauNMlPVtSMRtD_Kwqwx4LMeAwT0l32-8LrdsymlUCcQGAhX6su2IY4pacdvWZLH7CVcYkdEMGPcor53nO9nxkf8uelvE-TmI1SI4VcCUGf4ltVjGHbyfbbxE0XxgMk4Y8q09WMeBMkoUvKvA_lh6DtPhzWcI-Nbnyd31U3uTehoc3b5A3-cU-kbns4t0VCk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیک ادووکات سرمربی کوراسائو با 78 سال و 260 روز مسن ترین مربی در جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93010" target="_blank">📅 21:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پایان نیمه اول
آلمان 3 - کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93009" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93008" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلللل سوم برای آلمان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93007" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پنالتی برای آلمان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93006" target="_blank">📅 21:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqm59a4aYC7VHPyZP4THkRs8k3-MoXwb-BugWK8GG0llOyJdaXULS3q1ML-VpmwwvntuponDE80f3NUBOuR4JvPrSkm-XEwyCuQH3OZeHQdzvf5o3Se5-fuwscq9dEp_RAx-aDScIC3uMWRG3m62RXDu1yVbVZo4JGskL2AAjpfRhF_RVgezp83WltmICNUpdH13vRCSJKBDNk1Om0-79O_zAkrPwmUu50jSm5QGkUtwNMHWwGzJZdMbncKUP7Tq9t9s7sK6Fv5NSYlJy_UqwBDEkgtszy5VPi9MjsMdj9YNPFyyqy38orpSX4EZTacB6VJpteu523YF30KbC_05hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس رودریگر خوراک میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93005" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9MafFC4eeL7IcIfQpTbVzp9PYNGWScnAuWzCjcbFAYM1DHvgIXRPqswtym8-sv4DUIkJO-MJtaKti_jxh9a6m0oNQcPa2jyZNI7rSihWFhr2wnXTowAZ3yjY9Z9hANjWkr8Ukxr-bM65gk4lI__tmKDlrwNoWxcDJ-sLFi9OtNPc_YDUMusjmxdyHybvFI3zz-QxXOuN7taWJquu1Cpzwl4MqYML16ezBiAUYaiS2AjKIdFxXRXXXgLMrhRv_4Y6EW9yBrXC9q8F74IR-KGF-Bl8eqUmYtmWBlRyHH_N7RD9djX36nF2R4v9F9WBB_BY_hATa_6lAX6FErYWqWRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سریع ترین گل جام جهانی 2026 تا این لحظه توسط فلیکس انمچا به ثمر رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93004" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93002">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل دوم آلمان به کوراسائو توسط اشلوتربرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93002" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcYnpJI2zouUPX5xpmUtiaM7o-B5uv-TeDco5hW0woTOEve0thT7T1Tm6nIs2986j4jZCc71Laalo8A5y-jAyrO2w6QoOtqVFZK7ZowM2T1jiQX1q_xEVmIA2zuxjfsh6QuqN9MrHQZXumvWS7ZqhuRFmt7s3rDtoXmxfYmSyMLtowYsBzC2_VL7PbJrox0BGaV8z_SuEMAAwmO0QjLbnBGio9C1OFQ540Jxu7jsQOlqzW1a40cK1RWNi82U3sr0YPw-OE2t7VMcCqDA4yMhycXA38j-IEJOyeuYeBa2smDmC2duqA_VDZtcHQl_2m5YBDkYI4iO7lRZrB1jSYQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: ‏پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93001" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاو‌ام‌پی فینکس | صرافی ارز دیجیتال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkpu9GRfqFE-cetrgvuwSZkFMgfgj3AYWEUTBlRJEL5sM_EpuwBAJ4AddNGOiuFZTcW52mkNWrFApb0QxA09ZtgPiw_f9BwItHMA98LIa0wFJSGzFxBiTNXw86L3-kyghNIwCXgP9paYdP--vVubs39IZPTFM6islIiz4fjji4dLhodHd60ZIjm4615c0TszTYp6tB7ZUSpBJruVS992nOUoTJ49Nc78SRi70HVCxZ7R0-jw6m0bQ9b9EFbkyl_7buFMmMjy1r6bxd6z8vNBfBHCFOpAwFOLmBMQNQJK9XuaSNBvWePu09ieIPjYwpvmo-hQnQU2dQMNHI0IU8Yx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
تو اوام‌پی فینکسPOOL پول میاره
❗️
🔔
فقط ۱۳ روز دیگه فرصت داری که توی استخرهای تتر، طلا و بیت‌کوین مشارکت کنی و تا سقف ۱۹.۴٪ سود روزشمار ببری!
📣
به صورت نامحدود واریز و برداشت ارز دیجیتال انجام بده و تا سقف ۳۵ میلیون تومان هدیه بازگشت وجه از ما دریافت کن!
💥
وقت رو از دست نده؛ POOL منتظرته
🔗
کسب سود و دریافت هدیه واریز
شبکه‌های اجتماعی دیگه او‌ام‌پی‌ فینکس رو هم دنبال کنید.
💬
اینستاگرام
📹
یوتیوب
💬
ایکس
💬
بله
❤️
@ompfinex</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/93000" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWNKf1OTVCUzMIdDN7aQuf9YEjd3In2XbgjfaQkXHM1sNvnjQiIQChxKwYv--ArGtynKWYHDA7JQgF8OU2cWhNMn0sKgE7ENcjlpfiL_1KDcF-o9MHBvhUynnxaX-GEwy4eSk2BY0nZ2CdRFcFF-xTkkMMXz3evQZXfftcytelhtlXgDRXhevdpXJkoZWOZGwnLFR17MPqOqPsjJy4C2hHzp_p5efUw_YtXt-R2ckqL6W8E5rG44dQ9aijvvbAhG10lCINgtba6RH6P4W6US5yNNJh44CHSQZ1i1Mnk_9ZnBK3AJFR-zh4sfUyItLJJJ82tn-7n-15WJmGTn6OZlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92998" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گللللل آلمان دومی رو زد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92997" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آلمان بدجور فشار آورده</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92996" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چه سوپر سیوی داشت گلر کوراسائو</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92995" target="_blank">📅 20:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGHVX2CQdfAxMBghd89v73A26ccWZDB_SbdtOiCooILVRpXkbSPvzrFpLAlqDD1Z1E-19YWJ0DsBE8j3gkou8e07CezFsp9yw-zBEBdbEkGz9mPXx6NhkqJVjq-LkwNuMTW4uAEVNY1f6BsuxKWIEegIeT8ysgKysxEOVLVoIuDuxoSWutOcUaAyKv-2urNV2oPTT3xjYCa7uaPhGgAxh68aCxJLyBna5gcR999Tpjfigp0CELO3Pyhy3Ds32XQa7pH8N_pU6WiuKlzFmUaupIsr0i0IGmFOureUw8jaFcANvKoI3jNWL-__VTqy4MqGUgCx5HA3iN3x2bgtH7cbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالی دیوانه وار بازیکنای کوراسائو بعد از اولین گل تاریخشون تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92994" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کولینگ بریک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92993" target="_blank">📅 20:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92991">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=Whw2ejG7WD1IFP8waS9_5EhBMcNiByUf48ZNaPWG5T7W43NmSeGeYsXJh_g1eCj_YSYNH8Tu1QnV7dmM4drJ5l37FmpDC344YxJD0ofj_q64V8Fz3T5QWvqyz-yZY7iPvbLFVoF9NEtajn4NCbjalokH2t5w8R301060aKQiyFOnjT4FcByz9UaWvkJXHRFncUBSql2NXutDMQi4grx8MNVlZ047n7MoiwChai2Za7mavLtWg1dDdUjnfIdCPPYaqbrcyVmdnN83X647gW0-4ewj5e2GfKFhm0FkytWtzAKiyoy2zDwuPTgDTPHzw2eWw8TRmL6Y4XZZIwB0uNEiXYewwbKjDVexUtRQD8bmMs0tyKONbYQ0UPGkpuVNPzklCyndkObePsnytBxDOTiE6y_LRlBvUVXdTM1f5AmI0IhO3U6OaAfVCH-G42edExRFIv64lrX4UG68t2--EwlxaGZ4yDvl5njEwMQa3ULA9OCj5Emc96BEvrvsdN705SQbfSYDD-EwKy8kfIbVs1oudTvYtSNzS0I6hmiH1B7sFpLdnh-tWPXoMXMV2kt2Fo_f6OZUA7n6FbipYtoRw8p-4Ojp3GOFH-IGocu8ufYUlS65il7PeHiaa5jRc4iL8Aaz0S_NNuqpvdLoMZcvAuUc37xOXl5LhQlf7vFFTurmRCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=Whw2ejG7WD1IFP8waS9_5EhBMcNiByUf48ZNaPWG5T7W43NmSeGeYsXJh_g1eCj_YSYNH8Tu1QnV7dmM4drJ5l37FmpDC344YxJD0ofj_q64V8Fz3T5QWvqyz-yZY7iPvbLFVoF9NEtajn4NCbjalokH2t5w8R301060aKQiyFOnjT4FcByz9UaWvkJXHRFncUBSql2NXutDMQi4grx8MNVlZ047n7MoiwChai2Za7mavLtWg1dDdUjnfIdCPPYaqbrcyVmdnN83X647gW0-4ewj5e2GfKFhm0FkytWtzAKiyoy2zDwuPTgDTPHzw2eWw8TRmL6Y4XZZIwB0uNEiXYewwbKjDVexUtRQD8bmMs0tyKONbYQ0UPGkpuVNPzklCyndkObePsnytBxDOTiE6y_LRlBvUVXdTM1f5AmI0IhO3U6OaAfVCH-G42edExRFIv64lrX4UG68t2--EwlxaGZ4yDvl5njEwMQa3ULA9OCj5Emc96BEvrvsdN705SQbfSYDD-EwKy8kfIbVs1oudTvYtSNzS0I6hmiH1B7sFpLdnh-tWPXoMXMV2kt2Fo_f6OZUA7n6FbipYtoRw8p-4Ojp3GOFH-IGocu8ufYUlS65il7PeHiaa5jRc4iL8Aaz0S_NNuqpvdLoMZcvAuUc37xOXl5LhQlf7vFFTurmRCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول کوراسائو به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92991" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پشمام کوراسائو گل مساوی رو زد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92990" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWqDARsdck6syN6CzDyUyFRd6bD_hqmnxpQJmydIotItZaYuC9jRvelm3CnpMa-E-aYcv74jNmNEws8fzQEQihJEz1D8ozXGGDNPILXHrzsh6rtYVf-LUp9Rs_cON7estNM_HNolqMTywJ6B_YLhqV13G17J369H_HST7sQy3Gdl68nb3Ag4mRpdVdmPurfUZSpAtt5ebH6R_KhkgW5D3JKPvB7lcj2YKVbt_C0fULOfEqSczvirVKTILkDbR5pYpWNqolmgKlAmF55R3qhywFdv6ybWTArC4755UsUuMwGLWqOTYc5JNZixGSe6gZjBxVsEJjpi0HbFslN6BvF4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت گرم کردن آلمان چه خوشگله
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92989" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92988">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043736f33a.mp4?token=OCzheIyRblK0YEHTh-Jq2_2Z6K-a52LD_hSyro-CH7QMSoZBSWKAh0tMqiwEHhLE54Imn5MoXt3P_JQY-kbL12qDMa2a42Fk28DGe7bATyqQqcMDanYxWrBKRJkGAW8-QnJfAeKdtPYCQw-kMUxLo0itBHgc3VtnQGHps33yKs1LdrWBAP9uXVHlkfWqaWy1FNpnbpeWdXsx9q2r7HHabWzUk0CM6VxB8msmguxZQg6VeDHUIjkP4QwNfwqOao1Yie54FB34ABoJ4yKoFlfQu5DM7Edzb2p--LLHaYjksaoo8XtLmY6HG5FeXMGAZQr9HfWoH4GO-Fsh8EbboLKFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043736f33a.mp4?token=OCzheIyRblK0YEHTh-Jq2_2Z6K-a52LD_hSyro-CH7QMSoZBSWKAh0tMqiwEHhLE54Imn5MoXt3P_JQY-kbL12qDMa2a42Fk28DGe7bATyqQqcMDanYxWrBKRJkGAW8-QnJfAeKdtPYCQw-kMUxLo0itBHgc3VtnQGHps33yKs1LdrWBAP9uXVHlkfWqaWy1FNpnbpeWdXsx9q2r7HHabWzUk0CM6VxB8msmguxZQg6VeDHUIjkP4QwNfwqOao1Yie54FB34ABoJ4yKoFlfQu5DM7Edzb2p--LLHaYjksaoo8XtLmY6HG5FeXMGAZQr9HfWoH4GO-Fsh8EbboLKFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید : میخوام تو جام جهانی 2030 بازی کنم
نازاریو : 50 سال تمرین نیاز داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92988" target="_blank">📅 20:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92987">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=esNXM6yBGIXifykAC57zeBaG_i0Vvy9r_SzJ-tauuveJb2GC4kdxOibq-S8GERskOGgAxPobL63VefBBwCOo6rB7hWtSCgdjXuRhmz6wiXKGqH-bydQO6wA2DS5QLVhSaF7XXkSeDa3gABUFS3MrUtD5q-GGPbWXu6dTtp6LErMeYf_bqKePT-TTCMGebXJsJqwOga1bvT9XmxpbOh0RZGg9dCNcqFeYU0bIsqWgQbbC_cWVJqJSzZubYfVcmHo4ouYGWDG8OvLkRwSuiCIMupxuQBD5dzy6mpBm1BOy1zA2RsFUh5Y7HSllz2mMA7ng4pLxXm7ESLYwQRIL3NjGjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=esNXM6yBGIXifykAC57zeBaG_i0Vvy9r_SzJ-tauuveJb2GC4kdxOibq-S8GERskOGgAxPobL63VefBBwCOo6rB7hWtSCgdjXuRhmz6wiXKGqH-bydQO6wA2DS5QLVhSaF7XXkSeDa3gABUFS3MrUtD5q-GGPbWXu6dTtp6LErMeYf_bqKePT-TTCMGebXJsJqwOga1bvT9XmxpbOh0RZGg9dCNcqFeYU0bIsqWgQbbC_cWVJqJSzZubYfVcmHo4ouYGWDG8OvLkRwSuiCIMupxuQBD5dzy6mpBm1BOy1zA2RsFUh5Y7HSllz2mMA7ng4pLxXm7ESLYwQRIL3NjGjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند این روز های اینستاگرام از اعلام ترکیب تیم های جام جهانی و حالا ورژن ایرانیش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92987" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92986">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INsSD456q1s340vLdvknEWo6MT5ECzTyG8M_8XRj2paR2OC8h-Mm22AZ2Xe2XxAVrIsbZ56gvDbktqi1BXTyZz-CkYxp2X2YYoja8NGgwq0paT3GIeSzJauly1tI4SRUgEYQU8WzoWRJU8uxtSfRmrkl-41uBDEjE4zEo_LWqmxEIGvc41I0d5qMQ1m2EL1E56f5eJnM_FuGR_DczmY-3kdXon09jp5v82DVccbevWAqRgMIfc9SumLpS2l4oNU1a_YVv5b-vZ_PfdvHb6kUYVKod4M0fA9wIaKs2vJJD7inlYWY2YtJmWmQuAkOY7Msg0Bmsh_cfcxaSxIsU6diSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
برو ثبت‌نام کن، تو مسابقه شرکت کن و ۲۰۰ میلیون تومان ببر!
⏰
هر شب ساعت ۲۱
🎁
جایزه ۲۰۰ میلیون تومان بدون قرعه‌کشی
🔴
ویژه هواداران پرسپولیس
شاید امشب نوبت تو باشه!
اینجا شرکت کن:
📍
zaya.link/p4irm
#پرسپولیس
#ردکیو
#۲۰۰میلیون
#جایزه_نقدی
#RedQ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92986" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کوراسائو کلا تحت جو جام‌جهانی قرار گرفته و همش توپ لو میده</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92985" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92984">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQmsxEIEBrRNp5-BLsFJ9xFMaaW4ZlR7jw3EXNGWvvTIz5aWs93LYg5sl8sdFLwVlxvxLxoVFy-t3-C5v79nEHiurisp1HFuV2o6B9bzv5DM29qTp_PvrStib4zLywRq3gCVndSyT5PGwhwm-fEj8aEa6Z5uCL-uDM0Fkx6i_AUcm66T3tXFmTQv8gIS-oRoBzI8YM3y3ocveMguv-A7n9P7oA5RpmTKDDTMugPwtB7QhSYs3NoRZNSJaij-eFhLHRTrYBRDa11hoIgzDHTRqsCK2gctdldcIg2sby-10ZlPSNAssSM4A7OtFk7_MI-Bi7BzgQcNLqXn4dPSA7Zqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غنا؟
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92984" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آلمان می‌رفت گل دوم رو بزنه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92983" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=ZnQx7-KXBNMT8F2WX-PFfY-apVlSxTvt5fPaqoMdtUzvr3CgeTeRj7d8955rBGVKHZZdprqc1NCizkWwPgkNYDMAlti_H2iWfi3gqDRqXmpmX0hhG5ZbkvNfUvdcf0L0Gly5oeNyq3QS3VGncCjPlSJRs3b3s-yKw9bNO5J6wG2nNQSRhMdJO1nYcGRoHEal_cWpFrQjlfdENqUYgg91dZqSy1Uh_Rgo6WpqC7i-Bnvq1dmykkC5fVx8GJcA1cNpuQapa56IBduXWLffA60Yna1hE2fYIrxk8IAVX1QkoGCIVEb9_u8pXLJteBYx7URUAH6Q590_d2UeRJhPHnYIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=ZnQx7-KXBNMT8F2WX-PFfY-apVlSxTvt5fPaqoMdtUzvr3CgeTeRj7d8955rBGVKHZZdprqc1NCizkWwPgkNYDMAlti_H2iWfi3gqDRqXmpmX0hhG5ZbkvNfUvdcf0L0Gly5oeNyq3QS3VGncCjPlSJRs3b3s-yKw9bNO5J6wG2nNQSRhMdJO1nYcGRoHEal_cWpFrQjlfdENqUYgg91dZqSy1Uh_Rgo6WpqC7i-Bnvq1dmykkC5fVx8GJcA1cNpuQapa56IBduXWLffA60Yna1hE2fYIrxk8IAVX1QkoGCIVEb9_u8pXLJteBYx7URUAH6Q590_d2UeRJhPHnYIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به کوراسائو توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92982" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گللللل آلمان اولی رو زد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92981" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آلمانننننن دقیقهههههه ۵ زدددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92980" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گگگگگگلگل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92979" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4fWHgAjGEDxUq4NqaF3NKG2f4uDhM_DN7F0c-K-GrdfICNikwAcpnIey5-UaqTuHFDpL61LRxxMhdpuDh21__HN4mEowS5qkJNaPrecs3uTtXyy2H36JWFhTOJzXPU-rSRBgrVwYXSfXOYm6uP2eM7BPBBkm-Ug58cLCV-e-pWHeaoDGZKbcibDZClNhPwj93ACB5pYLEl_V9XsLuSdo1pEcTlsIIaoQKubz6WDVsoJf1l9SJBGZ8XyTVsz0S1PGKNSMDqubmdvs0VrEa0zq6UqRMT5L06yqtRW-JMeASGtA5dJTve2Z1hm7jCmAZtddDUemEj2RortStbhlKE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
: شبکه ESPN آرژانتین: مذاکرات وکلای انزو با رئال‌مادرید از یکماه پیش تا الان درحال پیگیریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92976" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کم‌کم بریم سراغ بازی آلماننننن و کوراسائو</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92975" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG2i6HHWMlvAzI6fmTjCtBLLoQidcUxjPwuY4XDi3bNCDkhYMjFVH7WdSM9p5q5wrH0BajfTsQsbKe3m3jq_W_FYRK3xGIQlcl8fAtuV5HooPIRQB3PU_vDYoqCCktmJG6-HAPeY6kGdcaitfTNKq49ut-ng8i3ldGKt5asoI32-67Fj1PJmvMFKxPhQrEjOkcTB9UCEYCmYfeScY0IEZf9h-vhCO2YoZgPBvtmXR8jQm0aRqTcqNvKC-RoW0zSHM1rZ1uGLQhfOme-qm5m__dgSGQbCAnIFszVYgQ9L42hHMJwc4-cdOAMDxV5hXpnkSZi4sNSN7WO9FJeBg2lwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید یاسین چوکو محافظ مسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92974" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-WdE1tF_Oac2hRGZcu8w7dIDERLCMZxs458V_pLGRWMnqmXI9wmc_fXbyFJrVfUhgq6Y5g1WV_x1H98izehKKASllmiCGuLTVuHNjmqoLAkCaVI2XZD9Oz73i28G8lE91uipKcg02Kbw-0BpdgGpaLHMAj-FZAraPYk_njh6XVzvnwil0wltcxA-VH6NIde0nBr9_HJEgrDFhpiwi040eOvDCY4DwXqYjhr0UIMVOVOST8gR6Vr0Y8DeGDW34E7xS8DoJhUnsbgAX59nn_TUl56d1lx7C4CuTNSwW-uyFCztNTvH2mVq2i35LxkhsKF1vz2zav6-DQws1A3vtGRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین تعداد فینالیست شدن تیم های ملی
🇳🇱
هلند ۳ بار فینال رفته ولی قهرمان نشده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92973" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er1NVNYXWbfO2Xglu1gnpH3OpHXKTnuF8-zhjkOLpmdA8PBDvHXSz0_x9wB9UCoGLOYk9Y3NxifebsToEhRUIalcUwDokivHUD6xH0_ud4NB7t1h1R85trVndvGKDanAaikot6LTFz6lrYIz5g0cp4VePNWtxqGo2-DtNnAudNUNodS67Gr1i2H8Kr7eYXj47ajwhhkrXpcZLsl72eV3Rr2ArI4n8RCzkCkEmtvAFaJxU5V9AHSkf9FBN_EL3qIL5XWqFoym1SEuxClfytRRykg_XktelGX8eTh8FQmczjyMEVmX3iamn-VmJk68WGG7XZTg-n-Z6Fy4_cjEWRODnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد پدرو پورو ستاره اسپانیایی با تاتنهام به مدت طولانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92971" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfrFIVgKY-hB5IlJwPFPhTKVhigOuDx-pw1iWXnBdZ1HIyuFpsK0_dq5ovpy9mv2-WqY04_qISnNW3ApEJvaDQrH6w7OlnSRBGnIiixqMNdMMIpYyfiU03U9OeH_aoKyz0QysSTRi6REpfG6Nt2w05nNmCG-0elGbd2rgswYn5g14dXNgON6GQ1h7045sXZ8w0v_wmOePgWfnJps4u0cPp2ob_8WKMcKKu0A1bopuDbZi9ztcfE7FwO0hTD99wYn2ZPydJKbE5WNhrL0eIYEBm1emQ6rUY57D64OWJhZh6dK05nJo6mfD_gu_YEKCMTD8xU9iJgiaHhSyNu0CEGL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92970" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpxKDoXvu3wBGGXSNVdcVK4Xs3vUJVA-HTU8XytNSnPEBokCSkZUV244EfzVZRPDfSFI8Jp7MmxJUQ1ouPQ_9L31TMSegnCEB-j9SGwE8GDbpRp15HSg9NWA_nYBL-BA4HRqdXv4_dqUQB1OqGq3SqviHMoYSxwi639hrn3q1BFOhVN38mUSs6jVihyEe9YLRIPh_QNrd7GMYJECzOqsLLXWbQJS9dtGD2YpU_T-Qn0Ymdhf12W5plGtl0Tl7WKcCPULOSh09nr3KIYrsySU1Tol2Danss9zvKVX9a3wEf39Z-v_Van3x8Ca5AwS1fNkVzTzS4AsXmf8647IyDNtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: نقل‌وانتقالات رئال‌مادرید هنوز ادامه داره. منتظر اخبار جذاب باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92969" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC3aUD4k-IFgs-LsnJ2qAw7Q84BB3jzSko-W0ZfJF-4bL5JgmLYjLzmecNRwx3QpM1hHxzerX-go1ayblsQKDzGG-gWTfM-Wx2YmqNi57USyCf2YHR6foeReyvqMsdzF8GQYOvafT-S8CHL0PqDLdOaPZY2ZttwTboIfwQrdHRhNb7pMJdTtlLka_BGs7BTqDf4bndgt0H68_8LIPRzLJBAn8NTh2WsG-xUPhPvnhM755ElteXLwPqftWUi66nLAeCuEFEq3vMnTR6PnVwVU1huAzqrpmtMgsYVs-VQkZf-UhFV50AUfWFzU4CIT186bnH3VV-1OGjOGNNAnQeKqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
سامی خدیرا دستیار ژوزه مورینیو در رئال مادرید خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92968" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92966">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnHAYLKs4HvuYGuIi7lP8yfPvzgr6wzIBGEFYKFSAPsjnJAbnd0b6DNkomfu43mJPG2mrja5BOHHLFHGYKpMybtup9wFNkGJUEI25SkS7Zcx0XBFpjWdrQIz2mh2Zu6RKpsQtQdnUfgrpnuwez_sy7C03waYIZsDoQZkW-DggBH0KCM-zLklh4zNGbx24rnPBJowDRYKNC_xLyXGDgvjESkhBNgxREwu8ALiTn8_WAZ7x8ktWsr1MSlBdw8s3S2Zoj_zHWGfK-Cwil2mIOKNDt7vCGwv3y8At6cTYcTCge2XjB0v0D9l0Z0w9WJKBLXQNCtmOr2h5w9GL5pS8YePOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeJwpwwxDVCGO59THVI5q2M1-u_u79i4PnU4dc42HLjhgxca2AbfNBHQvahCQOdsaqrPFHrSuSbSclVLx3t4cuf6j-7YMY85v2ETflktu8ujA6mLhqueZMuCLpvt5RuP7Il4FPkdgnwcHolE36JptFrvOe9PduWynkBZ9ltPrxmIs221reV-NhZsdyJXJnX3wX-t12strincFxFg1z9Ddl3HYhKYeLaq-gLQeXRMzECqfJ2UMhxc930U0zTRNkfrJLuAKM5GVSQI6Li-AVQ5OsOU0s4w22wHfOZ6GRs0p4t2aV4fFlKSf-aRXU2ApGGdwHKYnz1f3e-tlrxP67cUtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
حضور توماس مولر و شواین اشتایگر در ورزشگاه قبل از شروع بازی آلمان و کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92966" target="_blank">📅 20:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92965">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92965" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92964">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkLPYXVEtTEvpscL9kBXFSiruBfe4SXhHI2H6ybtzD-gNO_ZuN1LHOICCOZb1kkL3o70YW2cCwEYoggotD-elCt3RpS_Q7NqlxhrzjGcUDznh-eOciS2jr24outTMTYePIDJvsXmblBNAqJ0POUNt20x347xYOfAKj-maYO6rQt_HaKfQL4n-xg3SZGN8dsagXTOmgkkx3y1MCslgObCas0xy2N-OV-2swm-kUENZA_98twxL1aZ7-SaKBRuZcksB4zLx8zJA6zTxTGJUuaQOrgwdD8NqxI2dEQXuljC1_rMDdCl7U5gKQ4ZhEARuv_lxKJAM0nw0gBhA4bCfMHenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
رومانو: بعد حضور کوناته و داشتن رودیگر‌ و هویسن، رئال‌مادرید علاقه‌مند به کالافیوری نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92964" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUp_ughnUmQ6LXcfbe0sXH_viZbI6pSPh8BtrFn-xsMWI5_OiM6QPYQdU5190k1GHIU-oge6ifzdlUJbE1OCDD5rU2be5KKGht6UJxFYJL6UciUdfPx7BcimOnAuRC2MD04UfqyXrVjVpH8n4bwk0sRDzF0T9WIuCwz8KtWOAeQN8Lssf-l59UG_hwrfqoecloiyVMWmcxXO3wfn22Yt1SToK2qGj6SW-Z9rdDRNMSW2X4VqN7fNdWGnRHdVz8IXFJhqIIdJ0cGmdBsvm9BU0lxxMvzeKk0LbPGgR4vhbC_l3vufCNjZTT-6ktMlomNwBH2oYVRcjKLlY68qb-qhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام جهانی رو کامل و 4K ببین!
🏆
⚽️
خرید مستقیم اشتراک ESPN ، BEINsport و...
برای داشتن بهترین کیفیت و گزارشگر اصلی
🔥
با اکانت پی‌پل کایا
✅
✅
✅
میتونی با این اکانت چی داشته باشی
⁉️
🔹
اشتراک شبکه‌های ورزشی
🔹
اکانت‌های PRO اپ‌های مختلف
🔹
خرید از تمام سایت‌های خارجی
🔹
و هر پرداخت ارزی که فکرشو بکنی
چرا اکانت PayPal کایا
⁉️
چون این ویژگی‌ها رو داره:
💰
حساب بانکی متصل
💰
هویت شخصی
💰
متصل به ویزا کارت و مستر کارت
💰
ساخت کشورهای برتر
اطلاعات بیشتر و فعالسازی اکانت
👇🏻
🔥
doo.st/FIFApay
doo.st/FIFApay
doo.st/FIFApay</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92963" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92961">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=SW2p6-_pPiBkwLCwRMT_k33emEJhbsDXBlx7Qc2hvULCMN-hoC4nHrgKYdsWCpvN-6w8GBITCFrL2nj-1Gk8J2i9v8_F84SonvQIv7qv6FhKzHRAxJvumfxlsWhn0ScCocPKA-W_zgfh_2RTZVGBb1UfccJqeeQ7ekLGskv8QiKJ2u2xgLt_9lHlw1EUEPFtNYE4WF0RK5TSAwoSc16AB8_sgICIPtVDOIBDsrRxUl1KRe9NUI0-PkFLDQVcmI31eoJvq_2SkVAuBIgfcyNSJGv8JZKAMRDEt55hvBn5bdjQIAwO_XX-nWTf_BosXClBm34traXOYoeF4oOCbrYN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=SW2p6-_pPiBkwLCwRMT_k33emEJhbsDXBlx7Qc2hvULCMN-hoC4nHrgKYdsWCpvN-6w8GBITCFrL2nj-1Gk8J2i9v8_F84SonvQIv7qv6FhKzHRAxJvumfxlsWhn0ScCocPKA-W_zgfh_2RTZVGBb1UfccJqeeQ7ekLGskv8QiKJ2u2xgLt_9lHlw1EUEPFtNYE4WF0RK5TSAwoSc16AB8_sgICIPtVDOIBDsrRxUl1KRe9NUI0-PkFLDQVcmI31eoJvq_2SkVAuBIgfcyNSJGv8JZKAMRDEt55hvBn5bdjQIAwO_XX-nWTf_BosXClBm34traXOYoeF4oOCbrYN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92961" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdZoUf3hJfts_DcYjCRBQ9t25Lq7Ggyb1QZ9kgnWvMrd6vgGp3-nY_P1D3HDMBU2p0bFNsOK5bznJ00ygbSxQg_0KHFAOLxLMSAl_dxqhPNoaktMU_HxVvVJx924R2jZnvd10RJB-USM4gpr-w7rMZmoodEEvdwanWWh8jth3NKHp8kRF8j2dWP8RlPjYiR-X8OMkp7nIihfuxoHMHHKaCTe6W2Nls3S6nLM2yVs9r3-kqxVNiumksrLuNputNxY5czjSWzoDaOV6Zm1pCDOWUE086ENfXiBvGEiwDrTqQMkBt99AH5iRTwrtXL065w3N-mDzJ2wQS6Mw7NHbWAi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92959" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خریدای رئال بجا اینکه سر و صدا کنن کاملا کاربردی و متناسب با سبک نسبتا دفاعی مورینیو هست. پرز ظاهرا سر عقل اومده و نمیخواد پولاشو به کص گاو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92958" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پایان ست چهارم والیبال با برتری ایران
🇧🇪
بلژیک 2 | 17
🇮🇷
ایران 2 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92957" target="_blank">📅 19:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92956">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">كوناته ۲۷ ساله است. کوکوریا ۲۷ ساله است. دومفریس ۳۰ ساله است. سیلوا ۳۲ ساله است.
❌
خبری از جوانگرایی برای مورینیو نبود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92956" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92954" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92953" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz4lGtJgW715q6UzHAt736Gyh6T24o4mIrByZFpr4GWTOYAcd7tlztrAConaWzpLoZGa8lgo2jWdTDvU1Y8t6GvxHj5ZshQWhWUnflQLTZWf4flIqFH-ch8QH6WgoJe8byiMRWCghXBRIj99g9t3h-efi8hiGxcyKXzvVWpvdr2CLleLBzDfSusfNVZ5gIr2stFgj8KC525nFl1FF87Ath56WdvmWoHZjq6IEX4upN6ILpioZ8fR6gZ8BDwl_5P4I5_YatrfwlPBiesfiLPlCe9BSN9rUlUIZh2seoVkqoHGqO1gxRSFCQuouBiico5YRgPNGhZL0QxO_GPXcZqSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:
• ابراهیما کوناته.
• دینزل دومفریس.
• برناردو سیلوا.
• مارک کوکوریا.
پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92952" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92951" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSH5d0YUOlQv9wD4QbuVdR3iuUTqHrmIHuJ7C5bLNL9eeiU8rlxhIy7J3us1UIz0bR-VESnrtJAuOKGbrzxjEXk9hBd3pHbvOiNbPowPEhIsttdbz68gx7s3Xze1qoA6b0JNcPZ807NZn455-k4AlStR7HFfmqcnZKZ3VgobNseP4-wGGppG57QefBTzSfK8-stQb0N3Ry1W7Ziy5k04GVBCj9vHNh5uknmlABvY2iKK6piwRg0MWlZ92pNc8Yf0JP8HziJ49jlW4Oth4ualk6P-nreYk-nYvBMTZouw_HC-cFMR09HPnNCh5TBog654Uie0NZwCA66z6YjQHXYgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک کوکوریا، بازیکن جدید رئال مادرید، یکی از پرورش یافته های لاماسیا است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92950" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwO_IwCKzSQXY0ZM-bRQCgH2xy4u8FLsC3VJtDUdtWFgP2ko2amVTX4dLsmvcmrobZOQeb9T7Eh3BBnBAuqtYubk-LhHvosGWzQ76sWuzfEmAw9_VwEEJ59opgp99DVdnWcw3k5O4030F_wUyO3jpZ6zKQpAL5cmH1d9gtkfC9rBKwuaoN9vS6st5_myI7OfTUOmOjw3ewzO6pDxiTRiKk86jJ9zyZb-_oEEr1OBe314w6jbF43gDqCL5eH2ZAevqEpcd2B75y9aHxujjUqvFbxyB0R6fwxaK3t00xGXW8TZpEoDhXF6M1-HsGQ7OtS8FlR2lsQyDYqdLpvZixAGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92949" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIyTeXeOdKblMm3tEWxJxhx2QZs-iGu6lZ9B1pppLoLW39t0wto94fLT2F5jbRnRLyj3P8CVb10t4OK4-g0NsI8HHg5TrRZ511MYB-sIN06K4ilW4V8vSOqaA9URy_vKKVqUDIDDj_YzxiyJeg5tVBCRkyu3IFMs4QwbzGXvimFbg69stCY0UDNIae1DTZexHufhQxgtcbai-4vTN60Fftdz1YXX-mkL_ZzD9w8xp1ofXcaBe-6bUJ4d1vYzhsmbdO42EbIdH33uzYRHGKyx5L1PWaEgPL7H_g4uN9hOMFNbN7p5j0BtiZkSx8n9EY3T3RuuSV_-w9bX7V47kE5ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد آلمان:
بایرن مونیخ به دنبال تمدید قرارداد با مایکل اولیسه تا سال 2031 است. دستمزد اولیسه دو برابر خواهد شد و بالاترین دستمزد باشگاه خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92948" target="_blank">📅 19:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پایان ست سوم والیبال با برتری ایران
🇧🇪
بلژیک 2 | 23
🇮🇷
ایران 1 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92947" target="_blank">📅 19:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92946" target="_blank">📅 19:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92945" target="_blank">📅 19:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92944" target="_blank">📅 19:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-nxRGdutFVdY3P45nhwtxCcVRincjc-MU9pml8E09r7ZMs1axdTE_DQk_RK6ZnFCKSkuTILOi3uYlykjDUsJEYhjNk7x8OrNoeLvJautzHnS-PVv216ZVw0UQihsVL0e34vgCVlrDZCBGRpDTpIs9OxiHhAv40GgThvO99Yj0-aPiHL88b8EYacjTj1QUrW0qw2FpRvtD1gXv3e6DH-I1ACDSzA6yh-oqRGTtuuj1izj1329BZ6vPm-lhKz2FCA1D44ypvesb_XRnPb8f4hyn4-beh93G8IUxHhDvRHMet3at_e42w7KY3UVfyM2rGByZ4kux32hR6RexZqC9ZDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:
کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/92943" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJlp8B5yC7F_u0ljGUR0aJaUO1oJnXJ6hVphQ4I2er81ljBAp9n_HugOjNQUVuY9BMCG5TQastJqwgJneaywy0hp_ra4s5StW2I5sqliOlHiXwgEMCGjttbgLWXF_LRXOJ30VT6EeaD_aSvSVn-v114Ih65dbUzVDJ99Psj73zaBq1p0ITYOG4VrFEPJfz6W--cuX8RKOr0n6Fm0T123_wZXo4glXht2hVCt1JD8pIIPFftwXrBc3FTwBMgvrtNULXpzvNsLZ5YCW-mMIBDU35jF9Veq3WZ_HDvhLaOTHV2l0L5JU6Ix9cc17Hpb4MngbWEkZUMjatDT8Bz6gYjIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترکیب آلمان مقابل کوراسائو؛ ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92942" target="_blank">📅 19:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiNFbhjwNdURUM3tuP787R9jw0p3Uyqz39kN2RvYaLJ4OJayq5nlR34N59oWiHUnV_jOYpm-QcL40sYG5v162exVXcxjbskxHq_ptFDxzLypMmZwhJA3etx07MCjFvnvaGQLL-YphYqwyfOw0ZPb6y5KCsGwzghwM_ay9zSa-dC3uzjrojDCYEAceiwTuZa6KDbJjMTofUpNps-i9XjvmG_PTfOlzC5JWLHlUQcyq00CbMDejXioRr0BtoaKFrKoecXNST1DvF99LVDMOL9Ug_7AY8ZmUF8m7UFWsLTfb0A8rARJGju12ECjV4b-WA94285LMufdwh_Ttdde4pWttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترکیب آلمان مقابل کوراسائو؛ ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92941" target="_blank">📅 19:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان ست دوم والیبال
🇧🇪
بلژیک
2⃣
| 25
😐
🇮🇷
ایران
0⃣
| 22 این ست اختلاف ۳ امتیازی داشتیم و باختیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92940" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXOgGkGd_gc5tG5mCcSnjJLi8P0gBxzraKg0aWQRBsaEtDSTj7xNtfSAP60TRxrDW3UNnAZBPqbvzQJStdLajGLTT2lcj7QjAhISTe3AHU1yeQi0UQ5WHPatbd9HT3SJGMCkYGJ0DiBkSJdepD65pbXcHPMdTAlTgbTCyIAQIiIZK1-ca40ArcpFTwg2-7mN5gQkTZxxwsI2U-c7UTsCoGPXT-Uq00dAxvoyxQTApNJLi6pfu1TZClgFv_baf8pjfFaSENfRZ8vhf3V9B1BcQteSpzl6JjEZ0U4_RaNyh64GGPcl4GYniHmPK2EjSgux9SirjSW8NGfQr2RPeh0QDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تایمز:
باشگاه آرسنال مذاکرات خودش رو با ایوب بوعدی آغاز کرد! ارزش بوعدی قبل از جام جهانی ۵۰ میلیون یورو بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92938" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j96fDyk0T6KkFs8n4k41wbY7x8GzPTBzozmyEI-OaHM5DRdyjeiDyhqNx9WzlF9fYyRCKCBekbs1sGctylPV4-aCubMuqqD1n08LthBOup9MFJmr-I7YC6b7xorgAz7qgm-doyDJ3PoCy5GZiyzOl0ljZXNRCu-A49SdP70NS4tz2cF9rVuU61Wmxd-GdeOLXqogOkrqMximWBXCbGEKZIKLlaM-NGp__tsIqnnmG2GfPus641mIW4927oZPNmWXNO6mtciSTSsuz9JrrmZwBu4eiabE0FeOyPaJegnfH5Kfyd-4yaLoAEx6J93EDIdLGt0bCxoZq5tlzbDp9SzJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه‌های اسپانیایی مدعی شدن که مورینیو از عملکرد کارراس و گارسیا در دفاع چپ رئال‌مادرید رضایت نداره و ممکنه در صورت پیدا شدن گزینه مناسب، این بازیکنان رو در لیست فروش قرار بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92937" target="_blank">📅 18:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
به گفته منابع برزیلی، نیمار فردا به تمرینات گروهی برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92936" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc034209e5.mp4?token=Nrg5jEgjQRO7-QwzEMu3ZAFktBQ5tqWQ6cm6oIoUlevE3XSEESeW7GcxR-IBBoV_9kWZMabionuY9rVYoDGARH7txK2NhWftn8a9AmnCi-RETRfeuJLklRkl0QLDlW6i_8n99zlBvsfhrx_1YqnuhNt8lFvIF8Oc24u37gW3MXW6yFikjlpa2QlPEkuia4qVL2oWW9k_afeyrHmKLjadk_8EDcQy1qL79bbWXNA0YWEidwUNzIABUzkOD6spsbrUNl-ogrEkhyZKz3G1EI_yvGbEJHtkL4T4AaC94rp6Od8rMYkMWafy0ARMslj1Ek8JFa-gYvgGW_Bvk1R9o6P_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc034209e5.mp4?token=Nrg5jEgjQRO7-QwzEMu3ZAFktBQ5tqWQ6cm6oIoUlevE3XSEESeW7GcxR-IBBoV_9kWZMabionuY9rVYoDGARH7txK2NhWftn8a9AmnCi-RETRfeuJLklRkl0QLDlW6i_8n99zlBvsfhrx_1YqnuhNt8lFvIF8Oc24u37gW3MXW6yFikjlpa2QlPEkuia4qVL2oWW9k_afeyrHmKLjadk_8EDcQy1qL79bbWXNA0YWEidwUNzIABUzkOD6spsbrUNl-ogrEkhyZKz3G1EI_yvGbEJHtkL4T4AaC94rp6Od8rMYkMWafy0ARMslj1Ek8JFa-gYvgGW_Bvk1R9o6P_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ولی هواداران آمریکایی جام‌جهانی یچیز خاصین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92935" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پایان ست دوم والیبال
🇧🇪
بلژیک
2⃣
| 25
😐
🇮🇷
ایران
0⃣
| 22
این ست اختلاف ۳ امتیازی داشتیم و باختیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92933" target="_blank">📅 18:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQX3cJrRqeBXfxiTcceTEP5SmkNNtlhpFd64PxYxT9d0C3eedecPQDBLZ1y5pMZ_Ku--lHZgA6VVZrlOfh6R8mVtabf7t8PJfS5ACxfBAd0-pgi_DcQ-BzSJryxl3UPRmqFDkFakBgSmHdlLEKSL2Q7ZGEN8MliMyTNUwR32zwcn12yjOCmDO_5DJ6-M0A15BRFqntJU3Kj27-g9CO8ZppA9MWNLRFhJxzihgiTNuOHgsj4Vaic6yLlsWDPM4mQ6-xJ2P12Yn4IjR3XBj-uhnYek5ppX9c1tLoVd1yi-VhSyd0OPffPvd1ikmY4kigwDe9BS8A7EwF5LrKfCk06e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووورییی رومانو:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی مطمئن است که به زودی قرارداد یوشکو گوارديول را تمدید خواهد کرد.
🔵
قرارداد جدید تا ژوئن ۲۰۳۲ با حقوق بهبود یافته تمدید خواهد شد و باشگاه معتقد است که این قرارداد تقریباً نهایی شده و منتظر تأیید نهایی است.
🇪🇸
رئال مادرید هفته‌هاست تلاش‌های زیادی انجام می‌دهد، اما اکنون سیتی خوشبین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92932" target="_blank">📅 18:29 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
