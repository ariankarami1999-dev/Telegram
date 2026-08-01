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
<img src="https://cdn4.telesco.pe/file/uHaQaZ6FegJ4UqJdkTCjuG93Fw4Y4pcxErLMJ6NeWfY8UJ-ad9ZyyDitgsnfLpyepw4ZnlslBdrWLlFvCyLy7AuCHo2oGPV6rxTHL6dOy4Jsxr2f82FNVxpMxvGwZTLX0s31Ie68ZRzYeoQguSCCkv891MFUBaQ_H854a71S4zjO4nr589hs_QPsXg_EIyp3gZiL3XBSbWQ-yh7fW3V3FRkrd6GfqVESksoL8_v-whFqgQWzMHlm5sMGA-g6PPdW2xQdtB_NjSge9ypsYcgCXOYbSl3ktuzj4aOQg3A0q88ksblakYm75H0DZZFXHqCz02ny0Wf5-PC8qkcvpKlFGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-81612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پدرو سانچز، نخست وزیر اسپانیا رسما به گوه خوردن افتاده و خواستار یک جلسه اضطراری با کشور های اتحادیه اروپا در خصوص بحران به وجود اومده توسط مسلمون های غیر قانونی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/81612" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRtMW0RTg7t6M0TlB1xYT1Rp9WZ7779xbaww18GBuO1rm_89LUl8uUIsI6pQ3H2GFDiw2nclJt21ntLlHUmVo7Z8hNR0uSJ6dZFZeVmKVFrgSWwKXzEYFKYWpIzvg-zEuJpOziqICV7tXiSTL6oC8lybx70bel8vtrXbom5en5p0kW5Fpnk1EkG5fpRemZP-IC9WuNPlzT2eVUUBfhSn245mbooshkouOU2UdeWzbjWhoSafk0o0SxA7XQV9u40LTfoduOfuCyQynQN5hzR_lrwJkpgFE0gaqdMyTgfDhLSbkxuionRgjtKnk6nV3HHkPBBNGUqda2VyR-xSYek81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا به این بی ظرفیت چیزی نگید از این به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/81611" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امتحاناتون بالاخره تموم شد، چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/81610" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMHv5krfdYIpVoGFrF3bOWOMgcWLtJJl6Dqxxl9rPope6XvGVF_W2To2tpKMRhSXNE2xFKHPdkm35z6xnbOD-iwib2AH4sVSTFGTOUxHx87w5_AKasdjQP48qAjjOOZFkzgFCl5cZ9pVZdT7QOjGaeRFL9sSJG3ASS1yTukBTx3Y9-2RxBaZaq0K_-DH6aOn0VhTXCVCCi5ymckyrWU3xnovyPBGbjATtIPGDdRnlwFcmibtcW5MWgwNdnwkuqiu2ioABzq1dFRSkaW7fgRQDlvq8GhV6QERpHcS572TU1TM3oMnAh4KwLw_ehtVitEBooR28GP6ZTTAXJ8bQ6KoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaqIf7Dyj30arAerAvyGs6m5Z_CTccr-UPYJEaRw9_GuaMi4hnnIIOjqLZtyqjdKeTtSOmFr8jrGwaIOonaIAGdpbWDWTW_qKr0pCNQ26Y8zQHv1fVNTS1IALmOgoETDb78ZCOOZm3_wqPbW_KubWw1Amng0y1n5tBnwa8TyQjIrH7oWxbgnsQCh6laY_eoIvfrSn9rg9PvznJIUZvyqityT5QaUjZ8eJTMmArLudXCcWmPV3NFYJBw3AWhag99PfxLjMZRgnMF1KcxD6yJWxym8Ao-IU50EWAiDb77y8WCsB2xYDj3GXEBNn3gvUlhINeUnJvtzZl-6m-XMyGRQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYDeG2BzxZhVwn1CUMv0CoxF6G8CISXngKoBSBts0u-OPpljzai0svxUMstADkzQJoa4vApcJTqINyHWAqm4kSRR7NJII7dEEP6zLJlqAdK3b3W8FZZOS5d7YprIEJqcf0dC5exOji2p8YUuv0yRAAb5xtKIAclxxUcVhBQ0Pkm4Si_A5DBQDdmnCJVK3zNKxZEM7A1D8yBgdoDgphFC01z1wSkbJA4brITbhEQ8_nfTOl9IcickVPk92YknP3so7vfTGfASjSC6iLUHygdo9w4K9BBwAMPy8A_r1IPBA_vDw0Fr-pkypZ2aiRE_fhHNcccroX5Wz4oUyA7_CgZkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqLIBSXWqPFZfEpAMHwclqhDCU4OElymf2dKZb5fn9T1015CmqWOl5M8pnYdXvuDWHZu7jKUdoeJlGmfgqWCuSZmDzMK2km-OtfZIguQDOk_IWiM7ihpZZoe4-mh1FVl9WRJROBPEmwQUjmYtIZTo807yqADt0TU90rL47a1UyUCEveKi68FMnvRD6bedEjGnVWBv4eZiPtqT1nxEZIuoeGyWWYEWgAF2H25BQCleIW8HiYlA3jYw89xeN73srGjXrp3AgPu3_cyftkNRNB8EA7t1KpBWkFJ761a7qtJZK7DoYTYMFm1LWeSsa9vO_-oPREwvLkQPs9cLmjEzzBfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJbQHDCyBkHQA0zhWijrzP4B9eb63uns86j2QwRZP-OyqvsHejaUTuFfGIxW8WjQiJWlxoe6e0FuYb1rqLW2YDmz1OLaUXDfTbJx1pttEv1SXvPB6iEHvNPBsU0XHVTusM-TSKT01mZA1aCqb5Zky2_ws0DGn8XaVWH7OHW3EC84kCONGg8f4RMAUCxMbFkzW8xSg9pQQ7sNRAARMmwoZpPa41PMNbffUVsD59jlWIiasmfkDsCQ78bW7xOLrfTfoH0MqpHvNDf-ckVyDEX8zRvnTcI04VqJ_WxzoB9VxmFXOW8ln7DMg-E1sXZ9dM371n5N-9o_lO-NN_moubkf9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDo3UZij0scf1HImCEKsLwImV-AkiS5Ec2UWWD3EIlRPdzZM3-ncqsXRuNejtO5Q8kCDI4bLNX9pKb5XQgpKy45lB-_ni-67fVBXrgfb0xV3JDEV-jdwkp-zWQfOSlb1AL0Y6xgxyHwWFpAfSpZdL90Tx5rzhsWoBAMEpdlk9eaduRMuKL5YCaryyeN8Sg97PY-Tzt5UEmbf5_UmnUBm0Nct40hSlKnsLQTTz97M_5Xnfr3JXFiXK2ag5TlNSWUneYq2Yb87hJfTT-bd_SYaJuuVimSq5g2AmMqOKjyt-ym3DPid7JIriR_fEb2yxdii4b-uEB5KfdOHX7uwC5D--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_tlIsRGZa8v_xcqeydZ8ThmXgPDW-t7ROB7goWNsoHBNFjbvZaUeIGBFFi_eZ8pBe5jvyCREsQgx1cfFjnp-q2prKZA9mskKyg1n65KRv_LliJxqYTw08hmgkHh1xs6m9YB3jEbOIZWWCVfjh47ifjgdi5IMC7q5Za13mSzwhYO6zpvKaKuchagrV5YFrmQDmU55FVrA5hXVR0thmj1IOx_UPK495TPsuC0jGNJ-MMvxZVR1l1ygK7j_ZgL24JkVeCujkev_IznCOdAb1EeO4cVCjr5INO9-5KFNAGoAqRATU7udF10_w00sfpmKFNCq9WCF5BqBd2hw5aOBwex9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrJ6QlXFpbXvGHEJ4IaDOsPbsPdTytcfA81VVCqivhOekrpFeora7MXW2xbl2SCPf2SJIwQ9GBvm-CaLVREfrzwcNFq_6JgerQxB_1gZia-LhJ-jTYfpJ9IoJrkL9ji5y2OWt-dXaIwlTbTPGjzTiL6EDnSta4TnGqedgq1Vod5eUcCkGcZy8jo9_b7zcwjVQV8X2wu9VJlxUMtkLmd8T-lrHDdGLzv4QNh_Tlk1TzCNCUuuhw2pKp_j9Kv_59KWaFWBhiINnu8nMm3pX0mwU6B4ILWj1BzMJOGHW1FLp2Pb6d1ZgNwXNoWfrX0dNbUuBq6MI2LsRlVtXqQ34sjGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2I9Y9PomhAVnMgc3nI5eJnddaTU6gizVanxzBufNtNOAe6_9lDQuncloUxkI7NSOwVmTIch_y2XHlh-BzZcfOnWXY7iZ-xFgtZWyfMLPslUqRVzdL5RYq_n2Ff8OGTu9ZEEMPq2XK_Ai5sW96INa6QJwKe-u1LA9YGb1wF0ONNms4DcpCyTANVkRKW3R2BCLzYsPQqKADesIksrO2-EcW3ndY_P0adSxD2SWXYP_TBP130m1cIOFSfVfcFc-LR6sAn_QfjNZasrQ7J1CLYEN6awY1oXMffeMTnmuvkjpVYHU16fwN1kfuyKIxOlu7AZtJfJOi0zcBatv8pjWHUhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGxl3y7opa5FLyxD9CY-cczLEmWN0Cv8PQW2XFIxGW-0r-0F8D3oABQWqXpvEcrLSvdsanBAxKde-7PpL0mnubmzXzS9_CgviBpcIKsLT5Rcae2oQBfUxUi91c0gmAZC3viDCYBGvqfHjb5tZZWAhKsjJvyt5MpAfpEayKbx_IRUqlXKroEy70EbRGMMBwTBUFEqDvArKTAd35J03cd5tTGuuEez6Re-e7TK0L51vP2hEpv9wqkB5_XdqR3Ph61EUDnlD9ltl0OWjakdGWwsASheVms_iPhcrlmgw5oUDJiFPS8VLHYOw7H9LHY_Nk8NvPA88J10-r_gqoGjRRaQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU5IkPSs4it6eFvDdLBX0AFfAqYymb2HWSuMFFwopXziPeqU03cB9Sd-442njgDl5myQNmp3bk0hIRgytLCq7k9nYadV-tcOTys1gIksPfIhisuuSGa6y4churHAKOMPt03i4JHkH-zy-yWtwhQcyHkywD2A2NiQ5b0ob8OTqOBQirzMq-mTGStP21zg4fAhfb2S7GImNB98jEp80jCTmhwGgCH75Bw_kLb-Jq8K-D042lNVJ3okIXQu89EG2vi28oUi1PSzVH9G4CKS75RSCVynVqCM3xcfM_TRJKtnW-5idYHAjMd8lYxi45GeL4AJhaeJkZo_-tUdBcJ1LkHfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDr-fP0bUB9YyTohQsBsuAZizvJNzT9-UU3cd_4oTOkH-mp4a_vPIXDoLBZswaqfuDGRO_q5_S48ulbkDFb6xwEiiWHKb8Ffvf5KZmbziwxvrObrXZWamdlw-DxzZM8Vzu_lcdIHpQW-ZOhTIjosjAdFIMC5RbPvIFNPxUqXuAqk2XX8mirk6jzbDxgYpLHz3WuCHmiYdUqhxK6UmRCR_9FPcw9UCOnWu8AffzcMMdr5wk5D0Oc8i2jizgMAR6j4WP8v-D7dfGbRPIFDr12xaJ_egCgquql2c2FL6J-K4MYDhf5ftHGa3BDdiSRW5gsaG5S7ya0F1wIjn7DCGuEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9IDSjEtvIWh6hOUU7rQcrhUxfkebYgYmJGcbI1tlXBHBJ_g3MkiJCOoN95Fd9-XKdYrDPaoMVv3CiXpiEODsMIo5XiwovcTMkRo9dfFf2ylewzJWb4JgG0ot8GNkMQ_M_iZZL5hne8_q2_wXqOdTmBBAb7sKlDOs8PNvRdrcNN0Kstv8Dq7Sd9S4nei05MwAPao735wi-DacwtV3AH0W5PqrSzIXi9XhOJ0qeH4hNc3g0yZUTa64j2nppOuNnUPbar8X6EBtnyrtG2lgBKHvocEBnvKyIshNhDliwbACAqtKU-hKkSds2IXBSjcxjHwpKdB3W3j3HrjfBmZ-PB1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjiqgZEcQ9IjfL_JvoATboLYi6Co1zHmbuAdAt6RBFbonBeYENv-ZoGazPzdcLGElTkNTpxbivXcdCG06Un2TMG-a93LqNCXZJhhTcHaaau5PY7343yuMXUvHqLhkJ8s5I611WVLwD4bomdKhNwbU2xOj2QMHiXr41v7SRahFNGBPRJO89UUP_Yyh57oTCUZVFgAeUd7C2h0qrh1RticIrFEyS0vbhWN5sTr3cPMnmyVC2P0BW-W9IqAoSx6t0Bl_n7BaN1F0mljAoHbXcl30NVfyyZiLAkRhCEs2cpSpd1vBMjV6nNr1tHD-SD5zI89zuRJxgP2tbc1uaSfFkw4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFUWObYEUHFWvNL0BQz3IzvBAWupgaHdKBCRXZP_gqwdol61FgUJCWAEnpwNozsJ1ngzhvObCFg2dl6n_7OH_ZV_vLAXA2JjyNM57NPy_uGRIzub7juvAu99SGVw3tR9oUcATjHdAjUDB6mnZqVZvwdc6YP5H9hPEmUjHDA6olWmdzECjpyTPTcqk4KzuNuOpfe4vpZGPyVKvNS46RhM2moG1iZ1wqKfEO4nw1um1k17S3h4rkEy4jGPFvDXyPel6aCMKj2vWuUrJ8BOH9SrjkhfPmrkn3Z0IPJpvUkip2s1I5bRC7F2j3yRVz8cy5NJ1AZ8xT7FRL5QQ1VxrVnCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvsmp8kDBD0I93RurBaukJP-ujodWR3LLl4IIXZJpuffZJU3bi8qU59RUsVjB6mwhf0dHm7Za5Ai4KyZ4H0sX-WIy6S2yN3ppV2gKMVdTcaJzYFYBb0QfpymG5t0NcVX-JpnEH_sM47yu6yW5B5DS1SEekSi6IvmY618RMEqQuEbhV03DfFLbPR4RqOiP0kccxaG4Y5iysqNHmTHjg4Pytyl3etBzSzG0jmeh08urUnBeBLGTWgJ9joPYwFDJh1ymocRXq0BRi5VSzC6YU3ewJhKS4ZXWwEVqzrYe6DXT330a007Lrz7I1rDgFBVo6LlKVU7a-z3GTKpGM1SDWEVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao4B4vB_SDqNGVshHEsqmJXdvapmKf_XPY65D1k8O_Msc1fqmPPsqNdSOuUVHtXqIY5jEH7AP24awiJJORZLj5jiHzjR7iCs3hpBhnCdojm2VI3j4redWGpzIQdMS1bsTY05uWM6e6npSeN9mYJg3NizyRo9VX0Yf_5Xgt-bsvtKiXnKSs1P7aqPhmK7DPHPuarhoNo_jIs94AJWPizDujjeWOtA9o7_1IcCHgUA4govbLjEiimpoytgYtAYN_FIzlXSBmtBrqCdAbvQm_s1g__dfEYJoDxG9oHVsvM0AwsJ2kwRV1anh2FtZeOcIKQnG7giAB1tE16oDxs7lidIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0gf0vbAxSD7pVj1q6MAdi_hXuolFvumqX52JQUCvIw37b0Ve_noFH5Az_38pEEmNngm6baIMpy9c97nXenlh2XI_ynMFqDjeHkn8tO38mqswfQB_hooSnBfLsZCDafuVcIK4MZUvYjed1CjQhA5HLowHVaD5g1TxHjD0jfaV83JIG3lGBSgo5HcNPeP8REb9fVoIiq_hKryB-0l3ht8jmTvnVFnh_s8LauX4NynOdCC2BVF_LPPe7NIZTZNjPfe_bOGZdDrb0W961J06kwiwYVhMmLhRHOhuo7tZ9TPc_SIOOzb08IHp9OJIjHmfAtQBejozKmcRXmYQdYxggVcGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtu6cFMLGPOVOOizdvJBofZDikZUU2XViDaWbg5fOGYUtVK760BEs3m15Gf25esuVfpWOD855DL0BZ-RUxXwtO-gt-eY3RdNq1m8ZmkEB7FODGdUfqo3ndLcKb1o2YvJfPsaY76yUkOedbksVmHXn4jmC7qMfTAh2dTblrHBFHG6gBakwe2MvuomfGBSDracO8eBVPpETG2E80gg3Ig9GBhKhvEY_yTiNLE_41q2AyjtEfarNDVARf_xUaB5S5V2-1WrqNZNX5pr7rcXURFaGwqUzdXF9KoXr-DQYgtkXEbFmhu7zyBw_-aKTRoRTG1phsWc9stqPfQBk0aLcimhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ocuGOyiJA2BvwPLLLXWPgJekTdBYa7bxkr3lhUj5H7pMRVJ_WDYGbibU5wZT25fAz7ny3XseC54_XXAJ-jmPqoAvTG9Ai_1PAjQbszvYtXRcT9poYSVXRznWKD003gFszoJN5bgUpiFoHC9ISRmfiRTUkzWoMPiyYunArgA_-E9DotPlNJmk-ltETgumm4GerZIAdCPpNyudSTiAMoNSODfRM5Guuj_KSynip14k8wu6AkC6cJ1F5TtX5cUbYrvo_tk-pCtp5sX8glKXMNS7NoDIacBJlDKHmqt4hR7bqpSXmpcuaX7VGeKxbcFBruW2-XoZyiJCCDdpnXH0nacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKTBi5RMn62LvGDKeY6ZhK3XVvS_9H9rQXaZubyf7KtNU9XjBAn3cOy2WRDVqxxybgxNKBt4vSiNrt0TBPz3ovX9PsPg5efZIrOY3uHsglZi82M6vHGYduEWb3SeOcT60sqPhF6YOOcuFxJEDZXtOQA9zQs__Vrd7lNj-ljJGzR81KUdSegiiPz0QqndugM7bmJ74V5OPSt1TS2mxdLGMKa6BA1CCrCZne2XW7c1skNRCmdCWmwQqlY7DGYBb5g4WDT_CMpYYxHICgKOtqpDgj5Os1xii8BAyX64VYaSb2yQDbIYfoLNxi8NMVEjZ_kLp67Eyn5-ygsyPEP1OI8dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWZDFOZV7Ao2jKbiIzKFDZUTYCfAFGb2-Awi6qbP53cNXb_1h__DC4QG3H331-1gYA9M64kzO4x-ZujGQ6xqrThSmN6cuxcpysCJDP79aiXasJqQA-7NoQrv41VCk_Gc6PKMAj1mFRLLnYmcuzKZtDV_X7ADW51eT3uBbXVIwsApCVnLBMQBxVKY-vrW8tVbM_SNl90uVX70NqhXMmixhtQce3PItQjASmEhx5cIrPZNzYU7-ABge5WxDrjKiMnMmeFsxIl_064HTh0LQC8B70fWYjKS6eoOXL0zm6gtosKDoyCIK0iBbJhH83sexjtpTOG6rvNXYzVJu93pqX0mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj4VYHo1A6Bs9-VPbW2uOi-nc4jz1u0u7p5Si7swZdzbrdfxSKWhN3rd5MklMNIZRKmSMTflRnmxMiJHN6GhVI4KdSiYK9paoRHSoP6vntGH62tnOvjFaMuKSmo_y2vEnlxZ8tCMdlOQhslArShiHKGosAx_P7UzBASziWSwqU9uaRER_RPn_lgwdDbhzkbT-e5bwWkwcflmwvx37HINIyQEpdRuvkV_dmEX37BRHYGh6gFiCOfKOyzxdclfUsmEunoOzoLryggjFxiSqcMMzqUwgHEwonxv9aJBhCmkRJTks9jiysBZW6Z73t3e20iB807tKMV59Yta9vlZDEQzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FejKB5hRDEpqPQb3hwy3Yy4Ol0Qz_B9wqmeeGwlAwZoK0HQ72EkrYsryg0o3MLOVehC7glEPnV6j4iKcbgvlFoYiFjKVXsukaC37Cqpi-uIBXhEbZE0c2oPxEf0L816bvWzGwGN5H9LdZzg-IjVZVpHKgTDqx1mOGZeJAYYP_z9wnf4Zkd1O2HhORz7MJGce50lAlpl0In_X6YFhFvAwPWSuY_l0D3NQNaNd39BRdzhoPwSdOr7b6Vfjmi8OWcYpXqiaT9dknISi-pUEQtTAvuGRDCptiIluuj_S_qxwFrDkkCub9vXguU8hwMJccuLgzisovR3B0fgMnPppDhT0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbEGlqyCSK-eBefgqKXsXt4h4RF4jKjv52updaXCSEagSYYEmycynmSykoY4xPh6Hm9J-zKImZaC1kn8iGe4T2FaPb5QJiQ8iVpHQolINajsnUNn30QTgpjybg1nl2xkUYXPSoGBb-Nw3F1DzEtJgQklOZWWSM3eaYVG8uLAxeuGlUA7rAQiURKW6MG0myxQa1TSzKsZog_oES-zTwwUSCEn8MHkvTgMuqrvdF1B35D7pzpdScojxxx9ZGxJQWnFBQ6XujBBltiXgpzN2fMgkAwuAGWK3a0JhhaKeVfozpNJir61qY-s_ozumz_mcAUSbuNFB14uzQ6yOqYqM6qY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvTuze2-1YFuxDrlyUWy1BpaX2MYSJeUbRWnn4ZHq_T5fDZKjdbKw-jpmSjloU0IrMKQphhQS_dKcjCBFOsZsm8al9SKHr9KFbhdjTVU0lz9of8JijB6kLV60c4Z_HmsAcQGLeT5rGaJIkalxpCdasddygFx_zTGgMvPw_-ChCeIEAhkHUo9dhQaiL8g9X8ZBiNVtOEcfVnSQvK5Xr2ADet0b4SX_7SEWAbcKSe_auOUvajKj8mQWlqm_4clGCYl7E7XN8u62vtnoswpXEJNYVWNzMQzD9RUf-qgb99gqlFN1IAEV2cd3avzCgxeMcpEG0NU1GRv7xik2bI0uRQ1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sctq85JXrOhfCaa7vyLUl61GhGcgz4yVSmj420XeGkUyb9XrkIY7_oox6iVZdDnXDjCsAPNv6FfavBz_eaBbdD31Qt-9NMOVbbqw8QtmvTEezAP08tTQap7jZh7WjltRcB6I-JbUWkqkdxSobY90e9eD_2qfJDe78pXOWN9hIECru9jWeGvsRipI7raX7AQDlttnym9zhbpxoddhMoNRwv19EvtY4JJQ9T_irL9KXix1qwt9ceXdRUeTe54dexOpcU7U0_ax_DPTcBA33PB50BuRUep5aLmRuPEmurLhB2UCDS7eNaMpyVHpMGLmBFZLCWcPiiuEmaTm8RRc7QTiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYxRhAAti3mq7P7rImpr1gkhHtRlswNz95V5wvc9S-l3Yp5p2UHm-Gqy6UMtEMknS1U5x_a1_xVRyHlCMeJieNad55bbWS3PCF237OaUa7XRFuLK18TlaQXDyyI1Jyut1brC38A_jPFIyHUKPI9aRfowow37S2xE4clJFrJlzOzVwzT5ZqZ7E8T72DSX5v5uMhon8ljRuQbTIJ6qJRyyoC15w1XusEp0KoMBi_j50al0Ni02oIh906xxolwn4_ATFgptBzvztvDXbvdP8LcJuod7sQG_R25Rpnb9okTYnsuBfihrg8kEvZtRx_VuVqAfcFvNk5RbBQjb0nME1hTlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=E9LWB8Je1NpIINuBZ_oLYNg36jwjmxBFUhvjnPBSwHua_ohMTQ8rq_uJ1paWeFBVFpnO3RHjDqo5IR99plVGhc0bj2ui76E2-QE_tmYsM16Cv_0WZ1Tm30y1YmG6IyvZOw9Blqv4RLl7foz_kNp7L9DLDGxnW2zUEv-ZPg7Hvwq2CihlisEvyA5CVwL1BU9dA6SDXigluZnoFauD1PcWMCIsJbAA_KJiwAwPc0B9vUGDOwFHi7UA4gWnuCT2-e51Qbk7lNjEk0106TGpyYtklvn01cUtdsx8kLXTBvw7fBCpoB7gtjgGhu0X6i8YeF98opRdyT2TGfcpuqX5u8XedE9AAERUbUj0XcP8Wbgf-rG5Fgj3_WP5b7XlUkHJhyZnBeHX3aZBTgY7mpd3i7LuzE1lrdUdHXctMu1czzoFA1d-P24FV6_j-mxmOQjhFY8VQyuBNRO1SrbPC8y3SzupeRS7cNQJU9S2OqJA1SoiUcpueyPuqUdAVAhhlmEE82tnDYtPazzdnegcHk7J-KmE7rRFqtULqc3E5ulYma7ONjtyPZnOG5EKlGBOhGUjamm8cu6oOzrNY_lfOqQo6Z-JCAxxKRZ2EvN7UGDriTvEi9ZLHEycIVvDYBh80ebM7B_d6sQMOZpm_chokCbjD3xfqCF5RDRf6tmHjTpAAFHSfEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=E9LWB8Je1NpIINuBZ_oLYNg36jwjmxBFUhvjnPBSwHua_ohMTQ8rq_uJ1paWeFBVFpnO3RHjDqo5IR99plVGhc0bj2ui76E2-QE_tmYsM16Cv_0WZ1Tm30y1YmG6IyvZOw9Blqv4RLl7foz_kNp7L9DLDGxnW2zUEv-ZPg7Hvwq2CihlisEvyA5CVwL1BU9dA6SDXigluZnoFauD1PcWMCIsJbAA_KJiwAwPc0B9vUGDOwFHi7UA4gWnuCT2-e51Qbk7lNjEk0106TGpyYtklvn01cUtdsx8kLXTBvw7fBCpoB7gtjgGhu0X6i8YeF98opRdyT2TGfcpuqX5u8XedE9AAERUbUj0XcP8Wbgf-rG5Fgj3_WP5b7XlUkHJhyZnBeHX3aZBTgY7mpd3i7LuzE1lrdUdHXctMu1czzoFA1d-P24FV6_j-mxmOQjhFY8VQyuBNRO1SrbPC8y3SzupeRS7cNQJU9S2OqJA1SoiUcpueyPuqUdAVAhhlmEE82tnDYtPazzdnegcHk7J-KmE7rRFqtULqc3E5ulYma7ONjtyPZnOG5EKlGBOhGUjamm8cu6oOzrNY_lfOqQo6Z-JCAxxKRZ2EvN7UGDriTvEi9ZLHEycIVvDYBh80ebM7B_d6sQMOZpm_chokCbjD3xfqCF5RDRf6tmHjTpAAFHSfEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pfxD6gsqYFGo9_IVFrp10xD7oouFqQsfYn-sLgEjr4euOM5qTvCdurYgj-SWcRBkR1vERSoBlo-TGm1ASDM3TJIe8-Hj_BHmD9DJakAcaRA1cOS9Pi7I70cv3UWI1aYenpFnDxCA-cTslzd-B8XQNHmXOmpewUPEOgSq2v_eqq3uy8l4Ukzz2ArX2ygVZlk17hHO5db7Tm8O__FVb6MQB_NhcLm0UQoYKCk-BhZbA2YMFAwMVnEPwKZOHiXGcJ5sD2EYRGApLZ7kw9emPC2EH-ZzH2poSkTZvbjMxeSzvbYX3l0Hl2SwG0DYDY1R6kjYpBs0v1dgpDqVG77L9U0aRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDpBeS01CRXW2aMdOdGeAhLQnIXmQ-6-aP2xNGJgM8RPMOZ-xs01kYoB9K3P1MUyqmHlkuKMssudj7__aZkukDDqqpDviMGhhZGxppUAHxLH_64EFllTgKVey8cvzXXBFmz77X_5NqJYGfzyVJZRy68VS5LfO7as61Cv--UyzTRFOlZin9DkAVEKuxy6H0KNI8s5_iPZUBue_KANmDXRi8ALPDYu5PzlZfB1d5AUrC6QphkVCJTgpkkgD16TxQwIF4is7UpNWY7bRviD2BUD7st-xh920DZ3FulQ8ZkiBR1EpBXTJf-6OHxTrXXsW-tB_giIHnzzAjFLbn1fM8FIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5oOVCINNzjJ8G-uijtrPiCYatNRsYYKo8BO508VClqJNjee69H7Bl0zGG6P6jJy6TNB1n42CFJY-jzGyDPfYrNAD8N4pVUaEmZvZ5xPnofbWaGxQtqaIdXpbvYUcBdH5HD9sFfRiFEQAzkrhVj-Gd556eRy-9U_JoK0NE7NbPvZMbsM0URDJODtkwqEBWnrCgCP7Zy3UFyQWIwLhveeylwb2474j34CCcvA7lCi_BOHeHPf1BnE0lkD8jRar4UD0govoZ64_ATQKybj6t8TstHTv7ApaUiAl_0n3SGG4_1fvwgr7HeZIXYIapJx5_gOIS4AFX7LPiDBG3Z-vAIDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umJbrKqAmnZqKyyVBCoDjnDt0Mwma1vyL1xB1P4W5HJI5N-0hhw7novHd-IVJzD0rUaMb5uCuxg_a2j4R5C-h5B3_ZGNwG9ekIKK4up9PhgB8R-Kt_7qtIykjxx9MWw8hpksmkPCvrOT7wYyIlyqcsmf1k7EEsw2xa_lgA2niHsX8_hcA3cDOry5mDG-Mrc7H21wihBUWHNmNMVV-naIMgWLaPtkRt2fyp2IqpicVYbUYqaqcCwW6IlYsRzPLedWbBC2jEn3fsYhgYIQMlGweFtHgGrwlf1IOSPRUtI0ks2jq_59Djwi9ANkc8vKzXH0Gzk6Hil8bUhcS-5W2T_hcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhXU17QP-Ay39mpWndCTx2ucnWDjKxIu_3GVUoEtZzuuuiwHm9MSztcD9_DAhyaYaZrdO3mpv4Iv2Celvw4isg2x1m60YurLr_Jcp0UBOT7tBzqrnvur04LAVxPx9D2TgoCVfdFX7wtp1rMNQWKzcZ-d4D4wQxeD2Iv7Zso6LIOsbP9LnoqTGhc0w9bSKxGEqK45K6afsoZAoUNlgK5aDv3X83to5HDiu-wuoML49BWhvG46AL8n-RBBZabsGr1wJZbnpNcNDHGMcmyY0PMtXvVQJ6rJV0Ar_l7c44V7KJ8eQAHUHskrrtkrh2fi0pjfPu3gSk9iDGcAheaigMZVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUW9CMo9Ou-32cAf23K9flUJN49pHgjBb8zEiOGq8MoRGH75MWz0rwVetbOh5jzCIlKRBbGzS2hG90hM_kBMLa9tkaHCQ-2gREV9fN7zwRga420ACaH59P5nnKv9Ilh38fuJJW72LhCddkuJ7XfOAU_xC1JWMtzWkN1GGje0qs3fs-KEuTWIl_eFW_WxQzdNslBwpfmklCw1wZVXQguqUsIFWCov-GLfD82BklvBJjQ2rxTlRdsJf-qVLEaEi9KrebSt2XLEHMQh-M4JvZjcEUIPfC_f3z16Xt1ndoJ58LLqrpjmBF_oJm3yeM5cbZQdvu9mGB5hO2F6Am10HBnKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahuk8bipux-quU1D4gp6tweolOSM45VK-T2MO6gaJ_ZRX8spxK2NC2LFD3YTDkqCmlXqKXc-OqN_IKPHG5v_zsN6ChmjFoVMzbbdKjuBeWcYB9G-4x-1MQ0wtDSOXMBxNCwed4EOL2xDnRLFRSsRPlqfgKh0ZO_sMqlmfbpEudUMZfxfpBD6rpQcDzJPAmZnPRdriPCzjpkQ_tLpeDcMGRdxbmfckBDs1hDVWrufr9SgncMVZH6l_vOLJPqiiCChrpEdKrCv9lr_fmVDN9BCgfW_YBRcAvsdZg_mPd0bBR6O9zIgH07VVASe2WwlzYJ6cHX9u-5kvDB7MMYSzgJ4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8G0B0P6WoinTrK5r1dPTg_l3CXVwJN4H8RAT4h1wvDzzevhtiDJvbT2ltZ_AJx4qb7ipyfStnGCgLZ6u15Q_crx_NN8SDCayg7ygUZjVVAfQBnPok2aWmhD281o0hqyiVrEGdksxM94droXG2NF3DDsKY7dyghdujXINyOt7jqktg0lBDGyWP-VCOI37z2Qs39W08xtdvkonCEHacPKstuowsNJB6KXJULqZShb7_MT9cOeNs5WnngR_yYjKpyRXfLoHOCssHklvD-TADrceJVRtR769FWQ7Um4EXpH9aFi_MHG20pKNOzfWspOrd7K6uGxjfi4sEWbxGMJUubQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmkV2KXose4piuo8uno0LrF3NmClCeJEgaocnVPqtfNQSAtm9sNHbbaSlrZ_AE7lVGfCB_6kyesZWnQba4rkIeCrkPbLxcJx8nUP89njnPb0UnmCL-KELzdkWtwq5Kom2yUJ07CgHKvw_dkvVTaxnWCFyA_cOW4WqvK0Phx9X2bO6qGfhzWRvZ12ON4p-UEabY8cL2UvLnpUL9KJFSVESBibnakDCFw1BhCg9aXwKK5Axp0jCyBS1sfqvGf6jxrSW5oE-pAPOIgjfN7KJllKGeOg_zYZlR5e6hf4Lp1vVjcWt1DT_IGaH24pHGrYSblAy3fE9pgJiZkIZDXO2G7eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhFjw0g2oLs1pgT8dJ2PmdDC4uiOZj6AFCMd6NQ-1Sr8gvvz-SIWoob_7Jk-33j_IDj1AXMQn7wpi0uxSFJOkdxGN6I1TiJ7Laokens77hNmeZosg_mlY3bOlJ5fcHyREuzSVevT6WDrjOUAmy6UMOUUeI1gw7mpqD890zg2ep4mgHZg1bCvkeVgrXjLseWY8AhfaG67ZVfV0ux_HPKYBpYh5T5aEzw0-46X1NlxILJXuvcqhpZ2EC_kKqwrhNIBus3rc23FVw1CJEiaWYSrSR8btz14eu0uunj0AsdBgZ4XB2EENIPIyeUxeYmwomoVEBo8jIujLlG92WJl21ErDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH2cLmk6hRQhKBmZnv_PMRBSIKCKVO0KIjqpZseilIhM6sUU1W3YsXSlqDLwHnRylUIQoSPnY4V_ZzkQeswhtClDZr28lyAyd5ydXTFWt-j73_dbg3ffIZE7wm9OuXzAhhmbDH7NrL71fvE4l1MkpHlkbkZXV_PN7gjY-95D3UaSEysX6BAcjzzq7MUixGV23ct-55TPIZvYDwCSvDAaYdMPuRkZLDklP2YALaqYfVh-ZkLIVyRtfGkOB3VJvPTeAlC2vVbsMhKRlFbuOTU-_Y9hKoL8MyRSeGRCUEGwcZT6Xt0otAxrgH3JwPsC6z8Djdb6gncNHsYu24vnvFpNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6YpZQEt6fsyy_7e7akVgBZ3vksjJ5jXfKfnkgSv_tbQCxJjANktRIHAoF86rBCZ3bQ9TnMZXMuHR80MCW6mxmcDDFswGy9bhFgeq5uJo9tonmY5H3AxCttIzs0e-o-EPwC6kH7Hfyd3Ro77RkgTYFV6p2TGDJu-qAbbXGn__EJLCvDqiCBEerxhdHEf2jC0AXBvHSm_K5B29gxensefqV225UwDTPD9pIcK7t7uBTU1jwOPEll8qs4Upboas3XnXr3IcV0mPokqF7cwrHZaKZJQbZ1TSi-UAZ-BCgiQyk9556-Zjfnsl2_Z4CD4nSzqrfY8_2U_q4RJ9SlhST3cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW567rm8s6n4KsXx5rcf_1W6hSymuKPm0ltHHE-uTSQ5yDMbLAT0VQ1AerH1AVsxcsI4qc83Qd2MUdBoztkQJTY7NeCY0WMlAulkewlDZpi7avpyrHKWhSpGVIUgMYk7CGLnvC6nWiAFlVf4g0EgWAtYaS5_dqLnoYcPOzDNADJG1wchW7YMk2hiSXbkdHF0Uy7M9zUqXJ7BEGLmWst85kwJeIO58QSE1FMWcYu9v0sLRQd6pajT__BuGp7TPYH39tY2QbZNPM0GmrYReXFHriIrnD72gXAChmH32D1Nimqr-03VsaO4VaJVEIqKGeW9vGFOt75KIztihkhe4XGi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=Hz8LBH6XLrFYUlpIzgoGv9W7whckprsyMIWEXl4N0fWeS70Ks27QcjY-H8BSHSIUSNHoJT6BGBRzc15VfwOM9bQ6AowBvnB6UqHE9GDFisZo_rZRKZzuZzWrh1dM4o_DtkcEsYyczHIMWnRaImF5ZH9hEz-sQeIodeDbaoGrygBtQMqZh7mWRPFLsdwMyVMSgaG4lo9f5S17KPiVIUd709YvxQmD95fftANfVFDqtXOtG1_3nP00Mjsp98dn3AasQkG5-uLb0IQp38x6NRJlXrNTbZB5AaaS34OHy6OMuDqcyOfn-W4BNY5mQRTF8aMwAzka1rbIZ0LMO4w1dBmoiiBDJrSGjx118dCJNd0sRxlKS7nGWJnIm_gK7INRfScGVQQib9gahyixsxgzs7gfdpHXMa5434lNvU84OjWO0TznlUdapK618b0-FppGTs_rEJnr35vAx1CPNg64vWQWhsZrf1k0h5hVnqnkEUyAnaLSlW8GANwUqc4kKSgac0ZTIePE9_T0I8xnKaJUpI09Ood-jq4PqT7ihyWUVpLDSMmIHF8vKLhbbtvk0DRfsQ5omByrj-y8GXExyrNcxNEDl3Ok8Kj7Skuzx508p4XutxYT7zw8nQDsfkhUbbHx0-cylbpw5pUF6QWUZEeCANiYX3fYrum3cPeA1ihowRb0fNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=Hz8LBH6XLrFYUlpIzgoGv9W7whckprsyMIWEXl4N0fWeS70Ks27QcjY-H8BSHSIUSNHoJT6BGBRzc15VfwOM9bQ6AowBvnB6UqHE9GDFisZo_rZRKZzuZzWrh1dM4o_DtkcEsYyczHIMWnRaImF5ZH9hEz-sQeIodeDbaoGrygBtQMqZh7mWRPFLsdwMyVMSgaG4lo9f5S17KPiVIUd709YvxQmD95fftANfVFDqtXOtG1_3nP00Mjsp98dn3AasQkG5-uLb0IQp38x6NRJlXrNTbZB5AaaS34OHy6OMuDqcyOfn-W4BNY5mQRTF8aMwAzka1rbIZ0LMO4w1dBmoiiBDJrSGjx118dCJNd0sRxlKS7nGWJnIm_gK7INRfScGVQQib9gahyixsxgzs7gfdpHXMa5434lNvU84OjWO0TznlUdapK618b0-FppGTs_rEJnr35vAx1CPNg64vWQWhsZrf1k0h5hVnqnkEUyAnaLSlW8GANwUqc4kKSgac0ZTIePE9_T0I8xnKaJUpI09Ood-jq4PqT7ihyWUVpLDSMmIHF8vKLhbbtvk0DRfsQ5omByrj-y8GXExyrNcxNEDl3Ok8Kj7Skuzx508p4XutxYT7zw8nQDsfkhUbbHx0-cylbpw5pUF6QWUZEeCANiYX3fYrum3cPeA1ihowRb0fNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib2rpZvmAcmtfOPXm0WRb2DaDR_eEWgSMunoqWxpmznxVPwFJuNQgrgCkJSMhz1tl-tikwdBRE2ayAjWMmotVmqrLxYweM2qNnyjnjVYpVAGIogAS9VxENkBwfJahki1NINZgSAIEw8Dg3jPshZ1EPVYGChmh2XDLN6ac7Yx5Y6J0suPb321L_7QEudHImKGLZl7iJ2lm2FFWwKTOoo0JbZ-ASifGGetDW6sQeQaEiIsCJMwyS4Fuzabwqf13-iRRaTgB-og9RbEso51_IM6uf6AXj2BYbXykV8_wyhzlcKnh0Pqtbtyk5SatGW0lzVNyeN_fI84i20wCYCnDX13cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3iRlIV6w5FAPX8rNNgsDvzPT-mMkxWrcTvjDdufsXqNOLVkDMhvGwDplrPd80EWpZ_Pu_RfUe0e0cp5OMsG_-3J93SegeYkw7ttDG0VSjNwLKVDv2zbvvs0Y6oe7OXFnlMtH160nIVh1bxj8tqyIKa4swpMfnPMAwh-TLruOyhN2dkQpIwy-GffQVkKtObt_u84q1oyHLnyTGw8tEFHpAfDEp8caluGSJ6T4RqS6rVY_sYzydVOCNnTVPg2DyWm_c8GGfa8dq1NlNqSMxBRWexasqBY32exXwSq6RWRspKcubd7Ltp0Xy3a36iHVwmmmRPp9SCmRrwvaafBdyWyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iFtJzQ_CBmA3KkqrshEsSdD5CcOgnZF3uII2yTxrFXBPOXUKCNwXCsFrVdLk7rqMvqlaXPYbiKeuY1BLWeugl9wILllER2C3TT4WvyxbMqKEGsNzSuLPoyT6WwFDHsF6KDOAtWRPattzsJHI6WngnvIcACZHvFTfsfhLDcDgfg2hX78mw4PFTP_jhW6zK7VaTAXAGUSqm1ODWOH1U7ZeieX474lkjuXGnFPgZceSZz0hBGrROs22n8U4ijkmtA_kijRCpBGOwh9FyV-1rzX5eFPGE4EIwjdmaIpnvGy8ClSHrTxV3-ngcOEd1OoXlpmIVZ_DP2uHeRolPIZC--SsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iFtJzQ_CBmA3KkqrshEsSdD5CcOgnZF3uII2yTxrFXBPOXUKCNwXCsFrVdLk7rqMvqlaXPYbiKeuY1BLWeugl9wILllER2C3TT4WvyxbMqKEGsNzSuLPoyT6WwFDHsF6KDOAtWRPattzsJHI6WngnvIcACZHvFTfsfhLDcDgfg2hX78mw4PFTP_jhW6zK7VaTAXAGUSqm1ODWOH1U7ZeieX474lkjuXGnFPgZceSZz0hBGrROs22n8U4ijkmtA_kijRCpBGOwh9FyV-1rzX5eFPGE4EIwjdmaIpnvGy8ClSHrTxV3-ngcOEd1OoXlpmIVZ_DP2uHeRolPIZC--SsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuIlvLiy2vPt6MTW-liBn6-w4bfjO94OcqSdcXLmB5T_fgIYA5PnJSCQB0i_3Jwfd-0TP_fLfYdF7en5-BD9c14tvMHqT7kFezXhU9glYHozdu6p4N4683Bb0YTdlE41VGvsUxGBo7bnwrattfo25JRKKrx2ZTw-LbX-vPcCaoq6B-UPgiMCRxyK8rxTwj4Vs4txtxzwHnlyJKmSef_wc1MGvSNFbCTdgbhZ-qWKPOHLTmXi9JYyFsX7Tn7Rs32iehturnvXDDUlu-VNXC3aF4E5ftRz_WyvWHESlUxwvhWlhQHoxX09q4OQuC0tpVelkDKONsdJX8qZNSOfZ2W7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvW6Vx-gjx-7M3tjpRG-eDESrB1psVDT0dJCeTlCdMaAMJAQf3AP3evs149wIX8x9Q5IBvN79g4ORQ9f-cPeRPySFVoH_lAEmowixG3p4g7ie7ZY3G1Bki_CJEkhaCJkHHXbENJ5_esRdpH9EvZ0akbsuxL_ioB3Bs8SmgNTKHilUJvSha-yHmk2LZlR39ToeTuoEsBj8AUsQQvmXoX1X_1Zc2AkP1kG-DLN2b7bp3lGVoBNw3I9A0LhZQRs8uVa9W_lVx5CLTcOt0BlVRNn7As5A3NCGhNcgbrHXZ6RvYk2DryrzzixdmMx7ySN188PteivTja6sJ67avlcSTjcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
