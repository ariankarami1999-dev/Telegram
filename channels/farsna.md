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
<img src="https://cdn4.telesco.pe/file/ZCqcQ8i2RsBMf_LxmISIrqVNjhLjOylK3ACjs2oJ6NwLXREV8uRAVpetpUeUtcsq3xRKBxGaWEmSH0S5hllGBrpc7AwCrjOXwaz5u7lH298YAD1cUhio4RDy-QBJgBzA3EjGxjiv4gfdtPA_5_RzpWVzXoG9rk1CV2oRKdEeR1VAYjCzTqTQok24eJYZjNIT6ihsGGvstlvSjysMTvzZmtKRYBBLuSuBCt5aKfC1m4d3DMnC-PgSaW58J313gvoXligjN2cbO5MjOE4h3iQ3ciavtLVZNhS1rYlzKWVOgtVXBH-mt7hLBCXy1oiTcsiViTjLQSdi8NmrH5tlBJuMDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 01:10:23</div>
<hr>

<div class="tg-post" id="msg-449263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0mwyZ1UrP6r3ypWBQgNzrUCB3Knpcw1FI592YtIhioIu5asu7ZFzgXw8p3pxOk_asfX3Q7Uz94uJ_MOzjfJhrS84-O5NnlO4FyTD6hUwwJFZzl3SjQV-18HIWwyFc6EEii9CEynJ53dxYhn2U80-Rcb802JSsXBPeG3AXkHP_emtEgYGvnMwUl90q5dze2dqjwW7AKohSab2eqHjtGLw5St7MBtaJ70QohMFHUtv-9xWbzrvf3b92K1_4nvJfScM7JMi4x7QGEgp-g7XZmQyhmUTwj94drlV9UCJom2h-6uUZYQEX7XzAsZgiv6HoxbVDQShI_aauNdqlBlgmeysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8lLq-VW9468kvTl1ZT18hifS2K1yBvhsYlAwZtB4Ranv5u8ourLa8evnaAGGY7SN57f3xG7er248u9YlxCtyw4sDiXzWBjXFXvFRb2_73eCpmrsDL2LGOqRNmtevNXzRlVNdbSTzgau5XNEGhecKvwglEywlu27Xu38-0mPNACDTfD3G75baKFWAEezRO6UU_vETvjA8kC2U167w3W5EBhhJfDbkVV2S_aTj2l1eNFrlJkPGwo6X3u1VNlEssL_jVut8asrJND1q_zLWNyIsHtK7cPWVtgYPrg6_ZWP5SKQOTmnJD82a8EroAEHAc2Wj1b93W2ByLnfKucl7I8NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLiTh8pbKl_ERhvr2z62VrVXo5hqtnU_XpBo0xjT-4hf9i_rox1UbkZ-mS-CnIPMaMwYB1C0G-BtSsirgdcX72pIgunEfcLAk5ZFRIRrhXtdhkBLqv_AefFCRlK4mJJAIVJ5-vnGDQdS11xLl-KScNNhhPwMgoguZUhtizqD7QNVxK-rXwBqrjH40K73ALma2LdMytXcZJqzHhAS9nmKP0pitNfVyh1_9YulfuQlbHxswQpYwqHG7VfkFnQnOZLk_EQMynom_nFdQPgNTAQjkNZPU5SYXnAieHDpLsNlw847iPds6-9XX6zbcxnnmsYyKYQTDX5CYmdc-pcegjy9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-aqBe1rgULii5CIVVDw5Y4LL9cTnfPheZiGHDbVSb4Nptk56CZpAMzLu_03Tblv2gp1UnDURZND2Vn-0iTfOwjMwBTwURgjaLujX8O0l5yITAF-AErWLg4PhgLdlO0h-NKokCEDVCucat3uBSU9RCuLXJuqcjx0ss7sgm72tgm6ikUNJciMBWVm2USPXUz5k8sdqPJjQPIc42J0IF1N3AHFpAKVhr_wVr6zU7RpdkPUCcYE384C4xkESHQn8yYMwqRm4jRmipRhFo1lraU5tHbpSPUeaiAinmm0g9KTaz62h12tk5sc2p6ASSzihcZRcVRF-lsa6qMQlSyhViP4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OW7arzMsVO5iA5ReUdYG8LFOCcgOygeIq2toDpC4KRHycNrJ4wrTeV7KnIwxN3cXYF-QTtQnN6ZUPCi5NSQGrYTkXpwebZrg-N5Tm-rhZ__9DRx3BvK_G6oqyCpp9h3r0C7oNvfrZDTrfRGCiq8GitjreeyxwgZzTsH2R8n_uQIDe0Uch1hSjngd1rCnW4vjqj-dO22Yja7IJ3sRkMWTdxgajt9PU9k3zICTYAQj9-neHOEUtQc9G52EqoEkhBTQfKP5R2mTYiHSmNsWR02G2r9b8OHik1MUN0sXrpVZ6aF0-qY7HTPUWjQdNqtiSUiTNdQ3RYoS62AaZWaQtMpU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMAyLBr9o1qXLArqPciozH2O7Rk73niff_EIpZRS7V4VVx4n0t7hCqMqWB9StKtPd45s-L6xgQKfmoDiDDV8r107z89gwOZiWL-OlPR3paOWB4cyQych2hR_ZSbAcgvNhaGsfzDdGflMxjG3nA0Veja4gfkRG4hyhu2NNDmpPBgQGs9cVJy0OauJ43KaAfbx19d-qvV4qpsYC4RLmXw5P2f2zVw5dFNqo3TDrnUK1iMgS58qsa1vxSsDvbuDAsaAl1X-2GqkjVsJEipY4YdXkZXdg6TSnWY0DSZ5fkP6tHWghKw1UZ41cGjmoX6MeyeeuRV0MPEqigFrKjKgBqN5qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 503 · <a href="https://t.me/farsna/449263" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-XNWwEjsSS5iP2ldpXAxjUODoRc1Nqe2pWR5bYu2H2ZM1PQfKELx1roD-tHOY35oGNZ0CNMAnWYacvwyjamwCupAYyyZej4OxOF1M8hNQDMzISXtM44JjGpwKRWG_zijwPXj_1H0_cTd3IpYl4G2U2E1OWOApnoNKm8RXrl6GzfyicoPC2jldSbdPMm7j2cULbGRLptTjSq-gjTKkqZu3gjCoJlaSsECSLWKhSkdPY2Tn3Z0liynAHBoJz_Ry9E-6aQ3GQsQivFMuQOcJNYuQqgiy9EmDp2aBK4QMGC02kq3Jc2L9sryPs_qMlE57jB4OGyoBDI3HX43-kujvmq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByQa4QXhXQrFjJHuJQk4BMe7_km7fYni7oAQMZGeouEN0EZI9gpf0t_frEKsoOSCq0En8lkJXlYidDKSoO5OewSaziv6uzHS-VcEtM5pneptrTnSjbM2UFkhSpDTG23i2oh8HBqkoFc7G9pQ8RisP417UwJSFE-kR6R_HIm5eUomd5eiRgNfBpLft97HX5m1-KIWKzYbg4M1uZskK70fSVthVpYj5HdSO8wMrHVvfxUKqUJdmqEyGbED4o87vtfYZKwUpRt9A3iEexrWKbGHlGSKuceX3QLKNLf9hrlSJnhTUMu6x7moLqaQVv-krzfn-U7qgMASBs44kX8Ao_Fuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrbCy145ap1V9i2DpB0648iJnfl8oq2ffZCeP4aVe_87u5DE8WjCObcOaK9Yp36V9akPhz8NeZSN4HugK7Qb6kJNU35r0mt_o8M0mmAj0yyBEUfzRN6n_s1shVelIAvX3upVCFUzNN841L2i2q3qDAPUin8wOYdS-2cjO9hWPvLjWZo3OWGtnxalvZBswugaj-7h9cA9U5AH931DsIeMeGmCr8iqkVmsu_vi6MrvPJnhOV7hwN0hRZFp3IQgPIyT3JmBhvD0Ma8Kf5xOlLFz1QjL7SNjgrn9l8cVAJZ8xcwDABfS5yg-nf_XE3E7239u9i5EAfyKgilsqOlBouJ-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnoOkp3SZ9_CFddSkuqfg_THgtkXAFbb4rtVZgnf8LjFfYPLLkuoeX97-5KWGxUqltFUj9ZgcuwhAOepM6a5Dz_7jzqJsBfO5pbpfUdFMSKZD7qJSSQLmKJTHLUdbDpDfvIj7j3ZneP_aNYWWYQJ_P6kbDDgsT5HYNVtXxU3ydIT1mPJA2YS00kxq3AC95BG8QGzHZ13CM1oA0wR0kKP-LUQ7qhGgivF1_UuVFVVuiBHdweJJQi1m7N_GB4QrGQt-Uvgb71mXTfX2vieKNXggX4e3J2pIskipweyrP7FqQfJYouJI7fgRXWQEufs2Az8YIsOhloZ7KvI-g6EHraNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnE31rto323xBslJ6rubyZa8hyjJYQK_-tfm7yx8LQEntgO_CpViAvs00gkEaPqHtp_zYf4MmlqEuM6PIbub4w_E0TjjBiTpc1UXc4MGpqB4iovDkUyuJHZTXEyK1RPiGQMwm4PHuhX3HWt_oo1Q5AxfQLGukE4xXCxrfT76EVES5TQSaJr2nrv2xRhIG2eXjPEwsYhaf8Jrog_skbxCDM6KEsRqxuzoGhq-lBywtplRL-MbIUnwuOsPZHJCq-obpGexOxjEOCEqBHE5MlDTG75iPNSA0fRXupnI7FDf4z5OfCeQefZSWXAqbS59mngo-k3zDS0qs3D7pcQEU-zpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T56bsCjd-9ztS4OQto0TYQSruucluDYPToT9mlT7VADOAcQH6s7fOe279NDKpqQ_U0qDbUd4qqcIlsIM_83jVcmuK_4-M6asMRXnnWDbNK1RtPF15SSivzmr-P-7nbAj22vtVV0A8vm_9nwrF69EytIP5GnjEKNc5oDfdl7PADipmtFOZ9SoHJZhgBDVL2pByKTH_lc-DUQp_rfTSFqRZcozgADuXNdd865iLTOHcp9FHgk3IIOIECBIjLlWETGtlVthjg4okJoha0In0a3_44XVLgQffaIHAarTYADj8V0tNUTDdJU0ofu206fR9QyU-TLyUlgsqLTaGUSZyRuV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkLnMe43lSTNkP_73dA8rtMvdO8gHIzg1pa_X4fSBmKKOaO1GK_LoH0w_C9cPet8STYCdmZEQiNpFbRQ4UGJ7vDyCbjLbSrgtP2FB458D4kT3d8Y3tWudjUomxjNQiQsIyasOoVdEWJtAZ-VkR4En83mZ2X4fxHOwIigCH2rZWYy-L7EsA6u0EVrNNeNV-Bxcmugd_H9EhIbqRIZQe5gYEHJzaVWBdlSxuB8QPpjU5wte6kgTdQwc22Y9p9srOyj0x2tRyPZl_z_jUVGmwQPFF_Um5wT4COGc7RtXBOXsgZ6GHDbsGoRsMnlyk9W7xI8M0MOVMpWGIXFgxg0IAGvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njNaRKu4qGCWYo9m8L7aerEhjQYK0w1B-UPF9nAVTJB15WpUmcWoiGoYMws-ejr3aZSji4-uYghVchXbv613-63ldt1GsLTVdr9fMT6fjG3zSKYQHuJhf0gQL9Dl9CTiV5jIctACIs24Chma_6p7JkM0GwNr6l90eEXe5yh9N16jFga9kO28ogxllpo5dcM8VKadS8qxkj2-_eZag6wcIKfw8-BDPdZhUz7z9sWOr7lMzL7DGm6uewz8IwLzT1cLu9ttQcPzGp40z3Hntpv0n6OPN9IW72FAYEIHMgUSN3H-P6rClYIf-nS193GqpvCkpDpfqb_eX59iaf8kDc43fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zgug-IqPaVv7npwwRWeo_juDiTzmZaZH8FQDavY1fyLAg1Y64gk1YgLMUNAJUls0w8vLzPK3bgWGD5IX6L_FjR8pKQ7eYCe3h3ZLAD4YjwswcHqfrfhZQfs1Kg7HqHCKOuBuAvPri7wHTpBUcK-VS6COMYV24QUhp7R_RZjjYluQa2vNcl56WbL5Mux_WWlDBNmHGHzU5DEUkgH8w0rR0mfncI-hAL25ScuGstL4gmqJMBcRNs47JiVlEyo-gKId0lNLJcr0iAoj5RYmmp_F8d0Ln-UaiRN3loZ2xF-3nruEgCiU4lvLLW0F2a0XH6BK4_-KJGGsmE9kID-KOsO7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep_wPTFX6fnEzbUhd0RO0pX2ndvbM4BEKcuAfROLYD2qYAcx5bDxcbJEkALAWt6ZZuaHiUCTYZrUFyo3fq5bWXXLsc2EeExjyqH9DNHzhLSsaEE0cyPiVQBakhrc5zkdjkdWErJV3ERHTsjcF4zmENGIY7rVG8rgLQOVAXd8VRIEhMQkvQusZsp2u89qL2IIzwiBnfFSxkioMTtYfnjdfw8rBEu2vPtwIb8BHAL7Cx5mxCKKO4_GtFlsYRPcHIABwK6HmoikEtm0gRGjfbfDW1rUwZhbqXodNAMTP6Qrxh7jrqdUofdHDYJmI_3YHcHSN0im_OHSGUiRSY7B9SwS6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/farsna/449253" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRa83Rq_yWCGFQDgBAayUi5ht8ghka2actDVSikU7KXwfaR1jx2-1_CBXS2mFklbX9G3B9ODcrWdAe9To-xgssZe24-OufM5JSvapBRAZIbo8oz4qY4XM3HWfg4dzX1gan0ZWnZX6XvJbgHfgN55dkfmrmVsMrmPqQH5ODnRV0RKUAq7UiBJg09zzDtopJM_ISIrmIrnqYzL0ScBMlw2-GCjjw1RR7WRLE71CpgxjokTGtSkHtQxHFI1afAnoZvs6DIe_4E5NuB5vOrHV99mJrMeF_HyEQa96bTew5QMf0vaKqPElZecuLZqvJMiRfSdVteJEUf2KsvF4IXP9M3-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ۶۹ سال؛ وداع آخر در کربلا
🔹
پیکر صدپاره و مطهرش در بین‌الحرمین طواف داده می‌شود؛ گویی ارباب بی‌کفن، خود به استقبالِ این سرباز کهنه‌کار خویش آمده است و ۶۹ سال فراق در چند لحظه طواف ذوب می‌شود و تاریخ به احترام این عروج، کلاه از سر برمی‌دارد.
📎
خاطرات شنیدنی سفر رهبر انقلاب به کربلا در ۶۹ سال پیش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/449252" target="_blank">📅 00:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvHUbjTm3KYlCVl2AEOQcecJ23q30yv6s6445OXxaBEvm1O2GQOhaju-XdSN0JYf9trpCwAkRbk5ToF7gho5OnOIu2xYX6R0PsIQJhzLiIWKSkgO3UqE2RwpTCJFM3CAl_OfJgdrjBDv5pLXcRsiEkmSqNXz3fzY0ubHauqJBxLJNjee6RZxSF71MgdnJeyMRvWqrUnh_dU_R36rp398NWztxIUl5JmRKajLFNa67VXQfpq6PjMltPbf5N0CJJAPPPU2pvR43s5VTYY8WQtZ4o4Onl34wz4k-FoYaX4jsQ1dvJEizoAejWRXlfjpJJcu8CdfD0XLG2Ene4V86X0Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد حضور حدود ۸ میلیون نفر در مراسم تشییع رهبر شهید انقلاب در مشهد
🔹
معاون استانداری خراسان رضوی: تخمین زده می‌شود بین ۷ الی ۸ میلیون نفر در مراسم تشییع پیکر رهبر شهید انقلاب در مشهد شرکت کرده باشند.
🔹
برای تأمین امنیت این مراسم، حدود ۶۰ هزار نفر از ارکان امنیتی و نیروهای مسلح در کشور مستقر شدند که از این میان، ۱۰ هزار نفر مستقیماً در مسیر تشییع و مابقی در گلوگاه‌ها، مسیرهای ورودی و مرزها حضور داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/449251" target="_blank">📅 00:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توله‌یوزهای هلیا پیش‌از موعد مستقل شده‌اند
🔹
براساس اطلاعات رسیده به فارس، ۲ یوزپلنگ گمشدهٔ «هلیا» همان دو توله‌ای هستند که خرداد امسال در ۲ نوبت توسط دوربین‌های پایش ثبت شده‌اند. ۲ توله‌یوز خانوادهٔ «هلیا» که چندین روز از مادر خود دور مانده بودند، «پیش‌از…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/449250" target="_blank">📅 00:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثم مطیعی به یاد حسینیه امام خمینی خواند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/449249" target="_blank">📅 23:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ23wlw9A6csmftqxHl_NVJ0H8N-e4oNmGrwYidak-qTxvxGnTyXrQBVZEPQczOBll0135CyfQ2fXm-sKUdKF_khEwcBaaNk2IFBROxysYfSCtETSaX0FCh4dFKOuNNgw3gkAX03mSuMWT8YJmvP9Ln1Ka3d_LYAT6sSqesxU_NNXv9tIWaCa9Sb8PY20wUSeqrw_nj_zo0hHwOCuJovM1SPLfygN5ekybC-9LRRfTsIVXgUZrRuE-z6J078oo08kHtXLK8o_n-mmZWZzAmvnRlJWmsMbj135eLmS7ynudpc1LEJER7o5OM3zYlhq5m7p9xHsrF3p2Kx07trS5YLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ کشوری رهبری به این لطافت نداشته
🔹
اگر امروز مقام مادری را برتر از هر شغل و منصبی می‌داند، به این دلیل است که رهبر انقلاب تعریف جامع و لطیفی از نقش‌زن در کانون خانواده داشتند؛ به مقوله زن همچون «هوای خانه» نگاه می‌کردند.
🔹
«نمونه ادبیات لطیف و نگاه جامع رهبر شهید نسبت به زن و خانواده را در هیچ کجای دنیا و هیچ رهبری پیدا نمی‌کنیم. ایشان فرمودند زن باید «عفیف، محجبه و درعین‌حال در متن فعالیت‌های اجتماعی» باشد.»
📎
نمونه‌ای از تاثیرات رهبر شهید در زندگی زنان ایرانی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449248" target="_blank">📅 23:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تروریست عامل شهادت یک پلیس در کرمانشاه دستگیر شد
🔹
رئیس دادگستری آذربایجان غربی: تروریست مسلحی که عامل شهادت سرهنگ محسن چهری از کارکنان فراجا در کرمانشاه بود در سردشت دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/449247" target="_blank">📅 23:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر شهید در موج ۱۳۳ بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/449246" target="_blank">📅 23:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqq06_v2RPaQcdUt89uL9UTOfpKAkfGszSWwDno58DeM2-SpHeLebpVs87QilgFaALl2T_dgA38yH3P2T82CzK4p-ZmJT_MvhfQTAvDg-MZXY4JaRWAtzowvvdj0Iuovt7B-oxfaEj88-fdCA18WAT0YKNKfHb7bHp9WRFx0herWXtpK73wodv-mLwCLMaT1JQc0HAPqJK-wLHv8A7ztTUwXIRDzarhWv9JMZ2gZpbIFihNMOcNqq28_vwnbq4o0e4sMLvttg1qvY3EIexmKE-YKzrt9s__yvt-Jv4VZIuRkbT8HPigBZ4OSCunjc0ynlUAPVomneLY_YL6O2zX_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
این نقطه شروع کار خون توست...
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449245" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPzSvM-OI1kDjQ724DuuxDyF10yRfV5PauYZTUqdrYN-l1Es1jngt1u_L252q25J0BFAmGXODlxd5_j2bk_VHvru0f1mqnnUobKBCFmsC2MSjKfFEJNnbPISrzU32_XDLeXLEZforzQL7XOl6jSYt7HjtDgKYeIvvH5pieeeKMWYHWe3EspRdZ2Axr2WeR81LsjV54lIf2LcmdnHZKsn-zA3Y6xVMVOT18S4GBNMnJpqeghOCxG5sqcQtQsnqyDhxRl5KUKRRWfiwVdGa2Rp1e1DIowu5O0dXNzMht5TXE99opqRECTep0s0Dth9x81nSkrJ4ChZmTi0rkhqeInFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KegMrw7tvw6F1PcgvB1VqMOJ3TWBINSY7I0NYcGKPcY0hH_tSV8paIwM9eJwiD5FQhPSaPTW482BQvPaHSpA99FvsCmN0npuC6b-6qNjz2PqEyZQXJxrltUw6tHwfagtNlxXqehe1dupaqOwqqYLAiKmJ9K6POFKK7ShcFH8BrLqjlaXhDrVKjRqBij8VRRNnARXDOtT_tGeGLAEiB1IVQm1ERNFez9XmYyol7udkj-rLfdrbm5VEeD6X8Qifcnj0so6ZhFBn6sEgMX7ps_EaPvObfxo0cHscM5S9Wg_48mm7uZLRl0kO5KSjnOz0h7gni2_13sCzLb18BBwWl6JCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم انگلیس و نروژ
⏰
ساعت: ۰۰:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/449243" target="_blank">📅 23:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449242">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f727df6f.mp4?token=PJ5RbfKdaZMZLclL-ER2VvviVnGDagmV8F0TwUSPt3FA672Olrt3jEXfdrsPxoqMpM-CJVc0CW0axquUKNT8uqSn4HKPoczZ5SrVSmxvy_ZQZoM8DoFDRC0fDmNuM4uDfd9z-y9BpoOpkzgDGon77jv78qHCF8j8l_ae6CqF6JnWMADVDKIBEr62WeLE8TFG-Rv8G5vVJwbfy4TxvE6A0We4P8IelvCMenHChhya8tRRNfw14ADtAOwWja9nsJ2g8RoSTpdpTylqKRG4vyr4sNJNeLfdBS6m9VHi5cj9b1aD499bvSE4N4_FDV2VkFkCLQriEN3DbthNRYeOaP6QXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f727df6f.mp4?token=PJ5RbfKdaZMZLclL-ER2VvviVnGDagmV8F0TwUSPt3FA672Olrt3jEXfdrsPxoqMpM-CJVc0CW0axquUKNT8uqSn4HKPoczZ5SrVSmxvy_ZQZoM8DoFDRC0fDmNuM4uDfd9z-y9BpoOpkzgDGon77jv78qHCF8j8l_ae6CqF6JnWMADVDKIBEr62WeLE8TFG-Rv8G5vVJwbfy4TxvE6A0We4P8IelvCMenHChhya8tRRNfw14ADtAOwWja9nsJ2g8RoSTpdpTylqKRG4vyr4sNJNeLfdBS6m9VHi5cj9b1aD499bvSE4N4_FDV2VkFkCLQriEN3DbthNRYeOaP6QXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک روس مصدوم شد و به اسنایدر آمریکایی باخت
🔹
در مهم‌ترین مسابقه از مسابقات کشتی آزاد آمریکا (RAF)، در وزن ۹۷ کیلوگرم کایل اسنایدر آمریکایی موفق شد عبدالرشید سعدالله‌یف روس، قهرمان جهان و المپیک را شکست دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/449242" target="_blank">📅 23:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98dfa7bc47.mp4?token=foNYoAw_rjt_aOKH93i7UYzCIinSuw8c6kf5Emtim44FoH9l5-aymeERByRjl-ut7NfTgXUo5meBwQXp_ThVBgWmQWhAam_-HRcVSQuuMW4dM5f1BKHPH759ZJBzDLSxBz1LEBVT5qbdTUjvg2dFL_R4G1y0k783d9gPgHOb6Wbfhoxix9KUgejJ4lmpB52di9Yf-8bvo2R7Dn_e03hydD7dDr8p5OiJcfPigxkj88GXvm8q1isAtwqVBabdsmXkzL8H1hcdO_pMjDfceIpAYPpomVd1Tp3z0Y8SKDeo7CqhzA7DdIbskt_etV-ugs-h-MuZOP5iwgLqbKYd1omlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98dfa7bc47.mp4?token=foNYoAw_rjt_aOKH93i7UYzCIinSuw8c6kf5Emtim44FoH9l5-aymeERByRjl-ut7NfTgXUo5meBwQXp_ThVBgWmQWhAam_-HRcVSQuuMW4dM5f1BKHPH759ZJBzDLSxBz1LEBVT5qbdTUjvg2dFL_R4G1y0k783d9gPgHOb6Wbfhoxix9KUgejJ4lmpB52di9Yf-8bvo2R7Dn_e03hydD7dDr8p5OiJcfPigxkj88GXvm8q1isAtwqVBabdsmXkzL8H1hcdO_pMjDfceIpAYPpomVd1Tp3z0Y8SKDeo7CqhzA7DdIbskt_etV-ugs-h-MuZOP5iwgLqbKYd1omlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع عزاداران رهبر شهید در میدان بسیج زرند کرمان
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/449241" target="_blank">📅 22:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me-mW0idgd7nz7XTj3DRAZglAJHJf_Hoghg80PycoxSlEN0EwFmM8_YWrhhpTIsMM4A65o0haZi82QyNQVjPLWBbdpWqy3GU1ycG93J58fxnM4ExnOYL0-lCA05h3DWtRBmL_2IDPCkDiEusTmigzuAAUtfNiQgnEdzA96DP996GHq4Gl9wA8rrqWY-NUfhELGwuOuOb2tw6AtpR5BZ92uoKXdlP9YizE56DfWqRKDfnorNoWadWFUogW2GeDl2InTmnsWurA4_AGwrCPt1FefB_rrF7vtPhL3FIyvFS_FVDQxnRQ1T60Sgrhiwet-jHK05OmaKEplfI6pyUYvyE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkMik7IUJHWsjX6xoaQYccHTn1KbCcYpI47klJoJpg_U9X-6ymdEsKkBK7p3dMuFg5ZKygs96-FMJBECddXx2akpQHdu7pawMLyMTCaCc-bMfULmbX411zHWPd4V1rl-1zyk0AUW0WH4l1pibaWnN3zM06rdWQ6mVH3KkkgAc5HWw0GELXUC5xLyG_av1TiPkdyu9j6k--OZ7_teGwJbQ5CJ3RWQ0hheMyIh0zANk03_UVnQ6hO3Nw-04u5kSKMgj3x-yPbVGR9xO5i3NW397O-r4WDBqojBNaNFGZFSmaLhdOAGYEUATzZy4W5mhPfpfG7GiFabxIiwgVEBUwTFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TowKjOlatvCxY8dwINviOXqDLpSJR-bBf-7QpALfvL2PdlDKuQ6Scrba-x82MMCrgYZ8IlfyomJa0dd8pg7AywqOTilQhiwb9PMXiCxRWOtBeSEa2M5B0B6pX3FYm3eM5ONsERkRYvPQlCpayCGihiYfDmUill0iTjGsBgjA1_Oz37FVtJzU7nbjHLn6T_dJ1QS23d1vO4gSaq0sM9ueV4db25-ZCuJ9x-6VlLzMK_0mrTHsQEI_Rx3NTIqh7-0MeAPOeHEGvPa62FKWHtxY64TFcRD-ISkbo9AnRxX81_xJB5aNDktH48iicXe-6Vj_xpWjbWkfS-1HfQLdcZzPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUUwzzt-gU5D3oIdl94IkdWizDV89PYFuHqPZO-l_KGr-DJCE4wpi6RxP9_F3EP6f0ngFJdtWmmcJ9MU_Zr0Ug-wvhJwZXMlcc9pSzUjY0l_shKLgTbfO46EC_CthBYI_UMG3yeGNe7h0ypdxt6_1DrED74NwWVZRAkidaZyON_-pZAwHfVeIuS_hAZ6HNE3HNbCkapN1wzI89nx91BxDEfaK6Q79-GFwcQZEkSi92XbEes-EergWN9XaQodSozzPai8BLSbkjqvJqWdMYEydbxrkv4neeHMkk-CIe7CrPJiiVgUcV2BmJ70B8BqRPmf1Qpu_nSDN2K3_wOxpmxy_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع مردم ایلام با یک مهندس شهید
🔹
مراسم تشییع پیکر شهید محسن نجاتی با حضور گسترده مردم و مسئولان در گلزار شهدای صالح ایلام برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449237" target="_blank">📅 22:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت فردا هم ادامه دارد
🔹
سپاه سیدالشهدا(ع) استان تهران: فردا برای دومین روز متوالی، عملیات انهدام مهمات عمل‌نکرده ناشی از تجاوز آمریکایی-صهیونیستی در شهرستان پاکدشت انجام خواهد شد.
🔹
​این عملیات فنی از ساعت ۹ صبح الی ۱۳ ظهر با حضور تیم تخصصی و با امنیت کامل اجرا می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449236" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a06b3177.mp4?token=pAM18ZIoDThoYroMyyJM4pgdFZx2KVusn3AcSL9boGvHKBHTFQrB2_7a4MlSHMbEiMZnPd8HIhZj-GKuFJ9nxNEPxAzMUM6mownpLkcwfjF971a6qxZP6O6SEVOYeyxY6vlvTf6H-_R1wxHoFnodRomC7hQTpmKh4tonNIaRs8n-1BF-g1ZfehzTCdeUca0OZuGmtNOySIc4AsdHp6ofZbZmSUDWLJd54xKqw70tI_9i5q26CTecjAVwMuKuZBqmfB1MQew2DJLEde1cPuliZJia-mdcX_0hrWliwLBh-Vd4Fi0ariwL1Ug8vW0I0N9UNWfIN9jrb8UmORvtf9XECjtYlYtj6x_WOzgs1FYf1nmBHXvem7IgZ0A1KT0U49_39cRMM-MxKmTj-aNRn1WGkdOiFJh6ml_k1dflD_HY6xJVLe8B_oJv1Mg5YuHPIeJZrCBc4Kq-6Kxp0FXVUM5nylWEdkTy58UxP5WDYiD3YQX919Mlx-Fd609OEmLlfWpkgv13sFisZ_bDpJn8Vk5fbHvvGiZ5Iw85PQS8QzUMzayeZJMq4fFnabUURIM9uL1dcr4L79COC9fHdc2BvziojYUOHil4de1vrDkrhsk5y1uzP-jAGOp4BLvf1p4rmLqS4z2CcX2vP0E3anLhWpybbTP5O0KC-eiQx2VgrhpvHBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a06b3177.mp4?token=pAM18ZIoDThoYroMyyJM4pgdFZx2KVusn3AcSL9boGvHKBHTFQrB2_7a4MlSHMbEiMZnPd8HIhZj-GKuFJ9nxNEPxAzMUM6mownpLkcwfjF971a6qxZP6O6SEVOYeyxY6vlvTf6H-_R1wxHoFnodRomC7hQTpmKh4tonNIaRs8n-1BF-g1ZfehzTCdeUca0OZuGmtNOySIc4AsdHp6ofZbZmSUDWLJd54xKqw70tI_9i5q26CTecjAVwMuKuZBqmfB1MQew2DJLEde1cPuliZJia-mdcX_0hrWliwLBh-Vd4Fi0ariwL1Ug8vW0I0N9UNWfIN9jrb8UmORvtf9XECjtYlYtj6x_WOzgs1FYf1nmBHXvem7IgZ0A1KT0U49_39cRMM-MxKmTj-aNRn1WGkdOiFJh6ml_k1dflD_HY6xJVLe8B_oJv1Mg5YuHPIeJZrCBc4Kq-6Kxp0FXVUM5nylWEdkTy58UxP5WDYiD3YQX919Mlx-Fd609OEmLlfWpkgv13sFisZ_bDpJn8Vk5fbHvvGiZ5Iw85PQS8QzUMzayeZJMq4fFnabUURIM9uL1dcr4L79COC9fHdc2BvziojYUOHil4de1vrDkrhsk5y1uzP-jAGOp4BLvf1p4rmLqS4z2CcX2vP0E3anLhWpybbTP5O0KC-eiQx2VgrhpvHBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضرغامی: حتما باید اگر کسی نقدی به مسئولان در جریان مذاکرات دارد باید بیان کند و اصل امربه‌معروف هم دربارۀ اصحاب قدرت است
🔹
البته باید مواظب بود این نقدها به تخریب تبدیل نشود زیرا اختلاف‌افکنی با سخنان رهبر انقلاب مطابقت ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449235" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXxvox719J_O9bCcUymO9pYYdil9eitb0pJJcbk--oIv9xiFPjOaUw71B93-LRxCD2NKHcNXNlVO3_V-F-JwFjZgDnxSxMIknMbwy54XmzEwYYiYEN_zII6WkPnoBws8FXOMOp4uHPp7Nn9QGvvDVOf2o592uA4lkky1sFrxs9xnIWvOqo6SalUgdoJnKpkBQbALERj4xaKTGoBXRQ9OpKejmGUVxLaUs73VWFnG-7WhpwIo_Sm98TdDp9o2eA8V1c-AdgBgvEzcAxoZXILcY9wuQicfn3_nxTlH5grrPPDH0X192Rz5iNSYUTCPD7e1AibUUUrogc97akbHwc5VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل قطعی برق در چند نقطۀ کشور چه بود
🔹
هم‌زمان با افزایش قابل‌توجه دمای هوا، چند واحد نیروگاهی کشور به‌دلیل نقص فنی به‌صورت اضطراری از مدار خارج شدند و حدود هزار مگاوات از ظرفیت تولید برق کشور کاهش یافت.
🔹
خرابی ترانس در یکی از واحدهای نیروگاه تبریز و خم‌شدن روتور در یکی از واحدهای نیروگاه قشم از جمله دلایل خروج این واحدها از مدار بوده است.
🔹
رجبی مشهدی، معاون وزارت نیرو با اشاره به افزایش فشار بر شبکۀ برق به‌دلیل گرمای شدید و خروج اضطراری نیروگاه‌ها، از مردم خواست برای حفظ پایداری تأمین برق، در مصرف برق صرفه‌جویی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449234" target="_blank">📅 22:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2b14ee02.mp4?token=bYdKsC6-5flqkIsOTQOUZskYaA7XeowLXqecbxJW2_F_JnHu8q1hawPMzN24gHnlrF10i_MpKn6qSanvygsu1siHnqtW9_Ctr8vxqOp9-h09i0ou5iIfbL4mE37-ibvkiOjQp1dREhLaA124Mpy5KN_TE33CNu1pTGFYTi0Ksl03nk2568c63kHevAU6SrQAmYxlQogNRLGoNQmetMy5G7tuucMPsd_9fuFLr0IkmNsgHN1em25wP0vRaxy41BftPuFyIXFwxG5tIiDQr-LMNdH18_q_Y4UVsBWzbiBgipBBKBwUACUG811lYoGu7QnPpeFSc0oZE0K6Fg9QwT3sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2b14ee02.mp4?token=bYdKsC6-5flqkIsOTQOUZskYaA7XeowLXqecbxJW2_F_JnHu8q1hawPMzN24gHnlrF10i_MpKn6qSanvygsu1siHnqtW9_Ctr8vxqOp9-h09i0ou5iIfbL4mE37-ibvkiOjQp1dREhLaA124Mpy5KN_TE33CNu1pTGFYTi0Ksl03nk2568c63kHevAU6SrQAmYxlQogNRLGoNQmetMy5G7tuucMPsd_9fuFLr0IkmNsgHN1em25wP0vRaxy41BftPuFyIXFwxG5tIiDQr-LMNdH18_q_Y4UVsBWzbiBgipBBKBwUACUG811lYoGu7QnPpeFSc0oZE0K6Fg9QwT3sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۳۳ شب پایداری مردم شهرستان کوار استان فارس
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/449233" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔹
خبرگزاری عمان: عمان و ایران در مسقط گفتگوهایی را درباره تردد دریایی در تنگه هرمز برگزار کردند تا از ایمنی و آزادی این مسیر آبی اطمینان حاصل شود.
🔹
عمان و ایران توافق کردند که گفتگوهای فنی و سیاسی را برای رسیدن به توافقاتی مطابق با قوانین بین‌المللی، ادامه دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/449232" target="_blank">📅 22:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc69f6bc7.mp4?token=jd-Ojc4VFqVgF1q-CnjdbY_uLqirADgaFwTn-q6R1JFx7KuKtq8cFAPS35hfmVoP5KVSYr_I1eqEorNL2n1KcUPa_2kU-XP_clvaFj1RI2HogSXaqKnqQUEOi-QNY4mn9oNvKxRR0jVrB8LvmGuY8og5sGTGa4zNE8o3YLHz-ouEb3ImjpPwjWKIKs1Y0UXF7MTmLJzkYr5Ro9QTKw8EK5C78k6POUu4YIrmfRGj9hsqUxvG6765iOvsnxEV-ElHqbh5TWfWUDB3kuio37hxK8JjUfx1N8K574-aqvUzc_zswNrxdeuCK1T48zUBHkeuQCF35Xc3w_uPb1Tt2WjXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc69f6bc7.mp4?token=jd-Ojc4VFqVgF1q-CnjdbY_uLqirADgaFwTn-q6R1JFx7KuKtq8cFAPS35hfmVoP5KVSYr_I1eqEorNL2n1KcUPa_2kU-XP_clvaFj1RI2HogSXaqKnqQUEOi-QNY4mn9oNvKxRR0jVrB8LvmGuY8og5sGTGa4zNE8o3YLHz-ouEb3ImjpPwjWKIKs1Y0UXF7MTmLJzkYr5Ro9QTKw8EK5C78k6POUu4YIrmfRGj9hsqUxvG6765iOvsnxEV-ElHqbh5TWfWUDB3kuio37hxK8JjUfx1N8K574-aqvUzc_zswNrxdeuCK1T48zUBHkeuQCF35Xc3w_uPb1Tt2WjXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اختلال بانکی کِی تمام می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449231" target="_blank">📅 22:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da132def03.mp4?token=QQ3PNE2jkS754A-lpI1oxyRNSesbcKz76S8iL0rFxwqs8UjtVyeK6Hx_SibyFZWfZ1k7SYNo6z204moseVP1gPwjYtiTpZvxl7AWOh1b9BmdHTXzZKbr2y7UcE5i1jMugTsNuiaqmriQuWB27MUBoMltwmFkPOzMorwOP6nLvDAiSyS22BIxeCk4Q7OR-Q_2JYspggPV_7iS7Mqf1nOoJpOajEtxKOMjbc48p-Py2ElTSVH2yvxZhyjWWYHOjf9dqYhJVERdo0QAVf3BqJPjEbxEllYOAgCxiVV6WYwIWNmGtIVRuQBQnN6TiOmUX6GmBKmWdaqAHVyMfaybhsRtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da132def03.mp4?token=QQ3PNE2jkS754A-lpI1oxyRNSesbcKz76S8iL0rFxwqs8UjtVyeK6Hx_SibyFZWfZ1k7SYNo6z204moseVP1gPwjYtiTpZvxl7AWOh1b9BmdHTXzZKbr2y7UcE5i1jMugTsNuiaqmriQuWB27MUBoMltwmFkPOzMorwOP6nLvDAiSyS22BIxeCk4Q7OR-Q_2JYspggPV_7iS7Mqf1nOoJpOajEtxKOMjbc48p-Py2ElTSVH2yvxZhyjWWYHOjf9dqYhJVERdo0QAVf3BqJPjEbxEllYOAgCxiVV6WYwIWNmGtIVRuQBQnN6TiOmUX6GmBKmWdaqAHVyMfaybhsRtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیپم متفاوت است اما رهبرم را با تمام وجود دوست داشتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449230" target="_blank">📅 22:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640feee9bc.mp4?token=Aw52k8gaNMnl4DN9s-9opypaQEnqExqafgDNouA553aV2FnJKOdAhTfDhFKnc9jga9W-mxz6_DD_ax1qTnTJncEuY03GQFXGyFPi2nzVjm912Fj7pNka65w3KHgF1mLa-MAVhVxOT6Jjzl9TqRebPSm-cr-5WefHA7QZwnVDk19lGWvpKp9GiOmYJYEKFrXLlMNB3YxSf9YA7z1fSNHTOsQxWOzFZQiUKDayOoKY2EhZndwCCaQlyc4pZ2UYItNJD1O4p2zAhIAjntpEb3NVovMxTNEJhc6t0ivkQNMsytRhvzsr0eNK0IT-miu3uzNq61BdUnCDICCn85Rv44pjCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640feee9bc.mp4?token=Aw52k8gaNMnl4DN9s-9opypaQEnqExqafgDNouA553aV2FnJKOdAhTfDhFKnc9jga9W-mxz6_DD_ax1qTnTJncEuY03GQFXGyFPi2nzVjm912Fj7pNka65w3KHgF1mLa-MAVhVxOT6Jjzl9TqRebPSm-cr-5WefHA7QZwnVDk19lGWvpKp9GiOmYJYEKFrXLlMNB3YxSf9YA7z1fSNHTOsQxWOzFZQiUKDayOoKY2EhZndwCCaQlyc4pZ2UYItNJD1O4p2zAhIAjntpEb3NVovMxTNEJhc6t0ivkQNMsytRhvzsr0eNK0IT-miu3uzNq61BdUnCDICCn85Rv44pjCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولاک نوجوان گیلانی با تقلید از مداحی معروف حسین ستوده دربارۀ ایران در برنامه محفل ستاره‌‎ها
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449229" target="_blank">📅 22:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7uvWf8iQPgsNDzPVdtszfkuPaHiWYCGaPAqe4SsczgR-qfbzlL5ifQ64XGrOfToGIhSBdTWCq884CTRpGu3R6Psk-4ZMAzbopFDLhJxgjsW34mQ76DlFER_lHT1A_1eW33bpATK7xpGvZj9QruK80FVgLZjtjuPDFX4d3g36PzNzLSzedQQ5wqa2ZLNYGj1qnoQXNZFcX8XdKS-tFwVittu31g4Fr8Zi_fjTcmCvEVpzwM71MsIDuMKFaKq_XoFYRVczP-VlFAEfop2jR5CR2if7XgkOVAQtcWQZSOINp4tJmn1nYWM2A9tuFjkRz2tJipX50DwqbOQ1DrWgFaYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویکرد، فرآیند و دستاوردهای نظام شایسته گزینی؛
💥
گزارش جامع «نگاهی به فرآیند انتصابات در هلدینگ تاپیکو» منتشر شد
🔶
گزارش «نگاهی به فرآیند انتصابات در هلدینگ تاپیکو؛ رویکرد، فرآیند و دستاوردهای نظام شایسته‌گزینی» به بررسی طراحی و اجرای نظام جدید انتصابات مدیریتی در هلدینگ سرمایه‌گذاری نفت و گاز و پتروشیمی تأمین(تاپیکو) پرداخته است.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، این گزارش با هدف ارائه تصویری مستند از حرکت تاپیکو از انتصابات مبتنی بر تصمیمات موردی به سمت یک فرآیند نظام‌مند، شفاف و مبتنی بر شایستگی تدوین شده است.
🔶
هلدینگ تاپیکو به عنوان بزرگترین هلدینگ تخصصی شستا و یکی از بازیگران اصلی اقتصاد انرژی کشور، با مدیریت بیش از ۹۰ شرکت و بهره‌مندی از حدود ۱۶ هزار و ۵۰۰ نیروی انسانی متخصص، در زنجیره‌های مختلف نفت، گاز، پتروشیمی، پالایش، روانکار، لاستیک، قیر و صنایع سلولزی فعالیت دارد. این جایگاه راهبردی، ضرورت استقرار یک نظام حرفه‌ای و شفاف برای انتخاب مدیران را دوچندان کرده است.
🔹
برای دریافت متن کامل گزارش
اینجا
را کلیک کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449228" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sic8sdBv_pjVhmwUiu3ggMxdPK17M-7QNwCV2jpollZrVkmml1kf1ck_LQqJkjde1awn-ljqat58oYGWP3x2sxB7dwTiBmJ6L5Z0pwCtnrn1QFhyT-RVPNsWu4JDHEEuoH4eO-veJiQoZDyTluXnG4-IRdS8znkwk5lQlBxBY5f2FMzQ242fLTvWsaE--ZVQQOoCr1HRF40ql6EM5ox8hPJitkhjD9bOWJXt7kxLKgkSLiMQ0np2Pg8obbso438_W59-9OF9KARDylJdbEuPRmL3hK1NXjdULApLRqLPhIHoLdAU4yaxmYKofxAnHCMOAMIFyU9aG2lid5c1-jJFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#راهنمای_مشتریان
📲
آخرین وضعیت خدمات فعال بانک صادرات ایران
🔹
تلاش‌های شبانه‌روزی برای پایدار سازی سامانه ها و خدمات بانک برای رفع مشکلات اخیر ادامه دارد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/449227" target="_blank">📅 21:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/449226" target="_blank">📅 21:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1e380ff5.mp4?token=UXR6Keo0cziIuUohoeanuYk8-cYlajC1WcKykGtmiM9PpwqqmRPqY6DbIgysh_9yMyT3SPSBYQ_BvX-s98h0w5sUCFgUpKWBIYmKfBRLKsYQS47OL1XWX25NTc-iKDcH_LZC08sWLu8cDQ2vJ5KPGyvE0VJ71YK5Tyi8J2RdLNIoUJ9gAQRDENOiUrqK3uhuTc-F-2N1O6wAinEHvXRxMNadfXxL37J19KygWSY4D7yjz0ReCa6qkBdzKMaq1807VOCaH4iXdi8EP2H54TzX7JUPr-rZcOEQiB-SFH4ws31vl4_iOJ9u49If43ygAIK0nVfc2s-66OgPWysW6wQ71Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1e380ff5.mp4?token=UXR6Keo0cziIuUohoeanuYk8-cYlajC1WcKykGtmiM9PpwqqmRPqY6DbIgysh_9yMyT3SPSBYQ_BvX-s98h0w5sUCFgUpKWBIYmKfBRLKsYQS47OL1XWX25NTc-iKDcH_LZC08sWLu8cDQ2vJ5KPGyvE0VJ71YK5Tyi8J2RdLNIoUJ9gAQRDENOiUrqK3uhuTc-F-2N1O6wAinEHvXRxMNadfXxL37J19KygWSY4D7yjz0ReCa6qkBdzKMaq1807VOCaH4iXdi8EP2H54TzX7JUPr-rZcOEQiB-SFH4ws31vl4_iOJ9u49If43ygAIK0nVfc2s-66OgPWysW6wQ71Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد سرخ انتقام در تک‌تک خیابان‌های ایران فریاد می‌شود
🔹
شب ۱۳۳ تجمعات مردمی هم فرا رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/449225" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۰.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/449224" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۹.pdf</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/449224" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f1912163.mp4?token=vsPNcw9kbpSbcMQcn5eQoqt9Sd3iNEdIY5jeRqu1cHUy4vBeA0887Kr7gqXvXTysY1gEOuh3S3gZFW3_DdNid3BLEr0ZIHk76VsEHgMQvEI7JIYBVxK29gUi3eN8XVFa4-Ehfvq1VyfoBq8IGtL2pyVzqMUFIZGkvjlUqAYYqwAOUY8hFpItzuKwViQPSuh9m0ZcprAfrKJ76xOJ6EyXI7vo16r7fktZmA6Aq_GvM0XpBWvY8m746IOLGz4WWxBSmF2vXvqxGBHFRxINkCk5JK0FJPz_P8tXNqq4gvX_p79rbmEPOftbDraAaplnlvPXCtSxG7afoyRGyOvaPSf9pQONqh6td4HB0AY6wj1OP4v2C3422qM-G9lLKXc2HK9c2fXeA731hZSYuQOfytnaRfWS_Xck_ZWprWN5TlFF7NDL8nJPVKCZ5HqOv2FNhsjcwx5PWe9cnDCNIw5XN7_kMUxETtaukgf1K8uZq9RgvfyK96lgqCHNbVXdVqB1K9snUzVufiOs3RziOcyd7usm6B_HUyHS8JMQV_KaZLXTwr20mCZ0JT8rP2-p294Yo2MZeBO5fOTq3FVTcV-lbQmRbxA859uRDd1-vvyNVA9ywSKczsNF8pEkv0BfMoKFvI8_tEq67o8j61JYZHlp87vim5OHibcPom-bxdPKxpbjVLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f1912163.mp4?token=vsPNcw9kbpSbcMQcn5eQoqt9Sd3iNEdIY5jeRqu1cHUy4vBeA0887Kr7gqXvXTysY1gEOuh3S3gZFW3_DdNid3BLEr0ZIHk76VsEHgMQvEI7JIYBVxK29gUi3eN8XVFa4-Ehfvq1VyfoBq8IGtL2pyVzqMUFIZGkvjlUqAYYqwAOUY8hFpItzuKwViQPSuh9m0ZcprAfrKJ76xOJ6EyXI7vo16r7fktZmA6Aq_GvM0XpBWvY8m746IOLGz4WWxBSmF2vXvqxGBHFRxINkCk5JK0FJPz_P8tXNqq4gvX_p79rbmEPOftbDraAaplnlvPXCtSxG7afoyRGyOvaPSf9pQONqh6td4HB0AY6wj1OP4v2C3422qM-G9lLKXc2HK9c2fXeA731hZSYuQOfytnaRfWS_Xck_ZWprWN5TlFF7NDL8nJPVKCZ5HqOv2FNhsjcwx5PWe9cnDCNIw5XN7_kMUxETtaukgf1K8uZq9RgvfyK96lgqCHNbVXdVqB1K9snUzVufiOs3RziOcyd7usm6B_HUyHS8JMQV_KaZLXTwr20mCZ0JT8rP2-p294Yo2MZeBO5fOTq3FVTcV-lbQmRbxA859uRDd1-vvyNVA9ywSKczsNF8pEkv0BfMoKFvI8_tEq67o8j61JYZHlp87vim5OHibcPom-bxdPKxpbjVLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: لعنت خدا بر آن منافقانی که به خدا گمان سوء دارند و فکر می‌کنند خدا ملت ایران را در انتقام کمک نخواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/449223" target="_blank">📅 21:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478d72c5e.mp4?token=U_8n4xYTIRQNaP1RYJzlELuW24En-YJrk_pzNI_87cgurvRwfQbKGu-Dd4ixW2qqRxfbRjhxl0D2xDmve1mwp9HdOoB_dA_xdtxw0wYIxKXQtwlXkryzmXJcxAaGXYaVf6-qNk4hdYtH3AiTTiOasGGXC9bI82ZrBkEBm6TbvgZCXTs8FWa8IbEs5ceF4C1aeD_DNBrSTo9AobDYBJ34-lX_Vdcsov66nrMLlIdu_HjfhiD3IqS846Mv7YYrI4mr7FHOJoUm88gSEasbxgFTJ4jr-tRJXTCUVDar1l79XeUf3kt-BpeAfYxd2chcT45RR9akZtrftoG6sFbDr_Z0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478d72c5e.mp4?token=U_8n4xYTIRQNaP1RYJzlELuW24En-YJrk_pzNI_87cgurvRwfQbKGu-Dd4ixW2qqRxfbRjhxl0D2xDmve1mwp9HdOoB_dA_xdtxw0wYIxKXQtwlXkryzmXJcxAaGXYaVf6-qNk4hdYtH3AiTTiOasGGXC9bI82ZrBkEBm6TbvgZCXTs8FWa8IbEs5ceF4C1aeD_DNBrSTo9AobDYBJ34-lX_Vdcsov66nrMLlIdu_HjfhiD3IqS846Mv7YYrI4mr7FHOJoUm88gSEasbxgFTJ4jr-tRJXTCUVDar1l79XeUf3kt-BpeAfYxd2chcT45RR9akZtrftoG6sFbDr_Z0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: عقلانیت به ما می‌گوید باید انتقام گرفت. باید خواب آرام را از دشمنان و به‌ویژه مرتکبین این جنایت گرفت. دشمنان ما هم به‌شدت در دلشان رعب و وحشت جاری شده.   @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449222" target="_blank">📅 21:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449221">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16e075cca.mp4?token=DnjqGFefxWdyhlq_2jpZdQjM37ZfoVoy0U9JSFgLm6-o3RlrVKfkx_QLx6yCplJlCxTr2-mBgKB1vNGp0g-U6Bf6rZHvRBTv_6xP6Zc8wnmy7TqJEmxy5TCJvileIZYy7ge2o0j0-FJk3e2BVsumFMre8acj7j0G2SDvM6BV4lFcs7OLXBXyQn-OecW7j8gmf4b9tFi50eftDxBpQJ5IA8J5p0BRTfE0D7SjwxfslLhqc5LFt7lnDxso477ql8GqxjLlH1EfWMJPntGtgExtLxgP09CqgQrRPeBwVGkjjbKNb8JKmdBIFsQFSUzTuM9nQw0midXZRE2mB4rpavKqc51vqR4E0usc96nOnYZ-xQPZ-Y_RUnwRixHShn3TlkEyOaGeREHAN74lqlkM3DTkMNlH40cEu_PulfsB-SCby6KGmamQM5aVZMZhyDG88_nMSV-_0frnc137uHmnJKMj_xO3xEbKwTZyv8KOJjuaaAgDZq4J4tiXySinHkLzCumxChGYzk1GCnIQQV6zm7WHYnOXbpAecle7d8pj_8kzhzMo7mmsRWpNY8btPcOwY0ihVKuR371fDs6ngE6fxlv_RcSw7yHc1WMOx07eX8iRGzrl9EzGoMnCnAS-MEOlhnCgMgHDqecIj5SE5yvmom3bhZWP1jKhb5hoY1x_xY2TcVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16e075cca.mp4?token=DnjqGFefxWdyhlq_2jpZdQjM37ZfoVoy0U9JSFgLm6-o3RlrVKfkx_QLx6yCplJlCxTr2-mBgKB1vNGp0g-U6Bf6rZHvRBTv_6xP6Zc8wnmy7TqJEmxy5TCJvileIZYy7ge2o0j0-FJk3e2BVsumFMre8acj7j0G2SDvM6BV4lFcs7OLXBXyQn-OecW7j8gmf4b9tFi50eftDxBpQJ5IA8J5p0BRTfE0D7SjwxfslLhqc5LFt7lnDxso477ql8GqxjLlH1EfWMJPntGtgExtLxgP09CqgQrRPeBwVGkjjbKNb8JKmdBIFsQFSUzTuM9nQw0midXZRE2mB4rpavKqc51vqR4E0usc96nOnYZ-xQPZ-Y_RUnwRixHShn3TlkEyOaGeREHAN74lqlkM3DTkMNlH40cEu_PulfsB-SCby6KGmamQM5aVZMZhyDG88_nMSV-_0frnc137uHmnJKMj_xO3xEbKwTZyv8KOJjuaaAgDZq4J4tiXySinHkLzCumxChGYzk1GCnIQQV6zm7WHYnOXbpAecle7d8pj_8kzhzMo7mmsRWpNY8btPcOwY0ihVKuR371fDs6ngE6fxlv_RcSw7yHc1WMOx07eX8iRGzrl9EzGoMnCnAS-MEOlhnCgMgHDqecIj5SE5yvmom3bhZWP1jKhb5hoY1x_xY2TcVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: عقلانیت به ما می‌گوید باید انتقام گرفت. باید خواب آرام را از دشمنان و به‌ویژه مرتکبین این جنایت گرفت. دشمنان ما هم به‌شدت در دلشان رعب و وحشت جاری شده.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449221" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3fcDon9gVv0GuXESvZB_M2Q4bwgYpF5jiwSQs2RvYm2bN0FL9jV6H3UWzBHQx7zKbaWPBYyokDfNr3tzRRYKvLO4QI8v3ABinJoPYvJM44JdEcRr7YyOef68ARCdYpUVZWM7D5QRnGltUYx-c-v1AR_j5rWv5kBgGViG18lej9-IDzCuUtg9e3vCCgFikCx2Ip-ggsSb0W4vcQfSsraJpkm4_7xf9LPrY3Yv_VJHD6J_ACShyHVlwCMwnWomocNFlHzZ6Pjba-wQpYT0Jy6a_NJLlc-ir6IqvE5Mm5qNi_wUVG9fHjyk6xjZnu17MZKgJvgjLPLzx0ch4VSLU03aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نظرسنجی جدید از تجمعات مردمی سراسر کشور
🔸
خون‌خواهی رهبر شهید مهم‌ترین انگیزه حضور مردم در تجمعات است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449220" target="_blank">📅 21:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2de71c563.mp4?token=TZYWpB8kjnXd9LjGb2v6gKBoBLfrqSuJrk-FmcSCf2VGmcgb5NS0Rxs3W6AZIUMw1XiiV4iqclNZ8Sg22aaye5eMA1BPFfmaaZ4_gtNzkGVul9Ty6HFG8MdkjOgD_5meG7fyhSXJWej7CU-TG57OEHoYlstIFzwa2b6YCaLJ-MnJDyGNdvgF3nXzHDCXvMzp6gFNSZoWKMA7hg-xBC1gZuwNfTrQK7kQcGrYNLsxSPTd6VgWjlTM2VeU36zUGk59w3KjX1OTVj29XQaMm2RAeEr23MSrvKJ5paljVaioeMrzpZTTK7egsrNkGI0QUDGE03rbeIzaY55GU9v8J0EUPIVpU3c9mcOUWCBt1SVCmyYupAs63hDYbhSoJ8X16m-W9c_FPtz2dsE9trG6vCPI4xh9606KOWCLjSgd0UpgvbW2dfLsJSqvvRzZZt4veYSehI-dnSbpxOXIpHKDK5QC2Zf9RCRkdBNCZkyhMxRr2DmBDMoAchWOIZ0lfsNdK1CrRToYBMuUe1II-wyznGb6l7CmUbMhnbO6Fw3PWGX5QdWMe9v5l2dreE4i7kqxKNztchu8aqOftDiGv3uRaB4V-jL7nQAXSnEQYV3ohZycDW7N06YuE7NhnbGZ6_LJa_UdCBKSz1QV7k13mQQvruLT3qEnh--IJDx8BiTex7o79zU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2de71c563.mp4?token=TZYWpB8kjnXd9LjGb2v6gKBoBLfrqSuJrk-FmcSCf2VGmcgb5NS0Rxs3W6AZIUMw1XiiV4iqclNZ8Sg22aaye5eMA1BPFfmaaZ4_gtNzkGVul9Ty6HFG8MdkjOgD_5meG7fyhSXJWej7CU-TG57OEHoYlstIFzwa2b6YCaLJ-MnJDyGNdvgF3nXzHDCXvMzp6gFNSZoWKMA7hg-xBC1gZuwNfTrQK7kQcGrYNLsxSPTd6VgWjlTM2VeU36zUGk59w3KjX1OTVj29XQaMm2RAeEr23MSrvKJ5paljVaioeMrzpZTTK7egsrNkGI0QUDGE03rbeIzaY55GU9v8J0EUPIVpU3c9mcOUWCBt1SVCmyYupAs63hDYbhSoJ8X16m-W9c_FPtz2dsE9trG6vCPI4xh9606KOWCLjSgd0UpgvbW2dfLsJSqvvRzZZt4veYSehI-dnSbpxOXIpHKDK5QC2Zf9RCRkdBNCZkyhMxRr2DmBDMoAchWOIZ0lfsNdK1CrRToYBMuUe1II-wyznGb6l7CmUbMhnbO6Fw3PWGX5QdWMe9v5l2dreE4i7kqxKNztchu8aqOftDiGv3uRaB4V-jL7nQAXSnEQYV3ohZycDW7N06YuE7NhnbGZ6_LJa_UdCBKSz1QV7k13mQQvruLT3qEnh--IJDx8BiTex7o79zU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او سرور مقاومت‌کنندگان جهان بود
🎥
مردم عراق دربارۀ رهبر شهید ایران چه گفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449219" target="_blank">📅 21:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlnbirMxSpx9Wa1675ub9OiV-i6yEg4j7cb3jjxSLlvjDWdyrEQmXb2aegJuNCyE5iuGPIQLdMm6MqUJFwLOhfUKJMaeB2uQHS7bfBc-SJ7kyZ-FUPM42YWniZ7_zsd4zrDVN3iCPRHcgHQrJDJPmN6PnP5qtCfPXKf6yqYv_IH9dszq5sd9E-VKtDSc2SJTuKdOGOTqRnOZ8hu2GzuvfybZJjkQTNYBNJonwrc7aHzJesvM4GWYGUC2lX3MCqMgZI87m84cYuqWznsyOfLhRJ-tYAGfJ3W3RGSzN4ERyuPDZ4xLketYIWVUBWOV69y5fvY6wKd_1OUaqaSN5FHZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
🔹
«دیمیتری پسکوف» سخنگوی کرملین، با رد هرگونه احتمال شروع جنگ جهانی سوم از سوی روسیه، تأکید کرد که مسکو به اندازه کافی بزرگ و مسئولیت‌پذیر است تا دست به چنین اقدامی بزند.
🔹
وی با انتقاد شدید از رویکرد نظامی‌گرایانه اروپا، سیاستمداران این قاره را به «شستشوی مغزی» مالیات‌دهندگان خود متهم کرد و گفت که روسیه به عنوان «شر مطلق» معرفی می‌شود.
🔹
پسکوف در عین حال هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449218" target="_blank">📅 21:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722505521a.mp4?token=Ka_HCYjJJacA1EgnhfLjtP4ZlNKzIikcuIiCgwAozbQPioVCw55f4SZCm9pKtp3RO7u4cRUaVGltXWtz2sn7CM96AckaeGp7eh1HNJXks0--tIukkQYMMtVFHb4euiafW6I9mHChRYgj5--Msng-UrGCYnXQWALPrmSoE4k6_i86XcnmDM4ZFfdTli5H2w0TQBU-9YQ4UZ9bVwZE8H2AJoeF9EeuaoQWLDK0M2MfkUGR-KqHAJ3-JiwvROgS3oJasOYarkhTzPDasfwamG9cL4Uzg2mjYUzbjty35WUjgFC4WjQyBeZts8XGHXIyvX6L35JfkJWWCQFTtCNubws1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722505521a.mp4?token=Ka_HCYjJJacA1EgnhfLjtP4ZlNKzIikcuIiCgwAozbQPioVCw55f4SZCm9pKtp3RO7u4cRUaVGltXWtz2sn7CM96AckaeGp7eh1HNJXks0--tIukkQYMMtVFHb4euiafW6I9mHChRYgj5--Msng-UrGCYnXQWALPrmSoE4k6_i86XcnmDM4ZFfdTli5H2w0TQBU-9YQ4UZ9bVwZE8H2AJoeF9EeuaoQWLDK0M2MfkUGR-KqHAJ3-JiwvROgS3oJasOYarkhTzPDasfwamG9cL4Uzg2mjYUzbjty35WUjgFC4WjQyBeZts8XGHXIyvX6L35JfkJWWCQFTtCNubws1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در جایگاه سوختی در پایتخت اوکراین درپی حملۀ روسیه
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/449217" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea5cd6288.mp4?token=nFroUiiv3f9svO4CIqz3JCn2-uLTOQhiN_-M6sqQO8116op4PKF5InRPM5Xdb9ohBN0kPdW8Z0Jt-EHwiwtCx69NvPvLiwFKlskUTYhJxK7V5bdROfxc0A0OV_55vi46S9nLEbgmHRNUIZui15iMkrCLPHV3X2Y7KJ_uSwUYqmvOTPFnmbtekcZiTYzUYDQZTuC7O2ry8ieZMUihaVbY6zU6rD70k5rZe5jjGu5duwoiLWgqZKpeTi5hK1tH8HiGoAU0cYs8q3kQmkC9qy_n6JBPg_dbGWDb7Rn9DV5iSz1QVSoeM0Pkbw-osgwbeJCz-ihoDOFkVqpcaz-cjqwk2r6lXlHNEAMHB-2Cb-_UjVFUTzoa987cY5SRYxf9Kb_DMUUBPymP-DHTJfkKa-gI31aT0ZB5R2PXgwHAPNzBHHzgr33ZZtF525BBurR1zXHhxoxCUe4TW-SThehPaoYMilfav0YGOBOf05DOxm2k5ffq-ZdsWgBW4ZJeRprbaS8DioQ1BZpOWVuMvW80pbCmL-t-aBu4Vd1a7fQ3esC0oges1utDbe6HthasTvn59EkALnDm9PKmL0VT5TXZ8dyT4NFF-iBo7OVubIrJM3kVKZ3fiKmLNvMxT5XxEClR8VTgKAoxb7m2cGvBgsA_DW_JiddmZ7mcNF7nDdxR9YXiL9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea5cd6288.mp4?token=nFroUiiv3f9svO4CIqz3JCn2-uLTOQhiN_-M6sqQO8116op4PKF5InRPM5Xdb9ohBN0kPdW8Z0Jt-EHwiwtCx69NvPvLiwFKlskUTYhJxK7V5bdROfxc0A0OV_55vi46S9nLEbgmHRNUIZui15iMkrCLPHV3X2Y7KJ_uSwUYqmvOTPFnmbtekcZiTYzUYDQZTuC7O2ry8ieZMUihaVbY6zU6rD70k5rZe5jjGu5duwoiLWgqZKpeTi5hK1tH8HiGoAU0cYs8q3kQmkC9qy_n6JBPg_dbGWDb7Rn9DV5iSz1QVSoeM0Pkbw-osgwbeJCz-ihoDOFkVqpcaz-cjqwk2r6lXlHNEAMHB-2Cb-_UjVFUTzoa987cY5SRYxf9Kb_DMUUBPymP-DHTJfkKa-gI31aT0ZB5R2PXgwHAPNzBHHzgr33ZZtF525BBurR1zXHhxoxCUe4TW-SThehPaoYMilfav0YGOBOf05DOxm2k5ffq-ZdsWgBW4ZJeRprbaS8DioQ1BZpOWVuMvW80pbCmL-t-aBu4Vd1a7fQ3esC0oges1utDbe6HthasTvn59EkALnDm9PKmL0VT5TXZ8dyT4NFF-iBo7OVubIrJM3kVKZ3fiKmLNvMxT5XxEClR8VTgKAoxb7m2cGvBgsA_DW_JiddmZ7mcNF7nDdxR9YXiL9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در رواق دارالذکر به آقای شهید ایران چه می‌گویند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/449216" target="_blank">📅 21:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faIzhQw53v7Ti6WoS5btfADG6x5b6ghrtWiu4IlSiwj1b-OR7NDdiXHfGLFxfWYPoP8t6C0WvC2tcEhvLtJ7O-OWIE1ZJWt984ih-6cqia9w7eooMsUrl7H769k1631N4Iu2dlZPWhhWsS42NoOumpn72oE7Kf4p1meXMp4XHc0ox9Ub8PlG1Q_olQABwqeJiGCwr-isXNz9eSghLut72cEOWQK4vfT562Y6yFd8LmmlUGWhqj-9Hl9qPMGozlxyf8cw2wm5EJjeSbcnOKvKRTcWBq79FymQ0fb1prYMmVA0YL2oNpuqiblr9BdIuoStouf0r47_fuT6b1Tl-Qttig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWUtps7_fucN7t1DPW6Z7nfF-kSCU7DvgHVcqUwc5foBrx_arIEXq6koWPrWixZ2HBpS4IZgBDvfdYZTB3uJwDNV16RfqdH920ofQVXTVNjQWvoV5k3_SdBJ8ZKNQDGmLZ5zXSkbeEOSL-SnHEPyPkaHqBWuKHC2bH_bEg7y9WXLTPdx-oqOsOXcFqy52D6qUHH2egiHAVsi73_-P7dYCs3y5XA13zlXiAZr0kdIR5P4l1AbiCvEiVIKgdF2oNoUbQmNqIn3vOoJWvDlASTV8FHmrZ_PHKEMhYegtoDRDk--IwS4lo3cE3SahcfhwDtBNHIvvAtXxD_DaP_gAWj7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KysGvuKnEZURio-VzbYKhbU9AnOvDLKPP-ZfOUcghwguJkeAJ9LxBMm104Rqht7ENqMFBHisOC6BCr4cIt4opDJbzESklm8Jj-qCfiq5jIATdgejQ_mZbRAAD8DMjvJzPvuixUr5vH-mvsk5DpWJxvgiL8Xp8qBaMGjYWcmVa7-Lg4LCzOA2E2FerKFcXCvBGn9H5Pl1RLeaTRDL9sYuuvfwnsht5an4yLqnyqvUsv0Xi6ihtESYPMZx_UMQGfnXJkecEIgDqxEKeD7q7JFV1go7XymBN_RrNQ5YZ6ptL3sj7lTrU1zGxx4662N_Yma5WOfJPeH_YEfeU-dFGd6zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRFBGYwdMP2JHHVDyUYUSuhajJxvB0F95KxaUBRUAzSHiT6byFx_6aA-g2ik2caSwKghsrBE62JLo4Lht-qvKGx8K8nkY8HyqBfW-cBUaj0yVWmtqWG-hA2Kz3rJrfQBjrzRgNSwvz74KCeR8u-0QnXTLVf7tVu06_lBJqUJFqTIYNs_zx5yJNfQywZvdZxDzKG_z8ZGUPzW8k-m7ZTYPgdAQvWLI0ua1lVz16poZEzDUuPxq-k-DV5qdXWgBl5nsV7TKpIWR7sDAzofNyg8CTO_v7mpXD-juYocrsdjGQAhPjhOef8zrLBH02G2oN51ey-ENKWbakTvTr6Xj6fycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EACsYT8wGhQJxdyXkuslL_uWf6Nw6wRO70fhDelTlHSz0KiPcUQHirzMyvKnClCdOEBN-bqXKhcx7Nd4UTAVTuierw9wfapZQBepAY26C1AZUyOQGgRXPi_J9PSCQawat5Kf3LWyorAkzqoXRoC9bEtze0pctLOuuD5aFsitZiEuhSWScDUN-iSZJ-4b41xOTxoYYaJAV5mg9AiIULOfHFDqTy_XHzLpCkmBhcSITQWs5WtRnxDLVTL3ToR2s0zQV1VpYPHJy_BXPPsky-cPan0hyE9cBI4SOQfaAAbTy9AT7F6hy-7De2R4gMgt43AtxEbIHcryJ51DRtldGNnXOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع پرشور مردم البرز در بزرگداشت آقای شهید ایران
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449211" target="_blank">📅 21:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcad9066a.mp4?token=L0Z0_OXbtmAj1cNrhQTeMMR5QmpqWLogYXWVXnDUJwrBL83_ePb6bVYb1tgXiOJ8fFS8NgM_ta57VtFX80UtGRkZIfumdQmOZWReZy6BG84BnduBMj9lJoS_X18Rud4VF071ML6K3T_nuBBt_-qmp0ZCTpRnoREGo-pBjx8VCXx1Of0wSAmhcZP6k0R5l80c1kl20L0fAkJ54YQ1df_5p-7y6b5bCjhCnEygP4m96xkKvl4Ax4dyv6krdQW38vwP4m8cxx-LWiXr6L1OBgkbMsFhY-Vc3Wxif1BFavch-rL9mjX-q-0WUMGerFgCK5wqbr0vukRHvB9DHoBp_qehI5NanKVa5vJ4OQVlEH1_tKZCQc_19eqNQKzsTdDtOWJ07GhvdhztoeMf5FW--mSY_b4lgkN9lwSbrVZEhCaIesCEOkacAcn464kenYPUq44twAxVUF5XwXMuyDUdOBz0Qst19Po2-5WIq7-fL0dAglUBQZ_Tw8Q1aWY86NNZbhbRpXii8lU_MnhVQD_Sd_SXB04x2q1JtTYF5gqwSm8lK3bsCEvBgn9UnkkwtzSLd0cA3XRYej7VSBI56fAB4dhn1ZnbiTBQrib5AWv5i7zuXkdGK96518PNTFhiEs2PUAKAxWns8K-WEoWiaVW9MtfhobUo16F7gRcLRJAY8JCPm5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcad9066a.mp4?token=L0Z0_OXbtmAj1cNrhQTeMMR5QmpqWLogYXWVXnDUJwrBL83_ePb6bVYb1tgXiOJ8fFS8NgM_ta57VtFX80UtGRkZIfumdQmOZWReZy6BG84BnduBMj9lJoS_X18Rud4VF071ML6K3T_nuBBt_-qmp0ZCTpRnoREGo-pBjx8VCXx1Of0wSAmhcZP6k0R5l80c1kl20L0fAkJ54YQ1df_5p-7y6b5bCjhCnEygP4m96xkKvl4Ax4dyv6krdQW38vwP4m8cxx-LWiXr6L1OBgkbMsFhY-Vc3Wxif1BFavch-rL9mjX-q-0WUMGerFgCK5wqbr0vukRHvB9DHoBp_qehI5NanKVa5vJ4OQVlEH1_tKZCQc_19eqNQKzsTdDtOWJ07GhvdhztoeMf5FW--mSY_b4lgkN9lwSbrVZEhCaIesCEOkacAcn464kenYPUq44twAxVUF5XwXMuyDUdOBz0Qst19Po2-5WIq7-fL0dAglUBQZ_Tw8Q1aWY86NNZbhbRpXii8lU_MnhVQD_Sd_SXB04x2q1JtTYF5gqwSm8lK3bsCEvBgn9UnkkwtzSLd0cA3XRYej7VSBI56fAB4dhn1ZnbiTBQrib5AWv5i7zuXkdGK96518PNTFhiEs2PUAKAxWns8K-WEoWiaVW9MtfhobUo16F7gRcLRJAY8JCPm5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/449210" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f5344508.mp4?token=ZS07XjgGmNE0yr_Tlzc5O1qNnIL4l5NSr7DP-AQusdmMkt8MwP4jlmDz-jji9yVOUaUyZBD5cyt4DYmOB8x401EjVFEFosG1JO-2lnHfUZfiMJ7LCnVFNkM77JWAN_R94Z2-dU7tILvAFpio4h4mYxzucyUz1kB8MuR3oEH6rqSM6K2HJLT4RTJZ1i_7HEYu09lVL70BlSYbDghWaSVvIR4YN3Ji8WSFStms3BqZnWDhB4nMq19sD16vZzD-kP2LUqYxMoLy5zJIQwUn7fj4m3bf0cMl6VnW9ostw9ZwG3uSNvys4myAa1MuNEDoOKkPZRwbExhERSHjp7jSPHGxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f5344508.mp4?token=ZS07XjgGmNE0yr_Tlzc5O1qNnIL4l5NSr7DP-AQusdmMkt8MwP4jlmDz-jji9yVOUaUyZBD5cyt4DYmOB8x401EjVFEFosG1JO-2lnHfUZfiMJ7LCnVFNkM77JWAN_R94Z2-dU7tILvAFpio4h4mYxzucyUz1kB8MuR3oEH6rqSM6K2HJLT4RTJZ1i_7HEYu09lVL70BlSYbDghWaSVvIR4YN3Ji8WSFStms3BqZnWDhB4nMq19sD16vZzD-kP2LUqYxMoLy5zJIQwUn7fj4m3bf0cMl6VnW9ostw9ZwG3uSNvys4myAa1MuNEDoOKkPZRwbExhERSHjp7jSPHGxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش
معاون دبیر شورای‌عالی امنیت ملی به تشییع ۴۳ میلیونی رهبر شهید: پس از این تشییع پرشور مسئولیت خونخواهی سنگین‌تر است
🔹
باقری‌کنی: اتفاقی که در نجف و کربلا افتاد بی‌نظیر بود، از این جهت که رهبر جهان اسلام در کشوری دیگر مورد استقبال میلیونی مردم قرار گرفت.
🔹
پیام اصلی پیوند میلیونی مردم عراق و ایران، تأکید بر خونخواهی رهبر شهید جهان اسلام است که این پیام با پرچم‌های سرخ به‌خوبی نشان داده شد.
🔹
مقاومت امروز دیگر صرفاً یک جریان یا حرکت نیست؛ خون رهبر شهید باعث شد نهال مقاومت بارورتر و ریشه‌دارتر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/449209" target="_blank">📅 20:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5074b22b90.mp4?token=gp6GXG-MfBgppW2jNw8pgWfhl4nJIQzuBIA90DEy2gcZzaPZcs51LLAZZv28X4eiN_dtVa9tTizUIYAXatJvYEEZoU0JLPssv7fjY65Hvt-00023L3FRWtwpdEahYeKCWG78L7ZR9CUql6r1zfv_ke7uN_wynK5x3Z8R--Dtga5ycGnQwrZIpqp34miUJgHNjamNDRkDk-jGgI-a2G8S-VwDp7JyMj7vUn1LBLPGrYJOd75ad95t93IDHiP59HZrdY0tfoa2fdDAsCWuib53M1aT_Mj3UjHykyCvbSOd4bxzeIZ_2xa9S7VTuvXIzSOXmQEXpTh7t5vgaMVcW_jZYYneXFBzvuOI6U5_kaQhUfmmMPg4qnaRiQzIxfyAZZm4s4pCeSyYXetkdJnDIAu33O_8YKcTOY8pIIcwy5HsQiiGBDs-FtWoONrt9gO1pki_Raf5J4z7nCA9NYCbKZl9miDRqqfsZ7wJZoU2yd06xbl1GbSFCgn2U8aKRNUTNrwJNQUiTeeso7HUKe8ZIUoSSJJLwPnVKDmlouNyw7ylIDKmxsuLocZwZVxyhI-N3Wi9zNxA5Aus6N3CbuQzaiXH_NRLyfHOZ4lpbidVL7cB7OEHH3xoFUBfAVJfaOT47lsQukQxZVXycdpEsGSZnOsK-a_5p8weUoCygW3jUYNM_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5074b22b90.mp4?token=gp6GXG-MfBgppW2jNw8pgWfhl4nJIQzuBIA90DEy2gcZzaPZcs51LLAZZv28X4eiN_dtVa9tTizUIYAXatJvYEEZoU0JLPssv7fjY65Hvt-00023L3FRWtwpdEahYeKCWG78L7ZR9CUql6r1zfv_ke7uN_wynK5x3Z8R--Dtga5ycGnQwrZIpqp34miUJgHNjamNDRkDk-jGgI-a2G8S-VwDp7JyMj7vUn1LBLPGrYJOd75ad95t93IDHiP59HZrdY0tfoa2fdDAsCWuib53M1aT_Mj3UjHykyCvbSOd4bxzeIZ_2xa9S7VTuvXIzSOXmQEXpTh7t5vgaMVcW_jZYYneXFBzvuOI6U5_kaQhUfmmMPg4qnaRiQzIxfyAZZm4s4pCeSyYXetkdJnDIAu33O_8YKcTOY8pIIcwy5HsQiiGBDs-FtWoONrt9gO1pki_Raf5J4z7nCA9NYCbKZl9miDRqqfsZ7wJZoU2yd06xbl1GbSFCgn2U8aKRNUTNrwJNQUiTeeso7HUKe8ZIUoSSJJLwPnVKDmlouNyw7ylIDKmxsuLocZwZVxyhI-N3Wi9zNxA5Aus6N3CbuQzaiXH_NRLyfHOZ4lpbidVL7cB7OEHH3xoFUBfAVJfaOT47lsQukQxZVXycdpEsGSZnOsK-a_5p8weUoCygW3jUYNM_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عمری «امین» میخواند امین‌الله اینجا؛ این‌بار امین‌الله میخواند «امین» را
🔹
شعرخوانی مهدی رسولی در دومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در صحن جامع رضوی @Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/449208" target="_blank">📅 20:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCkPhH8d1DgnWjX-uYP5e4oMojGFv2j49O4dbGow4HRpKa8wU7iydwoamo0W4S2FUVSuVFLd1XbwvdD69WOPOwnS3lTyVldtnEy4y1pO1UfuxFc1U331SnX-ZocOGRWxD86Mp1dlHVU9BY4sXiGsZ475LxrbJ33OrI77W0NMvnQkA8669-99Z_k027O4Jb1TeZN4hM0U0WQfWg6Aymr6e1n6y4lnzdsUe5COGORUPYo8JwCZDSDcbNb4Hv7m2Usr32XsOYXl8NaJQgpsjBvpaRwuaORdw9mPXO1UJjJNwrqf43Y7Qv9XX6J14x537nfrSqYYjSXXYIR-jdoGwvtYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ ادعای ترامپ را بی‌اعتبار کرد
🔹
پایگاه تخصصی میلیتاری واچ مگزین: حضور جنگنده‌های میگ-۲۹ نیروی هوایی ایران در اسکورت هواپیمای حامل پیکر رهبر عالی ایران از آشکارترین نشانه‌های تداوم آمادگی عملیاتی این جنگنده‌ها پس از ماه‌ها حملات آمریکا به پایگاه‌های هوایی ایران است و ادعای دونالد ترامپ مبنی بر نابودی نیروی هوایی ایران را با چالش جدی روبه‌رو می‌کند.
🔹
به اعتقاد نویسنده این گزارش، توانایی ایران در حفظ ناوگان موجود می‌تواند نشان‌دهنده قابلیت این کشور برای حفظ آمادگی عملیاتی جنگنده‌های نسل جدید نیز باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449207" target="_blank">📅 20:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e7e76e84.mp4?token=aPfVC5uhibHVklo3pDbwglNDhmWEbVtjqY9GAq0D7z-cKLZYCh0J7vhCWefWxsrbrSdXS3Zo_AzgwJNB7mK3VXZd05e23Djo8FH34OakusZ8rED75W8NIYM4ZrjZxz9Z5XpszdGoovEEQ2xSD-9p8xnME3YvmVhOkmLzvPT19KxPtDZR5VLtrD9N4UlbCWNwwuBZGnQcZbgK9qMU7Qe6nOqVycaSwfHzovmaF68YIEtuQRPkA9-zP77VB45LyjTNljpG0ae8YAYuuZPFaNyS1xSQnQrDZe1AUPfYcW7OWwLXqMbmwAKm4gMELdt8r3032f6ykUa-LfFVdci3gdpaskryRKJEHvJ4-j9f0LQhooKr11MAi1Qyg-qKso3l8KEC3i3YoyhH0gw1J0M2jom8-T7dXZxVxuToVlgQCduQr2FtDEOACMNVNEYzrxNtzf7jhpMe4IuL21tcC6X9lObbuB-hnV4Hp7q7SEdO7aqpMI4HCsVJqwX104YK1bAnewTMZX442rJ3VphqGhpz7Q4UJbUWGlc6fWeehGGp39uw3rBGhTrhFrbFlyBLROCwoS-xQne_Ds5v1MGLvASGTG65WNlZ4ccOmihWSgwVJUKqhPtJQse1Lk8JSFNtMHiqISEsCrh2QeM2TbaZQLF4n_vyB9-8j5DTbLY6BdJx7pXm_Mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e7e76e84.mp4?token=aPfVC5uhibHVklo3pDbwglNDhmWEbVtjqY9GAq0D7z-cKLZYCh0J7vhCWefWxsrbrSdXS3Zo_AzgwJNB7mK3VXZd05e23Djo8FH34OakusZ8rED75W8NIYM4ZrjZxz9Z5XpszdGoovEEQ2xSD-9p8xnME3YvmVhOkmLzvPT19KxPtDZR5VLtrD9N4UlbCWNwwuBZGnQcZbgK9qMU7Qe6nOqVycaSwfHzovmaF68YIEtuQRPkA9-zP77VB45LyjTNljpG0ae8YAYuuZPFaNyS1xSQnQrDZe1AUPfYcW7OWwLXqMbmwAKm4gMELdt8r3032f6ykUa-LfFVdci3gdpaskryRKJEHvJ4-j9f0LQhooKr11MAi1Qyg-qKso3l8KEC3i3YoyhH0gw1J0M2jom8-T7dXZxVxuToVlgQCduQr2FtDEOACMNVNEYzrxNtzf7jhpMe4IuL21tcC6X9lObbuB-hnV4Hp7q7SEdO7aqpMI4HCsVJqwX104YK1bAnewTMZX442rJ3VphqGhpz7Q4UJbUWGlc6fWeehGGp39uw3rBGhTrhFrbFlyBLROCwoS-xQne_Ds5v1MGLvASGTG65WNlZ4ccOmihWSgwVJUKqhPtJQse1Lk8JSFNtMHiqISEsCrh2QeM2TbaZQLF4n_vyB9-8j5DTbLY6BdJx7pXm_Mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در دومین شب بزرگداشت رهبر شهید انقلاب در حرم رضوی   @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449206" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg_WdXDMfQKWxVOL166BCliDcFgYL3e2banVrzGH98yggd3NfDNyOAzt9u-icMQPoSZQNyRiLL5O_pVTs3XuJZTRSIJvUviEcts2cpHfMIidi-BbxdS7D7pJA6XfJenZNMVvFeTHUQRbUKpy_rFw29lEx-31ouq8wYPDh_zC_vA2SZh0P02zBbN-QUXzYUGn3GIehOsH82elODRTf5uDit_5lkebbgAIprVUJ2hdxPEX4aFerog3bMGFwacjqnSTlyofq24H_0WZPTWSXlWNLD_ghIGDmwNHl6Y8HyA4RABcLiAbyPH9dCVhVP1zUYRkqnlm2YMjPu0rc0DRA1gSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش از یک تن مواد مخدر در سیستان‌وبلوچستان
🔹
️فرمانده مرزبانی فراجا: با انهدام یک باند قاچاق مواد مخدر، یک تن و ۳۵ کیلوگرم مواد مخدر شامل ۶۰۰ کیلوگرم حشیش و ۴۳۵ کیلو گرم تریاک کشف شد.
🔹
یکی از اعضای اصلی این باند دستگیر و دو دستگاه خودروی حامل مواد مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449205" target="_blank">📅 20:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evBy1N4OM7onRalb0ei2OtnAQ_YrHbOvofBQ4IQGoEAWgCPHsYx28BBIhx_GEOty8I-mKudJx4nrtcLA0pOZy4jvsUOmCmIlyp-wDY0XUs-GnNzMD4jEriQidFc3tOTmoQ2cpsIRnwMbYu8KVSEh0F2ej15oXPhi1Gej-7aHYU97NZVT_GUEJ51O3nk529rKihwHQZ1mkvVA9A-4Pr-vvvwIw-V1EXelQ6Hx-cyx-X50P69cw3vkrLeZaXvEP0LdalubeGZ0kkd8iSzghtwQz4FrBRU_sr_eiCrv0fei8UWrazAXiFIEAqcOgdSFxYqMHbD09vNcjx5pORKbylS9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از  مزار آقای شهید ایران در حرم مطهر امام هشتم
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449204" target="_blank">📅 20:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXYU0IvCz3FuxDsHbuxeSjUy8VTRw8jVlHr0kwLaVoqWvsV0yAVCC9MbtWb2tUjkx1chCTuLpToKkm_YI2Z2vvVoO-p5uDlxIimcamfGuCPuM9nIx5xhyrd_U-Qvw2IFhpmgjlmBR21-R8unoqxo_PccCI-4i6GrDmIQC5XFYHnzy75rvPzm2A1Smb5cbKHV8D6s8FWSSWmIlLOnZzQw5-8FC1_1DzcZHcLS_UaxbJJ1nztag4ZmB65zT3BOqinvW0kl40ZQpCeHc3ILYN8ptl5UETzk-WOCQ4aiQd-cZ5ydtY1Ka_kdY4hajV_iFQcmxaC37-dKlSmsUyOgHuVJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح پایانه جدید شلمچۀ عراق
🔹
رئیس سازمان گذرگاه‌های مرزی عراق در افتتاح ساختمان جدید مرز شلمچه: تمامی آمادگی‌های لجستیکی و فنی برای ارائه مطلوب‌ترین خدمات در ایام زیارت اربعین تکمیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/449203" target="_blank">📅 20:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE14DHHgw2DgfeGZWNwUn-QZl5c6XW2O8avhs36BeAitmLIH_ujrzsSpMowCgY8u4QxdQdwRUlTRWsG3yGhrQ23D7VXz4ODKRxzNWkeMZUN8hB4-s0ZMWTUCBUC8ypMDbDC2DH9hHBVaegMn7r3_jKbxd5Yt0uSh9OsSdlyz5sShMgYV7JAHk119bDiuFANZKJ9x7kaNYxPXis5xtE7DwZg6mIW27eJ4GeUmjC6T_CrxSa8636yH7k6XhFt9O6_W2D19JTR3gdbFZ_IFbSHHBGL3T_oZWVESJYsjPa5CBKSvUr-4lFgzubsih0dQckRt-NAB6DTP3SbSYganumVX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان پرسپولیس از این تیم جدا شد
⚽️
با اعلام باشگاه پرسپولیس، امید عالیشاه کاپیتان چند فصل اخیر سرخ‌پوشان با توافقی دوجانبه از پرسپولیس جدا شد.
⚽️
همچنین میلاد سرلک هم به شکل توافقی از قرمزپوشان جدا شد و مجتبی فخریان هم به‌صورت قرضی به گل‌گهر پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449202" target="_blank">📅 20:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813f961e7.mp4?token=IwWQH2Rw-snAPt_Jfl7dOtSHGJKk5VcAlz1A7RDJFcfW7cX1apEFDh0EwwMMCgAJDMRfQ5HrU663UqexpiKU19f8aWI8pEhsI2Msm7WM7_bW-DX-6a4RaS9cDZ0Q_eCjlRI8FTiSXSIC8hgeJGkZ0df92gvlQff3xda4NjHLR9KjxkuU4U1C9WzB9e5SrmW0tlCpAzvNpxSYIs22NR0xBJbf4asrR4K_dCZ1G76LjfBRqM7zM-Pmdwa9ENddtLkAvlxTIbKAGoBzfR34PBo0yTzmTug53symXG0Q5PbP_7IMisfD9j-BxZGQRa9yyaZAYS72W6wD5dWoSRsrXLX54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813f961e7.mp4?token=IwWQH2Rw-snAPt_Jfl7dOtSHGJKk5VcAlz1A7RDJFcfW7cX1apEFDh0EwwMMCgAJDMRfQ5HrU663UqexpiKU19f8aWI8pEhsI2Msm7WM7_bW-DX-6a4RaS9cDZ0Q_eCjlRI8FTiSXSIC8hgeJGkZ0df92gvlQff3xda4NjHLR9KjxkuU4U1C9WzB9e5SrmW0tlCpAzvNpxSYIs22NR0xBJbf4asrR4K_dCZ1G76LjfBRqM7zM-Pmdwa9ENddtLkAvlxTIbKAGoBzfR34PBo0yTzmTug53symXG0Q5PbP_7IMisfD9j-BxZGQRa9yyaZAYS72W6wD5dWoSRsrXLX54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در دومین شب بزرگداشت رهبر
شهید انقلاب
در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/449201" target="_blank">📅 19:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_AxOl82oMdUwDLMiHpgZQ5fuLgDpaP5mc8neUvN3Dv5vPnj8AAtFzKCbqzDMdgvpN0i3PAiBsnibWZlxWLdj2lbIC8FAISc8VSVCv78XA5JANZbXe8BiNv4pYhqt42wzcqjjdKo1BVZ1783XrNkXl22xqpTJcvbXn2YxCSWXZIyqkkpOkfZZCdw6L9wlwaR5qW_NJiMQ78qxSMMyLh83zH49zF5-mI8snSXRzfVaTQyggueVYvvwpopm-wUnrO-SHCRqAGNqwufY2OKlXty2vwLCa6qFxcZKc_azRPltZVKUyk6WQ9CnFadb8KeVL4PR5QZ0cKvJ9QH2SFp6W9Vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهانه‌تراشی‌های اسرائیل برای خارج نشدن از مناطق اشغالی در لبنان
🔹
روزنامه صهیونیستی یدیعوت آحارونوت امروز شنبه به نقل از مقامات امنیتی اسرائیل گزارش داد که هنوز دستوری برای خروج نظامیان این رژیم از مناطق تحت اشغال خود در لبنان صادر نشده است.
🔹
این در حالی است که امروز یک هیأت نظامی آمریکایی در بیروت حضور دارد؛ آن هم به زعم تلاش برای خروج نظامیان صهیونیست از دو «منطقه آزمایشی».
🔹
در راستای کارشکنی صهیونیست‌ها در اجرای توافق اولیه دولت غربگرای لبنان با سران اسرائیل، یک مقام امنیتی این رژیم گفت که تحویل دو منطقه آزمایشی به ارتش لبنان «هفته‌ها طول خواهد کشید».
🔹
وی در توجیه این اقدام صهیونیست مدعی شد که ارتش لبنان هنوز آمادگی ندارد و تا زمانی که ارتش آماده شود، این دو منطقه تخلیه نخواهد شد.
🔹
این مقام صهیونیست در عین حال تأکید کرد که «ارزیابی ما این است ارتش لبنان قادر به منحل کردن حزب‌الله نیست».
🔹
دولت لبنان با عنوان جعلی «انحصار سلاح»، همان پروژه اسرائیلی خلع سلاح حزب‌الله را پیش برده، ولی مقاومت لبنان بارها تأکید کرده به هیچ عنوان سلاح خود را تحویل نخواهد داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/449200" target="_blank">📅 19:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449199">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0ualcF58nnJB7FI8_Jt7LSekMJv0Z7tfOwBzYArknKvIj3ErwVadBAoyaWMPELbWFgbp1v4IqIqllpLMtl8uyppj5XQTyLTMl53HHnwYtsPkc4Kj4bDmvTsYASwgtRHeOGNQyeWr0uzPSA3oVUW-B685QV4Q-NKbZ19j-7fkz8QsKDGewbkFIsnJmNqNUN41Cu4PNLuR5BOjXvfEXTJahvoxy9BhW0tVLYxzVgjW32mZ7_k97Hu8tfWAdHTr8eNaKjh6pp1HjENHU6A2qV8eHXhnxXNLyVVMZricOjlWUwd_uXi8eMbCUuQ5-RS9shqiATIULNZH6AAAiEDprsqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449199" target="_blank">📅 19:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3fc6df675.mp4?token=Lc94Xg1QABXbE8oqIHhttRSwd_N0awEXpBwySO9J2eHnmbsQet_1T8aOAQSI6jkxO4z8EDFBdIqgtiytdz4U6_B_uk2Ei6cXswQz84W-G_eEK9XyWjdGtkEANKpqxP3BuDxxVnzrVetoZrguHQk8WJZuZIl3CsjH9Vc7exI2gindT8LwHFFBrNAcsaSFQwdUMWGP1_O5BgBkLlsK_VfOYLcp_grZBXbcChSqCzwKubBVWPhAxRi62X3bPMZUWk4A-u_09l_mM7qL9LLQjH18L5npZ2G7cD0vSd-l5n5PJ4kWADkR6JJfNqc3ycZ0HHwoK2fgelz54_tO-1yeEvRuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3fc6df675.mp4?token=Lc94Xg1QABXbE8oqIHhttRSwd_N0awEXpBwySO9J2eHnmbsQet_1T8aOAQSI6jkxO4z8EDFBdIqgtiytdz4U6_B_uk2Ei6cXswQz84W-G_eEK9XyWjdGtkEANKpqxP3BuDxxVnzrVetoZrguHQk8WJZuZIl3CsjH9Vc7exI2gindT8LwHFFBrNAcsaSFQwdUMWGP1_O5BgBkLlsK_VfOYLcp_grZBXbcChSqCzwKubBVWPhAxRi62X3bPMZUWk4A-u_09l_mM7qL9LLQjH18L5npZ2G7cD0vSd-l5n5PJ4kWADkR6JJfNqc3ycZ0HHwoK2fgelz54_tO-1yeEvRuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله به تروریست‌های ضد ایرانی در سلیمانیه عراق
🔹
مقرهای متعلق به تروریست‌های تجزیه طلب ضد ایرانی، امروز شنبه، هدف حمله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449197" target="_blank">📅 19:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9571b6ead8.mp4?token=s_5UhOhlvczs4dH_KCL0PIx6zsz6j7UjglyHvwNvDCfSEImF0dPIvM2ZvkX98hrSz165v1UhCUfIKtIGvnzO041M44ztM7UNC1UUCemmY8RHwR8E_dE3U9efQgEzIFwzfHClVJlfJB7SONlN7TGsMh4IyMn7lfTi5kUhhncfvuUSQH3OYDZ51ItSSbIlJPCdyueITbvqIZP9Kywj_1F6iJgayf2MGo9IBx6lv7ML6pATKqwqu1ucCJDGq-JSVK7VFw6rvnKwfclWlWwxOV7yfryEGEMtPOVW4vcQSYXj35cPJMDsUWztFLardHWpN0MgoJ2wcCw6Q2yPBGkN8Wkf0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9571b6ead8.mp4?token=s_5UhOhlvczs4dH_KCL0PIx6zsz6j7UjglyHvwNvDCfSEImF0dPIvM2ZvkX98hrSz165v1UhCUfIKtIGvnzO041M44ztM7UNC1UUCemmY8RHwR8E_dE3U9efQgEzIFwzfHClVJlfJB7SONlN7TGsMh4IyMn7lfTi5kUhhncfvuUSQH3OYDZ51ItSSbIlJPCdyueITbvqIZP9Kywj_1F6iJgayf2MGo9IBx6lv7ML6pATKqwqu1ucCJDGq-JSVK7VFw6rvnKwfclWlWwxOV7yfryEGEMtPOVW4vcQSYXj35cPJMDsUWztFLardHWpN0MgoJ2wcCw6Q2yPBGkN8Wkf0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشیش و فعال سیاسی آمریکایی: ترامپ هیچ قصدی برای عمل به وعده‌هایش ندارد. از چه زمانی بزرگ‌ترین شیاد تاریخ به قول و قرارش اهمیت داده؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449196" target="_blank">📅 19:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPBYlMTiEd91CnZZaDFG-ImcIwri_WBjzUIg75DSptSKQHjYMyeq2MQUgZ3Qro6O4BAG6zBUabOdxGz3ETgTWWXGukmtPo_9Dak55H_bFYlF3pgtRqDKotn4NGlHO5CWgbJLslth-dwFRuWgPjtdYGV10GxWmalmgoHqjFUn19RLBfsn00RhH8AlQO-bwvvh25qbPP7rZcDst7AHTQDzt7sw8S4kyCVsg4Ug2dbjBxloAG3WnfcI-PFQZTyYummIJDzQbPlG7l63PLJgsegLrv20cMyJZMWZnXcBSagw0yDQZPCvO7cMcMT2OCALN1lEd8dGdYwJpNupx9uA0dqSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: پس از تشییع باشکوه رهبر، مقامات ایرانی جسورتر شده‌اند
🔹
مراسم گسترده و باشکوه تشییع رهبر عالی‌رتبۀ ایران که با حضور انبوه عزاداران برگزار شد، به صحنه‌ای برای نمایش قدرت رهبران جمهوری اسلامی تبدیل شده‌است.
🔹
به نظر می‌رسد اکنون تهران در قبال ایالات متحده با اعتمادبه‌نفس و جسارت بیشتری عمل می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449195" target="_blank">📅 18:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdde74aaaa.mp4?token=HGlsI9Q6Mj8aqo46Plzqthbku0Sm_WmDlN-IOKtV7b4_OZ1Db6P-A6s0Ow60xTzzvBWJH83lgVQxshScVKHtOn9wVN_mXm1LC4y-Os3VY_QBKW8MdSY15d5CT3DJq2d-bb6VV_Uj9WqmdZofS486OAWF4F3ee8grBR7Edzlh9j9rcidYd-Y-mC0xEKx5dwKtKt-w0M_5mVwRgAUgwNRnMKFdJFmZoSPkK-To4ugH7sRJQCU_4lx3gWPhqL_tJuYKth4015q2mUefgS3n_KziLUoWLceT0s9-Sybfh5a1r7GgTS_OYOSv8zfPe27-xXtBloNrlxRS2c3LegMS2Co40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdde74aaaa.mp4?token=HGlsI9Q6Mj8aqo46Plzqthbku0Sm_WmDlN-IOKtV7b4_OZ1Db6P-A6s0Ow60xTzzvBWJH83lgVQxshScVKHtOn9wVN_mXm1LC4y-Os3VY_QBKW8MdSY15d5CT3DJq2d-bb6VV_Uj9WqmdZofS486OAWF4F3ee8grBR7Edzlh9j9rcidYd-Y-mC0xEKx5dwKtKt-w0M_5mVwRgAUgwNRnMKFdJFmZoSPkK-To4ugH7sRJQCU_4lx3gWPhqL_tJuYKth4015q2mUefgS3n_KziLUoWLceT0s9-Sybfh5a1r7GgTS_OYOSv8zfPe27-xXtBloNrlxRS2c3LegMS2Co40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حداقل یادگار رهبر شهید را اذیت نکنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449194" target="_blank">📅 18:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شرکت برق تهران: خاموشی‌های منطقۀ ولیعصر و قائم‌مقام رفع شد
🔹
خاموشی‌های پراکنده در محدودۀ خیابان‌های ولیعصر و قائم‌مقام به‌دلیل افزایش بار شبکه و بروز اشکال فنی در یکی از خطوط برق‌رسانی رخ داده بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449193" target="_blank">📅 18:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8463a2e7d.mp4?token=bRitzE_lIbJ3oQP9qM8MW5gMstAFiQP0Yw-JKWWJ-WiqVzN9TDG4bLtBYjzMHEyot8elD4tks6BV9anAv1Lf2aSj7pk8J9JCKDE2c_67Xs4F15rEyuA2QFSsjsBEjd_XqB-SacR8F3ewGn-xSYwqTSlMOzob6ijGra13ATNhdwNAS6JYEOWER3fm4YE9Edbraf-wcf_7sDGa0gqmOG8Y8IzlYBGuChO5wEqrIzRRjNmyDi2U6sGP_WIiVnnINpIFHU7_xVmr8F_M7xbMAHFQnMRxC-kO3qMdEMu-EYmOHM5VDdQ1_OBQJfENfJbvPmptm7n7gZZLFioG2eGQ0YbfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8463a2e7d.mp4?token=bRitzE_lIbJ3oQP9qM8MW5gMstAFiQP0Yw-JKWWJ-WiqVzN9TDG4bLtBYjzMHEyot8elD4tks6BV9anAv1Lf2aSj7pk8J9JCKDE2c_67Xs4F15rEyuA2QFSsjsBEjd_XqB-SacR8F3ewGn-xSYwqTSlMOzob6ijGra13ATNhdwNAS6JYEOWER3fm4YE9Edbraf-wcf_7sDGa0gqmOG8Y8IzlYBGuChO5wEqrIzRRjNmyDi2U6sGP_WIiVnnINpIFHU7_xVmr8F_M7xbMAHFQnMRxC-kO3qMdEMu-EYmOHM5VDdQ1_OBQJfENfJbvPmptm7n7gZZLFioG2eGQ0YbfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر منتسب به محل اصابت موشک
‌
های ایرانی در پایگاه راهبردی آمریکا در اردن
🔹
رسانه‌ها تصویر ماهواره‌‎ای از پایگاه هوایی موفق السلطی آمریکا در اردن را منتشر کرده‌اند که در پی نقض مکرر آتش‌بس از سوی آمریکا، هدف قرار گرفته است.
🔹
این تصاویر از دست‌کم دو اصابت موفق حکایت دارد که به گفته رسانه‌ها، منجربه تخریب آشیانه جنگنده‌های آمریکایی شده است. در حال حاضر مشخص نیست که چه تجهیزات و ادواتی در این آشیانه‌ها قرار داشته است.
🔸
این در حالی است که پیش از این منابع آمریکایی و اردنی مدعی شده بودند که تمامی پرتابه‌ها رهگیری و منهدم شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449192" target="_blank">📅 18:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449191">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYFKmG6YJeHWVfJ0KFn74XEyfCOGEeCjQyKEJTPfExroRjPlgZy9HXK3HPkzu53mXmQn5ryH5ByjVzESMcuwdfeaCBrU0hoN3do2XziDrAa3Ce4WV54VxErMu7On-49QLcobuswWrBX7yMJifRShNW9ntOIWXAKuxAntMgkXw2QiaQ9Lbb5rLU3v7dI-uLnXAyo46WCPstVXB_Rs2oG2gdmBBn49LzxVPsyPKIvkE9R-RJTkasHnuvXJxgl5-ghTVQCIYOOCwV2SwEXdLa9qqvbHehpaWzNP_GjaGR4Rl-UziheUJ7bmenoSgXB8zEjDhM_dt3YpyJ1vJjjnPN6DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدحسین لطیفی: رهبر شهید پدری بود که آینده‌مان را ساخت
🔹
بعد از وداع تاریخی با پیکر رهبر شهید، بسیاری از مردم از ظاهر ماجرا عبور کردند و به عمق آنچه سال‌ها در این کشور شکل گرفته بود، رسیدند؛ مثل پدری که فرزندانش تا وقتی کنار او هستند، سختگیری‌هایش را می‌بینند، اما وقتی از میانشان می‌رود تازه می‌فهمند همه آن سختی‌ها برای آرامش و آینده‌شان بوده است.
🔹
بزرگ‌ترین دستاورد رهبر شهید، تنها مدیریت امروز نبود؛ ساختن آینده بود. آینده‌ای که به یک فرد وابسته نماند و با حذف یک نفر از هم نپاشد.
🔹
مردم نباید فراموش کنند چه مقاومت بزرگی پشت سر گذاشته شد و چگونه ساختاری شکل گرفت که امروز، با وجود سخت‌ترین آزمون‌ها، همچنان با اقتدار به مسیر خود ادامه می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449191" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449190">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2d18097.mp4?token=ODdnsfjZAqX6YtH6W_VrWnrkA2XinD5XB9DlAv5P7kp98wodWvIM-5RzbAe_p2e4-GNNx_BvbPi86DKigxzP56WDReOmz8zI0Rs-qmswlOKy-uATns3bVtAlTU2XCdDsL2R-W75ypiu9u8yM_J4Y_ZulDSe9_vfNtV5cgp7cFEu1rNv6-y2wAP3gTDTNkmVghxmIRK3MmpDaF49_vr_A0BSJ76xC6pLBoR-FnTylF42yag4EMnecnigJEqebMOyFDxhmSAUbiwdkgHEmTI6GneubMmuccBaBRBd1kSUIwV9ZBvqamxNy9m8rc6ApFf91BKrU05ZnMFHZ7Aw4AzB7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2d18097.mp4?token=ODdnsfjZAqX6YtH6W_VrWnrkA2XinD5XB9DlAv5P7kp98wodWvIM-5RzbAe_p2e4-GNNx_BvbPi86DKigxzP56WDReOmz8zI0Rs-qmswlOKy-uATns3bVtAlTU2XCdDsL2R-W75ypiu9u8yM_J4Y_ZulDSe9_vfNtV5cgp7cFEu1rNv6-y2wAP3gTDTNkmVghxmIRK3MmpDaF49_vr_A0BSJ76xC6pLBoR-FnTylF42yag4EMnecnigJEqebMOyFDxhmSAUbiwdkgHEmTI6GneubMmuccBaBRBd1kSUIwV9ZBvqamxNy9m8rc6ApFf91BKrU05ZnMFHZ7Aw4AzB7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی کمیسیون امنیت ملی مجلس: در تامین امنیت ملی خودمان با هیچ یک از کشورهای همسایه تعارف نداریم
.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449190" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449189">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmMpLliWVOl0KqNP1errwypITHD9xMqH2tPcAvngW2dayJ2MhND25mU3hsvZ3AhASHhfXAoPeI54Gb7rcX71neBnzJ8TpGx5k7h3AHCbEE2Hw9Dt0cvf2OgmJfzbRfrwks_RdnoYBcs4DN4iGhEAcAO6tBr59CszdXLnV0Gk5zY8OyeRF3OxpCXaOj9d17zZEP8z9NDZNmLFPFPtzFG9yKIWqPZ5v9xKmIhAZKI18gzrT4iMfi8UbGD96KSu2n-s21YQvusshDafwbGnKw8dJS-qWPTVC9NhOQDqK1M4fRPDSavWTFWoOOVm1zkaIqbhlN6BYoSijSlkKz0hFkI-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نظرسنجی جدید از تجمعات مردمی سراسر کشور
🔸
خون‌خواهی رهبر شهید مهم‌ترین انگیزه حضور مردم در تجمعات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/449189" target="_blank">📅 18:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449188">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmEPK8V-cup_ZuF-wKkiXh7b4-m27N9w3fDh0iGxFGXt5cKPyoVLoZXGnz4Kar3Obzc2T9S8bJpu9mmyh6psu30XHH6RnbABQL3K3W12errutYgCK73FnQCtCqeDgvdyplqtFfpgPvNoPJCeXWtYwQ0AGUoi8eUba3COL1NUaQT_px4RtnTzevWiI95CGK6pTWh9z_qRDquyJQ_xhwqCjscVZ6ZQ5v7qB-ZL4e6w9ES1-SA2NKEPQ5Pw_Psdt9m3s2d4Wpa-UPlJWD1pr6LPtaJeBdvqEttr_M9GjfOMlRjkbYs1GpHYSv8UWvWr4Xk2nFXCjvZ7KCjkXumnGcEwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ستاد تشییع رهبر شهید انقلاب: قدم اول در خون‌خواهی امام‌ شهیدمان، «انتقام» است‌
🔹
آنچه در مراسم‌های وداع و تشییع پیکر مطهر امام‌ مجاهد شهید در ایران و عراق بصورت چشمگیری مشاهده شد، پرچم‌های سرخ یالثارات‌الحسین(ع) در دستان عزاداران رهبر شهید بود.
🔹
امروز مطالبۀ خون‌خواهی رهبر شهیدمان، خواست آزادگان جهان، امت اسلامی و آحاد ملت ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/449188" target="_blank">📅 18:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449187">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a10bbdb5c7.mp4?token=DvzJgjXjv69p_cCpGEIPm8WtKshPhaN72oKpcTehGdVFVFnWOdTZUNv11pLeK-JgO21azH9Nl8bWIpc9I6jbMT3ppSRsJ5eMsgSva3BFMScxNlfRrBFxLCAhQDs79bZwiXZuQRNt-x5gTxu3ms87ZYWsKyqZ8K5HG0MtcKoKe9MtjlUNNrcPnURVpWoWU2M6WxhhkJNcktO5xMsbE_0__m778ycgRY9tSkU_Jfyli8lp1PaC4LNFXzZrlpDYX-T0EThYhLTMkGr18idqoj6MEC87c6pQ2w6DkFj4h3y0M722-t9f54yb7s-MQHhX_yNdlEg5fM-URKP5J1ZqOj7cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a10bbdb5c7.mp4?token=DvzJgjXjv69p_cCpGEIPm8WtKshPhaN72oKpcTehGdVFVFnWOdTZUNv11pLeK-JgO21azH9Nl8bWIpc9I6jbMT3ppSRsJ5eMsgSva3BFMScxNlfRrBFxLCAhQDs79bZwiXZuQRNt-x5gTxu3ms87ZYWsKyqZ8K5HG0MtcKoKe9MtjlUNNrcPnURVpWoWU2M6WxhhkJNcktO5xMsbE_0__m778ycgRY9tSkU_Jfyli8lp1PaC4LNFXzZrlpDYX-T0EThYhLTMkGr18idqoj6MEC87c6pQ2w6DkFj4h3y0M722-t9f54yb7s-MQHhX_yNdlEg5fM-URKP5J1ZqOj7cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ حملهٔ هوایی رژیم صهیونیستی به جنوب لبنان
🔸
منابع لبنانی از ۳ حملهٔ هوایی با استفاده از پهپاد و جنگنده به شهرک «المنصوری» در جنوب این کشور خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449187" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449186">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8JJHR_nMkUTDfMFhhjvoiH1kfmwOq2y-DqHV2RrsEdy1lyF5ig4uPXTdvPvwMFJP4bHbkntbOr03SZVYTLF7vPzCiGgf-ZJRSe-hTQS2oSTxRM7_r3PxKXr6C-zgk6_nwdpTKBvN38EDlHqpaYuuaDV9x1Szhx6A5_eIVvgWdWkbVORyXtB5QAZHbLexlTktvc16c06Iadp9DoL_huzIauguARuatp_xljLuuv-Vi_YY41F0FhlDeT6HjlOQO3_TyqXl6hya6Me6xywka_lAICFsnwaLBitBUtZoB6YxahK0lnXKqp0Lih4SXg9Haa_O5fvCtkdhbDzfvujsUAm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدادعادل: امروز تمام امت اسلام خون‌خواه رهبر شهید است
🔹
مردم رهبر شهید انقلاب را همانند پدر خود می‌دانستند، از این رو طبیعی است که امروز مطالبۀ خون‌خواهی ایشان را داشته باشند.
🔹
هر خانواده‌ای هنگامی که پدر خود را بر اثر ظلم و جنایت از دست می‌دهد، خون‌خواه او می‌شود و امروز خانوادۀ بزرگ امت اسلام و مردم ایران خون‌خواه رهبر شهید انقلاب هستند.
عکس: نگین همت‌زاده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449186" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449185">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0648e369.mp4?token=YKlbzxJJqetrcIUIPnkqqFLLkT4eivfIvM6TbIHvcYQlpswnnh9ws69q6tnfOABRtWvZyFlSwU6_2oFxxhEkqETRpM06ug0B6StCMXztB4joFDXQjdqShJX6NNiYqWjxXwncVRLSbxrKYiQ2Nd35jigIQjet_Z1ujWezB3Nvv8WuL5zd2UfQ57DPdLAMOwYbnUOIAF1QqIpxoFCjsEie5UA4OcIi-A9uML6Qm8bhPkS883W113U5uaTO5sMTWkZYBI8lPVK7_RSHwn8mHUpo48BdchL1FmD6CqmodCA4NnL5M7V45Xk4kftPphedUo5C-et_xMDQHfe18B0bI2lIVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0648e369.mp4?token=YKlbzxJJqetrcIUIPnkqqFLLkT4eivfIvM6TbIHvcYQlpswnnh9ws69q6tnfOABRtWvZyFlSwU6_2oFxxhEkqETRpM06ug0B6StCMXztB4joFDXQjdqShJX6NNiYqWjxXwncVRLSbxrKYiQ2Nd35jigIQjet_Z1ujWezB3Nvv8WuL5zd2UfQ57DPdLAMOwYbnUOIAF1QqIpxoFCjsEie5UA4OcIi-A9uML6Qm8bhPkS883W113U5uaTO5sMTWkZYBI8lPVK7_RSHwn8mHUpo48BdchL1FmD6CqmodCA4NnL5M7V45Xk4kftPphedUo5C-et_xMDQHfe18B0bI2lIVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید را در یک کلمه توصیف کنید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/449185" target="_blank">📅 18:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449184">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3M4hOCktrHKjxM4Xwa2qGpUYZXUEF4DNCi__W5ThDdmoJV0VTgKofDU87m9WMZ2abZhuR6UhpmjRijrCgyf2ip3ppomG0UdjeOtx2X0qnWFWtD_6hB4HYRl4FZTZFkMQpjvZjZ7PTsvQYyQyES0INiHX84QOQh-ZjfHpKV-g-ScIcQRrOX0Hg592j73PkjGQ2MMmatuEgFMgPgb4IIClOciOlnlTmP9IAjsfxfuk1FEwgIM5WYDth4jocMBmPRytFqUtN8av-J4sODAfmSbXmxpdilzGbi9QhYIXSHY7q9csrgdpIMYBxp-PV3tBOj6XK0W7JmyQRcS3YhH5jQVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: نقاط آسیب‌پذیر دشمن شناسایی و محاسبه شده و می‌دانیم در چه زمان و چگونه بر دشمن فشار وارد کنیم
🔹
ایران در جنگ تحمیلی دوم و سوم با پیشرفته‌ترین فناوری‌های اطلاعاتی، نظامی و جنگ روانی مواجه بود؛ عملکرد نیروهای مسلح در جنگ رمضان نسبت به جنگ ۱۲ روزه مبتکرانه تر و مقتدرانه‌تر در حوزه تاکتیک و تکنیک بود.
🔹
با وجود گستردگی و پیچیدگی میدان نبرد، نیروهای مسلح در کوتاه‌ترین زمان ممکن پاسخ قاطع به دشمن دادند؛ جنگ تحمیلی سوم بار دیگر ثابت کرد هر جا بر فناوری‌های نوین و دانش‌بنیان سرمایه‌گذاری کرده‌ایم، موفق بوده‌ایم.
🔹
تقویت بودجه دفاعی، توسعه فناوری‌های پیشرفته، بهره‌گیری از ظرفیت نخبگان داخل و خارج از کشور و ایجاد سازوکارهای چابک برای اکتساب فناوری باید با جدیت دنبال شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449184" target="_blank">📅 17:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449183">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54c80aa6a.mp4?token=HCpIbfVjt4ar9RQAPozrCFdlZx_u9-xZoeSA7BBgos7JTwjLyg4o0OAw4oRgNKbGt0SEy8ALDFHiEWuGDOqwE5oklKId9xQ3ZINFsyz9jwIo10PUoy7Qaif07QT5hmr4eJ2UYsYEKtw30jP2c0rMOuQupBEl4T9cZXykFqvM0ucSfhTKM_SkrmJQcx9gHStwFnSptHX1PjJT4QjhWGPXOEqDiGodwNYSnX6mwj-KWAXfRIr2CdL5rXJ7kH70oyNRKCiNl-TUuTFWe_zG7A9D3pgJF-sMbMBWdgIM68SLthubjb-jykp-doMb0JAAASE7_ow7FMJyaNrYolQVqfSYJrPM4J8SwjdAlmeQ6u0wpLF-90gPTvHBGHz--97Ez9ncST0NZUOFQI1i5jWZ0IeRj_sUqndlsGdlWX2jDnzCklAVIE8oF1YuN7a6Ey_Gn3Y_Xtbfp3403luTyN2KMsiFi9HN9wAt6txNVp18HAXi3XsB-xJZ_K2MQP-LCR3d5x61J9HcMMleCFMis0MF-DvrKffdPJPFGp8eVoOoLtetlzmtqzQktgDBmjUfz0Uua3xVhYpaqkM_YSa3yTqWDThXD92b3zOfhzQE68cwj4Cat0U3gGt22ZF_pqKoamkzzjxmndaS2jyQCtSHsIFJ9OmBbT4xOOc2NSBWBajTTI0j8W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54c80aa6a.mp4?token=HCpIbfVjt4ar9RQAPozrCFdlZx_u9-xZoeSA7BBgos7JTwjLyg4o0OAw4oRgNKbGt0SEy8ALDFHiEWuGDOqwE5oklKId9xQ3ZINFsyz9jwIo10PUoy7Qaif07QT5hmr4eJ2UYsYEKtw30jP2c0rMOuQupBEl4T9cZXykFqvM0ucSfhTKM_SkrmJQcx9gHStwFnSptHX1PjJT4QjhWGPXOEqDiGodwNYSnX6mwj-KWAXfRIr2CdL5rXJ7kH70oyNRKCiNl-TUuTFWe_zG7A9D3pgJF-sMbMBWdgIM68SLthubjb-jykp-doMb0JAAASE7_ow7FMJyaNrYolQVqfSYJrPM4J8SwjdAlmeQ6u0wpLF-90gPTvHBGHz--97Ez9ncST0NZUOFQI1i5jWZ0IeRj_sUqndlsGdlWX2jDnzCklAVIE8oF1YuN7a6Ey_Gn3Y_Xtbfp3403luTyN2KMsiFi9HN9wAt6txNVp18HAXi3XsB-xJZ_K2MQP-LCR3d5x61J9HcMMleCFMis0MF-DvrKffdPJPFGp8eVoOoLtetlzmtqzQktgDBmjUfz0Uua3xVhYpaqkM_YSa3yTqWDThXD92b3zOfhzQE68cwj4Cat0U3gGt22ZF_pqKoamkzzjxmndaS2jyQCtSHsIFJ9OmBbT4xOOc2NSBWBajTTI0j8W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید خیلی بامعرفت بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449183" target="_blank">📅 17:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449182">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cd335d0f.mp4?token=QLgUG5-wsu_CSctzHmZVdKR1JBrDLXDxoEYwrP86UkdzVEhemAaubfgnJ6kZGtTb-Zf1NRjYa44wGZqSVNYVTL2LX5uM1zgnTbwMgXHFVAAgLYjXBA4xNZ9nnpXn2LJZf2RrR3yhW6igAnIDfwYbF-tCuYd4AykxXW5pet0m1zwqn5cYOQCtqj-MedXSdAZSBhLqirw-sWZ2fC5Ly9TFawHX2Wo4pDLUWCQC6AXLsYs54DaPf2da2xnET-dijQ93vnZkMjiTZgHd68nxtvzNSeqbntZBPc16I8p8aMilgGGEjiSKuFphF9GIkFnaX4Cs9qRZP2ZNh0YUW-lZS7Rvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cd335d0f.mp4?token=QLgUG5-wsu_CSctzHmZVdKR1JBrDLXDxoEYwrP86UkdzVEhemAaubfgnJ6kZGtTb-Zf1NRjYa44wGZqSVNYVTL2LX5uM1zgnTbwMgXHFVAAgLYjXBA4xNZ9nnpXn2LJZf2RrR3yhW6igAnIDfwYbF-tCuYd4AykxXW5pet0m1zwqn5cYOQCtqj-MedXSdAZSBhLqirw-sWZ2fC5Ly9TFawHX2Wo4pDLUWCQC6AXLsYs54DaPf2da2xnET-dijQ93vnZkMjiTZgHd68nxtvzNSeqbntZBPc16I8p8aMilgGGEjiSKuFphF9GIkFnaX4Cs9qRZP2ZNh0YUW-lZS7Rvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پیرزن ۹۴ ساله‌ با ویلچر در مراسم عزاداری رهبر شهید شرکت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449182" target="_blank">📅 17:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449181">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20b915b99.mp4?token=kEuqTa5ECCvo92LhKO0Yat_EilkkbHF914Pm_8HT2MLLA_oJqF32Wzy2MboSAtlZfNITBBnaKHJ4uD00ugJ2Bq7N4mZdg9wTdqgZJqz2ThCwjhQ_BNaJVwmwiOpadvUAwr1hbX9cg29p8OLXa0CLn8c0ZOHY4B2rhtJ4nwVmfVykalaj0cCBvRTCHAvgNtdKCZR-26obCzycyjOqobCG_4vBKwbRx5zTpPx9jBUWIzIaXiiO8ZWHnEePD5xEGtB-ds3W2CcFeapwGsydd4xU6L-283UvKWG2-GyJcnA18JEk6Ga_NfnzRzSwTporQYES-8x3XMO9ZCx_QnakT6om0XuEXJh5QVnmcYn74cTSvPZQNcmk0ve-6E9sysUMoFAvDJsmL7I71LeVZFkqaobkgZWIWALs-904v8Z34AamReKxlcz3w0zxIua7XRrWlpccf1lQvGKbf6edeoV3yMe2ul5ATtKd-K6gdpZrzeGPrADnBf4iJRpd-eXzksoPnjW-quNnwRFOEm7hECwKzIeuxtMn62kngHpPKU2GY10RtZ2gA6xofL5PnmEjaKmAmYX3U8Od1ROCnUMEYkRZwTH58_1iwg3QcPkqEHKWTHvQCt76gwJOXmdR2oIRPkLVTQbL35LB4Q7wMQjZLLBn1modqM8Cc-304-QKKNo80W4osm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20b915b99.mp4?token=kEuqTa5ECCvo92LhKO0Yat_EilkkbHF914Pm_8HT2MLLA_oJqF32Wzy2MboSAtlZfNITBBnaKHJ4uD00ugJ2Bq7N4mZdg9wTdqgZJqz2ThCwjhQ_BNaJVwmwiOpadvUAwr1hbX9cg29p8OLXa0CLn8c0ZOHY4B2rhtJ4nwVmfVykalaj0cCBvRTCHAvgNtdKCZR-26obCzycyjOqobCG_4vBKwbRx5zTpPx9jBUWIzIaXiiO8ZWHnEePD5xEGtB-ds3W2CcFeapwGsydd4xU6L-283UvKWG2-GyJcnA18JEk6Ga_NfnzRzSwTporQYES-8x3XMO9ZCx_QnakT6om0XuEXJh5QVnmcYn74cTSvPZQNcmk0ve-6E9sysUMoFAvDJsmL7I71LeVZFkqaobkgZWIWALs-904v8Z34AamReKxlcz3w0zxIua7XRrWlpccf1lQvGKbf6edeoV3yMe2ul5ATtKd-K6gdpZrzeGPrADnBf4iJRpd-eXzksoPnjW-quNnwRFOEm7hECwKzIeuxtMn62kngHpPKU2GY10RtZ2gA6xofL5PnmEjaKmAmYX3U8Od1ROCnUMEYkRZwTH58_1iwg3QcPkqEHKWTHvQCt76gwJOXmdR2oIRPkLVTQbL35LB4Q7wMQjZLLBn1modqM8Cc-304-QKKNo80W4osm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که هر ایرانی، راوی آن شد
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449181" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449180">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0010f8fac.mp4?token=kFoadoz6kWC49470tSTUG0x-EAR2BlJbOxo_R0OTu6djxssOyyO8z4f_nkQdeGGNSQ0iDVD5VcMyR6EsQpBtQd3VptgjtEhMCcTefhaamITHHxfzyw9tYmXpYQWAAGmZU8mNhOvud7Fqp-o2Ej0TQzisS8OLneIScJ-FKZc86OQqr2q92QKDllGf1hKpBL-XLL_a9vhSFcnCrqsXlA1Vj95i6eywbKDDzMUTNQ-1ReemSApQtDUO-DJ_Tbn5C0ZZ4-u77JVCe8OaIMuHbv7lWYqmSSL6fP3SoIq7WTdZzelLXI2wH3KvR8BKy0FZVFbECGXPyBg-0UlEli3v0SVCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0010f8fac.mp4?token=kFoadoz6kWC49470tSTUG0x-EAR2BlJbOxo_R0OTu6djxssOyyO8z4f_nkQdeGGNSQ0iDVD5VcMyR6EsQpBtQd3VptgjtEhMCcTefhaamITHHxfzyw9tYmXpYQWAAGmZU8mNhOvud7Fqp-o2Ej0TQzisS8OLneIScJ-FKZc86OQqr2q92QKDllGf1hKpBL-XLL_a9vhSFcnCrqsXlA1Vj95i6eywbKDDzMUTNQ-1ReemSApQtDUO-DJ_Tbn5C0ZZ4-u77JVCe8OaIMuHbv7lWYqmSSL6fP3SoIq7WTdZzelLXI2wH3KvR8BKy0FZVFbECGXPyBg-0UlEli3v0SVCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیر ما بعد از شهادت رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449180" target="_blank">📅 17:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a05b8dab0.mp4?token=d_DgP2s0r0qQ9Sgl_hcsReIINARflQJc_dv-Bq6vz7jvKO0lY29zK6BneE1iHZdVh9f4FYbsf9IsTV2UK7VMCN4eKE7K6Ce4Al1TKxOjZXtJBEr-KcX4j_0YwVT7KyuXoiTAB-S3zq2IHThgUsYTywfWckTz8vR1GTbDPi59bzcBWDj9UakncOPGwfvwW1ni-mQZYViLGtMk_fE6qmHF65LzSClhbpGZhJsxe5TZIAruqTPxKMZtrHJf2m0Ya-DZKS-X_Zawz84KheZjyrcdySChTOBpEJLdHGdBnx3RiZAXrdoMDrf1-h8Vl4LKMIzvcWKuc1K7zR-JPqXAnH2SJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a05b8dab0.mp4?token=d_DgP2s0r0qQ9Sgl_hcsReIINARflQJc_dv-Bq6vz7jvKO0lY29zK6BneE1iHZdVh9f4FYbsf9IsTV2UK7VMCN4eKE7K6Ce4Al1TKxOjZXtJBEr-KcX4j_0YwVT7KyuXoiTAB-S3zq2IHThgUsYTywfWckTz8vR1GTbDPi59bzcBWDj9UakncOPGwfvwW1ni-mQZYViLGtMk_fE6qmHF65LzSClhbpGZhJsxe5TZIAruqTPxKMZtrHJf2m0Ya-DZKS-X_Zawz84KheZjyrcdySChTOBpEJLdHGdBnx3RiZAXrdoMDrf1-h8Vl4LKMIzvcWKuc1K7zR-JPqXAnH2SJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند کلام با امامِ شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449179" target="_blank">📅 17:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449178">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-pGCmg1E5ia5XqQyfKoT_9PluZVBl1-1UkA6k4ShwaYcnbw4Y_h8H2_zN8gyAvGD0FCO4ZPj-BU5nPmu9y9T68v3VQvjOpRB6Q_cbFfYspwxA9if-M8PfoV9kVQbUFFXF74hwrj6cNTIWF-qQymqokd8wyWaIwUN4KVQF9U_wkkXvyxuraoyql-U_9X3GMHMCdcK_1uoZj3qIE0w8-sb9XBMEdfuYk-r8bgj_jCVymZ4PRN0mW6B-jZVsIEt9xWnl5kH9dZZQshACXb_aWhYXeiRSWWzh4a_U1QqVNmHEhbMYda0BdPVqWBg3NoFEY8ys6OSv1Auu2AE15xGfz1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوت ناگهانی بازیکن آفریقای‌جنوبی حاضر در جام جهانی
⚽️
جیدن آدامز، بازیکن تیم ملی آفریقای جنوبی که در جام جهانی ۲۰۲۶ برای کشورش مقابل مکزیک، چک و کره‌جنوبی به میدان رفته بود، در سن ۲۵ سالگی درگذشت.
⚽️
براساس گزارش‌ها، علت مرگ آدامز هنوز اعلام نشده اما برخی از احتمال خودکشی او خبر داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449178" target="_blank">📅 16:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449177">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00e25a504.mp4?token=pHJXgiQ0eZksqCPUqPwKOCQkUXw9PJZL7gmPj9AVw4IH3RxNuXbncUjJNou8nK_IorV9HCzrkpgpI35D4rqnclGZukO6-UBmI_uUiBWCqs-73y64Gklr5UmLRZ3GV6WGhg9OrUoJkNy9L4WzEz3Wt-pJoVeqxfrvs4l8_12vcK_9o6NY4tGmzu2vegtbUJ2Ee0Z_8JNCPMwz5rTBcf3B4_0unthvNnTuoBIB5_set4aThAThUD8RIJVWaWMFctVrNcQv1VkaPWSAt_D3nAPK_9YzYkzaNkonzYKGwtJO_2tXbbFuIMJVKGUW31oY0nvGhZixMWcfMnQgCmBAzH0nK0mzzG8ulRt8EWKUhEmk9j4_slxp2ySOwt3LeZHqTlAyqLw9h3l7POXvXlj-bR91_lSIwhlBDqyVpsDXOj2yEGS7SwZO5MTLZeuFxL98vJNqkxlJAobkt-lUaP6Y4pYvD2G67PclblUHWyaDk-Du_8zoeKAcL37SyoLSpU83gvHKSbWGVvwoip6Lr2uyt9HLCZu-i8LKxJDm4f6yxsSwO3mzfS-Un_Tr4jvGc1Yo1Lkv1jUwIkztPluTQRE5NDX8NU3rqYdJR0Zv4oayykcjOm6JzLmWXPe8opTJP9cUhv_ohHVFpQ7sEfoiK-yAfbslbYm0K2Ircq3BRxrxm9koi7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00e25a504.mp4?token=pHJXgiQ0eZksqCPUqPwKOCQkUXw9PJZL7gmPj9AVw4IH3RxNuXbncUjJNou8nK_IorV9HCzrkpgpI35D4rqnclGZukO6-UBmI_uUiBWCqs-73y64Gklr5UmLRZ3GV6WGhg9OrUoJkNy9L4WzEz3Wt-pJoVeqxfrvs4l8_12vcK_9o6NY4tGmzu2vegtbUJ2Ee0Z_8JNCPMwz5rTBcf3B4_0unthvNnTuoBIB5_set4aThAThUD8RIJVWaWMFctVrNcQv1VkaPWSAt_D3nAPK_9YzYkzaNkonzYKGwtJO_2tXbbFuIMJVKGUW31oY0nvGhZixMWcfMnQgCmBAzH0nK0mzzG8ulRt8EWKUhEmk9j4_slxp2ySOwt3LeZHqTlAyqLw9h3l7POXvXlj-bR91_lSIwhlBDqyVpsDXOj2yEGS7SwZO5MTLZeuFxL98vJNqkxlJAobkt-lUaP6Y4pYvD2G67PclblUHWyaDk-Du_8zoeKAcL37SyoLSpU83gvHKSbWGVvwoip6Lr2uyt9HLCZu-i8LKxJDm4f6yxsSwO3mzfS-Un_Tr4jvGc1Yo1Lkv1jUwIkztPluTQRE5NDX8NU3rqYdJR0Zv4oayykcjOm6JzLmWXPe8opTJP9cUhv_ohHVFpQ7sEfoiK-yAfbslbYm0K2Ircq3BRxrxm9koi7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم آستارا در سومین روز خاکسپاری امام شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449177" target="_blank">📅 16:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449176">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTth42eJYw_qrsFqh6dL8fPHw_mIruXzyrNQFPYLE-p8A_YbmADsPobvVUFq2kISUDTwEkri4f7zgN8_VxpDO8GVDkd-gciy2RlaDgL7_xRcigRe6gZczCxla5s4dJPlXI0LaQdjbA99ZjeHdAwKSuQ_L78J8yO7PbYmLKMM1fyPcqm6h9UVlrQxEpYG08ED9K8tqfL2mPg98RBAA0XkiufABpVcKqq9_1oZzpZs2Hnsk5qMQNp0M-3v3yl3yyxRSVrHeXjEwHlWWkBpeDODvqaFTZYBC6j5q-WQ5trle4VrsjyGJ2K8HStaxRDVBLh8RVhAWrpxIIyxkR2uJNpJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: قاتلین امام شهید به سزای اعمال خود خواهند رسید
🔹
کوثری: ما باید به معنای واقعی کلمه بگوییم که انتقام ما از دشمن دو جنبه دارد: نخست، حذف کسانی که در به شهادت رساندن حضرت آقا و فرماندهان دستور دادند که این افراد حتماً شناسایی شده‌اند و مورد نظر مردم و مسئولان قرار خواهند گرفت.
🔹
دوم اینکه، بالاخره این کسانی که به ظاهر زندگی دنیایی اما در واقع یک زندگی حیوانی دارند قطعاً به سزای اعمال خود خواهند رسید.
🔹
ما بایستی راه رهبر شهید انقلاب را با صلابت و محکم ادامه دهیم و ان‌شاءالله خواسته‌های ایشان را که مسیر رسیدن به قله است، پیش ببریم  و عمل کنیم که در نهایت موجب رضایت ایشان گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/449176" target="_blank">📅 16:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449175">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=ailt0ln9uS6EEeyMXQqwHJNY6ptUL6stS3q8RxcV-MgrSjSWzk9nDOIudgmb9pN9DdHHzRFxalqwuLbdZHurRx8ggpXKtOQDg_yBY2CRtKirQ3ipEdatdJ5azPhXlsllO9o-LdPMpaCIWmeWIZyK6ZBeiaN6C-YqMmoj1yRP4nfH5LjZpajtM3L0uh6ht5jaK9DiVSSgKkVcfhD-OB0ty-QIZOym44ZRYVAUWcX6P0OOaEzRmA0eY1UTBnDVkZ5b0_mNL-tr49YPOrJfUquM8QWgPXo265ftTcLiVuW7WcRAp7C20U6ZTfqki6N9Cp_y5S5ZKXXVZY1sFNKacRQVzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=ailt0ln9uS6EEeyMXQqwHJNY6ptUL6stS3q8RxcV-MgrSjSWzk9nDOIudgmb9pN9DdHHzRFxalqwuLbdZHurRx8ggpXKtOQDg_yBY2CRtKirQ3ipEdatdJ5azPhXlsllO9o-LdPMpaCIWmeWIZyK6ZBeiaN6C-YqMmoj1yRP4nfH5LjZpajtM3L0uh6ht5jaK9DiVSSgKkVcfhD-OB0ty-QIZOym44ZRYVAUWcX6P0OOaEzRmA0eY1UTBnDVkZ5b0_mNL-tr49YPOrJfUquM8QWgPXo265ftTcLiVuW7WcRAp7C20U6ZTfqki6N9Cp_y5S5ZKXXVZY1sFNKacRQVzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی خاص از مزار رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449175" target="_blank">📅 16:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449174">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca96947bd.mp4?token=GcU3nMpnay0VyISCjRqamnMDfsW6El5cWGNBzq_WcVQPPCAAekil1t3VEaj0-w2gDAYhZ2CsqjsSyGc1xR56QTVA4h0LkQhRDsEje1Izf_QRzLLsqN_pYAbczGS1EBtai8I0rC71AhQF95lVrxPYUjGI5Qykn7fxMCwR--kVoES3lBiMcsBf2xQmiuD7YQxkDF9Q05_eoY8uUCcKfZa_elquvue7Jyws9r9NX9y_JwIlgCmXUQSyVzIzUmkWZpSnIg3vvcOwI-Xvf--qXeJWXyCwGJ52PtAawxQMEbMPf3T2VUzdSbaWaz3kyGK_qvU2qAG0vLqFMx6yhd0sr9dUiYGAb1Hehmi68jHHiJouva0_z0K3QSBIJOBvbkREFaVKebN4id7q9jAqDQpegmP2hgv5NjxmP9d9nW1yY_ySi8ou9Iygciox3Vz2thLGgZdKven599VotMOaHNDDXytLXbb05POx4TEwiPszemee0SbJ_23fkQOymh7yS-6gH91joUMGTSSXXwlqecHSnfohWGQ-kCwUHDxJGnH6K8KYLYL7mZre7d_qoKozUkAvO9JEwILtLqipwrKSd7itbDL7FBOJd6aSXjOP2U5shvJ5SvkKteylTs_K1DyirgQo3MtyW1rUXnmaosAQEMkyVU37ejOeo_gnf_CAZF4Btemjf-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca96947bd.mp4?token=GcU3nMpnay0VyISCjRqamnMDfsW6El5cWGNBzq_WcVQPPCAAekil1t3VEaj0-w2gDAYhZ2CsqjsSyGc1xR56QTVA4h0LkQhRDsEje1Izf_QRzLLsqN_pYAbczGS1EBtai8I0rC71AhQF95lVrxPYUjGI5Qykn7fxMCwR--kVoES3lBiMcsBf2xQmiuD7YQxkDF9Q05_eoY8uUCcKfZa_elquvue7Jyws9r9NX9y_JwIlgCmXUQSyVzIzUmkWZpSnIg3vvcOwI-Xvf--qXeJWXyCwGJ52PtAawxQMEbMPf3T2VUzdSbaWaz3kyGK_qvU2qAG0vLqFMx6yhd0sr9dUiYGAb1Hehmi68jHHiJouva0_z0K3QSBIJOBvbkREFaVKebN4id7q9jAqDQpegmP2hgv5NjxmP9d9nW1yY_ySi8ou9Iygciox3Vz2thLGgZdKven599VotMOaHNDDXytLXbb05POx4TEwiPszemee0SbJ_23fkQOymh7yS-6gH91joUMGTSSXXwlqecHSnfohWGQ-kCwUHDxJGnH6K8KYLYL7mZre7d_qoKozUkAvO9JEwILtLqipwrKSd7itbDL7FBOJd6aSXjOP2U5shvJ5SvkKteylTs_K1DyirgQo3MtyW1rUXnmaosAQEMkyVU37ejOeo_gnf_CAZF4Btemjf-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم ایران به ادبیات توهین‌آمیز ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449174" target="_blank">📅 16:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449173">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ffca2e91.mp4?token=qQnx7gTTNSMAAlf63-h2hHtQvRz2u2Udp0o-fBdBI8hsxqMQjBwv_BhRNm1og8vx78EWarL0559qn0zurUrYUVLTjzrzkb4Uih97mFczo8g48MMZY0rg5GUADuIES1Aonn1QU0jywIk_Q7GIxCDRFYPcR-Ki1hc_MdjnZD7qm62qT9G6qVbSJ5rumHfvMPdvq9-Dnxiadk4Xqlb0h9ZvF6aTB8MWRU8pFvfP-7Fru5Y8mL874tjr6czfrhtchw9GJEIgmO3aoVdAJjCn_DGmgi-5GSJXyv85IWXh8TBUAkpKdUiJudg1wCZON6vIP1mygRyE_XLIoUNF1-tWBQMXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ffca2e91.mp4?token=qQnx7gTTNSMAAlf63-h2hHtQvRz2u2Udp0o-fBdBI8hsxqMQjBwv_BhRNm1og8vx78EWarL0559qn0zurUrYUVLTjzrzkb4Uih97mFczo8g48MMZY0rg5GUADuIES1Aonn1QU0jywIk_Q7GIxCDRFYPcR-Ki1hc_MdjnZD7qm62qT9G6qVbSJ5rumHfvMPdvq9-Dnxiadk4Xqlb0h9ZvF6aTB8MWRU8pFvfP-7Fru5Y8mL874tjr6czfrhtchw9GJEIgmO3aoVdAJjCn_DGmgi-5GSJXyv85IWXh8TBUAkpKdUiJudg1wCZON6vIP1mygRyE_XLIoUNF1-tWBQMXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الجزیره از حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در شهرستان صور در جنوب لبنان خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449173" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449166">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZ5yQ8jEiqU90P6y6OwjVveyTps_9hV74BEtlEUVcrn_u00c75hjXzd_dwDPKuh77aeRXxvChLdgpWkz7oEBtBeh_Nuiq2KBHlNhozU-q3euE8cWwaxY4J68QiVrmnBWRiBj4mPL8uE1BqgGWSq2F0RzD-CtTmibcl18fJHOqkHv7yJwT2die70FrLkakhrDEwz28t-pa47QRSs1lQgIFdYsDJK32lg41kTbsDsenW0SxOq8eZ-MctVHhEEiPVSxj6oi8TDVCsE3N21UBGMItI6CYXcmFZPBLfrxJRz_uwdNLHqWzpnCsGDJd2HMjgvEljB4QdBJXykq0nqogttadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYbnr2o4v0uIP-lVMxMw8prxKyOulVqkEWzCUnMQRd2ZmThhw3zS8eVfUVcDwIfogXLZv3GD-M7zMzpXDABaHEyTRrZ-KiM0glEbv54fayt8v83mTIFNBq82_xQxcI5n18ZG8TfLeSMiTk43Glk74TstwClPnARC7p3Cpfj4hJQTdSa6sThndyjmCpvzK09MspGMGzlPSwD9RHRiw7zwwiY9Y7p_oCQ9QX-NB-dTP0JMeJLZPPm6hoDT8wro3bIK4i-SbG3_4CO1QU5x1qFu1Fug7B24GFeKuItUsjHvS2JmB-AE_Gay3iVG-RBEGygB1H753wX-EJ9O62oMoqZDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmXDrV9t4EQSm7xXpz4HXITXht2Isq_6qTSHsNW-1SFd20uwDTV7pl5gusKagMHgYUBlys2OkfdDDHzZScdaP2gvQDA3iPX33xVjC6qa4y1FPSfuduyjkYZJpe6e2sM-njc7Ccsb5czcyCdmR-y2tfdXxgwlyNCN-JPtRNcCsLWVrlHOIP1N-vUNrqSuoUZIeupAUD-47-FZ1jhGh6er1re3S8R0Z2NWRsxVrt9UY2aRlaJ9DRhC1NGQESG9p4I7Nw2PxhFoo0UhKjd6cevkgaTxX5vE0qKWGD11w5kOgjS7d9s8xHA5Kop_8PfEo69XjYnAZIZo7A8VLqVHITEeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUxR2CzeE3ty5YirmlTeeM1Cfk_5LWhzMEJ88FvQT4JgP0Hh4zvMxtntmWmcvRurQOLIT80qzLfLve1E4I3ly9ZXppNeLVkjA39vbW7tYKWg2Gp06ZN8vGAFoEzzPx4PytV9F7fY5akY-2fc7P2zbUn4NJ0zSY1I4uWCpX5IX4eLv0ZpiISICC67u4SmeXonk0iX0PEn2CyksfWj0SbAf-ijuw1AuTvFk2liMjbeFIHECN7PIBrtYdXhcJLz7Ld3gCHSP0ULTyMfml762CdON0EVkqmITo-5fryvfvPNzHfVoJJHkfMSFiAhiZpPDXMREkOfZAOk6f7V4QbC_2AEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI2D5OQgjOsu9reLK8ouYaTj4l-7G8sFh-oGhJVTJ9qcyicXeu9UMY2ffZ7HY0cPmeFcYrDIoWCBpJC525DN6cGrvrE7xNlaGjIxRhILdATE2IqAllBhC5nsnNb0qcOXIesXQ-eB3MVzTUXNdMInoRECaycGrDdDN9M1HHGlh6-TwenfRwXkQY6iAwk-ckEgIdHIGWiZxcneGLpOtnN0yY9TMuP3Ijx41mNZyIJXy4wQ9ll0UWKVMcgPTguaS3MG-ZRKPPzAChPizkzGgMj4mLeELlW00tmlIlk4uP9f0Cb4AYnLCp65b7lwIUCk02OMd8LCIoCaUnTKaG8le6FHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqaGBQ4FHVhcqcgFPrUGdXOxKyVtaht6fGoVKtb_sSTQb6URp01hbu70L5Hxx_b2dNlVjFXi4sxOwAoQv3Yyc9StdkNZPMBH4yHOGSn0z6ofr6Qq0grD5zIneRa979sQrtRon31-qcfq8ug6dRdGdIm70qUCIYuhomfidR9S2CCKIrbrc5KcL_MLeBwc122nj_vSIk4jPrfZogHHe74HwqpCotJpXZWTw3vHSShGF1Gv05OQg1QIiekcuJT3Tfi-QZUZC6KbAQy5g8Ad_AiVZl552WINKE7WqPwLVu8HuNggs2WIax8HuxpoN_5VnIF8nX0ikAWHxEqRkOOXE6RwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNx2bHgZDfNLbKUkztp0bPX720j1qt7EoDLBIbI9KICDnJqNqvy8EguO4bkdeWPFr6ApAmVlWw4hxxvvJoyy7qJ3_L0pRVlGYU04PcJrnu1WRzVviRYjPoJpLPDo_c72N3H4jQoKiWg2Q4CiBMjeJcUNGq9ysi3v7yYcQlz8mmZS4wCOP27x6zMr8Z1TgR5rYCtChPsTTyGblACZ43vylNaG-yVF3VvulLIgCrj65SgWuqlIBw8EXaeOJ0_9EiZl2luvz5HRquyrJxGAe9v7m51_d7UkP6uKa03jV4ASAtCH_q-hL5yNB4rlTb8lr3IfuqeMhOnNyGEiEJlpi53hzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت قائد شهید حضرت امام خامنه‌ای در مصلای تبریز
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449166" target="_blank">📅 16:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449165">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ceeacc63d.mp4?token=f2UdxAx9sSYNSJMfugSQIO3di_cPE6pAwQbaCrmCbM9uOgbkEu6XUNlqh2DEIj3Ba5HFiMlZWg8ieQPtTfRWs6TrXYYFAHGA3GYs9Ic4q7IvOYZMj0Xc2WUVNXMfjtF-EEpEOuhK62MyY0xmYQ27I9SydNyMUGHd308o_Byz-iccKflyi2Br2SzrbIJYIcU_zI422P8c5vh49B805gCIK2duzCv-Y6afvC_pjUWWUxD1rVWU9LrNfUYkiRvQtRSKzlhYv_xmqb3ELHgDYB20YtP63_5s1Adndkuckz5xBnXoSwRMHO6eBGt8T844fA6zMR_dTNHZHn3Ah88hAKTMmE6cKHiSWC7SGsSDsEIquGvQ-TbglAo3erIWyEkBr6j_NpxSSa040NmrYm_hVZHTv1DuE_P-u9NjIaFmqFGa-Ram1vy2McMKX-ad1xB3qD4o0jFF2qrcmpOR-DYH9wIGazgMAg8jJdf_c-kx14546nL0utFGpn7qXGNI59vnRjtVwpHw7_b3bGLa_m02ol6_MGL3kAhEGJSTaNxDNDPxZves3cyLGI7lRr1txyBIRmDUDMeortcn2Qfepv2HP7mlrmp1pcFg7Vk_K3FLZzD5VJYnAEoF0A36zbHh5IlhRAy1Zm1aTAJCIs_mFXQpfsvh1Zkv4gFKwkFJ9Tkv3z3F_PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ceeacc63d.mp4?token=f2UdxAx9sSYNSJMfugSQIO3di_cPE6pAwQbaCrmCbM9uOgbkEu6XUNlqh2DEIj3Ba5HFiMlZWg8ieQPtTfRWs6TrXYYFAHGA3GYs9Ic4q7IvOYZMj0Xc2WUVNXMfjtF-EEpEOuhK62MyY0xmYQ27I9SydNyMUGHd308o_Byz-iccKflyi2Br2SzrbIJYIcU_zI422P8c5vh49B805gCIK2duzCv-Y6afvC_pjUWWUxD1rVWU9LrNfUYkiRvQtRSKzlhYv_xmqb3ELHgDYB20YtP63_5s1Adndkuckz5xBnXoSwRMHO6eBGt8T844fA6zMR_dTNHZHn3Ah88hAKTMmE6cKHiSWC7SGsSDsEIquGvQ-TbglAo3erIWyEkBr6j_NpxSSa040NmrYm_hVZHTv1DuE_P-u9NjIaFmqFGa-Ram1vy2McMKX-ad1xB3qD4o0jFF2qrcmpOR-DYH9wIGazgMAg8jJdf_c-kx14546nL0utFGpn7qXGNI59vnRjtVwpHw7_b3bGLa_m02ol6_MGL3kAhEGJSTaNxDNDPxZves3cyLGI7lRr1txyBIRmDUDMeortcn2Qfepv2HP7mlrmp1pcFg7Vk_K3FLZzD5VJYnAEoF0A36zbHh5IlhRAy1Zm1aTAJCIs_mFXQpfsvh1Zkv4gFKwkFJ9Tkv3z3F_PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرداری که ۲ بار شهادت را تجربه کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449165" target="_blank">📅 16:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxuGtCizOqAGBv475R_8F8S1FgJxL1_4S8tapY0PK0qBBHnFC3qTSIyM_HQ5mvNi7aevdgOc2Ao4C68sYxd2hdzevMcU5Demhbj530xWzug2FOOTR2Y8n_FQAuV_BcBy33RWTMT0mMcGaM99LFYRhLesLndGrPu2_yO7W8Ug1Eu72JZ06tQsl4rmZngDw-JB-jI8J5eDM8GKDqSd3XaGRITrNfdM71QAy_M2u43KeLUBMEjiI75UMdpnMA71yOSLvQtdi8RHZLMT0prYLC0wZv6fPdoc0OFYENXN6UCCbtkXmaJFIWKGIYQ4esEVix4lLHI1M8BRKw6epG3NWkIRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌ثبت‌نام حج ۱۴۰۶ زودتر از همیشه آغاز می‌شود
🔹
معاون سازمان حج و زیارت اعلام کرد پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از یکشنبه ۲۱ تیر آغاز می‌شود.
🔹
در مرحله نخست، فقط افرادی که در کاروان‌های حج ۱۴۰۵ ثبت‌نام کرده‌اند اما موفق به اعزام نشده‌اند، امکان ثبت درخواست دارند…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449164" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd03739e4b.mp4?token=eBXznTEpFaMwwrewNJZTNYQYgT8KKdB9_fuzf8pRL-pE9-STSrVAgALZRPxV5FU4DHRIwgm2sNOv4BGIswPGSgXHPSVBpuoc1aiJDRHAxQKVurX1BcGW-_699IsIEnmwcd3CHVgd9psEAAMzW9BHdxOHBbNcamFYEBRWaWeK82AaJsH2vK0iQxplchupnojQXtmj11VrFTy2AyeqSdQhnChah6I00-8z3c5IhO9G3dZGrLmE254j9BNGZILJQnr0kXMGpBVxpMVcl3Qp2h-hHW3iCMVokt3WZ4ZCMIGJPTbYpEJe7Jl-8QmVcndZmGaK-9Ps8gXh4ZQ5YeEPVZ12xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd03739e4b.mp4?token=eBXznTEpFaMwwrewNJZTNYQYgT8KKdB9_fuzf8pRL-pE9-STSrVAgALZRPxV5FU4DHRIwgm2sNOv4BGIswPGSgXHPSVBpuoc1aiJDRHAxQKVurX1BcGW-_699IsIEnmwcd3CHVgd9psEAAMzW9BHdxOHBbNcamFYEBRWaWeK82AaJsH2vK0iQxplchupnojQXtmj11VrFTy2AyeqSdQhnChah6I00-8z3c5IhO9G3dZGrLmE254j9BNGZILJQnr0kXMGpBVxpMVcl3Qp2h-hHW3iCMVokt3WZ4ZCMIGJPTbYpEJe7Jl-8QmVcndZmGaK-9Ps8gXh4ZQ5YeEPVZ12xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع لبنانی از ۲ حملهٔ پهپادی ارتش صهیونیستی به جنوب لبنان خبر دادند  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449163" target="_blank">📅 15:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQfnrdTz4Y-hEig5Y9xgjGV89y90gAjrUXzTkIvsVb32h-lWKNavYXj9VvaFh-w7BQCSo-pJfXaz2u3eMyk_uRGPUv8SSbHH6N0JogQKslYUrvcbq3gwMx-057LedwKgiMGymGBgg76H1xDeVSMW36NfizfbAYGX7FEuoQEHaca_MA7gX8-c-Jd8DJWyDSyTuzC8xDB-_61VEngV1ugozjC3GDx311403ZcH98Tt2Zbcpf30StAaN8XR3A0tllMNulv4iIgDDtpK8dbOV65AvPT7BKNqOue7iKs6hKnw2ZdDO03B8bgL4OLqhR9guiVaGDHB5YsCg-PeeXsOEdCOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و شرط دریافت ارز اربعین اعلام شد
🔹
به‌گفتهٔ دبیر ستاد اربعین، توزیع ارز اربعین از امروز آغاز شده است و فقط زائرانی که در
سامانهٔ سماح
ثبت‌نام کنند می‌توانند تا ۲۰۰ هزار دینار عراق دریافت کنند؛ نرخ دولتی هر ۱۰۰۰ دینار برای زائران ۱۲۰ هزار تومان تعیین شده است.
🔹
متقاضیان می‌توانند با ثبت درخواست، ارز خود را از بانک‌های ملی، ملت، سپه، شهر، گردشگری، قرض‌الحسنه مهر ایران و پست‌بانک دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/449162" target="_blank">📅 14:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449161">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiZrGYVAAld6iIZrKDZkMfKaRdpd8DIKb6GOAgpxiKdq11nMxMJA0lj93Qc30ClDlyNNh8wOabK2UC_0hj9ccLndSn8T9-ckd1tKUDnfjeJNvHgh218DCukziZmyukcUIyaulBJhdkgBHF_7n1cLrdyQOXWlOh_w9Nm6UNbLECxk0wgAUWTz8ug3kMCMC03jUdWp7t1NCjIdDYAz6MVfMsHLcI4Y9BkjYkGTDdDIQ33zRTs-v7kuuMMrA5C4nRVJ1yEK60X011asZZqzkH8dwnE1fqgBv9PXTHU4v5sGHxFxt-I7Tx8YiXmJpgsKAjE_rvzJzm0P3IC0Di5d2Wf7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی پایگاه اطلاع‌رسانی رهبر معظم انقلاب
🔹
پایگاه اطلاع‌رسانی رهبر معظم انقلاب، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای راه‌اندازی شد.
🔹
مردم می‌توانند با مراجعه به نشانی
Rahbar.ir
به تازه‌ترین اخبار، اطلاعیه‌ها، پیام‌ها، بیانات، دیدارها، تصاویر، ویدئوها و سایر محتوای مرتبط با رهبر معظم انقلاب اسلامی دسترسی داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449161" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449160">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b36056a2b.mp4?token=PRogxiXjvf9iepWV_iJSk0fmZmL4vDRclEFhDL3Fm0rFETyG-2Sroiw5DjBr0eaDuOvt0rDXdC1jdCYvr1jRfEcGIRaRbwMDq-a7yfdgbt90f58uedYfqTEzwpa1NTwh7BN2DNAVlrYEArbPZ7bX8TrnqHE9D3njCixSdSDhPsrCR5LeyB5rvPBL-pbdxKgBzu255Nmel28YC7FBGWqtwM-J4l5hF_pQ0WDCNv242ys0gPhYboyLsQIj-XUkno2rsOjxwHA2fYMNtRSNGD8Nn5R8WcsS_tT6t_OTMf1pU6jdl4Tay5V0A3qhB5YKwNVf5zxx661wOroUoxUaAlohdEmsLbOSdOQzsOIypxN4NYUvpg_x9Xdh-D1gNRh8TGd8Itw8DH49-iRbMPVjkM8LPHvvzeRaiX1_jugyqWb70NRY3QBb5FhGYOe0kpnOEcmOeQHUeSwVQDg6mGwGZOcwhhNksV9SP25F9S9C-o_R-1CozRQM3Q46EpXPn6wttUyC53NGZfKgwbOZadn72MKp008dX40pLuhSvxgtUdR4a3PVxd_yVFP5maGR3vFV77tIejISx5hYEfSrm7ZLIXSfm-QZgRhkefjAalAYgo92MhaeiYBk6b24nu2p5OhWPoFrbN9JvTeyi2i_-bz5O-tj_aQRQC79Uvay1WkqxsQ8s4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b36056a2b.mp4?token=PRogxiXjvf9iepWV_iJSk0fmZmL4vDRclEFhDL3Fm0rFETyG-2Sroiw5DjBr0eaDuOvt0rDXdC1jdCYvr1jRfEcGIRaRbwMDq-a7yfdgbt90f58uedYfqTEzwpa1NTwh7BN2DNAVlrYEArbPZ7bX8TrnqHE9D3njCixSdSDhPsrCR5LeyB5rvPBL-pbdxKgBzu255Nmel28YC7FBGWqtwM-J4l5hF_pQ0WDCNv242ys0gPhYboyLsQIj-XUkno2rsOjxwHA2fYMNtRSNGD8Nn5R8WcsS_tT6t_OTMf1pU6jdl4Tay5V0A3qhB5YKwNVf5zxx661wOroUoxUaAlohdEmsLbOSdOQzsOIypxN4NYUvpg_x9Xdh-D1gNRh8TGd8Itw8DH49-iRbMPVjkM8LPHvvzeRaiX1_jugyqWb70NRY3QBb5FhGYOe0kpnOEcmOeQHUeSwVQDg6mGwGZOcwhhNksV9SP25F9S9C-o_R-1CozRQM3Q46EpXPn6wttUyC53NGZfKgwbOZadn72MKp008dX40pLuhSvxgtUdR4a3PVxd_yVFP5maGR3vFV77tIejISx5hYEfSrm7ZLIXSfm-QZgRhkefjAalAYgo92MhaeiYBk6b24nu2p5OhWPoFrbN9JvTeyi2i_-bz5O-tj_aQRQC79Uvay1WkqxsQ8s4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف طولانی زائران حرم رضوی برای حضور بر سر مزار رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449160" target="_blank">📅 14:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌ رهبر انقلاب: امید داریم آقای شهیدمان حضرت بقیة‌الله را همراهی کند
🔹
شما ای سرور عالی‌مقام! ای بزرگو‌ار! ای امام رئوف! یا اباالحسن الرّضا المرتضی که برترین صلوات خدا بر شما باد، اکنون جسم پاره‌پارهٔ خادمی از خادمین حضرتتان و عترت طاهره، پس‌از سال‌ها جِدّ…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449159" target="_blank">📅 14:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌ رهبر انقلاب: عهد می‌بندیم از جنایتکاران انتقام بگیریم
🔹
ای قتیل مظلوم! ای مظلوم سرافراز! ای بندهٔ صالح خدا! حال که با چشمان اشکبار و دل‌های شکسته با پیکر شما وداع می‌کنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم و آن طریق مستقیمی که شما ترسیم کردید…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449158" target="_blank">📅 14:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ رهبر انقلاب: ای پدر شهید امت! نوشیدن شهد شهادت که عمری در آرزوی آن بودید، گوارایتان باد!
🔹
پوشیدن خلعت شهادت با بدنی که نشان‌ها از مادرتان زهرای اطهر و جدتان اباعبدالله الحسین و ابالفضل العباس علیهم‌الصلاة والسلام دارد، مبارکتان باشد.
🔹
و شما ای همراهان…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449157" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌ رهبر انقلاب: آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک.
🔹
سلام بر امامی که ندای حیات‌بخش…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449156" target="_blank">📅 14:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ رهبر انقلاب: آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک.
🔹
سلام بر امامی که ندای حیات‌بخش…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449155" target="_blank">📅 14:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449153" target="_blank">📅 14:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/farsna/449152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449152" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تشکر رهبر انقلاب از حضور تاریخی ده‌ها میلیونی در ایران و عراق
🔹
جا دارد به همین مناسبت از حضور ده‌ها میلیونی، اعجاب‌برانگیز، دشمن‌شکن و تاریخی مردم در شهرها و روستاهای ایران و عراق خصوصاً تهران، قم، نجف، کربلا، و مشهد صمیمانه قدردانی میکنم. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/449151" target="_blank">📅 14:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhVtJ5NqdonIvZF2P8vYCRdhcDU__62967bk9hI2xj1wwuXoOqfFhJ9vyFNiEIMD2k252zikDqVdx8R0O9qx9zUnQPG00cM8B7iFkd5ddPk5hEfDR_p_y0Ml_xKzKiN7usPzTJs0NkqZnX8LL6-Vmnq_MSse3by-H-ouCmI1fU1Zqkb9CV2u0nP67vwxfTUXRA82G-NhsAPkJVY3t01FbcpK72I-cmG2DL_em3N9Xzpx7cEF3_2enye1dLfz6y0e4MaCQbk2A-_kzn5ltbYaae3Rk7vzPLAmloUAWYd949ilSveGXYF2ZuWxStFe5IxOEobn7CDntySkEEryO1KbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: عهد می‌بندیم که انتقام خون پاک رهبر شهید و همۀ شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449150" target="_blank">📅 14:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام مهم حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب اسلامی به‌مناسبت تشییع و تدفین آقای شهید ایران منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449149" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
هواشناسی: طی چند روز آینده نواحی جنوبی کشور دمای بالای ۵۰ درجه و تهران دمای بالای ۴۰ درجه خواهند داشت
🔹
شاخص اشعهٔ فرابنفش نیز افزایش خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449148" target="_blank">📅 13:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a458db9dec.mp4?token=aN4doTRf11yCFonzok8GgcN41Juc0rwO_dAaaMC-R-TeQyE43_55yBV9m2LsbNDHPXctpd6qHZTRsurO6PO27mXaZpkN0iC3FZQgDaD60usiQy9kpT1tzApI5X5-H558ksCwqHx4qHN7XMQCFu9gdWhZ4gfcBxeJ9RQb-dWo7q5TfdBREKIDcgwWI5V6HTOQnRp8vqsflurGKis1eywM2T8HsE32xsEHzkcabq657xTol0Rrrw97AT0Ei-QMhgmw1Qjjo6Mj-mrpyA92gHrbVNHR-zzGRaUDuqIu1upkPuB4iPTP7ITghPJH_8OH2S6fLuwab2xv58S4NdHSyWBcT4HQzDAP1yL_ByjMGf3QR4yfLalFsVZ_3TOIxL4zCng3pPJyCRA3EvqFKlhWn6npBPlQyYRXchVh92FsDVRTafPCO738ClbMH514pLKd9GkOvTW3p5_evGFOlgwfvFXryEJAQT7KcTMb1qSTTRAInnw0oOsMUdrDUF8OrvUnLHNNAQbFnRwMlAu7CVIWblsZHvKJ0_IXX27X--snjWODN0A0FwXVaNsXV49vTTM1gk5TM_u_Gkvlo6wPPOrzjwgWZmKG_lsblZFOZvWakV3ZL3jNOfNc-2HzjnYGrx8k1EYiz1PIvtg8-ODMKiqlydRPF0-Vp15AxTuqFgpItES2s_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a458db9dec.mp4?token=aN4doTRf11yCFonzok8GgcN41Juc0rwO_dAaaMC-R-TeQyE43_55yBV9m2LsbNDHPXctpd6qHZTRsurO6PO27mXaZpkN0iC3FZQgDaD60usiQy9kpT1tzApI5X5-H558ksCwqHx4qHN7XMQCFu9gdWhZ4gfcBxeJ9RQb-dWo7q5TfdBREKIDcgwWI5V6HTOQnRp8vqsflurGKis1eywM2T8HsE32xsEHzkcabq657xTol0Rrrw97AT0Ei-QMhgmw1Qjjo6Mj-mrpyA92gHrbVNHR-zzGRaUDuqIu1upkPuB4iPTP7ITghPJH_8OH2S6fLuwab2xv58S4NdHSyWBcT4HQzDAP1yL_ByjMGf3QR4yfLalFsVZ_3TOIxL4zCng3pPJyCRA3EvqFKlhWn6npBPlQyYRXchVh92FsDVRTafPCO738ClbMH514pLKd9GkOvTW3p5_evGFOlgwfvFXryEJAQT7KcTMb1qSTTRAInnw0oOsMUdrDUF8OrvUnLHNNAQbFnRwMlAu7CVIWblsZHvKJ0_IXX27X--snjWODN0A0FwXVaNsXV49vTTM1gk5TM_u_Gkvlo6wPPOrzjwgWZmKG_lsblZFOZvWakV3ZL3jNOfNc-2HzjnYGrx8k1EYiz1PIvtg8-ODMKiqlydRPF0-Vp15AxTuqFgpItES2s_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
صف طولانی زائران حرم رضوی برای حضور بر مزار مطهر «آقای شهید ایران» در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449147" target="_blank">📅 13:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=drbQ6BuCv7Aj4L7JUMp_bLSLGhsnzNOZLJO3fQKt5LCur2F5a417vYyvKVUTuDEhhdBMbPQMX2KQ3P9DSp8I5qlXNUdGkQQcoQpXM9JOUE4Z6cId6buUx3KjIpHo_hFNg6lWuSMP9D1UsTxGR3SKgEuOT-if-cXm3d7fltivoW_jOo0AssGVnroBkoeuGPgJSJtylHqaik7SDqTNaUBAdwRQHWrj3rXlKj0ebTNfJoab5G3GCf9MH96a0-w8lC-3ulFmSGeFi8onbxjcxP8AO2n25MC9zrmSvMYCR9f2ckPMamcTFD0wYY6OMmFwcxPSPY2ZPPcZ9PNXxykZTBTyJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=drbQ6BuCv7Aj4L7JUMp_bLSLGhsnzNOZLJO3fQKt5LCur2F5a417vYyvKVUTuDEhhdBMbPQMX2KQ3P9DSp8I5qlXNUdGkQQcoQpXM9JOUE4Z6cId6buUx3KjIpHo_hFNg6lWuSMP9D1UsTxGR3SKgEuOT-if-cXm3d7fltivoW_jOo0AssGVnroBkoeuGPgJSJtylHqaik7SDqTNaUBAdwRQHWrj3rXlKj0ebTNfJoab5G3GCf9MH96a0-w8lC-3ulFmSGeFi8onbxjcxP8AO2n25MC9zrmSvMYCR9f2ckPMamcTFD0wYY6OMmFwcxPSPY2ZPPcZ9PNXxykZTBTyJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع لبنانی از ۲ حملهٔ پهپادی ارتش صهیونیستی به جنوب لبنان خبر دادند
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449146" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جلسهٔ علنی مجلس فردا یا پس‌فردا برگزار می‌‎شود
🔹
به‌گفتۀ یکی از اعضای هیئت‌رئیسۀ مجلس، در هیئت‌رئیسه تصمیم گرفته شده که جلسۀ علنی مجلس به‌صورت حضوری، یکشنبه یا دوشنبه برگزار شود.
🔹
به‌گفتۀ او، تصمیم نهایی تا ساعات آینده گرفته می‌شود و به‌صورت رسمی اطلاع‌رسانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449145" target="_blank">📅 13:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منبع آگاه: مذاکره تا عقب‌نشینی آمریکا از مواضعش منتفی است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس: گزارش‌های منتشرشده در برخی رسانه‌های نزدیک به رژیم صهیونیستی درباره درخواست ایران برای مذاکره با آمریکا کذب است.
🔹
جمهوری اسلامی ایران هیچ درخواستی برای مذاکره با آمریکا ارائه نکرده و هیچ مذاکره‌ای نیز تا زمانی که طرف آمریکایی از مواضع خود عقب‌نشینی نکند، انجام نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449144" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaKrwgyI0aWTi50T2PLS6OSETi5L-gpG08nGlO97fpl9A3HDvpP1TQibKR_QDqvE5dQoDUKaFPmwrJVBkES1qbMJ6ebgwpf8vqYUf4GjlD9T6dJmVDxTVMuwZftslryQQaFY_wRgrD6L2gTDRF8FqXuNTxbki4cklNpSM6s6oifIX8N_o6xn8E5XW1rbM-8_71_m1j7i0AzbffrVD9hQvX1AqhVx1dfVAlfvrP0pZ-XIslQGnEXQ4xdxQCBCLz19MfbXLgT0wd4U7bti49P6dvu2t0kQbzrQx6yQ7nKuFVtkLE4g_lFw99xSqfDJiyh9TjCxD1ZttXA3vjPpBx1NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در مسیر لاریجانی؛ لانچر جنگ شناختی دست کیست؟
🔹
این روزها مردم ایران حق دارند خشمگین باشند. جنایت‌های آمریکا و رژیم صهیونیستی، شهادت رهبر، فرماندهان، دانشمندان و هم‌وطنان عزیزمان و اظهارات گستاخانه ترامپ، احساسات جامعه را جریحه‌دار کرده است. از سوی دیگر، بسیاری نیز گلایه دارند که چرا مسئولان به اندازۀ کافی به جنگ رسانه‌ای دشمن پاسخ نمی‌دهند و روشنگری لازم را انجام نمی‌دهند.
🔹
این مطالبه، مطالبه‌ای طبیعی است؛ اما نباید یک نکته مهم را فراموش کنیم. در میدان جنگ، همه یک مأموریت ندارند. فرمانده، نیروی اطلاعات، دیپلمات، رزمنده و دیده‌بان هر کدام وظیفه‌ای متفاوت دارند. اگر هرکس از روی احساس، مأموریت دیگری را بر عهده بگیرد، آرایش جبهه به هم می‌ریزد.
🔹
دستگاه دیپلماسی و نهادهای امنیتی گاهی به دلیل ملاحظات عملیاتی، نمی‌توانند همه واقعیت‌ها را بیان کنند؛ چراکه دشمن نیز رسانه‌ها را لحظه‌به‌لحظه رصد می‌کند. حتی ممکن است در برخی موارد، ضعف رسانه‌ای، تأخیر در اطلاع‌رسانی یا بی‌توجهی مدیریتی نیز وجود داشته باشد. مسئولان معصوم نیستند و خطا در هر مجموعه‌ای ممکن است رخ دهد.
🔹
اما حتی اگر چنین ضعفی وجود داشته باشد، راه اصلاح آن، توهین، تخریب و برهم زدن آرامش جبهه خودی نیست. این ضعف را می‌توان و باید نقد کرد، اما نقد با اهانت و هیجان‌زدگی تفاوت دارد.
دقیقاً همین نقطه، میدان جنگ شناختی است.
🔹
دشمن تلاش می‌کند خشم مردم را از خود منحرف کند و آن را متوجه مسئولان و نیروهای داخلی سازد. اگر بتواند میان مردم و مسئولانی که در خط مقدم دفاع از کشور قرار دارند شکاف ایجاد کند، بدون شلیک حتی یک گلوله به بخشی از هدف خود رسیده است.
🔹
امام راحل و رهبر شهید بارها بر صبر، بصیرت و حفظ وحدت تأکید کرده‌اند. تجربۀ برخورد با علی لاریجانی نیز نشان داد که گاهی فضای هیجانی، قضاوت‌های نادرستی را رقم می‌زند و بعدها بسیاری از همان منتقدان از رفتار خود پشیمان می‌شوند.
🔹
امروز نیز افرادی مانند محمدباقر قالیباف و سیدعباس عراقچی، فارغ از اختلاف‌نظرهای سیاسی، در صف نخست دفاع از منافع ملی قرار دارند و در صورت هرگونه اقدام تروریستی یا جنگ، جزو نخستین اهداف دشمن خواهند بود. ممکن است درباره روش‌ها نقد داشته باشیم، اما نباید جای رزمنده و دشمن را اشتباه بگیریم.
🔹
امروز مأموریت همۀ ما، شلیک موشک نیست؛ اما حفظ انسجام جبهه خودی، مقابله با شایعات، کنترل خشم و جلوگیری از دوقطبی‌سازی، بخشی از همین نبرد است.
🔹
در جنگ، رزمندۀ پشت لانچر اجازه ندارد از روی عصبانیت و بدون اطلاعات شلیک کند؛ چون ممکن است نیروهای خودی را هدف بگیرد. در جنگ شناختی نیز زبان، قلم و صفحه تلفن همراه ما همان لانچر است. هر جمله‌ای که از روی خشم و بدون دقت منتشر شود، اگر جبهه خودی را تضعیف کند، خواسته یا ناخواسته در زمین دشمن بازی کرده است.
🔹
خشم مردم سرمایه‌ای ارزشمند است؛ اما این سرمایه باید دقیقاً به سمت دشمن اصلی نشانه برود، نه به سوی کسانی که با همه ضعف‌ها و اختلاف‌نظرها، در خط مقدم دفاع از ایران ایستاده‌اند. از همین رو، اگر نقدی هم داریم، باید مسئولانه، منصفانه و در جهت اصلاح باشد، نه به گونه‌ای که آرایش جبهه خودی را بر هم بزند و دشمن را به هدفش نزدیک‌تر کند.
🔹
در پایان، نباید «دیپلماسی در میدان نبرد» و «اعتماد به دشمن» را با هم خلط کرد. مسئولان کشور بارها تأکید کرده‌اند که اگر مذاکره‌ای هم صورت گیرد، آن را بخشی از مدیریت میدان و «مذاکره در شرایط جنگ» می‌دانند، نه مذاکره‌ای از جنس اعتماد، سازش یا رابطه برد ـ برد با دشمن.
🔹
متأسفانه برخی اظهارنظرهای نسنجیده از سوی بعضی جریان‌های سیاسی که عقب‌نشینی و امتیازدهی را راه‌حل نهایی مشکلات معرفی می‌کنند، این دو مفهوم را در ذهن افکار عمومی درهم آمیخته و زمینه سوءبرداشت را فراهم کرده است.
🔹
درحالی که هم آموزه‌های قرآن کریم و هم تجربه تاریخی ملت ایران به ما می‌آموزد که به دشمن نباید اعتماد کرد و گره‌های اساسی کشور با تکیه بر اراده و توان داخلی گشوده می‌شود، نه با امید بستن به وعده‌های دشمن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449143" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تحلیل داده‌محور از اجرای تفاهم ایران و آمریکا؛ یک گروه دانشگاهی «تفاهم‌سنج» را راه‌اندازی کرد
🔹
گروهی از پژوهشگران و متخصصان دانشگاهی، سامانهٔ «تفاهم‌سنج» را با هدف ارائهٔ تصویری شفاف و مستند از روند اجرای تفاهم ایران و آمریکا راه‌اندازی کرده‌اند.
🔹
به‌گزارش فارس، در شرایطی که روایت‌های متفاوت و گاه متضادی دربارهٔ میزان پایبندی طرفین به توافقات موجود مطرح می‌شود، این گروه دانشگاهی با اتکا به روش‌های آماری و داده‌های مستند، امکان سنجش عینی‌تر اجرای تفاهم را فراهم آورده است.
🔹
در این سامانه، هر خبر یا رویداد مرتبط با اجرای تفاهم، ابتدا به‌عنوان یک «شاهد» ثبت شده و براساس ۳ معیار اعتبار منبع، کیفیت مستندات و میزان ارتباط با ۱۴ بند تفاهم ارزیابی می‌شود؛ سپس با استفاده از یک مدل آماری مبتنی‌بر تجمیع شواهد، میزان تأیید یا نقض هر تعهد محاسبه شده و برای هر بند و برای کل تفاهم، شاخصی بین صفر تا ۱۰۰ به‌صورت مستمر به‌روزرسانی می‌شود.
🔹
پژوهشگران این پروژه تأکید کرده‌اند که هدف از طراحی «تفاهم‌سنج»، فراهم‌آوردن بستری برای قضاوت مبتنی‌بر داده به‌جای روایت‌های غیرمستند است. این سامانه که کار خود را به‌صورت آزمایشی آغاز کرده، در دسترس عموم قرار گرفته و مخاطبان می‌توانند با مراجعه به نشانی
Tafahomsanj.com
از آخرین وضعیت شاخص اجرای تفاهم مطلع شوند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449142" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2NiktXL7a1j4SLB9Oz5Tf0R_wr7B77xDbAqScZDQlNL2mFWdQBGla3DwqBUKPX9oAu2H5X4eIEnwXku-6ok7Vr-P5E8RXUGtAx5ikF33BMmKo0dY3uJGZaFIew_ZGIBVAsfjrNsQIOk2FlekSxIyWXz7bkQXq_erwvcRBz9lDaSkrYZzY18i6BO7EbWqsq1SupwtJhvztJuyIGFbkQw8sVr-WZ8cZgOZKZsMYtMBZdA7oclHwoJdfpzYxlPzi3LHDEg5EmKTu6DoUllme2yNeY2O2F5QG131u85i6mCqTOP_huvHuMbCQNMDLpyx9Y19eUBQfqsbP8-Y6C9_x5AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح کاهش قیمت گوشت اجرا می‌شود
🔹
به گفتهٔ وزارت جهاد کشاورزی، حدود ۷۰ درصد هزینه تولید گوشت مربوط به خوراک دام است و وابستگی به علوفهٔ وارداتی باعث افزایش قیمت شده است.
🔹
وزارت جهاد کشاورزی با توسعهٔ تولید علوفه ارزان داخلی در زمین‌های دیم، به‌دنبال کاهش هزینه خوراک دام، افزایش تولید گوشت و کاهش قیمت آن است.
🔹
دولت قصد دارد با توسعهٔ کشت دیم، استفاده از بذرهای مقاوم، کشاورزی حفاظتی و روش‌های نوین، وابستگی به واردات خوراک دام را کاهش دهد.
🔹
برخی کارشناسان نسبت به موفقیت این طرح به‌دلیل کمبود بارندگی در ایران تردید دارند، اما برخی دیگر معتقدند فناوری‌های جدید کشاورزی و اصلاح بذر می‌تواند تولید علوفه در مناطق کم‌بارش را ممکن کند.
@Farsna
-
⁨Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449141" target="_blank">📅 13:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=oXg_DMXNoVdRKOId4mv3wypMOt8irgT3cesP3-vFa09TtpsivudLecqXz3vlZFpsjKLZaNlSBydE5h6YxVg6fBoZbaY-kyt0qBH4wjCHUtVkWky5VkFcFYPec_M2SR_tEFUAOlRLfoOvp3nCpdcFnSTfse0sZa8lUVsQjPaIJuTXU4Rmg0QvBlgq9XyxiXIbpImghhoaNONLYVUonMMTxbugrGXKJbCY94VpdUTiTrXhimW0c8OyrfnjnHDrgNw6lXK9AD6Pm2hD7AgDXw-egxWgvU63j3wRSgRSewi-Ocd8KkZin8c78RZJp5SX87JvcOI9OrqYVsIHsu0YacfFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=oXg_DMXNoVdRKOId4mv3wypMOt8irgT3cesP3-vFa09TtpsivudLecqXz3vlZFpsjKLZaNlSBydE5h6YxVg6fBoZbaY-kyt0qBH4wjCHUtVkWky5VkFcFYPec_M2SR_tEFUAOlRLfoOvp3nCpdcFnSTfse0sZa8lUVsQjPaIJuTXU4Rmg0QvBlgq9XyxiXIbpImghhoaNONLYVUonMMTxbugrGXKJbCY94VpdUTiTrXhimW0c8OyrfnjnHDrgNw6lXK9AD6Pm2hD7AgDXw-egxWgvU63j3wRSgRSewi-Ocd8KkZin8c78RZJp5SX87JvcOI9OrqYVsIHsu0YacfFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت مردان آهنین به تلویزیون با یک سورپرایز
🔹
سری جدید مسابقات مردان آهنین با اجرای آیدین ختایی که از شرکت کنندگان قدیمی این برنامه است و حضور فرامرز خودنگاه، رضا قرایی و محراب فاطمی به زودی از شبکه سه پخش می‌شود
🔹
مردان آهنین هر شب ساعت ۲۰ از شبکه سه پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449140" target="_blank">📅 13:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=mvxljjBY25b3mfJjsJH58TnEV4wdAwvxliEvmXUk_f7fhXDXPjwIshpU2bYkDCQM0xIQ6jmW2kjaHjUmyKk9NhWV3lWsGs2NJWtzKPqmv9TsmR0tiJJpkqzVKSqnblD1GiIEQgQeLVPtJiGwoXQ51I-QsbYJqlWw2eBac_h74a2OZAJ6PBRwYgYsM3l3hRtVCxturcS9wuuEIewpshMCmTQQUxcGX1alVaEV7S9ADTD8BxaBCJ_iuVZrEJh-cKlUYTAsak736y28hLKxvcCK6IWkY9VL3lt7PKK5ojSHOiCAprJPfFBCuGBaIUBbPUjcvMf3fu9fK-KNQO5sXhqyQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=mvxljjBY25b3mfJjsJH58TnEV4wdAwvxliEvmXUk_f7fhXDXPjwIshpU2bYkDCQM0xIQ6jmW2kjaHjUmyKk9NhWV3lWsGs2NJWtzKPqmv9TsmR0tiJJpkqzVKSqnblD1GiIEQgQeLVPtJiGwoXQ51I-QsbYJqlWw2eBac_h74a2OZAJ6PBRwYgYsM3l3hRtVCxturcS9wuuEIewpshMCmTQQUxcGX1alVaEV7S9ADTD8BxaBCJ_iuVZrEJh-cKlUYTAsak736y28hLKxvcCK6IWkY9VL3lt7PKK5ojSHOiCAprJPfFBCuGBaIUBbPUjcvMf3fu9fK-KNQO5sXhqyQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449139" target="_blank">📅 12:59 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
